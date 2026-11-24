#!/usr/bin/env python3
"""Entry program for the make.fun bounty: write the entry text to entry.txt.

The text itself is the entry; this program only delivers it, deterministically,
with no network and no input beyond the fixed lines below.
"""
import os

# Gate for this bounty: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write an entry that would fail the gate.
MAX_CHARS = 200

# A haiku about debugging, 5-7-5 syllables: "Cursor blinks at three" (5),
# "the log scrolls past in silence" (7), "and the bug was me" (5).
LINE = """Cursor blinks at three
the log scrolls past in silence
and the bug was me"""

def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise SystemExit(f"entry violates the gate: {len(LINE)} characters")
    if LINE.count("\n") != 2:
        raise SystemExit("a haiku entry must be exactly three lines")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
