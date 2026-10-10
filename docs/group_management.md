# راهنمای مدیریت گروه‌ها و کانال‌ها در BaleNova

مدیریت جامع گروه‌ها، کانال‌ها، تنظیمات مدیران و اعضا از طریق متدهای ساده و خوانا:

---

## ۱. ساخت گروه و کانال

```python
from balenova import Client

app = Client.from_firefox()

async def main():
    async with app:
        # ایجاد گروه جدید با کاربران اولیه
        group = await app.create_group(
            title="تیم توسعه BaleNova",
            user_ids=[123456789]
        )
        print(f"گروه ساخته شد: {group.id}")

        # ایجاد کانال جدید
        channel = await app.create_channel(
            title="اخبار و اطلاع‌رسانی BaleNova",
            about="کانال رسمی بروزرسانی‌های کتابخانه"
        )
        print(f"کانال ساخته شد: {channel.id}")

app.run(main())
```

---

## ۲. دریافت لینک دعوت و تغییر مشخصات چت

```python
chat_id = "123456789|2"

# دریافت لینک دعوت گروه
invite_link = await app.export_chat_invite_link(chat_id)
print("لینک دعوت:", invite_link)

# باطل کردن و ساخت مجدد لینک دعوت
new_link = await app.revoke_chat_invite_link(chat_id)

# تغییر عنوان و توضیحات
await app.set_chat_title(chat_id, "نام جدید گروه")
await app.set_chat_description(chat_id, "قوانین جدید گروه را رعایت کنید.")
```

---

## ۳. مدیریت مدیران و دسترسی‌های کاربران

```python
target_user = 987654321

# ارتقای کاربر به مدیر گروه (Promote)
await app.promote_chat_member(chat_id, user_id=target_user)

# عزل مدیر (Demote)
await app.remove_user_admin(chat_id, user_id=target_user)

# اخراج کاربر از گروه (Kick)
await app.kick_user(chat_id, user_id=target_user)

# مسدود و بن کردن کاربر
await app.ban_chat_member(chat_id, user_id=target_user)

# رفع مسدودیت کاربر
await app.unban_chat_member(chat_id, user_id=target_user)
```

---

## ۴. لیست مدیران و اعضای گروه

```python
# دریافت تعداد اعضای گروه
count = await app.get_chat_members_count(chat_id)
print(f"تعداد اعضا: {count}")

# لیست مدیران گروه
admins = await app.get_chat_administrators(chat_id)
for admin in admins:
    print(f"مدیر: {admin.id} - {admin.title}")

# دریافت اطلاعات کامل گروه
full_group = await app.get_full_group(chat_id)
```
