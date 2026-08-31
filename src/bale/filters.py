"""Composable filters for incoming user-session messages."""

from __future__ import annotations

import builtins
import inspect
import json
import re
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bale.client import Client
    from bale.models import Message

Predicate = Callable[["Client", "Message"], bool | Awaitable[bool]]


@dataclass(frozen=True, slots=True)
class Filter:
    """An async-aware predicate composable with ``&``, ``|`` and ``~``."""

    predicate: Predicate
    name: str = "filter"

    async def check(self, client: Client, message: Message) -> bool:
        result = self.predicate(client, message)
        if inspect.isawaitable(result):
            result = await result
        return bool(result)

    def __call__(self) -> Filter:
        """Allow a filter to be used as either a value or a function."""
        return self

    def __and__(self, other: Filter) -> Filter:
        async def combined(client: Client, message: Message) -> bool:
            return await self.check(client, message) and await other.check(
                client, message
            )

        return Filter(combined, f"({self.name} & {other.name})")

    def __or__(self, other: Filter) -> Filter:
        async def combined(client: Client, message: Message) -> bool:
            return await self.check(client, message) or await other.check(
                client, message
            )

        return Filter(combined, f"({self.name} | {other.name})")

    def __invert__(self) -> Filter:
        async def inverted(client: Client, message: Message) -> bool:
            return not await self.check(client, message)

        return Filter(inverted, f"~{self.name}")


def create(predicate: Predicate, name: str = "custom") -> Filter:
    return Filter(predicate, name)


def all_of(*items: Filter) -> Filter:
    async def predicate(client: Client, message: Message) -> bool:
        for item in items:
            if not await item.check(client, message):
                return False
        return True

    return Filter(predicate, "all")


def any_of(*items: Filter) -> Filter:
    async def predicate(client: Client, message: Message) -> bool:
        for item in items:
            if await item.check(client, message):
                return True
        return False

    return Filter(predicate, "any")


text = Filter(lambda _client, message: bool(message.text), "text")
content = Filter(lambda _client, message: bool(message.content), "content")
gift = Filter(lambda _client, message: message.gift is not None, "gift")
private = Filter(
    lambda _client, message: message.chat.type.value == "private", "private"
)
group = Filter(
    lambda _client, message: message.chat.type.value in {"group", "supergroup"},
    "group",
)
channel = Filter(
    lambda _client, message: message.chat.type.value == "channel", "channel"
)
incoming = Filter(lambda _client, message: message.is_incoming, "incoming")
outgoing = Filter(lambda _client, message: message.is_outgoing, "outgoing")
# ``self_`` avoids shadowing Python's ``self`` convention while remaining
# convenient for account-based automations.
self_ = outgoing
me = outgoing
bot = Filter(lambda _client, message: message.author.is_bot, "bot")
reply = Filter(lambda _client, message: message.replied_to is not None, "reply")


def _has_media(message: Message, kind: str | None = None) -> bool:
    content = message.raw.get("message") or {}
    if not isinstance(content, dict):
        return False
    direct_keys = {
        "photo": "photo_message",
        "video": "video_message",
        "audio": "audio_message",
        "voice": "voice_message",
        "sticker": "sticker_message",
        "location": "location_message",
        "contact": "contact_message",
        "animation": "animation_message",
    }
    detected = {media_kind for media_kind, key in direct_keys.items() if key in content}
    document = content.get("document_message")
    if isinstance(document, dict):
        ext = document.get("ext")
        ext = ext if isinstance(ext, dict) else {}
        document_kinds = {
            "document_ex_photo": "photo",
            "document_ex_video": "video",
            "document_ex_audio": "audio",
            "document_ex_voice": "voice",
            "document_ex_gif": "animation",
        }
        specialized = {value for key, value in document_kinds.items() if key in ext}
        detected.update(specialized or {"document"})
    json_message = content.get("json_message")
    if isinstance(json_message, dict):
        raw_json = json_message.get("raw_json")
        if isinstance(raw_json, str):
            try:
                decoded = json.loads(raw_json)
            except ValueError:
                decoded = None
            if isinstance(decoded, dict):
                data_type = re.sub(
                    r"[^a-z]", "", str(decoded.get("dataType", "")).casefold()
                )
            else:
                data_type = ""
            if data_type in {"location", "contact"}:
                detected.add(data_type)
    return bool(detected) if kind is None else kind in detected


media = Filter(lambda _client, message: _has_media(message), "media")
photo = Filter(lambda _client, message: _has_media(message, "photo"), "photo")
video = Filter(lambda _client, message: _has_media(message, "video"), "video")
audio = Filter(lambda _client, message: _has_media(message, "audio"), "audio")
voice = Filter(lambda _client, message: _has_media(message, "voice"), "voice")
document = Filter(lambda _client, message: _has_media(message, "document"), "document")
sticker = Filter(lambda _client, message: _has_media(message, "sticker"), "sticker")
location = Filter(lambda _client, message: _has_media(message, "location"), "location")
contact = Filter(lambda _client, message: _has_media(message, "contact"), "contact")
animation = Filter(
    lambda _client, message: _has_media(message, "animation"), "animation"
)
forwarded = Filter(
    lambda _client, message: builtins.any(
        message.raw.get(key)
        for key in ("forwarded_message", "forwarded_messages", "forward_info")
    ),
    "forwarded",
)

# Uppercase aliases make migration from libraries with class-style filters easy.
Text = text
Content = content
Private = private
Group = group
Channel = channel
Incoming = incoming
Outgoing = outgoing
Media = media
Photo = photo
Video = video
Audio = audio
Voice = voice
Document = document
Sticker = sticker
Location = location
Contact = contact
Animation = animation
Bot = bot
Gift = gift
Reply = reply
Forwarded = forwarded


def sender(user_id: int) -> Filter:
    """Match messages authored by a specific Bale user ID."""
    expected = int(user_id)
    return Filter(
        lambda _client, message: message.sender_id == expected,
        f"sender({expected})",
    )


user = sender


def chat(peer_id: int | str) -> Filter:
    """Match messages belonging to one ``<peer_id>|<peer_type>`` chat."""
    expected = str(peer_id)
    return Filter(
        lambda _client, message: message.chat.id == expected,
        f"chat({expected})",
    )


chat_id = chat


def chat_type(kind: str) -> Filter:
    """Match a chat type such as ``private``, ``group`` or ``channel``."""
    expected = kind.casefold()
    return Filter(
        lambda _client, message: message.chat.type.value == expected,
        f"chat_type({expected})",
    )


def regex(pattern: str, *, flags: int = 0) -> Filter:
    """Match a regular expression against message text/content."""
    compiled = re.compile(pattern, flags)
    return Filter(
        lambda _client, message: compiled.search(message.content) is not None,
        f"regex({pattern})",
    )


def command(
    name: str,
    prefix: str = "/",
    min_args: int | None = None,
    max_args: int | None = None,
) -> Filter:
    expected = f"{prefix}{name}".casefold()

    def predicate(_client: Client, message: Message) -> bool:
        if not message.text:
            return False
        parts = message.text.strip().split()
        count = len(parts) - 1
        return bool(parts) and (
            parts[0].casefold() == expected
            and (min_args is None or count >= min_args)
            and (max_args is None or count <= max_args)
        )

    return Filter(predicate, f"command({name})")


# Short aliases for convenient filter composition.
all = all_of
any = any_of


def not_(item: Filter) -> Filter:
    return ~item
