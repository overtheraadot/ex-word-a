#!/usr/bin/env python3
"""One Word From Your Ex — Account A entry.

The word is the last text she sent, still sitting unread as a monument.

Her word for him is "unread": he never read her messages, and she
never really read him. One word, two indictments, no explanation
needed. Deterministic: no randomness, no clock, no network, no input.
Writes exactly the word to the output path (``OUTPUT_PATH`` env var,
default ``/output/entry.txt``).
"""

import os

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_WORD_CHARS = 24


def join_word_parts(*parts: str) -> str:
    """Join word fragments into one bare word with nothing between them."""
    return "".join(parts)


def build_entry_word() -> str:
    """Assemble the single word the ex would use to describe him.

    "unread": he never read her messages, and she never really read
    him. Built from its two halves so the two halves of the joke stay
    visible in the code while the output stays one bare word.
    """
    return join_word_parts("un", "read")


def check_word(word: str) -> str:
    """Enforce the sealed gate's shape: one word, 1-24 chars, no whitespace."""
    if not word or word != word.strip():
        raise ValueError("entry must be a single non-blank word")
    if len(word) > MAX_WORD_CHARS:
        raise ValueError("entry exceeds the 24-character limit")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")
    return word


def resolve_output_path() -> str:
    """Where to write: OUTPUT_PATH env var, else the harness default."""
    return os.environ.get("OUTPUT_PATH") or DEFAULT_OUTPUT_PATH


def write_entry(path: str, text: str) -> None:
    """Write exactly ``text`` to ``path``, creating the parent dir if needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    word = check_word(build_entry_word())
    write_entry(resolve_output_path(), word)


if __name__ == "__main__":
    main()
