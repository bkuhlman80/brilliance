# Label-Change Rubric  
A checklist for evaluating proposed pair-label and triple-label changes in ****Inheritance_Regimes_v2_5.md****. Most tests apply equally to triple labels with minor adjustments — primary-capture (test 2) does not, since triples have three primaries rather than two. Run before submitting a label change to Claude Code, or as a review pass after a draft.  

## How to apply  
**Force binary calls on each test.** Either Pass or Fail. There is no marginal pass; if a test feels marginal, the analysis isn't done or the test wording isn't tight enough. Resolve the ambiguity rather than averaging it.  
**Discipline-native reader standard.** Tests 1, 2, and 9 evaluate the label as a discipline-native reader would interpret it, bringing their disciplinary operationalization with them. A naive-reader interpretation (the label read as colloquial English without disciplinary context) is too strict. The label-plus-anchor combination is what gets evaluated, not the label alone.  
**Test weighting.** The 17 tests do not contribute equally to a label decision.  
* **Primary discriminators (Tests 1, 2, 9):** These usually decide whether a label is good. Run these first. If a label fails any one of these, it fails — no need to run the others. If two candidates both clear all three, see the tie-breaking procedure below.  
* **Dimensional integrity (Tests 3, 4, 5, 6, 7):** These catch a specific failure class — labels that are type-essential or that name only the high pole of an unnamed dimension. Always run.  
* **Adjacency (Tests 10, 11):** Triple-coherence and sibling differentiation. Apply where relevant.  
**Vet candidates against the killing test.** Before proposing a replacement label, check it against the test that caused the previous candidate to fail. Do not propose A and then realize A has the same problem as the rejected B.  
  
## A. Function and primary fit *(primary discriminators)*  
### 1. Cybernetic-function fit  
Each row-slot has a defined cybernetic function: Controller (R1×R2, closed-loop control), Anticipator (R2×R3, model-informed regulation), Adapter (R3×R4, self-revising model), Explorer (R4×R1, exploratory action). The label has to read as that function.  
**To run:** Give a discipline-native expert the cybernetic function definition for the row-slot. Ask them to name the phenomenon the framework is pointing at. Would they reach for this label or a near-synonym?  
**Pass:** Yes — the discipline-native expert would describe this phenomenon with this label or a close cognate.  
**Fail:** No — the label evokes a different function. A Controller label that reads exploratory; an Adapter label that reads stabilizing; an Explorer label that reads constraining.  
**For pair labels:** the cybernetic function is one of Controller (R1×R2, closed-loop control), Anticipator (R2×R3, model-informed regulation), Adapter (R3×R4, self-revising model), or Explorer (R4×R1, exploratory action).  
**For triple labels:** the synthesis function is one of Planner (R1 absent, deliberative planning), Pursuer (R2 absent, adaptive goal-pursuit), Reactor (R3 absent, reactive control), or Conservator (R4 absent, anticipatory homeostasis). Triple labels must read as their synthesis function class.  
**Function descriptions for Test 1 use framework primitives only.** Combine the cybernetic or synthesis function with the level-specific motivation contents and unit-identity per `function_descriptions_reference.md`. Discipline content enters at the candidate-evaluation stage, not in the function description itself. Discipline-painted function descriptions silently bias the label search.  
## 2. Primary capture  
A pair label should evoke both contributing motivations, not just one.  
**To run:** Show the label to a discipline-native expert. Ask them to back-derive the two primaries from the label alone, without seeing the row-slot. Both primaries must be detectable.  
**Pass:** Both primaries are detectable. Asymmetric weighting is fine — one primary may carry more weight than the other — but both are recoverable.  
**Fail:** One primary is not detectable from the label, or detection requires interpretive stretching ("X is implicit because the construct presupposes it"). Implicit-by-presupposition is not detection.  
**For triple labels:** all three primaries must be detectable from the label, with the same Pass/Fail logic. Implicit-by-presupposition is not detection.  
  
## B. Dimensional reading *(filter — catches type-essentiality and high-pole collapse)*  
### 3. Within-type variation  
A dimensional label must describe a real spectrum among instances of the type.  
**To run:** Enumerate three or more real-world instances of the type. Place them along the proposed dimension from low to high. The placements must be meaningful and discriminable.  
**Pass:** A clear spectrum exists with recognizable exemplars at low, mid, and high ends.  
**Fail:** The dimension only discriminates between instances and non-instances of the type — the signature of a type-essential label, which belongs in ****capabilities_and_virtuous_cycles.md**** rather than the label library.  

