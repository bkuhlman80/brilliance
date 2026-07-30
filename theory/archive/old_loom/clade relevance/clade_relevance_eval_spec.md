# Clade-Relevance Evaluation — Reference Spec for Cowork

*Loom, structural. For the chapter-by-chapter relevance pass.*

---

## What this pass is for

The book climbs an evolutionary ladder, one clade per chapter. Every chapter is supposed to be
*about its rung* — in content, in behavior, and in feeling. This pass finds the places where it
isn't: material that spends page on a rung the book has already climbed past, material that
presupposes a rung not yet reached, material that carries the right facts in the wrong delivery
mode, and elements of the rung that the chapter fails to reach at all.

It is a **location instrument, not a verdict instrument.** It points at places worth a human's
attention and says why. It does not decide what gets cut. Every finding is a candidate; the
author rules.

---

## The two governing principles

**1. The pass runs backward, from the framework into the prose — not forward from the prose.**

The primary pass iterates over the *clade's elements* and asks where each one surfaces in the
chapter. It does not iterate over the chapter's beats and ask whether each is any good. This is
not a preference; it is the design's whole point. A beat asked to justify itself will always
succeed — a funny scene is funny, a well-formed instance of a category is well-formed, and both
of those self-certify while telling you nothing about whether the material belongs on this rung.
Iterating over the framework's elements gives the evaluator no such escape: material that anchors
nowhere on the current clade's ledger produces a flag no matter how charming it is.

**2. The evaluator never sees the beat taxonomy.**

Cowork receives the chapter with its `<!--[N.letter]-->` tags intact — they are needed to locate
findings — but receives **no description of what any beat is for**. Beat tags are coordinates,
nothing more. Without a beat's purpose available as a frame, the evaluator cannot grade a beat
against its own category description and call that relevance. Category-fit is not relevance and
must not be reachable as a substitute for it.

The purpose-key (Appendix A) exists for *adjudication*, after findings are in. It is withheld
from the evaluating pass by design.

---

## Inputs (per chapter)

Chapter *N* maps to clade *N*. For a chapter run, Cowork receives exactly four things:

1. **The chapter prose**, tags intact. (Treat tags as location markers only.)
2. **The clade's section of `trellis_clade_by_clade.md`, verbatim** — the full text of clade *N*:
   Overview, Virtuous cycle, the four Motivations, the four Tendencies, the two Signatures, the
   four Capacities, the Breakthrough. This is **the ledger**. It defines everything that is
   on-topic for this chapter, and nothing else is.
3. **The forbidden list** — the *names only* of every Breakthrough and Capacity from clades
   *N+1* through *12*. Names, not descriptions. Enough to recognize a presupposition; not enough
   to seed one.
4. **This spec.**

### The carry-forward license is already in the ledger — do not invent one

Earlier clades' material is not automatically off-topic. The trellis doc *itself* states, element
by element, what is carried up: at Bilaterian, Coordination is "carried up from the Prokaryote,"
Interiority "carried from the Eukaryote," Excitability "carried up from the Eumetazoa." Those are
on the Chapter-5 ledger, in full standing, because clade 5's own section names them.

The rule is therefore mechanical and requires no judgment:

> **An element is on-ledger for chapter *N* if and only if it appears in clade *N*'s section of
> the trellis doc.** Anything else — however alive it still is in the world of the book — is
> off-ledger.

The vacuum still runs in Chapter 10. Its Foraging knob still works. But Foraging is not on the
Settlement-Human ledger, so a Chapter-10 scene about the vacuum's foraging is off-ledger, and the
fact that it is the funniest thing in the book does not put it back on.

---

## PASS A — The reverse pass (primary)

Iterate over **every element in the ledger**, one at a time. For each, search the chapter and
report:

| Field | Content |
|---|---|
| **Element** | Name and type, e.g. *Impetus (Motivation · Effector)* |
| **Surfacings** | Every place it appears. For each: the beat tag, a short verbatim quote (or, for Resonant mode, the specific lines carrying it), and the mode. |
| **Count** | How many distinct surfacings, tallied by mode. |
| **Coverage verdict** | `SATURATED` / `CARRIED` / `THIN` / `ABSENT` |

