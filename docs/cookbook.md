# 🍳 کتاب آشپزی (Cookbook & Practical Recipes)

مجموعه‌ای از کامل‌ترین و کاربردی‌ترین نمونه‌کدهای آماده برای ساخت ربات‌ها و ابزارهای دنیای واقعی با کتابخانه **BaleNova**.

---

## ۱. ربات منشی و پشتیبانی (Support Assistant Bot)

پیام‌های ارسالی کاربران در پی‌وی را دریافت کرده و به ادمین فوروارد می‌کند؛ پاسخ‌های ادمین نیز مستقیماً به کاربر ریپلای می‌شود.

```python
from balenova import Client, events

app = Client.from_firefox()
ADMIN_ID = "2065995342|1"  # شناسه ادمین

@app.on(events.NewMessage(incoming=True))
async def support_handler(event: events.NewMessage):
    # اگر پیام از چت خصوصی غیر از ادمین باشد، به ادمین فوروارد کن
    if event.is_private and event.chat_id != ADMIN_ID:
        info_text = f"📩 پیام جدید از {event.from_user.full_name} (`{event.from_user.id}`):"
        await app.send_message(ADMIN_ID, info_text)
        await event.forward(ADMIN_ID)
        await event.reply("پیام شما به پشتیبانی ارسال شد. به زودی پاسخ خواهیم داد 🙏")

    # اگر ادمین روی پیامی ریپلای کرد، پاسخ را به کاربر مقصد بفرست
    elif event.chat_id == ADMIN_ID and event.is_reply:
        # منطق استخراج کاربر و ارسال پاسخ
        await event.reply("پاسخ شما برای کاربر ارسال گردید ✅")

app.run()
```

---

## ۲. ربات ناظر و ضداسپم گروه (Group Guardian Bot)

حذف پیام‌های حاوی کلمات غیراخلاقی، لینک‌های ناشناس، و اخراج کاربران متخلف.

```python
from balenova import Client, events

app = Client.from_firefox()
BAD_WORDS = ["تبلیغات", "عضویت در کانال", "شارژ رایگان"]

@app.on(events.NewMessage(incoming=True))
async def moderation_handler(event: events.NewMessage):
    # بررسی فقط در گروه‌ها
    if not event.is_group:
        return

    text = event.text.lower()
    for word in BAD_WORDS:
        if word in text:
            # ۱. حذف پیام اسپم
            await event.delete()
            
            # ۲. هشدار به کاربر
            warning = f"⚠️ کاربر {event.from_user.mention} ارسال این محتوا مجاز نیست!"
            await event.respond(warning)
            break

app.run()
```

---

## ۳. ربات دانلودر خودکار مدیا (Auto Media Downloader)

دانلود خودکار تصاویر و اسناد ارسالی کاربران و ذخیره آنها روی دیسک.

```python
import os
from balenova import Client, events

app = Client.from_firefox()
SAVE_DIR = "downloads"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.on(events.NewMessage(incoming=True))
async def media_downloader(event: events.NewMessage):
    if event.message.photo:
        await event.reply("در حال دانلود تصویر... ⏳")
        data = await event.message.photo.download()
        file_path = os.path.join(SAVE_DIR, f"photo_{event.id}.jpg")
        with open(file_path, "wb") as f:
            f.write(data)
        await event.reply(f"تصویر با موفقیت در سرور ذخیره شد ✅ ({len(data)} بایت)")

    elif event.message.document:
        await event.reply("در حال دریافت فایل... ⏳")
        data = await event.message.document.download()
        name = event.message.document.file_name or f"doc_{event.id}.bin"
        with open(os.path.join(SAVE_DIR, name), "wb") as f:
            f.write(data)
        await event.reply(f"فایل {name} با موفقیت ذخیره گردید ✅")

app.run()
```

---

## ۴. ربات دکمه‌های چند مرحله‌ای (FSM Interactive Bot)

فرم ثبت نام مرحله‌به‌مرحله با ذخیره موقت وضعیت در حافظه:

```python
from balenova import Client, filters
from balenova.fsm import State, StatesGroup
from balenova.types import Message

app = Client.from_firefox()

# ۱. تعریف مراحل فرم
class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()

@app.on_message(filters.command("register"))
async def start_register(client: Client, message: Message):
    ctx = message.get_fsm_context()
    await ctx.set_state(Registration.waiting_for_name)
    await message.reply("لطفاً نام و نام خانوادگی خود را ارسال کنید:")

@app.on_message(filters.state(Registration.waiting_for_name))
async def process_name(client: Client, message: Message):
    ctx = message.get_fsm_context()
    await ctx.update_data(user_name=message.text)
    await ctx.set_state(Registration.waiting_for_age)
    await message.reply(f"تشکر {message.text}! اکنون سن خود را وارد نمایید:")

@app.on_message(filters.state(Registration.waiting_for_age))
async def process_age(client: Client, message: Message):
    ctx = message.get_fsm_context()
    data = await ctx.get_data()
    name = data.get("user_name")
    age = message.text
    
    # اتمام فرم
    await ctx.finish()
    await message.reply(f"ثبت‌نام شما نهایی شد! 🎉\nنام: {name}\nسن: {age}")

app.run()
```
