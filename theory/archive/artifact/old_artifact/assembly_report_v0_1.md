# Assembly report — manuscript v0.1

Deliverable: `manuscript_v0_1.md`, 87,008 words including Night headings.
Assembly only. No voice rewriting was performed.

---

## 0. The headline, first

**The manuscript assembles to 86,956 words of body text ≈ 290 pages at 300 w/pp.**
The targets in the task sum to 74,797 ≈ 249pp. The stated goal is 200pp ≈ 60,000 w.

**The overrun is 90 pages, and the reason is specific and fixable:** five of the thirteen
rows in the running-order table carry a cut instruction that no section of the task
specifies a method for. §2 gives a method for the Bureau, §3 for the cells, §4 for
four_analysts, §5 for apparatus. Nothing gives a method for cutting deep time, the cycle,
or the fourth floor, and the Bureau's named blocks contain far less text than its stated
cut. Those cuts were therefore not performed, per §9 step 5 ("cut only the blocks named")
and §10 ("silently trimming to hit 200" is a failure mode).

| Cut asked for | Words asked | Words the named method actually removes | Shortfall |
|---|---|---|---|
| §5 First/second/third floor (§2) | 7,600 | 431 | **7,169** |
| §7 Deep time | 8,300 | — no method given — | **8,300** |
| §9 The cycle | 1,900 | — no method given — | **1,900** |
| §6 four_analysts | 1,650 | 302 (strip only; §4 says it "goes in whole") | **1,348** |
| §8 The fourth floor | 1,400 | — no method given — | **1,400** |
| §4 The sixteen cells (§3) | 13,400 | **13,758** | +358 (over-delivered) |

The cells cut is the only one whose method was fully specified, and it landed. That is the
finding: **the budget does not close because four of the five remaining cuts were never
specified, not because the material resisted.** See TODO-1.

---

## 1. Section word counts against budget

| Section | Target | Actual | Delta |
|---|---|---|---|
| §1 Groundwork | 8,400 | 6,096 | −2,304 *(grow)* |
| §2 The front door | 2,900 | 3,830 | +930 |
| §3 The architecture | 15,000 | 11,816 | −3,184 *(grow)* |
| §4 The sixteen cells | 7,800 | 8,281 | +481 |
| §5 First/second/third floor | 7,000 | 10,716 | +3,716 |
| §6 Where I checked it | 4,500 | 5,852 | +1,352 |
| §7 Deep time | 7,200 | 15,243 | +8,043 |
| §8 The fourth floor | 5,200 | 5,327 | +127 |
| §9 The cycle | 6,000 | 7,412 | +1,412 |
| §10 The eleven seconds | 900 | 737 | −163 |
| §11 The tax | 4,600 | 2,965 | −1,635 *(grow)* |
| §12 Going down / final scene | 2,400 | 5,782 | +3,382 |
| §13 The ending | 2,897 | 2,899 | +2 |
| **TOTAL** | **74,797** | **86,956** | **+12,159** |

Baselines verified against the task before any edit: Part I 6,187 / Part II non-cell 12,780 /
per-cell 21,176 / Part III 15,494 / Part IV 7,903 / Part V 3,079. All matched exactly.

---

## 2. Cut log

### 2.1 The sixteen cells (§3) — 21,176 → 7,418 w, **13,758 cut**

Executed the manuscript's own Prokaryote rule. Per-cell word counts after the cut:

| Cell | Tier | After |
|---|---|---|
| Protocell | medium | 478 |
| **Prokaryote** | **full — unchanged** | **1,344** |
| Eukaryote | short | 315 |
| Eumetazoa | short | 417 |
| Bilaterian | medium | 526 |
| Vertebrate | short | 363 |
| Mammal | short | 373 |
| Primate | short | 526 |
| Band-Human | medium | 723 |
| Settlement-Human | short | 379 |
| City-Human | short | 345 |
| Empire-Human | short | 417 |
| Big Five Buildup | (not a cell) | 197 |
| Computer / Network / Model / Agent | short | 187 / 196 / 179 / 264 |

The three medium cells land under the ~900 w guide (478 / 526 / 723) because overview +
virtuous cycle + breakthrough is simply not 900 words in the source. Nothing was padded.

**Citation preservation: verified, zero losses.** 88 distinct author-year keys before the
cut, 88 after. 69 citations sat in cut stanza prose and were moved into the surviving cell
paragraph as a closing source sentence. Query run:

