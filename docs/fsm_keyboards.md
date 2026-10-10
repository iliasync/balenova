# راهنمای کیبوردها و ماشین وضعیت (FSM)

کتابخانهٔ **BaleNova** مشابه فریم‌ورک‌های مدرن پایتون (نظیر `aiogram`)، ابزارهای کاملی برای ایجاد کلیدهای شیشه‌ای (Inline)، کیبوردهای ریپلای و ماشین وضعیت گفتگو (FSM) ارائه می‌دهد.

---

## ۱. کیبوردهای اینلاین و ریپلای (Keyboards)

### کیبورد اینلاین (InlineKeyboardMarkup)
دکمه‌های شیشه‌ای که زیر پیام پیوست می‌شوند و می‌توانند حاوی لینک یا دیتای کالبک (`callback_data`) باشند:

```python
from balenova import Client, InlineKeyboardMarkup, InlineKeyboardButton, events, filters

app = Client.from_firefox()


@app.on(events.NewMessage, filters.command("panel"))
async def show_panel(event: events.NewMessage):
    markup = InlineKeyboardMarkup()

    # افزودن دکمه‌ها در یک سطر
    markup.add(
        InlineKeyboardButton("وب‌سایت بله", url="https://bale.ai"),
        InlineKeyboardButton("تأیید سفارش", callback_data="btn_confirm"),
    )

    # افزودن سطر بعدی
    markup.row(InlineKeyboardButton("پشتیبانی", callback_data="btn_support"))

    await event.reply("کنترل پنل کاربری:", reply_markup=markup)
```

### کیبورد ریپلای (ReplyKeyboardMarkup)
دکمه‌هایی که در بخش پایین صفحه (زیر ورودی چت) جایگزین کیبورد معمولی می‌شوند:

```python
from balenova import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# ساخت کیبورد با درخواست دسترسی
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.row(
    KeyboardButton("ارسال شماره موبایل 📱", request_contact=True),
    KeyboardButton("ارسال موقعیت مکانی 📍", request_location=True),
)

# ارسال کیبورد
await event.reply("لطفاً اطلاعات خود را ارسال کنید:", reply_markup=menu_kb)

# حذف کیبورد در صورت نیاز
remove_kb = ReplyKeyboardRemove()
await event.reply("کیبورد برداشته شد.", reply_markup=remove_kb)
```

---

## ۲. ماشین وضعیت و فرم‌های چندمرحله‌ای (FSM)

برای ساخت فرایندهای مرحله‌به‌مرحله مانند ثبت‌نام، نظرسنجی یا خرید:

```python
from balenova import Client, StatesGroup, State, events, filters

app = Client.from_firefox()


# ۱. تعریف گروه‌های وضعیت
class Registration(StatesGroup):
    name = State()
    phone = State()


# ۲. شروع ثبت‌نام با دستور
@app.on(events.NewMessage, filters.command("register"))
async def start_reg(event: events.NewMessage):
    fsm = event.get_fsm_context()
    await fsm.set_state(Registration.name)
    await event.reply("لطفاً نام خود را بنویسید:")


# ۳. دریافت نام و رفتن به وضعیت بعدی
@app.on(events.NewMessage, filters.state(Registration.name))
async def get_name(event: events.NewMessage):
    fsm = event.get_fsm_context()
    await fsm.update_data(user_name=event.text)

    await fsm.set_state(Registration.phone)
    await event.reply(f"ممنون {event.text}! حالا شماره تماس را وارد کنید:")


# ۴. دریافت شماره و اتمام فرایند
@app.on(events.NewMessage, filters.state(Registration.phone))
async def get_phone(event: events.NewMessage):
    fsm = event.get_fsm_context()
    data = await fsm.get_data()
    user_name = data.get("user_name")

    # پاکسازی وضعیت برای پیام‌های بعدی
    await fsm.clear()

    await event.reply(f"ثبت‌نام کامل شد!\nنام: {user_name}\nتلفن: {event.text}")


app.run_forever()
```
