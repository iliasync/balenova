<div align="center" dir="rtl">

# 🚀 BaleNova (بلـه‌نـوا)

[![Version](https://img.shields.io/badge/version-0.3.1-emerald.svg?style=for-the-badge)](https://pypi.org/project/balenova/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/balenova/)
[![Protocol](https://img.shields.io/badge/protocol-Protobuf%20%7C%20gRPC--Web%20%7C%20WebSocket-5865F2.svg?style=for-the-badge)](https://web.bale.ai)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)

**کتابخانهٔ ناهمگام (Async)، فوق‌العاده سریع و کامل پایتون برای پیام‌رسان بله با معماری الهام‌گرفته از aiogram و Telethon.**
پشتیبانی خالص از پروتکل باینری Protobuf، وب‌سوکت، ورود خودکار بدون کد تایید از مرورگر، ساخت کیبوردهای شیشه‌ای و ریپلای، ماشین وضعیت چندمرحله‌ای (FSM)، تماس‌های زنده صوتی و تصویری گروهی با WebRTC/LiveKit، استوری‌ها، نظرسنجی و تمامی ۶۹۰ متد وب بله.

[📖 مشاهده سایت مستندات کامل (GitHub Pages)](https://iliasync.github.io/balenova/) · [📦 پکیج در PyPI](https://pypi.org/project/balenova/) · [🐛 گزارش باگ یا پیشنهاد](https://github.com/iliasync/balenova/issues)

---

</div>

<div dir="rtl">

## 📑 فهرست مطالب

1. [ویژگی‌های شاخص](#-ویژگیهای-شاخص)
2. [نصب و پیش‌نیازها](#-نصب-و-پیشنیازها)
3. [ورود و احراز هویت](#-ورود-و-احراز-هویت)
   - [ورود سریع بدون کد از مرورگر فایرفاکس (Client.from_firefox)](#۱-ورود-سریع-بدون-کد-از-مرورگر-فایرفاکس)
   - [ورود با شماره تلفن و کد تایید ترمینالی](#۲-ورود-با-شماره-تلفن-و-کد-پیامکی)
4. [شروع سریع و ساخت ربات (Quickstart)](#-شروع-سریع-و-ساخت-ربات)
5. [کلیدها و کیبوردهای بله (Keyboards & Buttons)](#-کیبوردها-و-کلیدهای-شیشهای-keyboards)
   - [کیبورد اینلاین شیشه‌ای (InlineKeyboardMarkup)](#کیبورد-اینلاین-شیشهای)
   - [کیبورد ریپلای دکمه‌ای (ReplyKeyboardMarkup)](#کیبورد-ریپلای-دکمهای)
6. [ماشین وضعیت گفتگو و فرم‌های چندمرحله‌ای (FSM)](#-ماشین-وضعیت-گفتگو-fsm)
7. [پیام‌رسانی و ارسال چندرسانه‌ای](#-پیامرسانی-و-ارسال-چندرسانهای)
   - [متن، ریپلای و واکنش (Reactions)](#ارسال-پیام-پاسخ-و-واکنش)
   - [عکس، ویدیو، وویس، موزیک و فایل](#ارسال-مدیا-و-فایل)
8. [استوری‌ها و نظرسنجی‌ها (Stories & Polls)](#-استوریها-و-نظرسنجیها)
9. [تماس‌های زنده گروهی با WebRTC و LiveKit](#-تماس-صوتی-و-تصویری-گروهی-webrtclivekit)
10. [دسترسی به تمامی ۶۹۰ متد وب بله (Full RPC Reference)](#-دسترسی-به-تمامی-۶۹۰-متد-وب-بله)
11. [توسعه و مشارکت](#-توسعه-و-مشارکت)

---

## 🌟 ویژگی‌های شاخص

- ⚡ **معماری مدرن مشابه aiogram:** بهره‌گیری از رویدادها (`events`)، دیسپچر، فیلترهای ترکیبی منطقی (`&`, `|`, `~`) و ساختار کاملاً شیء‌گرا.
- 🦊 **ورود فوری از مرورگر (`Client.from_firefox`):** استفاده مستقیم از نشست مرورگر بدون ارسال مجدد کد تایید پیامکی (OTP).
- ⌨️ **کیبوردهای شیشه‌ای و ریپلای:** ساخت آسان دکمه‌های اینلاین، دکمه‌های وب‌اپ (MiniApp) و ارسال موقعیت/مخاطب.
- 🚦 **سیستم مدیریت مرحله‌ای (FSM):** نگهداری داده‌ها و وضعیت کاربران در فرم‌های مرحله‌به‌مرحله.
- 📞 **تماس صوتی و تصویری Realtime:** اتصال Native به سرورهای WebRTC بله از طریق پروتکل رسمی LiveKit RTC.
- 🛡️ **امنیت بالا و ذخیره‌سازی ایزوله:** ذخیره سشن‌ها با سطح دسترسی سخت‌گیرانه (`0o600`) و محافظت در برابر نشت اطلاعات.
- 📚 **پوشش ۱۰۰ درصدی متدهای وب:** دسترسی به بیش از ۶۹۰ متد رسمی پلتفرم بله از طریق لایه‌های `app.api` و `app.rpc`.

---

## 📦 نصب و پیش‌نیازها

به پایتون ۳.۱۰ یا بالاتر نیاز است:

```bash
# نصب نسخه پایدار از PyPI
python -m pip install --upgrade balenova

# نصب با پشتیبانی از پخش صدای زنده در تماس (WebRTC Voice)
python -m pip install --upgrade "balenova[voice]"
```

نصب آخرین نسخه در حال توسعه از گیت‌هاب:
```bash
python -m pip install git+https://github.com/iliasync/balenova.git
```

---

## 🔑 ورود و احراز هویت

### ۱. ورود سریع بدون کد از مرورگر فایرفاکس
اگر در مرورگر فایرفاکس سیستم خود وارد [web.bale.ai](https://web.bale.ai) شده‌اید، نیازی به دریافت مجدد کد SMS یا ورود پسورد ندارید:

```python
from balenova import Client

app = Client.from_firefox()
app.run_forever()
```

### ۲. ورود با شماره تلفن و کد پیامکی
در اجرای اول، شماره تلفن و کد ۵ رقمی در ترمینال دریافت شده و نشست در فایلی امن ذخیره خواهد شد:

```python
from balenova import Client

app = Client("my_account")
app.run_forever()
```

---

## 🚀 شروع سریع و ساخت ربات

فایل `bot.py` را بسازید:

```python
from balenova import Client, events, filters

app = Client.from_firefox()


# پاسخ به دستور /start
@app.on(events.NewMessage, filters.command("start"))
async def start_handler(event: events.NewMessage):
    await event.reply("سلام! من با کتابخانه BaleNova آماده خدمت‌ام 🌱")


# دریافت پیام‌های متنی در چت‌های خصوصی
@app.on(events.NewMessage, filters.private & filters.text)
async def private_msg(event: events.NewMessage):
    if "سلام" in event.text:
        await event.reply("درود بر شما!")
    elif event.text == "پینگ":
        await event.answer("پونگ 🏓")


# واکنش به تغییر و ادیت شدن پیام
@app.on(events.MessageEdited)
async def edited_msg(event: events.MessageEdited):
    print(f"پیام در چت {event.chat.id} ویرایش شد: {event.text}")


app.run_forever()
```

---

## ⌨️ کیبوردها و کلیدهای شیشه‌ای (Keyboards)

### کیبورد اینلاین شیشه‌ای
```python
from balenova import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup()
markup.add(
    InlineKeyboardButton("ورود به سایت بله", url="https://bale.ai"),
    InlineKeyboardButton("تایید سفارش", callback_data="order_ok"),
)
markup.row(InlineKeyboardButton("پشتیبانی آنلاین", callback_data="support"))

await app.send_message(chat_id, "منوی اصلی خدمات:", reply_markup=markup)
```

### کیبورد ریپلای دکمه‌ای
```python
from balenova import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.row(
    KeyboardButton("ارسال شماره موبایل 📱", request_contact=True),
    KeyboardButton("ارسال موقعیت مکانی 📍", request_location=True),
)

await event.reply("لطفاً اطلاعات خود را ارسال کنید:", reply_markup=menu)

# حذف کیبورد:
# await event.reply("کیبورد برداشته شد", reply_markup=ReplyKeyboardRemove())
```

---

## 🚦 ماشین وضعیت گفتگو (FSM)

ساخت مراحل چندگانه ثبت‌نام یا پرسش و پاسخ:

```python
from balenova import Client, StatesGroup, State, events, filters

app = Client.from_firefox()


class RegisterFlow(StatesGroup):
    waiting_for_name = State()
    waiting_for_city = State()


@app.on(events.NewMessage, filters.command("register"))
async def start_reg(event: events.NewMessage):
    fsm = event.get_fsm_context()
    await fsm.set_state(RegisterFlow.waiting_for_name)
    await event.reply("نام خود را ارسال کنید:")


@app.on(events.NewMessage, filters.state(RegisterFlow.waiting_for_name))
async def get_name(event: events.NewMessage):
    fsm = event.get_fsm_context()
    await fsm.update_data(name=event.text)
    await fsm.set_state(RegisterFlow.waiting_for_city)
    await event.reply(f"خوش آمدید {event.text}! در کدام شهر زندگی می‌کنید؟")


@app.on(events.NewMessage, filters.state(RegisterFlow.waiting_for_city))
async def get_city(event: events.NewMessage):
    fsm = event.get_fsm_context()
    data = await fsm.get_data()
    user_name = data.get("name")
    city = event.text
    await fsm.clear()  # پایان وضعیت
    await event.reply(f"ثبت نام کامل شد:\n👤 نام: {user_name}\n🏙️ شهر: {city}")


app.run_forever()
```

---

## 💬 پیام‌رسانی و ارسال چندرسانه‌ای

### ارسال پیام، پاسخ و واکنش
```python
# ارسال پیام ساده
msg = await app.send_message(chat_id, "سلام دنیا!")

# ریپلای و ارسال ایموجی واکنش
await msg.reply("پاسخ به این پیام")
await msg.react("🔥")

# ویرایش و حذف
await msg.edit_text("متن اصلاح‌شده")
await msg.delete()
```

### ارسال مدیا و فایل
```python
# ارسال عکس با کپشن
await app.send_photo(chat_id, "image.jpg", caption="تصویر نمونه")

# ارسال وویس با شکل موج
await app.send_voice(chat_id, "voice.ogg", caption="صدای ضبط شده")

# ارسال سند یا فایل حجیم
await app.send_document(chat_id, "document.pdf")
```

---

## 📸 استوری‌ها و نظرسنجی‌ها

```python
# دریافت استوری‌ها و اموجی‌های مجاز ری‌اکشن
stories = await app.get_all_stories()
allowed_emojis = await app.get_story_reaction_emojis()
# ['❤', '😂', '👍', '👎', '😭', '😍', '👏', '🤯', '🔥', '😎', '💯', '🖤', '🇮🇷']

# ری‌اکشن به استوری
await app.react_to_story(story_id, "❤")

# شرکت در نظرسنجی
await app.vote_poll(poll_id=12345, option_ids=[0])
```

---

## 📞 تماس صوتی و تصویری گروهی (WebRTC/LiveKit)

کتابخانه BaleNova از پروتکل رمزنگاری شده مکالمه گروهی بله از طریق لایبریت LiveKit پشتیبانی می‌کند:

```python
# اتصال Typed به تماس گروهی
connection = await app.join_group_call_rtc(call_id, "نام کلاینت")
room = await connection.connect()

# تبادل صدا/تصویر با livekit.rtc ...

await room.disconnect()
await app.leave_group_call(call_id)
```

---

## 🌐 دسترسی به تمامی ۶۹۰ متد وب بله

هر متدی که در وب کلاینت بله وجود دارد، به سادگی قابل فراخوانی است:

```python
# شیوه ۱: پایتونیک با نام‌های snake_case
groups = await app.rpc("groups", "get_my_groups", mode=2, is_owner=True)
menu = await app.rpc("bill", "get_bill_menu")

# شیوه ۲: تایپ‌شده با پروتکل اصلی بله
groups = await app.api.groups.GetMyGroups(mode=2, isOwner=True)
wallets = await app.api.wallet.GetMyWallets()
```

---

## 🛠️ توسعه و مشارکت

```bash
git clone https://github.com/iliasync/balenova.git
cd balenova
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"
pytest
```

---

## 📄 مجوز

این پروژه تحت مجوز [MIT](LICENSE) منتشر شده است.

</div>
