# مرجع جامع متدهای سطح‌بالای پایتونیک BaleNova (Telegram-Style)

در کتابخانه **BaleNova** متدهای پرکاربرد سطح‌بالا مستقیماً روی شیء `app` (نمونه کلاس `Client`) تعریف شده‌اند. این متدها دارای **آرگومان‌های صریح، تایپ‌های مشخص پایتون (PEP 8)**، اعتبارسنجی خودکار و داکیومنت کامل به سبک **Telegram Bot API** هستند.

تمامی جدول‌های پارامترها به صورت **چپ‌به‌راست (LTR)** تنظیم شده‌اند و فیلدهای **الزامی (Required)** و **اختیاری (Optional)** کاملاً متمایز هستند.

---

## پیام‌رسانی و رسانه‌ها (Messaging & Media)

### `app.send_message`
ارسال پیام متنی به چت، گروه، کانال یا کاربر با قابلیت پیوست کیبورد شیشه‌ای یا ریپلای.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه مقصد پیام (مانند '123456789|1' یا '987654321|2'). |
| `text` | String | **Required** | متن پیامی که قصد ارسال آن را دارید (پشتیبانی از قالب‌بندی متنی). |
| `reply_to` | Integer | Optional | شناسه پیامی که این پیام به عنوان پاسخ (Reply) به آن ارسال می‌شود. |
| `reply_markup` | InlineKeyboardMarkup / ReplyKeyboardMarkup | Optional | کیبورد شیشه‌ای یا دکمه‌های پاسخ پیوست شده به پیام. |

</div>

**مقدار بازگشتی:** شیء `Message` ارسال شده شامل شناسه `id`، تاریخ و محتوا.

**نمونه کد پایتون (PEP 8):**
```python
# ارسال پیام متنی همراه با کیبورد اینلاین
markup = InlineKeyboardMarkup().row(
    InlineKeyboardButton("وب‌سایت", url="https://bale.ai"),
    InlineKeyboardButton("استعلام", callback_data="check"),
)
msg = await app.send_message(
    chat_id="123456789|1",
    text="سلام! پیام تستی با دکمه‌های شیشه‌ای.",
    reply_markup=markup,
)
```

---

### `app.send_photo`
ارسال تصویر از طریق فایل محلی، مسیر `Path` یا باینری بایت‌ها به چت مقصد.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت یا کاربر دریافت‌کننده تصویر. |
| `photo` | String / Path / Bytes | **Required** | مسیر فایل روی دیسک، آدرس URL یا باینری تصویر. |
| `caption` | String | Optional | متن توضیح یا کپشن تصویر (حداکثر ۱۰۲۴ کاراکتر). |
| `width` | Integer | Optional | عرض تصویر به پیکسل جهت بهینه‌سازی پیش‌نمایش. |
| `height` | Integer | Optional | ارتفاع تصویر به پیکسل. |
| `reply_to` | Integer | Optional | شناسه پیام والد جهت ریپلای کردن روی آن. |

</div>

**مقدار بازگشتی:** شیء `Message` ارسال شده شامل مشخصات سند تصویر.

**نمونه کد پایتون (PEP 8):**
```python
# ارسال تصویر از فایل محلی با کپشن
await app.send_photo(
    chat_id="123456789|1",
    photo="assets/banner.png",
    caption="تصویر اطلاعیه رسمی 🖼️",
)
```

---

### `app.send_video`
ارسال فایل ویدیویی به چت مقصد با قابلیت تعیین مدت زمان و اندازه تصویر.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت مقصد. |
| `video` | String / Path / Bytes | **Required** | مسیر فایل ویدیویی محلی یا باینری ویدیو. |
| `caption` | String | Optional | متن کپشن ویدیو. |
| `duration` | Integer | Optional | طول مدت ویدیو بر حسب ثانیه. |
| `width` | Integer | Optional | عرض فریم ویدیو. |
| `height` | Integer | Optional | ارتفاع فریم ویدیو. |
| `reply_to` | Integer | Optional | شناسه پیام جهت ریپلای. |

</div>

**مقدار بازگشتی:** شیء `Message` ویدیوی ارسال شده.

**نمونه کد پایتون (PEP 8):**
```python
# ارسال ویدیو با مشخصات مدت زمان
await app.send_video(
    chat_id="123456789|1",
    video="media/clip.mp4",
    duration=45,
    caption="ویدیو آموزشی نحوه کار با بات 🎬",
)
```

