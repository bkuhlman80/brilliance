#!/usr/bin/env python3
"""Turn a sequenced chapter .md into an EPUB tuned for ElevenReader TTS.

Lives in theory/chapters/ and writes to theory/chapters/epubs/ by default.

Every run bumps the source version -- ch_0_v3_2.md is renamed to ch_0_v3_3.md
and built as ch_0_v3_3.epub, and the superseded ch_0_v3_2.epub is removed.
Pass --no-bump to build in place.

Usage:
    python3 theory/chapters/md2epub.py theory/chapters/sequenced/ch_1_v3_5.md
    python3 theory/chapters/md2epub.py theory/chapters/sequenced/ch_*.md
    python3 theory/chapters/md2epub.py <chapter>.md -o ~/Desktop/protocell.epub
    python3 theory/chapters/md2epub.py <chapter>.md --dry-run  # the spoken text

What it does:
  * strips the <!--[2.a]--> structure tags (and any other HTML comment)
  * rewrites punctuation that TTS engines read badly (em dashes above all)
  * turns *asterisk* emphasis into real <em>/<strong> so no asterisk is spoken
  * splits at each `# ` heading into its own XHTML doc so chapter nav works
  * writes EPUB 3 with both nav.xhtml and a toc.ncx fallback

No third-party dependencies.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import os
import re
import sys
import unicodedata
import uuid
import zipfile

# A stable namespace so rebuilding the same source yields the same book id,
# which keeps readers from shelving the same chapter twice.
_NS = uuid.UUID("6f9d1f6e-1f2a-5a4b-9c3d-7e8f0a1b2c3d")

DASH_MODES = ("comma", "ellipsis", "space", "keep")
BRACKET_MODES = ("spoken", "commas", "keep")

# Anchored to this file, not the shell's cwd, so the books land in the same
# place no matter where the script is run from.
DEFAULT_OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "epubs")


# --------------------------------------------------------------------------
# text normalization
# --------------------------------------------------------------------------

def strip_comments(text: str) -> str:
    """Remove <!-- ... --> tags, including runs like <!--[2]--><!--[2.a]-->."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    # Lines that held nothing but tags are now blank; don't let them pile up.
    text = re.sub(r"[ \t]+$", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def normalize_dashes(text: str, mode: str) -> str:
    """Rewrite em/en dashes into something a TTS voice phrases correctly.

    ElevenLabs voices treat an em dash inconsistently -- sometimes a pause,
    sometimes nothing, occasionally a stumble. A comma is unambiguous in every
    engine, so that is the default. Rules run in order; earlier ones win.
    """
    if mode == "keep":
        return text

    # An en dash joining two words is a compound (Regulator-Reviser), not a pause.
    text = re.sub(r"(?<=\w)[ \t]*–[ \t]*(?=\w)", "-", text)

    replacement = {"comma": ", ", "ellipsis": " ... ", "space": " "}[mode]

    # A dash butted straight against a quote or an emphasis marker is an
    # interruption mark, not a pause -- the speaker is cut off or picking back
    # up. Requiring no space is what separates `It comes—"` (cut off) from
    # `he said — "and that's` (a real pause before the next quote).
    #
    # Speech cut off and narration picking straight up: `don't you—* urging a
    # thing`. Move the beat outside the marker rather than dropping it, or the
    # quote runs into the narration as one breath.
    text = re.sub(r"[ \t]*—([\"']|\*{1,3})[ \t]+(?=\S)", r"\1" + replacement, text)
    # Speech cut off at the end of a line: `It comes—"`.
    text = re.sub(r"[ \t]*—(?=[\"'*])", "", text)
    # Dash left dangling at the end of a paragraph: the break is pause enough.
    text = re.sub(r"[ \t]*—[ \t]*$", "", text, flags=re.M)
    # Signature lines: `— Bartholomew`.
    text = re.sub(r"^[ \t]*—[ \t]*", "", text, flags=re.M)
    # Speech resuming: `"— everything to its mark`, `*—there — there you`.
    # The quote or marker opens here (line start or preceded by a space).
    text = re.sub(r"(^|[ \t])([\"']|\*{1,3})—[ \t]*", r"\1\2", text, flags=re.M)
    # A closing quote or marker followed by narration: `and"—flat, to the table`.
    text = re.sub(r"(\w(?:[\"']|\*{1,3}))—[ \t]*", r"\1" + replacement, text)
    # Already punctuated on the left: don't stack a second comma on it.
    text = re.sub(r"([,;:.!?])[ \t]*—[ \t]*", r"\1 ", text)
    # Everything else.
    text = re.sub(r"[ \t]*—[ \t]*", replacement, text)
    # Any surviving en dash.
    text = re.sub(r"[ \t]*–[ \t]*", replacement, text)
    return text


OPEN_BRACKET = "OPEN-BRACKET"
CLOSE_BRACKET = "END-BRACKET"
CLOSE_BRACKETS = "END-BRACKETS"


def normalize_screen_notation(text: str, mode: str) -> str:
    """Make the screen-log notation speakable.

    `MIRA { WANTING [ TAKE VENT ] }` becomes, in `spoken` mode,
    `MIRA, OPEN-BRACKET, WANTING, OPEN-BRACKET, TAKE VENT, END-BRACKETS` -- the
    voice names the delimiters so the listener can hear the nesting instead of
    losing it. A run of closers collapses to one plural `END-BRACKETS` rather
    than stacking, which is what the notation sounds like when read aloud.

    `commas` drops the delimiters for a plain `MIRA, WANTING, TAKE VENT`. Braces
    and brackets are spoken identically: the shape of the nesting survives, the
    brace-vs-bracket distinction does not.

    The notation appears both inside backticks and bare in the prose, so both
    are handled the same way.
    """
    text = re.sub(r"`([^`\n]*)`", r"\1", text)  # inline code fences
    if mode == "keep":
        return text
    if mode == "commas":
        return re.sub(r"[{}\[\]]", ",", text)

    def close(m):
        n = len(re.findall(r"[}\]]", m.group(0)))
        return ", " + (CLOSE_BRACKETS if n > 1 else CLOSE_BRACKET)

    # Closers first, so a run like `] }` is counted before the openers move.
    text = re.sub(r"(?:[ \t]*[}\]])+", close, text)
    text = re.sub(r"[ \t]*[{\[][ \t]*", f", {OPEN_BRACKET}, ", text)
    return text


def tidy_commas(text: str) -> str:
    """Clean up the comma runs the dash and bracket rules can leave behind.

    Deliberately narrow: a comma already sitting correctly between two words --
    or inside an emphasis span like `*warm,*` -- must come out untouched, since
    that comma is doing the phrasing work the voice depends on.
    """
    text = re.sub(r"(?:[ \t]*,){2,}[ \t]*", ", ", text)   # `, ,` -> `,`
    text = re.sub(r"[ \t]+,(?=[ \t])", ",", text)          # ` , ` -> `, `
    text = re.sub(r"[ \t]*,[ \t]*(?=[.;:!?])", "", text)   # `, .` -> `.`
    text = re.sub(r"[ \t]*,[ \t]*(?=\))", "", text)        # `, )` -> `)`
    text = re.sub(r"[ \t]*,[ \t]*$", "", text, flags=re.M)  # trailing
    text = re.sub(r"^[ \t]*,[ \t]*", "", text, flags=re.M)  # leading
    return text


def normalize_text(text: str, dash_mode: str, bracket_mode: str = "spoken") -> str:
    """Fold the source down to characters a TTS engine reads cleanly."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = unicodedata.normalize("NFC", text)

    # Invisible characters that some engines vocalize as a glitch or a gap.
    for junk in ("﻿", "​", "‌", "‍", "⁠", "­"):
        text = text.replace(junk, "")
    # Exotic spaces -> plain space.
    text = re.sub(r"[       ]", " ", text)

    # Typographic quotes -> straight. Voices handle both, but straight quotes
    # keep the XHTML diffable and avoid mojibake on re-encode.
    text = text.translate(str.maketrans({
        "‘": "'", "’": "'", "‚": "'", "‛": "'",
        "“": '"', "”": '"', "„": '"', "‟": '"',
        "′": "'", "″": '"',
        "‐": "-", "‑": "-", "‒": "-", "―": "-",
        "…": "...",
    }))

    text = normalize_dashes(text, dash_mode)

    # Protect the horizontal rules before commas start moving around.
    rules = []

    def stash(m):
        rules.append(m.group(0))
        return f"\x00HR{len(rules) - 1}\x00"

    text = re.sub(r"^[ \t]*(?:[-*_][ \t]*){3,}$", stash, text, flags=re.M)

    text = normalize_screen_notation(text, bracket_mode)
    text = tidy_commas(text)

    for i, rule in enumerate(rules):
        text = text.replace(f"\x00HR{i}\x00", rule)

    # Symbols that get read as their literal name, or not at all.
    text = text.replace("&", " and ")
    text = re.sub(r"(?<=\S)[ \t]{2,}", " ", text)
    text = re.sub(r"[ \t]+$", "", text, flags=re.M)
    return text


def normalize_heading(text: str) -> str:
    """`Ch 1: Protocell` is spoken as "Ch"; say "Chapter" instead."""
    return re.sub(r"^Ch(?:\.|apter)?[ \t]+(\d+)\b", r"Chapter \1", text)


# --------------------------------------------------------------------------
# markdown -> blocks
# --------------------------------------------------------------------------

RE_HEADING = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*#*$")
RE_HR = re.compile(r"^[ \t]*(?:-[ \t]*){3,}$|^[ \t]*(?:\*[ \t]*){3,}$|^[ \t]*(?:_[ \t]*){3,}$")
RE_UL = re.compile(r"^[ \t]*[-+*][ \t]+(.*)$")
RE_OL = re.compile(r"^[ \t]*\d+[.)][ \t]+(.*)$")


def parse_blocks(text: str):
    """Return a flat list of ('h', level, text) / ('p', text) / ('hr',) /
    ('ul'|'ol', [items]) tuples."""
    lines = text.split("\n")
    blocks = []
    para: list[str] = []
    items: list[str] = []
    list_kind = None

    def flush_para():
        nonlocal para
        if para:
            blocks.append(("p", " ".join(para)))
            para = []

    def flush_list():
        nonlocal items, list_kind
        if items:
            blocks.append((list_kind, items))
            items = []
        list_kind = None

    for line in lines:
        if not line.strip():
            flush_para()
            flush_list()
            continue

        m = RE_HEADING.match(line)
        if m:
            flush_para()
            flush_list()
            blocks.append(("h", len(m.group(1)), normalize_heading(m.group(2).strip())))
            continue

        # An HR test must precede the list test: `---` also matches a bullet.
        if RE_HR.match(line):
            flush_para()
            flush_list()
            blocks.append(("hr",))
            continue

        m = RE_UL.match(line)
        if m:
            flush_para()
            if list_kind and list_kind != "ul":
                flush_list()
            list_kind = "ul"
            items.append(m.group(1).strip())
            continue

        m = RE_OL.match(line)
        if m:
            flush_para()
            if list_kind and list_kind != "ol":
                flush_list()
            list_kind = "ol"
            items.append(m.group(1).strip())
            continue

        flush_list()
        para.append(line.strip())

    flush_para()
    flush_list()
    return blocks


def inline(text: str) -> str:
    """Escape for XML, then turn asterisk emphasis into real tags.

    Escaping first means the emphasis tags we emit are the only markup in the
    result, so nothing user-supplied can inject an element.
    """
    out = html.escape(text, quote=False)
    out = re.sub(r"\*\*\*(?=\S)(.+?)(?<=\S)\*\*\*", r"<strong><em>\1</em></strong>", out)
    out = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\*(?=\S)(.+?)(?<=\S)\*", r"<em>\1</em>", out)
    out = out.replace("*", "")  # any unmatched marker would be read aloud
    return out


def plain(text: str) -> str:
    """Same as inline() but yielding what the voice actually says."""
    return re.sub(r"\*+", "", text)


# --------------------------------------------------------------------------
# sections
# --------------------------------------------------------------------------

class Section:
    def __init__(self, title: str, index: int):
        self.title = title
        self.index = index
        self.blocks: list = []
        self.subs: list[tuple[str, str]] = []  # (anchor, title)

    @property
    def href(self) -> str:
        return f"text/s{self.index:03d}.xhtml"


def split_sections(blocks, fallback_title: str) -> list[Section]:
    """One section per `# ` heading; anything before the first one leads."""
    sections: list[Section] = []
    current: Section | None = None
    sub_n = 0

    for block in blocks:
        if block[0] == "h" and block[1] == 1:
            current = Section(block[2], len(sections) + 1)
            sections.append(current)
            sub_n = 0
            continue
        if current is None:
            current = Section(fallback_title, 1)
            sections.append(current)
        if block[0] == "h" and block[1] == 2:
            sub_n += 1
            anchor = f"sec{sub_n}"
            current.subs.append((anchor, block[2]))
            current.blocks.append(("h", 2, block[2], anchor))
            continue
        current.blocks.append(block)

    if not sections:
        sections.append(Section(fallback_title, 1))
    return sections


def strip_byline(sections: list[Section]) -> None:
    """Drop a leading `*Author. draft. Month Year.*` line from each section."""
    pattern = re.compile(r"^\*.*\bdraft\b.*\*$", re.I)
    for sec in sections:
        if sec.blocks and sec.blocks[0][0] == "p" and pattern.match(sec.blocks[0][1].strip()):
            sec.blocks.pop(0)


def trim_rules(sections: list[Section]) -> None:
    """A scene break butted against a heading or the end of a section is noise."""
    for sec in sections:
        while sec.blocks and sec.blocks[0][0] == "hr":
            sec.blocks.pop(0)
        while sec.blocks and sec.blocks[-1][0] == "hr":
            sec.blocks.pop()
        trimmed = []
        for block in sec.blocks:
            if block[0] == "hr" and trimmed and trimmed[-1][0] == "h":
                continue
            if block[0] == "h" and trimmed and trimmed[-1][0] == "hr":
                trimmed.pop()
            trimmed.append(block)
        sec.blocks = trimmed


# --------------------------------------------------------------------------
# rendering
# --------------------------------------------------------------------------

def render_body(section: Section) -> str:
    out = [f"    <h1>{inline(section.title)}</h1>"]
    for block in section.blocks:
        kind = block[0]
        if kind == "h":
            level = min(block[1], 6)
            anchor = f' id="{block[3]}"' if len(block) > 3 else ""
            out.append(f"    <h{level}{anchor}>{inline(block[2])}</h{level}>")
        elif kind == "p":
            out.append(f"    <p>{inline(block[1])}</p>")
        elif kind == "hr":
            out.append('    <hr class="scene" />')
        elif kind in ("ul", "ol"):
            out.append(f"    <{kind}>")
            for item in block[1]:
                out.append(f"      <li>{inline(item)}</li>")
            out.append(f"    </{kind}>")
    return "\n".join(out)


def spoken_words(sections: list[Section]) -> int:
    """Count the words a voice actually utters -- headings and list items
    included, scene-break rules excluded."""
    n = 0
    for section in sections:
        n += len(plain(section.title).split())
        for block in section.blocks:
            if block[0] == "h":
                n += len(plain(block[2]).split())
            elif block[0] == "p":
                n += len(plain(block[1]).split())
            elif block[0] in ("ul", "ol"):
                n += sum(len(plain(item).split()) for item in block[1])
    return n


def render_plain(sections: list[Section]) -> str:
    """What ElevenReader will speak, as close as this script can tell."""
    out = []
    for section in sections:
        out.append(plain(section.title))
        out.append("")
        for block in section.blocks:
            kind = block[0]
            if kind == "h":
                out += [plain(block[2]), ""]
            elif kind == "p":
                out += [plain(block[1]), ""]
            elif kind == "hr":
                out += ["* * *", ""]
            elif kind in ("ul", "ol"):
                out += [plain(item) for item in block[1]]
                out.append("")
    return "\n".join(out).strip() + "\n"


CSS = """\
html, body { margin: 0; padding: 0; }
body { font-family: serif; line-height: 1.5; padding: 0 1em; }
h1, h2, h3 { font-weight: bold; line-height: 1.25; text-align: left;
             margin: 1.4em 0 0.6em; page-break-after: avoid; }
h1 { font-size: 1.5em; margin-top: 0; }
h2 { font-size: 1.2em; }
h3 { font-size: 1.05em; }
p { margin: 0 0 0.85em; text-indent: 0; }
ul, ol { margin: 0 0 0.85em 1.4em; padding: 0; }
li { margin: 0 0 0.4em; }
hr.scene { border: 0; height: 1.6em; margin: 0.6em 0; }
em { font-style: italic; }
strong { font-weight: bold; }
"""

XHTML = """\
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
  <head>
    <meta charset="utf-8" />
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="../style.css" />
  </head>
  <body>
    <section epub:type="chapter">
{body}
    </section>
  </body>
</html>
"""

CONTAINER = """\
<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml" />
  </rootfiles>
</container>
"""


def render_opf(meta, sections) -> str:
    manifest = [
        '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav" />',
        '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml" />',
        '    <item id="css" href="style.css" media-type="text/css" />',
    ]
    spine = []
    for sec in sections:
        sid = f"s{sec.index:03d}"
        manifest.append(
            f'    <item id="{sid}" href="{sec.href}" media-type="application/xhtml+xml" />'
        )
        spine.append(f'    <itemref idref="{sid}" />')
    return f"""\
<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0"
         unique-identifier="book-id" xml:lang="{meta['lang']}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="book-id">urn:uuid:{meta['uuid']}</dc:identifier>
    <dc:title>{html.escape(meta['title'])}</dc:title>
    <dc:creator>{html.escape(meta['author'])}</dc:creator>
    <dc:language>{meta['lang']}</dc:language>
    <meta property="dcterms:modified">{meta['modified']}</meta>
  </metadata>
  <manifest>
{chr(10).join(manifest)}
  </manifest>
  <spine toc="ncx">
{chr(10).join(spine)}
  </spine>
</package>
"""


def render_nav(meta, sections) -> str:
    items = []
    for sec in sections:
        entry = f'        <li><a href="{sec.href}">{html.escape(plain(sec.title))}</a>'
        if sec.subs:
            entry += "\n          <ul>\n"
            entry += "\n".join(
                f'            <li><a href="{sec.href}#{a}">{html.escape(plain(t))}</a></li>'
                for a, t in sec.subs
            )
            entry += "\n          </ul>\n        "
        items.append(entry + "</li>")
    return f"""\
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{meta['lang']}" lang="{meta['lang']}">
  <head>
    <meta charset="utf-8" />
    <title>{html.escape(meta['title'])}</title>
  </head>
  <body>
    <nav epub:type="toc" id="toc">
      <h1>Contents</h1>
      <ol>
{chr(10).join(items)}
      </ol>
    </nav>
  </body>
</html>
"""


def render_ncx(meta, sections) -> str:
    """EPUB 2 fallback; some readers still prefer it over nav.xhtml."""
    points = []
    n = 0
    for sec in sections:
        n += 1
        points.append(f"""\
    <navPoint id="np{n}" playOrder="{n}">
      <navLabel><text>{html.escape(plain(sec.title))}</text></navLabel>
      <content src="{sec.href}" />
    </navPoint>""")
        for anchor, title in sec.subs:
            n += 1
            points.append(f"""\
    <navPoint id="np{n}" playOrder="{n}">
      <navLabel><text>{html.escape(plain(title))}</text></navLabel>
      <content src="{sec.href}#{anchor}" />
    </navPoint>""")
    return f"""\
<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{meta['uuid']}" />
    <meta name="dtb:depth" content="2" />
    <meta name="dtb:totalPageCount" content="0" />
    <meta name="dtb:maxPageNumber" content="0" />
  </head>
  <docTitle><text>{html.escape(meta['title'])}</text></docTitle>
  <navMap>
{chr(10).join(points)}
  </navMap>
</ncx>
"""


def write_epub(path: str, meta, sections, zip_date) -> None:
    def add(zf, name, data, compress=zipfile.ZIP_DEFLATED):
        info = zipfile.ZipInfo(name, date_time=zip_date)
        info.compress_type = compress
        info.external_attr = 0o644 << 16
        zf.writestr(info, data)

    with zipfile.ZipFile(path, "w") as zf:
        # The spec requires `mimetype` first and stored uncompressed.
        add(zf, "mimetype", "application/epub+zip", zipfile.ZIP_STORED)
        add(zf, "META-INF/container.xml", CONTAINER)
        add(zf, "OEBPS/content.opf", render_opf(meta, sections))
        add(zf, "OEBPS/nav.xhtml", render_nav(meta, sections))
        add(zf, "OEBPS/toc.ncx", render_ncx(meta, sections))
        add(zf, "OEBPS/style.css", CSS)
        for sec in sections:
            add(zf, "OEBPS/" + sec.href, XHTML.format(
                lang=meta["lang"],
                title=html.escape(plain(sec.title)),
                body=render_body(sec),
            ))


# --------------------------------------------------------------------------
# version bumping
# --------------------------------------------------------------------------

RE_VERSION = re.compile(r"^(?P<base>.+)_v(?P<major>\d+)_(?P<minor>\d+)$")


def bumped_path(md_path: str) -> str | None:
    """`ch_0_v3_2.md` -> `ch_0_v3_3.md`; None if the name carries no version."""
    head, name = os.path.split(md_path)
    stem, ext = os.path.splitext(name)
    m = RE_VERSION.match(stem)
    if not m:
        return None
    minor = int(m.group("minor")) + 1
    return os.path.join(head, f"{m.group('base')}_v{m.group('major')}_{minor}{ext}")


def plan_bumps(sources: list[str], fail) -> dict[str, str]:
    """Work out every rename before performing any of them.

    Validating up front means a collision on the third file doesn't leave the
    first two already renamed.
    """
    plan: dict[str, str] = {}
    for src in sources:
        dst = bumped_path(src)
        if dst is None:
            print(f"warning: {os.path.basename(src)} has no _vN_N version; "
                  f"building without a bump", file=sys.stderr)
            continue
        if os.path.exists(dst):
            fail(f"cannot bump {os.path.basename(src)}: "
                 f"{os.path.basename(dst)} already exists")
        if dst in plan.values():
            fail(f"two sources would both bump to {os.path.basename(dst)}")
        plan[src] = dst
    return plan


# --------------------------------------------------------------------------
# readme
# --------------------------------------------------------------------------

SPEEDS = (1.0, 1.5, 2.0)


def listen_time(words: int, wpm: float, speed: float) -> str:
    minutes = int(round(words / (wpm * speed)))
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes:02d}m" if hours else f"{minutes}m"


def collect_stats(sources: list[str], sections: list[Section]) -> dict:
    """Numbers for the book just built, taken from the built sections.

    Read off what was actually written rather than re-parsing the source, so a
    merged build reports the merged totals.
    """
    lines = 0
    for path in sources:
        with open(path, encoding="utf-8") as fh:
            lines += len(fh.read().splitlines())

    head = sections[0].title
    m = re.match(r"Chapter (\d+):[ \t]*(.*)$", head)
    return {
        "source": ", ".join(os.path.basename(s) for s in sources),
        "number": m.group(1) if m else "",
        "title": (m.group(2) if m else head).strip(),
        "h1s": [s.title for s in sections],
        "words": spoken_words(sections),
        "lines": lines,
    }


TABLE_HEAD = ["Built", "Ch", "Title", "Source", "H1s", "Words", "Lines"]
TABLE_HEAD += [f"{s:g}x" for s in SPEEDS]
TABLE_ALIGN = ["---", "---:", "---", "---", "---", "---:", "---:"]
TABLE_ALIGN += ["---:"] * len(SPEEDS)

RE_TABLE_SEP = re.compile(r"^\|[ \t]*:?-{3,}")


def _row(cells) -> str:
    return "| " + " | ".join(cells) + " |"


def readme_header(wpm: float) -> list[str]:
    return [
        "# Chapter EPUBs",
        "",
        "Build log for [md2epub.py](../md2epub.py), which converts a chapter to an",
        "EPUB for ElevenReader TTS ingestion. Newest build first; entries are only",
        "ever added, never rewritten, so each row records what was true at the time",
        "it was built.",
        "",
        "Build one chapter with:",
        "",
        "```bash",
        "python3 theory/chapters/md2epub.py theory/chapters/sequenced/<chapter>.md",
        "```",
        "",
        "Every run bumps the source version -- `ch_0_v3_2.md` becomes `ch_0_v3_3.md`,",
        "built as `ch_0_v3_3.epub`, with the superseded EPUB removed. The `Source`",
        "column is the version each book was built from. Pass `--no-bump` to build",
        "in place.",
        "",
        f"Word counts are of the *spoken* text after normalization, so they include "
        f"headings and the spoken bracket tokens. Listen times assume {wpm:g} wpm at 1x.",
        "",
        _row(TABLE_HEAD),
        _row(TABLE_ALIGN),
    ]


def readme_row(stats: dict, wpm: float, built: str) -> str:
    h1s = str(len(stats["h1s"]))
    extra = "; ".join(stats["h1s"][1:])
    if extra:
        h1s += f" ({extra})"
    return _row([
        built, stats["number"] or "--", stats["title"], stats["source"], h1s,
        f"{stats['words']:,}", f"{stats['lines']:,}",
    ] + [listen_time(stats["words"], wpm, s) for s in SPEEDS])


def append_readme(out_dir: str, stats: dict, wpm: float, built: str) -> str:
    """Insert one row at the top of the table, leaving every existing line be.

    The file is append-only: nothing already written is rewritten or reordered,
    so the log survives hand-edits and format changes.
    """
    path = os.path.join(out_dir, "README.md")
    row = readme_row(stats, wpm, built)

    if os.path.isfile(path):
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        for i, line in enumerate(lines):
            if RE_TABLE_SEP.match(line):
                lines.insert(i + 1, row)
                break
        else:
            # No table to extend -- start one, keeping whatever is already here.
            lines = readme_header(wpm) + [row, ""] + lines
    else:
        lines = readme_header(wpm) + [row]

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return path


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------

def load(path: str, dash_mode: str, bracket_mode: str):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    text = normalize_text(strip_comments(raw), dash_mode, bracket_mode)
    return parse_blocks(text)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Convert sequenced chapter markdown to an ElevenReader-ready EPUB.")
    ap.add_argument("sources", nargs="+", metavar="FILE.md",
                    help="chapter markdown file(s) from theory/chapters/sequenced/")
    ap.add_argument("-o", "--output",
                    help="output .epub path (default: <stem>.epub in "
                         "theory/chapters/epubs/)")
    ap.add_argument("--merge", action="store_true",
                    help="combine multiple sources into one EPUB (default: one EPUB each)")
    ap.add_argument("--title", help="book title (default: the first `# ` heading)")
    ap.add_argument("--author", default="Brian Kuhlman", help="dc:creator (default: %(default)s)")
    ap.add_argument("--lang", default="en", help="dc:language (default: %(default)s)")
    ap.add_argument("--dash", choices=DASH_MODES, default="comma",
                    help="how to speak em dashes (default: %(default)s)")
    ap.add_argument("--keep-byline", action="store_true",
                    help="keep the `*Brian Kuhlman. draft. June 2026.*` line (default: drop it)")
    ap.add_argument("--brackets", choices=BRACKET_MODES, default="spoken",
                    help="screen-log notation: `spoken` names the delimiters "
                         "(MIRA, OPEN-BRACKET, WANTING, ...), `commas` drops "
                         "them, `keep` leaves { } [ ] intact "
                         "(default: %(default)s)")
    ap.add_argument("--no-bump", action="store_true",
                    help="do not bump the source version (default: every run "
                         "renames ch_0_v3_2.md to ch_0_v3_3.md and builds that)")
    ap.add_argument("--wpm", type=float, default=150.0,
                    help="words per minute at 1x, for the README listen times "
                         "(default: %(default)s)")
    ap.add_argument("--no-readme", action="store_true",
                    help="skip rewriting README.md in the output directory")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the text a voice would read; write nothing")
    args = ap.parse_args(argv)

    for src in args.sources:
        if not os.path.isfile(src):
            ap.error(f"no such file: {src}")

    groups = [args.sources] if (args.merge or len(args.sources) == 1) \
        else [[s] for s in args.sources]

    if args.output and len(groups) > 1:
        ap.error("--output takes a single file; add --merge or drop -o")

    # Bump first, then build from the new name, so the EPUB and its source
    # always carry the same version.
    superseded = {}
    if not args.dry_run and not args.no_bump:
        plan = plan_bumps(args.sources, ap.error)
        for src, dst in plan.items():
            os.rename(src, dst)
            print(f"{os.path.basename(src)} -> {os.path.basename(dst)}")
            superseded[dst] = os.path.splitext(os.path.basename(src))[0]
        groups = [[plan.get(s, s) for s in group] for group in groups]

    built_at = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    for group in groups:
        blocks = []
        for src in group:
            blocks.extend(load(src, args.dash, args.brackets))

        stem = os.path.splitext(os.path.basename(group[0]))[0]
        sections = split_sections(blocks, fallback_title=stem)
        if not args.keep_byline:
            strip_byline(sections)
        trim_rules(sections)

        title = args.title or plain(sections[0].title)

        if args.dry_run:
            sys.stdout.write(render_plain(sections))
            continue

        out = args.output or os.path.join(DEFAULT_OUT_DIR, stem + ".epub")
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        mtime = _dt.datetime.fromtimestamp(os.path.getmtime(group[0]), _dt.timezone.utc)
        meta = {
            "title": title,
            "author": args.author,
            "lang": args.lang,
            "uuid": uuid.uuid5(_NS, "|".join(sorted(os.path.basename(s) for s in group))),
            # Fixed from the source mtime so rebuilds are byte-identical.
            "modified": mtime.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        write_epub(out, meta, sections, mtime.timetuple()[:6])

        words = spoken_words(sections)
        print(f"{out}  ({len(sections)} section(s), ~{words:,} words, "
              f"~{listen_time(words, args.wpm, 1.0)} at {args.wpm:g} wpm)")
        out_dir = os.path.dirname(os.path.abspath(out))
        if not args.no_readme:
            path = append_readme(out_dir, collect_stats(group, sections),
                                 args.wpm, built_at)
            print(f"{path}  (row added)")

        # The previous version's EPUB is now orphaned -- its source no longer
        # exists under that name. Drop it so the folder keeps one per chapter.
        old_stem = superseded.get(group[0])
        if old_stem:
            stale = os.path.join(out_dir, old_stem + ".epub")
            if os.path.isfile(stale) and os.path.abspath(stale) != os.path.abspath(out):
                os.remove(stale)
                print(f"{stale}  (superseded, removed)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
