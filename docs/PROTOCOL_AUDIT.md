# ممیزی پروتکل

مبنای اصلی BaleNova رفتار فعلی `web.bale.ai` و تست با حساب واقعی است. schema
جامع و wrapperهای تولیدشدهٔ مخزن `mtp1376/bale` با اجازهٔ صریح صاحب اثر وارد
پروژه شده‌اند. انتساب اثر در `NOTICE` ثبت شده و این فایل‌ها برای جلوگیری از
تداخل با API سطح بالای BaleNova در `bale.full` نگه‌داری می‌شوند.

## پوشش کامل

namespace کامل از طریق `client.api` در دسترس است:

```python
from balenova import Client

client = Client("my_account")

# ورودی با keywordهای واقعی proto (camelCase)
groups = await client.api.groups.GetMyGroups(mode=0, isOwner=False)

# یا با پیام protobuf تایپ‌شده
from bale.full import bale_pb2

request = bale_pb2.GetMyGroupsRequest(mode=0)
groups = await client.api.groups.GetMyGroups(request)
```

این سطح شامل ۱۷۱۵ message، چهل‌وچهار service descriptor و ۶۰۷ RPC روی ۵۲
namespace سرویس است. ۶۰۶ RPC unary مستقیماً request را encode، به transport
فعلی BaleNova ارسال و response تایپ‌شده را decode می‌کنند. تنها
`MavizStream.SubscribeToUpdates` از نوع server-streaming است و مانند مخزن مرجع
در transport unary قابل مصرف نیست.

برای مشاهدهٔ امکانات:

```python
print(client.api.services)
print(client.api.rpcs)
print(client.api.has_rpc("bale.search.v1.Search", "SearchMessages"))
```

در ممیزی اخیر این بخش‌ها اضافه یا تکمیل شدند:

- دریافت bulk گروه‌های عضو با `GetMyGroups` و `LoadGroups`
- نگه‌داری `access_hash`، عضویت، `can_send_message` و `permissions` در `Chat`
- مجوز عضو، مشاهدهٔ پیام، مدیران، کاربران مسدود و گروه‌های مشترک
- چرخهٔ تماس خصوصی: شروع، پذیرش، دریافت و قطع
- شروع/حذف استریم تماس، بازخورد تماس و بالا/پایین‌بردن دست
- variantهای واقعی آپدیت پیام، واکنش، read/receive و تماس
- حفظ variant ناشناخته با شمارهٔ field و payload خام، بدون حذف خاموش داده

API سادهٔ قبلی برای کارهای رایج حفظ شده است. `client.api` سطح کامل و تایپ‌شده
را ارائه می‌کند و `Client.invoke_raw` نیز برای payloadهای آزمایشی باقی مانده
است.

تست زندهٔ فقط‌خواندنی:

```bash
BALE_SESSION='<user_id>:<jwt>' pytest -q tests/test_web_bale.py
```

این تست اتصال، دیالوگ، پارامترها، محدودیت آپلود، تماس‌های جاری و مسیر bulk
گروه‌ها را بررسی می‌کند و هیچ پیام یا تماسی ایجاد نمی‌کند.
