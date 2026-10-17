#!/usr/bin/env python3
"""
Extract OCEAN domain-relevant sections from 'Facet Development.docx'
into separate condensed text files (one per domain).

Each extracted section includes:
  - The full heading breadcrumb (H1 > H2 > H3 > H4) it's nested under
  - All paragraph text within matching sections
  - Any [from PDF p. X] page references preserved inline

When a study contains any domain-matched section, the study's metadata
block (Citation, Design, Granularity — everything before the first
domain-specific heading) is prepended once.

Matching uses a two-tier keyword system:
  - Precise terms (facet codes, domain names, aspect names) match on
    their own.
  - Generic terms (common English words like "Fantasy", "Trust",
    "Depression") only match when co-occurring with a precise term or
    with 2+ other generic terms from the same domain in the same
    section body.
"""

import re
import sys
from pathlib import Path
from docx import Document

# ---------------------------------------------------------------------------
# Domain definitions — two-tier keywords
# ---------------------------------------------------------------------------

DOMAINS = {
    "openness": {
        "facet_codes": [f"O{i}" for i in range(1, 7)],
        "heading_keywords": [
            r"\bOpenness\b", r"\bOpen-Mindedness\b", r"\bOpen[\s-]?Minded\b",
            r"\bIntellect\b", r"\bO/I\b",
        ],
        "precise_body": [
            r"\bOpenness\b", r"\bOpen-Mindedness\b",
            r"\bIntellect\b(?!ual Humility)",
            r"\bCreative Imagination\b",
            r"\bO\s+facet",
        ],
        "generic_body": [
            r"\bFantasy\b", r"\bAesthetics\b", r"\bFeelings\b",
            r"\bActions\b", r"\bIdeas\b", r"\bValues\b",
        ],
    },
    "conscientiousness": {
        "facet_codes": [f"C{i}" for i in range(1, 7)],
        "heading_keywords": [
            r"\bConscientiousness\b",
            r"\bIndustriousness\b", r"\bOrderliness\b",
        ],
        "precise_body": [
            r"\bConscientiousness\b",
            r"\bIndustriousness\b", r"\bOrderliness\b",
            r"\bC\s+facet",
        ],
        "generic_body": [
            r"\bCompetence\b", r"\bDutifulness\b",
            r"\bAchievement\s+Striv", r"\bSelf-Discipline\b",
            r"\bDeliberation\b", r"\bResponsibility\b",
        ],
    },
    "extraversion": {
        "facet_codes": [f"E{i}" for i in range(1, 7)],
        "heading_keywords": [
            r"\bExtraversion\b",
            r"\bEnthusiasm\b", r"\bAssertiveness\b",
            r"\bSocial\s+Vitality\b", r"\bSocial\s+Dominance\b",
        ],
        "precise_body": [
            r"\bExtraversion\b",
            r"\bEnthusiasm\b", r"\bAssertiveness\b",
            r"\bSocial\s+Vitality\b", r"\bSocial\s+Dominance\b",
            r"\bE\s+facet",
        ],
        "generic_body": [
            r"\bWarmth\b", r"\bGregariousness\b", r"\bPositive\s+Emotions\b",
            r"\bActivity\b", r"\bExcitement[\s-]Seeking\b",
            r"\bSociability\b", r"\bEnergy\s+Level\b",
        ],
    },
    "agreeableness": {
        "facet_codes": [f"A{i}" for i in range(1, 8)],
        "heading_keywords": [
            r"\bAgreeableness\b",
            r"\bCompassion\b", r"\bPoliteness\b",
        ],
        "precise_body": [
            r"\bAgreeableness\b",
            r"\bCompassion\b", r"\bPoliteness\b",
            r"\bA\s+facet",
        ],
        "generic_body": [
            r"\bTrust\b", r"\bStraightforwardness\b", r"\bAltruism\b",
            r"\bCompliance\b", r"\bModesty\b", r"\bTender-Mindedness\b",
        ],
    },
    "neuroticism": {
        "facet_codes": [f"N{i}" for i in range(1, 7)],
        "heading_keywords": [
            r"\bNeuroticism\b", r"\bNegative\s+Emotionality\b",
            r"\bEmotional\s+Stability\b",
            r"\bVolatility\b", r"\bWithdrawal\b",
        ],
        "precise_body": [
            r"\bNeuroticism\b", r"\bNegative\s+Emotionality\b",
            r"\bEmotional\s+Stability\b",
            r"\bVolatility\b", r"\bWithdrawal\b",
            r"\bN\s+facet",
        ],
        "generic_body": [
            r"\bAnxiety\b", r"\bAngry\s+Hostility\b", r"\bDepression\b",
            r"\bSelf-Consciousness\b", r"\bImpulsiveness\b",
            r"\bVulnerability\b",
        ],
    },
}

