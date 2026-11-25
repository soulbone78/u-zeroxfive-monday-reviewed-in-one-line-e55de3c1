#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one funny one-line review of the entrant's own Monday to
/output/entry.txt. Pure standard library, no network, no input files.
"""
import os
import sys

# Grader runs with `python3 -P -s`, which drops the script's directory from
# sys.path; this entry is a single file with no local imports, but keep the
# bootstrap anyway so the pattern holds if it ever grows a sibling module.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LINE = (
    "Monday review: my alarm gave up, my inbox doubled overnight, "
    "and I spent an hour in a meeting about a meeting that could "
    "have been an email."
)


def _verify_written(path: str, expected: str) -> None:
    """Re-read the written entry and confirm it round-trips exactly.

    Guards against a partial write or an encoding slip: what the judge
    reads must be byte-for-byte the text we validated above.
    """
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == expected, "written entry does not match validated text"
    assert written == written.strip(), "entry must not gain stray whitespace"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)  # exactly one line, no trailing newline
    _verify_written(out_path, text)


if __name__ == "__main__":
    main()
