"""List account dialogs grouped into groups, channels, chats, and bots."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages", type=int, default=10)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    client = make_client(args)
    try:
        await client.connect()
        buckets = await client.get_all_dialogs_by_type(max_pages=max(1, args.pages))
        for name, entries in buckets.items():
            print(f"{name}: {len(entries)}")
            for entry in entries[:5]:
                print("  -", getattr(entry, "id", getattr(entry, "peer_id", entry)))
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