---

### `app.send_voice`
ارسال صدای ضبط‌شده (Voice Message / شکل موج) به چت مقصد.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت مقصد. |
| `voice` | String / Path / Bytes | **Required** | مسیر فایل صوتی OGG/Opus یا بافر بایت‌ها. |
| `caption` | String | Optional | کپشن اختیاری برای فایل صوتی. |
| `duration` | Integer | Optional | مدت زمان پیام صوتی بر حسب ثانیه. |
| `reply_to` | Integer | Optional | شناسه پیام والد. |

</div>

**مقدار بازگشتی:** شیء `Message` صوتی ارسال شده.

**نمونه کد پایتون (PEP 8):**
```python
# ارسال پیام صوتی (Voice)
await app.send_voice(
    chat_id="123456789|1",
    voice="audio/voice.ogg",
    duration=15,
)
```

---

### `app.send_document`
ارسال هرگونه فایل، سند، آرشیو ZIP یا PDF با حفظ پسوند و نام اصلی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت مقصد. |
| `document` | String / Path / Bytes | **Required** | مسیر فایل یا بافر باینری سند. |
| `caption` | String | Optional | متن توضیح سند. |
| `reply_to` | Integer | Optional | شناسه پیام والد. |

</div>

**مقدار بازگشتی:** شیء `Message` سند ارسال شده.

**نمونه کد پایتون (PEP 8):**
```python
# ارسال فایل PDF
await app.send_document(
    chat_id="123456789|1",
    document="docs/contract.pdf",
    caption="نسخه نهایی قرارداد 📄",
)
```

---

### `app.send_sticker`
ارسال استیکر با ساختار شناسه استیکر پلتفرم بله.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت مقصد. |
| `sticker` | String / Mapping | **Required** | شناسه استیکر بله با ساختار '<file_id>:<access_hash>:<storage_version>:<sticker_id>:<collection_id>'. |
| `reply_to` | Integer | Optional | شناسه پیام والد جهت پاسخ. |

</div>

**مقدار بازگشتی:** شیء `Message` استیکر ارسال شده.

**نمونه کد پایتون (PEP 8):**
```python
# ارسال استیکر بله
await app.send_sticker(
    chat_id="123456789|1",
    sticker="123456:789012:1:345:678",
)
```

---

### `app.edit_message_text`
ویرایش متن پیامی که قبلاً توسط کلاینت در یک چت ارسال شده است.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت حاوی پیام. |
| `message_id` | Integer | **Required** | شناسه پیام جهت ویرایش متن. |
| `text` | String | **Required** | متن جدید جایگزین شده. |

</div>

**مقدار بازگشتی:** شیء `Message` با مشخصات بروزرسانی شده.

**نمونه کد پایتون (PEP 8):**
```python
# ویرایش متن پیام قبلی
await app.edit_message_text(
    chat_id="123456789|1",
    message_id=msg.id,
    text="متن ویرایش‌شده جدید ✍️",
)
```

---

### `app.delete_message`
حذف یک پیام ارسالی یا دریافتی در چت برای طرفین یا فقط کاربر جاری.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت مقصد. |
| `message_id` | Integer | **Required** | شناسه پیام جهت حذف. |
| `just_me` | Boolean | Optional | در صورت True پیام فقط برای کاربر جاری حذف می‌شود؛ پیش‌فرض False (حذف برای دو طرف). |

</div>

**مقدار بازگشتی:** تاییدیه موفقیت عملیات حذف (`DefaultResponse`).

**نمونه کد پایتون (PEP 8):**
```python
# حذف پیام برای طرفین
await app.delete_message(
    chat_id="123456789|1",
    message_id=msg.id,
)
```

---

### `app.forward_message`
فوروارد پیام از یک چت به چت دیگر با حفظ برچسب فرستنده اصلی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `from_chat_id` | String / Integer | **Required** | شناسه چت مبدا که پیام در آن قرار دارد. |
| `to_chat_id` | String / Integer | **Required** | شناسه چت مقصد جهت ارسال پیام فوروارد شده. |
| `message_id` | Integer | **Required** | شناسه پیام مورد نظر در چت مبدا. |

</div>

**مقدار بازگشتی:** شیء `Message` جدید فوروارد شده در چت مقصد.

**نمونه کد پایتون (PEP 8):**
```python
# فوروارد پیام از کاربر به کانال
await app.forward_message(
    from_chat_id="123456789|1",
    to_chat_id="987654321|2",
    message_id=12345,
)
```

