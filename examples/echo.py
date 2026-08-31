"""Run a private-chat echo userbot until Ctrl+C."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client

from bale import Client, Message, filters


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    client = make_client(parse_args())

    @client.on_connect
    async def connected(active_client: Client) -> None:
        me = active_client.user
        print(f"Connected as {me.full_name if me else 'unknown'}; press Ctrl+C to stop")

    @client.on_message(filters.private & filters.text & ~filters.command("ping"))
    async def echo(message: Message, _client: Client) -> None:
        if message.author.id != (_client.user.id if _client.user else 0):
            await message.reply(f"Echo: {message.text}")

    @client.on_command("ping")
    async def ping(message: Message, _client: Client) -> None:
        await message.reply("pong")

    @client.on_error
    async def log_error(error: BaseException, _client: Client) -> None:
        print(f"Handler error: {error}")

    try:
        await client.run()
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
