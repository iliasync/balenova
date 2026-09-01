from __future__ import annotations

from balenova import Client, events, filters

from .player import VoicePlayer

app = Client("my_account")
player = VoicePlayer(app)

HELP = """فرمان‌ها را با ویرایش پیام خودتان اجرا کنید:
!vc join 12345|2
!vc play       ← هنگام ریپلای روی آهنگ یا ویس
!vc pause
!vc resume
!vc stop
!vc status
!vc leave"""


@app.on(events.NewMessage, filters.outgoing & filters.text)
async def command(event):
    text = event.text.strip()
    if not text.startswith("!vc"):
        return
    try:
        answer = await handle_command(event, text)
    except Exception as error:
        answer = f"خطا: {error}"
    await event.message.edit_text(answer)


async def handle_command(event: events.NewMessage, text: str) -> str:
    parts = text.split()
    action = parts[1].casefold() if len(parts) > 1 else "help"
    if action == "join":
        chat_id = parts[2] if len(parts) > 2 else event.chat.id
        call_id = await player.join(chat_id)
        return f"وارد تماس {call_id} شد ✅"
    if action == "play":
        media = event.message.replied_to
        if media is None:
            return "روی یک آهنگ یا ویس ریپلای کنید."
        is_audio = await filters.audio.check(app, media)
        is_voice = await filters.voice.check(app, media)
        if not is_audio and not is_voice:
            return "پیام ریپلای‌شده آهنگ یا ویس نیست."
        await player.play(await media.download(), media.caption or "Bale audio")
        return "پخش شروع شد ▶️"
    if action == "pause":
        player.pause()
        return "پخش مکث شد ⏸"
    if action == "resume":
        player.resume()
        return "پخش ادامه پیدا کرد ▶️"
    if action == "stop":
        await player.stop()
        return "پخش متوقف شد ⏹"
    if action == "status":
        return player.status()
    if action == "leave":
        await player.leave()
        return "از تماس خارج شد ✅"
    return HELP


@app.on_shutdown
async def shutdown(_client):
    await player.leave()


if __name__ == "__main__":
    app.run_forever()
