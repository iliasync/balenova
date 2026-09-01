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

- [شروع سریع](USAGE.md)
- [API سطح‌بالا](api.md)
- [RPCهای تازهٔ بازیابی‌شده](recovered-rpcs.md)
- [مرجع کامل RPCها](rpc-reference.md)
- [پروتکل تماس و RTC](CALL_RTC_PROTOCOL.md)
- [گزارش ممیزی وب](WEB_PROTOCOL_AUDIT.md)
