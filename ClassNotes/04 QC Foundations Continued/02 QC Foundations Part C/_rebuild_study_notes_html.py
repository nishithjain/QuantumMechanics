#!/usr/bin/env python3
"""Rebuild Study_Notes.html body and TOC from Study_Notes.md (QC Foundations Part C)."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT / "Study_Notes.md"
HTML = ROOT / "Study_Notes.html"
FRAG = ROOT / "_full_frag.html"
ROOT_H1 = "qc-foundations-part-c"


def strip_tags(s: str) -> str:
    s = re.sub(r"<math[^>]*>.*?</math>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def parse_heading_tree(body_html: str) -> list[tuple[int, str, str]]:
    out: list[tuple[int, str, str]] = []
    for m in re.finditer(
        r"<h([234])\s+id=\"([^\"]+)\"[^>]*>(.*?)</h\1>",
        body_html,
        re.S,
    ):
        out.append((int(m.group(1)), strip_tags(m.group(3)), m.group(2)))
    return out


def build_toc(headings: list[tuple[int, str, str]]) -> str:
    lines = [
        '<nav aria-label="Contents"><details open><summary>In this lecture</summary>',
        "<ul>",
        f'<li><a href="#{ROOT_H1}" id="toc-{ROOT_H1}">QC Foundations Part C</a>',
        "<ul>",
    ]
    i = 0
    while i < len(headings):
        level, title, hid = headings[i]
        if level != 2:
            i += 1
            continue
        lines.append(f'<li><a href="#{hid}" id="toc-{hid}">{title}</a>')
        sub: list[str] = []
        j = i + 1
        while j < len(headings) and headings[j][0] > 2:
            lv, st, sl = headings[j]
            if lv == 3 and re.match(r"^\d+\.", st):
                sub.append(f'<li><a href="#{sl}">{st}</a></li>')
            j += 1
        if sub:
            lines.append("<ul>")
            lines.extend(sub)
            lines.append("</ul>")
        lines.append("</li>")
        i += 1
    lines.extend(["</ul>", "</li>", "</ul>", "</details></nav>"])
    return "\n".join(lines)


def main() -> None:
    subprocess.run(
        ["pandoc", str(MD), "-f", "markdown", "-t", "html", "--mathml", "-o", str(FRAG)],
        check=True,
    )
    frag = FRAG.read_text(encoding="utf-8")
    m = re.search(r"<body[^>]*>(.*)</body>", frag, re.S)
    body_inner = m.group(1).strip() if m else frag.strip()
    headings = parse_heading_tree(body_inner)
    html = HTML.read_text(encoding="utf-8")
    nav = build_toc(headings)
    nav_m = re.search(r"<nav aria-label=\"Contents\">.*?</nav>", html, re.S)
    if not nav_m:
        raise SystemExit("nav block not found")
    html = html[: nav_m.start()] + nav + html[nav_m.end() :]
    extra_css = """
  h1, h2, h3, h4 { line-height: 1.18; letter-spacing: -.035em; }
  h3 { font-size: 1.12rem; margin: 1.45rem 0 .6rem; color: #1b3873; font-weight: 700; }
  h4 { font-size: 1.02rem; margin: 1.15rem 0 .5rem; color: #2a4a7a; font-weight: 650; }
  .demo-frame { margin: 1.2rem 0 1.5rem; }
  .demo-frame iframe { width: 100%; min-height: 320px; background: #f6f8fc; border: 1px solid #dce3ef; border-radius: 12px; }
  .example-box {
    margin: 1rem 0 1.35rem; padding: 1.05rem 1.2rem;
    background: #f0f4fc; border: 1px solid #dce3ef; border-radius: 12px;
    border-left: 4px solid #2455c8;
  }
  nav ul ul ul { margin-left: .65rem; font-size: .8rem; }
"""
    if "h3 {" not in html or ".demo-frame" not in html:
        html = html.replace(
            "  h1, h2, h3 { line-height: 1.18; letter-spacing: -.035em; }",
            extra_css.strip(),
        )
    start = html.find('<main id="notes">')
    end = html.find("</main>", start)
    html = html[: start + len('<main id="notes">')] + "\n" + body_inner + "\n" + html[end:]
    HTML.write_text(html, encoding="utf-8")
    FRAG.unlink(missing_ok=True)
    print(f"Wrote {HTML}")


if __name__ == "__main__":
    main()
