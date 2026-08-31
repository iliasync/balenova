"""Capture RPC traffic emitted by the official Bale web client."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any
from urllib.parse import urlsplit

from google.protobuf.message import DecodeError

from bale.proto import decode_message, request_pb2
from bale.protocol import ProtocolRecorder

_REQUEST_TYPE_OVERRIDES = {
    ("bale.messaging.v2.Messaging", "PinMessage"): "request.PinMessages",
}
_SERVICE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_.]{2,199}$")
_METHOD_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]{1,99}$")


class OfficialWebCapture:
    """Classify and persist frames observed in the official web application."""

    def __init__(self, recorder: ProtocolRecorder) -> None:
        self.recorder = recorder
        self._pending: dict[int, tuple[str | None, str | None]] = {}

    async def websocket_frame(
        self,
        direction: str,
        payload: bytes | str,
        *,
        url: str,
    ) -> None:
        raw = payload.encode() if isinstance(payload, str) else payload
        if direction == "outbound":
            await self._outbound_websocket(raw, url)
        else:
            await self._inbound_websocket(raw, url)

    async def grpc_frame(
        self,
        direction: str,
        body: bytes,
        *,
        url: str,
    ) -> None:
        service, method = _rpc_from_url(url)
        unframed = _first_grpc_frame(body)
        await self.recorder.record(
            transport="official-web-grpc",
            direction=direction,
            kind=f"official_grpc_{direction}",
            service=service,
            method=method,
            raw=unframed,
            details={
                "url": url,
                "framed_size": len(body),
                "unframed": unframed is not body,
            },
        )

    async def _outbound_websocket(self, raw: bytes, url: str) -> None:
        try:
            envelope = decode_message("request.Request", raw)
        except DecodeError:
            await self._unknown_frame("outbound", raw, url)
            return
        request = envelope.get("ws_request")
        if not isinstance(request, Mapping) or not request.get("service_name"):
            await self._unknown_frame("outbound", raw, url)
            return
        service = str(request.get("service_name"))
        method = str(request.get("method"))
        index = int(request.get("index", 0))
        if (
            not _SERVICE_PATTERN.fullmatch(service)
            or not _METHOD_PATTERN.fullmatch(method)
            or index <= 0
        ):
            await self._unknown_frame("outbound", raw, url)
            return
        nested = bytes(request.get("payload", b""))
        self._pending[index] = (service, method)
        type_name = _request_type(service, method)
        decoded: dict[str, Any] | None = None
        if type_name:
            try:
                decoded = decode_message(type_name, nested)
            except DecodeError:
                type_name = None
        await self.recorder.record(
            transport="official-websocket",
            direction="outbound",
            kind="official_rpc_request",
            type_name=type_name,
            service=service,
            method=method,
            payload=decoded,
            raw=nested,
            details={"url": url, "index": index, "envelope_size": len(raw)},
        )

    async def _inbound_websocket(self, raw: bytes, url: str) -> None:
        try:
            envelope = decode_message("response.Response", raw)
        except DecodeError:
            await self._unknown_frame("inbound", raw, url)
            return
        response = envelope.get("ws_response")
        if isinstance(response, Mapping):
            index = int(response.get("index", 0))
            service, method = self._pending.pop(index, (None, None))
            nested = bytes(response.get("response", b""))
            error = response.get("error")
            await self.recorder.record(
                transport="official-websocket",
                direction="inbound",
                kind="official_rpc_error" if error else "official_rpc_response",
                service=service,
                method=method,
                payload=error if isinstance(error, Mapping) else None,
                raw=nested or None,
                error=(
                    str(error.get("message", "unknown RPC error"))
                    if isinstance(error, Mapping)
                    else None
                ),
                details={"url": url, "index": index, "envelope_size": len(raw)},
            )
            return
        update = envelope.get("ws_update")
        if isinstance(update, Mapping):
            await self.recorder.record(
                transport="official-websocket",
                direction="inbound",
                kind="official_update",
                type_name="response.Response",
                payload=envelope,
                raw=raw,
                details={"url": url},
            )
            return
        await self._unknown_frame("inbound", raw, url)

    async def _unknown_frame(self, direction: str, raw: bytes, url: str) -> None:
        await self.recorder.record(
            transport="official-websocket",
            direction=direction,
            kind="official_unknown_frame",
            raw=raw,
            details={"url": url},
        )


def _request_type(service: str, method: str) -> str | None:
    overridden = _REQUEST_TYPE_OVERRIDES.get((service, method))
    if overridden:
        return overridden
    candidates = (method, method.removesuffix("URL") + "Url")
    for candidate in candidates:
        if hasattr(request_pb2, candidate):
            return f"request.{candidate}"
    return None


def _rpc_from_url(url: str) -> tuple[str | None, str | None]:
    segments = [segment for segment in urlsplit(url).path.split("/") if segment]
    if len(segments) < 2:
        return None, None
    return segments[-2], segments[-1]


def _first_grpc_frame(body: bytes) -> bytes:
    if len(body) < 5 or body[0] not in (0, 1):
        return body
    size = int.from_bytes(body[1:5], "big")
    if 5 + size > len(body):
        return body
    return body[5 : 5 + size]
