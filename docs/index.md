# BaleNova

BaleNova یک کتابخانهٔ async و غیررسمی برای کار با حساب کاربری بله در Python است.
نسخهٔ فعلی شامل APIهای سطح‌بالا، ۶۱۰ RPC تایپ‌شدهٔ قبلی، ۸۰ RPC بازیابی‌شده از
`web@5.5.1+169491` و اتصال صوتی/تصویری مبتنی بر LiveKit است.

## نصب

```bash
pip install balenova
```

برای تماس صوتی:

```bash
pip install "balenova[voice]"
```

## نمونهٔ کوتاه

```python
from balenova import Client, events, filters

app = Client("my_account")


@app.on(events.NewMessage, filters.command("start"))
async def start(event):
    await event.reply("سلام!")


app.run_forever()
```

!!! warning "غیررسمی"
    این پروژه وابسته به API وب بله است. session، JWT و URL تماس را منتشر نکنید.

## بخش‌های مستندات

- [شروع سریع و نصب](USAGE.md)
- [ارسال پیام، رسانه‌ها و استیکر](messaging.md)
- [کیبوردها (Inline/Reply) و ماشین حالت (FSM)](fsm_keyboards.md)
- [امور بانکی، کارت‌ها و مینی‌اپ‌ها](banking_miniapps.md)
- [استوری‌ها، نظرسنجی‌ها و زمان‌بندی پیام](stories_polls_schedule.md)
- [مدیریت کامل گروه‌ها و کانال‌ها](group_management.md)
- [مرجع متدهای شیء اصلی Client](api.md)
- [۸۰ RPC تازهٔ بازیابی‌شده وب](recovered-rpcs.md)
- [مرجع کامل ۶۹۰+ RPC پروتکل بله](rpc-reference.md)
- [پروتکل تماس و RTC](CALL_RTC_PROTOCOL.md)
- [گزارش ممیزی وب](WEB_PROTOCOL_AUDIT.md)
