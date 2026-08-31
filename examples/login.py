"""Log in to a real Bale account and print the current user."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    client = make_client(parse_args())

    try:
        # connect() uses the saved session first. If it is missing or expired,
        # the phone number, code, and optional password are prompted here.
        await client.connect()
        me = await client.get_me()

        print("\nLogin successful")
        print(f"ID: {me.id}")
        print(f"Name: {me.full_name or '-'}")
        print(f"Username: @{me.username}" if me.username else "Username: -")
        print(f"Is bot: {me.is_bot}")
        print("Session saved in: sessions/my_account.session")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
