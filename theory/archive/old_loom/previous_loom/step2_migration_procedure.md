# Step 2 — Migration Procedure

Defines how Cowork relocates prose from the twelve (plus Ch0) master chapter files into the
fixed category/beat order locked in `category_sequencing_spec.md`. Written before any chapter is
touched. Two deliverables live here and in the companion file: this procedure, and
`step2_misfit_ledger.md` (the resolved-and-open misfit list).

## Governing rule: the source gets fixed, not just the copy

**Whenever a fix is made to a draft chapter (`ch_N_v2_*.md`), the same fix must be made in the
relevant `cat[N]_allchapters.md` file — every time, no exceptions.** This rule sits alongside the
directive's own two governing rules, not below them; it was learned the hard way on Ch1, where a
restored sentence went into the draft chapter but not into `cat1A_allchapters.md`, and only got
caught because Brian asked directly.

Why: `cat[N]_allchapters.md` is the source. The draft chapter is a copy generated from it. If a
fix lands only in the copy, the source is still wrong — and every future operation that reads the
source instead of the copy (a later chapter's migration using this category as a pattern, Step 3's
heading pass, Step 4's extraction pipeline, a future re-verification of this same chapter) inherits
the original error right back, silently, because nothing about the source file changed. The fix
didn't fail to propagate — it never existed anywhere the next reader would look. This is the same
failure mode `loom_project_summary.md` names as the whole reason this rebuild exists: extraction
has to be pure lookup against a trustworthy source, and a source with an unfixed, undocumented gap
is not trustworthy no matter how correct the one downstream chapter looks.

## Why this is mechanical, not judgment work

Step 1 already did the judgment: every surviving passage in every `cat[N]_allchapters.md` file
carries a category+beat tag, and — per the spec's unbreakable rule — any connective tissue that
isn't clearly "content" was already assigned to its nearest bounding beat during Step 1 review, not
left orphaned. So by the time migration runs, the hard call (does this sentence belong to 4.2 or
4.9?) is already made. Migration is relocation of already-labeled chunks into a fixed order — the
only new judgment allowed during Step 2 itself is resolving the misfit ledger (below), and that's
explicitly scoped, not open-ended re-litigation.

## Per-chapter procedure

For each chapter file (`ch_N_v2_*.md`, N = 0–12):

1. **Build the manifest.** Walk the 19-stop chapter spine in `master_category_beat_list.md`; each stop is one category,
   pulled from the corresponding `cat[N]_allchapters.md`. (An earlier draft split two categories
   across non-adjacent stops — old 4.5's Break beat and old 4.11's pitch/shelf-vs-logistics — so
   "walk the categories" and "walk the spine" diverged; those splits have since been promoted to
   standalone categories: 4.7 (The Break), 4.6 (Pitch/Reveal), and 4.14 (Logistics), so the two
   walks are the same operation again.) Record, for each passage, an exact anchor: the opening and
   closing phrase (quoted verbatim) or line range already cited in `category_sequencing_spec.md`
   where available.

2. **Verify every anchor with `grep -n` against the actual current chapter file before touching
   anything.** The spec's own citations (e.g. line numbers) were written against specific file
   versions (`ch_2_v2_9.md`, `ch_3_v2_12.md`) that are no longer current — the connected folder now
   holds `ch_2_v2_10.md`, `ch_3_v2_13.md`, and others one or more versions ahead. Treat every
   line-number citation in the spec as provisional until re-confirmed by grep against the live file.
   This is not optional — it's the exact failure mode the whole rebuild exists to eliminate.

3. **Cut each verified passage from its current location**, preserving its internal text exactly
   (no rewriting — that's Voice's and Step 3's work, not this step's).

4. **Reassemble the chapter** by walking the manifest in spine order: stop by stop, beat by beat
   within each stop. (The former split categories are now standalone stops — 4.7 (The Break),
   4.6 (Pitch/Reveal), and 4.14 (Logistics) each sit at their own spine position — so beats no
   longer scatter across non-adjacent stops by shared category number.) Where a beat is absent for this chapter, insert the explicit presence-rule
   marker (`### <!--[N-letter]--> (no [beat name] this chapter)`) rather than a gap. Where a stop is
   absent entirely for this chapter (e.g. Ch1 has no 4.10), skip it — no marker needed at the stop
   level, only at the beat level within a present stop.

5. **Apply machine-only tags, not craft headings, at this step.** Every relocated block gets its
   structural tag (`## <!--[N]-->` at category open, `### <!--[N-letter]-->` at each beat) so the
   result is immediately grep-verifiable. Do not write the on-brand clever heading names yet — that
   conflates mechanical relocation with the writing task Step 3 owns. A Step-2-complete chapter reads
   correctly in order but with placeholder/tag-only headers.

6. **Excise anything in `to_be_deleted.md`** for this chapter rather than relocating it.

7. **Category 2 does not go through steps 3–4 (cut/reassemble) in its interior.** Ruled in
   `step2_misfit_ledger.md` item 2: 2.b/2.c are interwoven registers inside one continuous
   conversation — cutting "all the b's then all the c's" apart means cutting mid-dialogue, which
   this category's own prose won't survive. Only the bracket is enforced: confirm 2.a opens and
   2.d closes when present; everything between them stays exactly where it sits, tags applied in
   place. Ch9 and Ch11 need a grep-verify pass first (flagged in the ledger) but that doesn't change
   the no-reorder rule for the interior.

8. **Category 3 is now LOCKED (ruled 2026-07-09): fixed order a→b→c.** Each chapter's fragments
   consolidate into three blocks — all 3.a (Bramblation), then all 3.b (Bramble + Chill), then all
   3.c (Bramblearning) — each block preserving the original relative order of its own fragments.
   Full ruling and per-chapter reordering in `cat3_allchapters.md`. One standing exception: where a
   later fragment has a hard grammatical or scene dependency on an immediately-preceding
   different-letter fragment (an anaphor like "which"/"now" with no other antecedent, or a
   setup/payoff split across one continuous action), keep that pair adjacent in original relative
   order rather than force pure block separation — same principle as Category 2's no-mid-scene-cut
   rule. Flagged inline in `cat3_allchapters.md` at every chapter where this applies (Ch5, Ch6,
   Ch7, Ch8, as of this pass). Migrate Category 3 normally now, same as the other categories.

9. **Write output to a new version file, not over the source.** These are Brian's manuscript files,
   not working documents — migrate into the next `_v2_N` filename (e.g. `ch_1_v2_3.md` →
   `ch_1_v2_4.md`) rather than overwriting, so the diff in step 10 has something to diff against and
   nothing is destroyed if a chapter needs to be redone.

10. **Word-count / content diff as the QC gate.** After reassembly, diff the new chapter against the
   old one: every sentence in the old file should appear exactly once in the new file, or be
   accounted for in `to_be_deleted.md`, or be flagged as a new misfit-ledger entry. No silent loss —
   this is the discipline the project summary names as the single biggest lesson from the first
   pipeline run ("two files differ in length, therefore the short one is corrupt" was wrong once
   already; don't repeat the inverse mistake by trusting a clean-looking diff without checking it).

11. **Any gap found during a chapter's diff gets fixed at the source first, the draft chapter
   second — never just the draft.** See the governing rule at the top of this document. Caught on
   Ch1 (2026-07-09) and now standing process for every chapter after it.

## Sequencing across chapters

Run chapters in order Ch0 → Ch12, one at a time, each one fully verified (grep-checked, diffed)
before starting the next. Do not batch all thirteen through in parallel — the value of this pipeline
is that each chapter's migration is boring and checkable; parallelizing trades that for speed we
don't need and removes the per-chapter verification gate.

## What Step 2 does not do

- No prose rewriting, no craft headings (Step 3).
- No re-opening of already-locked category/beat definitions (Step 1, closed).
- No silent resolution of misfit-ledger items — every multi-fit and zero-fit passage gets an
  explicit ruling recorded in `step2_misfit_ledger.md` before its chapter is migrated.
