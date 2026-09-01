"""High-level objects returned by the Bale user-session client."""

from __future__ import annotations

import base64
import json
from dataclasses import dataclass, field, fields
from enum import Enum, IntEnum
from typing import TYPE_CHECKING, Any, cast

from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message as ProtoMessage

from bale.errors import ClientStateError

if TYPE_CHECKING:
    from bale.client import Client


class Serializable:
    """Convenience conversion helpers shared by public response models."""

    def to_dict(self, *, include_raw: bool = False) -> dict[str, Any]:
        return cast(dict[str, Any], model_to_dict(self, include_raw=include_raw))

    def to_json(self, *, include_raw: bool = False, indent: int | None = 2) -> str:
        return json.dumps(
            self.to_dict(include_raw=include_raw),
            ensure_ascii=False,
            indent=indent,
            sort_keys=True,
        )

    def as_dict(self, *, include_raw: bool = False) -> dict[str, Any]:
        """Alias for :meth:`to_dict` with a discoverable Pythonic name."""
        return self.to_dict(include_raw=include_raw)

    def as_json(self, *, include_raw: bool = False, indent: int | None = 2) -> str:
        """Alias for :meth:`to_json` suitable for generic serializers."""
        return self.to_json(include_raw=include_raw, indent=indent)


def model_to_dict(value: Any, *, include_raw: bool = False) -> Any:
    """Convert a Bale model (including nested models) to JSON-safe values."""
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, ProtoMessage):
        return MessageToDict(
            value,
            preserving_proto_field_name=True,
            use_integers_for_enums=True,
        )
    if isinstance(value, bytes):
        return base64.b64encode(value).decode("ascii")
    if isinstance(value, Serializable):
        return {
            item.name: model_to_dict(getattr(value, item.name), include_raw=include_raw)
            for item in fields(cast(Any, value))
            if not item.name.startswith("_") and (include_raw or item.name != "raw")
        }
    if isinstance(value, dict):
        return {
            str(key): model_to_dict(item, include_raw=include_raw)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple, set)):
        return [model_to_dict(item, include_raw=include_raw) for item in value]
    return value


def model_to_json(
    value: Any, *, include_raw: bool = False, indent: int | None = 2
) -> str:
    """Serialize a model or response value as readable JSON."""
    return json.dumps(
        model_to_dict(value, include_raw=include_raw),
        ensure_ascii=False,
        indent=indent,
        sort_keys=True,
    )


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


class PrivacyType(IntEnum):
    INVITE = 0
    PRESENCE = 1
    MONEY_TRANSFER = 2


class PrivacyStatus(IntEnum):
    EVERYONE = 0
    CONTACTS = 1
    NOBODY = 2


class CallMode(IntEnum):
    UNKNOWN = 0
    PRIVATE = 1
    GROUP = 2
    MULTI_PEER = 3
    CHANNEL_LIVE = 4


class CallRecordQuality(IntEnum):
    NOT_SPECIFIED = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    ULTRA = 4
    ULTRA_PLUS = 5


@dataclass(slots=True)
class User(Serializable):
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
class Chat(Serializable):
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
        return await self._require_client().report_chat(self.id, reason, kind)

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Chat is not bound to a client")
        return self._client


@dataclass(slots=True)
class GiftPacket(Serializable):
    count: int = 0
    total_amount: int = 0
    giving_type: GivingType = GivingType.SAME
    token: str | None = None
    message: str | None = None
    owner_id: int | None = None
    show_amounts: bool = False


