#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — make.fun entry.

Writes one original funny line (at most 200 characters) to
/output/entry.txt. Fully deterministic: the line is a fixed string
literal. No randomness, no clock, no network, no environment input,
so every run produces byte-identical output.
"""

from pathlib import Path

LINE = "I asked an AI to write my wedding vows; it replied, 'As an AI language model, I don't do commitment.'"

# The joke: a wedding-vow setup (commitment) broken by the AI's own
# catchphrase — "commitment" lands twice, once as marriage, once as
# the model's refusal. One breath, punchline at the very end.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
