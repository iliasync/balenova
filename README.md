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
- تفکیک دیالوگ‌ها به گروه، کانال، چت خصوصی و بات با `get_groups()`،
  `get_channels()`، `get_private_chats()` و `get_bots()`

برای دریافت همهٔ صفحات (نه فقط صفحهٔ اول) از `get_all_dialogs_by_type()` استفاده
کنید. این متد به‌صورت پیش‌فرض entityها را با RPCهای خواندنی resolve می‌کند تا
کانال و گروه اشتباه نشوند؛ در حساب‌های بسیار بزرگ می‌توانید `page_size` و
`max_pages` را کاهش دهید تا محدودیت نرخ Web رعایت شود:

```python
result = await client.get_all_dialogs_by_type(page_size=100, max_pages=100)
groups = result["groups"]
channels = result["channels"]
private_chats = result["private_chats"]
bots = result["bots"]
```
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

علاوه بر APIهای پایه، wrapperهای فایل و upload، ارسال photo/video/audio/document،
location/contact/sticker، آواتار گروه، مدیریت اعضا، pin گروهی و multi-media با
نام‌های متناظر BaleJS در `Client` موجودند. این wrapperها فقط مسیر سشن اکانت را
پوشش می‌دهند و APIهای اختصاصی Bot API عمداً در این پروژه اضافه نشده‌اند.
برای session نیز `refresh_token()` و `terminate_all_sessions()` و برای لینک‌های
دعوت `get_group_preview()` در دسترس است.
در بررسی bundle فعلی Web بله، مدیریت sessionهای فعال (`get_auth_sessions()` و
`terminate_session()`) و مسیرهای جدید Nasim (`get_file_urls()`، resume، cancel و
public URL) نیز به proto و `Client` اضافه شده‌اند.
متدهای ضبط‌شدهٔ جدید نیز شامل `click_inline_button()`،
`message_remove_reaction()`، `get_messages_reactions()`،
`get_messages_views()` و مجموعهٔ تماس از `start_group_call()` تا مدیریت لینک،
شرکت‌کننده، reaction و recording هستند.

متدهای تماس، signaling بله را پوشش می‌دهند؛ انتقال صوت/تصویر WebRTC وظیفهٔ
لایهٔ رسانه است و در این کتابخانه ضبط یا پیاده‌سازی نشده است.

### خلاصهٔ ممیزی سازگاری

این ممیزی در ۳۱ اوت ۲۰۲۶ با bundle عمومی `web.bale.ai` و commit
`a98aa699847ca09ed42ea93eb498581ceb8bb761` از Balethon انجام شد. سطح «تأیید»
فقط به schema و نام RPC اشاره دارد، نه موفقیت اجرای زنده.

| منبع | RPC | متد محلی | وضعیت | سطح تأیید |
| --- | --- | --- | --- | --- |
| Web + Balethon userbot | `ai.bale.server.Files/GetNasimFileUrl` | `get_file()` | پشتیبانی | bundle + proto محلی |
| Web | `ai.bale.server.Files/GetNasimFileUrls` | `get_file_urls()` | پشتیبانی | bundle؛ پاسخ تکرارشونده |
| Web | `ai.bale.server.Files/GetNasimFileUploadResume` | `get_file_upload_resume()` | پشتیبانی | bundle + تست محلی |
| Web | `ai.bale.server.Files/FileUploadCancel` | `cancel_file_upload()` | پشتیبانی | bundle + تست محلی |
| Web | `bale.v1.Configs/GetParameters` | `get_parameters()` | پشتیبانی | bundle؛ `parameters` تکرارشونده |
| Web | `bale.auth.v1.Auth/GetAuthSessions` | `get_auth_sessions()` | پشتیبانی | bundle + تست محلی |
| Web | `bale.users.v1.Users/GetFullUser` و privacy/card/contact RPCها | — | مستند نشده | schema عمومی کافی برای wrapper امن یافت نشد |

Balethon همچنان یک کتابخانهٔ Bot API است؛ بنابراین webhook، `getUpdates`، پرداخت
بات، inline bot و سایر متدهای Bot API عمداً از این پروژه خارج هستند. همچنین
`DeleteAccount`، `LogOut`، تغییر امنیت حساب، wallet و عملیات مخرب Web wrapper
عمداً wrapper سطح بالا ندارند. هیچ RPC از جدول «مستند نشده» به‌صورت حدسی اضافه
نشده است.

برای اجرای smoke test روی Web بله، session اکانت را فقط از طریق متغیر محیطی بدهید
(این تست در اجرای عادی به‌صورت خودکار skip می‌شود):

```bash
BALE_SESSION='<user_id>:<jwt>' pytest -q tests/test_web_bale.py
```

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