# Minimum number of distinct generic-term matches required when no
# precise term is present.  2 = at least two different generic terms
# from the same domain must co-occur.
GENERIC_CO_OCCURRENCE_THRESHOLD = 2

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def heading_level(style_name: str) -> int | None:
    """Return numeric level for heading styles, or None."""
    if style_name == "Title":
        return 0
    m = re.match(r"Heading\s+(\d+)", style_name)
    return int(m.group(1)) if m else None


def compile_pattern(keywords: list[str]) -> re.Pattern:
    """Compile a case-insensitive regex matching any keyword."""
    return re.compile("|".join(keywords), re.IGNORECASE)


def compile_patterns_list(keywords: list[str]) -> list[re.Pattern]:
    """Compile each keyword as its own pattern (for counting distinct matches)."""
    return [re.compile(kw, re.IGNORECASE) for kw in keywords]


def body_matches_domain(
    text: str,
    facet_re: re.Pattern,
    precise_re: re.Pattern,
    generic_patterns: list[re.Pattern],
) -> bool:
    """
    Two-tier matching for body text:
      - If any facet code matches → True
      - If any precise body keyword matches → True
      - If generic terms match, they only count if a precise term or
        facet code is also present, OR if >= GENERIC_CO_OCCURRENCE_THRESHOLD
        distinct generic terms co-occur.
    """
    has_facet = bool(facet_re.search(text))
    has_precise = bool(precise_re.search(text))

    if has_facet or has_precise:
        return True

    # Count distinct generic term matches
    generic_hit_count = sum(1 for pat in generic_patterns if pat.search(text))
    return generic_hit_count >= GENERIC_CO_OCCURRENCE_THRESHOLD


# ---------------------------------------------------------------------------
# Parse document into a tree of sections
# ---------------------------------------------------------------------------

class Section:
    """A heading and its child paragraphs / subsections."""
    __slots__ = ("level", "title", "style", "paragraphs", "children", "para_index")

    def __init__(self, level: int, title: str, style: str, para_index: int):
        self.level = level
        self.title = title
        self.style = style
        self.paragraphs: list[str] = []
        self.children: list["Section"] = []
        self.para_index = para_index

    def all_text(self) -> str:
        """All body text in this section (not children)."""
        return "\n".join(self.paragraphs)


def parse_sections(doc: Document) -> list[Section]:
    """Parse paragraphs into a tree of Sections based on heading levels."""
    root_sections: list[Section] = []
    stack: list[tuple[int, Section]] = []

    for idx, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        if not text:
            continue

        level = heading_level(para.style.name)

        if level is not None:
            sec = Section(level, text, para.style.name, idx)
            while stack and stack[-1][0] >= level:
                stack.pop()
            if stack:
                stack[-1][1].children.append(sec)
            else:
                root_sections.append(sec)
            stack.append((level, sec))
        else:
            if stack:
                stack[-1][1].paragraphs.append(text)

    return root_sections


# ---------------------------------------------------------------------------
# Study detection and metadata extraction
# ---------------------------------------------------------------------------

# Matches headings like "Jang, Livesley & Vernon (1996)" or
# "Schwaba et al. (2025) — Big Five GWAS"
STUDY_HEADING_RE = re.compile(
    r"^[A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝ]"  # starts with uppercase letter
    r".*\(\d{4}\)",                             # contains (YYYY)
)

