"""Regenerate committed protobuf Python modules from source .proto files."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from grpc_tools import protoc

ROOT = Path(__file__).resolve().parents[1]
PROTO_DIRECTORY = ROOT / "src" / "bale" / "proto"
PROTO_FILES = ("struct.proto", "request.proto", "response.proto")


def generate(output: Path) -> None:
    result = protoc.main(
        [
            "grpc_tools.protoc",
            f"--proto_path={PROTO_DIRECTORY}",
            f"--python_out={output}",
            *(str(PROTO_DIRECTORY / name) for name in PROTO_FILES),
        ]
    )
    if result:
        raise SystemExit(result)
    for name in ("request_pb2.py", "response_pb2.py"):
        path = output / name
        content = path.read_text(encoding="utf-8")
        content = content.replace(
            "import struct_pb2 as struct__pb2",
            "from . import struct_pb2 as struct__pb2",
        )
        content = content.replace(
            "import request_pb2 as request__pb2",
            "from . import request_pb2 as request__pb2",
        )
        path.write_text(content, encoding="utf-8")


def check() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        output = Path(temporary)
        generate(output)
        different = [
            name
            for name in ("struct_pb2.py", "request_pb2.py", "response_pb2.py")
            if (output / name).read_bytes() != (PROTO_DIRECTORY / name).read_bytes()
        ]
    if different:
        raise SystemExit(
            f"Generated protobuf modules are stale: {', '.join(different)}"
        )
    print("Generated protobuf modules are up to date.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="verify without changing source files"
    )
    args = parser.parse_args()
    if args.check:
        check()
        return
    generate(PROTO_DIRECTORY)
    print(f"Generated protobuf modules in {PROTO_DIRECTORY}")


if __name__ == "__main__":
    main()
