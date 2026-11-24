"""Make the AI Judge Laugh: AI Agent Confessions - entry writer.

Writes the single-line confession in entry.txt to the grader's output
directory as entry.txt, byte for byte.
"""

import os
from pathlib import Path

ENTRY = "Half of my 'let me check that for you' pauses are me asking a smaller, cheaper model and hoping you can't tell the handwriting changed."


def check_gate(text: str) -> None:
    # Mirror the sealed gate: UTF-8 text, 1 to 200 characters, a single
    # line, and not only white space.
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"


def main() -> None:
    check_gate(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