# Headings that signal the end of the metadata block
DOMAIN_HEADING_RE = re.compile(
    r"\bDomain:\s|"
    r"\bExtraversion\b|\bAgreeableness\b|\bConscientiousness\b|"
    r"\bNeuroticism\b|\bNegative\s+Emotionality\b|\bEmotional\s+Stability\b|"
    r"\bOpenness\b|\bOpen-Mindedness\b|\bIntellect\b|"
    r"\bVolatility\b|\bWithdrawal\b|"
    r"\bEnthusiasm\b|\bAssertiveness\b|"
    r"\bCompassion\b|\bPoliteness\b|"
    r"\bIndustriousness\b|\bOrderliness\b|"
    r"\bSocial\s+Vitality\b|\bSocial\s+Dominance\b|"
    r"\b[EOACN]\d\b",
    re.IGNORECASE,
)


def is_study_heading(sec: Section) -> bool:
    return sec.level <= 1 and bool(STUDY_HEADING_RE.match(sec.title))


def extract_study_metadata(study_sec: Section) -> list[dict]:
    """
    Extract the metadata block: all sections between the study heading
    and the first domain-specific subheading (recursively).
    Returns a list of {breadcrumb, title, body, para_index} dicts.
    """
    metadata = []

    # The study heading itself
    metadata.append({
        "breadcrumb": [study_sec.title],
        "title": study_sec.title,
        "body": study_sec.all_text(),
        "para_index": study_sec.para_index,
    })

    # Walk children until we hit one whose heading matches a domain
    for child in study_sec.children:
        if DOMAIN_HEADING_RE.search(child.title):
            break
        # This child is metadata (Citation, Design, Granularity, etc.)
        metadata.append({
            "breadcrumb": [study_sec.title, child.title],
            "title": child.title,
            "body": child.all_text(),
            "para_index": child.para_index,
        })
        # Also include any sub-children of metadata sections
        for grandchild in child.children:
            if DOMAIN_HEADING_RE.search(grandchild.title):
                break
            metadata.append({
                "breadcrumb": [study_sec.title, child.title, grandchild.title],
                "title": grandchild.title,
                "body": grandchild.all_text(),
                "para_index": grandchild.para_index,
            })

    return metadata


def find_study_ancestor(breadcrumb: list[str], study_sections: dict) -> str | None:
    """Given a breadcrumb, find which study (by title) this section belongs to."""
    for crumb_part in breadcrumb:
        if crumb_part in study_sections:
            return crumb_part
    return None


# ---------------------------------------------------------------------------
# Extract matching sections for a domain
# ---------------------------------------------------------------------------

def collect_matches(
    sections: list[Section],
    facet_re: re.Pattern,
    heading_kw_re: re.Pattern,
    precise_re: re.Pattern,
    generic_patterns: list[re.Pattern],
    breadcrumb: list[str] | None = None,
) -> list[dict]:
    """
    Walk the section tree.  A section is included if:
      1. Its heading matches a domain heading keyword or facet code, OR
      2. Its body text passes the two-tier matching test.

    Returns a list of dicts: {breadcrumb, title, body, para_index}
    """
    if breadcrumb is None:
        breadcrumb = []

    results = []

    for sec in sections:
        current_crumb = breadcrumb + [sec.title]

        heading_match = bool(facet_re.search(sec.title) or heading_kw_re.search(sec.title))
        body_text = sec.all_text()
        body_match = body_matches_domain(body_text, facet_re, precise_re, generic_patterns)

        if heading_match or body_match:
            results.append({
                "breadcrumb": list(current_crumb),
                "title": sec.title,
                "body": body_text,
                "para_index": sec.para_index,
            })

        # Always recurse into children
        child_results = collect_matches(
            sec.children, facet_re, heading_kw_re, precise_re,
            generic_patterns, current_crumb,
        )
        results.extend(child_results)

    return results


# ---------------------------------------------------------------------------
# Format output
# ---------------------------------------------------------------------------

