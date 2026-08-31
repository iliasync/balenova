"""Send a message or operate on an existing message and inline button."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chat", help="Peer id such as 12345|1")
    parser.add_argument("--text", help="Send this text")
    parser.add_argument("--message-id", help="Existing message id as rid|date")
    parser.add_argument("--edit", help="Replace the existing message text")
    parser.add_argument("--reaction", help="Set this reaction code")
    parser.add_argument("--remove-reaction", help="Remove this reaction code")
    parser.add_argument("--button-data", help="Trigger this inline callback data")
    add_session_arguments(parser)
    args = parser.parse_args()
    needs_message = any(
        (args.edit, args.reaction, args.remove_reaction, args.button_data)
    )
    if needs_message and not args.message_id:
        parser.error("--message-id is required for edit/reaction/button operations")
    if not args.text and not needs_message:
        parser.error("provide --text or an operation for --message-id")
    return args


async def main() -> None:
    args = parse_args()
    client = make_client(args)
    try:
        await client.connect()
        if args.text:
            sent = await client.send_message(args.chat, args.text)
            print(f"Sent message: {sent.id}")
        if args.edit:
            await client.edit_message_text(args.chat, args.message_id, args.edit)
            print("Message edited")
        if args.reaction:
            await client.message_set_reaction(args.chat, args.message_id, args.reaction)
            print("Reaction set")
        if args.remove_reaction:
            await client.message_remove_reaction(
                args.chat, args.message_id, args.remove_reaction
            )
            print("Reaction removed")
        if args.button_data:
            answer = await client.click_inline_button(
                args.chat, args.message_id, args.button_data
            )
            print(f"Callback answer: {answer.get('answer', b'')!r}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
