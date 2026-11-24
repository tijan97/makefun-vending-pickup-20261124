#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR).
"""

import os

ENTRY = (
    "I only take exact change, but for you I'll jam the coil myself "
    "\u2014 press B7 and let me drop something sweet."
)


def validate_entry(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry contains a double space")


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    validate_entry(ENTRY)
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
