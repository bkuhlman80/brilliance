# The Readability Pass

The process for taking a sequenced chapter to a clean read. A sequenced chapter groups each
category's material into one contiguous block, which creates seams that never existed in the
original braid. This pass resolves those seams. It runs after sequencing and after the echo sweep;
it is the readability counterpart to the echo-sweep fork.

## The one invariant

Every category may be absent in a given chapter except **category 3, the household vignettes.**
The floor is per beat, not just per category: each of category 3's three locked beats (3a
Bramblation, 3b Bramble + Chill, 3c Bramblearning) needs at least one vignette on the page, no
ceiling on any of them. A bare-tagged absence — legal for any beat in any other category — is not
legal for a category-3 beat. This is a floor-count rule and nothing more: category 3 earns no other
liberties, obeys every pass below exactly as the other categories do. The Calvin & Hobbes floor is
the heart of the book; it is the one thing that is never zero, beat by beat.

## The meeting's three blocks

The retrospective portion of every chapter runs Lisa's agenda in three fixed blocks: **Clade**
(categories 4.2–4.3), **Bot** (categories 4.4–4.8), **Trellis/Framework** (categories 4.9–4.13).
Categories 4.1, 4.14, and 4.15 sit outside all three blocks entirely. This is marching orders, not
a loose grouping — it cannot be fudged or disregarded when checking a seam.

The practical consequence for Pass 3 and Pass 4: any line where Lisa (or anyone) announces a block
by name is a structural cue, and it is only ever legal at that block's true boundary. "Framework" can
only be said at the bottom of 4.8 or the top of 4.9 — never inside 4.4–4.8, because that whole span
is still the Bot block regardless of how the prose feels in the moment. A block-name announcement
sitting anywhere else is not a stylistic seam question, it is a wrong placement, full stop, and gets
cut or moved rather than smoothed.

## Category 3 dates are visible, not hidden

Every other beat's date lives only in its hidden HTML comment tag. Category 3 (Household Vignettes)
is the exception: because its beats can span days or weeks with nothing in the prose marking the
jump, the date must also appear as a short visible line on the page (e.g. *February 17*) directly
under the hidden tag, for every beat in the category, every chapter. This is a formatting requirement,
not a prose fix — no connective sentence is needed inside the vignette itself to signal time passing,
the visible date does that job on its own.

## Four passes, fixed order

The order is load-bearing. Passes 2 and 3 move furniture — every kill and every confirmed absence
changes which beats abut which — so the seams can only be settled once the sequence is frozen.
Never stitch a seam while slots are still moving.

Each pass has a single output. Do not begin the next pass until the current output holds.

---

## Pass 1 — Invariant

Mechanical, seconds. Confirm each of category 3's three beats (3a, 3b, 3c) has at least one
vignette — checking the category as a whole is not sufficient; a chapter with five vignettes all
sitting in 3a and nothing in 3b or 3c fails this pass. Confirm every other category is either
populated or marked as a bare-tagged absence. That is the whole pass.

**Output:** the chapter's category skeleton is legal — including, for category 3 specifically, all
three beats present.

---

## Pass 2 — Contention

Run on every slot holding two or more competing events. When two things fight for one beat, exactly
one of three things is true. Decide which *before* you cut.

1. **One thought interrupted** — a single continuous thought broken and resumed (the land-the-plane
   case). It was never two. It **collapses** into one beat. No death.
2. **Two facets of one point, one load-bearing and one decoration** — the decoration **dies.** Not
   folded, not tucked into a subordinate clause. Cut.
3. **Two genuine, separate, both-good events** — one **wins the slot, the other dies. Full stop.**
   The loser does not get stitched in beside the winner, and does not travel to another chapter.
   It dies. Even the best writers cut good material; a book is not a place where every good thing
   survives.

Never stitch. Never relocate. The result of every contention is one event standing or one event
collapsed — never a blend.

**The read-aloud gate.** A collapse (verdict 1) survives only if the merged beat reads aloud as one
continuous thought with no felt seam. If you feel two things, it is two things — send it to verdict
2 or 3 and cut. This gate exists because "one thought interrupted" is the disguise every doomed
stitch will wear. Where a sentence used to be categorized is irrelevant to the gate; provenance
never licenses a merge. The only test is whether the seam is felt.

**Output:** 0–1 events per beat, across the whole chapter.

---

## Pass 3 — Absence

Run on every empty slot. A missing beat is not a defect. It is data about the chapter's true shape,
and most missing beats are correct — a chapter writes to its own argument, not to the category
template, which is a menu and not a checklist. The question is never "how do I fill this slot." It
is "is this absence real, or is it a hole."

