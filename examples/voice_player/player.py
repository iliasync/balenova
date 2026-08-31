from __future__ import annotations

import asyncio
import contextlib
from typing import Any

from balenova import Client


class VoicePlayer:
    SAMPLE_RATE = 48_000
    CHANNELS = 1
    FRAME_SAMPLES = 480

    def __init__(self, client: Client) -> None:
        self.client = client
        self.room: Any = None
        self.source: Any = None
        self.call_id: int | None = None
        self.chat_id: str | None = None
        self.title: str | None = None
        self.last_error: str | None = None
        self._task: asyncio.Task[None] | None = None
        self._resume = asyncio.Event()
        self._resume.set()
        self._stop = asyncio.Event()

    async def join(self, chat_id: str) -> int:
        if self.call_id is not None:
            await self.leave()
        rtc = load_livekit()
        group_call = await self.client.get_group_call(chat_id)
        if group_call is None:
            started = await self.client.start_group_call(chat_id)
            group_call = started.get("group_call")
        if not isinstance(group_call, dict) or not group_call.get("id"):
            raise RuntimeError("تماس فعالی برای این گروه پیدا نشد")

        self.call_id = int(group_call["id"])
        joined = await self.client.join_group_call(self.call_id, "BaleNova Player")
        joined_call = joined.get("group_call")
        if isinstance(joined_call, dict):
            group_call = joined_call
        url, token = await self._credentials(group_call)

        self.room = rtc.Room()
        await self.room.connect(url, token)
        self.source = rtc.AudioSource(
            self.SAMPLE_RATE,
            self.CHANNELS,
            queue_size_ms=100,
        )
        track = rtc.LocalAudioTrack.create_audio_track("BaleNova", self.source)
        options = rtc.TrackPublishOptions(source=rtc.TrackSource.SOURCE_MICROPHONE)
        await self.room.local_participant.publish_track(track, options)
        self.chat_id = chat_id
        return self.call_id

    async def play(self, data: bytes, title: str = "audio") -> None:
        if self.source is None:
            raise RuntimeError("ابتدا با !vc join وارد تماس شوید")
        await self.stop()
        self.title = title
        self.last_error = None
        self._stop.clear()
        self._resume.set()
        self._task = asyncio.create_task(
            self._play_guarded(data), name="bale-voice-player"
        )

    def pause(self) -> None:
        self._resume.clear()

    def resume(self) -> None:
        self._resume.set()

    async def stop(self) -> None:
        self._stop.set()
        self._resume.set()
        if self._task:
            self._task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self._task
        self._task = None
        self.title = None
        if self.source is not None and hasattr(self.source, "clear_queue"):
            self.source.clear_queue()

    async def leave(self) -> None:
        await self.stop()
        if self.room is not None:
            await self.room.disconnect()
        if self.source is not None and hasattr(self.source, "aclose"):
            await self.source.aclose()
        if self.call_id is not None:
            await self.client.leave_group_call(self.call_id)
        self.room = self.source = None
        self.call_id = None
        self.chat_id = None

    def status(self) -> str:
        if self.call_id is None:
            return "پخش‌کننده داخل تماس نیست."
        state = "در حال پخش" if self._task else "آماده"
        if self._task and not self._resume.is_set():
            state = "مکث"
        error = f"\nخطا: {self.last_error}" if self.last_error else ""
        return f"تماس: {self.call_id}\nوضعیت: {state}\nفایل: {self.title or '-'}{error}"

    async def _credentials(self, group_call: dict[str, Any]) -> tuple[str, str]:
        token = unwrap(group_call.get("token"))
        url = unwrap(group_call.get("url"))
        if not url and self.call_id is not None:
            url = await self.client.get_call_wss_url(self.call_id)
        if not isinstance(url, str) or not url:
            raise RuntimeError("آدرس اتصال صوتی دریافت نشد")
        if not isinstance(token, str) or not token:
            raise RuntimeError("مجوز اتصال صوتی دریافت نشد")
        return url, token

    async def _play_guarded(self, data: bytes) -> None:
        try:
            await self._play(data)
        except asyncio.CancelledError:
            raise
        except Exception as error:
            self.last_error = str(error)
            print(f"پخش ناموفق بود: {error}")
        finally:
            self._task = None
            self.title = None

    async def _play(self, data: bytes) -> None:
        rtc = load_livekit()
        process = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            "pipe:0",
            "-f",
            "s16le",
            "-ar",
            str(self.SAMPLE_RATE),
            "-ac",
            str(self.CHANNELS),
            "pipe:1",
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        assert process.stdin is not None
        assert process.stdout is not None
        assert process.stderr is not None

        async def feed_input() -> None:
            for offset in range(0, len(data), 64 * 1024):
                process.stdin.write(data[offset : offset + 64 * 1024])
                await process.stdin.drain()
            process.stdin.close()

        feed_task = asyncio.create_task(feed_input())
        frame_size = self.FRAME_SAMPLES * self.CHANNELS * 2
        interrupted = False
        try:
            while chunk := await process.stdout.read(frame_size):
                if self._stop.is_set():
                    interrupted = True
                    break
                await self._resume.wait()
                chunk = chunk.ljust(frame_size, b"\0")
                frame = rtc.AudioFrame(
                    data=chunk,
                    sample_rate=self.SAMPLE_RATE,
                    num_channels=self.CHANNELS,
                    samples_per_channel=self.FRAME_SAMPLES,
                )
                await self.source.capture_frame(frame)
        except asyncio.CancelledError:
            interrupted = True
            raise
        finally:
            if interrupted and process.returncode is None:
                process.terminate()
            if interrupted:
                feed_task.cancel()
            with contextlib.suppress(asyncio.CancelledError, BrokenPipeError):
                await feed_task
            await process.wait()
        if process.returncode and not interrupted:
            error = await process.stderr.read()
            raise RuntimeError(error.decode("utf-8", errors="replace"))


def unwrap(value: Any) -> Any:
    return value.get("value") if isinstance(value, dict) else value


def load_livekit() -> Any:
    try:
        from livekit import rtc
    except ImportError as error:
        raise RuntimeError(
            "ابتدا pip install 'balenova[voice]' را اجرا کنید"
        ) from error
    return rtc
