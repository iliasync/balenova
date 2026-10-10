<div align="center" dir="rtl">

# 🚀 BaleNova (بلـه‌نـوا)

[![Version](https://img.shields.io/badge/version-0.3.1-emerald.svg?style=for-the-badge)](https://pypi.org/project/balenova/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/balenova/)
[![Protocol](https://img.shields.io/badge/protocol-Protobuf%20%7C%20gRPC--Web%20%7C%20WebSocket-5865F2.svg?style=for-the-badge)](https://web.bale.ai)
[![Methods](https://img.shields.io/badge/methods-690%20RPCs%20%7C%20830%2B%20Pythonic-f59e0b.svg?style=for-the-badge)](https://iliasync.github.io/balenova/all_methods_guide/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)

**کتابخانه ناهمگام (Async)، فوق‌العاده سریع، تایپ‌شده و جامع پایتون برای تعامل با پیام‌رسان بله با معماری الهام‌گرفته از aiogram و Telethon.**  
پوشش ۱۰۰ درصدی ۶۹۰ متد رسمی پروتکل وب بله با بیش از ۸۳۰ متد پایتونیک مستقل روی شیء `app`، ورود خودکار بدون کد تایید از مرورگر، ساخت کیبوردهای شیشه‌ای و ریپلای، ماشین وضعیت گفتگو (FSM)، کارت به کارت و کیف‌پول بانکی، استوری‌ها، تماس‌های زنده صوتی و تصویری گروهی با WebRTC/LiveKit و مینی‌اپ‌ها.

[📖 ورود به سایت مستندات رسمی (GitHub Pages)](https://iliasync.github.io/balenova/) · [📑 راهنمای جامع ۶۹۰ متد با پارامترها](https://iliasync.github.io/balenova/all_methods_guide/) · [📦 پکیج در PyPI](https://pypi.org/project/balenova/) · [🐛 گزارش باگ یا پیشنهاد](https://github.com/iliasync/balenova/issues)

---

</div>

<div dir="rtl">

## 📑 فهرست مطالب

1. [✨ ویژگی‌های شاخص و مزیت‌ها](#-ویژگیهای-شاخص-و-مزیتها)
2. [📦 نصب و راه‌اندازی](#-نصب-و-راهاندازی)
3. [🔑 احراز هویت و ورود هوشمند](#-احراز-هویت-و-ورود-هوشمند)
   - [ورود خودکار از مرورگرها (Firefox, Snap, Flatpak) بدون کد تایید](#۱-ورود-خودکار-از-مرورگر-بدون-کد-پیامکی)
   - [ورود با شماره تلفن و کد تایید ترمینالی](#۲-ورود-با-شماره-تلفن-و-کد-پیامکی)
4. [⚡ شروع سریع و ساخت اولین ربات](#-شروع-سریع-و-ساخت-اولین-ربات)
5. [⌨️ کیبوردهای شیشه‌ای و پاسخ (Keyboards)](#-کیبوردهای-شیشهای-و-پاسخ-keyboards)
6. [🚦 ماشین وضعیت و فرم‌های چندمرحله‌ای (FSM)](#-ماشین-وضعیت-و-فرمهای-چندمرحلهای-fsm)
7. [💳 امور بانکی، کیف‌پول و کارت به کارت](#-امور-بانکی-کیفپول-و-کارت-به-کارت)
8. [💬 ارسال انواع پیام، فایل و آلبوم رسانه‌ای](#-ارسال-انواع-پیام-فایل-و-آلبوم-رسانهای)
9. [📸 استوری‌ها، نظرسنجی‌ها و پیام‌های زمان‌بندی‌شده](#-استوریها-نظرسنجیها-و-پیامهای-زمانبندیشده)
10. [👥 مدیریت پیشرفته گروه‌ها، کانال‌ها و ادمین‌ها](#-مدیریت-پیشرفته-گروهها-کانالها-و-ادمینها)
11. [📞 تماس‌های صوتی و تصویری گروهی (WebRTC / LiveKit)](#-تماسهای-صوتی-و-تصویری-گروهی-webrtc--livekit)
12. [🌐 نحوه استفاده از کلیه ۶۹۰ متد وب بله](#-نحوه-استفاده-از-کلیه-۶۹۰-متد-وب-بله)
13. [🛠️ راهنمای توسعه و مشارکت](#-راهنمای-توسعه-و-مشارکت)

---

## ✨ ویژگی‌های شاخص و مزیت‌ها

- 🔥 **بیش از ۸۳۰ متد پایتونیک مستقل:** هر متدی در وب بله نام پایتونیک اختصاصی با آرگومان‌های صریح، تایپ کامل و Docstring دارد (`app.charge(...)`, `app.get_card_remain(...)`, `app.create_group(...)`).
- 🦊 **ورود جادویی از مرورگر (`Client.from_browser("auto")`):** خواندن سشن‌های فعال مرورگر فایرفاکس (لینوکس، Snap، Flatpak، ویندوز و مک) بدون نیاز به دریافت کد پیامکی.
- ⚡ **معماری رویدادمحور و فیلترهای پیشرفته:** شبیه `aiogram 3` با پشتیبانی از عملگرهای منطقی فیلترها (`&`, `|`, `~`)، دستورات متنی (`filters.command`) و وضعیت‌ها (`filters.state`).
- ⌨️ **سازنده کیبوردهای شیشه‌ای و دکمه‌ای:** با ساختار تمیز چیدمان ردیف‌ها (`row(...)`, `add(...)`)، دکمه‌های وب‌اپ (MiniApp) و کال‌بک داده.
- 🚦 **سیستم FSM توکار:** ذخیره‌سازی حافظه‌محور مقادیر موقت کاربران بدون نیاز به دیتابیس جداگانه.
- 💳 **خدمات جامع مالی بله:** کارت‌های ذخیره‌شده (Payvand)، استعلام موجودی، دریافت توکن درگاه انتقال وجه، خرید شارژ، اینترنت و قبوض.
- 📞 **پشتیبانی اختصاصی از WebRTC / LiveKit:** برقراری تماس گروهی رمزنگاری‌شده صوتی/تصویری.
- 🌙 **سایت مستندات مدرن با دارک‌مود خودکار:** هماهنگ با تم سیستم‌عامل کاربر با جستجوی سریع.

---

## 📦 نصب و راه‌اندازی

نصب نسخه پایدار از PyPI:

```bash
pip install --upgrade balenova
```

اگر نیاز به پشتیبانی از پخش صدای زنده در تماس‌های گروهی (WebRTC Voice) دارید:

```bash
pip install --upgrade "balenova[voice]"
```

---

## 🔑 احراز هویت و ورود هوشمند

### ۱. ورود خودکار از مرورگر (بدون کد پیامکی)
اگر در مرورگر فایرفاکس وارد وب بله شده‌اید، این متد بدون درخواست شماره یا OTP سشن را استخراج می‌کند:

```python
from balenova import Client

# تشخیص هوشمند مسیرهای مرورگر (شامل فایرفاکس، اسنپ و فلت‌پک)
app = Client.from_browser("auto")

# یا مستقیماً:
# app = Client.from_firefox()

app.run_forever()
```

### ۲. ورود با شماره تلفن و کد پیامکی
در اولین اجرا، شماره تلفن و کد تایید در ترمینال پرسیده شده و سشن در پوشه امن `sessions/` ذخیره می‌گردد:

```python
from balenova import Client

app = Client("my_account")
app.run_forever()
```

---

## ⚡ شروع سریع و ساخت اولین ربات

یک فایل `main.py` بسازید:

```python
from balenova import Client, events, filters

app = Client.from_browser("auto")

# پاسخ به دستور /start
@app.on(events.NewMessage, filters.command("start"))
async def start_handler(event: events.NewMessage):
    await event.reply("سلام! به بات BaleNova خوش آمدید 🚀")

# پاسخ به پیام‌های متنی حاوی کلمه خاص
@app.on(events.NewMessage, filters.text & filters.contains("قیمت"))
async def price_handler(event: events.NewMessage):
    await event.reply("برای استعلام قیمت‌ها دکمه زیر را لمس کنید.")

app.run_forever()
```

---

## ⌨️ کیبوردهای شیشه‌ای و پاسخ (Keyboards)

### کیبورد اینلاین شیشه‌ای (InlineKeyboardMarkup)

```python
from balenova.keyboards import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = (
    InlineKeyboardMarkup()
    .row(
        InlineKeyboardButton("🌐 وب‌سایت مستندات", url="https://iliasync.github.io/balenova/"),
        InlineKeyboardButton("⚡ استعلام موجودی", callback_data="check_balance")
    )
    .row(
        InlineKeyboardButton("🎮 اجرای مینی‌اپ", web_app_url="https://app.bale.ai")
    )
)

await app.send_message(chat_id, "منوی اصلی خدمات:", reply_markup=keyboard)
```

### کیبورد پاسخ معمولی (ReplyKeyboardMarkup)

```python
from balenova.keyboards import KeyboardButton, ReplyKeyboardMarkup

reply_kb = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .row(
        KeyboardButton("📱 ارسال شماره من", request_contact=True),
        KeyboardButton("📍 ارسال لوکیشن", request_location=True)
    )
    .row(
        KeyboardButton("ℹ️ درباره ما"),
        KeyboardButton("📞 ارتباط با پشتیبانی")
    )
)

await app.send_message(chat_id, "لطفاً یک گزینه را انتخاب کنید:", reply_markup=reply_kb)
```

---

## 🚦 ماشین وضعیت و فرم‌های چندمرحله‌ای (FSM)

پیاده‌سازی فرم‌های مرحله‌به‌مرحله با معماری دقیق `aiogram`:

```python
from balenova.fsm import State, StatesGroup

class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()

@app.on(events.NewMessage, filters.command("register"))
async def start_reg(event: events.NewMessage):
    fsm = event.get_fsm_context()
    await fsm.set_state(Registration.waiting_for_name)
    await event.reply("لطفاً نام و نام خانوادگی خود را ارسال کنید:")

@app.on(events.NewMessage, filters.state(Registration.waiting_for_name))
async def process_name(event: events.NewMessage):
    fsm = event.get_fsm_context()
    await fsm.update_data(full_name=event.text)
    await fsm.set_state(Registration.waiting_for_phone)
    await event.reply(f"ممنون {event.text}! حالا شماره تماس خود را ارسال کنید:")

@app.on(events.NewMessage, filters.state(Registration.waiting_for_phone))
async def process_phone(event: events.NewMessage):
    fsm = event.get_fsm_context()
    data = await fsm.get_data()
    await fsm.clear()  # اتمام فرآیند
    await event.reply(f"ثبت‌نام تکمیل شد!\nنام: {data['full_name']}\nشماره: {event.text}")
```

---

## 💳 امور بانکی، کیف‌پول و کارت به کارت

```python
# ۱. دریافت لیست کارت‌های بانکی پیوند ذخیره‌شده
cards = await app.get_payvand_cards()

# ۲. استعلام موجودی کارت بانکی شتابی با رمز دوم
balance = await app.get_card_balance(
    card_number="6037997123456789",
    cvv2="123",
    expire_date="28/05",
    pin2="123456"
)
print("موجودی قابل برداشت:", balance.availableBalanceAmount)

# ۳. دریافت توکن انتقال وجه کارت به کارت
token_res = await app.get_card_transfer_token(peer_user_id=123456, description="تسویه فاکتور")
print("آدرس درگاه بله:", token_res.requestEndPoint)

# ۴. تسویه و برداشت از کیف‌پول بله
await app.cash_out(amount=100000, iban="IR123456789012345678901234")
```

---

## 💬 ارسال انواع پیام، فایل و آلبوم رسانه‌ای

```python
# ارسال تصویر همراه با کپشن
await app.send_photo(chat_id, "banner.png", caption="تصویر اطلاعیه 🖼️")

# ارسال ویدیو با مدت زمان
await app.send_video(chat_id, "clip.mp4", duration=45, caption="کلیپ آموزشی")

# ارسال صدای ضبط شده (Voice)
await app.send_voice(chat_id, "voice.ogg", duration=15)

# ارسال فایل زیپ یا پی‌دی‌اف
await app.send_document(chat_id, "archive.zip")

# ارسال استیکر، فوروارد و پین کردن پیام
await app.forward_message(from_chat_id, to_chat_id, message_id)
await app.pin_message(chat_id, message_id)
await app.message_set_reaction(chat_id, message_id, "❤️")
```

---

## 📸 استوری‌ها، نظرسنجی‌ها و پیام‌های زمان‌بندی‌شده

```python
# استوری‌ها: دریافت، ری‌اکشن و آمار بازدید
stories = await app.get_all_stories()
await app.react_to_story(story_id="uuid_story", reaction="🔥")
viewers = await app.get_story_viewers(story_id="uuid_story")

# نظرسنجی: دریافت نتیجه، ثبت رای و بستن
poll_result = await app.get_poll_result(poll_id=987654)
await app.vote_poll(poll_id=987654, option_ids=[0])
await app.close_poll(poll_id=987654)

# پیام‌های زمان‌بندی شده: مشاهده تسک‌ها و لغو
tasks = await app.load_scheduled_tasks(chat_id)
await app.cancel_scheduled_tasks(task_ids=[101, 102])
```

---

## 👥 مدیریت پیشرفته گروه‌ها، کانال‌ها و ادمین‌ها

```python
# ایجاد گروه و کانال جدید
group = await app.create_group("گروه برنامه‌نویسان", user_ids=[12345, 67890])
channel = await app.create_channel("کانال رسمی اخبار", about="اطلاع‌رسانی مهم")

# لینک دعوت گروه
invite_url = await app.export_chat_invite_link(group.id)

# ارتقا، عزل و اخراج اعضا
await app.promote_chat_member(group.id, user_id=12345)
await app.remove_user_admin(group.id, user_id=12345)
await app.kick_user(group.id, user_id=67890)
await app.set_group_slow_mode(group.id, seconds=15)
```

---

## 📞 تماس‌های صوتی و تصویری گروهی (WebRTC / LiveKit)

اتصال Native به سرورهای کنفرانس تصویری و صوتی بله:

```python
# ورود به اتاق تماس با پروتکل رسمی LiveKit
conn = await app.join_group_call_rtc(call_id=1234567, client_name="ربات پاسخگو")
room = await conn.connect()

# کار با استریم‌های صوت و تصویر با livekit.rtc ...

await room.disconnect()
await app.leave_group_call(call_id=1234567)
```

---

## 🌐 نحوه استفاده از کلیه ۶۹۰ متد وب بله

کتابخانه به سه شیوه منعطف از تمام متدهای پروتکل پشتیبانی می‌کند:

```python
# شیوه ۱: متد پایتونیک مستقیم با آرگومان‌های صریح روی کلاینت (بیش از ۸۳۰ متد)
res = await app.charge(payment_token="tok_123", reference_no="ref_456")
res = await app.inquiry_bill(bill_type=1, bill_parameters="...")

# شیوه ۲: از طریق متد منعطف rpc
res = await app.rpc("bank", "GetCardRemain", pan="6037...", cvv2="123", expireDate="28/05", pin2="...")

# شیوه ۳: از طریق namespace رسمی و تایپ‌شده api
res = await app.api.bank.GetCardRemain(pan="6037...", cvv2="123", expireDate="28/05", pin2="...")
```

📖 **برای مشاهده پارامترها و نمونه کد تک‌تک ۶۹۰ متد، به [راهنمای جامع ۶۹۰ متد در مستندات رسمی](https://iliasync.github.io/balenova/all_methods_guide/) مراجعه کنید.**

---

## 🛠️ راهنمای توسعه و مشارکت

```bash
git clone https://github.com/iliasync/balenova.git
cd balenova
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"

# اجرای تست‌ها
pytest

# بررسی تایپ‌ها و استایل
mypy src
ruff check .
```

---

## 📄 مجوز و لایسنس

این پروژه تحت مجوز آزاد [MIT License](LICENSE) منتشر شده است. استفاده در پروژه‌های تجاری و شخصی کاملاً مجاز است.

</div>
