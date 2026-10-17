# Loom evaluation harness — orchestration protocol for Cowork

You (Cowork) run the nineteen category evaluations in parallel by spawning one Opus
subagent per category. Each subagent is a fresh, isolated Loom instance. This document is
for you, the orchestrator — the subagents never see it. Your job is to enforce structurally
the one discipline the subagent cannot be trusted to self-enforce: **the read gets
committed before the instruments arrive.**

## Prerequisite — the architecture brief

A cold subagent can feel prose but cannot *place* it, and placement is where Loom's value
lives. Before running anything, make sure an **architecture brief** exists: a condensed
scaffolding doc — the three lines (Genetic / Neuronal / Symbolic), the Feb-12 structure,
the POV and vote map, the relationship arcs, and each category's one-line definition. If
it doesn't exist yet, build it first. Without it, nineteen subagents will return competent
generic reads and none of the placement judgment the exercise exists to produce.

## Per category — setup

1. **Verify the content file upstream.** The subagent has no known-good copy to diff
   against, so completeness-checking is yours. Confirm `cat[N]_allchapters.md` is complete,
   correctly named, and matches the expected chapter count and rough word count before you
   spawn. This is where the byte-check lives now — do not delegate it to the subagent.
2. **Spawn the subagent with model `opus`.**
3. **Seed its context with exactly three documents:** the Loom operating core, the
   architecture brief, and `loom_evaluation_process.md`. **Do not put the predictions or
   the scores in the seed.** Do not describe their contents. The subagent may know it will
   receive three staged inputs (the process doc says so); it must not see any payload until
   it has committed the prior phase.

## Per category — run the three phases

Deliver one file per SendMessage, in this order, and **require the phase's response back
before you send the next file:**

- Message 1: `cat[N]_allchapters.md` → wait for the content read + placement.
- Message 2: `pred[N].md` → wait for the prediction sharpening.
- Message 3: `score[N].md` → wait for the final response, which ends with the card.

Never send a later file early. Never send two at once. Never answer the subagent's
questions by previewing a later input. If the subagent asks for predictions or scores
before it has committed the current phase, decline and ask it to finish the current phase
first. The staging is the whole method; if it leaks here, it leaks across all nineteen and
you find out in the synthesis pass.

## Per category — harvest

From the subagent's final (Message-3) response, extract everything between
`===LOOM CARD START===` and `===LOOM CARD END===` and save it as `card_[N].md`. Discard the
prose before the block — that's the subagent's thinking, not the deliverable. If the card
is missing fields or malformed, send it back once asking for a clean re-emit of the card
block only; do not hand-repair the schema.

## What the parallel pass is — and is not

The nineteen cards it produces are **draft candidates, not verdicts.** Nineteen
unsupervised Loom reads will be fluent, and fluent is exactly what hides a confabulated
finding or a converged-but-wrong read, because the pushback loop — a skeptical editor with
taste in this book challenging the read in real time — does not exist in an automated run.

So: parallelize the drudgery, keep the verdict. When the run completes, surface the cards
to Brian. He reads all nineteen. Any finding whose CONF line says "wants live re-run," plus
whichever cards look strongest or strangest, get re-run in a real conversation where the
pushback loop exists. The parallel pass is the net that catches candidates; Brian and a
live Loom are the verdict. Treating nineteen unsupervised reads as final is the same
mistake as treating the surprise tally as a verdict — trusting a fluent instrument because
it is convenient.

## After the nineteen — the twentieth

The twentieth conversation reads all nineteen cards together: it weighs the SYNTHESIS
blocks, decides which BOOK_LEVEL_FLAGs recurred often enough to count as real whole-book
patterns, and builds the running instrument-calibration profile out of the INSTRUMENT_NOTE
fields. That conversation needs its own note, which doesn't exist yet and shouldn't until
there are cards to synthesize — write it once the shape of what's accumulating is visible,
not before.
