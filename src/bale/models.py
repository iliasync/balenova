"""High-level objects returned by the Bale user-session client."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, IntEnum
from typing import TYPE_CHECKING, Any

from bale.errors import ClientStateError

if TYPE_CHECKING:
    from bale.client import Client


class ChatType(str, Enum):
    PRIVATE = "private"
    GROUP = "group"
    CHANNEL = "channel"
    BOT = "bot"
    SUPERGROUP = "supergroup"
    THREAD = "thread"
    UNKNOWN = "unknown"


class GivingType(IntEnum):
    SAME = 0
    RANDOM = 1


class GiftOpening(IntEnum):
    ALREADY_RECEIVED = 0
    SOLD_OUT = 1
    GIFT_CREATOR = 2
    SUCCESSFUL = 3
    PENDING = 4


class ReportKind(IntEnum):
    UNKNOWN = 0
    SCAM = 1
    INAPPROPRIATE_CONTENT = 2
    OTHER = 3
    VIOLENCE = 4
    SPAM = 5
    FALSE_INFORMATION = 6


class PeerSource(IntEnum):
    UNKNOWN = 0
    DIALOGS = 1
    VITRINE = 2
    MARKET = 3
    PRIVACY_BAR = 4


@dataclass(slots=True)
class User:
    id: int
    username: str | None = None
    name: str | None = None
    is_bot: bool = False
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def full_name(self) -> str:
        return self.name or ""

    def bind(self, client: Client) -> User:
        self._client = client
        return self


@dataclass(slots=True)
class Chat:
    peer_id: int
    peer_type: int
    title: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    type: ChatType = ChatType.UNKNOWN
    _client: Client | None = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self.type is ChatType.UNKNOWN:
            self.type = peer_type_to_chat_type(self.peer_type)

    @property
    def id(self) -> str:
        return f"{self.peer_id}|{self.peer_type}"

    @property
    def full_name(self) -> str:
        return " ".join(filter(None, (self.first_name, self.last_name))) or (
            self.title or ""
        )

    def bind(self, client: Client) -> Chat:
        self._client = client
        return self

    async def send(self, text: str) -> Message:
        return await self._require_client().send_message(self.id, text)

    async def load_history(self, limit: int = 20, from_date: int = -1) -> list[Message]:
        return await self._require_client().load_history(self.id, from_date, limit)

    async def report(
        self, reason: str | None = None, kind: ReportKind = ReportKind.SPAM
    ) -> Any:
        return await self._require_client().report_chat(self.id, reason, kind)

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Chat is not bound to a client")
        return self._client


@dataclass(slots=True)
class GiftPacket:
    count: int = 0
    total_amount: int = 0
    giving_type: GivingType = GivingType.SAME
    token: str | None = None
    message: str | None = None
    owner_id: int | None = None
    show_amounts: bool = False


@dataclass(slots=True)
class Message:
    rid: int | str
    date: int
    author: User
    chat: Chat
    text: str | None = None
    caption: str | None = None
    gift: GiftPacket | None = None
    replied_to: Message | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def id(self) -> str:
        return f"{self.rid}|{self.date}"

    @property
    def message_id(self) -> int | str:
        return self.rid

    @property
    def sender_id(self) -> int:
        return self.author.id

    @property
    def content(self) -> str:
        return self.text or self.caption or ""

    def bind(self, client: Client) -> Message:
        self._client = client
        self.author.bind(client)
        self.chat.bind(client)
        if self.replied_to:
            self.replied_to.bind(client)
        return self

    async def answer(self, text: str) -> Message:
        return await self._require_client().send_message(self.chat.id, text)

    async def reply(self, text: str) -> Message:
        return await self._require_client().send_message(self.chat.id, text, self)

    async def edit_text(self, text: str) -> DefaultResponse:
        return await self._require_client().edit_message_text(
            self.chat.id, self.id, text
        )

    async def delete(self, just_me: bool = False) -> DefaultResponse:
        return await self._require_client().delete_message(
            self.chat.id, self.id, just_me
        )

    async def seen(self) -> DefaultResponse:
        return await self._require_client().seen_chat(self.chat.id, self.date)

    async def react(self, code: str) -> dict[str, Any]:
        return await self._require_client().message_set_reaction(
            self.chat.id, self.id, code
        )

    async def forward(self, chat_id: str) -> DefaultResponse:
        return await self._require_client().forward_message(
            chat_id, self.chat.id, self.id
        )

    async def copy(self, chat_id: str) -> Message:
        return await self._require_client().copy_message(chat_id, self.chat.id, self.id)

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Message is not bound to a client")
        return self._client


@dataclass(frozen=True, slots=True)
class DefaultResponse:
    seq: int | None = None
    date: int | None = None


@dataclass(frozen=True, slots=True)
class OtherMessage:
    date: int
    message_id: int | str
    seq: int | None = None


@dataclass(frozen=True, slots=True)
class Winner:
    id: int
    amount: int = 0
    date: int | None = None


@dataclass(frozen=True, slots=True)
class PacketResponse:
    receivers: tuple[Winner, ...] = ()
    status: GiftOpening = GiftOpening.ALREADY_RECEIVED
    opened_count: int = 0
    win_amount: int = 0
    rank: int = 0


@dataclass(frozen=True, slots=True)
class Wallet:
    token: str
    is_merchant: bool = False
    app: str | None = None
    balance: int = 0
    level: int = 0
    pan: str | None = None
    account: str | None = None


@dataclass(frozen=True, slots=True)
class WalletResponse:
    wallet: Wallet | None = None
    first_name: str | None = None
    last_name: str | None = None


def peer_type_to_chat_type(peer_type: int) -> ChatType:
    return {
        1: ChatType.PRIVATE,
        2: ChatType.GROUP,
        3: ChatType.CHANNEL,
        4: ChatType.BOT,
        5: ChatType.SUPERGROUP,
        6: ChatType.THREAD,
    }.get(peer_type, ChatType.UNKNOWN)


def wrap_user(raw: dict[str, Any]) -> User:
    return User(
        id=int(raw.get("id", 0)),
        username=_wrapped(raw.get("nick")),
        name=_string(raw.get("name")),
        is_bot=bool(_wrapped(raw.get("is_bot"), False)),
    )


def wrap_group(raw: dict[str, Any]) -> Chat:
    group_type = raw.get("group_type")
    peer_type = 3 if group_type in (1, "GROUP_TYPE_CHANNEL") else 2
    if group_type in (2, "GROUP_TYPE_SUPER_GROUP"):
        peer_type = 5
    return Chat(
        peer_id=int(raw.get("id", 0)),
        peer_type=peer_type,
        title=_string(raw.get("title")),
        username=_wrapped(raw.get("nick")),
    )


def wrap_message(
    raw: dict[str, Any], *, chat: Chat | None = None, author: User | None = None
) -> Message:
    peer = raw.get("peer") or {}
    actual_chat = chat or Chat(int(peer.get("id", 0)), int(peer.get("type", 0)))
    actual_author = author or User(int(raw.get("sender_uid", 0)))
    content = raw.get("message") or {}
    text_message = content.get("text_message") or {}
    document_message = content.get("document_message") or {}
    caption = document_message.get("caption") or {}
    quoted = raw.get("quoted_message") or {}
    replied_to = None
    if quoted.get("quoted_message_content"):
        quoted_peer = quoted.get("quoted_peer") or peer
        replied_to = wrap_message(
            {
                "peer": quoted_peer,
                "sender_uid": quoted.get("sender_user_id", 0),
                "date": quoted.get("message_date", 0),
                "rid": _wrapped(quoted.get("message_id"), 0),
                "message": quoted["quoted_message_content"],
            }
        )
    return Message(
        rid=raw.get("rid", 0),
        date=int(raw.get("date", 0)),
        author=actual_author,
        chat=actual_chat,
        text=_string(text_message.get("text")),
        caption=_string(caption.get("text")),
        gift=_wrap_gift(content.get("gift")),
        replied_to=replied_to,
        raw=raw,
    )


def wrap_default(raw: dict[str, Any]) -> DefaultResponse:
    return DefaultResponse(
        seq=int(raw["seq"]) if "seq" in raw else None,
        date=int(raw["date"]) if "date" in raw else None,
    )


def _wrap_gift(raw: Any) -> GiftPacket | None:
    if not isinstance(raw, dict):
        return None
    giving_type = raw.get("giving_type", 0)
    return GiftPacket(
        count=int(raw.get("count", 0)),
        total_amount=int(raw.get("total_amount", 0)),
        giving_type=(
            GivingType.RANDOM
            if giving_type in (1, "GIVING_TYPE_RANDOM")
            else GivingType.SAME
        ),
        token=_wrapped(raw.get("token")),
        message=_wrapped(raw.get("message")),
        owner_id=int(raw["owner_id"]) if "owner_id" in raw else None,
        show_amounts=bool(_wrapped(raw.get("show_amounts"), False)),
    )


def _wrapped(value: Any, default: Any = None) -> Any:
    if isinstance(value, dict):
        return value.get("value", default)
    return default if value is None else value


def _string(value: Any) -> str | None:
    return value if isinstance(value, str) and value else None
