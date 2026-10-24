"""Dialog and conversations list models for Bale."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from bale.types.base import Serializable

if TYPE_CHECKING:
    from bale.client import Client
    from bale.types.chat import Chat
    from bale.types.message import Message


@dataclass(slots=True)
class Dialog(Serializable):
    """Represents a conversation entry in the user's dialogs list."""

    chat: Chat
    top_message: Message | None = None
    unread_count: int = 0
    is_pinned: bool = False
    draft: str | None = None
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def id(self) -> str:
        return self.chat.id

    @property
    def title(self) -> str:
        return self.chat.full_name

    def bind(self, client: Client) -> Dialog:
        self._client = client
        self.chat.bind(client)
        if self.top_message:
            self.top_message.bind(client)
        return self

    def __repr__(self) -> str:
        attrs = [f"chat={self.chat!r}"]
        if self.unread_count:
            attrs.append(f"unread_count={self.unread_count}")
        if self.is_pinned:
            attrs.append("is_pinned=True")
        return f"Dialog({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)


class DialogsList(list[Dialog]):
    """A list of Dialog objects with convenient lookup helpers."""

    def find_by_id(self, chat_id: int | str) -> Dialog | None:
        """Find a dialog by numeric peer ID or Bale 'id|type' string."""
        str_id = str(chat_id)
        for d in self:
            if d.chat.id == str_id or str(d.chat.peer_id) == str_id:
                return d
        return None

    def find_by_username(self, username: str) -> Dialog | None:
        """Find a dialog by @username."""
        clean = username.lstrip("@").lower()
        for d in self:
            if d.chat.username and d.chat.username.lower() == clean:
                return d
        return None
