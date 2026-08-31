"""List dialogs and optionally show recent history for one Bale peer."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--chat", help="Peer id such as 12345|1")
    parser.add_argument("--history-limit", type=int, default=10)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    client = make_client(args)
    try:
        await client.connect()
        result = await client.load_dialogs(limit=max(1, args.limit))
        dialogs = result.get("dialogs", [])
        print(f"Dialogs: {len(dialogs)}")
        for dialog in dialogs:
            peer = dialog.get("peer") or {}
            print(
                f"- {peer.get('id', 0)}|{peer.get('type', 0)} "
                f"unread={dialog.get('unread_count', 0)}"
            )

        if args.chat:
            history = await client.load_history(
                args.chat, limit=max(1, args.history_limit)
            )
            print(f"\nRecent messages in {args.chat}:")
            for message in history:
                print(f"- {message.id}: {message.content!r}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