@dataclass(slots=True)
class Message(Serializable):
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
    def is_outgoing(self) -> bool:
        """Whether this message was sent by the currently connected account.

        Bale identifies the author by account ID, so messages sent from another
        device/session of the same account are also correctly classified as
        outgoing. The protocol does not expose a reliable device/session ID.
        """
        if self._client is None or self._client.user is None:
            return False
        own_id = self._client.user.id
        if self.author.id == own_id:
            return True
        # Saved Messages is a private dialog whose peer is the account itself.
        # Some edited-message updates omit sender_uid (decoded as zero), but no
        # other account can author a message in this dialog.
        return bool(
            self.author.id == 0
            and self.chat.peer_type == 1
            and self.chat.peer_id == own_id
        )

    @property
    def is_incoming(self) -> bool:
        """Whether this message was authored by another account."""
        return not self.is_outgoing

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

    respond = answer

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

    async def download(self) -> bytes:
        return await self._require_client().download_media(self)

    async def clear_chat(self) -> DefaultResponse:
        return await self._require_client().clear_chat(self.chat.id)

    async def delete_chat(self) -> DefaultResponse:
        return await self._require_client().delete_chat(self.chat.id)

    async def load_history(self, limit: int = 20, from_date: int = -1) -> list[Message]:
        return await self._require_client().load_history(self.chat.id, from_date, limit)

    async def pin(self, just_mine: bool = False) -> DefaultResponse:
        return await self._require_client().pin_message(
            self.chat.id, self.id, just_mine
        )

    async def unpin(self) -> DefaultResponse:
        return await self._require_client().unpin_message(self.chat.id, self.id)

    async def unpin_all(self) -> DefaultResponse:
        return await self._require_client().unpin_all(self.chat.id)

    async def pin_in_group(self) -> DefaultResponse:
        return await self._require_client().pin_group_message(self.chat.id, self.id)

    async def unpin_in_group(self) -> DefaultResponse:
        return await self._require_client().unpin_group_message(self.chat.id, self.id)

    async def unpin_all_in_group(self) -> DefaultResponse:
        return await self._require_client().remove_group_pins(self.chat.id)

    async def load_pinned_messages(self) -> list[Message]:
        return await self._require_client().load_pinned_messages(self.chat.id)

    async def load_full_chat(self) -> dict[str, Any] | None:
        return await self._require_client().load_full_chat(self.chat.id)

    async def react(self, code: str) -> dict[str, Any]:
        return await self._require_client().message_set_reaction(
            self.chat.id, self.id, code
        )

    async def remove_reaction(self, code: str) -> dict[str, Any]:
        return await self._require_client().message_remove_reaction(
            self.chat.id, self.id, code
        )

    async def click(self, data: str) -> dict[str, Any]:
        """Trigger an inline callback using data from a message button."""
        return await self._require_client().click_inline_button(
            self.chat.id, self.id, data
        )

    async def forward(self, chat_id: str) -> DefaultResponse:
        return await self._require_client().forward_message(
            chat_id, self.chat.id, self.id
        )

    async def copy(self, chat_id: str) -> Message:
        return await self._require_client().copy_message(chat_id, self.chat.id, self.id)

    async def open_gift(self, receiver_token: str | None = None) -> PacketResponse:
        return await self._require_client().open_gift(self, receiver_token)

    open_packet = open_gift

    async def report(
        self, reason: str | None = None, kind: ReportKind = ReportKind.SPAM
    ) -> DefaultResponse:
        return await self._require_client().report_message(
            self.chat.id, self, reason, kind
        )

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Message is not bound to a client")
        return self._client


@dataclass(frozen=True, slots=True)
class DefaultResponse(Serializable):
    seq: int | None = None
    date: int | None = None
    state: bytes | None = None
    seq_big: int | None = None
    ext: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class OtherMessage(Serializable):
    date: int
    message_id: int | str
    seq: int | None = None


@dataclass(frozen=True, slots=True)
class Winner(Serializable):
    id: int
    amount: int = 0
    date: int | None = None


@dataclass(frozen=True, slots=True)
class PacketResponse(Serializable):
    receivers: tuple[Winner, ...] = ()
    status: GiftOpening = GiftOpening.ALREADY_RECEIVED
    opened_count: int = 0
    win_amount: int = 0
    rank: int = 0


@dataclass(frozen=True, slots=True)
class Wallet(Serializable):
    token: str
    is_merchant: bool = False
    app: str | None = None
    balance: int = 0
    level: int = 0
    pan: str | None = None
    account: str | None = None


@dataclass(frozen=True, slots=True)
class WalletResponse(Serializable):
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
        access_hash=int(raw.get("access_hash", 0)),
        is_member=bool(_wrapped(raw.get("is_member"), False)),
        can_send_message=bool(_wrapped(raw.get("can_send_message"), False)),
        permissions=(
            dict(raw["permissions"])
            if isinstance(raw.get("permissions"), dict)
            else {}
        ),
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
        state=bytes(raw["state"]) if "state" in raw else None,
        seq_big=int(raw["seq_big"]) if "seq_big" in raw else None,
        ext=dict(raw.get("ext", {})),
    )


def wrap_packet_response(raw: dict[str, Any]) -> PacketResponse:
    status = raw.get("status", 0)
    if isinstance(status, str):
        status = {
            "GIFT_OPENNING_SOLD_OUT": GiftOpening.SOLD_OUT,
            "GIFT_OPENNING_GIFT_CREATOR": GiftOpening.GIFT_CREATOR,
            "GIFT_OPENNING_SUCCESSFUL": GiftOpening.SUCCESSFUL,
            "GIFT_OPENNING_PENDING": GiftOpening.PENDING,
        }.get(status, GiftOpening.ALREADY_RECEIVED)
    return PacketResponse(
        receivers=tuple(
            Winner(
                id=int(item.get("id", 0)),
                amount=int(item.get("amount", 0)),
                date=int(item["date"]) if "date" in item else None,
            )
            for item in raw.get("receivers", [])
        ),
        status=GiftOpening(int(status)),
        opened_count=int(raw.get("openned_count", 0)),
        win_amount=int(_wrapped(raw.get("win_amount"), 0)),
        rank=int(_wrapped(raw.get("rank"), 0)),
    )


def wrap_wallet_response(raw: dict[str, Any]) -> WalletResponse:
    values = raw.get("wallet")
    value = values[0] if isinstance(values, list) and values else values
    wallet = None
    if isinstance(value, dict):
        wallet = Wallet(
            token=str(value.get("token", "")),
            is_merchant=bool(_wrapped(value.get("is_merchant"), False)),
            app=_string(value.get("app")),
            balance=int(value.get("balance", 0)),
            level=int(value.get("level", 0)),
            pan=_wrapped(value.get("pan")),
            account=_wrapped(value.get("account")),
        )
    return WalletResponse(
        wallet=wallet,
        first_name=_wrapped(raw.get("first_name")),
        last_name=_wrapped(raw.get("last_name")),
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
