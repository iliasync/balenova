# 🎛️ کیبوردها و تعاملات دکمه‌ای (Keyboards & Buttons)

پیام‌رسان بله از هر دو نوع کیبورد استاندارد پشتیبانی می‌کند:
1. **کیبورد شیشه‌ای (اینلاین یا زیرپیام)**: دکمه‌هایی که دقیقاً زیر پیام ارسالی قرار گرفته و با کلیک روی آنها می‌توان لینک باز کرد یا رویداد Callback ارسال نمود.
2. **کیبورد سفارشی (ریپلای یا پایین صفحه)**: دکمه‌هایی که به جای کیبورد لمسی گوشی در پایین چت قرار می‌گیرند و متنی را تایپ یا شماره تماس را ارسال می‌کنند.

---

## ۱. کیبورد شیشه‌ای (`InlineKeyboardMarkup`)

### مشخصات فیلدهای دکمه اینلاین (`InlineKeyboardButton`)
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `text` | `str` | <span class="badge required">Yes</span> | — | متن نمایشی روی دکمه |
| `url` | `Optional[str]` | <span class="badge optional">No</span> | `None` | آدرس لینکی که با کلیک در مرورگر باز می‌شود |
| `callback_data` | `Optional[str]` | <span class="badge optional">No</span> | `None` | داده متنی ارسالی به سرور ربات در صورت کلیک |

### نمونه ساخت کیبورد اینلاین چندسطحی
```python
from bale.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup([
    # ردیف اول: دو دکمه در یک خط
    [
        InlineKeyboardButton("📦 محصولات ما", callback_data="btn_products"),
        InlineKeyboardButton("🛍️ سبد خرید", callback_data="btn_cart"),
    ],
    # ردیف دوم: یک دکمه عریض
    [
        InlineKeyboardButton("🌐 ورود به سایت رسمی", url="https://github.com/iliasync/balenova")
    ]
])

await client.send_message(
    chat_id="pv_ilia",
    text="به فروشگاه بله خوش آمدید! یکی از گزینه‌ها را انتخاب کنید:",
    reply_markup=keyboard
)
```

---

## ۲. هندل کردن رویداد کلیک اینلاین (`CallbackQuery`)

زمانی که کاربر روی یک دکمه شیشه‌ای حاوی `callback_data` کلیک می‌کند، یک رویداد از نوع `events.CallbackQuery` دریافت می‌شود:

```python
from bale import Client, events

client = Client("bot_session")

@client.on(events.CallbackQuery)
async def handle_callbacks(event):
    data = event.data
    user_id = event.sender_id
    
    if data == "btn_products":
        await event.answer("در حال بارگذاری لیست محصولات...")
        await event.edit("لیست محصولات فعال:\n۱. بسته طلایی\n۲. بسته نقره‌ای")
    elif data == "btn_cart":
        await event.answer("سبد خرید شما در حال حاضر خالی است!", alert=True)

client.run()
```

---

## ۳. کیبورد پایین صفحه (`ReplyKeyboardMarkup`)

### مشخصات فیلدهای کیبورد ریپلای
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `keyboard` | `List[List[KeyboardButton]]` | <span class="badge required">Yes</span> | — | ماتریس ردیف‌ها و دکمه‌ها |
| `resize_keyboard` | `bool` | <span class="badge optional">No</span> | `True` | بهینه‌سازی و اندازه متناسب کیبورد |
| `one_time_keyboard` | `bool` | <span class="badge optional">No</span> | `False` | مخفی شدن کیبورد پس از یکبار استفاده |

### دکمه‌های ریپلای (`KeyboardButton`)
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `text` | `str` | <span class="badge required">Yes</span> | — | متن دکمه که با لمس آن ارسال می‌شود |
| `request_contact` | `bool` | <span class="badge optional">No</span> | `False` | درخواست ارسال شماره تلفن تاییدشده کاربر |

### نمونه ساخت کیبورد ریپلای با درخواست شماره موبایل
```python
from bale.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📱 ثبت‌نام با شماره همراه", request_contact=True)],
        [KeyboardButton("📄 شرایط و قوانین"), KeyboardButton("❓ راهنما")]
    ],
    resize_keyboard=True
)

await client.send_message(
    chat_id="pv_ilia",
    text="برای دسترسی به پنل کاربری، شماره خود را با دکمه زیر ارسال نمایید:",
    reply_markup=menu
)
```

### حذف کیبورد پایین صفحه (`ReplyKeyboardRemove`)
```python
from bale.types import ReplyKeyboardRemove

await client.send_message(
    chat_id="pv_ilia",
    text="کیبورد منو حذف گردید.",
    reply_markup=ReplyKeyboardRemove()
)
```
