from __future__ import annotations

import json
from typing import Any

import pytest

from bale.proto import struct_pb2
from balenova import Client, events, filters


class DummyGrpc:
    async def close(self) -> None:
        pass


def message_update(text: str = "/start") -> dict[str, Any]:
    return {
        "update": {
            "composed_update": {
                "message": {
                    "peer": {"id": 10, "type": 1},
                    "sender_uid": 20,
                    "date": 30,
                    "rid": 40,
                    "message": {"text_message": {"text": text}},
                }
            }
        }
    }


@pytest.mark.asyncio
async def test_class_based_message_event_supports_filters_and_json(tmp_path) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=DummyGrpc())  # type: ignore[arg-type]
    received: list[events.NewMessage] = []

    @client.on(events.NewMessage, filters.command("start"))
    async def handler(event: events.NewMessage) -> None:
        received.append(event)

    raw = message_update()
    await client._process_update(raw)

    assert len(received) == 1
    assert received[0].text == "/start"
    assert received[0].sender_id == 20
    assert received[0].is_private
    assert json.loads(received[0].to_json())["raw"] == raw
    assert await client.next_update(timeout=0.1) is received[0]


@pytest.mark.asyncio
async def test_message_sent_and_unknown_updates_are_always_classed(tmp_path) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=DummyGrpc())  # type: ignore[arg-type]
    received: list[events.Update] = []

    @client.on_update
    async def handler(update: events.Update, _client: Client) -> None:
        received.append(update)

    await client._process_update(
        {"update": {"composed_update": {"message_sent": b"ack", "future": 7}}}
    )

    assert [type(item) for item in received] == [
        events.MessageSent,
        events.RawUpdate,
    ]
    assert json.loads(received[0].to_json())["data"] == "YWNr"
    assert received[1].kind == "future"  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_changed_message_is_delivered_as_message_edited(tmp_path) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=DummyGrpc())  # type: ignore[arg-type]
    edited: list[events.MessageEdited] = []

    @client.on(events.MessageEdited)
    async def handler(event: events.MessageEdited) -> None:
        edited.append(event)

    await client._process_update(message_update("ordinary text"))
    await client._process_update(message_update("!status"))

    assert len(edited) == 1
    assert edited[0].text == "!status"
    assert isinstance(edited[0], events.NewMessage)


@pytest.mark.asyncio
async def test_explicit_web_edit_variant_is_delivered_as_message_edited(
    tmp_path,
) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=DummyGrpc())  # type: ignore[arg-type]
    raw = {
        "update": {
            "composed_update": {
                "message_content_changed": {
                    "peer": {"id": 42, "type": 1},
                    "rid": -100,
                    "date": {"value": 200},
                    "updater_user_id": {"value": 42},
                    "message": {"text_message": {"text": "!panel"}},
                }
            }
        }
    }

    await client._process_update(raw)
    event = await client.next_update(timeout=0.1)

    assert isinstance(event, events.MessageEdited)
    assert event.message.id == "-100|200"
    assert event.text == "!panel"


@pytest.mark.asyncio
async def test_unknown_wire_update_gets_stable_variant_name(tmp_path) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=DummyGrpc())  # type: ignore[arg-type]
    raw = {
        "update": {
            "composed_update": {
                "_unknown_fields": [
                    {"number": 6, "wire_type": 2, "data": b"payload"}
                ]
            }
        }
    }

    await client._process_update(raw)
    event = await client.next_update(timeout=0.1)

    assert isinstance(event, events.RawUpdate)
    assert event.kind == "typing"
    assert event.payload["number"] == 6


@pytest.mark.asyncio
async def test_compact_unknown_update_is_decoded_with_complete_proto(tmp_path) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=DummyGrpc())  # type: ignore[arg-type]
    encoded = struct_pb2.WebTyping(uid=42, typingType=3).SerializeToString()

    await client._process_update(
        {
            "update": {
                "composed_update": {
                    "_unknown_fields": [
                        {"number": 6, "wire_type": 2, "data": encoded}
                    ]
                }
            }
        }
    )
    event = await client.next_update(timeout=0.1)

    assert isinstance(event, events.RawUpdate)
    assert event.kind == "typing"
    assert event.payload["protobuf_type"] == "struct.WebTyping"
    assert event.payload["decoded"] == {"uid": 42, "typingType": 3}


def test_balenova_is_the_public_import() -> None:
    assert Client.__module__ == "bale.client"
    assert events.NewMessage.__name__ == "NewMessage"


def test_every_protocol_update_variant_has_a_stable_public_name() -> None:
    descriptor_fields = struct_pb2.WebUpdate.DESCRIPTOR.fields_by_number

    assert len(descriptor_fields) == 142
    assert {
        number: descriptor.name
        for number, descriptor in descriptor_fields.items()
    } == events._UPDATE_FIELD_NAMES
