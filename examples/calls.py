"""Inspect call logs or explicitly run a Bale group-call signaling action."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="action", required=True)
    subparsers.add_parser("logs")
    subparsers.add_parser("ongoing")

    generate = subparsers.add_parser("generate-link")
    generate.add_argument("--title")
    generate.add_argument("--private", action="store_true")

    start = subparsers.add_parser("start")
    start.add_argument("chat", help="Group/channel peer id")
    start.add_argument("--video", action="store_true")

    join = subparsers.add_parser("join")
    join.add_argument("call_id", type=int)
    join.add_argument("--name")

    leave = subparsers.add_parser("leave")
    leave.add_argument("call_id", type=int)
    leave.add_argument("--end", action="store_true")

    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    client = make_client(args)
    try:
        await client.connect()
        result: object
        if args.action == "logs":
            result = await client.get_call_logs()
        elif args.action == "ongoing":
            result = await client.get_ongoing_calls()
        elif args.action == "generate-link":
            result = await client.generate_call_link(
                is_public=not args.private, title=args.title
            )
        elif args.action == "start":
            result = await client.start_group_call(args.chat, video=args.video)
        elif args.action == "join":
            result = await client.join_group_call(args.call_id, args.name)
        else:
            result = await client.leave_group_call(args.call_id, end=args.end)
        print(result)
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
