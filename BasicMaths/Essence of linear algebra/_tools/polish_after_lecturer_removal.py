#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SUBS = [
    (r"follows the lesson sequence", "follow the teaching sequence"),
    (r"follow the lesson sequence", "follow the teaching sequence"),
    (r"Emphasis: that ", "Emphasis: "),
    (r"We now asks\b", "We now ask"),
    (r"> the lesson assumes", "> This chapter assumes"),
    (r"\bthe lesson first\b", "This section first"),
    (r"\bthe lesson uses\b", "This section uses"),
    (r"\bthe lesson notes that\b", "The notes observe that"),
    (r"\bthe lesson wants to\b", "The goal is to"),
    (r"\bthe lesson wants us to\b", "Try to"),
    (r"\bthe lesson asks us to\b", "Try to"),
    (r"\bthe lesson asks\b", "Ask"),
    (r"\bthe lesson says that\b", ""),
    (r"\bthe lesson says\b", ""),
    (r"\bthe lesson presents\b", "This section presents"),
    (r"\bthe lesson gives\b", "This section gives"),
    (r"\bthe lesson points out that\b", "Note that"),
    (r"\bthe lesson encourages\b", "Try to"),
    (r"\bthe lesson makes an important distinction\b", "Make an important distinction"),
    (r"\bthe lesson chooses\b", "Choose"),
    (r"\bthe lesson closes\b", "To close"),
    (r"\bthe lesson jokes\b", "It may seem surprising"),
    (r"\bthe lesson explicitly\b", "Explicitly"),
    (r"\bthe lesson also points out\b", "Also note"),
    (r"\bthe lesson also\b", "Also"),
    (r"\bthe lesson summarizes\b", "To summarize"),
    (r"\bthe lesson defines\b", "Define"),
    (r"\bthe lesson sharpens\b", "Sharpen"),
    (r"\bthe lesson is interested in\b", "Focus on"),
    (r"\bthe lesson deliberately\b", "Deliberately"),
    (r"\bthe lesson returns to\b", "Return to"),
    (r"\bthe lesson explained\b", "earlier chapters explained"),
    (r"\bthe lesson restricts attention to\b", "restrict attention to"),
    (r"\bthe lesson concludes\b", "To conclude"),
    (r"\bthe lesson temporarily\b", "Temporarily"),
    (r"\bthe lesson now asks\b", "We now ask"),
    (r"\bthe lesson now\b", "We now"),
    (r"\bthe lesson opens\b", "This section opens"),
    (r"\bthe lesson then asks\b", "Then ask"),
    (r"\bthe lesson then makes\b", "Then note"),
    (r"\bthe lesson then\b", "Then"),
    (r"\bthe lesson tracks\b", "Track"),
    (r"\bthe lesson suggests\b", "Try"),
    (r"\bthe lesson assumes\b", "This chapter assumes"),
    (r"\bthe lesson emphasizes\b", "Emphasis:"),
    (r"\bthe lesson intentionally\b", "Intentionally"),
    (r"\bthe lesson ends by\b", "To end,"),
    (r"\bthe lesson ends with\b", "To end with"),
    (r"\bthe lesson reuses\b", "Reuse"),
    (r"\bthe lesson shows\b", "Note"),
    (r"\bthe lesson steps back\b", "Step back"),
    (r"\bthe lesson is not a claim\b", "This is not a claim"),
    (r"\bthe lesson notes that\b", "Note that"),
    (r"\bthe lesson\b", "this lesson"),
    (r"^Note: ", ""),  # line-level below
]


def polish(text: str) -> str:
    for pat, repl in SUBS:
        if pat == r"^Note: ":
            continue
        text = re.sub(pat, repl, text, flags=re.IGNORECASE)

    lines = []
    for line in text.splitlines(keepends=True):
        raw = line.rstrip("\n\r")
        ending = line[len(raw) :]
        if raw.startswith("Note: "):
            raw = raw[6:]
            if raw:
                raw = raw[0].upper() + raw[1:]
        lines.append(raw + ending)
    text = "".join(lines)

    text = re.sub(r"  +", " ", text)
    text = re.sub(r" +([,.;:])", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main() -> None:
    for path in sorted(ROOT.glob("**/notes/lecture-notes.md")):
        original = path.read_text(encoding="utf-8")
        updated = polish(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            print(f"polished: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()