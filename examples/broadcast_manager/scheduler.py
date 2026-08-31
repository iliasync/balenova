from __future__ import annotations

import asyncio
import re
import time
from collections.abc import Awaitable, Callable, Mapping
from datetime import datetime, timedelta
from typing import Any, TypeVar

from balenova import BaleRpcError, Client

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
        self._request_lock = asyncio.Lock()
        self._last_request_at = 0.0

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
                        await self._with_rate_limit_retry(
                            lambda target=chat_id: self.client.copy_message(
                                target,
                                self.settings.banner_chat_id or "",
                                self.settings.banner_message_id or "",
                            ),
                            operation=f"ارسال به {chat_id}",
                        )
                    elif self.settings.banner_text:
                        await self._with_rate_limit_retry(
                            lambda target=chat_id: self.client.send(
                                target, self.settings.banner_text or ""
                            ),
                            operation=f"ارسال به {chat_id}",
                        )
                    else:
                        raise ValueError("No banner is configured")
                    sent += 1
                except Exception as error:
                    failed += 1
                    print(f"ارسال به {chat_id} ناموفق بود: {error}")
                if index + 1 < len(targets):
                    await asyncio.sleep(self.settings.gap_seconds)
            return sent, failed

    async def eligible_groups(
        self,
        limit: int | None = None,
        *,
        progress: Callable[[int, int, int], Awaitable[None]] | None = None,
    ) -> list[str]:
        """Find joined groups where this account may send messages.

        Prefer Bale's direct GetMyGroups + LoadGroups path. It resolves all
        memberships and effective send flags in two RPCs, avoiding a dialog scan
        and one GetFullGroup request per group. Older servers fall back to the
        paginated compatibility path below.
        """
        try:
            groups = await self._with_rate_limit_retry(
                self.client.get_my_groups,
                operation="دریافت مستقیم گروه‌های حساب",
            )
        except AttributeError:
            pass
        except BaleRpcError as error:
            if error.code not in {5, 12}:
                raise
        else:
            direct: list[str] = []
            candidates = [chat for chat in groups if chat.peer_type in {2, 5}]
            for checked, chat in enumerate(candidates, start=1):
                permitted = chat.can_send_message or bool(
                    chat.permissions.get("send_message", False)
                )
                if permitted:
                    direct.append(chat.id)
                    self.settings.group_ids = list(direct)
                    self.store.save(self.settings)
                    if limit is not None and len(direct) >= limit:
                        if progress:
                            await progress(checked, len(candidates), len(direct))
                        return direct
                if progress and checked % 10 == 0:
                    await progress(checked, len(candidates), len(direct))
            if progress:
                await progress(len(candidates), len(candidates), len(direct))
            return direct

        result: list[str] = []
        checked = 0
        min_date = -1
        seen: set[str] = set()
        page_size = 40

        while True:
            response = await self._with_rate_limit_retry(
                lambda cursor=min_date: self.client.load_dialogs(
                    limit=page_size, min_date=cursor
                ),
                operation="دریافت صفحهٔ گفتگوها",
            )
            dialogs = response.get("dialogs", [])
            if not isinstance(dialogs, list) or not dialogs:
                break

            page_groups: list[str] = []
            for dialog in dialogs:
                if not isinstance(dialog, Mapping):
                    continue
                peer = dialog.get("peer") or {}
                if not isinstance(peer, Mapping):
                    continue
                peer_id = int(peer.get("id", 0))
                peer_type = int(peer.get("type", 0))
                chat_id = f"{peer_id}|{peer_type}"
                if peer_id and peer_type in {2, 5} and chat_id not in seen:
                    seen.add(chat_id)
                    page_groups.append(chat_id)

            for chat_id in page_groups:
                checked += 1
                try:
                    if await self.can_send_messages(chat_id):
                        result.append(chat_id)
                        self.settings.group_ids = list(result)
                        self.store.save(self.settings)
                        if limit is not None and len(result) >= limit:
                            if progress:
                                await progress(checked, len(seen), len(result))
                            return result
                except Exception as error:
                    if _is_rate_limit_error(error):
                        raise
                    print(f"بررسی دسترسی گروه {chat_id} ناموفق بود: {error}")
                if progress and checked % 10 == 0:
                    await progress(checked, len(seen), len(result))

            dates = [
                int(item.get("sort_date", item.get("date", 0)))
                for item in dialogs
                if isinstance(item, Mapping)
            ]
            if len(dialogs) < page_size or not dates:
                break
            next_date = min(dates)
            if next_date >= min_date and min_date != -1:
                break
            min_date = next_date

        if progress:
            await progress(checked, len(seen), len(result))
        return result

    # Kept as a compatibility alias for code based on the first example version.
    managed_groups = eligible_groups

    async def can_send_messages(self, chat_id: str) -> bool:
        full_group = await self._with_rate_limit_retry(
            lambda: self.client.get_full_group(chat_id),
            operation=f"بررسی گروه {chat_id}",
        )
        return _full_group_can_send(full_group)

    async def group_from_link(self, link: str) -> str | None:
        preview = await self._with_rate_limit_retry(
            lambda: self.client.get_group_preview(link),
            operation="بررسی لینک گروه",
        )
        if not preview:
            return None
        full_group = preview.get("group")
        if not isinstance(full_group, dict) or not _full_group_can_send(full_group):
            return None
        group_id = int(full_group.get("id", 0))
        if not group_id:
            return None
        group_type = full_group.get("group_type", 0)
        peer_type = 5 if group_type in {2, "GROUP_TYPE_SUPER_GROUP"} else 2
        if group_type in {1, "GROUP_TYPE_CHANNEL"}:
            return None
        return f"{group_id}|{peer_type}"

    # Compatibility alias for code based on the first example version.
    is_managed_group = can_send_messages

    async def _with_rate_limit_retry(
        self, operation_call: Callable[[], Awaitable[_T]], *, operation: str
    ) -> _T:
        attempts = (
            self.settings.retry_attempts if self.settings.retry_rate_limits else 1
        )
        for attempt in range(attempts):
            try:
                async with self._request_lock:
                    elapsed = time.monotonic() - self._last_request_at
                    remaining = self.settings.scan_gap_seconds - elapsed
                    if remaining > 0:
                        await asyncio.sleep(remaining)
                    try:
                        return await operation_call()
                    finally:
                        self._last_request_at = time.monotonic()
            except Exception as error:
                if not _is_rate_limit_error(error):
                    raise
                if attempt + 1 >= attempts:
                    raise
                delay = _retry_after(error) or min(300.0, 15.0 * (2**attempt))
                print(
                    f"{operation}: محدودیت موقت؛ تلاش دوباره پس از {delay:g} ثانیه"
                )
                await asyncio.sleep(delay)
        raise RuntimeError("unreachable")

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


_T = TypeVar("_T")


def _full_group_can_send(full_group: dict[str, Any] | None) -> bool:
    if not full_group:
        return False
    member_value = full_group.get("is_member")
    if isinstance(member_value, dict):
        is_member = bool(member_value.get("value", False))
    else:
        is_member = bool(member_value)
    permissions = full_group.get("permissions")
    return bool(
        is_member
        and isinstance(permissions, dict)
        and permissions.get("send_message") is True
    )


def _is_rate_limit_error(error: BaseException) -> bool:
    if isinstance(error, BaleRpcError) and error.code in {8, 29, 429}:
        return True
    message = str(error).casefold()
    return any(
        marker in message
        for marker in (
            "rate limit",
            "too many request",
            "resource_exhausted",
            "flood",
            "try again later",
        )
    )


def _retry_after(error: BaseException) -> float | None:
    match = re.search(
        r"(?:retry[_ -]?after|flood[_ -]?wait)\D{0,8}(\d+)",
        str(error),
        flags=re.IGNORECASE,
    )
    return float(match.group(1)) if match else None
