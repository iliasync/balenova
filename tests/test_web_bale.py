"""Opt-in smoke tests against the real Bale web user-session endpoint.

Run with ``BALE_SESSION='<user_id>:<jwt>' pytest -q tests/test_web_bale.py``.
The test is skipped by default so normal CI never needs a credential.
"""

from __future__ import annotations

import os

import pytest

from bale import Client, User
from bale.proto import response_pb2


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

        group_peers = await client.get_my_group_peers()
        assert isinstance(group_peers, list)
        groups = await client.load_groups(group_peers[:25])
        assert len(groups) <= 25
        assert all(group.peer_type in {2, 3, 5} for group in groups)

        typed_groups = await client.api.groups.GetMyGroups(mode=0, isOwner=False)
        assert isinstance(typed_groups, response_pb2.WebGetMyGroupsResponse)
        assert len(typed_groups.groups) == len(group_peers)

        parameters = await client.get_parameters()
        assert isinstance(parameters, list)

        upload_limits = await client.get_upload_limits()
        assert upload_limits["upload_limit_bytes"] >= 0

        call_logs = await client.get_call_logs(page=1, limit=1)
        assert isinstance(call_logs.get("call_logs", []), list)

        ongoing_calls = await client.get_ongoing_calls(page=1, limit=1)
        assert isinstance(ongoing_calls, list)
        if ongoing_calls:
            call_id = ongoing_calls[0].get("call_id", {}).get("value")
            if call_id:
                assert await client.get_call_state(call_id) is not None
                assert await client.get_call_wss_url(call_id)
    finally:
        await client.close()
