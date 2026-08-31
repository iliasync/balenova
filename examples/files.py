"""نمایش ظرفیت آپلود حساب."""

from balenova import Client

app = Client("my_account")


async def main(client):
    limits = await client.get_upload_limits()
    print(limits)


app.run_task(main)
