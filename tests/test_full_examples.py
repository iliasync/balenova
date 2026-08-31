from __future__ import annotations

import io
import shutil
import wave
from datetime import datetime
from types import SimpleNamespace

import pytest

from balenova import BaleRpcError
from examples.broadcast_manager import app as broadcast_app
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


class FakeGroupClient(FakeBroadcastClient):
    def __init__(self) -> None:
        super().__init__()
        self.checked: list[str] = []

    async def load_dialogs(self, *, limit: int, min_date: int):
        assert limit == 40
        assert min_date == -1
        return {
            "dialogs": [
                {"peer": {"id": 1, "type": 2}, "sort_date": 30},
                {"peer": {"id": 2, "type": 5}, "sort_date": 20},
                {"peer": {"id": 3, "type": 2}, "sort_date": 10},
            ]
        }

    async def get_full_group(self, chat_id: str):
        self.checked.append(chat_id)
        return {
            "is_member": {"value": chat_id != "3|2"},
            "permissions": {"send_message": chat_id != "2|5"},
        }

    async def get_group_preview(self, link: str):
        assert link == "https://ble.ir/join/allowed"
        return {
            "group": {
                "id": 99,
                "group_type": "GROUP_TYPE_SUPER_GROUP",
                "is_member": {"value": True},
                "permissions": {"send_message": True},
            }
        }


class FakeDirectGroupClient(FakeBroadcastClient):
    def __init__(self) -> None:
        super().__init__()
        self.bulk_calls = 0

    async def get_my_groups(self):
        self.bulk_calls += 1
        return [
            SimpleNamespace(
                id="1|2", peer_type=2, can_send_message=True, permissions={}
            ),
            SimpleNamespace(
                id="2|5",
                peer_type=5,
                can_send_message=False,
                permissions={"send_message": True},
            ),
            SimpleNamespace(
                id="3|3",
                peer_type=3,
                can_send_message=True,
                permissions={"send_message": True},
            ),
            SimpleNamespace(
                id="4|2", peer_type=2, can_send_message=False, permissions={}
            ),
        ]


class RateLimitedClient(FakeBroadcastClient):
    def __init__(self) -> None:
        super().__init__()
        self.attempts = 0

    async def send(self, chat_id: str, text: str) -> None:
        self.attempts += 1
        if self.attempts == 1:
            raise BaleRpcError(8, "user_rate_limited retry_after 1")
        await super().send(chat_id, text)


class FakeVoiceClient:
    async def get_call_wss_url(self, call_id: int) -> str:
        return f"wss://call.example/{call_id}"


class FakePanelMessage:
    def __init__(self, text: str) -> None:
        self.text = text
        self.chat = SimpleNamespace(id="88|2")
        self.rid = -123
        self.date = 1_788_193_482_819
        self.is_outgoing = False
        self.edits: list[str] = []
        self.answers: list[str] = []

    @property
    def id(self) -> str:
        return f"{self.rid}|{self.date}"

    async def edit_text(self, text: str) -> None:
        self.edits.append(text)
        self.text = text

    async def answer(self, text: str) -> None:
        self.answers.append(text)


class FakeRawPanelClient:
    def __init__(self, message: FakePanelMessage) -> None:
        self.message = message

    def _wrap_message(self, payload):
        return self.message


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
    assert restored.interval_minutes == 60
    assert as_positive_int("10", minimum=10, maximum=600) == 10
    assert as_positive_int("1", minimum=1, maximum=60) == 1
    assert as_positive_int("60", minimum=1, maximum=60) == 60
    with pytest.raises(ValueError):
        as_positive_int("61", minimum=1, maximum=60)
    with pytest.raises(ValueError):
        as_positive_int("9", minimum=10, maximum=600)
    assert parse_time("09:05") == "09:05"


def test_group_links_are_extracted_line_by_line_and_deduplicated() -> None:
    assert broadcast_app.extract_group_links(
        "https://ble.ir/join/first\nble.ir/join/second\n"
        "https://ble.ir/join/first\nمتن اضافی"
    ) == [
        "https://ble.ir/join/first",
        "ble.ir/join/second",
    ]


def test_panel_checkbox_state_is_parsed_from_bale_list() -> None:
    assert broadcast_app.parse_panel_options(
        "پنل تبچی BaleNova\n\n"
        "- [x] ارسال زمان‌بندی‌شده\n"
        "- [ ] تلاش مجدد هنگام محدودیت\n"
        "- [X] نمایش پیشرفت اسکن\n\n"
        "آخرین تغییرات:\n• متن قدیمی"
    ) == {
        "enabled": True,
        "retry_rate_limits": False,
        "show_scan_progress": True,
    }


