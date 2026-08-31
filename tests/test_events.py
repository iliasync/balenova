from __future__ import annotations

import json
from typing import Any

import pytest

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
    async def handler(event: events.NewMessage, _client: Client) -> None:
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


def test_balenova_is_the_public_import() -> None:
    assert Client.__module__ == "bale.client"
    assert events.NewMessage.__name__ == "NewMessage"
