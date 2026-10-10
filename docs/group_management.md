# راهنمای مدیریت گروه‌ها، کانال‌ها و ادمین‌ها در BaleNova

تمامی کدهای این صفحه مطابق با استانداردهای رسمی **PEP 8** با تایپ‌های مشخص و سازمان‌دهی تمیز توابع نوشته شده‌اند.

---

## ۱. ساخت گروه و کانال جدید

```python
import asyncio
from balenova import Client

app = Client.from_browser("auto")


async def create_communities() -> None:
    async with app:
        # ۱. ساخت گروه جدید به همراه اعضای اولیه
        group = await app.create_group(
            title="تیم توسعه‌دهندگان پایتون",
            user_ids=[123456789],
        )
        print(f"گروه ساخته شد: {group.id}")

        # ۲. ساخت کانال جدید با عنوان و توضیحات
        channel = await app.create_channel(
            title="کانال رسمی اطلاع‌رسانی",
            about="کانال آخرین بروزرسانی‌های سامانه",
        )
        print(f"کانال ساخته شد: {channel.id}")


if __name__ == "__main__":
    asyncio.run(create_communities())
```

---

## ۲. لینک دعوت، نام و توضیحات چت

```python
async def manage_chat_profile(chat_id: str) -> None:
    async with app:
        # ساخت و دریافت لینک دعوت عمومی گروه
        invite_link = await app.export_chat_invite_link(chat_id=chat_id)
        print("لینک دعوت:", invite_link)

        # ابطال لینک قبلی و صدور لینک دعوت جدید
        new_link = await app.revoke_chat_invite_link(chat_id=chat_id)
        print("لینک دعوت جدید:", new_link)

        # تغییر عنوان چت
        await app.set_chat_title(chat_id=chat_id, title="نام جدید گروه")

        # تغییر توضیحات (Bio) چت
        await app.set_chat_description(
            chat_id=chat_id,
            description="قوانین جدید گفتگو را مطالعه بفرمایید.",
        )
```

---

## ۳. مدیریت مدیران، ترفیع و محدودسازی اعضا

```python
async def manage_members_and_admins(chat_id: str, target_user_id: int) -> None:
    async with app:
        # ۱. ترفیع کاربر به مدیر (Promote)
        await app.promote_chat_member(
            chat_id=chat_id,
            user_id=target_user_id,
        )

        # ۲. عزل مدیر (Demote)
        await app.remove_user_admin(
            chat_id=chat_id,
            user_id=target_user_id,
        )

        # ۳. تنظیم حالت آرام (Slow Mode) به مدت ۳۰ ثانیه
        await app.set_group_slow_mode(
            chat_id=chat_id,
            seconds=30,
        )

        # ۴. اخراج کاربر از گروه (Kick)
        await app.kick_user(
            chat_id=chat_id,
            user_id=target_user_id,
        )

        # ۵. مسدودسازی کاربر (Ban)
        await app.ban_chat_member(
            chat_id=chat_id,
            user_id=target_user_id,
        )

        # ۶. رفع مسدودسازی کاربر (Unban)
        await app.unban_chat_member(
            chat_id=chat_id,
            user_id=target_user_id,
        )
```

---

## ۴. لیست مدیران و مشخصات کامل چت

```python
async def fetch_chat_details(chat_id: str) -> None:
    async with app:
        # تعداد اعضای گروه یا کانال
        members_count = await app.get_chat_members_count(chat_id=chat_id)
        print(f"تعداد کل اعضا: {members_count}")

        # دریافت لیست مدیران
        admins = await app.get_chat_administrators(chat_id=chat_id)
        for admin in admins:
            print(f"شناسه مدیر: {admin.id} | عنوان: {admin.title}")

        # دریافت مشخصات کامل گروه
        full_group_info = await app.get_full_group(chat_id=chat_id)
        print("اطلاعات کامل:", full_group_info)
```
