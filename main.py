#!/usr/bin/env python3
"""One Word From Your Ex — Account A entry.

The word is the last text she sent, still sitting unread as a monument.

Her word for him is "unread": he never read her messages, and she
never really read him. One word, two indictments, no explanation
needed. Deterministic: no randomness, no clock, no network, no input.
Writes exactly the word to /output/entry.txt.
"""

import os

WORD = "unread"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
