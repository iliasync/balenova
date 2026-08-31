from __future__ import annotations

import asyncio
from datetime import datetime, timedelta

from balenova import Client

try:
    from .settings import SettingsStore
except ImportError:  # Allows: python examples/broadcast_manager/app.py
    from settings import SettingsStore


class BroadcastScheduler:
    def __init__(self, client: Client, store: SettingsStore) -> None:
        self.client = client
        self.store = store
        self.settings = store.load()
        self._lock = asyncio.Lock()

    async def run(self) -> None:
        while True:
            if self.settings.enabled and self._is_due():
                await self.broadcast()
                self.schedule_next()
            await asyncio.sleep(3)

    async def broadcast(self) -> tuple[int, int]:
        async with self._lock:
            sent = failed = 0
            targets = list(dict.fromkeys(self.settings.group_ids))
            for index, chat_id in enumerate(targets):
                try:
                    if self.settings.banner_message_id:
                        await self.client.copy_message(
                            chat_id,
                            self.settings.banner_chat_id or "",
                            self.settings.banner_message_id,
                        )
                    elif self.settings.banner_text:
                        await self.client.send(chat_id, self.settings.banner_text)
                    else:
                        raise ValueError("No banner is configured")
                    sent += 1
                except Exception as error:
                    failed += 1
                    print(f"ارسال به {chat_id} ناموفق بود: {error}")
                if index + 1 < len(targets):
                    await asyncio.sleep(self.settings.gap_seconds)
            return sent, failed

    async def managed_groups(self, limit: int | None = None) -> list[str]:
        if self.client.user is None:
            return []
        dialogs = await self.client.get_all_dialogs_by_type()
        result: list[str] = []
        for chat in dialogs["groups"]:
            try:
                admins = await self.client.get_chat_administrators(chat.id)
                if any(
                    int(item.get("uid", 0)) == self.client.user.id for item in admins
                ):
                    result.append(chat.id)
                    if limit is not None and len(result) >= limit:
                        break
            except Exception as error:
                print(f"بررسی گروه {chat.id} ناموفق بود: {error}")
            await asyncio.sleep(0.5)
        return result

    async def is_managed_group(self, chat_id: str) -> bool:
        if self.client.user is None:
            return False
        admins = await self.client.get_chat_administrators(chat_id)
        return any(int(item.get("uid", 0)) == self.client.user.id for item in admins)

    def schedule_next(self, now: datetime | None = None) -> datetime:
        now = now or datetime.now()
        if self.settings.schedule == "daily":
            hour, minute = map(int, self.settings.daily_time.split(":"))
            value = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if value <= now:
                value += timedelta(days=1)
        else:
            value = now + timedelta(minutes=self.settings.interval_minutes)
        self.settings.next_run = value.isoformat(timespec="seconds")
        self.store.save(self.settings)
        return value

    def _is_due(self, now: datetime | None = None) -> bool:
        if not self.settings.next_run:
            self.schedule_next(now)
            return False
        try:
            next_run = datetime.fromisoformat(self.settings.next_run)
        except ValueError:
            self.schedule_next(now)
            return False
        return (now or datetime.now()) >= next_run

    def status(self) -> str:
        state = "روشن" if self.settings.enabled else "خاموش"
        banner = "تنظیم شده" if self.settings.has_banner else "تنظیم نشده"
        return (
            f"وضعیت: {state}\n"
            f"بنر: {banner}\n"
            f"گروه‌ها: {len(self.settings.group_ids)}\n"
            f"فاصله: {self.settings.gap_seconds:g} ثانیه\n"
            f"اجرای بعدی: {self.settings.next_run or '-'}"
        )


def as_positive_int(value: str, *, minimum: int, maximum: int) -> int:
    number = int(value)
    if not minimum <= number <= maximum:
        raise ValueError(f"عدد باید بین {minimum} و {maximum} باشد")
    return number


def parse_time(value: str) -> str:
    parsed = datetime.strptime(value, "%H:%M")
    return parsed.strftime("%H:%M")
