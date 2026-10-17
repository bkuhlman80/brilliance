#!/usr/bin/env python3
"""
Align paper_index.md and annotated_bibliography.md so both files share
the same canonical ordering and numbering.

Canonical sort key: (first_author_surname, year, chapter_number, title_prefix)

Usage:
    python scripts/align_references.py --dry-run   # preview without writing
    python scripts/align_references.py              # execute
"""

import re
import sys
import shutil
import unicodedata
from pathlib import Path
from difflib import SequenceMatcher

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE = Path(__file__).resolve().parent.parent / "References"
PI_PATH = BASE / "paper_index.md"
AB_PATH = BASE / "annotated_bibliography.md"

# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

ENTRY_RE = re.compile(r"^### \d+[a-z]?\. ", re.MULTILINE)


def split_entries(text, file_type):
    """Split file text into (preamble, list_of_entry_strings, footer).

    An entry is everything from its ### header up to (not including) the next
    ### header or the footer marker.
    """
    # Find footer (paper_index only)
    footer = ""
    if file_type == "pi":
        footer_match = re.search(r"\n---\n\n## Summary Statistics.*", text, re.DOTALL)
        if footer_match:
            footer = text[footer_match.start():]
            text = text[:footer_match.start()]

    # Find all entry start positions
    starts = [m.start() for m in ENTRY_RE.finditer(text)]

    if not starts:
        return text, [], footer

    preamble = text[:starts[0]]
    entries = []
    for i, s in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        entries.append(text[s:end])

    return preamble, entries, footer


def parse_entry_header(entry_text):
    """Extract the number (str) and the label portion after the number."""
    m = re.match(r"^### (\d+[a-z]?)\. (.+)", entry_text)
    if m:
        return m.group(1), m.group(2).strip()
    return None, None


# ---------------------------------------------------------------------------
# Citation metadata extraction
# ---------------------------------------------------------------------------

DOI_RE = re.compile(r"https?://doi\.org/(\S+)")
YEAR_RE = re.compile(r"\((\d{4})\)")
# Match "Chapter X" or "Ch. X" in citations or headers
CHAPTER_RE = re.compile(r"(?:Chapter|Ch\.?)\s*(\d+)", re.IGNORECASE)
CONCLUSION_RE = re.compile(r"Conclusion", re.IGNORECASE)

# Surname prefixes that should be kept as part of the surname
SURNAME_PREFIX_RE = re.compile(
    r"^(van\s+den\s+|van\s+der\s+|van\s+de\s+|van\s+|von\s+|de\s+|di\s+|le\s+|du\s+|del\s+|della\s+|dos\s+|da\s+|el\s+|al-)",
    re.IGNORECASE,
)


def normalize_text(s):
    """Lowercase, normalize unicode, strip extra whitespace."""
    s = unicodedata.normalize("NFKD", s)
    return " ".join(s.lower().split())


def extract_doi(text):
    m = DOI_RE.search(text)
    if m:
        doi = m.group(1).rstrip(".,;:)")
        return doi.lower()
    return None


def extract_citation_line(entry_text):
    """Get the citation string from the entry."""
    for line in entry_text.split("\n"):
        line_stripped = line.strip().lstrip("- ")
        if line_stripped.startswith("**Citation:**"):
            return line_stripped.replace("**Citation:**", "").strip()
    return ""


def extract_first_author_surname(citation):
    """Extract first author's surname from a citation string."""
    if not citation or citation.startswith("*["):
        return ""

    # Remove leading "**Citation:** " if present
    citation = citation.strip()

    # The surname is everything up to the first comma (or period for single-author)
    # Handle patterns like "van den Berg, S. M." or "Røysamb, E."

    # First, grab text before the first comma or opening paren
    before_comma = re.split(r",|\(", citation)[0].strip()

    # Remove trailing period if present
    before_comma = before_comma.rstrip(".")

    return before_comma


def extract_year(citation):
    """Extract publication year from citation."""
    m = YEAR_RE.search(citation)
    if m:
        return int(m.group(1))
    return 9999


