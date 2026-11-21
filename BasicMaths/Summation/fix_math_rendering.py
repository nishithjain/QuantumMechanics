"""Normalize $$ fences and fix common LaTeX rendering issues in Summation_Basics.md."""
from __future__ import annotations

import re
from pathlib import Path

PATH = Path(__file__).with_name("Summation_Basics.md")
QUIZ_MARKER = "# Self-assessment quiz"


def collapse_empty_display_fences(text: str) -> str:
    """Turn consecutive $$ lines into a single opening or closing fence."""
    while True:
        new = re.sub(r"(?m)^\$\$\s*\n^\$\$\s*\n", "$$\n", text)
        if new == text:
            break
        text = new
    return text


def strip_fences_inside_aligned(text: str) -> str:
    """Remove spurious $$ lines inside \\begin{aligned} ... \\end{aligned}."""

    def fix_block(match: re.Match[str]) -> str:
        block = match.group(0)
        inner = block
        inner = re.sub(r"\n\$\$\s*\n", "\n", inner)
        return inner

    return re.sub(
        r"\$\$\s*\n\\begin\{aligned\}.*?\\end\{aligned\}\s*\n\$\$",
        fix_block,
        text,
        flags=re.DOTALL,
    )


def fix_kets_in_table_cells(text: str) -> str:
    """Use \\lvert in inline math inside tables so | is not parsed as a column delimiter."""
    lines = []
    for line in text.splitlines():
        if line.strip().startswith("|") and not re.match(r"^\|\s*[-:]+", line):
            line = line.replace("$|", r"$\lvert ")
            line = line.replace(r"\alpha_x|x\rangle", r"\alpha_x\lvert x\rangle")
            line = line.replace(r"\sum_x|\alpha_x|", r"\sum_x\lvert\alpha_x\rvert")
            line = line.replace(r"P(x)=|\alpha_x|", r"P(x)=\lvert\alpha_x\rvert")
        lines.append(line)
    return "\n".join(lines)


def use_explicit_magnitude_bars(text: str) -> str:
    """Use \\lvert\\cdot\\rvert for complex magnitudes (do not alter ket |\\psi\\rangle)."""
    lines = []
    for line in text.splitlines():
        if re.match(r"^\|z\|", line.strip()):
            line = line.replace("|z|", r"\lvert z\rvert")
        if "P=|\\alpha|^2" in line:
            line = line.replace("P=|\\alpha|^2", r"P=\lvert\alpha\rvert^2")
        lines.append(line)
    return "\n".join(lines)


def wrap_bare_display_lines(text: str) -> str:
    """Wrap known bare one-line formulas that lost their $$ fences."""
    bare_patterns = [
        r"^z=a\+bi\s*$",
        r"^f\(\d+\)\+f\(\d+\)\+f\(\d+\)\+f\(\d+\)\s*$",
    ]
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped == "$$":
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and any(re.match(p, stripped) for p in bare_patterns):
            out.append("$$")
            out.append(stripped)
            out.append("$$")
            continue
        out.append(line)
    return "\n".join(out)


def ensure_paragraph_breaks(text: str) -> str:
    """Blank line before lists / headers when missing (helps Markdown + math)."""
    text = re.sub(r"([^\n])\n(- \$\S)", r"\1\n\n\2", text)
    text = re.sub(r"([^\n])\n(\d+\. \*\*)", r"\1\n\n\2", text)
    text = re.sub(r"(For example:)\n(\$\$)", r"\1\n\n\2", text)
    text = re.sub(r"(Therefore:)\n(\$\$)", r"\1\n\n\2", text)
    text = re.sub(r"(Consider:)\n(\$\$)", r"\1\n\n\2", text)
    text = re.sub(r"(Expand it:)\n(\$\$)", r"\1\n\n\2", text)
    text = re.sub(r"(^In$)\n(\$\$)", r"\1\n\n\2", text, flags=re.M)
    return text


def validate_fences(notes: str) -> list[str]:
    errors: list[str] = []
    lines = notes.splitlines()
    in_display = False
    for i, line in enumerate(lines, 1):
        if line.strip() == "$$":
            in_display = not in_display
    if in_display:
        errors.append("Unclosed $$ display block at end of notes")
    return errors


def main() -> None:
    full = PATH.read_text(encoding="utf-8")
    if QUIZ_MARKER in full:
        notes, quiz_tail = full.split(QUIZ_MARKER, 1)
        notes = notes.rstrip() + "\n\n"
        quiz_tail = QUIZ_MARKER + quiz_tail
    else:
        notes, quiz_tail = full, ""

    notes = collapse_empty_display_fences(notes)
    notes = strip_fences_inside_aligned(notes)
    notes = fix_kets_in_table_cells(notes)
    notes = use_explicit_magnitude_bars(notes)
    notes = wrap_bare_display_lines(notes)
    notes = collapse_empty_display_fences(notes)
    notes = ensure_paragraph_breaks(notes)

    notes = re.sub(r"---# Self-assessment", "---\n\n# Self-assessment", notes)

    errs = validate_fences(notes)
    if errs:
        raise RuntimeError(errs)

    PATH.write_text(notes + quiz_tail, encoding="utf-8")
    print("fixed", PATH)


if __name__ == "__main__":
    main()