import argparse
import os
from datetime import datetime

from assests.start import fetch_heading


def current_time() -> str:
    """Return the current time formatted for display."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def list_directory(path: str) -> tuple[str, list[str]]:
    """Return the resolved path and its contents if it exists."""
    resolved = os.path.abspath(os.path.expanduser(path))
    if not os.path.isdir(resolved):
        raise FileNotFoundError(f"Directory not found: {path}")
    return resolved, sorted(os.listdir(resolved))


def run_cli():
    parser = argparse.ArgumentParser(
        description="xter-cli: quick banner, time, and directory helper"
    )
    parser.add_argument(
        "-H",
        "--heading",
        action="store_true",
        help="display the ASCII heading banner",
    )
    parser.add_argument(
        "-t",
        "--time",
        action="store_true",
        help="show the current time",
    )
    parser.add_argument(
        "-l",
        "--list",
        nargs="?",
        const=".",
        default=None,
        help="list contents of a directory (default: current directory)",
    )

    args = parser.parse_args()
    no_flags = not (args.heading or args.time or args.list is not None)

    if args.heading or no_flags:
        print(fetch_heading())

    if args.time or no_flags:
        print(f"Current time: {current_time()}")

    if args.list is not None:
        try:
            resolved, items = list_directory(args.list)
        except FileNotFoundError as exc:
            print(exc)
        else:
            print(f"Contents of {resolved}:")
            for name in items:
                print(f"- {name}")


if __name__ == "__main__":
    run_cli()
