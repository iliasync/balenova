# ⚡ BaleNova (بله‌نوا)

<div class="hero-card">
  <div class="hero-title">BaleNova Documentation</div>
  <div class="hero-subtitle">
    فریم‌ورک فوق‌سریع، ناهمگام (AsyncIO) و مدرن پایتون برای پیام‌رسان و سوپراپ بله<br>
    پوشش کامل بیش از ۸۳۰ متد پایتونیک با سینتکس دوگانه تلتون و پایروگرام
  </div>
  <div>
    <span class="badge badge-async">AsyncIO</span>
    <span class="badge badge-telethon">Telethon Syntax</span>
    <span class="badge badge-pyrogram">Pyrogram Style</span>
    <span class="badge badge-success">Zero-RPC</span>
    <span class="badge badge-warning">MIT Licensed</span>
  </div>
</div>

---

## 🌟 ویژگی‌های برجسته

<div class="card-grid">
  <div class="feature-card">
    <div class="feature-icon">🚫</div>
    <h3>تجربه خالص پایتون (Zero-RPC)</h3>
    <p>بدون نیاز به کار با ساختارهای پیچیده Protobuf یا فراخوانی‌های خام وب. همه چیز در قالب متدهای تمیز پایتون با Type Hinting دقیق ارائه شده است.</p>
  </div>
  <div class="feature-card">
    <div class="feature-icon">🦊</div>
    <h3>اتصال خودکار از مرورگر</h3>
    <p>با یک خط کد <code>Client.from_firefox()</code> مستقیماً به سشن فعال مرورگر فایرفاکس خود متصل شوید؛ بدون نیاز به دریافت مجدد کد تایید پیامکی!</p>
  </div>
  <div class="feature-card">
    <div class="feature-icon">⚡</div>
    <h3>سینتکس محبوب تلتون و پایروگرام</h3>
    <p>پشتیبانی کامل از دکوراتورهای رویدادمحور <code>@app.on(events.NewMessage)</code> و <code>@app.on_message</code> به همراه فیلترهای ترکیبی (<code>&</code>, <code>|</code>, <code>~</code>).</p>
  </div>
  <div class="feature-card">
    <div class="feature-icon">💬</div>
    <h3>دسترسی مستقیم (Dot-Access)</h3>
    <p>دسترسی ساده به ویژگی‌های پیام: <code>msg.text</code>, <code>msg.chat.title</code>, <code>msg.from_user.username</code>, <code>msg.is_outgoing</code>.</p>
  </div>
  <div class="feature-card">
    <div class="feature-icon">🎯</div>
    <h3>متدهای کنشی روی خود شیء</h3>
    <p>پاسخ‌گویی سریع روی شیء پیام بدون نیاز به فراخوانی‌های اضافه: <code>await msg.reply("...")</code>, <code>await msg.edit("...")</code>, <code>await msg.delete()</code>.</p>
  </div>
  <div class="feature-card">
    <div class="feature-icon">💳</div>
    <h3>امکانات جامع سوپراپ</h3>
    <p>پشتیبانی کامل از امور بانکی و کارت‌به‌کارت، پاکت‌های هدیه، کیبوردهای شیشه‌ای، ماشین وضعیت (FSM) و تماس‌های زنده صوتی-تصویری WebRTC.</p>
  </div>
</div>

---

## 🚀 شروع سریع در چند ثانیه

=== "سبک تلتون (Telethon Style)"

    ```python
    from balenova import Client, events

    # ساخت کلاینت (اتصال خودکار از فایرفاکس یا نام سشن دلخواه)
    app = Client.from_firefox()

    # دریافت پیام‌های ورودی با الگوی ریجکس
    @app.on(events.NewMessage(pattern=r"^/start", incoming=True))
    async def on_start(event: events.NewMessage):
        print(f"پیام جدید از {event.from_user.first_name}: {event.text}")
        await event.reply("سلام! ربات بله‌نوا با موفقیت فعال شد 🚀")
        await event.react("❤️")

    # اجرای مداوم و گوش به زنگ
    app.run()
    ```

=== "سبک پایروگرام (Pyrogram Style)"

    ```python
    from balenova import Client, filters
    from balenova.types import Message

    app = Client.from_firefox()

    # دریافت پیام‌های دستوری در چت خصوصی
    @app.on_message(filters.command("start") & filters.private)
    async def on_start(client: Client, message: Message):
        await message.reply(f"درود {message.from_user.first_name}! آماده پاسخ‌گویی هستم ⚡")
        await message.react("👍")

    app.run()
    ```

---

## 📊 جدول مقایسه BaleNova با روش‌های قدیمی

| قابلیت | BaleNova (بله‌نوا) | روش‌های خام و سنتی |
| :--- | :---: | :---: |
| **سطح سادگی کد** | بسیار بالا (بدون درگیری با پروتکل) | پیچیده و نیازمند دانش Protobuf |
| **سیستم رویدادها** | کلاس‌های ساختاریافته تلتون (`events.*`) | دیکشنری‌های خام و نامشخص |
| **لاگین از مرورگر** | ✅ یک خط کد (`Client.from_firefox()`) | ❌ نیازمند استخراج دستی توکن |
| **دسترسی به ویژگی‌ها** | ✅ دات-اکسس (`msg.text`, `msg.chat`) | ❌ دیکشنری‌های چندلایه |
| **متدهای کنشی شیء** | ✅ `msg.reply()`, `msg.edit()`, `msg.delete()` | ❌ صدا زدن متدهای متفرقه با پارامترهای طولانی |
| **بررسی خطا و پایداری** | استثناهای اختصاصی پایتونیک | خطاهای مبهم عددی سرور |

---

## 📚 سرفصل‌های جامع مستندات (به سبک تلگرام)

* [🚀 راهنمای نصب و احراز هویت](installation.md): شیوه‌های لاگین با SMS، فایرفاکس و توکن JWT.
* [🤖 راهنمای ساخت ربات (Event API)](bot_development.md): جدول کلاس‌های رویداد و فیلترهای Telethon و Pyrogram.
* [💬 مرجع متدها: پیام‌ها و رسانه‌ها](methods_messages.md): جدول کامل پارامترهای ارسال متن، رسانه، ادیت، حذف، فوروارد و پین.
* [👥 مرجع متدها: گفت‌وگوها و گروه‌ها](methods_chats.md): جدول پارامترهای دریافت لیست چت‌ها، مدیریت گروه، ادمین‌ها و دسترسی‌ها.
* [👤 مرجع متدها: کاربران و پروفایل](methods_users.md): جدول پارامترهای واکشی کاربر، جستجوی یوزرنیم، مسدودسازی و ویرایش نام.
* [📦 انواع داده و مدل‌ها (Types)](types.md): جدول فیلدها و متدهای فعال اشیای `Message`, `User`, `Chat`, `Dialog`, `Media`.
* [🎛️ کیبوردها و دکمه‌های شیشه‌ای](keyboards.md): ساخت اینلاین مارک‌آپ، دریافت کالبک‌ها و دکمه‌های ریپلای.
* [🍳 دستورالعمل‌ها و سناریوهای عملی (Cookbook)](cookbook.md): پروژه‌های آماده پشتیبانی، ضداسپم، دانلودر و ثبت‌نام FSM.
* [❓ پرسش‌های متداول (FAQ)](faq.md): پاسخ به مهم‌ترین سوالات فنی و معماری.
