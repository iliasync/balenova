"""Data models and serialization helpers for the Bale platform."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from bale.enums import (
    CallMode,
    CallRecordQuality,
    ChatType,
    GiftOpening,
    GivingType,
    MessageEntityType,
    PeerSource,
    PrivacyStatus,
    PrivacyType,
    ReportKind,
)
from bale.types.base import Serializable, model_to_dict, model_to_json
from bale.types.chat import Chat
from bale.types.entities import MessageEntity
from bale.types.message import Message, MessageButton, OtherMessage
from bale.types.user import User
from bale.types.wallet import (
    DefaultResponse,
    GiftPacket,
    PacketResponse,
    Wallet,
    WalletResponse,
    Winner,
)

if TYPE_CHECKING:
    pass


def peer_type_to_chat_type(peer_type: int) -> ChatType:
    return {
        1: ChatType.PRIVATE,
        2: ChatType.GROUP,
        3: ChatType.CHANNEL,
        4: ChatType.BOT,
        5: ChatType.SUPERGROUP,
        6: ChatType.THREAD,
    }.get(peer_type, ChatType.UNKNOWN)


def chat_type_to_peer_type(chat_type: ChatType | str | int) -> int:
    """Convert a ChatType enum, type name string, or integer to Bale wire peer type."""
    if isinstance(chat_type, int):
        return chat_type
    if isinstance(chat_type, ChatType):
        mapping = {
            ChatType.PRIVATE: 1,
            ChatType.GROUP: 2,
            ChatType.CHANNEL: 3,
            ChatType.BOT: 4,
            ChatType.SUPERGROUP: 5,
            ChatType.THREAD: 6,
        }
        return mapping.get(chat_type, 1)
    if isinstance(chat_type, str):
        normalized = chat_type.strip().lower()
        if normalized.isdigit():
            return int(normalized)
        str_mapping = {
            "private": 1,
            "user": 1,
            "group": 2,
            "channel": 3,
            "bot": 4,
            "supergroup": 5,
            "thread": 6,
        }
        if normalized in str_mapping:
            return str_mapping[normalized]
    raise ValueError(f"Invalid or unrecognized chat/peer type: {chat_type!r}")


def chat_id_to_peer_id(chat_id: int | str | User | Chat) -> int:
    """Extract numeric peer_id from any chat identifier.

    Supports:
        - Bale format: '123456|1' -> 123456, '987654|2' -> 987654
        - Telegram format: -100273076292 -> 273076292 (channel),
          -1509600244 -> 1509600244 (group)
        - Raw numbers / models: User / Chat -> integer ID
    """
    if isinstance(chat_id, Chat):
        return chat_id.peer_id
    if isinstance(chat_id, User):
        return chat_id.id
    if isinstance(chat_id, int):
        if chat_id < 0:
            s = str(chat_id)
            if s.startswith("-100") and len(s) > 4:
                return int(s[4:])
            return abs(chat_id)
        return chat_id
    if isinstance(chat_id, str):
        stripped = chat_id.strip()
        if "|" in stripped:
            first = stripped.split("|", 1)[0].strip()
            if first.lstrip("-").isdigit():
                return abs(int(first))
        if stripped.startswith("-100") and len(stripped) > 4 and stripped[4:].isdigit():
            return int(stripped[4:])
        if stripped.startswith("-") and stripped[1:].isdigit():
            return int(stripped[1:])
        if stripped.isdigit():
            return int(stripped)
    raise ValueError(f"Cannot extract numeric peer_id from {chat_id!r}")


def peer_id_to_chat_id(
    peer_id: int | str,
    peer_type: int | str | ChatType = 1,
    *,
    telegram_style: bool = False,
) -> str:
    """Format peer_id and peer_type into standard Bale chat_id string."""
    numeric_id = chat_id_to_peer_id(peer_id)
    resolved_type = chat_type_to_peer_type(peer_type)
    if telegram_style:
        if resolved_type in (3, 5):  # Channel / Supergroup
            return f"-100{numeric_id}"
        if resolved_type == 2:  # Group
            return f"-{numeric_id}"
        return str(numeric_id)
    return f"{numeric_id}|{resolved_type}"


def parse_chat_id(chat_id: int | str | User | Chat) -> tuple[int, int]:
    """Parse any chat identifier into a (peer_id, peer_type) tuple."""
    if isinstance(chat_id, Chat):
        return chat_id.peer_id, chat_id.peer_type
    if isinstance(chat_id, User):
        return chat_id.id, 4 if chat_id.is_bot else 1
    if isinstance(chat_id, int):
        if chat_id < 0:
            s = str(chat_id)
            if s.startswith("-100") and len(s) > 4:
                return int(s[4:]), 3
            return abs(chat_id), 2
        return chat_id, 1
    if isinstance(chat_id, str):
        stripped = chat_id.strip()
        if "|" in stripped:
            p_id, p_type = stripped.split("|", 1)
            return abs(int(p_id.strip())), int(p_type.strip())
        if stripped.startswith("-100") and len(stripped) > 4 and stripped[4:].isdigit():
            return int(stripped[4:]), 3
        if stripped.startswith("-") and stripped[1:].isdigit():
            return int(stripped[1:]), 2
        if stripped.isdigit():
            return int(stripped), 1
    raise ValueError(f"Cannot parse chat_id from {chat_id!r}")


def toggle_chat_id(
    identifier: int | str | User | Chat,
    *,
    peer_type: int | str | ChatType = 1,
    telegram_style: bool = False,
) -> int | str:
    """Two-way smart converter between chat_id and peer_id."""
    if isinstance(identifier, (Chat, User)):
        return identifier.peer_id if isinstance(identifier, Chat) else identifier.id

    if isinstance(identifier, str):
        stripped = identifier.strip()
        if "|" in stripped:
            return chat_id_to_peer_id(stripped)
        if stripped.startswith("-"):
            return chat_id_to_peer_id(stripped)
        if stripped.isdigit():
            return peer_id_to_chat_id(
                int(stripped), peer_type, telegram_style=telegram_style
            )

    if isinstance(identifier, int):
        if identifier < 0:
            return chat_id_to_peer_id(identifier)
        return peer_id_to_chat_id(identifier, peer_type, telegram_style=telegram_style)

    raise ValueError(f"Cannot toggle identifier: {identifier!r}")


convert_chat_id = toggle_chat_id


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
            dict(raw["permissions"]) if isinstance(raw.get("permissions"), dict) else {}
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


__all__ = [
    "CallMode",
    "CallRecordQuality",
    "Chat",
    "ChatType",
    "DefaultResponse",
    "GiftOpening",
    "GiftPacket",
    "GivingType",
    "Message",
    "MessageButton",
    "MessageEntity",
    "MessageEntityType",
    "OtherMessage",
    "PacketResponse",
    "PeerSource",
    "PrivacyStatus",
    "PrivacyType",
    "ReportKind",
    "Serializable",
    "User",
    "Wallet",
    "WalletResponse",
    "Winner",
    "chat_id_to_peer_id",
    "chat_type_to_peer_type",
    "convert_chat_id",
    "model_to_dict",
    "model_to_json",
    "parse_chat_id",
    "peer_id_to_chat_id",
    "peer_type_to_chat_type",
    "toggle_chat_id",
    "wrap_default",
    "wrap_group",
    "wrap_message",
    "wrap_packet_response",
    "wrap_user",
    "wrap_wallet_response",
]
