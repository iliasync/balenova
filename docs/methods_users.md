# 👤 مرجع جامع متدهای کاربران و مخاطبین (Users & Account API)

این بخش شامل تمام متدهای دریافت مشخصات حساب، واکشی اطلاعات کاربران، جستجوی یوزرنیم، مدیریت مخاطبین دفترچه تلفن، مسدودسازی و ویرایش پروفایل کاربری در بله است.

---

## فهرست الفبایی متدها
| Method | Summary | Return Type |
| :--- | :--- | :--- |
| [`get_me`](#get_me) | دریافت اطلاعات کامل حساب کاربری متصل | [`User`](types.md#user) |
| [`get_user`](#get_user) | دریافت مشخصات کاربر بر اساس شناسه یا یوزرنیم | `Optional[`[`User`](types.md#user)`]` |
| [`load_users`](#load_users) | دریافت گروهی مشخصات چندین کاربر به صورت همزمان | `List[`[`User`](types.md#user)`]` |
| [`search_username`](#search_username) | جستجوی دقیق شناسه کاربری (Handle) در سرور بله | `Optional[Union[User, Chat]]` |
| [`get_contacts`](#get_contacts) | دریافت لیست مخاطبین دفترچه تلفن حساب بله | `dict` |
| [`add_contact`](#add_contact) | افزودن مخاطب جدید با نام و شماره تلفن | `DefaultResponse` |
| [`remove_contact`](#remove_contact) | حذف یک مخاطب از دفترچه تلفن | `DefaultResponse` |
| [`search_contacts`](#search_contacts) | جستجو میان مخاطبین ذخیره‌شده | `dict` |
| [`block_user`](#block_user) | مسدود کردن (بلاک) یک کاربر | `DefaultResponse` |
| [`unblock_user`](#unblock_user) | رفع انسداد (آنبلاک) یک کاربر قبلاً مسدودشده | `DefaultResponse` |
| [`load_blocked_users`](#load_blocked_users) | دریافت لیست تمام کاربران مسدودشده توسط حساب | `List[dict]` |
| [`edit_name`](#edit_name) | تغییر نام نمایشی (Display Name) حساب شما | `DefaultResponse` |
| [`edit_about`](#edit_about) | تغییر متن وضعیت یا بیوگرافی (About/Bio) شما | `DefaultResponse` |
| [`edit_nickname`](#edit_nickname) | تنظیم یا تغییر شناسه کاربری عمومی (یوزرنیم) | `DefaultResponse` |
| [`check_nickname`](#check_nickname) | بررسی خالی بودن یا در دسترس بودن یک یوزرنیم | `bool` |

---

### `get_me`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت مشخصات کامل حساب جاری متصل به کلاینت (نام، یوزرنیم، آیدی عددی و وضعیت).

#### Parameters
این متد هیچ پارامتر ورودی اجباری ندارد.

##### Return Value
[`User`](types.md#user) — شیء کاربر متصل به همراه فیلد `is_self = True`.

##### Code Example
```python
me = await client.get_me()
print(f"وارد شدید به عنوان: {me.name} (@{me.username})")
print(f"شناسه کاربری عددی شما: {me.id}")
```

---

### `get_user`
<span class="badge get">GET</span> <span class="badge async">Async</span>

واکشی اطلاعات یک کاربر مشخص در پیام‌رسان بله با استفاده از آیدی عددی یا شیء کاربر.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `user_id` | `Union[int, str, User]` | <span class="badge required">Yes</span> | — | شناسه عددی کاربر یا رشته شناسه کاربری |

##### Return Value
`Optional[`[`User`](types.md#user)`]`

---

### `load_users`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت دسته‌جمعی اطلاعات لیستی از کاربران در یک درخواست شبکه‌ای.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `users` | `Iterable[Union[int, str]]` | <span class="badge required">Yes</span> | — | لیستی از شناسه‌های کاربری عددی |

##### Return Value
`List[`[`User`](types.md#user)`]`

---

### `search_username`
<span class="badge get">GET</span> <span class="badge async">Async</span>

جستجوی نام کاربری عمومی در دایرکتوری بله برای یافتن کاربر یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `query` | `str` | <span class="badge required">Yes</span> | — | نام کاربری با یا بدون علامت `@` |

##### Return Value
`Optional[Union[User, Chat]]`

---

### `get_contacts`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت لیست تمام مخاطبین ذخیره‌شده در حساب کاربری شما.

#### Parameters
این متد پارامتر اجباری ندارد.

##### Return Value
`dict` — دیکشنری شامل فهرست کامل مخاطبین.

---

### `add_contact`
<span class="badge post">POST</span> <span class="badge async">Async</span>

افزودن یک مخاطب جدید به دفترچه تلفن حساب بله.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `phone_number` | `str` | <span class="badge required">Yes</span> | — | شماره تماس به فرمت استاندارد (مانند `09121234567`) |
| `name` | `str` | <span class="badge required">Yes</span> | — | نام نمایشی مخاطب |

##### Return Value
`DefaultResponse`

---

### `remove_contact`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف یک مخاطب از دفترچه تلفن حساب.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربری مخاطب برای حذف |

##### Return Value
`DefaultResponse`

---

### `search_contacts`
<span class="badge get">GET</span> <span class="badge async">Async</span>

جستجوی متنی میان نام و شماره‌های مخاطبین.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `query` | `str` | <span class="badge required">Yes</span> | — | عبارت جستجو (نام یا شماره) |

##### Return Value
`dict`

---

### `block_user`
<span class="badge post">POST</span> <span class="badge async">Async</span>

مسدودسازی یک کاربر مشخص.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربری فرد مورد نظر |

##### Return Value
`DefaultResponse`

---

### `unblock_user`
<span class="badge post">POST</span> <span class="badge async">Async</span>

رفع مسدودیت یک کاربر قبلاً مسدودشده.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربر |

##### Return Value
`DefaultResponse`

---

### `load_blocked_users`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت لیست تمام کاربران مسدودشده توسط حساب کاربری شما.

##### Return Value
`List[dict]`

---

### `edit_name`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تغییر نام نمایشی اکانت شما.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `name` | `str` | <span class="badge required">Yes</span> | — | نام نمایشی جدید |

##### Return Value
`DefaultResponse`

---

### `edit_about`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تغییر متن وضعیت یا بیوگرافی (About/Bio).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `about` | `str` | <span class="badge required">Yes</span> | — | متن بیوگرافی جدید |

##### Return Value
`DefaultResponse`

---

### `edit_nickname`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تنظیم یا تغییر شناسه کاربری عمومی (یوزرنیم).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `nickname` | `str` | <span class="badge required">Yes</span> | — | یوزرنیم دلخواه بدون `@` |

##### Return Value
`DefaultResponse`

---

### `check_nickname`
<span class="badge get">GET</span> <span class="badge async">Async</span>

بررسی در دسترس بودن یک آیدی (Nickname).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `nickname` | `str` | <span class="badge required">Yes</span> | — | یوزرنیم مورد نظر برای استعلام |

##### Return Value
`bool`
