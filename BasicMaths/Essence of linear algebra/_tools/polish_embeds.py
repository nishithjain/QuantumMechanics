import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

for md in ROOT.glob("**/notes/lecture-notes.md"):
    text = md.read_text(encoding="utf-8")
    orig = text
    text = text.replace("<p>**Interactive:**", "<p><strong>Interactive:</strong>")
    text = re.sub(r'title="▶ Open ', 'title="', text)
    text = re.sub(r">Open ▶ Open ", ">Open ", text)
    text = re.sub(
        r'(<p><strong>Interactive:</strong> )▶ ',
        r"\1",
        text,
    )
    if text != orig:
        md.write_text(text, encoding="utf-8")
        print("Polished:", md.relative_to(ROOT))