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
        """Extract active Bale session from local Firefox cookies across platforms."""
        import glob

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
            home = os.path.expanduser("~")
            search_patterns = [
                # Linux Native, Snap, Flatpak
                "~/.mozilla/firefox/*/cookies.sqlite",
                "~/snap/firefox/common/.mozilla/firefox/*/cookies.sqlite",
                "~/.var/app/org.mozilla.firefox/.mozilla/firefox/*/cookies.sqlite",
                "~/.librewolf/*/cookies.sqlite",
                "~/.waterfox/*/cookies.sqlite",
                # macOS
                "~/Library/Application Support/Firefox/Profiles/*/cookies.sqlite",
                "~/Library/Application Support/Waterfox/Profiles/*/cookies.sqlite",
                "~/Library/Application Support/LibreWolf/Profiles/*/cookies.sqlite",
                # Android / Termux
                "/data/data/org.mozilla.firefox/files/mozilla/*/cookies.sqlite",
                "/data/data/org.mozilla.fenix/files/mozilla/*/cookies.sqlite",
                "/data/data/org.mozilla.focus/files/mozilla/*/cookies.sqlite",
                "/data/data/com.termux/files/home/.mozilla/firefox/*/cookies.sqlite",
                f"{home}/.mozilla/firefox/*/cookies.sqlite",
            ]
            appdata = os.environ.get("APPDATA")
            if appdata:
                # Windows
                search_patterns.extend(
                    [
                        os.path.join(
                            appdata,
                            "Mozilla",
                            "Firefox",
                            "Profiles",
                            "*",
                            "cookies.sqlite",
                        ),
                        os.path.join(
                            appdata, "Waterfox", "Profiles", "*", "cookies.sqlite"
                        ),
                        os.path.join(
                            appdata, "LibreWolf", "Profiles", "*", "cookies.sqlite"
                        ),
                        os.path.join(
                            appdata, "Floorp", "Profiles", "*", "cookies.sqlite"
                        ),
                    ]
                )
            for pat in search_patterns:
                for match in glob.glob(os.path.expanduser(pat)):
                    cookie_paths.append(Path(match))

        for cookie_db in cookie_paths:
            res = cls._read_sqlite_cookie(
                cookie_db,
                query=(
                    "SELECT value FROM moz_cookies "
                    "WHERE (host LIKE '%next-ws%' OR host LIKE '%bale.ai%') "
                    "AND name = 'access_token'"
                ),
            )
            if res:
                return cls(*res)

        raise AuthenticationError("No active Bale session found in Firefox cookies")

    @classmethod
    def from_chromium(
        cls,
        browser_name: str = "chrome",
        profile_path: str | Path | None = None,
    ) -> Session:
        """Extract active Bale session from Chromium-based browsers across platforms."""
        import glob

        cookie_paths: list[Path] = []
        if profile_path is not None:
            p = Path(profile_path).expanduser()
            if p.is_file():
                cookie_paths.append(p)
            elif p.is_dir():
                found_in_dir = (
                    list(p.glob("Cookies"))
                    or list(p.glob("**/Cookies"))
                    or list(p.glob("**/Network/Cookies"))
                )
                cookie_paths.extend(found_in_dir)
        else:
            home = os.path.expanduser("~")
            appdata = os.environ.get("APPDATA", "")
            localappdata = os.environ.get("LOCALAPPDATA", "")
            search_patterns = [
                # Linux Native
                "~/.config/google-chrome/*/Cookies",
                "~/.config/google-chrome/*/Network/Cookies",
                "~/.config/chromium/*/Cookies",
                "~/.config/chromium/*/Network/Cookies",
                "~/.config/BraveSoftware/Brave-Browser/*/Cookies",
                "~/.config/BraveSoftware/Brave-Browser/*/Network/Cookies",
                "~/.config/microsoft-edge/*/Cookies",
                "~/.config/microsoft-edge/*/Network/Cookies",
                "~/.config/opera/Cookies",
                "~/.config/opera/Network/Cookies",
                "~/.config/vivaldi/*/Cookies",
                "~/.config/vivaldi/*/Network/Cookies",
                "~/.config/yandex-browser/*/Cookies",
                # Linux Flatpak / Snap
                "~/.var/app/com.google.Chrome/config/google-chrome/*/Cookies",
                "~/.var/app/com.google.Chrome/config/google-chrome/*/Network/Cookies",
                "~/.var/app/org.chromium.Chromium/config/chromium/*/Cookies",
                "~/.var/app/com.brave.Browser/config/BraveSoftware/Brave-Browser/*/Cookies",
                "~/.var/app/com.microsoft.Edge/config/microsoft-edge/*/Cookies",
                "~/snap/chromium/common/chromium/*/Cookies",
                "~/snap/brave/common/BraveSoftware/Brave-Browser/*/Cookies",
                # macOS
                "~/Library/Application Support/Google/Chrome/*/Cookies",
                "~/Library/Application Support/Google/Chrome/*/Network/Cookies",
                "~/Library/Application Support/Chromium/*/Cookies",
                "~/Library/Application Support/Chromium/*/Network/Cookies",
                "~/Library/Application Support/BraveSoftware/Brave-Browser/*/Cookies",
                (
                    "~/Library/Application Support/BraveSoftware/Brave-Browser/*"
                    "/Network/Cookies"
                ),
                "~/Library/Application Support/Microsoft Edge/*/Cookies",
                "~/Library/Application Support/Microsoft Edge/*/Network/Cookies",
                "~/Library/Application Support/Arc/User Data/*/Cookies",
                "~/Library/Application Support/Arc/User Data/*/Network/Cookies",
                "~/Library/Application Support/Vivaldi/*/Cookies",
                "~/Library/Application Support/Vivaldi/*/Network/Cookies",
                "~/Library/Application Support/com.operasoftware.Opera/Cookies",
                # Android / Termux
                "/data/data/com.android.chrome/app_chrome/*/Cookies",
                "/data/data/com.android.chrome/app_chrome/Default/Cookies",
                "/data/data/com.brave.browser/app_chrome/*/Cookies",
                "/data/data/com.microsoft.emmx/app_chrome/*/Cookies",
                "/data/data/com.kiwibrowser.browser/app_chrome/*/Cookies",
                "/data/data/com.opera.browser/app_opera/*/Cookies",
                f"{home}/.config/google-chrome/*/Cookies",
            ]
            if localappdata:
                # Windows
                search_patterns.extend(
                    [
                        os.path.join(
                            localappdata,
                            "Google",
                            "Chrome",
                            "User Data",
                            "*",
                            "Network",
                            "Cookies",
                        ),
                        os.path.join(
                            localappdata,
                            "Google",
                            "Chrome",
                            "User Data",
                            "*",
                            "Cookies",
                        ),
                        os.path.join(
                            localappdata,
                            "Microsoft",
                            "Edge",
                            "User Data",
                            "*",
                            "Network",
                            "Cookies",
                        ),
                        os.path.join(
                            localappdata,
                            "BraveSoftware",
                            "Brave-Browser",
                            "User Data",
                            "*",
                            "Network",
                            "Cookies",
                        ),
                        os.path.join(
                            localappdata,
                            "Vivaldi",
                            "User Data",
                            "*",
                            "Network",
                            "Cookies",
                        ),
                        os.path.join(
                            localappdata,
                            "Yandex",
                            "YandexBrowser",
                            "User Data",
                            "*",
                            "Network",
                            "Cookies",
                        ),
                    ]
                )
            if appdata:
                search_patterns.extend(
                    [
                        os.path.join(
                            appdata,
                            "Opera Software",
                            "Opera Stable",
                            "Network",
                            "Cookies",
                        ),
                        os.path.join(
                            appdata,
                            "Opera Software",
                            "Opera GX Stable",
                            "Network",
                            "Cookies",
                        ),
                    ]
                )

            # Filter if specific browser requested
            target = browser_name.strip().casefold()
            for pat in search_patterns:
                if (
                    target not in {"chrome", "chromium", "auto", "all"}
                    and target not in pat.lower()
                ):
                    continue
                for match in glob.glob(os.path.expanduser(pat)):
                    cookie_paths.append(Path(match))

        for cookie_db in cookie_paths:
            res = cls._read_sqlite_cookie(
                cookie_db,
                query=(
                    "SELECT value, encrypted_value FROM cookies "
                    "WHERE (host_key LIKE '%next-ws%' OR host_key LIKE '%bale.ai%') "
                    "AND name = 'access_token'"
                ),
            )
            if res:
                return cls(*res)

        raise AuthenticationError(
            f"No active Bale session found in {browser_name} cookies"
        )

    @classmethod
    def _read_sqlite_cookie(
        cls,
        cookie_db: Path,
        query: str,
    ) -> tuple[int, str] | None:
        """Safely read SQLite cookie database and extract Bale user session."""
        import shutil
        import sqlite3

        if not cookie_db.exists():
            return None

        with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        try:
            shutil.copy2(cookie_db, tmp_path)
            conn = sqlite3.connect(f"file:{tmp_path}?mode=ro", uri=True)
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
            finally:
                conn.close()
        except Exception:
            return None
        finally:
            with contextlib.suppress(FileNotFoundError):
                tmp_path.unlink()

        for row in rows:
            # Handle moz_cookies (value,) or cookies (value, encrypted_value)
            raw_val = row[0] if row else None
            if raw_val and isinstance(raw_val, str) and "." in raw_val:
                session = cls._parse_jwt_session(raw_val)
                if session:
                    return session
            # If value was encrypted in Chromium
            if len(row) > 1 and row[1] and isinstance(row[1], bytes):
                enc = row[1]
                match = re.search(
                    rb"eyJ[a-zA-Z0-9_\-]+\.eyJ[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+",
                    enc,
                )
                if match:
                    token = match.group(0).decode("ascii", errors="ignore")
                    session = cls._parse_jwt_session(token)
                    if session:
                        return session
        return None

    @classmethod
    def _parse_jwt_session(cls, token: str) -> tuple[int, str] | None:
        """Extract user_id and token from JWT access_token."""
        import base64
        import json

        parts = token.split(".")
        if len(parts) < 2:
            return None
        payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
        try:
            payload_data = json.loads(base64.urlsafe_b64decode(payload_b64))
        except Exception:
            return None
        user_id = (
            payload_data.get("payload", {}).get("user_id")
            or payload_data.get("user_id")
            or payload_data.get("uid")
            or payload_data.get("sub")
        )
        if user_id is not None:
            try:
                return int(user_id), token
            except (ValueError, TypeError):
                return None
        return None

    @classmethod
    def from_browser(
        cls,
        browser: str = "auto",
        profile_path: str | Path | None = None,
    ) -> Session:
        """Extract active Bale session from local browsers across all operating systems.

        Supports:
            - Operating Systems: Linux (Native, Snap, Flatpak), Windows,
              macOS, Android (Termux)
            - Browsers: 'auto', 'firefox', 'chrome', 'chromium', 'edge',
              'brave', 'opera', 'vivaldi'

        Examples:
            >>> session = Session.from_browser("auto")
            >>> session = Session.from_browser("firefox")
            >>> session = Session.from_browser("chrome")
        """
        b = browser.strip().casefold()
        if b in {"firefox", "ff", "librewolf", "waterfox"}:
            return cls.from_firefox(profile_path)

        if b in {"chrome", "chromium", "edge", "brave", "opera", "vivaldi", "arc"}:
            return cls.from_chromium(b, profile_path)

        # "auto" or unrecognized: try Firefox first, then Chromium
        errors: list[str] = []
        try:
            return cls.from_firefox(profile_path)
        except AuthenticationError as exc:
            errors.append(f"Firefox: {exc}")

        try:
            return cls.from_chromium("auto", profile_path)
        except AuthenticationError as exc:
            errors.append(f"Chromium: {exc}")

        raise AuthenticationError(
            f"No active Bale session found in browsers (tried: {', '.join(errors)})"
        )


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
