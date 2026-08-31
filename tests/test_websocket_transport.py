from __future__ import annotations

import asyncio

import pytest

from bale.proto import decode_message, encode_message
from bale.protocol import ProtocolRecorder
from bale.transports.websocket import WebSocketTransport


class FakeSocket:
    def __init__(self) -> None:
        self.sent: list[bytes] = []
        self.closed = False
        self.sent_event = asyncio.Event()

    async def send(self, payload: bytes) -> None:
        self.sent.append(payload)
        self.sent_event.set()

    async def close(self) -> None:
        self.closed = True


@pytest.mark.asyncio
async def test_websocket_multiplexes_rpc_response_by_index() -> None:
    transport = WebSocketTransport("jwt")
    socket = FakeSocket()
    transport._socket = socket  # type: ignore[assignment]

    request_task = asyncio.create_task(
        transport.request(
            "bale.users.v1.Users",
            "EditName",
            "request.EditName",
            {"name": "Mahan"},
            "response.DefaultResponse",
        )
    )
    await asyncio.wait_for(socket.sent_event.wait(), timeout=1)

    envelope = decode_message("request.Request", socket.sent[0])
    index = envelope["ws_request"]["index"]
    nested_request = decode_message(
        "request.EditName", envelope["ws_request"]["payload"]
    )
    assert nested_request == {"name": "Mahan"}

    nested_response = encode_message("response.DefaultResponse", {"seq": 8, "date": 9})
    incoming = encode_message(
        "response.Response",
        {"ws_response": {"index": index, "response": nested_response}},
    )
    await transport._handle_incoming(incoming)

    assert await request_task == {"seq": 8, "date": 9}
    await transport.close()
    assert socket.closed


@pytest.mark.asyncio
async def test_websocket_supports_untyped_rpc_payloads() -> None:
    transport = WebSocketTransport("jwt")
    socket = FakeSocket()
    transport._socket = socket  # type: ignore[assignment]

    request_task = asyncio.create_task(
        transport.request_raw("bale.new.v1.New", "NewMethod", b"\x08\x01")
    )
    await asyncio.wait_for(socket.sent_event.wait(), timeout=1)
    envelope = decode_message("request.Request", socket.sent[0])["ws_request"]
    assert envelope["payload"] == b"\x08\x01"

    await transport._handle_incoming(
        encode_message(
            "response.Response",
            {
                "ws_response": {
                    "index": envelope["index"],
                    "response": b"\x08\x07",
                }
            },
        )
    )

    assert await request_task == b"\x08\x07"
    await transport.close()


@pytest.mark.asyncio
async def test_websocket_publishes_updates_to_queue_and_callback() -> None:
    transport = WebSocketTransport("jwt")
    received = []
    transport.add_update_handler(received.append)
    incoming = encode_message(
        "response.Response",
        {
            "ws_update": {
                "update": {
                    "composed_update": {
                        "message": {
                            "peer": {"id": 2, "type": 1},
                            "sender_uid": 3,
                            "date": 4,
                            "rid": 5,
                            "message": {"text_message": {"text": "hello"}},
                        }
                    }
                }
            }
        },
    )

    await transport._handle_incoming(incoming)

    queued = await transport.updates.get()
    assert queued == received[0]
    assert queued["update"]["composed_update"]["message"]["rid"] == 5


@pytest.mark.asyncio
async def test_websocket_never_saves_raw_auth_envelopes(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)
    transport = WebSocketTransport("jwt", recorder=recorder)
    socket = FakeSocket()
    transport._socket = socket  # type: ignore[assignment]

    request_task = asyncio.create_task(
        transport.request(
            "bale.auth.v1.Auth",
            "ValidateCode",
            "request.ValidateCode",
            {
                "transaction_hash": "transaction",
                "code": "12345",
                "is_jwt": {"value": True},
            },
            "response.Auth",
        )
    )
    await asyncio.wait_for(socket.sent_event.wait(), timeout=1)
    envelope = decode_message("request.Request", socket.sent[0])
    response = encode_message(
        "response.Auth", {"user": {"id": 1}, "jwt": {"value": "secret-jwt"}}
    )
    await transport._handle_incoming(
        encode_message(
            "response.Response",
            {
                "ws_response": {
                    "index": envelope["ws_request"]["index"],
                    "response": response,
                }
            },
        )
    )
    assert (await request_task)["jwt"]["value"] == "secret-jwt"

    assert list((recorder.path / "frames").iterdir()) == []
    await transport.close()
