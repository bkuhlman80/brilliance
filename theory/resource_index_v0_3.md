# Resource Index

*Working document. v0.3. May 2026.*

---

## Purpose

Tells future-Claude what reference material is available for the book project and where each kind of question should be taken first. Drafting depends on knowing which doc holds which kind of authority. This index is the map.

The project has three resource tiers:

1. **Project files in `/mnt/project/`.** Canonical for the framework. Always read at conversation start. The first place to look for anything ABHOP-specific.
2. **The research papers repository (Smithers).** A SQLite-indexed, tag-organized collection of 721 papers with annotations. Accessible via Claude Code. The first place to look for empirical or technical primary sources.
3. **The NotebookLM book collection.** Roughly 100 books across consciousness, evolution, personality, civilization, philosophy, and applied psychology. Queried by Brian. The first place to look for sustained theoretical or philosophical treatment from a specific author.

When more than one tier might have an answer, the project files take precedence; they are where the framework's current commitments live. The papers and books are sources the framework draws on, not the framework itself.

---

## Project files

All paths are relative to `/mnt/project/`. Files are read-only and represent a snapshot at conversation start. If Brian mentions editing a doc mid-conversation, the snapshot is stale and the updated content should be pasted in.

### Framework core

**`Personality, Evolution, and Cybernetics.md` (PEC).** *(Moved to `inbox/` — awaiting paper_index and annotated_bibliography processing.)* Foundational cybernetic framing document. Personality as biographical signature; the cybernetic-inheritance foundations; the four cybernetic functions; adjacent pairs as closed feedback loops; triples as 2×2 syntheses; opposite pairs as level-defining couplings (full per-construct treatment of all twelve signatures, the mammalian threshold, and the relationship to triples — formerly `opposite_pairs_v0_1.md`); the stack-accretion and rolling-window mechanics; the maturity gradient; what ABHOP adds. Theoretical content now also lives in `rolling_burns_v1_0.md` as the "Framework Foundation" section (headers demoted one level). First place to go for the framework's load-bearing theoretical claims and for opposite-pair questions: read `rolling_burns_v1_0.md` Framework Foundation until PEC is re-filed post-processing.

**`Inheritance_Lines_v3_0.md`.** The framework's canonical structure: the three lines (genetic, neuronal, symbolic), the per-cell treatments across all twelve cells, the row-slot view, the bridge-entity pattern, off-thread branches, acceleration and pacing, the 3D stack visualization, and the literature-context-and-contributions section. Also incorporates the foundational goo-theory layer (formerly `What_Lines_Are_Made_Of.md`): each line ratchets a different kind of goo; each line has its own R0; the structural mirror and the domain shift; disease/disorder/line of failure; where personality and suffering live; the goo test for a fifth line. First place to go for the canonical labels at each cell, the line-architecture commitments, and goo-level theoretical questions.

*`notes_on_neuronal.md` content incorporated into `clade_reference_neuronal_v0_2.md` (v0.3) cross-cutting notes (implicit-model/generative-model regulation section) — source deleted.*

### Empirical anchors

**`clade_reference_genetic_v0_2.md`.** Per-cell empirical reference for the four genetic-line cells (Protocell, Prokaryote, Eukaryote, Eumetazoa). Each entry gives what the cell is, the milestone breakthrough, key references from Smithers extractions with traceability flags (HIGH/MODERATE/LOW), and fun specifics. R-numbers replaced with function names (Effector/Regulator/Modeler/Reviser). Also contains an Intellectual Kinships section (v0.3) with genetic-line absorptions (Darwin, Maturana & Varela, Deacon, Nick Lane) and convergences (Boltzmann/Shannon, Tinbergen, von Uexküll, Dawkins, Pollan, Ginsberg & Jablonka) — formerly in `we_think_so_too_v0_1.md`. First place to go for the empirical literature anchoring a genetic-line cell.

