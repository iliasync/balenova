# مرجع جامع متدهای بله به سبک داکیومنت تلگرام (Telegram Bot API Style)

این مستند تمامی ۶۹۰ متد پروتکل بله را با استانداردهای رسمی مستندسازی تلگرام (مشابه Telegram Bot API Documentation) معرفی می‌کند. برای هر متد، شرح عملکرد، جدول چپ‌به‌راست (LTR) مشخصات پارامترهای ورودی (نوع داده، اجباری یا اختیاری بودن و توضیحات) و نمونه کد استفاده پایتونیک به سبک PEP 8 ارائه شده است.

---

## Push (مدیریت اعلان‌ها و توکن‌های پوش‌نوتیفیکیشن)
> شناسه کامل سرویس در شبکه بله: `ai.bale.pushak.Push` — تعداد متدها: **6**

### RegisterGooglePush
اجرای متد رسمی `Push.RegisterGooglePush` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `projectId` | Integer | **Required** | Wire field `projectId` (python arg: `project_id`). |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.register_google_push(project_id=12345, token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("push", "RegisterGooglePush", project_id=12345, token="value")
```

---

### RegisterPush
اجرای متد رسمی `Push.RegisterPush` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `register` | Object | **Optional** | Wire field `register` (python arg: `register`). |
| `pushVersion` | Integer | **Required** | Wire field `pushVersion` (python arg: `push_version`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `encryptionKey`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.register_push(register={...}, push_version=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("push", "RegisterPush", register={...}, push_version=12345)
```

---

### SetConfig
اجرای متد رسمی `Push.SetConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `config` | Object | **Optional** | Wire field `config` (python arg: `config`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_config(config={...})

# ۲. فراخوانی با RPC
result = await app.rpc("push", "SetConfig", config={...})
```

---

### UnregisterAllPushCredentials
اجرای متد رسمی `Push.UnregisterAllPushCredentials` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.unregister_all_push_credentials()

# ۲. فراخوانی با RPC
result = await app.rpc("push", "UnregisterAllPushCredentials")
```

---

### UnregisterGooglePush
اجرای متد رسمی `Push.UnregisterGooglePush` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.unregister_google_push(token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("push", "UnregisterGooglePush", token="value")
```

---

### UnregisterPush
اجرای متد رسمی `Push.UnregisterPush` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `unregister` | Object | **Optional** | Wire field `unregister` (python arg: `unregister`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.unregister_push(unregister={...})

# ۲. فراخوانی با RPC
result = await app.rpc("push", "UnregisterPush", unregister={...})
```

---

## Files (مدیریت فایل‌ها، آپلود نسیم، سهمیه و دانلود)
> شناسه کامل سرویس در شبکه بله: `ai.bale.server.Files` — تعداد متدها: **7**

### FileUploadCancel
اجرای متد رسمی `Files.FileUploadCancel` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `file` | Object | **Optional** | Wire field `file` (python arg: `file`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `canceled`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.file_upload_cancel(file={...})

# ۲. فراخوانی با RPC
result = await app.rpc("files", "FileUploadCancel", file={...})
```

---

### GetNasimFilePublicUrl
اجرای متد رسمی `Files.GetNasimFilePublicUrl` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `file` | Object | **Optional** | Wire field `file` (python arg: `file`). |
| `filename` | Object | **Optional** | Wire field `filename` (python arg: `filename`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fileUrl`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_nasim_file_public_url(peer={...}, file={...}, filename={...})

# ۲. فراخوانی با RPC
result = await app.rpc("files", "GetNasimFilePublicUrl", peer={...}, file={...}, filename={...})
```

---

### GetNasimFileUploadResume
اجرای متد رسمی `Files.GetNasimFileUploadResume` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `file` | Object | **Optional** | Wire field `file` (python arg: `file`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fileUrl, canResume`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_nasim_file_upload_resume(file={...})

# ۲. فراخوانی با RPC
result = await app.rpc("files", "GetNasimFileUploadResume", file={...})
```

---

### GetNasimFileUploadUrl
اجرای متد رسمی `Files.GetNasimFileUploadUrl` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `expectedSize` | Integer | **Required** | Wire field `expectedSize` (python arg: `expected_size`). |
| `crc` | Integer | **Required** | Wire field `crc` (python arg: `crc`). |
| `uid` | Integer | **Required** | Wire field `uid` (python arg: `uid`). |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |
| `mimeType` | String | **Required** | Wire field `mimeType` (python arg: `mime_type`). |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `sendType` | Object | **Optional** | Wire field `sendType` (python arg: `send_type`). |
| `chunkSize` | Integer | **Required** | Wire field `chunkSize` (python arg: `chunk_size`). |
| `compressedSize` | Integer | **Required** | Wire field `compressedSize` (python arg: `compressed_size`). |
| `fileKind` | Integer | **Required** | Wire field `fileKind` (python arg: `file_kind`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fileId, url, duplicate, chunkSize, blockSize`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_nasim_file_upload_url(expected_size=12345, crc=12345, uid=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("files", "GetNasimFileUploadUrl", expected_size=12345, crc=12345, uid=12345)
```

---

### GetNasimFileUrl
اجرای متد رسمی `Files.GetNasimFileUrl` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `file` | Object | **Optional** | Wire field `file` (python arg: `file`). |
| `ciphertext` | Boolean | **Required** | Wire field `ciphertext` (python arg: `ciphertext`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fileUrl`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_nasim_file_url(file={...}, ciphertext=True)

# ۲. فراخوانی با RPC
result = await app.rpc("files", "GetNasimFileUrl", file={...}, ciphertext=True)
```

---

### GetNasimFileUrls
اجرای متد رسمی `Files.GetNasimFileUrls` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `files` | Array of Object | **Required** | Wire field `files` (python arg: `files`). |
| `ciphertext` | Boolean | **Required** | Wire field `ciphertext` (python arg: `ciphertext`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fileUrls`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_nasim_file_urls(files={...}, ciphertext=True)

# ۲. فراخوانی با RPC
result = await app.rpc("files", "GetNasimFileUrls", files={...}, ciphertext=True)
```

---

### GetUploadLimits
اجرای متد رسمی `Files.GetUploadLimits` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `uploadLimitBytes, temporaryMaxBytes, permanentMaxBytes, boughtCapacityRemainingBytes, boughtCapacityUnlimited`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_upload_limits()

# ۲. فراخوانی با RPC
result = await app.rpc("files", "GetUploadLimits")
```

---

## BankAccountPreferences (تنظیمات حساب‌های بانکی و اطلاع‌رسانی یارا)
> شناسه کامل سرویس در شبکه بله: `bale.BankAccountPreferences.v1.BankAccountPreferences` — تعداد متدها: **3**

### ActivateYaraMessaging
اجرای متد رسمی `BankAccountPreferences.ActivateYaraMessaging` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `accountNumber` | String | **Required** | Wire field `accountNumber` (python arg: `account_number`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.activate_yara_messaging(account_number="value")

# ۲. فراخوانی با RPC
result = await app.rpc("bankaccountpreferences", "ActivateYaraMessaging", account_number="value")
```

---

### EditPreference
اجرای متد رسمی `BankAccountPreferences.EditPreference` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `preference` | Object | **Optional** | Wire field `preference` (python arg: `preference`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_preference(preference={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bankaccountpreferences", "EditPreference", preference={...})
```

---

### GetPreferences
اجرای متد رسمی `BankAccountPreferences.GetPreferences` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `accounts`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_preferences()

# ۲. فراخوانی با RPC
result = await app.rpc("bankaccountpreferences", "GetPreferences")
```

---

## Abacus (آمار بازدیدها، واکنش‌ها (ری‌اکشن) و شمارنده‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.abacus.v1.Abacus` — تعداد متدها: **9**

### EnableShowReactionFlag
اجرای متد رسمی `Abacus.EnableShowReactionFlag` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.enable_show_reaction_flag()

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "EnableShowReactionFlag")
```

---

### GetMessageReactionsList
اجرای متد رسمی `Abacus.GetMessageReactionsList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `page` | Integer | **Required** | Wire field `page` (python arg: `page`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userReactions`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_message_reactions_list(peer={...}, rid=12345, date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "GetMessageReactionsList", peer={...}, rid=12345, date=12345)
```

---

### GetMessagesReactions
اجرای متد رسمی `Abacus.GetMessagesReactions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `mids` | Array of Object | **Required** | Wire field `mids` (python arg: `mids`). |
| `originPeer` | Object | **Optional** | Wire field `originPeer` (python arg: `origin_peer`). |
| `originMids` | Array of Object | **Required** | Wire field `originMids` (python arg: `origin_mids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `containers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_messages_reactions(peer={...}, mids={...}, origin_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "GetMessagesReactions", peer={...}, mids={...}, origin_peer={...})
```

---

### GetMessagesViews
اجرای متد رسمی `Abacus.GetMessagesViews` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `mids` | Array of Object | **Required** | Wire field `mids` (python arg: `mids`). |
| `increment` | Boolean | **Required** | Wire field `increment` (python arg: `increment`). |
| `correctMids` | Array of Object | **Required** | Wire field `correctMids` (python arg: `correct_mids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `containers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_messages_views(peer={...}, mids={...}, increment=True)

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "GetMessagesViews", peer={...}, mids={...}, increment=True)
```

---

### GetShowReactionFlag
اجرای متد رسمی `Abacus.GetShowReactionFlag` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userId, isEnable`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_show_reaction_flag()

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "GetShowReactionFlag")
```

---

### LoadReactions
اجرای متد رسمی `Abacus.LoadReactions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `mids` | Array of Object | **Required** | Wire field `mids` (python arg: `mids`). |
| `ignoreCountViews` | Boolean | **Required** | Wire field `ignoreCountViews` (python arg: `ignore_count_views`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `containers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_reactions(peer={...}, mids={...}, ignore_count_views=True)

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "LoadReactions", peer={...}, mids={...}, ignore_count_views=True)
```

---

### MessageReactionsRead
اجرای متد رسمی `Abacus.MessageReactionsRead` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.message_reactions_read(peer={...}, message_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "MessageReactionsRead", peer={...}, message_id={...})
```

---

### MessageRemoveReaction
اجرای متد رسمی `Abacus.MessageRemoveReaction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, reactions, state`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.message_remove_reaction(peer={...}, rid=12345, code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "MessageRemoveReaction", peer={...}, rid=12345, code="value")
```

---

### MessageSetReaction
اجرای متد رسمی `Abacus.MessageSetReaction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, reactions, state`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.message_set_reaction(peer={...}, rid=12345, code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("abacus", "MessageSetReaction", peer={...}, rid=12345, code="value")
```

---

## Advertisement (سامانه تبلیغات، ایجاد کمپین، استعلام هزینه و تسویه حساب)
> شناسه کامل سرویس در شبکه بله: `bale.advertisement.v1.Advertisement` — تعداد متدها: **123**

### AddCustomIncome
اجرای متد رسمی `Advertisement.AddCustomIncome` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `type` | Integer | **Required** | Wire field `type` (python arg: `type`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `customerUserId` | Integer | **Required** | Wire field `customerUserId` (python arg: `customer_user_id`). |
| `customerName` | String | **Required** | Wire field `customerName` (python arg: `customer_name`). |
| `paymentMethod` | Integer | **Required** | Wire field `paymentMethod` (python arg: `payment_method`). |
| `paymentDate` | Integer | **Required** | Wire field `paymentDate` (python arg: `payment_date`). |
| `depositTrackingId` | Object | **Optional** | Wire field `depositTrackingId` (python arg: `deposit_tracking_id`). |
| `adId` | Object | **Optional** | Wire field `adId` (python arg: `ad_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `id`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_custom_income(type=12345, amount=12345, description="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "AddCustomIncome", type=12345, amount=12345, description="value")
```

---

### BuildAudienceQuery
اجرای متد رسمی `Advertisement.BuildAudienceQuery` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `definition` | Object | **Optional** | Wire field `definition` (python arg: `definition`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `query, estimatedSize`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.build_audience_query(definition={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "BuildAudienceQuery", definition={...})
```

---

### CalculatePrice
اجرای متد رسمی `Advertisement.CalculatePrice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `spot` | Integer | **Required** | Wire field `spot` (python arg: `spot`). |
| `viewCount` | Integer | **Required** | Wire field `viewCount` (python arg: `view_count`). |
| `clickCount` | Integer | **Required** | Wire field `clickCount` (python arg: `click_count`). |
| `link` | String | **Required** | Wire field `link` (python arg: `link`). |
| `isInstant` | Boolean | **Required** | Wire field `isInstant` (python arg: `is_instant`). |
| `tag1` | Integer | **Required** | Wire field `tag1` (python arg: `tag1`). |
| `tag2` | Integer | **Required** | Wire field `tag2` (python arg: `tag2`). |
| `targeting` | Object | **Optional** | Wire field `targeting` (python arg: `targeting`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `finalPrice, clickUnitPrice`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.calculate_price(spot=12345, view_count=12345, click_count=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CalculatePrice", spot=12345, view_count=12345, click_count=12345)
```

---

### ChangeAccountState
اجرای متد رسمی `Advertisement.ChangeAccountState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |
| `ownerId` | Integer | **Required** | Wire field `ownerId` (python arg: `owner_id`). |
| `reason` | String | **Required** | Wire field `reason` (python arg: `reason`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_account_state(state=12345, owner_id=12345, reason="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeAccountState", state=12345, owner_id=12345, reason="value")
```

---

### ChangeAdState
اجرای متد رسمی `Advertisement.ChangeAdState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |
| `reason` | String | **Required** | Wire field `reason` (python arg: `reason`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_ad_state(ad_id="value", state=12345, reason="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeAdState", ad_id="value", state=12345, reason="value")
```

---

### ChangeBonusCodeState
اجرای متد رسمی `Advertisement.ChangeBonusCodeState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_bonus_code_state(code="value", state=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeBonusCodeState", code="value", state=12345)
```

---

### ChangeCampaignContentState
اجرای متد رسمی `Advertisement.ChangeCampaignContentState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `campaignId` | String | **Required** | Wire field `campaignId` (python arg: `campaign_id`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |
| `reason` | String | **Required** | Wire field `reason` (python arg: `reason`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_campaign_content_state(campaign_id="value", state=12345, reason="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeCampaignContentState", campaign_id="value", state=12345, reason="value")
```

---

### ChangeCampaignState
اجرای متد رسمی `Advertisement.ChangeCampaignState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `campaignId` | String | **Required** | Wire field `campaignId` (python arg: `campaign_id`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |
| `rejectionReason` | String | **Required** | Wire field `rejectionReason` (python arg: `rejection_reason`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_campaign_state(campaign_id="value", state=12345, rejection_reason="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeCampaignState", campaign_id="value", state=12345, rejection_reason="value")
```

---

### ChangeChannelIncomeOwner
اجرای متد رسمی `Advertisement.ChangeChannelIncomeOwner` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_channel_income_owner(peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeChannelIncomeOwner", peer_id={...})
```

---

### ChangeChannelShowAdPermissions
اجرای متد رسمی `Advertisement.ChangeChannelShowAdPermissions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `showAds` | Object | **Optional** | Wire field `showAds` (python arg: `show_ads`). |
| `timeRestrict` | Object | **Optional** | Wire field `timeRestrict` (python arg: `time_restrict`). |
| `categoryFilter` | Object | **Optional** | Wire field `categoryFilter` (python arg: `category_filter`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_channel_show_ad_permissions(peer_id={...}, show_ads={...}, time_restrict={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeChannelShowAdPermissions", peer_id={...}, show_ads={...}, time_restrict={...})
```

---

### ChangeStatusDialogAdOrder
اجرای متد رسمی `Advertisement.ChangeStatusDialogAdOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `targetStatus` | Integer | **Required** | Wire field `targetStatus` (python arg: `target_status`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `rejectionReason` | Object | **Optional** | Wire field `rejectionReason` (python arg: `rejection_reason`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_status_dialog_ad_order(id="value", target_status=12345, date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeStatusDialogAdOrder", id="value", target_status=12345, date=12345)
```

---

### ChangeUserDataState
اجرای متد رسمی `Advertisement.ChangeUserDataState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ownerId` | Integer | **Required** | Wire field `ownerId` (python arg: `owner_id`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_user_data_state(owner_id=12345, state=12345, reason=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChangeUserDataState", owner_id=12345, state=12345, reason=12345)
```

---

### ChannelIncomeGetCredit
اجرای متد رسمی `Advertisement.ChannelIncomeGetCredit` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.channel_income_get_credit(peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChannelIncomeGetCredit", peer_id={...})
```

---

### ChannelIncomeKifTransfer
اجرای متد رسمی `Advertisement.ChannelIncomeKifTransfer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `payType` | Integer | **Required** | Wire field `payType` (python arg: `pay_type`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.channel_income_kif_transfer(peer_id={...}, pay_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChannelIncomeKifTransfer", peer_id={...}, pay_type=12345)
```

---

### ChannelIncomePayment
اجرای متد رسمی `Advertisement.ChannelIncomePayment` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `payType` | Integer | **Required** | Wire field `payType` (python arg: `pay_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `factorHtml`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.channel_income_payment(peer_id={...}, pay_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ChannelIncomePayment", peer_id={...}, pay_type=12345)
```

---

### ConvertIncome
اجرای متد رسمی `Advertisement.ConvertIncome` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `convertToPoints` | Object | **Optional** | Wire field `convertToPoints` (python arg: `convert_to_points`). |
| `convertToGiftPacket` | Object | **Optional** | Wire field `convertToGiftPacket` (python arg: `convert_to_gift_packet`). |
| `convertToGiftPacketForChannelOwner` | Object | **Optional** | Wire field `convertToGiftPacketForChannelOwner` (python arg: `convert_to_gift_packet_for_channel_owner`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.convert_income(convert_to_points={...}, convert_to_gift_packet={...}, convert_to_gift_packet_for_channel_owner={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ConvertIncome", convert_to_points={...}, convert_to_gift_packet={...}, convert_to_gift_packet_for_channel_owner={...})
```

---

### CreateAd
اجرای متد رسمی `Advertisement.CreateAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adData` | Object | **Optional** | Wire field `adData` (python arg: `ad_data`). |
| `price` | Integer | **Required** | Wire field `price` (python arg: `price`). |
| `depositTrackingId` | Object | **Optional** | Wire field `depositTrackingId` (python arg: `deposit_tracking_id`). |
| `paymentMethod` | Integer | **Required** | Wire field `paymentMethod` (python arg: `payment_method`). |
| `paymentDate` | Object | **Optional** | Wire field `paymentDate` (python arg: `payment_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `adId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_ad(ad_data={...}, price=12345, deposit_tracking_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CreateAd", ad_data={...}, price=12345, deposit_tracking_id={...})
```

---

### CreateAndStartChannelAd
اجرای متد رسمی `Advertisement.CreateAndStartChannelAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `link` | String | **Required** | Wire field `link` (python arg: `link`). |
| `platform` | Integer | **Required** | Wire field `platform` (python arg: `platform`). |
| `viewCount` | Integer | **Required** | Wire field `viewCount` (python arg: `view_count`). |
| `clickCount` | Integer | **Required** | Wire field `clickCount` (python arg: `click_count`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `id`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_and_start_channel_ad(title="value", description="value", link="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CreateAndStartChannelAd", title="value", description="value", link="value")
```

---

### CreateAutomatedAudience
اجرای متد رسمی `Advertisement.CreateAutomatedAudience` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `definition` | Object | **Optional** | Wire field `definition` (python arg: `definition`). |
| `single` | Object | **Optional** | Wire field `single` (python arg: `single`). |
| `randomGroups` | Object | **Optional** | Wire field `randomGroups` (python arg: `random_groups`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `result`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_automated_audience(definition={...}, single={...}, random_groups={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CreateAutomatedAudience", definition={...}, single={...}, random_groups={...})
```

---

### CreateBaleDialogCustomAd
اجرای متد رسمی `Advertisement.CreateBaleDialogCustomAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pic` | String | **Required** | Wire field `pic` (python arg: `pic`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `link` | String | **Required** | Wire field `link` (python arg: `link`). |
| `platform` | Integer | **Required** | Wire field `platform` (python arg: `platform`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `id`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_bale_dialog_custom_ad(pic="value", title="value", description="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CreateBaleDialogCustomAd", pic="value", title="value", description="value")
```

---

### CreateBonusCode
اجرای متد رسمی `Advertisement.CreateBonusCode` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `data` | Object | **Optional** | Wire field `data` (python arg: `data`). |
| `autoGenerate` | Boolean | **Required** | Wire field `autoGenerate` (python arg: `auto_generate`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `code`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_bonus_code(data={...}, auto_generate=True)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CreateBonusCode", data={...}, auto_generate=True)
```

---

### CreateChannelIncomeFactor
اجرای متد رسمی `Advertisement.CreateChannelIncomeFactor` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `year` | Integer | **Required** | Wire field `year` (python arg: `year`). |
| `month` | Integer | **Required** | Wire field `month` (python arg: `month`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `factorHtml`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_channel_income_factor(peer_id={...}, year=12345, month=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CreateChannelIncomeFactor", peer_id={...}, year=12345, month=12345)
```

---

### CreateCustomCampaignPackage
اجرای متد رسمی `Advertisement.CreateCustomCampaignPackage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userId` | Integer | **Optional** | Wire field `userId` (python arg: `user_id`). |
| `baseCredit` | Integer | **Required** | Wire field `baseCredit` (python arg: `base_credit`). |
| `creditExpireDays` | Integer | **Required** | Wire field `creditExpireDays` (python arg: `credit_expire_days`). |
| `campaignDailyCapacity` | Integer | **Required** | Wire field `campaignDailyCapacity` (python arg: `campaign_daily_capacity`). |
| `allowedConcurrentCampaign` | Integer | **Required** | Wire field `allowedConcurrentCampaign` (python arg: `allowed_concurrent_campaign`). |
| `audienceId` | Integer | **Optional** | Wire field `audienceId` (python arg: `audience_id`). |
| `campaignViewCoef` | Integer | **Required** | Wire field `campaignViewCoef` (python arg: `campaign_view_coef`). |
| `campaignClickCoef` | Integer | **Required** | Wire field `campaignClickCoef` (python arg: `campaign_click_coef`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_custom_campaign_package(user_id=12345, base_credit=12345, credit_expire_days=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "CreateCustomCampaignPackage", user_id=12345, base_credit=12345, credit_expire_days=12345)
```

---

### DeleteCustomIncome
اجرای متد رسمی `Advertisement.DeleteCustomIncome` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_custom_income(id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "DeleteCustomIncome", id="value")
```

---

### EditAccount
اجرای متد رسمی `Advertisement.EditAccount` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `account` | Object | **Optional** | Wire field `account` (python arg: `account`). |
| `isRestoreExpiredCredit` | Boolean | **Required** | Wire field `isRestoreExpiredCredit` (python arg: `is_restore_expired_credit`). |
| `depositTrackingId` | Object | **Optional** | Wire field `depositTrackingId` (python arg: `deposit_tracking_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_account(account={...}, is_restore_expired_credit=True, deposit_tracking_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "EditAccount", account={...}, is_restore_expired_credit=True, deposit_tracking_id={...})
```

---

### EditAd
اجرای متد رسمی `Advertisement.EditAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ad` | Object | **Optional** | Wire field `ad` (python arg: `ad`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_ad(ad={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "EditAd", ad={...})
```

---

### EditCampaignAd
اجرای متد رسمی `Advertisement.EditCampaignAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ad` | Object | **Optional** | Wire field `ad` (python arg: `ad`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_campaign_ad(ad={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "EditCampaignAd", ad={...})
```

---

### EditCampaignContent
اجرای متد رسمی `Advertisement.EditCampaignContent` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `campaign` | Object | **Optional** | Wire field `campaign` (python arg: `campaign`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_campaign_content(campaign={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "EditCampaignContent", campaign={...})
```

---

### EstimateChannelSponsoredIncome
اجرای متد رسمی `Advertisement.EstimateChannelSponsoredIncome` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `estimatedViews, estimatedIncome`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.estimate_channel_sponsored_income(peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "EstimateChannelSponsoredIncome", peer_id={...})
```

---

### FinishAd
اجرای متد رسمی `Advertisement.FinishAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.finish_ad(id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "FinishAd", id="value")
```

---

### FinishAdV2
اجرای متد رسمی `Advertisement.FinishAdV2` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.finish_ad_v2(ad_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "FinishAdV2", ad_id="value")
```

---

### FinishChannelAd
اجرای متد رسمی `Advertisement.FinishChannelAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.finish_channel_ad(id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "FinishChannelAd", id="value")
```

---

### GetAccountData
اجرای متد رسمی `Advertisement.GetAccountData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ownerId` | Integer | **Required** | Wire field `ownerId` (python arg: `owner_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_account_data(owner_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAccountData", owner_id=12345)
```

---

### GetAccounts
اجرای متد رسمی `Advertisement.GetAccounts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pageData` | Object | **Optional** | Wire field `pageData` (python arg: `page_data`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_accounts(page_data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAccounts", page_data={...})
```

---

### GetAccountsByState
اجرای متد رسمی `Advertisement.GetAccountsByState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |
| `pageData` | Object | **Optional** | Wire field `pageData` (python arg: `page_data`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_accounts_by_state(state=12345, page_data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAccountsByState", state=12345, page_data={...})
```

---

### GetActiveAds
اجرای متد رسمی `Advertisement.GetActiveAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_active_ads()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetActiveAds")
```

---

### GetActiveChannelAds
اجرای متد رسمی `Advertisement.GetActiveChannelAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_active_channel_ads()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetActiveChannelAds")
```

---

### GetAdData
اجرای متد رسمی `Advertisement.GetAdData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `adData`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ad_data(ad_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAdData", ad_id="value")
```

---

### GetAdDetail
اجرای متد رسمی `Advertisement.GetAdDetail` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `from` | Integer | **Required** | Wire field `from` (python arg: `from`). |
| `to` | Integer | **Required** | Wire field `to` (python arg: `to`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ad_detail(title="value", from=12345, to=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAdDetail", title="value", from=12345, to=12345)
```

---

### GetAdProvider
اجرای متد رسمی `Advertisement.GetAdProvider` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `adType` | Integer | **Required** | Wire field `adType` (python arg: `ad_type`). |
| `adSpot` | Integer | **Required** | Wire field `adSpot` (python arg: `ad_spot`). |
| `adCount` | Integer | **Required** | Wire field `adCount` (python arg: `ad_count`). |
| `includeNonZeroPlacements` | Object | **Optional** | Wire field `includeNonZeroPlacements` (python arg: `include_non_zero_placements`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `content`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ad_provider(peer_id={...}, ad_type=12345, ad_spot=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAdProvider", peer_id={...}, ad_type=12345, ad_spot=12345)
```

---

### GetAdReport
اجرای متد رسمی `Advertisement.GetAdReport` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `views, clicks, title, link`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ad_report(ad_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAdReport", ad_id="value")
```

---

### GetAdReportV2
اجرای متد رسمی `Advertisement.GetAdReportV2` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ad_report_v2(ad_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAdReportV2", ad_id="value")
```

---

### GetAdsBySpotAndPlatform
اجرای متد رسمی `Advertisement.GetAdsBySpotAndPlatform` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `spot` | Integer | **Required** | Wire field `spot` (python arg: `spot`). |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ads_by_spot_and_platform(spot=12345, peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAdsBySpotAndPlatform", spot=12345, peer_id={...})
```

---

### GetAdsByStateAndSpot
اجرای متد رسمی `Advertisement.GetAdsByStateAndSpot` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagingData` | Object | **Optional** | Wire field `pagingData` (python arg: `paging_data`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |
| `spot` | Integer | **Required** | Wire field `spot` (python arg: `spot`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ads_by_state_and_spot(paging_data={...}, state=12345, spot=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAdsByStateAndSpot", paging_data={...}, state=12345, spot=12345)
```

---

### GetAllChannelIncomesFactor
اجرای متد رسمی `Advertisement.GetAllChannelIncomesFactor` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `year` | Integer | **Required** | Wire field `year` (python arg: `year`). |
| `month` | Integer | **Required** | Wire field `month` (python arg: `month`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `factors`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_all_channel_incomes_factor(year=12345, month=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAllChannelIncomesFactor", year=12345, month=12345)
```

---

### GetAllPaymentHistory
اجرای متد رسمی `Advertisement.GetAllPaymentHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `startDate` | Integer | **Required** | Wire field `startDate` (python arg: `start_date`). |
| `endDate` | Integer | **Required** | Wire field `endDate` (python arg: `end_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `records`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_all_payment_history(start_date=12345, end_date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAllPaymentHistory", start_date=12345, end_date=12345)
```

---

### GetAvailableCampaignStartDate
اجرای متد رسمی `Advertisement.GetAvailableCampaignStartDate` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `date`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_available_campaign_start_date()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAvailableCampaignStartDate")
```

---

### GetAwaitingToShowAds
اجرای متد رسمی `Advertisement.GetAwaitingToShowAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_awaiting_to_show_ads()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAwaitingToShowAds")
```

---

### GetAwaitingToShowChannelAds
اجرای متد رسمی `Advertisement.GetAwaitingToShowChannelAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_awaiting_to_show_channel_ads()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetAwaitingToShowChannelAds")
```

---

### GetBaleCustomAd
اجرای متد رسمی `Advertisement.GetBaleCustomAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ad`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bale_custom_ad(ad_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetBaleCustomAd", ad_id="value")
```

---

### GetBonusCodeData
اجرای متد رسمی `Advertisement.GetBonusCodeData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bonus_code_data(code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetBonusCodeData", code="value")
```

---

### GetBonusCodes
اجرای متد رسمی `Advertisement.GetBonusCodes` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pageData` | Object | **Optional** | Wire field `pageData` (python arg: `page_data`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bonus_codes(page_data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetBonusCodes", page_data={...})
```

---

### GetBusinessAds
اجرای متد رسمی `Advertisement.GetBusinessAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagingData` | Object | **Optional** | Wire field `pagingData` (python arg: `paging_data`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_business_ads(paging_data={...}, state=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetBusinessAds", paging_data={...}, state=12345)
```

---

### GetCRMIssues
اجرای متد رسمی `Advertisement.GetCRMIssues` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userIssue` | Object | **Optional** | Wire field `userIssue` (python arg: `user_issue`). |
| `allIssue` | Object | **Optional** | Wire field `allIssue` (python arg: `all_issue`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_crm_issues(user_issue={...}, all_issue={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCRMIssues", user_issue={...}, all_issue={...})
```

---

### GetCampaignAds
اجرای متد رسمی `Advertisement.GetCampaignAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagingData` | Object | **Optional** | Wire field `pagingData` (python arg: `paging_data`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_campaign_ads(paging_data={...}, state=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCampaignAds", paging_data={...}, state=12345)
```

---

### GetCampaignContentById
اجرای متد رسمی `Advertisement.GetCampaignContentById` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `campaignId` | String | **Required** | Wire field `campaignId` (python arg: `campaign_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `campaign`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_campaign_content_by_id(campaign_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCampaignContentById", campaign_id="value")
```

---

### GetCampaignContents
اجرای متد رسمی `Advertisement.GetCampaignContents` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagingData` | Object | **Optional** | Wire field `pagingData` (python arg: `paging_data`). |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `campaigns`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_campaign_contents(paging_data={...}, state=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCampaignContents", paging_data={...}, state=12345)
```

---

### GetCampaignData
اجرای متد رسمی `Advertisement.GetCampaignData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `campaignId` | String | **Required** | Wire field `campaignId` (python arg: `campaign_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_campaign_data(campaign_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCampaignData", campaign_id="value")
```

---

### GetChannelAds
اجرای متد رسمی `Advertisement.GetChannelAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupId` | Object | **Optional** | Wire field `groupId` (python arg: `group_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_ads(group_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelAds", group_id={...})
```

---

### GetChannelEarnMoneyInfo
اجرای متد رسمی `Advertisement.GetChannelEarnMoneyInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupId` | Object | **Optional** | Wire field `groupId` (python arg: `group_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currentMonthIncome, notPaidIncome, adCount, adCountUpdateDate`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_earn_money_info(group_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelEarnMoneyInfo", group_id={...})
```

---

### GetChannelEarnMoneyStatus
اجرای متد رسمی `Advertisement.GetChannelEarnMoneyStatus` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupId` | Object | **Optional** | Wire field `groupId` (python arg: `group_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `status`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_earn_money_status(group_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelEarnMoneyStatus", group_id={...})
```

---

### GetChannelGraphReport
اجرای متد رسمی `Advertisement.GetChannelGraphReport` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `endTime` | Integer | **Required** | Wire field `endTime` (python arg: `end_time`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `viewGraph`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_graph_report(peer_id={...}, start_time=12345, end_time=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelGraphReport", peer_id={...}, start_time=12345, end_time=12345)
```

---

### GetChannelIncomeReport
اجرای متد رسمی `Advertisement.GetChannelIncomeReport` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `incomeReports`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_income_report(peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelIncomeReport", peer_id={...})
```

---

### GetChannelOwnerBankInformation
اجرای متد رسمی `Advertisement.GetChannelOwnerBankInformation` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channelId` | Object | **Optional** | Wire field `channelId` (python arg: `channel_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userId, nationalCode, birthDate, address, postalCode, melliAccountNumber, firstName, lastName, phone, state, reason, channelNick`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_owner_bank_information(channel_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelOwnerBankInformation", channel_id={...})
```

---

### GetChannelShowAdCategoryFilter
اجرای متد رسمی `Advertisement.GetChannelShowAdCategoryFilter` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `categories`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_show_ad_category_filter(peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelShowAdCategoryFilter", peer_id={...})
```

---

### GetChannelShowAdPermissions
اجرای متد رسمی `Advertisement.GetChannelShowAdPermissions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `showSponsoredAd, verifiedUserId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_show_ad_permissions(peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelShowAdPermissions", peer_id={...})
```

---

### GetChannelShowAdTimeRestrict
اجرای متد رسمی `Advertisement.GetChannelShowAdTimeRestrict` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_show_ad_time_restrict(peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelShowAdTimeRestrict", peer_id={...})
```

---

### GetChannelSponsoredIncomeReport
اجرای متد رسمی `Advertisement.GetChannelSponsoredIncomeReport` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `endTime` | Integer | **Required** | Wire field `endTime` (python arg: `end_time`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `totalViews, totalIncome, totalAdCount, averageCtr, dailyReports, categoryReports`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_sponsored_income_report(peer_id={...}, start_time=12345, end_time=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelSponsoredIncomeReport", peer_id={...}, start_time=12345, end_time=12345)
```

---

### GetChannelUndepositedIncomes
اجرای متد رسمی `Advertisement.GetChannelUndepositedIncomes` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `year` | Integer | **Required** | Wire field `year` (python arg: `year`). |
| `month` | Integer | **Required** | Wire field `month` (python arg: `month`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `items`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_undeposited_incomes(year=12345, month=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelUndepositedIncomes", year=12345, month=12345)
```

---

### GetChannelsViewReport
اجرای متد رسمی `Advertisement.GetChannelsViewReport` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `endTime` | Integer | **Required** | Wire field `endTime` (python arg: `end_time`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `channelsView`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channels_view_report(start_time=12345, end_time=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetChannelsViewReport", start_time=12345, end_time=12345)
```

---

### GetConfig
اجرای متد رسمی `Advertisement.GetConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `config`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_config()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetConfig")
```

---

### GetCreditHistory
اجرای متد رسمی `Advertisement.GetCreditHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ownerId` | Integer | **Required** | Wire field `ownerId` (python arg: `owner_id`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `endTime` | Integer | **Required** | Wire field `endTime` (python arg: `end_time`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `creditHistories`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_credit_history(owner_id=12345, start_time=12345, end_time=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCreditHistory", owner_id=12345, start_time=12345, end_time=12345)
```

---

### GetCreditableAccounts
اجرای متد رسمی `Advertisement.GetCreditableAccounts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pageData` | Object | **Optional** | Wire field `pageData` (python arg: `page_data`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_creditable_accounts(page_data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCreditableAccounts", page_data={...})
```

---

### GetCustomIncomes
اجرای متد رسمی `Advertisement.GetCustomIncomes` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `endTime` | Integer | **Required** | Wire field `endTime` (python arg: `end_time`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `records`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_custom_incomes(start_time=12345, end_time=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetCustomIncomes", start_time=12345, end_time=12345)
```

---

### GetDialogAdOrderDetails
اجرای متد رسمی `Advertisement.GetDialogAdOrderDetails` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogAdOrder`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_dialog_ad_order_details()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetDialogAdOrderDetails")
```

---

### GetDialogAdOrderPaymentToken
اجرای متد رسمی `Advertisement.GetDialogAdOrderPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `rialAmount` | Integer | **Required** | Wire field `rialAmount` (python arg: `rial_amount`). |
| `coinAmount` | Integer | **Required** | Wire field `coinAmount` (python arg: `coin_amount`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_dialog_ad_order_payment_token(id="value", rial_amount=12345, coin_amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetDialogAdOrderPaymentToken", id="value", rial_amount=12345, coin_amount=12345)
```

---

### GetFactorEligibleAds
اجرای متد رسمی `Advertisement.GetFactorEligibleAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `tBegin` | Integer | **Required** | Wire field `tBegin` (python arg: `t_begin`). |
| `tEnd` | Integer | **Required** | Wire field `tEnd` (python arg: `t_end`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_factor_eligible_ads(t_begin=12345, t_end=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetFactorEligibleAds", t_begin=12345, t_end=12345)
```

---

### GetInvoiceContent
اجرای متد رسمی `Advertisement.GetInvoiceContent` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `invoiceRequestId` | String | **Required** | Wire field `invoiceRequestId` (python arg: `invoice_request_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `id, description, responseCode, data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_invoice_content(invoice_request_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetInvoiceContent", invoice_request_id="value")
```

---

### GetLegalOrgChannels
اجرای متد رسمی `Advertisement.GetLegalOrgChannels` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `channels`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_legal_org_channels()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetLegalOrgChannels")
```

---

### GetMyContactPopularChannels
اجرای متد رسمی `Advertisement.GetMyContactPopularChannels` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `channels`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_my_contact_popular_channels()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetMyContactPopularChannels")
```

---

### GetOnBoardingChannels
اجرای متد رسمی `Advertisement.GetOnBoardingChannels` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `channels, showOnBoarding`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_on_boarding_channels()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetOnBoardingChannels")
```

---

### GetOnboardingPeers
اجرای متد رسمی `Advertisement.GetOnboardingPeers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `peers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_onboarding_peers()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetOnboardingPeers")
```

---

### GetOnboardingPosts
اجرای متد رسمی `Advertisement.GetOnboardingPosts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `posts`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_onboarding_posts(category_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetOnboardingPosts", category_id=12345)
```

---

### GetOnboardingSpotData
اجرای متد رسمی `Advertisement.GetOnboardingSpotData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `onboardingSpot` | Integer | **Required** | Wire field `onboardingSpot` (python arg: `onboarding_spot`). |
| `suggestedPeerType` | Integer | **Required** | Wire field `suggestedPeerType` (python arg: `suggested_peer_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `contactChannels, suggestedChannels`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_onboarding_spot_data(onboarding_spot=12345, suggested_peer_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetOnboardingSpotData", onboarding_spot=12345, suggested_peer_type=12345)
```

---

### GetOwnerIdByPhone
اجرای متد رسمی `Advertisement.GetOwnerIdByPhone` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phoneNumber` | String | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_owner_id_by_phone(phone_number="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetOwnerIdByPhone", phone_number="value")
```

---

### GetPaidAdsByTime
اجرای متد رسمی `Advertisement.GetPaidAdsByTime` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagingData` | Object | **Optional** | Wire field `pagingData` (python arg: `paging_data`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `endTime` | Integer | **Required** | Wire field `endTime` (python arg: `end_time`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_paid_ads_by_time(paging_data={...}, start_time=12345, end_time=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetPaidAdsByTime", paging_data={...}, start_time=12345, end_time=12345)
```

---

### GetPaymentData
اجرای متد رسمی `Advertisement.GetPaymentData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_payment_data(ad_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetPaymentData", ad_id="value")
```

---

### GetPeriodCapacityData
اجرای متد رسمی `Advertisement.GetPeriodCapacityData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `beginDate` | Integer | **Required** | Wire field `beginDate` (python arg: `begin_date`). |
| `endDate` | Integer | **Required** | Wire field `endDate` (python arg: `end_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_period_capacity_data(begin_date=12345, end_date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetPeriodCapacityData", begin_date=12345, end_date=12345)
```

---

### GetUserAds
اجرای متد رسمی `Advertisement.GetUserAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagingData` | Object | **Optional** | Wire field `pagingData` (python arg: `paging_data`). |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ads`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_ads(paging_data={...}, user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetUserAds", paging_data={...}, user_id=12345)
```

---

### GetUserAuthData
اجرای متد رسمی `Advertisement.GetUserAuthData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channelId` | Object | **Optional** | Wire field `channelId` (python arg: `channel_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userId, nationalCode, birthDate, address, postalCode, melliAccountNumber, firstName, lastName, phone, state, reason, channelNick`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_auth_data(channel_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetUserAuthData", channel_id={...})
```

---

### GetUserCampaigns
اجرای متد رسمی `Advertisement.GetUserCampaigns` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagingData` | Object | **Optional** | Wire field `pagingData` (python arg: `paging_data`). |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_campaigns(paging_data={...}, user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetUserCampaigns", paging_data={...}, user_id=12345)
```

---

### GetUserOnboardingScenario
اجرای متد رسمی `Advertisement.GetUserOnboardingScenario` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `scenario`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_onboarding_scenario()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetUserOnboardingScenario")
```

---

### GetUserStatus
اجرای متد رسمی `Advertisement.GetUserStatus` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `status`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_status(user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetUserStatus", user_id=12345)
```

---

### GetUsersAuthDataByState
اجرای متد رسمی `Advertisement.GetUsersAuthDataByState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `state` | Integer | **Required** | Wire field `state` (python arg: `state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `usersData`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_users_auth_data_by_state(state=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetUsersAuthDataByState", state=12345)
```

---

### GetVODContents
اجرای متد رسمی `Advertisement.GetVODContents` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `contents`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_vod_contents()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "GetVODContents")
```

---

### MergeCustomIncomeRecords
اجرای متد رسمی `Advertisement.MergeCustomIncomeRecords` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `customIncomeIds` | Array of String | **Required** | Wire field `customIncomeIds` (python arg: `custom_income_ids`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.merge_custom_income_records(custom_income_ids="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "MergeCustomIncomeRecords", custom_income_ids="value")
```

---

### MergeIncreaseCreditRecords
اجرای متد رسمی `Advertisement.MergeIncreaseCreditRecords` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `increaseCreditIds` | Array of String | **Required** | Wire field `increaseCreditIds` (python arg: `increase_credit_ids`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.merge_increase_credit_records(increase_credit_ids="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "MergeIncreaseCreditRecords", increase_credit_ids="value")
```

---

### ModifyCapacity
اجرای متد رسمی `Advertisement.ModifyCapacity` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `val` | Integer | **Required** | Wire field `val` (python arg: `val`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.modify_capacity(date=12345, val=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "ModifyCapacity", date=12345, val=12345)
```

---

### RegisterForEarnMoney
اجرای متد رسمی `Advertisement.RegisterForEarnMoney` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `info` | Object | **Optional** | Wire field `info` (python arg: `info`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.register_for_earn_money(info={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "RegisterForEarnMoney", info={...})
```

---

### RetryFailedAutoSentInvoice
اجرای متد رسمی `Advertisement.RetryFailedAutoSentInvoice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `failedInvoiceRequestId` | String | **Required** | Wire field `failedInvoiceRequestId` (python arg: `failed_invoice_request_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.retry_failed_auto_sent_invoice(failed_invoice_request_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "RetryFailedAutoSentInvoice", failed_invoice_request_id="value")
```

---

### SendAdminMessage
اجرای متد رسمی `Advertisement.SendAdminMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `receiver` | Integer | **Required** | Wire field `receiver` (python arg: `receiver`). |
| `messageText` | String | **Required** | Wire field `messageText` (python arg: `message_text`). |
| `fileId` | Integer | **Required** | Wire field `fileId` (python arg: `file_id`). |
| `fileName` | String | **Required** | Wire field `fileName` (python arg: `file_name`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_admin_message(receiver=12345, message_text="value", file_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SendAdminMessage", receiver=12345, message_text="value", file_id=12345)
```

---

### SendFactorMessage
اجرای متد رسمی `Advertisement.SendFactorMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channelId` | Integer | **Required** | Wire field `channelId` (python arg: `channel_id`). |
| `messageText` | String | **Required** | Wire field `messageText` (python arg: `message_text`). |
| `fileId` | Integer | **Required** | Wire field `fileId` (python arg: `file_id`). |
| `fileName` | String | **Required** | Wire field `fileName` (python arg: `file_name`). |
| `year` | Integer | **Required** | Wire field `year` (python arg: `year`). |
| `month` | Integer | **Required** | Wire field `month` (python arg: `month`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_factor_message(channel_id=12345, message_text="value", file_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SendFactorMessage", channel_id=12345, message_text="value", file_id=12345)
```

---

### SendInvoiceForPaymentHistoryRecord
اجرای متد رسمی `Advertisement.SendInvoiceForPaymentHistoryRecord` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `recordId` | String | **Required** | Wire field `recordId` (python arg: `record_id`). |
| `depositTrackingId` | Object | **Optional** | Wire field `depositTrackingId` (python arg: `deposit_tracking_id`). |
| `paymentHistoryType` | Integer | **Required** | Wire field `paymentHistoryType` (python arg: `payment_history_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `invoiceRequestId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_invoice_for_payment_history_record(record_id="value", deposit_tracking_id={...}, payment_history_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SendInvoiceForPaymentHistoryRecord", record_id="value", deposit_tracking_id={...}, payment_history_type=12345)
```

---

### SendLegalOrgChannelIncome
اجرای متد رسمی `Advertisement.SendLegalOrgChannelIncome` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channelId` | Integer | **Required** | Wire field `channelId` (python arg: `channel_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `results`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_legal_org_channel_income(channel_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SendLegalOrgChannelIncome", channel_id=12345)
```

---

### SetAdTarget
اجرای متد رسمی `Advertisement.SetAdTarget` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |
| `targeting` | Object | **Optional** | Wire field `targeting` (python arg: `targeting`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_ad_target(ad_id="value", targeting={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SetAdTarget", ad_id="value", targeting={...})
```

---

### SetCapacityMaxViews
اجرای متد رسمی `Advertisement.SetCapacityMaxViews` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `data` | Array of Object | **Required** | Wire field `data` (python arg: `data`). |
| `spot` | Integer | **Required** | Wire field `spot` (python arg: `spot`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_capacity_max_views(data={...}, spot=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SetCapacityMaxViews", data={...}, spot=12345)
```

---

### SetChannelInvoiceInfo
اجرای متد رسمی `Advertisement.SetChannelInvoiceInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `address` | String | **Required** | Wire field `address` (python arg: `address`). |
| `postalCode` | String | **Required** | Wire field `postalCode` (python arg: `postal_code`). |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |
| `tag1` | Integer | **Required** | Wire field `tag1` (python arg: `tag1`). |
| `tag2` | Integer | **Required** | Wire field `tag2` (python arg: `tag2`). |
| `birthDate` | String | **Required** | Wire field `birthDate` (python arg: `birth_date`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_channel_invoice_info(peer_id={...}, national_code="value", address="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SetChannelInvoiceInfo", peer_id={...}, national_code="value", address="value")
```

---

### SetChannelOwnerBankInformation
اجرای متد رسمی `Advertisement.SetChannelOwnerBankInformation` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channelId` | Object | **Optional** | Wire field `channelId` (python arg: `channel_id`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `birthDate` | String | **Required** | Wire field `birthDate` (python arg: `birth_date`). |
| `address` | String | **Required** | Wire field `address` (python arg: `address`). |
| `postalCode` | String | **Required** | Wire field `postalCode` (python arg: `postal_code`). |
| `melliAccountNumber` | String | **Required** | Wire field `melliAccountNumber` (python arg: `melli_account_number`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_channel_owner_bank_information(channel_id={...}, national_code="value", birth_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SetChannelOwnerBankInformation", channel_id={...}, national_code="value", birth_date="value")
```

---

### SetOnBoardingChannels
اجرای متد رسمی `Advertisement.SetOnBoardingChannels` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channels` | Array of Object | **Required** | Wire field `channels` (python arg: `channels`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_on_boarding_channels(channels={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SetOnBoardingChannels", channels={...})
```

---

### SetUserAuthData
اجرای متد رسمی `Advertisement.SetUserAuthData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channelId` | Object | **Optional** | Wire field `channelId` (python arg: `channel_id`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `birthDate` | String | **Required** | Wire field `birthDate` (python arg: `birth_date`). |
| `address` | String | **Required** | Wire field `address` (python arg: `address`). |
| `postalCode` | String | **Required** | Wire field `postalCode` (python arg: `postal_code`). |
| `melliAccountNumber` | String | **Required** | Wire field `melliAccountNumber` (python arg: `melli_account_number`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_user_auth_data(channel_id={...}, national_code="value", birth_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SetUserAuthData", channel_id={...}, national_code="value", birth_date="value")
```

---

### StartAd
اجرای متد رسمی `Advertisement.StartAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `platform` | Integer | **Required** | Wire field `platform` (python arg: `platform`). |
| `autoFinish` | Boolean | **Required** | Wire field `autoFinish` (python arg: `auto_finish`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_ad(ad_id="value", start_time=12345, platform=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "StartAd", ad_id="value", start_time=12345, platform=12345)
```

---

### StartBaleCustomAd
اجرای متد رسمی `Advertisement.StartBaleCustomAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `platform` | Integer | **Required** | Wire field `platform` (python arg: `platform`). |
| `pic` | String | **Required** | Wire field `pic` (python arg: `pic`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `link` | String | **Required** | Wire field `link` (python arg: `link`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `viewCount` | Integer | **Required** | Wire field `viewCount` (python arg: `view_count`). |
| `clickCount` | Integer | **Required** | Wire field `clickCount` (python arg: `click_count`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ad`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_bale_custom_ad(id="value", platform=12345, pic="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "StartBaleCustomAd", id="value", platform=12345, pic="value")
```

---

### StartChannelAdFromOrder
اجرای متد رسمی `Advertisement.StartChannelAdFromOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `link` | String | **Required** | Wire field `link` (python arg: `link`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `viewCount` | Integer | **Required** | Wire field `viewCount` (python arg: `view_count`). |
| `clickCount` | Integer | **Required** | Wire field `clickCount` (python arg: `click_count`). |
| `platform` | Integer | **Required** | Wire field `platform` (python arg: `platform`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_channel_ad_from_order(id="value", title="value", description="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "StartChannelAdFromOrder", id="value", title="value", description="value")
```

---

### StartFromOrder
اجرای متد رسمی `Advertisement.StartFromOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `platform` | Integer | **Required** | Wire field `platform` (python arg: `platform`). |
| `pic` | String | **Required** | Wire field `pic` (python arg: `pic`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `link` | String | **Required** | Wire field `link` (python arg: `link`). |
| `startTime` | Integer | **Required** | Wire field `startTime` (python arg: `start_time`). |
| `viewCount` | Integer | **Required** | Wire field `viewCount` (python arg: `view_count`). |
| `clickCount` | Integer | **Required** | Wire field `clickCount` (python arg: `click_count`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_from_order(id="value", platform=12345, pic="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "StartFromOrder", id="value", platform=12345, pic="value")
```

---

### StopAllBaleCustomAds
اجرای متد رسمی `Advertisement.StopAllBaleCustomAds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.stop_all_bale_custom_ads()

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "StopAllBaleCustomAds")
```

---

### SubmitChannelAdOrder
اجرای متد رسمی `Advertisement.SubmitChannelAdOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `order` | Object | **Optional** | Wire field `order` (python arg: `order`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.submit_channel_ad_order(order={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SubmitChannelAdOrder", order={...})
```

---

### SubmitDialogAdOrder
اجرای متد رسمی `Advertisement.SubmitDialogAdOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `dialogAdOrder` | Object | **Optional** | Wire field `dialogAdOrder` (python arg: `dialog_ad_order`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.submit_dialog_ad_order(dialog_ad_order={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SubmitDialogAdOrder", dialog_ad_order={...})
```

---

### SubmitPhotoForBaleCustomAd
اجرای متد رسمی `Advertisement.SubmitPhotoForBaleCustomAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `adId` | String | **Required** | Wire field `adId` (python arg: `ad_id`). |
| `pic` | String | **Required** | Wire field `pic` (python arg: `pic`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ad`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.submit_photo_for_bale_custom_ad(ad_id="value", pic="value")

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "SubmitPhotoForBaleCustomAd", ad_id="value", pic="value")
```

---

### UpdateBusinessAd
اجرای متد رسمی `Advertisement.UpdateBusinessAd` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `updatedAd` | Object | **Optional** | Wire field `updatedAd` (python arg: `updated_ad`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_business_ad(updated_ad={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "UpdateBusinessAd", updated_ad={...})
```

---

### UpdateCRMIssue
اجرای متد رسمی `Advertisement.UpdateCRMIssue` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `addIssue` | Object | **Optional** | Wire field `addIssue` (python arg: `add_issue`). |
| `addComment` | Object | **Optional** | Wire field `addComment` (python arg: `add_comment`). |
| `resolveIssue` | Object | **Optional** | Wire field `resolveIssue` (python arg: `resolve_issue`). |
| `ignoreUser` | Object | **Optional** | Wire field `ignoreUser` (python arg: `ignore_user`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_crm_issue(add_issue={...}, add_comment={...}, resolve_issue={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "UpdateCRMIssue", add_issue={...}, add_comment={...}, resolve_issue={...})
```

---

### UpdateClick
اجرای متد رسمی `Advertisement.UpdateClick` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_click(id="value", count=12345, peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "UpdateClick", id="value", count=12345, peer={...})
```

---

### UpdateGroupStatus
اجرای متد رسمی `Advertisement.UpdateGroupStatus` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupId` | Object | **Optional** | Wire field `groupId` (python arg: `group_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_group_status(group_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "UpdateGroupStatus", group_id={...})
```

---

### UpdateView
اجرای متد رسمی `Advertisement.UpdateView` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |
| `peerId` | Object | **Optional** | Wire field `peerId` (python arg: `peer_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `isSuccessful`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_view(id="value", count=12345, peer_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("advertisement", "UpdateView", id="value", count=12345, peer_id={...})
```

---

## AnonymousContact (تنظیمات پیام و ارتباط ناشناس)
> شناسه کامل سرویس در شبکه بله: `bale.anonymous_contact.v1.AnonymousContact` — تعداد متدها: **1**

### GetUserAnonymousContactPage
اجرای متد رسمی `AnonymousContact.GetUserAnonymousContactPage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_anonymous_contact_page()

# ۲. فراخوانی با RPC
result = await app.rpc("anonymouscontact", "GetUserAnonymousContactPage")
```

---

## Appzar (پلتفرم مینی‌اپ‌ها، لانچر وب‌اپ و دکمه‌های بات)
> شناسه کامل سرویس در شبکه بله: `bale.appzar.v1.Appzar` — تعداد متدها: **3**

### GetMenuButton
اجرای متد رسمی `Appzar.GetMenuButton` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `menuButton`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_menu_button(bot_user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("appzar", "GetMenuButton", bot_user_id=12345)
```

---

### GetMiniAppUrl
اجرای متد رسمی `Appzar.GetMiniAppUrl` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |
| `screenMode` | Integer | **Required** | Wire field `screenMode` (python arg: `screen_mode`). |
| `themeParams` | Object | **Optional** | Wire field `themeParams` (python arg: `theme_params`). |
| `main` | Object | **Optional** | Wire field `main` (python arg: `main`). |
| `menuButton` | Object | **Optional** | Wire field `menuButton` (python arg: `menu_button`). |
| `keyboardButton` | Object | **Optional** | Wire field `keyboardButton` (python arg: `keyboard_button`). |
| `directLink` | Object | **Optional** | Wire field `directLink` (python arg: `direct_link`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `url, screenMode, queryId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_mini_app_url(bot_user_id=12345, screen_mode=12345, theme_params={...})

# ۲. فراخوانی با RPC
result = await app.rpc("appzar", "GetMiniAppUrl", bot_user_id=12345, screen_mode=12345, theme_params={...})
```

---

### InvokeCustomMethod
اجرای متد رسمی `Appzar.InvokeCustomMethod` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |
| `method` | String | **Required** | Wire field `method` (python arg: `method`). |
| `params` | String | **Required** | Wire field `params` (python arg: `params`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `data`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.invoke_custom_method(bot_user_id=12345, method="value", params="value")

# ۲. فراخوانی با RPC
result = await app.rpc("appzar", "InvokeCustomMethod", bot_user_id=12345, method="value", params="value")
```

---

## Arbaeen (خدمات ارزی و ایستگاه‌های تحویل ارز اربعین)
> شناسه کامل سرویس در شبکه بله: `bale.arbaeen.v1.Arbaeen` — تعداد متدها: **19**

### CashPaymentCallback
اجرای متد رسمی `Arbaeen.CashPaymentCallback` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `paymentCode` | String | **Required** | Wire field `paymentCode` (python arg: `payment_code`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |
| `orderId` | Integer | **Required** | Wire field `orderId` (python arg: `order_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `firstName, lastName`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.cash_payment_callback(payment_code="value", national_code="value", user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "CashPaymentCallback", payment_code="value", national_code="value", user_id=12345)
```

---

### GetAdminStationList
اجرای متد رسمی `Arbaeen.GetAdminStationList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `stations`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_admin_station_list()

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetAdminStationList")
```

---

### GetArbaeenCurrenciesList
اجرای متد رسمی `Arbaeen.GetArbaeenCurrenciesList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currencies, icmsWage`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_arbaeen_currencies_list()

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetArbaeenCurrenciesList")
```

---

### GetArbaeenCurrencyPrice
اجرای متد رسمی `Arbaeen.GetArbaeenCurrencyPrice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `currencyType` | Integer | **Required** | Wire field `currencyType` (python arg: `currency_type`). |
| `currencyAmount` | Integer | **Required** | Wire field `currencyAmount` (python arg: `currency_amount`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |
| `countryCode` | Integer | **Required** | Wire field `countryCode` (python arg: `country_code`). |
| `exitDate` | String | **Required** | Wire field `exitDate` (python arg: `exit_date`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `deliveryStationType` | Integer | **Required** | Wire field `deliveryStationType` (python arg: `delivery_station_type`). |
| `stationId` | String | **Required** | Wire field `stationId` (python arg: `station_id`). |
| `bankType` | Integer | **Required** | Wire field `bankType` (python arg: `bank_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currencyRate, orderId, newCurrencyRate`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_arbaeen_currency_price(currency_type=12345, currency_amount=12345, reason=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetArbaeenCurrencyPrice", currency_type=12345, currency_amount=12345, reason=12345)
```

---

### GetArbaeenPaymentToken
اجرای متد رسمی `Arbaeen.GetArbaeenPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `orderId` | Integer | **Required** | Wire field `orderId` (python arg: `order_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, paymentGatewayPrefix, terminalId, paymentUrl`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_arbaeen_payment_token(order_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetArbaeenPaymentToken", order_id=12345)
```

---

### GetListOfArbaeenDeliveryStations
اجرای متد رسمی `Arbaeen.GetListOfArbaeenDeliveryStations` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `deliveryStationType` | Integer | **Required** | Wire field `deliveryStationType` (python arg: `delivery_station_type`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |
| `ExitDate` | String | **Required** | Wire field `ExitDate` (python arg: `exit_date`). |
| `bankType` | Integer | **Required** | Wire field `bankType` (python arg: `bank_type`). |
| `shouldReturnCapacity` | Object | **Optional** | Wire field `shouldReturnCapacity` (python arg: `should_return_capacity`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `stations`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_list_of_arbaeen_delivery_stations(delivery_station_type=12345, reason=12345, exit_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetListOfArbaeenDeliveryStations", delivery_station_type=12345, reason=12345, exit_date="value")
```

---

### GetListOfBoxOffice
اجرای متد رسمی `Arbaeen.GetListOfBoxOffice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `stationId` | String | **Required** | Wire field `stationId` (python arg: `station_id`). |
| `exitDate` | String | **Required** | Wire field `exitDate` (python arg: `exit_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `boxOffice`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_list_of_box_office(station_id="value", exit_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetListOfBoxOffice", station_id="value", exit_date="value")
```

---

### GetListOfBranches
اجرای متد رسمی `Arbaeen.GetListOfBranches` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `stateId` | String | **Required** | Wire field `stateId` (python arg: `state_id`). |
| `exitDate` | String | **Required** | Wire field `exitDate` (python arg: `exit_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `branches`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_list_of_branches(state_id="value", exit_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetListOfBranches", state_id="value", exit_date="value")
```

---

### GetListOfStates
اجرای متد رسمی `Arbaeen.GetListOfStates` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `states`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_list_of_states()

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetListOfStates")
```

---

### GetRate
اجرای متد رسمی `Arbaeen.GetRate` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `rate`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_rate()

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetRate")
```

---

### GetSuggestedGroups
اجرای متد رسمی `Arbaeen.GetSuggestedGroups` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `suggestedGroups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_suggested_groups()

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetSuggestedGroups")
```

---

### GetValidArbaeenBanks
اجرای متد رسمی `Arbaeen.GetValidArbaeenBanks` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `accountNationalCode` | Object | **Optional** | Wire field `accountNationalCode` (python arg: `account_national_code`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `banks`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_valid_arbaeen_banks(national_code="value", account_national_code={...})

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "GetValidArbaeenBanks", national_code="value", account_national_code={...})
```

---

### LoadArbaeenHistory
اجرای متد رسمی `Arbaeen.LoadArbaeenHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orders, approvalText`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_arbaeen_history()

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "LoadArbaeenHistory")
```

---

### SendOTP
اجرای متد رسمی `Arbaeen.SendOTP` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phoneNumber` | String | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_otp(phone_number="value")

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "SendOTP", phone_number="value")
```

---

### StartBot
اجرای متد رسمی `Arbaeen.StartBot` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_bot(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "StartBot", peer={...})
```

---

### UserHasAccess
اجرای متد رسمی `Arbaeen.UserHasAccess` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `access`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.user_has_access()

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "UserHasAccess")
```

---

### VerifyOTP
اجرای متد رسمی `Arbaeen.VerifyOTP` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phoneNumber` | String | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `verified`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_otp(phone_number="value", code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "VerifyOTP", phone_number="value", code="value")
```

---

### VerifyUserArbaeenAuthority
اجرای متد رسمی `Arbaeen.VerifyUserArbaeenAuthority` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `firstName` | String | **Required** | Wire field `firstName` (python arg: `first_name`). |
| `lastName` | String | **Required** | Wire field `lastName` (python arg: `last_name`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `passportCode` | String | **Required** | Wire field `passportCode` (python arg: `passport_code`). |
| `postalCode` | String | **Required** | Wire field `postalCode` (python arg: `postal_code`). |
| `birthDate` | String | **Required** | Wire field `birthDate` (python arg: `birth_date`). |
| `fatherName` | String | **Required** | Wire field `fatherName` (python arg: `father_name`). |
| `shId` | String | **Required** | Wire field `shId` (python arg: `sh_id`). |
| `bankType` | Integer | **Required** | Wire field `bankType` (python arg: `bank_type`). |
| `phoneNumber` | String | **Optional** | Wire field `phoneNumber` (python arg: `phone_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `approval`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_user_arbaeen_authority(first_name="value", last_name="value", national_code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "VerifyUserArbaeenAuthority", first_name="value", last_name="value", national_code="value")
```

---

### VerifyUserArbaeenExtraInfo
اجرای متد رسمی `Arbaeen.VerifyUserArbaeenExtraInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nakhodaInfo` | Object | **Optional** | Wire field `nakhodaInfo` (python arg: `nakhoda_info`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_user_arbaeen_extra_info(nakhoda_info={...})

# ۲. فراخوانی با RPC
result = await app.rpc("arbaeen", "VerifyUserArbaeenExtraInfo", nakhoda_info={...})
```

---

## Auth (احراز هویت، نشست‌ها، تایید دو مرحله‌ای و تغییر مشخصات)
> شناسه کامل سرویس در شبکه بله: `bale.auth.v1.Auth` — تعداد متدها: **27**

### ChangeLanguage
اجرای متد رسمی `Auth.ChangeLanguage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `language` | Integer | **Required** | Wire field `language` (python arg: `language`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_language(language=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "ChangeLanguage", language=12345)
```

---

### ChangePhone
اجرای متد رسمی `Auth.ChangePhone` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phoneNumber` | Integer | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_phone(phone_number=12345, code="value", transaction_hash="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "ChangePhone", phone_number=12345, code="value", transaction_hash="value")
```

---

### DeleteAccount
اجرای متد رسمی `Auth.DeleteAccount` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_account(code="value", transaction_hash="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "DeleteAccount", code="value", transaction_hash="value")
```

---

### DisableTwoFactorAuthentication
اجرای متد رسمی `Auth.DisableTwoFactorAuthentication` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.disable_two_factor_authentication()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "DisableTwoFactorAuthentication")
```

---

### EnableTwoFactorAuthentication
اجرای متد رسمی `Auth.EnableTwoFactorAuthentication` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `email` | String | **Required** | Wire field `email` (python arg: `email`). |
| `password` | String | **Required** | Wire field `password` (python arg: `password`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.enable_two_factor_authentication(email="value", password="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "EnableTwoFactorAuthentication", email="value", password="value")
```

---

### GetAuthSessions
اجرای متد رسمی `Auth.GetAuthSessions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userAuths`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_auth_sessions()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "GetAuthSessions")
```

---

### GetBajeBamTicket
اجرای متد رسمی `Auth.GetBajeBamTicket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `expDateTime` | Integer | **Required** | Wire field `expDateTime` (python arg: `exp_date_time`). |
| `mobileNo` | String | **Required** | Wire field `mobileNo` (python arg: `mobile_no`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ticket`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_baje_bam_ticket(exp_date_time=12345, mobile_no="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "GetBajeBamTicket", exp_date_time=12345, mobile_no="value")
```

---

### GetBaleTicket
اجرای متد رسمی `Auth.GetBaleTicket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `expDateTime` | Integer | **Required** | Wire field `expDateTime` (python arg: `exp_date_time`). |
| `mobileNo` | String | **Required** | Wire field `mobileNo` (python arg: `mobile_no`). |
| `clientId` | String | **Required** | Wire field `clientId` (python arg: `client_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `redirectUrl`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bale_ticket(exp_date_time=12345, mobile_no="value", client_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "GetBaleTicket", exp_date_time=12345, mobile_no="value", client_id="value")
```

---

### GetJWTToken
اجرای متد رسمی `Auth.GetJWTToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `jwt`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_jwt_token()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "GetJWTToken")
```

---

### GetTicket
اجرای متد رسمی `Auth.GetTicket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `jsonRequest` | String | **Required** | Wire field `jsonRequest` (python arg: `json_request`). |
| `jsonSign` | String | **Required** | Wire field `jsonSign` (python arg: `json_sign`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `redirectUrl`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ticket(json_request="value", json_sign="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "GetTicket", json_request="value", json_sign="value")
```

---

### GetUserIdToken
اجرای متد رسمی `Auth.GetUserIdToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ticket` | String | **Required** | Wire field `ticket` (python arg: `ticket`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, userId, source, service`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_id_token(ticket="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "GetUserIdToken", ticket="value")
```

---

### IsTwoFactorAuthenticationEnabled
اجرای متد رسمی `Auth.IsTwoFactorAuthenticationEnabled` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `isEnabled`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.is_two_factor_authentication_enabled()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "IsTwoFactorAuthenticationEnabled")
```

---

### LogOut
اجرای متد رسمی `Auth.LogOut` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `futureAuthToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.log_out()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "LogOut")
```

---

### RecoverPassword
اجرای متد رسمی `Auth.RecoverPassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `emailPattern`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.recover_password(transaction_hash="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "RecoverPassword", transaction_hash="value")
```

---

### SendChangePhoneVerificationCode
اجرای متد رسمی `Auth.SendChangePhoneVerificationCode` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactionHash, activationType`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_change_phone_verification_code()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "SendChangePhoneVerificationCode")
```

---

### SendDeleteAccountVerificationCode
اجرای متد رسمی `Auth.SendDeleteAccountVerificationCode` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactionHash, activationType`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_delete_account_verification_code()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "SendDeleteAccountVerificationCode")
```

---

### SetNewPassword
اجرای متد رسمی `Auth.SetNewPassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `newPassword` | String | **Required** | Wire field `newPassword` (python arg: `new_password`). |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_new_password(new_password="value", transaction_hash="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "SetNewPassword", new_password="value", transaction_hash="value")
```

---

### SignOut
اجرای متد رسمی `Auth.SignOut` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.sign_out()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "SignOut")
```

---

### SignUp
اجرای متد رسمی `Auth.SignUp` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |
| `sex` | Integer | **Required** | Wire field `sex` (python arg: `sex`). |
| `password` | Object | **Optional** | Wire field `password` (python arg: `password`). |
| `language` | Integer | **Required** | Wire field `language` (python arg: `language`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `user, config, jwt`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.sign_up(transaction_hash="value", name="value", sex=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "SignUp", transaction_hash="value", name="value", sex=12345)
```

---

### StartPhoneAuth
اجرای متد رسمی `Auth.StartPhoneAuth` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phoneNumber` | Integer | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `appId` | Integer | **Required** | Wire field `appId` (python arg: `app_id`). |
| `apiKey` | String | **Required** | Wire field `apiKey` (python arg: `api_key`). |
| `deviceHash` | Bytes | **Required** | Wire field `deviceHash` (python arg: `device_hash`). |
| `deviceTitle` | String | **Required** | Wire field `deviceTitle` (python arg: `device_title`). |
| `timeZone` | Object | **Optional** | Wire field `timeZone` (python arg: `time_zone`). |
| `preferredLanguages` | Array of String | **Required** | Wire field `preferredLanguages` (python arg: `preferred_languages`). |
| `imeiList` | Object | **Optional** | Wire field `imeiList` (python arg: `imei_list`). |
| `sendCodeType` | Integer | **Required** | Wire field `sendCodeType` (python arg: `send_code_type`). |
| `options` | Array of Integer | **Required** | Wire field `options` (python arg: `options`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactionHash, isRegistered, activationType, isImeiOk, sentCodeType, codeExpirationDate, nextSendCodeType, nextSendCodeWaitTime, codeTimeout, exInfoAddress, availableSendCodeTypes`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_phone_auth(phone_number=12345, app_id=12345, api_key="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "StartPhoneAuth", phone_number=12345, app_id=12345, api_key="value")
```

---

### TerminateAllSessions
اجرای متد رسمی `Auth.TerminateAllSessions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.terminate_all_sessions()

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "TerminateAllSessions")
```

---

### TerminateSession
اجرای متد رسمی `Auth.TerminateSession` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.terminate_session(id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "TerminateSession", id=12345)
```

---

### ValidateCode
اجرای متد رسمی `Auth.ValidateCode` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `isJwt` | Object | **Optional** | Wire field `isJwt` (python arg: `is_jwt`). |
| `futureAuthTokens` | Array of String | **Required** | Wire field `futureAuthTokens` (python arg: `future_auth_tokens`). |
| `language` | Integer | **Required** | Wire field `language` (python arg: `language`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `user, config, jwt`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.validate_code(transaction_hash="value", code="value", is_jwt={...})

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "ValidateCode", transaction_hash="value", code="value", is_jwt={...})
```

---

### ValidatePassword
اجرای متد رسمی `Auth.ValidatePassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |
| `password` | String | **Required** | Wire field `password` (python arg: `password`). |
| `isJwt` | Object | **Optional** | Wire field `isJwt` (python arg: `is_jwt`). |
| `language` | Integer | **Required** | Wire field `language` (python arg: `language`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `user, config, jwt`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.validate_password(transaction_hash="value", password="value", is_jwt={...})

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "ValidatePassword", transaction_hash="value", password="value", is_jwt={...})
```

---

### VerifyEmail
اجرای متد رسمی `Auth.VerifyEmail` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `email` | String | **Required** | Wire field `email` (python arg: `email`). |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_email(email="value", code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "VerifyEmail", email="value", code="value")
```

---

### VerifyPassword
اجرای متد رسمی `Auth.VerifyPassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `password` | String | **Required** | Wire field `password` (python arg: `password`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_password(password="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "VerifyPassword", password="value")
```

---

### VerifyPasswordRecovery
اجرای متد رسمی `Auth.VerifyPasswordRecovery` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |
| `transactionHash` | String | **Required** | Wire field `transactionHash` (python arg: `transaction_hash`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_password_recovery(code="value", transaction_hash="value")

# ۲. فراخوانی با RPC
result = await app.rpc("auth", "VerifyPasswordRecovery", code="value", transaction_hash="value")
```

---

## GoldGiftPacket (پاکت‌های هدیه طلایی بله‌بانک)
> شناسه کامل سرویس در شبکه بله: `bale.balebank.v1.GoldGiftPacket` — تعداد متدها: **3**

### GetWinnerIDs
اجرای متد رسمی `GoldGiftPacket.GetWinnerIDs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `giftPacketId` | Integer | **Required** | Wire field `giftPacketId` (python arg: `gift_packet_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `winners`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_winner_i_ds(gift_packet_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("goldgiftpacket", "GetWinnerIDs", gift_packet_id=12345)
```

---

### OpenGoldGiftPacket
اجرای متد رسمی `GoldGiftPacket.OpenGoldGiftPacket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `giftPacketId` | Integer | **Required** | Wire field `giftPacketId` (python arg: `gift_packet_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `openedCount, selfWinAmount, rank, giftReceivers, status, verificationDeadline`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.open_gold_gift_packet(gift_packet_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("goldgiftpacket", "OpenGoldGiftPacket", gift_packet_id=12345)
```

---

### SendGoldGiftPacket
اجرای متد رسمی `GoldGiftPacket.SendGoldGiftPacket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `givingType` | Integer | **Required** | Wire field `givingType` (python arg: `giving_type`). |
| `randomId` | Integer | **Required** | Wire field `randomId` (python arg: `random_id`). |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `giftPacketId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_gold_gift_packet(amount=12345, count=12345, description="value")

# ۲. فراخوانی با RPC
result = await app.rpc("goldgiftpacket", "SendGoldGiftPacket", amount=12345, count=12345, description="value")
```

---

## GoldWallet (کیف پول طلا و دریافت موجودی)
> شناسه کامل سرویس در شبکه بله: `bale.balebank.v1.GoldWallet` — تعداد متدها: **1**

### GetBalance
اجرای متد رسمی `GoldWallet.GetBalance` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_balance()

# ۲. فراخوانی با RPC
result = await app.rpc("goldwallet", "GetBalance")
```

---

## Bank (عملیات بانکی، موجودی شتاب، انتقال کارت‌به‌کارت و درگاه)
> شناسه کامل سرویس در شبکه بله: `bale.bank.v1.Bank` — تعداد متدها: **17**

### BuyFastCharge
اجرای متد رسمی `Bank.BuyFastCharge` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `phoneNumber` | Object | **Optional** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `operator` | Integer | **Required** | Wire field `operator` (python arg: `operator`). |
| `chargeType` | Integer | **Required** | Wire field `chargeType` (python arg: `charge_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactionDate, refrenceNumber, pin, serial`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.buy_fast_charge(amount=12345, phone_number={...}, operator=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "BuyFastCharge", amount=12345, phone_number={...}, operator=12345)
```

---

### GetCardRemain
اجرای متد رسمی `Bank.GetCardRemain` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardNumber` | String | **Required** | Wire field `cardNumber` (python arg: `card_number`). |
| `cvv2` | String | **Required** | Wire field `cvv2` (python arg: `cvv2`). |
| `expireDate` | String | **Required** | Wire field `expireDate` (python arg: `expire_date`). |
| `pin2` | String | **Required** | Wire field `pin2` (python arg: `pin2`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currentBalanceAmount, availableBalanceAmount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_card_remain(card_number="value", cvv2="value", expire_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetCardRemain", card_number="value", cvv2="value", expire_date="value")
```

---

### GetCardTransferToken
اجرای متد رسمی `Bank.GetCardTransferToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerUserId` | Object | **Optional** | Wire field `peerUserId` (python arg: `peer_user_id`). |
| `msgRid` | Object | **Optional** | Wire field `msgRid` (python arg: `msg_rid`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `requestEndPoint, token, destCardNo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_card_transfer_token(peer_user_id={...}, msg_rid={...}, description={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetCardTransferToken", peer_user_id={...}, msg_rid={...}, description={...})
```

---

### GetOTPToken
اجرای متد رسمی `Bank.GetOTPToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardNumberStartingSix` | String | **Required** | Wire field `cardNumberStartingSix` (python arg: `card_number_starting_six`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `requestEndPoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_otp_token(card_number_starting_six="value")

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetOTPToken", card_number_starting_six="value")
```

---

### GetOTPTokenV2
اجرای متد رسمی `Bank.GetOTPTokenV2` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `messagePeer` | Object | **Optional** | Wire field `messagePeer` (python arg: `message_peer`). |
| `msgRid` | Integer | **Required** | Wire field `msgRid` (python arg: `msg_rid`). |
| `msgDate` | Integer | **Required** | Wire field `msgDate` (python arg: `msg_date`). |
| `peerUserId` | Object | **Optional** | Wire field `peerUserId` (python arg: `peer_user_id`). |
| `cardNumberStartingSix` | String | **Required** | Wire field `cardNumberStartingSix` (python arg: `card_number_starting_six`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `requestEndPoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_otp_token_v2(message_peer={...}, msg_rid=12345, msg_date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetOTPTokenV2", message_peer={...}, msg_rid=12345, msg_date=12345)
```

---

### GetOrganizationPaymentToken
اجرای متد رسمی `Bank.GetOrganizationPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `organizationId` | String | **Required** | Wire field `organizationId` (python arg: `organization_id`). |
| `invoiceId` | String | **Required** | Wire field `invoiceId` (python arg: `invoice_id`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, billHolderName, amount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_organization_payment_token(organization_id="value", invoice_id="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetOrganizationPaymentToken", organization_id="value", invoice_id="value", amount=12345)
```

---

### GetPSProxyPaymentToken
اجرای متد رسمی `Bank.GetPSProxyPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `paymentAmount` | Integer | **Required** | Wire field `paymentAmount` (python arg: `payment_amount`). |
| `msg` | Object | **Optional** | Wire field `msg` (python arg: `msg`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `endpoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ps_proxy_payment_token(payment_amount=12345, msg={...}, description={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetPSProxyPaymentToken", payment_amount=12345, msg={...}, description={...})
```

---

### GetPSProxyToken
اجرای متد رسمی `Bank.GetPSProxyToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `endpoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ps_proxy_token()

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetPSProxyToken")
```

---

### GetPayMoneyRequestToken
اجرای متد رسمی `Bank.GetPayMoneyRequestToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `messagePeer` | Object | **Optional** | Wire field `messagePeer` (python arg: `message_peer`). |
| `msgRid` | Integer | **Required** | Wire field `msgRid` (python arg: `msg_rid`). |
| `msgDate` | Integer | **Required** | Wire field `msgDate` (python arg: `msg_date`). |
| `recipient` | Integer | **Required** | Wire field `recipient` (python arg: `recipient`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `requestEndPoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_pay_money_request_token(message_peer={...}, msg_rid=12345, msg_date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetPayMoneyRequestToken", message_peer={...}, msg_rid=12345, msg_date=12345)
```

---

### GetPaymentToken
اجرای متد رسمی `Bank.GetPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `msg` | Object | **Optional** | Wire field `msg` (python arg: `msg`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |
| `amount` | Object | **Optional** | Wire field `amount` (python arg: `amount`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, endpoint, terminalId, cardAcqId, orderId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_payment_token(msg={...}, description={...}, amount={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetPaymentToken", msg={...}, description={...}, amount={...})
```

---

### GetPayvandCard
اجرای متد رسمی `Bank.GetPayvandCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `index` | String | **Required** | Wire field `index` (python arg: `index`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `card`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_payvand_card(index="value")

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetPayvandCard", index="value")
```

---

### GetPayvandCardList
اجرای متد رسمی `Bank.GetPayvandCardList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `payvandCards`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_payvand_card_list()

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetPayvandCardList")
```

---

### GetRecentCharges
اجرای متد رسمی `Bank.GetRecentCharges` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `recentCharges`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_recent_charges()

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetRecentCharges")
```

---

### GetRemainToken
اجرای متد رسمی `Bank.GetRemainToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardNumberStartingSix` | String | **Required** | Wire field `cardNumberStartingSix` (python arg: `card_number_starting_six`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `requestEndPoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_remain_token(card_number_starting_six="value")

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetRemainToken", card_number_starting_six="value")
```

---

### GetSadadPSPPaymentToken
اجرای متد رسمی `Bank.GetSadadPSPPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `msg` | Object | **Optional** | Wire field `msg` (python arg: `msg`). |
| `paymentAmount` | Integer | **Required** | Wire field `paymentAmount` (python arg: `payment_amount`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `endpoint, token, terminalId, merchantCode`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_sadad_psp_payment_token(msg={...}, payment_amount=12345, description={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetSadadPSPPaymentToken", msg={...}, payment_amount=12345, description={...})
```

---

### GetTokenInvoice
اجرای متد رسمی `Bank.GetTokenInvoice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `service` | Integer | **Required** | Wire field `service` (python arg: `service`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `endpoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_token_invoice(service=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GetTokenInvoice", service=12345)
```

---

### GrantBankiAccess
اجرای متد رسمی `Bank.GrantBankiAccess` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `bot` | Object | **Optional** | Wire field `bot` (python arg: `bot`). |
| `serviceKey` | String | **Required** | Wire field `serviceKey` (python arg: `service_key`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.grant_banki_access(bot={...}, service_key="value")

# ۲. فراخوانی با RPC
result = await app.rpc("bank", "GrantBankiAccess", bot={...}, service_key="value")
```

---

## Bill (استعلام، ذخیره و پرداخت انواع قبوض خدماتی)
> شناسه کامل سرویس در شبکه بله: `bale.bill.v1.Bill` — تعداد متدها: **8**

### CreateSavedBill
اجرای متد رسمی `Bill.CreateSavedBill` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |
| `billType` | Integer | **Required** | Wire field `billType` (python arg: `bill_type`). |
| `billParameter` | Object | **Optional** | Wire field `billParameter` (python arg: `bill_parameter`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `id`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_saved_bill(name="value", bill_type=12345, bill_parameter={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "CreateSavedBill", name="value", bill_type=12345, bill_parameter={...})
```

---

### DeleteSavedBills
اجرای متد رسمی `Bill.DeleteSavedBills` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ids` | Array of Integer | **Required** | Wire field `ids` (python arg: `ids`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_saved_bills(ids=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "DeleteSavedBills", ids=12345)
```

---

### GetBillHistory
اجرای متد رسمی `Bill.GetBillHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |
| `page` | Integer | **Required** | Wire field `page` (python arg: `page`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bills`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bill_history(count=12345, page=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "GetBillHistory", count=12345, page=12345)
```

---

### GetBillMenu
اجرای متد رسمی `Bill.GetBillMenu` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `items, otherBillsEnabled, usedDefaultMenu`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bill_menu()

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "GetBillMenu")
```

---

### GetSavedBills
اجرای متد رسمی `Bill.GetSavedBills` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |
| `page` | Integer | **Required** | Wire field `page` (python arg: `page`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bills`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_saved_bills(count=12345, page=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "GetSavedBills", count=12345, page=12345)
```

---

### InquiryBill
اجرای متد رسمی `Bill.InquiryBill` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `billType` | Integer | **Required** | Wire field `billType` (python arg: `bill_type`). |
| `billParameters` | Object | **Optional** | Wire field `billParameters` (python arg: `bill_parameters`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bills, customerName`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.inquiry_bill(bill_type=12345, bill_parameters={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "InquiryBill", bill_type=12345, bill_parameters={...})
```

---

### PayBill
اجرای متد رسمی `Bill.PayBill` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `bill` | Object | **Optional** | Wire field `bill` (python arg: `bill`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.pay_bill(bill={...})

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "PayBill", bill={...})
```

---

### RenameSavedBill
اجرای متد رسمی `Bill.RenameSavedBill` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.rename_saved_bill(id=12345, name="value")

# ۲. فراخوانی با RPC
result = await app.rpc("bill", "RenameSavedBill", id=12345, name="value")
```

---

## CharnetService (خرید شارژ سیم‌کارت و بسته‌های اینترنت همراه)
> شناسه کامل سرویس در شبکه بله: `bale.charnet.v1.CharnetService` — تعداد متدها: **11**

### BuyCharge
اجرای متد رسمی `CharnetService.BuyCharge` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `walletToken` | String | **Required** | Wire field `walletToken` (python arg: `wallet_token`). |
| `phoneNumber` | String | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `operatorType` | Integer | **Required** | Wire field `operatorType` (python arg: `operator_type`). |
| `remaining` | Object | **Optional** | Wire field `remaining` (python arg: `remaining`). |
| `chargeType` | Integer | **Required** | Wire field `chargeType` (python arg: `charge_type`). |
| `targetUserId` | Object | **Optional** | Wire field `targetUserId` (python arg: `target_user_id`). |
| `voucherId` | Object | **Optional** | Wire field `voucherId` (python arg: `voucher_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken, receipt`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.buy_charge(wallet_token="value", phone_number="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "BuyCharge", wallet_token="value", phone_number="value", amount=12345)
```

---

### BuyInternetBundle
اجرای متد رسمی `CharnetService.BuyInternetBundle` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `walletToken` | String | **Required** | Wire field `walletToken` (python arg: `wallet_token`). |
| `phoneNumber` | String | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `bundleId` | Integer | **Required** | Wire field `bundleId` (python arg: `bundle_id`). |
| `operatorType` | Integer | **Required** | Wire field `operatorType` (python arg: `operator_type`). |
| `remaining` | Object | **Optional** | Wire field `remaining` (python arg: `remaining`). |
| `targetUserId` | Object | **Optional** | Wire field `targetUserId` (python arg: `target_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken, receipt`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.buy_internet_bundle(wallet_token="value", phone_number="value", bundle_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "BuyInternetBundle", wallet_token="value", phone_number="value", bundle_id=12345)
```

---

### DeleteRecentChargeOrder
اجرای متد رسمی `CharnetService.DeleteRecentChargeOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `accessHash` | String | **Required** | Wire field `accessHash` (python arg: `access_hash`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_recent_charge_order(access_hash="value")

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "DeleteRecentChargeOrder", access_hash="value")
```

---

### DeleteRecentInternetBundleOrder
اجرای متد رسمی `CharnetService.DeleteRecentInternetBundleOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `orderId` | Integer | **Required** | Wire field `orderId` (python arg: `order_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_recent_internet_bundle_order(order_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "DeleteRecentInternetBundleOrder", order_id=12345)
```

---

### GetAvailableCharges
اجرای متد رسمی `CharnetService.GetAvailableCharges` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `operator` | Integer | **Required** | Wire field `operator` (python arg: `operator`). |
| `chargeType` | Integer | **Required** | Wire field `chargeType` (python arg: `charge_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `amounts, canBeOptional`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_available_charges(operator=12345, charge_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "GetAvailableCharges", operator=12345, charge_type=12345)
```

---

### GetInternetBundleList
اجرای متد رسمی `CharnetService.GetInternetBundleList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `operatorType` | Integer | **Required** | Wire field `operatorType` (python arg: `operator_type`). |
| `simCardType` | Integer | **Required** | Wire field `simCardType` (python arg: `sim_card_type`). |
| `phoneNumber` | String | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bundleLists`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_internet_bundle_list(operator_type=12345, sim_card_type=12345, phone_number="value")

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "GetInternetBundleList", operator_type=12345, sim_card_type=12345, phone_number="value")
```

---

### GetInternetBundlePaymentToken
اجرای متد رسمی `CharnetService.GetInternetBundlePaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `operatorType` | Integer | **Required** | Wire field `operatorType` (python arg: `operator_type`). |
| `bundleId` | Integer | **Required** | Wire field `bundleId` (python arg: `bundle_id`). |
| `phoneNumber` | String | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `targetUserId` | Object | **Optional** | Wire field `targetUserId` (python arg: `target_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_internet_bundle_payment_token(operator_type=12345, bundle_id=12345, phone_number="value")

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "GetInternetBundlePaymentToken", operator_type=12345, bundle_id=12345, phone_number="value")
```

---

### GetRecentChargeOrders
اجرای متد رسمی `CharnetService.GetRecentChargeOrders` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |
| `types` | Array of Integer | **Required** | Wire field `types` (python arg: `types`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orders`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_recent_charge_orders(count=12345, types=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "GetRecentChargeOrders", count=12345, types=12345)
```

---

### GetRecentInternetBundleOrders
اجرای متد رسمی `CharnetService.GetRecentInternetBundleOrders` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orders`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_recent_internet_bundle_orders(count=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "GetRecentInternetBundleOrders", count=12345)
```

---

### GetTopUpChargePaymentToken
اجرای متد رسمی `CharnetService.GetTopUpChargePaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `providerCode` | String | **Required** | Wire field `providerCode` (python arg: `provider_code`). |
| `topupType` | String | **Required** | Wire field `topupType` (python arg: `topup_type`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `targetPhoneNumber` | String | **Required** | Wire field `targetPhoneNumber` (python arg: `target_phone_number`). |
| `targetUserId` | Object | **Optional** | Wire field `targetUserId` (python arg: `target_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_top_up_charge_payment_token(provider_code="value", topup_type="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "GetTopUpChargePaymentToken", provider_code="value", topup_type="value", amount=12345)
```

---

### GetVoucherChargePaymentToken
اجرای متد رسمی `CharnetService.GetVoucherChargePaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `providerCode` | String | **Required** | Wire field `providerCode` (python arg: `provider_code`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `targetUserId` | Object | **Optional** | Wire field `targetUserId` (python arg: `target_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_voucher_charge_payment_token(provider_code="value", amount=12345, target_user_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("charnetservice", "GetVoucherChargePaymentToken", provider_code="value", amount=12345, target_user_id={...})
```

---

## CrowdFunding (تامین مالی جمعی و مشارکت در پروژه‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.crowdfunding.v1.CrowdFunding` — تعداد متدها: **2**

### GetParticipants
اجرای متد رسمی `CrowdFunding.GetParticipants` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |
| `offset` | Integer | **Required** | Wire field `offset` (python arg: `offset`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userPayments`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_participants(message_id={...}, limit=12345, offset=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("crowdfunding", "GetParticipants", message_id={...}, limit=12345, offset=12345)
```

---

### GetTotalPaidAmount
اجرای متد رسمی `CrowdFunding.GetTotalPaidAmount` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `totalPaidAmount, creatorUserId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_total_paid_amount(message_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("crowdfunding", "GetTotalPaidAmount", message_id={...})
```

---

## Evex (صرافی اوکس و دریافت توکن و لیست ارزها)
> شناسه کامل سرویس در شبکه بله: `bale.evex.v1.Evex` — تعداد متدها: **8**

### GetEvexCurrenciesList
اجرای متد رسمی `Evex.GetEvexCurrenciesList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currencies, icmsWage`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_evex_currencies_list()

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "GetEvexCurrenciesList")
```

---

### GetEvexCurrencyPrice
اجرای متد رسمی `Evex.GetEvexCurrencyPrice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `currencyType` | Integer | **Required** | Wire field `currencyType` (python arg: `currency_type`). |
| `currencyAmount` | Integer | **Required** | Wire field `currencyAmount` (python arg: `currency_amount`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |
| `countryCode` | Integer | **Required** | Wire field `countryCode` (python arg: `country_code`). |
| `exitDate` | String | **Required** | Wire field `exitDate` (python arg: `exit_date`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `deliveryStationType` | Integer | **Required** | Wire field `deliveryStationType` (python arg: `delivery_station_type`). |
| `stationId` | String | **Required** | Wire field `stationId` (python arg: `station_id`). |
| `bankType` | Integer | **Required** | Wire field `bankType` (python arg: `bank_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currencyRate, orderId, amountToPay, rialAmount, melliWage, iceWage, otherWages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_evex_currency_price(currency_type=12345, currency_amount=12345, reason=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "GetEvexCurrencyPrice", currency_type=12345, currency_amount=12345, reason=12345)
```

---

### GetEvexPaymentToken
اجرای متد رسمی `Evex.GetEvexPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `orderId` | Integer | **Required** | Wire field `orderId` (python arg: `order_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, paymentGatewayPrefix, terminalId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_evex_payment_token(order_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "GetEvexPaymentToken", order_id=12345)
```

---

### GetListOfEvexDeliveryStations
اجرای متد رسمی `Evex.GetListOfEvexDeliveryStations` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `deliveryStationType` | Integer | **Required** | Wire field `deliveryStationType` (python arg: `delivery_station_type`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |
| `ExitDate` | String | **Required** | Wire field `ExitDate` (python arg: `exit_date`). |
| `bankType` | Integer | **Required** | Wire field `bankType` (python arg: `bank_type`). |
| `shouldReturnCapacity` | Object | **Optional** | Wire field `shouldReturnCapacity` (python arg: `should_return_capacity`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `stations`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_list_of_evex_delivery_stations(delivery_station_type=12345, reason=12345, exit_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "GetListOfEvexDeliveryStations", delivery_station_type=12345, reason=12345, exit_date="value")
```

---

### GetValidBanks
اجرای متد رسمی `Evex.GetValidBanks` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `accountNationalCode` | Object | **Optional** | Wire field `accountNationalCode` (python arg: `account_national_code`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `banks`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_valid_banks(national_code="value", account_national_code={...})

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "GetValidBanks", national_code="value", account_national_code={...})
```

---

### LoadEvexHistory
اجرای متد رسمی `Evex.LoadEvexHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orders, approvalText`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_evex_history()

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "LoadEvexHistory")
```

---

### VerifyUserEvexAuthority
اجرای متد رسمی `Evex.VerifyUserEvexAuthority` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `firstName` | String | **Required** | Wire field `firstName` (python arg: `first_name`). |
| `lastName` | String | **Required** | Wire field `lastName` (python arg: `last_name`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `passportCode` | String | **Required** | Wire field `passportCode` (python arg: `passport_code`). |
| `postalCode` | String | **Required** | Wire field `postalCode` (python arg: `postal_code`). |
| `birthDate` | String | **Required** | Wire field `birthDate` (python arg: `birth_date`). |
| `fatherName` | String | **Required** | Wire field `fatherName` (python arg: `father_name`). |
| `shId` | String | **Required** | Wire field `shId` (python arg: `sh_id`). |
| `bankType` | Integer | **Required** | Wire field `bankType` (python arg: `bank_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `approval`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_user_evex_authority(first_name="value", last_name="value", national_code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "VerifyUserEvexAuthority", first_name="value", last_name="value", national_code="value")
```

---

### VerifyUserEvexExtraInfo
اجرای متد رسمی `Evex.VerifyUserEvexExtraInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nakhodaInfo` | Object | **Optional** | Wire field `nakhodaInfo` (python arg: `nakhoda_info`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_user_evex_extra_info(nakhoda_info={...})

# ۲. فراخوانی با RPC
result = await app.rpc("evex", "VerifyUserEvexExtraInfo", nakhoda_info={...})
```

---

## Exchange (صرافی، نرخ لحظه‌ای ارزهای مسافرتی و نقدی)
> شناسه کامل سرویس در شبکه بله: `bale.exchange.v1.Exchange` — تعداد متدها: **10**

### GetCurrenciesList
اجرای متد رسمی `Exchange.GetCurrenciesList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currencies, icmsWage`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_currencies_list()

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetCurrenciesList")
```

---

### GetCurrencyPrice
اجرای متد رسمی `Exchange.GetCurrencyPrice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `currencyType` | Integer | **Required** | Wire field `currencyType` (python arg: `currency_type`). |
| `currencyAmount` | Integer | **Required** | Wire field `currencyAmount` (python arg: `currency_amount`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |
| `countryCode` | Integer | **Required** | Wire field `countryCode` (python arg: `country_code`). |
| `exitDate` | String | **Required** | Wire field `exitDate` (python arg: `exit_date`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `deliveryStationType` | Integer | **Required** | Wire field `deliveryStationType` (python arg: `delivery_station_type`). |
| `stationId` | String | **Required** | Wire field `stationId` (python arg: `station_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `currencyRate, orderId, amountToPay, rialAmount, melliWage, iceWage, otherWages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_currency_price(currency_type=12345, currency_amount=12345, reason=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetCurrencyPrice", currency_type=12345, currency_amount=12345, reason=12345)
```

---

### GetExchangeOrderInfo
اجرای متد رسمی `Exchange.GetExchangeOrderInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `orderId` | Integer | **Required** | Wire field `orderId` (python arg: `order_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orderStatus`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_exchange_order_info(order_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetExchangeOrderInfo", order_id=12345)
```

---

### GetExchangePaymentToken
اجرای متد رسمی `Exchange.GetExchangePaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `orderId` | Integer | **Required** | Wire field `orderId` (python arg: `order_id`). |
| `callBack` | String | **Required** | Wire field `callBack` (python arg: `call_back`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_exchange_payment_token(order_id=12345, call_back="value")

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetExchangePaymentToken", order_id=12345, call_back="value")
```

---

### GetInitialConfig
اجرای متد رسمی `Exchange.GetInitialConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `origin` | String | **Required** | Wire field `origin` (python arg: `origin`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_initial_config(origin="value")

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetInitialConfig", origin="value")
```

---

### GetListOfDeliveryStations
اجرای متد رسمی `Exchange.GetListOfDeliveryStations` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `deliveryStationType` | Integer | **Required** | Wire field `deliveryStationType` (python arg: `delivery_station_type`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |
| `ExitDate` | String | **Required** | Wire field `ExitDate` (python arg: `exit_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `stations`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_list_of_delivery_stations(delivery_station_type=12345, reason=12345, exit_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetListOfDeliveryStations", delivery_station_type=12345, reason=12345, exit_date="value")
```

---

### GetTravelCurrencyOrderInDetail
اجرای متد رسمی `Exchange.GetTravelCurrencyOrderInDetail` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phoneNumber` | String | **Optional** | Wire field `phoneNumber` (python arg: `phone_number`). |
| `nationalCode` | String | **Optional** | Wire field `nationalCode` (python arg: `national_code`). |
| `userId` | Integer | **Optional** | Wire field `userId` (python arg: `user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orders`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_travel_currency_order_in_detail(phone_number="value", national_code="value", user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetTravelCurrencyOrderInDetail", phone_number="value", national_code="value", user_id=12345)
```

---

### GetUserIcmsInfo
اجرای متد رسمی `Exchange.GetUserIcmsInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `birthDate` | String | **Required** | Wire field `birthDate` (python arg: `birth_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `firstName, lastName, nationalCode, passportCode, postalCode, birthDate, fatherName, shId, IsValid`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_icms_info(national_code="value", birth_date="value")

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "GetUserIcmsInfo", national_code="value", birth_date="value")
```

---

### LoadExchangeHistory
اجرای متد رسمی `Exchange.LoadExchangeHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orders, approvalText`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_exchange_history()

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "LoadExchangeHistory")
```

---

### VerifyUserExchangeAuthority
اجرای متد رسمی `Exchange.VerifyUserExchangeAuthority` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `firstName` | String | **Required** | Wire field `firstName` (python arg: `first_name`). |
| `lastName` | String | **Required** | Wire field `lastName` (python arg: `last_name`). |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `passportCode` | String | **Required** | Wire field `passportCode` (python arg: `passport_code`). |
| `postalCode` | String | **Required** | Wire field `postalCode` (python arg: `postal_code`). |
| `birthDate` | String | **Required** | Wire field `birthDate` (python arg: `birth_date`). |
| `fatherName` | String | **Required** | Wire field `fatherName` (python arg: `father_name`). |
| `shId` | String | **Required** | Wire field `shId` (python arg: `sh_id`). |
| `isValid` | Boolean | **Required** | Wire field `isValid` (python arg: `is_valid`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_user_exchange_authority(first_name="value", last_name="value", national_code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("exchange", "VerifyUserExchangeAuthority", first_name="value", last_name="value", national_code="value")
```

---

## Falake (بررسی وضعیت پیوندها و دامنه‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.falake.v1.Falake` — تعداد متدها: **1**

### GetLinkStatus
اجرای متد رسمی `Falake.GetLinkStatus` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_link_status()

# ۲. فراخوانی با RPC
result = await app.rpc("falake", "GetLinkStatus")
```

---

## fanoos (سامانه رهگیری و تحلیل رویدادهای فانوس)
> شناسه کامل سرویس در شبکه بله: `bale.fanoos.v1.fanoos` — تعداد متدها: **2**

### Send
اجرای متد رسمی `fanoos.Send` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `eventName` | String | **Required** | Wire field `eventName` (python arg: `event_name`). |
| `items` | Object | **Optional** | Wire field `items` (python arg: `items`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send(event_name="value", items={...}, date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("fanoos", "Send", event_name="value", items={...}, date=12345)
```

---

### SendBatch
اجرای متد رسمی `fanoos.SendBatch` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `events` | Array of Object | **Required** | Wire field `events` (python arg: `events`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_batch(events={...})

# ۲. فراخوانی با RPC
result = await app.rpc("fanoos", "SendBatch", events={...})
```

---

## FeedBack (ارسال بازخورد و پیشنهادات کاربران)
> شناسه کامل سرویس در شبکه بله: `bale.feedback.v1.FeedBack` — تعداد متدها: **1**

### SendFeedBack
اجرای متد رسمی `FeedBack.SendFeedBack` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_feed_back()

# ۲. فراخوانی با RPC
result = await app.rpc("feedback", "SendFeedBack")
```

---

## Garson (جستجوی خدمات، بات‌های دسته‌بندی‌شده و بنرها)
> شناسه کامل سرویس در شبکه بله: `bale.garson.v1.Garson` — تعداد متدها: **11**

### EditCustomServices
اجرای متد رسمی `Garson.EditCustomServices` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `items` | Array of Integer | **Required** | Wire field `items` (python arg: `items`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `customItems`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_custom_services(items=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "EditCustomServices", items=12345)
```

---

### GetAdvertisementBot
اجرای متد رسمی `Garson.GetAdvertisementBot` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bots`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_advertisement_bot()

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetAdvertisementBot")
```

---

### GetBotBanners
اجرای متد رسمی `Garson.GetBotBanners` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `banners`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bot_banners()

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetBotBanners")
```

---

### GetBotsByCategory
اجرای متد رسمی `Garson.GetBotsByCategory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |
| `pagination` | Object | **Optional** | Wire field `pagination` (python arg: `pagination`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bots`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bots_by_category(category_id=12345, pagination={...})

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetBotsByCategory", category_id=12345, pagination={...})
```

---

### GetCategorizedBots
اجرای متد رسمی `Garson.GetCategorizedBots` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `categorizedBots`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_categorized_bots()

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetCategorizedBots")
```

---

### GetCustomServices
اجرای متد رسمی `Garson.GetCustomServices` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `customItems`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_custom_services()

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetCustomServices")
```

---

### GetRecommendedBots
اجرای متد رسمی `Garson.GetRecommendedBots` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botId` | Integer | **Required** | Wire field `botId` (python arg: `bot_id`). |
| `pagination` | Object | **Optional** | Wire field `pagination` (python arg: `pagination`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bots, moreBotsUrl`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_recommended_bots(bot_id=12345, pagination={...})

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetRecommendedBots", bot_id=12345, pagination={...})
```

---

### GetServices
اجرای متد رسمی `Garson.GetServices` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `version` | Integer | **Required** | Wire field `version` (python arg: `version`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `version, isChanged, data, banners, services, sections`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_services(version=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetServices", version=12345)
```

---

### GetTrendBots
اجرای متد رسمی `Garson.GetTrendBots` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bots`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_trend_bots()

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetTrendBots")
```

---

### GetUserRepeatedBots
اجرای متد رسمی `Garson.GetUserRepeatedBots` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bots`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_repeated_bots()

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "GetUserRepeatedBots")
```

---

### SearchServices
اجرای متد رسمی `Garson.SearchServices` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `language` | Object | **Optional** | Wire field `language` (python arg: `language`). |
| `source` | Integer | **Required** | Wire field `source` (python arg: `source`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `sections`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_services(query={...}, language={...}, source=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("garson", "SearchServices", query={...}, language={...}, source=12345)
```

---

## GhasedakService (پیام‌رسانی سازمانی و سرویس قاصدک)
> شناسه کامل سرویس در شبکه بله: `bale.ghasedak.v1.GhasedakService` — تعداد متدها: **2**

### GetDiff
اجرای متد رسمی `GhasedakService.GetDiff` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `states` | Array of Object | **Required** | Wire field `states` (python arg: `states`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `updates, usersRefs, groupsRefs`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_diff(states={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ghasedakservice", "GetDiff", states={...}, optimizations=12345)
```

---

### GetRoutesStates
اجرای متد رسمی `GhasedakService.GetRoutesStates` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeers` | Array of Object | **Required** | Wire field `groupPeers` (python arg: `group_peers`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seqs`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_routes_states(group_peers={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ghasedakservice", "GetRoutesStates", group_peers={...}, optimizations=12345)
```

---

## GiftPacket (ارسال، بازکردن و توکن پرداخت پاکت‌های هدیه)
> شناسه کامل سرویس در شبکه بله: `bale.giftpacket.v1.GiftPacket` — تعداد متدها: **3**

### GetGiftPacketPaymentToken
اجرای متد رسمی `GiftPacket.GetGiftPacketPaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_gift_packet_payment_token(token="value", amount=12345, peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("giftpacket", "GetGiftPacketPaymentToken", token="value", amount=12345, peer={...})
```

---

### OpenGiftPacket
اجرای متد رسمی `GiftPacket.OpenGiftPacket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `msgIdentifier` | Object | **Optional** | Wire field `msgIdentifier` (python arg: `msg_identifier`). |
| `receiverWalletId` | String | **Required** | Wire field `receiverWalletId` (python arg: `receiver_wallet_id`). |
| `pageNo` | Object | **Optional** | Wire field `pageNo` (python arg: `page_no`). |
| `orderType` | Integer | **Required** | Wire field `orderType` (python arg: `order_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `giftReceivers, status, openedCount, selfWinAmount, rank, userOutPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.open_gift_packet(msg_identifier={...}, receiver_wallet_id="value", page_no={...})

# ۲. فراخوانی با RPC
result = await app.rpc("giftpacket", "OpenGiftPacket", msg_identifier={...}, receiver_wallet_id="value", page_no={...})
```

---

### SendGiftPacketWithWallet
اجرای متد رسمی `GiftPacket.SendGiftPacketWithWallet` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `randomId` | Integer | **Required** | Wire field `randomId` (python arg: `random_id`). |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |
| `sourceWalletId` | String | **Required** | Wire field `sourceWalletId` (python arg: `source_wallet_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_gift_packet_with_wallet(peer={...}, random_id=12345, message={...})

# ۲. فراخوانی با RPC
result = await app.rpc("giftpacket", "SendGiftPacketWithWallet", peer={...}, random_id=12345, message={...})
```

---

## Groups (مدیریت کامل گروه‌ها، کانال‌ها، ادمین‌ها و دسترسی‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.groups.v1.Groups` — تعداد متدها: **50**

### AddDiscussionGroupAdmin
اجرای متد رسمی `Groups.AddDiscussionGroupAdmin` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channel` | Object | **Optional** | Wire field `channel` (python arg: `channel`). |
| `discussionGroup` | Object | **Optional** | Wire field `discussionGroup` (python arg: `discussion_group`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_discussion_group_admin(channel={...}, discussion_group={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "AddDiscussionGroupAdmin", channel={...}, discussion_group={...})
```

---

### CreateGroup
اجرای متد رسمی `Groups.CreateGroup` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `users` | Array of Object | **Required** | Wire field `users` (python arg: `users`). |
| `groupType` | Integer | **Required** | Wire field `groupType` (python arg: `group_type`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |
| `nick` | Object | **Optional** | Wire field `nick` (python arg: `nick`). |
| `restriction` | Integer | **Required** | Wire field `restriction` (python arg: `restriction`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, group, users, userPeers, notAddedUserPeers, inviteLink`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_group(rid=12345, title="value", users={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "CreateGroup", rid=12345, title="value", users={...})
```

---

### EditChannelNick
اجرای متد رسمی `Groups.EditChannelNick` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `nick` | String | **Required** | Wire field `nick` (python arg: `nick`). |
| `randomId` | Integer | **Required** | Wire field `randomId` (python arg: `random_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_channel_nick(group_peer={...}, nick="value", random_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "EditChannelNick", group_peer={...}, nick="value", random_id=12345)
```

---

### EditGroupAbout
اجرای متد رسمی `Groups.EditGroupAbout` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `about` | Object | **Optional** | Wire field `about` (python arg: `about`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_group_about(group_peer={...}, rid=12345, about={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "EditGroupAbout", group_peer={...}, rid=12345, about={...})
```

---

### EditGroupAvatar
اجرای متد رسمی `Groups.EditGroupAvatar` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `fileLocation` | Object | **Optional** | Wire field `fileLocation` (python arg: `file_location`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `avatar, seq, state, date`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_group_avatar(group_peer={...}, file_location={...}, rid=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "EditGroupAvatar", group_peer={...}, file_location={...}, rid=12345)
```

---

### EditGroupDefaultCardNumber
اجرای متد رسمی `Groups.EditGroupDefaultCardNumber` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `cardNumber` | String | **Required** | Wire field `cardNumber` (python arg: `card_number`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_group_default_card_number(group_peer={...}, card_number="value")

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "EditGroupDefaultCardNumber", group_peer={...}, card_number="value")
```

---

### EditGroupTitle
اجرای متد رسمی `Groups.EditGroupTitle` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_group_title(group_peer={...}, title="value", rid=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "EditGroupTitle", group_peer={...}, title="value", rid=12345)
```

---

### FetchGroupAdmins
اجرای متد رسمی `Groups.FetchGroupAdmins` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupOutPeer` | Object | **Optional** | Wire field `groupOutPeer` (python arg: `group_out_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `users, admins`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.fetch_group_admins(group_out_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "FetchGroupAdmins", group_out_peer={...})
```

---

### GetBannedUsers
اجرای متد رسمی `Groups.GetBannedUsers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `bannedUsers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_banned_users(group={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetBannedUsers", group={...})
```

---

### GetCanSeeMessages
اجرای متد رسمی `Groups.GetCanSeeMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `canSeeMessages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_can_see_messages(group_peer={...}, user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetCanSeeMessages", group_peer={...}, user_id=12345)
```

---

### GetFullGroup
اجرای متد رسمی `Groups.GetFullGroup` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fullGroup`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_full_group(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetFullGroup", peer={...})
```

---

### GetGroupDefaultCardNumber
اجرای متد رسمی `Groups.GetGroupDefaultCardNumber` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeerr` | Object | **Optional** | Wire field `groupPeerr` (python arg: `group_peerr`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `defaultCardNumber`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_default_card_number(group_peerr={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetGroupDefaultCardNumber", group_peerr={...})
```

---

### GetGroupInviteURL
اجرای متد رسمی `Groups.GetGroupInviteURL` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `url`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_invite_url(group_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetGroupInviteURL", group_peer={...})
```

---

### GetGroupMembersCount
اجرای متد رسمی `Groups.GetGroupMembersCount` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `membersCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_members_count(group={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetGroupMembersCount", group={...})
```

---

### GetGroupPreview
اجرای متد رسمی `Groups.GetGroupPreview` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `isOpenedOutsideBale` | Object | **Optional** | Wire field `isOpenedOutsideBale` (python arg: `is_opened_outside_bale`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `group, action`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_preview(token="value", is_opened_outside_bale={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetGroupPreview", token="value", is_opened_outside_bale={...})
```

---

### GetGroupRecommendations
اجرای متد رسمی `Groups.GetGroupRecommendations` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `source` | Integer | **Required** | Wire field `source` (python arg: `source`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_recommendations(source=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetGroupRecommendations", source=12345)
```

---

### GetMemberPermissions
اجرای متد رسمی `Groups.GetMemberPermissions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |
| `user` | Object | **Optional** | Wire field `user` (python arg: `user`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `permissions`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_member_permissions(group={...}, user={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetMemberPermissions", group={...}, user={...})
```

---

### GetMutualGroups
اجرای متد رسمی `Groups.GetMutualGroups` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_mutual_groups(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetMutualGroups", peer={...})
```

---

### GetMyGroups
اجرای متد رسمی `Groups.GetMyGroups` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `mode` | Integer | **Required** | Wire field `mode` (python arg: `mode`). |
| `isOwner` | Boolean | **Required** | Wire field `isOwner` (python arg: `is_owner`). |
| `filters` | Array of Object | **Required** | Wire field `filters` (python arg: `filters`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_my_groups(mode=12345, is_owner=True, filters={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetMyGroups", mode=12345, is_owner=True, filters={...})
```

---

### GetPins
اجرای متد رسمی `Groups.GetPins` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `page` | Integer | **Required** | Wire field `page` (python arg: `page`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pins, count`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_pins(group_peer={...}, page=12345, limit=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "GetPins", group_peer={...}, page=12345, limit=12345)
```

---

### InviteUser
اجرای متد رسمی `Groups.InviteUser` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `user` | Object | **Optional** | Wire field `user` (python arg: `user`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |
| `messageCount` | Object | **Optional** | Wire field `messageCount` (python arg: `message_count`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.invite_user(group_peer={...}, user={...}, rid=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "InviteUser", group_peer={...}, user={...}, rid=12345)
```

---

### InviteUsers
اجرای متد رسمی `Groups.InviteUsers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `users` | Array of Object | **Required** | Wire field `users` (python arg: `users`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `notAddedUserPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.invite_users(group_peer={...}, rid=12345, users={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "InviteUsers", group_peer={...}, rid=12345, users={...})
```

---

### JoinGroup
اجرای متد رسمی `Groups.JoinGroup` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `group, seq, state, date, users, rid, userPeers, inviterUserId, groupSeq`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.join_group(token="value", optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "JoinGroup", token="value", optimizations=12345)
```

---

### JoinPublicGroup
اجرای متد رسمی `Groups.JoinPublicGroup` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `group, seq, state, date, users, rid, userPeers, inviterUserId, groupSeq`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.join_public_group(peer={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "JoinPublicGroup", peer={...}, optimizations=12345)
```

---

### KickUser
اجرای متد رسمی `Groups.KickUser` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `user` | Object | **Optional** | Wire field `user` (python arg: `user`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.kick_user(group_peer={...}, user={...}, rid=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "KickUser", group_peer={...}, user={...}, rid=12345)
```

---

### LeaveGroup
اجرای متد رسمی `Groups.LeaveGroup` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |
| `makeOrphan` | Object | **Optional** | Wire field `makeOrphan` (python arg: `make_orphan`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.leave_group(group_peer={...}, rid=12345, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "LeaveGroup", group_peer={...}, rid=12345, optimizations=12345)
```

---

### LoadFullGroups
اجرای متد رسمی `Groups.LoadFullGroups` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groups` | Array of Object | **Required** | Wire field `groups` (python arg: `groups`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_full_groups(groups={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "LoadFullGroups", groups={...})
```

---

### LoadGroupAvatars
اجرای متد رسمی `Groups.LoadGroupAvatars` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `avatars`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_group_avatars(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "LoadGroupAvatars", peer={...})
```

---

### LoadGroups
اجرای متد رسمی `Groups.LoadGroups` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_groups(peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "LoadGroups", peers={...})
```

---

### LoadMembers
اجرای متد رسمی `Groups.LoadMembers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |
| `next` | Object | **Optional** | Wire field `next` (python arg: `next`). |
| `condition` | Object | **Optional** | Wire field `condition` (python arg: `condition`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `members, next`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_members(group={...}, limit=12345, next={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "LoadMembers", group={...}, limit=12345, next={...})
```

---

### MakeUserAdmin
اجرای متد رسمی `Groups.MakeUserAdmin` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `userPeer` | Object | **Optional** | Wire field `userPeer` (python arg: `user_peer`). |
| `adminTitle` | Object | **Optional** | Wire field `adminTitle` (python arg: `admin_title`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.make_user_admin(group_peer={...}, user_peer={...}, admin_title={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "MakeUserAdmin", group_peer={...}, user_peer={...}, admin_title={...})
```

---

### PinMessage
اجرای متد رسمی `Groups.PinMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `senderUserId` | Integer | **Required** | Wire field `senderUserId` (python arg: `sender_user_id`). |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `msgRid` | Integer | **Required** | Wire field `msgRid` (python arg: `msg_rid`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.pin_message(sender_user_id=12345, group_peer={...}, date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "PinMessage", sender_user_id=12345, group_peer={...}, date=12345)
```

---

### RemoveDiscussionGroup
اجرای متد رسمی `Groups.RemoveDiscussionGroup` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `channel` | Object | **Optional** | Wire field `channel` (python arg: `channel`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_discussion_group(rid=12345, channel={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "RemoveDiscussionGroup", rid=12345, channel={...})
```

---

### RemoveGroupAvatar
اجرای متد رسمی `Groups.RemoveGroupAvatar` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |
| `avaterId` | Object | **Optional** | Wire field `avaterId` (python arg: `avater_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_group_avatar(group_peer={...}, rid=12345, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "RemoveGroupAvatar", group_peer={...}, rid=12345, optimizations=12345)
```

---

### RemovePin
اجرای متد رسمی `Groups.RemovePin` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_pin(group_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "RemovePin", group_peer={...})
```

---

### RemoveSinglePin
اجرای متد رسمی `Groups.RemoveSinglePin` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `msgRid` | Integer | **Required** | Wire field `msgRid` (python arg: `msg_rid`). |
| `msgDate` | Integer | **Required** | Wire field `msgDate` (python arg: `msg_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_single_pin(group_peer={...}, msg_rid=12345, msg_date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "RemoveSinglePin", group_peer={...}, msg_rid=12345, msg_date=12345)
```

---

### RemoveUserAdmin
اجرای متد رسمی `Groups.RemoveUserAdmin` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `userPeer` | Object | **Optional** | Wire field `userPeer` (python arg: `user_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_user_admin(group_peer={...}, user_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "RemoveUserAdmin", group_peer={...}, user_peer={...})
```

---

### RevokeInviteURL
اجرای متد رسمی `Groups.RevokeInviteURL` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `url`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.revoke_invite_url(group_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "RevokeInviteURL", group_peer={...})
```

---

### SetAvailableReactions
اجرای متد رسمی `Groups.SetAvailableReactions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |
| `codes` | Array of String | **Required** | Wire field `codes` (python arg: `codes`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_available_reactions(group={...}, codes="value")

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetAvailableReactions", group={...}, codes="value")
```

---

### SetCanSeeHistory
اجرای متد رسمی `Groups.SetCanSeeHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `canSeeHistory` | Boolean | **Required** | Wire field `canSeeHistory` (python arg: `can_see_history`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_can_see_history(group_peer={...}, can_see_history=True)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetCanSeeHistory", group_peer={...}, can_see_history=True)
```

---

### SetCanSeeMessages
اجرای متد رسمی `Groups.SetCanSeeMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |
| `canSeeMessages` | Boolean | **Required** | Wire field `canSeeMessages` (python arg: `can_see_messages`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_can_see_messages(group_peer={...}, user_id=12345, can_see_messages=True)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetCanSeeMessages", group_peer={...}, user_id=12345, can_see_messages=True)
```

---

### SetDiscussionGroup
اجرای متد رسمی `Groups.SetDiscussionGroup` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `channel` | Object | **Optional** | Wire field `channel` (python arg: `channel`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `discussionGroup, group`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_discussion_group(rid=12345, channel={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetDiscussionGroup", rid=12345, channel={...})
```

---

### SetGroupDefaultPermissions
اجرای متد رسمی `Groups.SetGroupDefaultPermissions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |
| `permissions` | Object | **Optional** | Wire field `permissions` (python arg: `permissions`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_group_default_permissions(group={...}, permissions={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetGroupDefaultPermissions", group={...}, permissions={...})
```

---

### SetMemberCustomTitle
اجرای متد رسمی `Groups.SetMemberCustomTitle` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupId` | Integer | **Required** | Wire field `groupId` (python arg: `group_id`). |
| `memberId` | Integer | **Required** | Wire field `memberId` (python arg: `member_id`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_member_custom_title(group_id=12345, member_id=12345, title="value")

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetMemberCustomTitle", group_id=12345, member_id=12345, title="value")
```

---

### SetMemberPermissions
اجرای متد رسمی `Groups.SetMemberPermissions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |
| `user` | Object | **Optional** | Wire field `user` (python arg: `user`). |
| `permissions` | Object | **Optional** | Wire field `permissions` (python arg: `permissions`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_member_permissions(group={...}, user={...}, permissions={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetMemberPermissions", group={...}, user={...}, permissions={...})
```

---

### SetRestriction
اجرای متد رسمی `Groups.SetRestriction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupOutPeer` | Object | **Optional** | Wire field `groupOutPeer` (python arg: `group_out_peer`). |
| `restriction` | Integer | **Required** | Wire field `restriction` (python arg: `restriction`). |
| `nick` | Object | **Optional** | Wire field `nick` (python arg: `nick`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_restriction(group_out_peer={...}, restriction=12345, nick={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetRestriction", group_out_peer={...}, restriction=12345, nick={...})
```

---

### SetSignMessages
اجرای متد رسمی `Groups.SetSignMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `signMessages` | Boolean | **Required** | Wire field `signMessages` (python arg: `sign_messages`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_sign_messages(group_peer={...}, sign_messages=True)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetSignMessages", group_peer={...}, sign_messages=True)
```

---

### SetSlowMode
اجرای متد رسمی `Groups.SetSlowMode` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group` | Object | **Optional** | Wire field `group` (python arg: `group`). |
| `seconds` | Object | **Optional** | Wire field `seconds` (python arg: `seconds`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_slow_mode(group={...}, seconds={...})

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "SetSlowMode", group={...}, seconds={...})
```

---

### TransferOwnership
اجرای متد رسمی `Groups.TransferOwnership` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `newOwner` | Integer | **Required** | Wire field `newOwner` (python arg: `new_owner`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.transfer_ownership(group_peer={...}, new_owner=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "TransferOwnership", group_peer={...}, new_owner=12345)
```

---

### UnBanUser
اجرای متد رسمی `Groups.UnBanUser` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groupPeer` | Object | **Optional** | Wire field `groupPeer` (python arg: `group_peer`). |
| `user` | Object | **Optional** | Wire field `user` (python arg: `user`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.un_ban_user(group_peer={...}, user={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("groups", "UnBanUser", group_peer={...}, user={...}, optimizations=12345)
```

---

## Ketf (خدمات بات‌ها، دکمه‌های اینلاین و وب‌اپ‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.ketf.v1.Ketf` — تعداد متدها: **14**

### GetBotGroupPermissions
اجرای متد رسمی `Ketf.GetBotGroupPermissions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |
| `groupId` | Integer | **Required** | Wire field `groupId` (python arg: `group_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `hasAccessToMessages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bot_group_permissions(bot_user_id=12345, group_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetBotGroupPermissions", bot_user_id=12345, group_id=12345)
```

---

### GetBotInfo
اجرای متد رسمی `Ketf.GetBotInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `botInfo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bot_info(bot_user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetBotInfo", bot_user_id=12345)
```

---

### GetBotWhiteList
اجرای متد رسمی `Ketf.GetBotWhiteList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `list`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bot_white_list(bot_user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetBotWhiteList", bot_user_id=12345)
```

---

### GetBots
اجرای متد رسمی `Ketf.GetBots` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pagination` | Object | **Optional** | Wire field `pagination` (python arg: `pagination`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pageCount, bots`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bots(pagination={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetBots", pagination={...})
```

---

### GetInlineBotResults
اجرای متد رسمی `Ketf.GetInlineBotResults` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | String | **Required** | Wire field `query` (python arg: `query`). |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |
| `offset` | String | **Required** | Wire field `offset` (python arg: `offset`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `results, nextOffset, queryId, isGallery`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_inline_bot_results(query="value", peer={...}, bot_user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetInlineBotResults", query="value", peer={...}, bot_user_id=12345)
```

---

### GetPaymentDetails
اجرای متد رسمی `Ketf.GetPaymentDetails` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `purchaseMessageId` | Object | **Optional** | Wire field `purchaseMessageId` (python arg: `purchase_message_id`). |
| `invoiceIdentifier` | Object | **Optional** | Wire field `invoiceIdentifier` (python arg: `invoice_identifier`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `title, totalAmount, paymentsHistory, session, disapproved, description, labeledPrices`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_payment_details(purchase_message_id={...}, invoice_identifier={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetPaymentDetails", purchase_message_id={...}, invoice_identifier={...})
```

---

### GetUserContext
اجرای متد رسمی `Ketf.GetUserContext` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `botUserId, userId, nonce, sign`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_context(bot_user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetUserContext", bot_user_id=12345)
```

---

### GetWebappHash
اجرای متد رسمی `Ketf.GetWebappHash` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |
| `data` | String | **Required** | Wire field `data` (python arg: `data`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `hash, queryId, authDate`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_webapp_hash(bot_user_id=12345, data="value")

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "GetWebappHash", bot_user_id=12345, data="value")
```

---

### InvokeCustomAction
اجرای متد رسمی `Ketf.InvokeCustomAction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | String | **Required** | Wire field `id` (python arg: `id`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `openDialogAction` | Object | **Optional** | Wire field `openDialogAction` (python arg: `open_dialog_action`). |
| `done` | Object | **Optional** | Wire field `done` (python arg: `done`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.invoke_custom_action(id="value", message_id={...}, peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "InvokeCustomAction", id="value", message_id={...}, peer={...})
```

---

### MakePayment
اجرای متد رسمی `Ketf.MakePayment` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `paymentSessionId` | String | **Required** | Wire field `paymentSessionId` (python arg: `payment_session_id`). |
| `paymentOptionId` | String | **Required** | Wire field `paymentOptionId` (python arg: `payment_option_id`). |
| `wallet` | Object | **Optional** | Wire field `wallet` (python arg: `wallet`). |
| `gateway` | Object | **Optional** | Wire field `gateway` (python arg: `gateway`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `gatewayRedirect, paymentReceipt`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.make_payment(payment_session_id="value", payment_option_id="value", wallet={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "MakePayment", payment_session_id="value", payment_option_id="value", wallet={...})
```

---

### SendAuthenticatedInlineCallBackData
اجرای متد رسمی `Ketf.SendAuthenticatedInlineCallBackData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `templateMessageId` | Object | **Optional** | Wire field `templateMessageId` (python arg: `template_message_id`). |
| `data` | Object | **Optional** | Wire field `data` (python arg: `data`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_authenticated_inline_call_back_data(template_message_id={...}, data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "SendAuthenticatedInlineCallBackData", template_message_id={...}, data={...})
```

---

### SendInlineCallBackData
اجرای متد رسمی `Ketf.SendInlineCallBackData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `historyMessageIdentifier` | Object | **Optional** | Wire field `historyMessageIdentifier` (python arg: `history_message_identifier`). |
| `data` | Object | **Optional** | Wire field `data` (python arg: `data`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_inline_call_back_data(history_message_identifier={...}, data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "SendInlineCallBackData", history_message_identifier={...}, data={...})
```

---

### SendInlineCallback
اجرای متد رسمی `Ketf.SendInlineCallback` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |
| `data` | Object | **Optional** | Wire field `data` (python arg: `data`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `answer`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_inline_callback(peer={...}, message_id={...}, data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "SendInlineCallback", peer={...}, message_id={...}, data={...})
```

---

### SendMiniAppData
اجرای متد رسمی `Ketf.SendMiniAppData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |
| `queryId` | Object | **Optional** | Wire field `queryId` (python arg: `query_id`). |
| `data` | Object | **Optional** | Wire field `data` (python arg: `data`). |
| `buttonText` | Object | **Optional** | Wire field `buttonText` (python arg: `button_text`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_mini_app_data(bot_user_id=12345, query_id={...}, data={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ketf", "SendMiniAppData", bot_user_id=12345, query_id={...}, data={...})
```

---

## Kifpool (کیف‌پول، شارژ، تسویه، اعتبار و تراکنش‌های ارزی)
> شناسه کامل سرویس در شبکه بله: `bale.kifpool.v1.Kifpool` — تعداد متدها: **30**

### CashOut
اجرای متد رسمی `Kifpool.CashOut` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `requestId` | String | **Required** | Wire field `requestId` (python arg: `request_id`). |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `account` | Object | **Optional** | Wire field `account` (python arg: `account`). |
| `pan` | Object | **Optional** | Wire field `pan` (python arg: `pan`). |
| `iban` | Object | **Optional** | Wire field `iban` (python arg: `iban`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `referenceNo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.cash_out(request_id="value", token="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CashOut", request_id="value", token="value", amount=12345)
```

---

### Charge
اجرای متد رسمی `Kifpool.Charge` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `paymentToken` | String | **Required** | Wire field `paymentToken` (python arg: `payment_token`). |
| `referenceNo` | Integer | **Required** | Wire field `referenceNo` (python arg: `reference_no`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.charge(payment_token="value", reference_no=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "Charge", payment_token="value", reference_no=12345)
```

---

### CheckChargePermission
اجرای متد رسمی `Kifpool.CheckChargePermission` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `paymentToken` | String | **Required** | Wire field `paymentToken` (python arg: `payment_token`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.check_charge_permission(payment_token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CheckChargePermission", payment_token="value")
```

---

### CreateKifpool
اجرای متد رسمی `Kifpool.CreateKifpool` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nationalId` | Object | **Optional** | Wire field `nationalId` (python arg: `national_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_kifpool(national_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CreateKifpool", national_id={...})
```

---

### CryptoCashOut
اجرای متد رسمی `Kifpool.CryptoCashOut` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `requestId` | String | **Required** | Wire field `requestId` (python arg: `request_id`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `account` | Object | **Optional** | Wire field `account` (python arg: `account`). |
| `pan` | Object | **Optional** | Wire field `pan` (python arg: `pan`). |
| `pocketType` | Integer | **Required** | Wire field `pocketType` (python arg: `pocket_type`). |
| `isMerchant` | Object | **Optional** | Wire field `isMerchant` (python arg: `is_merchant`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `referenceNo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.crypto_cash_out(request_id="value", amount=12345, account={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CryptoCashOut", request_id="value", amount=12345, account={...})
```

---

### CryptoInvoice
اجرای متد رسمی `Kifpool.CryptoInvoice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `pageSize` | Integer | **Required** | Wire field `pageSize` (python arg: `page_size`). |
| `pageNumber` | Integer | **Required** | Wire field `pageNumber` (python arg: `page_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `records`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.crypto_invoice(token="value", page_size=12345, page_number=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CryptoInvoice", token="value", page_size=12345, page_number=12345)
```

---

### CryptoPurchase
اجرای متد رسمی `Kifpool.CryptoPurchase` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `srcToken` | String | **Required** | Wire field `srcToken` (python arg: `src_token`). |
| `dstToken` | String | **Required** | Wire field `dstToken` (python arg: `dst_token`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `terminalId` | String | **Required** | Wire field `terminalId` (python arg: `terminal_id`). |
| `bornaTrxId` | String | **Required** | Wire field `bornaTrxId` (python arg: `borna_trx_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.crypto_purchase(amount=12345, src_token="value", dst_token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CryptoPurchase", amount=12345, src_token="value", dst_token="value")
```

---

### CryptoRefund
اجرای متد رسمی `Kifpool.CryptoRefund` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `approvalCode` | Integer | **Required** | Wire field `approvalCode` (python arg: `approval_code`). |
| `trxRefSrc` | String | **Required** | Wire field `trxRefSrc` (python arg: `trx_ref_src`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.crypto_refund(token="value", amount=12345, approval_code=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CryptoRefund", token="value", amount=12345, approval_code=12345)
```

---

### CryptoTransfer
اجرای متد رسمی `Kifpool.CryptoTransfer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `srcToken` | String | **Required** | Wire field `srcToken` (python arg: `src_token`). |
| `dstToken` | String | **Required** | Wire field `dstToken` (python arg: `dst_token`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |
| `dstPhoneNo` | Object | **Optional** | Wire field `dstPhoneNo` (python arg: `dst_phone_no`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `amount, date, approvalCode, srcToken, dstToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.crypto_transfer(amount=12345, src_token="value", dst_token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "CryptoTransfer", amount=12345, src_token="value", dst_token="value")
```

---

### FeeInquiry
اجرای متد رسمی `Kifpool.FeeInquiry` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `transactionType` | Object | **Optional** | Wire field `transactionType` (python arg: `transaction_type`). |
| `pocketType` | Integer | **Required** | Wire field `pocketType` (python arg: `pocket_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `amount, fee, responseData`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.fee_inquiry(amount=12345, transaction_type={...}, pocket_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "FeeInquiry", amount=12345, transaction_type={...}, pocket_type=12345)
```

---

### GetChargePaymentToken
اجرای متد رسمی `Kifpool.GetChargePaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `callbackType` | Integer | **Required** | Wire field `callbackType` (python arg: `callback_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_charge_payment_token(token="value", amount=12345, callback_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetChargePaymentToken", token="value", amount=12345, callback_type=12345)
```

---

### GetCredit
اجرای متد رسمی `Kifpool.GetCredit` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `balance, hasCredit`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_credit()

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetCredit")
```

---

### GetCryptoChargePaymentToken
اجرای متد رسمی `Kifpool.GetCryptoChargePaymentToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `receiverId` | String | **Required** | Wire field `receiverId` (python arg: `receiver_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_crypto_charge_payment_token(token="value", amount=12345, receiver_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetCryptoChargePaymentToken", token="value", amount=12345, receiver_id="value")
```

---

### GetCryptoWallets
اجرای متد رسمی `Kifpool.GetCryptoWallets` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `myCryptoWallets`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_crypto_wallets()

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetCryptoWallets")
```

---

### GetKifpoolOwner
اجرای متد رسمی `Kifpool.GetKifpoolOwner` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `walletToken` | String | **Required** | Wire field `walletToken` (python arg: `wallet_token`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `firstName, lastName, walletStatus, approvalCode`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_kifpool_owner(wallet_token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetKifpoolOwner", wallet_token="value")
```

---

### GetKifpoolPointBalance
اجرای متد رسمی `Kifpool.GetKifpoolPointBalance` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pointBalanceInfo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_kifpool_point_balance(token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetKifpoolPointBalance", token="value")
```

---

### GetKifpoolPointDetails
اجرای متد رسمی `Kifpool.GetKifpoolPointDetails` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `count` | Integer | **Required** | Wire field `count` (python arg: `count`). |
| `page` | Integer | **Required** | Wire field `page` (python arg: `page`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pointDetailsInfo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_kifpool_point_details(token="value", count=12345, page=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetKifpoolPointDetails", token="value", count=12345, page=12345)
```

---

### GetKifpoolPointSummery
اجرای متد رسمی `Kifpool.GetKifpoolPointSummery` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pointSummeryInfo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_kifpool_point_summery(token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetKifpoolPointSummery", token="value")
```

---

### GetKifpoolTransactionPoint
اجرای متد رسمی `Kifpool.GetKifpoolTransactionPoint` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionID` | Integer | **Required** | Wire field `transactionID` (python arg: `transaction_id`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `calculatedPoint, point, unitAmount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_kifpool_transaction_point(transaction_id=12345, amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetKifpoolTransactionPoint", transaction_id=12345, amount=12345)
```

---

### GetMyKifpools
اجرای متد رسمی `Kifpool.GetMyKifpools` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `invocationSpot` | Object | **Optional** | Wire field `invocationSpot` (python arg: `invocation_spot`). |
| `pocketType` | Integer | **Required** | Wire field `pocketType` (python arg: `pocket_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `myWallets, firstName, lastName`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_my_kifpools(invocation_spot={...}, pocket_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "GetMyKifpools", invocation_spot={...}, pocket_type=12345)
```

---

### Invoice
اجرای متد رسمی `Kifpool.Invoice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `pageSize` | Integer | **Required** | Wire field `pageSize` (python arg: `page_size`). |
| `pageNumber` | Integer | **Required** | Wire field `pageNumber` (python arg: `page_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `records`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.invoice(token="value", page_size=12345, page_number=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "Invoice", token="value", page_size=12345, page_number=12345)
```

---

### PayForMessage
اجرای متد رسمی `Kifpool.PayForMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `chargeAmount` | Integer | **Required** | Wire field `chargeAmount` (python arg: `charge_amount`). |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `status, paymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.pay_for_message(amount=12345, charge_amount=12345, message={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "PayForMessage", amount=12345, charge_amount=12345, message={...})
```

---

### Purchase
اجرای متد رسمی `Kifpool.Purchase` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `dstToken` | String | **Required** | Wire field `dstToken` (python arg: `dst_token`). |
| `srcToken` | String | **Required** | Wire field `srcToken` (python arg: `src_token`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `useCredit` | Object | **Optional** | Wire field `useCredit` (python arg: `use_credit`). |
| `couponId` | Object | **Optional** | Wire field `couponId` (python arg: `coupon_id`). |
| `terminalNo` | Object | **Optional** | Wire field `terminalNo` (python arg: `terminal_no`). |
| `stan` | Object | **Optional** | Wire field `stan` (python arg: `stan`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.purchase(amount=12345, dst_token="value", src_token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "Purchase", amount=12345, dst_token="value", src_token="value")
```

---

### PurchaseMessage
اجرای متد رسمی `Kifpool.PurchaseMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `historyId` | Object | **Optional** | Wire field `historyId` (python arg: `history_id`). |
| `amount` | Object | **Optional** | Wire field `amount` (python arg: `amount`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.purchase_message(history_id={...}, amount={...}, description={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "PurchaseMessage", history_id={...}, amount={...}, description={...})
```

---

### PurchaseMessageWithCharge
اجرای متد رسمی `Kifpool.PurchaseMessageWithCharge` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `historyId` | Object | **Optional** | Wire field `historyId` (python arg: `history_id`). |
| `amount` | Object | **Optional** | Wire field `amount` (python arg: `amount`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |
| `chargeAmount` | Integer | **Required** | Wire field `chargeAmount` (python arg: `charge_amount`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.purchase_message_with_charge(history_id={...}, amount={...}, description={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "PurchaseMessageWithCharge", history_id={...}, amount={...}, description={...})
```

---

### PurchaseWithCharge
اجرای متد رسمی `Kifpool.PurchaseWithCharge` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `dstToken` | String | **Required** | Wire field `dstToken` (python arg: `dst_token`). |
| `srcToken` | String | **Required** | Wire field `srcToken` (python arg: `src_token`). |
| `description` | String | **Required** | Wire field `description` (python arg: `description`). |
| `chargeAmount` | Integer | **Required** | Wire field `chargeAmount` (python arg: `charge_amount`). |
| `useCredit` | Object | **Optional** | Wire field `useCredit` (python arg: `use_credit`). |
| `couponId` | Object | **Optional** | Wire field `couponId` (python arg: `coupon_id`). |
| `terminalNo` | Object | **Optional** | Wire field `terminalNo` (python arg: `terminal_no`). |
| `stan` | Object | **Optional** | Wire field `stan` (python arg: `stan`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `paymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.purchase_with_charge(amount=12345, dst_token="value", src_token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "PurchaseWithCharge", amount=12345, dst_token="value", src_token="value")
```

---

### Transfer
اجرای متد رسمی `Kifpool.Transfer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `sourceToken` | String | **Required** | Wire field `sourceToken` (python arg: `source_token`). |
| `destinationToken` | Object | **Optional** | Wire field `destinationToken` (python arg: `destination_token`). |
| `destinationPhone` | Object | **Optional** | Wire field `destinationPhone` (python arg: `destination_phone`). |
| `destinationUserid` | Object | **Optional** | Wire field `destinationUserid` (python arg: `destination_userid`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.transfer(source_token="value", destination_token={...}, destination_phone={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "Transfer", source_token="value", destination_token={...}, destination_phone={...})
```

---

### UpgradeKifpool
اجرای متد رسمی `Kifpool.UpgradeKifpool` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `nationalId` | Object | **Optional** | Wire field `nationalId` (python arg: `national_id`). |
| `cardNo` | Object | **Optional** | Wire field `cardNo` (python arg: `card_no`). |
| `accountNo` | Object | **Optional** | Wire field `accountNo` (python arg: `account_no`). |
| `remainReferenceNumber` | String | **Required** | Wire field `remainReferenceNumber` (python arg: `remain_reference_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `level`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.upgrade_kifpool(token="value", national_id={...}, card_no={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "UpgradeKifpool", token="value", national_id={...}, card_no={...})
```

---

### VerifyCashOutKifpool
اجرای متد رسمی `Kifpool.VerifyCashOutKifpool` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `accountNo, firstName, lastName`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_cash_out_kifpool(token="value")

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "VerifyCashOutKifpool", token="value")
```

---

### VerifyPurchaseMessage
اجرای متد رسمی `Kifpool.VerifyPurchaseMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `historyId` | Object | **Optional** | Wire field `historyId` (python arg: `history_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `amount, paymentTypeTitle, paymentTitle`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_purchase_message(history_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("kifpool", "VerifyPurchaseMessage", history_id={...})
```

---

## LLMAuthService (احراز هویت خدمات هوش مصنوعی و مدل‌های زبانی)
> شناسه کامل سرویس در شبکه بله: `bale.llm_auth.v1.LLMAuthService` — تعداد متدها: **1**

### GetAuthToken
اجرای متد رسمی `LLMAuthService.GetAuthToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_auth_token()

# ۲. فراخوانی با RPC
result = await app.rpc("llmauthservice", "GetAuthToken")
```

---

## Magazine (پست‌های برتر، مجله بله، لایک و دسته‌بندی‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.magazine.v1.Magazine` — تعداد متدها: **9**

### GetMessageUpvoters
اجرای متد رسمی `Magazine.GetMessageUpvoters` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `loadMoreState, users`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_message_upvoters(load_more_state={...}, message={...})

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "GetMessageUpvoters", load_more_state={...}, message={...})
```

---

### GetMyUpvotes
اجرای متد رسمی `Magazine.GetMyUpvotes` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `upvotes`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_my_upvotes()

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "GetMyUpvotes")
```

---

### GetSimilarPosts
اجرای متد رسمی `Magazine.GetSimilarPosts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `messages, loadMoreState, similarPosts`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_similar_posts(message={...}, load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "GetSimilarPosts", message={...}, load_more_state={...})
```

---

### LoadCategories
اجرای متد رسمی `Magazine.LoadCategories` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `categories`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_categories()

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "LoadCategories")
```

---

### LoadCategoryFeedMessages
اجرای متد رسمی `Magazine.LoadCategoryFeedMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `loadMoreState, messages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_category_feed_messages(category_id=12345, load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "LoadCategoryFeedMessages", category_id=12345, load_more_state={...})
```

---

### LoadFeedMessages
اجرای متد رسمی `Magazine.LoadFeedMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `loadMoreState, messages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_feed_messages(load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "LoadFeedMessages", load_more_state={...})
```

---

### LoadInternalFeedMessages
اجرای متد رسمی `Magazine.LoadInternalFeedMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `loadMoreState, messages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_internal_feed_messages(load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "LoadInternalFeedMessages", load_more_state={...})
```

---

### RevokeUpvotedPost
اجرای متد رسمی `Magazine.RevokeUpvotedPost` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |
| `albumId` | Object | **Optional** | Wire field `albumId` (python arg: `album_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `upvotes`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.revoke_upvoted_post(message={...}, album_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "RevokeUpvotedPost", message={...}, album_id={...})
```

---

### UpvotePost
اجرای متد رسمی `Magazine.UpvotePost` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |
| `albumId` | Object | **Optional** | Wire field `albumId` (python arg: `album_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `upvotes`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.upvote_post(message={...}, album_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("magazine", "UpvotePost", message={...}, album_id={...})
```

---

## Market (فروشگاه بله، کمپین‌ها، تگ‌ها و محصولات)
> شناسه کامل سرویس در شبکه بله: `bale.market.v1.Market` — تعداد متدها: **26**

### AcceptCampaignMarket
اجرای متد رسمی `Market.AcceptCampaignMarket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `marketId` | Integer | **Required** | Wire field `marketId` (python arg: `market_id`). |
| `isPermanent` | Boolean | **Required** | Wire field `isPermanent` (python arg: `is_permanent`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.accept_campaign_market(market_id=12345, is_permanent=True)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "AcceptCampaignMarket", market_id=12345, is_permanent=True)
```

---

### AcceptMarketJoinRequest
اجرای متد رسمی `Market.AcceptMarketJoinRequest` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `marketPeerId` | Integer | **Required** | Wire field `marketPeerId` (python arg: `market_peer_id`). |
| `requestId` | Integer | **Required** | Wire field `requestId` (python arg: `request_id`). |
| `displayName` | String | **Required** | Wire field `displayName` (python arg: `display_name`). |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.accept_market_join_request(market_peer_id=12345, request_id=12345, display_name="value")

# ۲. فراخوانی با RPC
result = await app.rpc("market", "AcceptMarketJoinRequest", market_peer_id=12345, request_id=12345, display_name="value")
```

---

### CreateMarketJoinRequest
اجرای متد رسمی `Market.CreateMarketJoinRequest` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `marketPeerId` | Integer | **Required** | Wire field `marketPeerId` (python arg: `market_peer_id`). |
| `displayName` | String | **Required** | Wire field `displayName` (python arg: `display_name`). |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |
| `tagIds` | Array of Integer | **Required** | Wire field `tagIds` (python arg: `tag_ids`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_market_join_request(market_peer_id=12345, display_name="value", category_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "CreateMarketJoinRequest", market_peer_id=12345, display_name="value", category_id=12345)
```

---

### CreateTag
اجرای متد رسمی `Market.CreateTag` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `tag`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_tag(title="value", category_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "CreateTag", title="value", category_id=12345)
```

---

### GetCategoriesList
اجرای متد رسمی `Market.GetCategoriesList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |
| `level` | Object | **Optional** | Wire field `level` (python arg: `level`). |
| `includeSampleMarkets` | Object | **Optional** | Wire field `includeSampleMarkets` (python arg: `include_sample_markets`). |
| `version` | Object | **Optional** | Wire field `version` (python arg: `version`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `categories, version`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_categories_list(category_id=12345, level={...}, include_sample_markets={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetCategoriesList", category_id=12345, level={...}, include_sample_markets={...})
```

---

### GetCategoryMarkets
اجرای متد رسمی `Market.GetCategoryMarkets` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |
| `pagination` | Object | **Optional** | Wire field `pagination` (python arg: `pagination`). |
| `version` | Integer | **Required** | Wire field `version` (python arg: `version`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `markets, version`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_category_markets(category_id=12345, pagination={...}, version=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetCategoryMarkets", category_id=12345, pagination={...}, version=12345)
```

---

### GetCategoryProducts
اجرای متد رسمی `Market.GetCategoryProducts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |
| `pagination` | Object | **Optional** | Wire field `pagination` (python arg: `pagination`). |
| `version` | Integer | **Required** | Wire field `version` (python arg: `version`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `products, version`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_category_products(category_id=12345, pagination={...}, version=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetCategoryProducts", category_id=12345, pagination={...}, version=12345)
```

---

### GetIndexedProducts
اجرای متد رسمی `Market.GetIndexedProducts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `startDate` | Integer | **Required** | Wire field `startDate` (python arg: `start_date`). |
| `endDate` | Integer | **Required** | Wire field `endDate` (python arg: `end_date`). |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `products`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_indexed_products(start_date=12345, end_date=12345, category_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetIndexedProducts", start_date=12345, end_date=12345, category_id=12345)
```

---

### GetMarket
اجرای متد رسمی `Market.GetMarket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Integer | **Optional** | Wire field `peerId` (python arg: `peer_id`). |
| `nickName` | String | **Optional** | Wire field `nickName` (python arg: `nick_name`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `market, lastRequest`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_market(peer_id=12345, nick_name="value")

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetMarket", peer_id=12345, nick_name="value")
```

---

### GetMarketJoinRequests
اجرای متد رسمی `Market.GetMarketJoinRequests` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `marketJoinRequests`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_market_join_requests()

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetMarketJoinRequests")
```

---

### GetMarketsPendingJoinRequest
اجرای متد رسمی `Market.GetMarketsPendingJoinRequest` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `requests`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_markets_pending_join_request()

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetMarketsPendingJoinRequest")
```

---

### GetNumberOfSales
اجرای متد رسمی `Market.GetNumberOfSales` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `numberOfSales, isMarket`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_number_of_sales(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetNumberOfSales", peer={...})
```

---

### GetOnboardingStatus
اجرای متد رسمی `Market.GetOnboardingStatus` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `status, categoryIds, gender`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_onboarding_status()

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetOnboardingStatus")
```

---

### GetPendingCampaignMarkets
اجرای متد رسمی `Market.GetPendingCampaignMarkets` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `markets`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_pending_campaign_markets()

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetPendingCampaignMarkets")
```

---

### GetStores
اجرای متد رسمی `Market.GetStores` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `version` | Integer | **Required** | Wire field `version` (python arg: `version`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `stores, version`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_stores(version=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetStores", version=12345)
```

---

### GetTags
اجرای متد رسمی `Market.GetTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryId` | Integer | **Required** | Wire field `categoryId` (python arg: `category_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `tags`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_tags(category_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetTags", category_id=12345)
```

---

### GetTopMarkets
اجرای متد رسمی `Market.GetTopMarkets` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ratingType` | Integer | **Required** | Wire field `ratingType` (python arg: `rating_type`). |
| `pagination` | Object | **Optional** | Wire field `pagination` (python arg: `pagination`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `markets`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_top_markets(rating_type=12345, pagination={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetTopMarkets", rating_type=12345, pagination={...})
```

---

### GetYaldaStores
اجرای متد رسمی `Market.GetYaldaStores` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `version` | Integer | **Required** | Wire field `version` (python arg: `version`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `stores, version`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_yalda_stores(version=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "GetYaldaStores", version=12345)
```

---

### RejectCampaignMarket
اجرای متد رسمی `Market.RejectCampaignMarket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `marketId` | Integer | **Required** | Wire field `marketId` (python arg: `market_id`). |
| `isPermanent` | Boolean | **Required** | Wire field `isPermanent` (python arg: `is_permanent`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.reject_campaign_market(market_id=12345, is_permanent=True)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "RejectCampaignMarket", market_id=12345, is_permanent=True)
```

---

### RejectMarketJoinRequest
اجرای متد رسمی `Market.RejectMarketJoinRequest` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `marketPeerId` | Integer | **Required** | Wire field `marketPeerId` (python arg: `market_peer_id`). |
| `rejectCause` | Integer | **Required** | Wire field `rejectCause` (python arg: `reject_cause`). |
| `requestId` | Integer | **Required** | Wire field `requestId` (python arg: `request_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.reject_market_join_request(market_peer_id=12345, reject_cause=12345, request_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("market", "RejectMarketJoinRequest", market_peer_id=12345, reject_cause=12345, request_id=12345)
```

---

### SetGenericDeepLinks
اجرای متد رسمی `Market.SetGenericDeepLinks` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `links` | Array of Object | **Required** | Wire field `links` (python arg: `links`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_generic_deep_links(links={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "SetGenericDeepLinks", links={...})
```

---

### SetMarketBanners
اجرای متد رسمی `Market.SetMarketBanners` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `banners` | Array of Object | **Required** | Wire field `banners` (python arg: `banners`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_market_banners(banners={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "SetMarketBanners", banners={...})
```

---

### SetOnboardingData
اجرای متد رسمی `Market.SetOnboardingData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `categoryIds` | Array of Integer | **Required** | Wire field `categoryIds` (python arg: `category_ids`). |
| `gender` | Integer | **Required** | Wire field `gender` (python arg: `gender`). |
| `isSkipped` | Object | **Optional** | Wire field `isSkipped` (python arg: `is_skipped`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_onboarding_data(category_ids=12345, gender=12345, is_skipped={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "SetOnboardingData", category_ids=12345, gender=12345, is_skipped={...})
```

---

### SetPopularSearches
اجرای متد رسمی `Market.SetPopularSearches` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `items` | Array of Object | **Required** | Wire field `items` (python arg: `items`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_popular_searches(items={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "SetPopularSearches", items={...})
```

---

### SubmitMarketFeedback
اجرای متد رسمی `Market.SubmitMarketFeedback` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `rate` | Integer | **Required** | Wire field `rate` (python arg: `rate`). |
| `userOpinion` | Object | **Optional** | Wire field `userOpinion` (python arg: `user_opinion`). |
| `clientVersion` | Object | **Optional** | Wire field `clientVersion` (python arg: `client_version`). |
| `extraFields` | Array of Object | **Required** | Wire field `extraFields` (python arg: `extra_fields`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.submit_market_feedback(rate=12345, user_opinion={...}, client_version={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "SubmitMarketFeedback", rate=12345, user_opinion={...}, client_version={...})
```

---

### UpdateMarketInfo
اجرای متد رسمی `Market.UpdateMarketInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peerId` | Integer | **Required** | Wire field `peerId` (python arg: `peer_id`). |
| `displayName` | Object | **Optional** | Wire field `displayName` (python arg: `display_name`). |
| `primaryCategoryId` | Object | **Optional** | Wire field `primaryCategoryId` (python arg: `primary_category_id`). |
| `isBanned` | Object | **Optional** | Wire field `isBanned` (python arg: `is_banned`). |
| `isActive` | Object | **Optional** | Wire field `isActive` (python arg: `is_active`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_market_info(peer_id=12345, display_name={...}, primary_category_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("market", "UpdateMarketInfo", peer_id=12345, display_name={...}, primary_category_id={...})
```

---

## MavizStream (استریم رویدادها و دریافت تفاوت‌های بلادرنگ)
> شناسه کامل سرویس در شبکه بله: `bale.maviz.v1.MavizStream` — تعداد متدها: **4**

### GetDifference
اجرای متد رسمی `MavizStream.GetDifference` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `routeSequences` | Array of Object | **Required** | Wire field `routeSequences` (python arg: `route_sequences`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupEvents, usersRefs, groupsRefs`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_difference(route_sequences={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("mavizstream", "GetDifference", route_sequences={...}, optimizations=12345)
```

---

### SubscribeToThreadUpdates
اجرای متد رسمی `MavizStream.SubscribeToThreadUpdates` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `threadId` | Object | **Optional** | Wire field `threadId` (python arg: `thread_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.subscribe_to_thread_updates(peer={...}, thread_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("mavizstream", "SubscribeToThreadUpdates", peer={...}, thread_id={...})
```

---

### SubscribeToUpdates
اجرای متد رسمی `MavizStream.SubscribeToUpdates` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `isMtProto` | Boolean | **Required** | Wire field `isMtProto` (python arg: `is_mt_proto`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `update, routeId, sequence, timestamp, weakEvent, mtupdate, updates`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.subscribe_to_updates(is_mt_proto=True)

# ۲. فراخوانی با RPC
result = await app.rpc("mavizstream", "SubscribeToUpdates", is_mt_proto=True)
```

---

### UnsubscribeFromThreadUpdates
اجرای متد رسمی `MavizStream.UnsubscribeFromThreadUpdates` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `threadId` | Object | **Optional** | Wire field `threadId` (python arg: `thread_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.unsubscribe_from_thread_updates(peer={...}, thread_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("mavizstream", "UnsubscribeFromThreadUpdates", peer={...}, thread_id={...})
```

---

## Meet (کنفرانس و تماس‌های صوتی و تصویری گروهی LiveKit)
> شناسه کامل سرویس در شبکه بله: `bale.meet.v1.Meet` — تعداد متدها: **30**

### AcceptCall
اجرای متد رسمی `Meet.AcceptCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `inviteEnable` | Object | **Optional** | Wire field `inviteEnable` (python arg: `invite_enable`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `call, participants, seq, sipCall, isStream`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.accept_call(call_id=12345, invite_enable={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "AcceptCall", call_id=12345, invite_enable={...})
```

---

### AnswerCallJoinRequest
اجرای متد رسمی `Meet.AnswerCallJoinRequest` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `requesterIdentifier` | String | **Required** | Wire field `requesterIdentifier` (python arg: `requester_identifier`). |
| `isAllowed` | Boolean | **Required** | Wire field `isAllowed` (python arg: `is_allowed`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.answer_call_join_request(call_id=12345, requester_identifier="value", is_allowed=True)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "AnswerCallJoinRequest", call_id=12345, requester_identifier="value", is_allowed=True)
```

---

### AskToJoinCall
اجرای متد رسمی `Meet.AskToJoinCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.ask_to_join_call(call_id=12345, name="value")

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "AskToJoinCall", call_id=12345, name="value")
```

---

### DeleteCallLogs
اجرای متد رسمی `Meet.DeleteCallLogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callIds` | Array of Object | **Required** | Wire field `callIds` (python arg: `call_ids`). |
| `all` | Boolean | **Required** | Wire field `all` (python arg: `all`). |
| `invert` | Boolean | **Required** | Wire field `invert` (python arg: `invert`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_call_logs(call_ids={...}, all=True, invert=True)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "DeleteCallLogs", call_ids={...}, all=True, invert=True)
```

---

### DeleteStream
اجرای متد رسمی `Meet.DeleteStream` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `streamUser` | Object | **Optional** | Wire field `streamUser` (python arg: `stream_user`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_stream(stream_user={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "DeleteStream", stream_user={...})
```

---

### DiscardCall
اجرای متد رسمی `Meet.DiscardCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `duration` | Integer | **Required** | Wire field `duration` (python arg: `duration`). |
| `reason` | Integer | **Required** | Wire field `reason` (python arg: `reason`). |
| `type` | Integer | **Required** | Wire field `type` (python arg: `type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `call, participants, seq, sipCall, isStream`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.discard_call(call_id=12345, duration=12345, reason=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "DiscardCall", call_id=12345, duration=12345, reason=12345)
```

---

### GenerateCallLink
اجرای متد رسمی `Meet.GenerateCallLink` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `isPublic` | Boolean | **Required** | Wire field `isPublic` (python arg: `is_public`). |
| `callId` | Object | **Optional** | Wire field `callId` (python arg: `call_id`). |
| `title` | Object | **Optional** | Wire field `title` (python arg: `title`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupCall, linkExpirationPeriod`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.generate_call_link(is_public=True, call_id={...}, title={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "GenerateCallLink", is_public=True, call_id={...}, title={...})
```

---

### GetCallLinkDetails
اجرای متد رسمی `Meet.GetCallLinkDetails` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `session` | String | **Required** | Wire field `session` (python arg: `session`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupCall`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_call_link_details(session="value")

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "GetCallLinkDetails", session="value")
```

---

### GetCallLogs
اجرای متد رسمی `Meet.GetCallLogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pageNumber` | Object | **Optional** | Wire field `pageNumber` (python arg: `page_number`). |
| `pageSize` | Object | **Optional** | Wire field `pageSize` (python arg: `page_size`). |
| `afterDate` | Object | **Optional** | Wire field `afterDate` (python arg: `after_date`). |
| `beforeDate` | Object | **Optional** | Wire field `beforeDate` (python arg: `before_date`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `callLogs, total`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_call_logs(page_number={...}, page_size={...}, after_date={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "GetCallLogs", page_number={...}, page_size={...}, after_date={...})
```

---

### GetCallState
اجرای متد رسمی `Meet.GetCallState` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupCall`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_call_state(call_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "GetCallState", call_id=12345)
```

---

### GetGroupCall
اجرای متد رسمی `Meet.GetGroupCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupCall`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_call(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "GetGroupCall", peer={...})
```

---

### GetOngoingCalls
اجرای متد رسمی `Meet.GetOngoingCalls` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pageNumber` | Object | **Optional** | Wire field `pageNumber` (python arg: `page_number`). |
| `pageSize` | Object | **Optional** | Wire field `pageSize` (python arg: `page_size`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `callLogs`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_ongoing_calls(page_number={...}, page_size={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "GetOngoingCalls", page_number={...}, page_size={...})
```

---

### GetWssURL
اجرای متد رسمی `Meet.GetWssURL` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `url`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_wss_url(call_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "GetWssURL", call_id=12345)
```

---

### InviteToCall
اجرای متد رسمی `Meet.InviteToCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `invitees` | Array of Object | **Required** | Wire field `invitees` (python arg: `invitees`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `peerStates`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.invite_to_call(call_id=12345, invitees={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "InviteToCall", call_id=12345, invitees={...})
```

---

### JoinGroupCall
اجرای متد رسمی `Meet.JoinGroupCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `name` | Object | **Optional** | Wire field `name` (python arg: `name`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupCall, states`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.join_group_call(call_id=12345, name={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "JoinGroupCall", call_id=12345, name={...})
```

---

### LeaveGroupCall
اجرای متد رسمی `Meet.LeaveGroupCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `end` | Boolean | **Required** | Wire field `end` (python arg: `end`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupCall, seq`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.leave_group_call(call_id=12345, end=True)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "LeaveGroupCall", call_id=12345, end=True)
```

---

### MuteParticipant
اجرای متد رسمی `Meet.MuteParticipant` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `identity` | String | **Required** | Wire field `identity` (python arg: `identity`). |
| `trackId` | String | **Required** | Wire field `trackId` (python arg: `track_id`). |
| `revokePublishPermission` | Boolean | **Required** | Wire field `revokePublishPermission` (python arg: `revoke_publish_permission`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.mute_participant(call_id=12345, identity="value", track_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "MuteParticipant", call_id=12345, identity="value", track_id="value")
```

---

### ReceiveCall
اجرای متد رسمی `Meet.ReceiveCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.receive_call(call_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "ReceiveCall", call_id=12345)
```

---

### RemoveParticipant
اجرای متد رسمی `Meet.RemoveParticipant` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `identity` | String | **Required** | Wire field `identity` (python arg: `identity`). |
| `blockFromCall` | Boolean | **Required** | Wire field `blockFromCall` (python arg: `block_from_call`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_participant(call_id=12345, identity="value", block_from_call=True)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "RemoveParticipant", call_id=12345, identity="value", block_from_call=True)
```

---

### SendCallReaction
اجرای متد رسمی `Meet.SendCallReaction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `reaction` | String | **Required** | Wire field `reaction` (python arg: `reaction`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_call_reaction(call_id=12345, reaction="value")

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "SendCallReaction", call_id=12345, reaction="value")
```

---

### SendFanoosEvent
اجرای متد رسمی `Meet.SendFanoosEvent` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `eventName` | String | **Required** | Wire field `eventName` (python arg: `event_name`). |
| `items` | Object | **Optional** | Wire field `items` (python arg: `items`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_fanoos_event(event_name="value", items={...}, date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "SendFanoosEvent", event_name="value", items={...}, date=12345)
```

---

### SetLinkTitle
اجرای متد رسمی `Meet.SetLinkTitle` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |
| `callId` | Object | **Optional** | Wire field `callId` (python arg: `call_id`). |
| `linkUrl` | Object | **Optional** | Wire field `linkUrl` (python arg: `link_url`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_link_title(title="value", call_id={...}, link_url={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "SetLinkTitle", title="value", call_id={...}, link_url={...})
```

---

### StartCall
اجرای متد رسمی `Meet.StartCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `video` | Boolean | **Required** | Wire field `video` (python arg: `video`). |
| `internalCall` | Object | **Optional** | Wire field `internalCall` (python arg: `internal_call`). |
| `sipCall` | Object | **Optional** | Wire field `sipCall` (python arg: `sip_call`). |
| `liveKitCall` | Object | **Optional** | Wire field `liveKitCall` (python arg: `live_kit_call`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `call, participants, seq, sipCall, isStream`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_call(peer={...}, rid=12345, video=True)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "StartCall", peer={...}, rid=12345, video=True)
```

---

### StartGroupCall
اجرای متد رسمی `Meet.StartGroupCall` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `randomId` | Integer | **Required** | Wire field `randomId` (python arg: `random_id`). |
| `video` | Boolean | **Required** | Wire field `video` (python arg: `video`). |
| `mode` | Integer | **Required** | Wire field `mode` (python arg: `mode`). |
| `invitees` | Array of Object | **Required** | Wire field `invitees` (python arg: `invitees`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groupCall, seq`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_group_call(peer={...}, random_id=12345, video=True)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "StartGroupCall", peer={...}, random_id=12345, video=True)
```

---

### StartRecording
اجرای متد رسمی `Meet.StartRecording` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `layout` | String | **Required** | Wire field `layout` (python arg: `layout`). |
| `quality` | Integer | **Required** | Wire field `quality` (python arg: `quality`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_recording(call_id=12345, layout="value", quality=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "StartRecording", call_id=12345, layout="value", quality=12345)
```

---

### StartStream
اجرای متد رسمی `Meet.StartStream` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `streamUser` | Object | **Optional** | Wire field `streamUser` (python arg: `stream_user`). |
| `url` | String | **Required** | Wire field `url` (python arg: `url`). |
| `rtmpServer` | String | **Required** | Wire field `rtmpServer` (python arg: `rtmp_server`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `streamKey`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.start_stream(stream_user={...}, url="value", rtmp_server="value")

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "StartStream", stream_user={...}, url="value", rtmp_server="value")
```

---

### StopRecording
اجرای متد رسمی `Meet.StopRecording` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.stop_recording(call_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "StopRecording", call_id=12345)
```

---

### SubmitCallFeedback
اجرای متد رسمی `Meet.SubmitCallFeedback` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `rate` | Integer | **Required** | Wire field `rate` (python arg: `rate`). |
| `userOpinion` | Object | **Optional** | Wire field `userOpinion` (python arg: `user_opinion`). |
| `client` | Integer | **Required** | Wire field `client` (python arg: `client`). |
| `clientVersion` | Object | **Optional** | Wire field `clientVersion` (python arg: `client_version`). |
| `extraFields` | Array of Object | **Required** | Wire field `extraFields` (python arg: `extra_fields`). |
| `isStream` | Object | **Optional** | Wire field `isStream` (python arg: `is_stream`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.submit_call_feedback(call_id=12345, rate=12345, user_opinion={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "SubmitCallFeedback", call_id=12345, rate=12345, user_opinion={...})
```

---

### TakeCallAction
اجرای متد رسمی `Meet.TakeCallAction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `lowerHand` | Object | **Optional** | Wire field `lowerHand` (python arg: `lower_hand`). |
| `raiseHand` | Object | **Optional** | Wire field `raiseHand` (python arg: `raise_hand`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.take_call_action(call_id=12345, lower_hand={...}, raise_hand={...})

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "TakeCallAction", call_id=12345, lower_hand={...}, raise_hand={...})
```

---

### UpdateLayout
اجرای متد رسمی `Meet.UpdateLayout` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callId` | Integer | **Required** | Wire field `callId` (python arg: `call_id`). |
| `requestedLayout` | String | **Required** | Wire field `requestedLayout` (python arg: `requested_layout`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_layout(call_id=12345, requested_layout="value")

# ۲. فراخوانی با RPC
result = await app.rpc("meet", "UpdateLayout", call_id=12345, requested_layout="value")
```

---

## MessageStream (استریم دریافت و لغو پیام‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.message_stream.v1.MessageStream` — تعداد متدها: **2**

### CancelMessageStream
اجرای متد رسمی `MessageStream.CancelMessageStream` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.cancel_message_stream(ex_peer={...}, message_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messagestream", "CancelMessageStream", ex_peer={...}, message_id={...})
```

---

### ReceiveMessageStream
اجرای متد رسمی `MessageStream.ReceiveMessageStream` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |
| `fromChunkId` | Object | **Optional** | Wire field `fromChunkId` (python arg: `from_chunk_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `chunkTimeoutMillis`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.receive_message_stream(ex_peer={...}, message_id={...}, from_chunk_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messagestream", "ReceiveMessageStream", ex_peer={...}, message_id={...}, from_chunk_id={...})
```

---

## Messaging (مدیریت پیام‌ها، پوشه‌ها، تردها و بایگانی گفتگوها)
> شناسه کامل سرویس در شبکه بله: `bale.messaging.v2.Messaging` — تعداد متدها: **43**

### ArchiveDialogs
اجرای متد رسمی `Messaging.ArchiveDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeers` | Array of Object | **Required** | Wire field `exPeers` (python arg: `ex_peers`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.archive_dialogs(ex_peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "ArchiveDialogs", ex_peers={...})
```

---

### ClearChat
اجرای متد رسمی `Messaging.ClearChat` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.clear_chat(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "ClearChat", peer={...})
```

---

### CreateFolder
اجرای متد رسمی `Messaging.CreateFolder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `folderId, index, unreadPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_folder(name="value", peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "CreateFolder", name="value", peers={...})
```

---

### CreateReservedFolder
اجرای متد رسمی `Messaging.CreateReservedFolder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `index, unreadPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_reserved_folder(folder_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "CreateReservedFolder", folder_id=12345)
```

---

### CreateThread
اجرای متد رسمی `Messaging.CreateThread` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `randomId` | Integer | **Required** | Wire field `randomId` (python arg: `random_id`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `threadId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_thread(peer={...}, date=12345, random_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "CreateThread", peer={...}, date=12345, random_id=12345)
```

---

### CreateTopic
اجرای متد رسمی `Messaging.CreateTopic` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `topicId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_topic(ex_peer={...}, title="value")

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "CreateTopic", ex_peer={...}, title="value")
```

---

### DeleteChat
اجرای متد رسمی `Messaging.DeleteChat` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_chat(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "DeleteChat", peer={...})
```

---

### DeleteFolder
اجرای متد رسمی `Messaging.DeleteFolder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_folder(folder_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "DeleteFolder", folder_id=12345)
```

---

### DeleteMessage
اجرای متد رسمی `Messaging.DeleteMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rids` | Array of Integer | **Required** | Wire field `rids` (python arg: `rids`). |
| `dates` | Object | **Optional** | Wire field `dates` (python arg: `dates`). |
| `justMine` | Object | **Optional** | Wire field `justMine` (python arg: `just_mine`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_message(peer={...}, rids=12345, dates={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "DeleteMessage", peer={...}, rids=12345, dates={...})
```

---

### DeleteTopic
اجرای متد رسمی `Messaging.DeleteTopic` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `topicId` | Object | **Optional** | Wire field `topicId` (python arg: `topic_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_topic(ex_peer={...}, topic_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "DeleteTopic", ex_peer={...}, topic_id={...})
```

---

### EditFolder
اجرای متد رسمی `Messaging.EditFolder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |
| `addedPeers` | Array of Object | **Required** | Wire field `addedPeers` (python arg: `added_peers`). |
| `deletedPeers` | Array of Object | **Required** | Wire field `deletedPeers` (python arg: `deleted_peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `unreadPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_folder(folder_id=12345, name="value", added_peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "EditFolder", folder_id=12345, name="value", added_peers={...})
```

---

### EditTopic
اجرای متد رسمی `Messaging.EditTopic` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `topicId` | Object | **Optional** | Wire field `topicId` (python arg: `topic_id`). |
| `title` | String | **Required** | Wire field `title` (python arg: `title`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_topic(ex_peer={...}, topic_id={...}, title="value")

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "EditTopic", ex_peer={...}, topic_id={...}, title="value")
```

---

### FetchProtectedMessage
اجرای متد رسمی `Messaging.FetchProtectedMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `history`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.fetch_protected_message(peer={...}, message_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "FetchProtectedMessage", peer={...}, message_id={...})
```

---

### ForwardMessages
اجرای متد رسمی `Messaging.ForwardMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rid` | Array of Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `forwardedMessages` | Array of Object | **Required** | Wire field `forwardedMessages` (python arg: `forwarded_messages`). |
| `groupedId` | Object | **Optional** | Wire field `groupedId` (python arg: `grouped_id`). |
| `hideSender` | Boolean | **Required** | Wire field `hideSender` (python arg: `hide_sender`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.forward_messages(peer={...}, rid=12345, forwarded_messages={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "ForwardMessages", peer={...}, rid=12345, forwarded_messages={...})
```

---

### GetDiscussionMessage
اجرای متد رسمی `Messaging.GetDiscussionMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `discussionMessage`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_discussion_message(peer={...}, message_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "GetDiscussionMessage", peer={...}, message_id={...})
```

---

### GetMessagesRepliesInfo
اجرای متد رسمی `Messaging.GetMessagesRepliesInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `mids` | Array of Object | **Required** | Wire field `mids` (python arg: `mids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `containers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_messages_replies_info(peer={...}, mids={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "GetMessagesRepliesInfo", peer={...}, mids={...})
```

---

### GetTopicByID
اجرای متد رسمی `Messaging.GetTopicByID` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `topicId` | Object | **Optional** | Wire field `topicId` (python arg: `topic_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `topic`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_topic_by_id(ex_peer={...}, topic_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "GetTopicByID", ex_peer={...}, topic_id={...})
```

---

### GetTopics
اجرای متد رسمی `Messaging.GetTopics` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `minDate` | Integer | **Required** | Wire field `minDate` (python arg: `min_date`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `topics`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_topics(ex_peer={...}, min_date=12345, limit=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "GetTopics", ex_peer={...}, min_date=12345, limit=12345)
```

---

### LoadDialogs
اجرای متد رسمی `Messaging.LoadDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `minDate` | Integer | **Required** | Wire field `minDate` (python arg: `min_date`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |
| `dialogType` | Integer | **Required** | Wire field `dialogType` (python arg: `dialog_type`). |
| `excludePinnedDialogs` | Boolean | **Required** | Wire field `excludePinnedDialogs` (python arg: `exclude_pinned_dialogs`). |
| `archiveFilter` | Integer | **Required** | Wire field `archiveFilter` (python arg: `archive_filter`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groups, users, dialogs, userPeers, groupPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_dialogs(min_date=12345, limit=12345, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadDialogs", min_date=12345, limit=12345, optimizations=12345)
```

---

### LoadFolderDialogs
اجرای متد رسمی `Messaging.LoadFolderDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `minDate` | Integer | **Required** | Wire field `minDate` (python arg: `min_date`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |
| `archiveFilter` | Integer | **Required** | Wire field `archiveFilter` (python arg: `archive_filter`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogs`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_folder_dialogs(min_date=12345, limit=12345, folder_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadFolderDialogs", min_date=12345, limit=12345, folder_id=12345)
```

---

### LoadFolders
اجرای متد رسمی `Messaging.LoadFolders` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `includeMutedUnreadPeers` | Boolean | **Required** | Wire field `includeMutedUnreadPeers` (python arg: `include_muted_unread_peers`). |
| `isNewUser` | Boolean | **Required** | Wire field `isNewUser` (python arg: `is_new_user`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `folders, unreadPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_folders(include_muted_unread_peers=True, is_new_user=True)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadFolders", include_muted_unread_peers=True, is_new_user=True)
```

---

### LoadGroupedDialogs
اجرای متد رسمی `Messaging.LoadGroupedDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |
| `archiveFilter` | Integer | **Required** | Wire field `archiveFilter` (python arg: `archive_filter`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogs, users, groups, showArchived, showInvite, userPeers, groupPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_grouped_dialogs(optimizations=12345, archive_filter=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadGroupedDialogs", optimizations=12345, archive_filter=12345)
```

---

### LoadHistory
اجرای متد رسمی `Messaging.LoadHistory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `loadMode` | Integer | **Required** | Wire field `loadMode` (python arg: `load_mode`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `history, users, userPeers, groups, groupPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_history(peer={...}, date=12345, load_mode=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadHistory", peer={...}, date=12345, load_mode=12345)
```

---

### LoadPeerDialogs
اجرای متد رسمی `Messaging.LoadPeerDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogs, groups, users, userPeers, groupPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_peer_dialogs(peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadPeerDialogs", peers={...})
```

---

### LoadPeers
اجرای متد رسمی `Messaging.LoadPeers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `exPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_peers()

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadPeers")
```

---

### LoadPinnedDialogs
اجرای متد رسمی `Messaging.LoadPinnedDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogs`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_pinned_dialogs(folder_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadPinnedDialogs", folder_id=12345)
```

---

### LoadPinnedMessages
اجرای متد رسمی `Messaging.LoadPinnedMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pinnedMessages`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_pinned_messages(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadPinnedMessages", peer={...})
```

---

### LoadReplies
اجرای متد رسمی `Messaging.LoadReplies` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `threadId` | Object | **Optional** | Wire field `threadId` (python arg: `thread_id`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `loadMode` | Integer | **Required** | Wire field `loadMode` (python arg: `load_mode`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `history, users, userPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_replies(peer={...}, thread_id={...}, date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "LoadReplies", peer={...}, thread_id={...}, date=12345)
```

---

### MarkDialogsAsRead
اجرای متد رسمی `Messaging.MarkDialogsAsRead` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.mark_dialogs_as_read(peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "MarkDialogsAsRead", peers={...})
```

---

### MarkDialogsAsUnread
اجرای متد رسمی `Messaging.MarkDialogsAsUnread` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.mark_dialogs_as_unread(peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "MarkDialogsAsUnread", peers={...})
```

---

### MentionRead
اجرای متد رسمی `Messaging.MentionRead` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.mention_read(peer={...}, message_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "MentionRead", peer={...}, message_id={...})
```

---

### MessageRead
اجرای متد رسمی `Messaging.MessageRead` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.message_read(peer={...}, date=12345, ex_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "MessageRead", peer={...}, date=12345, ex_peer={...})
```

---

### MessageReceived
اجرای متد رسمی `Messaging.MessageReceived` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.message_received(peer={...}, date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "MessageReceived", peer={...}, date=12345)
```

---

### PinDialogs
اجرای متد رسمی `Messaging.PinDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogs, peers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.pin_dialogs(peers={...}, folder_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "PinDialogs", peers={...}, folder_id=12345)
```

---

### PinMessage
اجرای متد رسمی `Messaging.PinMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |
| `justMine` | Boolean | **Required** | Wire field `justMine` (python arg: `just_mine`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.pin_message(peer={...}, message_id={...}, just_mine=True)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "PinMessage", peer={...}, message_id={...}, just_mine=True)
```

---

### ReorderFolders
اجرای متد رسمی `Messaging.ReorderFolders` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `folderIds` | Array of Integer | **Required** | Wire field `folderIds` (python arg: `folder_ids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `folderIds`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.reorder_folders(folder_ids=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "ReorderFolders", folder_ids=12345)
```

---

### ReorderPinnedDialogs
اجرای متد رسمی `Messaging.ReorderPinnedDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogs, peers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.reorder_pinned_dialogs(peers={...}, folder_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "ReorderPinnedDialogs", peers={...}, folder_id=12345)
```

---

### SendMessage
اجرای متد رسمی `Messaging.SendMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |
| `isOnlyForUser` | Object | **Optional** | Wire field `isOnlyForUser` (python arg: `is_only_for_user`). |
| `quotedMessageReference` | Object | **Optional** | Wire field `quotedMessageReference` (python arg: `quoted_message_reference`). |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `isSilent` | Boolean | **Required** | Wire field `isSilent` (python arg: `is_silent`). |
| `threadId` | Object | **Optional** | Wire field `threadId` (python arg: `thread_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_message(peer={...}, rid=12345, message={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "SendMessage", peer={...}, rid=12345, message={...})
```

---

### SendMultiMediaMessage
اجرای متد رسمی `Messaging.SendMultiMediaMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `multiMedia` | Array of Object | **Required** | Wire field `multiMedia` (python arg: `multi_media`). |
| `repliedMessage` | Object | **Optional** | Wire field `repliedMessage` (python arg: `replied_message`). |
| `groupedId` | Integer | **Required** | Wire field `groupedId` (python arg: `grouped_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_multi_media_message(peer={...}, multi_media={...}, replied_message={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "SendMultiMediaMessage", peer={...}, multi_media={...}, replied_message={...})
```

---

### UnArchiveDialogs
اجرای متد رسمی `Messaging.UnArchiveDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeers` | Array of Object | **Required** | Wire field `exPeers` (python arg: `ex_peers`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.un_archive_dialogs(ex_peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "UnArchiveDialogs", ex_peers={...})
```

---

### UnPinMessages
اجرای متد رسمی `Messaging.UnPinMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `messageIds` | Array of Object | **Required** | Wire field `messageIds` (python arg: `message_ids`). |
| `all` | Boolean | **Required** | Wire field `all` (python arg: `all`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.un_pin_messages(peer={...}, message_ids={...}, all=True)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "UnPinMessages", peer={...}, message_ids={...}, all=True)
```

---

### UnpinDialogs
اجرای متد رسمی `Messaging.UnpinDialogs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |
| `folderId` | Integer | **Required** | Wire field `folderId` (python arg: `folder_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.unpin_dialogs(peers={...}, folder_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "UnpinDialogs", peers={...}, folder_id=12345)
```

---

### UpdateMessage
اجرای متد رسمی `Messaging.UpdateMessage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `rid` | Integer | **Required** | Wire field `rid` (python arg: `rid`). |
| `updatedMessage` | Object | **Optional** | Wire field `updatedMessage` (python arg: `updated_message`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, date, state, ext, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_message(peer={...}, rid=12345, updated_message={...})

# ۲. فراخوانی با RPC
result = await app.rpc("messaging", "UpdateMessage", peer={...}, rid=12345, updated_message={...})
```

---

## MicroBanki (خدمات میکروبانکی و توکن سرویس بام)
> شناسه کامل سرویس در شبکه بله: `bale.microbanki.v1.MicroBanki` — تعداد متدها: **3**

### GetBamServiceToken
اجرای متد رسمی `MicroBanki.GetBamServiceToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `service` | Integer | **Required** | Wire field `service` (python arg: `service`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `endpoint, token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bam_service_token(service=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("microbanki", "GetBamServiceToken", service=12345)
```

---

### GetMoneyRequestDetails
اجرای متد رسمی `MicroBanki.GetMoneyRequestDetails` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `totalAmount, payCount, lastPayDate, responseType`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_money_request_details(message={...})

# ۲. فراخوانی با RPC
result = await app.rpc("microbanki", "GetMoneyRequestDetails", message={...})
```

---

### GetMoneyRequestPaymentList
اجرای متد رسمی `MicroBanki.GetMoneyRequestPaymentList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `message` | Object | **Optional** | Wire field `message` (python arg: `message`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `payment, loadMoreState, responseType, userPeers, groupPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_money_request_payment_list(message={...}, load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("microbanki", "GetMoneyRequestPaymentList", message={...}, load_more_state={...})
```

---

## MyBank (اطلاعات حساب و سرویس مای‌بانک)
> شناسه کامل سرویس در شبکه بله: `bale.my_bank.v1.MyBank` — تعداد متدها: **1**

### GetMyBank
اجرای متد رسمی `MyBank.GetMyBank` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_my_bank()

# ۲. فراخوانی با RPC
result = await app.rpc("mybank", "GetMyBank")
```

---

## Negah (لیست دیده‌شدن پیام‌ها (Seen List))
> شناسه کامل سرویس در شبکه بله: `bale.negah.v1.Negah` — تعداد متدها: **1**

### GetMessageSeenList
اجرای متد رسمی `Negah.GetMessageSeenList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_message_seen_list()

# ۲. فراخوانی با RPC
result = await app.rpc("negah", "GetMessageSeenList")
```

---

## Organizations (مخاطبین سازمانی و اطلاعات سازمان‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.organizations.v1.Organizations` — تعداد متدها: **2**

### GetUserOrganizationInfo
اجرای متد رسمی `Organizations.GetUserOrganizationInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userOrganization`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_organization_info()

# ۲. فراخوانی با RPC
result = await app.rpc("organizations", "GetUserOrganizationInfo")
```

---

### GetUserOrganizationalContacts
اجرای متد رسمی `Organizations.GetUserOrganizationalContacts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_organizational_contacts()

# ۲. فراخوانی با RPC
result = await app.rpc("organizations", "GetUserOrganizationalContacts")
```

---

## Pfm (مدیریت مالی شخصی (PFM)، برچسب تراکنش‌ها و گزارش‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.pfm.v1.Pfm` — تعداد متدها: **15**

### AddDetailToTransaction
اجرای متد رسمی `Pfm.AddDetailToTransaction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Object | **Optional** | Wire field `id` (python arg: `id`). |
| `detail` | String | **Required** | Wire field `detail` (python arg: `detail`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_detail_to_transaction(id={...}, detail="value")

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "AddDetailToTransaction", id={...}, detail="value")
```

---

### AddTransactionTags
اجرای متد رسمی `Pfm.AddTransactionTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Object | **Optional** | Wire field `id` (python arg: `id`). |
| `tags` | Array of Object | **Required** | Wire field `tags` (python arg: `tags`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_transaction_tags(id={...}, tags={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "AddTransactionTags", id={...}, tags={...})
```

---

### AddUserTags
اجرای متد رسمی `Pfm.AddUserTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `tags` | Array of Object | **Required** | Wire field `tags` (python arg: `tags`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_user_tags(tags={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "AddUserTags", tags={...})
```

---

### FilterTaggedTransactions
اجرای متد رسمی `Pfm.FilterTaggedTransactions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ids` | Array of Object | **Required** | Wire field `ids` (python arg: `ids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `idsWithTag`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.filter_tagged_transactions(ids={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "FilterTaggedTransactions", ids={...})
```

---

### GetSubTransactions
اجرای متد رسمی `Pfm.GetSubTransactions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionId` | Object | **Optional** | Wire field `transactionId` (python arg: `transaction_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactionIds`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_sub_transactions(transaction_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "GetSubTransactions", transaction_id={...})
```

---

### GetTransactionTags
اجرای متد رسمی `Pfm.GetTransactionTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Object | **Optional** | Wire field `id` (python arg: `id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `tags`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_transaction_tags(id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "GetTransactionTags", id={...})
```

---

### GetUserAccounts
اجرای متد رسمی `Pfm.GetUserAccounts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `accounts, config`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_accounts()

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "GetUserAccounts")
```

---

### GetUserTags
اجرای متد رسمی `Pfm.GetUserTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `getUserTagType` | Integer | **Required** | Wire field `getUserTagType` (python arg: `get_user_tag_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `tags`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_tags(get_user_tag_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "GetUserTags", get_user_tag_type=12345)
```

---

### LoadTransactions
اجرای متد رسمی `Pfm.LoadTransactions` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `accountNumber` | Integer | **Required** | Wire field `accountNumber` (python arg: `account_number`). |
| `startDate` | Object | **Optional** | Wire field `startDate` (python arg: `start_date`). |
| `endDate` | Object | **Optional** | Wire field `endDate` (python arg: `end_date`). |
| `transactionType` | Integer | **Required** | Wire field `transactionType` (python arg: `transaction_type`). |
| `label` | Array of Object | **Required** | Wire field `label` (python arg: `label`). |
| `limit` | Integer | **Required** | Wire field `limit` (python arg: `limit`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |
| `loadMode` | Integer | **Required** | Wire field `loadMode` (python arg: `load_mode`). |
| `userTagType` | Integer | **Required** | Wire field `userTagType` (python arg: `user_tag_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactions, totalAmounts, loadMoreState, totalAmountsPerDay`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_transactions(account_number=12345, start_date={...}, end_date={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "LoadTransactions", account_number=12345, start_date={...}, end_date={...})
```

---

### LoadTransactionsByIDs
اجرای متد رسمی `Pfm.LoadTransactionsByIDs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionIds` | Array of Object | **Required** | Wire field `transactionIds` (python arg: `transaction_ids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactions`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_transactions_by_i_ds(transaction_ids={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "LoadTransactionsByIDs", transaction_ids={...})
```

---

### RemoveTransaction
اجرای متد رسمی `Pfm.RemoveTransaction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionIds` | Array of Object | **Required** | Wire field `transactionIds` (python arg: `transaction_ids`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_transaction(transaction_ids={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "RemoveTransaction", transaction_ids={...})
```

---

### RemoveTransactionTags
اجرای متد رسمی `Pfm.RemoveTransactionTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Object | **Optional** | Wire field `id` (python arg: `id`). |
| `tags` | Array of Object | **Required** | Wire field `tags` (python arg: `tags`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_transaction_tags(id={...}, tags={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "RemoveTransactionTags", id={...}, tags={...})
```

---

### RemoveUserTags
اجرای متد رسمی `Pfm.RemoveUserTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `tags` | Array of Object | **Required** | Wire field `tags` (python arg: `tags`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_user_tags(tags={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "RemoveUserTags", tags={...})
```

---

### ReviveTransaction
اجرای متد رسمی `Pfm.ReviveTransaction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionId` | Object | **Optional** | Wire field `transactionId` (python arg: `transaction_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.revive_transaction(transaction_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "ReviveTransaction", transaction_id={...})
```

---

### SplitTransaction
اجرای متد رسمی `Pfm.SplitTransaction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionId` | Object | **Optional** | Wire field `transactionId` (python arg: `transaction_id`). |
| `units` | Array of Object | **Required** | Wire field `units` (python arg: `units`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `splitTransactionIds`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.split_transaction(transaction_id={...}, units={...})

# ۲. فراخوانی با RPC
result = await app.rpc("pfm", "SplitTransaction", transaction_id={...}, units={...})
```

---

## Pishvaz (ابزارهای بازاریابی پیشواز و صفحات خوش‌آمدگویی)
> شناسه کامل سرویس در شبکه بله: `bale.pishvaz.v1.Pishvaz` — تعداد متدها: **3**

### GetMarketingToolsConfig
اجرای متد رسمی `Pishvaz.GetMarketingToolsConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `inApp, eventBar, dialogListBanner`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_marketing_tools_config()

# ۲. فراخوانی با RPC
result = await app.rpc("pishvaz", "GetMarketingToolsConfig")
```

---

### GetOnboardingPageData
اجرای متد رسمی `Pishvaz.GetOnboardingPageData` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `title, sections`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_onboarding_page_data()

# ۲. فراخوانی با RPC
result = await app.rpc("pishvaz", "GetOnboardingPageData")
```

---

### SetMarketingToolAction
اجرای متد رسمی `Pishvaz.SetMarketingToolAction` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |
| `actionType` | Integer | **Required** | Wire field `actionType` (python arg: `action_type`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_marketing_tool_action(id=12345, action_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("pishvaz", "SetMarketingToolAction", id=12345, action_type=12345)
```

---

## Poll (نظرسنجی، ایجاد، ثبت رای و بستن نظرسنجی)
> شناسه کامل سرویس در شبکه بله: `bale.poll.v1.Poll` — تعداد متدها: **5**

### ClosePoll
اجرای متد رسمی `Poll.ClosePoll` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pollId` | Integer | **Required** | Wire field `pollId` (python arg: `poll_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.close_poll(poll_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("poll", "ClosePoll", poll_id=12345)
```

---

### CreatePoll
اجرای متد رسمی `Poll.CreatePoll` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pollMessage` | Object | **Optional** | Wire field `pollMessage` (python arg: `poll_message`). |
| `createAt` | Integer | **Required** | Wire field `createAt` (python arg: `create_at`). |
| `expeer` | Object | **Optional** | Wire field `expeer` (python arg: `expeer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pollId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_poll(poll_message={...}, create_at=12345, expeer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("poll", "CreatePoll", poll_message={...}, create_at=12345, expeer={...})
```

---

### GetFullPollResult
اجرای متد رسمی `Poll.GetFullPollResult` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pollId` | Integer | **Required** | Wire field `pollId` (python arg: `poll_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fullPollResult`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_full_poll_result(poll_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("poll", "GetFullPollResult", poll_id=12345)
```

---

### GetPollResults
اجرای متد رسمی `Poll.GetPollResults` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pollIds` | Array of Integer | **Required** | Wire field `pollIds` (python arg: `poll_ids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pollResults`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_poll_results(poll_ids=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("poll", "GetPollResults", poll_ids=12345)
```

---

### Vote
اجرای متد رسمی `Poll.Vote` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `pollId` | Integer | **Required** | Wire field `pollId` (python arg: `poll_id`). |
| `isRetract` | Boolean | **Required** | Wire field `isRetract` (python arg: `is_retract`). |
| `voteAt` | Integer | **Required** | Wire field `voteAt` (python arg: `vote_at`). |
| `optionIds` | Array of Integer | **Required** | Wire field `optionIds` (python arg: `option_ids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `pollResult`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.vote(poll_id=12345, is_retract=True, vote_at=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("poll", "Vote", poll_id=12345, is_retract=True, vote_at=12345)
```

---

## Premium (بسته‌های بله ویژه (پرمیوم) و نشان‌های کاربری)
> شناسه کامل سرویس در شبکه بله: `bale.premium.v1.Premium` — تعداد متدها: **7**

### CalculateDiscountedPrice
اجرای متد رسمی `Premium.CalculateDiscountedPrice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `packageId` | Integer | **Required** | Wire field `packageId` (python arg: `package_id`). |
| `couponCode` | String | **Required** | Wire field `couponCode` (python arg: `coupon_code`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `discountedPrice`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.calculate_discounted_price(package_id=12345, coupon_code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("premium", "CalculateDiscountedPrice", package_id=12345, coupon_code="value")
```

---

### GetBadges
اجرای متد رسمی `Premium.GetBadges` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `categories`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_badges()

# ۲. فراخوانی با RPC
result = await app.rpc("premium", "GetBadges")
```

---

### GetPackages
اجرای متد رسمی `Premium.GetPackages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `packages, bundles`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_packages()

# ۲. فراخوانی با RPC
result = await app.rpc("premium", "GetPackages")
```

---

### IsPremium
اجرای متد رسمی `Premium.IsPremium` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |
| `withDetailOption` | Object | **Optional** | Wire field `withDetailOption` (python arg: `with_detail_option`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userStatus`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.is_premium(user_id=12345, with_detail_option={...})

# ۲. فراخوانی با RPC
result = await app.rpc("premium", "IsPremium", user_id=12345, with_detail_option={...})
```

---

### IsPremiumBatch
اجرای متد رسمی `Premium.IsPremiumBatch` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userIds` | Array of Integer | **Required** | Wire field `userIds` (python arg: `user_ids`). |
| `withDetailOption` | Object | **Optional** | Wire field `withDetailOption` (python arg: `with_detail_option`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `usersStatus`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.is_premium_batch(user_ids=12345, with_detail_option={...})

# ۲. فراخوانی با RPC
result = await app.rpc("premium", "IsPremiumBatch", user_ids=12345, with_detail_option={...})
```

---

### PurchasePackage
اجرای متد رسمی `Premium.PurchasePackage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `packageId` | Integer | **Required** | Wire field `packageId` (python arg: `package_id`). |
| `couponCode` | Object | **Optional** | Wire field `couponCode` (python arg: `coupon_code`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `sadadPaymentToken`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.purchase_package(package_id=12345, coupon_code={...})

# ۲. فراخوانی با RPC
result = await app.rpc("premium", "PurchasePackage", package_id=12345, coupon_code={...})
```

---

### SetUserBadge
اجرای متد رسمی `Premium.SetUserBadge` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `badgeId` | Integer | **Required** | Wire field `badgeId` (python arg: `badge_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_user_badge(badge_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("premium", "SetUserBadge", badge_id=12345)
```

---

## Presence (وضعیت آنلاین/آفلاین بودن کاربران و اعضای گروه)
> شناسه کامل سرویس در شبکه بله: `bale.presence.v1.Presence` — تعداد متدها: **11**

### GetContactsPresences
اجرای متد رسمی `Presence.GetContactsPresences` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `limit` | Object | **Optional** | Wire field `limit` (python arg: `limit`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `presences`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_contacts_presences(limit={...})

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "GetContactsPresences", limit={...})
```

---

### GetGroupMembersPresences
اجرای متد رسمی `Presence.GetGroupMembersPresences` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `presences`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_members_presences(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "GetGroupMembersPresences", peer={...})
```

---

### GetGroupOnlineCount
اجرای متد رسمی `Presence.GetGroupOnlineCount` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `count`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_group_online_count(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "GetGroupOnlineCount", peer={...})
```

---

### GetUsersPresence
اجرای متد رسمی `Presence.GetUsersPresence` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userIds` | Array of Integer | **Required** | Wire field `userIds` (python arg: `user_ids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `presences`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_users_presence(user_ids=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "GetUsersPresence", user_ids=12345)
```

---

### SetOnline
اجرای متد رسمی `Presence.SetOnline` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `isOnline` | Boolean | **Required** | Wire field `isOnline` (python arg: `is_online`). |
| `timeout` | Integer | **Required** | Wire field `timeout` (python arg: `timeout`). |
| `deviceType` | Integer | **Required** | Wire field `deviceType` (python arg: `device_type`). |
| `deviceCategory` | Object | **Optional** | Wire field `deviceCategory` (python arg: `device_category`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_online(is_online=True, timeout=12345, device_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "SetOnline", is_online=True, timeout=12345, device_type=12345)
```

---

### StopTyping
اجرای متد رسمی `Presence.StopTyping` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `typingType` | Integer | **Required** | Wire field `typingType` (python arg: `typing_type`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.stop_typing(peer={...}, typing_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "StopTyping", peer={...}, typing_type=12345)
```

---

### SubscribeFromGroupOnline
اجرای متد رسمی `Presence.SubscribeFromGroupOnline` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groups` | Array of Object | **Required** | Wire field `groups` (python arg: `groups`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.subscribe_from_group_online(groups={...})

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "SubscribeFromGroupOnline", groups={...})
```

---

### SubscribeFromOnline
اجرای متد رسمی `Presence.SubscribeFromOnline` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `users` | Array of Object | **Required** | Wire field `users` (python arg: `users`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.subscribe_from_online(users={...})

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "SubscribeFromOnline", users={...})
```

---

### SubscribeToGroupOnline
اجرای متد رسمی `Presence.SubscribeToGroupOnline` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `groups` | Array of Object | **Required** | Wire field `groups` (python arg: `groups`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.subscribe_to_group_online(groups={...})

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "SubscribeToGroupOnline", groups={...})
```

---

### SubscribeToOnline
اجرای متد رسمی `Presence.SubscribeToOnline` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `users` | Array of Object | **Required** | Wire field `users` (python arg: `users`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.subscribe_to_online(users={...})

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "SubscribeToOnline", users={...})
```

---

### Typing
اجرای متد رسمی `Presence.Typing` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |
| `typingType` | Integer | **Required** | Wire field `typingType` (python arg: `typing_type`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.typing(peer={...}, typing_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("presence", "Typing", peer={...}, typing_type=12345)
```

---

## Ramz (مدیریت رمز عبور، تایید دو مرحله‌ای و بازیابی)
> شناسه کامل سرویس در شبکه بله: `bale.ramz.v1.Ramz` — تعداد متدها: **7**

### CheckPassword
اجرای متد رسمی `Ramz.CheckPassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `password` | String | **Required** | Wire field `password` (python arg: `password`). |
| `servicesType` | Integer | **Required** | Wire field `servicesType` (python arg: `services_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.check_password(password="value", services_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ramz", "CheckPassword", password="value", services_type=12345)
```

---

### CheckPasswordSet
اجرای متد رسمی `Ramz.CheckPasswordSet` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `hasSet, isSessionAuthorized`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.check_password_set()

# ۲. فراخوانی با RPC
result = await app.rpc("ramz", "CheckPasswordSet")
```

---

### DeletePassword
اجرای متد رسمی `Ramz.DeletePassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `otp` | Integer | **Required** | Wire field `otp` (python arg: `otp`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.delete_password(otp=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ramz", "DeletePassword", otp=12345)
```

---

### ForgetPassword
اجرای متد رسمی `Ramz.ForgetPassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.forget_password()

# ۲. فراخوانی با RPC
result = await app.rpc("ramz", "ForgetPassword")
```

---

### SendOTP
اجرای متد رسمی `Ramz.SendOTP` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_otp()

# ۲. فراخوانی با RPC
result = await app.rpc("ramz", "SendOTP")
```

---

### SetPassword
اجرای متد رسمی `Ramz.SetPassword` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `password` | String | **Required** | Wire field `password` (python arg: `password`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_password(password="value")

# ۲. فراخوانی با RPC
result = await app.rpc("ramz", "SetPassword", password="value")
```

---

### ValidateOTP
اجرای متد رسمی `Ramz.ValidateOTP` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `otp` | Integer | **Required** | Wire field `otp` (python arg: `otp`). |
| `servicesType` | Integer | **Required** | Wire field `servicesType` (python arg: `services_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `otpValid`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.validate_otp(otp=12345, services_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("ramz", "ValidateOTP", otp=12345, services_type=12345)
```

---

## Recommender (پیشنهاد هوشمند کانال‌ها و گروه‌های مرتبط)
> شناسه کامل سرویس در شبکه بله: `bale.recommender.v1.Recommender` — تعداد متدها: **4**

### GetChannelRecommendations
اجرای متد رسمی `Recommender.GetChannelRecommendations` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `channels`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_recommendations()

# ۲. فراخوانی با RPC
result = await app.rpc("recommender", "GetChannelRecommendations")
```

---

### GetGroupsRecommendation
اجرای متد رسمی `Recommender.GetGroupsRecommendation` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `source` | Integer | **Required** | Wire field `source` (python arg: `source`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `groups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_groups_recommendation(source=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("recommender", "GetGroupsRecommendation", source=12345)
```

---

### GetRelatedChannels
اجرای متد رسمی `Recommender.GetRelatedChannels` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `relatedChannels`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_related_channels(ex_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("recommender", "GetRelatedChannels", ex_peer={...})
```

---

### GetRelatedGroups
اجرای متد رسمی `Recommender.GetRelatedGroups` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `relatedGroups`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_related_groups(ex_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("recommender", "GetRelatedGroups", ex_peer={...})
```

---

## Report (گزارش تخلفات، هرزنامه و محتوای نامناسب)
> شناسه کامل سرویس در شبکه بله: `bale.report.v1.Report` — تعداد متدها: **2**

### ReportDismiss
اجرای متد رسمی `Report.ReportDismiss` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.report_dismiss(ex_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("report", "ReportDismiss", ex_peer={...})
```

---

### ReportInappropriateContent
اجرای متد رسمی `Report.ReportInappropriateContent` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `report` | Object | **Optional** | Wire field `report` (python arg: `report`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.report_inappropriate_content(report={...})

# ۲. فراخوانی با RPC
result = await app.rpc("report", "ReportInappropriateContent", report={...})
```

---

## Sap (سامانه پیوند شاپرک، افزودن کارت و دریافت اطلاعات)
> شناسه کامل سرویس در شبکه بله: `bale.sap.v1.Sap` — تعداد متدها: **16**

### AddDestinationCards
اجرای متد رسمی `Sap.AddDestinationCards` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cards` | Array of Object | **Required** | Wire field `cards` (python arg: `cards`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ids`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_destination_cards(cards={...})

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "AddDestinationCards", cards={...})
```

---

### AddNewCards
اجرای متد رسمی `Sap.AddNewCards` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardInfo` | Array of Object | **Required** | Wire field `cardInfo` (python arg: `card_info`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `cardId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_new_cards(card_info={...})

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "AddNewCards", card_info={...})
```

---

### DeliverOtp
اجرای متد رسمی `Sap.DeliverOtp` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardId` | String | **Required** | Wire field `cardId` (python arg: `card_id`). |
| `destinationPan` | String | **Required** | Wire field `destinationPan` (python arg: `destination_pan`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `accessAddress` | String | **Required** | Wire field `accessAddress` (python arg: `access_address`). |
| `approvalCode` | String | **Required** | Wire field `approvalCode` (python arg: `approval_code`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `isDone`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.deliver_otp(card_id="value", destination_pan="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "DeliverOtp", card_id="value", destination_pan="value", amount=12345)
```

---

### EditCardExpirationDate
اجرای متد رسمی `Sap.EditCardExpirationDate` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardId` | String | **Required** | Wire field `cardId` (python arg: `card_id`). |
| `cardExpDate` | Object | **Optional** | Wire field `cardExpDate` (python arg: `card_exp_date`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_card_expiration_date(card_id="value", card_exp_date={...})

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "EditCardExpirationDate", card_id="value", card_exp_date={...})
```

---

### EnrollNewCard
اجرای متد رسمی `Sap.EnrollNewCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `origin` | Object | **Optional** | Wire field `origin` (python arg: `origin`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactionId, url`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.enroll_new_card(origin={...})

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "EnrollNewCard", origin={...})
```

---

### GetCardInfo
اجرای متد رسمی `Sap.GetCardInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transactionId` | String | **Required** | Wire field `transactionId` (python arg: `transaction_id`). |
| `cardInfo` | Object | **Optional** | Wire field `cardInfo` (python arg: `card_info`). |
| `cardId` | Object | **Optional** | Wire field `cardId` (python arg: `card_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `cardId, maskedPan`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_card_info(transaction_id="value", card_info={...}, card_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "GetCardInfo", transaction_id="value", card_info={...}, card_id={...})
```

---

### GetCards
اجرای متد رسمی `Sap.GetCards` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userCards`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_cards()

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "GetCards")
```

---

### GetDefaultCard
اجرای متد رسمی `Sap.GetDefaultCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `cardId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_default_card()

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "GetDefaultCard")
```

---

### GetDestinationCardInfo
اجرای متد رسمی `Sap.GetDestinationCardInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardId` | String | **Required** | Wire field `cardId` (python arg: `card_id`). |
| `destinationPan` | String | **Required** | Wire field `destinationPan` (python arg: `destination_pan`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `sourceAddress` | String | **Required** | Wire field `sourceAddress` (python arg: `source_address`). |
| `localize` | Integer | **Required** | Wire field `localize` (python arg: `localize`). |
| `targetUserId` | Object | **Optional** | Wire field `targetUserId` (python arg: `target_user_id`). |
| `messageData` | Object | **Optional** | Wire field `messageData` (python arg: `message_data`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `cardHolderName, approvalCode`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_destination_card_info(card_id="value", destination_pan="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "GetDestinationCardInfo", card_id="value", destination_pan="value", amount=12345)
```

---

### GetDestinationCards
اجرای متد رسمی `Sap.GetDestinationCards` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `cards`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_destination_cards()

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "GetDestinationCards")
```

---

### ReactivateApp
اجرای متد رسمی `Sap.ReactivateApp` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `transactionId, reactivationAddress`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.reactivate_app()

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "ReactivateApp")
```

---

### RemoveCard
اجرای متد رسمی `Sap.RemoveCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardId` | String | **Required** | Wire field `cardId` (python arg: `card_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_card(card_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "RemoveCard", card_id="value")
```

---

### RemoveDefaultCard
اجرای متد رسمی `Sap.RemoveDefaultCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_default_card()

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "RemoveDefaultCard")
```

---

### RemoveDestinationCards
اجرای متد رسمی `Sap.RemoveDestinationCards` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ids` | Array of String | **Required** | Wire field `ids` (python arg: `ids`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_destination_cards(ids="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "RemoveDestinationCards", ids="value")
```

---

### SetDefaultCard
اجرای متد رسمی `Sap.SetDefaultCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardId` | String | **Required** | Wire field `cardId` (python arg: `card_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_default_card(card_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "SetDefaultCard", card_id="value")
```

---

### TransferMoneyByCard
اجرای متد رسمی `Sap.TransferMoneyByCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `cardId` | String | **Required** | Wire field `cardId` (python arg: `card_id`). |
| `transferCode` | Integer | **Required** | Wire field `transferCode` (python arg: `transfer_code`). |
| `destinationPan` | String | **Required** | Wire field `destinationPan` (python arg: `destination_pan`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `pin` | String | **Required** | Wire field `pin` (python arg: `pin`). |
| `cvv2` | String | **Required** | Wire field `cvv2` (python arg: `cvv2`). |
| `expiryDate` | String | **Required** | Wire field `expiryDate` (python arg: `expiry_date`). |
| `sourceAddress` | String | **Required** | Wire field `sourceAddress` (python arg: `source_address`). |
| `localize` | Integer | **Required** | Wire field `localize` (python arg: `localize`). |
| `approvalCode` | String | **Required** | Wire field `approvalCode` (python arg: `approval_code`). |
| `encryptedTransferInfo` | Object | **Optional** | Wire field `encryptedTransferInfo` (python arg: `encrypted_transfer_info`). |
| `messageData` | Object | **Optional** | Wire field `messageData` (python arg: `message_data`). |
| `targetUserId` | Object | **Optional** | Wire field `targetUserId` (python arg: `target_user_id`). |
| `description` | Object | **Optional** | Wire field `description` (python arg: `description`). |
| `ramzToken` | Object | **Optional** | Wire field `ramzToken` (python arg: `ramz_token`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `traceNumber, transactionTime`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.transfer_money_by_card(card_id="value", transfer_code=12345, destination_pan="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sap", "TransferMoneyByCard", card_id="value", transfer_code=12345, destination_pan="value")
```

---

## Sarrafi (صرافی بله، سفارش‌گذاری، عمق بازار و کیف‌پول ارزی)
> شناسه کامل سرویس در شبکه بله: `bale.sarrafi.v1.Sarrafi` — تعداد متدها: **9**

### AuthenticateUser
اجرای متد رسمی `Sarrafi.AuthenticateUser` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nationalCode` | String | **Required** | Wire field `nationalCode` (python arg: `national_code`). |
| `accountNumber` | String | **Required** | Wire field `accountNumber` (python arg: `account_number`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.authenticate_user(national_code="value", account_number="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "AuthenticateUser", national_code="value", account_number="value")
```

---

### CreateOrder
اجرای متد رسمی `Sarrafi.CreateOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `symbol` | Integer | **Required** | Wire field `symbol` (python arg: `symbol`). |
| `side` | Integer | **Required** | Wire field `side` (python arg: `side`). |
| `price` | String | **Required** | Wire field `price` (python arg: `price`). |
| `quantity` | String | **Required** | Wire field `quantity` (python arg: `quantity`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.create_order(symbol=12345, side=12345, price="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "CreateOrder", symbol=12345, side=12345, price="value")
```

---

### GetChargeToken
اجرای متد رسمی `Sarrafi.GetChargeToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `currency` | Integer | **Required** | Wire field `currency` (python arg: `currency`). |
| `amount` | String | **Required** | Wire field `amount` (python arg: `amount`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `tokenUrl`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_charge_token(currency=12345, amount="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "GetChargeToken", currency=12345, amount="value")
```

---

### GetDepth
اجرای متد رسمی `Sarrafi.GetDepth` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `symbol` | Integer | **Required** | Wire field `symbol` (python arg: `symbol`). |
| `limit` | Integer | **Optional** | Wire field `limit` (python arg: `limit`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `marketDepth`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_depth(symbol=12345, limit=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "GetDepth", symbol=12345, limit=12345)
```

---

### GetOrder
اجرای متد رسمی `Sarrafi.GetOrder` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `orderId` | String | **Required** | Wire field `orderId` (python arg: `order_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `order, trades`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_order(order_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "GetOrder", order_id="value")
```

---

### GetOrders
اجرای متد رسمی `Sarrafi.GetOrders` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `orders, limit, offset`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_orders()

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "GetOrders")
```

---

### GetSession
اجرای متد رسمی `Sarrafi.GetSession` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `symbol` | Integer | **Required** | Wire field `symbol` (python arg: `symbol`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `openAt, closeAt, openingPrice, brokerFeePercentage, marketFeePercentage, priceTolerancePercentage, quantityTickSize`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_session(symbol=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "GetSession", symbol=12345)
```

---

### GetTickers
اجرای متد رسمی `Sarrafi.GetTickers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `usd, euro`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_tickers()

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "GetTickers")
```

---

### GetWallet
اجرای متد رسمی `Sarrafi.GetWallet` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `wallet`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_wallet()

# ۲. فراخوانی با RPC
result = await app.rpc("sarrafi", "GetWallet")
```

---

## Scheduler (زمان‌بندی ارسال پیام‌ها و تسک‌های آینده)
> شناسه کامل سرویس در شبکه بله: `bale.schedule.v1.Scheduler` — تعداد متدها: **6**

### ExecuteTaskNow
اجرای متد رسمی `Scheduler.ExecuteTaskNow` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `taskID` | Integer | **Required** | Wire field `taskID` (python arg: `task_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.execute_task_now(task_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("scheduler", "ExecuteTaskNow", task_id=12345)
```

---

### ListTasks
اجرای متد رسمی `Scheduler.ListTasks` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `type` | Integer | **Required** | Wire field `type` (python arg: `type`). |
| `status` | Integer | **Required** | Wire field `status` (python arg: `status`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `tasks`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.list_tasks(ex_peer={...}, type=12345, status=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("scheduler", "ListTasks", ex_peer={...}, type=12345, status=12345)
```

---

### PeersWithScheduleTask
اجرای متد رسمی `Scheduler.PeersWithScheduleTask` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `exPeer`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.peers_with_schedule_task()

# ۲. فراخوانی با RPC
result = await app.rpc("scheduler", "PeersWithScheduleTask")
```

---

### ReScheduleTask
اجرای متد رسمی `Scheduler.ReScheduleTask` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `taskID` | Integer | **Required** | Wire field `taskID` (python arg: `task_id`). |
| `scheduledAt` | Integer | **Optional** | Wire field `scheduledAt` (python arg: `scheduled_at`). |
| `payload` | Object | **Optional** | Wire field `payload` (python arg: `payload`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.re_schedule_task(task_id=12345, scheduled_at=12345, payload={...})

# ۲. فراخوانی با RPC
result = await app.rpc("scheduler", "ReScheduleTask", task_id=12345, scheduled_at=12345, payload={...})
```

---

### ScheduleTask
اجرای متد رسمی `Scheduler.ScheduleTask` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `scheduledAt` | Integer | **Optional** | Wire field `scheduledAt` (python arg: `scheduled_at`). |
| `payload` | Object | **Optional** | Wire field `payload` (python arg: `payload`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `taskId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.schedule_task(ex_peer={...}, scheduled_at=12345, payload={...})

# ۲. فراخوانی با RPC
result = await app.rpc("scheduler", "ScheduleTask", ex_peer={...}, scheduled_at=12345, payload={...})
```

---

### UnScheduleTask
اجرای متد رسمی `Scheduler.UnScheduleTask` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `taskIDs` | Array of Integer | **Required** | Wire field `taskIDs` (python arg: `task_ids`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `failedTaskIDs`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.un_schedule_task(task_ids=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("scheduler", "UnScheduleTask", task_ids=12345)
```

---

## Search (جستجوی جامع در پیام‌ها، چت‌ها، بازار و مخاطبین)
> شناسه کامل سرویس در شبکه بله: `bale.search.v1.Search` — تعداد متدها: **12**

### RecommendPeer
اجرای متد رسمی `Search.RecommendPeer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeerType` | Integer | **Required** | Wire field `exPeerType` (python arg: `ex_peer_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `peer`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.recommend_peer(ex_peer_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("search", "RecommendPeer", ex_peer_type=12345)
```

---

### SearchContent
اجرای متد رسمی `Search.SearchContent` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `contentType` | Integer | **Required** | Wire field `contentType` (python arg: `content_type`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `contentResults, loadMoreState, resultCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_content(query={...}, content_type=12345, load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchContent", query={...}, content_type=12345, load_more_state={...})
```

---

### SearchDialog
اجرای متد رسمی `Search.SearchDialog` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `dialogResults`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_dialog(query={...})

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchDialog", query={...})
```

---

### SearchMarket
اجرای متد رسمی `Search.SearchMarket` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `withCategory` | Object | **Optional** | Wire field `withCategory` (python arg: `with_category`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `marketResults, category, loadMoreState, resultCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_market(query={...}, with_category={...}, load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchMarket", query={...}, with_category={...}, load_more_state={...})
```

---

### SearchMarketPopular
اجرای متد رسمی `Search.SearchMarketPopular` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `popularResults`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_market_popular()

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchMarketPopular")
```

---

### SearchMedia
اجرای متد رسمی `Search.SearchMedia` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `date` | Object | **Optional** | Wire field `date` (python arg: `date`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |
| `loadMode` | Integer | **Required** | Wire field `loadMode` (python arg: `load_mode`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `searchResults, users, groups, loadMoreState, userOutPeers, groupOutPeers, resultCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_media(query={...}, date={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchMedia", query={...}, date={...}, optimizations=12345)
```

---

### SearchMembers
اجرای متد رسمی `Search.SearchMembers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |
| `users` | Array of Object | **Required** | Wire field `users` (python arg: `users`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `users, loadMoreState`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_members(query={...}, ex_peer={...}, load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchMembers", query={...}, ex_peer={...}, load_more_state={...})
```

---

### SearchMessageMore
اجرای متد رسمی `Search.SearchMessageMore` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `searchResults, users, groups, loadMoreState, userOutPeers, groupOutPeers, resultCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_message_more(load_more_state={...}, query={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchMessageMore", load_more_state={...}, query={...}, optimizations=12345)
```

---

### SearchMessages
اجرای متد رسمی `Search.SearchMessages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `searchResults, users, groups, loadMoreState, userOutPeers, groupOutPeers, resultCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_messages(query={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchMessages", query={...}, optimizations=12345)
```

---

### SearchPeer
اجرای متد رسمی `Search.SearchPeer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Array of Object | **Required** | Wire field `query` (python arg: `query`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `searchResults, users, groups, userPeers, groupPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_peer(query={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchPeer", query={...}, optimizations=12345)
```

---

### SearchProduct
اجرای متد رسمی `Search.SearchProduct` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `query` | Object | **Optional** | Wire field `query` (python arg: `query`). |
| `loadMoreState` | Object | **Optional** | Wire field `loadMoreState` (python arg: `load_more_state`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `productResults, loadMoreState, resultCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_product(query={...}, load_more_state={...})

# ۲. فراخوانی با RPC
result = await app.rpc("search", "SearchProduct", query={...}, load_more_state={...})
```

---

### UpdateSearchContentClick
اجرای متد رسمی `Search.UpdateSearchContentClick` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |
| `searchTab` | Integer | **Required** | Wire field `searchTab` (python arg: `search_tab`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.update_search_content_click(message_id={...}, search_tab=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("search", "UpdateSearchContentClick", message_id={...}, search_tab=12345)
```

---

## SharedMediaService (رسانه‌های اشتراکی و تاریخچه فایل‌های چت)
> شناسه کامل سرویس در شبکه بله: `bale.shared_media.v1.SharedMediaService` — تعداد متدها: **2**

### GetActiveSharedMedia
اجرای متد رسمی `SharedMediaService.GetActiveSharedMedia` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `activeTab`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_active_shared_media(ex_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("sharedmediaservice", "GetActiveSharedMedia", ex_peer={...})
```

---

### LoadMedia
اجرای متد رسمی `SharedMediaService.LoadMedia` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `date` | Object | **Optional** | Wire field `date` (python arg: `date`). |
| `contentType` | Integer | **Required** | Wire field `contentType` (python arg: `content_type`). |
| `loadMode` | Integer | **Required** | Wire field `loadMode` (python arg: `load_mode`). |
| `minimumResults` | Integer | **Required** | Wire field `minimumResults` (python arg: `minimum_results`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `mediaResults`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_media(ex_peer={...}, date={...}, content_type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("sharedmediaservice", "LoadMedia", ex_peer={...}, date={...}, content_type=12345)
```

---

## Story (استوری‌ها، ارسال، ری‌اکشن، بازدیدها و تنظیمات حریم)
> شناسه کامل سرویس در شبکه بله: `bale.story.v1.Story` — تعداد متدها: **24**

### AddBotStory
اجرای متد رسمی `Story.AddBotStory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `mediaStory` | Object | **Optional** | Wire field `mediaStory` (python arg: `media_story`). |
| `textStory` | Object | **Optional** | Wire field `textStory` (python arg: `text_story`). |
| `tagIds` | Array of Integer | **Required** | Wire field `tagIds` (python arg: `tag_ids`). |
| `expirationType` | Integer | **Required** | Wire field `expirationType` (python arg: `expiration_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `storyId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_bot_story(ex_peer={...}, media_story={...}, text_story={...})

# ۲. فراخوانی با RPC
result = await app.rpc("story", "AddBotStory", ex_peer={...}, media_story={...}, text_story={...})
```

---

### AddChannelStory
اجرای متد رسمی `Story.AddChannelStory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `mediaStory` | Object | **Optional** | Wire field `mediaStory` (python arg: `media_story`). |
| `hasReply` | Boolean | **Required** | Wire field `hasReply` (python arg: `has_reply`). |
| `tagIds` | Array of Integer | **Required** | Wire field `tagIds` (python arg: `tag_ids`). |
| `expirationType` | Integer | **Required** | Wire field `expirationType` (python arg: `expiration_type`). |
| `textStory` | Object | **Optional** | Wire field `textStory` (python arg: `text_story`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `storyId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_channel_story(ex_peer={...}, media_story={...}, has_reply=True)

# ۲. فراخوانی با RPC
result = await app.rpc("story", "AddChannelStory", ex_peer={...}, media_story={...}, has_reply=True)
```

---

### AddStory
اجرای متد رسمی `Story.AddStory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `mediaStory` | Object | **Optional** | Wire field `mediaStory` (python arg: `media_story`). |
| `textStory` | Object | **Optional** | Wire field `textStory` (python arg: `text_story`). |
| `tagIds` | Array of Integer | **Required** | Wire field `tagIds` (python arg: `tag_ids`). |
| `expirationType` | Integer | **Required** | Wire field `expirationType` (python arg: `expiration_type`). |
| `exceptionType` | Integer | **Required** | Wire field `exceptionType` (python arg: `exception_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `storyId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_story(media_story={...}, text_story={...}, tag_ids=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("story", "AddStory", media_story={...}, text_story={...}, tag_ids=12345)
```

---

### CanAddBotStory
اجرای متد رسمی `Story.CanAddBotStory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botUserId` | Integer | **Required** | Wire field `botUserId` (python arg: `bot_user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `canAddBotStory`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.can_add_bot_story(bot_user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("story", "CanAddBotStory", bot_user_id=12345)
```

---

### CheckLinkValidity
اجرای متد رسمی `Story.CheckLinkValidity` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |
| `link` | String | **Required** | Wire field `link` (python arg: `link`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.check_link_validity(ex_peer={...}, link="value")

# ۲. فراخوانی با RPC
result = await app.rpc("story", "CheckLinkValidity", ex_peer={...}, link="value")
```

---

### GetAllStories
اجرای متد رسمی `Story.GetAllStories` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userStories, channelStories, botStories, popularityList`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_all_stories()

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetAllStories")
```

---

### GetBotStories
اجرای متد رسمی `Story.GetBotStories` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `result, popularityList`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bot_stories()

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetBotStories")
```

---

### GetChannelStories
اجرای متد رسمی `Story.GetChannelStories` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `result, popularityList`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_channel_stories()

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetChannelStories")
```

---

### GetDefaultStoryBackgrounds
اجرای متد رسمی `Story.GetDefaultStoryBackgrounds` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `defaultStoryBackgrounds`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_default_story_backgrounds()

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetDefaultStoryBackgrounds")
```

---

### GetMostPopularStories
اجرای متد رسمی `Story.GetMostPopularStories` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `getSpecialStories` | Object | **Optional** | Wire field `getSpecialStories` (python arg: `get_special_stories`). |
| `optimization` | Integer | **Required** | Wire field `optimization` (python arg: `optimization`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `result, popularityList`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_most_popular_stories(get_special_stories={...}, optimization=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetMostPopularStories", get_special_stories={...}, optimization=12345)
```

---

### GetStories
اجرای متد رسمی `Story.GetStories` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `getUnmutual` | Object | **Optional** | Wire field `getUnmutual` (python arg: `get_unmutual`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `result, popularityList`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_stories(get_unmutual={...})

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetStories", get_unmutual={...})
```

---

### GetStoriesByList
اجرای متد رسمی `Story.GetStoriesByList` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `exPeers` | Array of Object | **Required** | Wire field `exPeers` (python arg: `ex_peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userStories, channelStories, botStories`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_stories_by_list(ex_peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetStoriesByList", ex_peers={...})
```

---

### GetStoryById
اجرای متد رسمی `Story.GetStoryById` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `storyId` | String | **Required** | Wire field `storyId` (python arg: `story_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `result, channelStoryResult, botStoryResult`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_story_by_id(story_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetStoryById", story_id="value")
```

---

### GetStoryReactionEmojis
اجرای متد رسمی `Story.GetStoryReactionEmojis` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `emojis`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_story_reaction_emojis()

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetStoryReactionEmojis")
```

---

### GetStoryTags
اجرای متد رسمی `Story.GetStoryTags` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `tags`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_story_tags()

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetStoryTags")
```

---

### GetStoryWidgets
اجرای متد رسمی `Story.GetStoryWidgets` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `storyId` | String | **Required** | Wire field `storyId` (python arg: `story_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `widgets`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_story_widgets(story_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetStoryWidgets", story_id="value")
```

---

### GetUserPrivacyConfig
اجرای متد رسمی `Story.GetUserPrivacyConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `result`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_privacy_config()

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetUserPrivacyConfig")
```

---

### GetUserStoryConfig
اجرای متد رسمی `Story.GetUserStoryConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `key` | Array of Integer | **Required** | Wire field `key` (python arg: `key`). |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `config`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_story_config(key=12345, ex_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetUserStoryConfig", key=12345, ex_peer={...})
```

---

### GetViewers
اجرای متد رسمی `Story.GetViewers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `storyId` | String | **Required** | Wire field `storyId` (python arg: `story_id`). |
| `pagination` | Object | **Optional** | Wire field `pagination` (python arg: `pagination`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `viewers, viewCount, likeCount, linkClickCount, emojiCount, restoryCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_viewers(story_id="value", pagination={...})

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetViewers", story_id="value", pagination={...})
```

---

### GetViewersCount
اجرای متد رسمی `Story.GetViewersCount` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `storyId` | String | **Required** | Wire field `storyId` (python arg: `story_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `viewCount, likeCount, linkClickCount, emojiCount, restoryCount`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_viewers_count(story_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("story", "GetViewersCount", story_id="value")
```

---

### ReactToStory
اجرای متد رسمی `Story.ReactToStory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `storyId` | String | **Required** | Wire field `storyId` (python arg: `story_id`). |
| `reaction` | String | **Required** | Wire field `reaction` (python arg: `reaction`). |
| `type` | Integer | **Required** | Wire field `type` (python arg: `type`). |
| `reactionType` | Integer | **Required** | Wire field `reactionType` (python arg: `reaction_type`). |
| `reactionText` | Object | **Optional** | Wire field `reactionText` (python arg: `reaction_text`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.react_to_story(story_id="value", reaction="value", type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("story", "ReactToStory", story_id="value", reaction="value", type=12345)
```

---

### RemoveStory
اجرای متد رسمی `Story.RemoveStory` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `storyId` | String | **Required** | Wire field `storyId` (python arg: `story_id`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_story(story_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("story", "RemoveStory", story_id="value")
```

---

### SetUserPrivacyConfig
اجرای متد رسمی `Story.SetUserPrivacyConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `config` | Object | **Optional** | Wire field `config` (python arg: `config`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_user_privacy_config(config={...})

# ۲. فراخوانی با RPC
result = await app.rpc("story", "SetUserPrivacyConfig", config={...})
```

---

### SetUserStoryConfig
اجرای متد رسمی `Story.SetUserStoryConfig` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `setType` | Integer | **Required** | Wire field `setType` (python arg: `set_type`). |
| `config` | Object | **Optional** | Wire field `config` (python arg: `config`). |
| `exPeer` | Object | **Optional** | Wire field `exPeer` (python arg: `ex_peer`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_user_story_config(set_type=12345, config={...}, ex_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("story", "SetUserStoryConfig", set_type=12345, config={...}, ex_peer={...})
```

---

## Timche (فروشگاه تیمچه و بررسی محصولات بات‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.timche.v1.Timche` — تعداد متدها: **5**

### AskBotReviewCallback
اجرای متد رسمی `Timche.AskBotReviewCallback` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botId` | Integer | **Required** | Wire field `botId` (python arg: `bot_id`). |
| `payload` | String | **Required** | Wire field `payload` (python arg: `payload`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.ask_bot_review_callback(bot_id=12345, payload="value")

# ۲. فراخوانی با RPC
result = await app.rpc("timche", "AskBotReviewCallback", bot_id=12345, payload="value")
```

---

### GetBotPage
اجرای متد رسمی `Timche.GetBotPage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botId` | Integer | **Required** | Wire field `botId` (python arg: `bot_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `name, nickname, activeUsers, averageRating, description, intro, avatar, imageLinks`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_bot_page(bot_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("timche", "GetBotPage", bot_id=12345)
```

---

### GetHomePage
اجرای متد رسمی `Timche.GetHomePage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `sections`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_home_page()

# ۲. فراخوانی با RPC
result = await app.rpc("timche", "GetHomePage")
```

---

### GetSectionPage
اجرای متد رسمی `Timche.GetSectionPage` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `sectionId` | Integer | **Required** | Wire field `sectionId` (python arg: `section_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `sectionId, sectionName, bots`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_section_page(section_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("timche", "GetSectionPage", section_id=12345)
```

---

### SubmitReview
اجرای متد رسمی `Timche.SubmitReview` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `botId` | Integer | **Required** | Wire field `botId` (python arg: `bot_id`). |
| `rating` | Object | **Optional** | Wire field `rating` (python arg: `rating`). |
| `comment` | Object | **Optional** | Wire field `comment` (python arg: `comment`). |
| `payload` | Object | **Optional** | Wire field `payload` (python arg: `payload`). |
| `origin` | Integer | **Required** | Wire field `origin` (python arg: `origin`). |
| `language` | Object | **Optional** | Wire field `language` (python arg: `language`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `shouldAskBaleReview, baleReviewText`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.submit_review(bot_id=12345, rating={...}, comment={...})

# ۲. فراخوانی با RPC
result = await app.rpc("timche", "SubmitReview", bot_id=12345, rating={...}, comment={...})
```

---

## TLDR (پیش‌نمایش هوشمند لینک‌ها و خلاصه‌سازی با AI)
> شناسه کامل سرویس در شبکه بله: `bale.tldr.v1.TLDR` — تعداد متدها: **2**

### GetLinkPreview
اجرای متد رسمی `TLDR.GetLinkPreview` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `url` | String | **Required** | Wire field `url` (python arg: `url`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `title, description, images`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_link_preview(url="value")

# ۲. فراخوانی با RPC
result = await app.rpc("tldr", "GetLinkPreview", url="value")
```

---

### GetLinkSummary
اجرای متد رسمی `TLDR.GetLinkSummary` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `url` | String | **Required** | Wire field `url` (python arg: `url`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `summary`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_link_summary(url="value")

# ۲. فراخوانی با RPC
result = await app.rpc("tldr", "GetLinkSummary", url="value")
```

---

## TopPeer (گفتگوهای برتر و اولویت‌دار کاربر)
> شناسه کامل سرویس در شبکه بله: `bale.top_peer.v1.TopPeer` — تعداد متدها: **2**

### GetTopPeer
اجرای متد رسمی `TopPeer.GetTopPeer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `topPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_top_peer()

# ۲. فراخوانی با RPC
result = await app.rpc("toppeer", "GetTopPeer")
```

---

### RemovePeer
اجرای متد رسمی `TopPeer.RemovePeer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `isRemoved`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_peer(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("toppeer", "RemovePeer", peer={...})
```

---

## AI (سرویس ترنسکریپت و تعامل با هوش مصنوعی)
> شناسه کامل سرویس در شبکه بله: `bale.turing.v1.AI` — تعداد متدها: **2**

### GetTranscript
اجرای متد رسمی `AI.GetTranscript` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `voice` | Object | **Optional** | Wire field `voice` (python arg: `voice`). |
| `outPeer` | Object | **Optional** | Wire field `outPeer` (python arg: `out_peer`). |
| `messageId` | Object | **Optional** | Wire field `messageId` (python arg: `message_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `mustWait, downloadSource`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_transcript(voice={...}, out_peer={...}, message_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ai", "GetTranscript", voice={...}, out_peer={...}, message_id={...})
```

---

### SendEvent
اجرای متد رسمی `AI.SendEvent` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `transcriptReactionEvent` | Object | **Optional** | Wire field `transcriptReactionEvent` (python arg: `transcript_reaction_event`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.send_event(transcript_reaction_event={...})

# ۲. فراخوانی با RPC
result = await app.rpc("ai", "SendEvent", transcript_reaction_event={...})
```

---

## Users (پروفایل، مسدودسازی، کارت‌های پیش‌فرض و مخاطبین)
> شناسه کامل سرویس در شبکه بله: `bale.users.v1.Users` — تعداد متدها: **36**

### AddCard
اجرای متد رسمی `Users.AddCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `bankCode` | String | **Required** | Wire field `bankCode` (python arg: `bank_code`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_card(bank_code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "AddCard", bank_code="value")
```

---

### AddContact
اجرای متد رسمی `Users.AddContact` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `uid` | Integer | **Required** | Wire field `uid` (python arg: `uid`). |
| `accessHash` | Integer | **Required** | Wire field `accessHash` (python arg: `access_hash`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_contact(uid=12345, access_hash=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "AddContact", uid=12345, access_hash=12345)
```

---

### BlockUser
اجرای متد رسمی `Users.BlockUser` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.block_user(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "BlockUser", peer={...})
```

---

### ChangeDefaultCardNumber
اجرای متد رسمی `Users.ChangeDefaultCardNumber` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `defaultCardNumber` | Object | **Optional** | Wire field `defaultCardNumber` (python arg: `default_card_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_default_card_number(default_card_number={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "ChangeDefaultCardNumber", default_card_number={...})
```

---

### ChangePhoneNumber
اجرای متد رسمی `Users.ChangePhoneNumber` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phoneNumber` | Integer | **Required** | Wire field `phoneNumber` (python arg: `phone_number`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.change_phone_number(phone_number=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "ChangePhoneNumber", phone_number=12345)
```

---

### CheckNickName
اجرای متد رسمی `Users.CheckNickName` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nickname` | String | **Required** | Wire field `nickname` (python arg: `nickname`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `value`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.check_nick_name(nickname="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "CheckNickName", nickname="value")
```

---

### ConfirmPhoneNumber
اجرای متد رسمی `Users.ConfirmPhoneNumber` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `code` | String | **Required** | Wire field `code` (python arg: `code`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.confirm_phone_number(code="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "ConfirmPhoneNumber", code="value")
```

---

### EditAbout
اجرای متد رسمی `Users.EditAbout` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `about` | Object | **Optional** | Wire field `about` (python arg: `about`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_about(about={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditAbout", about={...})
```

---

### EditAvatar
اجرای متد رسمی `Users.EditAvatar` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `fileLocation` | Object | **Optional** | Wire field `fileLocation` (python arg: `file_location`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `avatar, seq, state`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_avatar(file_location={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditAvatar", file_location={...})
```

---

### EditBirthDate
اجرای متد رسمی `Users.EditBirthDate` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `date` | Integer | **Required** | Wire field `date` (python arg: `date`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_birth_date(date=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditBirthDate", date=12345)
```

---

### EditMyPreferredLanguages
اجرای متد رسمی `Users.EditMyPreferredLanguages` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `preferredLanguages` | Array of String | **Required** | Wire field `preferredLanguages` (python arg: `preferred_languages`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_my_preferred_languages(preferred_languages="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditMyPreferredLanguages", preferred_languages="value")
```

---

### EditMyTimeZone
اجرای متد رسمی `Users.EditMyTimeZone` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `tz` | String | **Required** | Wire field `tz` (python arg: `tz`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_my_time_zone(tz="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditMyTimeZone", tz="value")
```

---

### EditName
اجرای متد رسمی `Users.EditName` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_name(name="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditName", name="value")
```

---

### EditNickName
اجرای متد رسمی `Users.EditNickName` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nickname` | Object | **Optional** | Wire field `nickname` (python arg: `nickname`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_nick_name(nickname={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditNickName", nickname={...})
```

---

### EditSex
اجرای متد رسمی `Users.EditSex` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `sex` | Integer | **Required** | Wire field `sex` (python arg: `sex`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_sex(sex=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditSex", sex=12345)
```

---

### EditUserLocalName
اجرای متد رسمی `Users.EditUserLocalName` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `uid` | Integer | **Required** | Wire field `uid` (python arg: `uid`). |
| `accessHash` | Integer | **Required** | Wire field `accessHash` (python arg: `access_hash`). |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_user_local_name(uid=12345, access_hash=12345, name="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "EditUserLocalName", uid=12345, access_hash=12345, name="value")
```

---

### GetContacts
اجرای متد رسمی `Users.GetContacts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `contactsHash` | String | **Required** | Wire field `contactsHash` (python arg: `contacts_hash`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `users, isNotChanged, userPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_contacts(contacts_hash="value", optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "GetContacts", contacts_hash="value", optimizations=12345)
```

---

### GetFullUser
اجرای متد رسمی `Users.GetFullUser` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fullUser`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_full_user(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "GetFullUser", peer={...})
```

---

### GetUserFullPrivacy
اجرای متد رسمی `Users.GetUserFullPrivacy` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `privacy`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_full_privacy(user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "GetUserFullPrivacy", user_id=12345)
```

---

### GetUserPrivacyStatus
اجرای متد رسمی `Users.GetUserPrivacyStatus` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |
| `type` | Integer | **Required** | Wire field `type` (python arg: `type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `status`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_user_privacy_status(user_id=12345, type=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "GetUserPrivacyStatus", user_id=12345, type=12345)
```

---

### GetUsersDefaultCardNumber
اجرای متد رسمی `Users.GetUsersDefaultCardNumber` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userId` | Array of Integer | **Required** | Wire field `userId` (python arg: `user_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `defaultCardNo`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_users_default_card_number(user_id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "GetUsersDefaultCardNumber", user_id=12345)
```

---

### ImportContacts
اجرای متد رسمی `Users.ImportContacts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `phones` | Array of Object | **Required** | Wire field `phones` (python arg: `phones`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `users, seq, state, userPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.import_contacts(phones={...}, optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "ImportContacts", phones={...}, optimizations=12345)
```

---

### IsNameAllowed
اجرای متد رسمی `Users.IsNameAllowed` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | String | **Required** | Wire field `name` (python arg: `name`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `value`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.is_name_allowed(name="value")

# ۲. فراخوانی با RPC
result = await app.rpc("users", "IsNameAllowed", name="value")
```

---

### LoadAvatars
اجرای متد رسمی `Users.LoadAvatars` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `avatars`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_avatars(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "LoadAvatars", peer={...})
```

---

### LoadBlockedUsers
اجرای متد رسمی `Users.LoadBlockedUsers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `userPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_blocked_users()

# ۲. فراخوانی با RPC
result = await app.rpc("users", "LoadBlockedUsers")
```

---

### LoadFullUsers
اجرای متد رسمی `Users.LoadFullUsers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userPeers` | Array of Object | **Required** | Wire field `userPeers` (python arg: `user_peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fullUsers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_full_users(user_peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "LoadFullUsers", user_peers={...})
```

---

### LoadFullUsersSequentially
اجرای متد رسمی `Users.LoadFullUsersSequentially` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userPeers` | Array of Object | **Required** | Wire field `userPeers` (python arg: `user_peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fullUsers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_full_users_sequentially(user_peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "LoadFullUsersSequentially", user_peers={...})
```

---

### LoadUsers
اجرای متد رسمی `Users.LoadUsers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peers` | Array of Object | **Required** | Wire field `peers` (python arg: `peers`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `users`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_users(peers={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "LoadUsers", peers={...})
```

---

### NotifyAboutDeviceInfo
اجرای متد رسمی `Users.NotifyAboutDeviceInfo` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `preferredLanguages` | Array of String | **Required** | Wire field `preferredLanguages` (python arg: `preferred_languages`). |
| `timeZone` | Object | **Optional** | Wire field `timeZone` (python arg: `time_zone`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.notify_about_device_info(preferred_languages="value", time_zone={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "NotifyAboutDeviceInfo", preferred_languages="value", time_zone={...})
```

---

### RemoveAvatar
اجرای متد رسمی `Users.RemoveAvatar` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `avaterId` | Object | **Optional** | Wire field `avaterId` (python arg: `avater_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_avatar(avater_id={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "RemoveAvatar", avater_id={...})
```

---

### RemoveContact
اجرای متد رسمی `Users.RemoveContact` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `uid` | Integer | **Required** | Wire field `uid` (python arg: `uid`). |
| `accessHash` | Integer | **Required** | Wire field `accessHash` (python arg: `access_hash`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_contact(uid=12345, access_hash=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "RemoveContact", uid=12345, access_hash=12345)
```

---

### RemoveDefaultCardNumber
اجرای متد رسمی `Users.RemoveDefaultCardNumber` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_default_card_number()

# ۲. فراخوانی با RPC
result = await app.rpc("users", "RemoveDefaultCardNumber")
```

---

### ResetContacts
اجرای متد رسمی `Users.ResetContacts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.reset_contacts()

# ۲. فراخوانی با RPC
result = await app.rpc("users", "ResetContacts")
```

---

### SearchContacts
اجرای متد رسمی `Users.SearchContacts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `request` | String | **Required** | Wire field `request` (python arg: `request`). |
| `optimizations` | Array of Integer | **Required** | Wire field `optimizations` (python arg: `optimizations`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `users, userPeers, groups, groupPeers`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.search_contacts(request="value", optimizations=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "SearchContacts", request="value", optimizations=12345)
```

---

### SetUserPrivacyStatus
اجرای متد رسمی `Users.SetUserPrivacyStatus` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `userId` | Integer | **Required** | Wire field `userId` (python arg: `user_id`). |
| `type` | Integer | **Required** | Wire field `type` (python arg: `type`). |
| `status` | Integer | **Required** | Wire field `status` (python arg: `status`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.set_user_privacy_status(user_id=12345, type=12345, status=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("users", "SetUserPrivacyStatus", user_id=12345, type=12345, status=12345)
```

---

### UnblockUser
اجرای متد رسمی `Users.UnblockUser` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `peer` | Object | **Optional** | Wire field `peer` (python arg: `peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.unblock_user(peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("users", "UnblockUser", peer={...})
```

---

## Configs (پیکربندی‌ها، پارامترهای کلاینت و آپدیت‌ها)
> شناسه کامل سرویس در شبکه بله: `bale.v1.Configs` — تعداد متدها: **3**

### EditParameter
اجرای متد رسمی `Configs.EditParameter` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `key` | String | **Required** | Wire field `key` (python arg: `key`). |
| `value` | Object | **Optional** | Wire field `value` (python arg: `value`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.edit_parameter(key="value", value={...})

# ۲. فراخوانی با RPC
result = await app.rpc("configs", "EditParameter", key="value", value={...})
```

---

### GetInAppUpdate
اجرای متد رسمی `Configs.GetInAppUpdate` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `fileId, accessHash, fileSize`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_in_app_update()

# ۲. فراخوانی با RPC
result = await app.rpc("configs", "GetInAppUpdate")
```

---

### GetParameters
اجرای متد رسمی `Configs.GetParameters` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `parameters`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_parameters()

# ۲. فراخوانی با RPC
result = await app.rpc("configs", "GetParameters")
```

---

## Images (استیکرها، بسته‌ها و گیف‌های متحرک)
> شناسه کامل سرویس در شبکه بله: `bale.v1.Images` — تعداد متدها: **10**

### AddGif
اجرای متد رسمی `Images.AddGif` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `gif` | Object | **Optional** | Wire field `gif` (python arg: `gif`). |
| `thumb` | Bytes | **Required** | Wire field `thumb` (python arg: `thumb`). |
| `mimeType` | Object | **Optional** | Wire field `mimeType` (python arg: `mime_type`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_gif(gif={...}, thumb="value", mime_type={...})

# ۲. فراخوانی با RPC
result = await app.rpc("images", "AddGif", gif={...}, thumb="value", mime_type={...})
```

---

### AddStickerCollection
اجرای متد رسمی `Images.AddStickerCollection` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |
| `accessHash` | Integer | **Required** | Wire field `accessHash` (python arg: `access_hash`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `collections, seq, state`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_sticker_collection(id=12345, access_hash=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("images", "AddStickerCollection", id=12345, access_hash=12345)
```

---

### AddStickerPack
اجرای متد رسمی `Images.AddStickerPack` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.add_sticker_pack(id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("images", "AddStickerPack", id=12345)
```

---

### GetSavedGifs
اجرای متد رسمی `Images.GetSavedGifs` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `offset` | Object | **Optional** | Wire field `offset` (python arg: `offset`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `gifs, offset`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_saved_gifs(offset={...})

# ۲. فراخوانی با RPC
result = await app.rpc("images", "GetSavedGifs", offset={...})
```

---

### LoadOwnStickers
اجرای متد رسمی `Images.LoadOwnStickers` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `offset` | Object | **Optional** | Wire field `offset` (python arg: `offset`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `ownStickers, offset`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_own_stickers(offset={...})

# ۲. فراخوانی با RPC
result = await app.rpc("images", "LoadOwnStickers", offset={...})
```

---

### LoadStickerCollection
اجرای متد رسمی `Images.LoadStickerCollection` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |
| `accessHash` | Integer | **Required** | Wire field `accessHash` (python arg: `access_hash`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `collection`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.load_sticker_collection(id=12345, access_hash=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("images", "LoadStickerCollection", id=12345, access_hash=12345)
```

---

### RemoveGif
اجرای متد رسمی `Images.RemoveGif` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `gif` | Object | **Optional** | Wire field `gif` (python arg: `gif`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_gif(gif={...})

# ۲. فراخوانی با RPC
result = await app.rpc("images", "RemoveGif", gif={...})
```

---

### RemoveStickerCollection
اجرای متد رسمی `Images.RemoveStickerCollection` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |
| `accessHash` | Integer | **Required** | Wire field `accessHash` (python arg: `access_hash`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `collections, seq, state`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_sticker_collection(id=12345, access_hash=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("images", "RemoveStickerCollection", id=12345, access_hash=12345)
```

---

### RemoveStickerPack
اجرای متد رسمی `Images.RemoveStickerPack` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | **Required** | Wire field `id` (python arg: `id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `seq, state, seqBig`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.remove_sticker_pack(id=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("images", "RemoveStickerPack", id=12345)
```

---

### UseGif
اجرای متد رسمی `Images.UseGif` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `gif` | Object | **Optional** | Wire field `gif` (python arg: `gif`). |
| `usedAt` | Integer | **Required** | Wire field `usedAt` (python arg: `used_at`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.use_gif(gif={...}, used_at=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("images", "UseGif", gif={...}, used_at=12345)
```

---

## Wallet (کیف‌پول، فعال‌سازی، پرداخت و تسویه حساب)
> شناسه کامل سرویس در شبکه بله: `bale.wallet.v1.Wallet` — تعداد متدها: **13**

### ActivateWallet
اجرای متد رسمی `Wallet.ActivateWallet` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `nationalId` | String | **Required** | Wire field `nationalId` (python arg: `national_id`). |
| `isAutoActivated` | Object | **Optional** | Wire field `isAutoActivated` (python arg: `is_auto_activated`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.activate_wallet(national_id="value", is_auto_activated={...})

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "ActivateWallet", national_id="value", is_auto_activated={...})
```

---

### CashOutFromWallet
اجرای متد رسمی `Wallet.CashOutFromWallet` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `token` | String | **Required** | Wire field `token` (python arg: `token`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.cash_out_from_wallet(token="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "CashOutFromWallet", token="value", amount=12345)
```

---

### GetMoneyRequestPaymentTokenByCard
اجرای متد رسمی `Wallet.GetMoneyRequestPaymentTokenByCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `msg` | Object | **Optional** | Wire field `msg` (python arg: `msg`). |
| `amount` | Object | **Optional** | Wire field `amount` (python arg: `amount`). |
| `regarding` | Object | **Optional** | Wire field `regarding` (python arg: `regarding`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, endpoint, terminalId, merchantId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_money_request_payment_token_by_card(msg={...}, amount={...}, regarding={...})

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "GetMoneyRequestPaymentTokenByCard", msg={...}, amount={...}, regarding={...})
```

---

### GetMyWallets
اجرای متد رسمی `Wallet.GetMyWallets` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `wallets`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_my_wallets()

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "GetMyWallets")
```

---

### GetPaymentTokenByCard
اجرای متد رسمی `Wallet.GetPaymentTokenByCard` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `targetWallet` | String | **Required** | Wire field `targetWallet` (python arg: `target_wallet`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `regarding` | Object | **Optional** | Wire field `regarding` (python arg: `regarding`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, endpoint, terminalId, merchantId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_payment_token_by_card(target_wallet="value", amount=12345, regarding={...})

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "GetPaymentTokenByCard", target_wallet="value", amount=12345, regarding={...})
```

---

### GetWalletChargeToken
اجرای متد رسمی `Wallet.GetWalletChargeToken` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `walletId` | String | **Required** | Wire field `walletId` (python arg: `wallet_id`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, endpoint, terminalId, merchantId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_wallet_charge_token(wallet_id="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "GetWalletChargeToken", wallet_id="value", amount=12345)
```

---

### GetWalletContracts
اجرای متد رسمی `Wallet.GetWalletContracts` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| *None* | — | — | This method takes no parameters. |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `startDate, endDate, merchantCustomerUniqueValue, limitations, agreementId, status`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_wallet_contracts()

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "GetWalletContracts")
```

---

### GetWalletInvoice
اجرای متد رسمی `Wallet.GetWalletInvoice` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `walletId` | String | **Required** | Wire field `walletId` (python arg: `wallet_id`). |
| `pageNumber` | Object | **Optional** | Wire field `pageNumber` (python arg: `page_number`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `invoices`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.get_wallet_invoice(wallet_id="value", page_number={...})

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "GetWalletInvoice", wallet_id="value", page_number={...})
```

---

### PayByWallet
اجرای متد رسمی `Wallet.PayByWallet` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `sourceWallet` | String | **Required** | Wire field `sourceWallet` (python arg: `source_wallet`). |
| `targetWallet` | String | **Required** | Wire field `targetWallet` (python arg: `target_wallet`). |
| `amount` | Integer | **Required** | Wire field `amount` (python arg: `amount`). |
| `currency` | Integer | **Required** | Wire field `currency` (python arg: `currency`). |
| `regarding` | Object | **Optional** | Wire field `regarding` (python arg: `regarding`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.pay_by_wallet(source_wallet="value", target_wallet="value", amount=12345)

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "PayByWallet", source_wallet="value", target_wallet="value", amount=12345)
```

---

### PayMoneyRequestByWallet
اجرای متد رسمی `Wallet.PayMoneyRequestByWallet` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `sourceWalletId` | String | **Required** | Wire field `sourceWalletId` (python arg: `source_wallet_id`). |
| `msg` | Object | **Optional** | Wire field `msg` (python arg: `msg`). |
| `amount` | Object | **Optional** | Wire field `amount` (python arg: `amount`). |
| `regarding` | Object | **Optional** | Wire field `regarding` (python arg: `regarding`). |

</div>

**مقدار بازگشتی:** پیام تاییدیه پیش‌فرض (`DefaultResponse` یا تایید موفقیت).

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.pay_money_request_by_wallet(source_wallet_id="value", msg={...}, amount={...})

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "PayMoneyRequestByWallet", source_wallet_id="value", msg={...}, amount={...})
```

---

### VerifyCashOut
اجرای متد رسمی `Wallet.VerifyCashOut` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `walletId` | String | **Required** | Wire field `walletId` (python arg: `wallet_id`). |
| `accountNo` | String | **Required** | Wire field `accountNo` (python arg: `account_no`). |
| `nationalId` | String | **Required** | Wire field `nationalId` (python arg: `national_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `token, name`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_cash_out(wallet_id="value", account_no="value", national_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "VerifyCashOut", wallet_id="value", account_no="value", national_id="value")
```

---

### VerifyPeer
اجرای متد رسمی `Wallet.VerifyPeer` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `targetPeer` | Object | **Optional** | Wire field `targetPeer` (python arg: `target_peer`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `targetWalletName, targetUserId, walletId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_peer(target_peer={...})

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "VerifyPeer", target_peer={...})
```

---

### VerifyQRCode
اجرای متد رسمی `Wallet.VerifyQRCode` در پلتفرم بله.

<div dir="ltr" markdown="1">

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `targetWalletId` | String | **Required** | Wire field `targetWalletId` (python arg: `target_wallet_id`). |

</div>

**مقدار بازگشتی:** شیء باینری Protobuf شامل فیلدهای `targetWalletName, targetUserId`.

**نمونه فراخوانی پایتون:**
```python
# ۱. متد مستقیم پایتونیک
result = await app.verify_qr_code(target_wallet_id="value")

# ۲. فراخوانی با RPC
result = await app.rpc("wallet", "VerifyQRCode", target_wallet_id="value")
```

---

