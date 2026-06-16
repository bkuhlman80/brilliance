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

**`Inheritance_Lines` line docs** The canonical label library — the exact name at every region of every cell. Each line file carries the shared architecture material (4×4 motivation matrix, row functions, row-slot view across all twelve cells with pair/triple/signature label libraries, eras and coinciding events, cell-names-as-clade-shorthand, 3D bramble visualization, and the Eronen-Bringmann / Bleidorn / Bareinboim / Ringwald four-paper literature anchor) plus that line's per-cell unified Venn tables. First place to go for canonical labels at any region of any cell.

**`lisa_presentations` line docs** Lisa's per-meeting segments across all twelve chapters, split by line (genetic = Ch 1–4, neuronal = Ch 5–8, symbolic = Ch 9–12; each line file carries the shared Section 1 vocabulary discipline and Section 3 cumulative arc). All three are now restructured to the current five-slot agenda (v0.2): under it Lisa stage-manages the meeting and, per chapter, presents tendencies (with Burns), motivations and signatures (with Marge), pitches the new knob's software (with Bart), runs the retirement-transition ritual (with Mira), and curates the Trellis-framework presentation; the framework-level retirement-transition exposition has moved to Cheryl's poetic interludes. Each line file has five per-chapter, per-segment subsections; the Trellis-block step 3 subsection carries the most-developed material and the other four hold TODO placeholders pending authorial drafting. Also useful for Lisa's vocabulary discipline (CS/biology/neuroscience native, aversive to psychology terms). First place to go for what Lisa is presenting in any given chapter.

**`cybernetics_and_sentience` doc** How to read the Venn architecture: the Port-Royal comprehension/extension gradient the diagram rides on, the four cybernetic functions (Effector, Regulator, Modeler, Reviser), and the constellations they compose — adjacent-pair feedback loops, triple syntheses, opposite-pair signatures. Grounds the geometry behind motivation, tendency, capacity, and breakthrough regions. The line-by-line diagram, label libraries, and row-slot tables live in the Inheritance_Lines line docs. First place to go for the logical structure of the Venn and the cybernetic-function definitions.

### Empirical anchors

**`clade_reference_genetic`.** Per-cell empirical reference for the four genetic-line cells (Protocell, Prokaryote, Eukaryote, Eumetazoa). Each entry gives what the cell is, the milestone breakthrough, key references from Smithers extractions with traceability flags (HIGH/MODERATE/LOW), and fun specifics. Also contains an Intellectual Kinships section with genetic-line absorptions (Darwin, Maturana & Varela, Deacon, Nick Lane) and convergences (Boltzmann/Shannon, Tinbergen, von Uexküll, Dawkins, Pollan, Ginsberg & Jablonka). First place to go for the empirical literature anchoring a genetic-line cell.

