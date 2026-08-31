# مستندات API پیام‌رسان بله (Bale)

این سند، **607 متد (RPC)** کلاینت وب بله را در قالب **52 سرویس** مستند می‌کند. برای هر متد: نام، گروه (سرویس)، ورودی‌ها، خروجی و **استنباطِ کاربرد** آن آمده است. خروجی‌هایی که «✔️ فقط تأیید» علامت خورده‌اند، پاسخ تهی (ack) برمی‌گردانند.

> ⚠️ ستون «کاربرد» بر پایهٔ نام متد، ورودی‌ها و دامنهٔ سرویس **استنباط** شده است (از روی JS مبهم‌سازی‌شدهٔ کلاینت وب استخراج شده) و مستندات رسمی بله نیست؛ ممکن است در مواردی دقیق نباشد.

## نحوهٔ فراخوانی از پایتون

```python
client = BaleClient(token); await client.connect()
# نام‌فضا = snake_case آخرین بخش نام سرویس؛ نام متد = همان نام وب
await client.messaging.SendMessage(peer={'type':1,'id':uid}, rid=rid,
                                   message={'textMessage':{'text':'سلام'}})
```

<a id="toc"></a>

## فهرست سرویس‌ها

- [اعلان‌های فشاری (Push) — `ai.bale.pushak.Push`](#svc-ai-bale-pushak-push) (6 متد)
- [مدیریت فایل‌ها — `ai.bale.server.Files`](#svc-ai-bale-server-files) (6 متد)
- [واکنش‌ها و بازدیدهای پیام — `bale.abacus.v1.Abacus`](#svc-bale-abacus-v1-abacus) (9 متد)
- [تبلیغات — `bale.advertisement.v1.Advertisement`](#svc-bale-advertisement-v1-advertisement) (108 متد)
- [تماس ناشناس — `bale.anonymous_contact.v1.AnonymousContact`](#svc-bale-anonymous_contact-v1-anonymouscontact) (1 متد)
- [مینی‌اپ‌ها و بات‌ها (Appzar) — `bale.appzar.v1.Appzar`](#svc-bale-appzar-v1-appzar) (3 متد)
- [احراز هویت و مدیریت حساب — `bale.auth.v1.Auth`](#svc-bale-auth-v1-auth) (26 متد)
- [پاکت طلای هدیه — `bale.balebank.v1.GoldGiftPacket`](#svc-bale-balebank-v1-goldgiftpacket) (3 متد)
- [کیف پول طلا — `bale.balebank.v1.GoldWallet`](#svc-bale-balebank-v1-goldwallet) (1 متد)
- [بانک و پرداخت — `bale.bank.v1.Bank`](#svc-bale-bank-v1-bank) (17 متد)
- [شارژ و بسته اینترنت — `bale.charnet.v1.CharnetService`](#svc-bale-charnet-v1-charnetservice) (11 متد)
- [تامین مالی جمعی — `bale.crowdfunding.v1.CrowdFunding`](#svc-bale-crowdfunding-v1-crowdfunding) (2 متد)
- [بررسی وضعیت لینک — `bale.falake.v1.Falake`](#svc-bale-falake-v1-falake) (1 متد)
- [تحلیل رویداد و ردیابی (فانوس) — `bale.fanoos.v1.fanoos`](#svc-bale-fanoos-v1-fanoos) (1 متد)
- [ارسال بازخورد — `bale.feedback.v1.FeedBack`](#svc-bale-feedback-v1-feedback) (1 متد)
- [کشف و مدیریت سرویس‌ها و بات‌ها — `bale.garson.v1.Garson`](#svc-bale-garson-v1-garson) (10 متد)
- [همگام‌سازی وضعیت مسیرها — `bale.ghasedak.v1.GhasedakService`](#svc-bale-ghasedak-v1-ghasedakservice) (2 متد)
- [پاکت هدیه — `bale.giftpacket.v1.GiftPacket`](#svc-bale-giftpacket-v1-giftpacket) (3 متد)
- [گروه‌ها و کانال‌ها — `bale.groups.v1.Groups`](#svc-bale-groups-v1-groups) (48 متد)
- [بات‌ها و مینی‌اپ‌ها — `bale.ketf.v1.Ketf`](#svc-bale-ketf-v1-ketf) (14 متد)
- [کیف پول و پرداخت — `bale.kifpool.v1.Kifpool`](#svc-bale-kifpool-v1-kifpool) (29 متد)
- [احراز هویت هوش مصنوعی — `bale.llm_auth.v1.LLMAuthService`](#svc-bale-llm_auth-v1-llmauthservice) (1 متد)
- [مجله و فید محتوا — `bale.magazine.v1.Magazine`](#svc-bale-magazine-v1-magazine) (9 متد)
- [مارکت و فروشگاه — `bale.market.v1.Market`](#svc-bale-market-v1-market) (26 متد)
- [دریافت به‌روزرسانی‌های جریانی — `bale.maviz.v1.MavizStream`](#svc-bale-maviz-v1-mavizstream) (4 متد)
- [تماس صوتی و تصویری (Meet) — `bale.meet.v1.Meet`](#svc-bale-meet-v1-meet) (30 متد)
- [استریم پیام — `bale.message_stream.v1.MessageStream`](#svc-bale-message_stream-v1-messagestream) (2 متد)
- [پیام‌رسانی — `bale.messaging.v2.Messaging`](#svc-bale-messaging-v2-messaging) (43 متد)
- [میکروبانکی (خدمات مالی) — `bale.microbanki.v1.MicroBanki`](#svc-bale-microbanki-v1-microbanki) (3 متد)
- [بانک من — `bale.my_bank.v1.MyBank`](#svc-bale-my_bank-v1-mybank) (1 متد)
- [وضعیت مشاهده پیام‌ها — `bale.negah.v1.Negah`](#svc-bale-negah-v1-negah) (1 متد)
- [سازمان‌ها — `bale.organizations.v1.Organizations`](#svc-bale-organizations-v1-organizations) (2 متد)
- [مدیریت مالی شخصی (PFM) — `bale.pfm.v1.Pfm`](#svc-bale-pfm-v1-pfm) (15 متد)
- [نظرسنجی — `bale.poll.v1.Poll`](#svc-bale-poll-v1-poll) (5 متد)
- [اشتراک پریمیوم — `bale.premium.v1.Premium`](#svc-bale-premium-v1-premium) (7 متد)
- [حضور و وضعیت آنلاین — `bale.presence.v1.Presence`](#svc-bale-presence-v1-presence) (11 متد)
- [رمز و احراز هویت — `bale.ramz.v1.Ramz`](#svc-bale-ramz-v1-ramz) (7 متد)
- [پیشنهاد کانال‌ها و گروه‌ها — `bale.recommender.v1.Recommender`](#svc-bale-recommender-v1-recommender) (4 متد)
- [گزارش محتوا — `bale.report.v1.Report`](#svc-bale-report-v1-report) (2 متد)
- [کارت‌های بانکی و پرداخت (SAP) — `bale.sap.v1.Sap`](#svc-bale-sap-v1-sap) (16 متد)
- [زمان‌بندی وظایف — `bale.schedule.v1.Scheduler`](#svc-bale-schedule-v1-scheduler) (6 متد)
- [جستجو — `bale.search.v1.Search`](#svc-bale-search-v1-search) (12 متد)
- [رسانه‌های مشترک — `bale.shared_media.v1.SharedMediaService`](#svc-bale-shared_media-v1-sharedmediaservice) (2 متد)
- [استوری‌ها — `bale.story.v1.Story`](#svc-bale-story-v1-story) (23 متد)
- [بازار ربات‌ها (Timche) — `bale.timche.v1.Timche`](#svc-bale-timche-v1-timche) (5 متد)
- [پیش‌نمایش و خلاصه لینک — `bale.tldr.v1.TLDR`](#svc-bale-tldr-v1-tldr) (2 متد)
- [مخاطبان برتر — `bale.top_peer.v1.TopPeer`](#svc-bale-top_peer-v1-toppeer) (2 متد)
- [هوش مصنوعی — `bale.turing.v1.AI`](#svc-bale-turing-v1-ai) (2 متد)
- [مدیریت کاربران — `bale.users.v1.Users`](#svc-bale-users-v1-users) (36 متد)
- [تنظیمات و پیکربندی — `bale.v1.Configs`](#svc-bale-v1-configs) (3 متد)
- [استیکر و GIF — `bale.v1.Images`](#svc-bale-v1-images) (10 متد)
- [کیف پول — `bale.wallet.v1.Wallet`](#svc-bale-wallet-v1-wallet) (13 متد)

---

<a id="svc-ai-bale-pushak-push"></a>

## اعلان‌های فشاری (Push) — `ai.bale.pushak.Push`

این سرویس مدیریت ثبت و لغو ثبت دستگاه‌های کاربر برای دریافت اعلان‌های فشاری (push notification) را بر عهده دارد. کلاینت از طریق این سرویس توکن‌های push خود را به سرور معرفی می‌کند تا پیام‌ها و رویدادها به‌صورت برخط به دستگاه کاربر ارسال شوند.

نام‌فضای پایتون: `client.push` — تعداد متد: 6

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `RegisterGooglePush` | `projectId: int64`، `token: string` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که کلاینت می‌خواهد توکن FCM (Firebase Cloud Messaging) دستگاه را با ارسال projectId و token به سرور ثبت کند تا اعلان‌های Google/FCM برای این دستگاه فعال شوند. |
| `RegisterPush` | `register: Register`، `pushVersion: int32` | `encryptionKey: bytes` | برای ثبت کلی دستگاه جهت دریافت اعلان فشاری استفاده می‌شود؛ کلاینت اطلاعات register و pushVersion را ارسال می‌کند تا سرور نسخه و نوع کانال push مورد استفاده را بشناسد. |
| `SetConfig` | `config: T_tl_91847` | ✔️ فقط تأیید | کلاینت با ارسال شیء config تنظیمات مربوط به رفتار اعلان‌های فشاری (مانند حالت بی‌صدا یا فیلترهای دریافت) را روی سرور به‌روزرسانی می‌کند. |
| `UnregisterAllPushCredentials` | — | ✔️ فقط تأیید | برای لغو ثبت تمام اعتبارنامه‌های push تمام دستگاه‌های کاربر به‌یکباره فراخوانی می‌شود؛ معمولاً هنگام خروج از حساب کاربری یا تغییر امنیتی انجام می‌گیرد. |
| `UnregisterGooglePush` | `token: string` | ✔️ فقط تأیید | با ارسال token مشخص، توکن FCM ثبت‌شده یک دستگاه را از سرور حذف می‌کند تا آن دستگاه دیگر اعلان‌های Google Push دریافت نکند. |
| `UnregisterPush` | `unregister: Unregister` | ✔️ فقط تأیید | برای لغو ثبت یک دستگاه خاص از سرویس push استفاده می‌شود؛ کلاینت شیء unregister را ارسال می‌کند تا اعلان‌های فشاری برای آن دستگاه متوقف شوند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-ai-bale-server-files"></a>

## مدیریت فایل‌ها — `ai.bale.server.Files`

این سرویس عملیات آپلود، لغو آپلود، و دریافت لینک دانلود فایل‌ها در پیام‌رسان بله را مدیریت می‌کند. کلاینت از این RPCها برای ارسال فایل به سرور Nasim و بازیابی URLهای عمومی یا خصوصی فایل استفاده می‌کند.

نام‌فضای پایتون: `client.files` — تعداد متد: 6

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `FileUploadCancel` | `file: FileLocation` | `canceled: bool` | هنگامی که کاربر آپلود یک فایل را قبل از تکمیل لغو می‌کند، کلاینت این RPC را با ارسال file (از نوع FileLocation) فراخوانی می‌کند تا سرور منابع رزرو‌شده برای آن آپلود را آزاد کند. |
| `GetNasimFilePublicUrl` | `peer: Bot`، `file: FileLocation`، `filename: StringValue` | `fileUrl: FileUrl` | برای دریافت لینک عمومی (قابل اشتراک‌گذاری) یک فایل متعلق به یک ربات (peer از نوع Bot) فراخوانی می‌شود؛ کلاینت با ارسال file و filename می‌تواند URL عمومی فایل را جهت نمایش یا اشتراک‌گذاری به‌دست آورد. |
| `GetNasimFileUploadResume` | `file: FileLocation` | `fileUrl: FileUrl`، `canResume: bool` | زمانی که آپلود یک فایل قطع شده و کلاینت قصد ادامه‌ی آن را دارد، این RPC با ارسال file (FileLocation) فراخوانی می‌شود تا اطلاعات وضعیت آپلود ناتمام بازیابی شده و آپلود از همان نقطه از سر گرفته شود. |
| `GetNasimFileUploadUrl` | `expectedSize: int32`، `crc: int64`، `uid: int64`، `name: string`، `mimeType: string`، `exPeer: ExPeer`، `sendType: SendType`، `chunkSize: int64` | `fileId: int64`، `url: string`، `duplicate: bool`، `chunkSize: int32`، `blockSize: int64` | پیش از آپلود یک فایل جدید، کلاینت این RPC را با اطلاعاتی مانند expectedSize، crc، mimeType، و exPeer فراخوانی می‌کند تا آدرس آپلود (URL) و تنظیمات لازم (مثل chunkSize) را از سرور Nasim دریافت کند. |
| `GetNasimFileUrl` | `file: FileLocation` | `fileUrl: FileUrl` | برای دریافت لینک دانلود یک فایل مشخص (با ارسال file از نوع FileLocation) استفاده می‌شود؛ کلاینت این RPC را هنگام نمایش یا دانلود محتوای رسانه‌ای فراخوانی می‌کند. |
| `GetNasimFileUrls` | `files: repeated FileLocation` | `fileUrls: repeated FileUrl` | برای دریافت یکجای لینک دانلود چندین فایل (files به صورت لیستی از FileLocation) به‌کار می‌رود؛ کلاینت این RPC را زمانی که نیاز به بارگذاری همزمان چندین رسانه دارد (مثلاً در گالری پیام‌ها) فراخوانی می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-abacus-v1-abacus"></a>

## واکنش‌ها و بازدیدهای پیام — `bale.abacus.v1.Abacus`

این سرویس مدیریت واکنش‌ها (reactions) و بازدیدهای پیام‌ها در پیام‌رسان بله را برعهده دارد. کلاینت از این سرویس برای ثبت، حذف، خواندن و بارگذاری واکنش‌های کاربران به پیام‌ها و همچنین دریافت آمار بازدید پیام‌ها استفاده می‌کند.

نام‌فضای پایتون: `client.abacus` — تعداد متد: 9

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `EnableShowReactionFlag` | — | ✔️ فقط تأیید | کلاینت این RPC را برای فعال‌سازی نمایش واکنش‌ها فراخوانی می‌کند؛ احتمالاً هنگامی که کاربر برای اولین بار با قابلیت واکنش آشنا می‌شود یا آن را در تنظیمات روشن می‌کند. |
| `GetMessageReactionsList` | `peer: Peer`، `rid: int64`، `date: int64`، `code: string`، `page: int32`، `limit: int32` | `userReactions: repeated UserReaction` | برای دریافت فهرست کاربرانی که به یک پیام مشخص (با peer و rid) با یک واکنش خاص (code) واکنش نشان داده‌اند فراخوانی می‌شود؛ پارامترهای page و limit نشان‌دهنده صفحه‌بندی نتایج هستند. |
| `GetMessagesReactions` | `peer: Peer`، `mids: repeated MessageId`، `originPeer: Peer`، `originMids: repeated MessageId` | `containers: repeated Container` | کلاینت برای دریافت خلاصه واکنش‌های چند پیام به‌طور همزمان (با ارسال لیست mids در peer) این RPC را صدا می‌زند؛ پارامترهای originPeer و originMids نیز برای پیام‌های فوروارد‌شده استفاده می‌شوند. |
| `GetMessagesViews` | `peer: Peer`، `mids: repeated MessageId`، `increment: bool`، `correctMids: repeated MessageId` | `containers: repeated T_THn` | برای دریافت تعداد بازدید پیام‌های یک peer (با لیست mids) فراخوانی می‌شود؛ اگر increment برابر true باشد، بازدید کاربر نیز به شمارنده افزوده می‌شود. |
| `GetShowReactionFlag` | — | `userId: int32`، `isEnable: bool` | کلاینت برای بررسی اینکه آیا قابلیت نمایش واکنش‌ها برای کاربر فعال است یا خیر این RPC را فراخوانی می‌کند؛ معمولاً هنگام راه‌اندازی اپلیکیشن یا بارگذاری تنظیمات کاربر صدا زده می‌شود. |
| `LoadReactions` | `peer: Peer`، `mids: repeated MessageId`، `ignoreCountViews: bool` | `containers: repeated Container` | برای بارگذاری اطلاعات واکنش‌های چند پیام (mids) در یک peer استفاده می‌شود؛ پارامتر ignoreCountViews مشخص می‌کند که آیا شمارنده بازدید در این درخواست نادیده گرفته شود. |
| `MessageReactionsRead` | `peer: ExPeer`، `messageId: MessageId` | ✔️ فقط تأیید | هنگامی که کاربر واکنش‌های یک پیام (messageId) را در peer مشاهده می‌کند فراخوانی می‌شود تا واکنش‌های آن پیام به‌عنوان «خوانده‌شده» علامت‌گذاری شوند. |
| `MessageRemoveReaction` | `peer: Peer`، `rid: int64`، `code: string`، `date: int64` | `seq: int32`، `reactions: repeated Reaction`، `state: bytes` | کلاینت برای حذف واکنش قبلی کاربر (با code مشخص) از یک پیام (peer و rid) این RPC را فراخوانی می‌کند؛ پارامتر date زمان ثبت واکنش اصلی را مشخص می‌کند. |
| `MessageSetReaction` | `peer: Peer`، `rid: int64`، `code: string`، `date: int64` | `seq: int32`، `reactions: repeated Reaction`، `state: bytes` | برای ثبت واکنش (emoji با code مشخص) روی یک پیام (peer و rid) فراخوانی می‌شود؛ date زمان ارسال واکنش را مشخص می‌کند و پاسخ وضعیت عملیات را بازمی‌گرداند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-advertisement-v1-advertisement"></a>

## تبلیغات — `bale.advertisement.v1.Advertisement`

این سرویس مدیریت کامل سیستم تبلیغات بله را فراهم می‌کند و شامل ایجاد و ویرایش آگهی‌ها، کمپین‌ها، حساب‌های تبلیغاتی، درآمد کانال‌ها و کدهای تخفیف می‌شود. کلاینت از این سرویس برای اجرای چرخه کامل تبلیغات، از ثبت آگهی تا پرداخت درآمد به صاحبان کانال، استفاده می‌کند.

نام‌فضای پایتون: `client.advertisement` — تعداد متد: 108

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AddCustomIncome` | `type: int32`، `amount: int64`، `description: string`، `customerUserId: int32`، `customerName: string`، `paymentMethod: int32`، `paymentDate: int64` | `id: string` | برای ثبت دستی یک درآمد سفارشی در سیستم تبلیغات فراخوانی می‌شود؛ مدیر با ارسال amount، customerUserId، paymentMethod و paymentDate یک پرداخت خارج از چرخه معمول را به حساب کاربر اضافه می‌کند. |
| `ChangeAccountState` | `state: int32`، `ownerId: int32`، `reason: string` | ✔️ فقط تأیید | وضعیت حساب تبلیغاتی یک کاربر (ownerId) را تغییر می‌دهد؛ احتمالاً برای فعال‌سازی، تعلیق یا مسدودکردن حساب آگهی‌دهنده به همراه دلیل (reason) استفاده می‌شود. |
| `ChangeAdState` | `adId: string`، `state: int32`، `reason: string` | ✔️ فقط تأیید | وضعیت یک آگهی مشخص (adId) را تغییر می‌دهد، برای مثال تأیید، رد یا توقف آگهی توسط ادمین یا سیستم بررسی محتوا، با ذکر دلیل (reason). |
| `ChangeBonusCodeState` | `code: string`، `state: int32` | ✔️ فقط تأیید | وضعیت یک کد تخفیف یا پاداش (code) را فعال یا غیرفعال می‌کند؛ معمولاً توسط ادمین برای مدیریت چرخه عمر کدهای بونوس فراخوانی می‌شود. |
| `ChangeCampaignContentState` | `campaignId: string`، `state: int32`، `reason: string` | ✔️ فقط تأیید | وضعیت محتوای یک کمپین (campaignId) را تغییر می‌دهد؛ کلاینت این RPC را هنگام تأیید یا رد محتوای کمپین در فرآیند بررسی، همراه با دلیل (reason)، فراخوانی می‌کند. |
| `ChangeCampaignState` | `campaignId: string`، `state: int32`، `rejectionReason: string` | ✔️ فقط تأیید | وضعیت کلی یک کمپین (campaignId) را تغییر می‌دهد؛ برای تأیید، رد یا توقف کمپین توسط ادمین استفاده می‌شود و در صورت رد، دلیل رد (rejectionReason) ارسال می‌گردد. |
| `ChangeChannelIncomeOwner` | `peerId: GroupPeer` | ✔️ فقط تأیید | مالکیت درآمد تبلیغاتی یک کانال (peerId) را تغییر می‌دهد؛ احتمالاً زمانی فراخوانی می‌شود که مدیریت کانال به فرد دیگری منتقل می‌شود و باید حساب درآمدی نیز به‌روز شود. |
| `ChangeChannelShowAdPermissions` | `peerId: GroupPeer`، `showAds: ShowAds`، `timeRestrict: TimeRestrict`، `categoryFilter: CategoryFilter` | ✔️ فقط تأیید | تنظیمات نمایش آگهی در یک کانال (peerId) را به‌روز می‌کند؛ با این RPC می‌توان مجوز نمایش آگهی (showAds)، محدودیت زمانی (timeRestrict) و فیلتر دسته‌بندی (categoryFilter) را برای کانال تعریف کرد. |
| `ChangeStatusDialogAdOrder` | `id: string`، `targetStatus: int32`، `date: int64`، `rejectionReason: StringValue` | ✔️ فقط تأیید | وضعیت یک سفارش آگهی دیالوگ (id) را به targetStatus جدید تغییر می‌دهد؛ تاریخ اجرا (date) و دلیل رد احتمالی (rejectionReason) نیز همراه درخواست ارسال می‌شوند. |
| `ChangeUserDataState` | `ownerId: int32`، `state: int32`، `reason: int32` | ✔️ فقط تأیید | وضعیت داده‌های تبلیغاتی مربوط به یک کاربر (ownerId) را تغییر می‌دهد؛ احتمالاً برای مدیریت رضایت کاربر به استفاده از داده برای هدف‌گیری تبلیغات، با ذکر دلیل، استفاده می‌شود. |
| `ChannelIncomeGetCredit` | `peerId: GroupPeer` | ✔️ فقط تأیید | اعتبار درآمد تبلیغاتی یک کانال (peerId) را به کیف پول یا حساب مرتبط منتقل می‌کند؛ صاحب کانال این RPC را برای دریافت موجودی انباشته‌شده از نمایش آگهی فراخوانی می‌کند. |
| `ChannelIncomeKifTransfer` | `peerId: GroupPeer`، `payType: int32` | ✔️ فقط تأیید | درآمد تبلیغاتی یک کانال (peerId) را با روش پرداخت مشخص (payType) به کیف پول (کیف) منتقل می‌کند؛ نوعی برداشت داخلی درآمد کانال به سمت کیف پول بله است. |
| `ChannelIncomePayment` | `peerId: GroupPeer`، `payType: int32` | `factorHtml: string` | پرداخت درآمد تبلیغاتی کانال (peerId) را با روش پرداخت تعیین‌شده (payType) انجام می‌دهد و پاسخ آن اطلاعات تراکنش پرداخت را برمی‌گرداند. |
| `ConvertIncome` | `convertToPoints: ConvertToPoints`، `convertToGiftPacket: ConvertToGiftPacket`، `convertToGiftPacketForChannelOwner: ConvertToGiftPacketForChannelOwner` | ✔️ فقط تأیید | درآمد تبلیغاتی را به فرمت دیگری تبدیل می‌کند؛ با توجه به فیلدهای ورودی، می‌توان آن را به امتیاز (convertToPoints)، پاکت هدیه (convertToGiftPacket) یا پاکت هدیه ویژه مالک کانال تبدیل کرد. |
| `CreateAd` | `adData: Ads`، `price: int64` | `adId: string` | یک آگهی جدید با داده‌های تبلیغاتی (adData) و قیمت مشخص (price) ایجاد می‌کند؛ آگهی‌دهنده این RPC را برای ثبت و ارسال آگهی جدید در سیستم تبلیغات بله فراخوانی می‌کند. |
| `CreateAndStartChannelAd` | `title: string`، `description: string`، `link: string`، `platform: int32`، `viewCount: int32`، `clickCount: int32`، `startTime: int64` | `id: string` | یک کمپین تبلیغاتی برای کانال ایجاد و بلافاصله شروع می‌کند؛ با ارسال title، description، link، platform، تعداد نمایش و کلیک هدف و زمان شروع (startTime)، آگهی بدون مرحله جداگانه تأیید اجرا می‌شود. |
| `CreateBaleDialogCustomAd` | `pic: string`، `title: string`، `description: string`، `link: string`، `platform: int32` | `id: string` | یک آگهی سفارشی برای دیالوگ بله ایجاد می‌کند؛ با ارسال تصویر (pic)، عنوان، توضیحات، لینک و پلتفرم هدف، آگهی‌ای طراحی می‌شود که در فضای چت نمایش داده خواهد شد. |
| `CreateBonusCode` | `data: T_tp_58187`، `autoGenerate: bool` | `code: string` | یک کد پاداش/تخفیف جدید در سیستم تبلیغات ایجاد می‌کند؛ با تنظیم data و فعال‌کردن autoGenerate می‌توان کد را به‌صورت خودکار تولید کرد یا کد دلخواه تعریف نمود. |
| `CreateChannelIncomeFactor` | `peerId: GroupPeer`، `year: int32`، `month: int32` | `factorHtml: string` | فاکتور درآمد ماهانه یک کانال (peerId) را برای سال (year) و ماه (month) مشخص صادر می‌کند؛ این فاکتور مبنای پرداخت درآمد تبلیغاتی به صاحب کانال است. |
| `CreateCustomCampaignPackage` | `userId: int32`، `baseCredit: int64`، `creditExpireDays: int32`، `campaignDailyCapacity: int64`، `allowedConcurrentCampaign: int32`، `audienceId: int32`، `campaignViewCoef: int32`، `campaignClickCoef: int32` | ✔️ فقط تأیید | یک پکیج کمپین سفارشی برای یک کاربر (userId) تعریف می‌کند؛ ادمین با این RPC مقدار اعتبار پایه، روزهای انقضا، ظرفیت روزانه، تعداد کمپین همزمان مجاز و ضرایب نمایش و کلیک را تنظیم می‌کند. |
| `DeleteCustomIncome` | `id: string` | ✔️ فقط تأیید | یک درآمد سفارشی ثبت‌شده (id) را از سیستم حذف می‌کند؛ معمولاً در صورت اشتباه در ثبت درآمد دستی، ادمین این RPC را فراخوانی می‌کند. |
| `EditAccount` | `account: Data`، `isRestoreExpiredCredit: bool` | ✔️ فقط تأیید | اطلاعات حساب تبلیغاتی (account) را ویرایش می‌کند؛ با فعال‌کردن isRestoreExpiredCredit می‌توان اعتبار منقضی‌شده را نیز بازگرداند. |
| `EditAd` | `ad: Ads` | ✔️ فقط تأیید | محتوای یک آگهی موجود (ad از نوع Ads) را ویرایش می‌کند؛ آگهی‌دهنده پیش از تأیید نهایی می‌تواند اطلاعات آگهی خود را به‌روز کند. |
| `EditCampaignAd` | `ad: T_tE_58187` | ✔️ فقط تأیید | آگهی مرتبط با یک کمپین (ad) را ویرایش می‌کند؛ کلاینت این RPC را برای اصلاح محتوا یا تنظیمات آگهی در چارچوب یک کمپین فعال یا در انتظار تأیید فراخوانی می‌کند. |
| `EditCampaignContent` | `campaign: Campaign` | ✔️ فقط تأیید | محتوای یک کمپین تبلیغاتی (campaign) را ویرایش می‌کند؛ هنگامی که آگهی‌دهنده نیاز به تغییر متن، تصویر یا تنظیمات هدف‌گیری کمپین دارد این RPC فراخوانی می‌شود. |
| `FinishAd` | `id: string` | ✔️ فقط تأیید | برای پایان دادن به یک آگهی معمولی با ارسال id آن فراخوانی می‌شود. کلاینت پس از اتمام دوره نمایش یا لغو دستی آگهی، این RPC را صدا می‌زند. |
| `FinishAdV2` | `adId: string` | ✔️ فقط تأیید | نسخه دوم پایان دادن به آگهی است که با adId فراخوانی می‌شود. احتمالاً برای پشتیبانی از ساختار جدیدتر آگهی‌ها جایگزین FinishAd شده است. |
| `FinishChannelAd` | `id: string` | ✔️ فقط تأیید | برای پایان دادن به آگهی کانالی با ارسال id آن استفاده می‌شود. کلاینت پس از اتمام مدت نمایش آگهی در کانال این متد را صدا می‌زند. |
| `GetAccountData` | `ownerId: int32` | `data: Data` | اطلاعات حساب تبلیغاتی یک کاربر یا ناشر را با ارسال ownerId برمی‌گرداند. معمولاً برای نمایش موجودی، وضعیت حساب و سایر جزئیات در پنل تبلیغات استفاده می‌شود. |
| `GetAccounts` | `pageData: PagingData` | `data: repeated Data` | لیست صفحه‌بندی‌شده‌ای از حساب‌های تبلیغاتی را با استفاده از pageData برمی‌گرداند. احتمالاً در پنل مدیریتی برای مشاهده همه حساب‌های ثبت‌شده به کار می‌رود. |
| `GetAccountsByState` | `state: int32`، `pageData: PagingData` | `data: repeated Data` | حساب‌های تبلیغاتی را بر اساس وضعیت (state) و صفحه‌بندی (pageData) فیلتر و بازمی‌گرداند. برای تفکیک حساب‌های فعال، معلق یا مسدود در پنل مدیریت استفاده می‌شود. |
| `GetActiveAds` | — | `ads: repeated DialogAdOrder` | فهرست تمام آگهی‌های در حال نمایش فعال را بدون نیاز به پارامتر ورودی برمی‌گرداند. کلاینت برای نمایش آگهی‌های جاری به کاربر این RPC را فراخوانی می‌کند. |
| `GetActiveChannelAds` | — | `ads: repeated Order` | لیست آگهی‌های کانالی فعال را برمی‌گرداند. برای واکشی آگهی‌هایی که در حال حاضر در کانال‌ها در حال نمایش هستند استفاده می‌شود. |
| `GetAdData` | `adId: string` | `adData: Ads` | اطلاعات کامل یک آگهی مشخص را با adId دریافت می‌کند. کلاینت برای نمایش جزئیات یا ویرایش یک آگهی خاص این متد را فراخوانی می‌کند. |
| `GetAdDetail` | `title: string`، `from: int64`، `to: int64` | `ads: repeated T_rg_58187` | جزئیات تحلیلی یک آگهی را بر اساس title و بازه زمانی from تا to برمی‌گرداند. احتمالاً برای مشاهده عملکرد آگهی در یک دوره مشخص در پنل گزارش‌گیری استفاده می‌شود. |
| `GetAdProvider` | `peerId: GroupPeer`، `adType: int32`، `adSpot: int32`، `adCount: int64` | `content: repeated Content` | ارائه‌دهنده آگهی مناسب را با توجه به peerId، adType، adSpot و adCount مشخص می‌کند. برای تعیین منبع نمایش آگهی در جایگاه و نوع درخواست‌شده استفاده می‌شود. |
| `GetAdReport` | `adId: string` | `views: int64`، `clicks: int64`، `title: string`، `link: string` | گزارش عملکرد یک آگهی را با adId دریافت می‌کند. تبلیغ‌دهنده برای مشاهده آمار نمایش، کلیک و بازدهی آگهی خود این RPC را فراخوانی می‌کند. |
| `GetAdReportV2` | `adId: string` | `data: T_tu_58187` | نسخه دوم گزارش آگهی را با adId برمی‌گرداند. احتمالاً ساختار داده غنی‌تری نسبت به GetAdReport ارائه می‌دهد و برای گزارش‌های تفصیلی‌تر به کار می‌رود. |
| `GetAdsBySpotAndPlatform` | `spot: int32`، `peerId: GroupPeer` | `data: T_tf_58187` | آگهی‌های مرتبط با یک جایگاه نمایش (spot) و یک peer مشخص را برمی‌گرداند. برای واکشی آگهی‌های متناسب با موقعیت و پلتفرم کاربر استفاده می‌شود. |
| `GetAdsByStateAndSpot` | `pagingData: PagingData`، `state: int32`، `spot: int32` | `ads: repeated Ads` | آگهی‌ها را بر اساس وضعیت (state)، جایگاه (spot) و pagingData فیلتر می‌کند. در پنل مدیریتی برای مشاهده آگهی‌های یک جایگاه خاص با وضعیت مشخص استفاده می‌شود. |
| `GetAllChannelIncomesFactor` | `year: int32`، `month: int32` | `factors: repeated Factor` | فاکتور درآمد تمام کانال‌ها را برای یک ماه و سال مشخص برمی‌گرداند. برای محاسبه و صدور فاکتور تسویه‌حساب درآمد ناشران کانالی به صورت دوره‌ای استفاده می‌شود. |
| `GetAvailableCampaignStartDate` | — | `date: int64` | اولین تاریخ موجود برای شروع یک کمپین تبلیغاتی را بدون نیاز به ورودی برمی‌گرداند. کلاینت هنگام ایجاد کمپین جدید این متد را فراخوانی می‌کند تا زودترین تاریخ ممکن را به کاربر نشان دهد. |
| `GetAwaitingToShowAds` | — | `ads: repeated DialogAdOrder` | لیست آگهی‌هایی که در صف انتظار نمایش هستند را بدون پارامتر برمی‌گرداند. برای مدیریت صف نمایش آگهی‌های تأیید‌شده‌ای که هنوز شروع نشده‌اند استفاده می‌شود. |
| `GetAwaitingToShowChannelAds` | — | `ads: repeated Order` | آگهی‌های کانالی در انتظار نمایش را برمی‌گرداند. مشابه GetAwaitingToShowAds اما مخصوص آگهی‌های کانالی است که هنوز پخش نشده‌اند. |
| `GetBaleCustomAd` | `adId: string` | `ad: Ad` | جزئیات یک آگهی سفارشی بله را با adId دریافت می‌کند. احتمالاً برای واکشی آگهی‌هایی با قالب یا تنظیمات ویژه که توسط تیم بله ایجاد شده‌اند استفاده می‌شود. |
| `GetBonusCodeData` | `code: string` | `data: T_tp_58187` | اطلاعات یک کد تخفیف یا پاداش تبلیغاتی را با ارسال code دریافت می‌کند. کلاینت هنگام اعمال کد تخفیف در فرآیند خرید آگهی این RPC را فراخوانی می‌کند. |
| `GetBonusCodes` | `pageData: PagingData` | `data: repeated T_tp_58187` | لیست صفحه‌بندی‌شده‌ای از کدهای پاداش موجود را با pageData برمی‌گرداند. در پنل مدیریتی برای مشاهده و مدیریت کدهای تخفیف تبلیغاتی استفاده می‌شود. |
| `GetBusinessAds` | `pagingData: PagingData`، `state: int32` | `ads: repeated UpdatedAd` | آگهی‌های کسب‌وکار را بر اساس وضعیت (state) و pagingData برمی‌گرداند. تبلیغ‌دهندگان سازمانی برای مشاهده آگهی‌های خود در وضعیت‌های مختلف این متد را فراخوانی می‌کنند. |
| `GetCRMIssues` | `userIssue: UserIssue`، `allIssue: AllIssue` | `data: repeated T_tw_58187` | مشکلات و تیکت‌های پشتیبانی مرتبط با تبلیغات را بر اساس userIssue یا allIssue دریافت می‌کند. برای مدیریت درخواست‌های پشتیبانی کاربران در سیستم CRM تبلیغات استفاده می‌شود. |
| `GetCampaignAds` | `pagingData: PagingData`، `state: int32` | `data: repeated T_tN_58187` | آگهی‌های کمپینی را بر اساس وضعیت (state) و pagingData به صورت صفحه‌بندی‌شده برمی‌گرداند. کلاینت برای مشاهده و مدیریت آگهی‌های یک کمپین در وضعیت‌های مختلف این RPC را فراخوانی می‌کند. |
| `GetCampaignContentById` | `campaignId: string` | `campaign: Campaign` | برای دریافت جزئیات محتوای یک کمپین تبلیغاتی مشخص با استفاده از campaignId فراخوانی می‌شود. تبلیغ‌دهنده با این RPC می‌تواند متن، تصویر یا سایر محتوای مرتبط با آن کمپین را بازیابی کند. |
| `GetCampaignContents` | `pagingData: PagingData`، `state: int32` | `campaigns: repeated Campaign` | فهرست صفحه‌بندی‌شده‌ای از محتواهای کمپین را بر اساس state (وضعیت) و pagingData برمی‌گرداند. کلاینت این RPC را برای نمایش لیست محتواهای فعال، در انتظار تأیید یا رد‌شده در پنل تبلیغاتی فراخوانی می‌کند. |
| `GetCampaignData` | `campaignId: string` | `data: T_tN_58187` | اطلاعات کلی یک کمپین تبلیغاتی شامل بودجه، بازه زمانی و هدف‌گذاری را با دادن campaignId برمی‌گرداند. تبلیغ‌دهنده پیش از ویرایش یا بررسی وضعیت کمپین این RPC را صدا می‌زند. |
| `GetChannelAds` | `groupId: Peer` | `ads: repeated T_ez_58187` | فهرست آگهی‌هایی که در حال حاضر برای کانال مشخص‌شده با groupId در حال نمایش هستند را برمی‌گرداند. مدیر کانال با این RPC می‌تواند ببیند چه تبلیغاتی در کانالش نشان داده می‌شود. |
| `GetChannelEarnMoneyInfo` | `groupId: Peer` | `currentMonthIncome: double`، `notPaidIncome: double`، `adCount: int64`، `adCountUpdateDate: int64` | اطلاعات برنامه کسب درآمد از تبلیغات برای کانال مشخص‌شده با groupId را برمی‌گرداند. مدیر کانال از این RPC برای مشاهده شرایط، نرخ‌ها و جزئیات طرح درآمدزایی کانالش استفاده می‌کند. |
| `GetChannelEarnMoneyStatus` | `groupId: Peer` | `status: int32` | وضعیت فعال یا غیرفعال بودن درآمدزایی از تبلیغات برای کانال مشخص‌شده با groupId را اعلام می‌کند. کلاینت پیش از نمایش گزینه‌های درآمدزایی در تنظیمات کانال این RPC را فراخوانی می‌کند. |
| `GetChannelGraphReport` | `peerId: GroupPeer`، `startTime: int64`، `endTime: int64` | `viewGraph: repeated ViewGraph` | گزارش نموداری آماری از عملکرد تبلیغات کانال در بازه زمانی مشخص‌شده توسط startTime و endTime برای peerId برمی‌گرداند. از این RPC در داشبورد تحلیل کانال برای رسم نمودار بازدید و درآمد استفاده می‌شود. |
| `GetChannelIncomeReport` | `peerId: GroupPeer` | `incomeReports: repeated IncomeReport` | گزارش کلی درآمد حاصل از تبلیغات کانال مشخص‌شده با peerId را برمی‌گرداند. مدیر کانال برای مشاهده مجموع درآمد تبلیغاتی خود این RPC را فراخوانی می‌کند. |
| `GetChannelOwnerBankInformation` | `channelId: GroupPeer` | `userId: int32`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string`، `firstName: string`، `lastName: string`، `phone: string`، `state: int32`، `reason: int32`، `channelNick: string` | اطلاعات حساب بانکی ثبت‌شده مالک کانال با channelId را برمی‌گرداند تا درآمد تبلیغاتی به آن واریز شود. این RPC هنگام نمایش یا تأیید اطلاعات بانکی در فرآیند تسویه‌حساب فراخوانی می‌شود. |
| `GetChannelShowAdCategoryFilter` | `peerId: GroupPeer` | `categories: repeated Category` | فیلترهای دسته‌بندی تبلیغات مجاز برای نمایش در کانال مشخص‌شده با peerId را برمی‌گرداند. مدیر کانال با این RPC می‌تواند ببیند کدام دسته‌های تبلیغاتی در کانالش مجاز یا مسدود هستند. |
| `GetChannelShowAdPermissions` | `peerId: GroupPeer` | `showSponsoredAd: bool`، `verifiedUserId: int32` | مجوزهای نمایش تبلیغ در کانال مشخص‌شده با peerId را برمی‌گرداند. کلاینت پیش از شروع نمایش آگهی در کانال این RPC را صدا می‌زند تا بررسی کند آیا کانال واجد شرایط است یا خیر. |
| `GetChannelShowAdTimeRestrict` | `peerId: GroupPeer` | `data: T_tS_58187` | محدودیت‌های زمانی نمایش تبلیغ (مثلاً ساعت‌های مجاز) برای کانال مشخص‌شده با peerId را برمی‌گرداند. این RPC هنگام زمان‌بندی ارسال آگهی توسط سیستم تبلیغاتی بله مورد استفاده قرار می‌گیرد. |
| `GetChannelsViewReport` | `startTime: int64`، `endTime: int64` | `channelsView: repeated ChannelsView` | گزارش تجمیعی بازدیدها و نمایش آگهی‌ها در تمام کانال‌های مرتبط را در بازه زمانی startTime تا endTime برمی‌گرداند. تبلیغ‌دهنده از این RPC برای ارزیابی کلی عملکرد کمپین‌هایش استفاده می‌کند. |
| `GetConfig` | — | `config: string` | تنظیمات و پارامترهای کلی سرویس تبلیغات بله را بدون نیاز به ورودی خاصی برمی‌گرداند. کلاینت هنگام راه‌اندازی یا بارگذاری پنل تبلیغاتی این RPC را برای دریافت پیکربندی سرور فراخوانی می‌کند. |
| `GetCreditHistory` | `ownerId: int32`، `startTime: int64`، `endTime: int64` | `creditHistories: repeated CreditHistory` | تاریخچه اعتبار مصرف‌شده و شارژشده حساب تبلیغاتی ownerId را در بازه زمانی startTime تا endTime برمی‌گرداند. تبلیغ‌دهنده از این RPC برای مشاهده سوابق مالی و حسابداری اعتبار تبلیغاتی خود استفاده می‌کند. |
| `GetCreditableAccounts` | `pageData: PagingData` | `data: repeated Data` | فهرست صفحه‌بندی‌شده‌ای از حساب‌هایی که امکان شارژ اعتبار تبلیغاتی دارند را با استفاده از pageData برمی‌گرداند. این RPC احتمالاً در پنل مدیریت برای انتخاب حساب هدف جهت اعمال اعتبار فراخوانی می‌شود. |
| `GetCustomIncomes` | `startTime: int64`، `endTime: int64` | `records: repeated T_tV_58187` | گزارش درآمدهای سفارشی (خارج از مسیر معمول) ثبت‌شده در بازه زمانی startTime تا endTime را برمی‌گرداند. این RPC احتمالاً در ابزارهای مدیریتی داخلی بله برای مشاهده درآمدهای ویژه یا توافقی استفاده می‌شود. |
| `GetDialogAdOrderDetails` | — | `dialogAdOrder: repeated DialogAdOrder` | جزئیات سفارش تبلیغ دیالوگی (آگهی نمایش داده‌شده در صفحه مکالمات) را بدون ورودی خاص برمی‌گرداند. کلاینت هنگام نمایش صفحه خلاصه سفارش آگهی دیالوگ پیش از پرداخت این RPC را فراخوانی می‌کند. |
| `GetDialogAdOrderPaymentToken` | `id: string`، `rialAmount: int64`، `coinAmount: int64` | `token: string` | توکن پرداخت برای سفارش آگهی دیالوگ را با دریافت id سفارش، rialAmount و coinAmount صادر می‌کند. این RPC پیش از هدایت کاربر به درگاه پرداخت برای تسویه هزینه تبلیغ دیالوگ فراخوانی می‌شود. |
| `GetFactorEligibleAds` | `tBegin: int64`، `tEnd: int64` | `ads: repeated T_th_58187` | فهرست آگهی‌هایی که در بازه زمانی tBegin تا tEnd واجد شرایط صدور فاکتور هستند را برمی‌گرداند. این RPC احتمالاً در فرآیند صدور صورت‌حساب دوره‌ای برای تبلیغ‌دهندگان مورد استفاده قرار می‌گیرد. |
| `GetMyContactPopularChannels` | — | `channels: repeated T_tk_58187` | فهرست کانال‌های محبوب در میان مخاطبان کاربر را بدون ورودی خاص برمی‌گرداند. این RPC برای نمایش پیشنهادهای کانال بر اساس علایق شبکه اجتماعی کاربر در صفحه کشف محتوا فراخوانی می‌شود. |
| `GetOnBoardingChannels` | — | `channels: repeated Channel`، `showOnBoarding: bool` | فهرست کانال‌های پیشنهادی برای نمایش در مرحله آنبوردینگ (ثبت‌نام اولیه) کاربر را برمی‌گرداند. بله از این RPC برای کمک به کاربران تازه‌وارد در انتخاب کانال‌های اولیه جهت عضویت استفاده می‌کند. |
| `GetOnboardingPeers` | — | `peers: repeated T_tm_58187` | فهرست peer های پیشنهادی (کاربران یا گروه‌ها) برای نمایش در فرآیند آنبوردینگ را بدون ورودی خاص برمی‌گرداند. این RPC برای آشنا کردن کاربران جدید با افراد یا گروه‌های مرتبط فراخوانی می‌شود. |
| `GetOnboardingPosts` | `categoryId: int32` | `posts: repeated Post` | پست‌های پیشنهادی برای نمایش در فرآیند آنبوردینگ بر اساس categoryId مشخص را برمی‌گرداند. بله از این RPC برای نمایش محتوای جذاب متناسب با علایق انتخابی کاربر تازه‌وارد استفاده می‌کند. |
| `GetOnboardingSpotData` | `onboardingSpot: int32`، `suggestedPeerType: int32` | `contactChannels: ContactChannels`، `suggestedChannels: SuggestedChannels` | داده‌های نمایشی یک موقعیت (spot) خاص در صفحه آنبوردینگ را با استفاده از onboardingSpot و suggestedPeerType برمی‌گرداند. این RPC برای بارگذاری پیشنهادهای هدفمند در هر بخش از فرآیند معرفی اولیه به کاربران جدید فراخوانی می‌شود. |
| `GetOwnerIdByPhone` | `phoneNumber: string` | `userId: int32` | با ارسال phoneNumber، شناسه مالک حساب تبلیغاتی متناظر با آن شماره تلفن را بازیابی می‌کند. احتمالاً برای تطابق کاربر در فرایند ثبت‌نام یا انتقال مالکیت کانال استفاده می‌شود. |
| `GetPaidAdsByTime` | `pagingData: PagingData`، `startTime: int64`، `endTime: int64` | `ads: repeated T_th_58187` | فهرست آگهی‌های پرداخت‌شده را در بازه زمانی مشخص (startTime تا endTime) با صفحه‌بندی pagingData برمی‌گرداند. برای گزارش‌گیری مالی و مرور سابقه تبلیغات پرداخت‌شده استفاده می‌شود. |
| `GetPaymentData` | `adId: string` | `data: T_tI_58187` | با دریافت adId، اطلاعات پرداخت مرتبط با یک آگهی خاص را برمی‌گرداند. برای نمایش جزئیات فاکتور یا وضعیت مالی یک تبلیغ به کار می‌رود. |
| `GetPeriodCapacityData` | `beginDate: int64`، `endDate: int64` | `data: repeated T_te_58187` | ظرفیت موجود برای انتشار تبلیغات را در بازه زمانی (beginDate تا endDate) بازیابی می‌کند. برای برنامه‌ریزی کمپین و بررسی ظرفیت تبلیغاتی در تقویم استفاده می‌شود. |
| `GetUserAds` | `pagingData: PagingData`، `userId: int32` | `ads: repeated Ads` | فهرست آگهی‌های یک کاربر مشخص (userId) را با صفحه‌بندی pagingData برمی‌گرداند. برای نمایش پنل مدیریت آگهی‌های تبلیغ‌دهنده استفاده می‌شود. |
| `GetUserAuthData` | `channelId: GroupPeer` | `userId: int32`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string`، `firstName: string`، `lastName: string`، `phone: string`، `state: int32`، `reason: int32`، `channelNick: string` | اطلاعات احراز هویت کاربر مرتبط با channelId (از نوع GroupPeer) را بازیابی می‌کند. احتمالاً برای بررسی وضعیت تأیید هویت ناشر کانال در سیستم درآمدزایی استفاده می‌شود. |
| `GetUserCampaigns` | `pagingData: PagingData`، `userId: int32` | `data: repeated T_tN_58187` | فهرست کمپین‌های تبلیغاتی یک کاربر (userId) را با صفحه‌بندی pagingData برمی‌گرداند. برای نمایش داشبورد کمپین‌های فعال و گذشته تبلیغ‌دهنده به کار می‌رود. |
| `GetUserOnboardingScenario` | — | `scenario: int32` | سناریوی راهنمای اولیه (onboarding) مخصوص کاربر جاری را بدون نیاز به پارامتر ورودی بازیابی می‌کند. برای نمایش مراحل معرفی سیستم تبلیغات به کاربران تازه‌وارد استفاده می‌شود. |
| `GetUserStatus` | `userId: int64` | `status: int32` | وضعیت حساب تبلیغاتی کاربر را با دریافت userId بررسی می‌کند. برای تشخیص اینکه آیا کاربر مجاز به ایجاد یا مدیریت تبلیغات است استفاده می‌شود. |
| `GetUsersAuthDataByState` | `state: int32` | `usersData: repeated UsersData` | فهرست کاربرانی که داده احراز هویتشان در وضعیت خاصی (state) قرار دارد را برمی‌گرداند. برای بررسی و مدیریت درخواست‌های تأیید هویت ناشران توسط ادمین استفاده می‌شود. |
| `GetVODContents` | — | `contents: repeated T_tB_58187` | محتواهای ویدیویی (VOD) موجود برای استفاده در تبلیغات را بدون نیاز به پارامتر ورودی بازیابی می‌کند. احتمالاً برای انتخاب محتوای ویدیویی هنگام ساخت آگهی تصویری استفاده می‌شود. |
| `ModifyCapacity` | `date: int64`، `val: int32` | ✔️ فقط تأیید | ظرفیت انتشار تبلیغات را برای تاریخ مشخصی (date) با مقدار val تغییر می‌دهد. ادمین از این متد برای افزایش یا کاهش ظرفیت روزانه تبلیغات استفاده می‌کند. |
| `RegisterForEarnMoney` | `info: T_eY_58187` | ✔️ فقط تأیید | کاربر را برای برنامه کسب درآمد از تبلیغات ثبت‌نام می‌کند و اطلاعات مورد نیاز را از طریق فیلد info ارسال می‌کند. برای ناشرانی که می‌خواهند از طریق کانال‌شان درآمد کسب کنند استفاده می‌شود. |
| `SendAdminMessage` | `receiver: int32`، `messageText: string`، `fileId: int64`، `fileName: string` | ✔️ فقط تأیید | یک پیام ادمین را با متن messageText و احتمالاً یک فایل (fileId و fileName) به کاربر receiver ارسال می‌کند. برای اطلاع‌رسانی رسمی سیستم به تبلیغ‌دهندگان یا ناشران استفاده می‌شود. |
| `SendFactorMessage` | `channelId: int32`، `messageText: string`، `fileId: int64`، `fileName: string`، `year: int32`، `month: int32` | ✔️ فقط تأیید | یک پیام فاکتور ماهانه (با year و month مشخص) را به channelId ارسال می‌کند و می‌تواند متن messageText و یک فایل پیوست (fileId و fileName) داشته باشد. برای ارسال صورتحساب درآمد تبلیغاتی ماهانه به ناشران کانال استفاده می‌شود. |
| `SetAdTarget` | `adId: string`، `targeting: Targeting` | ✔️ فقط تأیید | تنظیمات هدف‌گذاری (targeting) یک آگهی را بر اساس adId به‌روزرسانی می‌کند. تبلیغ‌دهنده از این متد برای مشخص کردن مخاطب هدف آگهی خود استفاده می‌کند. |
| `SetChannelInvoiceInfo` | `peerId: GroupPeer`، `nationalCode: string`، `address: string`، `postalCode: string`، `name: string`، `tag1: int32`، `tag2: int32`، `birthDate: string` | ✔️ فقط تأیید | اطلاعات فاکتور یک کانال مانند کد ملی، آدرس، کد پستی و تاریخ تولد را برای peerId (از نوع GroupPeer) ذخیره می‌کند. برای تکمیل اطلاعات هویتی ناشر جهت صدور فاکتور رسمی تبلیغاتی استفاده می‌شود. |
| `SetChannelOwnerBankInformation` | `channelId: GroupPeer`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string` | ✔️ فقط تأیید | اطلاعات بانکی مالک کانال شامل کد ملی، تاریخ تولد، آدرس، کد پستی و شماره حساب بانک ملی (melliAccountNumber) را برای channelId ثبت می‌کند. برای راه‌اندازی پرداخت درآمد تبلیغاتی به ناشر استفاده می‌شود. |
| `SetOnBoardingChannels` | `channels: repeated Channel` | ✔️ فقط تأیید | فهرستی از کانال‌ها (channels) را به عنوان کانال‌های پیشنهادی در فرایند راهنمای اولیه تعیین می‌کند. برای تنظیم کانال‌هایی که به کاربران تازه‌وارد در مرحله onboarding نشان داده می‌شود استفاده می‌شود. |
| `SetUserAuthData` | `channelId: GroupPeer`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string` | ✔️ فقط تأیید | اطلاعات احراز هویت کاربر (کد ملی، تاریخ تولد، آدرس، کد پستی و شماره حساب بانکی) را برای channelId مشخص ثبت یا به‌روزرسانی می‌کند. پیش‌نیاز فعال‌سازی درآمدزایی تبلیغاتی برای ناشران کانال است. |
| `StartAd` | `adId: string`، `startTime: int64`، `platform: int32`، `autoFinish: bool` | ✔️ فقط تأیید | یک آگهی (adId) را از زمان startTime روی پلتفرم (platform) مشخص شروع می‌کند و می‌توان autoFinish را برای پایان خودکار فعال کرد. برای راه‌اندازی کمپین تبلیغاتی پس از تأیید و پرداخت استفاده می‌شود. |
| `StartBaleCustomAd` | `id: string`، `platform: int32`، `pic: string`، `title: string`، `description: string`، `link: string`، `startTime: int64`، `viewCount: int32`، `clickCount: int32` | `ad: Ad` | یک آگهی سفارشی بله با مشخصات کامل (عنوان، توضیحات، لینک، تصویر، تعداد نمایش viewCount و کلیک clickCount) را از startTime راه‌اندازی می‌کند. برای اجرای کمپین‌های تبلیغاتی اختصاصی با ظرفیت از پیش تعریف‌شده استفاده می‌شود. |
| `StartChannelAdFromOrder` | `id: string`، `title: string`، `description: string`، `link: string`، `startTime: int64`، `viewCount: int32`، `clickCount: int32`، `platform: int32` | ✔️ فقط تأیید | یک تبلیغ کانالی را بر اساس سفارش موجود (id) با مشخصات عنوان، توضیحات، لینک، زمان شروع، تعداد نمایش و کلیک آغاز می‌کند. برای تبدیل سفارش تبلیغ کانالی به یک کمپین فعال استفاده می‌شود. |
| `StartFromOrder` | `id: string`، `platform: int32`، `pic: string`، `title: string`، `description: string`، `link: string`، `startTime: int64`، `viewCount: int64`، `clickCount: int64` | ✔️ فقط تأیید | یک آگهی استاندارد را بر اساس سفارش (id) با تمام مشخصات محتوایی (تصویر، عنوان، توضیحات، لینک) و ظرفیت (viewCount و clickCount) از startTime راه‌اندازی می‌کند. برای اجرای کمپین‌های تبلیغاتی که از طریق پنل سفارش‌دهی ثبت شده‌اند استفاده می‌شود. |
| `StopAllBaleCustomAds` | — | ✔️ فقط تأیید | تمام آگهی‌های سفارشی بله در حال اجرا را بدون نیاز به پارامتر ورودی متوقف می‌کند. ادمین از این متد برای توقف اضطراری همه کمپین‌های سفارشی فعال استفاده می‌کند. |
| `SubmitChannelAdOrder` | `order: Order` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که تبلیغ‌دهنده یک سفارش تبلیغاتی برای انتشار در کانال ثبت می‌کند؛ اطلاعات سفارش از طریق فیلد order از نوع Order ارسال می‌شود. |
| `SubmitDialogAdOrder` | `dialogAdOrder: DialogAdOrder` | ✔️ فقط تأیید | برای ثبت سفارش تبلیغاتی در فضای دیالوگ (چت خصوصی یا باکس پیام) استفاده می‌شود؛ جزئیات سفارش در فیلد dialogAdOrder از نوع DialogAdOrder ارسال می‌گردد. |
| `SubmitPhotoForBaleCustomAd` | `adId: string`، `pic: string` | `ad: Ad` | برای بارگذاری تصویر مرتبط با یک آگهی سفارشی بله فراخوانی می‌شود؛ کلاینت adId آگهی و آدرس یا شناسه تصویر را در فیلد pic ارسال می‌کند تا تصویر با تبلیغ مشخص مرتبط شود. |
| `UpdateBusinessAd` | `updatedAd: UpdatedAd` | ✔️ فقط تأیید | هنگامی استفاده می‌شود که تبلیغ‌دهنده بخواهد اطلاعات یک آگهی تجاری موجود را ویرایش کند؛ اطلاعات به‌روزشده از طریق فیلد updatedAd از نوع UpdatedAd ارسال می‌شود. |
| `UpdateCRMIssue` | `addIssue: AddIssue`، `addComment: AddComment`، `resolveIssue: ResolveIssue`، `ignoreUser: IgnoreUser` | ✔️ فقط تأیید | برای مدیریت مسائل CRM مرتبط با تبلیغات به‌کار می‌رود و امکان افزودن مشکل (addIssue)، ثبت نظر (addComment)، حل مشکل (resolveIssue) یا نادیده گرفتن کاربر (ignoreUser) را در یک درخواست فراهم می‌کند. |
| `UpdateClick` | `id: string`، `count: int32`، `peer: ExPeer` | ✔️ فقط تأیید | برای به‌روزرسانی تعداد کلیک‌های ثبت‌شده روی یک تبلیغ استفاده می‌شود؛ کلاینت id تبلیغ، تعداد کلیک‌ها (count) و اطلاعات peer کاربر کلیک‌کننده را ارسال می‌کند. |
| `UpdateGroupStatus` | `groupId: Peer` | ✔️ فقط تأیید | احتمالاً برای به‌روزرسانی وضعیت یک گروه در سامانه تبلیغات فراخوانی می‌شود؛ groupId از نوع Peer شناسه گروه مورد نظر را مشخص می‌کند. |
| `UpdateView` | `id: string`، `count: int32`، `peerId: GroupPeer` | `isSuccessful: bool` | برای ثبت و به‌روزرسانی تعداد بازدیدهای یک تبلیغ استفاده می‌شود؛ کلاینت id تبلیغ، تعداد بازدید (count) و شناسه گروه بازدیدکننده (peerId از نوع GroupPeer) را ارسال می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-anonymous_contact-v1-anonymouscontact"></a>

## تماس ناشناس — `bale.anonymous_contact.v1.AnonymousContact`

این سرویس امکان برقراری ارتباط ناشناس میان کاربران بله را فراهم می‌کند؛ به‌گونه‌ای که هویت طرفین پنهان بماند. کلاینت از این سرویس برای بازیابی اطلاعات صفحه تماس ناشناس کاربران استفاده می‌کند.

نام‌فضای پایتون: `client.anonymous_contact` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetUserAnonymousContactPage` | `userId: int32`، `serviceMessageRid: int64`، `serviceMessageDate: int64` | `countryNumber: string`، `registerAccountTime: ExtAnonymousContactInt64Value`، `lastTimeNameChanged: ExtAnonymousContactInt64Value`، `lastTimeAvatarChanged: ExtAnonymousContactInt64Value`، `commonGroups: repeated ExtAnonymousContactGroupPeer`، `extraInfo: repeated ExtAnonymousContactExtraInfo` | کلاینت این RPC را برای دریافت صفحه تماس ناشناس یک کاربر فراخوانی می‌کند؛ با ارسال userId، serviceMessageRid و serviceMessageDate، اطلاعات لازم برای نمایش یا ورود به صفحه تماس ناشناس آن کاربر بازگردانده می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-appzar-v1-appzar"></a>

## مینی‌اپ‌ها و بات‌ها (Appzar) — `bale.appzar.v1.Appzar`

این سرویس مدیریت مینی‌اپ‌ها (Mini Apps) و باتانه بله را فراهم می‌کند. کلاینت از طریق این سرویس می‌تواند دکمه‌های منو باتان را دریافت، آدرس بارگذاری مینی‌اپ را تهیه، و متدهای سفارشی باتان را فراخوانی کند.

نام‌فضای پایتون: `client.appzar` — تعداد متد: 3

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetMenuButton` | `botUserId: int64` | `menuButton: T_LF` | کلاینت این RPC را با ارسال botUserId فراخوانی می‌کند تا دکمه‌ی منوی تعریف‌شده برای یک بات را دریافت کند؛ معمولاً هنگام باز کردن پنجره چت با بات برای نمایش دکمه‌ی منو کنار فیلد متن استفاده می‌شود. |
| `GetMiniAppUrl` | `botUserId: int64`، `screenMode: int64`، `themeParams: ThemeParams`، `main: Main`، `menuButton: MenuButton`، `keyboardButton: KeyboardButton`، `directLink: DirectLink` | `url: bytes`، `screenMode: int64`، `queryId: StringValue` | وقتی کاربر می‌خواهد مینی‌اپ یک بات را باز کند، کلاینت با ارسال botUserId، screenMode، themeParams و سایر پارامترهای نمایشی این RPC را صدا می‌زند تا URL معتبر بارگذاری مینی‌اپ را از سرور دریافت کند. |
| `InvokeCustomMethod` | `botUserId: int64`، `method: bytes`، `params: bytes` | `data: bytes` | این RPC برای فراخوانی متدهای اختصاصی یک بات به‌کار می‌رود؛ کلاینت نام متد (method) و پارامترهای آن (params) را به‌صورت bytes همراه با botUserId ارسال می‌کند تا منطق سفارشی تعریف‌شده توسط بات اجرا شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-auth-v1-auth"></a>

## احراز هویت و مدیریت حساب — `bale.auth.v1.Auth`

این سرویس مسئول ورود، ثبت‌نام، خروج و مدیریت امنیت حساب کاربری در پیام‌رسان بله است. عملیات‌هایی مانند تأیید شماره تلفن، احراز هویت دو مرحله‌ای، تغییر رمز عبور و مدیریت نشست‌های فعال از طریق این سرویس انجام می‌شود.

نام‌فضای پایتون: `client.auth` — تعداد متد: 26

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `ChangePhone` | `phoneNumber: int64`، `code: string`، `transactionHash: string` | ✔️ فقط تأیید | وقتی کاربر می‌خواهد شماره تلفن مرتبط با حساب خود را تغییر دهد، این RPC فراخوانی می‌شود. کلاینت باید phoneNumber جدید، code تأیید و transactionHash دریافت‌شده از مرحله قبل را ارسال کند. |
| `DeleteAccount` | `code: string`، `transactionHash: string` | ✔️ فقط تأیید | برای حذف دائمی حساب کاربری استفاده می‌شود؛ کلاینت باید code تأیید و transactionHash مرحله قبل را ارائه دهد تا هویت کاربر تأیید شود. |
| `DisableTwoFactorAuthentication` | — | ✔️ فقط تأیید | وقتی کاربر می‌خواهد احراز هویت دو مرحله‌ای را غیرفعال کند، این RPC بدون هیچ ورودی خاصی فراخوانی می‌شود و تنظیم امنیتی را برای حساب جاری حذف می‌کند. |
| `EnableTwoFactorAuthentication` | `email: string`، `password: string` | ✔️ فقط تأیید | برای فعال‌سازی احراز هویت دو مرحله‌ای با ارسال email و password مورد نظر استفاده می‌شود تا یک لایه امنیتی اضافه به حساب کاربر اضافه شود. |
| `GetAuthSessions` | — | `userAuths: repeated UserAuth` | کلاینت این RPC را برای دریافت لیست تمام نشست‌های (session) فعال حساب کاربری فراخوانی می‌کند تا کاربر بتواند دستگاه‌های متصل خود را مشاهده و مدیریت کند. |
| `GetBajeBamTicket` | `expDateTime: int64`، `mobileNo: string` | `ticket: string` | برای دریافت یک ticket موقت جهت ورود به سرویس BajeBam (احتمالاً یک سرویس جانبی بله) با ارسال expDateTime و mobileNo استفاده می‌شود. |
| `GetBaleTicket` | `expDateTime: int64`، `mobileNo: string`، `clientId: string` | `redirectUrl: string` | این RPC یک ticket احراز هویت برای سرویس‌های بله صادر می‌کند؛ کلاینت expDateTime، mobileNo و clientId را ارسال می‌کند تا توکن دسترسی موقت دریافت نماید. |
| `GetJWTToken` | — | `jwt: StringValue` | کلاینت پس از احراز هویت موفق، این RPC را بدون پارامتر ورودی فراخوانی می‌کند تا یک توکن JWT برای استفاده در درخواست‌های بعدی API دریافت کند. |
| `GetTicket` | `jsonRequest: string`، `jsonSign: string` | `redirectUrl: string` | برای دریافت ticket احراز هویت بر اساس یک درخواست JSON امضاشده (jsonRequest و jsonSign) استفاده می‌شود؛ احتمالاً برای ورود از طریق سرویس‌های شخص ثالث یا SSO. |
| `GetUserIdToken` | `ticket: string` | `token: string`، `userId: int32`، `source: int32`، `service: string` | با ارسال ticket دریافت‌شده از مراحل قبل، این RPC یک توکن شناسه کاربری برمی‌گرداند که در سیستم‌های دیگر بله برای شناسایی کاربر به کار می‌رود. |
| `IsTwoFactorAuthenticationEnabled` | — | `isEnabled: bool` | کلاینت این RPC را فراخوانی می‌کند تا بررسی کند آیا احراز هویت دو مرحله‌ای برای حساب جاری فعال است یا خیر، معمولاً پیش از نمایش تنظیمات امنیتی به کاربر. |
| `LogOut` | — | `futureAuthToken: StringValue` | برای خروج از حساب کاربری و ابطال نشست جاری بدون ارسال هیچ پارامتری فراخوانی می‌شود؛ معمولاً پس از تأیید کاربر برای خروج استفاده می‌شود. |
| `RecoverPassword` | `transactionHash: string` | `emailPattern: string` | در فرآیند بازیابی رمز عبور، با ارسال transactionHash مرحله تأیید قبلی، این RPC اطلاعات لازم برای تنظیم رمز جدید را برمی‌گرداند. |
| `SendChangePhoneVerificationCode` | — | `transactionHash: string`، `activationType: int32` | وقتی کاربر درخواست تغییر شماره تلفن می‌دهد، این RPC کد تأیید را برای شماره جدید ارسال می‌کند تا فرآیند ChangePhone تکمیل شود. |
| `SendDeleteAccountVerificationCode` | — | `transactionHash: string`، `activationType: int32` | پیش از حذف حساب کاربری، کلاینت این RPC را فراخوانی می‌کند تا کد تأیید برای کاربر ارسال شود و هویت او احراز گردد. |
| `SetNewPassword` | `newPassword: string`، `transactionHash: string` | ✔️ فقط تأیید | پس از تأیید بازیابی رمز عبور، کلاینت این RPC را با newPassword جدید و transactionHash مرحله قبل فراخوانی می‌کند تا رمز عبور حساب به‌روز شود. |
| `SignOut` | — | ✔️ فقط تأیید | برای خروج از حساب و ابطال نشست جاری استفاده می‌شود؛ مشابه LogOut اما احتمالاً در جریان‌های متفاوت اپلیکیشن به‌کار می‌رود. |
| `SignUp` | `transactionHash: string`، `name: string`، `sex: int32`، `password: StringValue` | `user: User`، `config: T_TS`، `jwt: StringValue` | برای ثبت‌نام کاربر جدید استفاده می‌شود؛ کلاینت transactionHash، name، sex و اختیاری password را ارسال می‌کند تا حساب کاربری ایجاد و توکن احراز هویت دریافت شود. |
| `StartPhoneAuth` | `phoneNumber: int64`، `appId: int32`، `apiKey: string`، `deviceHash: bytes`، `deviceTitle: string`، `timeZone: StringValue`، `preferredLanguages: repeated string`، `imeiList: Value`، `sendCodeType: int32`، `options: repeated int32` | `transactionHash: string`، `isRegistered: bool`، `activationType: int32`، `isImeiOk: bool`، `sentCodeType: int32`، `codeExpirationDate: Int64Value_1`، `nextSendCodeType: int32`، `nextSendCodeWaitTime: Int64Value_1`، `codeTimeout: Int32Value_1`، `exInfoAddress: repeated ExInfoAddress`، `availableSendCodeTypes: repeated int32` | نقطه شروع فرآیند ورود یا ثبت‌نام است؛ کلاینت phoneNumber، appId، apiKey، deviceHash و اطلاعات دستگاه را ارسال می‌کند تا کد OTP ارسال و transactionHash دریافت شود. |
| `TerminateAllSessions` | — | ✔️ فقط تأیید | برای خروج همزمان از تمام دستگاه‌ها و ابطال همه نشست‌های فعال حساب کاربری استفاده می‌شود؛ معمولاً در موقعیت‌های امنیتی حساس. |
| `TerminateSession` | `id: int32` | ✔️ فقط تأیید | برای پایان‌دادن به یک نشست مشخص با ارسال id آن نشست فراخوانی می‌شود، تا کاربر بتواند از یک دستگاه خاص خارج شود. |
| `ValidateCode` | `transactionHash: string`، `code: string`، `isJwt: BoolValue_1`، `futureAuthTokens: repeated string` | `user: User`، `config: T_TS`، `jwt: StringValue` | پس از دریافت کد OTP، کلاینت این RPC را با transactionHash و code فراخوانی می‌کند تا کد تأیید شود و توکن احراز هویت (یا JWT در صورت تنظیم isJwt) دریافت گردد. |
| `ValidatePassword` | `transactionHash: string`، `password: string`، `isJwt: BoolValue_1` | `user: User`، `config: T_TS`، `jwt: StringValue` | وقتی احراز هویت دو مرحله‌ای فعال است، پس از ValidateCode، کلاینت این RPC را با transactionHash و password ارسال می‌کند تا مرحله نهایی ورود تکمیل شود. |
| `VerifyEmail` | `email: string`، `code: string` | ✔️ فقط تأیید | برای تأیید آدرس ایمیل در فرآیند فعال‌سازی احراز هویت دو مرحله‌ای استفاده می‌شود؛ کلاینت email و code تأیید ارسال‌شده به آن را ارائه می‌دهد. |
| `VerifyPassword` | `password: string` | ✔️ فقط تأیید | برای تأیید هویت کاربر با ارسال password جاری استفاده می‌شود؛ احتمالاً پیش از عملیات‌های حساسی مثل تغییر تنظیمات امنیتی یا حذف حساب فراخوانی می‌شود. |
| `VerifyPasswordRecovery` | `code: string`، `transactionHash: string` | ✔️ فقط تأیید | هنگامی که کاربر فرآیند بازیابی رمز عبور را آغاز کرده و کد تأیید دریافت کرده است، این RPC با ارسال code و transactionHash فراخوانی می‌شود تا صحت کد بازیابی تأیید شود و امکان تنظیم رمز جدید فراهم گردد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-balebank-v1-goldgiftpacket"></a>

## پاکت طلای هدیه — `bale.balebank.v1.GoldGiftPacket`

این سرویس امکان ارسال، باز کردن و مشاهده نتایج پاکت‌های هدیه طلا در پیام‌رسان بله را فراهم می‌کند. کاربران می‌توانند مقداری طلا را به صورت پاکت هدیه برای یک peer ارسال کنند و دریافت‌کنندگان پاکت را باز کرده و برندگان را مشاهده نمایند.

نام‌فضای پایتون: `client.gold_gift_packet` — تعداد متد: 3

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetWinnerIDs` | `giftPacketId: int64` | `winners: repeated Winner` | زمانی فراخوانی می‌شود که کلاینت می‌خواهد فهرست شناسه کاربران برنده یک پاکت طلای هدیه مشخص را دریافت کند؛ با ارسال giftPacketId، سرور لیست برندگان آن پاکت را بازمی‌گرداند. |
| `OpenGoldGiftPacket` | `giftPacketId: int64` | `openedCount: int64`، `selfWinAmount: int64`، `rank: int64`، `giftReceivers: repeated GiftReceiver`، `status: int32`، `verificationDeadline: Int64Value` | هنگامی فراخوانی می‌شود که کاربر روی یک پاکت طلای هدیه کلیک کرده و قصد باز کردن آن را دارد؛ با ارسال giftPacketId، سرور سهم طلای کاربر را محاسبه و به کیف پول او واریز می‌کند. |
| `SendGoldGiftPacket` | `amount: int64`، `count: int64`، `description: string`، `givingType: int32`، `randomId: int64`، `peer: Peer` | `giftPacketId: int64` | زمانی فراخوانی می‌شود که کاربر می‌خواهد یک پاکت هدیه طلا برای یک peer (گروه یا کاربر) ارسال کند؛ با مشخص کردن amount (مقدار طلا)، count (تعداد پاکت‌ها)، givingType (نوع توزیع) و description، پاکت هدیه ایجاد و ارسال می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-balebank-v1-goldwallet"></a>

## کیف پول طلا — `bale.balebank.v1.GoldWallet`

این سرویس امکان مدیریت کیف پول طلای کاربر در پیام‌رسان بله را فراهم می‌کند. از طریق این سرویس می‌توان به اطلاعات موجودی طلای کاربر دسترسی داشت.

نام‌فضای پایتون: `client.gold_wallet` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetBalance` | — | `balance: int64` | کلاینت این متد را برای دریافت موجودی فعلی کیف پول طلای کاربر فراخوانی می‌کند. معمولاً هنگام نمایش صفحه کیف پول طلا یا بررسی موجودی قبل از انجام تراکنش استفاده می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-bank-v1-bank"></a>

## بانک و پرداخت — `bale.bank.v1.Bank`

این سرویس عملیات بانکی و پرداخت درون‌برنامه‌ای بله را فراهم می‌کند، از جمله خرید شارژ، استعلام موجودی کارت، دریافت توکن‌های پرداخت از درگاه‌های مختلف و انتقال وجه بین کاربران.

نام‌فضای پایتون: `client.bank` — تعداد متد: 17

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `BuyFastCharge` | `amount: int64`، `phoneNumber: StringValue`، `operator: int32`، `chargeType: int32` | `transactionDate: int64`، `refrenceNumber: string`، `pin: StringValue`، `serial: StringValue` | زمانی فراخوانی می‌شود که کاربر می‌خواهد مستقیماً از کیف پول بله برای یک شماره تلفن (phoneNumber) با مبلغ (amount)، اپراتور (operator) و نوع شارژ (chargeType) مشخص، شارژ تلفن همراه خریداری کند. |
| `GetCardRemain` | `cardNumber: string`، `cvv2: string`، `expireDate: string`، `pin2: string` | `currentBalanceAmount: string`، `availableBalanceAmount: string` | برای استعلام موجودی یک کارت بانکی با ارائه شماره کارت (cardNumber)، cvv2، تاریخ انقضا (expireDate) و رمز دوم (pin2) فراخوانی می‌شود؛ پیش از انجام تراکنش جهت اطمینان از کافی‌بودن موجودی استفاده می‌گردد. |
| `GetCardTransferToken` | `peerUserId: Int32Value`، `msgRid: Int64Value_1`، `description: StringValue` | `requestEndPoint: string`، `token: string`، `destCardNo: StringValue` | برای دریافت توکن انتقال وجه از کارت به کارت فراخوانی می‌شود و با ارسال شناسه کاربر مقصد (peerUserId) و اختیاری شناسه پیام (msgRid)، توکن لازم برای شروع فرایند انتقال وجه را برمی‌گرداند. |
| `GetOTPToken` | `cardNumberStartingSix: string` | `requestEndPoint: string`، `token: string` | برای دریافت رمز یک‌بارمصرف (OTP) بر اساس شش رقم ابتدایی شماره کارت (cardNumberStartingSix) فراخوانی می‌شود تا کاربر بتواند تراکنش بانکی خود را احراز هویت کند. |
| `GetOTPTokenV2` | `messagePeer: Bot`، `msgRid: int64`، `msgDate: int64`، `peerUserId: Int32Value`، `cardNumberStartingSix: string` | `requestEndPoint: string`، `token: string` | نسخه بهبودیافته GetOTPToken است که علاوه بر شش رقم ابتدایی کارت، اطلاعات پیام (messagePeer، msgRid، msgDate) و شناسه کاربر مقصد (peerUserId) را نیز دریافت می‌کند تا OTP را در بستر یک مکالمه مشخص صادر کند. |
| `GetOrganizationPaymentToken` | `organizationId: string`، `invoiceId: string`، `amount: int64` | `token: string`، `billHolderName: string`، `amount: double` | هنگامی که کاربر قصد پرداخت قبض یا فاکتور سازمانی دارد فراخوانی می‌شود؛ با ارسال organizationId، invoiceId و amount، توکن لازم برای هدایت به درگاه پرداخت سازمان مربوطه را دریافت می‌کند. |
| `GetPSProxyPaymentToken` | `paymentAmount: int64`، `msg: Msg`، `description: StringValue` | `endpoint: string`، `token: string` | برای دریافت توکن پرداخت از طریق درگاه واسط (PSProxy) فراخوانی می‌شود؛ مبلغ (paymentAmount)، اطلاعات پیام (msg) و توضیحات (description) را می‌گیرد تا کاربر بتواند مبلغ مورد نظر را از طریق درگاه پراکسی پرداخت کند. |
| `GetPSProxyToken` | — | `endpoint: string`، `token: string` | برای دریافت توکن احراز هویت پایه از درگاه PSProxy بدون نیاز به پارامتر خاص فراخوانی می‌شود؛ احتمالاً پیش‌نیاز شروع هر جلسه پرداخت از طریق این درگاه است. |
| `GetPayMoneyRequestToken` | `messagePeer: Bot`، `msgRid: int64`، `msgDate: int64`، `recipient: int32`، `description: StringValue` | `requestEndPoint: string`، `token: string` | زمانی فراخوانی می‌شود که کاربری می‌خواهد درخواست دریافت وجه (Pay Money Request) از کاربر دیگری ارسال کند؛ با مشخص‌کردن messagePeer، msgRid، msgDate و recipient، توکن لازم برای عملیات درخواست پول را دریافت می‌کند. |
| `GetPaymentToken` | `msg: Msg`، `description: StringValue`، `amount: Int32Value` | `token: string`، `endpoint: string`، `terminalId: StringValue`، `cardAcqId: StringValue`، `orderId: Int64Value_1` | رایج‌ترین متد پرداخت است که برای دریافت توکن پرداخت از درگاه اصلی بله استفاده می‌شود؛ اطلاعات پیام (msg)، توضیحات (description) و مبلغ (amount) را دریافت کرده و توکنی برمی‌گرداند که کاربر برای تکمیل تراکنش به آن نیاز دارد. |
| `GetPayvandCard` | `index: string` | `card: string` | برای دریافت اطلاعات یک کارت پیوند خاص با استفاده از شناسه (index) فراخوانی می‌شود؛ احتمالاً در صفحه مدیریت کارت‌های بانکی برای نمایش جزئیات یک کارت مشخص به‌کار می‌رود. |
| `GetPayvandCardList` | — | `payvandCards: repeated PayvandCard` | فهرست تمام کارت‌های بانکی ثبت‌شده کاربر (کارت‌های پیوند) را بدون نیاز به پارامتر خاص بازمی‌گرداند؛ معمولاً در صفحه کیف پول یا هنگام انتخاب کارت برای پرداخت فراخوانی می‌شود. |
| `GetRecentCharges` | — | `recentCharges: repeated RecentCharge` | تاریخچه شارژ‌های اخیر خریداری‌شده توسط کاربر را بدون نیاز به پارامتر برمی‌گرداند؛ در صفحه سوابق خرید شارژ برای نمایش تراکنش‌های گذشته استفاده می‌شود. |
| `GetRemainToken` | `cardNumberStartingSix: string` | `requestEndPoint: string`، `token: string` | برای دریافت توکنی جهت استعلام موجودی کارت بانکی بر اساس شش رقم ابتدایی شماره کارت (cardNumberStartingSix) فراخوانی می‌شود؛ این توکن در مرحله بعدی به درگاه بانکی ارسال می‌گردد. |
| `GetSadadPSPPaymentToken` | `msg: Msg`، `paymentAmount: int64`، `description: StringValue` | `endpoint: string`، `token: string`، `terminalId: string`، `merchantCode: string` | برای دریافت توکن پرداخت از درگاه PSP سداد فراخوانی می‌شود؛ اطلاعات پیام (msg)، مبلغ (paymentAmount) و توضیحات (description) را دریافت کرده و کاربر را به درگاه پرداخت سداد هدایت می‌کند. |
| `GetTokenInvoice` | `service: int32` | `endpoint: string`، `token: string` | برای دریافت فاکتور یا اطلاعات صورتحساب مرتبط با یک سرویس خاص (service) فراخوانی می‌شود؛ احتمالاً پیش از پرداخت سرویس‌های اشتراکی یا سازمانی برای نمایش جزئیات مبلغ به کاربر استفاده می‌گردد. |
| `GrantBankiAccess` | `bot: UserPeer`، `serviceKey: string` | ✔️ فقط تأیید | برای اعطای دسترسی به سرویس بانکی «بانکی» به یک ربات (bot) با استفاده از کلید سرویس (serviceKey) فراخوانی می‌شود؛ این RPC احتمالاً در فرایند اتصال و یکپارچه‌سازی ربات‌های پرداخت با زیرساخت بانکی بله مورد استفاده قرار می‌گیرد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-charnet-v1-charnetservice"></a>

## شارژ و بسته اینترنت — `bale.charnet.v1.CharnetService`

این سرویس امکان خرید شارژ تلفن همراه و بسته‌های اینترنتی اپراتورهای مختلف را از طریق کیف پول بله فراهم می‌کند. کلاینت از این سرویس برای مدیریت سفارش‌های اخیر، دریافت لیست بسته‌ها و انجام پرداخت شارژ استفاده می‌نماید.

نام‌فضای پایتون: `client.charnet_service` — تعداد متد: 11

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `BuyCharge` | `walletToken: bytes`، `phoneNumber: bytes`، `amount: int64`، `operatorType: int64`، `remaining: Int64Value_1`، `chargeType: int64`، `targetUserId: Int32Value`، `voucherId: Int32Value` | `paymentToken: Offset`، `receipt: Receipt` | زمانی که کاربر می‌خواهد مستقیماً شارژ تلفن همراه بخرد؛ با ارسال walletToken، phoneNumber، amount، operatorType و chargeType پرداخت از کیف پول انجام می‌شود و در صورت تمایل می‌توان شارژ را برای کاربر دیگری (targetUserId) یا با کوپن تخفیف (voucherId) خریداری کرد. |
| `BuyInternetBundle` | `walletToken: bytes`، `phoneNumber: bytes`، `bundleId: int64`، `operatorType: int64`، `remaining: Int64Value_1`، `targetUserId: Int32Value` | `paymentToken: Offset`، `receipt: T_ei_76777` | برای خرید بسته اینترنتی برای یک شماره تلفن مشخص فراخوانی می‌شود؛ کلاینت bundleId و operatorType را به همراه walletToken ارسال می‌کند تا بسته از کیف پول پرداخت و برای phoneNumber یا targetUserId فعال شود. |
| `DeleteRecentChargeOrder` | `accessHash: bytes` | ✔️ فقط تأیید | هنگامی که کاربر می‌خواهد یک سفارش شارژ اخیر را از تاریخچه حذف کند؛ کلاینت accessHash آن سفارش را ارسال می‌کند تا از لیست سفارش‌های اخیر پاک شود. |
| `DeleteRecentInternetBundleOrder` | `orderId: int64` | ✔️ فقط تأیید | برای حذف یک سفارش بسته اینترنتی از تاریخچه اخیر استفاده می‌شود؛ کلاینت orderId سفارش مورد نظر را ارسال می‌کند تا آن رکورد پاک گردد. |
| `GetAvailableCharges` | `operator: int64`، `chargeType: int64` | `amounts: repeated int64`، `canBeOptional: int64` | پیش از خرید شارژ، کلاینت این RPC را فراخوانی می‌کند تا لیست مقادیر شارژ قابل خرید را بر اساس operator و chargeType دریافت کند و به کاربر نمایش دهد. |
| `GetInternetBundleList` | `operatorType: int64`، `simCardType: int64` | `bundleLists: repeated BundleList` | برای نمایش بسته‌های اینترنتی موجود به کاربر فراخوانی می‌شود؛ با ارسال operatorType و simCardType (سیم‌کارت دائمی یا اعتباری) لیست بسته‌های مناسب بازگردانده می‌شود. |
| `GetInternetBundlePaymentToken` | `operatorType: int64`، `bundleId: int64`، `phoneNumber: bytes`، `targetUserId: Int32Value` | `token: bytes` | پیش از نهایی‌سازی خرید بسته اینترنتی، کلاینت این متد را با operatorType، bundleId و phoneNumber فراخوانی می‌کند تا توکن پرداخت لازم برای تأیید تراکنش را دریافت نماید. |
| `GetRecentChargeOrders` | `count: int64`، `types: repeated int64` | `orders: repeated T_eo_76777` | برای نمایش تاریخچه سفارش‌های شارژ اخیر استفاده می‌شود؛ کلاینت تعداد (count) و فیلتر نوع (types) را ارسال می‌کند تا لیست سفارش‌های شارژ قبلی برای انتخاب سریع شماره یا مقدار مشابه نمایش داده شود. |
| `GetRecentInternetBundleOrders` | `count: int64` | `orders: repeated T_en_76777` | لیست سفارش‌های اخیر بسته اینترنتی را برمی‌گرداند؛ با ارسال count تعداد رکوردهای مورد نیاز مشخص می‌شود و کلاینت از این داده برای پیشنهاد تکرار خرید به کاربر استفاده می‌کند. |
| `GetTopUpChargePaymentToken` | `providerCode: bytes`، `topupType: bytes`، `amount: int64`، `targetPhoneNumber: bytes`، `targetUserId: Int32Value` | `token: bytes` | برای دریافت توکن پرداخت شارژ از نوع topup (شارژ مستقیم/فوری) فراخوانی می‌شود؛ کلاینت providerCode، topupType، amount و targetPhoneNumber را ارسال می‌کند تا توکنی برای تأیید پرداخت از کیف پول صادر شود. |
| `GetVoucherChargePaymentToken` | `providerCode: bytes`، `amount: int64`، `targetUserId: Int32Value` | `token: bytes` | زمانی که کاربر می‌خواهد شارژ را از طریق یک کوپن/voucher خریداری کند فراخوانی می‌شود؛ کلاینت providerCode، amount و targetUserId را ارسال می‌کند تا توکن پرداخت مخصوص این نوع خرید دریافت گردد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-crowdfunding-v1-crowdfunding"></a>

## تامین مالی جمعی — `bale.crowdfunding.v1.CrowdFunding`

این سرویس امکانات مربوط به تامین مالی جمعی (crowdfunding) در پیام‌رسان بله را فراهم می‌کند. کلاینت می‌تواند اطلاعات مشارکت‌کنندگان و مجموع مبالغ پرداخت‌شده برای یک پیام مرتبط با کمپین تامین مالی را دریافت کند.

نام‌فضای پایتون: `client.crowd_funding` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetParticipants` | `messageId: Msg`، `limit: int64`، `offset: int64` | `userPayments: repeated UserPayment` | زمانی فراخوانی می‌شود که کلاینت می‌خواهد فهرست کاربرانی را که در یک کمپین تامین مالی جمعی شرکت کرده‌اند نمایش دهد؛ با ارسال messageId (شناسه پیام مرتبط با کمپین)، limit و offset، لیست شرکت‌کنندگان به‌صورت صفحه‌بندی‌شده بازگردانده می‌شود. |
| `GetTotalPaidAmount` | `messageId: Msg` | `totalPaidAmount: int64`، `creatorUserId: int64` | برای دریافت مجموع مبالغ پرداخت‌شده در یک کمپین تامین مالی جمعی استفاده می‌شود؛ کلاینت با ارسال messageId پیام مربوطه، کل مبلغ جمع‌آوری‌شده را دریافت می‌کند تا وضعیت مالی کمپین را به کاربر نشان دهد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-falake-v1-falake"></a>

## بررسی وضعیت لینک — `bale.falake.v1.Falake`

این سرویس برای بررسی اعتبار و وضعیت لینک‌های اشتراک‌گذاری‌شده در بله استفاده می‌شود. کلاینت می‌تواند از طریق این سرویس مشخص کند که یک لینک معتبر، فعال یا منقضی است.

نام‌فضای پایتون: `client.falake` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetLinkStatus` | `link: string` | `linkStatus: ExtFalakeLinkStatus` | کلاینت این RPC را با ارسال یک link (رشته‌ای حاوی آدرس لینک) فراخوانی می‌کند تا وضعیت آن لینک را بررسی کند. این متد احتمالاً برای اعتبارسنجی لینک‌های دعوت، اشتراک یا لینک‌های عمومی قبل از استفاده یا نمایش به کاربر به کار می‌رود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-fanoos-v1-fanoos"></a>

## تحلیل رویداد و ردیابی (فانوس) — `bale.fanoos.v1.fanoos`

سرویس فانوس برای ارسال رویدادهای تحلیلی و ردیابی رفتار کاربر در اپلیکیشن بله استفاده می‌شود. کلاینت از این سرویس برای گزارش‌دهی رویدادهای مختلف (مانند کلیک‌ها، بازدیدها یا اقدامات کاربر) به سرور ارسال می‌کند.

نام‌فضای پایتون: `client.fanoos` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `Send` | `eventName: string`، `items: ExtFanoosItems`، `date: int64` | ✔️ فقط تأیید | کلاینت این متد را برای ارسال یک رویداد تحلیلی به سرور فراخوانی می‌کند؛ با ارسال eventName (نام رویداد)، items (داده‌های مرتبط با رویداد) و date (زمان وقوع رویداد)، اطلاعات رفتاری کاربر به سیستم ردیابی بله گزارش می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-feedback-v1-feedback"></a>

## ارسال بازخورد — `bale.feedback.v1.FeedBack`

این سرویس امکان ارسال بازخورد و نظرات کاربران را به سرور بله فراهم می‌کند. کاربران می‌توانند امتیاز، عنوان، توضیحات و جزئیات تکمیلی تجربه خود را از اپلیکیشن ارسال نمایند.

نام‌فضای پایتون: `client.feed_back` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `SendFeedBack` | `rate: int32`، `title: string`، `description: string`، `details: map<string, string>`، `mtDetails: ExtFeedBackMtDetails` | ✔️ فقط تأیید | هنگامی که کاربر می‌خواهد نظر یا بازخورد خود را درباره اپلیکیشن ثبت کند، این RPC فراخوانی می‌شود؛ با ارسال فیلدهای rate (امتیاز عددی)، title (عنوان)، description (توضیحات) و details (جزئیات کلیدی-مقداری اضافه)، بازخورد کاربر به سرور ارسال و ذخیره می‌گردد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-garson-v1-garson"></a>

## کشف و مدیریت سرویس‌ها و بات‌ها — `bale.garson.v1.Garson`

این سرویس مسئول فهرست‌بندی، دسته‌بندی و پیشنهاد بات‌ها و سرویس‌های مینی‌اپ در پیام‌رسان بله است. کلاینت از آن برای نمایش پنل «گارسون» (کاتالوگ سرویس‌ها) و شخصی‌سازی میانبرهای کاربر استفاده می‌کند.

نام‌فضای پایتون: `client.garson` — تعداد متد: 10

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `EditCustomServices` | — | `customItems: CustomItems` | هنگامی که کاربر می‌خواهد سرویس‌های میانبر سفارشی خود را در پنل گارسون ویرایش یا بازچینی کند فراخوانی می‌شود. این RPC تغییرات انتخاب شخصی کاربر را ذخیره می‌کند. |
| `GetAdvertisementBot` | — | `bots: repeated Bots` | برای دریافت اطلاعات بات تبلیغاتی پیش‌فرض بله فراخوانی می‌شود، احتمالاً جهت نمایش بنر یا پیشنهاد تبلیغاتی در صفحه گارسون. |
| `GetBotBanners` | — | `banners: repeated Banner` | کلاینت این RPC را برای دریافت بنرهای تبلیغاتی بات‌ها در صفحه اصلی پنل گارسون صدا می‌زند تا محتوای اسلایدر یا بنر بالای صفحه را بارگذاری کند. |
| `GetBotsByCategory` | `categoryId: int64`، `pagination: T_n8_51787` | `bots: CategorizedBot` | زمانی که کاربر روی یک دسته‌بندی مشخص در پنل گارسون ضربه می‌زند فراخوانی می‌شود؛ با ارسال categoryId و pagination لیست بات‌های آن دسته را صفحه‌بندی‌شده دریافت می‌کند. |
| `GetCategorizedBots` | — | `categorizedBots: repeated CategorizedBot` | برای دریافت کل فهرست بات‌ها به تفکیک دسته‌بندی در یک فراخوانی استفاده می‌شود، معمولاً برای رندر کردن صفحه اصلی پنل گارسون با بخش‌های دسته‌بندی‌شده. |
| `GetCustomServices` | — | `customItems: CustomItems` | میانبرهای سرویس سفارشی‌سازی‌شده کاربر را برمی‌گرداند تا در بالای پنل گارسون نمایش داده شوند؛ پس از ورود یا بازگشایی پنل فراخوانی می‌شود. |
| `GetRecommendedBots` | `botId: int64`، `pagination: T_n8_51787` | `bots: repeated Bots`، `moreBotsUrl: StringValue` | با ارسال botId یک بات خاص و پارامتر pagination، لیست بات‌های مشابه یا پیشنهادی مرتبط با آن را برمی‌گرداند؛ برای نمایش بخش «شاید دوست داشته باشید» در صفحه جزئیات بات به‌کار می‌رود. |
| `GetServices` | `version: int64` | `version: int64`، `isChanged: int64`، `data: bytes`، `banners: repeated Banner`، `services: Services`، `sections: repeated Section` | با ارسال version کلاینت، فهرست کامل سرویس‌های موجود در پنل گارسون را دریافت می‌کند؛ مکانیزم version به کلاینت اجازه می‌دهد فقط در صورت تغییر داده‌ها، فهرست را به‌روزرسانی کند. |
| `GetTrendBots` | — | `bots: repeated Bots` | لیست بات‌های پرطرفدار و ترند را برمی‌گرداند تا در بخش «محبوب‌ترین‌ها» یا «پرکاربردترین‌ها» در پنل گارسون به کاربر نمایش داده شود. |
| `GetUserRepeatedBots` | — | `bots: repeated Bots` | بات‌هایی را که کاربر به‌کرات با آن‌ها تعامل داشته برمی‌گرداند تا به‌عنوان «اخیراً استفاده‌شده» یا «پرکاربرد من» در صدر پنل گارسون نمایش داده شوند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-ghasedak-v1-ghasedakservice"></a>

## همگام‌سازی وضعیت مسیرها — `bale.ghasedak.v1.GhasedakService`

سرویس قاصدک (Ghasedak) مسئول همگام‌سازی وضعیت مکالمات و مسیرهای پیام‌رسانی در بله است. کلاینت از این سرویس برای دریافت تغییرات جدید (diff) و وضعیت به‌روز مسیرها استفاده می‌کند تا دیده‌شدن پیام‌ها و هدایت آن‌ها دقیق بماند.

نام‌فضای پایتون: `client.ghasedak_service` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetDiff` | `states: repeated State`، `optimizations: repeated int64` | `updates: repeated T_tW_88717`، `usersRefs: repeated UserPeer`، `groupsRefs: repeated GroupPeer` | کلاینت برای همگام‌سازی وضعیت محلی خود با سرور این RPC را فراخوانی می‌کند؛ با ارسال لیستی از states فعلی و پارامترهای optimizations، تغییراتی (diff) را دریافت می‌کند که باید اعمال شوند. این فراخوانی معمولاً هنگام بارگذاری اولیه اپلیکیشن یا پس از قطع اتصال انجام می‌شود. |
| `GetRoutesStates` | `groupPeers: repeated GroupPeer`، `optimizations: repeated int64` | `seqs: repeated State` | کلاینت با ارسال لیستی از groupPeers، وضعیت مسیرهای ارتباطی (routes) مربوط به آن گروه‌ها را از سرور درخواست می‌کند. این متد احتمالاً برای بررسی در دسترس‌بودن یا آخرین حالت مسیرهای پیام‌رسانی گروه‌ها به کار می‌رود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-giftpacket-v1-giftpacket"></a>

## پاکت هدیه — `bale.giftpacket.v1.GiftPacket`

این سرویس امکان ارسال، باز کردن و مدیریت پاکت‌های هدیه پولی در بله را فراهم می‌کند. کاربران می‌توانند مبلغی را به‌صورت پاکت هدیه برای مخاطبان یا گروه‌ها ارسال کنند و دریافت‌کنندگان آن را باز نمایند.

نام‌فضای پایتون: `client.gift_packet` — تعداد متد: 3

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetGiftPacketPaymentToken` | `token: bytes`، `amount: int64`، `peer: Peer`، `message: GiftPacketMessage` | `paymentToken: bytes` | کلاینت پیش از ارسال پاکت هدیه این RPC را فراخوانی می‌کند تا با ارسال token، amount، peer مقصد و پیام (message)، یک توکن پرداخت معتبر دریافت کند. این توکن در مرحله بعدی برای تکمیل فرایند پرداخت پاکت استفاده می‌شود. |
| `OpenGiftPacket` | `msgIdentifier: Msg`، `receiverWalletId: bytes`، `pageNo: Int32Value`، `orderType: int64` | `giftReceivers: repeated GiftReceiver`، `status: int64`، `openedCount: int64`، `selfWinAmount: Int64Value_1`، `rank: Int32Value`، `userOutPeers: repeated UserPeer` | وقتی کاربر روی یک پاکت هدیه در چت کلیک می‌کند، کلاینت با ارسال msgIdentifier (شناسه پیام)، receiverWalletId و پارامترهای صفحه‌بندی این RPC را صدا می‌زند تا پاکت را باز کرده و مبلغ را به کیف پول دریافت‌کننده واریز کند. |
| `SendGiftPacketWithWallet` | `peer: Peer`، `randomId: int64`، `message: GiftPacketMessage`، `sourceWalletId: bytes` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | برای ارسال مستقیم پاکت هدیه از کیف پول کاربر، کلاینت این RPC را با peer مقصد، randomId، پیام (message) و sourceWalletId (کیف پول مبدأ) فراخوانی می‌کند تا پاکت هدیه ایجاد و ارسال شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-groups-v1-groups"></a>

## گروه‌ها و کانال‌ها — `bale.groups.v1.Groups`

این سرویس مدیریت گروه‌ها و کانال‌های بله را بر عهده دارد و عملیاتی نظیر ساخت گروه، ویرایش اطلاعات، دعوت و اخراج اعضا، و دریافت اطلاعات گروه را فراهم می‌کند. کلاینت برای هر تعامل با گروه‌ها یا کانال‌ها — از عضویت تا مدیریت ادمین‌ها و پین‌ها — این سرویس را فراخوانی می‌کند.

نام‌فضای پایتون: `client.groups` — تعداد متد: 48

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AddDiscussionGroupAdmin` | `channel: GroupPeer`، `discussionGroup: GroupPeer` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | هنگامی که یک کانال دارای گروه بحث (discussion group) است، کلاینت این RPC را برای افزودن یک ادمین جدید به آن گروه بحث فراخوانی می‌کند. ورودی‌های channel و discussionGroup هر دو از نوع GroupPeer هستند و مشخص می‌کنند کانال و گروه بحث مرتبط کدامند. |
| `CreateGroup` | `rid: int64`، `title: string`، `users: repeated UserPeer`، `groupType: int32`، `optimizations: repeated int32`، `nick: StringValue`، `restriction: int32` | `seq: int32`، `state: bytes`، `group: Group`، `users: repeated User`، `userPeers: repeated UserPeer`، `notAddedUserPeers: repeated UserPeer`، `inviteLink: string` | کلاینت برای ایجاد یک گروه یا کانال جدید این RPC را با عنوان (title)، نوع گروه (groupType)، لیست کاربران اولیه (users) و یک شناسه تصادفی (rid) فراخوانی می‌کند. پارامتر nick نام نمایشی عمومی و restriction سطح محدودیت دسترسی گروه را تعیین می‌کند. |
| `EditChannelNick` | `groupPeer: GroupPeer`، `nick: string`، `randomId: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | برای تغییر نام کاربری (username/nick) یک کانال توسط ادمین فراخوانی می‌شود؛ کلاینت peer کانال (groupPeer)، نام کاربری جدید (nick) و یک شناسه تصادفی (randomId) ارسال می‌کند. این عملیات آدرس عمومی کانال را به‌روزرسانی می‌کند. |
| `EditGroupAbout` | `groupPeer: GroupPeer`، `rid: int64`، `about: StringValue`، `optimizations: repeated int32` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | ادمین گروه یا کانال برای به‌روزرسانی متن توضیحات (بیوگرافی/about) این RPC را با groupPeer، rid و مقدار جدید about فراخوانی می‌کند. احتمالاً rid برای جلوگیری از ارسال تکراری (idempotency) استفاده می‌شود. |
| `EditGroupAvatar` | `groupPeer: GroupPeer`، `fileLocation: FileLocation`، `rid: int64`، `optimizations: repeated int32` | `avatar: Avatar`، `seq: int32`، `state: bytes`، `date: int64` | کلاینت پس از آپلود تصویر جدید، این RPC را با groupPeer و fileLocation تصویر آپلودشده فراخوانی می‌کند تا آواتار گروه یا کانال به‌روز شود. rid برای تضمین یکتایی درخواست ارسال می‌شود. |
| `EditGroupDefaultCardNumber` | `groupPeer: GroupPeer`، `cardNumber: string` | ✔️ فقط تأیید | ادمین گروه برای تنظیم یا تغییر شماره کارت بانکی پیش‌فرض مرتبط با گروه این RPC را با groupPeer و cardNumber فراخوانی می‌کند. احتمالاً برای فعال‌سازی قابلیت پرداخت یا دریافت وجه در گروه استفاده می‌شود. |
| `EditGroupTitle` | `groupPeer: GroupPeer`، `title: string`، `rid: int64`، `optimizations: repeated int32` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | برای تغییر عنوان (نام نمایشی) یک گروه یا کانال توسط ادمین فراخوانی می‌شود؛ ورودی‌های groupPeer، title جدید و rid ارسال می‌شوند. پارامتر optimizations احتمالاً بر حجم داده‌های برگشتی تأثیر می‌گذارد. |
| `FetchGroupAdmins` | `groupOutPeer: GroupPeer` | `users: repeated UserPeer`، `admins: repeated Member` | کلاینت برای دریافت لیست ادمین‌های یک گروه یا کانال این RPC را با groupOutPeer فراخوانی می‌کند. معمولاً در صفحه مدیریت اعضا یا هنگام بررسی سطح دسترسی‌ها استفاده می‌شود. |
| `GetBannedUsers` | `group: GroupPeer` | `bannedUsers: repeated BannedUser` | ادمین گروه برای مشاهده لیست کاربرانی که از گروه (group) مسدود (ban) شده‌اند این RPC را فراخوانی می‌کند. خروجی برای مدیریت و رفع انسداد کاربران در تنظیمات گروه به‌کار می‌رود. |
| `GetCanSeeMessages` | `groupPeer: GroupPeer`، `userId: int32` | `canSeeMessages: bool` | کلاینت برای بررسی اینکه آیا یک کاربر خاص (userId) می‌تواند پیام‌های یک گروه (groupPeer) را ببیند یا نه، این RPC را فراخوانی می‌کند. احتمالاً در گروه‌هایی با محدودیت دسترسی یا قبل از ورود کاربر استفاده می‌شود. |
| `GetFullGroup` | `peer: GroupPeer` | `fullGroup: FullGroup` | کلاینت برای دریافت اطلاعات کامل یک گروه یا کانال (شامل اعضا، تنظیمات، توضیحات و آواتار) این RPC را با peer از نوع GroupPeer فراخوانی می‌کند. معمولاً هنگام باز کردن صفحه اطلاعات گروه فراخوانده می‌شود. |
| `GetGroupDefaultCardNumber` | `groupPeerr: GroupPeer` | `defaultCardNumber: string` | کلاینت برای دریافت شماره کارت بانکی پیش‌فرض تنظیم‌شده برای یک گروه (groupPeerr) این RPC را فراخوانی می‌کند. احتمالاً در بخش پرداخت یا اطلاعات مالی گروه نمایش داده می‌شود. |
| `GetGroupInviteURL` | `groupPeer: GroupPeer` | `url: string` | ادمین گروه برای دریافت لینک دعوت (invite URL) گروه این RPC را با groupPeer فراخوانی می‌کند. لینک برگشتی برای اشتراک‌گذاری خارجی و دعوت اعضای جدید استفاده می‌شود. |
| `GetGroupMembersCount` | `group: GroupPeer` | `membersCount: int32` | کلاینت برای دریافت تعداد اعضای یک گروه (group از نوع GroupPeer) این RPC را فراخوانی می‌کند. معمولاً برای نمایش آمار سریع در لیست گفتگوها یا صفحه گروه استفاده می‌شود. |
| `GetGroupPreview` | `token: string`، `isOpenedOutsideBale: BoolValue_2` | `group: FullGroup`، `action: int32` | قبل از پیوستن به گروه از طریق لینک دعوت، کلاینت این RPC را با token لینک دعوت فراخوانی می‌کند تا اطلاعات پیش‌نمایش گروه (نام، آواتار، تعداد اعضا) را نمایش دهد. پارامتر isOpenedOutsideBale مشخص می‌کند لینک از خارج اپلیکیشن باز شده یا نه. |
| `GetGroupRecommendations` | `source: int32` | `groups: repeated GroupPeer` | کلاینت برای دریافت لیست گروه‌ها یا کانال‌های پیشنهادی بر اساس منبع (source) این RPC را فراخوانی می‌کند. احتمالاً در بخش کشف محتوا یا هنگام جستجوی گروه‌های جدید نمایش داده می‌شود. |
| `GetMemberPermissions` | `group: GroupPeer`، `user: UserPeer` | `permissions: Permissions` | کلاینت برای بررسی سطح دسترسی یک عضو خاص (user) در یک گروه (group) این RPC را فراخوانی می‌کند. معمولاً در صفحه اطلاعات عضو یا برای اعمال محدودیت‌های UI بر اساس نقش کاربر استفاده می‌شود. |
| `GetMutualGroups` | `peer: UserPeer` | `groups: repeated GroupPeer` | کلاینت برای دریافت لیست گروه‌های مشترک بین کاربر جاری و یک کاربر دیگر (peer از نوع UserPeer) این RPC را فراخوانی می‌کند. معمولاً در پروفایل کاربر دیگر نمایش داده می‌شود. |
| `GetMyGroups` | `mode: int32`، `isOwner: bool`، `filters: repeated Filter` | `groups: repeated GroupPeer` | کلاینت برای دریافت لیست گروه‌ها و کانال‌هایی که کاربر عضو آن‌هاست این RPC را با پارامترهای mode، isOwner و filters فراخوانی می‌کند. با isOwner=true فقط گروه‌هایی که کاربر مالک (owner) آن‌هاست برگردانده می‌شوند. |
| `GetPins` | `groupPeer: GroupPeer`، `page: int32`، `limit: int32` | `pins: repeated History`، `count: int32` | کلاینت برای دریافت لیست پیام‌های پین‌شده یک گروه (groupPeer) این RPC را با پارامترهای صفحه‌بندی page و limit فراخوانی می‌کند. خروجی در بخش «پیام‌های پین‌شده» صفحه گروه نمایش داده می‌شود. |
| `InviteUser` | `groupPeer: GroupPeer`، `user: UserPeer`، `rid: int64`، `optimizations: repeated int32`، `messageCount: Int32Value` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | ادمین یا عضو مجاز برای اضافه کردن یک کاربر (user) به یک گروه (groupPeer) این RPC را با rid برای یکتایی و messageCount برای مشخص کردن تعداد پیام‌های تاریخچه قابل مشاهده توسط عضو جدید فراخوانی می‌کند. |
| `InviteUsers` | `groupPeer: GroupPeer`، `rid: int64`، `users: repeated UserPeer` | `notAddedUserPeers: repeated UserPeer` | مشابه InviteUser، اما برای دعوت گروهی چند کاربر (users به‌صورت لیست UserPeer) به یک گروه (groupPeer) در یک درخواست واحد استفاده می‌شود. rid برای جلوگیری از اجرای تکراری عملیات ارسال می‌شود. |
| `JoinGroup` | `token: string`، `optimizations: repeated int32` | `group: Group`، `seq: int32`، `state: bytes`، `date: int64`، `users: repeated User`، `rid: int64`، `userPeers: repeated UserPeer`، `inviterUserId: int32`، `groupSeq: int32` | کاربر برای پیوستن به یک گروه از طریق لینک دعوت، این RPC را با token لینک دعوت فراخوانی می‌کند. پارامتر optimizations حجم یا نوع داده‌های برگشتی پس از عضویت را کنترل می‌کند. |
| `JoinPublicGroup` | `peer: Bot`، `optimizations: repeated int32` | `group: Group`، `seq: int32`، `state: bytes`، `date: int64`، `users: repeated User`، `rid: int64`، `userPeers: repeated UserPeer`، `inviterUserId: int32`، `groupSeq: int32` | کاربر برای پیوستن به یک گروه یا کانال عمومی بدون نیاز به لینک دعوت این RPC را با peer از نوع Bot (شناسه عمومی گروه) فراخوانی می‌کند. معمولاً از صفحه پیش‌نمایش گروه یا نتایج جستجو استفاده می‌شود. |
| `KickUser` | `groupPeer: GroupPeer`، `user: UserPeer`، `rid: int64`، `optimizations: repeated int32` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | ادمین گروه برای اخراج یک عضو (user) از گروه (groupPeer) این RPC را با rid برای یکتایی درخواست فراخوانی می‌کند. کاربر اخراج‌شده دیگر به گروه دسترسی نخواهد داشت مگر دوباره دعوت شود. |
| `LeaveGroup` | `groupPeer: GroupPeer`، `rid: int64`، `optimizations: repeated int32`، `makeOrphan: BoolValue_1` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | زمانی فراخوانی می‌شود که کاربر بخواهد از یک گروه خارج شود؛ با ارسال groupPeer و rid گروه مورد نظر، عضویت کاربر لغو می‌گردد. پارامتر makeOrphan احتمالاً مشخص می‌کند که در صورت ترک مالک، گروه بدون سرپرست بماند. |
| `LoadFullGroups` | `groups: repeated GroupPeer` | `groups: repeated T_hI` | برای دریافت اطلاعات کامل چند گروه به‌صورت دسته‌ای استفاده می‌شود؛ با ارسال لیست groups، اطلاعات جامع هر گروه شامل متادیتا و تنظیمات بازگردانده می‌شود. |
| `LoadGroupAvatars` | `peer: GroupPeer` | `avatars: Avatars` | برای بارگذاری تصاویر پروفایل (آواتار) یک گروه با استفاده از peer گروه فراخوانی می‌شود، معمولاً هنگام نمایش صفحه جزئیات گروه یا لیست گروه‌ها. |
| `LoadGroups` | `peers: repeated GroupPeer` | `groups: repeated Group` | اطلاعات پایه چند گروه را به‌صورت دسته‌ای با دریافت لیست peers برمی‌گرداند؛ جهت نمایش سریع لیست گروه‌های کاربر در صفحه اصلی استفاده می‌شود. |
| `LoadMembers` | `group: GroupPeer`، `limit: int32`، `next: BytesValue`، `condition: Condition` | `members: repeated Member`، `next: BytesValue` | فهرست اعضای یک گروه را با صفحه‌بندی (limit و next) بارگذاری می‌کند؛ پارامتر condition احتمالاً فیلتری برای نوع عضویت (مثلاً فقط ادمین‌ها) اعمال می‌کند. |
| `MakeUserAdmin` | `groupPeer: GroupPeer`، `userPeer: UserPeer`، `adminTitle: StringValue` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | مالک یا ادمین گروه این RPC را فراخوانی می‌کند تا کاربری مشخص (userPeer) را در گروه (groupPeer) به مقام ادمین ارتقا دهد و می‌توان عنوان سفارشی ادمین (adminTitle) نیز تعیین کرد. |
| `PinMessage` | `senderUserId: int32`، `groupPeer: GroupPeer`، `date: int64`، `msgRid: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | برای پین کردن یک پیام در گروه استفاده می‌شود؛ با ارسال groupPeer، msgRid و date پیام مورد نظر، آن پیام در بالای گروه ثابت می‌ماند. |
| `RemoveDiscussionGroup` | `rid: int64`، `channel: GroupPeer` | ✔️ فقط تأیید | گروه بحث (Discussion Group) مرتبط با یک کانال را با دریافت channel و rid حذف می‌کند؛ این عملیات ارتباط بین کانال و گروه نظرات را قطع می‌کند. |
| `RemoveGroupAvatar` | `groupPeer: GroupPeer`، `rid: int64`، `optimizations: repeated int32`، `avaterId: Int64Value_1` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | تصویر پروفایل گروه را با ارسال groupPeer و avaterId حذف می‌کند؛ معمولاً از بخش تنظیمات گروه توسط ادمین فراخوانی می‌شود. |
| `RemovePin` | `groupPeer: GroupPeer` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | تمام پیام‌های پین‌شده یک گروه را با دریافت groupPeer لغو پین می‌کند؛ احتمالاً برای حذف دسته‌جمعی پین‌ها استفاده می‌شود. |
| `RemoveSinglePin` | `groupPeer: GroupPeer`، `msgRid: int64`، `msgDate: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | یک پیام پین‌شده مشخص را با استفاده از groupPeer، msgRid و msgDate از حالت پین خارج می‌کند، بدون تأثیر بر سایر پیام‌های پین‌شده. |
| `RemoveUserAdmin` | `groupPeer: GroupPeer`، `userPeer: UserPeer` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | دسترسی ادمین یک عضو (userPeer) را در گروه (groupPeer) لغو می‌کند؛ توسط مالک گروه هنگام تغییر نقش اعضا فراخوانی می‌شود. |
| `RevokeInviteURL` | `groupPeer: GroupPeer` | `url: string` | لینک دعوت فعلی گروه را با دریافت groupPeer باطل و یک لینک جدید تولید می‌کند؛ هنگامی استفاده می‌شود که ادمین بخواهد از ورود افراد ناخواسته با لینک قدیمی جلوگیری کند. |
| `SetAvailableReactions` | `group: GroupPeer`، `codes: repeated string` | ✔️ فقط تأیید | واکنش‌های (ایموجی‌های) مجاز برای یک گروه را با ارسال group و لیست codes تعریف می‌کند؛ ادمین از این RPC برای محدود یا سفارشی‌سازی واکنش‌های قابل استفاده توسط اعضا بهره می‌برد. |
| `SetCanSeeHistory` | `groupPeer: GroupPeer`، `canSeeHistory: bool` | ✔️ فقط تأیید | تعیین می‌کند آیا اعضای جدید گروه می‌توانند تاریخچه پیام‌های قبل از عضویت خود را ببینند یا خیر؛ با ارسال groupPeer و مقدار canSeeHistory توسط ادمین تنظیم می‌شود. |
| `SetCanSeeMessages` | `groupPeer: GroupPeer`، `userId: int32`، `canSeeMessages: bool` | ✔️ فقط تأیید | کنترل می‌کند که یک کاربر مشخص (userId) در گروه (groupPeer) توانایی مشاهده پیام‌ها را داشته باشد یا نه؛ احتمالاً برای محدودسازی دسترسی عضو خاص استفاده می‌شود. |
| `SetDiscussionGroup` | `rid: int64`، `channel: GroupPeer` | `discussionGroup: GroupPeer`، `group: Group` | یک گروه را به‌عنوان گروه بحث (Discussion Group) برای یک کانال تنظیم می‌کند؛ با ارسال channel و rid ارتباط بین کانال و گروه نظرات برقرار می‌شود. |
| `SetGroupDefaultPermissions` | `group: GroupPeer`، `permissions: Permissions` | ✔️ فقط تأیید | مجوزهای پیش‌فرض اعضای عادی گروه را با ارسال group و permissions تعریم می‌کند؛ ادمین از این RPC برای تعیین این‌که اعضا چه کارهایی می‌توانند انجام دهند استفاده می‌کند. |
| `SetMemberCustomTitle` | `groupId: int32`، `memberId: int32`، `title: string` | ✔️ فقط تأیید | یک عنوان سفارشی (title) برای عضو مشخص (memberId) در گروه (groupId) تعیین می‌کند؛ برای نمایش نقش یا لقب ویژه عضو زیر نام او در گروه استفاده می‌شود. |
| `SetMemberPermissions` | `group: GroupPeer`، `user: UserPeer`، `permissions: Permissions` | ✔️ فقط تأیید | مجوزهای اختصاصی یک عضو (user) در گروه (group) را به‌صورت جداگانه از مجوزهای پیش‌فرض تنظیم می‌کند؛ برای اعطا یا سلب قابلیت‌های خاص از یک عضو معین استفاده می‌شود. |
| `SetRestriction` | `groupOutPeer: GroupPeer`، `restriction: int32`، `nick: StringValue` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | محدودیت‌هایی را روی یک گروه یا کانال (groupOutPeer) اعمال می‌کند؛ پارامترهای restriction و nick احتمالاً نوع محدودیت و شناسه مرتبط را مشخص می‌کنند. |
| `TransferOwnership` | `groupPeer: GroupPeer`، `newOwner: int32` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | مالکیت گروه را از مالک فعلی به عضو دیگری (newOwner) منتقل می‌کند؛ با ارسال groupPeer و newOwner، تمام اختیارات مالک به کاربر جدید واگذار می‌شود. |
| `UnBanUser` | `groupPeer: GroupPeer`، `user: UserPeer`، `optimizations: repeated int32` | ✔️ فقط تأیید | محدودیت بن (مسدودسازی) یک کاربر (user) را در گروه (groupPeer) برمی‌دارد؛ توسط ادمین هنگام بازگشایی دسترسی کاربر بن‌شده فراخوانی می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-ketf-v1-ketf"></a>

## بات‌ها و مینی‌اپ‌ها — `bale.ketf.v1.Ketf`

این سرویس مدیریت بات‌های بله را پوشش می‌دهد و امکاناتی مانند دریافت اطلاعات بات، مجوزهای گروهی، نتایج inline، پرداخت درون‌برنامه‌ای و ارسال داده به مینی‌اپ‌ها را فراهم می‌کند. کلاینت از این سرویس برای تعامل با بات‌ها، دکمه‌های callback و فرآیند پرداخت از طریق بات استفاده می‌کند.

نام‌فضای پایتون: `client.ketf` — تعداد متد: 14

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetBotGroupPermissions` | `botUserId: int32`، `groupId: int32` | `hasAccessToMessages: bool` | برای بررسی مجوزهای یک بات (botUserId) در یک گروه مشخص (groupId) فراخوانی می‌شود تا مشخص شود بات چه دسترسی‌هایی در آن گروه دارد. |
| `GetBotInfo` | `botUserId: int32` | `botInfo: BotInfo` | اطلاعات پروفایل و مشخصات یک بات را با ارسال botUserId دریافت می‌کند؛ معمولاً هنگام نمایش صفحه معرفی بات یا بررسی وضعیت آن استفاده می‌شود. |
| `GetBotWhiteList` | `botUserId: int32` | `list: List` | لیست سفید (whitelist) کاربران یا گروه‌های مجاز برای استفاده از یک بات خاص (botUserId) را برمی‌گرداند؛ احتمالاً برای باتهای خصوصی یا محدود استفاده می‌شود. |
| `GetBots` | `pagination: T_jq` | `pageCount: int32`، `bots: repeated T_cC` | فهرست بات‌های موجود را با پشتیبانی از صفحه‌بندی (pagination) دریافت می‌کند؛ برای نمایش کاتالوگ یا لیست باتهای قابل استفاده توسط کاربر به کار می‌رود. |
| `GetInlineBotResults` | `query: string`، `peer: Peer`، `botUserId: int32`، `offset: string` | `results: repeated T_L`، `nextOffset: Offset`، `queryId: Int64Value_1`، `isGallery: bool` | هنگامی که کاربر در یک مکالمه (peer) متنی را با ذکر بات inline تایپ می‌کند، این RPC با query و botUserId فراخوانی می‌شود تا نتایج پیشنهادی بات برای نمایش به کاربر دریافت گردد. |
| `GetPaymentDetails` | `purchaseMessageId: Msg`، `invoiceIdentifier: InvoiceIdentifier` | `title: string`، `totalAmount: int64`، `paymentsHistory: repeated PaymentsHistory`، `session: Session`، `disapproved: Disapproved`، `description: string`، `labeledPrices: repeated LabeledPrice` | جزئیات یک پرداخت را بر اساس purchaseMessageId یا invoiceIdentifier دریافت می‌کند؛ پیش از تکمیل پرداخت یا برای نمایش خلاصه فاکتور فراخوانی می‌شود. |
| `GetUserContext` | `botUserId: int32` | `botUserId: int32`، `userId: int32`، `nonce: string`، `sign: string` | اطلاعات زمینه‌ای (context) کاربر جاری را در ارتباط با یک بات مشخص (botUserId) برمی‌گرداند؛ احتمالاً شامل وضعیت session یا داده‌های مرتبط با تعامل کاربر با بات است. |
| `GetWebappHash` | `botUserId: int32`، `data: string` | `hash: string`، `queryId: string`، `authDate: int64` | یک هش امنیتی برای تأیید اعتبار داده‌های webapp مرتبط با بات (botUserId) ایجاد می‌کند؛ هنگام باز کردن مینی‌اپ یا WebApp بات برای احراز هویت درخواست استفاده می‌شود. |
| `InvokeCustomAction` | `id: string`، `messageId: MessageId`، `peer: OutPeer`، `openDialogAction: OpenDialogAction`، `done: Done` | ✔️ فقط تأیید | یک اکشن سفارشی تعریف‌شده توسط بات را با ارسال id اکشن، messageId و peer اجرا می‌کند؛ برای تعامل با دکمه‌ها یا منوهای تعاملی پیام‌های بات به کار می‌رود. |
| `MakePayment` | `paymentSessionId: string`، `paymentOptionId: string`، `wallet: T_yS`، `gateway: Gateway` | `gatewayRedirect: GatewayRedirect`، `paymentReceipt: PaymentsHistory` | پرداخت نهایی را با استفاده از paymentSessionId، paymentOptionId، wallet و gateway انجام می‌دهد؛ هنگامی که کاربر روش پرداخت را انتخاب کرده و تأیید می‌کند فراخوانی می‌شود. |
| `SendAuthenticatedInlineCallBackData` | `templateMessageId: Msg`، `data: StringValue` | ✔️ فقط تأیید | داده callback احراز هویت‌شده را برای یک پیام template (templateMessageId) به بات ارسال می‌کند؛ برای دکمه‌هایی که نیاز به تأیید هویت کاربر دارند استفاده می‌شود. |
| `SendInlineCallBackData` | `historyMessageIdentifier: Msg`، `data: StringValue` | ✔️ فقط تأیید | داده callback مرتبط با یک پیام تاریخچه (historyMessageIdentifier) را به بات ارسال می‌کند؛ هنگام فشردن دکمه‌های inline keyboard پیام‌های بات فراخوانی می‌شود. |
| `SendInlineCallback` | `peer: ExPeer`، `messageId: MessageId`، `data: StringValue` | `answer: Answer` | رویداد callback دکمه inline را با مشخص کردن peer، messageId و data به بات مقصد ارسال می‌کند؛ نسخه گسترش‌یافته‌تر SendInlineCallBackData با پشتیبانی از ExPeer است. |
| `SendMiniAppData` | `botUserId: int32`، `queryId: StringValue`، `data: StringValue`، `buttonText: StringValue` | ✔️ فقط تأیید | داده‌ای را از مینی‌اپ (WebApp) به بات (botUserId) ارسال می‌کند؛ با queryId و data هنگامی که کاربر در مینی‌اپ فرمی را تأیید یا عملی را انجام می‌دهد فراخوانی می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-kifpool-v1-kifpool"></a>

## کیف پول و پرداخت — `bale.kifpool.v1.Kifpool`

این سرویس مدیریت کیف پول دیجیتال (kifpool) در پیام‌رسان بله را فراهم می‌کند و عملیاتی نظیر شارژ کیف پول، برداشت وجه، انتقال پول، خرید، پرداخت درون‌چتی و مدیریت کیف‌های رمزارزی را پوشش می‌دهد. کلاینت برای انجام تمام تراکنش‌های مالی، مشاهده موجودی و تاریخچه تراکنش‌ها از این سرویس استفاده می‌کند.

نام‌فضای پایتون: `client.kifpool` — تعداد متد: 29

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `CashOut` | `requestId: bytes`، `token: bytes`، `amount: int64`، `account: StringValue`، `pan: StringValue` | `referenceNo: int64` | کلاینت این متد را برای برداشت وجه از کیف پول به حساب بانکی فراخوانی می‌کند؛ مبلغ (amount)، شماره حساب یا شماره کارت (pan) و یک شناسه یکتا (requestId) برای جلوگیری از تراکنش تکراری ارسال می‌شود. |
| `Charge` | `paymentToken: bytes`، `referenceNo: int64` | ✔️ فقط تأیید | پس از هدایت کاربر به درگاه پرداخت بانکی، کلاینت با ارسال paymentToken و referenceNo این متد را صدا می‌زند تا موجودی کیف پول را شارژ کند. |
| `CheckChargePermission` | `paymentToken: bytes` | ✔️ فقط تأیید | پیش از شروع فرآیند شارژ، کلاینت با ارسال paymentToken بررسی می‌کند که آیا این توکن مجاز به شارژ کیف پول است یا خیر. |
| `CreateKifpool` | `nationalId: StringValue` | ✔️ فقط تأیید | کلاینت هنگام ثبت‌نام یا فعال‌سازی اولیه کیف پول، با ارسال nationalId (کد ملی کاربر) یک kifpool جدید ایجاد می‌کند. |
| `CryptoCashOut` | `requestId: bytes`، `amount: int64`، `account: StringValue`، `pan: StringValue`، `pocketType: int64`، `isMerchant: BoolValue_1` | `referenceNo: int64` | کلاینت این متد را برای برداشت وجه از کیف رمزارزی (crypto pocket) فراخوانی می‌کند؛ نوع پاکت (pocketType)، مبلغ، شماره حساب مقصد و اینکه آیا کاربر فروشنده است (isMerchant) ارسال می‌شود. |
| `CryptoInvoice` | `token: bytes`، `pageSize: int64`، `pageNumber: int64` | `records: repeated Record` | کلاینت برای دریافت لیست صورت‌حساب‌های تراکنش‌های رمزارزی با صفحه‌بندی (pageSize، pageNumber) این متد را فراخوانی می‌کند. |
| `CryptoPurchase` | `amount: int64`، `srcToken: bytes`، `dstToken: bytes`، `description: bytes`، `terminalId: bytes`، `bornaTrxId: bytes` | ✔️ فقط تأیید | کلاینت برای انجام خرید با کیف رمزارزی، با ارسال مبلغ (amount)، توکن مبدأ (srcToken)، توکن مقصد (dstToken) و شناسه ترمینال این متد را صدا می‌زند. |
| `CryptoRefund` | `token: bytes`، `amount: int64`، `approvalCode: int64`، `trxRefSrc: bytes` | ✔️ فقط تأیید | کلاینت برای بازگشت وجه یک تراکنش رمزارزی قبلی، با ارسال token، مبلغ (amount)، کد تأیید (approvalCode) و مرجع تراکنش اصلی (trxRefSrc) این متد را فراخوانی می‌کند. |
| `CryptoTransfer` | `amount: int64`، `srcToken: bytes`، `dstToken: bytes`، `description: StringValue`، `dstPhoneNo: StringValue` | `amount: int64`، `date: int64`، `approvalCode: int64`، `srcToken: bytes`، `dstToken: bytes` | کلاینت برای انتقال رمزارز به کاربر دیگر، با ارسال مبلغ، توکن مبدأ و مقصد و شماره تلفن گیرنده (dstPhoneNo) این متد را صدا می‌زند. |
| `GetChargePaymentToken` | `token: bytes`، `amount: int64`، `callbackType: int64` | `paymentToken: bytes` | کلاینت پیش از هدایت کاربر به درگاه پرداخت برای شارژ کیف پول، با ارسال token، مبلغ (amount) و نوع بازگشت (callbackType) یک paymentToken دریافت می‌کند. |
| `GetCredit` | — | `balance: Int64Value_1`، `hasCredit: int64` | کلاینت برای نمایش موجودی اعتبار فعلی کاربر (مثلاً اعتبار هدیه یا کشکبک) بدون نیاز به پارامتر ورودی این متد را فراخوانی می‌کند. |
| `GetCryptoChargePaymentToken` | `token: bytes`، `amount: int64`، `receiverId: bytes` | `paymentToken: bytes` | کلاینت پیش از شارژ کیف رمزارزی، با ارسال token، مبلغ و شناسه گیرنده (receiverId) یک paymentToken مخصوص رمزارز دریافت می‌کند. |
| `GetCryptoWallets` | — | `myCryptoWallets: repeated CryptoPocket` | کلاینت برای دریافت لیست کیف‌های رمزارزی کاربر بدون ارسال پارامتر این متد را فراخوانی می‌کند تا موجودی و اطلاعات هر کیف نمایش داده شود. |
| `GetKifpoolOwner` | `walletToken: bytes` | `firstName: StringValue`، `lastName: StringValue`، `walletStatus: int64`، `approvalCode: int64` | کلاینت با ارسال walletToken این متد را صدا می‌زند تا اطلاعات مالک یک kifpool مشخص (احتمالاً برای تأیید هویت گیرنده در انتقال وجه) را دریافت کند. |
| `GetKifpoolPointBalance` | `token: bytes` | `pointBalanceInfo: repeated PointBalanceInfo` | کلاینت با ارسال token کیف پول، موجودی امتیازات (points) انباشته‌شده در kifpool را دریافت می‌کند تا در بخش پاداش یا وفاداری نمایش دهد. |
| `GetKifpoolPointDetails` | `token: bytes`، `count: int64`، `page: int64` | `pointDetailsInfo: repeated PointDetailsInfo` | کلاینت برای نمایش جزئیات تاریخچه امتیازات کیف پول با صفحه‌بندی (page، count)، این متد را فراخوانی می‌کند. |
| `GetKifpoolPointSummery` | `token: bytes` | `pointSummeryInfo: repeated PointSummeryInfo` | کلاینت با ارسال token یک خلاصه کلی از وضعیت امتیازات kifpool (مجموع کسب‌شده، مصرف‌شده و باقی‌مانده) را دریافت می‌کند. |
| `GetKifpoolTransactionPoint` | `transactionID: int64`، `amount: int64` | `calculatedPoint: int64`، `point: int64`، `unitAmount: int64` | کلاینت با ارسال transactionID و amount، امتیاز متعلق به یک تراکنش مشخص را استعلام می‌کند؛ احتمالاً برای نمایش امتیاز کسب‌شده پس از انجام پرداخت. |
| `GetMyKifpools` | `invocationSpot: StringValue`، `pocketType: int64` | `myWallets: repeated MyWallet`، `firstName: StringValue`، `lastName: StringValue` | کلاینت برای دریافت لیست تمام کیف‌های پول متعلق به کاربر جاری، با ارسال نوع پاکت (pocketType) و محل فراخوانی (invocationSpot) این متد را صدا می‌زند. |
| `Invoice` | `token: bytes`، `pageSize: int64`، `pageNumber: int64` | `records: repeated Record` | کلاینت برای دریافت لیست صورت‌حساب‌های تراکنش‌های کیف پول معمولی با صفحه‌بندی (pageSize، pageNumber) و توکن کیف پول این متد را فراخوانی می‌کند. |
| `PayForMessage` | `amount: int64`، `chargeAmount: int64`، `message: Msg` | `status: int64`، `paymentToken: Offset` | کلاینت برای پرداخت درون‌چتی (ارسال پول همراه پیام)، با ارسال مبلغ (amount)، مقدار شارژ (chargeAmount) و پیام (message) این متد را صدا می‌زند. |
| `Purchase` | `amount: int64`، `dstToken: bytes`، `srcToken: bytes`، `description: bytes`، `useCredit: BoolValue_2`، `couponId: Int32Value`، `terminalNo: StringValue`، `stan: Int64Value` | ✔️ فقط تأیید | کلاینت برای خرید از فروشگاه یا پرداخت به یک کسب‌وکار، با ارسال مبلغ، توکن مبدأ (srcToken)، توکن مقصد (dstToken)، توضیحات و اختیاراً کد تخفیف (couponId) این متد را فراخوانی می‌کند. |
| `PurchaseMessage` | `historyId: Msg`، `amount: Int64Value_1`، `description: StringValue` | ✔️ فقط تأیید | کلاینت برای پرداخت بابت یک پیام خاص (مثلاً محتوای پولی)، با ارسال شناسه پیام (historyId از نوع Msg)، مبلغ و توضیحات این متد را صدا می‌زند. |
| `PurchaseMessageWithCharge` | `historyId: Msg`، `amount: Int64Value_1`، `description: StringValue`، `chargeAmount: int64` | `paymentToken: bytes` | مشابه PurchaseMessage، اما علاوه بر خرید پیام، مقداری نیز به کیف پول شارژ می‌شود؛ کلاینت chargeAmount اضافی را به همراه اطلاعات پیام و مبلغ خرید ارسال می‌کند. |
| `PurchaseWithCharge` | `amount: int64`، `dstToken: bytes`، `srcToken: bytes`، `description: bytes`، `chargeAmount: int64`، `useCredit: BoolValue_2`، `couponId: Int32Value`، `terminalNo: StringValue`، `stan: Int64Value` | `paymentToken: bytes` | مشابه Purchase، اما همزمان مقدار مشخصی نیز به کیف پول شارژ می‌شود؛ کلاینت chargeAmount را در کنار سایر پارامترهای خرید ارسال می‌کند تا خرید و شارژ در یک تراکنش انجام شود. |
| `Transfer` | `sourceToken: bytes`، `destinationToken: StringValue`، `destinationPhone: StringValue`، `destinationUserid: Int32Value`، `amount: int64`، `description: StringValue` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که کاربر می‌خواهد مبلغی (amount) را از کیف پول خود (sourceToken) به کاربر دیگری از طریق destinationToken، destinationPhone یا destinationUserid انتقال دهد. فیلد description توضیح اختیاری تراکنش را نگه می‌دارد. |
| `UpgradeKifpool` | `token: bytes`، `nationalId: StringValue`، `cardNo: StringValue`، `accountNo: StringValue`، `remainReferenceNumber: bytes` | `level: int64` | برای ارتقای سطح کیف پول کاربر با تأیید هویت استفاده می‌شود؛ کلاینت token کیف پول به همراه nationalId، cardNo و accountNo را ارسال می‌کند تا محدودیت‌های تراکنش حساب رفع شود. فیلد remainReferenceNumber احتمالاً شماره مرجع مرحله‌ی قبلی فرآیند ارتقا را حمل می‌کند. |
| `VerifyCashOutKifpool` | `token: bytes` | `accountNo: bytes`، `firstName: StringValue`، `lastName: StringValue` | پس از آغاز درخواست برداشت وجه، کلاینت با ارسال token تأیید می‌کند که عملیات برداشت (cash-out) معتبر و نهایی شود. این RPC مرحله‌ی تأیید دو‌مرحله‌ای برداشت از کیف پول است. |
| `VerifyPurchaseMessage` | `historyId: Msg` | `amount: Int64Value_1`، `paymentTypeTitle: StringValue`، `paymentTitle: StringValue` | برای تأیید صحت یک پیام خرید (purchase message) در تاریخچه‌ی تراکنش‌ها استفاده می‌شود؛ کلاینت historyId از نوع Msg را ارسال می‌کند تا سرور وضعیت یا اعتبار آن پرداخت را برگرداند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-llm_auth-v1-llmauthservice"></a>

## احراز هویت هوش مصنوعی — `bale.llm_auth.v1.LLMAuthService`

این سرویس مسئول صدور توکن احراز هویت برای دسترسی کلاینت‌ها به قابلیت‌های هوش مصنوعی (LLM) بله است. از طریق این سرویس، کلاینت می‌تواند توکن لازم برای فراخوانی APIهای مبتنی بر مدل‌های زبانی را دریافت کند.

نام‌فضای پایتون: `client.llm_auth_service` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetAuthToken` | — | `token: string`، `url: string`، `expiresIn: int64` | کلاینت این متد را فراخوانی می‌کند تا یک توکن احراز هویت معتبر برای استفاده از سرویس‌های هوش مصنوعی (LLM) بله دریافت کند. احتمالاً این توکن در درخواست‌های بعدی به سرویس‌های LLM به عنوان اعتبارنامه ارسال می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-magazine-v1-magazine"></a>

## مجله و فید محتوا — `bale.magazine.v1.Magazine`

این سرویس مدیریت فید مجله بله را بر عهده دارد و امکان مشاهده پست‌ها، دسته‌بندی‌ها و تعامل با محتوا از طریق لایک (upvote) را فراهم می‌کند. کلاینت از این سرویس برای بارگذاری فید عمومی یا داخلی، کشف پست‌های مشابه و مدیریت پست‌های پسندیده‌شده توسط کاربر استفاده می‌کند.

نام‌فضای پایتون: `client.magazine` — تعداد متد: 9

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetMessageUpvoters` | `loadMoreState: BytesValue`، `message: Msg` | `loadMoreState: BytesValue`، `users: repeated UserPeer` | برای دریافت فهرست کاربرانی که یک پیام مشخص (message) را لایک کرده‌اند فراخوانی می‌شود؛ با استفاده از loadMoreState می‌توان نتایج را صفحه‌بندی کرد. |
| `GetMyUpvotes` | — | `upvotes: Upvotes` | برای دریافت فهرست تمام پست‌هایی که کاربر جاری لایک کرده است استفاده می‌شود، بدون نیاز به پارامتر ورودی. |
| `GetSimilarPosts` | `message: Msg`، `loadMoreState: BytesValue` | `messages: repeated T_A_54329`، `loadMoreState: BytesValue`، `similarPosts: repeated SimilarPost` | کلاینت این RPC را با ارسال message فراخوانی می‌کند تا پست‌های مشابه آن را دریافت کند؛ loadMoreState برای بارگذاری صفحات بعدی نتایج به کار می‌رود. |
| `LoadCategories` | — | `categories: repeated T_L_54329` | برای دریافت فهرست دسته‌بندی‌های موجود در مجله بله فراخوانی می‌شود تا کلاینت بتواند منوی دسته‌بندی‌ها را نمایش دهد. |
| `LoadCategoryFeedMessages` | `categoryId: int64`، `loadMoreState: BytesValue` | `loadMoreState: BytesValue`، `messages: repeated T_A_54329` | با ارسال categoryId، پست‌های فید مربوط به یک دسته‌بندی خاص را بارگذاری می‌کند؛ loadMoreState برای صفحه‌بندی محتوای بیشتر استفاده می‌شود. |
| `LoadFeedMessages` | `loadMoreState: BytesValue` | `loadMoreState: BytesValue`، `messages: repeated T_A_54329` | پست‌های فید عمومی مجله بله را بارگذاری می‌کند؛ با ارسال loadMoreState می‌توان محتوای بیشتری را به صورت تدریجی دریافت کرد. |
| `LoadInternalFeedMessages` | `loadMoreState: BytesValue` | `loadMoreState: BytesValue`، `messages: repeated T_A_54329` | احتمالاً فید داخلی یا اختصاصی کاربر را بارگذاری می‌کند (مثلاً پست‌های کانال‌های دنبال‌شده)؛ مشابه LoadFeedMessages از loadMoreState برای صفحه‌بندی بهره می‌برد. |
| `RevokeUpvotedPost` | `message: Msg`، `albumId: Int64Value_1` | `upvotes: Upvotes` | زمانی فراخوانی می‌شود که کاربر لایک خود را از یک پست (message) پس می‌گیرد؛ albumId در صورت وجود آلبوم، پست مرتبط را مشخص می‌کند. |
| `UpvotePost` | `message: Msg`، `albumId: Int64Value_1` | `upvotes: Upvotes` | برای لایک کردن یک پست توسط کاربر استفاده می‌شود؛ message پست هدف را مشخص می‌کند و albumId در صورت نیاز شناسه آلبوم مرتبط را ارسال می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-market-v1-market"></a>

## مارکت و فروشگاه — `bale.market.v1.Market`

این سرویس مدیریت مارکت (بازار) بله را برعهده دارد و امکاناتی مانند ثبت و پذیرش فروشگاه‌ها، مدیریت دسته‌بندی‌ها و تگ‌ها، کمپین‌های تبلیغاتی، و دریافت اطلاعات محصولات و بازارهای برتر را فراهم می‌کند. کلاینت از این سرویس برای نمایش صفحه مارکت، پیوستن به فروشگاه، و مدیریت محتوای بازار استفاده می‌کند.

نام‌فضای پایتون: `client.market` — تعداد متد: 26

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AcceptCampaignMarket` | `marketId: int64`، `isPermanent: int64` | ✔️ فقط تأیید | زمانی که ادمین یا سیستم می‌خواهد درخواست مشارکت یک مارکت در کمپین تبلیغاتی را تأیید کند، این RPC با ارسال marketId و isPermanent فراخوانی می‌شود تا مارکت مربوطه به کمپین اضافه شود. |
| `AcceptMarketJoinRequest` | `marketPeerId: int64`، `requestId: int64`، `displayName: bytes`، `categoryId: int64` | ✔️ فقط تأیید | برای پذیرش درخواست پیوستن یک فروشگاه به مارکت بله فراخوانی می‌شود؛ با ارسال marketPeerId، requestId، displayName و categoryId، درخواست تأیید و فروشگاه در دسته‌بندی مناسب ثبت می‌گردد. |
| `CreateMarketJoinRequest` | `marketPeerId: int64`، `displayName: bytes`، `categoryId: int64`، `tagIds: repeated int64` | ✔️ فقط تأیید | زمانی که صاحب یک پیر (کانال یا گروه) می‌خواهد فروشگاه خود را در مارکت بله ثبت کند، این RPC با ارسال marketPeerId، displayName، categoryId و tagIds فراخوانی می‌شود تا درخواست پیوستن ایجاد شود. |
| `CreateTag` | `title: bytes`، `categoryId: int64` | `tag: T_iR_88717` | برای ایجاد یک تگ جدید در یک دسته‌بندی مشخص استفاده می‌شود؛ ادمین با ارسال title و categoryId این RPC را فراخوانی می‌کند تا تگ مربوطه در سیستم ثبت گردد. |
| `GetCategoriesList` | `categoryId: int64`، `level: Int32Value_1`، `includeSampleMarkets: BoolValue_2`، `version: Int32Value_1` | `categories: repeated T_iE_88717`، `version: Int32Value_1` | کلاینت برای دریافت فهرست دسته‌بندی‌های مارکت این RPC را فراخوانی می‌کند؛ با ارسال categoryId، level و includeSampleMarkets می‌توان درخت دسته‌بندی‌ها را در سطح دلخواه با یا بدون نمونه فروشگاه دریافت کرد. |
| `GetCategoryMarkets` | `categoryId: int64`، `pagination: Pagination`، `version: int64` | `markets: repeated MarketType`، `version: int64` | برای دریافت فهرست فروشگاه‌های موجود در یک دسته‌بندی خاص فراخوانی می‌شود؛ با ارسال categoryId و pagination می‌توان نتایج را صفحه‌بندی‌شده نمایش داد. |
| `GetCategoryProducts` | `categoryId: int64`، `pagination: Pagination`، `version: int64` | `products: repeated Product`، `version: int64` | کلاینت برای دریافت فهرست محصولات یک دسته‌بندی مشخص این RPC را فراخوانی می‌کند؛ با ارسال categoryId و pagination، محصولات آن دسته به‌صورت صفحه‌بندی‌شده بازگردانده می‌شوند. |
| `GetIndexedProducts` | `startDate: int64`، `endDate: int64`، `categoryId: int64` | `products: repeated Product` | احتمالاً برای دریافت محصولاتی که در بازه زمانی مشخص (startDate تا endDate) ایندکس شده‌اند استفاده می‌شود؛ با ارسال categoryId می‌توان نتایج را به یک دسته‌بندی محدود کرد. |
| `GetMarket` | `peerId: int64`، `nickName: bytes` | `market: T_iS_88717`، `lastRequest: Request` | کلاینت برای دریافت اطلاعات یک فروشگاه خاص این RPC را با peerId یا nickName فروشگاه فراخوانی می‌کند تا پروفایل و جزئیات آن مارکت را نمایش دهد. |
| `GetMarketJoinRequests` | — | `marketJoinRequests: repeated Request` | برای دریافت فهرست درخواست‌های پیوستن به مارکت که توسط کاربر جاری ارسال شده‌اند فراخوانی می‌شود تا وضعیت درخواست‌های ثبت فروشگاه قابل پیگیری باشد. |
| `GetMarketsPendingJoinRequest` | — | `requests: repeated Request` | ادمین مارکت با این RPC فهرست فروشگاه‌هایی را که درخواست پیوستن آن‌ها در انتظار بررسی است دریافت می‌کند تا بتواند آن‌ها را تأیید یا رد کند. |
| `GetNumberOfSales` | `peer: Peer` | `numberOfSales: int64`، `isMarket: int64` | با ارسال peer یک فروشگاه، تعداد فروش‌های آن مارکت دریافت می‌شود؛ این RPC معمولاً برای نمایش آمار فروش در پروفایل فروشگاه یا داشبورد فروشنده استفاده می‌شود. |
| `GetOnboardingStatus` | — | `status: int64`، `categoryIds: repeated int64`، `gender: int64` | کلاینت هنگام ورود به بخش مارکت این RPC را فراخوانی می‌کند تا مشخص شود آیا کاربر فرآیند آنبوردینگ (تنظیمات اولیه علاقه‌مندی‌ها) را تکمیل کرده یا خیر. |
| `GetPendingCampaignMarkets` | — | `markets: repeated T_iS_88717` | برای دریافت فهرست مارکت‌هایی که درخواست شرکت در کمپین تبلیغاتی آن‌ها هنوز بررسی نشده است فراخوانی می‌شود، احتمالاً توسط ادمین سیستم. |
| `GetStores` | `version: int64` | `stores: bytes`، `version: int64` | برای دریافت فهرست فروشگاه‌های مارکت بله فراخوانی می‌شود؛ با ارسال version می‌توان تغییرات نسبت به نسخه قبلی را دریافت کرد و از کش محلی استفاده نمود. |
| `GetTags` | `categoryId: int64` | `tags: repeated T_iR_88717` | با ارسال categoryId، فهرست تگ‌های مرتبط با آن دسته‌بندی دریافت می‌شود؛ این RPC معمولاً هنگام ثبت یا ویرایش فروشگاه برای نمایش تگ‌های قابل انتخاب فراخوانی می‌شود. |
| `GetTopMarkets` | `ratingType: int64`، `pagination: Pagination` | `markets: repeated MarketType` | کلاینت برای نمایش فروشگاه‌های برتر مارکت این RPC را با ratingType و pagination فراخوانی می‌کند تا لیست محبوب‌ترین یا پربازدیدترین فروشگاه‌ها را نشان دهد. |
| `GetYaldaStores` | `version: int64` | `stores: bytes`، `version: int64` | مشابه GetStores اما احتمالاً مخصوص رویداد یلدا است؛ با ارسال version فهرست فروشگاه‌های ویژه شب یلدا دریافت می‌شود تا در بخش تبلیغات یا صفحه ویژه یلدا نمایش داده شود. |
| `RejectCampaignMarket` | `marketId: int64`، `isPermanent: int64` | ✔️ فقط تأیید | ادمین با این RPC درخواست شرکت یک مارکت در کمپین تبلیغاتی را رد می‌کند؛ با ارسال marketId و isPermanent می‌توان رد موقت یا دائمی را مشخص کرد. |
| `RejectMarketJoinRequest` | `marketPeerId: int64`، `rejectCause: int64`، `requestId: int64` | ✔️ فقط تأیید | برای رد کردن درخواست پیوستن یک فروشگاه به مارکت فراخوانی می‌شود؛ با ارسال marketPeerId، requestId و rejectCause دلیل رد به سیستم ثبت می‌گردد. |
| `SetGenericDeepLinks` | `links: repeated Link` | ✔️ فقط تأیید | ادمین مارکت با این RPC فهرستی از deep link های عمومی را تنظیم می‌کند؛ با ارسال آرایه‌ای از links، لینک‌های مستقیم به بخش‌های مختلف مارکت ایجاد یا به‌روزرسانی می‌شوند. |
| `SetMarketBanners` | `banners: repeated T_ib_88717` | ✔️ فقط تأیید | برای تنظیم یا به‌روزرسانی بنرهای تبلیغاتی صفحه اصلی مارکت فراخوانی می‌شود؛ ادمین با ارسال آرایه‌ای از banners، تصاویر و لینک‌های بنر را تعریف می‌کند. |
| `SetOnboardingData` | `categoryIds: repeated int64`، `gender: int64`، `isSkipped: BoolValue_1` | ✔️ فقط تأیید | کاربر هنگام اولین ورود به مارکت با این RPC علاقه‌مندی‌های خود را (categoryIds و gender) ثبت می‌کند؛ در صورت رد کردن این مرحله، isSkipped برابر true ارسال می‌شود. |
| `SetPopularSearches` | `items: repeated T_i__88717` | ✔️ فقط تأیید | ادمین با این RPC فهرست جستجوهای پرطرفدار را در مارکت تنظیم می‌کند؛ با ارسال آرایه items، پیشنهادهای جستجو که به کاربران نمایش داده می‌شوند به‌روزرسانی می‌گردند. |
| `SubmitMarketFeedback` | `rate: int64`، `userOpinion: Offset`، `clientVersion: Offset`، `extraFields: map<string, bytes>` | ✔️ فقط تأیید | کاربر پس از تجربه استفاده از مارکت بله با این RPC بازخورد خود را ارسال می‌کند؛ با ارسال rate، userOpinion و clientVersion، نظر و امتیاز کاربر ثبت می‌شود. |
| `UpdateMarketInfo` | `peerId: int64`، `displayName: StringValue`، `primaryCategoryId: Int32Value`، `isBanned: BoolValue_1`، `isActive: BoolValue_1` | ✔️ فقط تأیید | کلاینت این RPC را برای به‌روزرسانی اطلاعات یک فروشگاه یا کسب‌وکار در بازار بله فراخوانی می‌کند. با ارسال peerId مربوط به فروشگاه، می‌توان نام نمایشی (displayName)، دسته‌بندی اصلی (primaryCategoryId)، وضعیت فعال یا غیرفعال بودن (isActive) و وضعیت مسدودیت (isBanned) را به‌روز کرد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-maviz-v1-mavizstream"></a>

## دریافت به‌روزرسانی‌های جریانی — `bale.maviz.v1.MavizStream`

این سرویس مکانیزم اشتراک و دریافت به‌روزرسانی‌های لحظه‌ای (آپدیت‌ها) از سرور بله را فراهم می‌کند. کلاینت از طریق این سرویس تفاوت رویدادهای از دست رفته را دریافت کرده و در رویدادهای مکالمات و thread‌ها مشترک می‌شود.

نام‌فضای پایتون: `client.maviz_stream` — تعداد متد: 4

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetDifference` | `routeSequences: repeated RouteSequence`، `optimizations: repeated int64` | `groupEvents: map<string, bytes>`، `usersRefs: repeated UserPeer`، `groupsRefs: repeated GroupPeer` | کلاینت پس از قطع اتصال یا راه‌اندازی مجدد، این RPC را فراخوانی می‌کند تا رویدادهای از دست رفته را بازیابی کند؛ با ارسال لیست routeSequences (شماره ترتیب هر مسیر) و optimizations، سرور تنها تفاوت‌های جدید را برمی‌گرداند. |
| `SubscribeToThreadUpdates` | `peer: ExPeer`، `threadId: MessageId` | ✔️ فقط تأیید | هنگامی که کاربر وارد یک thread خاص از مکالمه می‌شود، کلاینت با ارسال peer و threadId این RPC را صدا می‌زند تا به‌روزرسانی‌های آن thread (مانند پیام‌های جدید یا واکنش‌ها) را دریافت کند. |
| `SubscribeToUpdates` _(جریانی/streaming)_ | `isMtProto: int64` | `update: Update`، `routeId: int64`، `sequence: int64`، `timestamp: int64`، `weakEvent: WeakEvent`، `mtupdate: Mtupdate`، `updates: Updates` | کلاینت هنگام اتصال اولیه این RPC استریمینگ را باز می‌کند تا یک کانال دائمی برای دریافت تمام به‌روزرسانی‌های سرور (پیام، وضعیت آنلاین و غیره) داشته باشد؛ فیلد isMtProto احتمالاً نوع پروتکل ارتباطی را مشخص می‌کند. |
| `UnsubscribeFromThreadUpdates` | `peer: ExPeer`، `threadId: MessageId` | ✔️ فقط تأیید | زمانی که کاربر از یک thread خارج می‌شود یا آن را می‌بندد، کلاینت با ارسال peer و threadId این RPC را فراخوانی می‌کند تا اشتراک به‌روزرسانی‌های آن thread لغو شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-meet-v1-meet"></a>

## تماس صوتی و تصویری (Meet) — `bale.meet.v1.Meet`

این سرویس امکانات کامل تماس صوتی و تصویری بله را مدیریت می‌کند؛ از برقراری تماس فردی و گروهی گرفته تا کنترل شرکت‌کنندگان، ضبط جلسه، و تولید لینک دعوت.

نام‌فضای پایتون: `client.meet` — تعداد متد: 30

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AcceptCall` | `callId: int64`، `inviteEnable: BoolValue_2` | `call: Call`، `participants: repeated Peer`، `seq: int32`، `sipCall: T_HS`، `isStream: BoolValue_2` | وقتی کاربر یک تماس ورودی را می‌پذیرد، کلاینت این RPC را با callId مربوطه فراخوانی می‌کند. فیلد inviteEnable مشخص می‌کند که آیا کاربر پذیرنده می‌تواند دیگران را نیز به تماس دعوت کند. |
| `AnswerCallJoinRequest` | `callId: int64`، `requesterIdentifier: string`، `isAllowed: bool` | ✔️ فقط تأیید | میزبان تماس با این RPC به درخواست پیوستن یک کاربر (مشخص‌شده با requesterIdentifier) پاسخ می‌دهد و با تنظیم isAllowed مشخص می‌کند که آیا اجازه ورود دارد یا خیر. |
| `AskToJoinCall` | `callId: int64`، `name: string` | ✔️ فقط تأیید | کاربری که قصد دارد به یک تماس در حال جریان بپیوندد ولی نیاز به تأیید میزبان دارد، این RPC را با callId و name خود فراخوانی می‌کند تا درخواست پیوستن ارسال شود. |
| `DeleteCallLogs` | `callIds: repeated Int64Value_1`، `all: bool`، `invert: bool` | ✔️ فقط تأیید | برای حذف تاریخچه تماس‌ها استفاده می‌شود؛ کلاینت می‌تواند با ارائه لیست callIds تماس‌های خاص را حذف کند یا با تنظیم all=true همه لاگ‌ها را یکجا پاک نماید. |
| `DeleteStream` | `streamUser: ExPeer` | ✔️ فقط تأیید | احتمالاً برای حذف یک جریان استریم مرتبط با یک کاربر خاص (streamUser از نوع ExPeer) به‌کار می‌رود، مثلاً پس از پایان پخش زنده یا استریم اختصاصی آن کاربر. |
| `DiscardCall` | `callId: int64`، `duration: int32`، `reason: int32`، `type: int32` | `call: Call`، `participants: repeated Peer`، `seq: int32`، `sipCall: T_HS`، `isStream: BoolValue_2` | هنگامی که یک تماس به هر دلیلی (رد شدن، قطع ارتباط، پایان تماس) خاتمه می‌یابد، کلاینت این RPC را با callId، مدت تماس (duration)، دلیل (reason) و نوع تماس (type) فراخوانی می‌کند. |
| `GenerateCallLink` | `isPublic: bool`، `callId: Int64Value_1`، `title: Offset` | `groupCall: GroupCall`، `linkExpirationPeriod: int64` | برای ساخت لینک دعوت به یک تماس یا جلسه استفاده می‌شود؛ می‌توان لینک را عمومی (isPublic) یا خصوصی تعریف کرد و با title عنوانی برای آن مشخص نمود. |
| `GetCallLinkDetails` | `session: string` | `groupCall: GroupCall` | با دادن رشته session (که معمولاً بخشی از URL لینک دعوت است)، اطلاعات جلسه یا تماس مرتبط با آن لینک را دریافت می‌کند تا کاربر پیش از پیوستن از جزئیات آن مطلع شود. |
| `GetCallLogs` | `pageNumber: Int64Value_1`، `pageSize: Int64Value_1`، `afterDate: Int64Value_1`، `beforeDate: Int64Value_1` | `callLogs: repeated CallLog`، `total: int32` | تاریخچه تماس‌های کاربر را به‌صورت صفحه‌بندی‌شده برمی‌گرداند؛ کلاینت می‌تواند با pageNumber، pageSize و بازه زمانی afterDate/beforeDate فیلتر کند. |
| `GetCallState` | `callId: int64` | `groupCall: GroupCall` | وضعیت فعلی یک تماس مشخص را با استفاده از callId دریافت می‌کند؛ برای به‌روزرسانی UI یا بررسی اینکه تماس هنوز فعال است یا خیر کاربرد دارد. |
| `GetGroupCall` | `peer: OutPeer` | `groupCall: GroupCall` | اطلاعات تماس گروهی مرتبط با یک گروه یا کانال (peer) را واکشی می‌کند تا مشخص شود آیا تماس گروهی فعالی در آن peer در جریان است یا نه. |
| `GetOngoingCalls` | `pageNumber: Int64Value_1`، `pageSize: Int64Value_1` | `callLogs: repeated CallLog` | فهرست تماس‌های در حال جریان کاربر را به‌صورت صفحه‌بندی‌شده برمی‌گرداند؛ احتمالاً برای نمایش نشانگر «تماس فعال» در رابط کاربری استفاده می‌شود. |
| `GetWssURL` | `callId: int64` | `url: string` | آدرس WebSocket سرور مدیا را برای یک callId مشخص دریافت می‌کند تا کلاینت بتواند اتصال صوتی/تصویری WebRTC را از طریق آن برقرار کند. |
| `InviteToCall` | `callId: int64`، `invitees: repeated OutPeer` | `peerStates: repeated PeerState` | برای دعوت یک یا چند کاربر (invitees از نوع OutPeer) به یک تماس در حال جریان با callId استفاده می‌شود، مشابه افزودن اعضای جدید به یک تماس گروهی. |
| `JoinGroupCall` | `callId: int64`، `name: Offset` | `groupCall: GroupCall`، `states: repeated PeerState` | کاربر با این RPC به یک تماس گروهی موجود با callId می‌پیوندد و نام نمایشی خود (name) را ارسال می‌کند تا در لیست شرکت‌کنندگان نشان داده شود. |
| `LeaveGroupCall` | `callId: int64`، `end: bool` | `groupCall: GroupCall`، `seq: int32` | کاربر با فراخوانی این RPC از یک تماس گروهی خارج می‌شود؛ اگر end=true باشد، تماس برای همه شرکت‌کنندگان پایان می‌یابد (احتمالاً فقط میزبان این مجوز را دارد). |
| `MuteParticipant` | `callId: int64`، `identity: string`، `trackId: string`، `revokePublishPermission: bool` | ✔️ فقط تأیید | میزبان تماس با این RPC صدای یک شرکت‌کننده مشخص (identity) را قطع می‌کند؛ با تنظیم revokePublishPermission می‌توان مجوز انتشار صدا/تصویر را کاملاً لغو کرد. |
| `ReceiveCall` | `callId: int64` | ✔️ فقط تأیید | پس از دریافت اعلان تماس ورودی، کلاینت این RPC را با callId فراخوانی می‌کند تا به سرور اعلام کند که اعلان تماس دریافت شده است (acknowledge)، پیش از قبول یا رد کردن. |
| `RemoveParticipant` | `callId: int64`، `identity: string`، `blockFromCall: bool` | ✔️ فقط تأیید | میزبان با این RPC یک شرکت‌کننده (identity) را از تماس اخراج می‌کند؛ با blockFromCall=true می‌توان از پیوستن مجدد آن کاربر به همین تماس جلوگیری کرد. |
| `SendCallReaction` | `callId: int64`، `reaction: string` | ✔️ فقط تأیید | کاربر در طول یک تماس گروهی یک واکنش احساسی (مثل 👏 یا ❤️) ارسال می‌کند که با فیلد reaction مشخص شده و برای سایر شرکت‌کنندگان نمایش داده می‌شود. |
| `SendFanoosEvent` | `eventName: string`، `items: Ext`، `date: int64` | ✔️ فقط تأیید | یک رویداد تحلیلی یا ردیابی (analytics/tracking) با نام eventName و داده‌های اضافی (items) به سیستم Fanoos بله ارسال می‌کند؛ احتمالاً برای لاگ رویدادهای تماس جهت تحلیل استفاده می‌شود. |
| `SetLinkTitle` | `title: string`، `callId: Int64Value_1`، `linkUrl: Offset` | ✔️ فقط تأیید | عنوان یک لینک تماس را به‌روزرسانی می‌کند؛ با ارائه title جدید و callId یا linkUrl لینک مورد نظر مشخص می‌شود. |
| `StartCall` | `peer: Peer`، `rid: int64`، `video: bool`، `internalCall: InternalCall`، `sipCall: SipCall`، `liveKitCall: LiveKitCall` | `call: Call`، `participants: repeated Peer`، `seq: int32`، `sipCall: T_HS`، `isStream: BoolValue_2` | یک تماس جدید (فردی یا SIP یا LiveKit) را با ارسال peer مقصد و rid شروع می‌کند؛ فیلد video مشخص می‌کند که تماس تصویری است یا صوتی. |
| `StartGroupCall` | `peer: OutPeer`، `randomId: int64`، `video: bool`، `mode: int32`، `invitees: repeated OutPeer` | `groupCall: GroupCall`، `seq: int32` | یک تماس گروهی جدید برای یک گروه یا کانال (peer) ایجاد می‌کند؛ می‌توان حالت تماس (mode)، تصویری بودن (video) و فهرست اولیه دعوت‌شدگان (invitees) را مشخص کرد. |
| `StartRecording` | `callId: int64`، `layout: string`، `quality: int32` | ✔️ فقط تأیید | ضبط یک تماس در حال جریان (callId) را آغاز می‌کند؛ کلاینت می‌تواند چیدمان تصویر (layout) و کیفیت ضبط (quality) را نیز تنظیم نماید. |
| `StartStream` | `streamUser: ExPeer`، `url: string`، `rtmpServer: string` | `streamKey: string` | هنگامی که کاربر یا سیستم می‌خواهد یک استریم زنده را در جلسه شروع کند، این RPC فراخوانی می‌شود؛ با ارسال streamUser (کاربر استریم‌کننده)، url مقصد و rtmpServer، سرور پخش RTMP را راه‌اندازی می‌کند. |
| `StopRecording` | `callId: int64` | ✔️ فقط تأیید | برای پایان دادن به ضبط یک تماس یا جلسه در حال انجام با ارسال callId استفاده می‌شود؛ کلاینت این RPC را پس از اتمام جلسه یا بنا به درخواست میزبان فراخوانی می‌کند. |
| `SubmitCallFeedback` | `callId: int64`، `rate: int32`، `userOpinion: Offset`، `client: int32`، `clientVersion: Offset`، `extraFields: map<string, bytes>`، `isStream: BoolValue_2` | ✔️ فقط تأیید | پس از پایان تماس، کلاینت این RPC را برای ارسال بازخورد کیفی کاربر (rate، userOpinion) به همراه اطلاعات client و clientVersion فراخوانی می‌کند تا تجربه تماس ارزیابی شود. |
| `TakeCallAction` | `callId: int64`، `lowerHand: LowerHand`، `raiseHand: RaiseHand` | ✔️ فقط تأیید | در طول یک تماس گروهی، کاربر با این RPC اقداماتی مانند بالا بردن (raiseHand) یا پایین آوردن (lowerHand) دست را با ارسال callId انجام می‌دهد تا درخواست صحبت کردن را اعلام یا لغو کند. |
| `UpdateLayout` | `callId: int64`، `requestedLayout: string` | ✔️ فقط تأیید | برای تغییر چیدمان نمایش تصویر شرکت‌کنندگان در جلسه (requestedLayout) با ارسال callId فراخوانی می‌شود؛ احتمالاً توسط میزبان برای تنظیم نحوه نمایش ویدیوها استفاده می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-message_stream-v1-messagestream"></a>

## استریم پیام — `bale.message_stream.v1.MessageStream`

این سرویس مدیریت ارسال و دریافت پیام‌های جریانی (stream) در بله را بر عهده دارد. کلاینت از طریق این سرویس می‌تواند پیام‌های بزرگ یا چند‌بخشی را به‌صورت قطعه‌قطعه (chunk) دریافت یا لغو کند.

نام‌فضای پایتون: `client.message_stream` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `CancelMessageStream` | `exPeer: ExPeer`، `messageId: MessageId` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که کلاینت بخواهد دریافت یک پیام جریانی در حال انجام را متوقف و لغو کند؛ با ارسال exPeer و messageId، سرور را از انصراف از آن استریم مطلع می‌سازد. |
| `ReceiveMessageStream` | `exPeer: ExPeer`، `messageId: MessageId`، `fromChunkId: Int32Value` | `chunkTimeoutMillis: Int32Value` | برای دریافت محتوای یک پیام جریانی به‌صورت قطعه‌ای استفاده می‌شود؛ کلاینت با ارسال exPeer، messageId و fromChunkId مشخص می‌کند که از کدام chunk به بعد داده می‌خواهد، که این امکان ادامه دریافت پس از وقفه را فراهم می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-messaging-v2-messaging"></a>

## پیام‌رسانی — `bale.messaging.v2.Messaging`

این سرویس هسته اصلی پیام‌رسانی بله را پوشش می‌دهد و امکان ارسال، دریافت، مدیریت پیام‌ها، مکالمات (dialog)، پوشه‌ها (folder) و موضوعات (topic) را فراهم می‌کند. کلاینت برای بارگذاری تاریخچه چت، فوروارد کردن پیام، حذف مکالمه و سازماندهی لیست چت‌ها از این سرویس استفاده می‌کند.

نام‌فضای پایتون: `client.messaging` — تعداد متد: 43

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `ArchiveDialogs` | `exPeers: repeated ExPeer` | ✔️ فقط تأیید | کلاینت این RPC را برای آرشیو کردن یک یا چند مکالمه (exPeers) فراخوانی می‌کند تا آن‌ها را از لیست اصلی چت‌ها پنهان کرده و در بخش آرشیو قرار دهد. |
| `ClearChat` | `peer: Peer` | `seq: int32`، `state: bytes` | زمانی که کاربر می‌خواهد تمام پیام‌های یک مکالمه مشخص (peer) را پاک کند بدون اینکه چت را حذف کند، این متد فراخوانی می‌شود. |
| `CreateFolder` | `name: string`، `peers: repeated ExPeer` | `folderId: int32`، `index: int32`، `unreadPeers: repeated ExPeer` | کلاینت با ارسال name و لیستی از peers این متد را برای ساخت یک پوشه جدید جهت دسته‌بندی مکالمات فراخوانی می‌کند. |
| `CreateReservedFolder` | `folderId: int32` | `index: int32`، `unreadPeers: repeated ExPeer` | برای ایجاد یک پوشه از پیش‌تعریف‌شده (سیستمی) با شناسه folderId استفاده می‌شود؛ احتمالاً برای پوشه‌های پیش‌فرض مانند «مکالمات شخصی» یا «کانال‌ها». |
| `CreateThread` | `peer: OutPeer`، `date: int64`، `randomId: int64`، `title: string` | `threadId: int32` | کلاینت با ارسال peer، title، date و randomId یک thread جدید (رشته گفتگو) در یک چت یا کانال ایجاد می‌کند تا پیام‌ها به صورت موضوعی دسته‌بندی شوند. |
| `CreateTopic` | `exPeer: ExPeer`، `title: string` | `topicId: MessageId` | برای ساخت یک موضوع (topic) جدید با عنوان title در یک گروه یا کانال مشخص (exPeer) استفاده می‌شود تا گفتگوها زیر آن موضوع سازماندهی شوند. |
| `DeleteChat` | `peer: Peer` | `seq: int32`، `state: bytes` | کلاینت این متد را با ارسال peer برای حذف کامل یک مکالمه از لیست چت‌های کاربر فراخوانی می‌کند. |
| `DeleteFolder` | `folderId: int32` | ✔️ فقط تأیید | با ارسال folderId یک پوشه دلخواه را حذف می‌کند؛ مکالمات داخل پوشه حذف نمی‌شوند بلکه از دسته‌بندی خارج می‌شوند. |
| `DeleteMessage` | `peer: Peer`، `rids: repeated int64`، `dates: T_LWL`، `justMine: BoolValue_1` | `seq: int32`، `state: bytes` | کلاینت با ارسال peer و لیست rids (شناسه پیام‌ها) یک یا چند پیام را حذف می‌کند؛ فیلد justMine مشخص می‌کند که آیا حذف فقط برای کاربر جاری باشد یا برای همه. |
| `DeleteTopic` | `exPeer: ExPeer`، `topicId: MessageId` | ✔️ فقط تأیید | برای حذف یک موضوع (topic) مشخص با topicId از یک گروه یا کانال (exPeer) استفاده می‌شود. |
| `EditFolder` | `folderId: int32`، `name: string`، `addedPeers: repeated ExPeer`، `deletedPeers: repeated ExPeer` | `unreadPeers: repeated ExPeer` | کلاینت با ارسال folderId، name جدید و لیست addedPeers و deletedPeers یک پوشه موجود را ویرایش می‌کند (تغییر نام یا افزودن/حذف مکالمات). |
| `EditTopic` | `exPeer: ExPeer`، `topicId: MessageId`، `title: string` | ✔️ فقط تأیید | برای ویرایش عنوان (title) یک موضوع موجود با topicId در یک گروه یا کانال (exPeer) فراخوانی می‌شود. |
| `FetchProtectedMessage` | `peer: OutPeer`، `messageId: MessageId` | `history: History` | برای دریافت محتوای یک پیام محافظت‌شده (مثلاً پیام‌های با محدودیت فوروارد یا ذخیره) با messageId از peer مشخص استفاده می‌شود. |
| `ForwardMessages` | `peer: OutPeer`، `rid: repeated int64`، `forwardedMessages: repeated QuotedMessageReference`، `groupedId: Int64Value_1` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | کلاینت با ارسال peer مقصد و لیست forwardedMessages این متد را برای فوروارد کردن پیام‌ها به یک مکالمه دیگر فراخوانی می‌کند؛ groupedId برای ارسال گروهی رسانه‌ها استفاده می‌شود. |
| `GetDiscussionMessage` | `peer: ExPeer`، `messageId: MessageId` | `discussionMessage: History` | برای دریافت پیام discussion (نظرات/بحث) مرتبط با یک پیام خاص (messageId) در peer فراخوانی می‌شود؛ معمولاً برای نمایش بحث‌های زیر پست‌های کانال به کار می‌رود. |
| `GetMessagesRepliesInfo` | `peer: ExPeer`، `mids: repeated MessageId` | `containers: repeated T_yze` | با ارسال peer و لیست mids اطلاعات ریپلای‌های چند پیام را به صورت یکجا دریافت می‌کند؛ برای نمایش تعداد پاسخ‌ها در رابط کاربری استفاده می‌شود. |
| `GetTopicByID` | `exPeer: ExPeer`، `topicId: MessageId` | `topic: Topic` | کلاینت با ارسال exPeer و topicId اطلاعات یک موضوع خاص را دریافت می‌کند؛ احتمالاً هنگام باز کردن یک topic یا رفرش اطلاعات آن فراخوانی می‌شود. |
| `GetTopics` | `exPeer: ExPeer`، `minDate: int64`، `limit: int32` | `topics: repeated Topic` | لیست موضوعات (topics) یک گروه یا کانال (exPeer) را از تاریخ minDate با محدودیت limit بارگذاری می‌کند؛ برای نمایش فهرست موضوعات در رابط کاربری استفاده می‌شود. |
| `LoadDialogs` | `minDate: int64`، `limit: int32`، `optimizations: repeated int32`، `dialogType: int32`، `excludePinnedDialogs: bool`، `archiveFilter: int32` | `groups: repeated Group`، `users: repeated User`، `dialogs: repeated Dialog`، `userPeers: repeated UserPeer`، `groupPeers: repeated GroupPeer` | کلاینت این متد را برای بارگذاری لیست مکالمات (inbox) کاربر با پارامترهایی مانند minDate، limit، dialogType و archiveFilter فراخوانی می‌کند تا صفحه اصلی چت‌ها را نمایش دهد. |
| `LoadFolderDialogs` | `minDate: int64`، `limit: int32`، `folderId: int32`، `archiveFilter: int32` | `dialogs: repeated Dialog` | مکالمات داخل یک پوشه مشخص (folderId) را با فیلتر تاریخ و archiveFilter بارگذاری می‌کند؛ هنگام ورود کاربر به یک پوشه فراخوانی می‌شود. |
| `LoadFolders` | `includeMutedUnreadPeers: bool`، `isNewUser: bool` | `folders: repeated Folder`، `unreadPeers: repeated UnreadPeer` | لیست تمام پوشه‌های کاربر را بارگذاری می‌کند؛ فیلدهای includeMutedUnreadPeers و isNewUser رفتار پاسخ را تنظیم می‌کنند و معمولاً در زمان اجرای اولیه اپلیکیشن فراخوانی می‌شود. |
| `LoadGroupedDialogs` | `optimizations: repeated int32`، `archiveFilter: int32` | `dialogs: repeated T_wpU`، `users: repeated User`، `groups: repeated Group`، `showArchived: BoolValue_1`، `showInvite: BoolValue_1`، `userPeers: repeated UserPeer`، `groupPeers: repeated GroupPeer` | مکالمات را به صورت دسته‌بندی‌شده (گروهی) با فیلتر archiveFilter بارگذاری می‌کند؛ احتمالاً برای نمایش مکالمات دسته‌بندی‌شده بر اساس نوع (مثلاً ربات‌ها، کانال‌ها) استفاده می‌شود. |
| `LoadHistory` | `peer: Peer`، `date: int64`، `loadMode: int32`، `limit: int32`، `optimizations: repeated int32` | `history: repeated History`، `users: repeated User`، `userPeers: repeated UserPeer`، `groups: repeated Group`، `groupPeers: repeated GroupPeer` | کلاینت با ارسال peer، date، loadMode و limit تاریخچه پیام‌های یک مکالمه را بارگذاری می‌کند؛ loadMode جهت بارگذاری (قبل یا بعد از تاریخ مشخص) را تعیین می‌کند. |
| `LoadPeerDialogs` | `peers: repeated Peer` | `dialogs: repeated Dialog`، `groups: repeated Group`، `users: repeated User`، `userPeers: repeated UserPeer`، `groupPeers: repeated GroupPeer` | اطلاعات dialog چند peer مشخص را به صورت یکجا دریافت می‌کند؛ برای به‌روزرسانی وضعیت مکالمات انتخابی (مثلاً پس از یک اعلان) استفاده می‌شود. |
| `LoadPeers` | — | `exPeers: repeated ExPeer` | احتمالاً لیست تمام peer‌های شناخته‌شده کاربر (مخاطبان، گروه‌ها، کانال‌ها) را بدون پارامتر ورودی بارگذاری می‌کند؛ برای مقداردهی اولیه حافظه محلی کلاینت استفاده می‌شود. |
| `LoadPinnedDialogs` | `folderId: int32` | `dialogs: repeated Dialog` | کلاینت با ارسال folderId این RPC را فراخوانی می‌کند تا فهرست مکالمات پین‌شده در یک پوشه خاص را بارگذاری کند. معمولاً هنگام باز شدن لیست چت‌ها یا تغییر پوشه فعال استفاده می‌شود. |
| `LoadPinnedMessages` | `peer: ExPeer` | `pinnedMessages: repeated History` | با ارسال peer، تمام پیام‌های پین‌شده در یک مکالمه (چت، گروه یا کانال) را واکشی می‌کند. کلاینت معمولاً هنگام نمایش بخش «پیام‌های پین‌شده» در هدر مکالمه این متد را صدا می‌زند. |
| `LoadReplies` | `peer: ExPeer`، `threadId: MessageId`، `date: int64`، `loadMode: int32`، `limit: int32` | `history: repeated History`، `users: repeated User`، `userPeers: repeated UserPeer` | برای بارگذاری ریپلای‌های یک thread مشخص در مکالمه‌ای با peer معین فراخوانی می‌شود؛ با استفاده از threadId، date، loadMode و limit می‌توان صفحه‌بندی و جهت بارگذاری را کنترل کرد. کلاینت این متد را هنگام باز کردن thread یک پیام و نمایش پاسخ‌های آن به‌کار می‌برد. |
| `MarkDialogsAsRead` | `peers: repeated ExPeer` | `seq: int32`، `state: bytes` | کلاینت با ارسال لیستی از peers این RPC را صدا می‌زند تا چندین مکالمه را یک‌جا به‌عنوان خوانده‌شده علامت بزند. معمولاً هنگامی که کاربر گزینه «علامت‌گذاری همه به‌عنوان خوانده‌شده» را انتخاب می‌کند استفاده می‌شود. |
| `MarkDialogsAsUnread` | `peers: repeated ExPeer` | `seq: int32`، `state: bytes` | با ارسال لیست peers، مکالمات انتخاب‌شده را به‌عنوان نخوانده علامت‌گذاری می‌کند تا کاربر بعداً به آن‌ها توجه کند. این عملکرد معادل «نشانه‌گذاری برای پیگیری بعدی» است. |
| `MentionRead` | `peer: ExPeer`، `messageId: MessageId` | ✔️ فقط تأیید | وقتی کاربر روی نوتیفیکیشن منشن (mention) کلیک می‌کند یا به پیامی که در آن تگ شده می‌رسد، کلاینت با ارسال peer و messageId این RPC را فراخوانی می‌کند تا سرور بداند آن منشن دیده شده است. |
| `MessageRead` | `peer: Peer`، `date: int64`، `exPeer: ExPeer` | ✔️ فقط تأیید | کلاینت پس از اینکه کاربر یک پیام را مشاهده کرد، با ارسال peer، exPeer و date این متد را فراخوانی می‌کند تا وضعیت «خوانده‌شده» (تیک دوبل) برای پیام‌های تا آن تاریخ ثبت شود. |
| `MessageReceived` | `peer: Peer`، `date: int64` | ✔️ فقط تأیید | کلاینت پس از دریافت موفق پیام‌ها (حتی پیش از نمایش به کاربر) با ارسال peer و date این RPC را صدا می‌زند تا سرور از تحویل پیام مطلع شود (معادل تیک اول). |
| `PinDialogs` | `peers: repeated ExPeer`، `folderId: int32` | `dialogs: repeated Dialog`، `peers: repeated ExPeer` | با ارسال لیست peers و folderId، مکالمات انتخاب‌شده را در پوشه مشخص پین می‌کند تا همیشه در بالای لیست چت‌ها نمایش داده شوند. کلاینت این متد را هنگام عمل «پین کردن مکالمه» از منوی کانتکست فراخوانی می‌کند. |
| `PinMessage` | `peer: ExPeer`، `messageId: MessageId`، `justMine: bool` | ✔️ فقط تأیید | با ارسال peer، messageId و فلگ justMine یک پیام خاص را در مکالمه پین می‌کند؛ اگر justMine برابر true باشد پین فقط برای کاربر جاری است، در غیر این صورت برای همه اعضا نمایش داده می‌شود. |
| `ReorderFolders` | — | ✔️ فقط تأیید | کلاینت پس از اینکه کاربر ترتیب پوشه‌های چت را تغییر داد این RPC را فراخوانی می‌کند تا ترتیب جدید پوشه‌ها در سرور ذخیره شود. احتمالاً ترتیب جدید در بدنه درخواست ارسال می‌شود (فیلدهای ورودی در داده‌های موجود مشخص نیستند). |
| `ReorderPinnedDialogs` | `peers: repeated ExPeer`، `folderId: int32` | `dialogs: repeated Dialog`، `peers: repeated ExPeer` | وقتی کاربر مکالمات پین‌شده را جابه‌جا می‌کند، کلاینت با ارسال لیست مرتب‌شده peers و folderId ترتیب جدید پین‌ها را در آن پوشه به سرور اعلام می‌کند. |
| `SendMessage` | `peer: Peer`، `rid: int64`، `message: Message`، `isOnlyForUser: Int32Value`، `quotedMessageReference: QuotedMessageReference`، `exPeer: OutPeer`، `isSilent: bool`، `threadId: MessageId` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | اصلی‌ترین RPC ارسال پیام است که با ارسال peer، rid، message و اختیاری‌هایی مانند quotedMessageReference (ریپلای)، isSilent (بدون نوتیف) و threadId (ارسال در thread) کار می‌کند. کلاینت هر بار که کاربر دکمه ارسال را می‌زند این متد را فراخوانی می‌کند. |
| `SendMultiMediaMessage` | `peer: OutPeer`، `multiMedia: repeated MultiMedia`، `repliedMessage: QuotedMessageReference`، `groupedId: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | برای ارسال همزمان چند فایل رسانه‌ای (تصویر، ویدیو و غیره) به‌صورت یک آلبوم گروه‌بندی‌شده با groupedId استفاده می‌شود؛ کلاینت این متد را هنگامی که کاربر چند رسانه را با هم انتخاب و ارسال می‌کند به‌کار می‌برد. |
| `UnArchiveDialogs` | `exPeers: repeated ExPeer` | ✔️ فقط تأیید | با ارسال لیست exPeers، مکالمات آرشیوشده را از آرشیو خارج کرده و به لیست اصلی چت‌ها باز می‌گرداند. کلاینت این متد را هنگام عملیات «خروج از آرشیو» فراخوانی می‌کند. |
| `UnPinMessages` | `peer: ExPeer`، `messageIds: repeated MessageId`، `all: bool` | ✔️ فقط تأیید | با ارسال peer، لیست messageIds و فلگ all، پین یک یا چند پیام را برمی‌دارد؛ اگر all برابر true باشد تمام پیام‌های پین‌شده آن مکالمه آزاد می‌شوند. کلاینت این متد را هنگام آنپین کردن پیام از منوی مدیریت پیام فراخوانی می‌کند. |
| `UnpinDialogs` | `peers: repeated ExPeer`، `folderId: int32` | ✔️ فقط تأیید | با ارسال لیست peers و folderId، مکالمات پین‌شده را از حالت پین خارج می‌کند تا در موقعیت عادی لیست چت‌ها قرار گیرند. کلاینت این متد را هنگام انتخاب گزینه «برداشتن پین» از منوی مکالمه صدا می‌زند. |
| `UpdateMessage` | `peer: Peer`، `rid: int64`، `updatedMessage: Message` | `seq: int32`، `date: int64`، `state: bytes`، `ext: map<string, bytes>` | برای ویرایش محتوای یک پیام ارسال‌شده با ارسال peer، rid و updatedMessage استفاده می‌شود. کلاینت این RPC را هنگامی که کاربر پیام خود را ویرایش و تأیید می‌کند فراخوانی می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-microbanki-v1-microbanki"></a>

## میکروبانکی (خدمات مالی) — `bale.microbanki.v1.MicroBanki`

این سرویس امکانات مالی و بانکی پیام‌رسان بله را فراهم می‌کند، از جمله احراز هویت برای خدمات پرداخت و مدیریت درخواست‌های مالی بین کاربران. کلاینت از این سرویس برای دریافت توکن دسترسی، مشاهده جزئیات درخواست پول و فهرست پرداخت‌های مرتبط استفاده می‌کند.

نام‌فضای پایتون: `client.micro_banki` — تعداد متد: 3

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetBamServiceToken` | `service: int64` | `endpoint: bytes`، `token: bytes` | کلاینت این RPC را برای دریافت توکن احراز هویت یک سرویس BAM (خدمات مالی بله) فراخوانی می‌کند؛ شناسه سرویس مورد نظر از طریق فیلد service ارسال می‌شود تا دسترسی به آن سرویس مالی خاص مجاز شود. |
| `GetMoneyRequestDetails` | `message: Msg` | `totalAmount: int64`، `payCount: int64`، `lastPayDate: int64`، `responseType: int64` | برای دریافت جزئیات یک درخواست پول (مبلغ، فرستنده، وضعیت و غیره) فراخوانی می‌شود؛ پیام مرتبط با درخواست از طریق فیلد message از نوع Msg ارسال می‌گردد تا اطلاعات کامل آن درخواست مالی نمایش داده شود. |
| `GetMoneyRequestPaymentList` | `message: Msg`، `loadMoreState: BytesValue` | `payment: repeated Payment`، `loadMoreState: BytesValue`، `responseType: int64`، `userPeers: repeated UserPeer`، `groupPeers: repeated GroupPeer` | فهرست پرداخت‌های انجام‌شده در قالب یک درخواست پول گروهی را برمی‌گرداند؛ کلاینت با ارسال message و در صورت نیاز loadMoreState برای صفحه‌بندی، لیست پرداخت‌کنندگان را به‌صورت تدریجی بارگذاری می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-my_bank-v1-mybank"></a>

## بانک من — `bale.my_bank.v1.MyBank`

این سرویس اطلاعات حساب بانکی کاربر در اکوسیستم بله را مدیریت می‌کند. از طریق این سرویس می‌توان به جزئیات کیف پول و حساب مالی مرتبط با کاربر دسترسی پیدا کرد.

نام‌فضای پایتون: `client.my_bank` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetMyBank` | — | `data: string`، `version: int32`، `itemsVersion: int32`، `isChanged: bool` | زمانی فراخوانی می‌شود که کاربر می‌خواهد اطلاعات حساب بانکی خود را در بله مشاهده کند. این RPC بدون نیاز به پارامتر ورودی، داده‌های حساب مالی مرتبط با کاربر جاری را برمی‌گرداند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-negah-v1-negah"></a>

## وضعیت مشاهده پیام‌ها — `bale.negah.v1.Negah`

سرویس Negah امکان دریافت اطلاعات مربوط به وضعیت خوانده‌شدن پیام‌ها را فراهم می‌کند. این سرویس به کلاینت اجازه می‌دهد بداند چه کاربرانی یک پیام مشخص را مشاهده کرده‌اند.

نام‌فضای پایتون: `client.negah` — تعداد متد: 1

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetMessageSeenList` | `peer: ExtNegahPeer`، `messageId: ExtNegahMessageId`، `page: int32`، `limit: int32` | `usersSeen: repeated ExtNegahUserSeen`، `count: int32` | این RPC فهرست کاربرانی را که یک پیام مشخص را خوانده‌اند برمی‌گرداند؛ کلاینت با ارسال peer، messageId، و پارامترهای صفحه‌بندی (page و limit) این اطلاعات را به‌صورت صفحه‌بندی‌شده دریافت می‌کند. معمولاً هنگامی فراخوانی می‌شود که کاربر روی شمارنده «مشاهده‌شده» یک پیام در گروه یا کانال ضربه می‌زند تا لیست کامل بینندگان را ببیند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-organizations-v1-organizations"></a>

## سازمان‌ها — `bale.organizations.v1.Organizations`

این سرویس امکان دسترسی به اطلاعات سازمانی کاربران بله را فراهم می‌کند. با استفاده از این سرویس می‌توان اطلاعات سازمان مرتبط با کاربر و مخاطبین سازمانی او را بازیابی کرد.

نام‌فضای پایتون: `client.organizations` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetUserOrganizationInfo` | — | `userOrganization: UserOrganization` | این RPC برای دریافت اطلاعات سازمان متصل به حساب کاربری فراخوانی می‌شود؛ احتمالاً هنگام ورود به بخش سازمانی اپلیکیشن یا نمایش پروفایل سازمانی کاربر استفاده می‌گردد. |
| `GetUserOrganizationalContacts` | — | `userPeers: repeated UserPeer` | این RPC فهرست مخاطبین سازمانی کاربر را برمی‌گرداند و احتمالاً هنگام نمایش دفترچه تماس سازمانی یا جستجوی همکاران درون سازمان فراخوانی می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-pfm-v1-pfm"></a>

## مدیریت مالی شخصی (PFM) — `bale.pfm.v1.Pfm`

این سرویس امکانات مدیریت مالی شخصی را در اختیار کاربران بله قرار می‌دهد و شامل دسته‌بندی تراکنش‌ها، برچسب‌گذاری، مشاهده حساب‌ها و تقسیم تراکنش‌ها می‌شود. کلاینت از این سرویس برای سازمان‌دهی، جستجو و تحلیل تراکنش‌های مالی کاربر استفاده می‌کند.

نام‌فضای پایتون: `client.pfm` — تعداد متد: 15

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AddDetailToTransaction` | `id: Id`، `detail: bytes` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که کاربر می‌خواهد توضیح یا جزئیات اضافی (detail) به یک تراکنش مشخص با id معین اضافه کند. این امکان دسته‌بندی و یادداشت‌گذاری روی تراکنش‌های مالی را فراهم می‌کند. |
| `AddTransactionTags` | `id: Id`، `tags: repeated Tags` | ✔️ فقط تأیید | برای افزودن یک یا چند برچسب (tags) به تراکنشی با id مشخص استفاده می‌شود. کاربر با این RPC می‌تواند تراکنش‌های خود را دسته‌بندی و برچسب‌گذاری کند تا بعداً راحت‌تر بیابد. |
| `AddUserTags` | `tags: repeated Tags` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که بخواهیم برچسب‌های جدید (tags) را در سطح کاربر ایجاد یا ثبت کنیم. احتمالاً برای تعریف دسته‌بندی‌های سفارشی کاربر جهت استفاده در برچسب‌گذاری تراکنش‌ها به‌کار می‌رود. |
| `FilterTaggedTransactions` | `ids: repeated Id` | `idsWithTag: repeated Id` | با ارسال لیستی از ids، تراکنش‌هایی را که دارای برچسب هستند فیلتر کرده و برمی‌گرداند. کلاینت از این RPC برای نمایش تراکنش‌های برچسب‌دار از میان مجموعه‌ای از شناسه‌ها استفاده می‌کند. |
| `GetSubTransactions` | `transactionId: Id` | `transactionIds: repeated Id` | با ارائه transactionId یک تراکنش والد، زیرتراکنش‌های مرتبط با آن را دریافت می‌کند. این RPC معمولاً پس از تقسیم یک تراکنش (SplitTransaction) برای نمایش اجزای آن فراخوانی می‌شود. |
| `GetTransactionTags` | `id: Id` | `tags: repeated Tags` | برچسب‌های اختصاص‌یافته به یک تراکنش با id مشخص را برمی‌گرداند. کلاینت از این RPC برای نمایش یا ویرایش برچسب‌های یک تراکنش در صفحه جزئیات تراکنش استفاده می‌کند. |
| `GetUserAccounts` | — | `accounts: repeated Account`، `config: T_KW` | فهرست حساب‌های مالی کاربر جاری را بدون نیاز به پارامتر ورودی بازمی‌گرداند. کلاینت معمولاً در هنگام بارگذاری بخش مالی اپلیکیشن این RPC را فراخوانی می‌کند تا حساب‌های موجود کاربر را نمایش دهد. |
| `GetUserTags` | `getUserTagType: int64` | `tags: repeated Tags` | برچسب‌های تعریف‌شده توسط کاربر را با توجه به نوع (getUserTagType) بازمی‌گرداند. کلاینت از این RPC برای پر کردن لیست برچسب‌های قابل انتخاب هنگام دسته‌بندی تراکنش‌ها استفاده می‌کند. |
| `LoadTransactions` | `accountNumber: int64`، `startDate: Int64Value_1`، `endDate: Int64Value_1`، `transactionType: int64`، `label: repeated Tags`، `limit: int64`، `loadMoreState: Offset`، `loadMode: int64`، `userTagType: int64` | `transactions: repeated Transaction`، `totalAmounts: repeated TotalAmount`، `loadMoreState: Offset`، `totalAmountsPerDay: repeated TotalAmountsPerDay` | تراکنش‌های یک حساب (accountNumber) را با فیلترهای بازه زمانی (startDate، endDate)، نوع تراکنش، برچسب، و صفحه‌بندی (limit، loadMoreState) بارگذاری می‌کند. این RPC اصلی‌ترین متد برای نمایش تاریخچه تراکنش‌های مالی کاربر است. |
| `LoadTransactionsByIDs` | `transactionIds: repeated Id` | `transactions: repeated Transaction` | اطلاعات کامل چند تراکنش را با دریافت لیستی از transactionIds به‌صورت دسته‌ای بازمی‌گرداند. زمانی استفاده می‌شود که کلاینت شناسه تراکنش‌های مشخصی را دارد و نیاز به جزئیات کامل آن‌ها دارد. |
| `RemoveTransaction` | `transactionIds: repeated Id` | ✔️ فقط تأیید | یک یا چند تراکنش با شناسه‌های مشخص (transactionIds) را حذف می‌کند. کاربر از این RPC برای پاک‌کردن تراکنش‌های اشتباه یا غیرضروری از لیست مدیریت مالی خود استفاده می‌کند. |
| `RemoveTransactionTags` | `id: Id`، `tags: repeated Tags` | ✔️ فقط تأیید | برچسب‌های مشخصی (tags) را از تراکنشی با id معین حذف می‌کند. کلاینت این RPC را هنگامی فراخوانی می‌کند که کاربر می‌خواهد دسته‌بندی یا برچسب یک تراکنش را اصلاح یا حذف کند. |
| `RemoveUserTags` | `tags: repeated Tags` | ✔️ فقط تأیید | برچسب‌های سفارشی (tags) را در سطح کاربر حذف می‌کند. احتمالاً زمانی فراخوانی می‌شود که کاربر یک دسته‌بندی دست‌ساز خود را دیگر نمی‌خواهد و آن را از لیست برچسب‌هایش پاک می‌کند. |
| `ReviveTransaction` | `transactionId: Id` | ✔️ فقط تأیید | یک تراکنش حذف‌شده را با ارائه transactionId بازیابی می‌کند. این RPC احتمالاً معکوس عملیات RemoveTransaction است و به کاربر اجازه می‌دهد تراکنش پاک‌شده را بازگرداند. |
| `SplitTransaction` | `transactionId: Id`، `units: repeated Unit` | `splitTransactionIds: repeated Id` | یک تراکنش (transactionId) را به چند بخش (units) تقسیم می‌کند تا کاربر بتواند هزینه‌های مختلف درون یک پرداخت واحد را جداگانه دسته‌بندی کند. این قابلیت برای مدیریت دقیق‌تر هزینه‌ها در اپلیکیشن مالی شخصی کاربرد دارد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-poll-v1-poll"></a>

## نظرسنجی — `bale.poll.v1.Poll`

این سرویس امکان ایجاد، مدیریت و مشاهده نتایج نظرسنجی‌ها را در بله فراهم می‌کند. کلاینت می‌تواند نظرسنجی بسازد، به آن رأی دهد، نتایج را دریافت کند یا آن را ببندد.

نام‌فضای پایتون: `client.poll` — تعداد متد: 5

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `ClosePoll` | `pollId: int64` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که سازنده نظرسنجی بخواهد آن را زودتر از موعد ببندد و دیگر کاربران نتوانند رأی دهند؛ با ارسال pollId نظرسنجی مورد نظر مشخص می‌شود. |
| `CreatePoll` | `pollMessage: PollMessage`، `createAt: int64`، `expeer: ExPeer` | `pollId: int64` | برای ساخت یک نظرسنجی جدید و ارسال آن به یک مکالمه یا کانال استفاده می‌شود؛ کلاینت اطلاعات نظرسنجی را در pollMessage، زمان ایجاد را در createAt و مقصد ارسال را در expeer مشخص می‌کند. |
| `GetFullPollResult` | `pollId: int64` | `fullPollResult: repeated FullPollResult` | جزئیات کامل نتایج یک نظرسنجی خاص را با ارسال pollId دریافت می‌کند؛ احتمالاً شامل لیست رأی‌دهندگان به هر گزینه نیز می‌شود. |
| `GetPollResults` | — | `pollResults: repeated PollResult` | نتایج نظرسنجی‌ها را به صورت خلاصه دریافت می‌کند؛ از آنجا که ورودی خاصی ندارد، احتمالاً نتایج تمام نظرسنجی‌های مرتبط با کاربر جاری را برمی‌گرداند. |
| `Vote` | `pollId: int64`، `isRetract: int64`، `voteAt: int64`، `optionIds: repeated int64` | `pollResult: PollResult` | هنگامی که کاربر به گزینه‌ای در نظرسنجی رأی می‌دهد یا رأی خود را پس می‌گیرد فراخوانی می‌شود؛ با pollId نظرسنجی، optionIds گزینه‌های انتخابی و isRetract مشخص می‌شود که آیا این عمل ثبت رأی است یا لغو آن. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-premium-v1-premium"></a>

## اشتراک پریمیوم — `bale.premium.v1.Premium`

این سرویس امکانات اشتراک ویژه (Premium) بله را مدیریت می‌کند، از جمله خرید بسته‌های پریمیوم، اعمال کد تخفیف، بررسی وضعیت اشتراک کاربران و مدیریت نشان‌های (badge) ویژه.

نام‌فضای پایتون: `client.premium` — تعداد متد: 7

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `CalculateDiscountedPrice` | `packageId: int64`، `couponCode: string` | `discountedPrice: int64` | کلاینت پیش از خرید، این RPC را با packageId و couponCode فراخوانی می‌کند تا قیمت نهایی بسته پریمیوم پس از اعمال کد تخفیف را محاسبه و به کاربر نمایش دهد. |
| `GetBadges` | — | `categories: repeated T__c` | برای دریافت فهرست تمام نشان‌های (badge) موجود در سیستم پریمیوم فراخوانی می‌شود تا کاربر بتواند نشان دلخواه خود را انتخاب کند. |
| `GetPackages` | — | `packages: repeated Package`، `bundles: map<string, bytes>` | کلاینت این RPC را برای دریافت لیست بسته‌های اشتراک پریمیوم قابل خرید فراخوانی می‌کند تا گزینه‌های موجود را به کاربر نمایش دهد. |
| `IsPremium` | `userId: int32`، `withDetailOption: WithDetailOption` | `userStatus: UserStatus` | با ارسال userId و withDetailOption بررسی می‌کند که آیا یک کاربر خاص اشتراک پریمیوم فعال دارد یا خیر؛ احتمالاً برای نمایش نشان‌های ویژه یا آزادسازی قابلیت‌های محدود شده استفاده می‌شود. |
| `IsPremiumBatch` | `userIds: repeated int32`، `withDetailOption: WithDetailOption` | `usersStatus: repeated UserStatus` | مشابه IsPremium اما برای چندین کاربر به‌صورت همزمان؛ کلاینت لیستی از userIds را ارسال می‌کند تا وضعیت پریمیوم همه آن‌ها را در یک درخواست واحد بررسی کند. |
| `PurchasePackage` | `packageId: int64`، `couponCode: StringValue` | `sadadPaymentToken: string` | پس از تأیید کاربر، این RPC با packageId و couponCode اختیاری فراخوانی می‌شود تا خرید بسته اشتراک پریمیوم از طریق کیف پول بله نهایی شود. |
| `SetUserBadge` | `badgeId: int64` | ✔️ فقط تأیید | کاربر پریمیوم با ارسال badgeId، نشان فعال خود را تغییر می‌دهد تا نشان انتخابی در پروفایل یا کنار نام او نمایش داده شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-presence-v1-presence"></a>

## حضور و وضعیت آنلاین — `bale.presence.v1.Presence`

این سرویس وضعیت آنلاین/آفلاین کاربران و اعضای گروه‌ها را مدیریت می‌کند. کلاینت از طریق این سرویس حضور مخاطبان را دریافت، به‌روزرسانی و دنبال می‌کند و همچنین وضعیت تایپ‌کردن را به طرف مقابل اطلاع می‌دهد.

نام‌فضای پایتون: `client.presence` — تعداد متد: 11

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetContactsPresences` | `limit: Int32Value` | `presences: repeated PresenceType` | کلاینت این RPC را برای دریافت وضعیت آنلاین/آفلاین مخاطبان خود فراخوانی می‌کند. پارامتر limit تعداد نتایج بازگشتی را محدود می‌کند و معمولاً هنگام باز شدن لیست مخاطبان استفاده می‌شود. |
| `GetGroupMembersPresences` | `peer: GroupPeer` | `presences: repeated PresenceType` | برای دریافت وضعیت حضور اعضای یک گروه مشخص از طریق peer از نوع GroupPeer فراخوانی می‌شود. معمولاً هنگام باز کردن پنل اعضای گروه یا نمایش افراد آنلاین در گروه استفاده می‌شود. |
| `GetGroupOnlineCount` | `peer: GroupPeer` | `count: int32` | تعداد اعضای آنلاین یک گروه را با ارسال peer از نوع GroupPeer برمی‌گرداند. کلاینت این RPC را برای نمایش شمارش آنلاین‌ها در هدر گفتگوی گروهی فراخوانی می‌کند. |
| `GetUsersPresence` | — | `presences: repeated PresenceType` | وضعیت حضور یک یا چند کاربر را بازمی‌گرداند؛ احتمالاً شناسه کاربران از طریق context یا session ارسال می‌شود چون ورودی صریحی ندارد. کلاینت هنگام نیاز به بررسی وضعیت آنلاین کاربران خاص این متد را صدا می‌زند. |
| `SetOnline` | `isOnline: bool`، `timeout: int64`، `deviceType: int32`، `deviceCategory: StringValue` | ✔️ فقط تأیید | کلاینت با ارسال isOnline، timeout، deviceType و deviceCategory وضعیت آنلاین یا آفلاین خود را به سرور اعلام می‌کند. این RPC به‌صورت دوره‌ای یا هنگام تغییر وضعیت برنامه (فعال/غیرفعال) فراخوانی می‌شود. |
| `StopTyping` | `peer: Peer`، `typingType: int32` | ✔️ فقط تأیید | کلاینت با ارسال peer و typingType به سرور اطلاع می‌دهد که کاربر تایپ‌کردن را متوقف کرده است. این RPC هنگام پاک‌کردن متن یا خروج از کادر ورودی پیام فراخوانی می‌شود. |
| `SubscribeFromGroupOnline` | `groups: repeated GroupPeer` | ✔️ فقط تأیید | کلاینت از دریافت به‌روزرسانی‌های آنلاین برای گروه‌های مشخص‌شده در لیست groups لغو اشتراک می‌کند. احتمالاً هنگام بستن گفتگوی گروهی یا خروج از صفحه گروه فراخوانی می‌شود. |
| `SubscribeFromOnline` | `users: repeated UserPeer` | ✔️ فقط تأیید | کلاینت اشتراک دریافت وضعیت آنلاین کاربران موجود در لیست users را لغو می‌کند. معمولاً هنگام بستن پروفایل یا خروج از گفتگو با آن کاربران فراخوانی می‌شود. |
| `SubscribeToGroupOnline` | `groups: repeated GroupPeer` | ✔️ فقط تأیید | کلاینت با ارسال لیست groups از نوع GroupPeer درخواست می‌کند که تغییرات وضعیت آنلاین اعضای آن گروه‌ها را دریافت کند. معمولاً هنگام ورود به گفتگوی گروهی برای نمایش تعداد آنلاین‌ها فراخوانی می‌شود. |
| `SubscribeToOnline` | `users: repeated UserPeer` | ✔️ فقط تأیید | کلاینت با ارسال لیست users از نوع UserPeer اشتراک به‌روزرسانی‌های آنلاین آن کاربران را برقرار می‌کند. معمولاً هنگام باز کردن گفتگوی خصوصی یا مشاهده پروفایل کاربر فراخوانی می‌شود. |
| `Typing` | `peer: Peer`، `typingType: int32` | ✔️ فقط تأیید | کلاینت با ارسال peer و typingType به سرور اعلام می‌کند که کاربر در حال تایپ‌کردن یا ضبط صدا/ویدیو در آن مکالمه است. این RPC به‌صورت دوره‌ای هنگام ورود متن در کادر پیام ارسال می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-ramz-v1-ramz"></a>

## رمز و احراز هویت — `bale.ramz.v1.Ramz`

این سرویس مدیریت رمز عبور دوم (رمز بله) و فرآیند احراز هویت از طریق OTP را برعهده دارد. کلاینت از این سرویس برای تنظیم، بررسی، حذف و بازیابی رمز، و همچنین ارسال و اعتبارسنجی کد یک‌بار مصرف استفاده می‌کند.

نام‌فضای پایتون: `client.ramz` — تعداد متد: 7

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `CheckPassword` | `password: string`، `servicesType: int32` | `token: string` | زمانی فراخوانی می‌شود که کلاینت می‌خواهد صحت رمز عبور وارد‌شده توسط کاربر را تأیید کند؛ فیلد password رمز متنی و servicesType نوع سرویس موردنظر (مثلاً کیف پول یا سرویس خاص) را مشخص می‌کند. |
| `CheckPasswordSet` | — | `hasSet: bool`، `isSessionAuthorized: bool` | کلاینت این RPC را برای بررسی اینکه آیا کاربر از قبل رمز عبور تنظیم کرده است یا خیر فراخوانی می‌کند، تا در رابط کاربری گزینه‌های «تنظیم رمز» یا «تغییر رمز» را به‌درستی نمایش دهد. |
| `DeletePassword` | `otp: int32` | ✔️ فقط تأیید | برای حذف رمز عبور کاربر استفاده می‌شود؛ کلاینت کد OTP دریافت‌شده (فیلد otp) را جهت احراز هویت ارسال می‌کند تا عملیات حذف تأیید شود. |
| `ForgetPassword` | — | ✔️ فقط تأیید | هنگامی که کاربر رمز خود را فراموش کرده فراخوانی می‌شود و فرآیند بازیابی رمز را آغاز می‌کند؛ احتمالاً پس از این درخواست، یک OTP برای کاربر ارسال خواهد شد. |
| `SendOTP` | — | ✔️ فقط تأیید | کلاینت این RPC را برای درخواست ارسال کد یک‌بار مصرف (OTP) به کاربر فراخوانی می‌کند، معمولاً پیش از عملیات حساسی مانند حذف رمز یا تأیید هویت. |
| `SetPassword` | `password: string` | ✔️ فقط تأیید | برای تنظیم یا تغییر رمز عبور کاربر به کار می‌رود؛ کلاینت رمز جدید را از طریق فیلد password ارسال می‌کند. |
| `ValidateOTP` | `otp: int32`، `servicesType: int32` | `otpValid: bool` | کلاینت این RPC را برای اعتبارسنجی کد OTP وارد‌شده توسط کاربر فراخوانی می‌کند؛ فیلد otp کد دریافتی و servicesType نوع سرویسی که احراز هویت برای آن انجام می‌شود را مشخص می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-recommender-v1-recommender"></a>

## پیشنهاد کانال‌ها و گروه‌ها — `bale.recommender.v1.Recommender`

این سرویس مسئول ارائه پیشنهادهای هوشمند کانال‌ها و گروه‌ها به کاربران بله است. کلاینت با فراخوانی متدهای این سرویس، لیست کانال‌ها یا گروه‌های پیشنهادی و مرتبط را برای نمایش به کاربر دریافت می‌کند.

نام‌فضای پایتون: `client.recommender` — تعداد متد: 4

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetChannelRecommendations` | — | `channels: repeated GroupPeer` | کلاینت این متد را برای دریافت فهرست کانال‌های پیشنهادی برای کاربر فعلی فراخوانی می‌کند، بدون نیاز به ارسال پارامتر خاصی. احتمالاً در صفحه «کشف کانال‌ها» یا هنگام نمایش پیشنهادهای شخصی‌سازی‌شده استفاده می‌شود. |
| `GetGroupsRecommendation` | `source: int64` | `groups: repeated GroupPeer` | کلاینت این متد را با ارسال فیلد source (شناسه منبع به صورت int64) فراخوانی می‌کند تا فهرست گروه‌های پیشنهادی مرتبط با آن منبع را دریافت کند؛ احتمالاً برای نمایش گروه‌های مشابه یا مرتبط با یک گروه مشخص به کار می‌رود. |
| `GetRelatedChannels` | `exPeer: ExPeer` | `relatedChannels: repeated RelatedChannel` | کلاینت با ارسال exPeer (اطلاعات کانال مورد نظر) این متد را فراخوانی می‌کند تا لیست کانال‌های مرتبط با آن کانال را دریافت کند؛ معمولاً برای نمایش بخش «کانال‌های مشابه» در صفحه پروفایل کانال استفاده می‌شود. |
| `GetRelatedGroups` | `exPeer: ExPeer` | `relatedGroups: repeated RelatedGroup` | کلاینت با ارسال exPeer (اطلاعات گروه مورد نظر) این متد را فراخوانی می‌کند تا گروه‌های مرتبط با آن گروه را دریافت کند؛ احتمالاً برای پیشنهاد گروه‌های مشابه در صفحه پروفایل گروه به کار می‌رود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-report-v1-report"></a>

## گزارش محتوا — `bale.report.v1.Report`

این سرویس امکان گزارش‌دهی محتوای نامناسب و مدیریت گزارش‌های ارسال‌شده را در پیام‌رسان بله فراهم می‌کند. کلاینت از این سرویس برای اعلام تخلف یا رد کردن یک گزارش قبلی استفاده می‌کند.

نام‌فضای پایتون: `client.report` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `ReportDismiss` | `exPeer: ExPeer` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که کاربر یا سیستم بخواهد گزارش ثبت‌شده‌ای را برای یک peer مشخص (exPeer) نادیده بگیرد یا رد کند. این RPC احتمالاً پس از بررسی و بی‌اعتبار دانستن یک گزارش قبلی استفاده می‌شود. |
| `ReportInappropriateContent` | `report: ReportType` | ✔️ فقط تأیید | هنگامی فراخوانی می‌شود که کاربر بخواهد محتوایی را به عنوان نامناسب گزارش دهد؛ نوع تخلف از طریق فیلد report با نوع ReportType مشخص می‌شود. این RPC پایه‌ی سیستم گزارش محتوای مخالف قوانین در بله است. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-sap-v1-sap"></a>

## کارت‌های بانکی و پرداخت (SAP) — `bale.sap.v1.Sap`

این سرویس مدیریت کارت‌های بانکی کاربر در اپلیکیشن بله را بر عهده دارد و عملیاتی نظیر افزودن، حذف، تنظیم کارت پیش‌فرض و انتقال وجه کارت‌به‌کارت را فراهم می‌کند. همچنین فرآیند تأیید هویت (OTP) و ثبت کارت جدید را پشتیبانی می‌کند.

نام‌فضای پایتون: `client.sap` — تعداد متد: 16

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AddDestinationCards` | `cards: repeated Card` | `ids: repeated bytes` | کلاینت این RPC را برای افزودن یک یا چند کارت مقصد (cards) به لیست کارت‌های ذخیره‌شده برای انتقال وجه فراخوانی می‌کند. این کارت‌ها در پرداخت‌های بعدی به عنوان مقصد سریع در دسترس خواهند بود. |
| `AddNewCards` | `cardInfo: repeated CardInfo` | `cardId: repeated bytes` | زمانی که کاربر می‌خواهد کارت بانکی جدیدی را به حساب خود اضافه کند، کلاینت این RPC را با اطلاعات کارت (cardInfo) فراخوانی می‌کند. این متد اطلاعات یک یا چند کارت جدید را ثبت و به پروفایل کاربر پیوند می‌زند. |
| `DeliverOtp` | `cardId: bytes`، `destinationPan: bytes`، `amount: int64`، `accessAddress: bytes`، `approvalCode: bytes` | `isDone: BoolValue_2` | در فرآیند تأیید تراکنش، کلاینت این RPC را با شناسه کارت (cardId)، شماره کارت مقصد (destinationPan)، مبلغ (amount) و کد تأیید (approvalCode) فراخوانی می‌کند تا رمز یکبار مصرف (OTP) ارسال شود. این مرحله معمولاً پیش از نهایی‌سازی انتقال وجه انجام می‌شود. |
| `EditCardExpirationDate` | `cardId: bytes`، `cardExpDate: CardExpDate` | ✔️ فقط تأیید | کلاینت این RPC را برای به‌روزرسانی تاریخ انقضای یک کارت ثبت‌شده با ارسال cardId و cardExpDate جدید فراخوانی می‌کند. این عملیات زمانی لازم است که کارت تجدید شده و تاریخ انقضا تغییر کرده باشد. |
| `EnrollNewCard` | `origin: Offset` | `transactionId: bytes`، `url: bytes` | کلاینت این RPC را برای شروع فرآیند ثبت‌نام کارت بانکی جدید با مشخص کردن مبدأ (origin) فراخوانی می‌کند. احتمالاً این متد پیش‌مرحله‌ای برای هدایت کاربر به فرآیند احراز هویت و وارد کردن اطلاعات کارت است. |
| `GetCardInfo` | `transactionId: bytes`، `cardInfo: CardInfo`، `cardId: Offset` | `cardId: bytes`، `maskedPan: bytes` | کلاینت این RPC را برای دریافت اطلاعات تکمیلی یک کارت بانکی با استفاده از transactionId، cardInfo یا cardId فراخوانی می‌کند. این اطلاعات معمولاً در صفحه جزئیات کارت یا هنگام انجام تراکنش نمایش داده می‌شود. |
| `GetCards` | — | `userCards: repeated UserCard` | کلاینت این RPC را برای دریافت لیست تمام کارت‌های بانکی ثبت‌شده کاربر فراخوانی می‌کند. این متد معمولاً هنگام باز کردن بخش کیف پول یا صفحه پرداخت فراخوانی می‌شود تا کارت‌های موجود نمایش داده شوند. |
| `GetDefaultCard` | — | `cardId: Offset` | کلاینت این RPC را برای دریافت کارت پیش‌فرض کاربر فراخوانی می‌کند. این اطلاعات برای پیش‌انتخاب خودکار کارت در فرم‌های پرداخت و انتقال وجه استفاده می‌شود. |
| `GetDestinationCardInfo` | `cardId: bytes`، `destinationPan: bytes`، `amount: int64`، `sourceAddress: bytes`، `localize: int64`، `targetUserId: Int32Value_1`، `messageData: Msg` | `cardHolderName: bytes`، `approvalCode: bytes` | کلاینت این RPC را پیش از انتقال وجه با ارسال cardId، destinationPan، amount و اطلاعات targetUserId فراخوانی می‌کند تا اطلاعات کارت مقصد (نام صاحب حساب و غیره) را واکشی و به کاربر نمایش دهد. این مرحله به کاربر کمک می‌کند صحت کارت مقصد را پیش از تأیید نهایی بررسی کند. |
| `GetDestinationCards` | — | `cards: repeated Card` | کلاینت این RPC را برای دریافت لیست کارت‌های مقصد ذخیره‌شده فراخوانی می‌کند. این کارت‌ها به عنوان مقاصد سریع در صفحه انتقال وجه کارت‌به‌کارت نمایش داده می‌شوند. |
| `ReactivateApp` | — | `transactionId: bytes`، `reactivationAddress: bytes` | این RPC احتمالاً برای فعال‌سازی مجدد سرویس پرداخت یا کیف پول پس از یک دوره غیرفعالی یا تغییر وضعیت حساب فراخوانی می‌شود. کلاینت این متد را بدون ارسال پارامتر فراخوانی می‌کند. |
| `RemoveCard` | `cardId: bytes` | ✔️ فقط تأیید | کلاینت این RPC را با ارسال cardId برای حذف یک کارت بانکی از لیست کارت‌های ثبت‌شده کاربر فراخوانی می‌کند. این عملیات معمولاً از صفحه مدیریت کارت‌ها توسط کاربر انجام می‌شود. |
| `RemoveDefaultCard` | — | ✔️ فقط تأیید | کلاینت این RPC را برای لغو انتخاب کارت پیش‌فرض کاربر فراخوانی می‌کند. پس از این عملیات، هیچ کارتی به عنوان پیش‌فرض انتخاب نخواهد بود. |
| `RemoveDestinationCards` | `ids: repeated bytes` | ✔️ فقط تأیید | کلاینت این RPC را با ارسال لیستی از ids برای حذف یک یا چند کارت مقصد ذخیره‌شده فراخوانی می‌کند. این عملیات زمانی انجام می‌شود که کاربر می‌خواهد مقاصد سریع پرداخت خود را مدیریت کند. |
| `SetDefaultCard` | `cardId: bytes` | ✔️ فقط تأیید | کلاینت این RPC را با ارسال cardId برای تعیین یک کارت به عنوان کارت پیش‌فرض پرداخت فراخوانی می‌کند. کارت انتخاب‌شده در تمام تراکنش‌های آینده به صورت خودکار پیش‌انتخاب می‌شود. |
| `TransferMoneyByCard` | `cardId: bytes`، `transferCode: int64`، `destinationPan: bytes`، `amount: int64`، `pin: bytes`، `cvv2: bytes`، `expiryDate: bytes`، `sourceAddress: bytes`، `localize: int64`، `approvalCode: bytes`، `encryptedTransferInfo: Offset`، `messageData: Msg`، `targetUserId: Int32Value_1`، `description: Offset`، `ramzToken: Offset` | `traceNumber: bytes`، `transactionTime: bytes` | کلاینت این RPC را برای انجام انتقال وجه کارت‌به‌کارت با ارسال اطلاعات کامل تراکنش شامل cardId، destinationPan، amount، pin، cvv2، expiryDate و approvalCode فراخوانی می‌کند. این متد نقطه اصلی اجرای پرداخت در سرویس SAP است و پس از تأیید OTP نهایی می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-schedule-v1-scheduler"></a>

## زمان‌بندی وظایف — `bale.schedule.v1.Scheduler`

این سرویس امکان تعریف، مدیریت و اجرای وظایف زمان‌بندی‌شده (مانند ارسال پیام زمان‌بندی‌شده) را در پیام‌رسان بله فراهم می‌کند. کلاینت می‌تواند وظایف جدید برای یک peer ایجاد کند، زمان اجرا را تغییر دهد یا آن‌ها را لغو نماید.

نام‌فضای پایتون: `client.scheduler` — تعداد متد: 6

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `ExecuteTaskNow` | `taskID: int64` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که کاربر بخواهد یک وظیفه‌ی زمان‌بندی‌شده را پیش از موعد مقرر و فوری اجرا کند؛ کلاینت taskID مورد نظر را ارسال می‌کند تا سرور آن را بلافاصله اجرا نماید. |
| `ListTasks` | `exPeer: ExPeer`، `type: int64`، `status: int64` | `tasks: repeated Task` | برای دریافت فهرست وظایف زمان‌بندی‌شده‌ی مربوط به یک exPeer خاص استفاده می‌شود؛ کلاینت می‌تواند با فیلترهای type و status فقط وظایف با نوع یا وضعیت مشخص را دریافت کند. |
| `PeersWithScheduleTask` | — | `exPeer: repeated ExPeer` | احتمالاً برای دریافت فهرست peer‌هایی که حداقل یک وظیفه‌ی زمان‌بندی‌شده‌ی فعال دارند فراخوانی می‌شود، تا کلاینت بتواند نمایی کلی از مکالمات دارای پیام زمان‌بندی‌شده نشان دهد. |
| `ReScheduleTask` | `taskID: int64`، `scheduledAt: bytes`، `payload: T_Q_` | ✔️ فقط تأیید | زمانی استفاده می‌شود که کاربر بخواهد زمان اجرا یا محتوای یک وظیفه‌ی موجود را تغییر دهد؛ کلاینت taskID، زمان جدید scheduledAt و payload به‌روزشده را ارسال می‌کند. |
| `ScheduleTask` | `exPeer: ExPeer`، `scheduledAt: bytes`، `payload: T_Q_` | `taskId: int64` | برای ایجاد یک وظیفه‌ی زمان‌بندی‌شده‌ی جدید برای یک exPeer فراخوانی می‌شود؛ کلاینت زمان اجرا scheduledAt و محتوای عملیات payload را ارسال می‌کند تا سرور در موعد مقرر آن را اجرا نماید. |
| `UnScheduleTask` | — | ✔️ فقط تأیید | برای لغو و حذف یک وظیفه‌ی زمان‌بندی‌شده استفاده می‌شود تا دیگر در زمان تعیین‌شده اجرا نشود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-search-v1-search"></a>

## جستجو — `bale.search.v1.Search`

این سرویس قابلیت‌های جستجو در پیام‌رسان بله را فراهم می‌کند و به کلاینت امکان می‌دهد پیام‌ها، مخاطبان، رسانه‌ها، دیالوگ‌ها، اعضای گروه، محصولات مارکت و mini-appها را بر اساس کوئری جستجو کند. همچنین پیشنهاد peer و نمایش محتوای محبوب مارکت از دیگر قابلیت‌های این سرویس است.

نام‌فضای پایتون: `client.search` — تعداد متد: 12

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `RecommendPeer` | `exPeerType: int64` | `peer: repeated Peer` | کلاینت این RPC را برای دریافت فهرست peer های پیشنهادی (مخاطبان، گروه‌ها یا کانال‌ها) فراخوانی می‌کند. فیلد exPeerType نوع peer هایی که باید از نتایج حذف شوند را مشخص می‌کند. |
| `SearchContent` | `query: Query`، `contentType: int64`، `loadMoreState: BytesValue` | `contentResults: repeated ContentResult`، `loadMoreState: BytesValue`، `resultCount: int64` | برای جستجوی محتوا (مثلاً پیام، فایل یا لینک) بر اساس query و نوع محتوا (contentType) استفاده می‌شود. فیلد loadMoreState امکان صفحه‌بندی و بارگذاری نتایج بیشتر را فراهم می‌کند. |
| `SearchDialog` | `query: Query` | `dialogResults: repeated DialogResult` | کلاینت هنگامی که کاربر در کادر جستجو تایپ می‌کند این RPC را با query فراخوانی می‌کند تا دیالوگ‌های مطابق (چت‌های خصوصی، گروه‌ها یا کانال‌ها) را بیابد. |
| `SearchMarket` | `query: Query`، `withCategory: BoolValue_1`، `loadMoreState: BytesValue` | `marketResults: repeated MarketResult`، `category: T_iE_88717`، `loadMoreState: BytesValue`، `resultCount: int64` | برای جستجو در مارکت بله بر اساس query استفاده می‌شود؛ با تنظیم withCategory می‌توان نتایج را همراه با دسته‌بندی دریافت کرد و loadMoreState صفحه‌بندی را مدیریت می‌کند. |
| `SearchMarketPopular` | — | `popularResults: repeated PopularResult` | کلاینت این RPC را بدون هیچ ورودی‌ای فراخوانی می‌کند تا فهرست محبوب‌ترین آیتم‌های مارکت (mini-appها یا سرویس‌ها) را برای نمایش در صفحه اصلی مارکت دریافت کند. |
| `SearchMedia` | `query: AndQuery`، `date: Int64Value_1`، `optimizations: repeated int64`، `loadMode: int64` | `searchResults: repeated SearchResult`، `users: repeated User`، `groups: repeated Group`، `loadMoreState: BytesValue`، `userOutPeers: repeated UserPeer`، `groupOutPeers: repeated GroupPeer`، `resultCount: int64` | برای جستجوی رسانه‌ها (تصویر، ویدیو، فایل و غیره) با فیلتر تاریخ (date) و کوئری ترکیبی (AndQuery) استفاده می‌شود. پارامترهای optimizations و loadMode رفتار بارگذاری و بهینه‌سازی نتایج را کنترل می‌کنند. |
| `SearchMembers` | `query: Query`، `exPeer: ExPeer`، `loadMoreState: BytesValue`، `users: repeated UserPeer` | `users: repeated UserPeer`، `loadMoreState: BytesValue` | هنگامی که ادمین یا کاربر می‌خواهد اعضای یک گروه یا کانال (exPeer) را با نام جستجو کند این RPC فراخوانی می‌شود. فیلد users امکان محدود کردن جستجو به مجموعه‌ای مشخص از کاربران را می‌دهد و loadMoreState صفحه‌بندی را پشتیبانی می‌کند. |
| `SearchMessageMore` | `loadMoreState: BytesValue`، `query: AndQuery`، `optimizations: repeated int64` | `searchResults: repeated SearchResult`، `users: repeated User`، `groups: repeated Group`، `loadMoreState: BytesValue`، `userOutPeers: repeated UserPeer`، `groupOutPeers: repeated GroupPeer`، `resultCount: int64` | پس از یک جستجوی اولیه پیام، کلاینت برای بارگذاری صفحه بعدی نتایج این RPC را با loadMoreState دریافت‌شده از پاسخ قبلی فراخوانی می‌کند. query و optimizations باید با درخواست اولیه یکسان باشند. |
| `SearchMessages` | `query: AndQuery`، `optimizations: repeated int64` | `searchResults: repeated SearchResult`، `users: repeated User`، `groups: repeated Group`، `loadMoreState: BytesValue`، `userOutPeers: repeated UserPeer`، `groupOutPeers: repeated GroupPeer`، `resultCount: int64` | کلاینت این RPC را برای شروع جستجوی پیام‌ها با یک AndQuery (کوئری ترکیبی) فراخوانی می‌کند. پارامتر optimizations کنترل می‌کند که سرور چه بهینه‌سازی‌هایی روی نتایج اعمال کند. |
| `SearchPeer` | `query: repeated AndQuery`، `optimizations: repeated int64` | `searchResults: repeated T_I_`، `users: repeated User`، `groups: repeated Group`، `userPeers: repeated UserPeer`، `groupPeers: repeated GroupPeer` | برای جستجوی peer (کاربر، گروه یا کانال) با یک یا چند AndQuery استفاده می‌شود. احتمالاً هنگام تایپ نام در کادر جستجوی مخاطبان یا ارسال پیام جدید فراخوانی می‌شود. |
| `SearchProduct` | `query: Query`، `loadMoreState: BytesValue` | `productResults: repeated ProductResult`، `loadMoreState: BytesValue`، `resultCount: int64` | کلاینت این RPC را برای جستجوی محصولات در مارکت بله بر اساس query فراخوانی می‌کند؛ loadMoreState امکان دریافت صفحات بعدی نتایج را فراهم می‌کند. |
| `UpdateSearchContentClick` | `messageId: Msg`، `searchTab: int64` | ✔️ فقط تأیید | هنگامی که کاربر روی یک نتیجه جستجوی محتوا کلیک می‌کند، کلاینت این RPC را با messageId و searchTab (تب فعال جستجو) فراخوانی می‌کند تا رویداد کلیک برای تحلیل و بهبود رتبه‌بندی نتایج ثبت شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-shared_media-v1-sharedmediaservice"></a>

## رسانه‌های مشترک — `bale.shared_media.v1.SharedMediaService`

این سرویس امکان دسترسی به رسانه‌های به اشتراک گذاشته‌شده در مکالمات بله را فراهم می‌کند. کلاینت از آن برای واکشی و مرور تصاویر، ویدیوها و سایر فایل‌های رد و بدل‌شده با یک peer خاص استفاده می‌کند.

نام‌فضای پایتون: `client.shared_media_service` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetActiveSharedMedia` | `exPeer: ExPeer` | ✔️ فقط تأیید | کلاینت با ارسال exPeer، فهرست دسته‌بندی‌های فعال رسانه‌های مشترک (مثلاً عکس، فایل، لینک) را برای یک مکالمه دریافت می‌کند. این فراخوانی معمولاً هنگام باز کردن بخش «رسانه‌های مشترک» در پروفایل یک چت انجام می‌شود تا مشخص شود چه نوع محتوایی موجود است. |
| `LoadMedia` | `exPeer: ExPeer`، `date: Int64Value_1`، `contentType: int64`، `loadMode: int64`، `minimumResults: int64` | `mediaResults: repeated MediaResult` | کلاینت با ارسال exPeer، date (نقطه شروع زمانی)، contentType (نوع رسانه)، loadMode (جهت بارگذاری) و minimumResults، صفحه‌ای از رسانه‌های مشترک را واکشی می‌کند. این RPC برای پیمایش و بارگذاری تدریجی (lazy load) لیست رسانه‌های یک مکالمه به کار می‌رود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-story-v1-story"></a>

## استوری‌ها — `bale.story.v1.Story`

این سرویس مدیریت کامل استوری‌های بله را در اختیار کلاینت می‌گذارد؛ از انتشار و حذف استوری برای کاربران، ربات‌ها و کانال‌ها گرفته تا دریافت بازدیدکنندگان، واکنش‌ها، تگ‌ها و تنظیمات حریم خصوصی مرتبط با استوری.

نام‌فضای پایتون: `client.story` — تعداد متد: 23

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AddBotStory` | `exPeer: ExPeer`، `mediaStory: StoryContent`، `textStory: TextStory`، `tagIds: repeated int64`، `expirationType: int64` | `storyId: bytes` | هنگامی که یک ربات (با شناسه exPeer) می‌خواهد استوری رسانه‌ای یا متنی منتشر کند، این RPC فراخوانی می‌شود. کلاینت محتوای استوری (mediaStory یا textStory)، tagIds و expirationType را ارسال می‌کند تا استوری با تنظیمات انقضای مشخص برای ربات ایجاد گردد. |
| `AddChannelStory` | `exPeer: ExPeer`، `mediaStory: StoryContent`، `hasReply: int64`، `tagIds: repeated int64`، `expirationType: int64`، `textStory: TextStory` | `storyId: bytes` | برای انتشار استوری در یک کانال (با exPeer) فراخوانی می‌شود؛ کلاینت محتوای رسانه‌ای یا متنی، tagIds، expirationType و وضعیت امکان پاسخ (hasReply) را ارسال می‌کند تا استوری جدیدی در آن کانال ثبت شود. |
| `AddStory` | `mediaStory: StoryContent`، `textStory: TextStory`، `tagIds: repeated int64`، `expirationType: int64`، `exceptionType: int64` | `storyId: bytes` | کاربر برای انتشار استوری شخصی خود این RPC را صدا می‌زند؛ mediaStory یا textStory به همراه tagIds، expirationType و exceptionType (تعیین استثناهای دسترسی) ارسال می‌شوند. |
| `CanAddBotStory` | `botUserId: int64` | `canAddBotStory: int64` | پیش از انتشار استوری برای یک ربات، کلاینت با ارسال botUserId بررسی می‌کند که آیا آن ربات مجاز به داشتن استوری است یا نه. |
| `CheckLinkValidity` | `exPeer: ExPeer`، `link: bytes` | ✔️ فقط تأیید | برای تأیید اعتبار یک لینک (link) مرتبط با استوری در یک peer مشخص (exPeer) فراخوانی می‌شود؛ احتمالاً پیش از افزودن لینک به محتوای استوری استفاده می‌شود. |
| `GetBotStories` | — | `result: repeated BotStoryResult`، `popularityList: repeated PopularityList` | فهرست استوری‌های فعال ربات‌های مرتبط با کاربر جاری را بازمی‌گرداند؛ کلاینت برای نمایش استوری ربات‌ها در بخش مخصوص آن‌ها این RPC را فراخوانی می‌کند. |
| `GetChannelStories` | — | `result: repeated Result`، `popularityList: repeated PopularityList` | استوری‌های کانال‌هایی که کاربر در آن‌ها عضو است را دریافت می‌کند؛ برای نمایش استوری کانال‌ها در رابط کاربری استفاده می‌شود. |
| `GetDefaultStoryBackgrounds` | — | `defaultStoryBackgrounds: repeated StoryContent` | لیست پس‌زمینه‌های پیش‌فرض برای استوری متنی را از سرور دریافت می‌کند؛ معمولاً هنگام باز شدن ویرایشگر استوری متنی فراخوانی می‌شود. |
| `GetMostPopularStories` | `getSpecialStories: BoolValue_1`، `optimization: int64` | `result: repeated Result`، `popularityList: repeated PopularityList` | پرمخاطب‌ترین استوری‌ها را برمی‌گرداند؛ با ارسال getSpecialStories می‌توان استوری‌های ویژه را هم درخواست کرد و پارامتر optimization کیفیت پاسخ را تنظیم می‌کند. |
| `GetStories` | `getUnmutual: BoolValue_1` | `result: repeated UserStory`، `popularityList: repeated PopularityList` | استوری‌های مخاطبان کاربر را بازمی‌گرداند؛ با تنظیم getUnmutual می‌توان استوری کاربرانی را که رابطه متقابل ندارند نیز دریافت کرد. |
| `GetStoriesByList` | `exPeers: repeated ExPeer` | `userStories: repeated UserStory`، `channelStories: repeated Result`، `botStories: repeated BotStoryResult` | استوری‌های مجموعه‌ای از peer های مشخص (exPeers) را به‌صورت دسته‌ای دریافت می‌کند؛ برای بارگذاری هم‌زمان استوری چندین کاربر یا کانال استفاده می‌شود. |
| `GetStoryById` | `storyId: bytes` | `result: UserStory`، `channelStoryResult: Result`، `botStoryResult: BotStoryResult` | با ارسال storyId یک استوری خاص را از سرور دریافت می‌کند؛ معمولاً برای نمایش مستقیم یا دیپ‌لینک به یک استوری مشخص فراخوانی می‌شود. |
| `GetStoryReactionEmojis` | — | `emojis: repeated Emoji` | فهرست اموجی‌های مجاز برای واکنش به استوری را از سرور دریافت می‌کند؛ هنگام نمایش پنل واکنش به کاربر استفاده می‌شود. |
| `GetStoryTags` | — | `tags: repeated T_vw` | لیست تگ‌های قابل استفاده در استوری را برمی‌گرداند؛ کلاینت این داده را برای نمایش گزینه‌های تگ‌گذاری هنگام ایجاد استوری استفاده می‌کند. |
| `GetStoryWidgets` | `storyId: bytes` | `widgets: repeated Widget` | ویجت‌های تعاملی (مانند نظرسنجی یا لینک) مرتبط با یک استوری مشخص (storyId) را دریافت می‌کند؛ برای رندر کردن عناصر تعاملی روی استوری استفاده می‌شود. |
| `GetUserPrivacyConfig` | — | `result: repeated PrivacyConfig` | تنظیمات حریم خصوصی استوری کاربر جاری را از سرور دریافت می‌کند؛ هنگام ورود به بخش تنظیمات استوری یا نمایش وضعیت فعلی حریم خصوصی فراخوانی می‌شود. |
| `GetUserStoryConfig` | `key: repeated int64`، `exPeer: ExPeer` | `config: repeated Config` | تنظیمات پیکربندی استوری کاربر یا یک peer مشخص (exPeer) را با کلیدهای درخواستی (key) دریافت می‌کند؛ برای خواندن تنظیمات خاص مانند حالت سکوت یا مخفی‌سازی استفاده می‌شود. |
| `GetViewers` | `storyId: bytes`، `pagination: T_eC` | `viewers: repeated Viewer`، `viewCount: int64`، `likeCount: int64`، `linkClickCount: int64`، `emojiCount: int64`، `restoryCount: int64` | فهرست کاربرانی که استوری مشخص (storyId) را مشاهده کرده‌اند با پشتیبانی از صفحه‌بندی (pagination) برمی‌گرداند؛ برای نمایش لیست بازدیدکنندگان به صاحب استوری استفاده می‌شود. |
| `GetViewersCount` | `storyId: bytes` | `viewCount: int64`، `likeCount: int64`، `linkClickCount: int64`، `emojiCount: int64`، `restoryCount: int64` | تعداد کل بازدیدکنندگان یک استوری مشخص (storyId) را به‌صورت خلاصه برمی‌گرداند؛ برای نمایش سریع شمار بازدید بدون بارگذاری کامل لیست فراخوانی می‌شود. |
| `ReactToStory` | `storyId: bytes`، `reaction: bytes`، `type: int64`، `reactionType: int64`، `reactionText: StringValue` | ✔️ فقط تأیید | وقتی کاربر به یک استوری (storyId) واکنش نشان می‌دهد این RPC فراخوانی می‌شود؛ نوع واکنش (reaction، reactionType، type) و متن اختیاری (reactionText) به سرور ارسال می‌شوند. |
| `RemoveStory` | `storyId: bytes` | ✔️ فقط تأیید | برای حذف یک استوری با شناسه storyId استفاده می‌شود؛ کاربر یا ادمین کانال پس از انتشار استوری، با فراخوانی این RPC آن را از سرور پاک می‌کند. |
| `SetUserPrivacyConfig` | `config: PrivacyConfig` | ✔️ فقط تأیید | تنظیمات حریم خصوصی استوری کاربر را به‌روزرسانی می‌کند؛ کاربر از طریق ارسال config جدید مشخص می‌کند چه کسانی می‌توانند استوری‌هایش را ببینند. |
| `SetUserStoryConfig` | `setType: int64`، `config: Config`، `exPeer: ExPeer` | ✔️ فقط تأیید | پیکربندی استوری برای یک کاربر یا peer مشخص (exPeer) را ذخیره می‌کند؛ با ارسال setType و config می‌توان رفتارهایی مانند سکوت کردن یا مخفی کردن استوری را تنظیم کرد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-timche-v1-timche"></a>

## بازار ربات‌ها (Timche) — `bale.timche.v1.Timche`

این سرویس مربوط به بازار ربات‌های بله (Timche) است و امکان مشاهده صفحه اصلی، صفحه بخش‌ها، صفحه هر ربات و ثبت نظر و امتیاز کاربران را فراهم می‌کند. کلاینت از این سرویس برای نمایش فهرست ربات‌های موجود و تعامل کاربر با آن‌ها استفاده می‌کند.

نام‌فضای پایتون: `client.timche` — تعداد متد: 5

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AskBotReviewCallback` | `botId: int32`، `payload: string` | ✔️ فقط تأیید | کلاینت این متد را پس از دریافت یک callback از ربات (با شناسه botId و داده payload) فراخوانی می‌کند تا سرور را از پاسخ کاربر به درخواست نظردهی مطلع سازد. احتمالاً زمانی استفاده می‌شود که ربات از کاربر می‌خواهد نظر خود را ثبت کند و کاربر اقدام به این کار کند. |
| `GetBotPage` | `botId: int32` | `name: string`، `nickname: string`، `activeUsers: int32`، `averageRating: FloatValue`، `description: string`، `intro: string`، `avatar: Avatar`، `imageLinks: repeated string` | کلاینت با ارسال botId این متد را فراخوانی می‌کند تا اطلاعات کامل صفحه یک ربات خاص (توضیحات، امتیاز، نظرات و غیره) را از بازار ربات‌های بله دریافت کند. |
| `GetHomePage` | — | `sections: repeated T_u_72802` | کلاینت هنگام باز کردن بازار ربات‌ها (Timche) این متد را بدون هیچ پارامتری فراخوانی می‌کند تا محتوای صفحه اصلی شامل ربات‌های پیشنهادی، دسته‌بندی‌ها و بخش‌های ویژه را دریافت نماید. |
| `GetSectionPage` | `sectionId: int32` | `sectionId: int32`، `sectionName: string`، `bots: repeated T_c_72802` | کلاینت با ارسال sectionId این متد را فراخوانی می‌کند تا فهرست ربات‌های مربوط به یک بخش یا دسته‌بندی خاص در بازار بله را دریافت کند. |
| `SubmitReview` | `botId: int32`، `rating: Int32Value`، `comment: StringValue`، `payload: StringValue`، `origin: int32`، `language: StringValue` | `shouldAskBaleReview: bool`، `baleReviewText: string` | کلاینت هنگامی که کاربر می‌خواهد برای یک ربات نظر و امتیاز ثبت کند این متد را با botId، rating، comment و اطلاعات تکمیلی مانند origin و language فراخوانی می‌کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-tldr-v1-tldr"></a>

## پیش‌نمایش و خلاصه لینک — `bale.tldr.v1.TLDR`

این سرویس امکان دریافت اطلاعات پیش‌نمایش و خلاصه‌ی محتوای لینک‌های اینترنتی را فراهم می‌کند. کلاینت از این سرویس برای نمایش کارت پیش‌نمایش لینک در چت استفاده می‌کند.

نام‌فضای پایتون: `client.tldr` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetLinkPreview` | `url: bytes` | `title: bytes`، `description: bytes`، `images: repeated Image` | هنگامی که کاربر یک URL در پیام وارد می‌کند، کلاینت این RPC را با ارسال url فراخوانی می‌کند تا اطلاعات پیش‌نمایش لینک (مانند عنوان، تصویر و توضیحات) را دریافت کرده و به‌صورت کارت در رابط کاربری نمایش دهد. |
| `GetLinkSummary` | `url: bytes` | `summary: bytes` | احتمالاً برای دریافت خلاصه‌ی متنی یا ساختارمندتر محتوای یک URL به‌کار می‌رود؛ کلاینت url را ارسال می‌کند و پاسخ حاوی اطلاعات فشرده‌تری نسبت به GetLinkPreview درباره‌ی محتوای صفحه است. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-top_peer-v1-toppeer"></a>

## مخاطبان برتر — `bale.top_peer.v1.TopPeer`

این سرویس فهرست مخاطبان و peer‌هایی را مدیریت می‌کند که کاربر بیشترین تعامل را با آن‌ها داشته است. با استفاده از این سرویس می‌توان لیست top peer‌ها را دریافت کرد یا یک peer را از آن فهرست حذف نمود.

نام‌فضای پایتون: `client.top_peer` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetTopPeer` | — | `topPeers: repeated TopPeerType` | این متد برای دریافت فهرست مخاطبان یا چت‌های برتر کاربر فراخوانی می‌شود؛ معمولاً هنگام نمایش پیشنهادهای سریع در شروع مکالمه یا جستجو استفاده می‌شود. چون ورودی خاصی ندارد، لیست top peer‌ها بر اساس تاریخچه تعامل کاربر به‌صورت خودکار بازگردانده می‌شود. |
| `RemovePeer` | `peer: Peer` | `isRemoved: int64` | زمانی فراخوانی می‌شود که کاربر بخواهد یک peer مشخص را از فهرست مخاطبان برتر خود حذف کند. با ارسال شناسه peer مورد نظر، آن مخاطب دیگر در پیشنهادهای سریع نمایش داده نخواهد شد. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-turing-v1-ai"></a>

## هوش مصنوعی — `bale.turing.v1.AI`

این سرویس قابلیت‌های هوش مصنوعی بله را فراهم می‌کند و امکاناتی مانند تبدیل گفتار به متن (رونویسی پیام‌های صوتی) و دریافت رویدادهای تعاملی کاربر را در اختیار کلاینت قرار می‌دهد.

نام‌فضای پایتون: `client.ai` — تعداد متد: 2

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `GetTranscript` | `voice: Media`، `outPeer: OutPeer`، `messageId: MessageId` | `mustWait: bool`، `downloadSource: DownloadSource` | کلاینت این RPC را برای دریافت متن رونویسی‌شده یک پیام صوتی فراخوانی می‌کند؛ با ارسال voice (فایل رسانه‌ای)، outPeer (مکالمه مقصد) و messageId، سرور متن معادل آن پیام صوتی را بازمی‌گرداند. |
| `SendEvent` | `transcriptReactionEvent: TranscriptReactionEvent` | ✔️ فقط تأیید | کلاینت این RPC را برای ارسال رویداد واکنش کاربر به یک رونویسی (transcriptReactionEvent) به سرور فراخوانی می‌کند؛ احتمالاً برای ثبت بازخورد کاربر (مثلاً پسندیدن یا رد کردن نتیجه رونویسی) استفاده می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-users-v1-users"></a>

## مدیریت کاربران — `bale.users.v1.Users`

این سرویس مسئول مدیریت پروفایل کاربران، مخاطبین، تنظیمات حریم خصوصی و کارت‌های بانکی مرتبط با حساب کاربری در پیام‌رسان بله است. کلاینت از این سرویس برای ویرایش اطلاعات شخصی، افزودن یا مسدودکردن مخاطبین و دریافت جزئیات کامل پروفایل کاربران استفاده می‌کند.

نام‌فضای پایتون: `client.users` — تعداد متد: 36

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AddCard` | `bankCode: string` | ✔️ فقط تأیید | هنگامی که کاربر می‌خواهد یک کارت بانکی جدید به حساب خود اضافه کند فراخوانی می‌شود؛ کلاینت کد بانک (bankCode) را ارسال می‌کند تا کارت مربوطه به کیف پول بله متصل شود. |
| `AddContact` | `uid: int32`، `accessHash: int64` | `seq: int32`، `state: bytes` | برای افزودن یک کاربر به لیست مخاطبین استفاده می‌شود؛ کلاینت شناسه کاربر (uid) و accessHash مربوطه را ارسال می‌کند تا آن کاربر به عنوان مخاطب ذخیره شود. |
| `BlockUser` | `peer: UserPeer` | `seq: int32`، `state: bytes` | هنگامی که کاربر می‌خواهد یک کاربر دیگر را مسدود کند فراخوانی می‌شود؛ کلاینت peer از نوع UserPeer را ارسال می‌کند و پس از آن کاربر مسدودشده دیگر قادر به ارسال پیام نخواهد بود. |
| `ChangeDefaultCardNumber` | `defaultCardNumber: StringValue` | `seq: int32`، `state: bytes` | برای تغییر کارت بانکی پیش‌فرض کاربر در سیستم پرداخت بله به کار می‌رود؛ کلاینت شماره کارت جدید را از طریق defaultCardNumber ارسال می‌کند. |
| `ChangePhoneNumber` | `phoneNumber: int64` | ✔️ فقط تأیید | زمانی فراخوانی می‌شود که کاربر می‌خواهد شماره تلفن حساب خود را تغییر دهد؛ کلاینت شماره تلفن جدید (phoneNumber) را ارسال کرده و احتمالاً مرحله تأیید بعدی از طریق ConfirmPhoneNumber انجام می‌شود. |
| `CheckNickName` | `nickname: string` | `value: bool` | پیش از ثبت یا تغییر نام کاربری، کلاینت این متد را فراخوانی می‌کند تا بررسی کند آیا nickname مورد نظر در دسترس و مجاز است یا خیر؛ پاسخ از نوع BoolValue است. |
| `ConfirmPhoneNumber` | `code: string` | ✔️ فقط تأیید | پس از درخواست تغییر شماره تلفن، کاربر کد تأیید دریافت‌شده را از طریق این متد ارسال می‌کند (code) تا تغییر شماره تلفن نهایی شود. |
| `EditAbout` | `about: StringValue` | `seq: int32`، `state: bytes` | برای ویرایش بخش «درباره من» یا بیوگرافی پروفایل کاربر استفاده می‌شود؛ کلاینت متن جدید را در قالب about از نوع StringValue ارسال می‌کند. |
| `EditAvatar` | `fileLocation: FileLocation` | `avatar: Avatar`، `seq: int32`، `state: bytes` | هنگام تغییر تصویر پروفایل کاربر فراخوانی می‌شود؛ کلاینت مکان فایل آپلودشده (fileLocation) را ارسال می‌کند تا تصویر جدید به عنوان آواتار تنظیم شود. |
| `EditBirthDate` | `date: int64` | ✔️ فقط تأیید | برای ویرایش تاریخ تولد کاربر در پروفایل استفاده می‌شود؛ کلاینت تاریخ را به صورت timestamp (date از نوع int64) ارسال می‌کند. |
| `EditMyPreferredLanguages` | `preferredLanguages: repeated string` | `seq: int32`، `state: bytes` | زمانی که کاربر می‌خواهد زبان‌های ترجیحی خود را در تنظیمات حساب به‌روزرسانی کند فراخوانی می‌شود؛ کلاینت لیستی از کدهای زبان (preferredLanguages) را ارسال می‌کند. |
| `EditMyTimeZone` | `tz: string` | `seq: int32`، `state: bytes` | برای تنظیم منطقه زمانی حساب کاربری به کار می‌رود؛ کلاینت رشته منطقه زمانی (tz) را ارسال می‌کند تا نمایش زمان پیام‌ها و رویدادها متناسب با موقعیت کاربر باشد. |
| `EditName` | `name: string` | `seq: int32`، `state: bytes` | برای تغییر نام نمایشی کاربر در پروفایل استفاده می‌شود؛ کلاینت نام جدید (name) را ارسال می‌کند تا در پروفایل و لیست مخاطبین دیگران به‌روز شود. |
| `EditNickName` | `nickname: StringValue` | `seq: int32`، `state: bytes` | برای تغییر نام کاربری (username) حساب فراخوانی می‌شود؛ کلاینت نام کاربری جدید را از طریق nickname از نوع StringValue ارسال می‌کند و معمولاً پس از تأیید CheckNickName انجام می‌شود. |
| `EditSex` | `sex: int32` | ✔️ فقط تأیید | برای ویرایش جنسیت کاربر در پروفایل استفاده می‌شود؛ کلاینت مقدار عددی جنسیت (sex از نوع int32) را ارسال می‌کند. |
| `EditUserLocalName` | `uid: int32`، `accessHash: int64`، `name: string` | `seq: int32`، `state: bytes` | هنگامی که کاربر می‌خواهد نام محلی (دستی) یک مخاطب خاص را در دفتر مخاطبین خود تغییر دهد فراخوانی می‌شود؛ کلاینت uid، accessHash و نام جدید (name) را ارسال می‌کند. |
| `GetContacts` | `contactsHash: string`، `optimizations: repeated int32` | `users: repeated User`، `isNotChanged: bool`، `userPeers: repeated UserPeer` | برای دریافت لیست مخاطبین کاربر استفاده می‌شود؛ کلاینت contactsHash فعلی را ارسال می‌کند تا در صورت تغییر، لیست به‌روزشده دریافت شود و از دانلود مجدد داده‌های تغییرنیافته جلوگیری گردد. |
| `GetFullUser` | `peer: UserPeer` | `fullUser: T_n4` | برای دریافت اطلاعات کامل پروفایل یک کاربر (شامل بیو، آواتار، تنظیمات و غیره) فراخوانی می‌شود؛ کلاینت peer از نوع UserPeer را ارسال می‌کند تا جزئیات کامل آن کاربر را بگیرد. |
| `GetUserFullPrivacy` | `userId: int32` | `privacy: Privacy` | برای دریافت تمام تنظیمات حریم خصوصی یک کاربر مشخص استفاده می‌شود؛ کلاینت userId را ارسال می‌کند تا بفهمد آن کاربر چه سطحی از دسترسی به اطلاعات خود اعمال کرده است. |
| `GetUserPrivacyStatus` | `userId: int32`، `type: int32` | `status: int32` | برای بررسی وضعیت یک نوع خاص از حریم خصوصی کاربر (مثلاً آخرین بازدید یا عکس پروفایل) فراخوانی می‌شود؛ کلاینت userId و type (نوع تنظیم حریم خصوصی) را ارسال می‌کند. |
| `GetUsersDefaultCardNumber` | — | `defaultCardNo: repeated DefaultCardNo` | برای دریافت شماره کارت بانکی پیش‌فرض کاربر جاری فراخوانی می‌شود؛ این متد نیازی به ورودی ندارد و اطلاعات کارت پیش‌فرض ثبت‌شده در حساب را برمی‌گرداند. |
| `ImportContacts` | `phones: repeated Phone`، `optimizations: repeated int32` | `users: repeated User`، `seq: int32`، `state: bytes`، `userPeers: repeated UserPeer` | هنگام همگام‌سازی مخاطبین گوشی با سرور بله استفاده می‌شود؛ کلاینت لیستی از شماره تلفن‌ها (phones) را ارسال می‌کند تا مشخص شود کدام‌یک در بله حساب دارند و به مخاطبین اضافه شوند. |
| `IsNameAllowed` | `name: string` | `value: bool` | پیش از ثبت نام نمایشی، کلاینت این متد را فراخوانی می‌کند تا بررسی کند آیا name از نظر قوانین محتوایی بله مجاز است یا خیر؛ پاسخ از نوع BoolValue است. |
| `LoadAvatars` | `peer: UserPeer` | `avatars: Avatars` | برای دریافت لیست تصاویر پروفایل (تاریخچه آواتارها) یک کاربر فراخوانی می‌شود؛ کلاینت peer از نوع UserPeer را ارسال می‌کند تا تمام آواتارهای آن کاربر بارگذاری شوند. |
| `LoadBlockedUsers` | — | `userPeers: repeated UserPeer` | برای دریافت لیست کاربران مسدودشده توسط کاربر جاری استفاده می‌شود؛ این متد نیازی به ورودی ندارد و فهرست کامل کاربران بلاک‌شده را برمی‌گرداند. |
| `LoadFullUsers` | `userPeers: repeated UserPeer` | `fullUsers: repeated FullUser` | کلاینت برای دریافت اطلاعات کامل (پروفایل کامل) یک یا چند کاربر، لیستی از userPeers را ارسال می‌کند؛ معمولاً هنگام باز کردن پروفایل یا نمایش جزئیات کاربر فراخوانی می‌شود. |
| `LoadFullUsersSequentially` | `userPeers: repeated UserPeer` | `fullUsers: repeated FullUser` | مشابه LoadFullUsers است اما اطلاعات کامل کاربران را به‌صورت ترتیبی (یکی پس از دیگری) بارگذاری می‌کند؛ احتمالاً برای جلوگیری از بار زیاد یا محدودیت نرخ در درخواست‌های دسته‌ای استفاده می‌شود. |
| `LoadUsers` | `peers: repeated UserPeer` | `users: repeated User` | با ارسال لیستی از peers از نوع UserPeer، اطلاعات پایه چندین کاربر را به‌صورت همزمان دریافت می‌کند؛ معمولاً هنگام نمایش لیست مکالمات یا نتایج جستجو به کار می‌رود. |
| `NotifyAboutDeviceInfo` | `preferredLanguages: repeated string`، `timeZone: StringValue` | ✔️ فقط تأیید | کلاینت هنگام ورود یا تغییر تنظیمات دستگاه، اطلاعاتی مانند زبان‌های ترجیحی (preferredLanguages) و منطقه زمانی (timeZone) را به سرور اطلاع می‌دهد تا تجربه کاربری شخصی‌سازی شود. |
| `RemoveAvatar` | `avaterId: Int64Value_1` | `seq: int32`، `state: bytes` | کاربر با ارسال avaterId مشخص، یکی از تصاویر پروفایل خود را حذف می‌کند؛ این RPC هنگام مدیریت آواتارها در تنظیمات پروفایل فراخوانی می‌شود. |
| `RemoveContact` | `uid: int32`، `accessHash: int64` | `seq: int32`، `state: bytes` | کلاینت با ارسال uid و accessHash کاربر مورد نظر، آن را از لیست مخاطبین حذف می‌کند؛ هنگامی که کاربر گزینه «حذف مخاطب» را انتخاب می‌کند فراخوانی می‌شود. |
| `RemoveDefaultCardNumber` | — | `seq: int32`، `state: bytes` | شماره کارت بانکی پیش‌فرض کاربر را از حساب بله حذف می‌کند؛ احتمالاً در بخش کیف پول یا تنظیمات پرداخت استفاده می‌شود. |
| `ResetContacts` | — | ✔️ فقط تأیید | تمام مخاطبین همگام‌شده با سرور را پاک می‌کند و لیست مخاطبین را به حالت اولیه بازمی‌گرداند؛ معمولاً هنگام خروج از حساب یا همگام‌سازی مجدد دفترچه تلفن استفاده می‌شود. |
| `SearchContacts` | `request: string`، `optimizations: repeated int32` | `users: repeated User`، `userPeers: repeated UserPeer`، `groups: repeated Group`، `groupPeers: repeated GroupPeer` | با ارسال عبارت جستجو (request) و پارامترهای بهینه‌سازی (optimizations)، کاربران موجود در مخاطبین را جستجو می‌کند؛ هنگام تایپ در کادر جستجوی مخاطبین فراخوانی می‌شود. |
| `SetUserPrivacyStatus` | `userId: int32`، `type: int32`، `status: int32` | ✔️ فقط تأیید | تنظیمات حریم خصوصی یک کاربر خاص را با استفاده از userId، نوع تنظیم (type) و وضعیت (status) به‌روزرسانی می‌کند؛ برای مثال تعیین اینکه چه کسانی می‌توانند آخرین بازدید یا شماره تلفن را ببینند. |
| `UnblockUser` | `peer: UserPeer` | `seq: int32`، `state: bytes` | کاربر مسدودشده‌ای را با ارسال peer از نوع UserPeer از لیست بلاک خارج می‌کند؛ هنگامی که کاربر گزینه «رفع مسدودیت» را در پروفایل یا تنظیمات انتخاب می‌کند فراخوانی می‌شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-v1-configs"></a>

## تنظیمات و پیکربندی — `bale.v1.Configs`

این سرویس برای مدیریت پارامترهای پیکربندی سمت سرور و دریافت اطلاعات به‌روزرسانی درون‌برنامه‌ای استفاده می‌شود. کلاینت از طریق این سرویس می‌تواند تنظیمات پویای اپلیکیشن را بخواند یا تغییر دهد.

نام‌فضای پایتون: `client.configs` — تعداد متد: 3

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `EditParameter` | `key: string`، `value: StringValue` | `seq: int32`، `state: bytes` | زمانی فراخوانی می‌شود که کلاینت یا ادمین بخواهد مقدار یک پارامتر پیکربندی را تغییر دهد؛ با ارسال key (نام پارامتر) و value (مقدار جدید از نوع StringValue)، سرور تنظیم مربوطه را به‌روز می‌کند. |
| `GetInAppUpdate` | — | `fileId: int64`، `accessHash: int64`، `fileSize: int32` | کلاینت هنگام راه‌اندازی یا در فواصل زمانی مشخص این RPC را فراخوانی می‌کند تا بررسی کند آیا نسخه جدیدی از اپلیکیشن موجود است و آیا به‌روزرسانی اجباری یا اختیاری لازم است. |
| `GetParameters` | — | `parameters: repeated Parameter` | کلاینت در ابتدای اجرا یا پس از هر بار اتصال، این متد را صدا می‌زند تا مجموعه پارامترهای پیکربندی سمت سرور (مثل feature flagها یا حدودهای عملکردی) را دریافت کند. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-v1-images"></a>

## استیکر و GIF — `bale.v1.Images`

این سرویس مدیریت تصاویر متحرک (GIF) و استیکرهای کاربر را بر عهده دارد. کلاینت از این RPC‌ها برای افزودن، حذف و بارگذاری مجموعه‌های استیکر و GIF‌های ذخیره‌شده استفاده می‌کند.

نام‌فضای پایتون: `client.images` — تعداد متد: 10

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `AddGif` | `gif: FileLocation`، `thumb: bytes`، `mimeType: Offset` | `seq: int32`، `state: bytes` | هنگامی که کاربر یک GIF را در لیست GIF‌های ذخیره‌شده‌اش نگه‌داری می‌کند، کلاینت این RPC را با ارسال gif (FileLocation)، thumb (تصویر بندانگشتی) و mimeType فراخوانی می‌کند تا آن GIF به مجموعه شخصی کاربر اضافه شود. |
| `AddStickerCollection` | `id: int32`، `accessHash: int64` | `collections: repeated Collection`، `seq: int32`، `state: bytes` | برای اضافه کردن یک مجموعه استیکر به لیست مجموعه‌های کاربر استفاده می‌شود؛ کلاینت با ارسال id و accessHash مجموعه، درخواست افزودن آن را ارسال می‌کند. |
| `AddStickerPack` | `id: int32` | `seq: int32`، `state: bytes` | زمانی که کاربر یک پک استیکر را نصب یا به مجموعه‌های خود اضافه می‌کند، کلاینت این RPC را با id پک مربوطه صدا می‌زند. |
| `GetSavedGifs` | `offset: Offset` | `gifs: repeated Gifs`، `offset: Offset` | برای دریافت فهرست GIF‌های ذخیره‌شده کاربر استفاده می‌شود؛ کلاینت با ارسال offset می‌تواند نتایج را به صورت صفحه‌بندی‌شده دریافت کند. |
| `LoadOwnStickers` | `offset: Offset` | `ownStickers: repeated Collection`، `offset: Offset` | هنگام باز کردن پنل استیکر، کلاینت این RPC را با offset فراخوانی می‌کند تا استیکرهای متعلق به خود کاربر را به صورت صفحه‌بندی‌شده بارگذاری کند. |
| `LoadStickerCollection` | `id: int32`، `accessHash: int64` | `collection: Collection` | برای بارگذاری جزئیات و محتوای یک مجموعه استیکر مشخص با استفاده از id و accessHash آن مجموعه به کار می‌رود، احتمالاً هنگام مشاهده یا پیش‌نمایش یک پک استیکر. |
| `RemoveGif` | `gif: FileLocation` | `seq: int32`، `state: bytes` | زمانی که کاربر یک GIF را از لیست ذخیره‌شده‌هایش حذف می‌کند، کلاینت این RPC را با gif (FileLocation) همان GIF فراخوانی می‌کند. |
| `RemoveStickerCollection` | `id: int32`، `accessHash: int64` | `collections: repeated Collection`، `seq: int32`، `state: bytes` | برای حذف یک مجموعه استیکر از لیست مجموعه‌های کاربر استفاده می‌شود؛ کلاینت id و accessHash مجموعه را ارسال می‌کند تا آن مجموعه برداشته شود. |
| `RemoveStickerPack` | `id: int32` | `seq: int32`، `state: bytes` | هنگامی که کاربر یک پک استیکر را حذف یا آن را از مجموعه‌هایش برمی‌دارد، کلاینت این RPC را با id پک صدا می‌زند. |
| `UseGif` | `gif: FileLocation`، `usedAt: int64` | ✔️ فقط تأیید | هر بار که کاربر یک GIF را در چت ارسال می‌کند، کلاینت این RPC را با gif (FileLocation) و usedAt (زمان استفاده) فراخوانی می‌کند تا تاریخچه استفاده و رتبه‌بندی GIF‌ها به‌روز شود. |

[↑ بازگشت به فهرست](#toc)

<a id="svc-bale-wallet-v1-wallet"></a>

## کیف پول — `bale.wallet.v1.Wallet`

این سرویس امکانات مالی کیف پول بله را فراهم می‌کند و شامل فعال‌سازی کیف پول، انتقال وجه، برداشت، پرداخت درخواست پول و مشاهده تراکنش‌ها می‌شود. کلاینت از این RPCها برای مدیریت کامل کیف پول کاربر در اکوسیستم بله استفاده می‌کند.

نام‌فضای پایتون: `client.wallet` — تعداد متد: 13

| متد | ورودی‌ها | خروجی | کاربرد (استنباطی) |
|---|---|---|---|
| `ActivateWallet` | `nationalId: string`، `isAutoActivated: BoolValue_1` | ✔️ فقط تأیید | هنگامی که کاربر برای اولین بار می‌خواهد کیف پول خود را فعال کند، این RPC با ارسال nationalId و وضعیت فعال‌سازی خودکار (isAutoActivated) فراخوانی می‌شود. احتمالاً در فرآیند احراز هویت مالی و ثبت‌نام کیف پول به کار می‌رود. |
| `CashOutFromWallet` | `token: string`، `amount: int64` | ✔️ فقط تأیید | برای برداشت وجه از کیف پول و انتقال آن به حساب بانکی، کلاینت این RPC را با token احراز هویت و مقدار amount فراخوانی می‌کند. این عملیات پس از تأیید هویت از طریق VerifyCashOut انجام می‌شود. |
| `GetMoneyRequestPaymentTokenByCard` | `msg: Msg`، `amount: Int64Value_1`، `regarding: StringValue` | `token: string`، `endpoint: string`، `terminalId: string`، `merchantId: string` | زمانی که کاربر می‌خواهد یک درخواست پول (msg) را از طریق کارت بانکی پرداخت کند، این RPC برای دریافت توکن پرداخت فراخوانی می‌شود. فیلدهای msg، amount و regarding مشخص می‌کنند کدام درخواست پول با چه مبلغ و توضیحی پرداخت می‌شود. |
| `GetMyWallets` | — | `wallets: repeated WalletType` | برای دریافت لیست تمام کیف پول‌های متعلق به کاربر جاری، این RPC بدون هیچ ورودی فراخوانی می‌شود. کلاینت معمولاً در ابتدای ورود به بخش مالی یا هنگام انتخاب کیف پول مبدأ/مقصد از این RPC استفاده می‌کند. |
| `GetPaymentTokenByCard` | `targetWallet: string`، `amount: int64`، `regarding: StringValue` | `token: string`، `endpoint: string`، `terminalId: string`، `merchantId: string` | برای پرداخت از طریق کارت بانکی به یک کیف پول مقصد (targetWallet) با مبلغ مشخص (amount)، کلاینت این RPC را فراخوانی می‌کند تا توکن پرداخت لازم برای اتصال به درگاه بانکی را دریافت کند. فیلد regarding توضیح اختیاری تراکنش را در بر می‌گیرد. |
| `GetWalletChargeToken` | `walletId: string`، `amount: int64` | `token: string`، `endpoint: string`، `terminalId: string`، `merchantId: string` | هنگامی که کاربر می‌خواهد کیف پول خود (walletId) را از طریق درگاه بانکی شارژ کند، این RPC با مقدار amount فراخوانی می‌شود تا توکن لازم برای شروع فرآیند شارژ دریافت شود. |
| `GetWalletContracts` | — | `startDate: int64`، `endDate: int64`، `merchantCustomerUniqueValue: string`، `limitations: repeated Limitation`، `agreementId: string`، `status: int32` | برای دریافت قراردادها و توافقنامه‌های مرتبط با کیف پول (مثلاً شرایط استفاده از سرویس مالی)، این RPC بدون ورودی فراخوانی می‌شود. احتمالاً در مرحله فعال‌سازی یا تنظیمات کیف پول به کاربر نمایش داده می‌شود. |
| `GetWalletInvoice` | `walletId: string`، `pageNumber: Int32Value` | `invoices: repeated Invoice` | برای مشاهده تاریخچه و صورت‌حساب تراکنش‌های یک کیف پول مشخص (walletId)، کلاینت این RPC را با شماره صفحه (pageNumber) فراخوانی می‌کند. این RPC خروجی صفحه‌بندی‌شده از تراکنش‌های کیف پول ارائه می‌دهد. |
| `PayByWallet` | `sourceWallet: string`، `targetWallet: string`، `amount: int64`، `currency: int32`، `regarding: StringValue` | ✔️ فقط تأیید | برای انتقال مستقیم وجه از کیف پول مبدأ (sourceWallet) به کیف پول مقصد (targetWallet) با مقدار، ارز و توضیح مشخص، این RPC فراخوانی می‌شود. این اصلی‌ترین RPC برای پرداخت درون‌پلتفرمی بین کاربران بله است. |
| `PayMoneyRequestByWallet` | `sourceWalletId: string`، `msg: Msg`، `amount: Int64Value_1`، `regarding: StringValue` | ✔️ فقط تأیید | زمانی که کاربر یک درخواست پول دریافتی (msg) را از طریق کیف پول خود (sourceWalletId) می‌پردازد، این RPC با مقدار amount و توضیح regarding فراخوانی می‌شود. این RPC برای پاسخ به درخواست‌های پول ارسال‌شده توسط سایر کاربران در چت استفاده می‌شود. |
| `VerifyCashOut` | `walletId: string`، `accountNo: string`، `nationalId: string` | `token: string`، `name: string` | پیش از انجام برداشت وجه، کلاینت این RPC را با walletId، شماره حساب بانکی (accountNo) و کد ملی (nationalId) فراخوانی می‌کند تا صحت اطلاعات حساب مقصد را تأیید کند. این مرحله پیش‌نیاز امنیتی قبل از فراخوانی CashOutFromWallet است. |
| `VerifyPeer` | `targetPeer: Bot` | `targetWalletName: string`، `targetUserId: Int32Value`، `walletId: string` | برای تأیید هویت یک peer (مثلاً بات یا کاربر مقصد) پیش از انجام تراکنش مالی، این RPC با targetPeer فراخوانی می‌شود. احتمالاً جهت اطمینان از معتبر بودن طرف مقابل در فرآیندهای پرداخت به کار می‌رود. |
| `VerifyQRCode` | `targetWalletId: string` | `targetWalletName: string`، `targetUserId: Int32Value` | هنگامی که کاربر یک کد QR را اسکن می‌کند تا به کیف پول مقصد (targetWalletId) پرداخت کند، این RPC برای اعتبارسنجی و دریافت اطلاعات کیف پول مرتبط با آن کد QR فراخوانی می‌شود. |

[↑ بازگشت به فهرست](#toc)
