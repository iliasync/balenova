# ⚡ BaleNova (بله‌نوا)

> **فریم‌ورک فوق‌سریع، ناهمگام (Async) و مدرن پایتون برای پیام‌رسان و سوپراپ بله**  
> *Next-Generation High-Performance Async Python Framework for Bale Messenger & SuperApp*

[![PyPI version](https://img.shields.io/badge/pypi-v0.5.0-0088cc.svg?logo=pypi&logoColor=white)](https://pypi.org/project/balenova/)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-0088cc.svg)](https://iliasync.github.io/balenova/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Syntax](https://img.shields.io/badge/syntax-Telethon%20%26%20Pyrogram-blueviolet.svg)](https://github.com/iliasync/balenova)
[![Zero RPC](https://img.shields.io/badge/API-Zero--RPC%20Pure%20Python-success.svg)](https://github.com/iliasync/balenova)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

📚 **وب‌سایت مستندات آنلاین و راهنمای کامل:**  
👉 **[https://iliasync.github.io/balenova/](https://iliasync.github.io/balenova/)**

---

## 🌟 چرا BaleNova؟

* 🚫 **خداحافظی با RPC و خطاهای خام سرور (Zero-RPC):** دیگر نیازی به سر و کله زدن با Protobuf، ساختارهای درهم‌تنیده پیام، یا متدهای ناشناخته نیست. همه چیز در قالب متدهای سرراست و قابل فهم پایتون در دسترس است.
* 🦊 **شناسایی خودکار سشن فایرفاکس (`Client.from_firefox()`):** اتصال آنی به حساب فعال شما در مرورگر Firefox (لینوکس، ویندوز و مک) بدون نیاز به دریافت کد پیامکی مجدد.
* ⚡ **پشتیبانی دوگانه از سینتکس Telethon و Pyrogram:**
  * سبک تلتون: `@app.on(events.NewMessage(pattern=r"^/start", incoming=True))`
  * سبک پایروگرام: `@app.on_message(filters.command("start") & filters.private)`
* 💬 **دسترسی سریع و شهودی (Dot-Access):** دسترسی مستقیم به مقادیر پیام بدون باز کردن دیکشنری: `msg.text`, `msg.chat.title`, `msg.from_user.username`, `msg.id`, `msg.is_outgoing`.
* 🎯 **متدهای کنشی روی خود شیء پیام (Active Record):** پاسخ مستقیم با `await msg.reply("...")`، ویرایش پیام با `await msg.edit("...")`، حذف با `await msg.delete()` و ری‌اکشن با `await msg.react("🔥")`.
* 🗂️ **دریافت هوشمند گفتگوها (`await app.get_dialogs()`):** بازگرداندن اشیاء سطح بالای `Dialog` شامل آخرین پیام، تعداد پیام‌های خوانده‌نشده، عنوان کانال یا گروه بدون دغدغه تبدیل Peer.
* 🔍 **پرینت ساختاریافته و زیبا (`print(msg)`):** نمایش شفاف و فرمت‌شده‌ی اشیاء در لاگ‌ها و کنسول دیباگ.
* 💳 **پشتیبانی جامع از امکانات سوپراپ بله:** کیف‌پول، پاکت هدیه، کارت به کارت، کیبوردهای شیشه‌ای و اینلاین، نظرسنجی و تماس‌های صوتی-تصویری WebRTC/LiveKit.

---

## 📦 نصب

```bash
pip install balenova
```

یا نصب آخرین نسخه مستقیم از سورس مخزن:
```bash
pip install git+https://github.com/iliasync/balenova.git
```

---

## 🚀 شروع سریع (Quickstart)

### ۱. اتصال خودکار از طریق سشن فایرفاکس (بدون کد پیامکی)

```python
import asyncio
from balenova import Client

async def main():
    # اتصال مستقیم به سشن فعال در فایرفاکس شما
    app = Client.from_firefox()

    async with app:
        me = await app.get_me()
        print(f"Logged in as: {me.full_name} (@{me.username})")

        # ارسال پیام به چت شخصی (Saved Messages)
        msg = await app.send_message(f"{me.id}|1", "سلام از بله‌نوا 🚀")
        print(f"پیام ارسال شد با شناسه: {msg.id}")

        # ویرایش پیام
        await asyncio.sleep(1)
        await msg.edit("پیام ویرایش گردید ✅")

if __name__ == "__main__":
    asyncio.run(main())
```

---

### ۲. ساخت ربات پاسخ‌گو به سبک تلتون (Telethon-Style Events)

```python
from balenova import Client, events

app = Client("my_bot")

# دریافت دستور /start با پترن ریجکس و فقط پیام‌های ورودی
@app.on(events.NewMessage(pattern=r"^/start", incoming=True))
async def start_handler(event: events.NewMessage):
    # خروجی پرینت بسیار مرتب و خوانا
    print(event)

    # پاسخ مستقیم و ارسال ری‌اکشن
    await event.reply(f"درود {event.from_user.first_name}! ربات بله‌نوا آماده است ⚡")
    await event.react("❤️")

# دریافت دستور پینگ
@app.on(events.NewMessage(pattern=r"^پینگ$", incoming=True))
async def ping_handler(event: events.NewMessage):
    await event.reply("پونگ! 🏓")

# اجرای دائمی کلاینت
app.run()
```

---

### ۳. دریافت لیست گفتگوها و پیام‌های اخیر (Dialogs)

```python
import asyncio
from balenova import Client

async def main():
    async with Client.from_firefox() as app:
        # دریافت ۵ گفتگوی اخیر به صورت آبجکت‌های ساخت‌یافته
        dialogs = await app.get_dialogs(limit=5)
        
        for d in dialogs:
            title = d.chat.title or d.chat.full_name or d.chat.id
            last = d.top_message.text if d.top_message else "(بدون متن)"
            print(f"[{d.chat.type.value}] {title} | خوانده‌نشده: {d.unread_count} | آخرین پیام: {last[:30]}")

asyncio.run(main())
```

---

### ۴. ارسال کیبورد شیشه‌ای و اینلاین (Inline Keyboards)

```python
import asyncio
from balenova import Client
from balenova.keyboards import InlineKeyboardButton, InlineKeyboardMarkup

async def main():
    async with Client.from_firefox() as app:
        # ساخت کیبورد شیشه‌ای
        keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton("🌐 وب‌سایت مستندات", url="https://iliasync.github.io/balenova/"),
            InlineKeyboardButton("⚡ پشتیبانی", callback_data="support_click"),
        )

        target_chat = f"{app.user_id}|1"
        await app.send_message(target_chat, "یکی از گزینه‌های زیر را انتخاب نمایید:", reply_markup=keyboard)

asyncio.run(main())
```

---

### ۵. ورود با شماره تلفن و کد تایید ترمینالی

```python
import asyncio
from balenova import Client

async def login_flow():
    # ساخت کلاینت با نام نشست دلخواه (ذخیره امن در sessions/my_account.session)
    app = Client("my_account")
    await app.start()
    
    me = await app.get_me()
    print(f"ورود موفق به حساب: {me.full_name}")
    await app.close()

asyncio.run(login_flow())
```

---

## 📂 ساختار ماژولار و مهندسی پروژه (Clean Architecture)

```
new library for bale/
├── src/
│   └── bale/ (و balenova/)
│       ├── types/                  # تایپ‌های سطح بالا همراه با متدهای متصل (Active Record)
│       │   ├── user.py             # User با متدهای .send_message()، .block()، .unblock()
│       │   ├── chat.py             # Chat با متدهای .send_message()، .send_photo()، .leave()
│       │   ├── message.py          # Message با دسترسی دات‌اکسس (.text, .from_user, .buttons)
│       │   ├── dialog.py           # Dialog و DialogsList
│       │   ├── media.py            # Photo, Video, Audio, Voice, Document
│       │   ├── keyboard.py         # InlineKeyboardMarkup و ReplyKeyboardMarkup
│       │   └── events.py           # ChatActionEvent, CallbackQueryEvent, UserTypingEvent
│       ├── enums.py                # تمامی ثابت‌ها و تایپ‌های عددی (ChatType, ChatAction, ...)
│       ├── events.py               # رویدادهای Telethon-Style (@app.on(events.NewMessage))
│       ├── filters.py              # فیلترهای منطقی ترکیبی (& و | و ~) و ریجکس
│       ├── client.py               # کلاینت قدرتمند آسنکرون با بیش از ۸۳۰ متد
│       ├── session.py              # ذخیره‌سازی امن سشن و اتصال مستقیم به Firefox
│       └── transports/             # لایه ارتباطی پایدار WebSocket و gRPC-web
├── tests/                          # بیش از ۱۳۰ تست خودکار برای تضمین پایداری
└── docs/                           # مستندات کامل و کاتالوگ متدها
```

---

## 🛡️ لایسنس (License)

این پروژه تحت مجوز معتبر **MIT License** به صورت متن‌باز منتشر شده است.
