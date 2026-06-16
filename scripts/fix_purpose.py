#!/usr/bin/env python3
"""
One-shot script to fix non-standard Purpose values in paper_index.md and
annotated_bibliography.md.

Maps each entry (by ID) to the correct standard Purpose category.
Run once, then delete this script.

Usage:
    python scripts/fix_purpose.py --dry-run   # preview
    python scripts/fix_purpose.py              # apply
"""

import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "References"
PI_PATH = BASE / "paper_index.md"
AB_PATH = BASE / "annotated_bibliography.md"

# Mapping: entry_id -> correct Purpose value
# Classified by reading methodology and notes for each entry
FIXES = {
    # Minor variants of standard categories
    17:  "Original Research",          # "(methodological)" qualifier unnecessary
    35:  "Original Research",          # "(experimental)" qualifier unnecessary
    112: "Review",                     # "Review / Instrument Validation" → primary is Review (NEO-PI-R overview)
    321: "Original Research",          # "Original Research + Meta-Analysis" → primary is original longitudinal + meta
    395: "Review",                     # "Methods / Review" → methods tutorial
    403: "Original Research",          # "Original Research, Instrument Validation" → primary is original research
    434: "Review",                     # "Review / Theory" → narrative review
    451: "Commentary/Editorial",       # "Commentary / Methods" → methods commentary
    528: "Original Research",          # "Original Research, Instrument Validation" → primary is original research
    529: "Original Research",          # "Original Research / Monograph" → original research
    538: "Original Research",          # "Original Research (Mega-Analysis)" → mega-analysis is original research
    547: "Original Research",          # "Original Research, Instrument Validation" → EEfRT development + validation
    592: "Book Chapter",              # "Book Chapter or Review (PhD Thesis)" → PhD thesis chapter

    # Full-sentence descriptions that should be standard categories
    # Determined by reading methodology field

    # Original Research entries (empirical data collection/analysis)
    71:  "Original Research",          # Bleidorn 2020 — expert-consensus + 7-sample validation
    230: "Original Research",          # Hopwood 2010 — empirical CFA/EFA comparison
    233: "Original Research",          # Hopwood 2021 — 9 studies, scale development
    234: "Original Research",          # Hopwood 2024 — longitudinal replication
    235: "Original Research",          # Hopwood 2024 — cross-sectional survey
    236: "Original Research",          # Hopwood 2025 — longitudinal CLPS modeling
    249: "Original Research",          # Ilagan 2026 — daily diary ESM
    257: "Original Research",          # Jacobsson 2024 — cross-sectional clinical
    258: "Original Research",          # Jacobsson 2026 — naturalistic longitudinal
    279: "Original Research",          # Kerber 2026 — EMA ambulatory assessment
    338: "Original Research",          # Markon 2005 — meta-analysis + empirical replication
    379: "Original Research",          # Mulay 2019 — Delphi expert rating study
    393: "Original Research",          # Nissen 2025 — ESM measurement burst
    396: "Original Research",          # Oltmanns 2026 — AI model training on interviews
    404: "Original Research",          # Pavuluri 2025 — archival data + EEG
    405: "Original Research",          # Pavuluri 2025 — SEM, two samples
    415: "Original Research",          # Pezzuti 2025 — cross-cultural experiments
    418: "Original Research",          # Pick 2022 — cross-sectional survey, 42 societies
    437: "Original Research",          # Ren 2025 — twin study
    465: "Original Research",          # Schaub 2023 — structural MRI
    467: "Original Research",          # Schmitt 2008 — cross-cultural survey
    468: "Original Research",          # Schneider 2023 — secondary analysis of RCT
    480: "Original Research",          # Sharp 2026 — prospective longitudinal
    609: "Original Research",          # Zimmermann 2015 — other-rating IRT study

    # Review entries (narrative/theoretical synthesis without new data)
    231: "Review",                     # Hopwood 2013 — theoretical review of interpersonal PD theory
    232: "Review",                     # Hopwood 2018 — theoretical review integrating models
    237: "Review",                     # Hopwood 2025 — conceptual review of AMPD constructs
    239: "Review",                     # Houeto 2016 — narrative review, dual-pathway model
    264: "Review",                     # Johnson 2012 — narrative review of BAS-mania
    287: "Review",                     # Ko 2020 — multi-study integrative review
    294: "Review",                     # Kuijper 2012 — theoretical review of models
    327: "Review",                     # MacAulay 2014 — narrative review
    345: "Instrument Validation",      # Mayer 2025 — MSCEIT 2 development + validation (5 studies)
    359: "Review",                     # Michalski 2010 — narrative review
    364: "Review",                     # Miller 2018 — narrative review of PID-5 evidence
    386: "Review",                     # Nelson 2004 — theoretical review
    420: "Review",                     # Pincus 2018 — narrative review of interpersonal theory
    503: "Review",                     # Soto 2015 — narrative review of youth personality
    556: "Review",                     # Tyrer 2019 — narrative review by ICD-11 group

    # Meta-Analysis entries
    250: "Review",                     # Iliakis 2019 — cross-national data analysis (not meta-analysis per se)
    256: "Meta-Analysis",              # Jacobsson 2021 — systematic review + meta-analysis
    548: "Meta-Analysis",              # Trevisan 2019 — meta-analysis of 44 studies

    # Theory entries (primary contribution is a new theoretical framework)
    429: "Book Chapter",               # Read 2021 — theoretical book chapter with simulations
    430: "Theory",                     # Read 2026 — computational model paper
    606: "Theory",                     # Zavlis 2026 — computational model with simulations
}


