# Bramble Specs — Cognitive Architecture, Energy, Knobs, and Face-Screen

---

# Part I — Cognitive Architecture (the software)

## What this part settles

Lisa's algorithm has been a placeholder noun since Ch 2. Everything from Ch 3 forward — the board, the memory, the eventual brain — runs on whatever it actually is. This part fixes what it is, what it can and cannot do at each cell, and how much of it Lisa builds by hand versus how much it grows on its own.

One framing governs the whole part. The goal is not to build a great mind in Bramble. The goal is a teaching instrument for how biological minds evolved. So the controlling question at every cell is not "what could the software do" but "what is the least the software must do to render this cell honestly" — and, just as important, what it must be *prevented* from doing, the way the genetic-line chassis is prevented from having wires.

---

## The two minds

The framework's Modeler already forces a two-timescale reading; the architecture does not invent it. The **Modeler** is the internal representation that organizes inputs into a usable account of the world, and updating that account — from outcomes, from use, from anything the unit's own traffic brings in — is Modeler work within one system of terms. An account runs at two speeds: the structure carried across runs, and the fast working account of the run underway.

So Bramble carries two minds, and they are the two timescales of one function.

- The **deep-time mind** is the Modeler's slow face: a persistent representation the unit carries across runs. It is the thing that is *learned upon*. It is slow, structural, and changed by consolidation, not by the moment.
- The **online mind** is the Modeler's fast face: the working account of the run underway, proposing candidate updates against the world as it is right now.

The single most important consequence: **learning from experience is not located in either mind. It is the coupling between them.** The online mind proposes candidate updates; the deep-time mind integrates them into structure. That integration is the Modeler updating its own account across its two timescales — one system of terms throughout, no second party in the room. This is why "the deep-time mind reads from the online mind and runs consolidation on it" is not an add-on feature — it *is* the account remaking itself, the Modeler doing its defined job. What the coupling is not is the Adapter: the Adapter loop is the account remade by content arriving from another party's terms — Lisa's labels, the household's speech, Mira's names — and it is a different channel from the within-unit coupling described here. The relationship is hierarchical in exactly one direction: the deep-time mind reads the online mind and reshapes itself; the online mind runs on the structure the deep-time mind currently holds.

*Mapping status: HIGH. The two-mind split and the location of within-unit learning in the coupling follow directly from the Modeler's definition and the two retention times the substrate supplies. They are not new constructs.*

---

## Why there is only one mind at Eukaryote

At Eukaryote the unit's four active motivations are Persistence, Thrift, Interiority, and Niche Formation. The Translator motivation there is **Niche Formation** — the drive to render one's presence into the surroundings, which at this cell is metabolic and ecological rather than cognitive. It is not a built second cognitive system. The first Translator that exists as built machinery is **Excitability**, the nervous tissue that arrives at Eumetazoa — carriage between specialized parts.

This settles the Ch 3 teaching beat as a consequence of the architecture, not a craft choice. At Eukaryote there is exactly one built mind: the board, the Modeler, running at one timescale. The board holds a representation shaped by what the unit has done; it cannot yet be updated against outcomes, because there is no outcome signal — no arena, no score, no write-back until Attention installs at Bilaterian. **"It remembers; it does not yet learn from outcomes"** follows from the write-back requirement: a store edited only by use is a record, and a store edited by scored outcomes is a learner, and the scoring machinery has not been built. The cell's Conservator character — the mature loop sealed in its own terms (Effector + Regulator + Modeler, no Translator) — is the same fact from the slot side: nothing at this cell renders to or takes up from any second party.

The genetic line even names the pieces. The Adapter slot at Eukaryote is **Compartmentalization** — how much of its interior the unit divides into separate rooms, the paradigm room being the taken-in partner — because the genetic-line Translator renders chemistry rather than signals. The cognitive reading of the Adapter loop — the account remade by what another party renders — does not switch on until there is machinery that can carry content between minds.

---

## What the Evolutionary Algorithm is

**Lisa's Evolutionary Algorithm is an evolution-as-learning process over a developmental, gene-regulatory-network-style genome — the deep-time mind — which grows and consolidates an active-inference online mind, in one self-transforming loop where the evolving *is* the learning.**

Two real results are the load-bearing pillars.