---

### `app.copy_message`
کپی کردن محتوای یک پیام به چت دیگر بدون الصاق برچسب فوروارد (ارسال تمیز مجدد).

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `from_chat_id` | String / Integer | **Required** | شناسه چت مبدا. |
| `to_chat_id` | String / Integer | **Required** | شناسه چت مقصد. |
| `message_id` | Integer | **Required** | شناسه پیام مبدا. |

</div>

**مقدار بازگشتی:** شیء `Message` تازه ایجاد شده در مقصد.

**نمونه کد پایتون (PEP 8):**
```python
# کپی پیام بدون تگ فوروارد
await app.copy_message(
    from_chat_id="123456789|1",
    to_chat_id="987654321|2",
    message_id=12345,
)
```

---

### `app.pin_message`
سنجاق کردن (Pin) یک پیام در بالای صفحه چت یا گروه.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت یا گروه. |
| `message_id` | Integer | **Required** | شناسه پیام جهت سنجاق شدن. |

</div>

**مقدار بازگشتی:** تاییدیه موفقیت پین (`DefaultResponse`).

**نمونه کد پایتون (PEP 8):**
```python
# سنجاق کردن پیام
await app.pin_message(
    chat_id="123456789|2",
    message_id=msg.id,
)
```

---

### `app.unpin_message`
برداشتن سنجاق (Unpin) یک پیام در چت یا گروه.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت یا گروه. |
| `message_id` | Integer | **Required** | شناسه پیام جهت برداشتن سنجاق. |

</div>

**مقدار بازگشتی:** تاییدیه موفقیت برداشتن پین.

**نمونه کد پایتون (PEP 8):**
```python
# برداشتن پین پیام
await app.unpin_message(
    chat_id="123456789|2",
    message_id=msg.id,
)
```

---

### `app.message_set_reaction`
ثبت واکنش (ایموجی ری‌اکشن) به پیام مشخص شده.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت حاوی پیام. |
| `message_id` | Integer | **Required** | شناسه پیام مورد نظر. |
| `reaction` | String | **Required** | ایموجی واکنش (مانند '❤️', '👍', '🔥', '👏'). |

</div>

**مقدار بازگشتی:** پاسخ شامل وضعیت واکنش و شماره توالی جدید.

**نمونه کد پایتون (PEP 8):**
```python
# ثبت واکنش روی پیام
await app.message_set_reaction(
    chat_id="123456789|1",
    message_id=msg.id,
    reaction="🔥",
)
```

---

## امور بانکی و کیف‌پول (Banking & Wallet)

### `app.get_payvand_cards`
دریافت لیست کارت‌های بانکی پیوند شتابی ثبت‌شده روی شماره کاربر جاری.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء Protobuf شامل لیست کارت‌های بانکی (`payvandCards`).

**نمونه کد پایتون (PEP 8):**
```python
# دریافت کارت‌های متصل به حساب
cards = await app.get_payvand_cards()
print("کارت‌های من:", model_to_dict(cards))
```

---

### `app.get_card_balance`
استعلام موجودی کارت بانکی شتابی با استفاده از رمز دوم (پویا/ایستا).

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `card_number` | String | **Required** | شماره ۱۶ رقمی کارت بانکی شتابی. |
| `cvv2` | String | **Required** | کد ۳ یا ۴ رقمی CVV2 درج‌شده روی کارت. |
| `expire_date` | String | **Required** | تاریخ انقضای کارت با فرمت YY/MM (مانند '28/05'). |
| `pin2` | String | **Required** | رمز دوم اینترنتی (رمز پویا). |

</div>

**مقدار بازگشتی:** شیء Protobuf شامل فیلدهای `currentBalanceAmount` و `availableBalanceAmount`.

**نمونه کد پایتون (PEP 8):**
```python
# استعلام مانده حساب کارت
res = await app.get_card_balance(
    card_number="6037997123456789",
    cvv2="123",
    expire_date="28/05",
    pin2="123456",
)
print("موجودی فعلی:", res.currentBalanceAmount)
```

---