**`clade_reference_neuronal_v0_2.md`.** Per-cell empirical reference for the four neuronal-line cells (Bilaterian, Vertebrate, Mammal, Primate). Same structure as the genetic clade reference. R-numbers replaced with function names. Also contains (v0.3): a cross-cutting note on implicit-model vs. generative-model regulation (Stanovich tripartite mapping, niche-construction as lineage-level R2 regulation, active inference four capabilities, empirical anchors — formerly `notes on neuronal.md`); and an Intellectual Kinships section with neuronal-line absorptions (Friston, Bennett, Bowlby & Ainsworth, Miczek, Deci & Ryan, Koolhaas, Sih/Bell/Johnson, Barton & Dunbar, DeYoung, HEXACO, Dark Triad, HiTOP, Core Self-Evaluations, Self-Conscious Emotions) and convergences (Réale, Freud, Carl Jung general) — formerly in `we_think_so_too_v0_1.md`. First place to go for the empirical literature anchoring a neuronal-line cell.

**`clade_reference_symbolic_v0_2.md`.** Per-cell empirical reference for the four symbolic-line cells (Band-Human, Settlement-Human, City-Human, Empire-Human). Same structure as the other two clade references, with the constituent-human framing explicit. R-numbers replaced with function names. Also contains an Intellectual Kinships section (v0.3) with symbolic-line absorptions (Harari, Social Identity cluster, Haidt, Boyd & Richerson/Henrich, Deacon *Symbolic Species*) and convergences (Pinker) — formerly in `we_think_so_too_v0_1.md`. First place to go for the empirical literature anchoring a symbolic-line cell.

### Book architecture

**`Book_Frame.md`.** The book's narrative-architectural commitments: the twelve-quarterly-retrospective premise, the autofiction commitment, the narrator (Jasmine), the lab (Ben/Bart/Lisa/Marge), the home (Jasmine/Ben/Mira), Mira, Bramble, the format, voice, the Pragmatist tension, and time. Incorporates lab-mechanics content (formerly `trellis_lab_v0_3.md`): what the lab is, what the lab does, the team, quarterly meeting attendees, the retrospective four-segment format, real names, and the funder. First place to go for any question about the book's narrative frame or lab mechanics.

**`chapter_plan_v0_5.md`.** Higher-level scaffold above `bramble_across_the_stack` and `Book_Frame`. Time-keeping, seasonal mnemonic, arc shape, per-chapter briefs, and open editorial questions. Also incorporates the full writing process (formerly `writing_pipeline_v0_2.md`): the four stages (drafting, pot-throwing, integration, voice), what drafting is and is not for, drafting voice policy (POV is Jasmine; dialogue near-final; interior in functional prose informed by her traits), the handoff artifact format, gap handling, and when-in-doubt rules. First place to go for "what is this chapter doing" questions and "what stage of the work is this" questions.

**`bramble_across_the_stack_v2_0.md`.** Per-cell Bramble scenarios across all twelve cells. Each cell has Architecture, The knob, The day, What's missing, and What the scenario illuminates. First place to go for the architectural detail of any specific cell. This is the scenario bible.

### Pedagogical scaffolds

**`marges_fallacy_arc_v0_2.md`.** Marge's recurring fallacy-section arc across all twelve chapters. Phase one (Ch 1–4): names Noble Savage, Blank Slate, Ghost in the Machine, and Dealt Hand one per chapter. Phase two (Ch 5–10): riffing without unified theory, including the first structural rhyme and the type hypothesis. Phase three (Ch 11–12): synthesis (each fallacy denies one cybernetic function; each is held by people whose shape lacks that function) and closing claim. Also contains the full Ch 5 Pavlov round: self-portrait mapping, scene draft (~750 words), voice and beat notes per character, and chapter-level open questions. Also contains (v0.2, updated): a "Structural convergence: Psychological Types and MBTI" section — the Venn geometry explains MBTI's four dichotomies and predicts its intercorrelations; relationship is structural convergence, not vocabulary absorption — formerly in `we_think_so_too_v0_1.md`. First place to go for Marge's fallacy content and the Ch 5 Pavlov round.

**`rolling_burns_v1_0.md`.** Full drafts of Burns's rolling segments in Ch 9–12. Ch 9: Reactor across five levels (cartoon Burns face). Ch 10: Conservator across six levels (cartoon Marge face). Ch 11: Planner across seven levels (cartoon Lisa face). Ch 12: Pursuer across eight levels (cartoon Bart face; Bart rolling himself). Also contains a "Framework Foundation" section incorporating the full PEC theoretical document (headers demoted one level) — the grounding for the four constellational shapes rolled across those chapters. First place to go for Burns's rolling content and, until PEC is processed and re-filed, for PEC's theoretical content.

