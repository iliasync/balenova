# Bale Async

یک کتابخانهٔ Python کاملاً asynchronous برای ساخت userbot روی حساب واقعی بله، با
الهام از API کتابخانهٔ [balejs](https://github.com/Zellias/balejs).

> این پروژه از **Bot API** استفاده نمی‌کند. ارتباط حساب کاربری از طریق gRPC-web
> برای احراز هویت/fallback و WebSocket برای RPCهای زنده و updateها انجام می‌شود.

## ویژگی‌ها

- ورود session-first و ذخیرهٔ امن session با سطح دسترسی `0600`
- درخواست تعاملی شماره، کد و رمز دومرحله‌ای هنگام نبودن/انقضای session
- ورود مستقیم با session به شکل `<user_id>:<jwt>`
- WebSocket multiplexing، keepalive، timeout و RPCهای هم‌زمان
- gRPC-web async با retry و backoff
- مدل‌های typed برای `User`، `Chat` و `Message`
- handlerهای sync/async برای پیام و تمام updateهای خام، lifecycle hooks و فیلترها
- متدهای پیام، تاریخچه، دیالوگ، پروفایل، تایپ، واکنش، گزارش و جست‌وجو
- مدیریت گروه/کانال، اعضا، مجوزها، لینک دعوت و پیام‌های pinشده
- فایل و upload URL، آواتار گروه، multi-media، wallet و gift
- کلیک دکمهٔ inline، حذف واکنش و RPCهای signaling تماس گروهی
- بسته‌بندی مدرن `pyproject.toml`، نشانگر `py.typed` و کنترل Ruff/mypy

## نصب برای توسعه

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## شروع سریع

```python
from bale import Client, filters

client = Client(session_dir="sessions", session_name="my_account")


@client.on_message(filters.private & filters.text)
async def echo(message, _client):
    await message.reply(message.text)


@client.on_command("ping")
async def ping(message, _client):
    await message.reply("pong")


@client.on_error
async def log_error(error, _client):
    print(error)


@client.on_update
async def raw_update(update, _client):
    print((update.get("update") or {}).keys())
```

برای اجرای برنامه:

```python
import asyncio

asyncio.run(client.run())
```

در اولین اجرا شماره و کد ورود درخواست می‌شود و session ذخیره خواهد شد. اگر session
خراب یا منقضی باشد، ورود ترمینالی به‌طور خودکار دوباره اجرا می‌شود. در برنامه‌های
بدون ترمینال می‌توان callbackهای `phone_prompt`، `code_prompt`، `password_prompt`
و `signup_name_prompt` را به سازنده داد.

### نمونهٔ ورود و `get_me`

ابتدا پروژه را در محیط مجازی نصب کنید و سپس نمونهٔ آماده را اجرا کنید:

```bash
pip install -e .
python examples/login.py
```

در اجرای اول کد ارسال‌شده توسط بله و در صورت فعال بودن ورود دومرحله‌ای، رمز
عبور درخواست می‌شود. session در `sessions/my_account.session` ذخیره می‌شود و
اجراهای بعدی بدون درخواست دوبارهٔ کد از همان session استفاده می‌کنند.

### APIهای تکمیل‌شده از BaleJS و trace رسمی

علاوه بر APIهای پایه، wrapperهای فایل و upload، آواتار گروه، pin گروهی،
multi-media، wallet/gift و upvote با نام‌های متناظر BaleJS در `Client` موجودند.
متدهای ضبط‌شدهٔ جدید نیز شامل `click_inline_button()`،
`message_remove_reaction()`، `get_messages_reactions()`،
`get_messages_views()` و مجموعهٔ تماس از `start_group_call()` تا مدیریت لینک،
شرکت‌کننده، reaction و recording هستند.

متدهای تماس، signaling بله را پوشش می‌دهند؛ انتقال صوت/تصویر WebRTC وظیفهٔ
لایهٔ رسانه است و در این کتابخانه ضبط یا پیاده‌سازی نشده است.

### مثال‌های بیشتر

همهٔ مثال‌ها session را از `sessions/my_account.session` می‌خوانند و در صورت
نبودن یا انقضای آن، ورود ترمینالی را شروع می‌کنند. مسیر و نام session با
`--session-dir` و `--session-name` قابل تغییر است.

```bash
# userbot پاسخ‌گو تا Ctrl+C
python examples/echo.py

# دیالوگ‌ها و تاریخچه، فقط‌خواندنی
python examples/dialogs.py --chat '12345|1'

# ارسال پیام یا واکنش/کلیک روی یک پیام موجود
python examples/messages.py '12345|1' --text 'سلام'
python examples/messages.py '12345|4' --message-id '10|1700000000' --button-data ok

# اطلاعات گروه؛ عملیات مدیریتی فقط با گزینهٔ صریح انجام می‌شود
python examples/groups.py '12345|2'

# دریافت URL فایل یا slot آپلود
python examples/files.py download-url 10001 20002

# تماس‌ها؛ logs و ongoing فقط‌خواندنی‌اند
python examples/calls.py logs
python examples/calls.py generate-link --title 'جلسه'

# کیف پول فقط‌خواندنی یا ارسال صریح gift
python examples/gifts.py wallet

# شمارش امن تمام updateهای دریافتی، بدون چاپ payload خصوصی
python examples/updates.py --watch 30
```

برای مشاهدهٔ تمام گزینه‌ها روی هر مثال `--help` بزنید.

## API سطح پایین

هر RPC جدیدی که هنوز wrapper سطح بالا ندارد از همین حالا قابل فراخوانی است:

```python
result = await client.invoke(
    "bale.messaging.v2.Messaging",
    "LoadDialogs",
    "request.LoadDialogs",
    "response.LoadDialogs",
    {"min_date": -1, "limit": 40},
)
```

`invoke()` در حالت متصل از WebSocket و پیش از اتصال از gRPC-web استفاده می‌کند.

## توسعه و کنترل کیفیت

```bash
ruff check .
ruff format --check .
mypy src/bale
pytest
```

## آزمایش و توسعهٔ پروتکل

برای ضبط RPCها و updateهای حساب واقعی در حالت امن و opt-in:

```bash
python examples/protocol_lab.py
```

این فرمان تا فشردن `Ctrl+C` فعال می‌ماند. برای اجرای زمان‌دار می‌توانید مثلاً
`--watch 60` بدهید.

راهنمای inventory، مقایسهٔ schema و تولید مجدد protobuf در
[`protocol/README.md`](protocol/README.md) قرار دارد. traceها ممکن است شامل محتوای
خصوصی باشند و نباید commit یا منتشر شوند.

برای ضبط outboundهایی که فقط کلاینت رسمی تولید می‌کند—مانند کلیک دکمه و signaling
تماس—از `examples/official_web_protocol_lab.py` مطابق راهنمای protocol استفاده
کنید.

پروتکل‌های protobuf برگرفته از مخزن مرجع MIT هستند؛ جزئیات انتساب در `NOTICE`
آمده است.
