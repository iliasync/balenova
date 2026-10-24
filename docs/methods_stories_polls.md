# 📊 مرجع متدهای نظرسنجی، استوری و پیام‌های زمان‌بندی‌شده (Stories, Polls & Schedule API)

در این بخش متدهای مربوط به تعامل با نظرسنجی‌ها، انتشار و مشاهده استوری‌ها و زمان‌بندی ارسال خودکار پیام‌ها در بله مستند شده است.

---

## فهرست الفبایی متدها
| Method | Summary | Return Type |
| :--- | :--- | :--- |
| [`vote_poll`](#vote_poll) | ثبت رای کاربر در یک نظرسنجی چت یا کانال | `None` |
| [`close_poll`](#close_poll) | بستن و پایان دادن به رای‌گیری یک نظرسنجی | `None` |
| [`get_poll_result`](#get_poll_result) | دریافت آمار و نتایج آرای یک نظرسنجی مشخص | `ProtobufMessage` |
| [`get_all_stories`](#get_all_stories) | واکشی تمام استوری‌های فعال مخاطبین و کانال‌ها | `ProtobufMessage` |
| [`get_story`](#get_story) | دریافت جزئیات یک استوری با شناسه آن | `ProtobufMessage` |
| [`react_to_story`](#react_to_story) | ارسال واکنش ایموجی روی یک استوری | `None` |
| [`remove_story`](#remove_story) | حذف یک استوری منتشرشده توسط خود کاربر | `None` |
| [`get_story_viewers`](#get_story_viewers) | دریافت لیست افرادی که استوری شما را دیده‌اند | `ProtobufMessage` |
| [`schedule_task`](#schedule_task) | تنظیم ارسال خودکار پیام در یک زمان مشخص در آینده | `ProtobufMessage` |
| [`load_scheduled_tasks`](#load_scheduled_tasks) | دریافت لیست تمام پیام‌های زمان‌بندی‌شده در صف | `ProtobufMessage` |
| [`cancel_scheduled_tasks`](#cancel_scheduled_tasks) | لغو پیام‌های زمان‌بندی‌شده | `ProtobufMessage` |

---

### `vote_poll`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ثبت رای در یک نظرسنجی چندگزینه‌ای در بله.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `poll_id` | `int` | <span class="badge required">Yes</span> | — | شناسه عددی نظرسنجی |
| `chosen_options` | `Iterable[int]` | <span class="badge required">Yes</span> | — | ایندکس گزینه‌های انتخاب‌شده (از ۰ به بعد) |

##### Return Value
`None`

---

### `close_poll`
<span class="badge post">POST</span> <span class="badge async">Async</span>

پایان دادن به نظرسنجی توسط سازنده آن به منظور جلوگیری از ثبت آرای جدید.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `poll_id` | `int` | <span class="badge required">Yes</span> | — | شناسه نظرسنجی |

##### Return Value
`None`

---

### `get_poll_result`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت نتایج و درصد آرای ثبت‌شده برای گزینه‌های نظرسنجی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `poll_id` | `int` | <span class="badge required">Yes</span> | — | شناسه نظرسنجی |

##### Return Value
`ProtobufMessage`

---

### `get_all_stories`
<span class="badge get">GET</span> <span class="badge async">Async</span>

واکشی تمامی استوری‌های زنده مخاطبین دفترچه تلفن و کانال‌های عضو شده.

#### Parameters
این متد پارامتر اجباری ندارد.

##### Return Value
`ProtobufMessage`

---

### `get_story`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت جزئیات کامل یک استوری مشخص.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `story_id` | `str` | <span class="badge required">Yes</span> | — | شناسه استوری |

##### Return Value
`ProtobufMessage`

---

### `react_to_story`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال ایموجی ری‌اکشن برای استوری یک کاربر یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `story_id` | `str` | <span class="badge required">Yes</span> | — | شناسه استوری |
| `emoji` | `str` | <span class="badge required">Yes</span> | — | ایموجی واکنش (مانند `"❤️"` یا `"🔥"`) |

##### Return Value
`None`

---

### `remove_story`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف استوری ارسال شده توسط شما.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `story_id` | `str` | <span class="badge required">Yes</span> | — | شناسه استوری برای حذف |

##### Return Value
`None`

---

### `get_story_viewers`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت لیست افرادی که استوری شما را دیده‌اند.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `story_id` | `str` | <span class="badge required">Yes</span> | — | شناسه استوری |

##### Return Value
`ProtobufMessage`

---

### `schedule_task`
<span class="badge post">POST</span> <span class="badge async">Async</span>

برنامه‌ریزی برای ارسال یک پیام به چت یا گروه در تاریخی مشخص در آینده.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه مقصد |
| `date` | `int` | <span class="badge required">Yes</span> | — | زمان ارسال بر حسب میلی‌ثانیه یونیکس |
| `data` | `dict` | <span class="badge required">Yes</span> | — | محتوای پیام (متن، مدیا، کیبورد و...) |

##### Return Value
`ProtobufMessage`

---

### `load_scheduled_tasks`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت لیست پیام‌های زمان‌بندی‌شده‌ای که در صف ارسال قرار دارند.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه چت |

##### Return Value
`ProtobufMessage`

---

### `cancel_scheduled_tasks`
<span class="badge post">POST</span> <span class="badge async">Async</span>

لغو ارسال یک پیام زمان‌بندی‌شده.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `task_ids` | `Iterable[int]` | <span class="badge required">Yes</span> | — | شناسه‌های عددی تسک‌ها |

##### Return Value
`ProtobufMessage`