### `app.get_card_transfer_token`
دریافت توکن امن انتقال وجه کارت به کارت جهت شروع پرداخت درون‌برنامه‌ای بله.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer_user_id` | Integer | Optional | شناسه عددی کاربر مقصد (در صورت انتقال به شخص). |
| `msg_rid` | Integer | Optional | شناسه تصادفی پیام درخواست پول. |
| `description` | String | Optional | شرح تراکنش و بابت پرداخت. |

</div>

**مقدار بازگشتی:** شیء شامل آدرس درگاه (`requestEndPoint`) و توکن تراکنش (`token`).

**نمونه کد پایتون (PEP 8):**
```python
# دریافت توکن انتقال وجه
token = await app.get_card_transfer_token(
    peer_user_id=123456789,
    description="تسویه فاکتور شماره ۱۲۳",
)
print("آدرس درگاه:", token.requestEndPoint)
```

---

### `app.get_wallet`
مشاهده اطلاعات، موجودی و وضعیت فعال بودن کیف‌پول کاربر.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء `Wallet` شامل موجودی و توکن کیف‌پول.

**نمونه کد پایتون (PEP 8):**
```python
# مشاهده وضعیت کیف‌پول
wallet = await app.get_wallet()
print("موجودی کیف‌پول:", wallet.balance)
```

---

### `app.open_gift_packet`
باز کردن پاکت هدیه دریافت شده در گروه یا چت خصوصی و واریز به کیف‌پول.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت حاوی پاکت هدیه. |
| `packet_id` | String | **Required** | شناسه یکتای پاکت هدیه. |

</div>

**مقدار بازگشتی:** شیء `PacketResponse` شامل مبلغ دریافت شده و وضعیت باز شدن.

**نمونه کد پایتون (PEP 8):**
```python
# باز کردن پاکت هدیه
packet = await app.open_gift_packet(
    chat_id="123456789|2",
    packet_id="packet_uuid_here",
)
print("مبلغ هدیه:", packet.amount)
```

---

### `app.cash_out`
تسویه و انتقال وجه از کیف‌پول بله به حساب بانکی شبا یا کارت.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | مبلغ برداشت به ریال. |
| `iban` | String | Optional | شماره شبای مقصد با پیشوند IR. |
| `pan` | String | Optional | شماره کارت بانکی مقصد. |

</div>

**مقدار بازگشتی:** شیء تاییدیه درخواست تسویه حساب.

**نمونه کد پایتون (PEP 8):**
```python
# تسویه حساب به شماره شبا
await app.cash_out(
    amount=500000,
    iban="IR123456789012345678901234",
)
```

---

## مینی‌اپ‌ها، بات‌ها و هوش مصنوعی (MiniApps & AI)

### `app.get_miniapp_url`
دریافت نشانی اینترنتی امن برای بارگذاری و اجرای مینی‌اپ اختصاصی یک ربات.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `bot_user_id` | Integer | **Required** | شناسه عددی ربات مالک وب‌اپ. |
| `screen_mode` | Integer | Optional | حالت نمایش: ۱ (تمام صفحه) یا ۲ (پنجره پاپ‌آپ). پیش‌فرض ۱. |
| `theme_params` | Dict | Optional | پارامترهای رنگ و استایل تم کلاینت. |
| `direct_link` | Dict | Optional | پارامترهای لینک مستقیم و شروع خودکار. |

</div>

**مقدار بازگشتی:** شیء شامل نشانی بازکردن مینی‌اپ (`url`).

**نمونه کد پایتون (PEP 8):**
```python
# دریافت لینک مینی‌اپ بات
miniapp = await app.get_miniapp_url(
    bot_user_id=987654321,
    screen_mode=1,
)
print("لینک وب‌اپ:", miniapp.url)
```

---

### `app.get_link_preview`
استخراج عنوان، توضیحات، آیکون و تصویر پیش‌نمایش یک پیوند اینترنتی از طریق سرویس TLDR.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `url` | String | **Required** | نشانی کامل اینترنتی وب‌سایت مورد نظر. |

</div>

**مقدار بازگشتی:** شیء شامل `title`, `description` و تصاویر پیش‌نمایش.

**نمونه کد پایتون (PEP 8):**
```python
# پیش‌نمایش پیوند
preview = await app.get_link_preview("https://ble.ir")
print("عنوان وب‌سایت:", preview.title)
```

---

### `app.get_link_summary`
خلاصه‌سازی هوشمند و مبتنی بر مدل‌های زبانی هوش مصنوعی از متن و مقاله صفحه پیوند داده شده.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `url` | String | **Required** | نشانی صفحه اینترنتی جهت خلاصه‌سازی. |

</div>

**مقدار بازگشتی:** شیء شامل فیلد `summary` (خلاصه تولید شده توسط هوش مصنوعی).

**نمونه کد پایتون (PEP 8):**
```python
# خلاصه‌سازی هوشمند با هوش مصنوعی
summary = await app.get_link_summary("https://en.wikipedia.org/wiki/Python")
print("خلاصه AI:", summary.summary)
```

---

## استوری‌ها و نظرسنجی‌ها (Stories & Polls)

### `app.get_all_stories`
بارگذاری کلیه استوری‌های جاری کاربران، مخاطبین و کانال‌های دنبال‌شده.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء Protobuf شامل لیست استوری‌ها و اطلاعات ارسال‌کنندگان.

**نمونه کد پایتون (PEP 8):**
```python
# دریافت استوری‌ها
stories = await app.get_all_stories()
print("استوری‌های فعال:", model_to_dict(stories))
```

---

### `app.react_to_story`
ارسال ری‌اکشن ایموجی یا واکنش به استوری منتشر شده کاربر.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `story_id` | String | **Required** | شناسه یکتای UUID استوری. |
| `reaction` | String | **Required** | ایموجی واکنش (مانند '🔥', '❤', '👏'). |
| `reaction_type` | Integer | Optional | نوع واکنش (پیش‌فرض ۰). |

</div>

**مقدار بازگشتی:** تاییدیه موفقیت ثبت واکنش.

**نمونه کد پایتون (PEP 8):**
```python
# واکنش به استوری
await app.react_to_story(
    story_id="story_uuid_here",
    reaction="🔥",
)
```

---

### `app.get_story_viewers`
مشاهده لیست بینندگان و آمار بازدید استوری ارسال‌شده توسط شما.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `story_id` | String | **Required** | شناسه استوری شما. |
| `page` | Integer | Optional | شماره صفحه نتایج (پیش‌فرض ۱). |
| `page_size` | Integer | Optional | تعداد بیننده در هر صفحه (پیش‌فرض ۲۰). |

</div>

**مقدار بازگشتی:** لیست کاربران مشاهده‌کننده استوری و زمان بازدید.

**نمونه کد پایتون (PEP 8):**
```python
# مشاهده بینندگان استوری
viewers = await app.get_story_viewers(
    story_id="story_uuid_here",
    page=1,
    page_size=50,
)
```

---

### `app.remove_story`
حذف استوری فعال ارسال‌شده از سرورهای بله.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `story_id` | String | **Required** | شناسه استوری جهت حذف. |

</div>

**مقدار بازگشتی:** تاییدیه موفقیت حذف استوری.

**نمونه کد پایتون (PEP 8):**
```python
# حذف استوری
await app.remove_story(story_id="story_uuid_here")
```

---

### `app.get_poll_result`
دریافت وضعیت کامل و آمار آرای گزینه‌های یک نظرسنجی با شناسه نظرسنجی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `poll_id` | Integer | **Required** | شناسه عددی نظرسنجی. |

</div>

**مقدار بازگشتی:** شیء حاوی گزینه‌ها، تعداد آرا و درصد هر گزینه.

**نمونه کد پایتون (PEP 8):**
```python
# مشاهده نتایج نظرسنجی
poll_res = await app.get_poll_result(poll_id=998877)
print("آمار آرا:", model_to_dict(poll_res))
```

---

### `app.vote_poll`
ثبت رای در نظرسنجی برای یک یا چند گزینه، یا پس گرفتن رای ثبت‌شده قبلی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `poll_id` | Integer | **Required** | شناسه عددی نظرسنجی. |
| `option_ids` | Iterable[Integer] | **Required** | لیست شناسه‌های گزینه‌های مورد نظر برای رای دادن (شروع از ۰). |
| `is_retract` | Boolean | Optional | در صورت True رای کاربر از گزینه‌ها پس گرفته می‌شود (پیش‌فرض False). |

</div>

**مقدار بازگشتی:** شیء نتیجه نظرسنجی پس از اعمال رای جدید.

**نمونه کد پایتون (PEP 8):**
```python
# ثبت رای به گزینه اول
await app.vote_poll(
    poll_id=998877,
    option_ids=[0],
)

