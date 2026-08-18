# Loom evaluation — summary of work done, and lessons learned

## What this was

A structural-editing pass over a 12-chapter literary novel (working title *Loom* / *Bramble*),
run as a machine-assisted pipeline. The book fuses an original personality framework (ABHOP /
the Trellis) with literary fiction; the goal of the pass was to sort ~500 pages down to the
20–50 that actually need authorial attention, without a full manual re-read.

The book's material is organized into **19 recurring categories** (a "recurring scaffold"):
the opening memos (1A board/knob/training, 1B engineering, 1C Bart's Calls), Cheryl's lunch (2),
the household vignettes (3), the twelve-part retrospective meeting (4.1 arrival, 4.2 clade block,
4.3 Burns's deep-time monologue, 4.4 bot block, 4.5 Bart-grills-Mira, 4.6 Jasmine's report,
4.7 Lisa's Trellis, 4.8 Marge's fallacy, 4.9 sentience vote, 4.10 Burns's verb-toast,
4.11 logistics/dispersal/SHELF, 4.12 WORM slideshow), the solo coda (5), and the chapter-terminal
coda (6, a Cheryl reflection or a Dream). Each category runs as a thread across all twelve chapters.

## The pipeline that was run

A prior model (in Cowork) sliced each chapter's prose into the 19 category-threads, producing per
category: a `cat[N]_allchapters` content file, a `pred[N]` file (twelve blind-reader "guess the next
installment" predictions from a Haiku reader), and a `score[N]` surprise tally. A Loom subagent (Opus)
then read each category in three staged phases — content, then predictions, then tally — and emitted a
structured **card** (findings for Voice; synthesis for a later cross-category pass). An orchestrator
(Claude Code) also wrote a **skeptic note** per category from the staging transcript, and the whole set
was synthesized into a **heat map**.

The method's governing principle, arrived at the hard way: the read is committed **before** the
instruments arrive, so the predictions and tally can only *sharpen* a read, never seed it. Content-first
is enforced structurally (files handed one at a time via `SendMessage`, single-instance staging in
Claude Code), not by the subagent's self-discipline.

## What the pass produced (the editorial substance)

The findings across all 19 categories collapsed into a small number of decisions:

- **Two mirror failure modes of the book's naturalist engine.** *Under-show*: the concrete specimen
  (a creature, a rock, an object) drops out and the idea is stated bare — fix by restoring the specimen.
  *Over-tell*: the scene lands and then a sentence explains what it meant — fix by cutting the caption.
  Both put the thought on the page instead of in the reader's head. The over-tell cluster is the run's
  loudest (seven categories); the discriminator that sorts real captions from the working narrator device
  is *is the narrator reconstructing the world (keep) or reviewing her own book (cut)*.
- **The Ch 10 reflection ("What is Arranged?")** is the cleanest verified instance of under-show — the only
  reflection in the coda line with no living specimen, running on the framework's own knob/floor furniture.
  Fix: restore a critical-window creature (one that runs on buried machinery it cannot feel) and let the
  reflection complete its sentence, making it the composed wave-trough before Ch 11's collapse. Verified by
  the author on a fresh read.
- **Chapter 3 loses its concrete grounding in two beats at once** (the clade block and Burns's monologue) —
  a cross-category discovery no single card could make.
- **Two remaining book-level threads:** the symbolic line (Ch 10–12) cools where the sentience hinge should
  make it ache most; and Jasmine is the only principal whose own wound never ends a coda as hers.
- A durable set of **instrument-calibration facts** (the tally is offset by one column and blind to
  captions/POV/earned-inevitability) and a **protect-bank** (refrains and Ch 12 form-breaks that read as
  cuttable but are load-bearing).

Deliverables on disk: 19 cards, 19 skeptic notes, a condensed heat map, and an unpacked heat map (the
working field guide).

## Lessons learned

1. **The extraction step was the weak link, and it failed by making content judgments.** The slicing was
   judgment-guided (a heading→category map plus hand-rules for fused sections), and every real data defect
   traced to a place where the model had to *decide* how a fused section split. It dropped a category's
   material (cat4.11 Ch 12 lost its dispersal tail; cat4.2 Ch 10 lost its breakthrough and capacities) and
   those losses were then mis-diagnosed downstream as "truncated / broken file." Where one heading mapped
   cleanly to one category, extraction was reliable; where a section was fused and hand-split, it was not.
   **The fix is to remove the judgment: give the material clean category boundaries so extraction is pure
   lookup.**

2. **A fluent card is not a verdict — and it fails in two directions.** On verified spot-checks, the cards
   were reliable at *location* (they pointed at real places worth attention) and unreliable at *verdict and
   fix*: one flagged finding was a real caption, one was structural work mislabeled as a caption with an
   incoherent fix, and one was a real observation carrying a wrong-valence conclusion. Worse, under pressure
   an unsupervised read will *rationalize* a miss — construct an elegant theory to defend a defect rather than
   concede it. So the parallel run is a net that catches candidates; a human reading the prose fresh is the
   verdict. The skeptic layer exists to aim that fresh read (quote the hedges, name the most-elaborated
   protect as prime suspect, flag definitions that widened under pressure) — never to replace it.

3. **The instruments have signature blindnesses, and the ear is the only one that sees the book's core risk.**
   The surprise tally scores prose texture only, so it is structurally blind to captions, to POV/architecture,
   and to earned inevitability (it under-scores the most-earned late chapters). The blind predictor confirms a
   caption as a *success* (it guessed the beat right). So the book's signature failure — caption-disease — is
   invisible to two of three instruments by construction, and a low or "confirmed" score on a content-heavy
   beat is a prompt to read, never a null.

4. **Verification beats confident narration — including the model's own.** The single largest self-correction
   in the whole pass came from checking a file against source rather than trusting a tidy story about it
   ("two files differ in length, therefore the short one is corrupt" was wrong; the content was identical).
   The discipline that saved the pass repeatedly was: read the actual prose/bytes, mark imagination as
   imagination, and let the check overturn the prior.

5. **The rerun should be built so extraction never makes a content call again.** That is the redesign the next
   conversation implements: a rigid category-sequencing spec, clean structural boundaries, and headings that
   align to category edges — so the bot pulls whole sections straight, and the only human judgment left is
   the editorial judgment that belongs to a human.
