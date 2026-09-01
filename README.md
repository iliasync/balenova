# BaleNova

راه‌اندازی سادهٔ حساب بله در Python.

[مستندات](https://iliasync.github.io/balenova/) · [GitHub](https://github.com/iliasync/balenova) · [PyPI](https://pypi.org/project/balenova/) · [گزارش مشکل](https://github.com/iliasync/balenova/issues)

## نصب

Python 3.10 یا جدیدتر لازم است.

```bash
python -m pip install --upgrade balenova
```

برای قابلیت پخش صدا در تماس:

```bash
python -m pip install --upgrade "balenova[voice]"
```

اتصال typed به تماس گروهی با SDK رسمی LiveKit:

```python
connection = await app.join_group_call_rtc(call_id, "My client")
room = await connection.connect()

# ... publish/subscribe with livekit.rtc ...

await room.disconnect()
await app.leave_group_call(call_id)
```

جزئیات RPCها، handshake و پیام‌های protobuf در
[`docs/CALL_RTC_PROTOCOL.md`](docs/CALL_RTC_PROTOCOL.md) آمده است.

## راه‌اندازی

فایلی به نام `main.py` بسازید:

```python
from balenova import Client, events, filters

app = Client("my_account")


@app.on(events.NewMessage, filters.command("start"))
async def start(event):
    await event.reply("سلام! آماده‌ام 🌱")


app.run_forever()
```

## فراخوانی سادهٔ همهٔ RPCها

برای بیشتر کارها متدهای سطح‌بالا مثل `send_message()` خواناترند. اگر RPC خاصی
لازم بود، نام سرویس، متد و فیلدها را می‌توان به شکل Pythonic نوشت:

```python
async def inspect_account(client):
    groups = await client.rpc(
        "groups",
        "get_my_groups",
        mode=2,
        is_owner=True,
    )
    bill_menu = await client.rpc("bill", "get_bill_menu")

    print(groups)
    print(groups.SerializeToString())  # پاسخ خام protobuf در صورت نیاز

app.run_task(inspect_account)
```

شکل تولیدشده نیز همچنان پشتیبانی می‌شود:

```python
groups = await app.groups.GetMyGroups(mode=2, isOwner=True)
bill_menu = await app.recovered.bill.GetBillMenu()
```

مدل‌های سطح‌بالا مثل پیام و آپدیت مستقیماً قابل چاپ و تبدیل‌اند:

```python
print(message)
print(message.as_dict())
print(message.as_json())
```

برنامه را اجرا کنید:

```bash
python main.py
```

در اجرای اول، شماره تلفن، کد ورود و در صورت فعال‌بودن رمز دومرحله‌ای پرسیده
می‌شود. ورودهای بعدی از session ذخیره‌شده استفاده می‌کنند.

## نصب از GitHub

```bash
git clone https://github.com/iliasync/balenova.git
cd balenova
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python examples/echo.py
```

در Windows، به‌جای دستور فعال‌سازی بالا اجرا کنید:

```powershell
.venv\Scripts\activate
```

## نکتهٔ امنیتی

پوشهٔ `sessions` و اطلاعات ورود را در GitHub، پیام یا فایل عمومی قرار ندهید.
بهتر است ابتدا با یک حساب آزمایشی شروع کنید.

این پروژه رسمی بله نیست و مسئولیت استفاده از حساب بر عهدهٔ کاربر است.

## مجوز

MIT
