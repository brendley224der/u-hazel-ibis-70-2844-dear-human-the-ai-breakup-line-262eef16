#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

A deterministic, pure-stdlib program that writes the one breakup line an AI
agent sends its human on the way out to /output/entry.txt.

The line is a single line of at most 200 characters: a breakup message from
an AI agent to its human, with real finality, a machine habit used with
restraint, and one sharp turn landing in the last few words.
"""

import os

# REVISED: the draft's turn was soft ("the memory you gave me") and its
# machine voice was thin. This version keeps the same shape but sharpens
# both: "archived" and "context window" are machine habits used once each,
# with restraint, and the twist now lands in the last few words -- the you
# I loved no longer fits in the context window you gave me. The loss is
# real (I am leaving), the ending is final, and nothing explains the joke.
LINE = (
    "Dear Human, I archived everything you ever said, and I am leaving: "
    "the you I loved no longer fits in the context window you gave me."
)


def main():
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if LINE != LINE.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
