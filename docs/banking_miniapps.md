# راهنمای امور بانکی، کیف پول و مینی‌اپ‌ها در BaleNova

یکی از ویژگی‌های مهم پیام‌رسان بله، امکانات مالی (انتقال کارت به کارت، استعلام موجودی، دریافت پاکت هدیه) و پلتفرم مینی‌اپ‌ها (Appzar) است. در **BaleNova** متدهای سطح‌بالای مستقیمی برای تعامل با این سرویس‌ها تعبیه شده است.

---

## ۱. کارت‌های پیوند (کارت‌های بانکی ذخیره‌شده)

برای دریافت لیست کارت‌های بانکی ثبت‌شده روی حساب کاربری:

```python
from balenova import Client, model_to_dict

app = Client.from_firefox()

async def main():
    async with app:
        # دریافت کارت‌های متصل به حساب
        cards = await app.get_payvand_cards()
        print(model_to_dict(cards))

app.run(main())
```

---

## ۲. استعلام موجودی کارت بانکی

استعلام مانده‌حساب کارت شتابی با استفاده از رمز دوم (پویا/ایستا):

```python
balance_res = await app.get_card_balance(
    card_number="6037997123456789",
    cvv2="123",
    expire_date="28/05",
    pin2="123456"
)

print(f"موجودی فعلی: {balance_res.currentBalanceAmount}")
print(f"موجودی قابل برداشت: {balance_res.availableBalanceAmount}")
```

---

## ۳. دریافت توکن انتقال وجه و کارت به کارت

برای شروع فرآیند انتقال وجه یا پرداخت در بله:

```python
transfer_token = await app.get_card_transfer_token(
    peer_user_id=123456789,
    description="تسویه حساب خرید ماهانه"
)
print("آدرس درگاه:", transfer_token.requestEndPoint)
print("توکن تراکنش:", transfer_token.token)
```

---

## ۴. کیف پول و پاکت‌های هدیه (Gift Packets)

ارسال و بازکردن پاکت‌های هدیه و استعلام وضعیت کیف پول:

```python
# استعلام وضعیت کیف پول
wallet = await app.get_wallet()
print("موجودی کیف پول:", wallet.balance)

# باز کردن پاکت هدیه دریافتی
packet_result = await app.open_gift_packet(
    chat_id="123456789|2",
    packet_id="packet_uuid_here"
)
print("مبلغ دریافت شده:", packet_result.amount)
```

---

## ۵. اجرای مینی‌اپ‌ها (Mini Apps / Appzar)

دریافت لینک امن اجرای مینی‌اپ‌های بله با ارسال `bot_user_id`:

```python
miniapp = await app.get_miniapp_url(
    bot_user_id=987654321,
    screen_mode=1  # تمام‌صفحه یا پنجره‌ای
)
print("لینک اجرای مینی‌اپ:", miniapp.url)
```
