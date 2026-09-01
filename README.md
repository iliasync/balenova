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
