from __future__ import annotations

from datetime import datetime

import pytest

from examples.broadcast_manager.scheduler import (
    BroadcastScheduler,
    as_positive_int,
    parse_time,
)
from examples.broadcast_manager.settings import SettingsStore
from examples.voice_player.player import VoicePlayer, unwrap


class FakeBroadcastClient:
    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    async def send(self, chat_id: str, text: str) -> None:
        self.sent.append((chat_id, text))


class FakeVoiceClient:
    async def get_call_wss_url(self, call_id: int) -> str:
        return f"wss://call.example/{call_id}"


def test_broadcast_settings_are_persistent_and_safely_bounded(tmp_path) -> None:
    store = SettingsStore(tmp_path / "settings.json")
    settings = store.load()
    settings.banner_text = "hello"
    settings.group_ids = ["1|2"]
    settings.gap_seconds = 20
    store.save(settings)

    restored = store.load()
    assert restored.banner_text == "hello"
    assert restored.group_ids == ["1|2"]
    assert restored.gap_seconds == 20
    assert as_positive_int("10", minimum=10, maximum=600) == 10
    with pytest.raises(ValueError):
        as_positive_int("9", minimum=10, maximum=600)
    assert parse_time("09:05") == "09:05"


@pytest.mark.asyncio
async def test_broadcast_scheduler_sends_configured_banner(tmp_path) -> None:
    client = FakeBroadcastClient()
    scheduler = BroadcastScheduler(  # type: ignore[arg-type]
        client, SettingsStore(tmp_path / "settings.json")
    )
    scheduler.settings.banner_text = "approved announcement"
    scheduler.settings.group_ids = ["1|2"]

    assert await scheduler.broadcast() == (1, 0)
    assert client.sent == [("1|2", "approved announcement")]

    next_run = scheduler.schedule_next(datetime(2026, 8, 31, 10, 0))
    assert next_run == datetime(2026, 8, 31, 11, 0)


@pytest.mark.asyncio
async def test_voice_credentials_accept_wrapped_bale_url() -> None:
    player = VoicePlayer(FakeVoiceClient())  # type: ignore[arg-type]
    player.call_id = 77

    assert await player._credentials(
        {"url": {"value": "wss://voice.example"}, "token": "secret"}
    ) == ("wss://voice.example", "secret")
    assert unwrap({"value": "x"}) == "x"
