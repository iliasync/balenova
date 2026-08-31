# Bale Async

یک کتابخانهٔ Python کاملاً asynchronous برای ساخت userbot روی حساب واقعی بله، با
الهام از API کتابخانهٔ [balejs](https://github.com/Zellias/balejs).

> این پروژه از **Bot API** استفاده نمی‌کند. ارتباط حساب کاربری از طریق gRPC-web
> برای احراز هویت/fallback و WebSocket برای RPCهای زنده و updateها انجام می‌شود.

## ویژگی‌ها

- احراز هویت با شماره تلفن و ذخیرهٔ امن session با سطح دسترسی `0600`
- ورود مستقیم با session به شکل `<user_id>:<jwt>`
- WebSocket multiplexing، keepalive، timeout و RPCهای هم‌زمان
- gRPC-web async با retry و backoff
- مدل‌های typed برای `User`، `Chat` و `Message`
- handlerهای sync/async، lifecycle hooks و فیلترهای ترکیبی
- متدهای پیام، تاریخچه، دیالوگ، پروفایل، تایپ، واکنش، گزارش و جست‌وجو
- مدیریت گروه/کانال، اعضا، مجوزها، لینک دعوت و پیام‌های pinشده
- بسته‌بندی مدرن `pyproject.toml`، نشانگر `py.typed` و کنترل Ruff/mypy

## نصب برای توسعه

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## شروع سریع

```python
import os

from bale import Client, filters

client = Client(os.environ["BALE_PHONE_OR_SESSION"])


@client.on_message(filters.private & filters.text)
async def echo(message, _client):
    await message.reply(message.text)


@client.on_command("ping")
async def ping(message, _client):
    await message.reply("pong")


@client.on_error
async def log_error(error, _client):
    print(error)
```

برای اجرای برنامه:

```python
import asyncio

asyncio.run(client.run())
```

در اولین اجرا کد ورود درخواست می‌شود و session در مسیر جاری ذخیره خواهد شد. در
برنامه‌های بدون ترمینال می‌توان callbackهای `code_prompt`، `password_prompt` و
`signup_name_prompt` را به سازنده داد.

### نمونهٔ ورود و `get_me`

ابتدا پروژه را در محیط مجازی نصب کنید و سپس نمونهٔ آماده را اجرا کنید:

```bash
pip install -e .
python examples/login.py +989121234567
```

اگر شماره را در command line ندهید، برنامه آن را می‌پرسد:

```bash
python examples/login.py
```

در اجرای اول کد ارسال‌شده توسط بله و در صورت فعال بودن ورود دومرحله‌ای، رمز
عبور درخواست می‌شود. session در `sessions/my_account.session` ذخیره می‌شود و
اجراهای بعدی بدون درخواست دوبارهٔ کد از همان session استفاده می‌کنند.

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
python examples/protocol_lab.py +989121234567
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
