"""Watch incoming text messages with composable account-session filters."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client

from bale import Client, filters


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=60.0)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    client = make_client(args)

    @client.on_message(filters.incoming & filters.text & ~filters.bot)
    async def print_message(message, _client: Client) -> None:
        print(f"{message.chat.id} <{message.sender_id}>: {message.content}")

    try:
        await client.connect()
        await asyncio.sleep(max(0.0, args.seconds))
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
