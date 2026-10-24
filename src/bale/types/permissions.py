"""Chat permissions and admin privileges for Bale."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from bale.types.base import Serializable


@dataclass(slots=True)
class ChatPermissions(Serializable):
    """Describes actions a normal member can perform in a chat."""

    can_send_messages: bool = True
    can_send_media: bool = True
    can_send_stickers: bool = True
    can_send_polls: bool = True
    can_add_web_page_previews: bool = True
    can_change_info: bool = False
    can_invite_users: bool = True
    can_pin_messages: bool = False

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ChatPermissions:
        return cls(
            can_send_messages=bool(data.get("can_send_messages", True)),
            can_send_media=bool(data.get("can_send_media", True)),
            can_send_stickers=bool(data.get("can_send_stickers", True)),
            can_send_polls=bool(data.get("can_send_polls", True)),
            can_add_web_page_previews=bool(data.get("can_add_web_page_previews", True)),
            can_change_info=bool(data.get("can_change_info", False)),
            can_invite_users=bool(data.get("can_invite_users", True)),
            can_pin_messages=bool(data.get("can_pin_messages", False)),
        )


@dataclass(slots=True)
class ChatPrivileges(Serializable):
    """Describes privileges granted to an administrator in a chat."""

    is_anonymous: bool = False
    can_manage_chat: bool = True
    can_delete_messages: bool = True
    can_manage_video_chats: bool = False
    can_restrict_members: bool = True
    can_promote_members: bool = False
    can_change_info: bool = True
    can_invite_users: bool = True
    can_pin_messages: bool = True

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ChatPrivileges:
        return cls(
            is_anonymous=bool(data.get("is_anonymous", False)),
            can_manage_chat=bool(data.get("can_manage_chat", True)),
            can_delete_messages=bool(data.get("can_delete_messages", True)),
            can_manage_video_chats=bool(data.get("can_manage_video_chats", False)),
            can_restrict_members=bool(data.get("can_restrict_members", True)),
            can_promote_members=bool(data.get("can_promote_members", False)),
            can_change_info=bool(data.get("can_change_info", True)),
            can_invite_users=bool(data.get("can_invite_users", True)),
            can_pin_messages=bool(data.get("can_pin_messages", True)),
        )
