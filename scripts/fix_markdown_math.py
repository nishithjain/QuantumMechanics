"""Fix inline math matrices: Markdown eats one backslash before KaTeX.

In inline $...$ / \\(...\\), LaTeX row breaks need four backslashes in the
source (\\\\) so two survive to KaTeX. Also map \\(...\\) to $...$ for GFM.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MY_NOTES = ROOT / "MyNotes" / "MarkdownNotes"

MATRIX_ENV = re.compile(
    r"\\begin\{(bmatrix|pmatrix|matrix|vmatrix|Vmatrix|smallmatrix)\}"
    r"(.*?)"
    r"\\end\{\1\}",
    re.DOTALL,
)


def _double_matrix_row_seps(inner: str) -> str:
    """Turn LaTeX \\ row breaks into \\\\ for inline markdown math."""
    # Already quadrupled row breaks — idempotent re-runs.
    if re.search(r" \\\\\\\\ ", inner):
        return inner

    def repl_space(m: re.Match[str]) -> str:
        return " " + "\\\\" * 2 + " "

    inner = re.sub(r" \\\\ ", repl_space, inner)
    inner = re.sub(r" \\\\(\s*\\end\{)", r"\\\\\\\\\1", inner)
    return inner


def _fix_matrices_in_chunk(chunk: str) -> str:
    def repl(m: re.Match[str]) -> str:
        name, body = m.group(1), m.group(2)
        body = _double_matrix_row_seps(body)
        return rf"\begin{{{name}}}{body}\end{{{name}}}"

    return MATRIX_ENV.sub(repl, chunk)


def _convert_paren_math(chunk: str) -> str:
    """\\( ... \\) -> $ ... $ (GFM / VS Code math)."""

    def repl(m: re.Match[str]) -> str:
        return f"${m.group(1).strip()}$"

    return re.sub(
        r"\\\(([\s\S]*?)\\\)",
        repl,
        chunk,
    )


def fix_text(text: str) -> str:
    parts = re.split(r"(\$\$[\s\S]*?\$\$)", text)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Display math: keep single \\ inside matrices
            out.append(part)
        else:
            part = _convert_paren_math(part)
            part = _fix_matrices_in_chunk(part)
            out.append(part)
    return "".join(out)


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new = fix_text(text)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    import sys

    if "--all" in sys.argv:
        targets = sorted(p for p in ROOT.rglob("*.md") if "scripts" not in p.parts)
        label = "repository"
    else:
        targets = sorted(MY_NOTES.rglob("*.md"))
        label = "MyNotes/MarkdownNotes"

    count = 0
    for path in targets:
        if fix_file(path):
            count += 1
            print(path.relative_to(ROOT))
    print(f"Fixed {count} files in {label}")


if __name__ == "__main__":
    main()