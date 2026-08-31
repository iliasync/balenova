"""Session parsing and durable storage."""

from __future__ import annotations

import asyncio
import contextlib
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path

from bale.errors import AuthenticationError

_SESSION_PATTERN = re.compile(r"^(?P<user_id>\d+):(?P<jwt>.+)$", re.DOTALL)


@dataclass(frozen=True, slots=True)
class Session:
    user_id: int
    jwt: str

    @classmethod
    def parse(cls, value: str) -> Session:
        match = _SESSION_PATTERN.fullmatch(value.strip())
        if match is None:
            raise AuthenticationError("Invalid session; expected '<user_id>:<jwt>'")
        return cls(int(match.group("user_id")), match.group("jwt"))

    def __str__(self) -> str:
        return f"{self.user_id}:{self.jwt}"


class SessionStorage:
    def __init__(self, directory: str | Path, name: str) -> None:
        safe_name = re.sub(r"[^A-Za-z0-9_.-]", "_", name).strip("._")
        self.path = Path(directory).expanduser() / f"{safe_name or 'bale'}.session"

    async def load(self) -> Session | None:
        def read() -> Session | None:
            try:
                return Session.parse(self.path.read_text(encoding="utf-8"))
            except FileNotFoundError:
                return None

        return await asyncio.to_thread(read)

    async def save(self, session: Session) -> None:
        def write() -> None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            descriptor, temporary = tempfile.mkstemp(
                dir=self.path.parent, prefix=f".{self.path.name}.", text=True
            )
            try:
                os.fchmod(descriptor, 0o600)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    stream.write(str(session))
                os.replace(temporary, self.path)
            except BaseException:
                with contextlib.suppress(FileNotFoundError):
                    os.unlink(temporary)
                raise

        await asyncio.to_thread(write)

    async def delete(self) -> None:
        def remove() -> None:
            with contextlib.suppress(FileNotFoundError):
                self.path.unlink()

        await asyncio.to_thread(remove)
