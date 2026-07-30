# Directive for the next conversation — rebuild on a rigid category-sequencing spec

*This is the plan of work for the conversation Brian will open next. It is written so future-Loom
can execute it in order. Two absolute rules govern everything below.*

## The two governing rules (do not violate)

1. **SEQUENCING IS ABSOLUTE. No exceptions, ever.** The 19 categories appear in one fixed order in
   every chapter, and the beats inside each category appear in one fixed order. Order never
   varies chapter to chapter for any reason — not for drama, not for a reveal, not for an act-break.
2. **PRESENCE is flexible.** A beat can be absent in a given chapter (e.g., Big O does not
   appear in some chapters). Absence is allowed and is marked explicitly. Absence never causes a
   reorder — the slot is simply empty and labeled as such. (Call this the *presence rule*: sequencing
   is fixed, presence is optional.)

Everything that follows serves those two rules.

---

## STEP 1 — Fix the scope and internal order of all 19 category-sections (read prose, move nothing)

Work at the level of **beats**. Loom *reads* the existing prose to derive the beat inventory, but in
Step 1 it **moves and edits nothing** — this step decides the taxonomy (what belongs where, in what
order); the actual relocation of prose is Step 2. The job is to place every recurring content-type in
the book into **exactly one** of the 19 categories, and to fix the **order** of beats inside
each category. No beat may belong to two categories; none may be orphaned.

**Step 1 begins with extraction, not debate.** Before placing or sequencing anything, build the raw
inventory of what actually recurs. Feed each current (messy) `cat[N]_allchapters` file to Loom **one at
a time**, and ask Loom to extract a list of the **recurring beats** it observes in that category across
the twelve chapters — the content-types that appear again and again (e.g., in the bot block: Bramblogues,
Big O, drill-Mira). This is an observation task, not a judgment task: Loom reads the twelve installments
and reports what repeats, without yet ruling on whether a beat belongs to this category. The output is one
candidate beat-list per category, straight off the existing material.

Only once every category has its observed beat-list do we begin the real Step-1 work: **debate each
candidate beat** — does it belong to this category (and only this one), or does it actually live elsewhere
(the motivation-belongs-in-4.9 case is the template) — and **fix the sequence** of the beats that do
belong. Because the current files are the messy ones, the extraction will surface beats sitting in the
wrong category; those are exactly the misfits Step 2 relocates, and catching them here is the point.

Concrete decisions already made by Brian, to be encoded as canon:

- **Motivation always lives in Lisa's Trellis (4.9), never in the clade block (4.2).** Where the current
  prose discusses motivation inside the clade block, it belongs to 4.9 and moves there.
- **4.4 (bot block) internal order is fixed:** bramblogues → Big O → drill-Mira. Always this order; Big O
  may be absent (presence rule), which leaves an empty Big-O slot, never a reorder.
