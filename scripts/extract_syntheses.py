#!/usr/bin/env python3
"""
Extract a compressed verdict briefing from 'Facet Patterns - Syntheses.docx'.

Keeps:
  - Step 3: Convergence tables + proposed groupings (full)
  - Step 4: Misbehaving facets (full)
  - Step 5: Domain coherence assessments (full)
  - Step 6: Evidence gaps (full)
  - Cross-domain anomalies list (full)

Compresses:
  - Step 1: Full facet profiles → one-line dissociation flag summary per facet
  - Step 2: Three clusterings → verdict line only per clustering

Cuts:
  - Appendices, transparency notes, orientation sections
  - Raw study citations embedded in prose (kept as-is in retained sections;
    no automatic stripping since they're interleaved with verdicts)
"""

import re
from pathlib import Path
from docx import Document
from docx.table import Table
from docx.oxml.ns import qn

# ---------------------------------------------------------------------------
# Document traversal — paragraphs AND tables in order
# ---------------------------------------------------------------------------

def iter_block_items(parent):
    """
    Yield paragraphs and tables from a document body in document order.
    python-docx doesn't natively interleave these, so we walk the XML.
    """
    body = parent.element.body
    for child in body:
        if child.tag == qn('w:p'):
            yield parent.paragraphs[list(body.iterchildren(qn('w:p'))).index(child)]
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)


def table_to_text(table: Table) -> str:
    """Convert a docx Table to a compact markdown-style text table."""
    rows = []
    for row in table.rows:
        cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
        rows.append("| " + " | ".join(cells) + " |")
    if len(rows) >= 2:
        # Insert header separator after first row
        ncols = len(table.rows[0].cells)
        sep = "| " + " | ".join(["---"] * ncols) + " |"
        rows.insert(1, sep)
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Heading helpers
# ---------------------------------------------------------------------------

def heading_level(style_name: str) -> int | None:
    if style_name == "Title":
        return 0
    m = re.match(r"Heading\s+(\d+)", style_name)
    return int(m.group(1)) if m else None


def is_step_heading(text: str, level: int) -> tuple[int | None, str]:
    """Return (step_number, step_title) if this is a Step N heading."""
    m = re.match(r"Step\s+(\d+)\s*[:\-–—]\s*(.*)", text, re.IGNORECASE)
    if m and level == 2:
        return int(m.group(1)), m.group(2).strip()
    return None, ""


# ---------------------------------------------------------------------------
# Step 1 compression: extract dissociation flags only
# ---------------------------------------------------------------------------

def compress_step1(blocks: list) -> list[str]:
    """
    From Step 1 blocks, extract one line per facet with its dissociation flags.
    Facets are H3 headings; dissociation flags follow the label "Dissociation flags:".
    """
    lines = []
    current_facet = None
    capturing_flags = False
    flag_text_parts = []

    def flush_facet():
        nonlocal current_facet, capturing_flags, flag_text_parts
        if current_facet:
            flag_text = " ".join(flag_text_parts).strip()
            if flag_text:
                lines.append(f"  {current_facet}: {flag_text}")
            else:
                lines.append(f"  {current_facet}: No dissociation flags noted.")
        current_facet = None
        capturing_flags = False
        flag_text_parts = []

    for block in blocks:
        if isinstance(block, Table):
            continue
        text = block.text.strip()
        if not text:
            continue

        level = heading_level(block.style.name)

        if level == 3:
            flush_facet()
            current_facet = text
            capturing_flags = False
            flag_text_parts = []
        elif level is not None:
            # Any other heading ends the facet
            flush_facet()
        elif current_facet:
            if text.lower().startswith("dissociation flag"):
                capturing_flags = True
            elif capturing_flags:
                flag_text_parts.append(text)
            # If we see the next labeled section, stop capturing flags
            if re.match(r"^(Heritability|Developmental|Structural|Cross-domain)", text):
                if capturing_flags and text.lower().startswith(("heritability", "developmental", "structural")):
                    capturing_flags = False

    flush_facet()
    return lines


# ---------------------------------------------------------------------------
# Step 2 compression: extract verdict lines only
# ---------------------------------------------------------------------------

def compress_step2(blocks: list) -> list[str]:
    """
    From Step 2 blocks, extract the clustering verdict for each clustering (A/B/C).
    Verdict patterns:
      - "Clustering A: ..." or "Clustering B:" followed by a table
      - "Clustering from genetic evidence:" followed by group descriptions
      - "If forced to produce a grouping: ..."
    Also capture verdict tables.
    """
    lines = []
    current_clustering = None
    capturing_verdict = False
    in_group_descriptions = False

    for block in blocks:
        if isinstance(block, Table):
            if capturing_verdict:
                lines.append(table_to_text(block))
                capturing_verdict = False
            continue

        text = block.text.strip()
        if not text:
            continue

        level = heading_level(block.style.name)

        if level == 3:
            # New clustering heading
            current_clustering = text
            lines.append(f"\n  {text}")
            capturing_verdict = False
            in_group_descriptions = False
        elif level is not None and level <= 2:
            current_clustering = None
            capturing_verdict = False
            in_group_descriptions = False
        elif current_clustering:
            # Look for verdict line
            if re.match(r"^Clustering\s+[A-C]\s*:", text, re.IGNORECASE):
                lines.append(f"    Verdict: {text}")
                capturing_verdict = True
                in_group_descriptions = False
            elif re.match(r"^Clustering from genetic evidence", text, re.IGNORECASE):
                lines.append(f"    Verdict: {text}")
                in_group_descriptions = True
                capturing_verdict = False
            elif re.match(r"^If forced to produce", text, re.IGNORECASE):
                lines.append(f"    {text}")
            elif in_group_descriptions and re.match(r"^Group\s+[A-Z]\d", text):
                lines.append(f"    {text}")
            elif re.match(r"^(Group\s+[GS]\d|{)", text) and capturing_verdict:
                lines.append(f"    {text}")

    return lines


