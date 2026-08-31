"""تبدیل نتیجه به JSON."""

from balenova import Client

app = Client("my_account")


async def main(client):
    me = await client.get_me()
    print(me.to_json())


app.run_task(main)
