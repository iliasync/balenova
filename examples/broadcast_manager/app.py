from __future__ import annotations

import asyncio
import contextlib

from balenova import Client, events, filters

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
active_commands: set[tuple[str, str]] = set()


HELP = """فرمان‌ها را با ویرایش یکی از پیام‌های خودتان اجرا کنید:
!banner متن بنر
!banner                 ← هنگام ریپلای روی پیام بنر
!gap 15                 ← فاصله ارسال، حداقل ۱۰ ثانیه
!every 60               ← هر ۶۰ دقیقه
!at 21:30               ← هر روز در ساعت مشخص
!groups add 12345|2
!groups remove 12345|2
!groups count 5         ← پنج گروه تحت مدیریت
!groups all             ← همه گروه‌های تحت مدیریت
!groups list
!start / !stop / !now / !status"""


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


@app.on(events.NewMessage, filters.text)
async def command(event):
    text = event.text.strip()
    if not text.startswith("!") or not is_owner_command(event):
        return
    command_id = (event.chat.id, event.message.id)
    if command_id in active_commands:
        return
    active_commands.add(command_id)
    try:
        await event.message.edit_text("⏳ در حال انجام...")
        answer = await handle_command(event, text)
    except Exception as error:
        answer = f"خطا: {error}"
        print(answer)
    finally:
        active_commands.discard(command_id)
    try:
        await event.message.edit_text(answer)
    except Exception as error:
        print(f"ویرایش پیام نتیجه ناموفق بود: {error}")
        await event.answer(answer)


def is_owner_command(event: events.NewMessage) -> bool:
    if event.message.is_outgoing:
        return True
    user = app.user
    return bool(
        user
        and event.is_private
        and event.chat.peer_id == user.id
        and event.chat.peer_type == 1
    )


async def handle_command(event: events.NewMessage, text: str) -> str:
    global broadcast_task
    parts = text.split(maxsplit=2)
    name = parts[0].casefold()
    settings = scheduler.settings

    if name == "!help":
        return HELP
    if name == "!banner":
        if len(parts) > 1:
            settings.banner_text = text.split(maxsplit=1)[1]
            settings.banner_chat_id = settings.banner_message_id = None
            result = f"بنر متنی با {len(settings.banner_text)} نویسه ذخیره شد ✅"
        elif event.message.replied_to:
            banner = event.message.replied_to
            settings.banner_text = None
            settings.banner_chat_id = banner.chat.id
            settings.banner_message_id = banner.id
            result = f"پیام {banner.id} به‌عنوان بنر ذخیره شد ✅"
        else:
            return "روی پیام بنر ریپلای کنید یا متن را بعد از !banner بنویسید."
    elif name == "!gap":
        settings.gap_seconds = as_positive_int(parts[1], minimum=10, maximum=600)
        result = f"فاصلهٔ ارسال روی {settings.gap_seconds:g} ثانیه ذخیره شد ✅"
    elif name == "!every":
        settings.interval_minutes = as_positive_int(parts[1], minimum=30, maximum=10080)
        settings.schedule = "interval"
        next_run = scheduler.schedule_next()
        result = (
            f"ارسال هر {settings.interval_minutes} دقیقه؛ "
            f"بعدی: {next_run:%H:%M} ✅"
        )
    elif name == "!at":
        settings.daily_time = parse_time(parts[1])
        settings.schedule = "daily"
        next_run = scheduler.schedule_next()
        result = (
            f"ساعت {settings.daily_time} ذخیره شد؛ "
            f"بعدی: {next_run:%Y-%m-%d %H:%M} ✅"
        )
    elif name == "!groups":
        return await groups_command(parts[1:])
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


async def groups_command(arguments: list[str]) -> str:
    settings = scheduler.settings
    if not arguments or arguments[0] == "list":
        return "گروه‌ها:\n" + ("\n".join(settings.group_ids) or "-")
    action = arguments[0]
    if action in {"all", "count"}:
        limit = (
            None
            if action == "all"
            else as_positive_int(arguments[1], minimum=1, maximum=100)
        )
        settings.group_ids = await scheduler.managed_groups(limit)
    elif action == "add":
        chat_id = arguments[1]
        if not await scheduler.is_managed_group(chat_id):
            return "این حساب در گروه انتخاب‌شده مدیر نیست."
        if chat_id not in settings.group_ids:
            settings.group_ids.append(chat_id)
    elif action == "remove":
        settings.group_ids = [
            item for item in settings.group_ids if item != arguments[1]
        ]
    else:
        return HELP
    scheduler.store.save(settings)
    return f"{len(settings.group_ids)} گروه ذخیره شد ✅"


if __name__ == "__main__":
    app.run_forever()
