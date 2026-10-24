"""Friendly class-based updates and Telethon-style events for Bale."""

from __future__ import annotations

import json
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, cast

from google.protobuf.message_factory import GetMessageClass

from bale.filters import Filter, compile_filters
from bale.models import (
    Chat,
    ChatType,
    Message,
    Serializable,
    User,
    model_to_dict,
)
from bale.proto import struct_pb2

if TYPE_CHECKING:
    from bale.client import Client


class Event:
    """Base event container holding an optional compiled Filter for Telethon syntax."""

    target_update_type: type[Update] = cast(type["Update"], None)

    def __init__(self, filter: Filter | None = None) -> None:
        self.filter = filter


@dataclass(slots=True)
class Update(Serializable):
    """Base class for every update received by the client."""

    raw: dict[str, Any]
    _client: Client | None = field(default=None, init=False, repr=False, compare=False)

    @property
    def name(self) -> str:
        return type(self).__name__

    def bind(self, client: Client) -> Update:
        self._client = client
        return self

    def to_dict(self, *, include_raw: bool = True) -> dict[str, Any]:
        return Serializable.to_dict(self, include_raw=include_raw)

    def to_json(self, *, include_raw: bool = True, indent: int | None = 2) -> str:
        return json.dumps(
            self.to_dict(include_raw=include_raw),
            ensure_ascii=False,
            indent=indent,
            sort_keys=True,
        )


@dataclass(slots=True)
class NewMessage(Update, Event):
    """A newly received or sent message, or an event builder for message handlers."""

    message: Message = field(default_factory=lambda: cast(Message, None))
    filter: Filter | None = field(default=None, repr=False, compare=False)

    def __init__(
        self,
        raw: dict[str, Any] | None = None,
        message: Message | None = None,
        *,
        incoming: bool | None = None,
        outgoing: bool | None = None,
        outcoming: bool | None = None,
        chats: int | str | Iterable[int | str] | None = None,
        users: int | str | Iterable[int | str] | None = None,
        commands: str | Iterable[str] | None = None,
        pattern: str | re.Pattern[str] | None = None,
        func: Any = None,
        filter: Filter | None = None,
        **kwargs: Any,
    ) -> None:
        if raw is not None and isinstance(raw, dict) and message is not None:
            self.raw = raw
            self.message = message
            self.filter = None
            self._client = None
        else:
            self.raw = raw or {}
            self.message = cast(Message, None)
            self._client = None
            self.filter = filter or compile_filters(
                func,
                incoming_flag=incoming,
                outgoing_flag=outgoing,
                outcoming_flag=outcoming,
                chats_filter=chats,
                users_filter=users,
                commands_filter=commands,
                regex_pattern=pattern,
                **kwargs,
            )

    target_update_type = cast(type[Update], None)

    def bind(self, client: Client) -> NewMessage:
        self._client = client
        if self.message:
            self.message.bind(client)
        return self

    @property
    def id(self) -> str:
        return self.message.id if self.message else ""

    @property
    def text(self) -> str:
        return self.message.content if self.message else ""

    @property
    def content(self) -> str:
        return self.message.content if self.message else ""

    @property
    def chat(self) -> Chat:
        return self.message.chat

    @property
    def chat_id(self) -> str:
        return self.message.chat.id if self.message else ""

    @property
    def from_user(self) -> User:
        return self.message.author

    @property
    def sender(self) -> User:
        return self.message.author

    @property
    def sender_id(self) -> int:
        return self.message.sender_id if self.message else 0

    @property
    def pattern_match(self) -> Any:
        return self.message.matches if self.message else None

    @property
    def is_private(self) -> bool:
        return self.chat.type is ChatType.PRIVATE if self.message else False

    @property
    def is_group(self) -> bool:
        if not self.message:
            return False
        return self.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP}

    @property
    def is_channel(self) -> bool:
        return self.chat.type is ChatType.CHANNEL if self.message else False

    @property
    def is_outgoing(self) -> bool:
        return self.message.is_outgoing if self.message else False

    @property
    def is_incoming(self) -> bool:
        return self.message.is_incoming if self.message else False

    async def answer(self, text: str, *, reply_markup: Any = None) -> Message:
        return await self.message.answer(text, reply_markup=reply_markup)

    respond = answer

    async def reply(self, text: str, *, reply_markup: Any = None) -> Message:
        return await self.message.reply(text, reply_markup=reply_markup)

    async def reply_photo(
        self, photo: Any, caption: str = "", **kwargs: Any
    ) -> Message:
        return await self.message.reply_photo(photo, caption=caption, **kwargs)

    async def reply_document(
        self, document: Any, caption: str = "", **kwargs: Any
    ) -> Message:
        return await self.message.reply_document(document, caption=caption, **kwargs)

    async def edit(self, text: str) -> Any:
        return await self.message.edit_text(text)

    async def delete(self, just_me: bool = False) -> Any:
        return await self.message.delete(just_me)

    async def react(self, code: str = "👍") -> Any:
        return await self.message.react(code)

    async def forward(self, chat_id: Any) -> Any:
        return await self.message.forward(chat_id)

    async def copy(self, chat_id: Any) -> Any:
        return await self.message.copy(chat_id)

    def get_fsm_context(self) -> Any:
        return self.message.get_fsm_context()

    def __repr__(self) -> str:
        if self.message:
            return f"NewMessage(message={self.message!r})"
        return f"NewMessage(filter={self.filter!r})"

    def __str__(self) -> str:
        return repr(self)