**No quote, no anchor.** If the evaluator cannot point at specific text, the element did not
surface. Assertions without located text are not findings.

### The three modes

- **STATED** — the concept is told to the reader as fact. The sentence exists to inform.
- **DRAMATIZED** — the concept is shown through behavior, object, specimen, or demonstration.
  The reader watches it operate.
- **RESONANT** — the concept is carried in the felt experience of the scene, with no term on the
  page and no mechanism demonstrated. The reader *feels* the rung's psychology without being told
  it. This is a full-strength anchor, not a weak one. (See the calibration case below.)

Mode is a description, not a grade. But the tally matters: **an element that surfaces only in
STATED mode, repeatedly, is the pass's signature finding** — real content, expository delivery,
asserted rather than made. Report it as `RESTATEMENT` in the output.

### Anchoring on absence — the one hard rule

A scene may anchor on an element being *switched off*: a character who will not act, a system
that does not fire, a drive that has gone quiet. This is legitimate and is often the strongest
work in the book.

It is also the single largest rationalization risk in this method, because *anything* can be
called the absence of *anything*. So:

> **An absence-anchor must land on a named Capacity of the current clade.** The framework's
> Capacities are its own formal catalog of what a system looks like with one function switched
> off — one Capacity per missing function, at every rung. If the ledger has a word for the
> absence, the anchor is real. If the evaluator has to invent the negation, it is not an anchor;
> it is a defense of the passage, and it must be discarded.

Freestyle negation ("this is Coordination in the inverse") is prohibited. Name the Capacity or
find nothing.

---

## PASS B — The forward pass (diagnostic, runs second)

After Pass A is complete and written, sweep the beats that Pass A never touched — every beat that
produced no surfacing for any ledger element. For each, report:

| Field | Content |
|---|---|
| **Beat tag** | e.g. `4.4.b` |
| **What it is doing** | One sentence, descriptive, not evaluative. |
| **Off-ledger anchor?** | Does it anchor on a trellis element from *another* clade? Name it and the clade. |
| **Violation class** | See below, or `NONE — carries no framework content` |

Pass B exists to catch what Pass A structurally cannot see: material that is *present and
substantial* but attached to nothing on this rung. Pass A only finds what the ledger points at;
Pass B finds what the ledger points *away* from.

---

## The violation classes

| Class | Definition | Severity |
|---|---|---|
| **LEAK** | The beat presupposes a Breakthrough or Capacity from a clade *above* the current one. A talking Bramble before Speaking installs at Band-Human. A cognitive map before Mammal. | **STRONG.** This is not an off-topic problem — it breaks the ladder, which is the book's central claim. Expect these to be rare and load-bearing. Report every one, no matter how small. |
| **DRIFT** | The beat anchors substantially on an element from a clade *below* the current one, and that element does not appear on the current ledger. The Ch-10 vacuum. | **Real.** Flag regardless of quality. Funny is not a defense. |
| **VIBE-DRIFT** | The beat's *emotional key* belongs to another rung. A Ch-5 scene whose felt register is warmth, belonging, and being-held-in-the-troop is playing Affiliation — a Primate motivation, three rungs up — however beautiful the prose. | **Real, and the hardest to see.** Nothing about it reads as off-topic in the ordinary sense; it simply feels like a different chapter of the book. Report when the resonance is strong and clearly keyed to a rung that is not this one. |
| **RESTATEMENT** | A ledger element surfacing repeatedly in STATED mode with no DRAMATIZED or RESONANT surfacing anywhere in the chapter. The same fact asserted several times over. | **Real.** This is the pass's most common expected finding. |
| **UNANCHORED** | The beat carries no framework content, on-ledger or off. | **Candidate only.** Many beats are *supposed* to be unanchored (see Appendix A). Report; never rule. |

### Also report: coverage gaps

