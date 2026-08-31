# راهنمای استفادهٔ Bale Session

## اجرای مثال‌ها

همهٔ مثال‌ها فقط از session اکانت استفاده می‌کنند و عملیات مخرب انجام نمی‌دهند.
اگر session در `sessions/my_account.session` باشد، از ریشهٔ پروژه اجرا کنید:

```bash
python examples/login.py
python examples/json_output.py
python examples/dialogs_by_type.py
python examples/filter_messages.py --seconds 60
python examples/command_selfbot.py
```

برای مسیر یا نام دیگر:

```bash
python examples/login.py --session-dir sessions --session-name my_account
```

## فیلتر پیام و دستور

```python
from bale import Client, filters

client = Client(session_dir="sessions", session_name="my_account")


@client.on_message(filters.incoming & filters.private & filters.text)
async def private_text(message, client):
    print(message.content)


@client.on_message(filters.outgoing & filters.command("status"))
async def status(message, client):
    await message.answer("ok")
```

فیلترها با `&`، `|` و `~` ترکیب می‌شوند. فیلترهای ثابت مانند `filters.text` و
شکل callable آن‌ها مانند `filters.text()` معادل هستند.

## خروجی JSON

```python
me = await client.get_me()
print(me.to_json())
print(me.to_dict())
```

برای protobuf یا پاسخ‌های ترکیبی از `model_to_json(value)` استفاده کنید.

## پروفایل، مخاطبان و privacy

RPCهای account-session زیر با schema جاری Bale Web در دسترس‌اند:

```python
profile = await client.get_full_user(123456)
contacts = await client.get_contacts()
avatars = await client.load_user_avatars(123456)
blocked_peers = await client.load_blocked_users()

await client.add_contact(123456)
await client.block_user(123456)
await client.edit_time_zone("Asia/Tehran")
await client.edit_preferred_languages(["fa", "en"])
```

برای peerهایی که access hash واقعی آن‌ها در دسترس است، آن را با آرگومان کلیدی
`access_hash` بفرستید. مقدار پیش‌فرض سازگار با wrapperهای قدیمی `1` است. متدهای
تغییردهنده در تست زندهٔ پیش‌فرض اجرا نمی‌شوند.

این بسته فقط برای session واقعی حساب کاربری است؛ قابلیت‌های Bot API عمداً ارائه
نشده‌اند.
