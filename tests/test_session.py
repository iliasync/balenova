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