# پس گرفتن رای
await app.vote_poll(
    poll_id=998877,
    option_ids=[0],
    is_retract=True,
)
```

---

### `app.close_poll`
بستن نظرسنجی توسط مدیر جهت جلوگیری از ثبت آرای جدید.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `poll_id` | Integer | **Required** | شناسه عددی نظرسنجی جهت خاتمه دادن. |

</div>

**مقدار بازگشتی:** تاییدیه بسته شدن نظرسنجی.

**نمونه کد پایتون (PEP 8):**
```python
# بستن نظرسنجی
await app.close_poll(poll_id=998877)
```

---

## مدیریت گروه‌ها و کانال‌ها (Groups & Channels)

### `app.create_group`
ایجاد یک گروه جدید با عنوان مشخص و افزودن کاربران اولیه.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `title` | String | **Required** | عنوان یا نام گروه جدید. |
| `user_ids` | Iterable[Integer] | Optional | شناسه‌های کاربری اعضای اولیه برای عضویت در گروه. |

</div>

**مقدار بازگشتی:** شیء `Chat` مربوط به گروه ساخته‌شده شامل شناسه `id`.

**نمونه کد پایتون (PEP 8):**
```python
# ساخت گروه جدید
group = await app.create_group(
    title="تیم توسعه‌دهندگان",
    user_ids=[123456789],
)
print("شناسه گروه:", group.id)
```

---

### `app.create_channel`
ایجاد یک کانال اطلاع‌رسانی جدید با عنوان و توضیحات مشخص.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `title` | String | **Required** | نام یا عنوان کانال. |
| `about` | String | Optional | توضیحات یا بیوگرافی کانال. |

</div>

**مقدار بازگشتی:** شیء `Chat` مربوط به کانال ساخته‌شده.

**نمونه کد پایتون (PEP 8):**
```python
# ساخت کانال جدید
channel = await app.create_channel(
    title="کانال اخبار رسمی",
    about="آخرین اطلاعیه‌ها و اخبار سامانه",
)
print("شناسه کانال:", channel.id)
```

---

### `app.export_chat_invite_link`
ساخت و دریافت نشانی اینترنتی دعوت اختصاصی (Invite Link) برای ورود اعضا به گروه یا کانال.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه یا کانال. |

</div>

**مقدار بازگشتی:** رشته آدرس لینک دعوت (مانند `https://ble.ir/join/...`).

