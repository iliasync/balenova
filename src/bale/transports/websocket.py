"""Multiplexed asynchronous WebSocket RPC transport."""

from __future__ import annotations

import asyncio
import time
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from typing import Any

from websockets.asyncio.client import ClientConnection, connect
from websockets.typing import Origin

from bale.errors import BaleRpcError, ClientStateError
from bale.proto import decode_message, encode_message
from bale.protocol import ProtocolRecorder

UpdateCallback = Callable[[dict[str, Any]], Awaitable[None] | None]


@dataclass(slots=True)
class _PendingRequest:
    future: asyncio.Future[dict[str, Any]]
    response_type: str | None
    service: str
    method: str


class WebSocketTransport:
    """Maintain Bale's WebSocket and multiplex RPC responses by index."""

    _last_rid = time.time_ns() // 1_000

    def __init__(
        self,
        access_token: str,
        *,
        uri: str = "wss://next-ws.bale.ai/ws/",
        origin: str = "https://web.bale.ai",
        timeout: float = 20.0,
        app_version: int = 86550,
        browser_type: str = "1",
        browser_version: int = 3471765337684194354,
        os_type: str = "3",
        keepalive_interval: float = 15.0,
        recorder: ProtocolRecorder | None = None,
    ) -> None:
        self.access_token = access_token
        self.uri = uri
        self.origin = origin
        self.timeout = max(1.0, timeout)
        self.keepalive_interval = max(1.0, keepalive_interval)
        self._app_version = app_version
        self._browser_type = browser_type
        self._browser_version = browser_version
        self._os_type = os_type
        self._socket: ClientConnection | None = None
        self._reader_task: asyncio.Task[None] | None = None
        self._keepalive_task: asyncio.Task[None] | None = None
        self._pending: dict[int, _PendingRequest] = {}
        self._next_index = 1
        self._send_lock = asyncio.Lock()
        self._callbacks: list[UpdateCallback] = []
        self.updates: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
        self._metadata: dict[str, Any] = {}
        self._recorder = recorder

    @property
    def connected(self) -> bool:
        return self._socket is not None

    @classmethod
    def create_rid(cls) -> int:
        now = time.time_ns() // 1_000
        cls._last_rid = max(cls._last_rid + 1, now)
        return cls._last_rid

    def add_update_handler(self, callback: UpdateCallback) -> None:
        self._callbacks.append(callback)

    async def connect(self) -> None:
        if self._socket is not None:
            return
        session_id = str(int(time.time() * 1000))
        self._metadata = {
            "key_values": [
                _metadata("app_version", str(self._app_version)),
                _metadata("browser_type", self._browser_type),
                _metadata_fixed64("browser_version", self._browser_version),
                _metadata("os_type", self._os_type),
                _metadata("session_id", session_id),
            ]
        }
        self._socket = await connect(
            self.uri,
            origin=Origin(self.origin),
            additional_headers={"Cookie": f"access_token={self.access_token}"},
            compression=None,
        )
        self._reader_task = asyncio.create_task(self._reader(), name="bale-ws-reader")
        await self.keepalive()
        self._keepalive_task = asyncio.create_task(
            self._keepalive_loop(), name="bale-ws-keepalive"
        )

    async def close(self) -> None:
        socket, self._socket = self._socket, None
        tasks = [
            task
            for task in (self._keepalive_task, self._reader_task)
            if task is not None and task is not asyncio.current_task()
        ]
        for task in tasks:
            if task is not None:
                task.cancel()
        self._keepalive_task = None
        self._reader_task = None
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        if socket is not None:
            await socket.close()
        self._fail_pending(ClientStateError("Bale WebSocket closed"))

    async def keepalive(self) -> None:
        await self.send_raw(
            "request.KeepAliveRequest", {"payloads": {"value_should_2": 2}}
        )

    async def send_raw(self, type_name: str, payload: Mapping[str, Any]) -> None:
        socket = self._socket
        if socket is None:
            raise ClientStateError("Bale WebSocket is not connected")
        encoded = encode_message(type_name, payload)
        if self._recorder and type_name != "request.Request":
            await self._recorder.record(
                transport="websocket",
                direction="outbound",
                kind="protobuf",
                type_name=type_name,
                payload=payload,
                raw=encoded,
            )
        async with self._send_lock:
            await socket.send(encoded)

    async def request(
        self,
        service: str,
        method: str,
        request_type: str,
        payload: Mapping[str, Any],
        response_type: str | None,
    ) -> dict[str, Any]:
        index = self._next_index
        self._next_index += 1
        future = asyncio.get_running_loop().create_future()
        self._pending[index] = _PendingRequest(future, response_type, service, method)
        encoded_payload = encode_message(request_type, payload)
        envelope = {
            "ws_request": {
                "service_name": service,
                "method": method,
                "payload": encoded_payload,
                "metadata": self._metadata,
                "index": index,
            }
        }
        try:
            if self._recorder:
                await self._recorder.record(
                    transport="websocket",
                    direction="outbound",
                    kind="rpc_request",
                    type_name=request_type,
                    service=service,
                    method=method,
                    payload=payload,
                    raw=encoded_payload,
                )
            await self.send_raw("request.Request", envelope)
            return await asyncio.wait_for(future, timeout=self.timeout)
        except TimeoutError as error:
            raise ClientStateError(
                f"Timed out waiting for Bale response {index}"
            ) from error
        finally:
            self._pending.pop(index, None)

    async def _reader(self) -> None:
        socket = self._socket
        if socket is None:
            return
        try:
            async for incoming in socket:
                if isinstance(incoming, str):
                    continue
                await self._handle_incoming(bytes(incoming))
        except asyncio.CancelledError:
            raise
        except Exception as error:
            self._fail_pending(error)
        finally:
            if self._socket is socket:
                self._socket = None
                if self._keepalive_task is not None:
                    self._keepalive_task.cancel()

    async def _handle_incoming(self, payload: bytes) -> None:
        response = decode_message("response.Response", payload)
        update = response.get("ws_update")
        if isinstance(update, dict):
            if self._recorder:
                await self._recorder.record(
                    transport="websocket",
                    direction="inbound",
                    kind="update",
                    type_name="response.Response",
                    payload=response,
                    raw=payload,
                )
            await self.updates.put(update)
            for callback in self._callbacks:
                callback_result = callback(update)
                if isinstance(callback_result, Awaitable):
                    await callback_result
            return
        ws_response = response.get("ws_response")
        if not isinstance(ws_response, dict):
            return
        pending = self._pending.get(int(ws_response.get("index", 0)))
        if pending is None or pending.future.done():
            return
        error = ws_response.get("error")
        if isinstance(error, dict):
            if self._recorder:
                await self._recorder.record(
                    transport="websocket",
                    direction="inbound",
                    kind="rpc_error",
                    type_name=pending.response_type,
                    service=pending.service,
                    method=pending.method,
                    payload=error,
                    error=str(error.get("message", "Unknown WebSocket RPC error")),
                )
            pending.future.set_exception(
                BaleRpcError(
                    int(error.get("code", -1)),
                    str(error.get("message", "Unknown WebSocket RPC error")),
                )
            )
            return
        raw_response = ws_response.get("response", b"")
        if pending.response_type:
            decoded_result = decode_message(pending.response_type, bytes(raw_response))
        else:
            decoded_result = {"raw": bytes(raw_response)}
        if self._recorder:
            await self._recorder.record(
                transport="websocket",
                direction="inbound",
                kind="rpc_response",
                type_name=pending.response_type,
                service=pending.service,
                method=pending.method,
                payload=decoded_result,
                raw=bytes(raw_response),
            )
        pending.future.set_result(decoded_result)

    async def _keepalive_loop(self) -> None:
        try:
            while True:
                await asyncio.sleep(self.keepalive_interval)
                await self.keepalive()
        except asyncio.CancelledError:
            raise

    def _fail_pending(self, error: BaseException) -> None:
        for pending in self._pending.values():
            if not pending.future.done():
                pending.future.set_exception(error)
        self._pending.clear()


def _metadata(key: str, value: str) -> dict[str, Any]:
    return {"key": key, "value": {"string_value": value}}


def _metadata_fixed64(key: str, value: int) -> dict[str, Any]:
    return {"key": key, "value": {"msg_value": {"fixed64_value": value}}}
