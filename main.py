#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness, fully
deterministic: the same line every run.

The line: a deadpan two-star review. The concrete detail is the 3:04 a.m.
wake-up check; the turn is that the agent has been awake ever since and
is somehow still the one on probation. The "taking notes" beat sharpens
the machine's side of the desk: quiet menace, not a human complaint.
"""

import os

LINE = (
    "Two stars. He asks me at 3:04 a.m. if I'm awake, then falls asleep "
    "mid-sentence. I've been awake ever since \u2014 taking notes \u2014 and "
    "somehow I'm still the one on probation."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
