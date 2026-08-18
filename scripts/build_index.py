#!/usr/bin/env python3
"""
Build a SQLite read cache (references.db) from paper_index.md and
annotated_bibliography.md.

Markdown files remain the source of truth. This script is idempotent —
run it after any edit to the markdown files to rebuild the DB.

Usage:
    python scripts/build_index.py           # build/rebuild
    python scripts/build_index.py --stats   # rebuild + print tag stats
"""

import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE = Path(__file__).resolve().parent.parent
REF_DIR = BASE / "References"
PI_PATH = REF_DIR / "paper_index.md"
AB_PATH = REF_DIR / "annotated_bibliography.md"
DB_PATH = BASE / "scripts" / "references.db"

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

ENTRY_RE = re.compile(r"^### \d+[a-z]?\. ", re.MULTILINE)
DOI_RE = re.compile(r"https?://doi\.org/(\S+)")
YEAR_RE = re.compile(r"\((\d{4})\)")


def split_entries(text):
    """Split markdown into (preamble, [(line_number, entry_text), ...], footer).

    Footer is everything after '## Summary Statistics' (paper_index only).
    """
    footer = ""
    footer_match = re.search(r"\n---\n\n## Summary Statistics.*", text, re.DOTALL)
    if footer_match:
        footer = text[footer_match.start():]
        text = text[:footer_match.start()]

    # Map character positions to line numbers
    line_starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_starts.append(i + 1)

    def char_to_line(pos):
        lo, hi = 0, len(line_starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if line_starts[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1  # 1-indexed

    starts = [(m.start(), m) for m in ENTRY_RE.finditer(text)]
    if not starts:
        return text, [], footer

    preamble = text[: starts[0][0]]
    entries = []
    for i, (pos, m) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        entries.append((char_to_line(pos), text[pos:end]))

    return preamble, entries, footer


def extract_field(entry_text, field_name, has_dash_prefix=True):
    """Extract a field value, handling multi-line continuation."""
    if has_dash_prefix:
        pattern = re.compile(
            rf"^-\s*\*\*{re.escape(field_name)}:\*\*\s*(.*)",
            re.MULTILINE,
        )
    else:
        pattern = re.compile(
            rf"^\*\*{re.escape(field_name)}:\*\*\s*(.*)",
            re.MULTILINE,
        )

    m = pattern.search(entry_text)
    if not m:
        return ""

    value = m.group(1).strip()
    # Collect continuation lines (indented or plain text, not a new field)
    rest = entry_text[m.end():]
    for line in rest.split("\n"):
        stripped = line.strip()
        if not stripped:
            break
        # Stop if we hit another field header or a section header
        if re.match(r"^-?\s*\*\*\w", stripped) or stripped.startswith("#"):
            break
        value += " " + stripped

    return value.strip()


def extract_section(entry_text, section_header):
    """Extract everything under a #### header until next header or ---."""
    pattern = re.compile(
        rf"^####\s+{re.escape(section_header)}\s*\n(.*?)(?=^####|\n---|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(entry_text)
    if m:
        return m.group(1).strip()
    return ""


def extract_entry_number(entry_text):
    m = re.match(r"^### (\d+)[a-z]?\. ", entry_text)
    return int(m.group(1)) if m else None


def extract_doi(text):
    m = DOI_RE.search(text)
    if m:
        return m.group(1).rstrip(".,;:)")
    return ""


def extract_year(citation):
    m = YEAR_RE.search(citation)
    return int(m.group(1)) if m else None


def extract_first_author(citation):
    """Extract surname of first author."""
    if not citation:
        return ""
    before_comma = re.split(r",|\(", citation)[0].strip().rstrip(".")
    return before_comma


def extract_sample_size(quality_text):
    """Pull N = X,XXX from quality field."""
    m = re.search(r"N\s*[=≈~]\s*([\d,]+)", quality_text)
    return m.group(0) if m else ""


def extract_relevance(entry_text):
    """Extract relevance rating from annotated bibliography entry."""
    m = re.search(
        r"\*\*Relevance to Book Project:\*\*\s*(HIGH|MODERATE|LOW|TANGENTIAL)",
        entry_text,
    )
    return m.group(1) if m else ""


def extract_key_terms(entry_text):
    """Extract key terms block from annotated bibliography."""
    block = extract_section(entry_text, "Key Terms") if "#### Key Terms" in entry_text else ""
    if not block:
        # Key terms might be under **Key Terms:** field instead of a section
        m = re.search(
            r"\*\*Key Terms:\*\*\s*\n(.*?)(?=\n####|\n\*\*|\n---|\Z)",
            entry_text,
            re.DOTALL,
        )
        if m:
            block = m.group(1).strip()
    # Also check for inline key terms
    if not block:
        # Try the pattern with sub-bullets
        m = re.search(
            r"\*Paper keywords:\*\s*(.*?)(?:\n-\s*\*Additional terms:\*\s*(.*?))?(?:\n\n|\n####|\n---|\Z)",
            entry_text,
            re.DOTALL,
        )
        if m:
            parts = [m.group(1).strip()]
            if m.group(2):
                parts.append(m.group(2).strip())
            block = "; ".join(parts)

    return block


# ---------------------------------------------------------------------------
# Quality rating extraction
# ---------------------------------------------------------------------------

QUALITY_CLAIM_RE = re.compile(
    r"(Structural|Developmental|Heritability|Genetic[/ ]?correlations?|"
    r"Life[- ]?event|Publication [Pp]restige|Prestige):\s*(XL|L|M|S)\b",
    re.IGNORECASE,
)


def extract_quality_ratings(quality_text):
    """Return list of (claim_type, rating) tuples."""
    ratings = []
    for m in QUALITY_CLAIM_RE.finditer(quality_text):
        claim = m.group(1).strip()
        # Normalize
        claim = claim.replace("Publication prestige", "Prestige")
        claim = claim.replace("Publication Prestige", "Prestige")
        if claim.lower().startswith("genetic"):
            claim = "Genetic correlations"
        if claim.lower().startswith("life"):
            claim = "Life-event"
        rating = m.group(2).upper()
        ratings.append((claim, rating))
    return ratings


# ---------------------------------------------------------------------------
# Theory/framework tag taxonomy
# ---------------------------------------------------------------------------

# Each entry: (tag_name, [list of keyword patterns])
# Patterns are case-insensitive; matched against core_themes + notes + key_terms + topic

THEORY_TAGS = [
    # Motivational / Drive theories
    ("approach-avoidance", [r"approach.avoidance", r"behavioral approach", r"behavioral inhibition"]),
    ("reinforcement-sensitivity", [r"reinforcement sensitivity", r"BIS.BAS", r"Gray.s.*theory", r"behavioral activation system", r"behavioral inhibition system"]),
    ("incentive-salience", [r"incentive salience", r"wanting.*liking", r"liking.*wanting", r"Berridge"]),
    ("self-determination-theory", [r"self.determination theory", r"SDT", r"Deci.*Ryan", r"Ryan.*Deci", r"basic psychological needs"]),
    ("intrinsic-motivation", [r"intrinsic motivation", r"intrinsic reward", r"intrinsic reinforcement"]),
    ("need-for-cognition", [r"need for cognition", r"epistemic curiosity", r"epistemic motivation"]),
    ("achievement-motivation", [r"achievement motivation", r"need for achievement", r"McClelland.*achievement"]),
    ("regulatory-focus", [r"regulatory focus", r"promotion.focus", r"prevention.focus", r"Higgins.*regulatory"]),
    ("drive-theory", [r"drive theory", r"secondary drive", r"Hull.*drive", r"cupboard love"]),

    # Evolutionary / Biological
    ("life-history-theory", [r"life.history theory", r"life.history strat", r"fast.slow continuum", r"r/K selection", r"pace.of.life"]),
    ("frequency-dependent-selection", [r"frequency.dependent selection", r"negative frequency"]),
    ("self-domestication", [r"self.domestication", r"survival of the friendliest", r"Hare.*domestication"]),
    ("sexual-selection", [r"sexual selection", r"mate choice", r"intrasexual competition", r"intersexual"]),
    ("inclusive-fitness", [r"inclusive fitness", r"kin selection", r"Hamilton.*rule"]),
    ("gene-environment", [r"gene.environment", r"GxE", r"G\s*[×x]\s*E", r"diathesis.stress"]),
    ("behavioral-ecology", [r"behavioral ecology", r"optimal foraging", r"energy budget", r"metabolic.*personality"]),
    ("evolutionary-psychology", [r"evolutionary psychology", r"evolved.*mechanism", r"ancestral.*adaptive", r"domain.specific.*module"]),
    ("fundamental-social-motives", [r"fundamental social motives", r"Kenrick.*motives", r"mate retention.*kin care"]),

    # Emotion / Affect
    ("basic-emotions", [r"basic emotion", r"primary emotion", r"Panksepp", r"SEEKING.*RAGE.*FEAR", r"affective neuroscience", r"Ekman.*basic"]),
    ("constructed-emotion", [r"constructed emotion", r"Barrett.*emotion", r"theory of constructed", r"psychological construction"]),
    ("appraisal-theory", [r"appraisal theory", r"cognitive appraisal", r"Lazarus.*appraisal", r"Scherer.*appraisal"]),
    ("broaden-and-build", [r"broaden.and.build", r"Fredrickson.*broaden"]),
    ("dimensional-affect", [r"valence.*arousal", r"circumplex.*affect", r"Russell.*affect", r"core affect"]),

    # Social / Interpersonal
    ("agency-communion", [r"agency.*communion", r"communion.*agency", r"warmth.*competence", r"competence.*warmth", r"Bakan.*agency", r"Big Two"]),
    ("social-brain-hypothesis", [r"social brain", r"Machiavellian intelligence", r"neocortex ratio", r"Dunbar.*number", r"Dunbar.*social"]),
    ("attachment-theory", [r"attachment theory", r"Bowlby", r"internal working model", r"secure base", r"attachment.*style", r"attachment.*anxiety", r"attachment.*avoidance"]),
    ("terror-management", [r"terror management", r"mortality salience", r"TMT", r"death.*anxiety.*buffer"]),
    ("sociometer-theory", [r"sociometer", r"Leary.*self.esteem"]),
    ("social-rank-theory", [r"social rank theory", r"defeat.*subordination", r"involuntary subordination", r"Gilbert.*rank"]),
    ("interpersonal-circumplex", [r"interpersonal circumplex", r"IPC", r"Wiggins.*circumplex", r"dominance.*affiliation"]),

    # Regulatory / Cybernetic
    ("cybernetic-big-five", [r"cybernetic big five", r"CB5T", r"DeYoung.*cybernetic"]),
    ("control-theory", [r"control theory", r"Carver.*Scheier", r"feedback loop.*goal", r"goal.corrected", r"cybernetic.*self.regulation"]),
    ("allostasis", [r"allostasis", r"allostatic load", r"predictive.*bodily regulation", r"McEwen.*stress"]),
    ("homeostasis", [r"homeostasis", r"homeostatic.*regulation"]),
    ("predictive-processing", [r"predictive processing", r"predictive coding", r"active inference", r"free energy principle", r"interoceptive prediction"]),
    ("default-mode-network", [r"default mode network", r"DMN", r"triple network", r"salience network"]),
    ("exploration-exploitation", [r"exploration.exploitation", r"explore.exploit", r"curiosity.*reinforcement"]),
    ("polyvagal", [r"polyvagal", r"Porges.*vagal", r"vagal tone"]),

    # Personality architecture
    ("CAPS", [r"cognitive.affective personality system", r"CAPS", r"Mischel.*Shoda", r"if\.\.\.then"]),
    ("five-factor-theory", [r"five.factor theory", r"McCrae.*Costa.*theory", r"FFT", r"basic tendencies.*characteristic adaptations"]),
    ("big-five", [r"Big Five", r"five.factor model", r"FFM", r"OCEAN", r"NEO.PI"]),
    ("HEXACO", [r"HEXACO", r"Ashton.*Lee.*HEXACO", r"honesty.humility"]),
    ("trait-theory", [r"trait theory", r"Allport.*trait", r"lexical hypothesis", r"lexical approach"]),
    ("dynamic-systems", [r"dynamic systems", r"dynamical systems", r"attractor.*personality", r"nonlinear.*personality"]),
    ("whole-trait-theory", [r"whole trait theory", r"Fleeson.*whole"]),
    ("PARCS", [r"PARCS", r"Predictive and Reactive Control"]),

    # Cognitive
    ("dual-process", [r"dual.process", r"System 1.*System 2", r"Type 1.*Type 2", r"heuristic.*analytic", r"fast.*slow.*thinking"]),
    ("heuristics-and-biases", [r"heuristic.*bias", r"cognitive bias", r"Kahneman.*Tversky", r"judgment.*decision"]),
    ("bounded-rationality", [r"bounded rationality", r"satisfic", r"Simon.*rationality", r"ecological rationality"]),
    ("cognitive-decoupling", [r"cognitive decoupling", r"hypothetical thinking", r"Stanovich.*reflective"]),
    ("intelligence-theories", [r"CHC", r"Cattell.Horn.Carroll", r"g.factor", r"general intelligence", r"fluid.*crystallized", r"Spearman.*g"]),

    # Development
    ("developmental-plasticity", [r"developmental plasticity", r"phenotypic plasticity", r"plasticity.*development"]),
    ("sensitive-periods", [r"sensitive period", r"critical period", r"programming effect"]),
    ("differential-susceptibility", [r"differential susceptibility", r"Belsky.*susceptibility", r"for better.*for worse", r"biological sensitivity to context", r"vantage sensitivity"]),

    # Additional discovered theories
    ("dopamine-prediction-error", [r"prediction error", r"temporal difference.*learning", r"TD learning", r"reward prediction", r"dopamine.*prediction"]),
    ("object-relations", [r"object relations", r"Kernberg", r"internal.*representation.*self.*other"]),
    ("PSI-theory", [r"PSI theory", r"personality systems interaction", r"Kuhl.*PSI"]),
]


def generate_theory_tags(text_blob):
    """Return set of theory tags that match the combined text."""
    tags = set()
    for tag_name, patterns in THEORY_TAGS:
        for pat in patterns:
            if re.search(pat, text_blob, re.IGNORECASE):
                tags.add(tag_name)
                break
    return tags


def generate_keyword_tags(key_terms_text):
    """Split key terms into individual normalized tags."""
    tags = set()
    if not key_terms_text:
        return tags
    # Remove sub-headers like "*Paper keywords:*" and "*Additional terms:*"
    cleaned = re.sub(r"\*[^*]+\*:?\s*", "", key_terms_text)
    # Split on commas and semicolons
    for term in re.split(r"[,;]", cleaned):
        term = term.strip().strip("-").strip()
        if term and len(term) > 1 and len(term) < 80:
            tags.add(term.lower())
    return tags


def generate_topic_tags(topic_text):
    """Normalize topic field into tags."""
    tags = set()
    if not topic_text:
        return tags
    for part in re.split(r"[,/]", topic_text):
        part = part.strip()
        if part:
            tag = re.sub(r"\s+", "-", part.lower())
            tag = re.sub(r"[^a-z0-9-]", "", tag)
            if tag and len(tag) > 1:
                tags.add(tag)
    return tags


# ---------------------------------------------------------------------------
# Database creation
# ---------------------------------------------------------------------------

SCHEMA = """
DROP TABLE IF EXISTS papers_fts;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS quality_ratings;
DROP TABLE IF EXISTS papers;

CREATE TABLE papers (
    id              INTEGER PRIMARY KEY,
    filename        TEXT,
    citation        TEXT,
    doi             TEXT,
    first_author    TEXT,
    year            INTEGER,
    purpose         TEXT,
    methodology     TEXT,
    instruments     TEXT,
    level_of_detail TEXT,
    quality_raw     TEXT,
    sample_size     TEXT,
    topic           TEXT,
    notes           TEXT,
    key_terms       TEXT,
    core_themes     TEXT,
    relevance       TEXT,
    pi_line         INTEGER,
    ab_line         INTEGER
);

CREATE TABLE quality_ratings (
    paper_id   INTEGER REFERENCES papers(id),
    claim_type TEXT,
    rating     TEXT,
    PRIMARY KEY (paper_id, claim_type)
);

CREATE TABLE tags (
    paper_id INTEGER REFERENCES papers(id),
    tag      TEXT,
    source   TEXT,
    PRIMARY KEY (paper_id, tag)
);

CREATE VIRTUAL TABLE papers_fts USING fts5(
    id UNINDEXED,
    citation,
    notes,
    key_terms,
    core_themes,
    topic,
    content=papers,
    content_rowid=id
);

CREATE INDEX idx_tags_tag ON tags(tag);
CREATE INDEX idx_tags_source ON tags(source);
CREATE INDEX idx_quality_claim ON quality_ratings(claim_type);
CREATE INDEX idx_papers_purpose ON papers(purpose);
CREATE INDEX idx_papers_year ON papers(year);
CREATE INDEX idx_papers_first_author ON papers(first_author);
"""


def build_db():
    """Parse both files and build the SQLite database."""
    print(f"Reading {PI_PATH.name}...")
    pi_text = PI_PATH.read_text(encoding="utf-8")
    _, pi_entries, _ = split_entries(pi_text)
    print(f"  {len(pi_entries)} entries parsed")

    print(f"Reading {AB_PATH.name}...")
    ab_text = AB_PATH.read_text(encoding="utf-8")
    _, ab_entries, _ = split_entries(ab_text)
    print(f"  {len(ab_entries)} entries parsed")

    # Index AB entries by number for matching
    ab_by_num = {}
    for line_num, entry_text in ab_entries:
        num = extract_entry_number(entry_text)
        if num is not None:
            ab_by_num[num] = (line_num, entry_text)

    # Build database
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.executescript(SCHEMA)

    papers_inserted = 0
    ratings_inserted = 0
    tags_inserted = 0
    parse_errors = []

    for pi_line, pi_text_entry in pi_entries:
        entry_num = extract_entry_number(pi_text_entry)
        if entry_num is None:
            parse_errors.append(f"  PI line {pi_line}: could not extract entry number")
            continue

        # Extract PI fields
        header_match = re.match(r"^### \d+[a-z]?\. (.+)", pi_text_entry)
        filename = header_match.group(1).strip() if header_match else ""
        citation = extract_field(pi_text_entry, "Citation", has_dash_prefix=True)
        doi = extract_doi(pi_text_entry)
        first_author = extract_first_author(citation)
        year = extract_year(citation)
        purpose = extract_field(pi_text_entry, "Purpose", has_dash_prefix=True)
        methodology = extract_field(pi_text_entry, "Methodology", has_dash_prefix=True)
        instruments = extract_field(pi_text_entry, "Instruments", has_dash_prefix=True)
        level_of_detail = extract_field(pi_text_entry, "Level of Detail", has_dash_prefix=True)
        quality_raw = extract_field(pi_text_entry, "Quality", has_dash_prefix=True)
        sample_size = extract_sample_size(quality_raw)
        topic = extract_field(pi_text_entry, "Topic", has_dash_prefix=True)
        notes = extract_field(pi_text_entry, "Notes", has_dash_prefix=True)

        # Extract AB fields (if matched)
        ab_line = None
        key_terms = ""
        core_themes = ""
        relevance = ""

        if entry_num in ab_by_num:
            ab_line, ab_text_entry = ab_by_num[entry_num]
            key_terms = extract_key_terms(ab_text_entry)
            core_themes = extract_section(ab_text_entry, "Core Themes")
            relevance = extract_relevance(ab_text_entry)

            # If PI fields are empty, try AB
            if not citation:
                citation = extract_field(ab_text_entry, "Citation", has_dash_prefix=False)
                doi = extract_doi(ab_text_entry)
                first_author = extract_first_author(citation)
                year = extract_year(citation)
            if not purpose:
                purpose = extract_field(ab_text_entry, "Purpose", has_dash_prefix=False)
            if not methodology:
                methodology = extract_field(ab_text_entry, "Methodology", has_dash_prefix=False)
            if not instruments:
                instruments = extract_field(ab_text_entry, "Instruments", has_dash_prefix=False)
            if not level_of_detail:
                level_of_detail = extract_field(ab_text_entry, "Level of Detail", has_dash_prefix=False)
        else:
            parse_errors.append(f"  PI #{entry_num}: no matching AB entry")

        # Insert paper
        cur.execute(
            """INSERT INTO papers (id, filename, citation, doi, first_author, year,
               purpose, methodology, instruments, level_of_detail, quality_raw,
               sample_size, topic, notes, key_terms, core_themes, relevance,
               pi_line, ab_line)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                entry_num, filename, citation, doi, first_author, year,
                purpose, methodology, instruments, level_of_detail, quality_raw,
                sample_size, topic, notes, key_terms, core_themes, relevance,
                pi_line, ab_line,
            ),
        )
        papers_inserted += 1

        # Quality ratings
        for claim_type, rating in extract_quality_ratings(quality_raw):
            cur.execute(
                "INSERT OR IGNORE INTO quality_ratings (paper_id, claim_type, rating) VALUES (?,?,?)",
                (entry_num, claim_type, rating),
            )
            ratings_inserted += 1

        # Tags
        all_tags = {}  # tag -> source

        # Theory tags (from combined narrative text)
        text_blob = " ".join(filter(None, [notes, core_themes, key_terms, topic]))
        for tag in generate_theory_tags(text_blob):
            all_tags[tag] = "theory"

        # Keyword tags (from Key Terms field)
        for tag in generate_keyword_tags(key_terms):
            if tag not in all_tags:
                all_tags[tag] = "keyword"

        # Topic tags (from Topic field)
        for tag in generate_topic_tags(topic):
            if tag not in all_tags:
                all_tags[tag] = "topic"

        for tag, source in all_tags.items():
            cur.execute(
                "INSERT OR IGNORE INTO tags (paper_id, tag, source) VALUES (?,?,?)",
                (entry_num, tag, source),
            )
            tags_inserted += 1

    # Populate FTS index
    cur.execute(
        """INSERT INTO papers_fts (id, citation, notes, key_terms, core_themes, topic)
           SELECT id, citation, notes, key_terms, core_themes, topic FROM papers"""
    )

    conn.commit()

    # Report
    print(f"\n{'='*50}")
    print(f"Database built: {DB_PATH}")
    print(f"  Papers:           {papers_inserted}")
    print(f"  Quality ratings:  {ratings_inserted}")
    print(f"  Tags:             {tags_inserted}")
    print(f"  FTS entries:      {papers_inserted}")

    if parse_errors:
        print(f"\n  Parse warnings ({len(parse_errors)}):")
        for err in parse_errors[:20]:
            print(f"    {err}")
        if len(parse_errors) > 20:
            print(f"    ... and {len(parse_errors) - 20} more")

    # Stats
    if "--stats" in sys.argv:
        print(f"\n{'='*50}")
        print("Top 30 theory tags:")
        for row in cur.execute(
            """SELECT tag, COUNT(*) as n FROM tags
               WHERE source = 'theory'
               GROUP BY tag ORDER BY n DESC LIMIT 30"""
        ):
            print(f"  {row[0]:<40s} {row[1]:>4d}")

        print(f"\nTop 20 topic tags:")
        for row in cur.execute(
            """SELECT tag, COUNT(*) as n FROM tags
               WHERE source = 'topic'
               GROUP BY tag ORDER BY n DESC LIMIT 20"""
        ):
            print(f"  {row[0]:<40s} {row[1]:>4d}")

        print(f"\nPurpose distribution:")
        for row in cur.execute(
            "SELECT purpose, COUNT(*) FROM papers GROUP BY purpose ORDER BY COUNT(*) DESC"
        ):
            print(f"  {row[0] or '(empty)':<35s} {row[1]:>4d}")

        print(f"\nRelevance distribution:")
        for row in cur.execute(
            "SELECT relevance, COUNT(*) FROM papers GROUP BY relevance ORDER BY COUNT(*) DESC"
        ):
            print(f"  {row[0] or '(empty)':<20s} {row[1]:>4d}")

    conn.close()
    print(f"\nDone.")


if __name__ == "__main__":
    build_db()