```
distinct author-year keys BEFORE=88 AFTER=88 ; MISSING AFTER CUT: none
```
(Two apparent misses, `Hrdy 2009` and `styles 1999`, were regex parse artifacts of
"Hrdy, *Mothers and Others*, 2009" and "Koolhaas coping styles 1999"; both confirmed present.)

No citation had nowhere to go. The digital-line cells carry no citations in the source.

### 2.2 The Bureau (§2) — 26,827 → 26,396 w, **431 cut**

Only the blocks named in §2 were cut, per §9 step 5.

| Block | Source lines | Words |
|---|---|---|
| Registrar of Weather — duplicate case-build | 1061–1071 | 190 |
| The Man in the Coat | 1017–1028 | 126 |
| Committee chamber, reduced to one paragraph inside the Chairman's section | 957–968 | 55 |
| Narrator address — "the reader should take hold of it now… the answer to everything in this book" | 215 | 25 |
| Narrator address — "Here is a thing the reader had better have straight…" | 285 | 26 |
| Narrator address — "Remember that sentence." | 571 | 3 |
| Narrator address — "It is important to be clear about this." | 955 | 8 |
| Narrator address — "That is the part worth noticing." | 1111 | 6 |

**One ruling I made and want on the record.** §2 says to keep the *second* Registrar
treatment and cut the first. Cutting the whole first section (lines 1029–1082) would have
destroyed **"the two people with the same hands and the woman standing up"** (lines
1079–1081), which is on the §2 do-not-touch list. The duplication is specifically the
*case-build* — cellar ledger, Thursday forty-one years ago, nine signatures — which the
first section builds at 1061–1071 and the second rebuilds at 1091–1103. I cut only that.
The portrait, the missing weather, the deafness, and the same-hands passage all survive.

**Narrator addresses:** the defect (narrator turning from the story to instruct the reader
to retain something) returned 12 instances. Five cut, **four kept as instructed**, three
left because they are not the defect ("that is in the report, because it is evidence" ×2,
and the "worth noticing" inside the protected cellar-steps passage).

Kept: *"Hold on to that. It is going to matter enormously."* / *"Keep an eye on the pen."* /
*"Now here is a thing the reader must hold on to, and it is the same thing as the two
columns on the doorstep."* / *"There is no table. The reader will forgive the repetition."*

**No Bureau prose was line-edited.** Each of the seven pieces is a contiguous block,
cleanly delimited, so a wholesale replacement drops in without re-deriving placement.

### 2.3 four_analysts (§4) — 6,151 → 5,852 w, **302 cut**

Six `**Filing.**` header blocks removed; the `*Scope: this draft covers…*` preamble removed
entirely; both `(see "…," Part N)` document pointers removed.

---

## 3. Apparatus audit

### 3.1 four_analysts (§4 table)

| Term | Before | After |
|---|---|---|
| `canon` / `Canon` — **project sense (the defect)** | 16 | **0** |
| `pre-canon` | 2 | **0** |
| `Smithers` | 1 | **0** ✅ mandatory |
| `Epistemic status` | 9 | **0** |
| `this document` / `this draft` | 4 | **0** |
| `inheritance cycle` (as doc pointer) | 7 | **0** |
| `**Filing.**` | 6 | **0** |
| `the framework` (self-reference) | 10 | **0** |

Two `canon` **tokens** survive and are correct English, not the defect:
`"…stated explicitly in the canonical treatments…"` and `"…no single account unifies canon,
legal precedent, citation, curricula, archives, and recordkeeping…"` — the second is *canon*
as a category of cultural institution, which is the sense the section is about. Sweeping the
token rather than the defect would have broken that sentence.

### 3.2 Framework (§5 table) — queries run before editing, re-run after

| Term | Before | After |
|---|---|---|
| `Epistemic status` | 58 | **0** |
| `Liana's BHOP` | 18 | **0** |
| `[framework]` | 32 | **0** |
| `[established]` | 13 | **0** |
| `[inference]` | 4 | **0** |
| `[open]` | 2 | **0** |
| `Ratified mapping` | 5 | **0** |
| `canon` — project sense | 17 | **0** |
| `this doc` / `this document` | 5 | **0** |
| `movements` (structural) | 1 | **0** |
| `Forward pointer` | 1 | **0** |
| `journal-paper pipeline` | 1 | **0** |
| Part N cross-reference | 11 | **0** |
| table of contents (5 `- **Part N —**` lines) | 5 | **0** |

56 bracket tags removed in total (the extra 5 over 51 were compound variants:
`[established as formalism; framework as a line-goo]`, `[framework, contested in the field]`,
`[framework — the strongest support]`).

