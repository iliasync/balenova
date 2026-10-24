# 👥 مرجع جامع متدهای گفت‌وگوها، گروه‌ها و کانال‌ها (Chats & Dialogs API)

این بخش شامل تمام متدهای دریافت دیالوگ‌ها، مدیریت اعضا، ساخت گروه و کانال، تغییر دسترسی‌ها، آرشیو چت‌ها، پوشه‌بندی و پاکسازی تاریخچه در بله است.

---

## فهرست الفبایی متدها
| Method | Summary | Return Type |
| :--- | :--- | :--- |
| [`get_dialogs`](#get_dialogs) | دریافت فهرست آخرین گفتگوها و چت‌های فعال | `DialogsList[Dialog]` |
| [`get_chat`](#get_chat) | دریافت مشخصات کامل یک چت، گروه یا کانال با شناسه | [`Chat`](types.md#chat) |
| [`get_chat_members`](#get_chat_members) | دریافت لیست اعضای حاضر در گروه با جستجو و فیلتر | `dict` |
| [`get_chat_members_count`](#get_chat_members_count) | دریافت تعداد کل اعضای گروه یا کانال | `int` |
| [`create_group`](#create_group) | ایجاد یک گروه جدید در پیام‌رسان بله | [`Chat`](types.md#chat) |
| [`create_channel`](#create_channel) | ایجاد یک کانال عمومی یا خصوصی جدید | [`Chat`](types.md#chat) |
| [`edit_group_title`](#edit_group_title) | تغییر نام و عنوان گروه یا کانال | `DefaultResponse` |
| [`edit_group_about`](#edit_group_about) | تغییر بیوگرافی و توضیحات گروه | `DefaultResponse` |
| [`set_chat_photo`](#set_chat_photo) | تغییر تصویر یا آواتار چت | `DefaultResponse` |
| [`get_group_link`](#get_group_link) | دریافت لینک دعوت خصوصی به گروه | `Optional[str]` |
| [`revoke_group_link`](#revoke_group_link) | باطل کردن لینک دعوت قبلی و صدور لینک جدید | `Optional[str]` |
| [`join_chat`](#join_chat) | عضویت در گروه با لینک دعوت | [`Chat`](types.md#chat) |
| [`leave_chat`](#leave_chat) | ترک کردن گروه یا کانال | `DefaultResponse` |
| [`invite_user`](#invite_user) | دعوت و افزودن مستقیم کاربر به گروه | `dict` |
| [`kick_chat_member`](#kick_chat_member) | اخراج و مسدود کردن کاربر از گروه | `DefaultResponse` |
| [`promote_chat_member`](#promote_chat_member) | ارتقای عضو به مدیر با تعیین مجوزها | `DefaultResponse` |
| [`restrict_chat_member`](#restrict_chat_member) | محدود کردن دسترسی‌های عضو در گروه | `DefaultResponse` |
| [`fetch_group_admins`](#fetch_group_admins) | دریافت فهرست مدیران گروه یا کانال | `dict` |
| [`clear_chat`](#clear_chat) | پاکسازی تاریخچه پیام‌های یک چت | `DefaultResponse` |
| [`delete_chat`](#delete_chat) | حذف کامل یک گفت‌وگو از فهرست چت‌ها | `DefaultResponse` |
| [`archive_dialogs`](#archive_dialogs) | انتقال چت‌ها به پوشه آرشیو | `ProtobufMessage` |
| [`unarchive_dialogs`](#unarchive_dialogs) | خارج کردن چت‌ها از پوشه آرشیو | `ProtobufMessage` |
| [`create_folder`](#create_folder) | ساخت پوشه سفارشی برای دسته‌بندی چت‌ها | `ProtobufMessage` |
| [`delete_folder`](#delete_folder) | حذف یک پوشه سفارشی چت | `ProtobufMessage` |

---

### `get_dialogs`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت لیست آخرین گفت‌وگوهای کاربر (پی‌وی‌ها، گروه‌ها و کانال‌ها). (نام مستعار: `get_chats`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `limit` | `int` | <span class="badge optional">No</span> | `30` | تعداد گفتگوهایی که باید بارگذاری شوند |

##### Return Value
`DialogsList[Dialog]`

```python
dialogs = await client.get_dialogs(limit=20)
for d in dialogs:
    print(f"چت: {d.title} | ناخوانده: {d.unread_count}")
```

---

### `get_chat`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت اطلاعات و مشخصات یک گفت‌وگو، گروه یا کاربر بر اساس شناسه عددی، یوزرنیم یا شیء Peer.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str, User, Chat]` | <span class="badge required">Yes</span> | — | آیدی عددی، یوزرنیم با/بدون `@`، یا شناسه چت |

##### Return Value
[`Chat`](types.md#chat) یا [`User`](types.md#user) یا `None`.

---

### `get_chat_members`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت صفحه اعضای حاضر در گروه با پشتیبانی از جستجو و فیلترها.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `limit` | `int` | <span class="badge optional">No</span> | `200` | تعداد اعضا در هر درخواست |
| `query` | `Optional[str]` | <span class="badge optional">No</span> | `None` | جستجوی نام یا یوزرنیم عضو خاص |

##### Return Value
`dict` — دیکشنری حاوی لیست اعضا و توکن صفحه بعدی.

```python
members = await client.get_chat_members(group_id, limit=50)
for member in members.get("members", []):
    print(f"عضو: {member.get('user_id')}")
```

---

### `get_chat_members_count`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت تعداد دقیق اعضای عضو در گروه یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه گروه یا کانال |

##### Return Value
`int` — تعداد اعضا.

---

### `create_group`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ساخت یک گروه جدید در بله به همراه اعضای اولیه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `title` | `str` | <span class="badge required">Yes</span> | — | نام گروه جدید |
| `users` | `Optional[List[Union[int, str]]]` | <span class="badge optional">No</span> | `None` | اعضای اولیه |

##### Return Value
[`Chat`](types.md#chat)

---

### `create_channel`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ایجاد یک کانال جدید برای اطلاع‌رسانی یا انتشار محتوا.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `title` | `str` | <span class="badge required">Yes</span> | — | نام کانال |
| `about` | `Optional[str]` | <span class="badge optional">No</span> | `""` | بیوگرافی و توضیحات |

##### Return Value
[`Chat`](types.md#chat)

---

### `edit_group_title`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تغییر نام و عنوان گروه یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `title` | `str` | <span class="badge required">Yes</span> | — | عنوان جدید |

##### Return Value
`DefaultResponse`

---

### `edit_group_about`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تغییر بیوگرافی و توضیحات گروه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `about` | `str` | <span class="badge required">Yes</span> | — | متن بیوگرافی |

##### Return Value
`DefaultResponse`

---

### `set_chat_photo`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تغییر تصویر یا آواتار گروه یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت |
| `photo` | `Union[str, bytes]` | <span class="badge required">Yes</span> | — | تصویر جدید |

##### Return Value
`DefaultResponse`

---

### `get_group_link`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت لینک دعوت خصوصی به گروه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |

##### Return Value
`Optional[str]`

---

### `revoke_group_link`
<span class="badge post">POST</span> <span class="badge async">Async</span>

باطل کردن لینک دعوت گروه و تولید یک لینک جدید.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |

##### Return Value
`Optional[str]`

---

### `join_chat`
<span class="badge post">POST</span> <span class="badge async">Async</span>

عضویت در گروه یا کانال با لینک دعوت.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `token_or_url` | `str` | <span class="badge required">Yes</span> | — | لینک دعوت کامل یا توکن |

##### Return Value
[`Chat`](types.md#chat)

---

### `leave_chat`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ترک داوطلبانه گروه یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گفت‌وگو |

##### Return Value
`DefaultResponse`

---

### `invite_user`
<span class="badge post">POST</span> <span class="badge async">Async</span>

افزودن مستقیم یک کاربر به گروه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربر |

##### Return Value
`dict`

---

### `kick_chat_member`
<span class="badge post">POST</span> <span class="badge async">Async</span>

اخراج یک کاربر از گروه. (نام مستعار: `kick_user`).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربر اخراجی |

##### Return Value
`DefaultResponse`

---

### `promote_chat_member`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارتقا دادن یک عضو به مقام مدیریت گروه و تعیین دقیق دسترسی‌ها.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربری که ادمین می‌شود |
| `can_edit_info` | `bool` | <span class="badge optional">No</span> | `True` | دسترسی تغییر نام و بیوگرافی گروه |
| `can_delete_messages` | `bool` | <span class="badge optional">No</span> | `True` | دسترسی حذف پیام‌های اعضا |
| `can_invite_users` | `bool` | <span class="badge optional">No</span> | `True` | دسترسی دعوت اعضای جدید |
| `can_pin_messages` | `bool` | <span class="badge optional">No</span> | `True` | دسترسی سنجاق کردن پیام‌ها |

##### Return Value
`DefaultResponse`

---

### `restrict_chat_member`
<span class="badge post">POST</span> <span class="badge async">Async</span>

محدود کردن دسترسی‌های یک کاربر عادی در گروه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه گروه |
| `user_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه کاربر |
| `permissions` | `ChatPermissions` | <span class="badge required">Yes</span> | — | دسترسی‌های مجاز کاربر |

##### Return Value
`DefaultResponse`

---

### `fetch_group_admins`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت فهرست مدیران گروه یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه گروه |

##### Return Value
`dict`

---

### `clear_chat`
<span class="badge post">POST</span> <span class="badge async">Async</span>

پاکسازی تاریخچه تمام پیام‌های یک گفت‌وگو بدون ترک کردن آن.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه چت هدف |

##### Return Value
`DefaultResponse`

---

### `delete_chat`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف کامل یک گفت‌وگو از فهرست چت‌های حساب کاربری.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه چت برای حذف |

##### Return Value
`DefaultResponse`

---

### `archive_dialogs`
<span class="badge post">POST</span> <span class="badge async">Async</span>

انتقال یک یا چند گفت‌وگو به پوشه آرشیو.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_ids` | `Iterable[str]` | <span class="badge required">Yes</span> | — | لیستی از شناسه‌های چت برای آرشیو شدن |

##### Return Value
`ProtobufMessage`

---

### `unarchive_dialogs`
<span class="badge post">POST</span> <span class="badge async">Async</span>

خارج کردن چت‌ها از پوشه آرشیو و بازگرداندن آن‌ها به صفحه اصلی.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_ids` | `Iterable[str]` | <span class="badge required">Yes</span> | — | لیستی از شناسه‌های چت |

##### Return Value
`ProtobufMessage`

---

### `create_folder`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ایجاد پوشه سفارشی برای نظم‌دهی به گفت‌وگوها (مانند پوشه «کاری»، «دوستان»، «کانال‌ها»).

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `name` | `str` | <span class="badge required">Yes</span> | — | نام نمایشی پوشه |
| `categories` | `Iterable[int]` | <span class="badge required">Yes</span> | — | دسته‌بندی‌های چت‌های مجاز |

##### Return Value
`ProtobufMessage`

---

### `delete_folder`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف یک پوشه سفارشی چت با شناسه پوشه.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `folder_id` | `int` | <span class="badge required">Yes</span> | — | شناسه عددی پوشه |

##### Return Value
`ProtobufMessage`
