"""نمایش گفت‌وگوهای حساب."""

from balenova import Client

app = Client("my_account")


async def main(client):
    dialogs = await client.get_all_dialogs_by_type()
    for kind, chats in dialogs.items():
        print(f"{kind}: {len(chats)}")
        for chat in chats[:5]:
            print(" -", chat.full_name, chat.id)


app.run_task(main)