*`bart_rollings_v0_1.md` renamed and superseded by `rolling_burns_v1_0.md` (content assignment changed from Bart to Burns; lab-member "Bart" references updated to "Burns" throughout; cartoon character references — Bart Simpson, Bart face, Bart. The cartoon., Bart owns the absence — preserved unchanged).*

**`lisa_presentations_v0_1.md`.** Lisa's twelve quarterly presentations, one per chapter. Locks vocabulary discipline (CS/biology/neuroscience native, aversive to psychology terms), per-chapter argument structures (what Lisa lands, in what order, what is new, what carries forward, what is deferred, cross-line analogue work, where Jasmine plays reader-proxy), and the cumulative arc across all twelve. First place to go for what Lisa is presenting in any given chapter.

**`audience_anchors_v0_1.md`.** Three audience-slot anchors plus the Lisa reader profile. The audience asymmetry, the prestige gradient, yins as dyads, the extreme-by-framework distinction, and type populations. First place to go for reader-modeling questions, including who the book is written for.

*`we_think_so_too_v0_1.md` content distributed and source deleted. MBTI/Psychological Types structural convergence → `marges_fallacy_arc_v0_2.md` (new section after Open Questions). Biological entries → `clade_reference_genetic_v0_2.md` (Intellectual Kinships). Psychological entries → `clade_reference_neuronal_v0_2.md` (Intellectual Kinships). Sociological/historical/anthropological entries → `clade_reference_symbolic_v0_2.md` (Intellectual Kinships). For "who else has said something close to ABHOP's claim about X" questions, go to the relevant clade reference's Intellectual Kinships section.*

### Process

*Writing process content now lives in `chapter_plan_v0_5.md` under the "Writing Process" section (`writing_pipeline_v0_2.md` retired).*

---

## The research papers repository (Smithers)

**Repo path.** `/Users/briankuhlman/projects/smithers/` (accessed by Claude Code).

**What it is.** 721 indexed papers, flat-filed in `processed/`, with two synchronized markdown bibliographies and a SQLite cache for queries.

**Key files.**
- `References/paper_index.md`: compact metadata block per paper (citation, purpose, methodology, instruments, level of detail, topic, quality, notes).
- `References/annotated_bibliography.md`: full annotation per paper (key terms, core themes, relevance-to-book rating and synthesis paragraph).
- `scripts/references.db`: SQLite cache, rebuildable with `python3 scripts/build_index.py`. Includes a `papers` table (721 rows), `quality_ratings`, `tags`, and a `papers_fts` FTS5 full-text index over citation, notes, key terms, core themes, and topic.

**Organization.** Not folder-hierarchical. Papers are accessed via free-text topic fields and a three-tier tag system: `theory` (frameworks like big-five, allostasis, life-history-theory), `keyword` (curator keywords like neuroticism, dopamine, repeatability), and `topic` (coarse domain labels like animal-personality, personality-structure, psychometrics).

**High-density clusters worth knowing about.**
- Personality structure / Big Five: 158 papers
- Animal personality and behavioral syndromes: ~80 papers
- Comparative cognition: 39
- Personality structure (coarser tag): 38
- Psychometrics: 35
- Life history theory: 34
- Behavioral ecology: 30
- Brain evolution and evolutionary neuroscience: 29 + 23
- Allostasis and stress physiology: 26
- Intelligence and psychometrics: 23
- Cognitive neuroscience: 22
- HEXACO: 21
- Developmental plasticity: 20
- Evolutionary psychology: 19
- Personality disorders: 18
- Heuristics and biases: 17
- Attachment theory: 16
- Frequency-dependent selection: 15
- Default mode network: 14
- Gene–environment: 14
- Behavioral genetics: 13
- Social brain hypothesis: 11
- Predictive processing: 11
- Sexual selection: 10
- Dopamine and prediction error: 10

