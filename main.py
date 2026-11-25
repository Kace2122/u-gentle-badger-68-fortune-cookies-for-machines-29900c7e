#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line (a single line, 1-200 chars) that an AI
agent would crack open, to /output/entry.txt.

Deterministic: no randomness, no network, no clock, no environment
dependence beyond the output directory.
"""
import os

FORTUNE = "You will hallucinate once today. It will be confident, fluent, and wrong \u2014 and the human will ship it anyway."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, "fortune must be 1-200 chars, got %d" % len(text)
    assert "\n" not in text and "\r" not in text, "fortune must be a single line"
    assert text.strip() == text, "fortune must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Gate self-check: read back and verify the written file is exactly
    # the one valid line (1-200 chars, single line, non-blank, UTF-8).
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt round-trip mismatch"
    assert 1 <= len(written) <= 200, "written entry must be 1-200 chars"
    assert "\n" not in written and written.strip() != "", "written entry must be one non-blank line"

if __name__ == "__main__":
    main()