**نمونه کد پایتون (PEP 8):**
```python
# دریافت لینک دعوت گروه
link = await app.export_chat_invite_link("123456789|2")
print("لینک عضویت:", link)
```

---

### `app.revoke_chat_invite_link`
باطل کردن لینک دعوت قبلی و صدور بلافاصله یک لینک دعوت تازه.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه یا کانال. |

</div>

**مقدار بازگشتی:** رشته لینک دعوت جدید صادرشده.

**نمونه کد پایتون (PEP 8):**
```python
# باطل کردن لینک دعوت
new_link = await app.revoke_chat_invite_link("123456789|2")
print("لینک جدید:", new_link)
```

---

### `app.promote_chat_member`
ارتقای یک عضو عادی به مدیر (Admin) با دسترسی‌های مدیریتی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه. |
| `user_id` | Integer | **Required** | شناسه کاربری عضو مورد نظر جهت ارتقا به مدیر. |

</div>

**مقدار بازگشتی:** تاییدیه موفقیت عملیات ترفیع مدیر.

**نمونه کد پایتون (PEP 8):**
```python
# ارتقای کاربر به مدیر
await app.promote_chat_member(
    chat_id="123456789|2",
    user_id=987654321,
)
```

---

### `app.remove_user_admin`
عزل یک مدیر و بازگرداندن او به وضعیت کاربر عادی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه. |
| `user_id` | Integer | **Required** | شناسه کاربری مدیر مورد نظر جهت عزل. |

</div>

**مقدار بازگشتی:** تاییدیه عزل مدیر.

**نمونه کد پایتون (PEP 8):**
```python
# عزل دسترسی ادمین
await app.remove_user_admin(
    chat_id="123456789|2",
    user_id=987654321,
)
```

---

### `app.kick_user`
اخراج عضو از گروه با قابلیت بازگشت مجدد توسط لینک دعوت.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه. |
| `user_id` | Integer | **Required** | شناسه کاربری عضو مورد نظر جهت اخراج. |

</div>

**مقدار بازگشتی:** تاییدیه اخراج عضو.

**نمونه کد پایتون (PEP 8):**
```python
# اخراج کاربر از گروه
await app.kick_user(
    chat_id="123456789|2",
    user_id=987654321,
)
```

---

### `app.ban_chat_member`
مسدودسازی کامل (Ban) یک کاربر در گروه به نحوی که دیگر نتواند ملحق شود.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه. |
| `user_id` | Integer | **Required** | شناسه کاربر جهت مسدودسازی. |

