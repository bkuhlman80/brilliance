# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this workspace.

## Project Overview

A multi-topic research workspace for systematic literature analysis. Topics include personality structure (Big Five facets), cognitive neuroscience, attention, memory, heuristics & biases, rationality & judgment, psychometrics, and more as they emerge.

## Workspace Structure

```
smithers/
├── inbox/                  ← drop new PDFs here for processing
├── processed/              ← PDFs after indexing/extraction
├── tasks/                  ← analytical plans & research questions (flat, cross-topic)
├── extractions/            ← internal analytical documents, organized by artifact type
│   ├── field_reconnaissance/   ← Claude deep-research field surveys (cross-topic)
│   ├── source_cards/           ← NotebookLM bibliographic source-card extractions for HPAM
│   ├── hypothesis_tests/       ← Bright Triad / BRILLIANCE H1–H10 hypothesis tests
│   ├── cross_instrument_mapping/  ← Subscale crosswalks, correlation matrices, references
│   ├── domain_syntheses/       ← Personality facet patterns, developmental syntheses
│   ├── verifications/          ← Targeted fact-checking and contradiction analyses
│   └── dialogues/              ← Brian–Claude conversational artifacts
├── References/             ← study indexes, quality ratings, instrument mappings (flat)
│   ├── paper_index.md      ← master index of all papers (includes quality ratings)
│   ├── annotated_bibliography.md
│   └── ...                 ← subscale/instrument crosswalks
├── Summaries/              ← analytical syntheses & deliverables (flat)
├── scripts/                ← utility scripts
│   ├── build_index.py      ← rebuilds references.db from markdown files
│   ├── references.db       ← SQLite read cache (gitignored, generated)
│   └── align_references.py ← aligns numbering between reference files
└── CLAUDE.md
```

## Workflow

1. New PDFs go in `inbox/`
2. Process them → add entries to both reference files:
   - `References/paper_index.md` (metadata + quality ratings inline)
   - `References/annotated_bibliography.md` (full annotation)
   - If the publication source/journal is not identifiable from the PDF, do a quick web search to confirm it before rating
3. Move PDFs to `processed/`
4. Deeper analytical outputs go to the appropriate `extractions/<artifact-type>/` folder. Internal documents in `extractions/` also get paper_index + annotated_bibliography entries (numbered 711+, marked `Quality: N/A — internal`).
5. After adding/editing entries, rebuild the SQLite index: `python3 scripts/build_index.py`

## SQLite Reference Index

`scripts/references.db` is a read cache over the two markdown reference files. It enables instant queries instead of grep marathons.

**Rebuild:** `python3 scripts/build_index.py` (or `--stats` for tag/purpose distributions)

**Key tables:**
- `papers` — one row per entry (654 papers), with fields from both files + line references back to source
- `tags` — many-to-many tag associations (source: `theory` | `keyword` | `topic`)
- `quality_ratings` — claim-type ratings (Structural, Developmental, etc.)
- `papers_fts` — FTS5 full-text search across citation, notes, key_terms, core_themes, topic

**Example queries:**
```sql
-- Find papers by theory tag
SELECT id, first_author, year, substr(citation, 1, 80)
FROM papers WHERE id IN (SELECT paper_id FROM tags WHERE tag = 'attachment-theory');

-- Full-text search
SELECT id, first_author, year, snippet(papers_fts, 3, '>>>', '<<<', '...', 20)
FROM papers_fts JOIN papers ON papers.id = papers_fts.id
WHERE papers_fts MATCH 'allostasis AND prediction';

-- Papers rated XL on any claim
SELECT p.id, p.first_author, p.year, q.claim_type, q.rating
FROM quality_ratings q JOIN papers p ON p.id = q.paper_id
WHERE q.rating = 'XL';

-- All theory tags and their counts
SELECT tag, COUNT(*) FROM tags WHERE source = 'theory' GROUP BY tag ORDER BY COUNT(*) DESC;
```

## Study Quality T-Shirt Sizing Rubric

Ratings reflect methodological weight per claim type, not importance of findings. Rate each claim type the study actually addresses — leave others as "—".

