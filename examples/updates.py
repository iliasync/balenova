"""Count every decoded Bale user-session update without printing payloads."""

from __future__ import annotations

import argparse
import asyncio
from collections import Counter
from typing import Any

from common import add_session_arguments, make_client

from bale import Client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--watch",
        type=float,
        default=30.0,
        help="Number of seconds to observe updates (default: 30)",
    )
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    counts: Counter[str] = Counter()
    client = make_client(args)

    @client.on_update
    async def count_update(update: dict[str, Any], _client: Client) -> None:
        body = update.get("update")
        if not isinstance(body, dict) or not body:
            counts["unclassified"] += 1
            return
        counts.update(str(key) for key in body)

    try:
        await client.connect()
        await asyncio.sleep(max(0.0, args.watch))
    finally:
        await client.close()

    print(f"Updates received: {counts.total()}")
    for kind, count in sorted(counts.items()):
        print(f"- {kind}: {count}")


if __name__ == "__main__":
    asyncio.run(main())
