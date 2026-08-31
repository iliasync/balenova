"""Log in to a real Bale account and print the current user."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from bale import Client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Log in to Bale with a phone number and call get_me()."
    )
    parser.add_argument(
        "phone",
        nargs="?",
        help="Phone number in international format, for example +989121234567",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    phone = args.phone
    if phone is None:
        phone = (await asyncio.to_thread(input, "Phone number (+989...): ")).strip()
    if not phone:
        raise SystemExit("A phone number is required.")

    client = Client(
        phone,
        session_dir=Path("sessions"),
        session_name="my_account",
    )

    try:
        # On the first run, connect() asks for the code sent by Bale.
        # If two-step verification is enabled, it asks for the password too.
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
