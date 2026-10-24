# 🤖 راهنمای جامع ساخت ربات و سیستم رویدادها (Events & Bot API)

کتابخانه **BaleNova** سیستم رویدادمحور فوق‌العاده مدرن و جامعی را بر اساس دو استاندارد برتر پایتون (**Telethon** و **Pyrogram**) پیاده‌سازی کرده است. شما می‌توانید بسته به سلیقه خود از هر کدام از این دو شیوه برای پردازش ریل‌تایم آپدیت‌ها استفاده کنید.

---

## ۱. جدول کلاس‌های رویداد (Event Classes)

| Event Class | Trigger | Key Attributes | Active Methods |
| :--- | :--- | :--- | :--- |
| [`events.NewMessage`](#eventsnewmessage) | دریافت هر پیام جدید در چت، گروه یا کانال | `event.message`, `event.chat`, `event.sender` | `event.reply()`, `event.respond()` |
| [`events.MessageEdited`](#eventsmessageedited) | ویرایش شدن یک پیام در گفت‌وگو | `event.message`, `event.chat`, `event.sender` | `event.reply()` |
| [`events.MessageDeleted`](#eventsmessagedeleted) | حذف یک یا چند پیام در چت | `event.message_ids`, `event.chat_id` | — |
| [`events.CallbackQuery`](#eventscallbackquery) | لمس دکمه شیشه‌ای (اینلاین) توسط کاربر | `event.data`, `event.from_user`, `event.message` | `event.answer()`, `event.edit()` |
| [`events.ChatAction`](#eventschataction) | عضویت، خروج یا اخراج اعضا در گروه | `event.user_joined`, `event.user_left`, `event.from_user` | `event.reply()` |
| [`events.UserTyping`](#eventsusertyping) | شروع تایپ یا ضبط ویس توسط کاربر | `event.chat_id`, `event.user_id`, `event.action` | — |

---

## ۲. مشخصات و فیلترهای رویدادها

### `events.NewMessage`
این رویداد اصلی‌ترین ایونت برای بات‌ها و یوزربات‌ها است. با ارسال آرگومان به این کلاس، می‌توانید پیام‌ها را پیش از رسیدن به هندلر فیلتر نمایید:

#### Parametersی سازنده فیلتر
| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `pattern` | `Union[str, Pattern]` | `None` | عبارت منظم (Regex) برای تطبیق روی متن پیام |
| `incoming` | `Optional[bool]` | `None` | اگر `True` باشد، فقط پیام‌های دریافتی از دیگران پردازش می‌شوند |
| `outgoing` | `Optional[bool]` | `None` | اگر `True` باشد، فقط پیام‌های ارسالی خودمان پردازش می‌شوند |
| `chats` | `Union[int, str, List]` | `None` | محدود کردن رویداد به یک یا چند چت یا گروه مشخص |
| `forwards` | `Optional[bool]` | `None` | فیلتر پیام‌های فوروارد شده |

#### جدول اتریبیوت‌های شیء رویداد `NewMessage`
| Attribute | Type | Description |
| :--- | :--- | :--- |
| `event.message` | [`Message`](types.md#message) | شیء کامل پیام دریافت شده |
| `event.text` | `str` | میان‌بر مستقیم برای دریافت متن پیام |
| `event.chat_id` | `Union[int, str]` | شناسه چتی که پیام در آن آمده |
| `event.sender_id` | `Optional[int]` | شناسه کاربر ارسال‌کننده پیام |
| `event.pattern_match` | `re.Match` | شیء تطابق ریجکس (حاوی گروه‌های استخراج شده با `group(1)`) |
| `event.is_private` | `bool` | آیا پیام در گفت‌وگوی خصوصی آمده است؟ |
| `event.is_group` | `bool` | آیا پیام در یک گروه ارسال شده است؟ |
| `event.is_channel` | `bool` | آیا پیام در یک کانال بله منتشر شده است؟ |

---

### `events.MessageEdited`
برانگیخته شدن هنگام ویرایش شدن متن یک پیام در چت.
دارای تمام ویژگی‌ها و متدهای مشابه `events.NewMessage` است.

---

### `events.MessageDeleted`
برانگیخته شدن به محض حذف شدن یک یا چند پیام در یک گفت‌وگو.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `event.message_ids` | `List[int]` | لیست شناسه‌های پیام‌های حذف شده |
| `event.chat_id` | `Union[int, str]` | شناسه چتی که پیام‌ها در آن پاک شدند |

---

### `events.CallbackQuery`
دریافت رویداد لمس دکمه‌های شیشه‌ای توسط کاربران.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `event.data` | `str` | رشته متنی تعریف‌شده در `callback_data` دکمه |
| `event.from_user` | [`User`](types.md#user) | کاربری که روی دکمه کلیک کرده |
| `event.message` | `Optional[Message]` | پیامی که دکمه به آن متصل بوده است |

---

### `events.ChatAction`
رویداد ورود، خروج، یا اخراج اعضا در گروه‌ها.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `event.user_joined` | `bool` | آیا عضو جدیدی به گروه پیوسته است؟ |
| `event.user_left` | `bool` | آیا عضوی گروه را ترک کرده یا اخراج شده؟ |
| `event.from_user` | `User` | کاربر انجام‌دهنده اکشن |

---

### `events.UserTyping`
رویداد وضعیت تایپ یا ضبط ویس کاربر در چت.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `event.chat_id` | `Union[int, str]` | شناسه چت |
| `event.user_id` | `int` | شناسه کاربر در حال تایپ |

### متدهای کاربردی رویداد
| Method | Parameters | Description |
| :--- | :--- | :--- |
| `await event.reply(text, ...)` | `text: str, reply_markup=None` | ارسال پاسخ مستقیم (ریپلای) روی پیام دریافتی |
| `await event.respond(text, ...)` | `text: str, reply_markup=None` | ارسال پیام در همان چت بدون ریپلای |
| `await event.delete()` | — | حذف فوری پیام ارسال شده |

#### کدهای نمونه Telethon Style
```python
from bale import Client, events

client = Client.from_firefox()

# ۱. استخراج متغیر با ریجکس (محاسبه جمع دو عدد)
@client.on(events.NewMessage(pattern=r"^/calc\s+(\d+)\s*\+\s*(\d+)$"))
async def calc_handler(event):
    n1 = int(event.pattern_match.group(1))
    n2 = int(event.pattern_match.group(2))
    await event.reply(f"پاسخ: {n1 + n2} ✅")

# ۲. ضدلینک و فیلتر کلمات در گروه‌ها
@client.on(events.NewMessage(incoming=True))
async def antilink_handler(event):
    if not event.is_group:
        return
    if "ble.ir/join/" in event.text or "t.me/" in event.text:
        await event.delete()
        await event.respond(f"ارسال لینک توسط کاربر {event.sender_id} ممنوع است! ❌")

# ۳. پاسخ اختصاصی به دستور /start
@client.on(events.NewMessage(pattern=r"^/start$"))
async def start_handler(event):
    await event.reply("سلام! به ربات BaleNova خوش آمدید 🌟")

client.run()
```

---

## ۳. سبک پایروگرام (`@client.on_message` + فیلترها)

اگر به متدولوژی دکوراتورهای مجزا و عملگرهای بیتی (`&`, `|`, `~`) علاقه دارید:

### جدول فیلترهای درون‌ساخت
| Filter | Functionality | Example |
| :--- | :--- | :--- |
| `filters.text` | پیام‌های دارای متن | `filters.text` |
| `filters.command(name)` | دستورات ربات (شروع با `/`) | `filters.command("start")` |
| `filters.regex(pattern)` | تطبیق با عبارت منظم | `filters.regex(r"^قیمت \w+")` |
| `filters.private` | چت‌های دو نفره خصوصی | `filters.private` |
| `filters.group` | گروه‌ها و سوپرگروه‌ها | `filters.group` |
| `filters.channel` | کانال‌ها | `filters.channel` |
| `filters.incoming` | پیام‌های دریافتی از کاربران دیگر | `filters.incoming` |
| `filters.outgoing` یا `filters.me` | پیام‌های ارسالی خودمان | `filters.me` |
| `filters.reply` | پیام‌هایی که ریپلای هستند | `filters.reply` |
| `filters.photo` | پیام‌های حاوی تصویر | `filters.photo` |
| `filters.document` | پیام‌های حاوی سند و فایل | `filters.document` |

#### کدهای نمونه Pyrogram Style
```python
from bale import Client, filters
from bale.types import Message

client = Client("pyrogram_bot")

# ترکیب فیلترها با عملگر AND و NOT:
# دستور help در چت‌های خصوصی، به شرطی که پیام دریافتی باشد نه ارسالی خودمان
@client.on_message(filters.command("help") & filters.private & ~filters.me)
async def help_handler(c: Client, msg: Message):
    guide = (
        "راهنمای فرامین:\n"
        "• /start - شروع مجدد\n"
        "• /status - وضعیت سرور\n"
        "• /ping - سنجش پینگ"
    )
    await msg.reply(guide)

client.run()
```
