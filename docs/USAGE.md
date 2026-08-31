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

فایل را با Python اجرا کنید. در اولین اجرا اطلاعات ورود پرسیده می‌شود و برای
دفعات بعد داخل پوشهٔ `sessions` ذخیره خواهد شد.

پوشهٔ `sessions` را در GitHub قرار ندهید.

مخزن پروژه: [github.com/iliasync/balenova](https://github.com/iliasync/balenova)

صفحهٔ نصب: [pypi.org/project/balenova](https://pypi.org/project/balenova/)