@pytest.mark.asyncio
async def test_senderless_click_on_remembered_panel_updates_and_reedits(
    tmp_path, monkeypatch
) -> None:
    panel_scheduler = BroadcastScheduler(  # type: ignore[arg-type]
        FakeBroadcastClient(), SettingsStore(tmp_path / "panel.json")
    )
    monkeypatch.setattr(broadcast_app, "scheduler", panel_scheduler)
    message = FakePanelMessage(
        "پنل تبچی BaleNova\n\n"
        "- [ ] ارسال زمان‌بندی‌شده\n"
        "- [ ] تلاش مجدد هنگام محدودیت\n"
        "- [x] نمایش پیشرفت اسکن"
    )
    broadcast_app.remember_panel(message)  # type: ignore[arg-type]

    await broadcast_app.command(message)  # type: ignore[arg-type]

    assert panel_scheduler.settings.retry_rate_limits is False
    assert len(message.edits) == 1
    assert "آخرین تغییرات:" in message.edits[0]
    assert "تلاش مجدد هنگام محدودیت خاموش شد" in message.edits[0]
    assert panel_scheduler.store.load().panel_message_keys == ["88|2#-123"]

    # The update caused by the program's own edit must not loop.
    await broadcast_app.command(message)  # type: ignore[arg-type]
    assert len(message.edits) == 1


@pytest.mark.asyncio
async def test_raw_websocket_panel_update_is_applied_without_polling(
    tmp_path, monkeypatch
) -> None:
    message = FakePanelMessage(broadcast_app.PANEL_HEADER)
    panel_scheduler = BroadcastScheduler(  # type: ignore[arg-type]
        FakeBroadcastClient(), SettingsStore(tmp_path / "panel-raw.json")
    )
    monkeypatch.setattr(broadcast_app, "scheduler", panel_scheduler)
    broadcast_app.remember_panel(message)  # type: ignore[arg-type]
    clicked_text = (
        "پنل تبچی BaleNova\n\n"
        "- [ ] ارسال زمان‌بندی‌شده\n"
        "- [ ] تلاش مجدد هنگام محدودیت\n"
        "- [x] نمایش پیشرفت اسکن"
    )

    await broadcast_app.raw_panel_update(
        {
            "update": {
                "composed_update": {
                    "message": {"message": {"text_message": {"text": clicked_text}}}
                }
            }
        },
        FakeRawPanelClient(message),  # type: ignore[arg-type]
    )

    assert panel_scheduler.settings.retry_rate_limits is False
    assert "آخرین تغییرات:" in message.edits[-1]


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
async def test_group_scan_uses_membership_and_send_permission(tmp_path) -> None:
    client = FakeGroupClient()
    scheduler = BroadcastScheduler(  # type: ignore[arg-type]
        client, SettingsStore(tmp_path / "settings.json")
    )
    scheduler.settings.scan_gap_seconds = 0

    assert await scheduler.eligible_groups() == ["1|2"]
    assert client.checked == ["1|2", "2|5", "3|2"]
    assert scheduler.store.load().group_ids == ["1|2"]


@pytest.mark.asyncio
async def test_group_scan_prefers_bulk_membership_and_permission_flags(
    tmp_path,
) -> None:
    client = FakeDirectGroupClient()
    scheduler = BroadcastScheduler(  # type: ignore[arg-type]
        client, SettingsStore(tmp_path / "settings.json")
    )

    assert await scheduler.eligible_groups() == ["1|2", "2|5"]
    assert client.bulk_calls == 1
    assert scheduler.store.load().group_ids == ["1|2", "2|5"]


@pytest.mark.asyncio
async def test_group_link_uses_preview_membership_and_send_permission(tmp_path) -> None:
    client = FakeGroupClient()
    scheduler = BroadcastScheduler(  # type: ignore[arg-type]
        client, SettingsStore(tmp_path / "settings.json")
    )
    scheduler.settings.scan_gap_seconds = 0

    assert await scheduler.group_from_link(
        "https://ble.ir/join/allowed"
    ) == "99|5"


@pytest.mark.asyncio
async def test_broadcast_retries_temporary_rate_limit(tmp_path, monkeypatch) -> None:
    client = RateLimitedClient()
    scheduler = BroadcastScheduler(  # type: ignore[arg-type]
        client, SettingsStore(tmp_path / "settings.json")
    )
    scheduler.settings.banner_text = "hello"
    scheduler.settings.group_ids = ["1|2"]

    async def no_sleep(_seconds: float) -> None:
        return None

    monkeypatch.setattr("examples.broadcast_manager.scheduler.asyncio.sleep", no_sleep)
    assert await scheduler.broadcast() == (1, 0)
    assert client.attempts == 2


