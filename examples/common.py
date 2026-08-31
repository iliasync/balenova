"""Shared command-line helpers for the examples."""

from __future__ import annotations

import argparse
from pathlib import Path

from balenova import Client


def add_session_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--session-dir",
        type=Path,
        default=Path("sessions"),
        help="Directory containing Bale session files (default: sessions)",
    )
    parser.add_argument(
        "--session-name",
        default="my_account",
        help="Session file name without the .session suffix",
    )


def make_client(args: argparse.Namespace) -> Client:
    return Client(session_dir=args.session_dir, session_name=args.session_name)
