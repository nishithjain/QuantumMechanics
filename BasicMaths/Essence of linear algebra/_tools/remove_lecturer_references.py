#!/usr/bin/env python3
"""Remove the word 'lecturer' from all notes/lecture-notes.md files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Longest / most specific replacements first (case-insensitive via re.IGNORECASE)
PHRASES: list[tuple[str, str]] = [
    (r"## 9\. The lecturer's first determinant example", "## 9. First determinant example"),
    (r"## 6\. The lecturer's correction:", "## 6. Correction:"),
    (r"## 8\. The lecturer's closing advice:", "## 8. Closing advice:"),
    (r"### 2\.1 Build the lecturer's vector", "### 2.1 Build the example vector"),
    (r"### 2\.2 What the lecturer calls a \*basis\*", "### 2.2 What we call a *basis*"),
    (r"### 10\.4 The lecturer's closing puzzle", "### 10.4 Closing puzzle"),
    (r"## 10\. Lecturer's numerical sanity check:", "## 10. Numerical sanity check:"),
    (r"## 12\. Final reflection: what the lecturer wants you to understand",
     "## 12. Final reflection: what to take away"),
    (r"## Review: the ideas in the lecturer's order", "## Review: the ideas in order"),
    (r"\*\*Approach:\*\* follow the lecturer's order", "**Approach:** follow the lesson order"),
    (r"they follow the lecturer's sequence", "they follow the lesson sequence"),
    (r"follows the lecturer's sequence", "follows the lesson sequence"),
    (r"follow the lecturer's order", "follow the lesson order"),
    (r"from the lecturer's central examples", "from the central examples in the source material"),
    (r"the lecturer's actual teaching progression", "the actual teaching progression"),
    (r"quoted by the lecturer for his two slanted arrows",
     "quoted in the source for the two slanted arrows"),
    (r"\(the lecturer demonstrates", "(this demo illustrates"),
    (r"not a claim that the lecturer assigned them",
     "not a claim that the source video assigned them"),
    (r"In the lecturer's numerical example", "In the numerical example"),
    (r"in the lecturer's numerical example", "in the numerical example"),
    (r"In the lecturer's geometric picture", "In the geometric picture"),
    (r"in the lecturer's diagram", "in the diagram"),
    (r"In the lecturer's example", "In the example"),
    (r"the lecturer's later numerical example", "the later numerical example"),
    (r"The lecturer's \*later numerical example\*", "The *later numerical example*"),
    (r"The lecturer's clever move", "The clever move"),
    (r"The lecturer's next question", "The next question"),
    (r"The lecturer's important point", "An important point"),
    (r"the lecturer's strongest warnings", "the strongest warnings"),
    (r"The lecturer's main insight", "The main insight"),
    (r"The lecturer's answer", "The answer"),
    (r"The lecturer's guideline", "The guideline"),
    (r"The lecturer's central 3D mental image", "The central 3D mental image"),
    (r"The lecturer's point", "The key point"),
    (r"The lecturer's reasoning", "This reasoning"),
    (r"The lecturer's recap", "this recap"),
    (r"the lecturer's idea", "the central idea"),
    (r"the lecturer's vector", "the example vector"),
    (r"So the lecturer's vector", "So the example vector"),
    (r"To make the lecturer's idea concrete", "To make the idea concrete"),
    (r"That is the lecturer's next question", "That is the next question"),
    (r"That completes the lecturer's recap", "That completes this recap"),
    (r"The lecturer's geometric picture", "The geometric picture"),
    (r"homework question from his first linear algebra class",
     "homework question from a first linear algebra class"),
    (r"This time the lecturer wants us to see", "This time the goal is to see"),
    (r"But the lecturer wants you to remember", "But remember"),
    (r"why the lecturer was able to say earlier", "why we were able to say earlier"),
    (r"Later in the lecture, the lecturer gives", "Later in the lesson, the source gives"),
    (r"A diagram in the original lecture is suggested",
     "A diagram in the original lesson is suggested"),
    (r"the spoken explanation", "the spoken explanation"),  # no-op anchor
    (r"The lecture does not spell out the full 3 × 3 calculation formula in the spoken transcript\. Instead, the lecturer recommends",
     "The lesson does not spell out the full 3 × 3 calculation formula in the spoken transcript. Instead, practice"),
    (r"Near the end of the lecture, the lecturer returns",
     "Near the end of the lesson, return"),
    (r"does the lecturer introduce", "introduce"),
    (r"the lecturer describes them as", "think of them as"),
    (r"The lecturer describes the plane as", "Think of the plane as"),
    (r"He gives a helpful geometric way", "Here is a helpful geometric way"),
    (r"he challenges us to calculate", "the challenge is to calculate"),
    (r"The lecturer closes by asking you to", "Close by asking yourself to"),
    (r"The lecturer closes with a thought exercise:",
     "Close with a thought exercise:"),
]

# Line-start sentence openers (multiline mode per line applied separately)
LINE_STARTERS: list[tuple[str, str]] = [
    (r"The lecturer now ", "We now "),
    (r"The lecturer begins ", "This section begins "),
    (r"The lecturer starts ", "This section starts "),
    (r"The lecturer emphasizes ", "Emphasis: "),
    (r"The lecturer considers ", "Consider "),
    (r"The lecturer considers:", "Consider:"),
    (r"The lecturer asks us ", "Try to "),
    (r"The lecturer asks ", ""),
    (r"The lecturer gives ", ""),
    (r"The lecturer points out that ", "Note that "),
    (r"The lecturer points out ", "Note: "),
    (r"The lecturer says ", ""),
    (r"The lecturer states that ", ""),
    (r"The lecturer also gives ", "Also: "),
    (r"The lecturer uses ", "Use "),
    (r"The lecturer connects ", "This connects "),
    (r"The lecturer calls ", ""),
    (r"The lecturer introduces ", "Introduce "),
    (r"The lecturer first imagines ", "First imagine "),
    (r"The lecturer does \*\*not\*\* ", "Do **not** "),
    (r"The lecturer does not ", "The source does not "),
    (r"The lecturer deliberately ", "Deliberately, "),
    (r"The lecturer proposes ", "Consider: "),
    (r"The lecturer expressly warns ", "Important warning: "),
    (r"The lecturer warns ", "Warning: "),
    (r"The lecturer builds ", "The reasoning builds "),
    (r"The lecturer pauses to ", "Pause to "),
    (r"The lecturer pauses the ", "Pause the "),
    (r"The lecturer mentions ", "The source mentions "),
    (r"The lecturer closes by ", "In closing, "),
    (r"The lecturer closes with ", "To close, "),
    (r"The lecturer poses ", ""),
    (r"The lecturer recommends ", ""),
    (r"The lecturer next ", "Next, "),
    (r"The lecturer replaces ", "Replace "),
    (r"The lecturer chooses ", "Choose "),
    (r"The lecturer recalls ", "Recall "),
    (r"The lecturer returns to ", "Return to "),
    (r"The lecturer imagines ", "Imagine "),
    (r"The lecturer describes ", ""),
    (r"The lecturer challenges ", ""),
    (r"The lecturer explains ", "Explain "),
    (r"The lecturer demonstrates ", "The demo shows "),
    (r"Now the lecturer ", "Now "),
    (r"Next, the lecturer ", "Next, "),
    (r"Before finding `x,y`, the lecturer ", "Before finding `x,y`, note "),
    (r"Before moving to the next video, the lecturer ", "Before moving on, "),
    (r"After explaining the meaning, the lecturer ", "After explaining the meaning, "),
    (r"After a 3D linear transformation, the cube may become a slanted box-like shape. The lecturer calls this",
     "After a 3D linear transformation, the cube may become a slanted box-like shape. Call this"),
    (r"So far, we have described the determinant as an area-scaling factor. But the lecturer pauses to clarify",
     "So far, we have described the determinant as an area-scaling factor. Pause to clarify"),
    (r"Near the end, the lecturer ", "Near the end, "),
    (r"Only after showing how standard and alternative bases work does the lecturer introduce",
     "Only after showing how standard and alternative bases work, introduce"),
    (r"The lecturer ", "Note: "),  # catch-all — last resort for line start
]

# Mid-sentence patterns
MID: list[tuple[str, str]] = [
    (r"\bthe lecturer wants us to see\b", "the goal is to see"),
    (r"\bthe lecturer wants you to remember\b", "remember"),
    (r"\bYet the lecturer says that\b", "Yet exploring"),
    (r"\bThe lecturer introduces this special case\b", "This special case is introduced"),
    (r"\bThe lecturer emphasizes signed volumes\b", "Signed volumes are emphasized"),
    (r"\bwhere the lecturer\b", "where the lesson"),
    (r"\bwhen the lecturer\b", "when the lesson"),
    (r"\bas the lecturer\b", "as the lesson"),
    (r"\bif the lecturer\b", "if the lesson"),
]

# Final sweep: any remaining lecturer (possessive and bare)
FINAL: list[tuple[str, str]] = [
    (r"[Ll]ecturer's", ""),
    (r"[Tt]he lecturer", "the lesson"),
    (r"\b[Ll]ecturer\b", "instructor"),  # should not appear; then second pass
]


def transform(text: str) -> str:
    for pat, repl in PHRASES:
        text = re.sub(pat, repl, text, flags=re.IGNORECASE)

  # Line-by-line starters
    lines = []
    for line in text.splitlines(keepends=True):
        raw = line.rstrip("\n\r")
        ending = line[len(raw) :]
        for pat, repl in LINE_STARTERS:
            m = re.match(pat, raw)
            if m:
                raw = repl + raw[m.end() :]
                break
        for pat, repl in MID:
            raw = re.sub(pat, repl, raw, flags=re.IGNORECASE)
        lines.append(raw + ending)
    text = "".join(lines)

    for pat, repl in FINAL:
        text = re.sub(pat, repl, text)

    # Clean up artifacts from empty lecturer's removal
    text = re.sub(r"\bthe lesson's\b", "the", text, flags=re.IGNORECASE)
    text = re.sub(r"  +", " ", text)
    text = re.sub(r" +([,.;:])", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main() -> None:
    paths = sorted(ROOT.glob("**/notes/lecture-notes.md"))
    for path in paths:
        original = path.read_text(encoding="utf-8")
        if not re.search(r"lecturer", original, re.IGNORECASE):
            continue
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            print(f"updated: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()