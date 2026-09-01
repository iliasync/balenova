# ممیزی پروتکل وب بله — ۲۰۲۶-۰۹-۰۱

این ممیزی با سشن مجاز حساب، روی نسخهٔ رسمی وب بله انجام شده است. برای جلوگیری
از تغییر یا قفل‌شدن پروفایل اصلی، مرورگر با یک کپی موقت از پروفایل اجرا شد و
کپی موقت پس از پایان کار حذف شد.

## نسخه و دامنهٔ بررسی

- نسخهٔ وب: `web@5.5.1+169491`
- فایل‌های JavaScript بررسی‌شده: ۲۲۷
- ماژول‌های Rspack/Webpack بررسی‌شده: ۳٬۶۶۷
- سرویس‌های gRPC-Web: ۵۲
- متدهای RPC: ۶۸۳
- codecهای پروتوباف: ۱٬۹۶۰
- فیلدهای بازیابی‌شده از codecها: ۵٬۵۲۰
- فیلد مجهول یا reference حل‌نشده: صفر

فهرست کامل هر RPC همراه با فیلدهای ورودی و خروجی و همچنین گراف کامل codecها در
`protocol/official-web-5.5.1.json` قرار دارد. این فایل شامل اطلاعات حساب، توکن،
متن پیام، payload یا raw frame نیست.

## وضعیت ادغام در کتابخانه

پیش از این ممیزی، کتابخانه ۵۲ سرویس و ۶۱۰ RPC داشت. اکنون هر ۸۰ RPC تازه با
protobuf ورودی/خروجی در `client.recovered` ادغام شده‌اند. registry نهایی ۵۹ سرویس
و ۶۹۰ RPC دارد و هر ۶۸۳ descriptor فعال build رسمی را پوشش می‌دهد:

- ۶۸۳ متد در هر دو نسخه مشترک‌اند؛
- ۵۰۳ متد مشترک از نظر شکل مستقیم ورودی و خروجی دقیقاً برابرند؛
- ۱۸۰ متد مشترک حداقل یک اختلاف schema دارند؛
- ۱۲۳ ورودی و ۹۸ خروجی اختلاف schema دارند؛
- متد اضافهٔ ادغام‌نشده باقی نمانده است؛
- ۷ متد موجود در کتابخانه دیگر descriptor فعال در build جاری ندارند.

هفت سرویس تازه‌ای که ادغام شدند عبارت‌اند از:

- `bale.BankAccountPreferences.v1.BankAccountPreferences` — ۳ متد
- `bale.arbaeen.v1.Arbaeen` — ۱۹ متد
- `bale.bill.v1.Bill` — ۸ متد
- `bale.evex.v1.Evex` — ۸ متد
- `bale.exchange.v1.Exchange` — ۱۰ متد
- `bale.pishvaz.v1.Pishvaz` — ۳ متد
- `bale.sarrafi.v1.Sarrafi` — ۹ متد

۲۰ متد دیگر نیز به namespace سرویس‌های موجود اضافه شده‌اند: Advertisement
(۱۵)، Garson (۱)، Groups (۲)، Kifpool (۱) و Story (۱).

هفت descriptor حذف‌شده از build جاری:

- `AnonymousContact/GetUserAnonymousContactPage`
- `GoldWallet/GetBalance`
- `Falake/GetLinkStatus`
- `FeedBack/SendFeedBack`
- `LLMAuthService/GetAuthToken`
- `MyBank/GetMyBank`
- `Negah/GetMessageSeenList`

نمونه‌هایی از اختلاف schema عبارت‌اند از اضافه‌شدن `compressedSize` و `fileKind`
به `GetNasimFileUploadUrl`، اضافه‌شدن `language` به درخواست‌های ورود، تغییر چند
فیلد Appzar از bytes/int64 به string/int32، و اضافه‌شدن `seqBig` به پاسخ مشترک
عملیات به‌روزرسانی. جزئیات تمام اختلاف‌ها در
`protocol/official-web-5.5.1-vs-library.json` موجود است.

## تأیید زنده

یک capture زندهٔ ۱۵ثانیه‌ای، فقط از metadata و بدون payload/raw، ۱۴۰ رویداد و
۱۷ RPC واقعی را ثبت کرد. سرویس تازهٔ
`bale.pishvaz.v1.Pishvaz/GetMarketingToolsConfig` نیز در ترافیک واقعی مشاهده شد.
تست smoke کتابخانه با `sessions/my_account.session` نیز موفق بود.

هیچ متد ارسال پیام، حذف، پرداخت، انتقال وجه، ایجاد سفارش یا تغییر حساب در این
ممیزی فراخوانی نشد.

## تکرار استخراج

پس از دانلود assetهای build رسمی در یک پوشه:

```bash
node scripts/extract_web_protocol.mjs BUNDLE_DIR protocol/official-web.json
.venv/bin/python scripts/compare_web_protocol.py \
  protocol/official-web.json --output protocol/official-web-vs-library.json
```

نام اصلی TypeScript بعضی پیام‌های تو‌در‌تو در bundle مینیمایز شده است. برای این
پیام‌ها catalog از شناسهٔ بدون ابهام `module:local/export:name` استفاده می‌کند؛
شمارهٔ فیلد، نام فیلد، wire type، repeated/map بودن و reference پیام مقصد کامل
بازیابی شده‌اند. این ممیزی تمام schemaهای ارسال‌شده در build وب را پوشش می‌دهد،
نه APIهای احتمالی سمت سرور که هیچ کدی برای آن‌ها در build وب منتشر نشده است.