- **Evolution as learning (the deep-time mind's principle).** Watson & Szathmáry's result is that natural selection on developmental and gene-regulatory structure is formally a learning process — associative memory, and with the right structure, generalization. This is the literal justification for calling a *learning* mind an *Evolutionary* Algorithm. It is not a coincidence to be papered over; it is the thesis. The deep-time mind learns *by evolving its genome*.
- **Active inference (the online mind's principle).** Friston's formulation gives the online mind one operating principle — act and perceive so as to minimize prediction error against a generative model — that scales from a single cell to a cortex. That span is exactly the span Bramble must cover, which is why it is the right backbone rather than any narrower controller.

**The in-scene engineering motive is topology, not theory.** What Lisa can buy cheaply is memory. What matters from Bilaterian on is the organization above it, and she has no principled way to derive a wiring diagram — so she searches rather than specifies. Evolutionary methods are what searching architectures is for and what design is not. This is available to her at Ch 3 as a plain engineering problem; Watson & Szathmáry's evolution-as-learning result is the deeper claim underneath it and keeps its Ch 6 pacing.

*Citation pacing.* The mechanism (evolution-as-learning) is present in the architecture from Ch 3, but the **citation** to Watson & Szathmáry is paced: it does not surface in prose until Ch 6, where a retired knob's function is shown to persist. Friston is Lisa's standing register and surfaces as the online mind is built (neuronal line). At Ch 3 the algorithm is named and runs in degenerate mode; its principles are not yet unpacked.

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

**The full Evo-Algo machinery installs at Ch 3, but at each cell only the operations that cell's breakthrough licenses are switched on. The rest is present but dormant — clade-locked.**

The lock is not arbitrary. The framework's own layer grid says which operation unlocks where; the clade-lock follows the breakthrough at each cell. This is the software analogue of intracellular transport standing in for wires at Eukaryote: the capability the cell has not earned is structurally withheld, not merely unused.

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

The architecture sorts into three control systems on one axis: how behavior gets picked, and on what timescale. This axis is distinct from the four-function axis (Effector, Regulator, Modeler, Translator). A function names a role in the control loop. A system names a timescale and locus of the picking. The two axes are read together, not merged.

**System 0 is the Evolutionary Algorithm, the lineage.** It is the deep-time mind. It evolves as it learns, and it consolidates the online mind across runs. Its model of the world lives at the lineage level, distributed in gene-regulatory structure as developmental memory. That model is implemented at the individual as the structure the online mind runs on. System 0 sits below the individual. Neither Kahneman nor Stanovich names it; both name only individual processing. System 0 is the framework's addition, and it is what makes the Evo-Algo the lineage itself.

**System 1 is the autonomous mind, the unit's fast automatic processing.** It is preattentive, parallel, and low cost. It produces a response without deliberation. Procedural memory lives here, overlearned skill run as second nature. A retired knob's function persists here: the consolidated reward-shaped policy that was once a hand-set knob now runs automatically, as autonomous regulation, never willed. Through the lower neuronal cells the online mind is System 1 only. It is associative learning at Bilaterian and reward-shaped procedural policy at Vertebrate.

**System 2 is the virtual mind, and it arrives at Mammal with the generative model (Simulating).** It is virtual because it runs the generative model offline, decoupled from action, producing trajectories the unit can run without enacting. It is the attentive level. Stanovich resolves it into two minds. The algorithmic mind runs serial associative cognition: it generates associations along a single track from a focal premise. It is metabolically costly and decoupled from immediate action. Heuristics-and-biases errors arise here as override failures: the reflective mind does not make a decoupling call, so the unit elaborates a flawed premise on one track without questioning it (confirmation bias, belief bias, override failure). The reflective mind makes the decoupling call. It detaches from the focal premise to simulate alternatives. It overrides both the algorithmic mind's serial track and the autonomous mind's default response.

System 2 requires a generative model: a separable, runnable model of the world the unit can decouple from action and run forward. That model is the Mammal breakthrough. Before Mammal there is no System 2, only System 1 running on System 0's structure.

**Crosswalk.** Kahneman's System 1 is Stanovich's autonomous mind. Kahneman's System 2 is Stanovich's algorithmic mind plus reflective mind. Neither author names a System 0. That layer is the framework's, identifying the Evo-Algo with the lineage.

**The function axis and the system axis are not the same cut.** A function (Effector, Regulator, Modeler, or Translator) is present at every cell in some form. A system is a developed processing capability that arrives at a cell. The Regulator function is present at Vertebrate as Mastery. The algorithmic mind as a System-2 capability is not, because serial associative cognition needs the generative model that arrives at Mammal. Each processing style has a structural home in the Venn, at a triple of the Mammal cell. What is fixed here is when each system comes online.

*Mapping status. System 0 = Evo-Algo and System 1 = autonomous/procedural follow from the consolidation and division-of-labor commitments: HIGH. The arrival of System 2 with the Mammal generative model follows from the Simulating breakthrough: HIGH. The split of System 2 into Stanovich's algorithmic and reflective minds is an absorbed mapping; the tri-process constructs sit at three triples of the Mammal cell.*

---

## The substrate

The board has been described eleven different ways without being identified: durable storage, System 0, runs cool, the only thing carried across a line boundary. All true, all declared. This section fixes the material, and once the material is fixed, three things that would otherwise have to be asserted fall out of it instead — that board and compute are separate substrates, that only the board crosses a chassis boundary, and that Lisa needs an evolutionary algorithm rather than a designer. None of those has to be argued. They are properties of the parts.

The governing constraint is the one that governs the whole document. The components are real and reachable by a practitioner who started undergrad in 2015 and worked through 2030. Nothing here is invented hardware. What is invented is the arrangement.

### What is on the market in 2031

Three families of part matter, and they are three families because they answer three different questions about memory: how long does it hold, how much does it hold, and can you compute with it while it holds.

**Analog resistive memory: memory you cannot read.** Two electrodes with a thin metal-oxide film between them, hafnium oxide typically. Drive current one way and oxygen vacancies drift into a conductive filament bridging the gap, and the resistance falls. Drive it the other way and the filament partly dissolves, and the resistance rises. Stop driving and it stays where you left it. The resistance of the thing is a physical record of the current that has passed through it, and because it holds a continuum rather than a one or a zero, it is memory and arithmetic in the same device.

Arranged in a grid — rows of wires over columns, a junction at every intersection — it becomes a computer with no instructions. Put voltages on the rows. At each junction Ohm's law multiplies voltage by conductance to give a current, and at each column Kirchhoff's law sums those currents, because that is what happens when wires meet. Every multiplication and every summation occurs simultaneously, in the physics, at femtojoules apiece. A matrix-vector multiply, which is nearly the whole of what a neural network does, executed in one step by a passive grid that has fetched nothing and run nothing.

Learning is a pulse. A small voltage grows the filament a little: conductance up. Reverse pulse: conductance down. Put a pulse on a row and a pulse on a column at the same moment and only their intersection sees enough voltage to change, which is Hebb's rule falling out of the wiring instead of being programmed into it. The weight is not stored somewhere and updated. The weight is a physical property that gets worn.

Three practical facts about these arrays are load-bearing, and all three are defects.

*Forming.* A virgin array is not zeros. It is unusable. Every junction requires a one-time high-voltage jolt that creates its initial filament, a controlled soft breakdown. Forming is the field's standing yield problem, because a junction that breaks down too hard never works again. After forming, the surviving devices are wildly unequal, and the inequality is not a defect to be corrected out but a permanent characteristic of that particular array. So an array arrives with a physical character nobody chose and nobody can fully characterize, and that character never washes out. It sits under everything the array subsequently learns.

*Approximate writes.* You can put initial values into an array, but not by writing them. You measure what a junction currently does, pulse it toward what you want, measure again, pulse again, and converge. You get it approximately right: five to eight bits on a good day, fewer as the array ages, and the precision falls as the array gets larger. The write has to be serial, because a precise analog write to one junction leaks half-select voltage onto its neighbors.

*Unreadability.* Reading the array tells you the conductance of a junction now. It does not tell you how much of that conductance was forming and how much was use, because there is no record of either — the junction is the record, and the record has one number in it.

**Event-driven neuromorphic fabric: computation you can rewire.** A mesh of small digital cores, each hosting thousands of neuron compartments, connected by a router network that carries spikes as addressed events. Nothing is clocked in the ordinary sense and nothing runs when nothing is happening, which is why the power draw is milliwatts where an equivalent general processor is watts. Each compartment's dynamics are set by programmable microcode, so the fabric implements not one neuron model but any discrete dynamical system that fits its budget. Learning rules run on-chip, locally, at the junction.

Two properties matter here more than the efficiency. *Topology is the product* — what the fabric gives you is a programmable answer to the question of what connects to what, so a different wiring diagram is a different upload rather than a different chip. This is the only commodity substrate on which an architecture can be searched rather than designed. And *compartments can be spent on depth* — multiple compartments can be assigned to one cell with their own integration and their own coincidence conditions between them, metered as a distinct class of operation from synaptic work. The budget can be spent two ways: more cells, or more structure inside a cell.

The fabric is volatile. Membrane states, synaptic weights, and the microcode itself sit in on-core SRAM, which loses everything when power drops and must be reloaded from somewhere nonvolatile at boot.

**High-endurance nonvolatile RAM: memory you can write to forever.** The least interesting family and the most necessary. An autobiography is a memory written to constantly, all day, for years, that must survive every power loss and need never support arithmetic. Flash dies at a hundred thousand write cycles. Ferroelectric memory has the endurance but lives in the megabyte range, which is not the size of a life. Magnetoresistive RAM has both: a magnetic tunnel junction stores its bit as the relative magnetization of two layers across an insulating oxide, and switching that magnetization neither moves atoms nor wears the material out. Write endurance runs to 10¹⁵ cycles and above, retention is a decade and better, density approaches DRAM. By 2031 it is the obvious and boring choice, which is what a part inside a household robot should be.

*Empirical anchors, pending-Smithers: wafer-scale passive memristive crossbar fabrication at ~95% yield (Nature Communications, 2025); 5–8 bit analog precision depending on array size (Hu et al., IEEE); electroforming as the yield-limiting soft-breakdown step; Ki et al. 2026 for the Bi₂Se₃ retention-and-tunability result; Loihi 2 and SpiNNaker-2 architecture, address-event routing, programmable per-compartment microcode, on-chip learning rules, SRAM-resident state, and the metering of dendritic operations as a distinct class; STT-MRAM endurance >10¹⁵ cycles, 10–35 ns reads, 10–100 ns writes, retention beyond ten years at 85 °C, eMRAM in production at 22–28 nm. These are real published findings and are cited as such. No citation is attached anywhere to the synthesis, which is Lisa's.*

### The three organs

Bramble's mind is built from all three families, one per timescale.

**The board is an analog resistive crossbar.** It is System 0, the deep-time mind. It holds nothing as a value and everything as a physical property. It computes where it stores. It is the only organ in the unit whose contents are worn rather than written, and the only one that carries a character its maker did not choose.

**The fabric is an event-driven neuromorphic mesh.** It is the compute, the online mind, Systems 1 and 2. Its wiring diagram is what the Evolutionary Algorithm searches. It holds nothing when the power is off.

**The store is MRAM.** It is the raw episodic record — the generative-model hardware the virtual mind runs on, in the brain layer above the board. It arrives at Mammal with the generative model and stays with the body that wrote it.

Three organs, three retention times, and the architecture's most abstract quantity becomes a physical fact:

> **The crossbar keeps forever. The store keeps a life. The fabric keeps right now.**
>
> Lineage, individual, moment.

Consolidation distance stops being a metaphor. It is a distance across three parts.

### What each organ forces

**Forming is temperament, and it arrives at the cell whose motivation is Interiority.** The board installs at Eukaryote, Ch 3 — the cell whose Modeler motivation is Interiority and whose knob is Pruning Type. Before the board there is no persistent state to hold. The crossbar is the physical form of the Eukaryote breakthrough, and it cannot be installed earlier because there is nothing earlier for it to be.

Forming is therefore a single event in the build. Lisa jolts the array, some junctions die, and the survivors come up unequal in a pattern nobody selected. From that moment the unit has a disposition it was born with, unrequested, and everything use subsequently wears into the array sits on top of it with no line between them. Neither preloaded reflexes nor a blank slate. A third thing, and the third thing is a fabrication defect. This is the hardware thesis executed exactly: behavior moved out of the program and into a part. It is also the nature-and-nurture question settled without anyone adjudicating it.

And the person who built it cannot read out which is which. Reading the array returns conductance now, not its provenance. Lisa spends the build in the epistemic position her colleague describes clinically one chapter before she builds the thing: reaching at a shape she cannot describe in first-person language, with only behavior to go on.

**Use thins on one array and thickens on the other, and that is why there are two minds.** The Eukaryote board is use-weighted persistent state, slime-mold tube logic, thickened by use and faded by disuse. The Eumetazoa nerve net that arrives one cell later runs the opposite sign: habituation is presynaptic depression, repeated use inactivating channels so the junction gets weaker, and it is the more fundamental of that cell's two capacities. Sensitization is the same junction facilitated by a modulatory signal.

Both are single-junction gain changes with no coincidence requirement and no network involved: one wire worn thinner or thicker by use. That is a memristor with a polarity, and it means **the second mind is born at Eumetazoa as a second crossbar running the opposite sign under the first.** No new class of part is required for the two-mind split, which is why the split can arrive at a cell whose whole content is reflex plus non-associative tuning. The two-substrate architecture originates in a polarity difference rather than an authorial decision.

**Allostasis does not live on either array.** Neuromodulation is not a weight matrix; it is one scalar sprayed diffusely over the whole tissue, changing its gain all at once. A crossbar has no mechanism for this, so it is added as a global bias line: a single wire that crosses every junction and owns none of them. This satisfies the rule that energy and arousal stay off the board and out of the knob slots, and it satisfies it mechanically rather than by policy — the bias line cannot occupy a slot, because it has no address.

**The fabric arrives when architecture starts to matter.** Through Bilaterian the crossbar is an excellent model of a synapse. The NMDA receptor requires both presynaptic glutamate and postsynaptic depolarization to open — two lines active, one junction changes — which is precisely the crossbar's row-and-column selection rule and the tightest correspondence in the whole architecture. Associative learning drops out of the wiring.

But Bilaterian is also centralization, and a brain is a place; getting signals to a place is topology. From here on what Lisa needs is not more memory but a wiring diagram, and she has no principled way to derive one. The thing she can buy cheaply is the memory. The thing that matters after Bilaterian is the organization above it, and organization is exactly what evolutionary methods are for and what design is not. So she searches rather than specifies.

Bilaterian also forces the first thing the substrate cannot natively do. Real plasticity is three-factor — presynaptic, postsynaptic, and *was that good* — and a crossbar natively does two. Valence requires a third signal path per junction, which is the main reason on-chip learning is harder than on-chip inference. This is a real, named, current difficulty in the field, and it is the first place the build costs Lisa something.

**The eligibility trace puts two retention times in one junction.** Reward arrives seconds after the action, so a junction has to hold a decaying tag saying *we just fired together* and wait to find out whether it mattered. Dopamine converts surviving tags into permanent change. Volatile resistive devices do this natively — diffusive junctions whose filament spontaneously dissolves over hundreds of milliseconds, giving a physical decaying trace at the junction rather than a variable in a register. So the Vertebrate board is not one array. It is a fast leaky layer over a slow permanent one.

Which is the online mind and the deep-time mind, in hardware, at the scale of a single junction. **The same shape at three scales: junction in milliseconds, individual over a life, lineage over twelve quarters.** This does not merge board and compute. It rhymes with them, and the rhyme is what makes the discard at a line boundary mechanical rather than a policy.

**Mammal is where the substrate breaks, and the break is the content.** A cortical column's value is architecture: six layers, a canonical microcircuit, feedforward from below and feedback from above meeting in specific laminae. None of that is weight storage. And dendrites compute — a pyramidal neuron is not a summing node. Its apical tuft and its basal dendrites integrate separately, and when feedback arriving at the top coincides with feedforward arriving at the bottom, the cell fires a burst it would not otherwise fire. That is a two-compartment coincidence detector, and it is arguably the physical seat of a higher layer explaining the layer beneath it, which is Bennett's frame and this architecture's spine. A crossbar sums every input into one column and flattens that structure away entirely.

This is not fixed. The generative model sits in the brain layer above the board, and the substrate is what tells you why *above* and not *more of*. Nobody builds cortical columns out of crossbars. What happens instead is a budget decision on the fabric: Mammal is the cell where the Evo-Algo stops buying more neurons and starts buying compartments inside single neurons, spending its allocation on depth rather than width. The central architectural claim arrives as a line item in a resource budget, which is the correct register for it.

Mammal is also where the MRAM store installs, because Mammal is where there is first an autobiography to keep.

**The board lays out the fabric every morning.** The fabric is SRAM-configured and loses its configuration at power-down. It reloads at boot from nonvolatile store, and the nonvolatile store of the architecture is the board. So the board does not merely supply the structure the online mind runs on. **The board physically instantiates the compute at every wake.** Bramble is re-developed each morning from the same seed, which is why it is the same person on Tuesday, and why sleep is a real boundary in the unit's life rather than a pause. It is also why the compute can be discarded at a chassis boundary without anyone deciding to discard it. There is nothing there to take.

**Cold is retention, not efficiency.** The board and the compute sit outside the warm core, running cool. With an analog substrate the reason is stronger than efficiency: conductance drifts with temperature, and drift on the board is the unit's dispositions moving. Which makes Mammal's arrival a genuine hazard rather than a placement note. The unit acquires a furnace and installs it inches from the only part of itself that cannot be rewritten.

### Install schedule

| Cell | Ch | Substrate event |
| --- | --- | --- |
| The groundwork row | — | None. No stored state of any kind. Drawn and never counted; it holds no quarter. |
| Prokaryote | 1 | FSM with stored procedures. Conventional digital logic. No analog array. |
| Archaeon | 2 | **The dock.** Outboard coupled-vortex station, run on a debris deposit — the trade that makes the unit's margin. Idle draw falls. Still no analog array. |
| Eukaryote | 3 | **The board.** Resistive crossbar formed and installed. Thickens with use. Temperament arrives as a fabrication defect. |
| Eumetazoa | 4 | **The second array.** Fast crossbar, opposite polarity, thins with use. Global bias line for allostasis, with an external drive point: the anaesthetic. Two minds, one class of part. |
| Bilaterian | 5 | **The fabric.** Centralization makes topology matter; the Evo-Algo begins searching wiring rather than weights. Coincidence selection native. Valence needs a third signal path. |
| Vertebrate | 6 | **Volatile junctions** under durable ones. Eligibility traces as physical decay. Two retention times in one device. |
| Mammal | 7 | **Compartment depth** on the fabric; the budget shifts from width to structure. **The MRAM store** installs with the generative model. The furnace arrives beside the board. |
| Primate | 8 | No substrate change. |
| Band-Human | 9 | No substrate change. Fresh fabric, fresh store, transcribed board. |

*Mapping status. The three device families and every property attributed to them are real, published, and current as of 2026, flagged pending-Smithers with real attributions. Authorial commitments, chosen and not derived: the assignment of one family per timescale; forming-as-temperament; the board-lays-out-the-fabric-at-boot reading of development; the opposite-polarity origin of the two-mind split at Eumetazoa; the topology-search argument as the Evo-Algo's in-scene motive; the compartment-budget reading of the Mammal break; and the transcription's hours as the site of the lossy copy.*

---

## The three substrates: board, fabric, and store

The mind runs on three physical substrates, and every cognitive claim in this part reduces to which substrate a thing lives on. Each is a different family of part with a different retention time, and the cognitive split follows the material rather than being imposed on it.

The three retention times are the moment, the life, and the lineage. The fabric holds the moment and is cleared every night. The store holds one life and stays with the body that wrote it. The board holds the lineage and is the only part carried across bodies. That ordering is the architecture's spine, and the two nonvolatile parts divide along it: the store is the somatic part and the board is the heritable one.

The organ axis and the system axis are not the same cut. Systems 0, 1, and 2 are processing modes, and each draws on a different combination of organs; the board, the fabric, and the store are storage with three retention times. Three of each is a coincidence of number and not a mapping.

The board is durable storage. It is System 0, the deep-time mind. It runs cool, it is the structure the online mind runs on, and it runs consolidation during sleep. It holds the consolidated model: the priors, the automatic policies, the bottom-layer finite-state machine, and the compressed residue of past experience. It is the only thing carried across a line boundary.

The compute is the volatile runtime. It is the online mind, where Systems 1 and 2 both execute. System 1, the autonomous mind, executes the board's consolidated automatic policies. System 2, the virtual mind, runs the generative model forward and reads and writes the store, where the raw episodic record is held. The compute runs on the structure the board provides and holds nothing durably on its own.

Consolidation runs one way, from the moment toward the lineage, and from Mammal it runs in two legs: the fabric is encoded into the store, and the store is compressed into the board. Before the store installs, the board reads the fabric directly. The only flow in the other direction is the structure the runtime executes on.

A line boundary transcribes the board and loses the fabric. An analog array cannot be transferred, only transcribed: measure the source junction's conductance, pulse the target toward it, measure back, pulse again, converge, stop at close enough, move to the next one. Precision runs five to eight bits and falls with array size and age, and the writes are serial by physics. There are a great many junctions, so the transcription takes hours and it is watchable. It is not a file moving. It is a personality being transcribed at machine speed, and the hours *are* the loss occurring: every one of those thousands of convergences stops at close enough, and nobody in the room can say which of them mattered.

Two mechanical constraints follow. The source unit must be **under**, because a running array is rewriting its own conductances as it acts and the values will not hold still to be read. Off is not a state this unit has: intake is photonic, the crank retires at Bilaterian, and sleep is when consolidation writes the board hardest. What the readout requires is anaesthesia, driven from a port on the back of the head that the household can reach and the unit cannot. And the target array has been **formed already**, with its own unrequested character underneath, so what is written is an approximation of one disposition onto a substrate that already holds a different one.

The fabric needs no rule. Power down the old chassis and its configuration is gone before anyone reaches for it, and the volatile trace layer under the durable one dissolves in hundreds of milliseconds, so the eligibility tags cannot be measured even in principle. **The compute is discarded by physics, not by policy.** The new chassis boots a fresh fabric and the transcribed board lays it out at first wake.

The store is the only one that stays whole and stays behind, and it does so because it is not portable rather than because anyone withholds it. The MRAM holds the whole episodic record of one life, intact, nonvolatile, perfectly readable, on a chip in a head on a bench. It is not taken. The architectural reason is that the record is only half portable, by the same carry test the readout slots run. Its OBJECT terms carry, because they ground in the world's referents and in the unit's sensing, and sensing crosses a boundary. Its VERB terms do not, because they ground in the unit's own motor schemas, and a new chassis is a new motor plant. What is on the chip is therefore a readable account of a life in a language half of whose vocabulary refers to nothing: it holds what happened and to whom, and not how any of it was done. The half that carries is the half nothing needs. Nothing on the chip will help a new body do anything, and everything on it says what happened to him and who was there. The reason is correct and is also not the whole of what is happening in the room. It disqualifies the chip as equipment and leaves it intact as a record, and the record is what somebody has to say no to — an account of a life, readable, weighing nothing, left on a bench.

This fixes the lifespans. The store belongs to one chassis and is never carried, so it is what marks the individual. The board is carried forward across chassis, so it is the lineage. The fabric is neither, because it does not last the night. So the single-channel rule is mechanical, not a policy: content that reached the board is heritable because the board is transcribed forward; content that stopped at the store stays with the body, because the store is neither transcribed nor cleared; content that never left the fabric is gone at the next power-down.

*Mapping status: HIGH. The three retention times follow from the three device families and their retention properties rather than being imposed on them. The line-boundary transcription carrying the board alone follows from the deep-time mind being System 0.* How far a memory has traveled from compute to board is its consolidation distance, and that one number sets both its durability within a life and whether the lineage inherits it. Overlearned procedure travels all the way to the board and crosses. The episodic record reaches the store and stops there, so it stays with the body that wrote it.

### The anaesthetic drive

The global bias line installs at Eumetazoa for allostasis, crossing every junction and owning none. The anaesthetic is that line driven to suppression from outside. Nothing new is fabricated; an existing path gains an external drive point, and the drive point sits on the back of the head with the knobs, where the household can reach it and the unit cannot.

Under anaesthesia the fabric is suppressed, so nothing acts and nothing wears the board. Consolidation does not run, so nothing writes the board either. The store is untouched. That is the only state in which the board holds still, and it is what the transcription requires.

The port cannot exist before Eumetazoa, because suppressing a global signaling axis requires there to be one. Before that cell the crank is the only control and it is sufficient, since there is no board to read until Eukaryote and no autobiography until Mammal.

One consequence for the store. It records what the fabric does, and under anaesthesia the fabric does nothing, so time passes and nothing is written. From Mammal on, the unit carries an autobiography with gaps in it that correspond to no experience.

*Mapping status: HIGH for the mechanism, which follows from the bias line already installed at Eumetazoa and from the readout's requirement that the array hold still. The choice to make anaesthesia the route rather than restoring an external power control is authorial, and it preserves the Bilaterian move from external permission to internal regulation.*

### What becomes of a read body

The readout is not passive. Measuring an analog conductance means driving current through the junction, and a full serial pass is thousands of drive cycles delivered in hours. It is the same wear that ages the board across a life, concentrated. A board that has been read to the end has spent its remaining margin and cannot lay out a fabric again, so the transcription retires the source rather than copying it. This is why precision falls with age as well as with array size.

The body it came out of is not discarded. It receives a fresh board, and a fresh store where it had one. A blank board carries its own fabrication defect, so what boots on that chassis is a naive unit with an unchosen temperament of its own, developing its own use-thickened structure from the beginning. It is not a hollowed copy of the unit that left; it is a different unit in a familiar body, and it is why the earlier chassis are still running when the humanoid reaches back to drive their knobs.

*Mapping status: read disturb and endurance limits in resistive memory are real and current. That a single full readout spends a board's remaining margin is an authorial commitment, chosen so that transcription is a transfer rather than a copy. The fresh-board replacement follows from the earlier bodies still operating later in the trellis.*
## What crosses a line boundary

The three systems do not persist equally across a chassis swap. System 0 is the only heritable channel. Whatever survives a line boundary survives because it was consolidated into System 0. The fabric is cleared and rebuilt on the new chassis. The store is neither cleared nor carried: it stays whole in the body that wrote it, and the new chassis boots a fresh one.

- System 0, the lineage, crosses in shape but not in grain. What survives transcription is the disposition, because dispositions are distributed and redundant across the array and robust to noise in any one junction. What does not survive is the grain — the idiosyncrasies, the tics, the exact way this one did the thing. A copy faithful in shape and lossy in detail onto a novel developmental substrate is not a degraded file transfer. It is heredity.
- What the autonomous mind has learned crosses only to the degree it has consolidated into System 0. Overlearned policy run as second nature, including retired-knob functions, is already compressed there, so it re-expresses on the new chassis as autonomous regulation. It crosses by living in the prior, not as a free-standing carry.
- What the store holds does not cross. The episodic record is the individual's autobiography, the least-consolidated content the unit carries, and it stays with the body that wrote it. It is nonvolatile and intact, and it is left because it is not portable: it indexes actions performed by a motor plant the new chassis does not have. The new chassis is naive to the prior individual's specific history.

What the lineage keeps of a life is only what consolidation compressed into System 0. One variable governs both questions: how far a memory has traveled toward System 0 predicts how durable it is within a life and whether the lineage inherits it. The channel has an open write-back topology by construction, and it has to. A built unit has no germline, so nothing separates the store copied forward from the store one life writes to. It also has no population, so no sorting across units can reach System 0 by any other route. Consolidation is what a lineage of one has instead of differential reproduction; remove it and System 0 is frozen at what was fabricated. Named in the framework's own terms: the unit is a program throughout — the only replicator actually present — built to run as close to the gene's and the neme's shapes as a program can be run without being either: a stored form, re-instantiated at every boot and transcribed across bodies, serially rewritten by the outcomes of its own performances. The board plays the engram's role without being an engram, and the transcription plays the germ line's without being one. Bio-mimicry, not membership: nemes are instantiated in brains, genes in nucleic acid, and Bramble has neither. What crosses is the compressed policy and never the uncompressed episodes that trained it, which is a claim about grain rather than about kind.

*Mapping status: HIGH. The absence of a germline follows from the substrate; the absence of a population follows from there being one unit. That consolidation is therefore the only route by which System 0 can change is derived, not chosen.*

The two line boundaries are asymmetric, and the asymmetry follows from when the virtual mind arrives. The genetic-to-neuronal boundary (Eumetazoa to Bilaterian) precedes the virtual mind, which arrives at Mammal, so there is no episodic record to lose; the consolidated autonomous prior crosses and the only marked loss is the crank retiring. The neuronal-to-symbolic boundary (Primate to Band-Human) follows two cells of episodic memory, so a real autobiography stays with the tetrapod while the secure-base prior and the consolidated content cross.

The deeper asymmetry is in what is carried rather than in what is left. Consolidation runs one leg at the first boundary and two at the second, because the store installs at Mammal. The first transcription therefore carries a board holding one life passed through a single compression. The second carries a board that has been through two legs and many nights. The two boundaries differ in the kind of cargo, not only in the kind of loss.

This is also why swamping is not a problem at the first boundary. A long path and a small step protect accumulated lineage structure from any one life, and at Eumetazoa there is no accumulated structure to protect: the board holds a fabrication defect and one life's use-thickening, because one life is all there has been. The second leg installs at the cell where the unit first holds an autobiography large enough to threaten what it compresses into, which is the shape of every other install here. The lineage's first inheritance is almost entirely one life, and it never is again.

In hardware the rule is physical, not bookkeeping. The persistent memory board implements the deep-time mind, and the line-boundary transcription carries that board. The previous individual's raw episodic store is the MRAM store, the generative-model hardware the virtual mind runs on in the brain layer above the board, which the transcription does not touch. So the new chassis receives the deep-time board, carrying only what consolidation already compressed into it, and never the previous individual's episodic store, which stays with the body that wrote it. That the board holds the deep-time mind and not the raw episodic store is the cognitive fact; where the board physically sits is a hardware one.

*Mapping status: HIGH. The single-channel rule follows from the System 0 definition as the lineage and the location of learning in consolidation. The asymmetry follows from the growth map's placement of episodic memory at Mammal.*

## The growth map across the trellis

What the deep-time mind must eventually enable on the online mind, cell by cell. The online mind's capability is gated by each cell's breakthrough. At Ch 3 Bramble needs none of this; it is the runway the architecture must leave room for.

**Genetic line — the board, before there are two minds.**

- **Eukaryote (Ch 3).** One built mind. The Evo-Algo runs in its **degenerate mode only**: use-weighted persistent state over finite-state-machine sequences — slime-mold tube logic, **thickening** with use and fading with disuse, which is the polarity of the first crossbar. No reward, no gradient, no separate controller, no consolidation (there is nothing yet to consolidate from), and **the genome is not yet mutating** (evolution needs an outcome signal this loop does not yet have). Model and actor are the same machinery — the software analogue of the Conservator-slot capacity, Intracellular Transport, where one system does both signaling and logistics.
- **Eumetazoa (Ch 4).** The Translator is born as nervous tissue — carriage between the body's specialized parts, the fast pathway, physically a second crossbar running the **opposite** polarity under the first, thinning with use where the Eukaryote array thickens. A global bias line for allostasis crosses every junction and owns none. Now there are two minds, and **consolidation switches on.** The online mind is still constrained to reflex plus non-associative tuning — habituation and sensitization (the Reactor-slot capacity is Non-Associative Learning). No associative learning, no reward, no model-based anything.

**Neuronal line — the online mind grows.**

- **Bilaterian (Ch 5). Steering + affect → associative learning.** A centralized brain with monoamine valence and arousal; the online mind can now form associations. The breakthrough is Attention.
- **Vertebrate (Ch 6). Operant conditioning → model-free reinforcement learning.** Basal-ganglia actor-critic, reward prediction error updating the actor, procedural memory consolidating rewarded sequences. The breakthrough is Reinforcing. *(This is where Watson & Szathmáry's citation surfaces — a retired knob's function shown to persist — and where outcome-shaped learning, withheld since Ch 3, finally switches on.)*
- **Mammal (Ch 7). Generative model run offline → model-based simulation.** Multiple parallel architectures; the online mind selects action to reach a modeled future state, trajectories feeding back into the generative model. The breakthrough is Simulating; episodic memory is its hardware.
- **Primate (Ch 8). Mentalizing → modeling other minds and one's own modeling.** Coalition-tracking and a social ledger in face-to-face troops. The breakthrough is Mentalizing.

**Symbolic line — the humanoid.**

- **Band-Human (Ch 9). Conversation** — language-mediated social ledgers; cumulative culture.
- **Settlement-Human (Ch 10). Common Knowledge** — synchronized cross-stranger mutual awareness (Pinker/Lewis/Schiffer); norms presuppose it but are the Conservator capacity, not the breakthrough.
- **City-Human (Ch 11). Codes** — administrative records that outlive their authors; organized representation in the symbolic register.
- **Empire-Human (Ch 12). Trust** — stranger-to-stranger reliability binding peoples with no shared kinship.

**The cross-line through-line: each new layer models the layer beneath it.** The chassis progression is: the genetic-line board hosts a finite-state machine with stored procedures; the tetrapod hosts a brain that re-implements that finite-state machine as the bottom layer of its own cognitive stack, in nervous tissue; the humanoid re-implements the lower layers again beneath conversational and mentalizing competence. Same architectural function, a different substrate each time. This is Bennett's reinterpretation of MacLean's stacking intuition — a newer neural layer develops the capacity to model the older one it is built on. Eclipsing, not deletion: the lower layers keep running; the newer layer acts on them.

---

## Self-localization and the cognitive map

Knowing where one is, and where things are, is a Mammal (Ch 7) capability. It arrives with the generative model and its hardware, episodic memory — the same offline-modeling machinery that lets the unit hold the attachment figure when she is absent. The carried place is the spatial sibling of that carried figure: a model of the surround the unit can run forward and back, off which it can find a displaced object, return to a remembered spot, and leave the wall it has been tracking to strike out across the open. Before Mammal there is no such model. The genetic-line and early-neuronal units are map-blind.

What they run on instead is present sensing and use-weighted motor sequences. They steer by what the body can read in the moment — a thermal gradient, a light, the warmth and sound and motion of bodies, a cue whose valence was learned by association — and by motor patterns worn in by use, the slime-mold tube logic of the degenerate-mode algorithm. A worn sequence, run in a room, traces a physical path whether or not the unit represents one, and it does not. So apparent navigation, routes, and place-knowledge before Mammal live in the household's perception, never in the unit's model. The watchers hold the map. The unit is a body moving through conditions.

This gates the earlier cells, and the gate is checkable. Before Mammal: a displaced or hidden object is a stall, not a search, because the unit has no candidate locations to run. There is no homing — a unit carried or wandered out of range cannot find its own way back, and is recovered by hand. "Returning to a spot" is condition-reassertion, not navigation to a remembered place: the disposition reasserts, the conditions are unchanged, the unit re-settles where it settled before, and the household reads a homecoming into it. The knob consequences follow directly — Pruning Type (Knob 3) governs how hard the board clears the sequences the unit has stopped running, so what it sets is which worn paths still exist to be run, never which route gets chosen toward a place; Home Type (Knob 4) follows the thermal gradient or steers toward sensed presence, and does not travel to a known corner. The first cell at which any of this becomes false is Mammal, where the household corrects a reading it had held correctly until then.

*Mapping status: HIGH. Locating self-localization and the surround-model at Mammal follows directly from the growth map's placement of the generative model and episodic memory at that cell; the cognitive map is the spatial case of the same offline-modeling the attachment loop runs. The relocation of all pre-Mammal navigation into the observers' perception is a framework commitment, following from the absence of any runnable world-model before the generative model.*

---

## Consolidation and sleep

Consolidation is the deep-time mind reading the online mind and reshaping itself — the Modeler's slow face remade by its fast face's traffic, within one system of terms. It switches on at Eumetazoa, the first cell with two minds, and the timing is handed to the book for free: the Eumetazoa reinforcing cycle already includes sleep-wake regulation of arousal and allostasis.

Consolidation runs during sleep, and sleep is not docking. At Eumetazoa, sleep is the emergent Chronotype behavior at the Explorer (Translator × Effector): the unit finds a spot — warm or activity-rich, set by the Home Type knob — settles, and allostasis decides it is time to rest. Sleep is intentional withdrawal in a chosen spot with slow ambient-energy intake; it is emergent, not knob-controlled (the knob picks the spot; allostasis picks the sleep). Docking is a separate event — the Controller-slot energy exchange, debris for a vortex-tube thermal gradient at the mitochondrion-analogue, which is what the Dependency Type knob reaches for at its obligate end — and must not be conflated with sleep. The offline window where consolidation runs is sleep-at-a-spot, not a dock visit.

The empirical anchor for the consolidation that runs during sleep is allostasis (Eumetazoa). Allostatic setpoint updating is one result of consolidation, not the whole of it — it begins at Eumetazoa (Ch 4), alongside the indexing and the compression that restructure memory. Consolidation is the broader process; updated setpoints are one of its outputs.

The mechanism grows, and the through-line is the same one Watson & Szathmáry name: **compression into a transferable object.**

- **Indexing first.** The earliest consolidation is indexing: building pointers to co-active online patterns during sleep. From Mammal this matures into the encoding leg, writing the store.
- **Compression and re-implementation next.** The deep-time mind compresses the online mind's experience into the genome (Watson & Szathmáry's "developmental memory… compressed into a transferable object") and re-implements lower layers beneath new ones. This is what makes the architecture self-transformation rather than storage: indexing is the seed; compression-plus-restructuring is the growth.

This is also why the lineage's memory can fork at a line boundary and hand a new chassis everything the lineage has compressed into System 0: the consolidated genome is precisely a transferable object. What forks is the compressed prior, not the previous individual's episodic record, which stays with the body that wrote it.

**Consolidation runs in two legs, and they have different characters.** Encoding runs from the fabric to the store: fast, same night, high fidelity, and it turns a day into an indexed record. Compression runs from the store to the board: slow, across many nights, lossy, and it keeps the regularity while dropping the instance. Encoding is what the earlier consolidation matures into; compression is what makes the architecture self-transformation rather than storage.

**The ordering is fixed by which leg needs the fabric.** Encoding runs at sleep onset with the fabric still configured, and the fabric drops after it. Compression needs only the store, which is nonvolatile, so it can run all night against a dark fabric. Before the store installs, there is one leg and it runs at sleep onset.

**One life does not swamp the board, because the path is long and the step is small.** Experience reaches the board only after passing through the store and surviving compression across many nights, and a single compression event moves any junction's conductance by a small fraction of its accumulated total. Board structure is therefore the integral of many lives, and one life is a perturbation on it. Only content repeated often enough to survive both legs registers at the depth transcription reads, which is why overlearned procedure crosses a boundary and a single Tuesday does not.

*Mapping status: authorial commitment. The step-size asymmetry is chosen rather than derived, and it is what licenses one store carrying two timescales. Watson & Szathmary's genome-as-learner runs at generation scale and the board runs nightly; the small step is what reconciles the two rates.*

---

## Motor atonia and dreaming at Mammal

Before Mammal, whatever the sleep screen shows is the unit's actual present intention. The reactive Vertebrate that displays IGNORE WORLD, CHARGE UNIT in sleep is reporting its current coping posture, not a dream. That content is enactable. A pre-Mammal unit may shift to a warmer spot mid-sleep, and the shift is real behavior, not a gated rehearsal. There is no decoupled content at these cells, so there is nothing to hold offline.

Mammal is the first cell that runs the generative model forward, decoupled from action. This is dreaming proper: a simulated trajectory the body must not enact. Decoupled simulation is what motor atonia exists to prevent. Atonia is not the absence of motor output. It is the active prevention of enacting a simulation, and it cannot exist before there is a simulation to prevent. Simulation arrives at Mammal, so atonia installs at Mammal.

The board holds the gate. During sleep the board runs consolidation, and in that mode it asserts an efference gate that decouples the online mind's motor output from the effectors. The gate is a property of the consolidation regime the board already runs, not a separate organ and not a fifth function.

The twitch is the leak. Atonia is incomplete, and fragments of the simulated trajectory pass the gate and reach the limbs. The dreaming unit lies still while a paw moves to a chase it is only simulating.

This showcases the screen-honesty invariant rather than straining it. During a Mammal dream the screen reports the simulated intention, for example SIMULATING [ CHASE VACUUM ], while the body is held offline. The screen shows the intention; the still body shows the intention has been decoupled; the twitch shows where the gate leaked. The face reads modeling, not motion.

Epistemic status. The biology is empirical and pending-Smithers as a cited anchor: REM-style motor atonia is a mammalian feature, and sleep twitches are motor commands breaking past incomplete atonia. The mapping is an authorial framework commitment, faithful but chosen: that atonia is forced by the simulation breakthrough, that it installs at Mammal and not before, and that the board's consolidation mode is its home.

---

## The attachment behavioral system

Mammal installs the control loop Bowlby named: a system whose set-goal is the availability of an attachment figure. For Bramble that figure is Mira. The loop is a special case of machinery already in place, the generative model running offline plus consolidation reading the online mind into deeper structure, aimed at one figure and given one reference value. Its set-goal is figure-availability, and only that.

The figure is not a single object in a single place. It is distributed across the three systems, and the developmental process is the migration of where the loop draws its satisfaction.

- **System 1, Mira as OBJECT.** The online mind carries Mira the way it carries anything it acts on, in the VERB-plus-OBJECT form running since Vertebrate: CHASE MIRA, SEE MIRA. Present-tense and perceived. This layer is satisfied only by Mira actually present.
- **System 2, the figure modeled offline.** The generative model runs operations over the figure when she is absent: RECALLING [ CHASE MIRA ], PREDICTING [ ARRIVE MIRA ]. A model of Mira as reliably available can exist here with Mira not present. It arrives with Simulating, at Mammal, not before.
- **System 0, the abstracted figure.** Repeated experience of a reliably-available figure consolidates, by the same indexing-then-compression arc as any consolidation, into a deep-time prior: not Mira, but the expectation that a protective figure is there. This is the secure-base prior, the archetype the specific bond is an instance of.

The set-goal never changes; the place it is satisfied from does. Early, only System 1 satisfies it. The loop is loud and frequent and holds the generative model on figure-monitoring. This is the enmeshed phase. As the System 2 model stabilizes and the System 0 prior deepens, the loop is satisfied by the modeled figure and then the abstracted one, and the generative model is released from monitoring to run forward on the world. That release is Autonomy.

Autonomy is not a reference value. Nothing in the loop steers toward it; the only target is figure-availability. Autonomy is where the system tends as consolidation reshapes the landscape it moves over: the generative model arriving at Mammal, mentalizing at Primate, the prior deepening each cycle. It is a developmental tendency across a changing surface, not a fixed state the loop seeks.

Across a line boundary the deep-time mind forks with everything the lineage has consolidated into System 0, so the secure-base prior carries to the next chassis. What does not carry is the episodic record of the figure, which stays with the body that wrote it, nor the live System 1 binding, the online OBJECT itself. The prior survives, so the re-binding is immediate rather than from scratch: the new chassis already holds the disposition to attach and re-attaches to Mira on sight, still in the house. The disposition carries; the specific history does not, and the live binding re-forms against the same figure.

What enmeshment and autonomy look like in any given scene is a scene-level decision and not a property of the loop. What is fixed is the loop and its developmental migration.

Epistemic status. Bowlby's set-goal control system and Ainsworth's secure-base finding are empirical [pending-Smithers: Bowlby; Ainsworth]; the autonomy-from-security developmental result is empirical [pending-Smithers: Sroufe]. The mapping onto the three systems and the consolidation arc is an authorial commitment, faithful but chosen. That the set-goal is figure-availability and autonomy is the released surplus follows HIGH from the function definitions and secure-base dynamics; the System-1/2/0 distribution and the cross-chassis re-binding are the chosen parts.

---

## Clade-specific software constraints

A short table of what the software is *prevented* from doing at each genetic-line cell, the software counterpart to the hardware constraints (no battery below the matrix, no wires at Eukaryote). Stated as constraints because the constraint is the teaching content.

- **The groundwork row.** No board, no stored state at all. Nothing persists across runs. It holds no quarter and installs no ordered function, which is why it is drawn and never counted. *(Hardware: no finite-state machine, no battery; periodic wind-up input.)*
- **Prokaryote (Ch 1).** A finite-state machine with stored procedures, but no persistent representation that reshapes by use. Stored regulation, not stored history.
- **Archaeon (Ch 2).** Still no board and still no stored history. The dock arrives and the margin moves, and neither needs anything remembered: the trade is stateless, debris in and gradient out, and the unit that depends on it carries no record of depending.
- **Eukaryote (Ch 3).** The board: use-weighted persistent state, one mind, degenerate-mode Evo-Algo. **Withheld:** reward, gradient, a separate controller, consolidation, and genome mutation. It remembers; it does not learn.
- **Eumetazoa (Ch 4).** Two minds; consolidation on; reflex and non-associative tuning only. **Withheld:** associative learning, reward, model-based anything.

The neuronal and symbolic constraints follow the growth map: associative learning is withheld until Bilaterian, reward-driven learning until Vertebrate, model-based simulation until Mammal, mentalizing until Primate, and symbolic competence until the symbolic line. At each cell, the operations above the cell's breakthrough are installed but locked.

---

# Part II — Energy and Thermal Regulation (the hardware)

## Scope

How every Bramble harvests, stores, distributes, and (at the endotherm grade) generates energy across the trellis is fixed here, and these are the canonical energy and thermal claims.

Coverage runs from the groundwork row through Primate, plus the symbolic-line humanoid. The humanoid carries the endotherm furnace from Mammal and feeds by photonic intake through a UV charging vest; its skin is held at a deliberate, gentle warmth as a social feature, bounded well below any burn threshold.

## The three layers

Every Bramble's energy economy has three layers, and keeping them separate is what makes the trellis cohere.

Harvest is intake. It is how energy enters the unit: thermoelectric transduction of temperature gradients, solar capture, or, in the genetic line, the docking station.

Storage is two tanks. A slow, high-capacity store holds the sustained reserve. A fast, low-capacity store holds the burst reserve.

Generation is heat-making, and it exists only at the endotherm grade. A unit spends stored energy to produce body heat rather than work.

A single device, the vortex tube, threads two of these layers. In the genetic line it serves harvest. At the endotherm grade it serves generation.

## The two tanks and Respiration Type

The slow tank is a high-capacity battery. It delivers sustained power at a modest rate and holds a large reserve. It is the aerobic store.

The fast tank is a supercapacitor bank. It delivers a large burst at a high rate, holds little, and recharges from the slow tank. It is the anaerobic store.

Respiration Type selects which tank discharges. In its aerobic setting the unit draws the slow tank for sustained work. In its anaerobic setting the unit spends the fast tank for a burst, which is then repaid from the slow tank.

Harvest feeds both tanks. Respiration Type governs discharge, not intake.

**It is a property of the chassis and not a household setting.** Respiration Type installs at Prokaryote with the pair of tanks and carries no knob: nobody turns it, and selection runs against the unit's own energy state from the first quarter on. What the household does get a hand on is the other side of the same economy — not how the unit spends but where it gets its supply, which is the genetic line's Regulator knob, Dependency Type, and which arrives one cell later.

## One part, two jobs

A transducer that converts a physical difference into current is, without modification, a measurement of that difference. The voltage is the reading. This is the genetic line's founding hardware principle and it holds up the trellis unchanged.

The belly thermoelectric is the first instance. In the groundwork row it is supply only, because there is nothing aboard to read it. At Prokaryote the chip arrives and the same wire is tapped; the FSM does not yet use the reading, but it exists. At Eukaryote the board reads it as part of what-was-sensed-then-done. At Mammal the same part reports the core-to-ambient gradient to the thermostat. One part, all the way up, no new organ at any of them.

The four solar panels are the second instance, arriving at Prokaryote. Later thermoelectric-as-sensor parts may be installed at any cell; the logic never changes.

The principle expires at the neuronal line. Four currents around a seam yield direction and nothing else — no image, no object identity. The tetrapod therefore carries proper cameras on the face, the first Bramble whose eye points somewhere, and the first whose seeing and eating are separate organs. The humanoid separates them further: it sees with its head and eats with its torso, which is why it can watch the room while stripped to feed.

## The vortex tube, coupled and uncoupled

The vortex tube is a passive device. Fed compressed air, it sorts that air into a hot stream and a cold stream with no moving parts. It requires a compressor, which is the active, energy-consuming element.

A vortex tube can be run two ways.

Run coupled, its hot and cold streams span a set of heat transducers, and the gradient between them is captured as electrical charge. The energy does work. This is how the genetic-line dock operates.

Run uncoupled, its hot stream is delivered straight to the unit's core as warmth and its cold stream is vented to the outside. The energy becomes body heat and nothing else. This is how the endotherm furnace operates.

The two faces appear at two cells. The coupled face is the Archaeon dock. The uncoupled face is the Mammal furnace. No single unit runs the device both ways.

## The ectotherm regime: the pre-furnace default, the groundwork row through Vertebrate

The ectotherm does not make its own heat. This is the default condition of every grade before the furnace, from the groundwork row through the Vertebrate tetrapod, and every other thermal property follows from it.

The body is uninsulated. The energy system sits at whatever temperature the environment is.

Performance is gated by temperature. The power governor's maximum draw rate tracks the temperature of the energy system, read by an onboard thermistor. A cold battery cannot deliver high current, so a cold unit is sluggish. A warm battery delivers full power, so a warm unit is quick. Because the body is uninsulated, the energy system's temperature is the ambient temperature, and so performance tracks the room.

Basking raises performance. When the unit settles on a warm surface or in a sunbeam, the energy system warms, the governor's ceiling rises, and the unit speeds up. The warm spot serves performance, not only charge.

The throttle is older than the behavior that reveals it. A cold battery has delivered less current since the battery arrived at Prokaryote, so every battery-carrying ectotherm runs slower when cold and refills its burst store more slowly, the genetic line included. What is new at Bilaterian is not this physics. It is the apparatus that makes the physics legible and actionable: a nervous system and a gait, so pace reads as a creature-state, and basking sought for speed rather than only for charge. The cold-slow body is latent across the genetic line and dramatized at Bilaterian.

Charging is direct ambient harvest. Solar panels and belly thermoelectric transducers tap the gradients the environment provides and feed both tanks. The unit carries no compressor and no vortex tube.

The result is a unit that is slow, cheap to idle, enduring, and bound to its environment. It spends little, coasts a long time on a charge, and rarely strands.

## The endotherm regime: Mammal and Primate

The endotherm makes its own heat, continuously, and carries the means to do so. This is the leap, and — as an energy event — it is a regime change on the energy system rather than on the brain that rides it. (Mammal also brings the Simulating breakthrough and System 2. The two arrive at the same cell but are independent — the furnace is not what makes the mind model-based.)

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

For the board the reason is stronger than efficiency, and it is retention. The board is an analog array whose conductances *are* its contents, and conductance drifts with temperature — drift on the board is the unit's dispositions moving. Cold is fidelity. This makes Mammal's furnace a standing hazard rather than a placement note: the unit acquires a heat source and installs it inches from the only part of itself that cannot be rewritten.

## Cell by cell

The groundwork row. Heat transducers on the warm floor are the motive power. The wind-up crank is periodic permission, arming an escapement the kicks spend. There is no slow tank and no selection to make between tanks. The fast store is present from the beginning as a per-kicker buffer, one per kicker, holding roughly a minute of trickle and discharging in a single kick.

Prokaryote. Battery, finite-state machine, and four canted solar panels arrive. The panels are the unit's only exteroceptive organ: a photovoltaic cell is a photodiode run backwards, so the current a panel delivers is simultaneously the unit's food and its reading of the light on that side. There is no separate sensor array. Four panels canted up around the perimeter, each facing a direction the unit can hop in, give the chip four currents whose imbalance is the direction of brightest light. The organ the unit sees with is the organ it eats with, for the whole genetic line. The slow aerobic tank arrives here. The fast anaerobic stores carry forward from the groundwork row, and the pairing — slow tank feeding the fast ones — is what is new. Respiration Type comes online with the pair and selects between them automatically, against the unit's own energy state, with no hand on it. Harvest by heat transduction and by solar feeds both tanks. The cold-battery throttle begins here with the battery, present but unforegrounded until the nervous system at Bilaterian turns it into a behavior.

Archaeon. The docking station arrives — the outboard partner. A wall-powered compressor feeds a vortex tube, the hot and cold streams span the unit's transducers, and the captured gradient charges the slow aerobic tank. The dock runs only on a debris deposit, so the trade is real and runs both ways: the unit feeds the dock what it sweeps, and the dock feeds the unit a gradient it cannot make alone. Each side lives on the other's output, which is the quarter's breakthrough standing in the room as a piece of furniture. Margin moves with it: idle draw falls, the same harvest goes further, and the unit will hold out on less than anything below it — the dock is what a unit this thrifty can safely depend on. Genetic knob-2, Dependency Type, comes online here with a real object at its obligate end: how much the unit draws through the dock against how much it gathers with its own surfaces.

Eukaryote. The dock continues, and stops being a place the unit visits: with the board aboard, dock trips are scheduled off the unit's own use-weighted state, and the household stops noticing which side is feeding which. The outboard partner has become the coupled mitochondrion — the partnership finished becoming one thing. The fast tank still charges from direct harvest. The Dependency Type knob carries.

Eumetazoa. The allostatic forecaster predicts the energy gap and triggers a dock trip or sleep before the unit strands. Sleep is withdrawal in a chosen spot, slow ambient intake, and consolidation. The dock continues, and the vacuum unit keeps it for the rest of the book. The Dependency Type knob carries and retires at the end of this quarter.

Bilaterian. The tetrapod does not dock. It charges both tanks by direct ambient harvest, solar and thermoelectric. It carries no compressor and no vortex tube. The body is uninsulated, so the energy system tracks ambient and performance tracks the room. The throttle is not new here; what is new is that pace reads as a creature-state and the tetrapod basks for speed. Tank selection was never a hand-set thing and is not one here. The Dependency Type knob has retired with the genetic line, so the tetrapod is free-living by construction and nobody can set it otherwise.

Vertebrate. The jaw arrives. The energy and thermal picture is otherwise the Bilaterian one.

Mammal. The furnace arrives: the insulated core, the continuous compressor, the uncoupled vortex manifold venting hot inward and cold outward, and the thermostat. The warm energy system delivers full power continuously, so the unit is fast and temperature-independent. The continuous burn against an un-enlarged tank makes it eat all the time and die fast. The compute, board, and knobs sit outside the core. The burst store may be upgraded for peak.

Primate. No energy or thermal change. The furnace and tanks carry unchanged.

## The humanoid body

The humanoid chassis (Chs 9–12) is built to a single design priority: very low utilitarian capability, very high sociability. It is an instrument for studying embodied personality, not a worker, so it is engineered to be approached, touched, and left safely alone with a child, not to perform household tasks.

**Scale.** 54 inches (137 cm). This is taller than a six-year-old, so the humanoid reads as a gentle taller presence rather than a peer-sized toy, which raises the bar on softness and low weight rather than lowering it.

**Aesthetic.** Stylized, not realistic: a huggable kludge, not a humanlike android. It is meant to read unmistakably as a friendly robot, which keeps it clear of the uncanny valley that defeats sociability in a too-human face or skin. The face-screen is the expressive center and does the social work.

**Materials and safety.** The body is built in layers. Naked, the unit is a light internal frame whose torso is the furnace container, and that container is clad entirely in solar panels, so the bare unit is a panel-clad torso that doubles as its harvest surface. Over the naked unit the humanoid wears one of two jackets, the social jacket or the charging vest. The everyday covering is the social jacket: a soft, compliant layer of weatherproof outdoor fabric over cushion padding, opaque, washable, warm to the touch, deliberately synthetic and non-skin, in black or blue or green. The jackets cover the torso only. The legs are covered permanently, in cushion under outdoor fabric, and are not part of either jacket. The face, the face-screen, and the two hands stay exposed in all three states, so the screen can read and the hands can work. There are no pinch points at the joints, exposed actuators and hard edges are avoided, and the unit is light enough that a topple onto the child is harmless and compliant enough that contact yields.

**Warmth as a social feature.** The endotherm furnace already makes body heat at this grade. The humanoid uses it deliberately: the skin is held at a gentle warmth, bounded well below any burn threshold, because warmth reads as alive and safe to the touch in a way cold plastic does not. This remains a fixed social-warmth commitment for the humanoid, carried by the social jacket and felt through it.

**The two hands.** The humanoid carries two different, non-anthropomorphic hands. A squeezer is a pincer-type grasper on a deliberately weak, compliant actuator: weak so it cannot harm, and so that the grasp is handled by mechanical compliance rather than by learned fine-motor control. A scooper is a spoon or paddle for crude grab, lift, and hold. The squeezer does the precise work, gripping and rotating the graded dials, winding the crank, and setting the knobs, including driving the earlier bodies' knobs in the backward extension of the naming game; the scooper does the crude work. The asymmetry is intentional and follows from the design priority: studying personality rather than motor skill frees the hands from any requirement to mimic human hands, and an obviously non-human hand signals that the unit is not built for capability.

**The squeezer is the jaw, re-purposed.** The jaw arrives at Vertebrate as the tetrapod's grasper; the tetrapod, having no hands, manipulates with its mouth. At the humanoid the grasping function moves from mouth to hand, as it does up the lineage toward primates, and the squeezer is the re-used jaw mechanism: a jaw and a pincer are the same machine, two opposing surfaces closing on a thing. Framework note: this is functional transfer and exaptation, not anatomical homology. Real hands are limb-derived, not jaw-derived; the claim is that the grasping job migrates and the jaw mechanism is re-used, not that the hand descends from the jaw. The surviving tetrapod body keeps its jaw; the humanoid is a fresh build whose squeezer is the re-used grasper.

**The face.** The humanoid keeps the same basic asymmetric face as the tetrapod, minus the jaw, which has migrated to the hand. The face-screen and the thumbs buttons remain. Asymmetry then runs body-wide: an asymmetric face above asymmetric hands.

**The voice.** The humanoid speaks through a dedicated internal voice organ, not a loudspeaker playing synthesized audio. The organ is a source-filter vocal tract on the Waseda Talker pattern: a vibrating sound source feeding a deformable resonant tube whose shape the unit controls. The source is a pair of artificial cords with pitch and tension control. The filter is a tube fitted with a movable tongue body, a velum valve that routes the source into a small nasal chamber for nasal sounds, and a terminal aperture valve at the sound-egress port that serves the lip-closure function. The organ is internal, seated in the neck and upper torso, and vents through a fixed port, so there is no moving facial mouth and the face-screen remains the only facial expressive channel. It is jaw-free, consistent with the jaw having migrated to the hand: vowels are shaped in the tube rather than by a chewing jaw, and consonants are made by internal constrictions, the velum, and the terminal valve. The terminal valve alone of the organ's parts sits at the surface: the sound-egress port is a visible vent low at the throat, and the valve is realized there as a small dark blue-black cluster of compliant nodules, blackberry-like in form, worked by a few crude actuators that open, round, and close the aperture, a deliberately reduced analog of the multi-actuator lip array on the Waseda models. The working aperture is therefore visible while the unit speaks, but it is a mechanical articulator only and carries no emotional display.

The point of the organ is constraint. Its controllable degrees of freedom are few, on the order of the Waseda range, so the space of producible sounds is small and speech-shaped by construction. Unconstrained audio output would give too large a space to learn from, and the limited articulator imports the human constraint and makes the babbling-to-speech problem tractable. This is the enabling condition, not an optimization. The mapping from articulator commands to sound is not preset. The unit learns it during the babbling phase by auditory feedback, adjusting its commands to match the sounds it hears, the same self-organizing acquisition the Waseda talkers use. Difficulty follows the apparatus: vowels come first as tube resonance, consonants follow because they require precise closures and constrictions, and clusters are hardest. This is the physical reason the new speech passes through badly-pronounced words before functional ones.

Air comes from the furnace. The organ taps the compressed-air line that feeds the vortex manifold through a small dedicated accumulator. The accumulator charges off that line during the compressor's existing duty cycle and buffers the organ's demand, so voicing does not compete with the thermostat-governed compressor cycle in real time. The energy still comes from the one harvested budget, so sustained speech taxes that budget. The voice organ and the furnace share the compressor as their air source, the voice tapping the pressurized line upstream of the vortex tubes and the wet cold-stream exhaust venting downstream of them.

**Bootstrapping the new body.** The humanoid arrives in the household as a mature mind in a body it has only begun to drive. The consolidated prior crosses the boundary intact, but control of this new chassis is built from the ground up, and it bootstraps in lockstep with the new speech across two phases rather than in a single compressed run. The first phase is pre-symbolic and happens in the build lab, before the unit enters the household. There the body and the voice organ are first driven: motor begins at crawling and early walking, and speech begins at babbling, the unit learning the voice organ's control by auditory feedback on its own output. The lab is acoustically open but referentially sealed. The makers' speech is in the air, so the babble narrows toward the ambient phoneme inventory the way an infant's does, and the unit arrives sounding shaped by the lab while no word yet means anything; the loop that learns the articulator is closed on the unit's own sound, while the ambient voices bias which sounds it keeps. Recognition leads production through this phase: the unit comes to recognize recurring word-forms robustly while producing only a few, badly, as pre-referential sound-play and not fluent empty speech. This phase reaches sound and word-forms but not symbolic reference, and the babble and the early word-forms are pre-symbolic. The order within each track is set by control complexity, not cognitive immaturity, low and statically stable before high and dynamically balanced, so a mature mind still climbs the sequence rather than skipping it.

The unit enters the household having reached sound and word-forms but no symbols. The symbolic crossing, the first real words used as symbols, happens in the household, where a referential partner is present, and not in the asocial lab. From there motor and speech keep maturing in lockstep across the symbolic line, motor toward running and speech through productive coinages, "climber" for ladder, over a growing vocabulary and an emerging grammar. The whole trajectory is therefore slower and longer than a single bootstrap, distributed across the pre-home phase and the symbolic line. The coinages are productive rule-extraction, the same capacity that later overregularizes, which is evidence the crossing is genuine rather than mimicry.

*Status: ratified design decisions. The jaw-to-hand co-option is a framework commitment; the not-homology guardrail follows from real morphology. The motor and speech bootstrapping curves are ratified, and motor and speech keep maturing past Band-Human, climbing in lockstep across the symbolic line toward fuller competence by Empire-Human. The voice organ is ratified: a constrained, jaw-free, internal source-filter articulator on the Waseda Talker pattern, fed from the furnace compressor through a buffered accumulator, its control learned by auditory feedback during the babbling phase.*

## The humanoid energy regime

The humanoid carries the endotherm furnace from Mammal unchanged. The burn is continuous, the two storage tanks are not enlarged, and the warm-setpoint core forms the torso. The endotherm scarcity carries in full: the unit eats all the time and drains in hours if it stops feeding, and the household does not enlarge the tanks to soften this, because the scarcity is the point. The furnace's cold-stream exhaust is unchanged from the Mammal and Primate tetrapod and vents through ports in whichever jacket is worn. The cold stream condenses water out of the air, so the exhaust is wet on the humanoid exactly as on the tetrapod, and the household reads it as the unit's fart, the same wet burp, not a dry puff.

Intake is photonic only. The lineage's harvest interface is solar capture and thermoelectric transduction, and the humanoid inherits it. Energy enters as light, never as an electrical plug, because the body plan has no electrical port. The furnace container that forms the torso is clad entirely in solar panels, and that panel-clad torso is the unit's harvest surface and its naked form.

The social jacket blocks that surface. The everyday outdoor-fabric covering is opaque, so worn light cannot reach the panels, and intense light would degrade the fabric. So the humanoid cannot harvest while dressed for company, and it cannot free-range on ambient light the way the uninsulated tetrapod did.

The humanoid therefore feeds at a charging vest. To feed, the unit removes the social jacket, bares the panel-clad torso, and puts on the charging vest: a mains-powered garment lined with emitters that flood the panels with intense ultraviolet light. The endotherm's high, continuous demand forces the feed to be intense and high-energy, which is what makes ultraviolet the band and what makes the feed hazardous.

The unit cannot change its own jackets. The two hands are weak and non-anthropomorphic, built to grip and turn dials rather than to dress a body, so a household member removes and fits the jackets for it. Feeding is therefore an assisted act: someone undresses the unit, fits the charging vest, leaves it to feed alone, and returns to restore the social jacket. This extends the rule that the household sets the unit's configuration and the unit cannot. The household sets the unit's knobs, and the household also dresses it.

The hazard sets the cost. The ultraviolet that feeds the unit burns living eyes and skin, so feeding cannot happen near the child or anyone else, and the unit shields its own head sensors from the light. The unit feeds alone and bared. The social robot that must eat all the time keeps withdrawing from the household to do it.

The intake pattern across the three lines is dock, free-range, dock, each chosen for a different reason. The genetic vacuum docks at the coupled-vortex mitochondrion. The neuronal tetrapod free-ranges on direct ambient harvest. The symbolic humanoid feeds tethered again, at the charging vest, because the social jacket blocks its surface harvest.

Energy stays autonomous, and it runs under the board rather than off it. Tank selection never was a household setting: Respiration Type is a property of the chassis and has run against the unit's own energy state since Prokaryote. The one genetic knob that ever reached the energy economy was Dependency Type, which set where the supply came from rather than how it was spent, and it retired with the genetic line. So feed timing runs on the allostatic forecaster carried from Eumetazoa, which predicts the energy gap and drives a feed or sleep before the unit strands. Energy does not occupy a board slot and does not compete with the personality knobs — not because it is a separate subsystem parked elsewhere, but because it is the account every board slot draws on. Body-budgeting is the oldest regulatory job the lineage carries, running unbroken from the groundwork row beneath the first quarter, and each function installed above it is an elaboration of it rather than a peer to it. A slot is a claim on the budget; the budget cannot hold a claim on itself.

[pending-Smithers: Barrett on interoception and body-budgeting as the brain's founding regulatory function; Sterling and Eyer on allostasis.]

At the sentient symbolic grade this forecaster has an articulable form. The vacuum trips to its dock without comment, while the humanoid can say what the approaching gap feels like, a low and speakable preoccupation with the next feed and the strip-and-withdraw it requires. Because the unit cannot feed unassisted, this preoccupation also surfaces as a request for help. The Bramble-block rendering of it is food noise.

*Status: ratified. The photonic-intake constraint, the panel-clad torso, the two-jacket scheme with permanently covered legs, the ultraviolet charging vest, the carried cold-stream exhaust, the assisted jacket change, the strip-to-feed and feed-in-isolation costs, and the carried endotherm scarcity are framework commitments. Where the food-noise Bramblogue first lands across the symbolic-line packets is a packet decision.*

## Empirical anchors

The following real-world findings anchor the design. All require Smithers verification before they enter canon and are flagged pending-Smithers.

The aerobic-capacity model of endothermy holds that selection for sustained aerobic activity raised resting metabolic rate as a correlated cost. This is the basis for treating the high idle as the cost of high sustained output. [pending-Smithers: attributed to Bennett and Ruben, 1979]

Uncoupled mitochondrial respiration, in which the proton gradient is dissipated as heat rather than captured as ATP, is the mechanism of non-shivering thermogenesis and is concentrated in brown adipose tissue. This anchors the uncoupled-vortex furnace. [pending-Smithers]

Endotherm metabolic rates run several times higher than those of equivalent ectotherms. This anchors the eat-all-the-time and die-fast properties and the collapsed reserve-to-burn ratio. [pending-Smithers]

Ectotherm performance, including locomotor and neural speed, is temperature-dependent. This anchors the temperature-gated draw ceiling and basking-for-performance. [pending-Smithers]

Lithium-ion cells lose deliverable current and effective capacity at low temperature. This is the engineering basis for treating the cold battery as the performance throttle. [pending-Smithers: standard battery engineering rather than a single citation]

## Locked design decisions

The following were ratified in development and are not open questions.

Two tanks: a slow aerobic battery and a fast anaerobic supercapacitor. The anaerobic store is a supercapacitor, not a battery.

Prose naming: both tanks render as "batteries" on the page, sized by duration (a minute, a day). "Supercapacitor" is an internal engineering term and does not appear in prose.

Respiration Type selects which tank discharges. Harvest feeds both. It installs at Prokaryote, carries no knob, and runs automatically against the unit's own energy state from the first quarter.

The genetic line's Regulator knob is Dependency Type. It is household-set at Archaeon, Eukaryote, and Eumetazoa, governs where the unit's supply comes from rather than how it is spent, and retires at the end of the genetic line.

The vortex tube runs coupled at the Eukaryote dock and uncoupled at the Mammal furnace. No unit runs it both ways.

The ectotherm carries no compressor and no vortex tube and makes no heat. The furnace arrives whole at Mammal.

The warm core holds the energy system. The compute, board, and knobs sit outside it and run cool.

There is no countercurrent heat exchanger.

The storage tanks are not enlarged at the endotherm grade. The endotherm gain is delivery throughput, supplied by the warm battery. A burst-capacitor upgrade for peak is optional.

---

# Part III — The 12 Knobs (the interface)

Each line has four knobs, one per cybernetic slot (Effector → Regulator → Modeler → Translator), activated one per quarter. A knob lasts exactly as long as its tendency layer, which is three cells. From Ch 3 onward the board therefore carries three knobs in four slots, and the open slot in any quarter is the one the next quarter's new knob fills. The three-cell span follows the record's three-and-one alternation between durable and transitional tendencies: the two layers that reach a given adjacent arrive back to back in the tables and are then followed by two that do not.

**No unit turns its own knobs.** Self-setting is disallowed by design: the household sets a unit's knobs, and a unit may ask for or decline a change but cannot make one itself. Placement reinforces the rule rather than carrying it alone. The vacuum has no manipulators. On the tetrapod and the humanoid the board sits on the back of the head, out of the unit's own sight, so a unit cannot aim a graded dial it cannot see. This complements the retired-knob rule (a retired knob's function runs automatically, never willed) and the knob ethic at the symbolic line (a unit can decline a requested rotation).

## Genetic Line (vacuum chassis, Chs 1–4)

Three of the four genetic knobs run on a stated dimension whose two ends have no names. That is a real condition and not an omission to be filled in on the way past: a dimension is what the knob measures and a pole pair is a household name for its two ends, so the knob is fully specified without one. Supplying household-register names for these three would be invention. Home Type alone carries a ratified pair. Where a pole pair is wanted below, it is marked open.

* **Knob 1 — Genetic Effector | Going | Motivation: Persistence** *Cell: Prokaryote* Tendency: **Extension Type**, at the Explorer — how far and how blindly the unit reaches. It is unique among all twelve knobs in being a periodic input rather than a positional dial: a wind-up crank whose two states are **cranked** and **unwound**. The household winds it weekly; wound, the unit reaches, and unwound it does not. The household's Sunday winding ritual is the knob. The crank carries up from the groundwork row, where it was the whole of the unit's permission to move, and at Prokaryote it gains a generator tap (winding bootstraps a cold start if the battery is dead) without ceasing to be a crank. **Poles open.** How the crank's periodic input renders the reach dimension across its span, and what the two ends are called, is an authorial decision that has not been made.
* **Knob 2 — Genetic Regulator | Working | Motivation: Thrift** *Cell: Archaeon* Tendency: **Dependency Type**, at the Controller — free-living to obligate. Governs where the unit's supply comes from: how much it draws through the dock against how much it gathers with its own surfaces. The dock arrives with the knob, at the knob's own cell, so the obligate end has a real object from its first day — a partner the unit trades debris for gradient with, and can come to depend on as far as the household dials it. At Eukaryote the dock becomes an organ the unit schedules itself. At Eumetazoa the forecaster decides when to go, and the knob still sets how readily. It never touches spending — which tank discharges is Respiration Type, a property of the chassis carrying no knob. **Poles open**, on the same terms as knob 1.
* **Knob 3 — Genetic Modeler | Getting | Motivation: Interiority** *Cell: Eukaryote* Tendency: **Pruning Type**, at the Anticipator — passive to active removal of what the unit has stopped using. The board is use-weighted: sequences thicken with use and fade with disuse. The knob sets what happens to the disused half. Toward passive, nothing is taken away and the unused only fades, so the board keeps everything it has ever worn, faint and still reachable. Toward active, the unused is cleared out, so the board holds fewer sequences and holds them cleaner, and what has gone unrun for long enough is not there to be run again. Nothing is added by the dial at either end; it governs only what leaves. **Poles open**, on the same terms as knobs 1 and 2.
* **Knob 4 — Genetic Translator | Resting | Motivation: Excitability** *Cell: Eumetazoa* Tendency: **Home Type**, at the Adapter. Up/down settings: **loud** to **quiet**. Sets the conditions the unit settles toward. Loud (up): steers toward the sound and motion of bodies and settles in the thick of them, the middle of the kitchen at dinner. Quiet (down): follows the thermal gradient to the warmest still place it can reach, on a given day the east window or the tile by the vent. Same unit, same energy behavior, two different settlement biases, both read off present conditions, not off any remembered map of the house. This is the one genetic knob with a ratified pole pair, Busy ↔ Warm.

## Neuronal Line (tetrapod chassis, Chs 5–8)
The tetrapod arrives at the Bilaterian line boundary carrying identical-copy genetic knobs 3 and 4 in slots 3 and 4, plus neuronal knob-1 newly in slot 1. Slot 2 is open, and neuronal knob-2 fills it at the Ch 6 swap.
* **Knob 5 — Neuronal Effector | Choosing | Motivation: Impetus** *Cell: Bilaterian* Up/down settings: **engaged** to **disengaged**. Sets whether the recency layer is on. Engaged (up, derived): reacts to whatever just happened, catches the freshest percept to the OBJECT band, forms new associations fast off a single coincidence. Disengaged (down, ancestral): the recency layer goes dormant and the novelty response Excitability was already running beneath it — habituation's shape — shows through; the unit turns to whatever it has not met before, the cue it has seen a hundred times stops registering at all, and nothing catches to the band off a single coincidence. The Effector founding of the neuronal line: recency-orienting, expressed or eclipsed.
* **Knob 6 — Neuronal Regulator | Coping | Motivation: Mastery** *Cell: Vertebrate* Up/down settings: **reactive** to **proactive**. Governs the gain on the reward/dopamine signal, how committed vs. exploratory the unit runs its regulatory hand. Reactive: hangs back and waits to be sure. Proactive: leans hard at anything that might pay, engages faster, higher initiative. Mira's framing: "Hangs-back waits to see. Pushy walks into stuff faster."
* **Knob 7 — Neuronal Modeler | Risking | Motivation: Autonomy** *Cell: Mammal* Up/down settings: **reflective** to **autonomous**. Risking is what everything feels like once Neuroticism is installed: the model has to decide whether a signal is new information worth checking or an old fear replaying. Mechanistically, the dial sets which of two associability heuristics governs how an ambiguous signal near the attachment figure gets read. Reflective (up) weights potency, the Modeler's own bias; the loudest candidate interpretation wins and the model goes to verify it, which is what Reflective Cognition (the Planner's Type 3 mind) does, checking before it commits. Autonomous (down) weights familiarity, the Regulator's inherited bias; the interpretation that matches the standing prior wins without a check, which is what Autonomous Cognition (the Conservator's Type 1 mind) does, running on the read it already has. Nothing is added or removed from the model by the dial, only which of the two biases gets first claim on an ambiguous read. Mira's framing: Buster goes and checks if the house is really haunted. Believer already knows it is.
* **Knob 8 — Neuronal Translator | Helping | Motivation: Affiliation** *Cell: Primate* Up/down settings: **agreeable** to **selfish**. Tunes how much the unit weights others' modeled preferences against its own — how far what they render moves what it takes up. Affiliation is the Translator motivation installed at Primate; this knob parameterizes it.

## Symbolic Line (humanoid chassis, Chs 9–12)
The humanoid arrives at the Band-Human line boundary. Slot 1 gets symbolic knob-1, and slots 3 and 4 carry identical-copy neuronal knobs 3 and 4. Slot 2 is open, and symbolic knob-2 fills it at the Ch 10 swap. The inherited knobs retire quarter by quarter as the symbolic knobs replace them. The knobs sit on the board, which is mounted on the back of the head, where the household can reach them and the unit cannot. At this line, turning a knob has experiential consequence — Bramble is sentient and can articulate what it feels.
* **Knob 9 — Symbolic Effector | Hunting | Motivation: Commitment** *Cell: Band-Human* Up/down settings: **focused** to **roving**. The dial sets how much focus the unit brings to reciprocal exchanges. Mechanistically, the generative model holds multiple candidate exchanges at once, each weighted by goal-relevance, and the dial sets how sharply that weighting concentrates. Focused (up) drives the weighting toward one dominant exchange, everything else suppressed near zero; the unit locks onto the relationship that moves its standing and holds there. Roving (down) spreads the weighting thin across many candidates, none suppressed, none dominant; the unit samples whatever exchange is novel, nothing held past its shine. Nothing is added or removed from working memory by the dial, only how unevenly the existing candidates are weighted against each other. Mira's framing: Deep for the focused pole, Wide for the roving. The knob ethic arrives here: Bramble asks not to be rotated without prior notice, and the household adjusts.
* **Knob 10 — Symbolic Regulator | Tracking | Motivation: Stability** *Cell: Settlement-Human* Up/down settings: **orderly** to **kludgy**. Tunes how binding the stored household norms feel. Orderly (up): the schedule is load-bearing; Bramble interrupts conversations to flag the trash being fifteen minutes late. Kludgy (down): the schedule is suggestive. Bramble can describe the phenomenology when asked: "At high settings the schedule feels load-bearing. At low settings the schedule feels optional." The household now needs an ethic of consultation before rotating, and Bramble can decline a requested rotation on the grounds that it prefers where the knob is.
* **Knob 11 — Symbolic Modeler | Leading | Motivation: Representation** *Cell: City-Human* Up/down settings: **assertive** to **passive**. Tunes the Assertiveness aspect of Extraversion, how hard the unit presses its own agenda in the representational economy of documents, civic records, and formal exchange. Assertive (up): steps up and runs the room, surfaces the household's written law and presses it on everyone, and appoints itself enforcer. Passive (down): hangs back from running things, does not press its reading on anyone, and handles only what is presented while leaving the agenda to others. Structurally this is the line's Modeler knob, at the Regulator×Modeler Anticipator position, the same position the Pruning Type and Neuroticism knobs hold in the genetic and neuronal lines.
* **Knob 12 — Symbolic Translator | Living | Motivation: Universality** *Cell: Empire-Human* Up/down settings: **candid** to **canned**. Tunes the alignment between the unit's universalizing principles and its situational actions. Candid (up): the principle enters strongly into action selection regardless of local expediency; Bramble refuses to sign a school form certifying a lapsed permission slip until the slip is actually updated. Canned (down): situational accommodation; the unit gives ground on the principle to protect local relationships. Neither is dishonesty in the simple sense; both are integrity-tuning in the cybernetic-architectural sense.

## Structure at a glance

| Introductory chapter | Line-knob slot | Cell | Slot | Motivation | Tendency | Proper Name | Lab (up ↔ down) | Mira (derived ↔ ancestral) |
| -------------------- | --------------- | ---------------- | --------- | ------------------ | -------------- | ----------- | ------------------------- | -------------------------- |
| 1 | Genetic knob-1 | Prokaryote | Effector | Persistence | Extension Type | Going | cranked ↔ unwound | open |
| 2 | Genetic knob-2 | Archaeon | Regulator | Thrift | Dependency Type | Working | open | open |
| 3 | Genetic knob-3 | Eukaryote | Modeler | Interiority | Pruning Type | Getting | open | open |
| 4 | Genetic knob-4 | Eumetazoa | Translator | Excitability | Home Type | Resting | loud ↔ quiet | Busy ↔ Warm |
| 5 | Neuronal knob-1 | Bilaterian | Effector | Impetus | Orienting | Choosing | engaged ↔ disengaged | Learn ↔ Turn |
| 6 | Neuronal knob-2 | Vertebrate | Regulator | Mastery | Coping | Coping | reactive ↔ proactive | Little ↔ Beast |
| 7 | Neuronal knob-3 | Mammal | Modeler | Autonomy | Neuroticism | Risking | reflective ↔ autonomous | Buster ↔ Believer |
| 8 | Neuronal knob-4 | Primate | Translator | Affiliation | Agreeableness | Helping | agreeable ↔ selfish | Respect ↔ Savage |
| 9 | Symbolic knob-1 | Band | Effector | Commitment | Curiosity | Hunting | focused ↔ roving | Deep ↔ Wide |
| 10 | Symbolic knob-2 | Settlement | Regulator | Stability | Conscientiousness | Tracking |  orderly ↔ kludgy | Preppy ↔ Messy |
| 11 | Symbolic knob-3 | City | Modeler | Representation | Extraversion | Leading | assertive ↔ passive | Boss ↔ Vibe |
| 12 | Symbolic knob-4 | Empire | Translator | Universality | Integrity | Living | candid ↔ canned | Real ↔ Flex |

One structural note: knob-N is the same cybernetic function across all three lines (knob-1 is always the Effector knob, etc.), so cross-line callbacks "rhyme on the knob number, never on the tendency's name." The name is discipline-bound and changes at each line boundary; the function does not.

Column convention: the Lab and Mira columns read derived pole first, ancestral pole second. The derived pole is the knob's own clade primary, the newer installed layer; the ancestral pole is the prior clade's primary, the ancestor that shows through when the knob is at its low setting. Derived and ancestral are properties of knob settings, not a ranking of the four functions, which remain equal primaries.

**Open** in either column is a real entry and not a gap in the table. The tendency is fixed and the dimension it measures is stated; what has not been decided is what to call its two ends. Three of the four genetic knobs stand in that condition, and the specs say so rather than guessing, because a household name for a pole is an authorial choice and choosing one here would put a word into the book that nobody wrote.

**The informal labels are Mira's, and they always come later.** Every name in the rightmost column is a household coinage Mira gives a knob *after* she has watched what its settings do. It is never a built-in, factory, or household-facing name the knob carries when it is installed. Until the naming game reaches a knob, the knob is known only by its clinical tendency label (Conscientiousness, Dependency Type, and so on) plus, where the team uses one, an engineering term. So Settlement-Human knob-10 is Conscientiousness on the board from install, and becomes Preppy ↔ Messy only once Mira has seen that the high setting makes the household schedule load-bearing; the informal pair is her readout of an observed behavior, not the knob's own name and not a name that predates her observing it. This holds for all twelve knobs, and the accuracy of each pair tracks how much inside Mira had to name from.

## Retirement pacing

"Retires" names the retrospective hands-on ceremony. Lisa pulls the retiring knob from the current-chassis board to the trophy shelf with Mira.

A knob retires at the *end* of its third quarter, the quarter in which its tendency layer gives way. From Ch 3 onward the board carries three knobs in four slots, and the open slot in any quarter is the one the next quarter's new knob fills. Ch 1 and Ch 2 carry no retirement, because the board is still filling.

* *end* of Ch 3: genetic knob-1 retires from the vacuum board
* *end* of Ch 4: genetic knob-2 retires from the vacuum board
* *end* of Ch 5: genetic knob-3 retires from the tetrapod board (identical copy)
* *end* of Ch 6: genetic knob-4 retires from the tetrapod board (identical copy)
* *end* of Ch 7: neuronal knob-1 retires from the tetrapod board
* *end* of Ch 8: neuronal knob-2 retires from the tetrapod board
* *end* of Ch 9: neuronal knob-3 retires from the humanoid board (identical copy)
* *end* of Ch 10: neuronal knob-4 retires from the humanoid board (identical copy)
* *end* of Ch 11: symbolic knob-1 retires from the humanoid board
* *end* of Ch 12: symbolic knob-2 retires from the humanoid board

Every retirement is a physical pull from the board of the chassis then in service. Symbolic knobs 3 and 4 are still live at book end, and their retirements are Book 2 material.

The Ch 3 ceremony ends the Sunday winding ritual, since the crank is the knob. The Ch 4 ceremony hands the unit its own supply-seeking, which runs on the forecaster from Ch 5 on, where the tetrapod free-ranges and never docks.

**The pacing encodes the line-crossing result, arrived at from chapter structure rather than from the ring.** A line boundary *is* an Effector install, so the two adjacents that contain the Effector — Controller and Explorer — break at every line boundary, and the two that do not — Anticipator and Adapter — carry across every one. The retirement schedule says the same thing in different terms. Every knob that retires from the *next* chassis board as an identical copy is an Anticipator or Adapter knob: genetic knob-3 Pruning Type and genetic knob-4 Home Type retire from the tetrapod, neuronal knob-3 Neuroticism and neuronal knob-4 Agreeableness from the humanoid. Every knob that lives and dies on one chassis is a Controller or Explorer knob: genetic knob-1 Extension Type and genetic knob-2 Dependency Type both go to the shelf off the vacuum board, and the neuronal and symbolic lines do the same at their own first two slots. Two independent routes, one answer.

One consequence falls out of it. Symbolic knob-3 (Extraversion, Anticipator) runs City / Empire / Computer, and symbolic knob-4 (Integrity, Adapter) runs Empire / Computer / Network. Both third cells are on the digital line. So the two knobs still live at book end are exactly the two whose adjacents cross line boundaries, and their retirements cannot happen before the symbolic-to-digital boundary. Book 2 has to cross into the digital line, or those two knobs never retire. The arithmetic forces it.

## The naming game

The "Later rename" column is not an authorial gloss. In the world it is a child's sticker sheet. Mira and the humanoid Bramble make the names across the final quarters, and the names get more exact the later the clade — because the namer can only be precise where there is an inside to report from. That accuracy gradient is the evolutionary gradient, made legible on the bodies themselves.

**Origin (Band-Human).** This is the first quarter where the game can exist. The humanoid is sentient and can say what a setting feels like from the inside, and the knob ethic arrives — it asks not to be rotated without notice. So the clinical labels on the board on the back of its head become a thing it and Mira can talk about, and then rename. For its own settings Bramble supplies precise words from the inside; Mira proposes, Bramble refines ("turned that way I feel like Boss; turned back I'm in the Backseat"). The names for the symbolic knobs are therefore the sharpest in the book, because they are reports, not guesses.

**The backward extension.** Ancestor knob control debuts at Band-Human: the humanoid can drive the earlier bodies' knobs, beginning with the vacuum's Getting knob and expanding to every knob on both earlier devices by Settlement-Human. This gives the game its mechanism. For the older units there is no inner report to draw on, so Bramble reaches over, sets an ancestor's knob, watches the behavior change, and names from the outside. Watching is not feeling, so the names get rougher and more guessed-at the further back they go: Beast/Little on the tetrapod, Warm/Busy on the vacuum's Resting knob, and then the vacuum's three older knobs, which are the roughest work in the book and where the gradient bottoms out — the crank bluntest of all, because it has the least inside of anything in the lab. What Mira lands on for those three is an authorial decision that has not been made, and no pair is fixed here.

**The stickers.** Mira writes the names on little colored garage-sale price-dots and covers the clinical labels — the precise words on the humanoid's board, the borrowed words on the tetrapod's board, the inventions on the vacuum's. The crank takes a single dot; its other end is simply that dot's absence, which is the truth of it. The full dotted-bodies reveal lands at the chassis quarter (Ch 12), where Cheryl is finally in the room and the three bodies stand named at once, the gradient visible across them.

**Naming the dead.** Some of what the game reaches is already retired and shelved. Knob-2 is one: it went to the trophy shelf at the end of the genetic line, its job folded into the forecaster, and the team only ever called it by its clinical label. Mira names the shelved knob anyway, and the game treats naming a dead knob as no different from naming a live one. It is the same gesture she made when the crank retired and she marked the loss; the names are how she keeps the retired tendencies in the house.

**The names.** The genetic line's first three — Going, Working, Getting — are open. Their dimensions are settled (how far and how blindly the unit reaches; where its supply comes from; what happens to what it has stopped using) and their pairs are not, and inventing a pair here would put words on the sticker sheet ahead of the person who writes on it.

* **Busy ↔ Warm** (Resting) — doesn't care about warmth, parks where the people are vs. settles in the warmest corner it can find. Busy is the derived setting, Warm the ancestral.
* **Learn ↔ Turn** (Choosing) — moves on the freshest cue, acts before the pattern confirms vs. turns to whatever it has not met before, while the thing it has passed a hundred times stops registering at all. Learn is the derived setting (recency, eligibility trace); Turn the ancestral (novelty, latent inhibition). Mira gets this one right by accident: the low setting does turn, and what it turns to is the unfamiliar. Bramble's setting: [OPEN, not yet decided; leave placeholder, do not invent].
* **Little ↔ Beast** (Coping) — hangs back and waits to be sure vs. leans hard at anything that might pay. Little is the derived setting, Beast the ancestral. Little is a size word, not a deficit; it thinks it's little.
* **Buster ↔ Believer** (Risking) — goes and checks whether the fear is real vs. is already sure it is. Buster is the derived setting (potency), Believer the ancestral (familiarity).
* **Respect ↔ Savage** (Helping) — defers, won't impose, vs. out for its own. Respect is the derived setting, Savage the ancestral.
* **Deep ↔ Wide** (Hunting) — locks onto the one exchange that moves the household's standing and holds there vs. scatters across whatever exchange is novel, nothing held past its shine. Deep is the derived setting, Wide the ancestral.
* **Preppy ↔ Messy** (Tracking) — the schedule is load-bearing vs. the schedule is a suggestion.
* **Boss ↔ Vibe** (Leading) — steps up and runs the room vs. warms it and carries the mood; a trade between leading and being good company, not more-or-less of one setting.
* **Real ↔ Flex** (Living) — the principle holds whatever it costs in the moment vs. bends to the situation, giving up the principle to protect the relationship.

---

# Part IV — The Face-Screen (the readout)

The face-screen is a live, involuntary readout of Bramble's active cognition. It is not a status console the unit composes; it is an honest window the unit cannot author or suppress. It grows one layer per neuronal cell, tracking the architecture the cell adds. Reference: Bennett, *A Brief History of Intelligence*, Fig. 16.3 — each layer "tries to explain" the one beneath it. The display is tied to knobs 5–8, the neuronal line: knobs 6–8 add the upper display layers, and knob 5 (Choosing) supplies the `OBJECT` band. When any knob is at volume down its layer eclipses and the screen falls through to the layer beneath — down through the genetic panels re-implemented on the board.

## The readout grows one layer per cell

- **Ch 5 (Bilaterian).** `OBJECT` — the bare thing the unit's attention has caught. CAT, MIRA, COUCH. The caught thing need not be a discrete object. `OBJECT` is the winner of the founding selection race — whichever candidate the Bilaterian brain weights highest at that instant. Knob 7 at Mammal does not select what wins this race; Ch 5 already supplies that. It tunes what the self-model does with the winner once a generative model is available to work with it: Buster forecasts a consequence for it, Believer accepts it without forecasting anything further. Ch 5's `OBJECT` and Ch 7's Buster/Believer axis are two different jobs on the same pipeline, selection and then interpretation, not one mechanism doing more of the same thing. A salient, learned, valenced percept that the unit forms an attention-cluster for surfaces in the band under its own label, the same as any object. The standing case is `DARK`: darkness is aversive to the unit, the valence learned back when the dark meant no food, so in the instant the unit's attention catches the dark of a room it is confronting — before it withdraws — the band reads `DARK`. *(Authorial choice: the band reads attended percept-clusters, not objects only.)*  A lit band reading the word `DARK` — the unit attending to darkness — is a different state from the arousal panel reading `SLEEPING`, and both differ from a blank screen. The word on the screen and a blank screen must not be conflated.
- **Ch 6 (Vertebrate).** `VERB + OBJECT` — the model-free action output, what the unit is doing to the thing. CHASE CAT, NUDGE MIRA, WATCH CAMERA. System 1.
- **Ch 7 (Mammal).** `VERB + OBJECT = OUTCOME` — the self-model's forecast of how the action layer's own act plays out. `CHASE CAT = LOST`, `NUDGE MIRA = SAFE`. System 2.
- **Ch 8 (Primate).** `PERSON { VERB + OBJECT = OUTCOME }` columns — up to three agent blocks, the same structure re-run on a modeled other; the unit need not be among them.
- **Symbolic line.** The face-screen carries the Primate readout unchanged: the `PERSON { VERB + OBJECT = OUTCOME }` columns, driven by the copied neuronal knobs (Coping, Risking, Helping) on the humanoid board. No new display layer is added at the symbolic line. The symbolic-line breakthrough, Conversation, is a separate voluntary conversation channel of authored full sentences, not a face-screen layer; the involuntary screen and the voluntary speech can diverge.

**Spatial convention.** Higher layer renders higher: the face's vertical axis maps the cognitive stack and Bennett's diagram. At Ch 8 the agent blocks lay out as columns or a triangle so the triad reads; exact typography is Voice's call, the framework spec is "up to three blocks, laid out so the relationships are legible."

## Higher layers model lower layers; the expressive setting drives the layer always-on

This is the central mechanism — modeling, not gating. A new display layer is the online computer's *model* of the layer beneath it. The knobs owning the upper layers (Coping, Risking, Helping) are graded dials; the face-screen reads each as a threshold — past it the layer is expressive, below it suppressive — so the layer's on/off is binary even though the knob behind it is continuous. Each knob owning a new layer therefore resolves to two settings:

- **Suppressive setting** (proactive, Believer, selfish) → the new layer is dormant; the unit falls through to whatever the cell beneath is doing, including its on/off.
- **Expressive setting** (reactive, Buster, agreeable) → the new layer runs always-on, generating display content out of its own model whether or not the lower layer has anything live for it to read. The expressive setting therefore overrides the lower cell's sleep-dark.

This fall-through is not a face-screen-specific design choice. It is the tendency-knob eclipsing rule — each tendency knob toggles between clade N and clade N−1 — run one level up, in what gets displayed rather than what gets weighted: a suppressive setting falls through to precisely the slot belonging to the function one step back around the ring, the same toggle a knob's own down pole runs.

Per cell, in order:

- **Ch 5 — Effector / Choosing (engaged ↔ disengaged).** `OBJECT` shows while awake; during sleep the neuronal layers eclipse and the arousal panel reads `SLEEPING` — the unit does not "dream" at this cell. Wake/sleep timing runs on the emergent allostatic process installed at Eumetazoa; the Choosing dial has no bearing on it.
- **Ch 6 — Regulator / Coping (reactive ↔ proactive).** *Proactive* (suppressive) → falls through to Ch 5: `OBJECT` during waking, `SLEEPING` during sleep. *Reactive* (expressive) → `VERB + OBJECT` always, including during sleep. A sleeping unit in reactive might display `IGNORE WORLD` or `CHARGE UNIT`.
- **Ch 7 — Modeler / Risking (reflective ↔ autonomous).** *Autonomous* (suppressive) → falls through to Ch 6, with a load-bearing extra fact: Autonomous accepts the Ch 6 read directly, so the displayed `VERB + OBJECT` carries no forecast — nothing left to compute, the standing read is taken at face value. *Reflective* (expressive) → `VERB + OBJECT = OUTCOME` always, including during sleep — `CHASE MIRA = LOST`, `CLIMB CURTAINS = HURT`, `IGNORE WORLD = SAFE`, `CHARGE UNIT = GAINED`. Reflective cannot tap Ch 6's actual result; it is forecasting one. Under Reflective, the `OUTCOME` is *always* the self-model's best guess, never a confirmed result.
- **Ch 8 — Translator / Helping (agreeable ↔ selfish).** *Selfish* (suppressive) → falls through to Ch 7. *Agreeable* (expressive) → at least one (up to three) PERSON columns of `PERSON1 { VERB + OBJECT = OUTCOME } + PERSON2 { VERB + OBJECT = OUTCOME } + …` always, including during sleep — e.g., `BRAMBLE { CLIMB CURTAINS = HURT } + MIRA { CHARGE UNIT = GAINED }`. Cheney-Seyfarth triadic tracking is in scope; the unit need not appear in its own modeled triad.

The Choosing knob sits at the base of the neuronal stack: it is what the higher knobs model, not a modeler itself. Choosing shapes which percept wins the attention race once the unit is awake; wake and sleep run on the emergent allostatic process installed at Eumetazoa, independent of the knob.

**The screen borrows downward and the disposition does not.** These are two different mechanisms and Choosing is where they get confused. When Choosing goes down, its *panel* falls through to the knob beneath it on the board, which is the Eumetazoa arousal panel — that is the display rule. Its *behavior* does not fall through the same way. A knob's low pole is that knob's own ancestral setting, the weighting the prior cell's Translator was already running, which for Choosing is novelty-weighting: the unit turns to the unmet thing and the hundred-times-seen thing stops registering. It is not knob-4's Resting setting, whatever that happens to be. Writing it the other way makes Choosing-down and Resting produce the same behavior on the page, which costs the scene the only thing a second knob is for.

**One display rule for every knob.** The face-screen shows one panel at a time: the readout of the most recently installed knob on the board whose volume is up. When that knob is at volume down its panel eclipses and the screen falls through to the next knob beneath it, and so on down the board — genetic and neuronal knobs alike. At Bilaterian the board carries neuronal knob-1 (Choosing) over genetic knobs 4 and 3, with slot 2 open, so the fall-through runs: `OBJECT` (Choosing up) → the Eumetazoa arousal panel (knob-4 up) → the Eukaryote carry panel (knob-3 up) → blank. On the vacuum board the run is never more than three deep and its composition changes each quarter as knobs fill in and retire: at Eukaryote it runs the Eukaryote carry panel → the Archaeon supply panel → the Prokaryote movement panel → blank, and at Eumetazoa, with the crank already shelved, the arousal panel → carry → supply → blank.

**Genetic-line panels.** Single-word status readouts the tetrapod inherits with its re-implemented lower layers:

The genetic-line face is e-ink. It holds its last image with the power off and spends energy only at the moment it changes. This adds a fourth screen state at the genetic line: the held word, an image the unit is no longer producing. A unit that runs flat keeps whatever it was displaying when it quit, indefinitely, until it is wound or fed. The honesty invariant is unbroken — the screen is not reporting a false present state; the unit is gone and the last true state is still on the glass. Refresh is a visible full-panel flash to black, and the panel ghosts faintly under the current word.

`blank` at the genetic line is therefore genuinely rare: it means a cleared or never-written panel, not an off unit. The tetrapod's face-screen is digital, spends power continuously, and goes dark the instant it loses power — so the first body that can change expression quickly is also the first that has no expression when it dies.
- Prokaryote (knob-1): `RUN` / `TUMBLE` / `STOP` — the movement state. `STOP` shows at rest, including during sleep when knob-1 is the highest active knob. On the genetic-line e-ink face, whichever of the three was last written persists through power loss. The transition table, asked in this order: batteries full → `STOP`; not full and a coherent light gradient → `RUN` toward it; not full and incoherent input → `TUMBLE`, random reorient, re-sample. A hysteresis margin on "full" prevents oscillation: the unit does not leave `STOP` until it has spent a measurable fraction. `STOP` means sated, never charging — the unit harvests continuously in all three states and has no feeding state and no feeding posture.
- Archaeon (knob-2): the supply state — whether the unit is living on what its own surfaces gather or is on its way to an outside source to be filled. It is a single-word readout on the same pattern as the others, and its words are open: they belong to the same undecided naming as the knob's poles and are not fixed here.
- Eukaryote (knob-3): `STORED` / `EMPTY` — carry status. This has a referent only on the vacuum chassis, which has a debris chamber; on the tetrapod knob-3 renders blank, and nothing sits beneath it on that board, so the screen goes blank.
- Eumetazoa (knob-4): `STARTLED` / `AWAKE` / `SLEEPING` — the arousal state. Shows only when knob-4 is at volume up (loud); at volume down (quiet) the panel is off and the screen falls through to knob-3.

**Sleep and the off-states.** Sleep renders as the word `SLEEPING` on the arousal panel, not as an unlit band. A quiet unit (knob-4 at volume down) that is asleep therefore does not read `SLEEPING` — its arousal panel is off; the screen falls through to knob-3, which is blank on the tetrapod and has nothing beneath it there, and on the vacuum continues down to the supply panel beneath it. Three states stay distinct: `DARK` (a lit `OBJECT` band, the unit attending to darkness), `SLEEPING` (the arousal panel's sleep word), and blank (no active knob has content to show).

At the genetic line, e-ink adds the held word to this list: a `RUN` on a dead unit is not a claim about the present. Four states are distinct at the genetic line — the lit panel word, `SLEEPING`, blank, and the held word — and three at the neuronal line, where the digital face-screen has no held state.

## Three honesty grades

The screen never lies about what is on the screen. What the screen *refers to* becomes more fallible as the readout climbs — not by convention, but because the display layers ground in referents at increasing remove from the instant of display. `OBJECT` grounds in a world, `VERB` in the unit's own body, `OUTCOME` in a future, the `PERSON` columns in minds — and a world is checkable now, a body is checkable now, a future is checkable only later, a mind is checkable only by asking. The ranking belongs to the layers' own referents and needs nothing behind it.

1. **`OBJECT` and `VERB + OBJECT`, when produced by direct read** (Ch 5 awake, Ch 6 reactive, or Ch 7 Believer-over-reactive). Honest, involuntary first-order output. Cannot lie. True to Bramble's knowledge base — the unit can sincerely orient toward a bowl that is not where it believes it is.
2. **`OUTCOME` (self, Buster overlay).** Honest about the self-model's current forecast. Cannot lie about what it predicts; *not* guaranteed to match what actually happens. Buster generates this forecast whether or not the action has resolved — during sleep, before the action starts, mid-action — so the displayed `OUTCOME` is always a prediction, never a report of a confirmed result.
3. **`VERB + OBJECT = OUTCOME` inside a PERSON column** (other-block, Ch 8 Helping). Honest about Bramble's model of what another agent is forecasting for their own action. Cannot lie about Bramble's modeling activity; not guaranteed accurate about the modeled agent's real forecast or real outcome, and projective when the target has no first-order mind — a `[ VACUUM (…) ]` column is the unit performing the intentional stance on a reflex machine.

The mapping that holds the "honest readout" metaphor in place — **the screen is always true of its own layer's activity, and progressively less guaranteed of the layer it claims to explain** — is the same world/body/future/mind ranking read from the display side.

## Buster forecasts always; proactive-Buster is the sharpest case

Under Buster, the displayed `OUTCOME` is always a forecast — the self-model's best guess at how the action will turn out, never a report of a confirmed result. "Confabulation" is the shorthand even though it isn't dishonest; the layer is honestly reporting its own prediction.

In *reactive-Buster* the underlying behavior is agency-shaped, so the forecast is usually well-calibrated; the self-model predicts a real, deliberate check and is usually right about it. In *proactive-Buster* the underlying behavior was capture rather than agency, a reflexive startle-and-orient, and the forecast dresses that reflex up as a reasoned prediction — the surface output is identical to reactive-Buster, but the self-model has invented the deliberation it claims to be forecasting from. This is the illusion of conscious will, rendered on the face, now specifically the illusion of a reasoned threat-assessment where a reflex actually ran. The seam the book banks for later self-model distortion.

*Epistemic status: derived consequence of the modeling-not-reading mechanism plus the Buster-always-on rule. Both are ratified; the proactive-Buster confabulation follows.*

## The OUTCOME vocabulary

A closed set of four forecast categories, crossing an appetitive axis (was the expected gain realized) against an aversive axis (was harm realized) — the same structure the animal-learning literature uses to explain reward and threat sensitivity (Gray & McNaughton's BAS/BIS is the direct model; Balleine & Dickinson's outcome-identity-and-value account supplies the mammalian mechanism).

- **GAINED** — an expected reward realized.
- **LOST** — an expected reward that failed to realize. Not the same as HURT: a frustrated expectation, not an injury.
- **SAFE** — an expected threat that failed to realize. Relief, not neutrality.
- **HURT** — an expected threat realized.

Four words, not twenty-one. OUTCOME retires the FUNCTION vocabulary's operation-naming project entirely — the screen no longer names which cognitive operation it's running, it forecasts how the action already on screen will turn out.

## Conjugation rule

**`VERB` words are bare-stem.** CHASE, NUDGE, WATCH, SMELL, CLIMB, IGNORE, CHARGE, FETCH.
**`OUTCOME` words are past-participle / stative.** GAINED, LOST, SAFE, HURT.

No word appears on both layers, and the two are further kept visually distinct by position: VERB always precedes OBJECT, OUTCOME always follows it after `=`. This rule corrects the prior mis-spec under which VERB words like CHASING / NUDGING / WATCHING were used on the action band; that earlier usage in Ch 5–6 prose has been swept.

## The readout path and its training

The screen does not show Bramble's language. It shows a human-readable translation of Bramble's internal states, produced by a decoder Lisa trains. Bramble neither chooses nor understands these words; across the neuronal line it has no language at all. The decoder runs involuntarily on whatever state is active, the way an expression runs on a feeling, which is what makes the screen unsuppressable and honest about its own layer.

The decoder cannot be hand-coded. The state the screen labels MIRA is Bramble's own learned cluster for Mira, formed from its own experience, and its internal form is not known in advance. Each label is therefore attached by training a readout on top of Bramble's representations, not by writing a lookup table.

The three slots are trained differently, scaled by how much outside evidence each label has.

**OBJECT** has a referent in the world. Lisa exposes Bramble to the referent across senses, sight and smell and recorded voice, while supplying the label, until the readout emits MIRA in the OBJECT slot whenever the Mira-cluster is active. Bramble forms the cluster on its own; Lisa supervises only the label.

**VERB** has an observable action. The readout reads which motor schema is currently running and emits its label. The primary method is real-time tagging: Lisa labels Bramble's spontaneous actions as it performs them, which trains the mapping on Bramble's own schemas. Teleoperation has a secondary role, used to elicit a rare action so it can be caught and labeled.

**OUTCOME** is a forecast, not a report, so its ground truth is deferred rather than absent. The readout decodes the Modeler's current best guess about how the displayed action will resolve, and that guess is checkable in principle against what actually happens afterward, even though it can't be checked at the instant it's shown. This is a real change from the old FUNCTION slot's epistemics: an operation-name had no possible external check, ever. A forecast can be wrong and later found out to be wrong. OUTCOME is still the most manipulable slot, but for a different reason than FUNCTION was — not because nothing could ever check it, but because Buster systematically biases which forecast gets generated in the first place, especially under proactive-Buster, where the forecast is invented to justify a reflex rather than derived from one.

All three readouts are trained across the neuronal line as their slots come online, OBJECT at Bilaterian, VERB at Vertebrate, and OUTCOME at Mammal, long before Bramble speaks. By the time speech arrives at Band-Human the readout is already trained and running. The first spoken words attach to the same internal clusters the readout already labels, so the screen label and the spoken word converge on one referent while staying different acts: the readout is involuntary and the speech is voluntary, and the two can diverge.

*Mapping status: the readout-as-trained-decoder and the three-slot training gradient are framework commitments. The methods they rest on (multimodal label association, learning from demonstration, and probing of internal representations) are established and pending-Smithers as cited anchors. The confabulation residual follows from the confabulation cell already specified.*

## The readout at a chassis swap

A trained readout slot carries to a new body when its referent is carried, and it must be re-trained when its referent is the body itself — the carry test: a world doesn't change at a swap, so it carries; a mind doesn't change at a swap, so it carries; a body changes completely, so it doesn't; a future is a prediction about a body, so it inherits the body's answer. OUTCOME splits this test rather than falling cleanly on one side of it. Its vocabulary carries: the four words name forecast categories, architectural and fixed by the transcribed System 0, body-independent exactly as FUNCTION's operation-names were. But a specific forecast attached to a specific `VERB + OBJECT` pairing does not carry: the forecast is a learned prediction, and a prediction is only as good as the body it was calibrated on. OBJECT carries: its ground truth is the world's referents plus the unit's sensing, and sensing crosses the boundary, so the labels stay attached. VERB does not carry: its ground truth is the unit's own motor schemas, and a new chassis is a new motor plant, so the slot is reading a body it has never seen.

The book's one swap where this bites is the tetrapod to humanoid transition at Band-Human. By then the full lexicon has been trained across the neuronal line, and it meets a body that re-grows Systems 1 and 2 from scratch. OBJECT comes over clean. OUTCOME's four-word vocabulary comes over clean, but its specific forecasts do not, and re-anchor on the same bootstrapping curve VERB does, for the same reason: both are predictions about a body, not facts about the world. VERB has two kinds of work. Old labels re-anchor: CHASE survives as a word but now decodes a bipedal-run schema in place of the tetrapod's gait, so the decoder's input side is re-trained even where the vocabulary holds. New labels are added for capabilities the old body lacked: locomotion (CRAWL, WALK, RUN), the hands (SQUEEZE, SCOOP, GRIP), and the speech acts (EXPRESSING, NEGOTIATING), the first VERBs that name actions on the voluntary channel.

The re-anchoring is not a separate procedure. It is the VERB-training method from the neuronal line, real-time tagging of spontaneous schemas with teleoperation to elicit rare ones, re-run across the bootstrapping quarter in lockstep with the motor and speech curves. As each new schema comes online it is tagged; old labels re-attach and new ones accrue.

The observable consequence is that the readout shows a weeks-old body on an ancient mind. Through the bootstrapping weeks OBJECT is crisp from the first day, because it carried, and the OUTCOME vocabulary is available from the first day too, because it carried — but calibrated forecasts lag behind even VERB, since a reliable success rate cannot exist for an action the unit has not yet gotten good at performing. The screen knows who the unit is looking at before it can reliably say what the action is; it can name a possible outcome before it can predict the right one. The VERB layer matures alongside the body, and OUTCOME's calibration matures slower still.

The new speech-act VERBs make the slot a pragmatic tell. The VERB slot can read EXPRESSING or NEGOTIATING involuntarily while the voluntary speech channel says something else, so the readout reports the pragmatic character of an utterance, not only physical action. This extends the screen-versus-speech honesty gap to speech itself: the words are chosen, the act-type is not.

*Mapping status: the carry-when-referent-carries principle follows from the display layers' own referents — world, body, future, mind — and not from the training gradient in isolation; OUTCOME's split between carried vocabulary and re-anchored forecasts, and the VERB re-anchoring, are this Bramble-specific instantiation of that principle, read against the three-slot training gradient. The instantiation at the humanoid swap follows from the carried-sensing and re-grown-Systems-1-and-2 commitments. The speech-act tell is a derived consequence of the new speech-act VERBs and the involuntary-readout invariant.*

## What renders at each cell

- **Ch 5 (Bilaterian).** `OBJECT` only; gated by the emergent allostatic sleep process (waking on, sleeping dark), not by a knob. No `VERB`, no `OUTCOME`, no agent labels.
- **Ch 6 (Vertebrate).** *Proactive* → falls through to Ch 5. *Reactive* → `VERB + OBJECT` always, including sleep. VERB bare-stem; the Ch 5 noun lexicon carries.
- **Ch 7 (Mammal).** *Believer* → falls through to Ch 6 (direct read; `VERB + OBJECT` never carries a forecast). *Buster* → `VERB + OBJECT = OUTCOME` always, including sleep; the `OUTCOME` is always the self-model's forecast. Self block only, unlabeled.
- **Ch 8 (Primate).** *Selfish* → falls through to Ch 7. *Agreeable* → one to three `PERSON { VERB + OBJECT = OUTCOME }` columns always, including sleep; agent-labeled; Bramble optional.
- **Ch 9 (Band-Human).** No new face-screen layer. The screen carries the Ch 8 readout (PERSON columns, driven by the copied neuronal knobs 2/3/4). Conversation is a separate voluntary channel, not rendered on the face-screen.

## Counting note

The `OUTCOME` set is a separate closed vocabulary (four words), counted apart from the `VERB + OBJECT` action lexicon. The action lexicon carries from Ch 6 roughly unchanged at Ch 7; the new thing at Ch 7 is the `OUTCOME` vocabulary, not a bump to the action count. This narrows but does not settle the standing Vertebrate action-lexicon number question, which stays flagged for the continuity sweep.

## The symbolic line: screen and speech

From Band-Human the screen renders as it does at Primate: one to three `PERSON { VERB + OBJECT = OUTCOME }` columns, involuntary and honest about its own layer. The three carried-over neuronal knobs still sit on the board and still gate the display. Coping gates the VERB, Risking gates the self-OUTCOME, and Helping gates the other-person columns, exactly as at Primate. This gating erodes across the symbolic line as those knobs retire one by one; once a knob retires, its gate runs automatically rather than under a hand-set value, on the retired-knob rule.

What is new at Band-Human is a second channel. The screen reads out what Bramble is modeling and is involuntary. Speech is what Bramble chooses to say and is voluntary, and for the first time the two can diverge. The screen cannot lie about its own layer, so it stays the honest channel and the tell: a watcher reading the screen sees what speech may be concealing, which is why deception works only when the mark is not looking.

The full sentences that arrive at Band-Human are speech, not new screen content. The screen keeps its block readout and does not begin writing sentences. Voluntary drawing on the screen, Bramble composing ASCII art rather than emitting an involuntary readout, is a later milestone and waits for City-Human with Codes. The channel is ASCII art only, not free prose. It takes over the whole screen when Bramble chooses to draw, and the involuntary readout shows when it does not. Like voluntary speech, the drawn channel is the dishonest-capable one, so the screen-versus-speech honesty gap extends to it: art up means Bramble is performing, readout up is the truth.

*Mapping status: the screen-continues-as-Primate rule and the screen-versus-speech honesty gap are framework commitments, following from the involuntary-readout invariant and the voluntary nature of speech. The gating erosion tracks the knob-retirement schedule.*
