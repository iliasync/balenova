# 💬 مرجع جامع متدهای پیام‌ها و رسانه‌ها (Messages & Media API)

این بخش شامل تمام متدهای ارسال، دریافت تاریخچه، دانلود مدیا، ویرایش، حذف، فوروارد، پین، ری‌اکشن، سین‌زدن و کار با انواع رسانه‌ها در پیام‌رسان بله است.

---

## فهرست الفبایی متدها
| Method | Summary | Return Type |
| :--- | :--- | :--- |
| [`send_message`](#send_message) | ارسال پیام متنی به کاربر، گروه یا کانال | [`Message`](types.md#message) |
| [`edit_message`](#edit_message) | ویرایش متن یک پیام ارسال‌شده | `DefaultResponse` |
| [`delete_message`](#delete_message) | حذف یک پیام از تاریخچه گفت‌وگو | `DefaultResponse` |
| [`forward_messages`](#forward_messages) | فوروارد کردن پیام از یک چت به چت دیگر | `DefaultResponse` |
| [`copy_message`](#copy_message) | کپی کردن پیام بدون برچسب فوروارد | [`Message`](types.md#message) |
| [`get_history`](#get_history) | دریافت تاریخچه پیام‌های قبلی چت با صفحه‌بندی | `List[`[`Message`](types.md#message)`]` |
| [`mark_as_read`](#mark_as_read) | اعلام خوانده‌شدن (Seen / Read) پیام‌های چت | `DefaultResponse` |
| [`download_media`](#download_media) | دانلود مستقیم فایل، تصویر، ویس یا ویدیو به صورت بایت | `bytes` |
| [`download_file`](#download_file) | دانلود فایل با شناسه فایل ابری بله | `bytes` |
| [`send_photo`](#send_photo) | ارسال عکس همراه با کپشن | [`Message`](types.md#message) |
| [`send_document`](#send_document) | ارسال فایل یا سند بدون فشرده‌سازی | [`Message`](types.md#message) |
| [`send_audio`](#send_audio) | ارسال فایل موسیقی یا فایل صوتی | [`Message`](types.md#message) |
| [`send_video`](#send_video) | ارسال ویدیو با قابلیت پیش‌نمایش | [`Message`](types.md#message) |
| [`send_voice`](#send_voice) | ارسال پیام صوتی (Voice) با شکل‌موج | [`Message`](types.md#message) |
| [`send_sticker`](#send_sticker) | ارسال استیکر بله | [`Message`](types.md#message) |
| [`send_location`](#send_location) | ارسال موقعیت مکانی جغرافیایی (GPS) | [`Message`](types.md#message) |
| [`send_contact`](#send_contact) | ارسال کارت مخاطب و شماره تماس | [`Message`](types.md#message) |
| [`pin_message`](#pin_message) | پین کردن پیام در بالای صفحه چت | `DefaultResponse` |
| [`unpin_message`](#unpin_message) | برداشتن سنجاق پیام | `DefaultResponse` |
| [`unpin_all`](#unpin_all) | حذف تمام پیام‌های پین‌شده در چت | `DefaultResponse` |
| [`set_reaction`](#set_reaction) | ثبت ایموجی واکنش روی پیام | `dict` |
| [`remove_reaction`](#remove_reaction) | حذف واکنش قبلی روی پیام | `dict` |
| [`send_action`](#send_action) | ارسال وضعیت (تایپینگ، آپلود و...) | `DefaultResponse` |

---

### `send_message`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال پیام متنی به چت، گروه یا کانال با پشتیبانی از مارک‌داون و کیبوردها.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str, User, Chat]` | <span class="badge required">Yes</span> | — | شناسه مقصد (عددی، یوزرنیم با/بدون `@`، یا Peer) |
| `text` | `str` | <span class="badge required">Yes</span> | — | متن پیام (تا ۴۰۹۶ کاراکتر) |
| `reply_to_message_id` | `Optional[Union[int, str]]` | <span class="badge optional">No</span> | `None` | شناسه پیامی که پاسخ به آن ارسال می‌شود |
| `reply_markup` | `Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]]` | <span class="badge optional">No</span> | `None` | دکمه‌های شیشه‌ای یا ریپلای کیبورد |

##### Return Value
[`Message`](types.md#message)

```python
msg = await client.send_message("pv_ilia", "سلام از BaleNova! 🚀")
```

---

### `get_history`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت پیام‌های قبلی چت با قابلیت پیمایش زمانی (Pagination). (نام مستعار: `load_history`, `get_messages`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت یا گروه |
| `from_date` | `int` | <span class="badge optional">No</span> | `-1` | زمان شروع برحسب میلی‌ثانیه (`-1` یعنی از جدیدترین پیام‌ها) |
| `limit` | `int` | <span class="badge optional">No</span> | `20` | تعداد پیام‌هایی که باید برگردانده شوند |

##### Return Value
`List[`[`Message`](types.md#message)`]`

##### Code Example
```python
# واکشی ۵۰ پیام اخیر چت
messages = await client.get_history("pv_ilia", limit=50)
for m in messages:
    print(f"[{m.date}] {m.from_user.name if m.from_user else 'ناشناس'}: {m.text}")
```

---

### `download_media`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دانلود مستقیم فایل چندرسانه‌ای پیوست‌شده به پیام (عکس، ویدیو، وویس، سند یا استیکر) به صورت بایت خام.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `message` | [`Message`](types.md#message) | <span class="badge required">Yes</span> | — | شیء پیامی که دارای رسانه است |

##### Return Value
`bytes` — بایت‌های محتوای فایل دانلودشده.

##### Code Example
```python
# روش ۱: از طریق کلاینت
media_bytes = await client.download_media(message)
with open("downloaded_file.jpg", "wb") as f:
    f.write(media_bytes)

# روش ۲: به صورت اکتیو رکورد روی خود شیء پیام!
file_data = await message.download()
```

---

### `download_file`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دانلود هر فایلی از سرورهای ابری بله با استفاده از شناسه فایل (`file_id`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `file_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه یکتای فایل |
| `access_hash` | `Union[int, str]` | <span class="badge required">Yes</span> | — | اکسس هش معتبر فایل |

##### Return Value
`bytes`

---

### `mark_as_read`
<span class="badge post">POST</span> <span class="badge async">Async</span>

علامت‌گذاری پیام‌های یک چت به عنوان «خوانده‌شده» (سین زدن). (نام مستعار: `message_read`, `read_chat`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت مقصد |
| `date` | `Optional[int]` | <span class="badge optional">No</span> | زمان حال | پیام‌های تا این زمان به عنوان خوانده‌شده ثبت می‌شوند |

##### Return Value
`DefaultResponse`

##### Code Example
```python
# سین زدن تمام پیام‌های دریافتی تا این لحظه
await client.mark_as_read("pv_ilia")
```

---

### `edit_message`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ویرایش متن یک پیام ارسال‌شده. (نام مستعار: `edit_message_text`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str, User, Chat]` | <span class="badge required">Yes</span> | — | شناسه چت |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیامی که باید ویرایش شود |
| `text` | `str` | <span class="badge required">Yes</span> | — | متن جدید |

##### Return Value
`DefaultResponse`

```python
await client.edit_message("pv_ilia", msg.id, "متن ویرایش شد! ✏️")
# یا اکتیو رکورد:
await msg.edit("متن جدید")
```

---

### `delete_message`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف یک پیام از چت. (نام مستعار: `delete_messages`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str, User, Chat]` | <span class="badge required">Yes</span> | — | شناسه چت |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیام |

##### Return Value
`DefaultResponse`

```python
await client.delete_message("pv_ilia", msg.id)
# یا اکتیو رکورد:
await msg.delete()
```

---

### `forward_messages`
<span class="badge post">POST</span> <span class="badge async">Async</span>

فوروارد پیام از یک چت به چت دیگر. (نام مستعار: `forward_message`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مقصد |
| `from_chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مبدا |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیام |

##### Return Value
`DefaultResponse`

---

### `copy_message`
<span class="badge post">POST</span> <span class="badge async">Async</span>

کپی کردن پیام بدون نمایش نام فرستنده اصلی یا برچسب فوروارد.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مقصد |
| `from_chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مبدا |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیام |

##### Return Value
[`Message`](types.md#message)

---

### `send_photo`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال تصویر به همراه کپشن اختیاری.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه مقصد |
| `photo` | `Union[str, bytes, BinaryIO]` | <span class="badge required">Yes</span> | — | مسیر فایل روی دیسک، بایت‌ها، یا شیء فایل |
| `caption` | `Optional[str]` | <span class="badge optional">No</span> | `""` | کپشن زیر تصویر |
| `reply_to_message_id` | `Optional[Union[int, str]]` | <span class="badge optional">No</span> | `None` | شناسه پیام ریپلای |

##### Return Value
[`Message`](types.md#message)

---

### `send_document`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال فایل یا سند دلخواه (PDF, ZIP, APK و...).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مقصد |
| `document` | `Union[str, bytes, BinaryIO]` | <span class="badge required">Yes</span> | — | مسیر فایل یا بایت‌های داده |
| `file_name` | `Optional[str]` | <span class="badge optional">No</span> | نام فایل | نام نمایشی فایل |
| `caption` | `Optional[str]` | <span class="badge optional">No</span> | `""` | کپشن پیوست‌شده |

##### Return Value
[`Message`](types.md#message)

---

### `send_audio`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال فایل صوتی یا موسیقی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مقصد |
| `audio` | `Union[str, bytes, BinaryIO]` | <span class="badge required">Yes</span> | — | مسیر یا بایت‌های موسیقی |
| `caption` | `Optional[str]` | <span class="badge optional">No</span> | `""` | کپشن |

##### Return Value
[`Message`](types.md#message)

---

### `send_video`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال فایل ویدیویی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مقصد |
| `video` | `Union[str, bytes, BinaryIO]` | <span class="badge required">Yes</span> | — | مسیر یا بایت‌های ویدیو |
| `caption` | `Optional[str]` | <span class="badge optional">No</span> | `""` | کپشن |

##### Return Value
[`Message`](types.md#message)

---

### `send_voice`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال پیام صوتی (Voice Note) با شکل‌موج.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مقصد |
| `voice` | `Union[str, bytes, BinaryIO]` | <span class="badge required">Yes</span> | — | مسیر فایل ویس (OGG/Opus) |
| `duration` | `Optional[int]` | <span class="badge optional">No</span> | `0` | مدت زمان به ثانیه |

##### Return Value
[`Message`](types.md#message)

---

### `send_sticker`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال استیکر با شناسه فایل یا فایل تصویری.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | چت مقصد |
| `sticker` | `Union[str, bytes]` | <span class="badge required">Yes</span> | — | شناسه فایل استیکر یا مسیر فایل |

##### Return Value
[`Message`](types.md#message)

---

### `send_location`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال مختصات جغرافیایی به صورت نقشه تعاملی بله.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه مقصد |
| `latitude` | `float` | <span class="badge required">Yes</span> | — | عرض جغرافیایی (Latitude) |
| `longitude` | `float` | <span class="badge required">Yes</span> | — | طول جغرافیایی (Longitude) |

##### Return Value
[`Message`](types.md#message)

```python
# ارسال لوکیشن میدان آزادی تهران
await client.send_location("pv_ilia", latitude=35.6997, longitude=51.3380)
```

---

### `send_contact`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال کارت مخاطب و شماره همراه به چت.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه مقصد |
| `phone_number` | `str` | <span class="badge required">Yes</span> | — | شماره تلفن همراه مخاطب |
| `name` | `str` | <span class="badge required">Yes</span> | — | نام نمایشی مخاطب |

##### Return Value
[`Message`](types.md#message)

---

### `pin_message`
<span class="badge post">POST</span> <span class="badge async">Async</span>

سنجاق کردن یک پیام در بالای چت یا گروه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت یا گروه |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیامی که باید پین شود |

##### Return Value
`DefaultResponse`

---

### `unpin_message`
<span class="badge post">POST</span> <span class="badge async">Async</span>

برداشتن سنجاق از یک پیام مشخص.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیام پین‌شده |

##### Return Value
`DefaultResponse`

---

### `unpin_all`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف تمام سنجاق‌های گفت‌وگو.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت |

##### Return Value
`DefaultResponse`

---

### `set_reaction`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ثبت واکنش ایموجی (مانند 👍, ❤️, 🔥, 🎉) روی پیام.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت هدف |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیام |
| `code` | `str` | <span class="badge required">Yes</span> | — | کاراکتر ایموجی واکنش (مانند `"❤️"` یا `"🔥"`) |

##### Return Value
`dict`

---

### `remove_reaction`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف واکنش ثبت‌شده کاربر از روی پیام.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت هدف |
| `message_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه پیام |
| `code` | `str` | <span class="badge required">Yes</span> | — | ایموجی قبلاً ثبت‌شده |

##### Return Value
`dict`

---

### `send_action`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال وضعیت زنده چت به منظور نمایش تایپ، آپلود فایل و غیره.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت |
| `action` | `ChatAction` | <span class="badge required">Yes</span> | — | وضعیت از `bale.enums.ChatAction` (مثل `TYPING`, `RECORD_VOICE`) |

##### Return Value
`DefaultResponse`