Six `canon` **tokens** survive, all ordinary English: *canonical example* (Port-Royal),
*canon since Wiener*, *the canonical circuit*, *the shared canonical circuit*, and two
*canonical statement*.

**Two counts in the task did not match the file, and the discrepancy was the query, not the
text.** `this doc/this document` was given as 7; the token returns 5. Part cross-references
were given as 23; the actual pointer defect returns 11 (5 in the deleted contents block,
5 Part headings, and "Parts I and II describe… This Part describes…"). The `above`/`below`/
`earlier`/`later` family — 78 hits — is almost entirely substantive (*below setpoint*,
*earlier clade*, *later cell*) and was correctly left alone.

### 3.3 The `Liana's BHOP` residue sweep — **105 hits, logged not converted**

After the 18 were gone, I swept for the pattern §5 names: *any sentence where the manuscript
is the grammatical subject of its own claim.* Query:

```
\b(the framework|this framework|the framework's|this book|the book|
   this treatment|these pages|the present account|the account here)\b
```

**105 hits.** Representative: *"The framework holds that mitochondria are the engine of that
bigness."* / *"The framework claims that genes, brains, talk, and code run the same process."*
/ *"Where the framework stands. The framework proposes an accounting and a typology."*

§5 says to *log what comes back*, and I have not converted them. Converting 105 sentences to
first person in one pass is precisely the uniform-mannerism failure §10 warns about — the
same sentence-shape landing on a fixed interval for 290 pages. This is the single largest
voice-pass job in the manuscript and it should be done chunk by chunk with the author.
Full line-numbered inventory available on request. See TODO-2.

---

## 4. Epistemic-note map (§6)

58 notes before. **21 deleted (36%), 37 survive.** All headers stripped; all bracket tags
gone; no grading notation anywhere.

**Deleted (21).** Four went with the cell cut (Eukaryote, Eumetazoa, Primate, City-Human).
Seventeen more were marked:

- Part I: the "framework positioning, ratified" note.
- Part II: the 2×2-derivation note (it said **"HIGH confidence"** — grading notation, which
  §6 bans outright), and the two-goo note.
- Part III (6): attention-as-selection, the three-way distinction, the correlation-structure
  mechanism, the coevolutionary-events note, outgroup comparison, loss-versus-gain asymmetry.
- Part IV (7): apomixis, the second dissipative-structure note, the four discard classes,
  accessibility/morphospace, Weismann's barrier, the soil seed bank, erosion pressure.
- Part V (1): the residue-and-irreducibility note.

**Where the silences fall.** Deliberately *not* where the claims are safest. The two long
gaps are the deep-time stretch (genealogy, ecology, the goo test, the negative-findings
material) and the middle of the cycle (the sites, the discards, the seed bank, the liana
figure) — the two places the writing is plainly enjoying itself and reaching furthest. The
tax material keeps most of its notes, including the warm mend passage at the very end.

**Clustering preserved:** three notes still land close together in the Part II architecture
run (the four function-jobs, the absent-function extension, the layered-architecture note),
which reads as something bothering him on one page.

**Not done, deliberately:** the rewrites. §6 asks for the map and says not to attempt them.
Length variation across an order of magnitude comes from the voice pass; the surviving
notes currently run 21–292 w. See TODO-3.

---

## 5. The Nights (§7)

Fourteen headings. Sequence used:

> One · Two · Three · Four · Five · Six · Seven · **Eight and Nine** · Eleven · Twelve ·
> **Fourteen** · **Fifteen and Sixteen** · Eighteen · Nineteen

Regular One through Seven across Groundwork and the architecture. Past the first third it
degrades: two folded headings (Eight-and-Nine, Fifteen-and-Sixteen) and three skipped
numbers (Ten, Thirteen, Seventeen). Last heading is Night Nineteen, roughly two-thirds
through, inside deep time. **Nothing from there to the end** — the fourth floor, the cycle,
the eleven seconds, the tax, the final scene, and the ending all run without headings.

**The count does not resolve.** A reader counting headings gets 14. A reader reading numbers
gets to 19. Neither number is stated anywhere, and no total appears in the manuscript.

**No table of contents.** The five `- **Part N —**` lines and "This book carries five
movements" were deleted from the front matter — they were a contents page and the banned
word in the same block.

Heading structure below Night level: `##`/`###` kept where navigational, and the five
`# Part N —` headings deleted outright since the new section structure replaces them.

---