### 4. Bottom-of-distribution  
The canonized dimensional rule applied as a test.  
**To run:** Imagine the lowest-scoring possible instance of the type on this dimension. Is it still an instance of the type (a poor one) or a non-instance?  
**Pass:** Low scorers are still instances.  
**Fail:** Low scorers are non-instances. If the label fails, the type-essential content needs to move to the capabilities doc and the pair-slot needs a different, dimensional label.  

### 5. Dimension vs. high-end  
The label must name the dimension itself, not just the high-end behavior on that dimension. When a label collapses to the high end, the low end becomes unsayable except by negation.  
**To run:** Construct two sentences: "Instance X is high on [label]" and "Instance X is low on [label]." Both must parse as meaningful claims about real instances.  
**Pass:** Both poles are sayable. "High Reliable" and "Low Reliable" both describe real computers.  
**Fail:** Only the high pole parses, and the low pole reduces to "non-X" or "default." If the label fails, find a dimensional anchor that admits both poles, or rewrite to the underlying dimension.  
**On bipolar dimensions:** labels name dimensions. A configuration that sits at the low pole of the dimension is still labeled by the dimension. Test 5 fails when the label has no low pole at all (i.e., when "low [label]" reduces to non-instance). It does not fail when a particular configuration happens to fall at the low end.  

### 6. Valence neutrality  
A dimensional label should not smuggle a positive or negative pole into the construct unless the framework is making that choice deliberately.  
**To run:** Say "Instance X is low on [label]" out loud. Ask whether the statement sounds neutral, accusatory, or approving.  
**Pass:** Both poles can be asserted without baked-in praise or blame, OR the valence is intentional and matches a literature precedent. (Big Five names Neuroticism at the negative pole rather than as Emotional Stability — a deliberate theoretical commitment, not an accident.)  
**Fail:** The label sounds approving or disapproving and the valence wasn't chosen on purpose. Decide between adopting the valence intentionally (and documenting why) or finding a value-neutral term.  

### 7. Persistence intact, meaning stable  
Pair labels persist upward through every level the configuration remains in the active foreground. The new label has to keep working at every persistence level AND mean the same construct at each level — coherence alone is not enough.  
**To run:** Identify which levels the pair persists to (consult the row-slot pair table). For each level, ask two questions: (a) do real-world instances of that level vary along this dimension? (b) Is the dimension the same construct at this level as at the level where the label was born?  
**Pass:** Both readings hold at every persistence level.  
**Fail:** Dimension goes flat at higher levels, OR shifts meaning under the persistence rule (coherent at each level but slipping in construct from level to level — e.g., "protocol conformance" at Networks shading into "API conformance" at AI/ML and "agent protocol conformance" at Agents).  

### 8. Triple labeling: form convention
Triple labels carry a form risk that pair labels don't. The configuration is named by which motivation is absent, which invites character-type framing — descriptions of "the entity that emerges when X is in shadow." Adjective character-type labels reliably fail the dimensional reading tests in section B: they collapse Test 5 (the low pole becomes "non-X" or "default"), they fail Test 6 (character types carry valence — Selfish, Callous, Aimless, Hungry), and they quietly mis-cite Test 1 by naming a phenotype rather than a synthesis function.
Convention. Triple labels should take the form of construct names — typically nouns (Sensitization, Appetence, Predictive Homeostasis). Adjectival forms may pass only when a discipline anchors the adjective as a measured bipolar dimension with both poles named in the literature (e.g., Neurotic from Big Five Neuroticism, where the dimension is itself the construct and the low pole is measurable).
The default form for triples is the noun. Adjectival triple labels are admissible only under the discipline-anchored exception above.
Pair labels are not subject to this convention. Pair-label form follows the construct name closest to the discipline-native dimensional vocabulary; compound adjective forms (Conscientious-Habitual), noun-phrase forms (Exploration-Dispersion), and single-construct names (Coalitional) all qualify equally.

