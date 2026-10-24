# 🔄 ماشین وضعیت مکالمه و فرم‌ها (Finite State Machine - FSM)

در بسیاری از ربات‌های پیشرفته (مانند ربات‌های ثبت‌نام، فروشگاهی، نظرسنجی و پشتیبانی)، لازم است ربات اطلاعات کاربر را مرحله‌به‌مرحله دریافت کند. **BaleNova** سیستم مدیریت وضعیت یکپارچه‌ای مشابه فریم‌ورک‌های مدرن پایتون در اختیار شما می‌گذارد.

---

## ۱. ساختار تعریف وضعیت‌ها (`StatesGroup`)

برای تعریف مراحل گفت‌وگو، از کلاس `StatesGroup` و اشیای `State` استفاده می‌شود:

```python
from bale.fsm import StatesGroup, State

class RegistrationForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()
    waiting_for_phone = State()
```

---

## ۲. نمونه کامل ربات ثبت‌نام چندمرحله‌ای

در این سناریو، ربات با دریافت دستور `/register` وارد اولین مرحله شده و در هر گام داده کاربر را ذخیره کرده و به گام بعدی می‌رود:

```python
from bale import Client, events, filters
from bale.fsm import StatesGroup, State, FSMContext

app = Client.from_firefox()

class RegistrationForm(StatesGroup):
    name = State()
    age = State()

# گام ۱: شروع ثبت‌نام
@app.on(events.NewMessage(pattern=r"^/register$"))
async def start_register(event, state: FSMContext):
    await state.set_state(RegistrationForm.name)
    await event.reply("به فرآیند ثبت‌نام خوش آمدید! 🌸\nلطفاً نام و نام‌خانوادگی خود را ارسال کنید:")

# گام ۲: دریافت نام و پرسش سن
@app.on(events.NewMessage(state=RegistrationForm.name))
async def process_name(event, state: FSMContext):
    # ذخیره داده در حافظه وضعیت
    await state.update_data(full_name=event.text)
    
    # انتقال به وضعیت بعدی
    await state.set_state(RegistrationForm.age)
    await event.reply(f"ممنون {event.text} عزیز! حالا لطفاً سن خود را به عدد وارد کنید:")

# گام ۳: دریافت سن و تکمیل فرآیند
@app.on(events.NewMessage(state=RegistrationForm.age))
async def process_age(event, state: FSMContext):
    if not event.text.isdigit():
        await event.reply("⚠️ لطفاً سن خود را فقط به صورت عدد انگلیسی وارد نمایید:")
        return

    data = await state.get_data()
    user_name = data.get("full_name")
    user_age = event.text
    
    # پاکسازی وضعیت کاربر
    await state.clear()
    
    summary = (
        "✅ ثبت‌نام با موفقیت به پایان رسید!\n"
        f"• نام: {user_name}\n"
        f"• سن: {user_age} سال\n\n"
        "اطلاعات شما با موفقیت در سامانه ذخیره گردید."
    )
    await event.reply(summary)

app.run()
```

---

## ۳. متدهای کلیدی کلاس `FSMContext`

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `await state.set_state(state)` | شیء `State` | تنظیم مرحله جدید برای کاربر جاری |
| `await state.get_state()` | — | دریافت نام وضعیت فعلی کاربر |
| `await state.update_data(**kwargs)` | کلید و مقادیر | ذخیره و انباشت اطلاعات موقت در حافظه کاربر |
| `await state.get_data()` | — | بازگرداندن دیکشنری تمام داده‌های ذخیره‌شده تا این لحظه |
| `await state.clear()` | — | ریست و پاکسازی کامل وضعیت و داده‌های موقت |
