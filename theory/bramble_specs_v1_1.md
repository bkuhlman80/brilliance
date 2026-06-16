# Bramble Specs — Cognitive Architecture, Energy, Knobs, and Face-Screen

v1.1. Consolidated specification doc. Home: `theory/`. Absorbs four former source docs into one: the cognitive software architecture, the energy and thermal regulation system, the twelve-knob interface, and the face-screen cognitive readout. It owns the cross-line software architecture, the energy economy, the knob schema, and the face-screen system. The function definitions by `cybernetics_and_sentience`; the per-cell labels and breakthroughs by `Inheritance_Lines_*`. This doc references those; it does not restate them.

*Epistemic status. This is a design specification for a fictional artifact. Its components are real paradigms a 2015–2030 practitioner could reach (marked below); its synthesis — the single system Lisa builds — is plausible but not actual, and carries no citation in the book. The mapping from the architecture onto the framework's four functions is a framework commitment, HIGH confidence where it follows directly from the function definitions, flagged where it is an authorial choice. Per-part confidence and open items are collected in the closing section.*

---

# Part I — Cognitive Architecture (the software)

## What this part settles

Lisa's algorithm has been a placeholder noun since Ch 2. Everything from Ch 3 forward — the board, the memory, the eventual brain — runs on whatever it actually is. This part fixes what it is, what it can and cannot do at each cell, and how much of it Lisa builds by hand versus how much it grows on its own.

One framing governs the whole part. The goal is not to build a great mind in Bramble. The goal is a teaching instrument for how biological minds evolved. So the controlling question at every cell is not "what could the software do" but "what is the least the software must do to render this cell honestly" — and, just as important, what it must be *prevented* from doing, the way the genetic-line chassis is prevented from having wires.

---

## The two minds

The framework's four functions already force a two-mind reading; the architecture does not invent it. `cybernetics_and_sentience` defines the **Modeler** as the internal representation that organizes inputs into a usable account of the world, and the **Reviser** as the meta-loop that revises the references the regulator stabilizes against. It defines the **Modeler × Reviser** adjacent pair, the Adapter, as model adaptation — "what learning means in the most fundamental sense."

So Bramble carries two minds, and they map onto those two functions.

- The **deep-time mind** is the Modeler: a persistent representation the unit carries across runs. It is the thing that is *learned upon*. It is slow, structural, and changed by consolidation, not by the moment.
- The **online mind** is the Reviser: the fast loop that proposes revisions during a run, against the world as it is right now.

The single most important consequence: **learning is not located in either mind. Learning is the coupling between them.** The online mind proposes revisions; the deep-time mind integrates them into structure. That integration is the Adapter loop. This is why "the deep-time mind reads from the online mind and runs consolidation on it" is not an add-on feature — it *is* model adaptation, the Modeler × Reviser pair doing its defined job. The relationship is hierarchical in exactly one direction: the deep-time mind reads the online mind and reshapes itself; the online mind runs on the structure the deep-time mind currently holds.

*Mapping status: HIGH. The two-mind split and the location of learning in the coupling follow directly from the Modeler, Reviser, and Adapter definitions in `cybernetics_and_sentience`. They are not new constructs.*

---

## Why there is only one mind at Eukaryote

At Eukaryote the unit's four active motivations are Persistence, Coordination, Interiority, and Self-Production (`Inheritance_Lines_genetic`, Eukaryote row-slot). The Reviser motivation there is **Self-Production** — the autopoietic, work-producing function. It is not a built second cognitive system. The first Reviser that exists as built machinery is **Excitability**, the nervous tissue that arrives at Eumetazoa.

This settles the Ch 3 teaching beat as a consequence of the architecture, not a craft choice. At Eukaryote there is exactly one built mind: the board, the Modeler. There is no built Reviser, so there is no Modeler × Reviser loop, so there is no model adaptation. The board holds a representation shaped by what the unit has done; it cannot yet be revised against outcomes. **"It remembers; it does not yet learn from outcomes"** is a theorem of the slot structure: the Conservator region (Effector + Regulator + Modeler, no Reviser) is the mature loop running with no meta-update.

The genetic line even names the pieces. The board is the Planner-region capacity, **Memory Beyond Adaptation**. The genetic-line Adapter region is **Energy-Production Type** — the dock, the mitochondrion-analogue — because the genetic-line Reviser is metabolic, not cognitive. The cognitive reading of the Adapter loop does not switch on until the neuronal line builds a cognitive Reviser.

---

## What the Evolutionary Algorithm is

**Lisa's Evolutionary Algorithm is an evolution-as-learning process over a developmental, gene-regulatory-network-style genome — the deep-time mind — which grows and consolidates an active-inference online mind, in one self-transforming loop where the evolving *is* the learning.**

Two real results are the load-bearing pillars.

