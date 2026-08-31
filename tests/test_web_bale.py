"""Opt-in smoke tests against the real Bale web user-session endpoint.

Run with ``BALE_SESSION='<user_id>:<jwt>' pytest -q tests/test_web_bale.py``.
The test is skipped by default so normal CI never needs a credential.
"""

from __future__ import annotations

import os

import pytest

from bale import Client, User


@pytest.mark.asyncio
@pytest.mark.skipif(
    not os.getenv("BALE_SESSION"),
    reason="set BALE_SESSION to run the authenticated Bale web smoke test",
)
async def test_real_bale_web_account_session_smoke() -> None:
    session = os.environ["BALE_SESSION"]
    client = Client(
        session,
        websocket_options={"timeout": 15.0, "keepalive_interval": 10.0},
    )
    try:
        await client.connect()
        assert isinstance(client.user, User)
        assert client.user.id == int(session.split(":", 1)[0])

        dialogs = await client.load_dialogs(limit=1)
        assert isinstance(dialogs, dict)
    finally:
        await client.close()
