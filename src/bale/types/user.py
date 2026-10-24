"""High-level User type for Bale."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from bale.errors import ClientStateError
from bale.types.base import Serializable

if TYPE_CHECKING:
    from bale.client import Client
    from bale.types.message import Message


@dataclass(slots=True)
class User(Serializable):
    """Represents a user account or bot in Bale."""

    id: int
    username: str | None = None
    name: str | None = None
    is_bot: bool = False
    _is_self: bool = field(default=False, repr=False, compare=False)
    _phone: str | None = field(default=None, repr=False, compare=False)
    _client: Client | None = field(default=None, repr=False, compare=False)

    @property
    def is_self(self) -> bool:
        """Whether this user is the currently logged-in account."""
        if self._is_self:
            return True
        if self._client and self._client.user:
            return self._client.user.id == self.id
        return False

    @is_self.setter
    def is_self(self, value: bool) -> None:
        self._is_self = value

    @property
    def phone(self) -> str | None:
        return self._phone

    @phone.setter
    def phone(self, value: str | None) -> None:
        self._phone = value

    @property
    def full_name(self) -> str:
        """Returns the user's display name."""
        return self.name or ""

    @property
    def first_name(self) -> str:
        """First name extracted from full name."""
        if not self.name:
            return ""
        parts = self.name.split(None, 1)
        return parts[0] if parts else ""

    @property
    def last_name(self) -> str | None:
        """Last name extracted from full name if present."""
        if not self.name:
            return None
        parts = self.name.split(None, 1)
        return parts[1] if len(parts) > 1 else None

    @property
    def mention(self) -> str:
        """Mention tag for the user (@username or markdown link)."""
        if self.username:
            return f"@{self.username}"
        return f"[{self.full_name or self.id}](bale://user?id={self.id})"

    def bind(self, client: Client) -> User:
        """Bind this User instance to an active Client session."""
        self._client = client
        return self

    def _require_client(self) -> Client:
        if self._client is None:
            raise ClientStateError("User is not bound to a client")
        return self._client

    async def send_message(self, text: str, **kwargs: Any) -> Message:
        """Send a direct message to this user."""
        return await self._require_client().send_message(str(self.id), text, **kwargs)

    async def block(self) -> Any:
        """Block this user."""
        return await self._require_client().block_user(self.id)

    async def unblock(self) -> Any:
        """Unblock this user."""
        return await self._require_client().unblock_user(self.id)

    def __repr__(self) -> str:
        attrs = [f"id={self.id}"]
        if self.name:
            attrs.append(f"name={self.name!r}")
        if self.username:
            attrs.append(f"username={self.username!r}")
        if self.is_bot:
            attrs.append("is_bot=True")
        return f"User({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)
