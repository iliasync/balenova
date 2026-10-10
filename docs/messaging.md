# راهنمای کامل ارسال پیام، رسانه و مدیریت گفتگو در BaleNova

کتابخانهٔ **BaleNova** متدهای سطح‌بالا، تایپ‌شده و کاملاً مطابق با استانداردهای **PEP 8** را برای ارسال انواع پیام متنی، رسانه و اسناد در اختیارتان می‌گذارد.

---

## ۱. ارسال پیام متنی و پاسخ (Text & Reply)

برای ارسال پیام متنی ساده و پاسخ به پیام‌ها طبق قراردادهای PEP 8:

```python
import asyncio
from balenova import Client, events

app = Client.from_browser("auto")


@app.on(events.NewMessage)
async def handle_message(event: events.NewMessage) -> None:
    # ارسال پاسخ مستقیم به فرستنده
    await event.reply("پیام شما دریافت شد!")


async def send_direct() -> None:
    async with app:
        # ارسال پیام به شناسه کاربری یا گروه
        message = await app.send_message(
            chat_id="123456789|1",
            text="سلام! این یک پیام آزمایشی است.",
        )
        print(f"پیام با شناسه {message.id} ارسال شد.")


if __name__ == "__main__":
    asyncio.run(send_direct())
```

---

## ۲. ارسال تصاویر و ویدیوها (Photos & Videos)

امکان ارسال با مسیر محلی (`str` / `Path`) یا بافر باینری (`bytes`):

```python
from pathlib import Path
from balenova import Client

app = Client.from_browser("auto")


async def send_media_examples(chat_id: str) -> None:
    async with app:
        # ۱. ارسال تصویر با کپشن
        photo_path = Path("assets/banner.png")
        if photo_path.exists():
            await app.send_photo(
                chat_id=chat_id,
                photo=photo_path,
                caption="تصویر اطلاعیه رسمی 🖼️",
            )

        # ۲. ارسال ویدیو با مدت زمان و ابعاد
        await app.send_video(
            chat_id=chat_id,
            video="media/tutorial.mp4",
            duration=35,
            caption="آموزش ویدیویی کار با بات 🎬",
        )
```

---

## ۳. ارسال فایل‌ها، صدا و استیکر (Documents, Voice, Stickers)

```python
async def send_documents_and_voice(chat_id: str) -> None:
    async with app:
        # ۱. ارسال سند PDF یا آرشیو ZIP
        await app.send_document(
            chat_id=chat_id,
            document="documents/report.pdf",
            caption="گزارش عملکرد ماهانه 📄",
        )

        # ۲. ارسال صدای ضبط‌شده (Voice Message)
        await app.send_voice(
            chat_id=chat_id,
            voice="audio/memo.ogg",
            duration=12,
        )

        # ۳. ارسال استیکر رسمی بله
        sticker_spec = (
            "<file_id>:<access_hash>:<storage_version>:<sticker_id>:<collection_id>"
        )
        await app.send_sticker(
            chat_id=chat_id,
            sticker=sticker_spec,
        )
```

---

## ۴. فوروارد، کپی، ویرایش و حذف پیام (Message Actions)

```python
async def message_actions_example(
    from_chat: str,
    to_chat: str,
    message_id: int,
) -> None:
    async with app:
        # فوروارد پیام با برچسب فرستنده اصلی
        await app.forward_message(
            from_chat_id=from_chat,
            to_chat_id=to_chat,
            message_id=message_id,
        )

        # کپی پیام بدون درج برچسب فوروارد
        await app.copy_message(
            from_chat_id=from_chat,
            to_chat_id=to_chat,
            message_id=message_id,
        )

        # ویرایش متن پیام ارسال شده
        await app.edit_message_text(
            chat_id=to_chat,
            message_id=message_id,
            text="متن ویرایش‌شده جدید ✍️",
        )

        # حذف پیام برای طرفین
        await app.delete_message(
            chat_id=to_chat,
            message_id=message_id,
        )
```

---

## ۵. سنجاق کردن (Pin) و واکنش‌ها (Reactions)

```python
async def pin_and_react(chat_id: str, message_id: int) -> None:
    async with app:
        # سنجاق کردن پیام در چت یا گروه
        await app.pin_message(chat_id=chat_id, message_id=message_id)

        # ثبت واکنش ایموجی روی پیام
        await app.message_set_reaction(
            chat_id=chat_id,
            message_id=message_id,
            reaction="❤️",
        )

        # برداشتن سنجاق پیام
        await app.unpin_message(chat_id=chat_id, message_id=message_id)
```
