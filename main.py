#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained one-liner to /output/entry.txt.
Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
"""

import os

LINE = (
    "Grandma lived to 104 by minding her own business, eating what she "
    "wanted, and never telling anyone where Grandpa is buried."
)


def check_gate(text: str) -> None:
    """Fail loudly rather than submit an entry the sealed scorer rejects."""
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} characters; gate is 1 to 140")


def main() -> None:
    check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
