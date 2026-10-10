# راهنمای کامل ارسال پیام و فایل در BaleNova

کتابخانهٔ **BaleNova** متدهای سطح‌بالا و ساده‌ای را شبیه به فریم‌ورک‌های مدرن تلگرام (مانند `aiogram`) در اختیارتان می‌گذارد تا بدون درگیر شدن با پروتکل‌های پیچیدهٔ وب و ساختارهای داخلی Protobuf، انواع پیام و رسانه را ارسال و مدیریت کنید.

---

## ۱. ارسال پیام متنی ساده

برای ارسال پیام متنی، کافی است شناسهٔ چت یا کاربر را بدهید:

```python
from balenova import Client

app = Client.from_firefox()

async def main():
    async with app:
        # ارسال به چت، گروه یا کاربر
        msg = await app.send_message("123456789|1", "سلام! این یک پیام آزمایشی با BaleNova است.")
        print(f"پیام با شناسه {msg.id} ارسال شد.")

app.run(main())
```

---

## ۲. ارسال عکس و ویدیو

می‌توانید عکس یا ویدیو را با ارسال مسیر فایل محلی یا بایت‌های مستقیم ارسال کنید:

```python
# ارسال تصویر همراه با کپشن
await app.send_photo(
    "123456789|1",
    photo="banner.png",
    caption="تصویر جدید وب‌سایت 🖼️"
)

# ارسال ویدیو با ابعاد و مدت زمان
await app.send_video(
    "123456789|1",
    video="tutorial.mp4",
    caption="آموزش کار با بات 🎬"
)
```

---

## ۳. ارسال فایل، وویس و استیکر

```python
# ارسال سند یا فایل دلخواه (PDF، زیپ و ...)
await app.send_document(
    "123456789|1",
    document="report.pdf",
    caption="گزارش نهایی ماهانه 📄"
)

# ارسال صدای ضبط‌شده (Voice)
await app.send_voice(
    "123456789|1",
    voice="voice.ogg",
    duration=12
)

# ارسال استیکر بله
await app.send_sticker(
    "123456789|1",
    sticker="<file_id>:<access_hash>:<storage_version>:<sticker_id>:<collection_id>"
)
```

---

## ۴. فوروارد، ویرایش و حذف پیام

```python
# فوروارد پیام به چت دیگر
await app.forward_message(
    from_chat_id="123456789|1",
    to_chat_id="987654321|2",
    message_id=msg.id
)

# کپی کردن پیام (ارسال مجدد بدون تگ فوروارد)
await app.copy_message(
    from_chat_id="123456789|1",
    to_chat_id="987654321|2",
    message_id=msg.id
)

# ویرایش متن پیام ارسال‌شده
await app.edit_message_text(
    chat_id="123456789|1",
    message_id=msg.id,
    text="متن ویرایش‌شده جدید ✍️"
)

# حذف پیام
await app.delete_message(
    chat_id="123456789|1",
    message_id=msg.id
)
```

---

## ۵. پین کردن و واکنش (Reaction) به پیام‌ها

```python
# پین کردن پیام در گروه یا چت
await app.pin_message(chat_id="123456789|2", message_id=msg.id)

# برداشتن پین پیام
await app.unpin_message(chat_id="123456789|2", message_id=msg.id)

# ثبت واکنش (ایموجی) روی پیام
await app.message_set_reaction(
    chat_id="123456789|1",
    message_id=msg.id,
    reaction="👍"
)
```
