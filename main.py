#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email entry.

Writes one joke line to /output/entry.txt. The line was chosen by manual
ranking against the competition's judge brief (on-topic, laugh lands on the
last word, fresh angle, tight wording, true to real meetings). See
candidates.md for the full candidate list and the ranking.
"""

import os

LINE = "Nobody had read the email, so the meeting was just the email, read out loud, slowly, by six people taking turns."

# The competition gate: /output/entry.txt must be UTF-8 text of 1-200
# characters, not only white space. Refuse to write an invalid line
# rather than silently submitting a losing entry.
MAX_CHARS = 200


def main():
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        raise SystemExit(
            f"entry line fails the gate: {len(LINE)} chars, "
            f"blank={not LINE.strip()}"
        )
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line, no newline")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back what was written: the entry is judged byte for byte, so
    # refuse a run whose output differs from the chosen line by even one
    # byte instead of submitting a corrupted file.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            f"entry mismatch after write: wrote {len(written)} chars, "
            f"expected {len(LINE)}"
        )


if __name__ == "__main__":
    main()
