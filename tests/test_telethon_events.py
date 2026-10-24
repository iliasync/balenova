"""Tests for Telethon-style events, dot-access navigation, and representations."""

from __future__ import annotations

from typing import Any

import pytest

from bale.types import (
    Chat,
    Message,
    MessageButton,
    User,
)
from balenova import Client, events


class DummyGrpc:
    async def close(self) -> None:
        pass


def make_message_update(
    text: str = "/start hello", chat_id: int = 10, sender_id: int = 20, rid: int = 40
) -> dict[str, Any]:
    return {
        "update": {
            "composed_update": {
                "message": {
                    "peer": {"id": chat_id, "type": 1},
                    "sender_uid": sender_id,
                    "date": 100,
                    "rid": rid,
                    "message": {"text_message": {"text": text}},
                }
            }
        }
    }


def test_string_and_repr_representations() -> None:
    user = User(id=123, username="test_user", name="Ali Reza", is_bot=False)
    user_repr = repr(user)
    assert user_repr.startswith("User(")
    assert "id=123" in user_repr
    assert "username='test_user'" in user_repr
    assert "name='Ali Reza'" in user_repr
    assert str(user) == user_repr

    chat = Chat(peer_id=456, peer_type=2, title="Developers Group")
    chat_repr = repr(chat)
    assert chat_repr.startswith("Chat(")
    assert "id='456|2'" in chat_repr
    assert "title='Developers Group'" in chat_repr
    assert str(chat) == chat_repr

    btn = MessageButton(text="Confirm", data="action_confirm", row=0, col=1)
    btn_repr = repr(btn)
    assert "text='Confirm'" in btn_repr
    assert "data='action_confirm'" in btn_repr
    assert "pos=(0, 1)" in btn_repr

    msg = Message(
        rid=999,
        date=1234567,
        author=user,
        chat=chat,
        text="Hello world!",
    )
    msg_repr = repr(msg)
    assert "Message(" in msg_repr
    assert "text='Hello world!'" in msg_repr
    assert "id='999|1234567'" in msg_repr
    assert str(msg) == msg_repr


def test_dot_access_and_shortcuts() -> None:
    user = User(id=77, username="coder", name="John Doe")
    chat = Chat(peer_id=88, peer_type=1, title="Private Chat")
    msg = Message(
        rid=500,
        date=200,
        author=user,
        chat=chat,
        text="/echo testing 1 2 3",
    )

    # Dot-access
    assert msg.text == "/echo testing 1 2 3"
    assert msg.content == "/echo testing 1 2 3"
    assert msg.from_user.id == 77
    assert msg.from_user.first_name == "John"
    assert msg.from_user.last_name == "Doe"
    assert msg.from_user.username == "coder"
    assert msg.chat.id == "88|1"
    assert msg.chat.is_private is True
    assert msg.chat.is_group is False

    # Command helpers
    assert msg.command == "echo"
    assert msg.command_args == "testing 1 2 3"


@pytest.mark.asyncio
async def test_telethon_style_event_filtering(tmp_path) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=DummyGrpc())  # type: ignore[arg-type]
    received: list[events.NewMessage] = []

    # Telethon style: @client.on(events.NewMessage(pattern=..., incoming=...))
    @client.on(events.NewMessage(pattern=r"^/greet\s+(\w+)", incoming=True))
    async def handler(event: events.NewMessage) -> None:
        received.append(event)

    # Non-matching message
    await client._process_update(make_message_update("/help"))
    assert len(received) == 0

    # Matching message
    await client._process_update(make_message_update("/greet Mahdi"))
    assert len(received) == 1
    assert received[0].text == "/greet Mahdi"
    assert received[0].pattern_match is not None
    assert received[0].pattern_match.group(1) == "Mahdi"
    assert received[0].sender_id == 20
    assert received[0].from_user.id == 20