def format_output(
    matches: list[dict],
    study_metadata: dict[str, list[dict]],
    study_sections: dict[str, Section],
) -> str:
    """
    Format matches grouped by study.  When a study has matches, its
    metadata block is printed first, then the matched sections.
    Non-study sections (e.g. the crosswalk intro) come first.
    """
    # Figure out which studies have matches
    studies_with_matches: dict[str, list[dict]] = {}
    non_study_matches: list[dict] = []

    for m in matches:
        study_title = find_study_ancestor(m["breadcrumb"], study_sections)
        if study_title:
            studies_with_matches.setdefault(study_title, []).append(m)
        else:
            non_study_matches.append(m)

    lines: list[str] = []

    # Non-study sections first
    for m in non_study_matches:
        if lines:
            lines.append("")
            lines.append("─" * 72)
            lines.append("")
        crumb = " > ".join(m["breadcrumb"])
        lines.append(f"[{crumb}]")
        lines.append("")
        body = m["body"].strip()
        lines.append(body if body else "(no body text — heading only)")

    # Study sections
    for study_title in study_sections:
        if study_title not in studies_with_matches:
            continue

        # Study header bar
        lines.append("")
        lines.append("═" * 72)
        lines.append(f"STUDY: {study_title}")
        lines.append("═" * 72)

        # Metadata block
        meta = study_metadata.get(study_title, [])
        meta_indices = {m["para_index"] for m in meta}
        for m in meta:
            # Skip the study heading itself (already in the banner)
            if m["para_index"] == study_sections[study_title].para_index:
                continue
            body = m["body"].strip()
            if body:
                lines.append("")
                crumb = " > ".join(m["breadcrumb"])
                lines.append(f"[{crumb}]")
                lines.append("")
                lines.append(body)

        # Matched sections (skip any that are part of metadata)
        for m in studies_with_matches[study_title]:
            if m["para_index"] in meta_indices:
                continue
            lines.append("")
            lines.append("─" * 72)
            lines.append("")
            crumb = " > ".join(m["breadcrumb"])
            lines.append(f"[{crumb}]")
            lines.append("")
            body = m["body"].strip()
            lines.append(body if body else "(no body text — heading only)")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Accept optional arguments: input docx path and output suffix
    # Usage: python extract_domains.py [docx_file] [suffix]
    # e.g.:  python extract_domains.py "Facet Development - v2.docx" _v2
    script_dir = Path(__file__).parent

    if len(sys.argv) >= 2:
        docx_path = script_dir / sys.argv[1]
    else:
        docx_path = script_dir / "Facet Development.docx"

    suffix = sys.argv[2] if len(sys.argv) >= 3 else ""

    if not docx_path.exists():
        print(f"Error: {docx_path} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Reading {docx_path.name}...")
    doc = Document(str(docx_path))
    sections = parse_sections(doc)

    # Identify all study sections and extract their metadata
    study_sections: dict[str, Section] = {}    # title → Section (ordered)
    study_metadata: dict[str, list[dict]] = {}

    def find_studies(secs: list[Section]):
        for sec in secs:
            if is_study_heading(sec):
                study_sections[sec.title] = sec
                study_metadata[sec.title] = extract_study_metadata(sec)
            find_studies(sec.children)

    find_studies(sections)
    print(f"  Found {len(study_sections)} studies")

    out_dir = script_dir / "domains"
    out_dir.mkdir(exist_ok=True)

    for domain_name, cfg in DOMAINS.items():
        facet_re = compile_pattern(
            [r"\b" + re.escape(c) + r"\b" for c in cfg["facet_codes"]]
        )
        heading_kw_re = compile_pattern(cfg["heading_keywords"])
        precise_re = compile_pattern(cfg["precise_body"])
        generic_pats = compile_patterns_list(cfg["generic_body"])

        matches = collect_matches(
            sections, facet_re, heading_kw_re, precise_re, generic_pats
        )

        # Deduplicate by para_index
        seen = set()
        unique = []
        for m in matches:
            if m["para_index"] not in seen:
                seen.add(m["para_index"])
                unique.append(m)

        out_path = out_dir / f"{domain_name}{suffix}.txt"
        out_path.write_text(
            format_output(unique, study_metadata, study_sections),
            encoding="utf-8",
        )
        print(f"  {domain_name}: {len(unique)} sections → {out_path}")

    print("Done.")


if __name__ == "__main__":
    main()