NewMessage.target_update_type = NewMessage


@dataclass(slots=True)
class MessageEdited(NewMessage):
    """A message whose content changed while the client was running."""


MessageEdited.target_update_type = MessageEdited


@dataclass(slots=True)
class MessageSent(Update):
    """Confirmation data for a message sent by the current account."""

    data: Any


@dataclass(slots=True)
class RawUpdate(Update):
    """A decoded update that does not yet have a dedicated convenience class."""

    kind: str
    payload: Any


class MessageDeleted(Event):
    """Event builder triggered when messages are deleted."""

    target_update_type = Update


class ChatAction(Event):
    """Event builder triggered on chat member changes (join, leave, kick)."""

    target_update_type = Update


class CallbackQuery(Event):
    """Event builder triggered when an inline keyboard callback button is clicked."""

    target_update_type = Update


class UserTyping(Event):
    """Event builder triggered when a user is typing."""

    target_update_type = Update


class UserUpdate(Event):
    """Event builder triggered when user profile or status changes."""

    target_update_type = Update


class MessageRead(Event):
    """Event builder triggered when messages are read."""

    target_update_type = Update


class Reaction(Event):
    """Event builder triggered on message reactions."""

    target_update_type = Update


class JoinRequest(Event):
    """Event builder triggered when a user requests to join."""

    target_update_type = Update


class Raw(Event):
    """Event builder triggered on all raw updates."""

    target_update_type = Update


_WEB_UPDATE_DESCRIPTOR = cast(Any, struct_pb2).WebUpdate.DESCRIPTOR
_UPDATE_FIELD_NAMES = {
    number: descriptor.name
    for number, descriptor in _WEB_UPDATE_DESCRIPTOR.fields_by_number.items()
}


def _snake_case(value: str) -> str:
    return "".join(
        ("_" + char.lower()) if char.isupper() else char for char in value
    ).lstrip("_")


def _edited_message_payload(payload: dict[str, Any]) -> dict[str, Any]:
    date = payload.get("date", 0)
    if isinstance(date, dict):
        date = date.get("value", 0)
    updater = payload.get("updater_user_id", 0)
    if isinstance(updater, dict):
        updater = updater.get("value", 0)
    return {
        "peer": payload.get("peer", {}),
        "sender_uid": updater,
        "date": date,
        "rid": payload.get("rid", 0),
        "message": payload.get("message", {}),
        "quoted_message": payload.get("quoted_message", {}),
    }


def _decode_complete_update_field(field: dict[str, Any]) -> dict[str, Any]:
    number = int(field.get("number", 0))
    data = field.get("data")
    update_type = cast(Any, struct_pb2).WebUpdate
    descriptor = update_type.DESCRIPTOR.fields_by_number.get(number)
    if (
        descriptor is None
        or descriptor.message_type is None
        or not isinstance(data, bytes | bytearray | memoryview)
    ):
        return field
    try:
        message_type = GetMessageClass(descriptor.message_type)
        message = message_type.FromString(bytes(data))
    except Exception:
        return field
    return {
        **field,
        "protobuf_type": descriptor.message_type.full_name,
        "decoded": model_to_dict(message, include_raw=True),
    }


def build_updates(
    raw: dict[str, Any],
    message_factory: Callable[[dict[str, Any]], Message],
) -> list[Update]:
    """Turn every decoded item in an update envelope into a public class."""
    update = raw.get("update")
    composed = update.get("composed_update") if isinstance(update, dict) else None
    if not isinstance(composed, dict) or not composed:
        return [RawUpdate(raw, "unknown", model_to_dict(raw, include_raw=True))]

    result: list[Update] = []
    for kind, payload in composed.items():
        if kind == "message" and isinstance(payload, dict):
            result.append(NewMessage(raw, message_factory(payload)))
        elif kind == "message_content_changed" and isinstance(payload, dict):
            result.append(
                MessageEdited(raw, message_factory(_edited_message_payload(payload)))
            )
        elif kind == "message_sent":
            result.append(MessageSent(raw, payload))
        elif kind == "_unknown_fields" and isinstance(payload, list):
            for f in payload:
                if not isinstance(f, dict):
                    continue
                number = int(f.get("number", 0))
                name = _UPDATE_FIELD_NAMES.get(number, f"field_{number}")
                result.append(
                    RawUpdate(
                        raw,
                        _snake_case(name),
                        _decode_complete_update_field(f),
                    )
                )
        else:
            result.append(RawUpdate(raw, kind, payload))
    return result


__all__ = [
    "CallbackQuery",
    "ChatAction",
    "Event",
    "JoinRequest",
    "MessageDeleted",
    "MessageEdited",
    "MessageRead",
    "MessageSent",
    "NewMessage",
    "Raw",
    "RawUpdate",
    "Reaction",
    "Update",
    "UserTyping",
    "UserUpdate",
    "build_updates",
]
