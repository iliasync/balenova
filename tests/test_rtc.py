from __future__ import annotations

import base64
import gzip
import json
import sys
from types import ModuleType
from urllib.parse import urlencode

import pytest

from bale import Client
from bale.rtc import (
    CallRtcConnection,
    call_rtc_connection_from_group_call,
    decode_livekit_join_request,
    parse_call_wss_url,
)


def b64url(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).rstrip(b"=").decode("ascii")


def varint(value: int) -> bytes:
    result = bytearray()
    while value > 0x7F:
        result.append((value & 0x7F) | 0x80)
        value >>= 7
    result.append(value)
    return bytes(result)


def bytes_field(number: int, value: bytes) -> bytes:
    return varint(number << 3 | 2) + varint(len(value)) + value


def fake_token() -> str:
    header = b64url(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
    payload = b64url(
        json.dumps(
            {
                "iss": "fake-issuer",
                "sub": "fake-subject",
                "nbf": 1_700_000_000,
                "exp": 4_000_000_000,
                "video": {
                    "canPublish": True,
                    "canPublishData": False,
                    "canSubscribe": True,
                    "room": "fake-room",
                    "roomAdmin": True,
                    "roomJoin": True,
                },
            }
        ).encode()
    )
    return f"{header}.{payload}.fake-signature"


def wrapped_join_request() -> tuple[str, bytes]:
    # JoinRequest fields 1 (ClientInfo) and 2 (ConnectionSettings).
    protobuf = bytes_field(1, b"\x08\x01") + bytes_field(2, b"\x08\x01")
    compressed = gzip.compress(protobuf, mtime=0)
    wrapped = b"\x08\x01" + bytes_field(2, compressed)
    return b64url(wrapped), protobuf


def test_parse_browser_call_url_decodes_safe_rtc_metadata() -> None:
    encoded_join, protobuf = wrapped_join_request()
    token = fake_token()
    query = urlencode(
        {
            "region": "test",
            "access_token": token,
            "join_request": encoded_join,
        }
    )

    connection = parse_call_wss_url(
        f"wss://meet.example.test/instance/rtc/v1?{query}"
    )

    assert connection.server_url == (
        "wss://meet.example.test/instance/rtc/v1?region=test"
    )
    assert connection.access_token == token
    assert connection.permissions.can_publish is True
    assert connection.permissions.can_publish_data is False
    assert connection.permissions.can_subscribe is True
    assert connection.permissions.room_admin is True
    assert connection.permissions.room_join is True
    assert connection.not_before == 1_700_000_000
    assert connection.expires_at == 4_000_000_000
    assert connection.expired is False
    assert connection.join_request is not None
    assert connection.join_request.compression == "gzip"
    assert connection.join_request.protobuf == protobuf
    assert connection.join_request.field_numbers == (1, 2)
    rendered = repr(connection)
    assert token not in rendered
    assert "fake-issuer" not in rendered
    assert "fake-subject" not in rendered
    assert "fake-room" not in rendered


def test_decode_uncompressed_wrapped_join_request() -> None:
    protobuf = bytes_field(7, b"payload")
    wrapped = b"\x08\x00" + bytes_field(2, protobuf)

    decoded = decode_livekit_join_request(b64url(wrapped))

    assert decoded.compression == "none"
    assert decoded.protobuf == protobuf
    assert decoded.field_numbers == (7,)


@pytest.mark.parametrize(
    "value, message",
    [
        ("not base64!", "base64url"),
        (b64url(b"\x08\x02\x12\x00"), "unsupported"),
        (b64url(b"\x08\x01\x12\x03bad"), "gzip"),
    ],
)
def test_decode_join_request_rejects_invalid_envelopes(
    value: str, message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        decode_livekit_join_request(value)


def test_group_call_credentials_support_bale_url_wrapper() -> None:
    connection = call_rtc_connection_from_group_call(
        {
            "token": fake_token(),
            "url": {"text": "wss://meet.example.test/instance"},
        }
    )

    assert connection.server_url == "wss://meet.example.test/instance"
    assert connection.permissions.can_subscribe is True


@pytest.mark.asyncio
async def test_connection_uses_official_livekit_room(monkeypatch) -> None:
    calls: list[tuple[str, str, object | None]] = []

    class FakeRoom:
        async def connect(
            self, url: str, token: str, options: object | None = None
        ) -> None:
            calls.append((url, token, options))

    livekit = ModuleType("livekit")
    rtc = ModuleType("livekit.rtc")
    rtc.Room = FakeRoom  # type: ignore[attr-defined]
    livekit.rtc = rtc  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "livekit", livekit)
    monkeypatch.setitem(sys.modules, "livekit.rtc", rtc)
    connection = CallRtcConnection(
        "wss://meet.example.test/instance", fake_token()
    )
    options = object()

    room = await connection.connect(options)

    assert isinstance(room, FakeRoom)
    assert calls == [
        ("wss://meet.example.test/instance", connection.access_token, options)
    ]


@pytest.mark.asyncio
async def test_client_join_group_call_rtc_uses_wss_fallback(monkeypatch) -> None:
    client = Client("42:account-token")

    async def join_group_call(call_id: int | str, name: str | None = None) -> dict:
        assert (call_id, name) == (789, "Player")
        return {"group_call": {"id": 789, "token": fake_token()}}

    async def get_call_wss_url(call_id: int | str) -> str:
        assert call_id == 789
        return "wss://meet.example.test/instance"

    monkeypatch.setattr(client, "join_group_call", join_group_call)
    monkeypatch.setattr(client, "get_call_wss_url", get_call_wss_url)

    connection = await client.join_group_call_rtc(789, "Player")

    assert connection.server_url == "wss://meet.example.test/instance"
    assert connection.permissions.can_publish is True
