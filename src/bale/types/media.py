"""Media objects attached to Bale messages."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from bale.errors import ClientStateError
from bale.types.base import Serializable

if TYPE_CHECKING:
    from bale.client import Client


@dataclass(slots=True)
class Media(Serializable):
    """Base class for media attachments."""

    file_id: int | str = 0
    access_hash: int = 0
    file_size: int = 0
    mime_type: str = ""
    _client: Client | None = field(default=None, repr=False, compare=False)

    def bind(self, client: Client) -> Media:
        self._client = client
        return self

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("Media object is not bound to a client")
        return self._client

    async def download(self) -> bytes:
        """Download media file bytes."""
        return await self._require_client().download_file(
            self.file_id, self.access_hash
        )


@dataclass(slots=True)
class Photo(Media):
    """Represents a photo attachment."""

    width: int = 0
    height: int = 0
    thumb: bytes | None = None

    def __repr__(self) -> str:
        return (
            f"Photo(file_id={self.file_id}, width={self.width}, "
            f"height={self.height}, size={self.file_size})"
        )


@dataclass(slots=True)
class Video(Media):
    """Represents a video attachment."""

    duration: int = 0
    width: int = 0
    height: int = 0

    def __repr__(self) -> str:
        return (
            f"Video(file_id={self.file_id}, duration={self.duration}s, "
            f"width={self.width}, height={self.height})"
        )


@dataclass(slots=True)
class Voice(Media):
    """Represents a voice message attachment."""

    duration: int = 0

    def __repr__(self) -> str:
        return f"Voice(file_id={self.file_id}, duration={self.duration}s)"


@dataclass(slots=True)
class Audio(Media):
    """Represents an audio / music attachment."""

    duration: int = 0
    title: str | None = None
    performer: str | None = None

    def __repr__(self) -> str:
        attrs = [f"file_id={self.file_id}", f"duration={self.duration}s"]
        if self.title:
            attrs.append(f"title={self.title!r}")
        if self.performer:
            attrs.append(f"performer={self.performer!r}")
        return f"Audio({', '.join(attrs)})"


@dataclass(slots=True)
class Document(Media):
    """Represents a general document or file attachment."""

    file_name: str | None = None

    def __repr__(self) -> str:
        attrs = [f"file_id={self.file_id}"]
        if self.file_name:
            attrs.append(f"file_name={self.file_name!r}")
        attrs.append(f"size={self.file_size}")
        return f"Document({', '.join(attrs)})"


@dataclass(slots=True)
class Sticker(Media):
    """Represents a sticker attachment."""

    width: int = 0
    height: int = 0
    emoji: str | None = None

    def __repr__(self) -> str:
        attrs = [f"file_id={self.file_id}"]
        if self.emoji:
            attrs.append(f"emoji={self.emoji!r}")
        return f"Sticker({', '.join(attrs)})"


@dataclass(slots=True)
class PollOption(Serializable):
    """Represents an individual option in a poll."""

    text: str
    voter_count: int = 0

    def __repr__(self) -> str:
        return f"PollOption(text={self.text!r}, votes={self.voter_count})"


@dataclass(slots=True)
class Poll(Serializable):
    """Represents a poll attachment."""

    id: int
    question: str
    options: list[PollOption] = field(default_factory=list)
    total_voter_count: int = 0
    is_closed: bool = False
    is_anonymous: bool = True
    multiple_choice: bool = False

    def __repr__(self) -> str:
        return (
            f"Poll(id={self.id}, question={self.question!r}, "
            f"total_votes={self.total_voter_count}, is_closed={self.is_closed})"
        )


@dataclass(slots=True)
class Location(Serializable):
    """Represents a geographical location."""

    latitude: float
    longitude: float

    def __repr__(self) -> str:
        return f"Location(lat={self.latitude}, lng={self.longitude})"


@dataclass(slots=True)
class Contact(Serializable):
    """Represents a phone contact."""

    phone_number: str
    first_name: str
    last_name: str | None = None
    user_id: int | None = None

    def __repr__(self) -> str:
        attrs = [f"phone={self.phone_number!r}", f"first_name={self.first_name!r}"]
        if self.last_name:
            attrs.append(f"last_name={self.last_name!r}")
        if self.user_id:
            attrs.append(f"user_id={self.user_id}")
        return f"Contact({', '.join(attrs)})"