## 6. Hard-constraint audits (§8)

**Citation ceiling — PASS.** 52 distinct years appear in the assembled file. **Nothing later
than 2017.** Query: all `\b(19\d{2}|20\d{2})\b` matches, filtered to `> 2021` → zero results.
The ceiling has 4 years of headroom.

**Rule 3 — one item to surface.** `Smithers` 0, and 0 for every other novel name swept
(Marge, Lisa, Bart, Burns, Mira, HEXACON, Loom, Cheryl, Arlo, Provo). **One hit for
`Bramble`** — but it is the botanical bramble, inside the trellis/liana/climb vocabulary:
*"The bramble tops out at this line's Reviser cell."* Not the character. Flagged anyway,
because it is a lexical collision with a novel character name. See TODO-6.

**Nothing decodes.** No ciphers, acrostics, or resolving dates were introduced. The Nights
sequence was specifically built not to resolve.

**Religion / community / family — nothing devotional found; three analytic mentions logged**
as §8 requires:
1. *"religious orders and universities at the city level"* — an institution type in a list of
   elaborations.
2. `creed` ×2 in the Empire-Human cell — *"a currency, a law, a creed, or a shared identity"*
   and *"Coin, contract, and creed"*, both naming a class of universalizing framework.
3. The source's *"universalizing monotheism"* and the Caliphates example did **not** survive
   the cell cut and are gone.

None is devotional or anti-devotional; all three treat religion as a coordination technology.
The author's call. See TODO-7.

**Typography — done.** 3,147 double-spaces applied globally after all text moves. Zero
single-spaced sentence breaks remain. Markdown table rows and headings excluded; initials
(`E. O. Wilson`) and `et al. 2009` correctly not touched.

**Title — untouched**, including the "or/of" in `Liana's Brief History or Personality`.

---

## 7. TODO — growth targets, decisions, and strains

### Decisions the author needs to make

