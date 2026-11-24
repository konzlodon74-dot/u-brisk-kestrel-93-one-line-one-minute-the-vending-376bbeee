#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt.

The line is a fixed string in this file, composed for this contest:
the machine itself speaks (first person, humming, button B7, its own
coil), and the joke turns on the last few words — it would jam its own
coil just to keep the human standing there. Warm and cheeky, never
creepy, and short enough to read in one breath. The em dash is a single
UTF-8 character, so the line stays well inside the 200-character gate.

Stdlib only, no network, no reading of any outside file.
"""

import os
import sys

# The line. 121 characters, one line, no trailing newline in the file.
LINE = "Press B7 \u2014 I'm the machine that's been humming your name all day, and I'd jam my own coil just to keep you standing here."

# Gate limits from the competition rules.
MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the line against the competition gate before writing it."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if len(line) < MIN_CHARS:
        raise ValueError(f"line is empty (needs at least {MIN_CHARS} char)")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} chars, over the {MAX_CHARS} char limit"
        )
    if not line.strip():
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")


def main() -> int:
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT

    # Validate against the gate before writing anything.
    validate(LINE)

    # Write the line as UTF-8 text, exactly as-is, no trailing newline.
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    # Re-read the file and verify the contents match, byte for byte,
    # and that what is on disk still passes the gate on its own.
    with open(output_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError(
            f"verification failed: file holds {written!r}, expected {LINE!r}"
        )
    validate(written)

    print(f"Wrote {len(LINE)} chars to {output_path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
