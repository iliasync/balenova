"""Friendly class-based updates delivered by :class:`bale.Client`."""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, cast

from google.protobuf.message_factory import GetMessageClass

from bale.models import Chat, ChatType, Message, Serializable, User, model_to_dict
from bale.proto import struct_pb2

if TYPE_CHECKING:
    from bale.client import Client


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
        return super().to_dict(include_raw=include_raw)

    def to_json(self, *, include_raw: bool = True, indent: int | None = 2) -> str:
        return json.dumps(
            self.to_dict(include_raw=include_raw),
            ensure_ascii=False,
            indent=indent,
            sort_keys=True,
        )


@dataclass(slots=True)
class NewMessage(Update):
    """A newly received or sent message."""

    message: Message

    def bind(self, client: Client) -> NewMessage:
        super().bind(client)
        self.message.bind(client)
        return self

    @property
    def text(self) -> str:
        return self.message.content

    @property
    def content(self) -> str:
        return self.message.content

    @property
    def chat(self) -> Chat:
        return self.message.chat

    @property
    def sender(self) -> User:
        return self.message.author

    @property
    def sender_id(self) -> int:
        return self.message.sender_id

    @property
    def is_private(self) -> bool:
        return self.chat.type is ChatType.PRIVATE

    @property
    def is_group(self) -> bool:
        return self.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP}

    @property
    def is_channel(self) -> bool:
        return self.chat.type is ChatType.CHANNEL

    async def answer(self, text: str) -> Message:
        return await self.message.answer(text)

    respond = answer

    async def reply(self, text: str) -> Message:
        return await self.message.reply(text)

    async def delete(self, just_me: bool = False) -> Any:
        return await self.message.delete(just_me)


@dataclass(slots=True)
class MessageEdited(NewMessage):
    """A message whose content changed while the client was running."""


@dataclass(slots=True)
class MessageSent(Update):
    """Confirmation data for a message sent by the current account."""

    data: Any


@dataclass(slots=True)
class RawUpdate(Update):
    """A decoded update that does not yet have a dedicated convenience class."""

    kind: str
    payload: Any


# Field numbers are part of Bale's wire contract. Keeping the complete known
# name table means an update added to our typed protobuf subset is still
# surfaced as e.g. ``RawUpdate(kind="typing")`` rather than disappearing.
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
    """Decode a field omitted by the compact event schema with the full proto."""
    number = int(field.get("number", 0))
    data = field.get("data")
    update_type = cast(Any, struct_pb2).WebUpdate
    descriptor = update_type.DESCRIPTOR.fields_by_number.get(number)
    if descriptor is None or descriptor.message_type is None or not isinstance(
        data, bytes | bytearray | memoryview
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
            for field in payload:
                if not isinstance(field, dict):
                    continue
                number = int(field.get("number", 0))
                name = _UPDATE_FIELD_NAMES.get(number, f"field_{number}")
                result.append(
                    RawUpdate(
                        raw,
                        _snake_case(name),
                        _decode_complete_update_field(field),
                    )
                )
        else:
            result.append(RawUpdate(raw, kind, payload))
    return result


__all__ = ["MessageEdited", "MessageSent", "NewMessage", "RawUpdate", "Update"]
