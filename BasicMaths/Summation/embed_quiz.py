"""Embed the quiz into Summation_Basics.md as an iframe srcdoc block."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

DIR = Path(__file__).parent
MD = DIR / "Summation_Basics.md"
QUIZ = DIR / "summation_quantum_quiz.html"

QUIZ_SECTION = '''# Self-assessment quiz

The quiz is **embedded below** in this document. Scroll down, answer the questions, then click **Check answers**.

> **Cursor / VS Code preview:** If the frame looks empty, use **Markdown: Open Preview to the Side** (`Ctrl+K V`). Some previews block embedded pages; open `Summation_Basics.html` in a browser for the full notes + quiz in one page.

<div class="summation-quiz-embed">
<iframe
  title="Summation and quantum states quiz"
  style="width:100%;min-height:1400px;border:1px solid #dce3ed;border-radius:12px;background:#f5f7fb;"
  loading="lazy"
  srcdoc="{srcdoc}">
</iframe>
</div>
'''


def main() -> None:
    quiz_html = QUIZ.read_text(encoding="utf-8").strip()
    srcdoc = html.escape(quiz_html, quote=True)
    section = QUIZ_SECTION.format(srcdoc=srcdoc)

    text = MD.read_text(encoding="utf-8")
    text = re.sub(
        r"# Self-assessment quiz\r?\n.*?(?=\r?\n---\r?\n\r?\n## Suggested way)",
        section + "\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace(
        "4. Open `summation_quantum_quiz.html` in a browser after studying all seven lessons.",
        "4. Complete the **embedded quiz** at the end of this document (or open `Summation_Basics.html` in a browser).",
    )
    MD.write_text(text, encoding="utf-8")

    build_combined_html(DIR, text, quiz_html)
    print("embedded quiz in", MD)
    print("wrote", DIR / "Summation_Basics.html")


def build_combined_html(directory: Path, md_text: str, quiz_html: str) -> None:
    """Single browser page: notes (pre-rendered shell) + embedded quiz."""
    notes_md = re.split(r"\r?\n# Self-assessment quiz\r?\n", md_text, maxsplit=1)[0].strip()
    notes_json = json.dumps(notes_md)
    quiz_escaped = html.escape(quiz_html, quote=True)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Summation Basics for Quantum Computing</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
  body {{
    font-family: Georgia, "Times New Roman", serif;
    line-height: 1.65;
    max-width: 920px;
    margin: 0 auto;
    padding: 24px 20px 48px;
    color: #1a1a1a;
    background: #fafafa;
  }}
  #notes h1, #notes h2, #notes h3 {{ color: #183b66; }}
  #notes table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
  #notes th, #notes td {{ border: 1px solid #ccd3de; padding: 8px 10px; }}
  #notes th {{ background: #eef2f7; }}
  #notes code {{ background: #eef2f7; padding: 2px 5px; border-radius: 4px; }}
  .quiz-frame {{
    width: 100%;
    min-height: 1400px;
    border: 1px solid #dce3ed;
    border-radius: 12px;
    margin-top: 24px;
    background: #f5f7fb;
  }}
  hr {{ border: 0; border-top: 1px solid #dce3ed; margin: 2.5rem 0; }}
</style>
</head>
<body>
<div id="notes"></div>
<hr>
<h2 style="color:#183b66;">Self-assessment quiz</h2>
<iframe class="quiz-frame" title="Quiz" srcdoc="{quiz_escaped}"></iframe>
<script>
marked.setOptions({{ breaks: true, gfm: true }});
const md = {notes_json};
document.getElementById("notes").innerHTML = marked.parse(md);
if (typeof renderMathInElement === "function") {{
  renderMathInElement(document.getElementById("notes"), {{
    delimiters: [
      {{ left: "$$", right: "$$", display: true }},
      {{ left: "$", right: "$", display: false }}
    ],
    throwOnError: false
  }});
}}
</script>
</body>
</html>
"""
    (directory / "Summation_Basics.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()