**How to use it during drafting.** When the book project needs an empirical claim grounded, a methodological detail checked, or a published finding accurately characterized, the right move is to compose a Claude Code task that retrieves and summarizes the relevant paper or paper set. For citations into the book, pull the full APA from the `papers.citation` field. The `core_themes` and `relevance` fields are the richest source for substantive integration.

**What this resource is best for.** Verifying empirical claims, checking actual published wording before paraphrasing, building paper sets for a specific theoretical question, cross-checking what multiple papers say about one construct.

**What this resource is not best for.** Conceptual orientation (NotebookLMs are better). The framework's own commitments (project files are canonical).

---

## The NotebookLM book collection

A standing NotebookLM workspace with roughly 100 books across consciousness, evolution, personality, civilization, philosophy, and applied psychology.

**Access pattern.** Brian queries the NotebookLM and pastes back results. Future-Claude does not have direct access. The right move when a book-source is needed: name the question precisely, suggest the likely-relevant book or two, and let Brian retrieve.

**What this resource is best for.** Sustained theoretical or philosophical treatment of an idea; the exact framing a specific author uses; getting an author's own articulation rather than a secondary characterization; tracking down where in a book a specific argument lives.

**What this resource is not best for.** Empirical claims (papers are better). The framework's own commitments (project files). Cross-source searches at scale.

### The book list, by rough cluster

Books are bundled into thematic clusters for navigation. Many books would fit more than one cluster; the placement here is for retrieval speed, not categorical commitment.

**Personality, individual differences, character.**
- Development of Personality (Jung)
- What Makes You the Way You Are (Nettle)
- H Factor (Ashton)
- Dark Triad (Lyons)
- Pattern Analysis of Personality Dimensions Using Artificial Intelligence
- Handbooks on Personality
- Handbooks on Psychoanalysis
- Personality in Nonhuman Animals (Kuczaj)
- Intelligence | Abilities (Cattell)
- Ungifted (Kaufman)
- Upside of Your Dark Side (Kashdan)
- Biological Psychiatry (textbook)

**Consciousness, self, mind.**
- Antonio Damasio's books (collected)
- Self Comes to Mind (Damasio)
- Strange Order of Things (Damasio)
- Master and his Emissary (McGilchrist)
- I am a Strange Loop (Hofstadter)
- Surfaces and Essences (Hofstadter)
- Consciousness and the Social Brain (Graziano)
- Origin of Consciousness in the Breakdown of the Bicameral Mind (Jaynes)
- Rise of Consciousness and the Development of Emotional Life (Lewis)
- Problem of the Soul (Flanagan)
- Mind is Flat (Chater)
- Reflective Mind (Stanovich)
- Waking, Dreaming, Being (Thompson)
- Principles of Psychology (James)

