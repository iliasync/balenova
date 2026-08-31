"""پاسخ خودکار به پیام‌های خصوصی."""

from balenova import Client, events, filters

app = Client("my_account")


@app.on(events.NewMessage, filters.incoming & filters.private & filters.text)
async def echo(event):
    await event.reply(f"گفتی: {event.text}")


app.run_forever()