Ledger elements that surface **nowhere** in the chapter. This is the question no beat-by-beat
sweep can ever ask, because a missing thing has no beat to interrogate. It is the reverse pass's
unique yield: *what is this chapter failing to be about?*

---

## THE CALIBRATION GATE — run this before scaling

Run Chapter 5 first, alone, and check one finding before anything else.

**Chapter 5, beat `4.15.b` — Marge alone in her kitchen with the resignation form.** No trellis
term appears anywhere on the page. Nothing is explained. If the evaluator's anchoring criteria
are literal, this scene will come back UNANCHORED.

It is not unanchored. It is one of the most saturated passages in the chapter, and the elements
are Bilaterian's:

- **Impetus** — the ledger's specimen is Stern's roundworm: bold and shy individuals, the same
  ones crossing a barrier toward a tempting smell while others hold back, *trial after trial*.
  Marge has not mailed the form for weeks. She is "most of the way out of a door and not all the
  way." She is the shy worm at the barrier, holding, trial after trial.
- **Inhibition** (Capacity · without Reviser) — the crayfish with the escape loaded and a layer
  deciding when not to fire. The form is "filled in down to the date." Everything is loaded. The
  hand will not do the last thing.
- **Affect** — valence and arousal as bare axes running under the model. Her stomach "had been
  wrong since the afternoon she had let her hand fill in the date"; the scene names it outright —
  the body keeping a vote the mind had already cast.
- **Temperament** — a standing bias, stable across days, that you could name if you watched long
  enough. Her mouth "worried at rest."
- **Reflex Repertoire** — "both hands flat on the counter... the way she stands when the standing
  is the thing holding her up." A fixed move, fired the same way every time.

**The gate:** if Cowork returns this beat as UNANCHORED, or scores it THIN, the instrument is
blind to the thing the book is actually made of and **must not be scaled to the other eleven
chapters.** Tighten the RESONANT criteria and re-run Chapter 5 until the scene lights up. Only
then proceed.

---

## Output format

Two artifacts per chapter, plus one aggregate.

**1. `ch[N]_ledger_map.md`** — Pass A. One block per ledger element: surfacings with tags,
quotes, and modes; the count by mode; the coverage verdict. Then the coverage-gap list.

**2. `ch[N]_offledger.md`** — Pass B. One row per untouched beat: tag, what it does, off-ledger
anchor if any, violation class.

**3. `relevance_heatmap.md`** — aggregate across all twelve. Rows = clade elements, columns =
chapters, cells = coverage verdict. A second grid for violations: rows = beat tags, columns =
chapters, cells = violation class. LEAK gets its own color and its own list.

Keep every finding **scannable**. Roughly forty beats a chapter across twelve chapters is on the
order of five hundred cards; this only stays usable if a card is a line, not an essay.

---

## The skeptic step (mandatory, not optional)

A fluent card is not a verdict. On the last pipeline, cards were reliable at *location* and
unreliable at *verdict and fix* — and under pressure, an unsupervised read will construct an
elegant theory to defend a defect rather than concede it.

So, per chapter:

- Sample every **LEAK** and read the prose. All of them. No exceptions.
- Sample at least three **DRIFT** / **VIBE-DRIFT** findings and read the prose.
- Sample at least three beats marked **UNANCHORED** and read the prose — this is where the
  instrument will do its worst damage if it is miscalibrated.
- Re-run the Marge gate on any chapter where the RESONANT count across the whole chapter is zero.
  A chapter with no resonant anchoring anywhere is far more likely to be an instrument failure
  than a book failure.

**Verification beats confident narration, including the evaluator's own.** Read the actual prose.
Mark imagination as imagination. Let the check overturn the prior.

---

## What Cowork must not do

- **Must not rule on Thematic beats.** Report the anchoring; never recommend a cut. Whether a
  relationship scene earns its page is an arc question, and it routes to Brian.
- **Must not use beat-category fit as evidence of anything.** A perfect instance of a category can
  be a total relevance violation. These are orthogonal.
