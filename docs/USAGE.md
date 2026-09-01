# راه‌اندازی BaleNova

## نصب

```bash
python -m pip install --upgrade balenova
```

## اجرا

```python
from balenova import Client

app = Client("my_account")
app.run_forever()
```

## انتخاب سطح API

سه مسیر سازگار برای کار با کتابخانه وجود دارد:

```python
# ساده‌ترین مسیر برای کارهای رایج
await app.send_message(chat, "سلام")

# دسترسی Pythonic به هر RPC تایپ‌شده؛ نام متد و فیلد snake_case است
groups = await app.rpc("groups", "get_my_groups", mode=2, is_owner=True)

# نام دقیق تولیدشده از پروتکل، برای تطبیق مستقیم با مستندات Bale
groups = await app.groups.GetMyGroups(mode=2, isOwner=True)
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
data = message.to_dict()       # یا as_dict()
text = message.to_json()       # یا as_json()
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
