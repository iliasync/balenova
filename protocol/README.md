# Protocol development workflow

این پوشه برای توسعه و نسخه‌بندی پروتکل حساب کاربری بله است. فایل‌های اصلی
پروتکل در `src/bale/proto/*.proto` نگه‌داری می‌شوند و فایل‌های `*_pb2.py` خروجی
تولیدشدهٔ آن‌ها هستند.

## ۱. ثبت snapshot فعلی

```bash
python -m bale.tools.proto inventory -o protocol/before.json
```

snapshot شامل تمام messageها، enumها، شماره و نوع fieldها و hash منابع است.

## ۲. ضبط رفتار اکانت

```bash
python examples/protocol_lab.py
```

این حالت تا زمان فشردن `Ctrl+C` فعال می‌ماند و سپس trace را ذخیره و اتصال را
می‌بندد. اجرای زمان‌دار همچنان با گزینه‌ای مانند `--watch 60` ممکن است.

برای ثبت تاریخچهٔ یک peer مشخص:

```bash
python examples/protocol_lab.py --chat '12345|1'
```

traceها در `protocol/traces/` قرار می‌گیرند و عمداً توسط Git نادیده گرفته
می‌شوند. payload ممکن است حاوی پیام خصوصی باشد؛ آن را عمومی یا commit نکنید.
JWT، رمز، کد ورود و frame خام احراز هویت به‌صورت پیش‌فرض ذخیره نمی‌شوند.
همچنین user-info، query string و fragment آدرس‌ها حذف می‌شوند تا tokenهای اتصال
و WebRTC وارد metadata گزارش نشوند.

گزارش یک trace:

```bash
python -m bale.tools.proto report protocol/traces/trace-...
```

پس از افزودن field یا message جدید، frameهای قبلی را با schema جدید دوباره decode
کنید:

```bash
python -m bale.tools.proto replay protocol/traces/trace-... -o replay.json
```

برای decode یک frame مشخص:

```bash
python -m bale.tools.proto decode response.Response protocol/traces/trace-.../frames/000010.bin
```

## ۳. افزودن تعریف جدید

فایل binary به‌تنهایی نام و معنای fieldهای ناشناخته را مشخص نمی‌کند. تعریف جدید
باید با مقایسهٔ descriptor یا کد کلاینت رسمی بله و چند trace مستقل به یکی از
فایل‌های `request.proto`، `response.proto` یا `struct.proto` اضافه شود.

بعد از ویرایش protoها:

```bash
python scripts/generate_proto.py
ruff format src tests examples scripts
pytest
```

## ۴. مقایسهٔ schema

```bash
python -m bale.tools.proto inventory -o protocol/after.json
python -m bale.tools.proto diff protocol/before.json protocol/after.json
```

هر قابلیت جدید باید همراه wrapper تایپ‌شده، fixture ناشناس‌شده و تست encode / decode
اضافه شود.

## ضبط outboundهای کلاینت رسمی

اتصال کتابخانه فقط RPCهایی را می‌بیند که خود کتابخانه ارسال کرده است. برای کشف
عملیات‌هایی مانند کلیک دکمه، signaling تماس صوتی یا قابلیت‌هایی که هنوز wrapper
ندارند، ترافیک نسخهٔ وب رسمی را با Chromium ضبط کنید:

```bash
pip install -e '.[research]'
playwright install chromium
python examples/official_web_protocol_lab.py
```

اگر Chrome یا Chromium روی سیستم نصب باشد، دانلود مرورگر Playwright لازم نیست.

مرورگر با پروفایل پایدار `protocol/browser-profile/` باز می‌شود. یک‌بار داخل نسخهٔ
وب بله وارد شوید، عملیات موردنظر را انجام دهید و در ترمینال `Ctrl+C` بزنید.
WebSocketهای outbound/inbound و درخواست‌های gRPC-web ذخیره می‌شوند. برای RPCهای
جدید نام service و method، index و بایت‌های request/response نگه‌داری می‌شوند حتی
اگر message متناظر هنوز در protoهای پروژه وجود نداشته باشد.
فریم‌هایی که فقط به‌طور تصادفی مانند protobuf قابل decode هستند، با اعتبارسنجی
نام service/method به‌عنوان `official_unknown_frame` نگه‌داری می‌شوند.

در تماس صوتی فقط پیام‌های signaling قابل ضبط هستند؛ جریان رمزگذاری‌شدهٔ صدای
WebRTC/RTP عمداً ضبط نمی‌شود.