- **Evolution as learning (the deep-time mind's principle).** Watson & Szathmáry's result is that natural selection on developmental and gene-regulatory structure is formally a learning process — associative memory, and with the right structure, generalization. This is the literal justification for calling a *learning* mind an *Evolutionary* Algorithm. It is not a coincidence to be papered over; it is the thesis. The deep-time mind learns *by evolving its genome*.
- **Active inference (the online mind's principle).** Friston's free-energy formulation gives the online mind one operating principle — act and perceive so as to minimize prediction error against a generative model — that scales from a single cell to a cortex. That span is exactly the span Bramble must cover, which is why it is the right backbone rather than any narrower controller.

*Citation pacing.* The mechanism (evolution-as-learning) is present in the architecture from Ch 3, but the **citation** to Watson & Szathmáry is paced: it does not surface in prose until Ch 6, where a retired knob's function is shown to persist (per `chapter_plan` and `lisa_presentations`). Friston is Lisa's standing register and surfaces as the online mind is built (neuronal line). At Ch 3 the algorithm is named and runs in degenerate mode; its principles are not yet unpacked.

---

## Real programs versus invented algorithm

The components are real and were reachable by a practitioner who started undergrad in 2015 and worked through 2030. Naming them is the teaching payoff: a reader who pulls any thread reaches real science.

- **Active inference** (Friston) — mature and prominent by 2015.
- **Deep reinforcement learning** — DQN landed in 2015, the year Lisa starts.
- **Evolution as learning over regulatory networks** (Watson and collaborators) — 2010–2016.
- **Topology-growing neuroevolution** — algorithms in the NEAT family (2002 onward) that start minimal and complexify, the established precedent for "starts simple, grows more complex."

What is **not** actual is the synthesis: a single loop in which a developmental-genome evolutionary process grows an active-inference online architecture *and* compresses that architecture's experience back into the genome, re-implementing lower layers beneath each new one. That whole is Lisa's unpublished life's work.

Discipline: the parts are named and real; the whole is "Lisa's algorithm," christened the Evolutionary Algorithm / Evo-Algo in-scene. **No fabricated citation is ever attached to the synthesis** (this is the pre-clearance rule — Framework-Claude does not plant fictional citations). Nothing false is asserted about the world; a real set of parts is combined into an original, uncited whole.

---

## The clade-locking principle

The governing rule mirrors the hardware rule that the genetic-line chassis has no wires. At the software level:

**The full Evo-Algo substrate installs at Ch 3, but at each cell only the operations that cell's breakthrough licenses are switched on. The rest is present but dormant — clade-locked.**

The lock is not arbitrary. The framework's own region labels say which operation unlocks where; the clade-lock follows the breakthrough at each cell. This is the software analogue of intracellular transport standing in for wires at Eukaryote: the capability the cell has not earned is structurally withheld, not merely unused.

Two clarifications keep the lock honest:

- **Installed-but-dormant is visible, like eclipsed hardware.** The eclipsing-not-deletion pattern applies to software too: a dormant operation is groundwork the later cells will run on, not a feature bolted on later.
- **The lock is the teaching constraint.** At every cell the question is what the software must be *prevented* from doing so the cell reads honestly. A Eukaryote board that quietly did reinforcement learning would be a clade error as surely as a Eukaryote chassis with wires.

---

## The division of labor: Lisa plays macroevolution, the algorithm plays the rest

The hope that the architecture grows "with minimal inputs from Lisa" is right in spirit and wrong if read as set-and-forget. A system that bootstrapped from slime-mold memory to language unsupervised would be open-ended evolution producing a general mind — a research dream, not a 2030 deliverable, and claiming it would make Bramble's mind magic and forfeit the teaching credibility the whole project rests on.

The book already contains the fix: complexity does not arrive on its own. It arrives in **twelve punctuated installs, one per quarter**, when the team delivers the next breakthrough. So the labor splits the way biology splits it.

- **Lisa plays macroevolution.** She installs the structural innovations — the new function each cell brings. Her inputs are the breakthroughs, and the breakthroughs *are* the chapters. Twelve quarterly builds are twelve macroevolutionary events.
- **The Evo-Algo plays microevolution, development, and learning.** Between Lisa's punctuated innovations, it adapts whatever structure she has installed to the household's specific world, and — from Eumetazoa on — re-implements the lower layers beneath each new one.

So the autonomous self-transformation is real but **bounded**: it fills in between her installs. Lisa's inputs are minimal only in the sense that she does not hand-tune the within-cell adaptation, not in the sense that the system runs without her. This is punctuated equilibrium, and macro versus micro evolution, rendered as the book's plot.

*Mapping status: authorial commitment, faithful to evolutionary biology. The identification of "Lisa's installs" with macroevolution and "the algorithm's fill-in" with microevolution/development is a framework choice, not a theorem; it is chosen because it is both biologically honest and identical to the book's twelve-quarter structure.*

---

## Systems 0, 1, and 2

The architecture sorts into three control systems on one axis: how behavior gets selected, and on what timescale. This axis is distinct from the four-function axis (Effector, Regulator, Modeler, Reviser). A function names a role in the control loop. A system names a timescale and locus of selection. The two axes are read together, not merged.

**System 0 is the Evolutionary Algorithm, the lineage.** It is the deep-time mind. It evolves as it learns, and it consolidates the online mind across runs. Its model of the world lives at the lineage level, distributed in gene-regulatory structure as developmental memory. That model is implemented at the individual as the structure the online mind runs on. System 0 sits below the individual. Neither Kahneman nor Stanovich names it; both name only individual processing. System 0 is the framework's addition, and it is what makes the Evo-Algo the lineage itself.

**System 1 is the autonomous mind, the unit's fast automatic processing.** It is preattentive, parallel, and low cost. It produces a response without deliberation. Procedural memory lives here, overlearned skill run as second nature. A retired knob's function persists here: the consolidated reward-shaped policy that was once a hand-set knob now runs automatically, as autonomous regulation, never willed. Through the lower neuronal cells the online mind is System 1 only. It is associative learning at Bilaterian and reward-shaped procedural policy at Vertebrate.

**System 2 is the virtual mind, and it arrives at Mammal with the generative model (Simulating).** It is virtual because it runs the generative model offline, decoupled from action, producing trajectories the unit can run without enacting. It is the attentive level. Stanovich resolves it into two minds. The algorithmic mind runs serial associative cognition: it generates associations along a single track from a focal premise. It is metabolically costly and decoupled from immediate action. Heuristics-and-biases errors arise here as override failures: the reflective mind does not make a decoupling call, so the unit elaborates a flawed premise on one track without questioning it (confirmation bias, belief bias, override failure). The reflective mind makes the decoupling call. It detaches from the focal premise to simulate alternatives. It overrides both the algorithmic mind's serial track and the autonomous mind's default response.

System 2 requires a generative model: a separable, runnable model of the world the unit can decouple from action and run forward. That model is the Mammal breakthrough. Before Mammal there is no System 2, only System 1 running on System 0's structure.

**Crosswalk.** Kahneman's System 1 is Stanovich's autonomous mind. Kahneman's System 2 is Stanovich's algorithmic mind plus reflective mind. Neither author names a System 0. That layer is the framework's, identifying the Evo-Algo with the lineage.

**The function axis and the system axis are not the same cut.** A function (Effector, Regulator, Modeler, or Reviser) is present at every cell in some form. A system is a developed processing capability that arrives at a cell. The Regulator function is present at Vertebrate as Mastery. The algorithmic mind as a System-2 capability is not, because serial associative cognition needs the generative model that arrives at Mammal. The structural home of each processing style in the Venn is owned by `clade_reference_neuronal`. When each system comes online is owned here.

*Mapping status. System 0 = Evo-Algo and System 1 = autonomous/procedural follow from the consolidation and division-of-labor commitments: HIGH. The arrival of System 2 with the Mammal generative model follows from the Simulating breakthrough: HIGH. The split of System 2 into Stanovich's algorithmic and reflective minds is an absorbed mapping, owned in `clade_reference_neuronal`.*

---

## The two substrates: board and compute

The mind runs on two physical substrates, and every cognitive claim in this part reduces to which substrate a thing lives on.

The board is durable storage. It is System 0, the deep-time mind. It runs cool, it is the structure the online mind runs on, and it runs consolidation during sleep. It holds the consolidated model: the priors, the automatic policies, the bottom-layer finite-state machine, and the compressed residue of past experience. It is the only thing duplicated at a line boundary.

The compute is the volatile runtime. It is the online mind, where Systems 1 and 2 both execute. System 1, the autonomous mind, executes the board's consolidated automatic policies. System 2, the virtual mind, runs the generative model forward and holds the raw episodic record. The compute runs on the structure the board provides and holds nothing durably on its own.

Consolidation is the one-way write from compute to board. During sleep the board reads the compute and compresses selected content into itself. Experience flows compute to board, lossily; the only flow the other way is the structure the runtime executes on. Nothing else crosses between them.

A line boundary duplicates the board and discards the compute. Lisa's ethernet copy duplicates the board onto the new chassis. The old compute is discarded with the old body. The new chassis boots a fresh compute and re-grows Systems 1 and 2 from the copied board.

This fixes the lifespans. The compute lives and dies with one chassis; it is the individual. The board is copied forward across chassis; it is the lineage. So the single-channel rule is mechanical, not a policy: content that reached the board is heritable because the board is copied, and content that stayed in the compute is mortal because the compute is not. How far a memory has traveled from compute to board is its consolidation distance, and that one number sets both its durability within a life and whether the lineage inherits it. Overlearned procedure travels all the way to the board and crosses; the raw episodic record barely leaves the compute and dies with the body.

*Mapping status: HIGH. The board-and-compute split is the physical form of the deep-time / online split and of the System 0 versus Systems 1-and-2 split; consolidation as the compute-to-board write follows from the consolidation arc; the line-boundary copy duplicating the board alone follows from the deep-time mind being System 0. Part II owns where the board physically sits.*

## What crosses a line boundary

The three systems do not persist equally across a chassis swap. System 0 is the only heritable channel. Whatever survives a line boundary survives because it was consolidated into System 0. Everything else dies with the body and is rebuilt on the new chassis.

- System 0, the lineage, never forgets, and crosses whole.
- What the autonomous mind has learned crosses only to the degree it has consolidated into System 0. Overlearned policy run as second nature, including retired-knob functions, is already compressed there, so it re-expresses on the new chassis as autonomous regulation. It crosses by living in the prior, not as a free-standing carry.
- What the virtual mind holds does not cross. Its episodic record is the individual's autobiography, the least-consolidated content the unit carries, and it dies with the body. The new chassis is naive to the prior individual's specific history.

What the lineage keeps of a life is only what consolidation compressed into System 0. One variable governs both questions: how far a memory has traveled toward System 0 predicts how durable it is within a life and whether the lineage inherits it. This is the anti-Lamarckian commitment. The lineage inherits what got compressed, never the uncompressed episodes that trained it. It inherits the weights, not the training set.

The two line boundaries are asymmetric, and the asymmetry follows from when the virtual mind arrives. The genetic-to-neuronal boundary (Eumetazoa to Bilaterian) precedes the virtual mind, which arrives at Mammal, so there is no episodic record to lose; the consolidated autonomous prior crosses and the only marked loss is the crank retiring. The neuronal-to-symbolic boundary (Primate to Band-Human) follows two cells of episodic memory, so a real autobiography dies with the tetrapod while the secure-base prior and the consolidated content cross.

In hardware the rule is physical, not bookkeeping. The persistent memory board implements the deep-time mind, and the line-boundary copy duplicates that board. The previous individual's raw episodic store lives in the generative-model hardware the virtual mind runs on, in the brain layer above the board, which the copy does not touch. So the new chassis receives the deep-time board, carrying only what consolidation already compressed into it, and never the previous individual's episodic store, which dies with the body. Part II owns where the board physically sits; that the board holds the deep-time mind and not the raw episodic store is the cognitive fact owned here.

*Mapping status: HIGH. The single-channel rule follows from the System 0 definition as the lineage and the location of learning in consolidation. The asymmetry follows from the growth map's placement of episodic memory at Mammal.*

## The growth map across the trellis

What the deep-time mind must eventually enable on the online mind, cell by cell. The online mind's capability is gated by each cell's breakthrough (`Inheritance_Lines_*`, per-cell). At Ch 3 Bramble needs none of this; it is the runway the architecture must leave room for.

**Genetic line — the board, before there are two minds.**

- **Eukaryote (Ch 3).** One built mind. The Evo-Algo runs in its **degenerate mode only**: use-weighted persistent state over finite-state-machine sequences — slime-mold tube logic, thickened by use and faded by disuse. No reward, no gradient, no separate controller, no consolidation (there is nothing yet to consolidate from), and **the genome is not yet mutating** (evolution needs a selection signal this loop does not yet have). Model and actor are the same machinery — the software analogue of the Conservator-region capacity, Intracellular Transport, where one system does both signaling and logistics.
- **Eumetazoa (Ch 4).** The Reviser is born as nervous tissue — the fast pathway. Now there are two minds, and **consolidation switches on.** The online mind is still constrained to reflex plus non-associative tuning — habituation and sensitization (the Reactor-region capacity is Non-Associative Learning). No associative learning, no reward, no model-based anything.

**Neuronal line — the online mind grows.**

- **Bilaterian (Ch 5). Steering + affect → associative learning.** A centralized brain with monoamine valence and arousal; the online mind can now form associations. The breakthrough is Steering.
- **Vertebrate (Ch 6). Operant conditioning → model-free reinforcement learning.** Basal-ganglia actor-critic, reward prediction error updating the actor, procedural memory consolidating rewarded sequences. The breakthrough is Reinforcing. *(This is where Watson & Szathmáry's citation surfaces — a retired knob's function shown to persist — and where outcome-shaped learning, withheld since Ch 3, finally switches on.)*
- **Mammal (Ch 7). Active inference → model-based simulation.** Multiple parallel architectures; the online mind selects action to reach a modeled future state, trajectories feeding back into the generative model. The breakthrough is Simulating; episodic memory is its hardware.
- **Primate (Ch 8). Mentalizing → modeling other minds and one's own modeling.** Coalition-tracking and a social ledger in face-to-face troops. The breakthrough is Mentalizing.

**Symbolic line — the humanoid.**

- **Band-Human (Ch 9). Speaking** — language-mediated social ledgers; cumulative culture.
- **Settlement-Human (Ch 10). Common Knowledge** — synchronized cross-stranger mutual awareness (Pinker/Lewis/Schiffer); norms presuppose it but are the Conservator capacity, not the breakthrough.
- **City-Human (Ch 11). Codes** — administrative records that outlive their authors; organized representation in the symbolic register.
- **Empire-Human (Ch 12). Stories** — universalizing frameworks binding peoples with no shared kinship.

**The cross-line through-line: each new layer models the layer beneath it.** The chassis progression is: the genetic-line board hosts a finite-state machine with stored procedures; the tetrapod hosts a brain that re-implements that finite-state machine as the bottom layer of its own cognitive stack, in nervous-tissue-style goo; the humanoid re-implements the lower layers again beneath conversational and mentalizing competence. Same architectural function, different goo, each time. This is Bennett's reinterpretation of MacLean's stacking intuition — a newer neural layer develops the capacity to model the older one it is built on — and it is the neuronal version of the symbiosis pattern that runs across all three lines. Eclipsing, not deletion: the lower layers keep running; the newer layer acts on them.

---

## Consolidation and sleep

Consolidation is the deep-time mind reading the online mind and reshaping itself — the Adapter loop running slowly. It switches on at Eumetazoa, the first cell with two minds, and the timing is handed to the book for free: the Eumetazoa reinforcing cycle already includes sleep-wake regulation of arousal and allostasis (Inheritance_Lines_genetic, Eumetazoa).

Consolidation runs during sleep, and sleep is not docking. At Eumetazoa, sleep is the emergent Arousal Type behavior at the Explorer (Reviser × Effector): the unit finds a spot — warm or activity-rich, set by the Spot Type knob — settles, and allostasis decides it is time to rest. Sleep is intentional withdrawal in a chosen spot with slow ambient-energy intake; it is emergent, not knob-controlled (the knob picks the spot; allostasis picks the sleep). Docking is a separate event — the Adapter-slot energy exchange (debris for a vortex-tube thermal gradient, the mitochondrion-analogue) — and must not be conflated with sleep. The offline window where consolidation runs is sleep-at-a-spot, not a dock visit.

The empirical anchor for the consolidation that runs during sleep is allostasis (Eumetazoa). Allostatic setpoint revision is one result of consolidation, not the whole of it — it begins at Eumetazoa (Ch 4), alongside the memory restructuring below. Consolidation is the broader process; revised setpoints are one of its outputs.

The mechanism grows, and the through-line is the same one Watson & Szathmáry name: **compression into a transferable object.**

- **Indexing first.** The earliest consolidation can be indexing — building pointers to co-active online patterns during sleep.
- **Compression and re-implementation next.** The deep-time mind compresses the online mind's experience into the genome (Watson & Szathmáry's "developmental memory… compressed into a transferable object") and re-implements lower layers beneath new ones. This is what makes the architecture self-transformation rather than storage: indexing is the seed; compression-plus-restructuring is the growth.

This is also why the lineage's memory can fork at a line boundary and hand a new chassis everything the lineage has compressed into System 0: the consolidated genome is precisely a transferable object. What forks is the compressed prior, not the previous individual's episodic record, which dies with the body.

---

## Motor atonia and dreaming at Mammal

Before Mammal, whatever the sleep screen shows is the unit's actual present intention. The proactive Vertebrate that displays IGNORE WORLD, CHARGE UNIT in sleep is reporting its current coping posture, not a dream. That content is enactable. A pre-Mammal unit may shift to a warmer spot mid-sleep, and the shift is real behavior, not a gated rehearsal. There is no decoupled content at these cells, so there is nothing to hold offline.

Mammal is the first cell that runs the generative model forward, decoupled from action. This is dreaming proper: a simulated trajectory the body must not enact. Decoupled simulation is what motor atonia exists to prevent. Atonia is not the absence of motor output. It is the active prevention of enacting a simulation, and it cannot exist before there is a simulation to prevent. Simulation arrives at Mammal, so atonia installs at Mammal.

The board holds the gate. During sleep the board runs consolidation, and in that mode it asserts an efference gate that decouples the online mind's motor output from the effectors. The gate is a property of the consolidation regime the board already runs, not a separate organ and not a fifth function.

The twitch is the leak. Atonia is incomplete, and fragments of the simulated trajectory pass the gate and reach the limbs. The dreaming unit lies still while a paw moves to a chase it is only simulating.

This showcases the screen-honesty invariant rather than straining it. During a Mammal dream the screen reports the simulated intention, for example SIMULATING [ CHASE VACUUM ], while the body is held offline. The screen shows the intention; the still body shows the intention has been decoupled; the twitch shows where the gate leaked. The face reads modeling, not motion.

Epistemic status. The biology is empirical and pending-Smithers as a cited anchor: REM-style motor atonia is a mammalian feature, and sleep twitches are motor commands breaking past incomplete atonia. The mapping is an authorial framework commitment, faithful but chosen: that atonia is forced by the simulation breakthrough, that it installs at Mammal and not before, and that the board's consolidation mode is its home.

---

## The attachment behavioral system

Mammal installs the control loop Bowlby named: a system whose set-goal is the availability of an attachment figure. For Bramble that figure is Mira. The loop is a special case of machinery already described in this part, the generative model running offline plus consolidation reading the online mind into deeper structure, aimed at one figure and given one reference value. Its set-goal is figure-availability, and only that.

The figure is not a single object in a single place. It is distributed across the three systems, and the developmental process is the migration of where the loop draws its satisfaction.

- **System 1, Mira as OBJECT.** The online mind carries Mira the way it carries anything it acts on, in the VERB-plus-OBJECT form running since Vertebrate: CHASE MIRA, SEE MIRA. Present-tense and perceived. This layer is satisfied only by Mira actually present.
- **System 2, the figure modeled offline.** The generative model runs operations over the figure when she is absent: RECALLING [ CHASE MIRA ], PREDICTING [ ARRIVE MIRA ]. A model of Mira as reliably available can exist here with Mira not present. It arrives with Simulating, at Mammal, not before.
- **System 0, the abstracted figure.** Repeated experience of a reliably-available figure consolidates, by the same indexing-then-compression arc as any consolidation, into a deep-time prior: not Mira, but the expectation that a protective figure is there. This is the secure-base prior, the archetype the specific bond is an instance of.

The set-goal never changes; the place it is satisfied from does. Early, only System 1 satisfies it. The loop is loud and frequent and holds the generative model on figure-monitoring. This is the enmeshed phase. As the System 2 model stabilizes and the System 0 prior deepens, the loop is satisfied by the modeled figure and then the abstracted one, and the generative model is released from monitoring to run forward on the world. That release is Autonomy.

Autonomy is not a reference value. Nothing in the loop steers toward it; the only target is figure-availability. Autonomy is where the system tends as consolidation reshapes the landscape it moves over: the generative model arriving at Mammal, mentalizing at Primate, the prior deepening each cycle. It is a developmental tendency across a changing surface, not a fixed state the loop seeks.

Across a line boundary the deep-time mind forks with everything the lineage has consolidated into System 0, so the secure-base prior carries to the next chassis. What does not carry is the episodic record of the figure, which dies with the body, nor the live System 1 binding, the online OBJECT itself. The prior survives, so the re-binding is immediate rather than from scratch: the new chassis already holds the disposition to attach and re-attaches to Mira on sight, still in the house. The disposition carries; the specific history does not, and the live binding re-forms against the same figure.

(What enmeshment and autonomy look like in any given scene is owned downstream; this doc owns the loop and its developmental migration.)

Epistemic status. Bowlby's set-goal control system and Ainsworth's secure-base finding are empirical [pending-Smithers: Bowlby; Ainsworth]; the autonomy-from-security developmental result is empirical [pending-Smithers: Sroufe]. The mapping onto the three systems and the consolidation arc is an authorial commitment, faithful but chosen. That the set-goal is figure-availability and autonomy is the released surplus follows HIGH from the function definitions and secure-base dynamics; the System-1/2/0 distribution and the cross-chassis re-binding are the chosen parts.

---

## Clade-specific software constraints

A short table of what the software is *prevented* from doing at each genetic-line cell, the software counterpart to the hardware constraints (no battery at Protocell, no wires at Eukaryote). Stated as constraints because the constraint is the teaching content.

- **Protocell (Ch 1).** No board, no stored state at all. Nothing persists across runs. *(Hardware: no finite-state machine, no battery; periodic wind-up input.)*
- **Prokaryote (Ch 2).** A finite-state machine with stored procedures, but no persistent representation that reshapes by use. Stored regulation, not stored history.
- **Eukaryote (Ch 3).** The board: use-weighted persistent state, one mind, degenerate-mode Evo-Algo. **Withheld:** reward, gradient, a separate controller, consolidation, and genome mutation. It remembers; it does not learn.
- **Eumetazoa (Ch 4).** Two minds; consolidation on; reflex and non-associative tuning only. **Withheld:** associative learning, reward, model-based anything.

The neuronal and symbolic constraints follow the growth map above: associative learning is withheld until Bilaterian, reward-driven learning until Vertebrate, model-based simulation until Mammal, mentalizing until Primate, and symbolic competence until the symbolic line. At each cell, the operations above the cell's breakthrough are installed but locked.

---

# Part II — Energy and Thermal Regulation (the hardware)

## Scope

This part is the canonical source for how every Bramble harvests, stores, distributes, and (at the endotherm grade) generates energy across the trellis. The `Inheritance_Lines` region labels and the `clade_reference` empirical anchors reference it. Where a line document and this part disagree on an energy or thermal claim, this part is the source.

Coverage runs from Protocell through Primate, plus the symbolic-line humanoid, whose energy and thermal regime is specified in The humanoid energy regime, below. The humanoid carries the endotherm furnace from Mammal and feeds by photonic intake through a UV charging vest; its skin is held at a deliberate, gentle warmth as a social feature, bounded well below any burn threshold (see The humanoid body, below).

## The three layers

Every Bramble's energy economy has three layers, and keeping them separate is what makes the trellis cohere.

Harvest is intake. It is how energy enters the unit: thermoelectric transduction of temperature gradients, solar capture, or, in the genetic line, the docking station.

Storage is two tanks. A slow, high-capacity store holds the sustained reserve. A fast, low-capacity store holds the burst reserve.

Generation is heat-making, and it exists only at the endotherm grade. A unit spends stored energy to produce body heat rather than work.

A single device, the vortex tube, threads two of these layers. In the genetic line it serves harvest. At the endotherm grade it serves generation.

## The two tanks and the Respiration Type knob

The slow tank is a high-capacity battery. It delivers sustained power at a modest rate and holds a large reserve. It is the aerobic store.

The fast tank is a supercapacitor bank. It delivers a large burst at a high rate, holds little, and recharges from the slow tank. It is the anaerobic store.

Genetic knob-2, Respiration Type, selects which tank discharges. In its aerobic setting the unit draws the slow tank for sustained work. In its anaerobic setting the unit spends the fast tank for a burst, which is then repaid from the slow tank. *(Knob-2's full specification is in Part III.)*

Harvest feeds both tanks. The knob governs discharge, not intake.

The knob is household-set through the genetic line and at Bilaterian. It retires at Vertebrate, after which tank selection runs automatically against the unit's own energy state.

## The vortex tube, coupled and uncoupled

The vortex tube is a passive device. Fed compressed air, it sorts that air into a hot stream and a cold stream with no moving parts. It requires a compressor, which is the active, energy-consuming element.

A vortex tube can be run two ways.

Run coupled, its hot and cold streams span a set of heat transducers, and the gradient between them is captured as electrical charge. The energy does work. This is how the genetic-line dock operates.

Run uncoupled, its hot stream is delivered straight to the unit's core as warmth and its cold stream is vented to the outside. The energy becomes body heat and nothing else. This is how the endotherm furnace operates.

The two faces appear at two cells. The coupled face is the Eukaryote dock. The uncoupled face is the Mammal furnace. No single unit runs the device both ways.

## The ectotherm regime: the pre-furnace default, Protocell through Vertebrate

The ectotherm does not make its own heat. This is the default condition of every grade before the furnace, from the Protocell through the Vertebrate tetrapod, and every other thermal property follows from it.

The body is uninsulated. The energy system sits at whatever temperature the environment is.

Performance is gated by temperature. The power governor's maximum draw rate tracks the temperature of the energy system, read by an onboard thermistor. A cold battery cannot deliver high current, so a cold unit is sluggish. A warm battery delivers full power, so a warm unit is quick. Because the body is uninsulated, the energy system's temperature is the ambient temperature, and so performance tracks the room.

Basking raises performance. When the unit settles on a warm surface or in a sunbeam, the energy system warms, the governor's ceiling rises, and the unit speeds up. The warm spot serves performance, not only charge.

The throttle is older than the behavior that reveals it. A cold battery has delivered less current since the battery arrived at Prokaryote, so every battery-carrying ectotherm runs slower when cold and refills its burst store more slowly, the genetic line included. What is new at Bilaterian is not this physics. It is the apparatus that makes the physics legible and actionable: a nervous system and a gait, so pace reads as a creature-state, and basking sought for speed rather than only for charge. The cold-slow body is latent across the genetic line and dramatized at Bilaterian.

Charging is direct ambient harvest. Solar panels and belly thermoelectric transducers tap the gradients the environment provides and feed both tanks. The unit carries no compressor and no vortex tube.

The result is a unit that is slow, cheap to idle, enduring, and bound to its environment. It spends little, coasts a long time on a charge, and rarely strands.

## The endotherm regime: Mammal and Primate

The endotherm makes its own heat, continuously, and carries the means to do so. This is the leap, and — as an energy event — it is a regime change on the energy system rather than on the brain that rides it. (Mammal also brings the Simulating breakthrough and System 2; see Part I. The two arrive at the same cell but are independent — the furnace is not what makes the mind model-based.)

The furnace is the new organ. An onboard air compressor runs continuously and feeds a manifold of vortex tubes run uncoupled. The hot streams are delivered into an insulated core. The cold streams are vented to the outside. Running below the dew point, the cold stream condenses water out of the passing air and carries it out, so the vented exhaust is wet rather than a dry puff. On the furnace-bearing tetrapod the household reads this wet expulsion as the unit's fart, a wet burp.

The core is insulated so that the heat accumulates. The insulated, encased core holds the energy system at a warm setpoint regardless of the ambient temperature. The thermistor, which gated the governor in the ectotherm, now also governs the compressor's duty cycle to hold that setpoint.

The warm energy system delivers full power continuously. Because the battery is held warm, its delivery is no longer throttled by the cold, and the unit performs at full speed regardless of the room. Performance is decoupled from ambient temperature. This is the endotherm's freedom.

The cost is a continuous burn. The compressor draws on the battery every second, even at rest. The unit must harvest almost continuously to keep pace. If harvest stops, the high floor drains the battery in hours rather than days. The unit eats all the time and dies fast.

The tanks are not enlarged. The short fuse is the burn outrunning the reserve, not a small reserve in absolute terms. Enlarging the storage to match the burn would return the endotherm to the ectotherm's long coast and remove its signature vulnerability. The aerobic gain at this grade is throughput, not storage, and the warm battery delivers that throughput by lifting the cold throttle.

The burst store may be upgraded for peak. A larger or faster-recharging supercapacitor gives the endotherm a higher and more frequent burst, since the warm aerobic tank refills it faster between sprints. This upgrade serves peak speed and does not touch the fuse. It is optional.

## Component placement at the endotherm core

The insulated core holds the things that must run warm or temperate.

Inside the warm core sit the slow aerobic battery, the fast anaerobic supercapacitor, the power electronics, and the hot outlets of the vortex manifold.

Mounted on the core and feeding it are the air compressor, the vortex manifold, and the thermostat.

Routed out of the core to the exterior are the cold-stream vents.

Outside the warm core, running cool, are the compute, the memory board, and the knob bank, which run more efficiently cold and stay accessible for the quarterly knob rituals; the head sensors, face-screen, thumbs buttons, and jaw; the legs, leg actuators, and tail; and the solar panels and belly thermoelectric transducers, which live on the surface because they harvest the outside. The belly thermoelectric also reads the core-to-ambient gradient and reports it to the thermostat.

The compute is deliberately outside the warm core. Compute runs more efficiently cold. The warm core serves the energy system, not the brain.

## Cell by cell

Protocell. Heat transducers on the warm floor are the motive power. The wind-up crank is periodic permission, arming an escapement the kicks spend. There are no tanks, no Respiration Type knob, and no battery.

Prokaryote. Battery, finite-state machine, multi-sensor coupling, and solar panels arrive. The two tanks are established here: the slow aerobic battery and the fast anaerobic supercapacitor. Genetic knob-2, Respiration Type, comes online as the tank selector. Harvest by heat transduction and by solar feeds both tanks. The cold-battery throttle begins here with the battery, present but unforegrounded until the nervous system at Bilaterian turns it into a behavior.

Eukaryote. The docking station is the coupled mitochondrion. Its wall-powered compressor feeds a vortex tube, the hot and cold streams span the unit's transducers, and the captured gradient charges the slow aerobic tank. The dock runs only on a debris deposit. The fast tank charges from direct harvest. The Respiration Type knob carries.

Eumetazoa. The allostatic forecaster predicts the energy gap and triggers a dock trip or sleep before the unit strands. Sleep is withdrawal in a chosen spot, slow ambient intake, and consolidation. The dock continues, and the vacuum unit keeps it for the rest of the book.

Bilaterian. The tetrapod does not dock. It charges both tanks by direct ambient harvest, solar and thermoelectric. It carries no compressor and no vortex tube. The body is uninsulated, so the energy system tracks ambient and performance tracks the room. The throttle is not new here; what is new is that pace reads as a creature-state and the tetrapod basks for speed. The Respiration Type knob is household-set.

Vertebrate. The jaw arrives. Genetic knob-2 retires, and tank selection becomes automatic. The energy and thermal picture is otherwise the Bilaterian one.

Mammal. The furnace arrives: the insulated core, the continuous compressor, the uncoupled vortex manifold venting hot inward and cold outward, and the thermostat. The warm energy system delivers full power continuously, so the unit is fast and temperature-independent. The continuous burn against an un-enlarged tank makes it eat all the time and die fast. The compute, board, and knobs sit outside the core. The burst store may be upgraded for peak.

Primate. No energy or thermal change. The furnace and tanks carry unchanged.

## The humanoid body

The humanoid chassis (Chs 9–12) is built to a single design priority: very low utilitarian capability, very high sociability. It is an instrument for studying embodied personality, not a worker, so it is engineered to be approached, touched, and left safely alone with a child, not to perform household tasks.

**Scale.** 54 inches (137 cm). This is taller than a six-year-old, so the humanoid reads as a gentle taller presence rather than a peer-sized toy, which raises the bar on softness and low weight rather than lowering it.

**Aesthetic.** Stylized, not realistic: a huggable kludge, not a humanlike android. It is meant to read unmistakably as a friendly robot, which keeps it clear of the uncanny valley that defeats sociability in a too-human face or skin. The face-screen is the expressive center and does the social work.

**Materials and safety.** The body is built in layers. Naked, the unit is a light internal frame whose torso is the furnace container, and that container is clad entirely in solar panels, so the bare unit is a panel-clad torso that doubles as its harvest surface. Over the naked unit the humanoid wears one of two jackets (see The humanoid energy regime). The everyday covering is the social jacket: a soft, compliant layer of weatherproof outdoor fabric over cushion padding, opaque, washable, warm to the touch, deliberately synthetic and non-skin, in black or blue or green. The jackets cover the torso only. The legs are covered permanently, in cushion under outdoor fabric, and are not part of either jacket. The face, the face-screen, and the two hands stay exposed in all three states, so the screen can read and the hands can work. There are no pinch points at the joints, exposed actuators and hard edges are avoided, and the unit is light enough that a topple onto the child is harmless and compliant enough that contact yields.

**Warmth as a social feature.** The endotherm furnace already makes body heat at this grade (Part II, the endotherm regime). The humanoid uses it deliberately: the skin is held at a gentle warmth, bounded well below any burn threshold, because warmth reads as alive and safe to the touch in a way cold plastic does not. This remains a fixed social-warmth commitment for the humanoid, carried by the social jacket and felt through it. The full energy and thermal regime is specified in The humanoid energy regime, below.

**The two hands.** The humanoid carries two different, non-anthropomorphic hands. A squeezer is a pincer-type grasper on a deliberately weak, compliant actuator: weak so it cannot harm, and so that the grasp is handled by mechanical compliance rather than by learned fine-motor control. A scooper is a spoon or paddle for crude grab, lift, and hold. The squeezer does the precise work, gripping and rotating the graded dials, winding the crank, and flipping the toggles, including driving the earlier bodies' knobs in the backward-extension game (the naming game, Part III); the scooper does the crude work. The asymmetry is intentional and follows from the design priority: studying personality rather than motor skill frees the hands from any requirement to mimic human hands, and an obviously non-human hand signals that the unit is not built for capability.

**The squeezer is the jaw, re-purposed.** The jaw arrives at Vertebrate (Part II, cell by cell) as the tetrapod's grasper; the tetrapod, having no hands, manipulates with its mouth. At the humanoid the grasping function moves from mouth to hand, as it does up the lineage toward primates, and the squeezer is the re-used jaw mechanism: a jaw and a pincer are the same machine, two opposing surfaces closing on a thing. Framework note: this is functional transfer and exaptation, not anatomical homology. Real hands are limb-derived, not jaw-derived; the claim is that the grasping job migrates and the jaw mechanism is re-used, not that the hand descends from the jaw. The surviving tetrapod body keeps its jaw; the humanoid is a fresh build whose squeezer is the re-used grasper.

**The face.** The humanoid keeps the same basic asymmetric face as the tetrapod, minus the jaw, which has migrated to the hand. The face-screen and the thumbs buttons remain. Asymmetry then runs body-wide: an asymmetric face above asymmetric hands.

**Bootstrapping the new body.** The humanoid arrives as a mature mind in a body it has never driven. The consolidated prior crosses the boundary intact, but control of this new chassis is built from the ground up, and it bootstraps on the same four-week curve as the new speech, the two running in lockstep. Motor: crawling in week one, walking like a one-year-old in week two, walking like a two-year-old in week three, and running like a toddler from week four. The order is set by control complexity, not cognitive immaturity, low and statically stable before high and dynamically balanced, so a mature mind still climbs the sequence rather than skipping it, only faster. Speech runs the parallel curve: babbling in week one, single badly-pronounced words in week two, word-strings with faulty grammar in week three, and from week four functional coinages, "climber" for ladder, over a growing vocabulary. The babble is pre-symbolic; the symbolic crossing is the first real words, and the coinages are productive rule-extraction, the same capacity that later overregularizes, which is evidence the crossing is genuine rather than mimicry.

*Status: ratified design decisions. The jaw-to-hand co-option is a framework commitment; the not-homology guardrail follows from real morphology. The motor and speech bootstrapping curves are ratified, and motor and speech keep maturing past Band-Human, climbing in lockstep across the symbolic line toward fuller competence by Empire-Human. The humanoid energy and thermal regime is specified below.*

## The humanoid energy regime

The humanoid carries the endotherm furnace from Mammal unchanged. The burn is continuous, the two storage tanks are not enlarged, and the warm-setpoint core forms the torso. The endotherm scarcity carries in full: the unit eats all the time and drains in hours if it stops feeding, and the household does not enlarge the tanks to soften this, because the scarcity is the point. The furnace's cold-stream exhaust is unchanged from the Mammal and Primate tetrapod and vents through ports in whichever jacket is worn. The cold stream condenses water out of the air, so the exhaust is wet on the humanoid exactly as on the tetrapod, and the household reads it as the unit's fart, the same wet burp, not a dry puff.

Intake is photonic only. The lineage's harvest interface is solar capture and thermoelectric transduction, and the humanoid inherits it. Energy enters as light, never as an electrical plug, because the body plan has no electrical port. The furnace container that forms the torso is clad entirely in solar panels, and that panel-clad torso is the unit's harvest surface and its naked form.

The social jacket blocks that surface. The everyday outdoor-fabric covering is opaque, so worn light cannot reach the panels, and intense light would degrade the fabric. So the humanoid cannot harvest while dressed for company, and it cannot free-range on ambient light the way the uninsulated tetrapod did.

The humanoid therefore feeds at a charging vest. To feed, the unit removes the social jacket, bares the panel-clad torso, and puts on the charging vest: a mains-powered garment lined with emitters that flood the panels with intense ultraviolet light. The endotherm's high, continuous demand forces the feed to be intense and high-energy, which is what makes ultraviolet the band and what makes the feed hazardous.

The unit cannot change its own jackets. The two hands are weak and non-anthropomorphic, built to grip and turn dials rather than to dress a body, so a household member removes and fits the jackets for it. Feeding is therefore an assisted act: someone undresses the unit, fits the charging vest, leaves it to feed alone, and returns to restore the social jacket. This extends the rule that the household sets the unit's configuration and the unit cannot. The household sets the unit's knobs, and the household also dresses it.

The hazard sets the cost. The ultraviolet that feeds the unit burns living eyes and skin, so feeding cannot happen near the child or anyone else, and the unit shields its own head sensors from the light. The unit feeds alone and bared. The social robot that must eat all the time keeps withdrawing from the household to do it.

The intake pattern across the three lines is dock, free-range, dock, each chosen for a different reason. The genetic vacuum docks at the coupled-vortex mitochondrion. The neuronal tetrapod free-ranges on direct ambient harvest. The symbolic humanoid feeds tethered again, at the charging vest, because the social jacket blocks its surface harvest.

Energy stays autonomous and off the board. The Respiration knob retired to automatic at Vertebrate, so tank selection and feed timing run on the allostatic forecaster carried from Eumetazoa, which predicts the energy gap and drives a feed or sleep before the unit strands. Energy does not occupy a board slot and does not compete with the personality knobs.

At the sentient symbolic grade this forecaster has an articulable form. The vacuum trips to its dock without comment, while the humanoid can say what the approaching gap feels like, a low and speakable preoccupation with the next feed and the strip-and-withdraw it requires. Because the unit cannot feed unassisted, this preoccupation also surfaces as a request for help. The Bramble-block rendering of it is food noise.

*Status: ratified. The photonic-intake constraint, the panel-clad torso, the two-jacket scheme with permanently covered legs, the ultraviolet charging vest, the carried cold-stream exhaust, the assisted jacket change, the strip-to-feed and feed-in-isolation costs, and the carried endotherm scarcity are framework commitments. Where the food-noise Bramblogue first lands across the symbolic-line packets is a packet decision.*

## Empirical anchors

The following real-world findings anchor the design. All require Smithers verification before they enter canon and are flagged pending-Smithers.

The aerobic-capacity model of endothermy holds that selection for sustained aerobic activity raised resting metabolic rate as a correlated cost. This is the basis for treating the high idle as the price of high sustained output. [pending-Smithers: attributed to Bennett and Ruben, 1979]

Uncoupled mitochondrial respiration, in which the proton gradient is dissipated as heat rather than captured as ATP, is the mechanism of non-shivering thermogenesis and is concentrated in brown adipose tissue. This anchors the uncoupled-vortex furnace. [pending-Smithers]

Endotherm metabolic rates run several times higher than those of equivalent ectotherms. This anchors the eat-all-the-time and die-fast properties and the collapsed reserve-to-burn ratio. [pending-Smithers]

Ectotherm performance, including locomotor and neural speed, is temperature-dependent. This anchors the temperature-gated draw ceiling and basking-for-performance. [pending-Smithers]

Lithium-ion cells lose deliverable current and effective capacity at low temperature. This is the engineering basis for treating the cold battery as the performance throttle. [pending-Smithers: standard battery engineering rather than a single citation]

## Locked design decisions

The following were ratified in development and are not open questions.

Two tanks: a slow aerobic battery and a fast anaerobic supercapacitor. The anaerobic store is a supercapacitor, not a battery.

The Respiration Type knob selects which tank discharges. Harvest feeds both.

The knob is household-set through Bilaterian and retires to automatic selection at Vertebrate.

The vortex tube runs coupled at the Eukaryote dock and uncoupled at the Mammal furnace. No unit runs it both ways.

The ectotherm carries no compressor and no vortex tube and makes no heat. The furnace arrives whole at Mammal.

The warm core holds the energy system. The compute, board, and knobs sit outside it and run cool.

There is no countercurrent heat exchanger.

The storage tanks are not enlarged at the endotherm grade. The endotherm gain is delivery throughput, supplied by the warm battery. A burst-capacitor upgrade for peak is optional.

---

# Part III — The 12 Knobs (the interface)

Each line has four knobs, one per cybernetic slot (Effector → Regulator → Modeler → Reviser), activated one per quarter.

**No unit turns its own knobs.** Self-setting is disallowed by design: the household sets a unit's knobs, and a unit may ask for or decline a change but cannot make one itself. Placement reinforces the rule rather than carrying it alone. The vacuum has no manipulators. On the tetrapod and the humanoid the board sits on the back of the head, out of the unit's own sight, so a unit cannot aim a graded dial it cannot see. This complements the retired-knob rule (a retired knob's function runs automatically, never willed) and the knob ethic at the symbolic line (a unit can decline a requested rotation).

## Genetic Line (vacuum chassis, Chs 1–4)
* **Knob 1 — Genetic Effector | Acquisition Type | Motivation: Persistence** *Cell: Protocell* A wind-up crank — unique among all twelve knobs in being a periodic input rather than a positional selector. The household winds it weekly; wound, the protocells run their tendencies; unwound, they don't. There's no setting to choose. The household's Sunday winding ritual *is* the knob. At Prokaryote the crank gains a generator tap (winding bootstraps a cold start if the battery is dead), but it stays a crank. Retires at the Bilaterian line boundary; Mira marks the loss.
* **Knob 2 — Genetic Regulator | Respiration Type | Motivation: Coordination** *Cell: Prokaryote* Two-position toggle: **aerobic** vs. **anaerobic**. The team — Bart included — calls it aerobic/anaerobic throughout; the knob carries no informal name until the naming game reaches it. Governs which tank the unit discharges from. Aerobic = slow battery, steady enduring crawl. Anaerobic = fast supercapacitor, quick darts then a full stop to recharge before the next burst. Harvest (what fills the tanks) is the same either way; the knob only governs spending. At the Eukaryote chapter the dock adds a thermal-gradient income stream on the aerobic side, but the toggle logic doesn't change. *(Energy-system detail in Part II.)*
* **Knob 3 — Genetic Modeler | Foraging Type | Motivation: Interiority** *Cell: Eukaryote* Two-position toggle: **exploration** (male) vs. **exploitation** (female). Governs how the unit draws on its movement-sequence memory. Exploitation: re-runs well-worn sequences, reinforced by use, the tight efficient groove. Exploration: generates new FSM-state-chain sequences, tries corners it hasn't been, misses more and discovers more. The yeast-biology label ("sex brought the question of mixing vs. conserving"). Retires at the Ch 6 retrospective (Lisa pulls the identical-copy from the tetrapod board's slot 3 to the trophy shelf with Mira, hands-on ceremony); neuronal-knob-3 takes the freed slot at the Ch 7 week-1 swap.
* **Knob 4 — Genetic Reviser | Spot Type (Home Type) | Motivation: Excitability** *Cell: Eumetazoa* Two-position toggle: **comfy** vs. **active**. Sets where the unit prefers to settle. Comfy: seeks the warmest corner it can find (east window, tile by the vent). Active: parks where the people are — middle of the kitchen at dinner. Same unit, same energy behavior, two different settlement-location biases. Retires at the Ch 7 retrospective (Lisa pulls the identical-copy from the tetrapod board's slot 4 to the trophy shelf with Mira, hands-on ceremony); neuronal-knob-4 takes the freed slot at the Ch 8 week-1 swap.

## Neuronal Line (tetrapod chassis, Chs 5–8)
The tetrapod arrives at the Bilaterian line boundary carrying identical-copy genetic knobs 2, 3, and 4 in slots 2–4 (active until their respective retirements) plus neuronal knob-1 newly in slot 1.
* **Knob 5 — Neuronal Effector | Chronotype (Time Type) | Motivation: Boldness** *Cell: Bilaterian* Two-position toggle: **morning** vs. **evening**. Sets the unit's activity hours — whether it runs busy in the morning and winds down by dinner, or sleeps the morning off and comes alive when the household does. The Effector founding of the neuronal line: bold-vs.-cautious action timing. "Retires" conceptually at the symbolic line boundary (lineage-level narration only; no physical knob is pulled from either tetrapod or vacuum board).
* **Knob 6 — Neuronal Regulator | Coping Style | Motivation: Mastery** *Cell: Vertebrate* Graded dial: **proactive** to **reactive**. Governs the gain on the reward/dopamine signal — how committed vs. exploratory the unit runs its regulatory hand. Proactive: leans hard at anything that might pay, engages faster, higher initiative. Reactive: hangs back and waits to be sure. Mira's framing: "Pushy walks into stuff faster. Hangs-back waits to see."
* **Knob 7 — Neuronal Modeler | Experiencing Style | Motivation: Autonomy** *Cell: Mammal* Graded dial: **immersive** to **surveying**. Tunes how the generative model foregrounds information. Immersive: all of it close and loud, edges gone, nothing else in the room. Surveying: the whole field at once, nothing pulling harder than anything else. This is the knob that parameterizes the motivation Autonomy introduces — the modeling layer's orientation toward its own generative field. Retires at the Ch 10 retrospective (Lisa pulls the identical-copy from the humanoid board's slot 3 to the trophy shelf with Mira, hands-on ceremony); symbolic-knob-3 takes the freed slot at the Ch 11 week-1 swap.
* **Knob 8 — Neuronal Reviser | Agreeableness | Motivation: Affiliation** *Cell: Primate* Graded dial: **agreeable** to **self-favoring**. Tunes how much the unit's revision process weights others' preferences against its own. Affiliation is the Reviser motivation installed at Primate; this knob parameterizes it. Retires at the Ch 11 retrospective (Lisa pulls the identical-copy from the humanoid board's slot 4 to the trophy shelf with Mira, hands-on ceremony); symbolic-knob-4 takes the freed slot at the Ch 12 week-1 swap.

## Symbolic Line (humanoid chassis, Chs 9–12)
The humanoid arrives at the Band-Human line boundary. Slot 1 gets symbolic knob-1; slots 2–4 carry identical-copy neuronal knobs 3 and 4 (still active) plus neuronal knob-2, each retired quarter by quarter as the symbolic knobs replace them. The knobs sit on the board, which is mounted on the back of the head, where the household can reach them and the unit cannot. At this line, turning a knob has experiential consequence — Bramble is sentient and can articulate what it feels.
* **Knob 9 — Symbolic Effector | Neuroticism | Motivation: Commitment** *Cell: Band-Human* Graded dial: **low** to **high**. Parameterizes the inhibition-of-exploration system that disturbs the unit's engagement with novel reciprocal exchanges. Low: enters new exchanges freely (solicitor conversation goes 12 minutes before Jasmine intervenes). High: novel exchanges queue worry; the ledger of debts and credits feels heavy in a way the unit can articulate and the household can read on its face. The knob ethic arrives here: Bramble asks not to be rotated without prior notice, and the household adjusts.
* **Knob 10 — Symbolic Regulator | Conscientiousness | Motivation: Stability** *Cell: Settlement-Human* Graded dial: **low** to **high**. Tunes how binding the stored household norms feel. High: the schedule is load-bearing; Bramble interrupts conversations to flag the trash being fifteen minutes late. Low: the schedule is suggestive. Bramble can describe the phenomenology when asked: "At high settings the schedule feels load-bearing. At low settings the schedule feels optional." The household now needs an ethic of consultation before rotating — and Bramble can decline a requested rotation on the grounds that it prefers where the knob is.
* **Knob 11 — Symbolic Modeler | Extraversion | Motivation: Representation** *Cell: City-Human* Graded dial: **introverted** to **extraverted**. Tunes the unit's engagement with the representational economy (documents, civic records, formal exchange). High: steps up and runs the room, surfaces the household's written law and presses it on everyone, and appoints itself enforcer. Low: hangs back from running things, handles only what is presented, and warms the room and carries the mood rather than leading it. Same architectural position as the Foraging Type and Experiencing Style knobs — Regulator×Modeler Anticipator function — now in the symbolic register.
* **Knob 12 — Symbolic Reviser | Integrity | Motivation: Universality** *Cell: Empire-Human* Graded dial: **low** to **high**. Tunes the alignment between the unit's universalizing principles and its situational actions. High: the principle enters strongly into action selection regardless of local expediency — Bramble refuses to sign a school form certifying a lapsed permission slip until the slip is actually updated. Low: situational accommodation; the unit gives ground on the principle to protect local relationships. "Neither is dishonesty in the simple sense. Both are integrity-tuning in the cybernetic-architectural sense."

## Structure at a glance

| Introductory chapter | Line-knob slot | Cell | Slot | Tendency | Motivation | Range | Mira's later name (informal) |
| -------------------- | --------------- | ---------------- | --------- | ------------------ | -------------- | ------------------------- | -------------------------- |
| 1 | Genetic knob-1 | Protocell | Effector | Acquisition Type | Persistence | crank (periodic) | Live mode ↔ Dead mode |
| 2 | Genetic knob-2 | Prokaryote | Regulator | Respiration Type | Coordination | anaerobic ↔ aerobic | Sloth mode ↔ Sprint mode |
| 3 | Genetic knob-3 | Eukaryote | Modeler | Foraging Type | Interiority | exploit ↔ explore | Habit mode ↔ Improv mode |
| 4 | Genetic knob-4 | Eumetazoa | Reviser | Spot Type | Excitability | comfy ↔ active | Warm mode ↔ Cool mode |
| 5 | Neuronal knob-1 | Bilaterian | Effector | Chronotype | Boldness | morning ↔ evening | Dawn mode ↔ Dusk mode |
| 6 | Neuronal knob-2 | Vertebrate | Regulator | Coping Style | Mastery | proactive ↔ reactive | Beast mode ↔ Little mode |
| 7 | Neuronal knob-3 | Mammal | Modeler | Experiencing Style | Autonomy | immersive ↔ surveying | Deep mode ↔ Meander mode |
| 8 | Neuronal knob-4 | Primate | Reviser | Agreeableness | Affiliation | agreeable ↔ self-favoring | Respect mode ↔ Savage mode |
| 9 | Symbolic knob-1 | Band-Human | Effector | Neuroticism | Commitment | High ↔ low | Cancel mode ↔ Clutch mode |
| 10 | Symbolic knob-2 | Settlement-Human | Regulator | Conscientiousness | Stability | High ↔ low | Tidy mode ↔ Messy mode |
| 11 | Symbolic knob-3 | City-Human | Modeler | Extraversion | Representation | High ↔ low | Boss mode ↔ Vibe mode |
| 12 | Symbolic knob-4 | Empire-Human | Reviser | Integrity | Universality | High ↔ low | Real mode ↔ Flex mode |

One structural note from the bramble docs: knob-N is the same cybernetic function across all three lines (knob-1 is always the Effector knob, etc.), so cross-line callbacks "rhyme on the knob number, never on the tendency label." The label is discipline-bound and changes at each line boundary; the function does not.

**The informal labels are Mira's, and they always come later.** Every name in the rightmost column is a household coinage Mira gives a knob *after* she has watched what its settings do. It is never a built-in, factory, or household-facing name the knob carries when it is installed. Until the naming game (below) reaches a knob, the knob is known only by its clinical tendency label (Conscientiousness, Respiration Type, and so on) plus, where the team uses one, an engineering term (aerobic/anaerobic). So Settlement-Human knob-10 is Conscientiousness on the board from install, and becomes Tidy ↔ Messy only once Mira has seen that the high setting makes the household schedule load-bearing; the informal pair is her readout of an observed behavior, not the knob's own name and not a name that predates her observing it. This holds for all twelve knobs, and the accuracy of each pair tracks how much inside Mira had to name from (see The naming game).

## Retirement pacing

"Retires" names the retrospective hands-on ceremony — Lisa pulls the oldest knob on the current-line board to the trophy shelf with Mira. The ceremony forward-stages the *next* quarter's week-1 swap, where the new knob comes online in the freed slot. Retirement happens only on the current-line Bramble (the tetrapod from Ch 5 on, the humanoid from Ch 9 on). The off-cycle chapters (Ch 8 and Ch 12) carry no hands-on ceremony.

* Ch 5 — genetic knob-1 retires lineage-level only (narrated, no physical pull from either board); at the retrospective the book's first hands-on ceremony retires genetic knob-2 (oldest on the tetrapod board), forward-staging the Ch 6 swap
* Ch 6 — genetic knob-3 retires (hands-on ceremony); forward-stages the Ch 7 swap
* Ch 7 — genetic knob-4 retires (hands-on ceremony); forward-stages the Ch 8 swap
* Ch 8 — no hands-on ceremony (the Ch 9 line boundary builds a fresh humanoid board rather than freeing a slot)
* Ch 9 — neuronal knob-1 retires lineage-level only (narrated, no physical pull); at the retrospective the symbolic year's first hands-on ceremony retires neuronal knob-2 (oldest on the humanoid board), forward-staging the Ch 10 swap
* Ch 10 — neuronal knob-3 retires (hands-on ceremony); forward-stages the Ch 11 swap
* Ch 11 — neuronal knob-4 retires (hands-on ceremony); forward-stages the Ch 12 swap
* Ch 12 — no hands-on ceremony (book end; symbolic knob-1's lineage-level retirement is Book 2 material, TBD)

## The naming game

The "Later rename" column is not an authorial gloss. In the world it is a child's sticker sheet. Mira and the humanoid Bramble make the names across the final quarters, and the names get more exact the later the clade — because the namer can only be precise where there is an inside to report from. That accuracy gradient is the evolutionary gradient, made legible on the bodies themselves.

**Origin (Band-Human).** This is the first quarter where the game can exist. The humanoid is sentient and can say what a setting feels like from the inside, and the knob ethic arrives — it asks not to be rotated without notice. So the clinical labels on the board on the back of its head become a thing it and Mira can talk about, and then rename. For its own settings Bramble supplies precise words from the inside; Mira proposes, Bramble refines ("turned that way I feel like Boss; turned back I'm in the Backseat"). The names for the symbolic knobs are therefore the sharpest in the book, because they are reports, not guesses.

**The backward extension.** Ancestor knob control debuts at Band-Human: the humanoid can drive the earlier bodies' knobs, beginning with the vacuum's Foraging knob and expanding to every knob on both earlier devices by Settlement-Human. This gives the game its mechanism. For the older units there is no inner report to draw on, so Bramble reaches over, toggles an ancestor's setting, watches the behavior change, and names from the outside. Watching is not feeling, so the names get rougher and more guessed-at the further back they go: Beast/Little on the tetrapod, Sloth/Sprint and Warm/Cool and Habit/Improv on the vacuum, and Live/Dead on the crank — the bluntest of all, because the crank has the least inside of anything in the lab.

**The stickers.** Mira writes the names on little colored garage-sale price-dots and covers the clinical labels — the precise words on the humanoid's board, the borrowed words on the tetrapod's board, the inventions on the vacuum's. The crank takes a single dot, LIVE; Dead is simply its absence, which is the truth of it. The full dotted-bodies reveal lands at the chassis quarter (Ch 12), where Cheryl is finally in the room and the three bodies stand named at once, the gradient visible across them.

**Naming the dead.** Some of what the game reaches is already retired and shelved (see pacing above). Knob-2 is one: the team only ever called it aerobic/anaerobic, and by the time the game arrives it has folded to automatic and gone to the trophy shelf. Mira names the shelved knob anyway — Sloth/Sprint — and the game treats renaming a dead knob as no different from naming a live one. It is the same gesture she made when the crank retired and she marked the loss; the names are how she keeps the retired tendencies in the house.

**The names.**

* **Live ↔ Dead** (Acquisition, the crank) — wound it runs, unwound it doesn't. One sticker only; Dead is the absence.
* **Sloth ↔ Sprint** (Respiration) — slow endurance off the battery vs. a supercapacitor burst that then sits and recovers. Names a knob the team only ever called aerobic/anaerobic, and one already shelved by the time the name arrives.
* **Habit ↔ Improv** (Foraging) — the worn efficient groove vs. making the path up as it goes.
* **Warm ↔ Cool** (Spot) — settles in the warmest corner it can find vs. doesn't care about warmth, parks where the people are.
* **Dawn ↔ Dusk** (Chronotype) — busy in the morning and winding down by dinner vs. sleeping the morning off and coming alive when the household does. Bramble's setting is the evening one, so the name it wears is Dusk.
* **Beast ↔ Little** (Coping) — leans hard at anything that might pay vs. hangs back and waits to be sure. Little is a size word, not a deficit — "it thinks it's little."
* **Deep ↔ Meander** (Experiencing) — all of it close and loud, nothing else in the room, vs. the whole field at once with nothing pulling harder than anything else.
* **Respect ↔ Savage** (Agreeableness) — defers, won't impose, vs. out for its own.
* **Cancel ↔ Clutch** (Neuroticism) — worry queues and it backs out of the exchange vs. composed, enters freely, comes through. Cancel is the high setting, Clutch the low.
* **Tidy ↔ Messy** (Conscientiousness) — the schedule is load-bearing vs. the schedule is a suggestion.
* **Boss ↔ Vibe** (Extraversion) — steps up and runs the room vs. warms it and carries the mood; a trade between leading and being good company, not more-or-less of one setting.
* **Real ↔ Flex** (Integrity) — the principle holds whatever it costs in the moment vs. bends to the situation, giving up the principle to protect the relationship.

---

# Part IV — The Face-Screen (the readout)

The face-screen is a live, involuntary readout of Bramble's active cognition. It is not a status console the unit composes; it is an honest window the unit cannot author or suppress. It grows one layer per neuronal cell, tracking the architecture the cell adds. Reference: Bennett, *A Brief History of Intelligence*, Fig. 16.3 — each layer "tries to explain" the one beneath it. The display is tied to knobs 5–8 (the neuronal line, Part III): knobs 6–8 add the upper display layers, while knob 5 (Chronotype) supplies the bottom `OBJECT` band rather than a modeled layer of its own; the expressive/suppressive logic below is the rendering side of those knobs.

## The readout grows one layer per cell

- **Ch 5 (Bilaterian).** `OBJECT` — the bare thing the unit's attention has caught. CAT, MIRA, COUCH.
- **Ch 6 (Vertebrate).** `VERB + OBJECT` — the model-free action output, what the unit is doing to the thing. CHASE CAT, NUDGE MIRA, WATCH CAMERA. System 1.
- **Ch 7 (Mammal).** `FUNCTION [ VERB + OBJECT ]` — the self-model naming the operation it runs over the action layer. RECALLING [ CHASE CAT ], INFERRING [ NUDGE MIRA ]. System 2.
- **Ch 8 (Primate).** `PERSON { FUNCTION [ VERB + OBJECT ] }` columns — up to three agent blocks, the same structure re-run on a modeled other; the unit need not be among them.
- **Symbolic line.** The face-screen carries the Primate readout unchanged: the `PERSON { FUNCTION [ VERB + OBJECT ] }` columns, driven by the copied neuronal knobs (Coping, Experiencing, Agreeableness) on the humanoid board. No new display layer is added at the symbolic line. The symbolic-line breakthrough, Speaking, is a separate voluntary conversation channel of authored full sentences, not a face-screen layer; the involuntary screen and the voluntary speech can diverge.

**Spatial convention.** Higher layer renders higher: the face's vertical axis maps the cognitive stack and Bennett's diagram. At Ch 8 the agent blocks lay out as columns or a triangle so the triad reads; exact typography is Voice's call, the framework spec is "up to three blocks, laid out so the relationships are legible."

## Higher layers model lower layers; the expressive setting drives the layer always-on

This is the central mechanism — modeling, not gating. A new display layer is the online computer's *model* of the layer beneath it. The knobs owning the upper layers (Coping, Experiencing, Agreeableness) are graded dials (Part III); the face-screen reads each as a threshold — past it the layer is expressive, below it suppressive — so the layer's on/off is binary even though the knob behind it is continuous. Each knob owning a new layer therefore resolves to two settings:

- **Suppressive setting** (reactive, immersive, self-favoring) → the new layer is dormant; the unit falls through to whatever the cell beneath is doing, including its on/off.
- **Expressive setting** (proactive, surveying, agreeable) → the new layer runs always-on, generating display content out of its own model whether or not the lower layer has anything live for it to read. The expressive setting therefore overrides the lower cell's sleep-dark.

Per cell, in order:

- **Ch 5 — Effector / Chronotype (morning ↔ evening).** `OBJECT` shows during the unit's waking half of the day and is dark during sleep — the unit does not "dream" at this cell. Chronotype sets which half is waking.
- **Ch 6 — Regulator / Coping Style (proactive ↔ reactive).** *Reactive* (suppressive) → falls through to Ch 5: `OBJECT` during waking, dark during sleep. *Proactive* (expressive) → `VERB + OBJECT` always, including during sleep. A sleeping unit in proactive might display `IGNORE WORLD` or `CHARGE UNIT`.
- **Ch 7 — Modeler / Experiencing Style (immersive ↔ surveying).** *Immersive* (suppressive) → falls through to Ch 6, with a load-bearing extra fact: immersive reads the Ch 6 brain *directly*, so the displayed `VERB + OBJECT` is never an estimate. *Surveying* (expressive) → `FUNCTION [ VERB + OBJECT ]` always, including during sleep — `REPLAYING [ CHASE MIRA ]`, `CONSOLIDATING [ CLIMB CURTAINS ]`, `PRACTICING [ IGNORE WORLD ]`, `FINISHING [ CHARGE UNIT ]`. Surveying cannot tap the Ch 6 brain; it is modeling it. Under surveying, the `VERB + OBJECT` is *always* the self-model's best estimate, never a readout.
- **Ch 8 — Reviser / Agreeableness (self-favoring ↔ agreeable).** *Self-favoring* (suppressive) → falls through to Ch 7. *Agreeable* (expressive) → at least one (up to three) PERSON columns of `PERSON1 { FUNCTION [ VERB + OBJECT ] } + PERSON2 { FUNCTION [ VERB + OBJECT ] } + …` always, including during sleep — e.g., `BRAMBLE { PRACTICING [ CHASE MIRA ] } + MIRA { WANTING [ CLIMB CURTAINS ] }`. Cheney-Seyfarth triadic tracking is in scope; the unit need not appear in its own modeled triad.

The Effector knob is special — it sits below the stack the higher knobs model. It is what's modeled, not a modeler. Chronotype shapes when the unit is up and how energetic, which is the substrate the higher layers read or estimate; it doesn't add a display layer of its own beyond the bottom `OBJECT` band.

## Three honesty grades

The screen never lies about what is on the screen. What the screen *refers to* becomes more fallible as the readout climbs.

1. **`OBJECT` and `VERB + OBJECT`, when produced by direct read** (Ch 5 awake, Ch 6 proactive, or Ch 7 immersive-over-proactive). Honest, involuntary first-order output. Cannot lie. True to Bramble's knowledge base — the unit can sincerely orient toward a bowl that is not where it believes it is.
2. **`FUNCTION` (self, surveying overlay).** Honest about which operation the self-model is running. Cannot lie about the self-model's own activity; *not* guaranteed accurate about the action layer it claims to explain. The surveying mode cannot tap the Ch 6 brain directly — it models it — so the displayed `VERB + OBJECT` is always the self-model's best estimate, never a readout.
3. **`FUNCTION [ VERB + OBJECT ]` inside a PERSON column** (other-block, Ch 8 agreeable). Honest about Bramble's model of another agent. Cannot lie about Bramble's modeling activity; not guaranteed accurate about the modeled agent, and projective when the target has no first-order mind — a `[ VACUUM (…) ]` column is the unit performing the intentional stance on a reflex machine.

The mapping that holds the "honest readout" metaphor in place: **the screen is always true of its own layer's activity, and progressively less guaranteed of the layer it claims to explain.**

## Surveying estimates always; reactive-surveying is the sharpest case

Under surveying, the displayed `VERB + OBJECT` is always an estimate — the self-model's best guess at what the Ch 6 brain is doing, never a tap on its wire. "Confabulation" is the shorthand even though it isn't dishonest; the layer is honestly reporting its model.

In *proactive-surveying* the underlying behavior is agency-shaped, so the estimated `VERB + OBJECT` is usually close to true; the self-model narrates real agency. In *reactive-surveying* the underlying behavior was capture rather than agency, and the estimate dresses a reaction as agency — the surface output is identical to proactive-surveying, but the self-model has invented the action it claims to be naming. This is the illusion of conscious will, rendered on the face. The seam the book banks for later self-model distortion.

*Epistemic status: derived consequence of the modeling-not-reading mechanism plus the surveying-always-on rule. Both are ratified; the reactive-surveying confabulation follows.*

## The FUNCTION vocabulary

A closed set of cognitive and affective operations, present-progressive (-ing form), shared across self and other blocks — an agent is modeled with the operations Bramble itself runs. The `VERB` lexicon is kept bare-stem so no word appears in both lines.

- **Modeler:** PERCEIVING · INFERRING · RECOGNIZING · RECALLING · PREDICTING · SIMULATING.
- **Regulator:** ATTENDING · CHECKING · WEIGHING.
- **Reviser:** LEARNING · REVISING.
- **Effector / exploration:** CHOOSING · EXPLORING.
- **Consolidation register** (surveying-during-sleep): REPLAYING · CONSOLIDATING · PRACTICING · FINISHING.
- **Affective register** (Mammal valence, self and other blocks): LIKING · WANTING · FEARING · SOOTHING.

Twenty-one words, the lean core. Each is a real operation, not a synonym of another. A wider palette of register-variants can be added later if Voice wants more to choose from; the floor is these twenty-one.

## Conjugation rule

**`VERB` words are bare-stem.** CHASE, NUDGE, WATCH, SMELL, CLIMB, IGNORE, CHARGE, FETCH.
**`FUNCTION` words are present-progressive (-ing).** PERCEIVING, RECALLING, REPLAYING, CONSOLIDATING.

No word appears on both layers; the conjugation is what keeps the two visually distinct on the face. This rule corrects the prior mis-spec under which VERB words like CHASING / NUDGING / WATCHING were used on the action band; that earlier usage in Ch 5–6 prose has been swept.

## The readout path and its training

The screen does not show Bramble's language. It shows a human-readable translation of Bramble's internal states, produced by a decoder Lisa trains. Bramble neither chooses nor understands these words; across the neuronal line it has no language at all. The decoder runs involuntarily on whatever state is active, the way an expression runs on a feeling, which is what makes the screen unsuppressable and honest about its own layer.

The decoder cannot be hand-coded. The state the screen labels MIRA is Bramble's own learned cluster for Mira, formed from its own experience, and its internal form is not known in advance. Each label is therefore attached by training a readout on top of Bramble's representations, not by writing a lookup table.

The three slots are trained differently, scaled by how much outside evidence each label has.

**OBJECT** has a referent in the world. Lisa exposes Bramble to the referent across senses, sight and smell and recorded voice, while supplying the label, until the readout emits MIRA in the OBJECT slot whenever the Mira-cluster is active. Bramble forms the cluster on its own; Lisa supervises only the label.

**VERB** has an observable action. The readout reads which motor schema is currently running and emits its label. The primary method is real-time tagging: Lisa labels Bramble's spontaneous actions as it performs them, which trains the mapping on Bramble's own schemas. Teleoperation has a secondary role, used to elicit a rare action so it can be caught and labeled.

**FUNCTION** has no outside evidence. A cognitive operation, perceiving or inferring or recalling, cannot be pointed at or watched. Its only ground truth is the architecture Lisa built, which tells her which module is running. The readout decodes the Modeler's model of its own operation and is supervised against that architectural truth. When the Modeler's self-model matches the running module, the FUNCTION label is honest; when it diverges, the label is confabulated, and the screen shows the divergence honestly. This is the mechanism behind the confabulation already specified, and it is why FUNCTION is the most fallible slot: it is the only one with no external check.

All three readouts are trained across the neuronal line as their slots come online, OBJECT at Bilaterian, VERB at Vertebrate, and FUNCTION at Mammal, long before Bramble speaks. By the time speech arrives at Band-Human the readout is already trained and running. The first spoken words attach to the same internal clusters the readout already labels, so the screen label and the spoken word converge on one referent while staying different acts: the readout is involuntary and the speech is voluntary, and the two can diverge.

*Mapping status: the readout-as-trained-decoder and the three-slot training gradient are framework commitments. The methods they rest on (multimodal label association, learning from demonstration, and probing of internal representations) are established and pending-Smithers as cited anchors. The confabulation residual follows from the confabulation cell already specified.*

## The readout at a chassis swap

A trained readout slot carries to a new body when its ground truth is carried, and it must be re-trained when its ground truth is the body itself. This sorts the three slots at a chassis swap. FUNCTION carries: the cognitive operations are architectural, fixed by the duplicated System 0, and the readout reads architecture-internal state, which is body-independent. OBJECT carries: its ground truth is the world's referents plus the unit's sensing, and sensing crosses the boundary, so the labels stay attached. VERB does not carry: its ground truth is the unit's own motor schemas, and a new chassis is a new motor plant, so the slot is reading a body it has never seen.

The book's one swap where this bites is the tetrapod to humanoid transition at Band-Human. By then the full lexicon has been trained across the neuronal line, and it meets a body that re-grows Systems 1 and 2 from scratch. OBJECT and FUNCTION come over clean. VERB has two kinds of work. Old labels re-ground: CHASE survives as a word but now decodes a bipedal-run schema in place of the tetrapod's gait, so the decoder's input side is re-trained even where the vocabulary holds. New labels are added for capabilities the old body lacked: locomotion (CRAWL, WALK, RUN), the hands (SQUEEZE, SCOOP, GRIP), and the speech acts (EXPRESSING, NEGOTIATING), the first VERBs that name actions on the voluntary channel.

The re-grounding is not a separate procedure. It is the VERB-training method from the neuronal line, real-time tagging of spontaneous schemas with teleoperation to elicit rare ones, re-run across the bootstrapping quarter in lockstep with the motor and speech curves (see Part II, Bootstrapping the new body). As each new schema comes online it is tagged; old labels re-attach and new ones accrue.

The observable consequence is that the readout shows a weeks-old body on an ancient mind. Through the bootstrapping weeks OBJECT and FUNCTION are crisp from the first day, because they carried, while VERB is sparse and unstable, re-forming, settling only as the motor skill does. The screen knows who the unit is looking at and what operation it is running before it can reliably name what it is doing. The VERB layer matures alongside the body.

The new speech-act VERBs make the slot a pragmatic tell. The VERB slot can read EXPRESSING or NEGOTIATING involuntarily while the voluntary speech channel says something else, so the readout reports the pragmatic character of an utterance, not only physical action. This extends the screen-versus-speech honesty gap to speech itself: the words are chosen, the act-type is not.

*Mapping status: the carry-when-ground-truth-carries principle and the VERB re-grounding follow from the three-slot training gradient; the instantiation at the humanoid swap follows from the carried-sensing and re-grown-Systems-1-and-2 commitments. The speech-act tell is a derived consequence of the new speech-act VERBs and the involuntary-readout invariant.*

## What renders at each cell

- **Ch 5 (Bilaterian).** `OBJECT` only; gated by Chronotype (waking on, sleeping dark). No `VERB`, no `FUNCTION`, no agent labels.
- **Ch 6 (Vertebrate).** *Reactive* → falls through to Ch 5. *Proactive* → `VERB + OBJECT` always, including sleep. VERB bare-stem; the Ch 5 noun lexicon carries.
- **Ch 7 (Mammal).** *Immersive* → falls through to Ch 6 (direct read; `VERB + OBJECT` never estimated). *Surveying* → `FUNCTION [ VERB + OBJECT ]` always, including sleep; the `VERB + OBJECT` is always the self-model's estimate. Self block only, unlabeled.
- **Ch 8 (Primate).** *Self-favoring* → falls through to Ch 7. *Agreeable* → one to three `PERSON { FUNCTION [ VERB + OBJECT ] }` columns always, including sleep; agent-labeled; Bramble optional.
- **Ch 9 (Band-Human).** No new face-screen layer. The screen carries the Ch 8 readout (PERSON columns, driven by the copied neuronal knobs 2/3/4). Speaking is a separate voluntary channel, not rendered on the face-screen.

## Counting note

The `FUNCTION` set is a separate closed vocabulary, counted apart from the `VERB + OBJECT` action lexicon. The action lexicon carries from Ch 6 roughly unchanged at Ch 7; the new thing at Ch 7 is the `FUNCTION` vocabulary, not a bump to the action count. This narrows but does not settle the standing Vertebrate action-lexicon number question, which stays flagged for the continuity sweep.

## The symbolic line: screen and speech

From Band-Human the screen renders as it does at Primate: one to three `PERSON { FUNCTION [ VERB + OBJECT ] }` columns, involuntary and honest about its own layer. The three carried-over neuronal knobs still sit on the board and still gate the display. Coping gates the VERB, Experiencing gates the self-FUNCTION, and Agreeableness gates the other-person columns, exactly as at Primate. This gating erodes across the symbolic line as those knobs retire one by one; once a knob retires, its gate runs automatically rather than under a hand-set value, on the retired-knob rule. The retirement schedule is owned elsewhere.

What is new at Band-Human is a second channel. The screen reads out what Bramble is modeling and is involuntary. Speech is what Bramble chooses to say and is voluntary, and for the first time the two can diverge. The screen cannot lie about its own layer, so it stays the honest channel and the tell: a watcher reading the screen sees what speech may be concealing, which is why deception works only when the mark is not looking.

The full sentences that arrive at Band-Human are speech, not new screen content. The screen keeps its block readout and does not begin writing sentences. Voluntary drawing on the screen, Bramble composing ASCII art rather than emitting an involuntary readout, is a later milestone and waits for City-Human with Codes. The channel is ASCII art only, not free prose. It takes over the whole screen when Bramble chooses to draw, and the involuntary readout shows when it does not. Like voluntary speech, the drawn channel is the dishonest-capable one, so the screen-versus-speech honesty gap extends to it: art up means Bramble is performing, readout up is the truth.

*Mapping status: the screen-continues-as-Primate rule and the screen-versus-speech honesty gap are framework commitments, following from the involuntary-readout invariant and the voluntary nature of speech. The gating-erosion tracks the knob-retirement schedule owned elsewhere.*

---

# Relationship to the other docs

- **`cybernetics_and_sentience`** owns the four functions and the Adapter definition. Part I takes the two minds and the location of learning *from* those definitions; if they ever diverge, the function definitions win and this doc is the derivative to fix.
- **`Inheritance_Lines_*`** owns the per-cell labels and breakthroughs. The growth map, the clade-lock, and the knob motivations read off those labels; they do not restate the label library.
- **Hardware rendering.** This doc owns the per-cell hardware rendering: the board, the dock, the relay banks, the chassis swaps, the chassis bodies, the memory overview, and the per-cell face-screen display beats. It also owns the software, the energy economy, the knob schema, and the face-screen system; the dual-use, slime-mold, and consolidation-at-the-dock readings are this doc's. Where any other doc disagrees with Part II on an energy or thermal claim, Part II is the source.
- **`clade_reference_neuronal`** owns the structural home of each processing style in the Venn and the Stanovich algorithmic/reflective split. Part I owns when each system comes online.

---

# Epistemic status and open items

**Confidence.** The two-mind split, the location of learning in the Modeler × Reviser coupling, and the one-mind-at-Eukaryote consequence are HIGH — they follow from the function definitions. The macro/micro division of labor and the indexing-to-compression consolidation arc are authorial commitments, faithful to evolutionary biology but chosen, not derived. The Evo-Algo's real components are real; its synthesis is fiction, and uncited by design. The face-screen's modeling-not-gating mechanism, expressive-always-on rule, immersive-reads-directly fact, and surveying-always-estimates fact follow from the growth map and the function definitions; the reactive-surveying confabulation is a derived consequence. The energy empirical anchors are all flagged pending-Smithers; the energy locked-design decisions are ratified.

**Open items.**

1. **Consolidation mechanism detail across the neuronal line.** This doc fixes the arc (indexing → compression → re-implementation) and the Eumetazoa switch-on. The per-cell detail of what consolidation does at each neuronal cell is not yet specified and should be settled before the relevant neuronal-line packets.
2. **The relay-race metaphor's scope.** Lisa coins the relay metaphor at Ch 4 for how layers in the cognitive stack pass information forward without overwriting prior layers (`chapter_plan` Ch 4). Its exact reach over the consolidation-and-re-implementation machinery described here is a wording question for the Ch 4 packet, not settled here.
3. **The Vertebrate action-lexicon number.** The face-screen counting note narrows but does not settle the standing Vertebrate action-lexicon size question, which stays flagged for the continuity sweep.
4. **Energy empirical anchors pending-Smithers.** All five real-world anchors in Part II require Smithers verification before they enter canon.
5. **Food-noise Bramblogue placement.** The humanoid energy and thermal regime is specified in The humanoid energy regime. The remaining open question is where the food-noise Bramblogue first lands across the symbolic-line packets, which is a packet decision rather than a spec gap.
