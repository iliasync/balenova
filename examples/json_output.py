"""Print the authenticated account as a class, dict, and JSON."""

from __future__ import annotations

import argparse
import asyncio

from common import add_session_arguments, make_client

from balenova import model_to_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    add_session_arguments(parser)
    return parser.parse_args()


async def main() -> None:
    client = make_client(parse_args())
    try:
        await client.connect()
        me = await client.get_me()
        print("Class:", me)
        print("Dict:", me.to_dict())
        print("JSON:\n", model_to_json(me))
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
