"""نمایش تماس‌های اخیر."""

from balenova import Client

app = Client("my_account")


async def main(client):
    calls = await client.get_call_logs()
    print(calls)


app.run_task(main)
