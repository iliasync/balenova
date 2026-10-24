"""High-level Chat type for Bale dialogs, groups, channels, and private chats."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from bale.enums import ChatType, GivingType, ReportKind
from bale.errors import ClientStateError
from bale.types.base import Serializable

if TYPE_CHECKING:
    from bale.client import Client
    from bale.types.message import Message
    from bale.types.wallet import DefaultResponse


@dataclass(slots=True)
class Chat(Serializable):
    """Represents a private conversation, group, or channel in Bale."""

    peer_id: int
    peer_type: int
    title: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    type: ChatType = ChatType.UNKNOWN
    access_hash: int = 0
    is_member: bool = False
    can_send_message: bool = False
    permissions: dict[str, Any] = field(default_factory=dict)
    _client: Client | None = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self.type is ChatType.UNKNOWN:
            from bale.models import peer_type_to_chat_type

            self.type = peer_type_to_chat_type(self.peer_type)

    @property
    def id(self) -> str:
        """String representation of Bale peer (e.g. '123456|1' or '987654|2')."""
        return f"{self.peer_id}|{self.peer_type}"

    @property
    def full_name(self) -> str:
        """Display title or user's full name."""
        return " ".join(filter(None, (self.first_name, self.last_name))) or (
            self.title or ""
        )

    @property
    def is_private(self) -> bool:
        """Whether this chat is a 1-on-1 private conversation."""
        return self.type in (ChatType.PRIVATE, ChatType.BOT) or self.peer_type in (1, 4)

    @property
    def is_group(self) -> bool:
        """Whether this chat is a group or supergroup."""
        is_type = self.type in (ChatType.GROUP, ChatType.SUPERGROUP)
        return is_type or self.peer_type in (2, 5)

    @property
    def is_channel(self) -> bool:
        """Whether this chat is a broadcast channel."""
        return self.type == ChatType.CHANNEL or self.peer_type == 3

    @property
    def mention(self) -> str:
        """Public mention tag or markdown link."""
        if self.username:
            return f"@{self.username}"
        return f"[{self.full_name}](bale://chat?id={self.peer_id})"

    def bind(self, client: Client) -> Chat:
        """Bind this Chat instance to an active Client session."""
        self._client = client
        return self

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Chat is not bound to a client")
        return self._client

    async def send(self, text: str, **kwargs: Any) -> Message:
        """Send a message to this chat."""
        return await self._require_client().send_message(self.id, text, **kwargs)

    send_message = send

    async def send_photo(
        self,
        photo: Any,
        caption: str = "",
        **kwargs: Any,
    ) -> Message:
        """Send a photo to this chat."""
        return await self._require_client().send_photo(
            self.id, photo, caption=caption, **kwargs
        )

    async def send_document(
        self,
        document: Any,
        caption: str = "",
        **kwargs: Any,
    ) -> Message:
        """Send a document or file to this chat."""
        return await self._require_client().send_document(
            self.id, document, caption=caption, **kwargs
        )

    async def send_action(self, action: int = 1) -> bool:
        """Send a chat action indicator (typing=1, etc.)."""
        return bool(await self._require_client().typing(self.id, action))

    async def load_history(self, limit: int = 20, from_date: int = -1) -> list[Message]:
        """Load recent message history in this chat."""
        return await self._require_client().load_history(self.id, from_date, limit)

    async def send_gift(
        self,
        amount: int,
        message: str,
        *,
        gift_count: int = 1,
        giving_type: GivingType = GivingType.SAME,
        show_amounts: bool = True,
        token: str | None = None,
    ) -> DefaultResponse:
        """Send a gift packet in this chat."""
        return await self._require_client().send_gift(
            self.id,
            amount,
            message,
            gift_count=gift_count,
            giving_type=giving_type,
            show_amounts=show_amounts,
            token=token,
        )

    send_giftpacket = send_gift

    async def report(
        self, reason: str | None = None, kind: ReportKind = ReportKind.SPAM
    ) -> Any:
        """Report this chat for spam or violation."""
        return await self._require_client().report_chat(self.id, reason, kind)

    async def leave(self) -> Any:
        """Leave this group or channel."""
        return await self._require_client().leave_chat(self.id)

    def __repr__(self) -> str:
        attrs = [f"id={self.id!r}", f"type={self.type.value!r}"]
        if self.title:
            attrs.append(f"title={self.title!r}")
        if self.username:
            attrs.append(f"username={self.username!r}")
        return f"Chat({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)