- **XL** — Gold standard (large N, appropriate design, strong controls, replication)
- **L** — Strong (moderate-to-large N, appropriate design, some limitations)
- **M** — Adequate (informative but should not be trusted alone)
- **S** — Use with caution (underpowered or design limitations threaten claims)

### Claim-type guidelines

**Developmental** (mean-level change, stability, trajectories):
- XL: Large meta-analysis of longitudinal studies OR multiple independent longitudinal panels
- L: Multi-wave longitudinal (3+ waves), N ≥ 500
- M: Cross-sectional age comparisons (even with large N) OR 2-wave longitudinal OR very small longitudinal N
- S: Single-wave cross-sectional with small N or severe cohort confounds

**Structural** (factor structure, convergent/discriminant validity):
- XL: Multiple independent samples with cross-validation, standard instrument, broad facet coverage
- L: Large N OR multi-sample, standard instrument
- M: Non-standard instrument, single domain only, or low reliability
- S: Exploratory analysis on a single small sample

**Heritability** (univariate genetic/environmental variance decomposition):
- XL: Large twin/pedigree sample (1,000+ pairs) or meta-analysis of twin studies
- L: Twin study with 500+ pairs, ideally cross-cultural replication
- M: Twin study with 250–500 pairs, or adequate N but selective facet coverage
- S: < 250 pairs or design features that compromise estimates (e.g., no DZ comparison)

**Genetic correlations** (multivariate genetic models, cross-trait genetic overlap):
- L: Multivariate genetic models with 500+ pairs or large pedigree/GWAS
- M: Multivariate models with moderate N (250–500 pairs) or selective trait coverage
- S: Small N with wide CIs, single candidate-gene studies, or no multiple-testing correction

**Life-event** (effects of specific events on personality):
- L: Prospective longitudinal with pre/post measurement, adequate N for the event
- M: Retrospective or 2-wave with modest event-group N
- S: Severely underpowered event subgroup or no pre-event baseline

**Publication prestige** (non-empirical work: reviews, book chapters, commentaries — NOT meta-analyses):
- XL: Annual Review chapter, major handbook chapter (e.g., Handbook of Personality), or review in a top-tier outlet (Psychological Bulletin, PSPR)
- L: Chapter in a well-regarded edited volume, review in a strong specialty journal
- M: Standard journal review/commentary, chapter in a niche volume
- S: Commentary in a minor outlet, non-peer-reviewed piece, conference proceeding

### Downgrade flags

Apply these regardless of N when relevant:
- Non-standard or short-form instrument with low facet reliability (α < .60)
- Domain-level only — note "no facet data" in design notes
- Single sociocultural context for claims requiring generalizability
- Self-report only when claim requires method separation
- Preprint / not yet peer-reviewed

## Trellis website copy contract (two-tool ownership)

The `website/` site is built by two tools with a hard split to prevent copy
drift. Full contract in [website/README.md](website/README.md). The Code tool's
obligations:

- **Own the words.** All copy the Code tool edits lives in `website/framework-data.js`
  (cell/region prose) or `website/ui-copy.js` (chrome microcopy). Never edit
  `website/Bramble Explorer.dc.html` — that file belongs to the Design tool.
- **Never take a Design bundle's data file.** When integrating a Design handoff,
  copy in *only* `Bramble Explorer.dc.html` (+ `runtime/` if changed). Do NOT
  overwrite `framework-data.js` or `ui-copy.js` from the bundle — doing so is the
  exact regression that reverted Impetus→Boldness (commit e939769).
- **Build + deploy belong to the Code tool:** `python3 website/build_site.py`
  then `wrangler pages deploy website/site --project-name trellis-framework --branch main`.
- If a design change needs a new label/key, the Code tool adds it to the data
  file; Design never ships data to supply it.

## Conventions

- All text files use `.md` extension (not `.txt`)
- `paper_index.md` and `annotated_bibliography.md` are the authoritative cross-references; each entry has a Topic field
- `extractions/` is organized by artifact type (field_reconnaissance, source_cards, hypothesis_tests, cross_instrument_mapping, domain_syntheses, verifications, dialogues), not by topic; `tasks/`, `References/`, and `Summaries/` are flat