## C. Disciplinary anchor *(primary discriminator)*  
### 9. Anchor real, primary, discipline-named, and dimensionally matched  
The Notes column carries the disciplinary anchor that justifies the label. Two things have to be true: the anchor exists as a real, primary citation; AND the discipline uses the term in the same dimensional sense the framework wants. The second is more often missed than the first, because verifying a citation exists is mechanical while verifying the discipline-native sense matches requires deeper analysis.  
**To run:** First, identify the dimensional sense the framework wants — what does "high X" vs. "low X" mean in the framework's usage? Then name the discipline that owns the construct and ask whether its native usage matches:  
* Does the discipline use the term as a *dimension* (the framework's mode) or as a *category* (mismatch)?  
* As a *property* (matches) or as a *metric* (mismatch)?  
* As a configurational state (matches) or as a capability descriptor (mismatch)?  
Only after that check, verify the citation itself: name the author or work, verify it exists, verify it is primary to the labeled construct rather than a tangential mention.  
**Pass:** The discipline-native sense matches the framework's dimensional use, AND the anchor is identifiable, real, and primary.  
**Fail:** Discipline-native sense differs from framework's use (category-vs-dimension, metric-vs-construct, capability-descriptor-vs-state); vague anchor ("ML literature"); wrong attribution; or a citation that exists but doesn't actually anchor *this* construct.  
**Empty Notes = automatic Fail.** A label without an anchor in the Notes column fails Test 9 regardless of structural cleanness. The H-confidence flag presumes anchor existence; if the anchor is not written down, the H presumption is unverified.  
**Operationalization in Notes.** The Notes column carries a citation plus the operative phrase from the discipline that makes both primaries (or all three primaries for triples) recoverable. "Author Year" alone is incomplete; the operationalization phrase is what closes the discipline-native reader's interpretive loop.  
  
## D. Adjacency *(adjacency check)*  
### 10. Triple coherence  
The triple labels at the same level that share both primaries with the pair should read as elaborations of the pair: pair + third primary = triple's character. If the new pair label breaks this, the pair is likely under-specifying or mis-specifying.  
**To run:** Identify the two triples at the same level that include both primaries of the pair. For each, read aloud "[pair label] + [third primary] = [triple label]" and ask whether the elaboration tracks.  
**Pass:** Both elaborations read coherently.  
**Fail:** A triple becomes incoherent or feels disconnected from the pair when stated this way.  
## 11. Differential specificity  
Each pair label at a level must be distinguishable from its three siblings (the other three pair labels at the same level). If a candidate label blurs with another label at the same level, the four pairs aren't doing distinct work.  
**To run:** For the level where the label is born, list the four pair labels. Describe a real instance that scores high on the proposed label but low on the other three. Then describe an instance for each sibling that scores high on it but low on the proposed label.  
**Pass:** Real instances exist that distinguish the proposed label from each of its three siblings.  
**Fail:** Two labels collapse into the same description, or no real instance can be cleanly placed high on one and low on another. Resolve by sharpening the proposed label's dimensional content, or by noting the redundancy explicitly.  
  
## E. Tie-breaking  
When two or more candidates clear all three primary discriminators (Tests 1, 2, 9) and all dimensional-integrity tests (3, 4, 5, 6), the rubric does not strictly rank them. Apply the following procedure in order:  
1. **Function-fit specificity.** Prefer the candidate whose Test 1 reading is most specific to the row-slot's cybernetic function — not just compatible with it. A label that *only* describes the function in question beats one that could plausibly describe an adjacent slot.  
2. **Primary-capture balance.** Prefer the candidate whose Test 2 capture is most balanced between the two primaries. A label that evokes both primaries equally beats one that captures both but leans heavily on one.  
3. **Persistence robustness.** If the pair persists across multiple levels, prefer the candidate whose construct stays most stable across persistence levels (Test 7).  
4. **Anchor centrality.** Prefer the candidate whose anchor is most central to the discipline that owns the construct, rather than peripheral or contested within the discipline.  
If candidates tie on all four, they are genuinely interchangeable on rubric grounds. Author preference and project aesthetic are then legitimate decision criteria.  
  
## Appendix: Five-tier confidence rubric  
Confidence flags follow a five-tier rubric:  
* **H** — validated construct from level-matched literature, function-fit clean.  
* **MH** — strong domain term with minor scope mismatch or scholar-borrowed but neutral; OR coherent with function and reads cleanly without literature anchor.  
* **M** — reasonable extension into new domain, function-fit acceptable.  
* **LM** — scholar's term from contested literature, OR fits structurally but reads jargony, OR the level's domain premise is iffy.  
* **L** — speculative placeholder.  
