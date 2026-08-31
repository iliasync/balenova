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
- `events.MessageEdited` برای ویرایش واقعی پیام (variant وب بله)
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

شماره و بایت خام variantهایی که هنوز مدل اختصاصی ندارند نیز حفظ می‌شود؛ بنابراین
آپدیت تازهٔ بله در تبدیل protobuf به دیکشنری بی‌صدا حذف نخواهد شد.

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

برای گرفتن همهٔ گروه‌های حساب، به‌جای پیمایش دیالوگ‌ها و اجرای یک درخواست برای
هر گروه، مسیر bulk خود بله در دسترس است:

```python
groups = await client.get_my_groups()
sendable = [
    group
    for group in groups
    if group.peer_type in {2, 5}
    and (group.can_send_message or group.permissions.get("send_message"))
]
```

این مسیر از `GetMyGroups` و `LoadGroups` استفاده می‌کند و `access_hash`، وضعیت
عضویت و مجوز مؤثر ارسال را در مدل `Chat` نگه می‌دارد. APIهای
`get_member_permissions`، `get_can_see_messages`، `fetch_group_admins`،
`get_banned_users` و `get_mutual_groups` نیز اضافه شده‌اند.

چرخهٔ تماس خصوصی و استریم نیز شامل `start_call`، `accept_call`، `receive_call`،
`discard_call`، `start_call_stream`، `delete_call_stream`،
`submit_call_feedback` و `raise_call_hand`/`lower_call_hand` است.

## کل پروتکل Bale Web

علاوه بر API ساده، تمام ۶۰۷ RPC بازیابی‌شده در ۵۲ namespace سرویس از طریق
`client.api` در دسترس‌اند:

```python
groups = await client.api.groups.GetMyGroups(mode=0, isOwner=False)
top_peers = await client.api.top_peer.GetTopPeer()

print(client.api.services)
print(client.api.rpcs)
```

نام fieldها در این سطح دقیقاً نام protobuf است و ممکن است camelCase باشد. برای
ساخت request تایپ‌شده نیز می‌توان از `bale.full.bale_pb2` و
`bale.full.bale_ext_pb2` استفاده کرد. API سادهٔ snake_case همچنان بدون تغییر
کار می‌کند. namespaceهای سازگار با مخزن مرجع مانند
`client.messaging.SendMessage(...)` نیز مستقیماً در دسترس‌اند. فهرست کامل
متدها در [راهنمای فارسی](docs/FULL_API_FA.md) و
[مرجع انگلیسی](docs/FULL_API.md) آمده است.

روی خود پیام نیز میان‌برهای آماده وجود دارد:

```python
await event.message.respond("سلام")
await event.message.edit_text("متن جدید")
await event.message.delete()
await event.message.react("❤")
```

نمونه‌های بیشتر در پوشهٔ [`examples`](examples) و راهنمای ساده در
[`docs/USAGE.md`](docs/USAGE.md) قرار دارند. نتیجه و قواعد ممیزی مخزن مقایسه‌ای
نیز در [`docs/PROTOCOL_AUDIT.md`](docs/PROTOCOL_AUDIT.md) ثبت شده است.

دو پروژهٔ نمونهٔ کامل نیز آماده شده‌اند:

- [`examples/broadcast_manager`](examples/broadcast_manager): تنظیم بنر، ساعت یا
  فاصلهٔ دوره‌ای، انتخاب گروه‌های دارای مجوز ارسال پیام و ارسال نرخ‌محدود
- [`examples/voice_player`](examples/voice_player): پخش آهنگ یا ویس ریپلای‌شده در
  تماس گروهی با فرمان‌های ویرایشی

## نکتهٔ مهم

این پروژه رسمیِ بله نیست. از حساب آزمایشی شروع کنید، اطلاعات ورود و فایل‌های
session را منتشر نکنید و مسئولیت استفاده از حساب بر عهدهٔ خود شماست.

## مجوز

هستهٔ BaleNova تحت MIT است. فایل‌های واردشده در `src/bale/full` متعلق به
Mohammad Teimori Pabandi هستند، با اجازهٔ صاحب اثر در این پروژه قرار گرفته‌اند
و مجوز اصلی خود را در [`src/bale/full/LICENSE`](src/bale/full/LICENSE) حفظ
می‌کنند. جزئیات انتساب در [`NOTICE`](NOTICE) آمده است.