</div>

**مقدار بازگشتی:** تاییدیه مسدودسازی کاربر.

**نمونه کد پایتون (PEP 8):**
```python
# مسدود و بن کردن کاربر
await app.ban_chat_member(
    chat_id="123456789|2",
    user_id=987654321,
)
```

---

### `app.unban_chat_member`
رفع مسدودیت (Unban) کاربری که قبلاً در گروه بن شده بود.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه. |
| `user_id` | Integer | **Required** | شناسه کاربر جهت رفع مسدودسازی. |

</div>

**مقدار بازگشتی:** تاییدیه رفع مسدودسازی.

**نمونه کد پایتون (PEP 8):**
```python
# رفع بن کاربر
await app.unban_chat_member(
    chat_id="123456789|2",
    user_id=987654321,
)
```

---

### `app.set_group_slow_mode`
فعال‌سازی و تنظیم وقفه حالت آرام (Slow Mode) برای ارسال پیام اعضا در گروه.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه. |
| `seconds` | Integer | **Required** | مدت زمان وقفه بر حسب ثانیه (مثلاً ۱۰، ۳۰، ۶۰ ثانیه؛ برای غیرفعال‌سازی عدد ۰). |

</div>

**مقدار بازگشتی:** تاییدیه تنظیم اسلومود گروه.

**نمونه کد پایتون (PEP 8):**
```python
# فعال‌سازی اسلومود ۳۰ ثانیه‌ای
await app.set_group_slow_mode(
    chat_id="123456789|2",
    seconds=30,
)
```

---

### `app.get_chat_administrators`
دریافت لیست کامل مدیران یک گروه یا کانال به همراه عنوان مدیریتی هر یک.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه یا کانال. |

</div>

**مقدار بازگشتی:** لیستی از اشیاء مدیران شامل شناسه `id` و `title`.

**نمونه کد پایتون (PEP 8):**
```python
# دریافت ادمین‌های گروه
admins = await app.get_chat_administrators("123456789|2")
for admin in admins:
    print("مدیر:", admin.id, admin.title)
```

---

### `app.get_chat_members_count`
مشاهده تعداد کل اعضای فعال یک گروه یا دنبال‌کنندگان کانال.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه گروه یا کانال. |

</div>

**مقدار بازگشتی:** عدد صحیح (`int`) نشان‌دهنده تعداد اعضا.

**نمونه کد پایتون (PEP 8):**
```python
# دریافت تعداد اعضای گروه
count = await app.get_chat_members_count("123456789|2")
print("تعداد اعضا:", count)
```

---

## پیام‌های زمان‌بندی‌شده و پوشه‌ها (Schedulers & Folders)

### `app.load_scheduled_tasks`
دریافت لیست تسک‌ها و پیام‌های زمان‌بندی‌شده جهت ارسال در آینده در یک چت مشخص.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_id` | String / Integer | **Required** | شناسه چت یا گروه. |
| `task_type` | Integer | Optional | نوع تسک (پیش‌فرض ۰ برای پیام‌ها). |
| `status` | Integer | Optional | وضعیت تسک (پیش‌فرض ۰ برای در انتظار ارسال). |

</div>

**مقدار بازگشتی:** شیء Protobuf حاوی لیست تسک‌های زمان‌بندی‌شده.

**نمونه کد پایتون (PEP 8):**
```python
# دریافت تسک‌های زمان‌بندی‌شده
tasks = await app.load_scheduled_tasks("123456789|1")
print("تسک‌های زمان‌بندی:", model_to_dict(tasks))
```

---

### `app.cancel_scheduled_tasks`
لغو یک یا چند تسک یا پیام زمان‌بندی‌شده قبل از ارسال آن‌ها.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `task_ids` | Iterable[Integer] | **Required** | لیست شناسه‌های تسک‌های مورد نظر جهت لغو. |

</div>

**مقدار بازگشتی:** تاییدیه لغو تسک‌ها.

**نمونه کد پایتون (PEP 8):**
```python
# لغو پیام‌های زمان‌بندی شده
await app.cancel_scheduled_tasks(task_ids=[101, 102])
```

---

### `app.create_folder`
ایجاد یک پوشه (Folder / Tab) جدید در لیست گفتگوها جهت دسته‌بندی چت‌ها.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | String | **Required** | نام یا عنوان پوشه (مانند 'کانال‌ها', 'کاری'). |
| `chat_ids` | Iterable[String] | Optional | لیست شناسه‌های چت‌هایی که مایلید درون این پوشه قرار گیرند. |

</div>

**مقدار بازگشتی:** شیء Protobuf حاوی مشخصات پوشه ایجاد شده.

**نمونه کد پایتون (PEP 8):**
```python
# ایجاد پوشه جدید
await app.create_folder(
    name="کانال‌های خبری",
    chat_ids=["123456789|2", "987654321|2"],
)
```

---

### `app.delete_folder`
حذف یک پوشه چت بر اساس شناسه عددی آن.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `folder_id` | Integer | **Required** | شناسه عددی پوشه جهت حذف. |

</div>

**مقدار بازگشتی:** تاییدیه حذف پوشه.

**نمونه کد پایتون (PEP 8):**
```python
# حذف پوشه گفتگوها
await app.delete_folder(folder_id=12)
```

---

### `app.archive_dialogs`
انتقال یک یا چند گفتگو به بخش بایگانی (Archive) چت‌ها.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_ids` | Iterable[String] | **Required** | لیست شناسه‌های چت‌هایی که باید بایگانی شوند. |

