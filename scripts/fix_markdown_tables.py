"""Fix markdown table cells: bare | in kets/bra breaks column parsing."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def is_table_separator(line: str) -> bool:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return False
    inner = s[1:-1]
    return bool(re.fullmatch(r"[\s\-:|]+", inner))


def is_table_row(line: str) -> bool:
    s = line.strip()
    if not s.startswith("|"):
        return False
    if is_table_separator(s):
        return False
    return s.count("|") >= 2


def fix_dirac_pipes(body: str) -> str:
    """Use \\lvert/\\rvert so | is not a table delimiter."""
    # Repeat until stable (multiple kets in one expression).
    for _ in range(32):
        new = re.sub(r"\|([^|]+?)\\rangle", r"\\lvert \1\\rangle", body)
        if new == body:
            break
        body = new
    body = re.sub(r"\\langle\s+([^|\\]+?)\|", r"\\langle \1\\rvert ", body)
    return body


def fix_inline_math(body: str) -> str:
    body = fix_dirac_pipes(body)
    return f"${body}$"


def fix_table_line(line: str) -> str:
    fixed = line

    # \( ... \) → $...$ with safe dirac symbols
    fixed = re.sub(
        r"\\\(((?:[^\\]|\\.)*?)\\\)",
        lambda m: fix_inline_math(m.group(1)),
        fixed,
    )

    # Each $...$ segment in the row
    def fix_dollar_seg(m: re.Match[str]) -> str:
        return "$" + fix_dirac_pipes(m.group(1)) + "$"

    fixed = re.sub(r"\$([^$]+)\$", fix_dollar_seg, fixed)

    return fixed


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    changed = False
    for line in lines:
        if is_table_row(line):
            new_line = fix_table_line(line)
            if new_line != line:
                changed = True
            out.append(new_line)
        else:
            out.append(line)
    if changed:
        path.write_text("".join(out), encoding="utf-8")
    return changed


def main() -> None:
    count = 0
    for path in sorted(ROOT.rglob("*.md")):
        if "scripts" in path.parts:
            continue
        if fix_file(path):
            count += 1
            print(path.relative_to(ROOT))
    print(f"Fixed {count} files")


if __name__ == "__main__":
    main()