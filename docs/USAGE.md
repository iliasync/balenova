# راهنمای سادهٔ BaleNova

## نصب و ورود

```bash
pip install balenova
```

```python
from balenova import Client

app = Client("personal")
app.run_forever()
```

برنامه در اولین اجرا اطلاعات ورود را می‌پرسد. پوشهٔ `sessions` را هیچ‌وقت در
GitHub قرار ندهید.

## پاسخ به پیام

```python
from balenova import Client, events, filters

app = Client("personal")


@app.on(events.NewMessage, filters.incoming & filters.private)
async def reply(event):
    await event.reply("سلام 👋")


app.run_forever()
```

## ساخت دستور

```python
@app.on(events.NewMessage, filters.command("ping"))
async def ping(event):
    await event.reply("pong")
```

دستوری که کاربر می‌فرستد `/ping` است.

## فیلترهای پرکاربرد

```python
filters.incoming  # پیام دریافتی
filters.outgoing  # پیام ارسالی خودتان
filters.private  # گفت‌وگوی خصوصی
filters.group  # گروه
filters.channel  # کانال
filters.text  # متن
filters.photo  # عکس
filters.video  # ویدیو
filters.document  # فایل
filters.reply  # پیام پاسخ‌دار
filters.sender(12345)  # فرستندهٔ مشخص
filters.regex(r"سلام")
```

نمونهٔ ترکیب:

```python
photos_from_groups = filters.incoming & filters.group & filters.photo
```

## ارسال پیام

```python
await client.send("12345|1", "سلام")
```

شناسهٔ گفت‌وگو را می‌توانید از `event.chat.id` بگیرید.

## اطلاعات پیام

```python
print(event.text)
print(event.sender)
print(event.sender_id)
print(event.chat)
print(event.message.id)
```

## کارهای آماده روی پیام

```python
await event.answer("پیام عادی")
await event.reply("پاسخ به همین پیام")
await event.delete()
await event.message.edit_text("ویرایش شد")
await event.message.seen()
await event.message.forward("67890|1")
```

## کاربر و گفت‌وگو

```python
me = await client.get_me()
chat = await client.get_entity("username")

print(me.full_name)
print(chat.to_json() if chat else "پیدا نشد")
```

## تاریخچه بدون صفحه‌بندی دستی

```python
async for message in client.iter_messages("12345|1", limit=100):
    print(message.content)
```

## JSON

```python
data = event.to_dict()
text = event.to_json()
```

همین دو متد روی `Message`، `User` و `Chat` هم وجود دارد.

## همهٔ رویدادها

```python
@app.on_update
async def inspect(update):
    print(update.name)
```

یا فقط یک کلاس مشخص:

```python
@app.on(events.NewMessage)
async def messages(event):
    print(event.text)
```

## اجرای مثال‌های آماده

پس از دریافت سورس پروژه:

```bash
pip install -e .
python examples/login.py
python examples/echo.py
python examples/commands.py
python examples/dialogs.py
```

برای دیدن گزینه‌های هر مثال، `--help` بزنید.