**TODO-1 — THE FIRST THING. The total is 290pp against a 200pp goal.**
Four of the five outstanding cuts have no specified method (deep time 8,300; the cycle 1,900;
the fourth floor 1,400; and 7,169 of the Bureau's 7,600). Levers, in the task's own order:
1. **The Bureau, currently 62pp** — far larger than the 42pp the task assumed, because the
   named cuts removed 431 w, not 7,600. It is a single-day first draft and the likeliest
   thing to shrink wholesale.
2. **The sixteen cells** are already *under* target and cannot give more.
3. **Deep time, 51pp** — carries the whole 8,300 overrun on its own.
Note that §12 (final scene, 5,782 w) and §5 (floors 1–3, 10,716 w) are each roughly double
their targets; the task's own "~2,700" and "~14,600" estimates were low against the file.

**TODO-2 — 105 manuscript-as-subject sentences.** The residue of `Liana's BHOP`. Logged, not
converted, on purpose (§10). Largest single voice-pass job.

**TODO-3 — 37 epistemic notes flagged for rewriting.** Map is in §4 above. They need the
order-of-magnitude length variation and the first-person inconsistency; do not do it in one
pass.

**TODO-4 — placement conflict in the task, resolved by judgment.** §2's table puts the final
scene in "§12"; the "Placement of the final scene, precisely" note puts it *inside* §11 The
tax, "after the duty-cycle transfer and before the mismatch argument". I followed the precise
note. There is no literal "duty cycle" in Part V — the transfer argument is the conservation
law ("the cost moves forward in time, or sideways onto another payer") and its audit, which
close out **The Visible Tax**. The mismatch argument is *"The maintenance-blind unit fails by
regime mismatch"* inside **When the Tax Comes Due**. I placed the final scene at the clean
section boundary between them (after *What a Selector Credits*), rather than splitting a
section mid-run. Move it 20 lines later if you want it literally abutting the mismatch para.

**TODO-5 — governing-document conflict.** `abhop_text_companion_brief.md` §3 says to convert
the epistemic notes into *"one person's fixed grading notation… introduced once, tersely…
then applied relentlessly."* `the_author_john_smirker.md` (v1.1) says the exact opposite:
*"No grading notation… A system maintained flawlessly across two hundred pages is the
fingerprint of an editor,"* and calls it "the exact defect this rewrite exists to remove."
The task's §6 follows Smirker. I followed Smirker. The companion brief also still recommends
the superseded "bench technician" biography and spells the name *Smircher* (as does
`artifact_context_brief_v1_0.md`, which additionally calls the book *Liona's*). Worth a
version bump on the companion brief so the next reader isn't working from a retired ruling.

**TODO-6 — `Bramble`.** One botanical use in the digital-line material. Not the character,
but it is the character's name. Strike or keep.

**TODO-7 — three analytic mentions of religion.** Logged in §6 above. §8 wants religion
simply absent; these are institutional/analytic rather than devotional. Author's call.

**TODO-8 — the digital line and Rule 3, raised as a question not a finding.** The Agent cell
is an explicit structural prediction about self-directed goal-formation, and it names
"the problem of a goal pursued with stability negated." Nothing names a robot, a team, a
competition, or a child, and the line is load-bearing structure the task itself depends on
(§2 places the fourth floor at the digital-line-as-terminal-Reviser material). Raising it
only because "predicts anything in the novel" is a broader test than "names."

### Growth targets — marked in place, not written

Per the task, no new material was written. Three sections are under budget by design:

| Section | Now | Target | Needed |
|---|---|---|---|
| §1 Groundwork | 6,096 | 8,400 | +2,304 |
| §3 The architecture | 11,816 | 15,000 | +3,184 |
| §11 The tax | 2,965 | 4,600 | +1,635 |

Growth is voice work: restatement, second person, worked examples with the arithmetic shown,
in-line admissions of ignorance. §11 is the most promising — it is the shortest section
against target and it is where the maintenance material and the one warm passage live.

### Open items from §11 of the task

- **"Four organizations, thirty-seven years"** — present in the ending, in the loose-ends
  material: *"There is no room with all three of those people in it. Four organizations,
  thirty-seven years, and I never saw a problem get solved that did not belong to somebody
  in particular."* This is the one place the career is on the page. Flagged for striking.
- **The design-condition arithmetic** — present and *internally correct*: 8,760 hours in a
  year, one percent is 87.6, called as 88 hours. The arithmetic checks. What still needs a
  source is the convention itself (that the design condition is the 1%-of-hours figure)
  before print.
- **Citations with nowhere to go** — none. All 69 relocated.

### Bureau continuity strains after the split (§2 asks to list, not fix)

The six-week clock now spans ~290 pages. Every strain found:

| Where | Strain |
|---|---|
| Front door | *"You will meet them on the fourth floor, sitting in a chair by a window"* — forward reference to a piece now ~120pp away. |
| Front door | *"Then he did something Dera did not understand for six weeks"* — sets a clock that now runs the length of the book. |
| Second floor | *"You know what that is about. You were there. It was the small thing in the dust on the doorstep, in her first ten minutes."* — back-reference to piece 1, now ~60pp back. |
| Second floor | *"it is the same thing as the two columns on the doorstep, so it should not be difficult"* — same, and it asserts the callback is easy. |
| Second floor | *"It stayed there for four weeks… while she went up two more floors and down a cellar"* — forward reference to floors not yet read. |
| Third floor | *"In the fourth week she told him what had happened at the Archivist's register in her first week."* — back to piece 2. |
| Eleven seconds | Now sits in §9, ~110pp from the doorstep it depends on: *"she looked at the two chalk columns on the step"*, and *"On the third floor the Registrar went on writing. On the first floor the forty…"* — references both floors from outside them. |
| Final scene | *"which the Porter told her on the first day"*; *"She broke them eleven times in her first hour"*; *"She had walked in with it six weeks earlier"* — three separate reaches back to piece 1, now ~250pp away. |
| Sizing | Installments are unevenly sized as required: 3,830 / 4,213 / 2,554 / 3,949 / 5,327, plus the 737 extraction. The fourth floor **is** the largest floor installment. Note the final scene (5,782) is larger still, so the fourth floor is not the largest Bureau block overall. |

---

## 8. What was not done, and why

- **No voice rewriting.** No paragraph was rewritten into Smirker's voice. No restatement,
  second person, worked examples, or in-line admissions of ignorance were added to existing
  prose. First-person conversions were made *only* where §4 and §5 explicitly required them
  (the 18 `Liana's BHOP`, the `canon` instances, the `framework`-as-subject sentences inside
  four_analysts).
- **No growth material written.** Three sections sit under target with TODOs.
- **The ending untouched.** `ending_draft_v0_1.md` went in verbatim — verified
  whitespace-normalised identical. The numbered list still has 1 and 2 and no 3. It still
  breaks off mid-sentence: *"…two readings of a unit that has changed in the meantime, and"*.
  No closing line, no heading, no completion.
- **The unspecified cuts.** Reported rather than invented.
- **The 105 residue sentences.** Logged rather than converted.
