"""Inspect the current wallet or explicitly send a Bale gift packet."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client

from bale import GivingType


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="action", required=True)
    subparsers.add_parser("wallet")

    send = subparsers.add_parser("send")
    send.add_argument("chat", help="Destination peer id")
    send.add_argument("amount", type=int)
    send.add_argument("message")
    send.add_argument("--count", type=int, default=1)
    send.add_argument("--random", action="store_true")
    send.add_argument("--hide-amounts", action="store_true")

    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    client = make_client(args)
    try:
        await client.connect()
        if args.action == "wallet":
            wallet = await client.get_wallet()
            if wallet.wallet is None:
                print("No wallet is available for this account")
            else:
                print(f"Balance: {wallet.wallet.balance}")
                print(f"Level: {wallet.wallet.level}")
        else:
            response = await client.send_gift(
                args.chat,
                args.amount,
                args.message,
                gift_count=max(1, args.count),
                giving_type=(GivingType.RANDOM if args.random else GivingType.SAME),
                show_amounts=not args.hide_amounts,
            )
            print(f"Gift sent: seq={response.seq} date={response.date}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