# ---------------------------------------------------------------------------
# Full section extraction (Steps 3-6, cross-domain)
# ---------------------------------------------------------------------------

def extract_full_section(blocks: list) -> list[str]:
    """Extract all content from a section, including tables."""
    lines = []
    for block in blocks:
        if isinstance(block, Table):
            lines.append("")
            lines.append(table_to_text(block))
            lines.append("")
        else:
            text = block.text.strip()
            if not text:
                continue
            level = heading_level(block.style.name)
            if level is not None:
                if level <= 1:
                    lines.append(f"\n{'=' * 72}")
                    lines.append(text)
                    lines.append('=' * 72)
                elif level == 2:
                    lines.append(f"\n{'─' * 60}")
                    lines.append(text)
                    lines.append('─' * 60)
                elif level == 3:
                    lines.append(f"\n### {text}")
                elif level == 4:
                    lines.append(f"\n#### {text}")
            else:
                lines.append(text)
    return lines


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------

def main():
    script_dir = Path(__file__).parent
    docx_path = script_dir / "Facet Patterns - Syntheses.docx"
    if not docx_path.exists():
        print(f"Error: {docx_path} not found")
        return

    print(f"Reading {docx_path.name}...")
    doc = Document(str(docx_path))

    # Build ordered list of all blocks (paragraphs + tables)
    all_blocks = list(iter_block_items(doc))
    print(f"  {len(all_blocks)} blocks total")

    # Segment into sections by tracking headings
    # We need to identify: Title, H1 (domain synthesis), H2 (step headings)
    output_lines = []
    i = 0

    while i < len(all_blocks):
        block = all_blocks[i]

        if isinstance(block, Table):
            i += 1
            continue

        text = block.text.strip()
        if not text:
            i += 1
            continue

        level = heading_level(block.style.name)

        # Title level — domain separator
        if level == 0:
            output_lines.append("")
            output_lines.append("=" * 72)
            output_lines.append(f"DOMAIN: {text.upper()}")
            output_lines.append("=" * 72)
            i += 1
            continue

        # H1 — synthesis heading
        if level == 1:
            output_lines.append("")
            output_lines.append(f"## {text}")
            i += 1
            continue

        # H2 — could be a step heading or other section
        if level == 2:
            step_num, step_title = is_step_heading(text, level)

            if step_num is not None:
                # Collect all blocks belonging to this step (until next H2 or H1)
                step_blocks = []
                j = i + 1
                while j < len(all_blocks):
                    b = all_blocks[j]
                    if isinstance(b, Table):
                        step_blocks.append(b)
                        j += 1
                        continue
                    bl = heading_level(b.style.name)
                    if bl is not None and bl <= 2:
                        break
                    step_blocks.append(b)
                    j += 1

                if step_num == 1:
                    output_lines.append(f"\n--- Step 1: Facet Profiles (dissociation flags only) ---")
                    compressed = compress_step1(step_blocks)
                    output_lines.extend(compressed)
                elif step_num == 2:
                    output_lines.append(f"\n--- Step 2: Clusterings (verdicts only) ---")
                    compressed = compress_step2(step_blocks)
                    output_lines.extend(compressed)
                elif step_num in (3, 4, 5, 6):
                    label = {3: "Convergence Assessment",
                             4: "Misbehaving Facets",
                             5: "Domain Coherence",
                             6: "Evidence Gaps"}[step_num]
                    output_lines.append(f"\n--- Step {step_num}: {label} ---")
                    extracted = extract_full_section(step_blocks)
                    output_lines.extend(extracted)

                i = j
                continue

            # Check for cross-domain sections we want to keep
            elif any(kw in text.lower() for kw in [
                "cross-domain facet clustering",
                "recurring structural motif",
                "evidence that domain boundaries",
                "cross-domain anomalies",
                "quality-weighted conflict",
                "synthesis: what cross-domain",
                "evidence gaps",
                "domain coherence ranking",
                "cross-domain genetic bridge",
            ]):
                # Collect section
                section_blocks = []
                j = i + 1
                while j < len(all_blocks):
                    b = all_blocks[j]
                    if isinstance(b, Table):
                        section_blocks.append(b)
                        j += 1
                        continue
                    bl = heading_level(b.style.name)
                    if bl is not None and bl <= 2:
                        break
                    section_blocks.append(b)
                    j += 1

                output_lines.append(f"\n{'─' * 60}")
                output_lines.append(text)
                output_lines.append('─' * 60)
                extracted = extract_full_section(section_blocks)
                output_lines.extend(extracted)
                i = j
                continue

            # Skip: Orientation, Appendix, Transparency Notes, NEO-PI-R Facets list, etc.
            else:
                # Skip this section
                j = i + 1
                while j < len(all_blocks):
                    b = all_blocks[j]
                    if isinstance(b, Table):
                        j += 1
                        continue
                    bl = heading_level(b.style.name)
                    if bl is not None and bl <= 2:
                        break
                    j += 1
                i = j
                continue

        i += 1

    # Write output
    out_path = script_dir / "facet_syntheses.txt"
    out_path.write_text("\n".join(output_lines) + "\n", encoding="utf-8")

    line_count = len(output_lines)
    print(f"  Output: {out_path} ({line_count} lines)")
    print("Done.")


if __name__ == "__main__":
    main()
