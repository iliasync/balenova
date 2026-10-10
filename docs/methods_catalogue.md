# فهرست کامل متدهای سطح‌بالای BaleNova (بیش از ۳۸۰ متد پایتونیک)

تمامی متدهای پرکاربرد و تخصصی وب بله مستقیماً روی شیء `app` (نمونه کلاس `Client`) به صورت توابع مستقیم، با اسامی خوانا و پایتونیک در دسترس شما هستند. نیازی به صدا زدن دستورات خام پروتکل نیست!

---

## ۱. امور مالی، بانکی، کیف‌پول و ارزها (Financial & Wallet)

| متد پایتونیک | توضیح عملکرد | نمونه استفاده |
| :--- | :--- | :--- |
| `app.get_payvand_cards()` | دریافت لیست کارت‌های بانکی ثبت‌شده کاربر | `cards = await app.get_payvand_cards()` |
| `app.get_card_balance(...)` | استعلام موجودی کارت بانکی شتابی | `await app.get_card_balance(pan, cvv2, exp, pin2)` |
| `app.get_card_transfer_token(...)` | دریافت توکن تراکنش کارت به کارت | `await app.get_card_transfer_token(peer_id, ...)` |
| `app.get_wallet()` | مشاهده اطلاعات و موجودی کیف پول کاربر | `wallet = await app.get_wallet()` |
| `app.open_gift_packet(...)` | باز کردن پاکت هدیه دریافتی | `await app.open_gift_packet(chat_id, packet_id)` |
| `app.cash_out(...)` | تسویه و برداشت وجه از کیف پول | `await app.cash_out(amount=50000, iban="...")` |
| `app.charge(...)` | شارژ مستقیم کیف پول | `await app.charge(paymentToken="...", referenceNo="...")` |
| `app.check_charge_permission(...)` | بررسی مجاز بودن شارژ کیف پول | `await app.check_charge_permission(paymentToken="...")` |
| `app.create_kifpool(...)` | افتتاح کیف پول با کدملی | `await app.create_kifpool(nationalId="...")` |
| `app.crypto_cash_out(...)` | برداشت ارزی/کریپتویی از کیف پول | `await app.crypto_cash_out(amount=100, ...)` |
| `app.crypto_transfer(...)` | انتقال موجودی به شماره مقصد | `await app.crypto_transfer(amount=50, dstPhoneNo="...")` |
| `app.get_credit()` | دریافت سقف اعتبار کیف‌پول | `await app.get_credit()` |
| `app.inquiry_bill(...)` | استعلام شناسه قبض و پرداخت | `await app.inquiry_bill(billType=1, ...)` |
| `app.pay_bill(...)` | پرداخت انواع قبوض خدماتی | `await app.pay_bill(bill=...)` |
| `app.buy_charge(...)` | خرید مستقیم شارژ سیم‌کارت | `await app.buy_charge(phoneNumber="0912...", ...)` |
| `app.buy_internet_bundle(...)` | خرید مستقیم بسته‌های اینترنتی | `await app.buy_internet_bundle(phoneNumber="0912...", ...)` |
| `app.get_currencies_list()` | دریافت لیست نرخ ارزهای مسافرتی و نقدی | `await app.get_currencies_list()` |

---

## ۲. ارسال پیام، فایل، رسانه و مدیریت چت‌ها (Messaging & Media)

| متد پایتونیک | توضیح عملکرد | نمونه استفاده |
| :--- | :--- | :--- |
| `app.send_message(...)` | ارسال پیام متنی با پشتیبانی از دکمه‌ها | `await app.send_message(peer, "سلام", reply_markup=...)` |
| `app.send_photo(...)` | ارسال تصویر از فایل محلی یا بافر بایت | `await app.send_photo(peer, "img.png", caption="...")` |
| `app.send_video(...)` | ارسال ویدیو با کپشن و مدت زمان | `await app.send_video(peer, "video.mp4")` |
| `app.send_voice(...)` | ارسال صدای ضبط‌شده (Voice) | `await app.send_voice(peer, "voice.ogg", duration=10)` |
| `app.send_document(...)` | ارسال انواع فایل و سند (PDF, Zip و ...) | `await app.send_document(peer, "file.zip")` |
| `app.send_sticker(...)` | ارسال استیکر بله | `await app.send_sticker(peer, sticker_id)` |
| `app.edit_message_text(...)` | ویرایش متن پیام ارسال شده | `await app.edit_message_text(peer, msg_id, "متن جدید")` |
| `app.delete_message(...)` | حذف پیام برای طرفین | `await app.delete_message(peer, msg_id)` |
| `app.forward_message(...)` | فوروارد پیام از چتی به چت دیگر | `await app.forward_message(from_chat, to_chat, msg_id)` |
| `app.copy_message(...)` | کپی پیام بدون درج تگ فوروارد | `await app.copy_message(from_chat, to_chat, msg_id)` |
| `app.pin_message(...)` | سنجاق کردن پیام در چت | `await app.pin_message(peer, msg_id)` |
| `app.unpin_message(...)` | برداشتن سنجاق پیام | `await app.unpin_message(peer, msg_id)` |
| `app.create_folder(...)` | ساخت پوشه / تب تفکیک گفتگوها | `await app.create_folder("کانال‌های خبری", [cid1, cid2])` |
| `app.delete_folder(...)` | حذف پوشه چت‌ها با شناسه | `await app.delete_folder(folder_id)` |
| `app.archive_dialogs(...)` | انتقال چت‌ها به بایگانی (آرشیو) | `await app.archive_dialogs([cid1, cid2])` |
| `app.unarchive_dialogs(...)` | خارج کردن چت‌ها از بایگانی | `await app.unarchive_dialogs([cid1, cid2])` |
| `app.message_set_reaction(...)` | ثبت واکنش (ری‌اکشن ایموجی) به پیام | `await app.message_set_reaction(peer, msg_id, "❤️")` |

