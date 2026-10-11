<div align="center" dir="rtl">

# 🚀 BaleNova (بلـه‌نـوا)

[![Version](https://img.shields.io/badge/version-0.4.0-emerald.svg?style=for-the-badge)](https://pypi.org/project/balenova/)
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
9. [🔄 تبدیل شناسه چت و شناسه پیر (chat_id ⟷ peer_id)](#-تبدیل-شناسه-چت-و-شناسه-پیر-chat_id--peer_id)
10. [📸 استوری‌ها، نظرسنجی‌ها و پیام‌های زمان‌بندی‌شده](#-استوریها-نظرسنجیها-و-پیامهای-زمانبندیشده)
11. [👥 مدیریت پیشرفته گروه‌ها، کانال‌ها و ادمین‌ها](#-مدیریت-پیشرفته-گروهها-کانالها-و-ادمینها)
12. [📞 تماس‌های صوتی و تصویری گروهی (WebRTC / LiveKit)](#-تماسهای-صوتی-و-تصویری-گروهی-webrtc--livekit)
13. [🌐 نحوه استفاده از کلیه ۶۹۰ متد وب بله](#-نحوه-استفاده-از-کلیه-۶۹۰-متد-وب-بله)
14. [🛠️ راهنمای توسعه و مشارکت](#-راهنمای-توسعه-و-مشارکت)

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

کتابخانه BaleNova کامل‌ترین ابزارهای مالی و بانکی پیام‌رسان بله (شبکه شتاب، پرداخت‌ساز، پیوند و کیف‌پول) را به صورت متدهای سطح‌بالا و تایپ‌شده ارائه می‌دهد:

### متد 
دریافت لیست کارت‌های بانکی پیوند شتابی ثبت‌شده روی شماره کاربر جاری.

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء Protobuf شامل لیست کارت‌های بانکی ().



---

### متد 
استعلام موجودی کارت بانکی شتابی با استفاده از رمز دوم (پویا یا ایستا).

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | String | **Required** | شماره ۱۶ رقمی کارت بانکی شتابی مبدا. |
|  | String | **Required** | کد ۳ یا ۴ رقمی CVV2 درج‌شده روی کارت. |
|  | String | **Required** | تاریخ انقضای کارت با فرمت YY/MM (مانند '28/05'). |
|  | String | **Required** | رمز دوم اینترنتی (رمز یکبار مصرف یا پویا). |

</div>

**مقدار بازگشتی:** شیء Protobuf شامل فیلدهای  و .



---

### متد 
دریافت توکن امن انتقال وجه کارت به کارت جهت شروع تراکنش درون‌برنامه‌ای بله.

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | Integer | Optional | شناسه عددی کاربر مقصد (در صورت انتقال به شخص). |
|  | Integer | Optional | شناسه تصادفی پیام درخواست پول. |
|  | String | Optional | شرح تراکنش و بابت پرداخت. |

</div>

**مقدار بازگشتی:** شیء شامل آدرس درگاه () و توکن تراکنش ().



---

### متد  و 
مشاهده موجودی کیف‌پول بله و ثبت درخواست تسویه حساب به شماره شبا یا کارت بانکی.

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | Integer | **Required (in cash_out)** | مبلغ برداشت به ریال. |
|  | String | Optional (in cash_out) | شماره شبای مقصد با پیشوند IR (۲۴ رقمی). |
|  | String | Optional (in cash_out) | شماره کارت بانکی مقصد (۱۶ رقمی). |

</div>



---

## 💬 ارسال انواع پیام، فایل و آلبوم رسانه‌ای

BaleNova متدهای استاندارد سطح‌بالا و کامل برای ارسال انواع پیام و رسانه‌ها مطابق استانداردهای Telegram Bot API فراهم ساخته است:

### متد 
ارسال پیام متنی به چت، گروه، کانال یا کاربر با پشتیبانی از کیبورد شیشه‌ای یا ریپلای.

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | String / Integer | **Required** | شناسه مقصد چت (مانند '123456789|1' یا '987654321|2'). |
|  | String | **Required** | متن پیام ارسالی (پشتیبانی از قالب‌بندی متنی). |
|  | Integer | Optional | شناسه پیامی که این پیام به عنوان پاسخ به آن ارسال می‌شود. |
|  | InlineKeyboardMarkup / ReplyKeyboardMarkup | Optional | کیبورد شیشه‌ای یا دکمه‌های پاسخ پیوست شده به پیام. |

</div>

**مقدار بازگشتی:** شیء  ارسال شده.



---

### متدهای ارسال چندرسانه‌ای (, , , )

<div dir=ltr markdown="1">

| Method | Media Parameter | Extra Parameters | Description |
| :--- | :--- | :--- | :--- |
|  |  (Path / Bytes / URL) | , , ,  | ارسال عکس همراه با کپشن اختیاری. |
|  |  (Path / Bytes / URL) | , , ,  | ارسال ویدیو با مدت زمان و رزولوشن. |
|  |  (Path / Bytes / OGG) | , ,  | ارسال پیام صوتی با شکل موج. |
|  |  (Path / Bytes) | ,  | ارسال انواع فایل، PDF و آرشیو ZIP. |
|  |  (ID String) |  | ارسال استیکرهای رسمی بله. |

</div>



---

### متدهای ویرایش، حذف، فوروارد، پین و ری‌اکشن

<div dir=ltr markdown="1">

| Method | Parameters | Required | Description |
| :--- | :--- | :--- | :--- |
|  | , ,  | **All Required** | ویرایش متن پیام ارسال شده. |
|  | , ,  | ,  | حذف پیام برای طرفین یا فقط کاربر جاری. |
|  | , ,  | **All Required** | فوروارد پیام با حفظ برچسب فرستنده. |
|  | , ,  | **All Required** | کپی تمیز پیام بدون برچسب فوروارد. |
|  | ,  | **All Required** | سنجاق کردن پیام در بالای صفحه چت. |
|  | ,  | **All Required** | برداشتن سنجاق پیام پین‌شده. |
|  | , ,  | **All Required** | ثبت واکنش ایموجی (مانند '❤️', '🔥'). |

</div>



---

## 🔄 تبدیل شناسه چت و شناسه پیر ( ⟷ )

در پیام‌رسان بله، شناسه‌های گفتگو ترکیبی از شناسه عددی و نوع گفتگو هستند (مانند  برای کاربر یا  برای گروه). BaleNova توابع و متدهای اختصاصی و بدون نیاز به اینترنت برای تبدیل دوطرفه فراهم کرده است:

<div dir=ltr markdown="1">

| Function / Method | Input | Output | Description |
| :--- | :--- | :--- | :--- |
|  |  |  | استخراج شناسه عددی خالص (peer_id) از رشته chat_id. |
|  | ,  |  | ساخت رشته استاندارد chat_id از شناسه و نوع چت. |
|  |  |  | تجزیه شناسه به تاپل دو مقداری . |

</div>

**جدول انواع نوع چت (Peer Type):**
-  یا  / : گفتگوی خصوصی دوطرفه
-  یا : گروه عادی
-  یا : کانال اطلاع‌رسانی
-  یا : ربات بله
-  یا : ابرگروه
-  یا : تاپیک و رشته پیام



---

## 📸 استوری‌ها، نظرسنجی‌ها و پیام‌های زمان‌بندی‌شده

پشتیبانی کامل از قابلیت‌های اختصاصی جدید پیام‌رسان بله:

### متد  و 
بارگذاری استوری‌ها، مشاهده بینندگان و ارسال واکنش ایموجی:

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | String | **Required (in react/viewers)** | شناسه یکتای UUID استوری. |
|  | String | **Required (in react)** | ایموجی واکنش (مانند '🔥', '❤', '👏'). |
|  | Integer | Optional (in viewers) | شماره صفحه نتایج بینندگان (پیش‌فرض ۱). |

</div>



---

### متد  و 
دریافت آمار زنده، ثبت رای یا لغو رای در نظرسنجی‌ها:

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | Integer | **Required** | شناسه عددی نظرسنجی. |
|  | Iterable[Integer] | **Required (in vote)** | شناسه‌های گزینه‌های مورد نظر (شروع از ۰). |
|  | Boolean | Optional (in vote) | لغو و پس گرفتن رای قبلی (پیش‌فرض False). |

</div>



---

### متد  و 
مدیریت صف پیام‌های زمان‌بندی‌شده جهت ارسال در زمان معین در آینده:



---

## 👥 مدیریت پیشرفته گروه‌ها، کانال‌ها و ادمین‌ها

پشتیبانی کامل از تمامی قابلیت‌های مدیریت و نظارت بر گروه‌ها و کانال‌ها:

### متد  و 

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | String | **Required** | عنوان یا نام گروه / کانال جدید. |
|  | Iterable[Integer] | Optional (group) | شناسه‌های کاربری اعضای اولیه برای عضویت در گروه. |
|  | String | Optional (channel) | توضیحات یا بیوگرافی کانال. |

</div>

**مقدار بازگشتی:** شیء  ساخته‌شده شامل شناسه uid=1000(mahan) gid=1000(mahan) groups=1000(mahan),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),111(lpadmin),114(lxd),116(docker).



---

### متدهای لینک دعوت، ارتقا، عزل، اخراج و اسلومود

<div dir=ltr markdown="1">

| Method | Parameters | Required | Description |
| :--- | :--- | :--- | :--- |
|  |  | **Required** | ساخت و دریافت لینک دعوت اختصاصی. |
|  |  | **Required** | باطل کردن لینک قبلی و صدور لینک جدید. |
|  | ,  | **All Required** | ارتقای یک عضو عادی به مدیر (Admin). |
|  | ,  | **All Required** | عزل مدیر و بازگرداندن به عضو عادی. |
|  | ,  | **All Required** | اخراج کاربر از گروه (امکان بازگشت با لینک دارد). |
|  | ,  | **All Required** | مسدودسازی کامل کاربر در گروه (بن دائم). |
|  | ,  | **All Required** | رفع مسدودیت (Unban) کاربر. |
|  | ,  | **All Required** | فعال‌سازی حالت آرام (Slow Mode) بر حسب ثانیه. |

</div>



---

## 📞 تماس‌های صوتی و تصویری گروهی (WebRTC / LiveKit)

پیام‌رسان بله برای تماس‌های صوتی و تصویری گروهی از سرورهای پیشرفته **LiveKit WebRTC** استفاده می‌کند. BaleNova پشتیبانی Native و کاملی از این قابلیت ارائه می‌دهد:

### متد 
اتصال بلادرنگ به سرورهای کنفرانس WebRTC بله در یک تماس گروهی.

<div dir=ltr markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
|  | Integer | **Required** | شناسه عددی تماس گروهی. |
|  | String | Optional | نام نمایشی کلاینت در اتاق کنفرانس صوتی/تصویری. |

</div>

**مقدار بازگشتی:** شیء  جهت اتصال مستقیم به اتاق لایوکیت.



---

## 🌐 نحوه استفاده از کلیه ۶۹۰ متد وب بله

کتابخانه BaleNova به سه شیوه بسیار منعطف دسترسی به **۱۰۰٪ تمامی ۶۹۰ متد پروتکل رسمی وب بله** را ممکن می‌سازد:

### ۱. متدهای پایتونیک سطح‌بالا و تایپ‌شده مستقیم ()
بیش از **۸۳۰ متد** پایتونیک مستقل روی شیء  تعریف شده‌اند که پارامترهای هر متد را به صورت تایپ‌شده با نام‌های استاندارد پایتونی دریافت می‌کنند:



---

### ۲. فراخوانی داینامیک با متد 
فراخوانی هر متد بر اساس نام سرویس و متد بدون واسطه:



---

### ۳. فراخوانی ساختاریافته از طریق فضای نام رسمی 
دسترسی کامپایل‌شده و سلسله‌مراتبی بر اساس بسته‌های رسمی پروتکل:



---

### 📑 مراجع مستندات تفصیلی متدها

| مرجع مستندات | توضیحات | لینک |
| :--- | :--- | :--- |
| **راهنمای جامع ۶۹۰ متد RPC** | مستندات کامل تک‌تک ۶۹۰ متد پروتکل وب به سبک Telegram Bot API همراه با جداول LTR فیلدها و انواع داده‌ها | [مشاهده راهنمای ۶۹۰ متد](https://iliasync.github.io/balenova/all_methods_guide/) |
| **راهنمای متدهای پایتونیک** | تشریح کامل متدهای سطح‌بالای کلاینت با انواع داده پایتون و نمونه کدهای PEP 8 | [مشاهده متدهای پایتونیک](https://iliasync.github.io/balenova/pythonic_rpc_methods/) |
| **امور مالی و مینی‌اپ‌ها** | راهنمای کارت به کارت، استعلام موجودی، خرید شارژ، قبوض و اجرای MiniAppها | [مشاهده راهنمای مالی](https://iliasync.github.io/balenova/banking_miniapps/) |
| **استوری‌ها و پیام‌های زمان‌بندی‌شده** | راهنمای کامل استوری، نظرسنجی و صف زمان‌بندی پیام‌ها | [مشاهده راهنمای استوری‌ها](https://iliasync.github.io/balenova/stories_polls_schedule/) |

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
