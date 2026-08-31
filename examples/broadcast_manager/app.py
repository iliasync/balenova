from __future__ import annotations

import asyncio
import contextlib
import re
from typing import Any

from balenova import BaleRpcError, Client, Message, filters

try:
    from .scheduler import BroadcastScheduler, as_positive_int, parse_time
    from .settings import SettingsStore
except ImportError:  # Allows: python examples/broadcast_manager/app.py
    from scheduler import BroadcastScheduler, as_positive_int, parse_time
    from settings import SettingsStore

app = Client("broadcast_manager")
scheduler = BroadcastScheduler(app, SettingsStore())
worker: asyncio.Task[None] | None = None
broadcast_task: asyncio.Task[tuple[int, int]] | None = None
active_commands: set[tuple[str, int | str]] = set()


HELP = """فرمان‌ها را با ویرایش یکی از پیام‌های خودتان اجرا کنید:
!banner متن بنر
!banner                 ← هنگام ریپلای روی پیام بنر
!gap 15                 ← فاصله ارسال، حداقل ۱۰ ثانیه
!every 1..60            ← فاصلهٔ دوره از ۱ تا ۶۰ دقیقه
!at 21:30               ← هر روز در ساعت مشخص
!groups add 12345|2
!groups add             ← داخل خود گروه
!groups links           ← ریپلای روی پیام لینک‌ها
!groups remove 12345|2
!groups count 5         ← پنج گروه دارای مجوز ارسال پیام
!groups all             ← همه گروه‌های عضو با مجوز ارسال پیام
!groups list
!add / !addlinks        ← میان‌بر دو دستور بالا
!panel                  ← پنل چک‌لیستی
!start / !stop / !now / !status"""

PANEL_HEADER = "پنل تبچی BaleNova"
PANEL_OPTIONS = {
    "ارسال زمان‌بندی‌شده": "enabled",
    "تلاش مجدد هنگام محدودیت": "retry_rate_limits",
    "نمایش پیشرفت اسکن": "show_scan_progress",
}
LINK_PATTERN = re.compile(r"(?:https?://)?ble\.ir/join/[^\s]+", re.IGNORECASE)


@app.on_initialize
async def initialize(_client):
    global worker
    worker = asyncio.create_task(scheduler.run(), name="broadcast-scheduler")


@app.on_connect
async def connected(client):
    account = client.user.full_name if client.user else "ناشناخته"
    print(f"BaleNova متصل شد: {account}")
    print("فرمان !help را در پیام‌های ذخیره‌شده بفرستید یا ویرایش کنید.")


@app.on_shutdown
async def shutdown(_client):
    global worker, broadcast_task
    if worker:
        worker.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await worker
    if broadcast_task:
        broadcast_task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await broadcast_task
    worker = broadcast_task = None


@app.on_raw_update
async def raw_panel_update(raw: dict[str, Any], client: Client) -> None:
    update = raw.get("update")
    composed = update.get("composed_update") if isinstance(update, dict) else None
    payload = composed.get("message") if isinstance(composed, dict) else None
    if not isinstance(payload, dict) and isinstance(composed, dict):
        edited = composed.get("message_content_changed")
        if isinstance(edited, dict):
            date = edited.get("date", 0)
            if isinstance(date, dict):
                date = date.get("value", 0)
            updater = edited.get("updater_user_id", 0)
            if isinstance(updater, dict):
                updater = updater.get("value", 0)
            payload = {
                "peer": edited.get("peer", {}),
                "sender_uid": updater,
                "date": date,
                "rid": edited.get("rid", 0),
                "message": edited.get("message", {}),
            }
    if not isinstance(payload, dict):
        return
    content = payload.get("message")
    text_message = content.get("text_message") if isinstance(content, dict) else None
    text = text_message.get("text") if isinstance(text_message, dict) else None
    if not isinstance(text, str) or not text.strip().startswith(PANEL_HEADER):
        return
    message = client._wrap_message(payload)
    if not is_owner_command(message) and not is_known_panel(message):
        return
    if panel_message_key(message) not in scheduler.settings.panel_message_keys:
        remember_panel(message)
    await apply_panel_edit(message, text.strip())


@app.on_message(filters.text)
async def command(message: Message):
    text = (message.text or "").strip()
    owner_command = is_owner_command(message)
    known_panel = is_known_panel(message)
    if not owner_command and not known_panel:
        return
    if text.startswith(PANEL_HEADER):
        if panel_message_key(message) not in scheduler.settings.panel_message_keys:
            remember_panel(message)
        await apply_panel_edit(message, text)
        return
    if not text.startswith("!"):
        return
    command_id = (message.chat.id, message.rid)
    if command_id in active_commands:
        return
    active_commands.add(command_id)
    try:
        try:
            await message.edit_text("⏳ فرمان دریافت شد؛ در حال انجام...")
        except Exception as error:
            # Status feedback is best-effort and must never prevent execution.
            print(f"ویرایش وضعیت فرمان ناموفق بود: {error}")
        answer = await handle_command(message, text)
    except Exception as error:
        answer = f"خطا: {error}"
        print(answer)
    finally:
        active_commands.discard(command_id)
    try:
        await message.edit_text(answer)
    except Exception as error:
        print(f"ویرایش پیام نتیجه ناموفق بود: {error}")
        await message.answer(answer)