</div>

**مقدار بازگشتی:** تاییدیه انتقال به بایگانی.

**نمونه کد پایتون (PEP 8):**
```python
# بایگانی گفتگوها
await app.archive_dialogs(chat_ids=["123456789|1"])
```

---

### `app.unarchive_dialogs`
خارج کردن گفتگوها از بایگانی و بازگرداندن آن‌ها به صندوق اصلی چت‌ها.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `chat_ids` | Iterable[String] | **Required** | لیست شناسه‌های گفتگوها. |

</div>

**مقدار بازگشتی:** تاییدیه خروج از بایگانی.

**نمونه کد پایتون (PEP 8):**
```python
# خروج گفتگو از بایگانی
await app.unarchive_dialogs(chat_ids=["123456789|1"])
```

---

## تماس‌های صوتی و تصویری Realtime (WebRTC Calls)

### `app.start_call`
آغاز یک تماس یک‌به‌یک (Peer-to-Peer) صوتی یا تصویری با کاربر دیگر.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `user_id` | Integer | **Required** | شناسه عددی کاربر مخاطب. |
| `is_video` | Boolean | Optional | تماس تصویری (True) یا صوتی (False). پیش‌فرض False. |

</div>

**مقدار بازگشتی:** شیء اطلاعات تماس شامل `call_id` و وضعیت شروع مکالمه.

**نمونه کد پایتون (PEP 8):**
```python
# آغاز تماس صوتی
call = await app.start_call(user_id=123456789)
print("شناسه تماس:", call.call_id)
```

---

### `app.receive_call`
پاسخ دادن و پذیرش یک تماس ورودی دریافتی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `call_id` | Integer | **Required** | شناسه تماس ورودی جهت پذیرش. |

</div>

**مقدار بازگشتی:** تاییدیه پذیرش تماس.

**نمونه کد پایتون (PEP 8):**
```python
# پاسخ دادن به تماس
await app.receive_call(call_id=call.call_id)
```

---

### `app.discard_call`
رد تماس یا قطع مکالمه در حال انجام.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `call_id` | Integer | **Required** | شناسه تماس جاری جهت قطع. |

</div>

**مقدار بازگشتی:** تاییدیه قطع تماس.

**نمونه کد پایتون (PEP 8):**
```python
# قطع تماس
await app.discard_call(call_id=call.call_id)
```

---

### `app.join_group_call_rtc`
اتصال بلادرنگ به سرورهای WebRTC بله مبتنی بر LiveKit در یک تماس گروهی.

<div dir="ltr" markdown="1">

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `call_id` | Integer | **Required** | شناسه عددی تماس گروهی. |
| `client_name` | String | Optional | نام نمایشی کلاینت در اتاق کنفرانس. |

</div>

**مقدار بازگشتی:** شیء `CallRtcConnection` جهت اتصال مستقیم به اتاق لایوکیت.

**نمونه کد پایتون (PEP 8):**
```python
# اتصال به اتاق کنفرانس LiveKit
conn = await app.join_group_call_rtc(call_id=123456, client_name="ربات هوشمند")
room = await conn.connect()

# کار با استریم‌های صوت و تصویر با livekit.rtc ...

await room.disconnect()
await app.leave_group_call(call_id=123456)
```

---

