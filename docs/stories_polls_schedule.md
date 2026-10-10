# راهنمای استوری‌ها، نظرسنجی‌ها و پیام‌های زمان‌بندی‌شده

در **BaleNova** متدهای ویژه‌ای برای کار با استوری‌های کاربران و کانال‌ها، نظرسنجی‌های گروهی و ارسال پیام‌های زمان‌بندی‌شده وجود دارد.

---

## ۱. استوری‌ها (Stories)

### دریافت استوری‌ها و ایموجی‌های مجاز واکنش
```python
from balenova import Client, model_to_dict

app = Client.from_firefox()

async def main():
    async with app:
        # دریافت تمام استوری‌های جاری
        all_stories = await app.get_all_stories()
        print(model_to_dict(all_stories))

        # دریافت لیست ایموجی‌های مجاز برای ری‌اکشن به استوری
        emojis = await app.get_story_reaction_emojis()
        print("ایموجی‌های مجاز:", emojis)
```

### واکنش و مشاهده آمار بازدید استوری
```python
story_id = "uuid_of_the_story"

# ارسال واکنش به استوری
await app.react_to_story(story_id, reaction="🔥")

# دریافت بینندگان و آمار استوری
viewers = await app.get_story_viewers(story_id, page=1, page_size=50)
print(model_to_dict(viewers))

# حذف استوری
await app.remove_story(story_id)
```

---

## ۲. نظرسنجی‌ها (Polls)

### دریافت نتایج نظرسنجی و رای دادن
```python
poll_id = 99887766

# دریافت نتیجه کامل نظرسنجی
result = await app.get_poll_result(poll_id)
print(model_to_dict(result))

# ثبت رای به گزینه‌های مورد نظر (مثلاً گزینه ۱)
await app.vote_poll(poll_id, option_ids=[1])

# پس گرفتن رای
await app.vote_poll(poll_id, option_ids=[1], is_retract=True)

# بستن نظرسنجی
await app.close_poll(poll_id)
```

---

## ۳. زمان‌بندی پیام‌ها (Scheduler)

امکان مشاهده و لغو کارهای زمان‌بندی‌شده در چت‌ها:

```python
# لیست پیام‌ها و کارهای زمان‌بندی‌شده در یک چت
tasks = await app.load_scheduled_tasks("123456789|1")
print(model_to_dict(tasks))

# لغو کارهای زمان‌بندی‌شده
await app.cancel_scheduled_tasks(task_ids=[12345, 67890])
```

---

## ۴. پیش‌نمایش و خلاصه‌سازی هوشمند لینک‌ها (TLDR / AI)

```python
# دریافت عنوان، توضیحات و تصاویر بندانگشتی لینک
preview = await app.get_link_preview("https://ble.ir")
print(f"عنوان: {preview.title}")

# دریافت خلاصهٔ مبتنی بر هوش مصنوعی لینک
summary = await app.get_link_summary("https://en.wikipedia.org/wiki/Python_(programming_language)")
print("خلاصه لینک:", summary.summary)
```