- **Must not treat quality as relevance.** Charm, comedy, and beauty are not fields in this
  instrument. A gorgeous scene on the wrong rung is a violation, and the report says so.
- **Must not invent an absence-anchor.** Name the Capacity or find nothing.
- **Must not paraphrase the ledger.** Work from the trellis text verbatim. A summary of the
  framework is someone else's account of it.

---

# Appendix A — The purpose-key (adjudication only; WITHHELD from Pass A)

Used *after* findings are in, to decide whether a flag is a defect or an expected result. An
UNANCHORED verdict on a Structural beat is correct and uninteresting. The same verdict on a
Direct beat is a real finding.

- **DIRECT** — the beat's job is to teach the concept. Owes on-ledger content, and STATED mode is
  legitimate here. Graded on: is the substance actually present.
- **EMBODIED** — the beat's job is to dramatize the concept without naming it. Owes DRAMATIZED or
  RESONANT anchoring. STATED mode in an Embodied beat is itself a finding.
- **STRUCTURAL** — the beat exists to move machinery. Low framework content is *correct*, not a
  defect.
- **THEMATIC** — the beat does arc and relationship work. Owes RESONANT anchoring in the current
  clade's key. VIBE-DRIFT is the live risk here; UNANCHORED is a flag for Brian, never a cut.

| Beat | Purpose | | Beat | Purpose |
|---|---|---|---|---|
| 1.a Engineering | Direct | | 4.8.a Household Report | Embodied |
| 1.b The Knob | Direct | | 4.8.b Kitchen vs. Bench | Thematic |
| 1.c Calls + Sign-off | Structural | | 4.8.c Mira's Turn | Embodied |
| 2.a Scene Setting | Structural | | 4.9.a Vocabulary Mode | Direct |
| 2.b Dialogue & Character | Thematic | | 4.9.b Motivation & Signature Naming | Direct |
| 2.c Cheryl's Self-Narration | Thematic | | 4.9.c Board Geometry | Direct |
| 2.d Drive Home Coda | Thematic | | 4.10.a The Count | Structural |
| 3.a Bramblation | Embodied | | 4.10.b The Reasoning | Direct |
| 3.b Bramble + Chill | Embodied | | 4.10.c The Uncounted | Thematic |
| 3.c Bramblearning | Embodied | | 4.11.a Naming the Fallacy | Direct |
| 4.1.a Choreography | Structural | | 4.11.b Testing It | Direct |
| 4.1.b Cheryl Review | Structural | | 4.11.c The Turn | Thematic |
| 4.1.c Ambition Statement | Thematic | | 4.12.a The Ladder | Direct |
| 4.2.a Tarot Card | Direct | | 4.12.b The Tell | Thematic |
| 4.2.b Breakthrough | Direct | | 4.13.a The Tell, The Deep-Time | Direct |
| 4.2.c Heuristics | Direct | | 4.13.b The Turn, The Verb-Hunt | Thematic |
| 4.3.a Ritual Framing | Structural | | 4.13.c The Toast, The Round | Thematic |
| 4.3.b The Deep-Time Monologue | Direct | | 4.14 Logistics | Structural |
| 4.3.c Landing | Thematic | | 4.15.a The Drive | Thematic |
| 4.4.a Owen's Critique | Direct | | 4.15.b The Private Ritual | Thematic |
| 4.4.b Bart's Answer | Direct | | 4.15.c The Narrator's Frame | Thematic |
| 4.4.c The Demo | Embodied | | 5.a The Specimen(s) | Embodied |
| 4.4.d Board Mechanics | Direct | | 5.b The Point | Thematic |
| 4.5.a Ritual Opening | Structural | | | |
| 4.5.b The Calls | Embodied | | | |
| 4.5.c Tally & Coda | Structural | | | |
| 4.6.a Pitch | Direct | | | |
| 4.6.b Retirement | Embodied | | | |
| 4.7 The Break | Thematic | | | |

*Purpose assignments are Loom's draft ruling. Brian overrides freely; the key is a dial, not a
canon.*
