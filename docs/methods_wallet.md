# 💳 مرجع متدهای امور بانکی، کیف پول و پاکت هدیه (Wallet & Banking API)

یکی از منحصر‌به‌فردترین و برجسته‌ترین قابلیت‌های پیام‌رسان بله، یکپارچگی عمیق با شبکه بانکی شتاب، سیستم پرداخت، کیف پول و امکان ارسال پاکت هدیه (عیدی و جوایز نقدی) است. در این بخش تمامی متدهای بانکی و مالی کتابخانه با مشخصات دقیق مستند شده‌اند.

---

## فهرست الفبایی متدها
| Method | Summary | Return Type |
| :--- | :--- | :--- |
| [`get_wallet`](#get_wallet) | استعلام موجودی و وضعیت کیف پول دیجیتال بله | `WalletResponse` |
| [`send_gift`](#send_gift) | ساخت و ارسال پاکت هدیه نقدی در چت یا گروه | `DefaultResponse` |
| [`open_gift`](#open_gift) | باز کردن و دریافت سهم نقدی از یک پاکت هدیه | `DefaultResponse` |
| [`get_payvand_cards`](#get_payvand_cards) | دریافت لیست کارت‌های بانکی ثبت‌شده کاربر در سامانه پیوند شتاب | `ProtobufMessage` |
| [`get_card_balance`](#get_card_balance) | استعلام لحظه‌ای مانده‌حساب کارت بانکی با رمز دوم | `ProtobufMessage` |
| [`get_card_transfer_token`](#get_card_transfer_token) | صدور توکن امنیتی برای انجام عملیات کارت‌به‌کارت | `ProtobufMessage` |
| [`change_default_card_number`](#change_default_card_number) | تغییر کارت بانکی پیش‌فرض جهت واریز و دریافت وجه | `ProtobufMessage` |
| [`remove_default_card_number`](#remove_default_card_number) | حذف کارت بانکی پیش‌فرض حساب | `ProtobufMessage` |
| [`get_bill_menu`](#get_bill_menu) | استعلام منوی پرداخت قبوض خدماتی | `ProtobufMessage` |

---

### `get_wallet`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت مشخصات کامل کیف پول کاربر، توکن معتبر کیف پول و موجودی فعال. (نام مستعار: `get_my_kifpools`).

#### Parameters
این متد هیچ ورودی اجباری دریافت نمی‌کند.

##### Return Value
`WalletResponse` — شامل شیء `wallet` حاوی `token`، شناسه کیف پول و موجودی.

##### Code Example
```python
wallet_info = await client.get_wallet()
if wallet_info.wallet:
    print(f"توکن کیف پول: {wallet_info.wallet.token}")
    print(f"وضعیت فعال: {wallet_info.wallet.is_active}")
```

---

### `send_gift`
<span class="badge post">POST</span> <span class="badge async">Async</span>

ارسال پاکت هدیه نقدی (عیدی، پاداش مسابقه یا قرعه‌کشی) به یک کاربر، گروه یا کانال.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `Union[int, str]` | <span class="badge required">Yes</span> | — | شناسه چت یا گروه مقصد که پاکت در آن فرستاده می‌شود |
| `amount` | `int` | <span class="badge required">Yes</span> | — | مبلغ کل پاکت هدیه به ریال (مثلاً `100000` ریال) |
| `message` | `str` | <span class="badge required">Yes</span> | — | پیام متنی تبریک یا عنوان پاکت هدیه |
| `gift_count` | `int` | <span class="badge optional">No</span> | `1` | تعداد نفراتی که می‌توانند از این پاکت سهم بردارند |
| `giving_type` | `GivingType` | <span class="badge optional">No</span> | `SAME` | نوع تقسیم: `SAME` (مساوی) یا `RANDOM` (شانسی/شانس متغیر) |
| `show_amounts` | `bool` | <span class="badge optional">No</span> | `True` | آیا مبالغ برداشتی برای سایرین نمایش داده شود؟ |
| `token` | `Optional[str]` | <span class="badge optional">No</span> | خودکار | توکن کیف پول (در صورت ارسال نشدن، خودکار واکشی می‌شود) |

##### Return Value
`DefaultResponse`

##### Code Example
```python
from bale.enums import GivingType

# ارسال پاکت هدیه ۱۰۰ هزار تومانی به ۵ نفر با مبالغ شانسی!
await client.send_gift(
    chat_id="my_group_id",
    amount=1_000_000,  # ریال
    message="عیدی توسعه‌دهندگان BaleNova! 🎁",
    gift_count=5,
    giving_type=GivingType.RANDOM
)
```

---

### `open_gift`
<span class="badge post">POST</span> <span class="badge async">Async</span>

باز کردن یک پاکت هدیه دریافت شده در چت و واریز سهم نقدی به کیف پول.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `chat_id` | `str` | <span class="badge required">Yes</span> | — | شناسه چتی که پاکت در آن قرار دارد |
| `message_id` | `str` | <span class="badge required">Yes</span> | — | شناسه پیامی که حاوی پاکت هدیه است |

##### Return Value
`DefaultResponse`

---

### `get_payvand_cards`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت فهرست تمام کارت‌های شتابی تاییدشده کاربر در سامانه پیوند بانک مرکزی.

#### Parameters
این متد پارامتری دریافت نمی‌کند.

##### Return Value
`ProtobufMessage` — شامل شماره کارت‌های ماسک‌شده، نام بانک صادرکننده و تاریخ انقضا.

---

### `get_card_balance`
<span class="badge post">POST</span> <span class="badge async">Async</span>

استعلام موجودی کارت بانکی کاربر با وارد کردن اطلاعات امنیتی رمز پویا و CVV2.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `card_number` | `str` | <span class="badge required">Yes</span> | — | شماره ۱۶ رقمی کارت بانکی |
| `cvv2` | `str` | <span class="badge required">Yes</span> | — | کد CVV2 درج‌شده روی کارت |
| `expire_date` | `str` | <span class="badge required">Yes</span> | — | تاریخ انقضا به فرمت ۴ رقمی (مثلاً `"0408"`) |
| `pin2` | `str` | <span class="badge required">Yes</span> | — | رمز دوم یک‌بار مصرف پویا (OTP) |

##### Return Value
`ProtobufMessage`

---

### `get_card_transfer_token`
<span class="badge post">POST</span> <span class="badge async">Async</span>

دریافت توکن رمزنگاری‌شده انتقال وجه جهت انجام کارت‌به‌کارت امن.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `source_card` | `str` | <span class="badge required">Yes</span> | — | شماره کارت مبدا ۱۶ رقمی |
| `dest_card` | `str` | <span class="badge required">Yes</span> | — | شماره کارت مقصد |
| `amount` | `int` | <span class="badge required">Yes</span> | — | مبلغ انتقال به ریال |

##### Return Value
`ProtobufMessage`

---

### `change_default_card_number`
<span class="badge post">POST</span> <span class="badge async">Async</span>

تنظیم کارت بانکی پیش‌فرض حساب جهت تسویه‌حساب و دریافت مبالغ.

#### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `card_number` | `str` | <span class="badge required">Yes</span> | — | شماره کارت ۱۶ رقمی مقصد |

##### Return Value
`ProtobufMessage`

---

### `remove_default_card_number`
<span class="badge post">POST</span> <span class="badge async">Async</span>

حذف شماره کارت پیش‌فرض تعیین‌شده در حساب.

#### Parameters
این متد ورودی دریافت نمی‌کند.

##### Return Value
`ProtobufMessage`

---

### `get_bill_menu`
<span class="badge get">GET</span> <span class="badge async">Async</span>

دریافت منوی دسته‌بندی و استعلام قبوض آب، برق، گاز و تلفن.

#### Parameters
این متد پارامتری دریافت نمی‌کند.

##### Return Value
`ProtobufMessage`