@pytest.mark.asyncio
async def test_voice_credentials_accept_wrapped_bale_url() -> None:
    player = VoicePlayer(FakeVoiceClient())  # type: ignore[arg-type]
    player.call_id = 77

    assert await player._credentials(
        {"url": {"text": "wss://voice.example"}, "token": "secret"}
    ) == ("wss://voice.example", "secret")
    assert unwrap({"value": "x"}) == "x"


class FakeCallClient:
    def __init__(self, *, active: bool = False) -> None:
        self.active = active
        self.left: list[tuple[int, bool]] = []

    async def get_group_call(self, _chat_id: str):
        if not self.active:
            return None
        return {"id": 76, "url": {"text": "wss://voice"}, "token": "token"}

    async def start_group_call(self, _chat_id: str):
        return {
            "group_call": {
                "id": 77,
                "url": {"text": "wss://voice"},
                "token": "token",
            }
        }

    async def join_group_call(self, call_id: int, _name: str):
        return {
            "group_call": {
                "id": call_id,
                "url": {"text": "wss://voice"},
                "token": "token",
            }
        }

    async def leave_group_call(self, call_id: int, *, end: bool = False):
        self.left.append((call_id, end))


class FakeAudioSource:
    def __init__(self, *_args, **_kwargs) -> None:
        self.frames: list[object] = []
        self.closed = False

    async def capture_frame(self, frame: object) -> None:
        self.frames.append(frame)

    def clear_queue(self) -> None:
        pass

    async def aclose(self) -> None:
        self.closed = True


class FakeParticipant:
    def __init__(self) -> None:
        self.published: list[tuple[object, object]] = []

    async def publish_track(self, track: object, options: object) -> None:
        self.published.append((track, options))


class FakeRoom:
    fail_connect = False

    def __init__(self) -> None:
        self.local_participant = FakeParticipant()
        self.disconnected = False

    async def connect(self, _url: str, _token: str) -> None:
        if self.fail_connect:
            raise RuntimeError("connect failed")

    async def disconnect(self) -> None:
        self.disconnected = True


class FakeRtc:
    Room = FakeRoom
    AudioSource = FakeAudioSource
    TrackSource = SimpleNamespace(SOURCE_MICROPHONE="microphone")
    LocalAudioTrack = SimpleNamespace(
        create_audio_track=lambda name, source: (name, source)
    )
    TrackPublishOptions = SimpleNamespace
    AudioFrame = SimpleNamespace


@pytest.mark.asyncio
async def test_voice_player_ends_calls_it_started(monkeypatch) -> None:
    client = FakeCallClient()
    player = VoicePlayer(client)  # type: ignore[arg-type]
    monkeypatch.setattr("examples.voice_player.player.load_livekit", lambda: FakeRtc)

    assert await player.join("1|2") == 77
    source = player.source
    await player.leave()

    assert client.left == [(77, True)]
    assert source.closed is True
    assert player.call_id is None


@pytest.mark.asyncio
async def test_voice_player_rolls_back_failed_livekit_connection(monkeypatch) -> None:
    client = FakeCallClient()
    player = VoicePlayer(client)  # type: ignore[arg-type]
    monkeypatch.setattr("examples.voice_player.player.load_livekit", lambda: FakeRtc)
    monkeypatch.setattr(FakeRoom, "fail_connect", True)

    with pytest.raises(RuntimeError, match="connect failed"):
        await player.join("1|2")

    assert client.left == [(77, True)]
    assert player.call_id is None
    assert player.room is None


@pytest.mark.asyncio
@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg is required")
async def test_voice_player_decodes_audio_into_complete_livekit_frames(
    monkeypatch,
) -> None:
    client = FakeCallClient(active=True)
    player = VoicePlayer(client)  # type: ignore[arg-type]
    player.source = FakeAudioSource()
    monkeypatch.setattr("examples.voice_player.player.load_livekit", lambda: FakeRtc)
    pcm = b"\x00\x00" * (VoicePlayer.SAMPLE_RATE // 20)
    encoded = io.BytesIO()
    with wave.open(encoded, "wb") as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(VoicePlayer.SAMPLE_RATE)
        stream.writeframes(pcm)

    await player._play(encoded.getvalue())

    assert len(player.source.frames) == 5
    assert all(
        len(frame.data) == VoicePlayer.FRAME_SAMPLES * 2
        for frame in player.source.frames
    )
