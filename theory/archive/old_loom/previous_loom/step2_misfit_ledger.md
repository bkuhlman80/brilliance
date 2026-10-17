# Step 2 — Misfit Ledger

Every multi-fit and zero-fit item open after Step 1's first pass, plus the structural findings that
surfaced while ruling on them — including one correction after Brian challenged the first pass's
1D and Category 3 rulings directly (2026-07-09, same day). Two items turned out to already be
resolved on inspection (the spec's own notes were stale, not the underlying work); two required a
real editorial call; one required locating genuinely uncaptured prose and giving it a home; one
(Category 3) is reopened and waiting on an authorial decision that can't be discovered by reading
closer. All rulings and the actual file edits they required are applied in
`category_sequencing_spec.md`, `cat1D_allchapters.md`, `cat4.9_allchapters.md`,
`cat4.11_allchapters.md`, and `cat4.13_allchapters.md` — this file is the record of *why*, not a
to-do list.

---

## RULED

### 1. Category 1D beat taxonomy — locked, ONE beat (corrected same day)
First pass collapsed four provisional labels to two (1D.a Board Status, 1D.b Credit to Lisa).
Brian challenged the two-beat count directly. Re-tested against the standard used everywhere else
in this document — a split beat needs distinguishable, orderable *stages* of one ritual, the way
1C's Calls must precede its Dare. Credit to Lisa doesn't have that relationship to Board Status: it
never stands alone, never opens, never appears anywhere except as the tail of a status report
already in progress, and Ch8's text visibly continues mid-sentence across the "boundary" — one
continuous report, not two content-types. Corrected to **one beat, 1D**, absorbing both the
attribution-clause pattern and both extended instances (Ch9's Lab Note, Ch5's Mira-recognition
passage) as features of that one beat, not siblings of it. Full ruling in
`category_sequencing_spec.md`.

### 2 & 3. Categories 2 and 3 — different rulings, split apart after Brian's correction
First pass treated both the same way (no fixed order, tag in place, nothing moves) on the reasoning
that both categories' beats tag continuous material rather than ritual slots. Brian accepted that
reasoning for Category 2 and rejected it for Category 3 — and the distinction is real, not
stylistic: Category 2's b/c interior is genuinely inseparable (interwoven dialogue, cutting it
means cutting mid-conversation), while Category 3's fragments are discrete `---`-bounded units that
*can* be regrouped without breaking anything mid-sentence. "The current order is already natural"
isn't sufficient grounds to leave Category 3 alone, given this project's explicit mandate to break
existing sequence and rebuild deliberately, not just do the minimum the taxonomy requires.

**Category 2 — LOCKED.** 2.a opens, 2.d closes when present, b/c interior stays exactly where it
sits, migration is tag-in-place only inside the bracket. Two chapters flagged for a grep-verify
before they migrate, not blocking: Ch9's lunch opens 2.c→2.b→2.a and Ch11 carries three separate
2.a instances — real multi-stop structure or a tagging slip, doesn't change the no-reorder rule
either way.

**Category 3 — LOCKED (2026-07-09).** Brian ruled: fixed order a→b→c, each chapter's fragments
consolidated into three blocks rather than left in their original alternating order. See
`category_sequencing_spec.md`'s Category 3 section for the full ruling and the one standing
exception (hard scene/grammatical dependencies keep their pair adjacent rather than being split
across blocks — same principle as Category 2's no-mid-scene-cut rule). Reordering applied to
Ch1–Ch9 in `cat3_allchapters.md` this same pass; Ch10–Ch12 not yet touched.

*Separate, not a Step 1/2 question:* whether the five 2.d absences (Ch4/8/9/12) should get new
codas written is a content decision already in motion elsewhere (Voice has drafts per prior
session's memory) — orthogonal to locking the taxonomy.

### 4. Cat4.9 Ch2 "unsorted MIGRATED CONTENT" — already resolved, spec note was stale
Read the actual Ch2 section of `cat4.9_allchapters.md`: fully tagged 4.9.a/b/c, no unsorted blob.
The physical-hardware portion that traveled with it was already correctly split out to
`cat4.4_allchapters.md` as 4.4.d, confirmed present there. The "Categories with pending inbound
migrations" section in `category_sequencing_spec.md` describing this as unsorted was true partway
through Step 1 and never updated after later passes closed it. Struck and annotated as superseded in
the spec; no content-level work needed.

### 5. Cat4.11 Ch6 "Off the Board" fragment — real gap, now filled
This one was genuinely missing, not misfiled. Traced it to the master file directly
(`ch_6_v2_6.md`, lines 394–396): Burns's "Experiencing Style" aside and Marge's "how, not
what-it's-like" rebuke sit between the already-captured 4.9.c ARCH-mode block and the already-
captured 4.10.b vote-friction fragment, and had never been tagged anywhere — a real two-paragraph
gap a mechanical migration would have silently dropped. **Ruling:** 4.9.a (Vocabulary Mode) —
it's definitional work on the quarter's knob-name, the same function 4.9.a performs everywhere
else, just run as a refusal instead of a translation. Added to `cat4.9_allchapters.md` as a new
tagged fragment, with the exact anchor and a note explaining the handoff into the pre-existing
4.10.b material. Cross-referenced in `cat4.11_allchapters.md` and `cat4.10_allchapters.md`.

---

## CONFIRMED

### 6. Cat4.6/4.14 (old 4.11) Ch12 — Category-1 contamination exclusion
Found independent corroboration while reading `cat1D_allchapters.md` for item 1: its own Ch12 entry
documents restoring this exact paragraph after finding it had been wrongly excluded from old 4.11 (now 4.6/4.14) and
never re-filed anywhere. Confirmed from both the excluding file and the receiving file, not just
the original excluder's say-so. Exclusion stands.

### 7. Cat4.13 Ch11 — possible bleed into 4.14 logistics (old 4.11.c)
Checked `cat4.14_allchapters.md`, now built: 4.14 is present for Ch11 there with no overlap
against 4.13's "To Count" span. Fully accounted for; nothing missing from either file. Both files
annotated with the confirmation.

---

## Cross-cutting risk (unchanged, still live)

**Version drift between the spec's citations and the live chapter files.** The connected
`chapters/` folder holds `ch_2_v2_10.md`, `ch_3_v2_13.md`, `ch_4_v2_13.md`, `ch_9_v2_12.md`,
`ch_10_v2_9.md`, `ch_11_v2_9.md` — one or more versions ahead of several filenames cited in
`category_sequencing_spec.md`. Every citation used in this ledger's rulings was re-verified against
the *current* file (the Ch6 "Experiencing Style" trace, the Ch9 4.9 recheck, the Ch12 1D/4.6-4.14
cross-check all read live files directly, not the spec's citations). Any citation in the spec not
yet re-verified this way should still be treated as provisional. This stays Step 2 migration
procedure item 2 — restated here as the reason none of the above rulings skipped a grep.

---

## Status

All five original items closed and locked (1, 2, 3, 4, 5), plus both confirmations (6, 7).
**Category 3 (item 3) ruled 2026-07-09: a→b→c, block-consolidated.** No categories remain blocked;
all nineteen migrate normally now.
