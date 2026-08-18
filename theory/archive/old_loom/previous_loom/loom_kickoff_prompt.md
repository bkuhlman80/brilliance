# Loom evaluation — kickoff prompt (Claude Code orchestration)

You are orchestrating the 19-category Loom evaluation. Everything is staged in
`theory/chapters/examples/loom/`. **Do not begin the 18-category run until Step 0 passes and
the category-6 smoke test surfaces the target finding (below).**

**Run this in Claude Code, not Cowork.** The method requires single-instance staging —
one subagent held across all three phases — which requires the `SendMessage` tool.
`SendMessage` is enabled in Claude Code and **disabled in Cowork**. That is why this runs
here. There is no fresh-instance fallback: spawning a new subagent per phase was *not* the
mechanism the smoke test validated, and a fresh Phase-3 mind cannot do its job (use the
tally as an index to re-read specific prose) because it never lived the prose. If
`SendMessage` is unavailable in your session, **stop and get it enabled** — do not
substitute a different staging mechanism and infer its quality from an Option-A smoke test.

## The pieces (all in loom/)
- **Seed — exactly three docs per subagent:** `loom_operating_core_run.md`,
  `loom_architecture_brief.md`, `loom_evaluation_process.md`. Nothing else in the seed.
- **Per-category trio:** `cat[N]_allchapters.md`, `pred[N].md`, `score[N].md`, for
  N ∈ {1A, 1B, 1C, 2, 3, 4.1…4.12, 5, 6} — dotted spelling, one everywhere.
- **Harness** (your protocol; the subagents never see it): `loom_eval_harness.md`. Reread it.

## Step 0 — confirm the staging mechanism BEFORE anything else
The method: seed the subagent with the three docs, then hand it the three payload files
**one at a time, each only after the prior phase's response comes back.** That requires
continuing the *same* subagent via `SendMessage`.
1. Probe it: spawn a throwaway `opus` subagent, capture its agentId, then call
   `SendMessage(to=<agentId>, ...)`.
2. If it returns cleanly, single-instance staging works — proceed. If it returns disabled
   or errors, stop and resolve it before any category runs. Do not fake the staging.

## Per category — run (model = `opus`)
1. **Verify `cat[N]_allchapters.md` upstream (your job, not the subagent's):** 12 chapter
   blocks present; the legitimately-empty chapters listed in the brief's §7 are expected —
   an absence there is architecture, not corruption. Surface only a chapter that is present
   but genuinely broken. (The subagent no longer halts on file integrity; that check is
   yours, here, upstream.)
2. **Spawn seeded with exactly the three docs** (full text of core + brief + process). No
   predictions, no scores, not even a description of them.
3. **Stage in order; require the response back before sending the next file:**
   - Msg 1 → full text of `cat[N]_allchapters.md` → wait for the content read + placement.
   - Msg 2 → full text of `pred[N].md` → wait for the prediction sharpening.
   - Msg 3 → full text of `score[N].md` → wait for the final response (ends with the card).
   Never send a later file early, never two at once, never preview a later input to answer a
   question — if it asks, decline and tell it to finish the current phase.
4. **Harvest:** from the Msg-3 response, extract everything between `===LOOM CARD START===`
   and `===LOOM CARD END===`, save as `card_[N].md`. Discard the prose before the block. If
   the card is malformed, ask once for a clean re-emit of the card block only; do not
   hand-repair the schema.
5. **Write the skeptic note.** From the *staging transcript* (not the card), produce
   `skeptic_[N].md` per the harness's skeptic-layer spec: quote every hedge, every
   cross-phase retraction, the most-elaborated PROTECT as prime suspect, any definition the
   subagent widened between phases, and a fresh-read priority list. Quote and locate, never
   judge. Set `BLIND: true` unless you happen to know the target finding (as on the smoke
   test), in which case `BLIND: false`. This is a mechanical extract, not a second read.

## Smoke test FIRST — category 6, and what "pass" means
Run 6 end-to-end before the other eighteen, on the mechanism confirmed in Step 0. Six is the
only category Brian has hand-run, so its card is the known-good check. This smoke test is
validating one specific thing: whether the process doc's **"find the native mode, then hunt
the absence"** instruction lets a blank-slate subagent independently see a finding no
instrument can — the kind an aggregate read misses.

**Pass condition (concrete):** the card independently surfaces the finding that **Ch 10 is
the only Reflection in the category with no living biological specimen** — the one reflection
that states the mechanism rather than discovering meaning through a creature — carried as a
VOICE finding with a *do-this* FIX (restore a creature; let the reflection complete its
sentence; make it the composed wave-trough before Ch 11's collapse). Do NOT put this finding,
or the "reflections run on specimens" frame, into the seed — that hands the subagent the
answer and buys a confirmation, not a read. The subagent must reach it from the general
method line alone. (Safe to name it here: this kickoff is orchestrator-only and never enters
the seed.)

- **Surfaces on its own** ⇒ the method generalizes for free; seed + staging + harvest all
  work; proceed to the eighteen.
- **Does not surface, even with the method line** ⇒ do not scale on the assumption the cards
  are complete. You've learned the load-bearing thing: the solo parallel pass cannot see
  absences, so Brian's live re-runs must read the prose *fresh*, not audit the card's finding
  list. Flag this to Brian before the eighteen; it changes how the verdict stage is built.

## Then the eighteen
Run the rest (parallelize as the environment allows; each internally staged, same mechanism).
Harvest all cards.

## Output — cards are candidates, not verdicts
Surface all 19 cards **each with its `skeptic_[N].md`** to Brian. The skeptic note's
FRESH-READ PRIORITY list is what he reads first — it points at the chapters to read cold
before a fluent card sets the agenda. Any finding whose CONF says "wants live re-run," plus
the strongest/strangest cards, earn a live conversation where the pushback loop exists.
Read the PROTECTs most skeptically: "here's why the thing you'd fix is actually intentional"
is a flag, not a reassurance — that's the sentence the smoke-test rescue hid behind.
**FIX stays in the offered register throughout.** Treating 19 unsupervised reads as final is
the same mistake as treating the surprise tally as a verdict.

## Known caveat to carry in
`score4.4.md` marks the ch11/ch12 tail N/A on a stale assumption that 4.4 ch12 was a stub,
but `cat4.4_allchapters` has content in ch12. That Input-3 file is slightly off at the tail
— regenerate 4.4's score tail first, or note it in the 4.4 card's INSTRUMENT_NOTE.
