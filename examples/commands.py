"""ساخت دستور /start."""

from balenova import Client, events, filters

app = Client("my_account")


@app.on(events.NewMessage, filters.command("start"))
async def start(event):
    await event.reply("سلام! آماده‌ام 🌱")


app.run_forever()
