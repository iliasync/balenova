"""Rich event update classes for Bale, inspired by Telethon and Pyrogram."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from bale.errors import ClientStateError
from bale.types.base import Serializable
from bale.types.chat import Chat
from bale.types.message import Message
from bale.types.user import User

if TYPE_CHECKING:
    from bale.client import Client


@dataclass(slots=True)
class ChatActionEvent(Serializable):
    """Event triggered on member joins, departures, kicks, or chat settings changes."""

    chat: Chat
    from_user: User
    action: str  # "joined", "left", "kicked", "promoted", "demoted", "new_title"
    actor: User | None = None
    date: int = 0
    title: str | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def user_joined(self) -> bool:
        return self.action in ("joined", "invite")

    @property
    def user_left(self) -> bool:
        return self.action == "left"

    @property
    def user_kicked(self) -> bool:
        return self.action == "kicked"

    def bind(self, client: Client) -> ChatActionEvent:
        self._client = client
        self.chat.bind(client)
        self.from_user.bind(client)
        if self.actor:
            self.actor.bind(client)
        return self

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Event is not bound to a client")
        return self._client

    async def reply(self, text: str, **kwargs: Any) -> Message:
        """Reply with a message in this chat."""
        return await self._require_client().send_message(self.chat.id, text, **kwargs)

    def __repr__(self) -> str:
        return (
            f"ChatActionEvent(chat={self.chat!r}, from_user={self.from_user!r}, "
            f"action={self.action!r})"
        )

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class CallbackQueryEvent(Serializable):
    """Event triggered when an inline keyboard callback button is clicked."""

    id: str | int
    chat: Chat
    from_user: User
    data: str
    message: Message | None = None
    pattern_match: Any = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def data_str(self) -> str:
        return self.data

    def bind(self, client: Client) -> CallbackQueryEvent:
        self._client = client
        self.chat.bind(client)
        self.from_user.bind(client)
        if self.message:
            self.message.bind(client)
        return self

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("CallbackQueryEvent is not bound to a client")
        return self._client

    async def answer(self, text: str = "", *, alert: bool = False) -> Any:
        """Acknowledge or answer the callback query with an optional popup alert."""
        # Bale handles inline callbacks via message clicks; acknowledgement is optional
        return True

    async def edit(self, text: str, *, reply_markup: Any = None) -> Any:
        """Edit the message containing the button."""
        if self.message:
            return await self.message.edit_text(text)
        return await self._require_client().edit_message_text(
            self.chat.id, str(self.id), text
        )

    def __repr__(self) -> str:
        return (
            f"CallbackQueryEvent(chat={self.chat!r}, from_user={self.from_user!r}, "
            f"data={self.data!r})"
        )

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class MessageDeletedEvent(Serializable):
    """Event triggered when messages are deleted."""

    chat_id: str | int
    message_ids: list[int | str]
    chat: Chat | None = None
    _client: Client | None = field(default=None, repr=False, compare=False)

    def bind(self, client: Client) -> MessageDeletedEvent:
        self._client = client
        if self.chat:
            self.chat.bind(client)
        return self

    def __repr__(self) -> str:
        return (
            f"MessageDeletedEvent(chat_id={self.chat_id!r}, "
            f"message_ids={self.message_ids!r})"
        )

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class UserTypingEvent(Serializable):
    """Event triggered when a user starts typing or uploading media in a chat."""

    chat: Chat
    from_user: User
    action: str = "typing"
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def is_typing(self) -> bool:
        return self.action == "typing"

    def bind(self, client: Client) -> UserTypingEvent:
        self._client = client
        self.chat.bind(client)
        self.from_user.bind(client)
        return self

    def __repr__(self) -> str:
        return (
            f"UserTypingEvent(chat={self.chat!r}, from_user={self.from_user!r}, "
            f"action={self.action!r})"
        )

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class UserStatusEvent(Serializable):
    """Event triggered when a user's presence changes (online / offline)."""

    from_user: User
    status: str = "offline"  # "online" or "offline"
    last_seen: int = 0
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def is_online(self) -> bool:
        return self.status == "online"

    @property
    def is_offline(self) -> bool:
        return not self.is_online

    def bind(self, client: Client) -> UserStatusEvent:
        self._client = client
        self.from_user.bind(client)
        return self

    def __repr__(self) -> str:
        return f"UserStatusEvent(from_user={self.from_user!r}, status={self.status!r})"

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class MessageReadEvent(Serializable):
    """Event triggered when messages are marked as read."""

    chat: Chat
    max_id: int | str
    is_outbox: bool = False
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def is_inbox(self) -> bool:
        return not self.is_outbox

    def bind(self, client: Client) -> MessageReadEvent:
        self._client = client
        self.chat.bind(client)
        return self

    def __repr__(self) -> str:
        return (
            f"MessageReadEvent(chat={self.chat!r}, max_id={self.max_id!r}, "
            f"is_outbox={self.is_outbox})"
        )

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class ReactionUpdateEvent(Serializable):
    """Event triggered when an emoji reaction is added or modified."""

    chat: Chat
    message_id: int | str
    from_user: User
    reaction: str
    _client: Client | None = field(default=None, repr=False, compare=False)

    def bind(self, client: Client) -> ReactionUpdateEvent:
        self._client = client
        self.chat.bind(client)
        self.from_user.bind(client)
        return self

    def __repr__(self) -> str:
        return (
            f"ReactionUpdateEvent(chat={self.chat!r}, message_id={self.message_id!r}, "
            f"reaction={self.reaction!r}, from_user={self.from_user!r})"
        )

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class JoinRequestEvent(Serializable):
    """Event triggered when a user requests to join a private group or channel."""

    chat: Chat
    from_user: User
    about: str | None = None
    _client: Client | None = field(default=None, repr=False, compare=False)

    def bind(self, client: Client) -> JoinRequestEvent:
        self._client = client
        self.chat.bind(client)
        self.from_user.bind(client)
        return self

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("JoinRequestEvent is not bound to a client")
        return self._client

    async def approve(self) -> Any:
        """Approve the join request."""
        # Using chat management rpc
        return await self._require_client().rpc(
            "bale.group.v1.Group",
            "ApproveJoinRequest",
            peer=self.chat.id,
            user_id=self.from_user.id,
        )

    async def decline(self) -> Any:
        """Decline the join request."""
        return await self._require_client().rpc(
            "bale.group.v1.Group",
            "DeclineJoinRequest",
            peer=self.chat.id,
            user_id=self.from_user.id,
        )

    def __repr__(self) -> str:
        return f"JoinRequestEvent(chat={self.chat!r}, from_user={self.from_user!r})"

    def __str__(self) -> str:
        return repr(self)
