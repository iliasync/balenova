"""ارسال یک پیام."""

from balenova import Client

app = Client("my_account")
CHAT_ID = "12345|1"  # شناسهٔ گفت‌وگوی خودتان


async def main(client):
    message = await client.send(CHAT_ID, "سلام از BaleNova")
    print(message.id)


app.run_task(main)
