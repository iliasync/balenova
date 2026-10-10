# راه‌اندازی BaleNova

## نصب

```bash
python -m pip install --upgrade balenova
```

## ورود و راه‌اندازی

### ورود خودکار از مرورگر (بدون نیاز به کد تایید)
اگر در مرورگر فایرفاکس (یا سایر مرورگرها) به وب بله (`web.bale.ai`) لاگین هستید، BaleNova می‌تواند بدون درخواست شماره تلفن و کد تایید، سشن فعال شما را به شکل خودکار تشخیص داده و بخواند:

```python
from balenova import Client

# تشخیص هوشمند و خودکار مرورگر (پشتیبانی از Firefox، Snap، Flatpak و پروفایل‌های سفارشی)
app = Client.from_browser("auto")

# یا اختصاصاً از فایرفاکس:
# app = Client.from_firefox()

app.run_forever()
```

### ورود ترمینالی با شماره تلفن
در صورت اجرای عادی، شماره تلفن و کد ورود در ترمینال پرسیده شده و سشن برای دفعات بعدی ذخیره می‌شود:

```python
from balenova import Client

app = Client("my_account")
app.run_forever()
```

## انتخاب سطح API

چهار مسیر سازگار برای کار با کتابخانه وجود دارد:

```python
# ۱. ساده‌ترین متدهای سطح‌بالا برای کارهای روزمره
await app.send_message(chat, "سلام")
stories = await app.get_all_stories()
emojis = await app.get_story_reaction_emojis()
await app.react_to_story(story_id, "❤")

# ۲. فراخوانی پایتونیک به هر RPC رسمی وب
groups = await app.rpc("groups", "get_my_groups", mode=2, is_owner=True)

# ۳. کالکشن تایپ‌شده و مستقیم تمام سرویس‌های پروتکل بله
groups = await app.api.groups.GetMyGroups(mode=2, isOwner=True)
poll_res = await app.api.poll.GetFullPollResult(pollId=12345)
```

`app.rpc()` هم RPCهای اصلی و هم RPCهای بازیابی‌شده را پیدا می‌کند:

```python
menu = await app.rpc("bill", "get_bill_menu")

# شکل صریح همان فراخوانی
menu = await app.recovered.bill.GetBillMenu()
```

برای بررسی قابلیت‌ها بدون ارسال درخواست:

```python
app.api.has_rpc("groups", "get_my_groups")
app.api.all_services
app.api.all_rpcs
```

`app.rpc()` مخصوص RPCهای unary است. برای stream آپدیت‌ها از API اختصاصی stream
یا `run_forever()` استفاده کنید.

## چاپ، dict و JSON

پیام‌ها، کاربران، چت‌ها و updateها نمایش خوانا دارند و بدون serializer جداگانه
قابل تبدیل‌اند:

```python
print(message)
data = message.to_dict()  # یا as_dict()
text = message.to_json()  # یا as_json()
```

برای پاسخ protobuf یا ساختارهای تو در تو از توابع عمومی استفاده کنید:

```python
from balenova import model_to_dict, model_to_json

print(model_to_json(groups))
payload = model_to_dict({"message": message, "groups": groups})
```

فیلد خام `raw` مدل‌ها به‌طور پیش‌فرض وارد JSON نمی‌شود. اگر برای اشکال‌زدایی
لازم است، `include_raw=True` بدهید.

فایل را با Python اجرا کنید. در اولین اجرا اطلاعات ورود پرسیده می‌شود و برای
دفعات بعد داخل پوشهٔ `sessions` ذخیره خواهد شد.

پوشهٔ `sessions` را در GitHub قرار ندهید.

مخزن پروژه: [github.com/iliasync/balenova](https://github.com/iliasync/balenova)

صفحهٔ نصب: [pypi.org/project/balenova](https://pypi.org/project/balenova/)
