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

    @classmethod
    def from_firefox(cls, profile_path: str | Path | None = None) -> Session:
        """Extract active Bale session from local Firefox cookies."""
        import base64
        import glob
        import json
        import shutil
        import sqlite3

        cookie_paths: list[Path] = []
        if profile_path is not None:
            p = Path(profile_path).expanduser()
            if p.is_file() and p.name == "cookies.sqlite":
                cookie_paths.append(p)
            elif p.is_dir():
                found_in_dir = list(p.glob("cookies.sqlite")) or list(
                    p.glob("**/cookies.sqlite")
                )
                cookie_paths.extend(found_in_dir)
        else:
            search_patterns = [
                "~/.mozilla/firefox/*/cookies.sqlite",
                "~/snap/firefox/common/.mozilla/firefox/*/cookies.sqlite",
                "~/.var/app/org.mozilla.firefox/.mozilla/firefox/*/cookies.sqlite",
                "~/Library/Application Support/Firefox/Profiles/*/cookies.sqlite",
            ]
            appdata = os.environ.get("APPDATA")
            if appdata:
                search_patterns.append(
                    os.path.join(
                        appdata, "Mozilla", "Firefox", "Profiles", "*", "cookies.sqlite"
                    )
                )
            for pat in search_patterns:
                for match in glob.glob(os.path.expanduser(pat)):
                    cookie_paths.append(Path(match))

        for cookie_db in cookie_paths:
            if not cookie_db.exists():
                continue
            try:
                with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as tmp:
                    tmp_path = Path(tmp.name)
                try:
                    shutil.copy2(cookie_db, tmp_path)
                    conn = sqlite3.connect(f"file:{tmp_path}?mode=ro", uri=True)
                    try:
                        cursor = conn.cursor()
                        cursor.execute(
                            "SELECT value FROM moz_cookies "
                            "WHERE host LIKE '%next-ws%' AND name = 'access_token'"
                        )
                        rows = cursor.fetchall()
                    finally:
                        conn.close()
                finally:
                    with contextlib.suppress(FileNotFoundError):
                        tmp_path.unlink()

                for (token,) in rows:
                    if not isinstance(token, str) or "." not in token:
                        continue
                    parts = token.split(".")
                    if len(parts) < 2:
                        continue
                    payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
                    try:
                        payload_data = json.loads(base64.urlsafe_b64decode(payload_b64))
                    except Exception:
                        continue
                    user_id = (
                        payload_data.get("payload", {}).get("user_id")
                        or payload_data.get("user_id")
                        or payload_data.get("uid")
                        or payload_data.get("sub")
                    )
                    if user_id is not None:
                        return cls(int(user_id), token)
            except Exception:
                continue

        raise AuthenticationError("No active Bale session found in Firefox cookies")


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
