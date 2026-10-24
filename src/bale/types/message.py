"""High-level Message and MessageButton types for Bale."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from bale.enums import ReportKind
from bale.errors import ClientStateError
from bale.types.base import Serializable
from bale.types.chat import Chat
from bale.types.media import (
    Audio,
    Contact,
    Document,
    Location,
    Photo,
    Poll,
    PollOption,
    Sticker,
    Video,
    Voice,
)
from bale.types.user import User
from bale.types.wallet import DefaultResponse, GiftPacket, PacketResponse

if TYPE_CHECKING:
    from bale.client import Client


class MessageButton:
    """Represents an interactive button on a message in Bale."""

    def __init__(
        self,
        text: str,
        data: str | bytes | None = None,
        url: str | None = None,
        button_type: str = "callback",
        row: int = 0,
        col: int = 0,
        message: Message | None = None,
        raw: Any = None,
    ):
        self.text = text
        self.data = data
        self.url = url
        self.type = button_type
        self.row = row
        self.col = col
        self._message = message
        self._raw = raw

    @property
    def data_str(self) -> str:
        """Returns button data decoded as a string."""
        if isinstance(self.data, bytes):
            return self.data.decode("utf-8", errors="replace")
        return str(self.data or "")

    @property
    def is_callback(self) -> bool:
        return self.type == "callback" or self.data is not None

    @property
    def is_url(self) -> bool:
        return self.type == "url" or self.url is not None

    async def click(self) -> Any:
        """Clicks this button using the logged-in client session."""
        if not self._message:
            raise ClientStateError("Button is not bound to a Message")
        return await self._message.click(self.data_str)

    def to_dict(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "data": self.data_str if self.data else None,
            "url": self.url,
            "type": self.type,
            "row": self.row,
            "col": self.col,
        }

    def __repr__(self) -> str:
        attrs = [f"text={self.text!r}"]
        if self.data:
            attrs.append(f"data={self.data_str!r}")
        if self.url:
            attrs.append(f"url={self.url!r}")
        attrs.append(f"pos=({self.row}, {self.col})")
        return f"MessageButton({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)


@dataclass(frozen=True, slots=True)
class OtherMessage(Serializable):
    """Auxiliary message reference identifier."""

    date: int
    message_id: int | str
    seq: int | None = None


@dataclass(slots=True)
class Message(Serializable):
    """Represents a message sent or received in Bale."""

    rid: int | str
    date: int
    author: User
    chat: Chat
    text: str | None = None
    caption: str | None = None
    gift: GiftPacket | None = None
    replied_to: Message | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)
    _matches: Any = field(default=None, repr=False, compare=False)
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def matches(self) -> Any:
        return self._matches

    @matches.setter
    def matches(self, value: Any) -> None:
        self._matches = value

    @property
    def id(self) -> str:
        """Standard combined message identifier ('rid|date')."""
        return f"{self.rid}|{self.date}"

    @property
    def message_id(self) -> int | str:
        """Numeric or raw rid of the message."""
        return self.rid

    @property
    def sender_id(self) -> int:
        """User ID of the author."""
        return self.author.id

    @property
    def from_user(self) -> User:
        """Alias for :attr:`author` for Pyrogram / aiogram parity."""
        return self.author

    @property
    def reply_to_message(self) -> Message | None:
        """Alias for :attr:`replied_to`."""
        return self.replied_to

    @property
    def reply_to_message_id(self) -> int | str | None:
        """ID of the message this message replies to, if any."""
        return self.replied_to.message_id if self.replied_to else None

    @property
    def is_reply(self) -> bool:
        """Whether this message is a reply to another message."""
        return self.replied_to is not None

    @property
    def is_outgoing(self) -> bool:
        """Whether this message was sent by the currently connected account."""
        if self._client is None or self._client.user is None:
            return False
        own_id = self._client.user.id
        if self.author.id == own_id:
            return True
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
        """Message text or caption."""
        return self.text or self.caption or ""

    @property
    def command(self) -> str | None:
        """Bot command name if message text starts with '/'."""
        txt = self.content.strip()
        if txt.startswith("/"):
            parts = txt[1:].split(None, 1)
            cmd = parts[0].split("@", 1)[0]
            return cmd
        return None

    @property
    def command_args(self) -> str | None:
        """Arguments string after the command, if any."""
        txt = self.content.strip()
        if txt.startswith("/"):
            parts = txt.split(None, 1)
            return parts[1] if len(parts) > 1 else ""
        return None

    @property
    def photo(self) -> Photo | None:
        """Photo media attachment if present."""
        doc = (self.raw.get("message") or {}).get("document_message")
        if doc and str(doc.get("mime_type", "")).startswith("image/"):
            p = Photo(
                file_id=doc.get("file_id", 0),
                access_hash=doc.get("access_hash", 0),
                file_size=doc.get("file_size", 0),
                mime_type=doc.get("mime_type", ""),
            )
            if self._client:
                p.bind(self._client)
            return p
        return None

    @property
    def document(self) -> Document | None:
        """Document media attachment if present."""
        doc = (self.raw.get("message") or {}).get("document_message")
        if doc and not str(doc.get("mime_type", "")).startswith("image/"):
            d = Document(
                file_id=doc.get("file_id", 0),
                access_hash=doc.get("access_hash", 0),
                file_size=doc.get("file_size", 0),
                mime_type=doc.get("mime_type", ""),
                file_name=(doc.get("caption") or {}).get("text"),
            )
            if self._client:
                d.bind(self._client)
            return d
        return None

    @property
    def video(self) -> Video | None:
        """Video media attachment if present."""
        doc = (self.raw.get("message") or {}).get("document_message")
        if doc and str(doc.get("mime_type", "")).startswith("video/"):
            v = Video(
                file_id=doc.get("file_id", 0),
                access_hash=doc.get("access_hash", 0),
                file_size=doc.get("file_size", 0),
                mime_type=doc.get("mime_type", ""),
            )
            if self._client:
                v.bind(self._client)
            return v
        return None

    @property
    def voice(self) -> Voice | None:
        """Voice note media attachment if present."""
        content = self.raw.get("message") or {}
        doc = content.get("document_message")
        if doc and "audio/ogg" in str(doc.get("mime_type", "")):
            vo = Voice(
                file_id=doc.get("file_id", 0),
                access_hash=doc.get("access_hash", 0),
                file_size=doc.get("file_size", 0),
                mime_type=doc.get("mime_type", ""),
            )
            if self._client:
                vo.bind(self._client)
            return vo
        return None

    @property
    def audio(self) -> Audio | None:
        """Audio / Music media attachment if present."""
        doc = (self.raw.get("message") or {}).get("document_message")
        if doc and str(doc.get("mime_type", "")).startswith("audio/"):
            au = Audio(
                file_id=doc.get("file_id", 0),
                access_hash=doc.get("access_hash", 0),
                file_size=doc.get("file_size", 0),
                mime_type=doc.get("mime_type", ""),
            )
            if self._client:
                au.bind(self._client)
            return au
        return None

    @property
    def sticker(self) -> Sticker | None:
        """Sticker media attachment if present."""
        content = self.raw.get("message") or {}
        st = content.get("sticker_message") or content.get("sticker")
        if st:
            s = Sticker(
                file_id=st.get("file_id", 0),
                access_hash=st.get("access_hash", 0),
                file_size=st.get("file_size", 0),
                emoji=(st.get("emoji") or {}).get("value"),
            )
            if self._client:
                s.bind(self._client)
            return s
        return None

    @property
    def location(self) -> Location | None:
        """Geographical location if attached."""
        content = self.raw.get("message") or {}
        loc = content.get("location_message") or content.get("location")
        if loc:
            return Location(
                latitude=float(loc.get("latitude", 0.0)),
                longitude=float(loc.get("longitude", 0.0)),
            )
        return None

    @property
    def contact(self) -> Contact | None:
        """Contact card if attached."""
        content = self.raw.get("message") or {}
        cnt = content.get("contact_message") or content.get("contact")
        if cnt:
            return Contact(
                phone_number=str(cnt.get("phone_number", "")),
                first_name=str(cnt.get("name") or cnt.get("first_name", "")),
                user_id=cnt.get("user_id"),
            )
        return None

    @property
    def poll(self) -> Poll | None:
        """Poll attachment if present."""
        content = self.raw.get("message") or {}
        p = content.get("poll_message") or content.get("poll")
        if p:
            options: list[PollOption] = []
            for opt in p.get("options", []):
                options.append(
                    PollOption(
                        text=opt.get("text", ""),
                        voter_count=int(opt.get("voter_count", 0)),
                    )
                )
            return Poll(
                id=int(p.get("poll_id", 0)),
                question=p.get("question", ""),
                options=options,
                total_voter_count=int(p.get("total_voters", 0)),
                is_closed=bool(p.get("is_closed", False)),
            )
        return None

    @property
    def media(
        self,
    ) -> (
        Photo
        | Video
        | Voice
        | Audio
        | Document
        | Sticker
        | Location
        | Contact
        | Poll
        | None
    ):
        """Return whichever media attachment is present in the message."""
        return (
            self.photo
            or self.video
            or self.voice
            or self.audio
            or self.document
            or self.sticker
            or self.location
            or self.contact
            or self.poll
        )

    @property
    def buttons(self) -> list[list[MessageButton]]:
        """Parsed 2D matrix of interactive message buttons."""
        content = self.raw.get("message") or {}
        markup = (
            (content.get("text_message") or {}).get("reply_markup")
            or (content.get("document_message") or {}).get("reply_markup")
            or self.raw.get("reply_markup")
            or {}
        )
        inline_markup = markup.get("inline_keyboard_markup") or {}
        rows = inline_markup.get("list_of_inline_list") or []
        parsed: list[list[MessageButton]] = []
        for r_idx, row in enumerate(rows):
            cur_row: list[MessageButton] = []
            buttons = row.get("inline_list") or []
            for c_idx, btn in enumerate(buttons):
                cb_data = (btn.get("callback_data") or {}).get("value")
                url = (btn.get("url") or {}).get("value")
                cur_row.append(
                    MessageButton(
                        text=btn.get("text", ""),
                        data=cb_data,
                        url=url,
                        row=r_idx,
                        col=c_idx,
                        message=self,
                        raw=btn,
                    )
                )
            if cur_row:
                parsed.append(cur_row)
        return parsed

    def bind(self, client: Client) -> Message:
        """Bind this message and its nested chat/author to an active client."""
        self._client = client
        self.author.bind(client)
        self.chat.bind(client)
        if self.replied_to:
            self.replied_to.bind(client)
        return self

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Message is not bound to a client")
        return self._client

    async def answer(self, text: str, *, reply_markup: Any = None) -> Message:
        """Send a new message to the same chat."""
        return await self._require_client().send_message(
            self.chat.id, text, reply_markup=reply_markup
        )

    respond = answer

    async def reply(self, text: str, *, reply_markup: Any = None) -> Message:
        """Reply directly to this message."""
        return await self._require_client().send_message(
            self.chat.id, text, self, reply_markup=reply_markup
        )

    async def reply_photo(
        self, photo: Any, caption: str = "", **kwargs: Any
    ) -> Message:
        """Reply to this message with a photo."""
        return await self._require_client().send_photo(
            self.chat.id, photo, caption=caption, reply_to=self, **kwargs
        )

    async def reply_document(
        self, document: Any, caption: str = "", **kwargs: Any
    ) -> Message:
        """Reply to this message with a document or file."""
        return await self._require_client().send_document(
            self.chat.id, document, caption=caption, reply_to=self, **kwargs
        )

    async def reply_voice(
        self, voice: Any, duration: int = 0, **kwargs: Any
    ) -> Message:
        """Reply to this message with a voice note."""
        return await self._require_client().send_voice(
            self.chat.id, voice, duration=duration, reply_to=self, **kwargs
        )

    async def reply_video(
        self, video: Any, caption: str = "", **kwargs: Any
    ) -> Message:
        """Reply to this message with a video."""
        return await self._require_client().send_video(
            self.chat.id, video, caption=caption, reply_to=self, **kwargs
        )

    async def reply_audio(
        self, audio: Any, caption: str = "", **kwargs: Any
    ) -> Message:
        """Reply to this message with an audio file."""
        return await self._require_client().send_audio(
            self.chat.id, audio, caption=caption, reply_to=self, **kwargs
        )

    async def reply_sticker(self, sticker: Any, **kwargs: Any) -> Message:
        """Reply to this message with a sticker."""
        return await self._require_client().send_sticker(
            self.chat.id, sticker, reply_to=self, **kwargs
        )

    async def edit_text(self, text: str) -> DefaultResponse:
        """Edit the text content of this message."""
        return await self._require_client().edit_message_text(
            self.chat.id, self.id, text
        )

    edit = edit_text

    async def delete(self, just_me: bool = False) -> DefaultResponse:
        """Delete this message."""
        return await self._require_client().delete_message(
            self.chat.id, self.id, just_me
        )

    async def seen(self) -> DefaultResponse:
        """Mark this message as read."""
        return await self._require_client().mark_as_read(self.chat.id, self.date)

    read = seen
    mark_as_read = seen

    async def download(self) -> bytes:
        """Download media file attached to this message."""
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

    async def react(self, code: str = "👍") -> dict[str, Any]:
        """Add an emoji reaction to this message."""
        return await self._require_client().message_set_reaction(
            self.chat.id, self.id, code
        )

    async def remove_reaction(self, code: str) -> dict[str, Any]:
        """Remove an emoji reaction from this message."""
        return await self._require_client().message_remove_reaction(
            self.chat.id, self.id, code
        )

    async def click(self, data: str) -> dict[str, Any]:
        """Trigger an inline callback using data from a message button."""
        return await self._require_client().click_inline_button(
            self.chat.id, self.id, data
        )

    async def forward(self, chat_id: str | int | Chat | User) -> DefaultResponse:
        """Forward this message to another chat."""
        target_id: str = (
            str(chat_id.id) if isinstance(chat_id, (Chat, User)) else str(chat_id)
        )
        return await self._require_client().forward_message(
            target_id, self.chat.id, self.id
        )

    async def copy(self, chat_id: str | int | Chat | User) -> Message:
        """Copy this message and send it to another chat."""
        target_id: str = (
            str(chat_id.id) if isinstance(chat_id, (Chat, User)) else str(chat_id)
        )
        return await self._require_client().copy_message(
            target_id, self.chat.id, self.id
        )

    async def open_gift(self, receiver_token: str | None = None) -> PacketResponse:
        return await self._require_client().open_gift(self, receiver_token)

    open_packet = open_gift

    async def report(
        self, reason: str | None = None, kind: ReportKind = ReportKind.SPAM
    ) -> DefaultResponse:
        return await self._require_client().report_message(
            self.chat.id, self, reason, kind
        )

    def get_fsm_context(self) -> Any:
        return self._require_client().get_fsm_context(self.chat.id, self.author.id)

    def __repr__(self) -> str:
        attrs = [
            f"id={self.id!r}",
            f"chat={self.chat!r}",
            f"from_user={self.author!r}",
        ]
        if self.text:
            attrs.append(f"text={self.text!r}")
        elif self.caption:
            attrs.append(f"caption={self.caption!r}")
        if self.buttons:
            attrs.append(f"buttons={self.buttons!r}")
        return f"Message({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)
