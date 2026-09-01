# ۸۰ RPC تازهٔ build وب

این متدها اکنون همراه protobuf ورودی و خروجی در کتابخانه قابل فراخوانی‌اند.
برای جلوگیری از شکستن APIهای قدیمی، در namespace جداگانهٔ `client.recovered`
قرار گرفته‌اند.

```python
# روش کوتاه با namespace سرویس
menu = await client.recovered.bill.GetBillMenu()

# روش عمومی با نام کامل سرویس
result = await client.recovered.call(
    "bale.groups.v1.Groups",
    "SetSlowMode",
    group={"groupId": 123, "accessHash": 1},
    seconds={"value": 30},
)
```

namespaceهای موجود:

`bank_account_preferences`، `advertisement`، `arbaeen`، `bill`، `evex`،
`exchange`، `garson`، `groups`، `kifpool`، `pishvaz`، `sarrafi` و `story`.

## متدهای راحت‌تر

```python
await client.set_group_slow_mode("123|2", 30)
await client.set_group_sign_messages("123|2", True)

bill_menu = await client.get_bill_menu()
stories = await client.get_all_stories()
marketing = await client.get_marketing_tools_config()
services = await client.search_bale_services("پرداخت", language="fa")
```

!!! note
    پاسخ namespace بازیابی‌شده یک protobuf message است. برای تبدیل آن به dict از
    `model_to_dict(response)` استفاده کنید.

فهرست فیلدهای تمام متدها در [مرجع کامل RPCها](rpc-reference.md) آمده است.
