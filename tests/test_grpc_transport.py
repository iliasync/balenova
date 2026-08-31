from __future__ import annotations

import httpx
import pytest

from bale.errors import BaleRpcError
from bale.proto import decode_message, encode_message
from bale.transports.grpc import GrpcTransport


def grpc_frame(payload: bytes) -> bytes:
    return b"\x00" + len(payload).to_bytes(4, "big") + payload


@pytest.mark.asyncio
async def test_grpc_request_frames_payload_and_sends_session_cookie() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        body = await request.aread()
        size = int.from_bytes(body[1:5], "big")
        decoded = decode_message("request.EditName", body[5 : 5 + size])
        assert decoded == {"name": "Mahan"}
        assert request.headers["cookie"] == "access_token=jwt-token"
        response = encode_message("response.DefaultResponse", {"seq": 7, "date": 42})
        return httpx.Response(200, content=grpc_frame(response))

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    transport = GrpcTransport(http_client=http, max_retries=0)

    result = await transport.request(
        "bale.users.v1.Users",
        "EditName",
        "request.EditName",
        "response.DefaultResponse",
        {"name": "Mahan"},
        access_token="jwt-token",
    )

    assert result == {"seq": 7, "date": 42}
    await http.aclose()


@pytest.mark.asyncio
async def test_grpc_retries_transient_rpc_error() -> None:
    attempts = 0

    def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                503,
                headers={"grpc-status": "503", "grpc-message": "unavailable"},
            )
        encoded = encode_message("response.DefaultResponse", {"seq": 1})
        return httpx.Response(200, content=grpc_frame(encoded))

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    transport = GrpcTransport(http_client=http, max_retries=1, retry_delay=0)

    assert (
        await transport.request(
            "service", "method", "request.SignOut", "response.DefaultResponse", {}
        )
    )["seq"] == 1
    assert attempts == 2
    await http.aclose()


@pytest.mark.asyncio
async def test_grpc_surfaces_non_retriable_error() -> None:
    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            400, headers={"grpc-status": "3", "grpc-message": "INVALID"}
        )

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    transport = GrpcTransport(http_client=http, max_retries=2)

    with pytest.raises(BaleRpcError) as captured:
        await transport.request(
            "service", "method", "request.SignOut", "response.DefaultResponse", {}
        )

    assert captured.value.code == 3
    assert captured.value.reason == "service/method"
    await http.aclose()


@pytest.mark.asyncio
async def test_grpc_supports_untyped_rpc_payloads() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        body = await request.aread()
        assert body == grpc_frame(b"\x08\x01")
        return httpx.Response(200, content=grpc_frame(b"\x12\x03raw"))

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    transport = GrpcTransport(http_client=http, max_retries=0)

    result = await transport.request_raw(
        "bale.new.v1.New", "NewMethod", b"\x08\x01", access_token="jwt"
    )

    assert result == b"\x12\x03raw"
    await http.aclose()
