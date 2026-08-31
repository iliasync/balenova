"""Asynchronous gRPC-web transport for Bale RPC calls."""

from __future__ import annotations

import asyncio
import time
from collections.abc import AsyncIterator, Mapping
from typing import Any

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
                raw_response = _unframe(response.content)
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
        raw_status = response.headers.get("grpc-status", "0")
        try:
            grpc_status = int(raw_status)
        except ValueError:
            grpc_status = -1
        message = response.headers.get("grpc-message")
        if message or grpc_status != 0:
            raise BaleRpcError(
                grpc_status,
                message or f"HTTP {response.status_code}",
                reason=f"{service}/{method}",
            )
        if not response.is_success:
            raise BaleRpcError(
                response.status_code,
                f"HTTP {response.status_code}",
                reason=f"{service}/{method}",
            )


def _is_retriable(status: int) -> bool:
    return status in _RETRIABLE_STATUS_CODES or status >= 500


def _unframe(body: bytes) -> bytes:
    """Extract the first data frame and ignore optional gRPC trailers."""
    if len(body) < 5:
        return b""
    frame_length = int.from_bytes(body[1:5], "big")
    frame_end = 5 + frame_length
    if frame_end > len(body):
        raise BaleRpcError(-1, "Truncated gRPC-web response")
    return body[5:frame_end]
