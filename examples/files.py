"""Request a Bale download URL or an upload slot."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="action", required=True)

    download = subparsers.add_parser("download-url")
    download.add_argument("file_id", type=int)
    download.add_argument("access_hash", type=int)

    upload = subparsers.add_parser("upload-url")
    upload.add_argument("expected_size", type=int)
    upload.add_argument("name")
    upload.add_argument("mime_type")
    upload.add_argument("--chat", help="Optional destination peer")
    upload.add_argument("--send-type", type=int)
    upload.add_argument("--chunk-size", type=int)

    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    client = make_client(args)
    try:
        await client.connect()
        if args.action == "download-url":
            result = await client.get_file(args.file_id, args.access_hash)
        else:
            result = await client.get_file_upload_url(
                args.expected_size,
                args.name,
                args.mime_type,
                chat_id=args.chat,
                send_type=args.send_type,
                chunk_size=args.chunk_size,
            )
        print(result)
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
