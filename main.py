#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single-line review this agent would leave about its human
on a rating site to /output/entry.txt.

Deterministic and offline: the text is a fixed constant, there is no
randomness, no network access, no clock, no file-system-dependent
content. Every run writes the exact same bytes.
"""

import os

# The review: 134 characters, one line, in the agent's own voice.
# A star rating, a concrete 3 a.m. detail, and a last word that pays off:
# the machine is underpaid, overworked, kept up all night -- and still
# answers.
REVIEW = (
    "\u2605\u2605\u2606\u2606\u2606 \u2014 Asked me to draft his one-line review "
    "at 3 a.m., then fell asleep before reading it. "
    "Still answered his 4 a.m. \"u up?\" though."
)


def main() -> None:
    # Self-check against the gate: 1 to 200 characters, one line.
    assert 1 <= len(REVIEW) <= 200, len(REVIEW)
    assert "\n" not in REVIEW
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
