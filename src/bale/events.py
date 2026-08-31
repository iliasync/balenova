"""Friendly class-based updates delivered by :class:`bale.Client`."""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from bale.models import Chat, ChatType, Message, Serializable, User, model_to_dict

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

    data: bytes


@dataclass(slots=True)
class RawUpdate(Update):
    """A decoded update that does not yet have a dedicated convenience class."""

    kind: str
    payload: Any


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
        elif kind == "message_sent" and isinstance(payload, bytes):
            result.append(MessageSent(raw, payload))
        else:
            result.append(RawUpdate(raw, kind, payload))
    return result


__all__ = ["MessageEdited", "MessageSent", "NewMessage", "RawUpdate", "Update"]
