"""Asynchronous gRPC-web transport for Bale RPC calls."""

from __future__ import annotations

import asyncio
import time
from collections.abc import AsyncIterator, Mapping
from typing import Any
from urllib.parse import unquote

import httpx

from bale.errors import BaleRpcError
from bale.proto import decode_message, encode_message
from bale.protocol import ProtocolRecorder

_RETRIABLE_STATUS_CODES = {408, 409, 425, 429}


class GrpcTransport:
    """Send unary protobuf calls over Bale's gRPC-web endpoint."""

    def __init__(
        self,
        *,
        base_url: str = "https://next-ws.bale.ai",
        origin: str = "https://web.bale.ai",
        app_version: str = "113466",
        browser_type: str = "1",
        browser_version: str = "138.0.0.0",
        os_type: str = "3",
        timeout: float = 30.0,
        max_retries: int = 1,
        retry_delay: float = 0.4,
        http_client: httpx.AsyncClient | None = None,
        recorder: ProtocolRecorder | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = max(1.0, timeout)
        self.max_retries = max(0, max_retries)
        self.retry_delay = max(0.0, retry_delay)
        self._owns_client = http_client is None
        self._client = http_client or httpx.AsyncClient()
        self._recorder = recorder
        session_id = str(int(time.time() * 1000))
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 "
            "Safari/537.36"
        )
        self._headers = {
            "content-type": "application/grpc-web+proto",
            "user-agent": user_agent,
            "app_version": app_version,
            "browser_type": browser_type,
            "browser_version": browser_version,
            "os_type": os_type,
            "mt_app_version": app_version,
            "mt_browser_type": browser_type,
            "mt_browser_version": browser_version,
            "mt_os_type": os_type,
            "mt_session_id": session_id,
            "origin": origin,
            "session_id": session_id,
        }

    async def close(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def request(
        self,
        service: str,
        method: str,
        request_type: str,
        response_type: str,
        payload: Mapping[str, Any],
        *,
        access_token: str | None = None,
    ) -> dict[str, Any]:
        encoded = encode_message(request_type, payload)
        raw_response = await self._request_encoded(
            service,
            method,
            encoded,
            access_token=access_token,
            request_type=request_type,
            request_payload=payload,
            response_type=response_type,
        )
        return decode_message(response_type, raw_response)

    async def request_raw(
        self,
        service: str,
        method: str,
        payload: bytes,
        *,
        access_token: str | None = None,
    ) -> bytes:
        """Invoke a unary RPC without requiring generated protobuf classes."""
        return await self._request_encoded(
            service,
            method,
            payload,
            access_token=access_token,
        )

    async def stream_raw(
        self,
        service: str,
        method: str,
        payload: bytes,
        *,
        access_token: str | None = None,
        timeout: float | None = None,
    ) -> AsyncIterator[bytes]:
        """Yield every protobuf message from a server-streaming gRPC-web RPC."""
        body = b"\x00" + len(payload).to_bytes(4, "big") + payload
        headers = dict(self._headers)
        if access_token:
            headers["cookie"] = f"access_token={access_token}"

        if self._recorder:
            await self._recorder.record(
                transport="grpc-web",
                direction="outbound",
                kind="rpc_stream_request",
                service=service,
                method=method,
                raw=payload,
            )

        stream_timeout: float | httpx.Timeout
        if timeout is None:
            stream_timeout = httpx.Timeout(self.timeout, read=None)
        else:
            stream_timeout = timeout
        async with self._client.stream(
            "POST",
            f"{self.base_url}/{service}/{method}",
            content=body,
            headers=headers,
            timeout=stream_timeout,
        ) as response:
            self._raise_for_error(response, service, method)
            buffer = b""
            trailers: dict[str, str] = {}
            async for chunk in response.aiter_bytes():
                buffer += chunk
                while len(buffer) >= 5:
                    frame_length = int.from_bytes(buffer[1:5], "big")
                    frame_end = 5 + frame_length
                    if len(buffer) < frame_end:
                        break
                    flags = buffer[0]
                    frame, buffer = buffer[5:frame_end], buffer[frame_end:]
                    if flags & 0x80:
                        trailers.update(_decode_trailers(frame))
                        continue
                    if self._recorder:
                        await self._recorder.record(
                            transport="grpc-web",
                            direction="inbound",
                            kind="rpc_stream_response",
                            service=service,
                            method=method,
                            raw=frame,
                        )
                    yield frame
            if buffer:
                raise BaleRpcError(
                    -1,
                    "Truncated gRPC-web stream frame",
                    reason=f"{service}/{method}",
                )
            self._raise_for_status(trailers, service, method)

    async def upload(
        self, url: str, payload: bytes, *, chunk_size: int | None = None
    ) -> None:
        """Upload bytes to a Nasim URL returned by Bale."""
        content: bytes | AsyncIterator[bytes] = payload
        if chunk_size is not None:
            if chunk_size <= 0:
                raise ValueError("chunk_size must be positive")

            async def chunks() -> AsyncIterator[bytes]:
                for offset in range(0, len(payload), chunk_size):
                    yield payload[offset : offset + chunk_size]

            content = chunks()
        response = await self._client.put(url, content=content, timeout=self.timeout)
        response.raise_for_status()

    async def download(self, url: str, *, timeout: int | float | None = None) -> bytes:
        """Download bytes from a file URL returned by Bale."""
        response = await self._client.get(
            url,
            timeout=float(timeout) if timeout is not None else self.timeout,
        )
        response.raise_for_status()
        return response.content

    async def _request_encoded(
        self,
        service: str,
        method: str,
        encoded: bytes,
        *,
        access_token: str | None,
        request_type: str | None = None,
        request_payload: Mapping[str, Any] | None = None,
        response_type: str | None = None,
    ) -> bytes:
        body = b"\x00" + len(encoded).to_bytes(4, "big") + encoded
        if self._recorder:
            await self._recorder.record(
                transport="grpc-web",
                direction="outbound",
                kind="rpc_request",
                type_name=request_type,
                service=service,
                method=method,
                payload=request_payload,
                raw=encoded,
            )
        headers = dict(self._headers)
        if access_token:
            headers["cookie"] = f"access_token={access_token}"

        for attempt in range(self.max_retries + 1):
            try:
                response = await self._client.post(
                    f"{self.base_url}/{service}/{method}",
                    content=body,
                    headers=headers,
                    timeout=self.timeout,
                )
                self._raise_for_error(response, service, method)
                raw_response, trailers = _unframe_with_trailers(response.content)
                self._raise_for_status(trailers, service, method)
                decoded = (
                    decode_message(response_type, raw_response)
                    if response_type
                    else None
                )
                if self._recorder:
                    await self._recorder.record(
                        transport="grpc-web",
                        direction="inbound",
                        kind="rpc_response",
                        type_name=response_type,
                        service=service,
                        method=method,
                        payload=decoded,
                        raw=raw_response,
                    )
                return raw_response
            except (httpx.TimeoutException, httpx.NetworkError):
                if attempt >= self.max_retries:
                    raise
            except BaleRpcError as error:
                if self._recorder:
                    await self._recorder.record(
                        transport="grpc-web",
                        direction="inbound",
                        kind="rpc_error",
                        type_name=response_type,
                        service=service,
                        method=method,
                        error=str(error),
                    )
                if attempt >= self.max_retries or not _is_retriable(error.code):
                    raise
            await asyncio.sleep(self.retry_delay * (attempt + 1))

        raise AssertionError("unreachable")

    @staticmethod
    def _raise_for_error(response: httpx.Response, service: str, method: str) -> None:
        GrpcTransport._raise_for_status(response.headers, service, method)
        if not response.is_success:
            raise BaleRpcError(
                response.status_code,
                f"HTTP {response.status_code}",
                reason=f"{service}/{method}",
            )

    @staticmethod
    def _raise_for_status(
        metadata: Mapping[str, str], service: str, method: str
    ) -> None:
        raw_status = metadata.get("grpc-status", "0")
        try:
            grpc_status = int(raw_status)
        except ValueError:
            grpc_status = -1
        message = metadata.get("grpc-message")
        if message or grpc_status != 0:
            raise BaleRpcError(
                grpc_status,
                unquote(message) if message else "Unknown gRPC error",
                reason=f"{service}/{method}",
                details=dict(metadata),
            )


def _is_retriable(status: int) -> bool:
    return status in _RETRIABLE_STATUS_CODES or status >= 500


def _unframe(body: bytes) -> bytes:
    """Extract and join data frames while validating optional trailers."""
    payload, _trailers = _unframe_with_trailers(body)
    return payload


def _unframe_with_trailers(body: bytes) -> tuple[bytes, dict[str, str]]:
    offset = 0
    data_frames: list[bytes] = []
    trailers: dict[str, str] = {}
    while offset < len(body):
        if len(body) - offset < 5:
            raise BaleRpcError(-1, "Truncated gRPC-web frame header")
        flags = body[offset]
        frame_length = int.from_bytes(body[offset + 1 : offset + 5], "big")
        start = offset + 5
        end = start + frame_length
        if end > len(body):
            raise BaleRpcError(-1, "Truncated gRPC-web response")
        frame = body[start:end]
        if flags & 0x80:
            trailers.update(_decode_trailers(frame))
        else:
            data_frames.append(frame)
        offset = end
    return b"".join(data_frames), trailers


def _decode_trailers(frame: bytes) -> dict[str, str]:
    trailers: dict[str, str] = {}
    for line in frame.decode("utf-8", errors="replace").splitlines():
        key, separator, value = line.partition(":")
        if separator:
            trailers[key.strip().lower()] = value.strip()
    return trailers
