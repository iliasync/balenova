# راهنمای استوری‌ها، نظرسنجی‌ها و پیام‌های زمان‌بندی‌شده

نمونه کدهای این صفحه به طور کامل بر اساس قواعد نام‌گذاری، فواصل خطوط و قراردادهای **PEP 8** سازمان‌دهی شده‌اند.

---

## ۱. استوری‌ها (Stories)

### مشاهده استوری‌ها و لیست ایموجی‌های مجاز واکنش
```python
import asyncio
from balenova import Client, model_to_dict

app = Client.from_browser("auto")


async def explore_stories() -> None:
    async with app:
        # دریافت کل استوری‌های فعال
        stories_response = await app.get_all_stories()
        print("استوری‌ها:", model_to_dict(stories_response))

        # لیست ایموجی‌های مجاز ری‌اکشن
        emojis = await app.get_story_reaction_emojis()
        print("ایموجی‌های مجاز:", emojis)


if __name__ == "__main__":
    asyncio.run(explore_stories())
```

### ارسال واکنش و دریافت آمار بینندگان
```python
async def story_interactions(story_id: str) -> None:
    async with app:
        # ۱. ارسال ری‌اکشن به استوری
        await app.react_to_story(
            story_id=story_id,
            reaction="🔥",
        )

        # ۲. مشاهده لیست بینندگان استوری
        viewers = await app.get_story_viewers(
            story_id=story_id,
            page=1,
            page_size=30,
        )
        print("بینندگان:", model_to_dict(viewers))

        # ۳. حذف استوری
        await app.remove_story(story_id=story_id)
```

---

## ۲. نظرسنجی‌ها (Polls)

```python
async def poll_operations(poll_id: int) -> None:
    async with app:
        # دریافت نتایج و جزئیات نظرسنجی
        poll_info = await app.get_poll_result(poll_id=poll_id)
        print("اطلاعات نظرسنجی:", model_to_dict(poll_info))

        # ثبت رای به گزینه اول
        await app.vote_poll(
            poll_id=poll_id,
            option_ids=[0],
        )

        # پس گرفتن رای ثبت شده
        await app.vote_poll(
            poll_id=poll_id,
            option_ids=[0],
            is_retract=True,
        )

        # بستن نظرسنجی توسط ادمین
        await app.close_poll(poll_id=poll_id)
```

---

## ۳. پیام‌های زمان‌بندی‌شده (Scheduled Messages)

```python
async def scheduler_operations(chat_id: str) -> None:
    async with app:
        # دریافت کارهای زمان‌بندی‌شده در چت
        tasks = await app.load_scheduled_tasks(chat_id=chat_id)
        print("تسک‌های زمان‌بندی‌شده:", model_to_dict(tasks))

        # لغو تسک‌های زمان‌بندی‌شده
        await app.cancel_scheduled_tasks(task_ids=[101, 102])
```

---

## ۴. پیش‌نمایش و خلاصه‌سازی هوشمند پیوندها (AI / TLDR)

```python
async def analyze_url(url: str) -> None:
    async with app:
        # دریافت پیش‌نمایش متادیتای وب‌سایت
        preview = await app.get_link_preview(url=url)
        print("عنوان سایت:", preview.title)

        # دریافت خلاصه‌سازی هوشمند محتوای صفحه با هوش مصنوعی
        summary_res = await app.get_link_summary(url=url)
        print("خلاصه AI:", summary_res.summary)
```
