# راهنمای امور مالی، کارت به کارت و مینی‌اپ‌ها در BaleNova

تمامی متدهای بانکی و کیف‌پول بله با رعایت اصول نام‌گذاری و استانداردهای **PEP 8** برای استفاده توسعه‌دهندگان پیاده‌سازی شده‌اند.

---

## ۱. دریافت کارت‌های ذخیره‌شده (Payvand Cards)

برای دریافت و لیست کردن کارت‌های متصل به شماره حساب کاربری:

```python
import asyncio
from balenova import Client, model_to_dict

app = Client.from_browser("auto")


async def list_saved_cards() -> None:
    async with app:
        # دریافت کارت‌های پیوند کاربر
        response = await app.get_payvand_cards()
        cards_dict = model_to_dict(response)
        print("کارت‌های متصل به حساب:", cards_dict)


if __name__ == "__main__":
    asyncio.run(list_saved_cards())
```

---

## ۲. استعلام موجودی کارت بانکی (Card Balance Inquiry)

```python
async def check_card_balance_example() -> None:
    async with app:
        # استعلام موجودی با رمز دوم پویا / ایستا
        result = await app.get_card_balance(
            card_number="6037997123456789",
            cvv2="123",
            expire_date="28/05",
            pin2="123456",
        )
        print(f"موجودی فعلی: {result.currentBalanceAmount} ریال")
        print(f"موجودی قابل برداشت: {result.availableBalanceAmount} ریال")
```

---

## ۳. انتقال وجه کارت به کارت (Card Transfer Token)

```python
async def request_card_transfer_token(peer_id: int) -> None:
    async with app:
        # دریافت توکن انتقال وجه
        token_res = await app.get_card_transfer_token(
            peer_user_id=peer_id,
            description="تسویه هزینه دوره آموزشی",
        )
        print("آدرس درگاه امن بله:", token_res.requestEndPoint)
        print("شناسه توکن:", token_res.token)
```

---

## ۴. کیف‌پول، برداشت و پاکت‌های هدیه (Wallet & Gifts)

```python
async def wallet_operations_example() -> None:
    async with app:
        # ۱. مشاهده موجودی کیف‌پول بله
        wallet = await app.get_wallet()
        print(f"موجودی کیف‌پول: {wallet.balance}")

        # ۲. تسویه و انتقال وجه از کیف‌پول به شبا
        await app.cash_out(
            amount=500_000,
            iban="IR123456789012345678901234",
        )

        # ۳. باز کردن پاکت هدیه (Gift Packet)
        packet = await app.open_gift_packet(
            chat_id="123456789|2",
            packet_id="packet_unique_uuid",
        )
        print(f"مبلغ هدیه دریافت شده: {packet.amount}")
```

---

## ۵. اجرای مینی‌اپ‌ها (Mini Apps / Appzar)

دریافت آدرس امن بارگذاری مینی‌اپ با شناسه ربات:

```python
async def open_bot_miniapp(bot_id: int) -> None:
    async with app:
        miniapp_res = await app.get_miniapp_url(
            bot_user_id=bot_id,
            screen_mode=1,  # حالت ۱: تمام‌صفحه
        )
        print("آدرس وب‌اپلیکیشن بله:", miniapp_res.url)
```
