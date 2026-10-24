# 📦 مرجع انواع داده و مدل‌ها (Types & Data Models)

تمامی اشیای دریافتی و ارسالی در **BaleNova** بر پایه کلاس‌های داده پایتونیک (`dataclass`) با تایپینگ قوی و ساختار استاندارد تلگرام پیاده‌سازی شده‌اند. شما می‌توانید مستقیماً از طریق ویژگی‌ها (Dot-Access) به تمامی فیلدها دسترسی داشته و از متدهای تعبیه‌شده اکتیو رکورد استفاده نمایید.

---

## فهرست اشیای اصلی
| نوع شیء (Type) | توضیحات |
| :--- | :--- |
| [`Message`](#message) | شیء پیام حاوی متن، فرستنده، رسانه و اکشن‌های فعال (`reply`, `edit`, `delete`, `download`) |
| [`User`](#user) | نمایانگر حساب یک کاربر یا ربات در بله |
| [`Chat`](#chat) | نمایانگر گفت‌وگوی دوطرفه (PV)، گروه (Group) یا کانال (Channel) |
| [`Dialog`](#dialog) | نمایانگر خلاصه یک گفتگو در صفحه اصلی (لیست چت‌ها) همراه با تعداد پیام ناخوانده |
| [`CallbackQuery`](#callbackquery) | شیء دریافتی هنگام کلیک کاربر روی دکمه شیشه‌ای اینلاین |
| [`ChatPermissions`](#chatpermissions) | دسترسی‌ها و محدودیت‌های اعضای گروه |
| [`Contact`](#contact) | اطلاعات کارت مخاطب و شماره تلفن |
| [`Location`](#location) | موقعیت مکانی جغرافیایی (عرض و طول جغرافیایی) |
| [`Photo`](#photo) | شیء رسانه تصویر ارسال‌شده در چت |
| [`Document`](#document) | شیء سند یا فایل بدون فشرده‌سازی |
| [`Audio`](#audio) | شیء فایل صوتی یا موسیقی |
| [`Voice`](#voice) | شیء پیام صوتی ضبط‌شده (ویس) با شکل‌موج |
| [`Video`](#video) | شیء فایل ویدیویی با ابعاد و مدت زمان |
| [`Sticker`](#sticker) | شیء استیکر بله با ایموجی متناظر |
| [`InlineKeyboardMarkup`](#inlinekeyboardmarkup) | ماتریس دکمه‌های شیشه‌ای متصل به پیام |
| [`ReplyKeyboardMarkup`](#replykeyboardmarkup) | کیبورد سفارشی پایین صفحه |

---

## `Message`
<span class="badge telethon">Active Record</span>

نمایانگر یک پیام در پیام‌رسان بله است. تمامی پیام‌های دریافتی از رویدادها یا خروجی متدهای ارسال از این نوع هستند.

### Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` | شناسه یکتای عددی پیام در گفت‌وگو |
| `chat` | [`Chat`](#chat) | شیء گفت‌وگو (چت، گروه یا کانالی که پیام در آن است) |
| `from_user` | `Optional[`[`User`](#user)`]` | فرستنده پیام (در صورت ارسال توسط کاربر) |
| `text` | `str` | متن پیام یا کپشن رسانه ارسالی |
| `date` | `int` | زمان ارسال پیام به وقت یونیکس (Unix Timestamp) |
| `reply_to_message_id` | `Optional[int]` | شناسه پیامی که این پیام در پاسخ به آن ارسال شده است |
| `forward_from` | `Optional[`[`User`](#user)`]` | فرستنده اصلی پیام در صورت فوروارد شدن |
| `media` | `Optional[Union[Photo, Document, Audio, Video, Voice, Sticker, Location, Contact]]` | شیء رسانه پیوست‌شده به پیام |
| `is_outgoing` | `bool` | آیا پیام توسط خود ما ارسال شده است؟ |
| `raw` | `dict` | دیکشنری کامل و خام دریافتی از سرور بله |

### Active Methods
| Method | Parameters | Description |
| :--- | :--- | :--- |
| `reply(text, ...)` | `text: str, reply_markup=None` | ارسال مستقیم پاسخ روی همین پیام |
| `edit(text)` | `text: str` | ویرایش فوری متن همین پیام |
| `delete()` | — | حذف همین پیام از تاریخچه چت |
| `pin()` | — | پین و سنجاق کردن این پیام در بالای گروه یا چت |
| `react(emoji)` | `emoji: str` | ثبت سریع یک ایموجی واکنش (مانند "❤️", "👍") روی پیام |
| `download()` | — | دانلود مستقیم رسانه موجود در پیام به صورت بایت خام (`bytes`) |

##### Code Example کاربردی
```python
@client.on(events.NewMessage)
async def message_handler(event):
    msg: Message = event.message
    
    # پاسخ مستقیم:
    reply = await msg.reply("پیام دریافت شد! 🌸")
    
    # ری‌اکشن:
    await msg.react("🔥")
    
    # دانلود در صورت وجود فایل:
    if msg.media:
        data = await msg.download()
        print(f"فایل با حجم {len(data)} بایت دانلود شد.")
```

---

## `User`
نمایانگر یک کاربر، مخاطب، یا حساب ربات در پیام‌رسان بله.

### Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` | شناسه عددی و یکتای کاربر در بله |
| `name` | `str` | نام و نام خانوادگی نمایشی کاربر |
| `username` | `Optional[str]` | شناسه عمومی کاربر (یوزرنیم بدون علامت `@`) |
| `phone` | `Optional[str]` | شماره تلفن کاربر (در صورت وجود دسترسی در حریم خصوصی) |
| `about` | `Optional[str]` | متن وضعیت یا بیوگرافی کاربر |
| `is_bot` | `bool` | آیا این حساب یک ربات است؟ |
| `is_self` | `bool` | آیا این حساب متعلق به خود کاربر متصل (لاگین‌شده) است؟ |
| `raw` | `dict` | دیکشنری کامل سرور |

### ویژگی‌ها و میان‌برها (Properties)
- `mention`: ساخت نام کاربری به صورت `@username` یا لینک مستقیم به کاربر.
- `first_name`: استخراج بخش اول نام نمایشی.

---

## `Chat`
نمایانگر یک محیط گفت‌وگو شامل چت دونفره خصوصی، گروه، یا کانال اطلاع‌رسانی.

### Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `Union[int, str]` | شناسه یکتای گفت‌وگو در بله |
| `title` | `str` | عنوان گروه، نام کانال یا نام مخاطب در چت خصوصی |
| `type` | `ChatType` | نوع چت از `bale.enums.ChatType` (`PRIVATE`, `GROUP`, `CHANNEL`) |
| `username` | `Optional[str]` | نام کاربری عمومی کانال یا گروه عمومی |
| `about` | `Optional[str]` | توضیحات و بیوگرافی گروه یا کانال |
| `members_count` | `Optional[int]` | تعداد اعضای حاضر در گروه یا کانال |
| `raw` | `dict` | داده‌های خام دریافتی |

### ویژگی‌ها (Properties)
- `is_private`: برابر `True` اگر گفت‌وگو از نوع پی‌وی خصوصی باشد.
- `is_group`: برابر `True` اگر گفت‌وگو یک گروه عادی یا سوپرگروه باشد.
- `is_channel`: برابر `True` اگر گفت‌وگو یک کانال بله باشد.

---

## `Dialog`
نمایانگر یک ردیف در صفحه فهرست گفتگوها.

### Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `Union[int, str]` | شناسه چت مرتبط با این دیالوگ |
| `title` | `str` | عنوان یا نام چت |
| `unread_count` | `int` | تعداد پیام‌های خوانده‌نشده |
| `last_message` | `Optional[Message]` | آخرین پیام تبادل‌شده |
| `is_pinned` | `bool` | وضعیت سنجاق بودن چت |
| `is_muted` | `bool` | وضعیت سایلنت بودن |

---

## `CallbackQuery`
شیء رویداد لمس دکمه شیشه‌ای (اینلاین) توسط کاربر.

### Fields و متدها
| Field / Method | Type | Description |
| :--- | :--- | :--- |
| `data` | `str` | داده ارسالی از دکمه (`callback_data`) |
| `from_user` | [`User`](#user) | کاربری که دکمه را لمس کرده |
| `message` | `Optional[Message]` | پیامی که دکمه زیر آن قرار دارد |
| `await answer(text, alert=False)` | — | نمایش اعلان متنی یا پاپ‌آپ پاپ‌آپ آلرت به کاربر |
| `await edit(text, ...)` | — | ویرایش سریع پیامی که دکمه زیر آن است |

---

## `ChatPermissions`
تنظیم مجوزها و دسترسی‌های کاربران در گروه‌ها.

| Field | Type | Default | Description |
| :--- | :--- | :---: | :--- |
| `can_send_messages` | `bool` | `True` | اجازه ارسال پیام متنی |
| `can_send_media` | `bool` | `True` | اجازه ارسال عکس و ویدیو و فایل |
| `can_send_polls` | `bool` | `True` | اجازه ارسال نظرسنجی |
| `can_invite_users` | `bool` | `True` | اجازه افزودن دوستان به گروه |
| `can_pin_messages` | `bool` | `False` | اجازه سنجاق پیام |
| `can_change_info` | `bool` | `False` | اجازه تغییر نام و بیوگرافی گروه |

---

## `Location` و `Contact`

### `Location`
| Field | Type | Description |
| :--- | :--- | :--- |
| `latitude` | `float` | عرض جغرافیایی موقعیت مکانی |
| `longitude` | `float` | طول جغرافیایی موقعیت مکانی |

### `Contact`
| Field | Type | Description |
| :--- | :--- | :--- |
| `phone_number` | `str` | شماره تماس مخاطب |
| `name` | `str` | نام و نام خانوادگی مخاطب |
| `user_id` | `Optional[int]` | شناسه کاربری در بله (در صورت عضویت) |

---

## اشیای چندرسانه‌ای (Media Objects)

### `Photo`
| Field | Type | Description |
| :--- | :--- | :--- |
| `file_id` | `str` | شناسه دسترسی به فایل تصویر |
| `file_size` | `int` | حجم فایل بر حسب بایت |
| `width` | `int` | عرض تصویر بر حسب پیکسل |
| `height` | `int` | ارتفاع تصویر بر حسب پیکسل |

### `Document`
| Field | Type | Description |
| :--- | :--- | :--- |
| `file_id` | `str` | شناسه فایل |
| `file_name` | `Optional[str]` | نام اصلی فایل با پسوند |
| `file_size` | `int` | اندازه فایل به بایت |
| `mime_type` | `Optional[str]` | فرمت استاندارد فایل |

### `Voice`
| Field | Type | Description |
| :--- | :--- | :--- |
| `file_id` | `str` | شناسه ویس |
| `duration` | `int` | مدت زمان ضبط به ثانیه |
| `file_size` | `int` | حجم ویس به بایت |

### `Audio`
| Field | Type | Description |
| :--- | :--- | :--- |
| `file_id` | `str` | شناسه آهنگ یا ترک صوتی |
| `file_name` | `Optional[str]` | نام فایل موسیقی |
| `duration` | `int` | زمان پخش به ثانیه |
| `file_size` | `int` | حجم به بایت |
| `mime_type` | `Optional[str]` | نوع فرمت صوتی |

### `Video`
| Field | Type | Description |
| :--- | :--- | :--- |
| `file_id` | `str` | شناسه فایل ویدیو |
| `width` | `int` | پهنای تصویر به پیکسل |
| `height` | `int` | ارتفاع ویدیو به پیکسل |
| `duration` | `int` | مدت زمان به ثانیه |
| `file_size` | `int` | حجم ویدیو به بایت |

### `Sticker`
| Field | Type | Description |
| :--- | :--- | :--- |
| `file_id` | `str` | شناسه استیکر |
| `width` | `int` | عرض استیکر |
| `height` | `int` | ارتفاع استیکر |
| `emoji` | `Optional[str]` | ایموجی متناظر با استیکر |

---

## `InlineKeyboardMarkup`
کیبورد شیشه‌ای که زیر پیام قرار می‌گیرد:
```python
from bale.types import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="باز کردن وب‌سایت 🌐", url="https://ble.ir")],
    [InlineKeyboardButton(text="اطلاعات حساب 📊", callback_data="btn_info")]
])
```

---

## `ReplyKeyboardMarkup`
کیبورد سفارشی که جایگزین کیبورد اصلی گوشی در پایین صفحه می‌شود:
```python
from bale.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍️ مشاهده محصولات"), KeyboardButton(text="📦 پیگیری سفارش")],
        [KeyboardButton(text="📞 ارسال شماره تماس", request_contact=True)]
    ],
    resize_keyboard=True
)
```
