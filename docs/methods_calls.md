# 📞 مرجع متدهای تماس‌های صوتی و تصویری (Calls & WebRTC API)

پیام‌رسان بله از پروتکل استاندارد WebRTC و زیرساخت سرورهای لایوکیت (LiveKit) برای برقراری تماس‌های صوتی، تصویری و جلسات گروهی بهره می‌برد. در این بخش متدهای کلاینت برای کنترل تماس‌ها مستند شده است.

---

## فهرست الفبایی متدها
| Method | Summary | Return Type |
| :--- | :--- | :--- |
| [`start_call`](#start_call) | شروع تماس دو نفره صوتی یا تصویری با یک کاربر | `dict` |
| [`accept_call`](#accept_call) | پذیرفتن تماس ورودی و تبادل کلیدهای SDP | `dict` |
| [`discard_call`](#discard_call) | قطع یا رد تماس فعال | `DefaultResponse` |
| [`start_group_call`](#start_group_call) | آغاز تماس گروهی (جلسه صوتی/تصویری) در گروه | `dict` |
| [`join_group_call`](#join_group_call) | پیوستن به تماس گروهی در حال اجرا | `dict` |
| [`leave_group_call`](#leave_group_call) | خروج از جلسه تماس گروهی | `DefaultResponse` |
| [`generate_call_link`](#generate_call_link) | ساخت لینک اختصاصی برای دعوت مهمان به تماس | `dict` |
| [`raise_call_hand`](#raise_call_hand) | بالا بردن دست در جلسه صوتی برای اجازه صحبت | `DefaultResponse` |
| [`lower_call_hand`](#lower_call_hand) | پایین آوردن دست در تماس | `DefaultResponse` |
| [`start_call_recording`](#start_call_recording) | شروع ضبط جلسه صوتی یا تصویری | `DefaultResponse` |
| [`stop_call_recording`](#stop_call_recording) | توقف ضبط جلسه تماس | `DefaultResponse` |

---

### `start_call`
<span class="badge post">POST</span> <span class="badge async">Async</span>

برقراری تماس مستقیم صوتی یا تصویری با یک مخاطب.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربر مقصد |
| `is_video` | `bool` | <span class="badge optional">No</span> | `False` | آیا تماس تصویری باشد؟ |

##### Return Value
`dict` — شامل شناسه تماس (`call_id`) و توکن اتصال وب‌سوکت لایوکیت.

---

### `accept_call`
<span class="badge post">POST</span> <span class="badge async">Async</span>

پاسخ دادن به تماس دریافتی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `call_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه تماس ورودی |

##### Return Value
`dict`

---

### `discard_call`
<span class="badge post">POST</span> <span class="badge async">Async</span>

قطع کردن تماس جاری یا رد تماس دریافتی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `call_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه تماس |

##### Return Value
`DefaultResponse`

---

### `start_group_call`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ایجاد جلسه صوتی زنده (Voice Chat) در یک گروه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `title` | `Optional[str]` | <span class="badge optional">No</span> | `""` | عنوان یا موضوع گفت‌وگوی صوتی |

##### Return Value
`dict`

---

### `join_group_call`
<span class="badge post">POST</span> <span class="badge async">Async</span>

پیوستن به جلسه صوتی گروهی در حال برگزاری.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه گروه |

##### Return Value
`dict`

---

### `leave_group_call`
<span class="badge post">POST</span> <span class="badge async">Async</span>

خروج از جلسه تماس گروهی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه گروه |

##### Return Value
`DefaultResponse`

---

### `generate_call_link`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ساخت پیوند دعوت اینترنتی برای اضافه کردن شرکت‌کنندگان بدون نیاز به عضویت در گروه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `title` | `str` | <span class="badge required">Yes</span> | — | عنوان جلسه |

##### Return Value
`dict`

---

### `raise_call_hand`
<span class="badge post">POST</span> <span class="badge async">Async</span>

بالا بردن دست در جلسه صوتی برای اجازه صحبت.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه چت یا گروه |

##### Return Value
`DefaultResponse`

---

### `lower_call_hand`
<span class="badge post">POST</span> <span class="badge async">Async</span>

پایین آوردن دست در تماس گروهی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه چت |

##### Return Value
`DefaultResponse`

---

### `start_call_recording`
<span class="badge post">POST</span> <span class="badge async">Async</span>

شروع ضبط جلسه صوتی یا تصویری توسط مدیر.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `call_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه تماس |

##### Return Value
`DefaultResponse`

---

### `stop_call_recording`
<span class="badge post">POST</span> <span class="badge async">Async</span>

توقف ضبط جلسه صوتی و دریافت فایل خروجی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `call_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه تماس |

##### Return Value
`DefaultResponse`
