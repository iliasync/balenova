# ⚙️ مرجع متدهای امنیت، نشست‌ها و حریم خصوصی (Settings & Security API)

در این بخش متدهای مربوط به مدیریت نشست‌های فعال، بستن نشست‌ها از راه دور، تنظیمات حریم خصوصی (آخرین بازدید، عکس پروفایل) و زبان حساب کاربری مستند شده است.

---

## فهرست الفبایی متدها
| Method | Summary | Return Type |
| :--- | :--- | :--- |
| [`get_auth_sessions`](#get_auth_sessions) | دریافت لیست دستگاه‌ها و نشست‌های فعال لاگین‌شده | `List[dict]` |
| [`terminate_session`](#terminate_session) | قطع اتصال و خروج اجباری یک دستگاه مشخص | `DefaultResponse` |
| [`terminate_all_sessions`](#terminate_all_sessions) | خروج از تمامی دستگاه‌ها به جز دستگاه فعلی | `DefaultResponse` |
| [`get_user_privacy_status`](#get_user_privacy_status) | دریافت تنظیمات حریم خصوصی (آخرین بازدید، تماس و...) | `dict` |
| [`set_user_privacy_status`](#set_user_privacy_status) | تغییر سیاست حریم خصوصی برای یک دسته‌بندی | `DefaultResponse` |
| [`edit_time_zone`](#edit_time_zone) | تغییر منطقه زمانی حساب کاربری | `DefaultResponse` |

---

### `get_auth_sessions`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت مشخصات تمامی نشست‌های فعال حساب (مدل دستگاه، نسخه اپلیکیشن، آدرس IP و زمان آخرین استفاده).

#### Parameters
این متد پارامتر اجباری ندارد.

##### Return Value
`List[dict]` — لیستی از اطلاعات سشن‌ها حاوی `id`, `device_title`, `ip`, `auth_time`.

---

### `terminate_session`
<span class="badge post">POST</span> <span class="badge async">Async</span>

پایان دادن به دسترسی یک نشست ناشناس یا قدیمی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `session_id` | `int` | <span class="badge required">Yes</span> | — | شناسه عددی سشن برای ابطال |

##### Return Value
`DefaultResponse`

---

### `terminate_all_sessions`
<span class="badge post">POST</span> <span class="badge async">Async</span>

خروج فوری و هم‌زمان از تمام سیستم‌ها، مرورگرها و گوشی‌های دیگر.

#### Parameters
این متد پارامتری دریافت نمی‌کند.

##### Return Value
`DefaultResponse`

---

### `get_user_privacy_status`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت وضعیت حریم خصوصی کاربر برای ویژگی‌های مختلف (مانند آخرین بازدید، عکس پروفایل، تماس صوتی).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `rule_type` | `int` | <span class="badge required">Yes</span> | — | کد دسته‌بندی حریم خصوصی |

##### Return Value
`dict`

---

### `set_user_privacy_status`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تنظیم و تغییر دسترسی‌های حریم خصوصی (مثلاً نمایش آخرین بازدید فقط برای مخاطبین).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `rule_type` | `int` | <span class="badge required">Yes</span> | — | نوع قانون حریم خصوصی |
| `rule_value` | `int` | <span class="badge required">Yes</span> | — | مقدار جدید قانون (همه، مخاطبین، هیچ‌کس) |

##### Return Value
`DefaultResponse`

---

### `edit_time_zone`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تغییر منطقه زمانی حساب کاربری.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `time_zone` | `str` | <span class="badge required">Yes</span> | — | شناسه موقعیت زمانی (مثلاً `"Asia/Tehran"`) |

##### Return Value
`DefaultResponse`
