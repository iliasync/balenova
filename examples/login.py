"""ورود و نمایش اطلاعات حساب."""

from balenova import Client

app = Client("my_account")


async def main(client):
    me = await client.get_me()
    print(me.full_name)
    print(me.id)


app.run_task(main)
