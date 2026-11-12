from pathlib import Path
import re

p = Path("Study_Notes.md")
text = p.read_text(encoding="utf-8")

text = re.sub(
    r"\n\*\*How to read this file\.\*\*[^\n]+\n\n"
    r"\| If you're revising… \| Read… \|\n"
    r"\| --- \| --- \|\n"
    r"(?:\|[^\n]+\n)+",
    "\n\n**Open the notes.** Keep the `assets` folder next to this file. "
    "Use [Study_Notes.html](Study_Notes.html) in a browser for the navigation sidebar.\n\n",
    text,
    count=1,
)
text = text.replace("**Notation card (bookmark this).**", "**Notation card.**")
text = re.sub(r"\n### What to expect\n\nSections[^\n]+\n\n", "\n", text)
text = re.sub(
    r"\n### Plain-language map\n\n\| Classroom picture.*?\n\n",
    "\n",
    text,
    flags=re.S,
)
text = re.sub(r"\n### What comes next\n\n[^\n]+\n\n", "\n", text)
text = re.sub(r"^[^\n]*\*\*Key takeaway\.\*\*[^\n]*\n+", "", text, flags=re.M)

pat = re.compile(r"^### \d+\.\d+[^\n]*\n(?:(?!^### |^## ).*\n)*", re.M)
text = pat.sub("", text)

text = re.sub(r"\n### Memorize this pair\n\n[^\n]+\n\n", "\n", text)
text = re.sub(r"\n---\n\n\n## Appendix A\..*?(?=\n\*Sources\.)", "\n\n", text, flags=re.S)
text = re.sub(r"\n---\n\n\*Sources\.", "\n\n*Sources.", text)
text = re.sub(r"\n---\n(?=\n## )", "\n", text)
text = re.sub(r"\n{4,}", "\n\n\n", text)
text = re.sub(r"^\*Slides?[^\n]*\.\*\n+", "", text, flags=re.M)
text = re.sub(
    r"\nUse this table when translating homework diagrams to algebra\.\n\n",
    "\n",
    text,
)
text = text.replace(
    "These follow slide 36. Attempt each with kets before matrices.",
    "Attempt each with kets before matrices.",
)

p.write_text(text, encoding="utf-8")
print("lines:", len(text.splitlines()))
