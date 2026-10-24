"""Formatting and mention entities for Bale messages."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from bale.enums import MessageEntityType
from bale.types.base import Serializable

if TYPE_CHECKING:
    from bale.types.user import User


@dataclass(frozen=True, slots=True)
class MessageEntity(Serializable):
    """Represents a formatted region (bold, italic, mention, url) in text."""

    type: str | MessageEntityType
    offset: int
    length: int
    url: str | None = None
    user: User | None = None

    def __repr__(self) -> str:
        attrs = [
            f"type={self.type!r}",
            f"offset={self.offset}",
            f"length={self.length}",
        ]
        if self.url:
            attrs.append(f"url={self.url!r}")
        if self.user:
            attrs.append(f"user={self.user!r}")
        return f"MessageEntity({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)
