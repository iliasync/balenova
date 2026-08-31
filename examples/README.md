# مثال‌های BaleNova

همهٔ مثال‌ها کوتاه و مستقل‌اند. ابتدا کتابخانه را نصب کنید:

```bash
pip install -e .
```

سپس یکی را اجرا کنید:

```bash
python examples/login.py
python examples/echo.py
python examples/commands.py
```

در اولین اجرا اطلاعات ورود پرسیده می‌شود و دفعات بعد از فایل ذخیره‌شده در
`sessions/my_account.session` استفاده خواهد شد.

در مثال‌هایی که `CHAT_ID` یا `GROUP_ID` دارند، مقدار نمونه را با شناسهٔ واقعی
خودتان جایگزین کنید.

| فایل | کاربرد |
| --- | --- |
| `login.py` | ورود و نمایش حساب |
| `echo.py` | پاسخ خودکار |
| `commands.py` | دستور `/start` |
| `messages.py` | ارسال پیام |
| `dialogs.py` | نمایش گفت‌وگوها |
| `json_output.py` | خروجی JSON |
| `updates.py` | مشاهدهٔ رویدادها |
| `files.py` | ظرفیت آپلود |
| `groups.py` | اطلاعات گروه |
| `gifts.py` | اطلاعات کیف پول |
| `calls.py` | تماس‌های اخیر |
