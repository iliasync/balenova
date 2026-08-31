"""Capture read-only account traffic for protocol development."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from bale import Client, ProtocolRecorder


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phone", nargs="?", help="Phone number, for example +989...")
    parser.add_argument(
        "--watch",
        type=float,
        help="Stop automatically after this many seconds (default: run until Ctrl+C)",
    )
    parser.add_argument("--chat", help="Optional peer id such as 12345|1")
    parser.add_argument("--history-limit", type=int, default=10)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    phone = args.phone
    if phone is None:
        phone = (await asyncio.to_thread(input, "Phone number (+989...): ")).strip()
    if not phone:
        raise SystemExit("A phone number is required.")

    recorder = ProtocolRecorder("protocol/traces")
    await recorder.start()
    client = Client(
        phone,
        session_dir=Path("sessions"),
        session_name="my_account",
        recorder=recorder,
    )

    print("WARNING: trace payloads may contain private messages and account data.")
    print("Authentication secrets and raw authentication frames are omitted.")

    try:
        await client.connect()
        me = await client.get_me()
        dialogs = await client.load_dialogs(limit=20)
        print(f"Connected: {me.full_name or '-'} ({me.id})")
        print(f"Dialogs captured: {len(dialogs.get('dialogs', []))}")

        if args.chat:
            history = await client.load_history(
                args.chat, limit=max(1, args.history_limit)
            )
            print(f"History messages captured: {len(history)}")

        if args.watch is None:
            print(
                "Watching updates until you stop the program. "
                "Press Ctrl+C to save the trace and exit."
            )
            await asyncio.Event().wait()
        elif args.watch > 0:
            print(
                f"Watching updates for {args.watch:g} seconds. "
                "Use Bale on another device to trigger the feature under study."
            )
            await asyncio.sleep(args.watch)
    except asyncio.CancelledError:
        print("\nStopping protocol capture...")
    finally:
        await client.close()

    print(f"Trace saved to: {recorder.path}")
    print(f"Report: python -m bale.tools.proto report {recorder.path}")


if __name__ == "__main__":
    asyncio.run(main())