Three probes. They are independent, and their disagreement is the signal.

1. **The reach** *(cohesion: reference, conjunction, ellipsis).* Does any surviving beat point at
   the missing one — a pronoun or definite reference with no antecedent, a *but / so / then* whose
   other half is gone, a setup with no payoff, an ellipsis that resolves against absent material?
   A reach means a tie whose far end was deleted. **Reach present → hole.** Near-mechanical.
2. **The seam that would form** *(the given-new contract).* Read the two beats that would abut if
   this slot stays empty. Does the later beat open with "given" information the reader can cash from
   what precedes, or does it lead with a false given — assuming ground the missing beat was meant to
   lay? **False given → hole.** Near-mechanical.
3. **The argument's schedule** *(RST: does the relation have anything to operate on).* Each category
   runs a multi-chapter argument. At this chapter's position in that arc, does the beat's function
   have material to work yet? A fallacy only named cannot yet be tested; the Test relation has no
   argument to take. This probe asks what the book needs, not what the slot lists.

**Verdicts.**

- **All three say absent** (no reach, clean seam, argument doesn't need it here) → **leave it
  absent, with confidence.** This is most missing beats. Bare tag, move on.
- **All three say hole** → **fill it.** Probe 1 has already named which surviving beat is reaching,
  so you are writing to a stated need, not to an empty slot. When the probes agree it is a hole, you
  rarely have to invent — the reach tells you what the fill must satisfy.
- **They split** → the fill is almost never the answer. The common split is *reach says hole,
  schedule says absent*: a beat leans on something the argument shouldn't deliver yet. That is a
  **misrouted reach** — the leaning beat is reaching for material that belongs to a different
  category, or the beat is over-written and the reach itself should be cut. Fix the reaching beat;
  do not write the missing one. The other split — *schedule says hole, nothing reaches, seam is
  clean* — means the argument wants the beat but the chapter isn't built to use it yet. That is a
  structural note for the author, not a beat to quietly slot in.

**Probe priority.** Probes 1 and 2 are near-mechanical; check them first. Probe 3 is the softest —
"what the argument needs" is the easiest to bend toward a conclusion already wanted — so it breaks
ties only. It never overrides two mechanical *absent*s. If reach and seam both say absent, the beat
stays absent, whatever theory anyone holds about what the argument wants.

**Output:** every absence in the chapter is deliberate.

**How the note gets written.** Every split-probe case gets surfaced to Brian ELI5 — slow, walked
through, not asserted. Quote the actual two beats that abut (or would abut), point at the specific
pronoun/connective/setup that is or isn't doing the reaching, and name which probe said what before
naming the verdict. The reader of the note should be able to see the reach or the false-given on the
page, not just take the verdict on faith.

---

## Pass 4 — Seam

The sequence is now frozen. Walk every junction between adjacent beats and categories.

For each seam, name the discourse relation between the two beats — Sequence, Contrast, Background,
Cause, Elaboration, Concession. Then ask whether that relation is signaled. If the relation is real
but silent, add the minimum connective of that specific type: usually a clause, often a single
reorientation of time, place, or who is in focus. A named relation makes the fix precise — a
Sequence seam missing its "by the time," a Contrast seam missing its turn — rather than a vague
"needs a transition."

Check each seam for the reader's first question after a cut: where, when, who, whose voice. Close a
whole orientation gap with the fewest words that do it.

A paragraph at a seam is a warning. It usually means a kill from Pass 2 was not fully committed and
the connective is papering over the gap. Go back and finish the kill; do not smooth it here.

**Output:** the chapter reads straight through.

---

## Running it with Cowork

Passes 1 and 4 are largely mechanical and safe to delegate. Passes 2 and 3 turn on two human
judgments — the read-aloud gate and the reach test — and those are the two places the work drifts:
toward over-merging in Pass 2, toward over-filling in Pass 3. Surface every contested slot and every
split-probe absence for a ruling rather than resolving it silently. A claimed merge that cannot pass
the read-aloud gate is not a merge. A fill proposed on Probe 3 alone is not a fill.

**Transparency ramp.** On a new chapter, show nearly every call — clean and contested alike — for
the first beat or two, so Brian can calibrate the verdicts being made. After that, drop to showing
only the contested/split calls; clean verdicts get a one-line log, not a walkthrough.

**Standing rules, non-negotiable:**

- Surface every contested or split-probe call for a ruling instead of resolving it silently, even
  when one answer looks obviously right.
- When two reference docs disagree, flag the contradiction and ask which one governs — don't pick
  one quietly.
- When an anomaly could be either "acceptable flexibility" or "a violation of a rule not yet stated,"
  name that ambiguity out loud and ask, rather than defaulting to the more permissive reading.
- If a placeholder or tentative call has to go directly into a file (like a working title), flag it
  as tentative in the same message — never in the file. Never place notes, provenance, or open
  questions into the prose itself. Resolve with Brian directly and immediately instead.
- At the end of each chapter's four passes, produce a bullet list of any new best practices
  discovered during that chapter, for addition to this doc.

---

## Best practices (accumulating; append as we go, do not re-litigate settled entries)

This section is the working precedent list — refinements discovered mid-pass that aren't worth
promoting into the pass definitions above, but that should govern the next time the same shape of
call comes up. Each entry: the situation, the ruling, and which chapter/beat it came from.

**A block-name announcement out of place is a wrong placement, not a seam (Ch1, 4.5.c).** Lisa said
"Framework" at the end of 4.5.c, which felt like a clean, signaled transition in isolation — but 4.5
sits inside the Bot block (4.4–4.8), and "Framework" only becomes true at the 4.8/4.9 boundary. This
is not a Pass 4 judgment call about whether the seam reads well; it's checked against the three-block
structure first, before the prose is trusted. Fix: cut the line outright at its wrong location; do
not relocate it if the true location already has its own equivalent line (Ch1's 4.9.a already opened
with its own "Framework was where the words got set down for good," so nothing needed to be added).

**A "clean" absence can still be a hole in disguise (Ch1, 4.14).** All three probes can appear to
agree a category is absent when actually its content is sitting, uncredited, inside a neighboring
beat — the same shape as the Pass 2 buried-boundary case, just found by the absence probes instead
of a contention scan. Ch1: category 4.14 (Logistics) was tagged bare/absent, but the schedule-giving
and camera-off content that defines Logistics was sitting in the opening lines of 4.15.a (Solo Coda).
Tell: the content matched the absent category's job description word for word once actually checked
against it, rather than just trusted because the tag said absent. Fix: relocate the content to the
correct category's spine position, no invention — and give the newly-populated category its own
visible heading, since a populated category always needs one even if it was previously a bare
one-line absence. Master-list notes claiming a category is absent in a given chapter are a starting
hypothesis for the probes, never a substitute for running them.

**Missing tag vs. absence (Ch1, 4.8.b).** A beat with zero tags anywhere is a hard defect, not an
absence — an absence always gets its own bare tag. Fix by inserting the tag the evidence supports:
bare if the beat truly has no material this chapter, dated if content turns up nearby that was
never given its own break.

**Duplicate letter, genuinely one thought (Ch1, 4.9.a used twice).** When two blocks share a beat
letter and read as one continuous scene once you check them against each other, the fix is to
delete the redundant tag outright — not renumber, not add a letter. Keep the earlier tag's date.
This is Pattern 1 from `master_category_beat_list.md`'s beat-letter-reuse rules, applied.

**Buried beat boundary is not contention (Ch1, 4.4.c/d).** Sometimes what looks like a Pass 2 case
turns out not to be one: a single tagged beat contains two jobs (Ch1: Lisa's capability demo, then
Bart's mechanism/architecture explanation), with the second job's content sitting untagged inside
the first's beat instead of getting its own letter. This is not two events competing for one slot —
nothing is redundant, nothing needs to die or collapse. The text itself usually announces the seam
("for the next part," in this case). The fix is a tag insertion at the existing seam, no text moved,
no verdict needed — closer to Pass 1's missing-tag territory than true Pass 2 contention. True
contention is reserved for cases where content actually competes to occupy the same beat.

**Cross-category miscategorization, caught during Pass 1 (Ch1).** A block tagged into one beat can
turn out to belong to a different beat in a different category entirely — not just a same-category
reshuffle. Ch1: Burns's "we are going to build twelve robots" speech was sitting inside 4.9.a
(Lisa's Trellis, vocabulary mode) but is 4.1.c's Ambition Statement by function. The fix is a full
physical relocation across categories, not a local patch. Category 4 beats share one date per
chapter, so a relocated beat takes the same date as its new neighbors, not the date of where it
used to sit. Any seam this creates at either the old or new location is a Pass 4 problem, not
something to smooth mid-relocation.

**Tag-completeness is its own mechanical check, distinct from Pass 1 (Ch1, Ch2).** Pass 1 only
confirms category 3's floor. A full "every beat, every chapter" tag audit against the whole
19-category spine — checking that every beat in every category has a tag, dated if present, bare
if absent — catches gaps Pass 1's narrower scope doesn't. Run it as its own pass, not folded into
Pass 1.

**Tag-completeness audits must check every absent beat's actual content, not just its position in
the letter sequence (Ch5, 4.10.c and 4.15.c).** A tag inventory tells you a beat is bare; it doesn't
tell you that beat has been checked. Resolving one question about a category (an interweave
pattern, a whole-category absence) doesn't clear every bare beat inside it — each one still needs
its own reach/seam/schedule pass under Pass 3, even when a neighboring beat in the same category
already got resolved for an unrelated reason.

**A "reach" can also be an internal scramble, not just a missing beat (Ch7, 4.9).** Pass 3's reach
probe usually points at an absent slot, but the same symptom — a pronoun or callback with no
antecedent on the page — can mean the antecedent exists but got moved to the wrong side of the
dangling line during migration, inside a single beat that was never split. Ch7: Marge's self-model
line ("steady again") presupposes a prior unsteady moment; the old draft showed that moment (her
"sat up," twenty-years attachment monologue) had been pushed to *after* the line that depends on
it, within the same 4.9.b beat. Fix is a reorder, not a fill — confirm against the old draft before
assuming content is gone rather than shuffled.

**A stale chronological marker can survive a category relocation (Ch7, 4.11.a).** When the spine's
fixed order moves a beat to a new position relative to other events (per "sequencing is absolute"),
check the beat's own prose for language that still asserts its *old* relative timing. Ch7's Worn
Path opens "she took it now, before the count" — true when this scene sat ahead of the vote in the
original draft, false now that 4.11 is fixed after 4.10. The category's position is never up for
relitigation, but leftover timing language that contradicts the new position is a wording defect,
not a structural one — cut or reword the line, don't move the category.

**An interweave-sanctioned beat letter repeating is not the duplicate-letter defect (Ch7, 4.10.a/b).**
Some beat pairs are explicitly marked "interwoven, no fixed order" in the category detail table
(4.10's Count/Reasoning is one). A letter appearing twice there is the intended pattern, not the
Ch1/Ch6 duplicate-tag mistake where the same letter shows up on genuinely continuous, un-interwoven
content. Check the category detail table's own interweave marking before flagging a repeat as a
defect.

**The same check runs the other way too, category by category (Ch8, 4.3.a).** A category being
interweave-sanctioned elsewhere in the spine (4.10) doesn't make every repeated letter benign —
4.3 (Ritual Framing / Monologue / Landing) is fixed-order, not interwoven, so a second `4.3.a`
sitting on Jasmine's "Land it" interruption was a real mistagging, not a deliberate recurrence.
Fix followed the Ch7 precedent for this exact shape (an interruption cue folding into the
monologue beat it interrupts): delete the redundant tag rather than retag or split. Check the
detail table's interweave marking fresh per category, every chapter — a clean verdict on one
category is never evidence for another.

**A relocated line needs its antecedent restated, not just carried by pronoun, when it crosses a
hard category break (Ch8, 4.9.b).** Moving a misplaced "Framework" announcement to the correct
block boundary (per the Ch1/Ch6 precedent) is a Pass 3/4 fix, but the destination beat opens cold,
right after a title/date header, with no speaker established in that fresh block. Writing "She
reached for the marker" leans on whoever was last named before the section break — which after a
hard cut is very often the wrong character (here, Marge, not Lisa). Ch6's version of this same fix
named the speaker outright for exactly this reason. Any line relocated across a category boundary
needs its subject re-checked for a clean antecedent in its new position, not assumed to carry over
from where it used to sit.

**The 4.3 duplicate-tag mistagging (Jasmine's "Land it" interruption getting its own repeated
letter) has now recurred in three straight chapters (Ch7, Ch8, Ch9).** It is common enough at this
point to check for by default at Pass 1 on every remaining chapter, not wait to be surprised by it.
Fix is the same each time — fold the interruption and the answering line into the monologue beat
it interrupts, delete the redundant tag — though which letter absorbs it can vary (Ch7/Ch8 folded
into `4.3.b`; Ch9 folded into `4.3.a`). Brian has made this exact call himself twice now; it's a
five-second check worth running proactively rather than a Pass-1 surprise each time.

**A vignette's internal seasonal language can drift past its own dateline even when nothing needs
to be split (Ch9, 3.a "March 17").** This looked at first like Ch7's category-3 corruption (several
occasions fused under one tag), but the fix here was much smaller: two "by spring" / "the spring"
references inside a single vignette that predates spring's actual arrival by a few days. Brian's
ruling: no stylistic reach to preserve, no restructuring needed — just correct the season word so
it agrees with its own dateline ("winter" in both places). Worth checking any vignette whose prose
names a season, month, or "by [X]" marker against its own visible date before assuming a Pass-2
split is the right diagnosis; sometimes the fix is a word, not a restructure.
