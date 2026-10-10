from __future__ import annotations

import os

import pytest

from bale.errors import AuthenticationError
from bale.session import Session, SessionStorage


def test_session_round_trip() -> None:
    session = Session.parse("123:header.payload.signature")
    assert session.user_id == 123
    assert session.jwt == "header.payload.signature"
    assert str(session) == "123:header.payload.signature"


def test_invalid_session_is_rejected() -> None:
    with pytest.raises(AuthenticationError):
        Session.parse("not-a-session")


@pytest.mark.asyncio
async def test_session_storage_is_atomic_private_and_deletable(tmp_path) -> None:
    storage = SessionStorage(tmp_path, "+98 / unsafe")
    session = Session(123, "jwt")

    await storage.save(session)

    assert storage.path.name == "98___unsafe.session"
    assert await storage.load() == session
    assert os.stat(storage.path).st_mode & 0o777 == 0o600

    await storage.delete()
    assert await storage.load() is None


def test_session_from_firefox_mock(tmp_path) -> None:
    import base64
    import json
    import sqlite3

    db_path = tmp_path / "cookies.sqlite"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE moz_cookies "
        "(id INTEGER PRIMARY KEY, host TEXT, name TEXT, value TEXT)"
    )
    payload = json.dumps({"payload": {"user_id": 987654}}).encode()
    b64_payload = base64.urlsafe_b64encode(payload).decode().rstrip("=")
    fake_token = f"fakeheader.{b64_payload}.fakesig"
    c.execute(
        "INSERT INTO moz_cookies (host, name, value) VALUES (?, ?, ?)",
        (".next-ws.bale.ai", "access_token", fake_token),
    )
    conn.commit()
    conn.close()

    session = Session.from_firefox(db_path)
    assert session.user_id == 987654
    assert session.jwt == fake_token