def is_owner_command(message: Message) -> bool:
    if message.is_outgoing:
        return True
    user = app.user
    return bool(
        user
        and message.chat.peer_id == user.id
        and message.chat.peer_type == 1
    )


async def handle_command(message: Message, text: str) -> str:
    global broadcast_task
    parts = text.split(maxsplit=2)
    name = parts[0].casefold()
    settings = scheduler.settings

    if name == "!help":
        return HELP
    if name == "!panel":
        remember_panel(message)
        return render_panel()
    if name == "!banner":
        if len(parts) > 1:
            settings.banner_text = text.split(maxsplit=1)[1]
            settings.banner_chat_id = settings.banner_message_id = None
            result = f"بنر متنی با {len(settings.banner_text)} نویسه ذخیره شد ✅"
        elif message.replied_to:
            banner = message.replied_to
            settings.banner_text = None
            settings.banner_chat_id = banner.chat.id
            settings.banner_message_id = banner.id
            result = f"پیام {banner.id} به‌عنوان بنر ذخیره شد ✅"
        else:
            return "روی پیام بنر ریپلای کنید یا متن را بعد از !banner بنویسید."
    elif name == "!gap":
        if len(parts) < 2:
            return "روش استفاده: !gap 15"
        settings.gap_seconds = as_positive_int(parts[1], minimum=10, maximum=600)
        result = f"فاصلهٔ ارسال روی {settings.gap_seconds:g} ثانیه ذخیره شد ✅"
    elif name == "!every":
        if len(parts) < 2:
            return "روش استفاده: !every 60"
        settings.interval_minutes = as_positive_int(parts[1], minimum=1, maximum=60)
        settings.schedule = "interval"
        next_run = scheduler.schedule_next()
        result = (
            f"ارسال هر {settings.interval_minutes} دقیقه؛ "
            f"بعدی: {next_run:%H:%M} ✅"
        )
    elif name == "!at":
        if len(parts) < 2:
            return "روش استفاده: !at 21:30"
        settings.daily_time = parse_time(parts[1])
        settings.schedule = "daily"
        next_run = scheduler.schedule_next()
        result = (
            f"ساعت {settings.daily_time} ذخیره شد؛ "
            f"بعدی: {next_run:%Y-%m-%d %H:%M} ✅"
        )
    elif name == "!groups":
        return await groups_command(parts[1:], message)
    elif name == "!add":
        return await groups_command(["add"], message)
    elif name == "!addlinks":
        return await groups_command(["links"], message)
    elif name == "!start":
        if not settings.has_banner or not settings.group_ids:
            return "ابتدا بنر و حداقل یک گروه را تنظیم کنید."
        settings.enabled = True
        next_run = scheduler.schedule_next()
        result = f"ارسال خودکار روشن شد؛ اجرای بعدی: {next_run:%Y-%m-%d %H:%M} ✅"
    elif name == "!stop":
        settings.enabled = False
        result = "ارسال خودکار خاموش شد ✅"
    elif name == "!now":
        if not settings.has_banner or not settings.group_ids:
            return "ابتدا بنر و گروه‌ها را تنظیم کنید."
        sent, failed = await scheduler.broadcast()
        return f"ارسال تمام شد؛ موفق: {sent}، ناموفق: {failed} ✅"
    elif name == "!status":
        return scheduler.status()
    else:
        return HELP

    scheduler.store.save(settings)
    return result


@app.on_error
async def log_error(error):
    print(f"خطای برنامه: {error}")


