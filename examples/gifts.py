"""نمایش کیف پول حساب."""

from balenova import Client

app = Client("my_account")


async def main(client):
    wallet = await client.get_wallet()
    print(wallet.to_json())


app.run_task(main)