def apply_fixes(filepath, has_dash_prefix=True):
    """Fix Purpose fields in a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    changes = []

    for entry_id, correct_purpose in FIXES.items():
        # Build pattern for this entry's Purpose line
        # Paper index: `- **Purpose:** value`
        # Annotated bib: `**Purpose:** value`
        if has_dash_prefix:
            # Match the entire Purpose line within the entry (between ### headers)
            pattern = re.compile(
                rf"(### {entry_id}\. .+?\n(?:.*?\n)*?-\s*\*\*Purpose:\*\*\s*)(.+?)(\n)",
                re.DOTALL,
            )
        else:
            pattern = re.compile(
                rf"(### {entry_id}\. .+?\n(?:.*?\n)*?\*\*Purpose:\*\*\s*)(.+?)(\n)",
                re.DOTALL,
            )

        m = pattern.search(text)
        if m:
            old_purpose = m.group(2).strip()
            if old_purpose != correct_purpose:
                changes.append((entry_id, old_purpose[:60], correct_purpose))
                text = text[:m.start(2)] + correct_purpose + text[m.start(3):]

    return text, changes


def main():
    dry_run = "--dry-run" in sys.argv

    print(f"{'DRY RUN' if dry_run else 'APPLYING'}: Fix non-standard Purpose values\n")

    # Paper Index
    pi_text, pi_changes = apply_fixes(PI_PATH, has_dash_prefix=True)
    print(f"paper_index.md: {len(pi_changes)} changes")
    for eid, old, new in pi_changes:
        print(f"  #{eid}: '{old}' → '{new}'")

    # Annotated Bibliography
    ab_text, ab_changes = apply_fixes(AB_PATH, has_dash_prefix=False)
    print(f"\nannotated_bibliography.md: {len(ab_changes)} changes")
    for eid, old, new in ab_changes:
        print(f"  #{eid}: '{old}' → '{new}'")

    if dry_run:
        print(f"\nDry run complete. Would change {len(pi_changes)} + {len(ab_changes)} lines.")
        return

    PI_PATH.write_text(pi_text, encoding="utf-8")
    AB_PATH.write_text(ab_text, encoding="utf-8")
    print(f"\nFiles written. Run `python3 scripts/build_index.py` to rebuild the index.")


if __name__ == "__main__":
    main()