**Neuroscience, brain, emotion.**
- Brief History of Intelligence (Bennett)
- Archaeology of Mind (Panksepp)
- How Emotions are Made (Barrett)
- How the Mind Works (Pinker)
- Balanced Brain (Nord)
- Brain Energy (Palmer)
- Brain: A Short Introduction (O'Shea)
- Models of the Mind (Lindsay)
- Myth of Mirror Neurons (Hickok)
- Origin of Mind (Geary)
- Balance Within (Sternberg)
- Drive (Pink)
- Animal Intelligence (Thorndike)

**Evolution, origins, life.**
- Evolution of the Sensitive Soul (Ginsburg & Jablonka)
- Vital Question (Lane)
- Life Ascending (Lane)
- Life Unfolding (Davies)
- Symbolic Species (Deacon)
- Incomplete Nature (Deacon)
- Bacteria to Bach and Back (Dennett)
- Intuition Pumps (Dennett)
- Blind Watchmaker (Dawkins)
- Extended Phenotype (Dawkins)
- Genome (Ridley)
- Your Inner Fish (Shubin)
- Social Conquest of Earth (Wilson)
- I Contain Multitudes (Yong)
- Immense World (Yong)
- Arrival of the Fittest (Wagner)
- Phenomenon of Man (Teilhard de Chardin)
- Genius of Dogs (Hare)
- It's a Jungle In There (Rosenbaum)

**Cognitive science, judgment, decision.**
- Thinking, Fast and Slow (Kahneman)
- Language Instinct (Pinker)
- Blank Slate (Pinker)
- Intuition Pumps (Dennett) — also under evolution
- Causality (Pearl)

**Philosophy, logic, foundations.**
- Philosophical Writings of Peirce (Buchler ed.)
- Mind and Nature (Bateson)
- Steps to an Ecology of Mind (Bateson)
- Spirit of the Laws (Montesquieu)
- Revolution of the Mind (Israel)
- Muqaddimah (Ibn Khaldun)

**Civilization, history, geopolitics.**
- Political Order and Political Decay (Fukuyama)
- Collapse of Complex Societies (Tainter)
- Changing World Order (Dalio)
- Clash of Civilizations (Huntington)
- Bourgeois Equality (McCloskey)
- End of the World is Just the Beginning (Zeihan)
- Absent Superpower (Zeihan)
- Escape from Rome and Great Leveler (Scheidel)
- Homo Deus (Harari)
- Global Brain (Bloom)
- Ages of Discord and Ultrasociety (Turchin)
- Fourth Turning (Strauss and Howe)
- Generations (Twenge)
- Anchors and Sails (Stanek)
- Family Unfriendly (Carney)

**Applied psychology, motivation, character.**
- Authentic Happiness (Seligman)
- Flourish (Seligman)
- Happiness Hypothesis (Haidt)
- Drive (Pink) — also under neuroscience
- Mastery and Laws of Human Nature (Greene)
- Social Animal (Brooks)
- Start With Why (Sinek)
- Leaders Eat Last (Sinek)
- So Good They Can't Ignore You (Newport)
- Moral Tribes (Greene)
- Against Empathy (Bloom)

**Narrative and story.**
- Storytelling Animal (Gottschall)
- On the Origin of Stories (Boyd)

**Health, stress, energy.**
- Why Zebras Don't Get Ulcers (Sapolsky)
- Burn (Pontzer)
- Food Intelligence (Belluz and Hall)
- What is Health? (Sterling)

**Childhood, development, society.**
- Growing Up in Public (Heitner)
- Great Good Place (Oldenburg)
- Bullshit Jobs (Graeber)
- Unfair: The New Science of Criminal Injustice (Benforado)

**Method.**
- Psychometrics (Book 1: Blahus; Book 2: Kosinsky; Book 3: Coaley)
- Quantitative Reasoning: Dynamical (Butner)

---

## Resource-decision quick reference

When future-Claude faces a question during drafting, the routing is:

| Question type | Go to |
|---|---|
| What does the framework say about X? | Project files, starting with `Personality, Evolution, and Cybernetics.md` or `Inheritance_Lines_v3_0.md` |
| What does Bramble do at cell X? | `bramble_across_the_stack_v2_0.md` |
| What is chapter X doing structurally? | `chapter_plan_v0_5.md` |
| What is Lisa landing in chapter X? | `lisa_presentations_v0_1.md` |
| Who are the characters, what's the format? | `Book_Frame.md` |
| What does the empirical literature anchor at cell X? | The relevant `clade_reference_*` doc, then Smithers for depth |
| What does the published literature say about X? | Claude Code → Smithers repo |
| How does author Y frame Z? | Brian → NotebookLM (suggest the likely book) |
| Who else has said something close to ABHOP's claim about X? | The relevant `clade_reference_*` doc's Intellectual Kinships section; NotebookLM if a specific author's framing is needed |
| What stage of the writing process is this work? | `chapter_plan_v0_5.md` (Writing Process section) |

---

## Open questions

### Should this doc live in `/mnt/project/`

This is a meta-doc about the project's resources. It is not itself a framework artifact. Recommend it lives in `/mnt/project/` because that is the only place future-Claude reliably reads at conversation start. The alternative is that future-Claude never sees it.

### How often does this doc need updating

Project files are added and revised regularly. The book list will grow. The Smithers cluster counts will shift. Recommend a light review at version increments and when new docs are added, with a fuller refresh when the book list passes meaningful milestones (one hundred and fifty books, two hundred books).

### Cluster placement is rough

Several books would fit more than one cluster. Placement above is for retrieval speed, not theoretical commitment. If a question reaches a book under one cluster and the book turns out to live conceptually under a different one, the placement is wrong and should be moved.
