# BaleNova

کار با حساب بله در Python، با یک API ساده و قابل‌فهم.

## نصب

```bash
pip install balenova
```

Python 3.10 یا جدیدتر لازم است.

## شروع در کمتر از یک دقیقه

یک فایل به نام `main.py` بسازید:

```python
from balenova import Client, events, filters

app = Client("my_account")


@app.on(events.NewMessage, filters.command("start"))
async def start(event):
    await event.reply("سلام! من آماده‌ام 🌱")


app.run_forever()
```

سپس اجرا کنید:

```bash
python main.py
```

بار اول شماره، کد ورود و در صورت نیاز رمز دومرحله‌ای پرسیده می‌شود. دفعات بعد
ورود ذخیره‌شده استفاده خواهد شد.

## پیام‌ها

```python
@app.on(events.NewMessage, filters.private & filters.text)
async def new_message(event):
    print(event.text)
    print(event.sender_id)
    print(event.chat.id)

    await event.answer("پیامت رسید")
    await event.reply("این پیام به‌صورت پاسخ ارسال شد")
```

فیلترها را می‌توان با `&`، `|` و `~` ترکیب کرد:

```python
only_commands = filters.incoming & filters.private & filters.command("help")
```

## همهٔ به‌روزرسانی‌ها به‌صورت کلاس

هر به‌روزرسانی یک شیء مشخص است:

- `events.NewMessage` برای پیام تازه
- `events.MessageSent` برای تأیید ارسال
- `events.RawUpdate` برای موارد دیگری که دادهٔ آن‌ها دریافت شده است
- `events.Update` پایهٔ مشترک همهٔ موارد

```python
@app.on_update
async def every_update(update):
    print(update.name)
    print(update.to_json())
```

برای گرفتن فقط یک نوع:

```python
@app.on(events.MessageSent)
async def sent(update):
    print(update.to_dict())
```

## تبدیل نتیجه‌ها به JSON

مدل‌هایی مانند پیام، کاربر، گفت‌وگو و به‌روزرسانی مستقیماً قابل تبدیل‌اند:

```python
print(event.to_dict())
print(event.to_json())

me = await client.get_me()
print(me.to_json())
```

## میان‌برهای کاربردی

```python
await client.send("12345|1", "سلام")
chat = await client.get_entity("username")

async for message in client.iter_messages("12345|1", limit=100):
    print(message.text)

limits = await client.get_upload_limits()
```

روی خود پیام نیز میان‌برهای آماده وجود دارد:

```python
await event.message.respond("سلام")
await event.message.edit_text("متن جدید")
await event.message.delete()
await event.message.react("❤")
```

نمونه‌های بیشتر در پوشهٔ [`examples`](examples) و راهنمای ساده در
[`docs/USAGE.md`](docs/USAGE.md) قرار دارند.

دو پروژهٔ نمونهٔ کامل نیز آماده شده‌اند:

- [`examples/broadcast_manager`](examples/broadcast_manager): تنظیم بنر، ساعت یا
  فاصلهٔ دوره‌ای، انتخاب تعداد گروه‌های تحت مدیریت و فاصله بین ارسال‌ها
- [`examples/voice_player`](examples/voice_player): پخش آهنگ یا ویس ریپلای‌شده در
  تماس گروهی با فرمان‌های ویرایشی

## نکتهٔ مهم

این پروژه رسمیِ بله نیست. از حساب آزمایشی شروع کنید، اطلاعات ورود و فایل‌های
session را منتشر نکنید و مسئولیت استفاده از حساب بر عهدهٔ خود شماست.

## مجوز

MIT — جزئیات حقوقی لازم در فایل [`NOTICE`](NOTICE) نگه‌داری می‌شود.