def extract_title(citation):
    """Extract title from citation — text after '). ' up to next period + italic marker."""
    # Pattern: ....(YEAR). Title here. *Journal*...
    m = re.search(r"\)\.\s+(.+?)(?:\.\s+\*|\.\s+In\s|\.\s+https?://)", citation)
    if m:
        return normalize_text(m.group(1))
    # Fallback: grab everything after year paren
    m = re.search(r"\)\.\s+(.+)", citation)
    if m:
        return normalize_text(m.group(1)[:80])
    return ""


def extract_chapter_number(entry_text, citation):
    """Extract chapter number for multi-chapter works (e.g., Bennett 2023)."""
    # Check header line
    header_line = entry_text.split("\n")[0]

    # Check for "Conclusion" in header or citation
    if CONCLUSION_RE.search(header_line) or CONCLUSION_RE.search(citation):
        return 999

    # Check header for ch patterns
    m = re.search(r"[Cc]h\.?\s*(\d+)|[Cc]hapter\s*(\d+)", header_line)
    if m:
        return int(m.group(1) or m.group(2))

    # Check citation
    m = CHAPTER_RE.search(citation)
    if m:
        return int(m.group(1))

    return 0  # non-chapter entry


def is_broken_entry(entry_text):
    """Check if entry is broken/duplicate/incomplete."""
    citation = extract_citation_line(entry_text)
    return citation.startswith("*[") or citation.startswith("[")


def get_entry_metadata(entry_text):
    """Extract all metadata from an entry."""
    citation = extract_citation_line(entry_text)
    num, label = parse_entry_header(entry_text)

    return {
        "number": num,
        "label": label,
        "text": entry_text,
        "citation": citation,
        "doi": extract_doi(entry_text),
        "surname": extract_first_author_surname(citation),
        "year": extract_year(citation),
        "title": extract_title(citation),
        "chapter": extract_chapter_number(entry_text, citation),
        "broken": is_broken_entry(entry_text),
    }


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------

def normalize_surname_for_matching(surname):
    """Normalize surname for comparison."""
    s = normalize_text(surname)
    # Remove accents for matching purposes
    s = "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )
    return s.strip()