**`clade_reference_neuronal.** Per-cell empirical reference for the four neuronal-line cells (Bilaterian, Vertebrate, Mammal, Primate). Same structure as the genetic clade reference. Also contains a cross-cutting note on implicit-model vs. generative-model regulation (Stanovich tripartite mapping, niche-construction as lineage-level Regulator regulation, active inference four capabilities, empirical anchors); and an Intellectual Kinships section with neuronal-line absorptions (Friston, Bennett, Bowlby & Ainsworth, Miczek, Deci & Ryan, Koolhaas, Sih/Bell/Johnson, Barton & Dunbar, DeYoung, HEXACO, Dark Triad, HiTOP, Core Self-Evaluations, Self-Conscious Emotions) and convergences (Réale, Freud, Carl Jung general). First place to go for the empirical literature anchoring a neuronal-line cell.

**`clade_reference_symbolic`.** Per-cell empirical reference for the four symbolic-line cells (Band-Human, Settlement-Human, City-Human, Empire-Human). Same structure as the other two clade references, with the constituent-human framing explicit. Also contains an Intellectual Kinships section with symbolic-line absorptions (Harari, Social Identity cluster, Haidt, Boyd & Richerson/Henrich, Deacon *Symbolic Species*), convergences (Pinker), and a learning lineage (Cangelosi, Steels, Kirby, Taniguchi, Thelen & Adolph, the Szathmáry tie) covering language and motor acquisition and language-as-evolution. First place to go for the empirical literature anchoring a symbolic-line cell.

**`burns_deep_time` line docs** Burns' deep-time and environmental reference for the *Environment and tendencies* clade-block segment, split by line (genetic = Ch 1–4, neuronal = Ch 5–8, symbolic = Ch 9–12). Each line file carries the shared framework (Purpose, the relevant category set, Maintenance notes) plus its four per-cell environmental profiles — time period, environment of emergence, climate, plate tectonics/regional geography, atmosphere and ocean chemistry, biotic context, key fossil/archaeological sites, and signature evidentiary signal. The genetic and neuronal files use the biological-clade category set; the symbolic file uses the symbolic-line set. Environmental sibling to the clade_reference docs. First place to go for the deep-time and environmental context of a specific clade.

### Book architecture

**`Book_Frame` doc** The book's narrative-architectural commitments: the twelve-quarterly-retrospective premise, the autofiction commitment, the narrator (Cheryl), the lab (Burns/Bart/Lisa/Marge), the home (Jasmine/Ben/Mira), Mira, Bramble, the format, voice, and time. Incorporates lab-mechanics content: what the lab is, what the lab does, the team, the components-and-functions register split, quarterly meeting attendees, the three-block retrospective agenda (Clade, Bramble, Trellis) with Lisa-bookended logistics, real names, and the funder. Interludes are three-part (build log → vignette → lunch) at every between-chapter break except Interlude 0→1, which is vignette only because the Pitch is now Ch 0's closing scene; the narrator works along a graduated interpretive-distance gradient from Ch 0's opening scenes through the recurring lunches to the Ch 12 retrospective. First place to go for any question about the book's narrative frame or lab mechanics.

**`chapter_plan` line docs** Higher-level scaffold above `bramble_specs` and `Book_Frame`, split by line (genetic = Ch 1–4, neuronal = Ch 5–8, symbolic = Ch 9–12; each line file carries the full shared scaffolding sections, and the genetic-line file additionally holds the opening Ch 0, on a frame structure that folds in the former Prelude and the Pitch). Time-keeping, arc shape, per-chapter briefs, and open editorial questions. Standard time-keeping interlude rows are three-part (build log → vignette → lunch); Interlude 0→1 is vignette only, since the Pitch is now Ch 0's closing scene. First place to go for "what is this chapter doing" questions.

**`bramble_specs` doc** The consolidated cross-line spec, canonical source across four parts. **Part I (Cognitive Architecture)** owns the cognitive-software thread: the two-mind split (online mind and deep-time mind), learning located in the Modeler × Reviser coupling, the Evo-Algo as System 0, the System 0/1/2 crosswalk, the consolidation-and-sleep arc, and the cross-boundary inheritance rule (System 0 the only heritable channel). **Part II (Energy and Thermal Regulation)** owns the energy-and-thermal thread from Protocell through Primate: harvest, the two storage tanks and the Respiration Type knob, the coupled and uncoupled faces of the vortex tube, the ectotherm regime at Bilaterian and Vertebrate, and the endotherm furnace at Mammal and Primate; symbolic-line humanoid energy is out of scope and not yet specified. **Part III (The 12 Knobs)** owns the knob schema across all three lines, the retirement pacing, and the naming game. **Part IV (The Face-Screen)** owns the cognitive-readout system: the per-layer growth law, modeling-not-gating, honesty grades, FUNCTION vocabulary, and conjugation rule. First place to go for how the software, the energy economy, the knobs, or the face-screen work, both across cells and at any specific cell.

### Pedagogical scaffolds

**`marges_fallacy_arc` docs** Marge's recurring fallacy-section arc across all twelve chapters, split by line (genetic = Ch 1–4, neuronal = Ch 5–8, symbolic = Ch 9–12; each line file carries the shared "The arc", "Distribution", and "Marge's Venn" sections). Phase one (Ch 1–4): names Ghost in the Machine, Blank Slate, Noble Savage, and Dealt Hand one per chapter. Phase two (Ch 5–10): riffing without unified theory, including the first structural rhyme and the type hypothesis. Phase three (Ch 11–12): synthesis (each fallacy denies one cybernetic function; each is held by people whose shape lacks that function) and closing claim. The neuronal-line file contains the full Ch 5 Pavlov round: self-portrait mapping, scene draft, voice and beat notes per character, and chapter-level open questions. The genetic-line file contains the "Marge's Venn" section: an idiosyncratic mapping where each cybernetic function takes one MBTI label (Effector=Intuition, Regulator=Introversion, Modeler=Thinking, Reviser=Extroversion) and the four pair-syntheses take the other four (Controller=Feeling, Anticipator=Judgment, Adapter=Sensation, Explorer=Perception); the four labmates with their MBTI wobbles. First place to go for Marge's fallacy content and the Ch 5 Pavlov round.

**`rolling_bart` doc** Full drafts of the shape-shifter segments; only applies in symbolic line chapters -- Ch 9-12: Pursuer (Ch 9, five levels), Conservator (Ch 10, six levels), Planner (Ch 11, seven levels), Reactor (Ch 12, eight levels). Bart runs all four — one capacity per chapter, carried across the levels from Bilaterian up — at Trellis-block step 1 of the symbolic-line meetings. He proposed the format and presents it in an ethological, comedic register. The segments are pedagogical and comedic, with no emotional payoff: Bart presents his own shape (the Reactor) as a comedic self-portrait that doesn't model itself from outside. Each level's slide overlays the matching Simpsons cartoon face on the example (Mr. Burns = Pursuer, Marge = Conservator, Lisa = Planner, Bart Simpson = Reactor); the lab cast's real faces never appear. First place to go for shape-shifter content. 

### Handoff machinery

**`handoff_template` doc** The fill-in template for each per-chapter handoff packet between the framework project and the voice project. One filled copy per chapter+interlude unit. Defines the packet's Section A (preceding interlude), Section B (chapter), Section C (background), and Section D (empirical menu); names the markup conventions (`MANDATORY` / `VERBATIM` / `LOAD-BEARING` / `EDITABLE ORDER` / `MANDATORY ORDER`); and carries the per-segment scaffolding for retrospective and prequel chapter types. First place to go for how to compose a packet.

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
| What does Bramble do at cell X? | `bramble_specs` doc (software, energy, knobs, face-screen) plus `Inheritance_Lines_` (labels) plus the relevant `chapter_plan_` (chapter responsibility) |
| Which tendency does a clade's knob control? | `bramble_specs` doc Part III (knob to tendency label) plus `Inheritance_Lines_*` (tendency to Venn position) |
| What is chapter X doing structurally? | The relevant `chapter_plan_*` doc line file (genetic Ch 1–4, neuronal 5–8, symbolic 9–12) |
| What is Lisa landing in chapter X? | The relevant `lisa_presentations_*` doc line file |
| Who are the characters, what's the format? | `Book_Frame.md` |
| What does the empirical literature anchor at cell X? | The relevant `clade_reference_*` doc, then Smithers for depth |
| What does the published literature say about X? | Claude Code → Smithers repo |
| How does author Y frame Z? | Brian → NotebookLM (suggest the likely book) |
| Who else has said something close to ABHOP's claim about X? | The relevant `clade_reference_*` doc's Intellectual Kinships section; NotebookLM if a specific author's framing is needed |

---

## Maintenance notes

**Workspace layout (2026-05).** The line-split docs live in per-line subfolders: `theory/genetic/`, `theory/neuronal/`, and `theory/symbolic/`. Each subfolder holds that line's file for every split family — clade_reference, Inheritance_Lines, chapter_plan, lisa_presentations, marges_fallacy_arc, burns_deep_time — and each line file carries the full shared framework for its family (the genetic-line files additionally carry any genetic-only opening material, such as chapter_plan's opening Ch 0, which now folds in the former Prelude and Pitch). Docs that do not split by line stay in `theory/`: `Book_Frame.md`, and this index. One unsplit doc, `rolling_bart` doc, lives in `theory/neuronal/` rather than the root, because its shape-shifter content lands in the neuronal line. Filenames in this doc are identifiers; the line suffix (`_genetic_`/`_neuronal_`/`_symbolic_`) tells you which subfolder a split doc lives in.

**Agenda restructure (2026-05).** The quarterly-retrospective format has been restructured from the old seven-segment spine into three named content blocks — Clade, Bramble, Trellis — bookended by Lisa-run Open and Close logistics. `Book_Frame.md`, the `chapter_plan_*` doc line files, and the `lisa_presentations_*` doc line files all reflect the new agenda.

**Scene decor vs. theory (2026-05).** Seasonal mnemonic in scene structure is narrator decor, not theory.

**Location.** This doc lives in `/mnt/project/`. It is a meta-doc about the project's resources, not itself a framework artifact, but `/mnt/project/` is the only place future-Claude reliably reads at conversation start.

**Update cadence.** Light review at version increments and when new docs are added; fuller refresh when the book list passes meaningful milestones (one hundred and fifty books, two hundred books).

**Cluster placement.** Book-list cluster placement is for retrieval speed, not theoretical commitment. Several books would fit more than one cluster. Move on demand if a query reaches a book under one cluster and the book turns out to live conceptually under a different one.
