# Loom evaluation — orchestrator synthesis (all 19 categories)

Run complete. 19 category reads, each internally staged content → predictions → tally via a
single held Opus subagent (SendMessage), harvested to `card_[N].md` + `skeptic_[N].md`.
**These cards are candidates, not verdicts.** Read the skeptic notes' FRESH-READ PRIORITY
lists first — they point at the prose to read cold before a fluent card sets the agenda.

## How to read this pile
- Every `card_[N].md` is the subagent's deliverable. Every `skeptic_[N].md` is a mechanical
  extract (hedges, cross-phase retractions, most-elaborated PROTECT as prime suspect, a
  fresh-read priority list). BLIND: true on all except cat 6 (smoke test, BLIND: false).
- Read the PROTECTs most skeptically: "here's why the thing you'd fix is actually
  intentional" is a flag, not a reassurance — that's the sentence the smoke-test rescue hid
  behind (below).

---

## Carry this in first — the smoke-test result (cat 6)

The cat-6 smoke test did **not** pass on the original process. The solo pass mislocated the
target (put its finding on Ch 9, and affirmatively *cleared* Ch 10). A steered live pushback
then located Ch 10 but **exonerated** it — the instrument talked itself out of the finding as
fluently as it had talked itself in. You approved a fix: a **mechanical census step** added
to the Input-1 process (`loom_evaluation_process.md`; original backed up as
`loom_evaluation_process.md.pre_census.bak`). A clean re-smoke then surfaced **Ch 10 as F1
unaided** — but only the *location*; the earned-vs-defect *valence* stayed open, correctly
deferred to you. All eighteen ran with the census step.

**Load-bearing lesson:** the cards are fluent in both directions. Fresh-read the prose; do
not audit the card's finding list.

---

## Cross-category patterns (the twentieth-conversation material)

### 1. Narrator over-tells the thought at hinge / late / symbolic-line chapters — THE recurring finding
The book's signature art is "the thought that closes in the reader's head, not on the page."
The most-repeated flaw across the run is the narrator (or a coda) closing it *on the page*,
clustered at act-breaks (Ch 9), payoff turns (Ch 10), and the symbolic line. Instances:
- **6** F1 — Ch 10 states the mechanism vs. discovering it through a creature (smoke target)
- **4.1** F1 — Ch 3/6/10 POV-seating closes caption the beat / front-load later beats
- **4.5** F1 — Ch 11 "the city-self arrived at five years old" (abstract caption + double close)
- **4.6** F1 — Ch 9 "both were true at once and the book would need them both" (narrates its own method)
- **4.8** F2 — Ch 10 coda "the shape cannot watch itself hold" (re-states earned irony)
- **4.9** F1 — Ch 10 ladder/rung exegesis after the child's line lands it
- **4.10** F2 — Ch 8 paragraph psychological X-ray of Burns
- **4.11** F1 — Ch 9–11 "nobody said the plain fact of it" hardens into a template
- **4.12** F1 — Ch 11 Planner coda restates the paradox three times
Every instance is **ear-only or ear-primary** — the tally scores a caption as success (it's
not a surprise) and often on a beat the predictor guessed right. This is the single strongest
whole-book candidate and the thing most worth your live attention. Note the counter-reading
that recurs too: in the symbolic line, narrator-density is *designed* to grow — so several of
these are genuine valence calls, not settled defects.

### 2. Instrument-calibration profile (the tally)
- **Column OFFSET, confirmed independently by ~10 categories:** `c_k` scores the guess made
  *after* Ch k against **actual Ch (k+1)**; the last scored column's target is a spurious
  "Ch 13" (unscored). Re-index every tally by +1 before reading a cell. (Only the pre-census
  cat-6 v1 read cells naively; every clean card uses the offset.)
- **The seven axes are prose-TEXTURE axes** (Register/Concreteness/Interiority/Silence/
  Signature/Duration/Attention). They are structurally blind to: (a) captions/over-gloss
  (not a surprise); (b) POV/architectural rupture (texture holds while architecture breaks —
  cat 5); (c) earned inevitability (payoff chapters score lowest precisely because they land
  hardest — cat 3); (d) content-events in framework categories (voice stays faithful whether
  the idea detonates or goes inert — cat 4.7).
- **Therefore: low tally cells are NOT evidence of slack, and loud cells are usually the book
  working** (reveals, ruptures) **or the instrument breaking** (empty/truncated/placeholder
  chapters throwing false sweeps). At least once the tally *mis-valenced slack as a virtue*
  (cat 4.3 Ch 3 undershoot logged as a Duration violation = "surprise").
- **Duration is the noisiest axis** in several categories — blind readers can't gauge length;
  discount its violations as book events.

### 3. Symbolic-line (Ch 9–12) seed-then-withhold vs. slack
Several cards flag the late chapters as either the book's Book-1-closing patience (a capacity
*seeded* then deliberately withheld into Book 2) or genuine cooling. 4.4 (Ch 11 concealment
door opened, Ch 12 bramblogue absent), 1B/1C (late cooling), 6 (Ch 10 specimen absent). Mixed
valence; needs you. 4.4's F2 is explicitly contingent on a cross-check you can do: does the
Ch 12 WORM (4.12) or the Ch 12 essay carry the un-walked concealment door?

### 4. Corroboration-by-instrument-silence (a reasoning tic to watch in the cards)
Many ear-only findings are defended with "the tally can't see it, which proves it's the
ear-only kind." Valid per the process doc — but unfalsifiable. The skeptic notes flag this
consistently. Treat those findings as leads to fresh-read, not as corroborated.

---

## Integrity / artifact issues found upstream (my job, not the subagents')

