"""Convert ../animations/*.html markdown links to iframe embeds in lecture-notes.md."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[([^\]]+)\]\((\.\./animations/[^)]+\.html)\)")

IFRAME_STYLE = "max-width:980px;border:1px solid #dce4ef;border-radius:12px;background:#f3f6fb;"
DEFAULT_HEIGHT = "820"


def embed_block(url: str, title: str, intro: str = "") -> str:
    parts = []
    if intro.strip():
        parts.append(intro.strip())
        parts.append("")
    parts.extend(
        [
            "<iframe",
            f'  src="{url}"',
            f'  title="{title}"',
            '  width="100%"',
            f'  height="{DEFAULT_HEIGHT}"',
            f'  style="{IFRAME_STYLE}"',
            '  loading="lazy">',
            "</iframe>",
            "",
            f'<p><a href="{url}">Open {title} in full tab</a> if the embed does not load.</p>',
        ]
    )
    return "\n".join(parts)


def process_line(line: str, seen: dict) -> str:
    if "<iframe" in line or 'src="../animations/' in line:
        return line
    if "../animations/" not in line:
        return line

    matches = list(LINK_RE.finditer(line))
    if not matches:
        return line

    if len(matches) > 1:
        return LINK_RE.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', line)

    m = matches[0]
    title, url = m.group(1), m.group(2)
    stripped = line.strip()
    rest = (stripped[: m.start()] + stripped[m.end() :]).strip()
    rest = re.sub(r"^\*\*Interactive:\*\*\s*", "", rest)
    rest = re.sub(r"^▶\s*", "", rest)
    rest = rest.strip(" .*")

    prefix = line[: m.start()].strip()
    suffix = line[m.end() :]
    desc = suffix.lstrip(". ").strip()

    if url in seen:
        extra = desc if desc and not desc.startswith("(") else title
        return (
            f'<p><em>Interactive:</em> {extra} '
            f'<a href="{url}">Open in full tab</a> (embedded above).</p>'
        )

    seen[url] = True

    if not rest or rest in ("**", "*"):
        intro = f"<p><strong>Interactive:</strong> {title}</p>"
        return embed_block(url, title, intro)

    intro_text = ""
    if prefix:
        intro_text = prefix
    if desc:
        if intro_text:
            intro_text = intro_text.rstrip(":") + ". " + desc if intro_text.endswith(":") else intro_text + " " + desc
        else:
            intro_text = desc
    if not intro_text:
        intro_text = title
    intro = f"<p>{intro_text}</p>"
    return embed_block(url, title, intro)


def normalize_existing_determinant_block(text: str) -> str:
    """Align section 5 wording with the standard fallback line."""
    old = (
        "<p>If the embed does not load in your viewer, open\n"
        '<a href="../animations/animation-06-determinant-meaning.html">Animation 06 — What the determinant tells us</a>\n'
        "in a new tab.</p>"
    )
    new = (
        '<p><a href="../animations/animation-06-determinant-meaning.html">'
        "Open Animation 06 — What the determinant tells us in full tab</a> if the embed does not load.</p>"
    )
    return text.replace(old, new)


def process_file(md: Path) -> bool:
    text = md.read_text(encoding="utf-8")
    seen: dict = {}
    new_lines = [process_line(line, seen) for line in text.splitlines()]
    new_text = "\n".join(new_lines)
    if text.endswith("\n"):
        new_text += "\n"
    new_text = normalize_existing_determinant_block(new_text)
    if new_text != text:
        md.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    for md in sorted(ROOT.glob("**/notes/lecture-notes.md")):
        if process_file(md):
            print("Updated:", md.relative_to(ROOT))
        else:
            print("No change:", md.relative_to(ROOT))


if __name__ == "__main__":
    main()