async def groups_command(arguments: list[str], message: Message) -> str:
    settings = scheduler.settings
    if not arguments or arguments[0] == "list":
        return "گروه‌ها:\n" + ("\n".join(settings.group_ids) or "-")
    action = arguments[0].casefold()
    if action in {"all", "count"}:
        if action == "count" and len(arguments) < 2:
            return "روش استفاده: !groups count 5"
        limit = (
            None
            if action == "all"
            else as_positive_int(arguments[1], minimum=1, maximum=100)
        )

        async def show_progress(checked: int, total: int, found: int) -> None:
            try:
                await message.edit_text(
                    f"⏳ بررسی گروه‌ها: {checked}/{total}؛ واجد دسترسی: {found}"
                )
            except Exception as error:
                print(f"نمایش پیشرفت ناموفق بود: {error}")

        progress = show_progress if settings.show_scan_progress else None
        settings.group_ids = await scheduler.eligible_groups(limit, progress=progress)
    elif action == "add":
        if len(arguments) >= 2:
            chat_id = arguments[1]
        elif message.chat.peer_type in {2, 5}:
            chat_id = message.chat.id
        else:
            return "این دستور را داخل گروه بفرستید یا شناسهٔ گروه را وارد کنید."
        if not await scheduler.can_send_messages(chat_id):
            return "عضویت یا مجوز ارسال پیام در این گروه تأیید نشد."
        if chat_id not in settings.group_ids:
            settings.group_ids.append(chat_id)
    elif action == "links":
        source = message.replied_to
        if source is None:
            return "روی پیامی که در هر خط یک لینک گروه دارد ریپلای کنید."
        links = extract_group_links(source.content)
        if not links:
            return "هیچ لینک معتبر ble.ir/join در پیام ریپلای‌شده پیدا نشد."
        added = duplicate = rejected = 0
        for link in links:
            try:
                chat_id = await scheduler.group_from_link(link)
            except BaleRpcError as error:
                if error.code == 8:
                    raise
                print(f"بررسی لینک {link} ناموفق بود: {error}")
                rejected += 1
                continue
            except Exception as error:
                print(f"بررسی لینک {link} ناموفق بود: {error}")
                rejected += 1
                continue
            if chat_id is None:
                rejected += 1
            elif chat_id in settings.group_ids:
                duplicate += 1
            else:
                settings.group_ids.append(chat_id)
                scheduler.store.save(settings)
                added += 1
        return (
            f"پردازش لینک‌ها تمام شد؛ افزوده: {added}، تکراری: {duplicate}، "
            f"ردشده/بدون دسترسی: {rejected} ✅"
        )
    elif action == "remove":
        if len(arguments) < 2:
            return "روش استفاده: !groups remove 12345|2"
        settings.group_ids = [
            item for item in settings.group_ids if item != arguments[1]
        ]
    else:
        return HELP
    scheduler.store.save(settings)
    return f"{len(settings.group_ids)} گروه ذخیره شد ✅"


def extract_group_links(text: str) -> list[str]:
    links = [match.group(0).rstrip(".,،؛;)]") for match in LINK_PATTERN.finditer(text)]
    return list(dict.fromkeys(links))


def panel_message_key(message: Message) -> str:
    return f"{message.chat.id}#{message.rid}"


def is_known_panel(message: Message) -> bool:
    known = scheduler.settings.panel_message_keys
    if panel_message_key(message) in known:
        return True
    previous = message.raw.get("previous_message_id")
    if isinstance(previous, dict) and previous.get("rid") is not None:
        previous_key = f"{message.chat.id}#{previous['rid']}"
        return previous_key in known
    return False


def remember_panel(message: Message) -> None:
    settings = scheduler.settings
    key = panel_message_key(message)
    settings.panel_message_keys = [
        *(item for item in settings.panel_message_keys if item != key),
        key,
    ][-20:]
    scheduler.store.save(settings)


def render_panel(change_notes: list[str] | None = None) -> str:
    settings = scheduler.settings
    lines = [PANEL_HEADER, ""]
    for label, field in PANEL_OPTIONS.items():
        mark = "x" if getattr(settings, field) else " "
        lines.append(f"- [{mark}] {label}")
    lines.extend(
        (
            "",
            "برای تغییر روی تیک‌ها بزنید؛ [x] روشن و [ ] خاموش است.",
            f"گروه‌ها: {len(settings.group_ids)} | بنر: "
            f"{'تنظیم است' if settings.has_banner else 'تنظیم نیست'}",
        )
    )
    if change_notes:
        lines.extend(("", "آخرین تغییرات:", *(f"• {note}" for note in change_notes)))
    return "\n".join(lines)


async def apply_panel_edit(message: Message, text: str) -> None:
    settings = scheduler.settings
    requested = parse_panel_options(text)
    changed = {
        field: value
        for field, value in requested.items()
        if bool(getattr(settings, field)) != value
    }
    # The update generated by our own canonical edit has no setting changes.
    if not changed:
        return

    print(
        "تغییر پنل دریافت شد: "
        + ", ".join(
            f"{field}={'on' if value else 'off'}" for field, value in changed.items()
        )
    )

    was_enabled = settings.enabled
    for field, value in changed.items():
        setattr(settings, field, value)
    notes: list[str] = []
    enable_rejected = False
    if settings.enabled and (not settings.has_banner or not settings.group_ids):
        settings.enabled = False
        enable_rejected = True
        notes.append("ارسال زمان‌بندی‌شده روشن نشد؛ ابتدا بنر و گروه تنظیم کنید")
    elif settings.enabled and not was_enabled:
        scheduler.schedule_next()
    for label, field in PANEL_OPTIONS.items():
        if field not in changed or (field == "enabled" and enable_rejected):
            continue
        state = "روشن شد" if getattr(settings, field) else "خاموش شد"
        notes.append(f"{label} {state}")
    scheduler.store.save(settings)
    updated = render_panel(notes)
    try:
        await message.edit_text(updated)
    except Exception as error:
        print(f"به‌روزرسانی پنل ناموفق بود: {error}")
        await message.answer(updated)


def parse_panel_options(text: str) -> dict[str, bool]:
    requested: dict[str, bool] = {}
    for line in text.splitlines():
        match = re.fullmatch(r"- \[([ xX])\]\s+(.+?)\s*", line)
        if match and match.group(2) in PANEL_OPTIONS:
            requested[PANEL_OPTIONS[match.group(2)]] = (
                match.group(1).casefold() == "x"
            )
    return requested


if __name__ == "__main__":
    app.run_forever()
