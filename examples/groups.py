"""Inspect a group and optionally perform an explicit administration action."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chat", help="Group/channel peer id such as 12345|2")
    parser.add_argument("--members-limit", type=int, default=20)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--set-title")
    actions.add_argument("--invite-user", type=int)
    actions.add_argument("--kick-user", type=int)
    actions.add_argument("--unban-user", type=int)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    client = make_client(args)
    try:
        await client.connect()
        full_group = await client.get_full_group(args.chat)
        count = await client.get_group_members_count(args.chat)
        members = await client.load_members(args.chat, limit=max(1, args.members_limit))
        avatars = await client.load_group_avatars(args.chat)
        invite_url = await client.get_group_link(args.chat)
        print(f"Title: {(full_group or {}).get('title', '-')}")
        print(f"Members: {count} (loaded {len(members.get('members', []))})")
        print(f"Avatars: {len(avatars)}")
        print(f"Invite URL: {invite_url or '-'}")

        if args.set_title:
            await client.edit_group_title(args.chat, args.set_title)
            print("Group title updated")
        elif args.invite_user is not None:
            await client.invite_users(args.chat, [args.invite_user])
            print("Invitation sent")
        elif args.kick_user is not None:
            await client.kick_user(args.chat, args.kick_user)
            print("User removed")
        elif args.unban_user is not None:
            await client.unban_user(args.chat, args.unban_user)
            print("User unbanned")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
