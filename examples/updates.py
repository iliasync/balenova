"""نمایش رویدادها."""

from balenova import Client

app = Client("my_account")


@app.on_update
async def update_received(update):
    print(update.name)
    print(update.to_json())


app.run_forever()