---

## ۳. مدیریت گروه‌ها، کانال‌ها و ادمین‌ها (Groups & Admins)

| متد پایتونیک | توضیح عملکرد | نمونه استفاده |
| :--- | :--- | :--- |
| `app.create_group(...)` | ایجاد گروه جدید با کاربران اولیه | `group = await app.create_group("گروه تست", [uid1])` |
| `app.create_channel(...)` | ساخت کانال جدید با توضیحات | `channel = await app.create_channel("کانال تست")` |
| `app.export_chat_invite_link(...)` | ساخت و دریافت لینک دعوت اختصاصی | `link = await app.export_chat_invite_link(chat_id)` |
| `app.revoke_chat_invite_link(...)` | باطل کردن لینک دعوت فعلی و ساخت لینک جدید | `await app.revoke_chat_invite_link(chat_id)` |
| `app.promote_chat_member(...)` | ارتقای کاربر عادی به مدیر گروه | `await app.promote_chat_member(chat_id, user_id)` |
| `app.remove_user_admin(...)` | عزل دسترسی مدیریت کاربر | `await app.remove_user_admin(chat_id, user_id)` |
| `app.kick_user(...)` | اخراج کاربر از گروه | `await app.kick_user(chat_id, user_id)` |
| `app.ban_chat_member(...)` | مسدودسازی و بن کاربر در گروه | `await app.ban_chat_member(chat_id, user_id)` |
| `app.unban_chat_member(...)` | رفع مسدودیت کاربر | `await app.unban_chat_member(chat_id, user_id)` |
| `app.set_chat_title(...)` | تغییر نام گروه یا کانال | `await app.set_chat_title(chat_id, "عنوان جدید")` |
| `app.set_chat_description(...)` | تغییر بیو و توضیحات چت | `await app.set_chat_description(chat_id, "توضیح جدید")` |
| `app.set_group_slow_mode(...)` | فعال‌سازی حالت آرام (Slow Mode) | `await app.set_group_slow_mode(chat_id, seconds=30)` |
| `app.get_chat_administrators(...)` | دریافت لیست تمام مدیران چت | `admins = await app.get_chat_administrators(chat_id)` |
| `app.get_chat_members_count(...)` | دریافت تعداد اعضای گروه یا کانال | `count = await app.get_chat_members_count(chat_id)` |

---

## ۴. استوری‌ها، نظرسنجی‌ها و ابزارهای هوش مصنوعی (Stories, Polls & AI)

| متد پایتونیک | توضیح عملکرد | نمونه استفاده |
| :--- | :--- | :--- |
| `app.get_all_stories()` | بارگذاری تمامی استوری‌های فعال | `await app.get_all_stories()` |
| `app.get_story(...)` | دریافت مشخصات استوری با شناسه | `await app.get_story(story_id)` |
| `app.react_to_story(...)` | ارسال ری‌اکشن به استوری | `await app.react_to_story(story_id, "🔥")` |
| `app.get_story_viewers(...)` | مشاهده آمار و بینندگان استوری شما | `await app.get_story_viewers(story_id)` |
| `app.remove_story(...)` | حذف استوری منتشر شده | `await app.remove_story(story_id)` |
| `app.get_poll_result(...)` | مشاهده آمار و جزئیات یک نظرسنجی | `await app.get_poll_result(poll_id)` |
| `app.vote_poll(...)` | رای دادن یا پس گرفتن رای در نظرسنجی | `await app.vote_poll(poll_id, option_ids=[1])` |
| `app.close_poll(...)` | بستن نظرسنجی توسط مدیر | `await app.close_poll(poll_id)` |
| `app.get_link_preview(...)` | پیش‌نمایش متادیتا و تصویر یک URL | `await app.get_link_preview("https://...")` |
| `app.get_link_summary(...)` | خلاصه‌سازی هوشمند محتوای وب‌سایت با AI | `await app.get_link_summary("https://...")` |
| `app.get_miniapp_url(...)` | دریافت لینک امن مینی‌اپ‌های بات‌ها | `await app.get_miniapp_url(bot_id)` |
| `app.load_scheduled_tasks(...)` | دریافت لیست پیام‌های زمان‌بندی‌شده | `await app.load_scheduled_tasks(chat_id)` |
| `app.cancel_scheduled_tasks(...)` | لغو پیام‌های زمان‌بندی‌شده | `await app.cancel_scheduled_tasks([tid1, tid2])` |

---

## ۵. تماس‌های صوتی و تصویری (Calls & WebRTC)

| متد پایتونیک | توضیح عملکرد | نمونه استفاده |
| :--- | :--- | :--- |
| `app.start_call(...)` | شروع تماس یک‌به‌یک جدید | `call = await app.start_call(target_uid)` |
| `app.receive_call(...)` | پاسخ دادن به تماس ورودی | `await app.receive_call(call_id)` |
| `app.discard_call(...)` | رد تماس یا قطع مکالمه | `await app.discard_call(call_id)` |
| `app.start_group_call(...)` | شروع تماس گروهی در یک گپ | `call = await app.start_group_call(chat_id)` |
| `app.join_group_call(...)` | ملحق شدن به تماس گروهی | `await app.join_group_call(call_id)` |
| `app.join_group_call_rtc(...)` | اتصال بلادرنگ به اتاق LiveKit WebRTC | `rtc = await app.join_group_call_rtc(call_id)` |
| `app.mute_participant(...)` | بی‌صدا کردن شرکت‌کننده در تماس | `await app.mute_participant(call_id=..., ...)` |