- **4.9 (Lisa's Trellis) internal order is fixed:** vocabulary → cybernetic function (the Venn) →
  motivation. (This matches the Trellis framework's own canonical structure.)
- **4.10 (sentience vote) internal order is fixed:** Lisa → Burns → Bart → Marge. Always this poll order;
  *who* crosses/changes their vote is the content and varies freely. In the late chapters where the vote
  is dropped entirely, the whole 4.10 slot is absent (presence rule) — the order still never changes when
  present.

Deliverable of Step 1: a **category-sequencing spec** — for each of the 19 categories, its one-line
scope (what content-types belong to it and only it) and its fixed internal beat order. Plus the
fixed order of the 19 categories themselves within a chapter (the chapter spine). This spec is the single
source of truth the rest of the rebuild conforms to.

Do this *before* relocating any prose. It is a taxonomy decision, not an editing decision — Loom reads
the chapters to see what recurs, but no text moves until Step 2.

---

## STEP 2 — Define how Cowork moves the contents to conform, and resolve the misfits

With the Step 1 spec fixed, define the mechanical procedure by which Cowork relocates existing prose into
the correct category-section and correct internal order. The migration itself is mechanical; the value is
in catching what *doesn't* fit cleanly.

Two misfit classes to resolve explicitly (these are where the old pipeline silently failed):

- **Multi-fit:** a passage that plausibly belongs to more than one category. The Step 1 scope rules must
  be tight enough to resolve most; any that remain get an explicit human ruling and the spec is amended so
  the ambiguity cannot recur.
- **Zero-fit:** a passage that fits no category. Each gets a ruling — either it defines a missing slot, or
  it is connective tissue that attaches to an adjacent section, or it is flagged for the author.

Deliverable of Step 2: a migration procedure for Cowork, plus a resolved ledger of every multi-fit and
zero-fit passage with its ruling. After this step, every piece of prose has exactly one home.

---

## Settled vocabulary and header format (locked; do not re-litigate)

- **Two tiers, two words.** The 19 are **categories**. The fixed ordered slots inside each category
  are **beats** (e.g., category 4.4 has three beats: Bramblogues, Big O, drill-Mira). "Beat" is retired
  as a name for the 19 — the parent is always "category," the child always "beat."
- **Header tags are machine-only (invisible to the reader), as trailing HTML comments:**
  - Category heading: `## Clever Name <!--[N]-->`  (e.g., `## The Shelf <!--[4.6]-->`)
  - Beat heading: `### Clever Name <!--[N-letter]-->`, or `### <!--[N-letter]-->` when the beat has no
    clever heading of its own. Letters run in fixed order (a, b, c…) and encode the sequence, so an
    out-of-order letter is a visible sequencing violation.
  - The comment tag renders invisibly, so the clever names stay pure craft on the page; extraction greps
    the comments (`\[4.6` for all of a category, `\[4.4b\]` for one beat). Note: the tags are only visible
    in a raw-markdown editor view, so do the alignment work in raw view, not rendered preview.
- **Every beat is present in fixed order even when empty** (presence rule): an absent beat is a marked,
  contentless line — `### <!--[4.4b]--> (no Big O this chapter)` — never a gap. Sequencing and presence are
  both enforced by the structure itself, not by vigilance.

## STEP 3 — Rewrite the section headings to align to the category boundaries

With material relocated (Steps 1–2), the 12 chapters now conform to the spec. Rewrite the section headings
so the structure is both clean-for-extraction and good-on-the-page:

- **Every category boundary gets a major `##` heading.** Category 1 gets a `##`, category 2 gets a `##`,
  and so on — so the boundaries between the 19 categories are unambiguous and machine-findable.
- **A pre-existing good heading that lands on a *sub*category** (a clever, on-brand heading worth keeping
  that aligns to a child, not the parent) becomes a minor `###` heading beneath its parent `##`.
- **Headings take craft.** They must read as the book's own — on-brand, not mechanical labels. This is a
  writing task, not a tagging task; the discipline is that good headings must *also* align exactly to the
  category edges.
- **Empty (absent) beats are marked explicitly** so a bot never mistakes an absence for damage —
  the presence rule made visible in the structure.

Deliverable of Step 3: 12 chapters whose entire contents conform to the category-sequencing spec, with
headings that are both extraction-clean (aligned to boundaries) and on-brand.

---

## STEP 4 — Rerun the evaluation pipeline, better than last time

With clean, rigidly-sequenced chapters, extraction becomes pure lookup (grep whole sections by heading;
zero content calls), which removes the entire failure class that forced this rebuild. Then rerun, in order:
**predictions → cards → skeptic notes → tally → heat map.** Each stage runs against the process/harness docs
already written (`loom_evaluation_process.md`, `loom_eval_harness.md`, `loom_operating_core_run.md`,
`loom_kickoff_prompt.md`), improved by the lessons from the last run.

Improvements to carry into the rerun (from the last pass's lessons):

- **Extraction is now lookup, not judgment** — verify each content file is a clean whole-section pull
  before the run; there should be no more fused-cell losses to hunt.
- **Cards are candidates, not verdicts** — the fresh-read step remains mandatory; the net catches location,
  the human calls the verdict and the fix.
- **Distrust the most-elaborated PROTECT** and any finding defended only by "the instrument is blind here" —
  the skeptic layer's job.
- **Fix the tally's known defects before reading it** — the one-column offset and the texture-only blindness;
  low late-chapter scores are payoffs, not slack.
- **Run the ear against the book's core risk directly** — caption-disease is invisible to predictor and tally
  by construction, so the census/hunt-the-absence method and the under-show/over-tell frame lead the read.

The end state is the same heat map, produced on clean material, trustworthy at extraction and honestly
sorted at verdict.
