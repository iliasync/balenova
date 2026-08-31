"""Reply to a simple command sent from this account."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client

from balenova import Client, filters


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    client = make_client(parse_args())

    @client.on_message(filters.outgoing & filters.command("status"))
    async def status(message, _client: Client) -> None:
        await message.answer("BaleNova is online")

    try:
        await client.run()
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
