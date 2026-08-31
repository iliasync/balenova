from __future__ import annotations

import httpx
import pytest

from bale.errors import BaleRpcError, RpcStatus
from bale.proto import decode_message, encode_message
from bale.transports.grpc import GrpcTransport


def grpc_frame(payload: bytes) -> bytes:
    return b"\x00" + len(payload).to_bytes(4, "big") + payload


def grpc_trailer(**values: str) -> bytes:
    payload = "\r\n".join(f"{key}: {value}" for key, value in values.items()).encode()
    return b"\x80" + len(payload).to_bytes(4, "big") + payload


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
    assert captured.value.status is RpcStatus.INVALID_ARGUMENT
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


@pytest.mark.asyncio
async def test_grpc_yields_every_server_stream_message() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        assert await request.aread() == grpc_frame(b"request")
        assert request.extensions["timeout"]["read"] is None
        return httpx.Response(
            200,
            content=(
                grpc_frame(b"first")
                + grpc_frame(b"second")
                + grpc_trailer(**{"grpc-status": "0"})
            ),
        )

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    transport = GrpcTransport(http_client=http, max_retries=0)

    messages = [
        item
        async for item in transport.stream_raw(
            "service", "stream", b"request", access_token="jwt"
        )
    ]

    assert messages == [b"first", b"second"]
    await http.aclose()


@pytest.mark.asyncio
async def test_grpc_surfaces_percent_decoded_trailer_error_and_retry_after() -> None:
    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            content=grpc_trailer(
                **{
                    "grpc-status": "8",
                    "grpc-message": "user_rate_limited%20retry_after%203",
                }
            ),
        )

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    transport = GrpcTransport(http_client=http, max_retries=0)

    with pytest.raises(BaleRpcError) as captured:
        await transport.request_raw("service", "method", b"")

    error = captured.value
    assert error.status is RpcStatus.RESOURCE_EXHAUSTED
    assert error.is_rate_limited
    assert error.retry_after == 3
    assert error.to_dict()["message"] == "user_rate_limited retry_after 3"
    assert error.details["grpc-status"] == "8"
    await http.aclose()
