# راهنمای کیبوردها و ماشین وضعیت گفتگو (FSM)

این راهنما بر اساس استانداردهای کدنویسی **PEP 8** نگارش شده و نحوه ساخت کیبوردهای شیشه‌ای، کیبوردهای پاسخ و مدیریت مراحل فرم‌ها را تشریح می‌کند.

---

## ۱. کیبوردهای اینلاین شیشه‌ای (InlineKeyboardMarkup)

کلیدهای شیشه‌ای زیر پیام قرار می‌گیرند و برای باز کردن لینک‌ها یا ارسال داده‌های بازگشتی (`callback_data`) کاربرد دارند:

```python
from balenova import Client, events, filters
from balenova.keyboards import InlineKeyboardButton, InlineKeyboardMarkup

app = Client.from_browser("auto")


def build_main_inline_keyboard() -> InlineKeyboardMarkup:
    """ساخت کیبورد اینلاین اصلی با ساختار ردیف‌های منظم."""
    return (
        InlineKeyboardMarkup()
        .row(
            InlineKeyboardButton(
                text="🌐 سایت مستندات",
                url="https://iliasync.github.io/balenova/",
            ),
            InlineKeyboardButton(
                text="⚡ استعلام حساب",
                callback_data="btn_check_account",
            ),
        )
        .row(
            InlineKeyboardButton(
                text="🎮 اجرای مینی‌اپ",
                web_app_url="https://app.bale.ai",
            ),
            InlineKeyboardButton(
                text="📞 پشتیبانی",
                callback_data="btn_support",
            ),
        )
    )


@app.on(events.NewMessage, filters.command("panel"))
async def handle_panel_command(event: events.NewMessage) -> None:
    keyboard = build_main_inline_keyboard()
    await event.reply("کنترل پنل کاربری:", reply_markup=keyboard)
```

---

## ۲. کیبوردهای پاسخ زیرین (ReplyKeyboardMarkup)

این دکمه‌ها در پایین صفحه جایگزین صفحه کلید دستگاه می‌شوند:

```python
from balenova.keyboards import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


def build_contact_reply_keyboard() -> ReplyKeyboardMarkup:
    """ساخت کیبورد پاسخ با درخواست دسترسی شماره و موقعیت."""
    return (
        ReplyKeyboardMarkup(resize_keyboard=True)
        .row(
            KeyboardButton(
                text="📱 ارسال شماره من",
                request_contact=True,
            ),
            KeyboardButton(
                text="📍 ارسال موقعیت مکانی",
                request_location=True,
            ),
        )
        .row(
            KeyboardButton(text="ℹ️ اطلاعات حساب"),
            KeyboardButton(text="❌ انصراف"),
        )
    )


@app.on(events.NewMessage, filters.command("menu"))
async def handle_menu_command(event: events.NewMessage) -> None:
    reply_kb = build_contact_reply_keyboard()
    await event.reply("لطفاً یک گزینه را انتخاب کنید:", reply_markup=reply_kb)


@app.on(events.NewMessage, filters.text == "❌ انصراف")
async def handle_cancel(event: events.NewMessage) -> None:
    # حذف کامل کیبورد از صفحه کاربر
    remove_kb = ReplyKeyboardRemove()
    await event.reply("منو بسته شد.", reply_markup=remove_kb)
```

---

## ۳. ماشین وضعیت گفتگو و فرم‌های چندمرحله‌ای (FSM)

سیستم FSM توکار برای نگهداری مقادیر موقت کاربران بدون تداخل پیام‌ها طراحی شده است:

```python
from balenova import Client, events, filters
from balenova.fsm import State, StatesGroup

app = Client.from_browser("auto")


class UserProfileForm(StatesGroup):
    """تعریف مراحل فرم دریافت مشخصات کاربری."""

    waiting_for_name = State()
    waiting_for_age = State()
    waiting_for_city = State()


# مرحله ۱: شروع دریافت مشخصات
@app.on(events.NewMessage, filters.command("signup"))
async def start_signup(event: events.NewMessage) -> None:
    fsm = event.get_fsm_context()
    await fsm.set_state(UserProfileForm.waiting_for_name)
    await event.reply("سلام! لطفاً نام و نام خانوادگی خود را ارسال کنید:")


# مرحله ۲: اعتبارسنجی نام و رفتن به سن
@app.on(events.NewMessage, filters.state(UserProfileForm.waiting_for_name))
async def process_name(event: events.NewMessage) -> None:
    fsm = event.get_fsm_context()
    full_name = event.text.strip()

    if len(full_name) < 3:
        await event.reply("نام وارد شده کوتاه است. لطفاً نام کامل را بنویسید:")
        return

    await fsm.update_data(full_name=full_name)
    await fsm.set_state(UserProfileForm.waiting_for_age)
    await event.reply(f"متشکرم {full_name}! حالا سن خود را وارد کنید:")


# مرحله ۳: اعتبارسنجی سن و رفتن به شهر
@app.on(events.NewMessage, filters.state(UserProfileForm.waiting_for_age))
async def process_age(event: events.NewMessage) -> None:
    fsm = event.get_fsm_context()

    if not event.text.isdigit():
        await event.reply("لطفاً سن خود را فقط به صورت عدد بنویسید:")
        return

    await fsm.update_data(age=int(event.text))
    await fsm.set_state(UserProfileForm.waiting_for_city)
    await event.reply("در کدام شهر سکونت دارید؟")


# مرحله ۴: دریافت شهر و ذخیره نهایی
@app.on(events.NewMessage, filters.state(UserProfileForm.waiting_for_city))
async def process_city(event: events.NewMessage) -> None:
    fsm = event.get_fsm_context()
    data = await fsm.get_data()

    # پاکسازی وضعیت FSM پس از پایان فرم
    await fsm.clear()

    full_name = data.get("full_name")
    age = data.get("age")
    city = event.text.strip()

    summary = (
        "🎉 ثبت‌نام با موفقیت انجام شد:\n"
        f"👤 نام: {full_name}\n"
        f"🎂 سن: {age}\n"
        f"🏙️ شهر: {city}"
    )
    await event.reply(summary)


if __name__ == "__main__":
    app.run_forever()
```
