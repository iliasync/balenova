"""نمایش اطلاعات و اعضای یک گروه."""

from balenova import Client

app = Client("my_account")
GROUP_ID = "12345|2"  # شناسهٔ گروه خودتان


async def main(client):
    group = await client.get_entity(GROUP_ID)
    members = await client.load_members(GROUP_ID, limit=20)
    print(group.to_json() if group else "گروه پیدا نشد")
    print(members["members"])


app.run_task(main)