def match_entries(pi_entries, ab_entries):
    """Match paper_index entries to annotated_bibliography entries.

    Returns: list of (pi_meta, ab_meta) pairs, plus unmatched lists.
    """
    matched = []
    unmatched_pi = []
    unmatched_ab = list(range(len(ab_entries)))  # indices

    # Build DOI index for AB
    ab_by_doi = {}
    for i, ab in enumerate(ab_entries):
        if ab["doi"]:
            ab_by_doi[ab["doi"]] = i

    # Build surname+year index for AB
    ab_by_sy = {}
    for i, ab in enumerate(ab_entries):
        key = (normalize_surname_for_matching(ab["surname"]), ab["year"])
        ab_by_sy.setdefault(key, []).append(i)

    matched_ab_indices = set()

    # Tier 1: DOI match
    doi_matches = 0
    for pi in pi_entries:
        if pi["broken"]:
            unmatched_pi.append(pi)
            continue
        if pi["doi"] and pi["doi"] in ab_by_doi:
            ab_idx = ab_by_doi[pi["doi"]]
            if ab_idx not in matched_ab_indices:
                matched.append((pi, ab_entries[ab_idx]))
                matched_ab_indices.add(ab_idx)
                doi_matches += 1
                continue
        # Not matched by DOI — try later
        pi["_needs_fallback"] = True

    # Tier 2: surname + year + title similarity
    sy_matches = 0
    fuzzy_matches = 0
    for pi in pi_entries:
        if pi["broken"] or not pi.get("_needs_fallback"):
            continue

        pi_key = (normalize_surname_for_matching(pi["surname"]), pi["year"])
        candidates = ab_by_sy.get(pi_key, [])
        candidates = [c for c in candidates if c not in matched_ab_indices]

        if len(candidates) == 1:
            matched.append((pi, ab_entries[candidates[0]]))
            matched_ab_indices.add(candidates[0])
            sy_matches += 1
            pi.pop("_needs_fallback", None)
            continue

        if len(candidates) > 1:
            # Use title similarity to disambiguate
            best_idx = None
            best_ratio = 0
            for c in candidates:
                ratio = SequenceMatcher(
                    None,
                    normalize_text(pi["title"])[:60],
                    normalize_text(ab_entries[c]["title"])[:60],
                ).ratio()
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_idx = c
            if best_idx is not None and best_ratio > 0.3:
                matched.append((pi, ab_entries[best_idx]))
                matched_ab_indices.add(best_idx)
                fuzzy_matches += 1
                pi.pop("_needs_fallback", None)
                continue

        # Still unmatched
        pi.pop("_needs_fallback", None)

    # Tier 3: broader fuzzy matching for remaining
    remaining_pi = [pi for pi in pi_entries if not pi["broken"] and pi.get("_needs_fallback")]
    for pi in remaining_pi:
        # Try matching just on surname with fuzzy title
        pi_sn = normalize_surname_for_matching(pi["surname"])
        best_idx = None
        best_score = 0
        for i in range(len(ab_entries)):
            if i in matched_ab_indices:
                continue
            ab = ab_entries[i]
            ab_sn = normalize_surname_for_matching(ab["surname"])
            if pi_sn == ab_sn:
                title_sim = SequenceMatcher(
                    None,
                    normalize_text(pi["title"])[:60],
                    normalize_text(ab["title"])[:60],
                ).ratio()
                if title_sim > best_score:
                    best_score = title_sim
                    best_idx = i
        if best_idx is not None and best_score > 0.2:
            matched.append((pi, ab_entries[best_idx]))
            matched_ab_indices.add(best_idx)
            fuzzy_matches += 1
            pi.pop("_needs_fallback", None)
        else:
            unmatched_pi.append(pi)
            pi.pop("_needs_fallback", None)

    # Remaining unmatched PI
    for pi in pi_entries:
        if pi.get("_needs_fallback"):
            unmatched_pi.append(pi)
            pi.pop("_needs_fallback", None)

    unmatched_ab_list = [ab_entries[i] for i in range(len(ab_entries)) if i not in matched_ab_indices]

    stats = {
        "doi": doi_matches,
        "surname_year": sy_matches,
        "fuzzy": fuzzy_matches,
        "unmatched_pi": len(unmatched_pi),
        "unmatched_ab": len(unmatched_ab_list),
        "total_matched": len(matched),
    }

    return matched, unmatched_pi, unmatched_ab_list, stats


# ---------------------------------------------------------------------------
# Sorting
# ---------------------------------------------------------------------------

def sort_key(pair):
    """Canonical sort key from a matched (pi, ab) pair."""
    # Use AB metadata as primary (cleaner author names)
    meta = pair[1]  # ab entry
    pi_meta = pair[0]

    surname = normalize_surname_for_matching(meta["surname"])
    year = meta["year"]
    chapter = meta["chapter"] or pi_meta["chapter"] or 0
    title = normalize_text(meta["title"])[:50]

    return (surname, year, chapter, title)


# ---------------------------------------------------------------------------
# Rewriting
# ---------------------------------------------------------------------------

def rewrite_entry_number(entry_text, new_number):
    """Replace the entry number in the ### header."""
    return re.sub(
        r"^### \d+[a-z]?\. ",
        f"### {new_number}. ",
        entry_text,
        count=1,
    )


def rebuild_file(preamble, sorted_entries, footer, file_type):
    """Reassemble a file from its parts."""
    parts = [preamble.rstrip("\n") + "\n"]

    for entry_text in sorted_entries:
        if file_type == "ab":
            # Ensure entry ends with \n---\n\n
            entry_text = entry_text.rstrip("\n").rstrip("-").rstrip("\n")
            parts.append(entry_text + "\n\n---\n")
        else:
            # paper_index: entries separated by blank lines
            parts.append(entry_text.rstrip("\n") + "\n")

    content = "\n".join(parts)

    if footer:
        content = content.rstrip("\n") + "\n\n" + footer.lstrip("\n")

    return content