All 19 content files had 12 chapter blocks with the §7-expected empties. But two blocks are
**present-but-broken**, and the apparatus files have defects:
- **cat4.2 Ch 10 — TRUNCATED.** ~400 words (vs ~1,400–1,700 neighbors); ends at Bart's
  "so I'll get out of his way" handoff, missing the breakthrough and all four capacities.
  Verified. Carried as artifact, not a book finding.
- **cat4.11 Ch 12 — TRUNCATED.** 48 words (title + byline + one sentence). Verified. Artifact.
  Ambiguous: deliberate inversion (retirement category ending on an *installation*, cut
  mid-log) or broken export — your call.
- **score4.4 — stale tail.** Ch 11/12 marked N/A on a wrong "Ch 12 was a stub" assumption;
  Ch 12 has content. Handled: 4.4's F2 rests on prose only, tally silent (not corroborating).
- **CR definitional split (4.1).** The prediction + score files define "CR" as *Cheryl-Review*
  (a Ch 2-only device); the brief says *camera-roll*. So the camera-roll red-light thread went
  **unscored** across the apparatus — a coverage gap other 4.x cards may share.
- **Brief/scorecard vs prose (4.4).** Both encode "Big O absent Ch 11," but the prose keeps
  Owen present as a pointed silence (the device's best moment). Risk: a continuity pass
  "fixes" the prose to match the stale spec. Correct the note, don't cut the silence.
- **Draft typos for Framework** (not book findings): 4.2 "chemotazis" / "the program haing
  depth"; 4.8 "hankercheif" / "you read it kid sitting in front of you".

---

## What earns a live re-run (ranked)

Nearly every VOICE finding is tagged "wants live re-run." Priority order for the room:

1. **cat 6 F1 — Ch 10 specimen absence.** The smoke-test finding; valence open (first
   caption-drift vs. earned City-Human pivot). Given the smoke-test history, read Ch 10 cold
   first. The census surfaced the location; only you settle the valence.
2. **The narrator-over-gloss cluster (pattern 1).** Sharpest instances to run: 4.9 Ch 10 (high
   conf), 4.8 Ch 10, 4.11 Ch 9–11, 4.6 Ch 9, 4.5 Ch 11, 4.12 Ch 11, 4.1 Ch 3/6. Decide once
   whether this is a book-wide tic or designed symbolic-line density — it recurs too often to
   settle per-card.
3. **cat 4.3 F1 — Ch 3 "Bigger" undershoot.** High-conf lapse by ear, but predictor+tally read
   the undershoot as a virtue. The one card where the instruments actively point the wrong way.
4. **cat 4.9 F3 — Ch 7 Bart's crossing buried under its proof.** Valence genuinely open
   (designed anticlimax vs. flattening the book's own stated event).
5. **cat 5 F1 / Jasmine under-isolated** and **cat 2 F1 / Ch 7 trough** — both cross-category
   questions (is Jasmine under-served book-wide? is a "trough" load-bearing?).
6. **The strongest/strangest cards to just re-read whole:** 6, 4.9, 4.8, 4.12, 5 (the
   book's spine and its confessional).

## Card index
| Cat | Lead finding (1-line) | # VOICE | Card / Skeptic |
|---|---|---|---|
| 1A | Ch 11 Extraverted knob thin; Ch 2 form-break | 2 | card_1A / skeptic_1A |
| 1B | Ch 6 build-log without Bart's tell | 1 | card_1B / skeptic_1B |
| 1C | Ch 10–12 honesty-ledger drops, dares calcify | 1 | card_1C / skeptic_1C |
| 2 | Ch 7 Arlo mirror-turn thin | 2 | card_2 / skeptic_2 |
| 3 | Ch 11 doubled stranger-briefing | 1 | card_3 / skeptic_3 |
| 4.1 | POV-seating close captions the beat | 1 | card_4.1 / skeptic_4.1 |
| 4.2 | Ch 3 two capacities go abstract; Ch 6 buried spine (Ch 10 TRUNCATED) | 2 | card_4.2 / skeptic_4.2 |
| 4.3 | Ch 3 undersells "boredom is the runway" | 2 | card_4.3 / skeptic_4.3 |
| 4.4 | Owen Ch 11 silence protect; Ch 12 engine absent | 3 | card_4.4 / skeptic_4.4 |
| 4.5 | Ch 11 double-close caption; Ch 2 scoreboard | 2 | card_4.5 / skeptic_4.5 |
| 4.6 | Ch 9 narrator over-explains | 1 | card_4.6 / skeptic_4.6 |
| 4.7 | Ch 6 framework runs cool (no wrangle); Lisa departure | 2 | card_4.7 / skeptic_4.7 |
| 4.8 | Protect the overrun; Ch 10 coda over-tells | 2 | card_4.8 / skeptic_4.8 |
| 4.9 | Ch 10 captions its peak; Ch 5 refrain silent; Ch 7 crossing buried | 3 | card_4.9 / skeptic_4.9 |
| 4.10 | Ch 5 drops Mira's seal; Ch 8 over-decode | 2 | card_4.10 / skeptic_4.10 |
| 4.11 | Ch 9–11 gloss template; Ch 8 over-gloss (Ch 12 TRUNCATED) | 2 | card_4.11 / skeptic_4.11 |
| 4.12 | Ch 11 Planner coda over-explains | 2 | card_4.12 / skeptic_4.12 |
| 5 | Jasmine un-isolated; Ch 5 Marge caption | 2 | card_5 / skeptic_5 |
| 6 | Ch 10 only Reflection w/ no living specimen (smoke) | 2 | card_6 / skeptic_6 |

Also on disk for the record: `card_6_v1_precensus.md` (the mislocated solo pass) and
`card_6_post_pushback.md` (the steered diagnostic that exonerated Ch 10).
