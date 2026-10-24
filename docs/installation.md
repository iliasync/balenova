# 🚀 راهنمای نصب و احراز هویت (Installation & Auth)

کتابخانه **BaleNova** سریع‌ترین و منعطف‌ترین فریم‌ورک پایتون برای کار با پیام‌رسان بله است که هم از حساب‌های کاربری واقعی (Userbot) و هم از ربات‌ها پشتیبانی کامل می‌کند.

---

## ۱. پیش‌نیازها و نصب

برای استفاده از این کتابخانه به پایتون نسخه **3.10 یا بالاتر** نیاز دارید.

```bash
# نصب با pip
pip install balenova

# یا نصب با uv (بسیار سریع)
uv pip install balenova
```

---

## ۲. روش‌های احراز هویت (Authentication)

برای اتصال به سرورهای بله، چندین شیوه امن و کاربردی در نظر گرفته شده است:

### روش اول: ورود با شماره تلفن و کد تایید (پیش‌فرض)
در این روش، با وارد کردن نام دلخواه برای نشست (Session)، در صورت عدم وجود سشن قبلی، کتابخانه از شما شماره تلفن و کد تایید پیامک‌شده را در ترمینال درخواست می‌کند و اطلاعات سشن را با مجوزهای امنیتی ایزوله (`0600`) ذخیره می‌نماید:

```python
import asyncio
from bale import Client

async def main():
    async with Client("my_account") as client:
        me = await client.get_me()
        print(f"خوش آمدید: {me.name} (@{me.username})")

asyncio.run(main())
```

---

### روش دوم: همگام‌سازی مستقیم ۱ ثانیه‌ای با فایرفاکس (محیط محلی)
اگر روی سیستم خود در مرورگر فایرفاکس وارد نسخه وب بله (`web.bale.ai`) شده‌اید، نیازی به دریافت مجدد کد SMS ندارید! کافی است از متد جادویی `from_firefox()` استفاده کنید:

```python
import asyncio
from bale import Client

async def main():
    # سشن را مستقیماً و خودکار از کوکی مرورگر فایرفاکس استخراج می‌کند:
    async with Client.from_firefox() as client:
        me = await client.get_me()
        print(f"لاگین موفق با حساب کاربری: {me.name}")

asyncio.run(main())
```

---

### روش سوم: ورود مستقیم با توکن JWT یا رشته سشن
اگر توکن دسترسی بله (`access_token`) یا نشست ذخیره‌شده را از قبل در دست دارید:

```python
from bale import Client

# اتصال از طریق توکن JWT وب
client = Client.from_jwt("YOUR_JWT_ACCESS_TOKEN", user_id=2065995342)

# اتصال از طریق رشته استخراج‌شده سشن (String Session)
client = Client.from_string_session("2065995342:eyJhbGciOiJIUzI1NiIsInR5cCI6...")
```

---

## ۳. چرخه حیات کلاینت (Lifecycle & Runner)

برای اجرای کلاینت و ربات، دو شیوه اصلی وجود دارد:

### شیوه ۱: مدیریت خودکار با `async with` (برای اسکریپت‌ها و فراخوانی متدها)
در این روش، با ورود به بلوک `async with` اتصال برقرار و احراز هویت انجام شده و در انتهای بلوک کانکشن‌های وب‌سوکت و منابع به صورت پاکسازی‌شده بسته می‌شوند:

```python
async with Client("my_bot") as client:
    await client.send_message("pv_ilia", "سلام، این یک اسکریپت خودکار است!")
```

### شیوه ۲: اجرای بلندمدت ربات با `client.run()` (برای بات‌های لایو)
برای ربات‌هایی که باید به صورت دائمی (۲۴/۷) گوش‌به‌زنگ رویدادها و آپدیت‌ها باشند:

```python
from bale import Client, events

client = Client("bot_session")

@client.on(events.NewMessage)
async def on_message(event):
    if event.message.text == "سلام":
        await event.reply("درود!")

# اجرای مداوم و بی‌پایان تا زمان زدن Ctrl+C در ترمینال
client.run()
```