# ---------------------------------------------------------------------------
# Summary Statistics update
# ---------------------------------------------------------------------------

def update_summary_stats(footer, new_total, purpose_counts):
    """Update the total count in the Summary Statistics footer."""
    footer = re.sub(
        r"\| \*\*Total papers\*\* \| \d+ \|",
        f"| **Total papers** | {new_total} |",
        footer,
    )
    return footer


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv

    print(f"{'DRY RUN' if dry_run else 'EXECUTING'}: Aligning reference files\n")

    # Read files
    pi_text = PI_PATH.read_text(encoding="utf-8")
    ab_text = AB_PATH.read_text(encoding="utf-8")

    # Parse
    pi_preamble, pi_raw_entries, pi_footer = split_entries(pi_text, "pi")
    ab_preamble, ab_raw_entries, ab_footer = split_entries(ab_text, "ab")

    print(f"paper_index:   {len(pi_raw_entries)} entries parsed")
    print(f"annotated_bib: {len(ab_raw_entries)} entries parsed")

    # Extract metadata
    pi_entries = [get_entry_metadata(e) for e in pi_raw_entries]
    ab_entries = [get_entry_metadata(e) for e in ab_raw_entries]

    broken_count = sum(1 for e in pi_entries if e["broken"])
    print(f"Broken/duplicate PI entries: {broken_count}")

    # Deduplicate PI entries: remove broken + DOI/citation duplicates
    seen_pi_dois = {}
    seen_pi_citations = {}
    pi_dupes = []
    deduped_pi = []
    for pi in pi_entries:
        if pi["broken"]:
            pi_dupes.append(pi)
            continue
        is_dupe = False
        if pi["doi"]:
            if pi["doi"] in seen_pi_dois:
                is_dupe = True
            else:
                seen_pi_dois[pi["doi"]] = pi["number"]
        if not is_dupe:
            cite_key = normalize_text(pi["citation"])[:120]
            if cite_key and cite_key in seen_pi_citations:
                is_dupe = True
            else:
                seen_pi_citations[cite_key] = pi["number"]
        if is_dupe:
            pi_dupes.append(pi)
        else:
            deduped_pi.append(pi)

    if pi_dupes:
        print(f"Removed PI entries (broken + duplicates): {len(pi_dupes)}")
        for d in pi_dupes:
            reason = "broken" if d["broken"] else "duplicate"
            print(f"  #{d['number']}: {d['label'][:50]}  [{reason}]")

    pi_entries = deduped_pi

    # Deduplicate AB entries: when two entries share a DOI, or have
    # very similar citations, keep the one with more content (longer text / has DOI).
    # Two-pass approach: first collect all entries by DOI, then pick best.
    ab_by_doi = {}
    for i, ab in enumerate(ab_entries):
        if ab["doi"]:
            ab_by_doi.setdefault(ab["doi"], []).append(i)

    # Mark indices to remove (keep the longest entry for each DOI group)
    remove_ab = set()
    for doi, indices in ab_by_doi.items():
        if len(indices) > 1:
            # Keep the one with longest text
            best = max(indices, key=lambda i: len(ab_entries[i]["text"]))
            for idx in indices:
                if idx != best:
                    remove_ab.add(idx)

    # Also check for citation-text duplicates among remaining entries
    # (catches pairs where one copy lacks DOI but is the same paper)
    # Only consider non-chapter entries; require very high similarity (>0.85)
    remaining = [i for i in range(len(ab_entries)) if i not in remove_ab]
    sy_groups = {}
    for i in remaining:
        ab = ab_entries[i]
        # Skip chapter entries — they share author+year but are distinct
        if ab["chapter"] and ab["chapter"] > 0:
            continue
        sn = normalize_surname_for_matching(ab["surname"])
        yr = ab["year"]
        sy_groups.setdefault((sn, yr), []).append(i)

    for key, indices in sy_groups.items():
        if len(indices) < 2:
            continue
        # Pairwise comparison within group
        for a in range(len(indices)):
            if indices[a] in remove_ab:
                continue
            for b in range(a + 1, len(indices)):
                if indices[b] in remove_ab:
                    continue
                cite_a = normalize_text(ab_entries[indices[a]]["citation"])
                cite_b = normalize_text(ab_entries[indices[b]]["citation"])
                # Use high threshold to avoid false dedup of different papers
                sim = SequenceMatcher(None, cite_a, cite_b).ratio()
                if sim > 0.85:
                    # Keep the one with more content
                    if len(ab_entries[indices[b]]["text"]) > len(ab_entries[indices[a]]["text"]):
                        remove_ab.add(indices[a])
                    else:
                        remove_ab.add(indices[b])

    ab_dupes = [ab_entries[i] for i in sorted(remove_ab)]
    deduped_ab = [ab_entries[i] for i in range(len(ab_entries)) if i not in remove_ab]

    if ab_dupes:
        print(f"Duplicate AB entries removed: {len(ab_dupes)}")
        for d in ab_dupes:
            print(f"  #{d['number']}: {d['surname']} ({d['year']})  DOI={d['doi']}")

    ab_entries = deduped_ab

    # Match
    matched, unmatched_pi, unmatched_ab, stats = match_entries(pi_entries, ab_entries)

    print(f"\n=== Matching Report ===")
    print(f"DOI matches:        {stats['doi']}")
    print(f"Surname+Year:       {stats['surname_year']}")
    print(f"Fuzzy:              {stats['fuzzy']}")
    print(f"Total matched:      {stats['total_matched']}")
    print(f"Unmatched PI:       {stats['unmatched_pi']} (broken/dropped)")
    print(f"Unmatched AB:       {stats['unmatched_ab']}")

    if unmatched_pi:
        print(f"\n--- Unmatched paper_index entries (will be dropped) ---")
        for e in unmatched_pi:
            print(f"  #{e['number']}: {e['label'][:60]}  [{e['surname']}, {e['year']}]")

    if unmatched_ab:
        print(f"\n--- Unmatched annotated_bibliography entries ---")
        for e in unmatched_ab:
            print(f"  #{e['number']}: {e['surname']} ({e['year']})  DOI={e['doi']}")

    # Sort
    matched.sort(key=sort_key)

    print(f"\n=== Sort Preview (first 15) ===")
    for i, (pi, ab) in enumerate(matched[:15], 1):
        print(f"  {i:3d}. {ab['surname'][:25]:<25s} ({ab['year']})  [PI: #{pi['number']}, AB: #{ab['number']}]")
    print(f"  ...")
    print(f"=== Sort Preview (last 10) ===")
    for i, (pi, ab) in enumerate(matched[-10:], len(matched) - 9):
        print(f"  {i:3d}. {ab['surname'][:25]:<25s} ({ab['year']})  [PI: #{pi['number']}, AB: #{ab['number']}]")

    if dry_run:
        print(f"\nDry run complete. {len(matched)} entries would be written.")
        return

    # Backup
    shutil.copy2(PI_PATH, PI_PATH.with_suffix(".md.bak"))
    shutil.copy2(AB_PATH, AB_PATH.with_suffix(".md.bak"))
    print(f"\nBackups created: *.md.bak")

    # Renumber and collect
    pi_sorted = []
    ab_sorted = []
    for new_num, (pi, ab) in enumerate(matched, 1):
        pi_sorted.append(rewrite_entry_number(pi["text"], new_num))
        ab_sorted.append(rewrite_entry_number(ab["text"], new_num))

    # Update footer
    new_total = len(matched)
    pi_footer = update_summary_stats(pi_footer, new_total, {})

    # Rebuild and write
    pi_out = rebuild_file(pi_preamble, pi_sorted, pi_footer, "pi")
    ab_out = rebuild_file(ab_preamble, ab_sorted, ab_footer, "ab")

    PI_PATH.write_text(pi_out, encoding="utf-8")
    AB_PATH.write_text(ab_out, encoding="utf-8")

    print(f"\nWrote {len(matched)} entries to both files.")
    print(f"  paper_index.md:           {len(pi_out)} chars")
    print(f"  annotated_bibliography.md: {len(ab_out)} chars")


if __name__ == "__main__":
    main()
