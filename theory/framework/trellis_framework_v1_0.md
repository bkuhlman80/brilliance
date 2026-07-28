# Trellis Framework — Deep-Time Architecture and Bramble's Cognitive Rendering

This doc carries five movements.

- **Part I — The deep-time evolutionary story.** What personality is, what each inheritance line is made of, how the bramble grows up the trellis, the ecology across lines, the genealogy of the thread, and what the Trellis Framework adds.
- **Part II — Bramble's cognitive rendering.** A stub. The four functions force a two-mind reading — the deep-time mind as Modeler, the online mind as Reviser, coupled by the Adapter loop Part III defines. The full cognitive architecture is owned by `bramble_specs` Part I.
- **Part III — Venn architecture foundations.** The structural geometry the rest of the framework rests on: the Port-Royal gradient the Venns ride on, the four cybernetic functions (Effector, Regulator, Modeler, Reviser), the adjacent-pair loops (Controller, Anticipator, Adapter, Explorer), the 2×2 triple constellations (Planner, Reactor, Pursuer, Conservator), the opposite-pair signatures (Connector, Operator), and the disease / disorder / disorganization line-of-failure taxonomy. Refer back when a constellation or signature in Parts I or II needs its definition or its placement justified.

- **Part IV — The selection cycle.** What one turn of inheritance is made of: the four stages, the four sites they run between, why there are four of each, what each stage discards, and the per-line tables that fill the slots. Refer here when a claim about how a line inherits needs its mechanism.
- **Part V — Maintenance, failure, and the ethics of the tax.** What order costs to hold, what happens when the bill is not paid, and the moral reading the framework's failure taxonomy already carries.

**Authority for framework labels.** The per-cell label libraries — the specific motivation names, capacity names, signature constructs, and breakthroughs at each of the twelve cells — are not in this doc. They live in the **Inheritance_Lines docs** (one per line: genetic, neuronal, symbolic, digital). When this doc references a motivation by name (Persistence, Excitability, Commitment, and so on) or a row-slot label, the authoritative definition is the corresponding line's Inheritance_Lines doc. If a name in this doc and a name in an Inheritance_Lines doc disagree, this doc wins and the Inheritance_Lines doc is the derivative to fix.


# Part I — The deep-time evolutionary story

## Personality as Biographical Signature

What makes trait talk apply to bacteria but not to thermostats?

Both have the cybernetic components. A thermostat has a sensor (the thermometer), a comparator (the rule "above/below setpoint"), an effector (the heater), and a goal (the setpoint). A bacterium has the same four functions, instantiated in different machinery. By the components alone, both should support trait description. Neither does for thermostats. Bacteria do. Bacteriologists routinely describe strains as bold, sluggish, sociable, cooperative, or exploitative, and the descriptions earn their keep.

The difference is inheritance.

Trait adjectives are distributional summaries. Saying a system is "bold" is a probabilistic claim about how it tends to weight action under uncertainty across a class of situations. A distributional summary presupposes multiple situations where the parameter expresses, probabilistic rather than deterministic response, consistency in the pattern, and a reference distribution against which "tends to" is meaningful. The reference distribution is what makes the trait reading possible.

Inheritance creates the reference distribution. It propagates parameters across instances so variation persists; subjects parameter variation to selection so the distribution becomes structured rather than drifting to noise; preserves successful constellations so they appear repeatedly in the lineage; and generates novelty so the distribution stays alive. Without inheritance, the lineage has no parameter distribution; without a parameter distribution, individual readings have nothing to be a position within.

A thermostat lineage does not exist. There is no thermostat-to-thermostat parameter flow contingent on which thermostats functioned well. The variation across thermostats reflects designer choice, not selection. So the cybernetic loop is present, but the biographical structure is not. Trait adjectives describe systems with histories; thermostats do not have biographies.

The biographical signature is what every line has evolved a genre to compress. Humans get obituaries. Bacterial strains get strain reports. Codebases get postmortems. Civilizations get historiographies. Trained models get model cards. Agents get deployment retrospectives. Different names, same form: a small set of characterizing adjectives summarizing how the unit tended across the distribution of situations it occupied. A personality assessment of a living unit is a prospective bet on which adjectives the eventual retrospective compression will land on. Things without biographies get event descriptions instead. Hurricanes get meteorological summaries and thermostats get spec sheets, the genre that fits what they actually are.

This is the structural reason the Trellis Framework's scope criterion takes the shape it does. The framework applies to inheritance-bearing units, systems that perpetuate themselves through environmental coupling, transmitting pattern across time. The criterion excludes thermostats, hurricanes, and rocks not on intuitive grounds but on principled ones: they do not transmit pattern to successors, so there is no lineage for selection to write onto, so there is no biographical signature for trait adjectives to summarize.

The same argument extends the Trellis Framework into lines that are not biological. Code lineages exist (forks, version control, kernel inheritance). Trained-model lineages exist (base weights, fine-tuning chains). Agent constellations propagate (prompt patterns, tool inheritance). The line is engineered at origin, but parameter flow contingent on what works is present. So personality applies, not by metaphorical extension from biological cases, but by the same structural argument that licensed it for bacteria.

**Personality is the biographical signature of a cybernetic loop subject to inheritance.** Wherever both conditions hold, traits apply. Where either fails, they do not.

---

## Cybernetic-Inheritance Foundations

The cybernetic-inheritance claim (surviving lineages are regulators with internalized models of their environments, and the dynamic operates in the same algorithmic terms across lines) has a substantial literature. The Trellis Framework stands in this tradition rather than against it.

The foundations are distributed across several anchors. No single paper underwrites the entire cross-line claim. This is honest: the substrate-independence claim is doing real work and benefits from convergence across multiple traditions rather than dependence on any one of them.

### The Good Regulator Theorem

Conant & Ashby (1970): "Every good regulator of a system must be a model of that system." A regulator that successfully tracks a system must, by theorem, be isomorphic to a model of it. Stated as a formal result, not an empirical generalization.

Applied at the lineage scale: a surviving lineage is a regulator whose continued existence demonstrates successful tracking of its environment. By the theorem, its accumulated parameters constitute a model of that environment. The model is not represented anywhere explicitly. It is distributed across the lineage's inherited architecture, the way the trained weights of a neural network are distributed across its parameters. But it is structurally present, and the lineage's behavior reflects it.

This is the substrate-independent foundation that licenses the Trellis Framework's cross-line claim. Whatever the substrate (DNA, neural pattern, cultural transmission, code), surviving lineages are good regulators of their environments by the same theorem. The architecture is cybernetic at every line by entailment, not by analogy.

*Epistemic status: Conant-Ashby is a theorem with formal standing. Its application to inheritance-bearing lineages is the move the Trellis Framework makes. The application is consistent with cybernetic-inheritance literature (Bateson, Maturana, Friston) but the lineage from Conant-Ashby specifically to that literature is convergent rather than direct. Most contemporary cyberneticists arrive at the result through their own reasoning rather than citing the 1970 paper.*

The lineage's model is implicit, distributed across inherited architecture. It can also take a concrete, locatable form.

Physarum shows this at single-cell scale. A plasmodial slime mold is one large cell, many-nucleated, with no brain and no synapses. Saigusa et al. (2008) exposed the organism to dry-air pulses at a fixed interval, which slowed its movement. After several cycles the cell began slowing in advance of each pulse. It kept slowing at the expected time even when a pulse did not arrive. The period of its environment was held in cytoplasmic streaming and tube-diameter dynamics, not in any neural tissue.

*Epistemic status: the anticipation result is published. Reading single-cell behavior of this kind as memory or cognition is contested in the broader literature (e.g., Gershman et al. 2021). The framework draws on what the experiment shows, a cell whose internal dynamics carry the timing of its world, not on the stronger cognitive interpretation.*

A model grows under rising variety. A larger model needs room to sit in and energy to run. Scale is the eukaryotic answer, the breakthrough the framework names Scale & Size: the lineage builds a cell orders of magnitude larger, with an interior large enough to house a larger model.

The framework holds that mitochondria are the engine of that bigness. Lane argues, in *Power, Sex, Suicide* (2005) and *The Vital Question* (2015), that internalizing energy-generating membranes as mitochondria supplied the energy per gene that made the new size affordable. The careful consensus disputes the strong form — population-geneticists, Lynch and Marinov most prominently, have argued that what looks like an energy story is really a population-size story, bioenergetics no prime mover. The dispute is live; the framework keeps the bioenergetic conviction while acknowledging it. Either way, scale is the room a growing model requires, and stored regulation is the move that precedes the modeling — the model surfaces and grows on top of it, not the other way around.

### Attractors

The Good Regulator theorem (Conant & Ashby 1970) and the Law of Requisite Variety (Ashby 1956) together generate a dynamical attractor. Any unit whose environment outruns its Regulator stored procedures is pulled toward developing Modeler internal modeling, or it dies. There are no other options. The Regulator alone is bounded. Stored procedures cover known cases. As environmental variety grows, the Regulator hits a ceiling. The unit must either develop additional variety or fail at regulation. Failure means the lineage dies. Surviving lineages are the ones that built the Modeler.

Mammalian Modeler did not evolve because mammals wanted to think. It evolved because some pre-mammalian lineages faced environments that outran vertebrate Regulator + Reviser, and the lineages that built the agranular PFC, the limbic system, and the hippocampus regulated those environments. The lineages that did not build the Modeler went extinct or stayed off-thread.

The "must" in "every good regulator must have a model" is this gravitational pull, not a logical tautology. The Regulator is not the Modeler. The Regulator function (stabilization against stored references) is distinct from the Modeler function (internal representation). What the theorems together say is that any unit whose environment exceeds the Regulator's variety is pulled toward developing the Modeler, because the Modeler is the only path to matching the environment's variety. Resisting the pull means dying out.

This is Joseph Campbell's call to adventure operating at the level of evolutionary architecture. The hero in the ordinary world is being pulled toward the special world by forces she does not fully understand. She refuses, then accepts, then crosses the threshold. Most pre-mammalian synapsids refused the call. The ones that crossed the threshold became mammals. The same call sounded earlier for bilaterians (predator-prey arms races demanded vertebrate Regulator) and sounds later for symbolic-line units (settlements introduce the Regulator as Stability, cities introduce the Modeler as Representation, empires introduce the Reviser as Universality).

The Good Regulator theorem and the Law of Requisite Variety together are the gravitational engine of evolutionary complexity. Every line-transition is a unit answering a call it had no choice but to answer if it wanted to keep regulating.

### Requisite Variety

Ashby's second theorem (*Introduction to Cybernetics*, 1956) is the law of requisite variety: only variety can destroy variety. A regulator must have at least as many internal states as the perturbations it can encounter. Holding course against a complex environment requires a regulator at least as complex as the environment's relevant disturbance-space.

This explains evolutionary complexity at the structural level. Lineages do not evolve complexity because complexity is intrinsically valuable. They evolve complexity because regulating against complex environments requires complex regulators. As environments get more variable, regulators must add variety to stay in the game.

The Cambrian explosion is a clean illustration. Predator-prey coevolution drives an arms race. The predator's sensory and motor variety pressures the prey's evasive variety. The prey's evasion pressures the predator's pursuit. The vertebrate Regulator introduction (basal ganglia plus operant conditioning, the Reinforcing breakthrough) emerges in this arms race because animals running model-free reinforcement learning have more requisite variety than animals running pure reflex circuits. Variety in stored procedures matches variety in the environment.

The pattern runs across lines. Eukaryote scale-and-size emerges because regulating multi-component cellular machinery requires more variety than prokaryote regulation can produce. Cities emerge because regulating multi-settlement territory requires more variety than settlements alone can produce. Empires emerge because regulating multi-city populations requires more variety than cities alone can produce. Each line-transition is a variety-jump driven by complexity in the regulated environment that the prior line could not match.

The Good Regulator theorem and the Law of Requisite Variety are two halves of the same architectural claim. The first says regulating requires modeling. The second says modeling must be at least as varied as what it models. Together they explain why surviving lineages are organized the way they are.

### Evolution as Learning

Watson & Szathmáry (2016) demonstrates that evolutionary dynamics and learning dynamics are different instantiations of the same algorithmic principles. Two formal equivalences carry the load:

(a) Bayesian updating is mathematically equivalent to soft selection on genotypes in asexual populations (Harper; Shalizi).

(b) The multiplicative weights update algorithm is mathematically equivalent to selection on individual alleles at linkage equilibrium in sexual populations (Chastain et al.).

Both equivalences are conditional. The Bayesian-asexual equivalence requires that the population be asexual, that genotypes cannot be decomposed into independently fit components. The MWUA-sexual equivalence requires linkage equilibrium, absent epistasis. The conditions matter; the equivalences are not unrestricted.

What the equivalences underwrite, in the form Watson states it: evolution and learning are not merely analogous processes but different instantiations of the same algorithmic principles. Selection is computation; lineages compute over generations the way learning systems compute over training cycles.

The mechanism by which this computation accumulates is gene-regulatory architecture internalizing the correlation structure of selective environments, the way a neural net stores training-set statistics in its weights. Watson et al. (2014) demonstrated, in simulation, that evolved gene-regulatory networks form a distributed developmental memory of phenotypes selected in the past, spontaneously recreating these phenotypes as attractors of development, and generalizing to produce novel combinations of phenotypic modules fit for environments not previously selected for.

*Epistemic status: the formal equivalences are stated by Watson & Szathmáry as established mathematical results, attributed to prior work. The developmental-memory and generalization claims are demonstrated in simulation; the authors flag the extension to biological generality as an outstanding question.*

### Multi-Scale Competency

Levin & Watson (2025) argues for cognition all the way down. Agential competency is present, by degrees, at many interdependent organizational levels of biology. The central architectural claim: there are no dumb parts in biology, because cognition is pervasive and scale-agnostic. Newer levels harness and integrate the autonomy of older levels rather than overwriting them.

Substrate-independence is a central conceptual move in the paper: connectionist learning principles can be implemented in many physical systems from gene networks to protein networks to ecosystems, and Hebbian learning can be demonstrated in non-neural and non-biological systems. The scope as the authors define it is biological-organizational levels plus computational hardware.

For the Trellis Framework's purposes, the paper underwrites scale-free competency from the genetic through the neuronal line, plus silicon. It does not address symbolic or cultural inheritance directly. Extending the cybernetic-inheritance claim into the symbolic line requires additional anchors.

*Epistemic status: the paper is an OSF preprint (May 2025). The multi-scale competency claim is asserted with explicit hedging on degree (cognition has degrees of relevance, not equally meaningful at every scale). The substrate-independence claim is well-developed within cell and developmental biology and computational hardware; the symbolic line is out of scope for this paper.*

### Free Energy and Active Inference

The free energy principle gives a substrate-independent formulation: any system that maintains itself against entropy must minimize a quantity equivalent to free energy, which can be decomposed as expected free energy into pragmatic value (preferred outcomes) and epistemic value (information gain). Safron & DeYoung (2021) maps this onto CB5T's metatraits: the Stability metatrait tracks pragmatic value (precision over preferences, the C matrix); the Plasticity metatrait tracks epistemic value (precision over policies).

For the Trellis Framework, FEP operates as a substrate-independent principle that applies wherever a system maintains itself against entropy, compatible with cybernetic-inheritance at every level. Active inference is the specific mammalian instantiation. Other lines run other line-native machinery: ratcheting at protocell, state-dependent gating at prokaryote, associative learning at bilaterian, reinforcement learning at vertebrate, gossip-tracked social debt at band, code-tracked obligation at city.

The Regulator and Reviser are cross-level structural roles. The machinery implementing them changes by level.

Safron & DeYoung is the strongest existing precedent for grounding CB5T's metatraits in cybernetic-architectural terms. They did that work in detail, with neurobiological grounding, and proposed a methodology (P-structures) for operationalizing it. The Trellis Framework inherits the empirical and theoretical apparatus, cites heavily, and does not duplicate.

### Earlier and Adjacent Traditions

Bateson (1967, 1972, 1979) gives the earliest sharp formulation of the cybernetic view of inheritance, information as restraint, surviving lineages as the residue of a process that ruthlessly enumerated and excluded alternatives. Uexküll's umwelt theory (1934) supplies the environment-construction piece that requisite variety leaves implicit: the regulator regulates against the organism-relative perceptual-effector world, not against objective physical reality. Maturana & Varela's autopoiesis is structural to the Trellis Framework's scope criterion (self-maintaining environmental coupling). Pattee on semiotic closure: biology as hierarchical self-modeling. Jablonka & Lamb (2005) on multi-track inheritance (genetic, epigenetic, behavioral, symbolic) carries the symbolic-line extension that Levin & Watson does not address. Deacon (*Incomplete Nature*, 2012; Shannon-Boltzmann-Darwin, 2007\) provides the entropy-reduction framing the framework's scope criterion follows.

The Trellis Framework inherits from all of these. The framework's distinctive contributions sit on top, not against.

---

## What Lines Are Made Of

These commitments define what each line is and what it does: the inheritance modality it runs on, the heritable unit it names, the kind of goo it ratchets, its variation-selection cycle, its pre-line groundwork, the machinery that instantiates the cybernetic dynamic, and the test for what would count as a new line. The cross-line cybernetic claim they rest on — surviving lineages as good regulators with internalized models — is grounded above and in Part III below.

### Inheritance Lines

Each line is a distinct inheritance modality, a way of moving information across time that wasn't available before:

- **Genetic** stores information in nucleic acid, transmits via reproduction, modifies through mutation and selection. It ratchets Boltzmann goo.
- **Neuronal** stores information in neural patterns, transmits via behavior and learning, modifies through experience. It ratchets Kullback-Leibler goo (the relative entropy between what the world delivers and what the agent's generative model expected).
- **Symbolic** stores information in network-defined signs, transmits via teaching and copying, modifies through cultural innovation. It ratchets Shannon goo.

### The Heritable Unit Each Line Ratchets

Each line names a unit of inheritance — the smallest thing the line copies, varies, and selects.

- **Genetic — the gene.** The molecular replicator: a heritable set of instructions in nucleic acid.
- **Neuronal — the neme.** The reinforced operant: a unit of behavior selected by its consequences within a lifetime (the name is built from Semon's *mneme*). The neme matures across the neuronal line, from the bare reinforced operant to a unit revised against an internal model.
- **Symbolic — the meme.** A unit of culture copied between agents. *Meme* here is the unit itself; a meme-complex is the fauna built from memes, the superorganism sense used elsewhere in this doc. Unit and fauna are different levels, not competing definitions.
- **Fourth — held as a program.** Its unit is the program, a generative set of instructions in the engineering sense, outside the *-eme* family.

A seed carries no picture of the plant. It is not a description of a finished stem that the growing then tries to match. It is a set of instructions that, run in soil, produces a stem, and nothing in the seed knows what that stem will look like or how far it will reach. The reach is settled afterward, by the soil, by the clearing, and by what earlier growth left standing.

This rules out any name for the unit that implies a drawing was made first. A drawing has someone who drew it, working toward a result held in mind beforehand. Gardens are tended that way. Nobody tends the liana. So the unit at every line has to be the seed and not the drawing: something that runs and produces, with no foresight of the product and nobody behind it who wanted that product. A candidate name that smuggles in someone who wanted the outcome fails on that ground alone.

At most lines the seed and what the seed is written on come apart. A seed weathers, is half-eaten, is read wrong. The instructions inside it and the husk carrying them have separate fates, and the difference between them is measurable because it shows up as damage.

At the digital line every copy is exact. Nothing can happen to the husk that does not happen to the instructions, so the two stop having separate fates and there is nothing left between them to measure. Seed and inscription fuse. That fusion is not the figure wearing thin at its last line. It is what copying without loss means, said in the figure's own terms: lossless copying is precisely the condition under which a carrier stops being a separate thing from what it carries.

The lines differ in where inheritance is located. The genetic line inherits across the germline, between generations. The neuronal line interiorizes inheritance into the single agent's repertoire, so its inheritance is lifetime-bounded: the neme is selected and retained within one life and does not, by itself, cross to the next. The symbolic line externalizes inheritance again into a shared corpus that outlives any agent. Germline, lifetime, minds, corpus — the locus moves out, in, and out again.

Because the neuronal line interiorized inheritance into a single life, it had to interiorize selection too. The neme's selector is attention: the contest in which candidate behaviors compete for expression, scored by reward and retained by consolidation into an engram. Attention and reward are the competition-arena and the fitness-criterion of a within-lifetime Darwinism, the way the environment and differential survival are the genetic line's. This is the evolution-as-learning equivalence recorded above, run inside one agent. Attention is the neuronal line's selector across all four of its cells. It founds at the Bilaterian, the line's first cell, and runs from there to the Primate. Attention selects by competition, not by allocation. Candidate behaviors carry weight in proportion to their goal-relevance; the candidate with the most weight wins expression, and the margin by which it wins is set by how concentrated or spread the weighting is across the full candidate set. Nothing is drawn down or used up in the winning. This is a structural claim, not a metaphor: the same competition-and-normalization dynamic recurs at every neuronal cell from Bilaterian through Primate, sharpening and generalizing but never changing kind. *Epistemic status: the competition/normalization framing is a framework theoretical commitment, consistent with contemporary selection-based accounts of attention (Logan 2026) but not itself requiring their endorsement — Bramble instantiates this claim as fictional architecture, not as a settled empirical verdict.*

*Epistemic status: the gene as molecular replicator (Dawkins) and the meme (Dawkins) are established usages; the neme — the reinforced operant as a within-lifetime replicator, with attention as its selector — is a framework-native naming built on Skinner's selection-by-consequences and the operant/reinforcement-learning machinery already placed at Vertebrate. The locus progression is a framework theoretical commitment. The fourth unit is the program.*

### The Neme, Developed

It matures across the line, operant to internal model. The model-free reading (Vertebrate, Reinforcing) gives the operant, selection on overt behavior. The model-based reading (Mammal, Simulating) gives a second form of the same logic, the tested hypothesis, Popper's "let your hypotheses die in your stead," selection on simulated behavior before a body is committed. The neme matures from operant to internal model, tracking the within-line move Vertebrate to Mammal, the way the meme matures across its own cells from Conversation to Stories.

Dennett's Tower is the backbone for the whole inheritance arc. Generate-and-Test runs Darwinian, Skinnerian, Popperian, Gregorian, and that maps onto the lines almost one to one: Darwinian is genetic, Skinnerian is the neuronal model-free neme, Popperian is the neuronal model-based neme, and Gregorian, named for Richard Gregory's mind-tools, is the symbolic meme. The Tower places the neme in a principled sequence and ties the arc to a named framework rather than an ad hoc one.

The neme is what is inherited. The engram is where it is written: Semon's other 1904 coinage, the physical memory change an experience leaves behind, and now an active research object in its own right, localized and manipulated in identified cells (Tonegawa). The two are not rivals, and the line keeps both words. Naming the unit after the engram would name it after the place a thing is stored rather than after the thing, which is the error that calls a gene chromatin.

A boundary to keep. Temperament is not the neme. Temperament and behavioral syndrome are substantially genetically heritable, the genetic line's reach into the neuronal machinery, the parameter settings that bias which operants get learned. The neme is the *learned* policy, the line's own acquired replicator. Keeping these separate matters.

Transmission: operant, then tradition. Genes cross between bodies; memes cross between minds. The neme uses two channels, and they are ordered rather than rival.
- *Within a lifetime,* via memory. The neme passes from past-self to future-self by consolidation. This is the cleanest distinction from both neighbors: the neuronal line is the first line where an agent inherits from its own past, interiorizing inheritance before the symbolic line re-exteriorizes it. On its own it does not accumulate across generations, which is exactly what the second channel adds.
- *Across generations,* via animal tradition. Socially-learned behavior (birdsong dialects, tool-use cultures, foraging traditions; Whiten, Laland) accumulates across generations without symbols, giving the neuronal line a between-agents channel parallel to genes and memes. It stays distinct from the meme by a sharp criterion: transmitted by imitation of behavior, with no shared symbol system or we-mode.

Both hold, in order. The operant is the within-lifetime neme; the animal tradition is the socially-learned operant, the bridge residue the symbolic line inherits and symbolically encodes. The progression operant to tradition to meme lands exactly on the Primate-to-Bands handoff, the Sociometer's social reflexes becoming culture. It is not either/or; it is the maturation of the neme into the meme.

The neuronal line's inheritance is lifetime-bounded. It accumulates across deep time only by borrowing a neighbor's channel: genetic assimilation (the Baldwin effect) downward, or animal tradition and culture upward. Genes and memes accumulate on their own across generations; the operant, alone, dies with the organism. This is the line whose inheritance cannot escape the lifetime without help, and it is the structural counterpart to the within-lifetime selection attention performs: a line that inherits inside one life also selects inside one life.

### Attention, Developed

The mechanism is scarcity. Selection bites only where a limited resource forces competition; in the genetic case that is finite carrying capacity. The neme's scarce resource is attention, one body, one action channel, a bounded workspace. Many operants are always live; only some win the workspace, drive behavior, and earn the reward that consolidates them. Attention is the bottleneck they compete through, which is the biased-competition account (Desimone and Duncan) and the global workspace (Baars; Dehaene) read as a selection arena, in the spirit of William James's original definition of attention as taking possession of one object out of several possible. Attention is the carrying capacity of the neme's Darwinism. The framing is Donald Campbell's: blind variation needs a selective-retention filter, and at the neuronal line attention is that filter's gate.

This is not neuronal-specific. Every line's selector (differential reproduction at genetic, attention at neuronal, differential adoption via joint attention at symbolic) runs the same four function-biases: recency (Effector), familiarity (Regulator), potency (Modeler), novelty (Reviser). Pavlov's heuristics are the neuronal line's name for these; the genetic line runs them as differential-reproduction biases, the symbolic line as differential-adoption biases. One set of biases, three selectors.

This is not grafted onto the framework: it is already in the goo. The neuronal goo is Friston's free energy, and in active inference attention is precision-weighting, the gain on which prediction errors update the model and select the policy. The machinery the neme is selected in carries attention as a native parameter. The Regulator line regulates by allocating precision, and which neme regulates is set by where precision goes. Edelman's Neural Darwinism gives the same shape one level down: variation and selection among competing neuronal groups, which is what an attentional contest is in the tissue.

It also firms the neme's selection step. The division of labor: attention is the competition arena (what gets expressed and competes) and reward is the fitness criterion (which expressed variant is retained). Attention runs the contest; reward scores it; consolidation writes the winner to the engram. Together they are the neuronal line's within-lifetime Darwin, with behavioral exploration on the Explorer edge as its blind variation.

One disambiguation. "Attention" names two things at different points of the loop. Attention as resource (the bounded workspace) is the selector. Attention as spotlight (what is attended to now) is the phenotype of whichever neme just won. The faculty selects; the spotlight is the readout.

**Where attention goes across the lines** (the symbolic step is firm; the digital line's selector is the open sub-question). Internalized selector at the neuronal line; then *joint* attention at the bridge to the symbolic line, where shared attention is the groundwork of the we-mode and the public focal point Common Knowledge runs on; attention externalizes again as the symbolic line picks it up. The digital line's selector has human attention as its candidate: the attention economy as its selection environment, which would make attention the selector at both ends, brought indoors at the neuronal line and the scarce thing blind digital variation competes for at the far end.

*Epistemic status: attention as selection (James, biased competition, global workspace) and attention as precision (active inference) are established. Attention as the neme's internalized selector, and its extension into joint attention at the symbolic bridge, are framework theoretical commitments, well-motivated by the Friston goo.*

### Each Line Ratchets a Different Kind of Goo

*A note on the word.* Throughout this doc, *goo* is the term for the stuff each line works — the medium each inheritance line acts on and ratchets.

The cross-line architecture has the same cybernetic decomposition (Effector, Regulator, Modeler, Reviser) at every line, instantiated in line-specific machinery. The line-specific machinery differs because each line is a different kind of goo-ratchet. Same architectural function, different goo being ratcheted.

The three kinds of goo:

- **Genetic line ratchets Boltzmann goo.** Life maintains itself far from physical equilibrium. Cells, organisms, and lineages are constellations that ratchet thermodynamic disorder by importing low-entropy energy and exporting high-entropy waste. Selection preserves the constellations that ratchet best.
- **Neuronal line ratchets Friston goo.** A system that persists must keep itself in a narrow set of expected states; it minimizes an upper bound on the surprise that would measure this directly — variational free energy, in the form *complexity minus accuracy*. Perception lowers it by updating the model; action lowers it by changing the world to match the model. The result is an agent that resists dispersion into improbable states. Affective and motivational structure (sensorimotor reentrant signaling shaped into trait-level dispositional architecture, empirically documented from vertebrates up) is what running Friston goo looks like at the unit level. The Venn of Lines section below gives the full argument; this row records the line-level commitment.
- **Symbolic line ratchets Shannon goo.** Symbols are constraints on signal-space. Lexicons, grammars, conventions, and pragmatic norms each reduce the space of legitimate messages by large factors. Cultural transmission preserves the constraints that work for coordinating groups. Empires ratchet the random message-space into shared symbolic systems.

Each line does the same Darwin-level goo reduction (selection-mediated pattern preservation) at the line level, but on a different kind of goo at the unit level. This explains why the lines are genuinely different despite sharing cybernetic architecture. Same cybernetic structure, different goo, different mechanisms, different timescales.

*Epistemic status: the genetic-line Boltzmann-goo claim follows from Deacon's Shannon-Boltzmann-Darwin framework (2007a, 2007b, 2012). The neuronal-line Friston-goo claim sits on the variational-free-energy formalism (established as formalism; the line-goo reading is a framework commitment); the behavioral-syndrome literature (Sih, Bell & Johnson 2004; Koolhaas) supplies the empirical-trait surface. The symbolic-line Shannon-goo claim is a framework-native application of the same principle.*

### The Seam: What Maintenance Holds Invariant

*"Good seams make good neighbors." After Robert Frost, "Mending Wall," itself a poem about the tax of keeping a boundary.*

Maintenance is not the freezing of everything. A unit that held every part rigid could not vary at all, and could not be repaired part by part. Maintenance holds invariant a specific, sparse set of parts, so that change elsewhere does not destroy the unit. Those held-invariant parts are the panels; the places where change is allowed are the seams.

The seam is a thin link. Kirschner and Gerhart call it weak regulatory linkage: a connection that carries almost no information, a switch rather than a specification, so that either side can be rewired without redesigning the other. The conserved core processes are the panels, the deeply reused machinery that never gets touched. A good seam sits where the unit already articulates, at a joint the structure has rather than a cut made against the grain.

Each goo has its own seam, its own thin switch. These are the ratified anchors, one per line.

- **Genetic goo: the enhancer.** A cis-regulatory switch decides where and when a gene fires without altering the gene. The stickleback loses its pelvic spine by deleting one tissue-specific enhancer while keeping the gene it still needs elsewhere. The enhancer is the genetic crease: change lands there, the coding panel holds.
- **Neuronal goo: the calibrated cortical setting.** The neocortex runs one shared circuit, the same excitatory and inhibitory cell types in the same layering, tiled across every area. What redeploys that shared circuit for a local job is a thin regional setting, spine density and the excitation-inhibition ratio varying along a gradient, which on crossing a threshold makes the same circuit compute something new: working memory in association cortex, feature detection in early sensory cortex. The setting is the neuronal enhancer. It redeploys conserved machinery without rewriting it, the way a cis-regulatory switch redeploys a gene.
- **Symbolic goo: the arbitrary sign.** The link between a sign and its meaning is conventional, not fixed by either side, so a word can be reassigned or extended to a new job without rebuilding sound or sense. Polysemy is the symbolic enhancer: one word does many jobs, each gated by its own context, each reworkable alone.
- **Digital goo: the crease.** In the crease pattern the fold lines carry the articulation and the panels stay rigid, which is the origami identity given in "The Mirror: Two Poles, Two Functions" (Part III).

The genetic seam closes too, and its closing is the older, better-named case. Every cell carries the same genome, so the genome is the shared machinery; what redeploys it for one cell's job is the epigenetic state, the pattern of methylation and chromatin that switches genes on and off without touching the sequence. That state is a maintained switch. At each division the epigenome is copied onto the daughter strand, which is how a liver cell stays a liver cell across a lifetime of divisions without editing its DNA. The epigenome is the genetic line's homeostat, and what it maintains is which seams are open. Differentiation is the switch closing: Waddington's landscape names it, the cell rolling into a canalized valley, chromatin condensing into its identity, the state holding and resisting return. Reprogramming a cell back toward a stem state is reopening that window, the genetic-line counterpart of reopening a sensitive period. So the enhancer is where the genetic seam is placed and the epigenetic landscape is how it is set. The modern dissolution of the gene as a tidy discrete unit says the same thing from the other side: the coding sequence is the panel, and regulation is the seam.

The neuronal seam closes the same way, and there the cut-and-set operation has a precise molecular mechanism: the sensitive period. Experience opens a window: parvalbumin maturation triggers onset, perineuronal nets brake closure. Pruning then sharpens selectivity without changing what the circuit computes, using far fewer connections for the same task, so the reward system still learns reward and the whisker map still maps whiskers. Closure locks the setting into structure, so it cannot be dialed back without reopening the window. This is the neuronal line's version of a fold that holds once made, and it settles what the earlier precision reading was reaching for: precision-weighting is the runtime face of the same regional setting the sensitive period fixes in place, the moment-to-moment expression of a seam that development already cut. At the level of wiring rather than circuit the same organization shows up independently, the connectome partitioning into dense communities linked by sparse ties, and the network-neuroscience literature ties those low-traffic between-community boundaries to the same evolvability Kirschner and Gerhart named.

That the neuronal seam exists at all depends on the machinery being shared, and this is general. A seam needs a reused unit to switch. Where every function had its own dedicated module, as faculty modularity claims, nothing would be shared, nothing could be cheaply redeployed, and there would be no thin switch to cut. The evidence against a modular cortex is therefore evidence for a seamed one. The pattern holds across all four goos: the enhancer needs a reused gene, the sign needs a reused signifier, the crease needs one sheet, and the cortical setting needs one shared circuit. Faculty modularity is the anti-seam architecture, which is why the framework does not adopt it.

Evolvability is good seam placement, and it is where the maintenance pole hands something to the variation pole. But the seams are not placed by foresight reaching for future variation, because nothing in blind evolution reaches forward. They fall out of paying less. Connection cost is the visible tax (see "The Visible Tax," Part V) at its most literal: wiring is anti-entropic work paid to build and to maintain every cycle, in volume, in conduction delay, and in metabolic upkeep, which Bullmore and Sporns call the economy of the brain. Clune, Mouret, and Lipson evolved networks under selection for performance alone and got no reliable modularity; add a penalty on connection count and modularity appeared on its own, and the modular networks turned out to be more evolvable. So the causal order is clean, and it keeps each function in its place: Darwin, at the center, selects on cost; the Regulator economizes the maintained architecture to meet it; re-cuttable seams fall out as a byproduct; and the Reviser is freed to cut them. Evolvability is never the target of selection, only what rides along when maintenance is made cheap. The maintenance pole places the seams the variation pole uses, which is the internal dynamic of the whole Operator diagonal. Modularity is then the survivorship signature of which cheap-to-maintain architectures also proved cheap to re-cut when the world moved. Wagner and Altenberg describe the two shapes a clean seam takes once it has arrived, parcellation and integration, the cross-links between functional complexes severed or the links within one tightened.

The same runs at the genetic line, where the tax already has a name. A toolkit gene like Pitx1 or Pax6 is reused for many jobs across the body and across deep time, which is what makes it cheap to keep and expensive to change, because one edit to its coding sequence strikes every job it does at once. That coupling cost is pleiotropy, and pleiotropy is the genetic form of connection cost. Evolution pays it down the same way it pays down wiring, by putting a separate regulatory switch on each deployment, so one job can be re-cut without disturbing the others. This is why the genome's regulation is modular while its coding units are shared: the modular layer of switches exists to redeploy a shared gene without collateral damage, and those switches sit where they do because they lower the cost of the sharing, not because the flexibility they later supply was selected for. Modular genome and shared gene are therefore one fact, the same one the connectome and the canonical circuit are: a modular layer whose whole job is to deploy a shared unit cheaply.

The symbolic line's organisms are not only words but institutions, and the seam runs at both levels. A word gets its evolvability from loose reference and reuse, which let meanings be re-pointed and stretched without rebuilding the language, and the institution repeats the move one level up. There the shared unit is the office. A presidency persists across presidents and a judgeship across judges, so the office is the panel and the holder is the deployment, and the seam that swaps them is the election, a thin periodic switch that changes the government without changing the regime. The connection cost is concentrated power: an office that does too many jobs is institutional pleiotropy, because striking it strikes everything, and no one function can be reformed without deforming the rest. The modularity that pays that down is separation of powers, which is functional, and federalism, which is spatial, dense authority inside a unit and sparse across its boundary. Reformability then rides along free, the same byproduct as at every other line: the separated powers were placed to stop any one office from striking everything at once, and the capacity to reform one branch without collapsing the whole fell out of that. Madison and Clune are making one argument.

Degeneracy is the mechanism that gets robustness and evolvability at once. Degeneracy is not redundancy. Redundancy is identical backups; degeneracy is structurally different parts that can cover the same function. A degenerate architecture maintains itself when a part fails, because another kind of part takes the load, and it varies well, because the spare parts are raw material for new functions. Degeneracy is how a unit keeps the panels holding while the seams stay open. The genetic code is the textbook case: many codons map to one amino acid, so most single-letter changes are silent, and the code is at once robust to error and free to wander.

How much disturbance maintenance can absorb depends on whether it can re-reference. A Regulator that defends one fixed reference gives engineering resilience: fast return to a single setpoint, and brittleness the moment the world leaves that setpoint's range. Coupling maintenance to revision gives ecological resilience: the unit shifts to a different stable state and persists across a band of conditions rather than one. Engineering resilience is the panel holding; ecological resilience is the panel that can be re-creased when the load changes. This is the first place the two poles (see "The Mirror: Two Poles, Two Functions," Part III) need each other, because ecological resilience is maintenance that has borrowed the Reviser.

The digital line is where they need each other most. Its unit is the program, the shortest code that produces a structure, and it is the Reviser line, the tree's variation function, so its native work is generation. Here the maintenance tax and the variation goo stop being two quantities. The goo is Kolmogorov complexity, which is description length, and the way a blind digital process gets cheap is by shortening that same description. Reuse is how a program shortens: store a function once and refer to it many times rather than writing it out at each use. So compression, cost, and modularity become one move, and the byproduct account stops being a mechanism and becomes an identity, minimizing the tax being the same act as compressing the program being the same act as factoring it into reusable parts. This is the first pole, source coding, and at it the origami identity (Part III) becomes exact rather than figurative: compression and seam placement are literally the same operation.

The second pole runs the other way. A program also has to survive copying, and copying runs over a noisy channel, so persistence at the digital line means adding structured redundancy back in, error-correcting code that lets the program be reconstructed intact after noise. This is channel coding, and it is what lossless copying is made of. It is also what lifts the ceiling: the other three lines copy lossily, errors accumulate across generations, and that degradation is the cap on how complex an inherited thing can get. Pay the error-correction tax in full and the cap lifts, which is why the digital line is the unbounded one. Lossless copying, the line's defining signature, is a maintenance achievement, the noise that limits every other line finally defeated.

The two poles trade against each other, and here the tradeoff is exact rather than a gesture. Compression removes redundancy; error correction adds it back; every bit spent making the copy robust is a bit not spent making it short. Shannon's separation of source coding from channel coding is that budget written down, rate against reliability. At the biological lines the same tension was real but unquantified, a golfed viral genome that is brittle set against a bloated eukaryotic one that is robust, with no clean accounting between them. At the digital line it is the clean accounting. So the fourth line is where the two poles stop being a mirror and become a single conserved budget: the variation pole wants the program short, the maintenance pole wants the copy safe, and a fixed rate has to be split between them. It is fitting that this happens at the Reviser line, where variation is the line's whole identity and maintenance is the tax it must pay to persist at all.

The two measures in that budget are not the same kind of thing, and keeping them apart is what makes the accounting honest. Kolmogorov complexity is a property of a single object: the length of the shortest program that produces it, with no distribution anywhere in it. Shannon's rate is a property of an ensemble: bits per symbol averaged over a source that emits many messages. The separation theorem is an ensemble theorem, and it is what makes the split exact. So the fixed rate the two poles divide is Shannon's, and the exactness the digital line gains is Shannon's exactness. The same tradeoff does hold object by object, because a program written to survive noise is written longer, and a longer program has a longer shortest description. What it does not have there is a theorem to close it, or even a computable price, since K is uncomputable. The two measures meet asymptotically, the expected shortest description of a message from a computable source converging on the source's entropy, which is why one accounting can run over the other's goo without lying. Kolmogorov names what the line ratchets. Shannon prices what a copy costs.

*Epistemic status: the enhancer seam, degeneracy, the epigenetic maintenance of cell state, Waddington's landscape, and DNA repair and CRISPR immunity are established biology. The shared canonical circuit, sensitive-period calibration, and pruning-tunes-selectivity are the mainstream neuroscience reading; the one live counterpoint is primary sensory cortex under early deprivation, where whether repurposing is genuine or potentiation of pre-existing wiring is unsettled, which touches the bottom of the hierarchy and not the shared-circuit claim above it. Reading the epigenome as the genetic line's homeostat, and the four seams (enhancer, calibrated cortical setting, arbitrary sign, crease), are committed framework mappings. The byproduct account of evolvability, seams placed by minimizing the maintenance tax, is committed and runs at three lines: connection cost in the brain, pleiotropy cost in the genome, concentrated-power cost in institutions, following Clune, the economy-of-the-brain literature, and the demonstration that regulatory-network modularity emerges from specialization and cost. The digital capstone is committed with the rest: Shannon's coding theorems and Kolmogorov complexity are established mathematics, and the digital line's two poles are the framework's maintenance and variation made into one budget.*

### The Four Functions as the Variation-Selection Cycle

The Effector-Regulator-Modeler-Reviser cybernetic decomposition is not just four cybernetic functions held alongside each other. It is the variation-selection cycle made architectural:

- **Reviser is variation.** The undirected supply the rest of the cycle works on.
- **Modeler is modeling.** Internal representation of what the ratchet produces.
- **Regulator is stabilization.** Regulated control against stored references.
- **Effector is the selection-outcome.** What propagates when the ratchet meets Darwin.

**What the ratchet word commits to.** A Brownian ratchet has three parts: undirected variation, a rectifier that lets motion through one way and blocks the other, and free energy spent to reset the mechanism each cycle. Feynman's ratchet-and-pawl exists to show the first two are not enough. At thermal equilibrium the pawl gives no net motion, and without the paid reset the device is a perpetual motion machine. The framework's use of the word means all three.

The three parts sit in three different places. The Reviser is the variation. The gate at Retention is the rectifier. The maintenance tax is the reset, set out in Part V. The ratchet is therefore the whole loop and not any one function in it.

The rectifier is Retention and not all four stages. Every stage narrows, but narrowing inside a turn does not accumulate, because the next turn draws fresh from the store. Only Retention writes to the store, and running one way is a between-turn property.

The rectifier has two phases rather than one catch. A tendril coils before it commits: the first hold is carried by turgor and comes undone when the plant dries, and only later does the core lignify into a hold that no longer depends on water. A gate that can decline needs the provisional phase, and the transition between the two is what costs.

*Ratified mapping. Transfers: the three parts, the necessity of all three, and the result that a device without the reset is a perpetual motion machine. Does not transfer: a designer, a purpose for the motion, or a chosen direction. The Brownian ratchet is the safest machine word available here because its whole content is that the machine does not run for free. The three-part structure is established physics, after Smoluchowski and Feynman; placing the three parts on the Reviser, the gate, and the maintenance tax is framework. The tendril's two phases are established botany (Klimm, Speck and Thielen, Advanced Science, 2023): in the free coiling phase the spring's tension and its form still depend on turgor pressure, and in the stabilization phase the center lignifies and the form holds independent of hydration. Reading the provisional phase as what lets a gate decline is framework.*

Each line runs the same four-part cycle on its goo. Boltzmann thermodynamic chaos becomes variation through self-production, modeling through interiority, regulation through coordination, and selection of fitness. Same cycle, four times, four kinds of goo.

This is why Reviser motivations introduce at the end of the prior line and carry as Reviser of the new line. They are the goo the new line selects on. This is also why Effector and Reviser sit at opposite ends of the variation-selection cycle. Reviser generates variation. Effector is the selection-outcome. They are the two ends of the cycle.

The Reviser motivation of each line names the goo each line ratchets. The Effector motivation names what Darwin selects on it:

| Line | Reviser motivation (goo) | Darwin-on-goo | Effector outcome |
|--------|--------------------|---------------------|------------|
| Genetic | Self-Production (Boltzmann goo) | thermodynamic selection | Persistence |
| Neuronal | Excitability (Kullback-Leibler goo) | prediction-error selection | Impetus |
| Symbolic | Affiliation (Shannon goo) | exchange-based selection | Commitment |

The mapping at genetic is cleanest. Self-Production directly names Deacon's teleodynamic goo-ratchet work. The mappings at neuronal and symbolic require reading Excitability as FEP-flavored active engagement and Autonomy as self-revising symbolic constraint. These require interpretation, but they are not strained. Framework concepts often unify multiple aspects of a phenomenon.

The Regulator and Modeler positions also gain principled architectural roles under this reading. They are the stable structures that emerge between variation and selection: stored models (Modeler) and stabilized regulation (Regulator). The full architecture is variation, then modeling, then stabilization, then selected outcome, running on each line's goo.

The goo-ratchet wears a better image than the machine word suggests: the fertilized egg. Variation at a line boundary is the carried Reviser motivation of the prior line — Excitability out of the genetic line, Affiliation out of the neuronal — entering the next line as the goo it will select on. That carried variation is blind and unbound, and most of it does not take; Darwin selects the little that implants as the next line's founding Effector. The egg names the vulnerability in this. A fertilized egg is the product of recombination, blind variation with no foresight; it is unbound, not yet implanted; and most eggs never implant at all. The founding Effector it can become is raw — its evolutionary signature is a regulatory layer not yet stabilized — so a line begins at its most exposed. The risk is structural, not incidental: the culmination of one line is the infancy of the next, and infancy is where a line is most easily lost.

### The Three Kernels

Three of the framework's Reviser cells are already realized, each a blind, unbounded peak within its own line, before the wraparound binds it into the next line's founding Effector.

**Eumetazoa, the blind, unbounded genetic line.** Reviser motivation Excitability; the bridge residue is the Reflex Repertoire. The genetic line's engine is heritable variation; at its Reviser cell the engine turns on multicellular organization itself, through differentiation, the Reviser's literal evolutionary signature, division of labor among parts. Run unbounded, that is the Cambrian explosion of body plans. Run blind, it is variation without foresight, most of the disparity pruned by extinction. The residue is excitable nervous tissue, which the neuronal line inherits and organizes into a brain.

**Primate, the blind, unbounded neuronal line.** Reviser motivation Affiliation; the bridge residue is the Sociometer. The neuronal line's engine is modeling; at its Reviser cell it turns modeling on other minds and on its own modeling. Run unbounded, that is the social-brain arms race, deeper mentalizing selecting for deeper mentalizing with no recursion ceiling. Run blind, it is a fitness-blind runaway, the line trades ecological range for cognitive depth and pays in lost territory. The residue is the social-reflex repertoire, which the symbolic line inherits and organizes into a superorganism.

**Empire, the blind, unbounded symbolic line.** Reviser motivation Universality; the signature is Identity. The symbolic line's engine is shared representation; at its Reviser cell it turns representation universal, into self-propagating meme-complexes that scale past anyone who could vouch for them. Run unbounded, that is universalizing ideology, open-ended and recombining. Run blind, it is the framework's non-sentient fauna: the meme-complex propagates by differential survival among ideologies, indifferent to the welfare of the constituents it runs on. The residue is the externalized, universalized symbolic corpus, which the fourth line inherits.

### The Three Darwinisms

Three claims about selection are easy to blur. Naming them is the wall.

Selection for fitness is the standard claim, and it sits at the center: variation plus the selective retention of what works, which increases fit across a lineage. It is Darwin, the breakthrough at the center of the Venn, not one of the two poles, and it is developed above as Donald Campbell's selective retention alongside the variation function (see "The Four Functions as the Variation-Selection Cycle" and "Why the Cycle Turns: Absence Recruits"). It is not re-argued here.

Selection for evolvability takes the byproduct form rather than the direct one. The vulnerable version says evolvability is itself a target of selection. The framework does not need that. It says instead that minimizing the maintenance tax produces re-cuttable architecture on its own, and evolvability rides along. So the map from variation to outcome is shaped, and seams do end up where functionally related parts vary together, but by cost pressure from the maintenance pole, not by the center reaching forward for future variation. What is asserted at full strength is that the seams are real and load-bearing; what is dropped is the claim that they were selected for.

Allocation is the third claim, and it is a different axis. It asks how much of a finite budget a unit spends maintaining itself versus spending on the next copy. This is disposable soma, and it is not about how a unit maintains but about how much it maintains at all. It is named here and deferred, because folding it into the maintenance axis would blur a knob with an axis.

*Epistemic status: the three-way distinction is a framework discipline commitment. The placement of fitness above, evolvability here, and allocation in future work, is settled.*

### Each Line Has Its Own Pre-Line Groundwork

Deacon's pre-life dynamics (homeodynamic, morphodynamic, teleodynamic processes) are the pre-line groundwork of the genetic line, the groundwork that prepared chemistry for life. This pattern generalizes. Each line has its own pre-line groundwork that did the goo-ratcheting work that prepared the line for emergence. Each line's pre-line groundwork is the prior line's mature output, which closes the loop.

- **Pre-line groundwork of genetic:** Deacon's homeodynamic, morphodynamic, and teleodynamic processes. Thermodynamic ratchets that prepared chemistry for life.
- **Pre-line groundwork of neuronal:** pre-neural sensory and behavioral coordination in early multicellular organisms. Affective ratchets that prepared bodies for brains.
- **Pre-line groundwork of symbolic:** pre-symbolic animal signaling, indexical and iconic reference. Shannon ratchets that prepared cognition for symbols. Deacon's *Symbolic Species* (1997) details this transition.

### The Structural Mirror and the Domain Shift

Two patterns run together at every line.

**Pattern 1: structural mirror.** Each line repeats the same cybernetic decomposition (Effector, Regulator, Modeler, Reviser). The cybernetic structure is the same at every line because it is the minimum cybernetic decomposition.

**Pattern 2: domain shift.** Each line's primary domain of action is the goo of the line one level back. The unit at each level acts on the prior line's goo, even while it is built from that goo. Genetic units act on chemistry. Neuronal units act on biology, navigating ecological niches and finding food. Symbolic units (bands, cities, empires) act on cognition, shaping member minds via stories, norms, codes, and institutions.

The two patterns run together because the new line emerges precisely when the prior line's goo becomes complex enough that a specialized control layer is worth its overhead. Neuronal systems emerged when bodies became complex enough that distributed neural coordination paid off relative to its metabolic cost. Symbolic systems emerged when groups became complex enough that culture-based coordination outpaced direct social learning.

The framework's flora-and-fauna picture encodes this pattern. The body is genetic-line flora. Once the brain emerges, the body is what the brain rides on and operates on. Cognition is neuronal-line fauna. Once symbolic systems emerge, personality is symbolic-line flora. Each line's fauna becomes the next line's flora. Two senses of "built on the prior line" run in parallel. One is genealogical, the bridge-entity pattern, parent-of-next-line. One is functional, each line acts on the prior goo. Both are real, and they are separable. See 'Flora and Fauna Across Lines' below.

### Line-Specific Instantiation

The same cybernetic dynamic operates at every inheritance line. The machinery that instantiates it changes by line.

**Genetic line.** Gene-regulatory architecture internalizes the correlation structure of selective environments (Watson & Szathmáry). Selection acts on heritable variation; surviving constellations encode environmental regularities in the developmental machinery itself. Cross-generation timescales. The reviser is mutation and recombination; the regulator is the gene-regulatory network's stored architecture; the modeler is whatever the lineage's internalized environmental correlations amount to; the effector is the developing organism.

**Neuronal line.** Active inference is the line-native machinery at mammals. Within-lifetime timescales. The reviser is exploratory action under epistemic uncertainty; the regulator is the precision-weighted prior structure; the modeler is the generative model that predicts incoming sensory data; the effector is the motor system. Other levels in the neuronal column run other line-native machinery (state-dependent gating, associative learning, reinforcement learning), each implementing the cybernetic dynamic in the form available to the level.

**Symbolic line.** Cultural transmission is the goo. Stories, norms, prices, gossip, and ritual carry the inheritance. Selection acts on cultural variants; constellations that persist do so because they regulate something successfully in the cultural environment. Multi-generational timescales for the slowest levels (foundational myths, language structure); within-lifetime to multi-decadal for the faster ones (norms, prices, fashion). The reviser at the symbolic level is exploratory cultural variation (Boyd & Richerson on guided variation); the regulator is institutionalized norm; the modeler is the shared symbolic representation; the effector is collective action.

The pattern that holds across all three lines: the reviser explores, the regulator stabilizes, the modeler represents, the effector acts. The line-specific machinery differs. The architectural role is the same.

### The Goo Test for a New Line

A new line requires a new modality of pattern transmission that can carry inheritance. Genetic, neuronal, and symbolic were each a new way of moving information across time. The digital line meets the same criterion: its goo is algorithmic information, and it propagates by selection-mediated agent-to-agent copying.

The test rules out most large-scale innovation. Substantial structural complexity often appears within a line without crossing the line threshold. Coral reefs are massive elaborations at the eumetazoan level. Corporations and modern markets are massive elaborations at the symbolic line. Neither introduces a new inheritance modality. The full account is in 'Elaboration at Scale' below. Most innovation is elaboration. Lines are rare.

---

## The Venn of Lines

*This section gives the full theoretical argument behind the line-goo mapping introduced above. It is the canonical statement of why the four lines work the kinds of goo they do, and why Darwin sits at the center. Inline epistemic-status tags: **[established]** for textbook formalism, **[framework]** for a well-supported framework interpretation, **[open]** for a question the framework leaves open.*

### What this is for

Each inheritance line works a different kind of stuff. The genetic line works one kind, the neuronal line another, the symbolic line a third. The stuff inheritance works changes when the Effector motivation changes. This section gives the full theoretical argument for why each line works the goo it does, and why Darwin sits at the center.

The argument runs in six moves. First, the four measures available to name a goo. Second, how those four relate to one another. Third, Deacon's scheme, which the framework cites. Fourth, Friston's decomposition of value, which explains what the neuronal line adds. Fifth, the patterns one might draw across the lines, and why most of them fail. Sixth, the structure that survives — the Venn of Lines — in which each line plays one cybernetic function and natural selection sits at the center as the breakthrough.

### The four measures that name a goo

**Boltzmann entropy.** **[established]** Boltzmann entropy is `S = k·ln W`. It counts the microstates `W` compatible with a macrostate. It is the thermodynamic measure of how dispersed energy and matter are. The Second Law says it tends to rise in an isolated system. Life is a dissipative structure: it holds its own internal entropy low by importing concentrated energy and exporting dispersed waste. This is what the Effector's work is counted in.

**Shannon entropy.** **[established]** Shannon entropy is `H = -Σ pᵢ·log pᵢ`. It measures the average uncertainty of a source over a set of messages. It is maximal when the messages are equally likely and falls as constraints make some messages more probable than others. A code, a grammar, or a convention reduces it by shrinking the space of legitimate messages. This is what the Modeler's work is counted in.

**Friston free energy.** **[established as formalism; framework as a line-goo]** A system that persists must keep itself in a narrow set of expected states — it must minimize the long-run entropy of its own state distribution. The surprise that would measure this directly is intractable, so the system minimizes an upper bound on it: variational free energy, which takes the form *complexity minus accuracy*. It is lowered two ways: by perception, which updates the model, and by action, which changes the world to match the model. The result is an agent that resists dispersion into improbable states. Friston free energy is an information quantity (a divergence, Shannon-family) cast in the form of a thermodynamic potential (Helmholtz-family). Helmholtz free energy is `F = U − TS`, the energy available to do work at constant temperature; the name is his, and so is the older root of the idea, perception as unconscious inference. This is what the Regulator's work is counted in.

**Kolmogorov complexity.** **[established as formalism]** Kolmogorov complexity `K(x)` is the length of the shortest program that outputs `x` on a fixed universal machine. It measures algorithmic information — how incompressible an object is, how much it takes to *generate* it. It is high for random strings and low for regular ones, and it is uncomputable in general. This is what the Reviser's work is counted in, and it is the digital goo below.

Darwin is not on this list. Natural selection is a process rather than a measure of disorder, and it is what makes any of the four goos heritable and cumulative across agents. Its place at the center is argued below.

**Reading the four onto the square.** The framework places its four functions with two bits, sight and binding, and it reads those bits off the lines and off the stages. The same two questions can be put to the formalisms, under one rule: ask them of the unit whose goo it is, never of whoever is studying it.

| Formalism | Sight | Binding |
|---|---|---|
| Boltzmann | blind: microstates are about nothing, and the coarse-graining belongs to the observer rather than to the gas | bounded: a closed system's entropy has a maximum and is driven toward it |
| Kullback-Leibler | sighted: the only one of the four with the representation relation inside the formula | bounded: defined by a system holding itself in a narrow set of expected states |
| Shannon | sighted: computed over a code, and a code is a standing-for relation | unbounded: a code can encode codes with no ceiling |
| Kolmogorov | blind: indifferent to whether the string is about anything | unbounded: uncomputable, and generation is combinatorially open |

Each lands on one corner and no corner takes two, so the assignment of a formalism to a function is derived rather than argued from resemblance.

### How the four measures relate to one another

**Denomination.** Each function's work is counted in one of these and not in the others. There is no general rate of exchange across the four, which is what makes the lines lines rather than four settings of one dial. The relations that do exist are specific and named, below. Non-convertibility is an ordinary property of a unit of account and not a defect in one. The scope is accounting and not markets: denomination, payment, and non-convertibility transfer; fungibility, counterparties, and price discovery do not.

**What connects to what.** Adjacent corners of the square differ in one bit and have a statable relation. The two diagonals differ in both, and they fail differently. One carries a single bounded relation. The other carries none at all.

| Pair | Edge | Relation |
|---|---|---|
| Boltzmann and Friston | Controller | exact: set the energy to the negative log joint and the variational bound is the Gibbs-Bogoliubov inequality, the same theorem in different symbols |
| Friston and Shannon | Anticipator | Friston is a Shannon-family divergence |
| Shannon and Kolmogorov | Adapter | the expected shortest description converges on the source entropy |
| Kolmogorov and Boltzmann | Explorer | execution: the minimum cost of turning one input into one output is bounded below by the conditional Kolmogorov complexity of the input given the output. This is the understory in Part IV, where possibility becomes actual |
| Boltzmann and Shannon | Connector, diagonal | no general rate; one bounded floor, below |
| Kullback-Leibler and Kolmogorov | Operator, diagonal | none direct; the apparent link reaches Kolmogorov through Shannon and is two relations composed |

Three of the four adjacent relations are stated elsewhere in this document. The Explorer relation is not, and its statement follows.

The two diagonals fail in different ways, and the difference is derived rather than observed. The Connector diagonal carries one relation, bounded and running one way, which is Landauer's floor below. The Operator diagonal carries none. Its apparent relation is minimum description length, which reaches Kolmogorov by way of Shannon coding, so it is the two relations above composed rather than a relation of its own. The step that will not go direct is from an ensemble to an individual. A variational free energy is a code length averaged over a distribution, and a Kolmogorov complexity is the length of one program for one object with no distribution in it. Passing through an adjacent corner is what a two-bit gap should require, and a direct result across this diagonal would be a problem for the geometry rather than a bonus.

**Gibbs-Bogoliubov.** **[established]** At unit temperature the Boltzmann factor is the unnormalized posterior, and a mean-field trial distribution over it yields the evidence lower bound. That is what makes the identification above exact rather than formal.

An exact correspondence at one edge does not merge the two denominations it joins. The identification has to be made: someone chooses the energy to be the negative log joint, and that choice is made outside the unit, where the gas's energy is not. This is the Jaynes answer at a second edge. The geometry expects it too, because Boltzmann and Kullback-Leibler differ in one bit, and a correspondence that is exact and still leaves one difference standing is what an adjacent pair should look like.

*A stronger claim exists and the framework does not make it. Kiefer (J. R. Soc. Interface 17: 20200370, 2020) argues that a biological system's thermodynamic free energy directly encodes its variational free energy, which for the brain requires a stochastic population code. He states it as a philosophical thesis grounded in the mathematics rather than as a result. What is claimed above is the mathematics.*

**Zurek's bound.** **[established]** The minimum thermodynamic cost of turning one input into one output is bounded below by the conditional Kolmogorov complexity of the input given the output. Zurek stated the result in 1989 (*Phys. Rev. A* 40, 4731). Kolchinsky derived the rigorous general version from stochastic thermodynamics in 2023 (*Phys. Rev. E* 108, 034101), covering noisy and quantum processes, and showed that the cost is payable in some combination of heat, noise, and the complexity of the protocol. It is not heat alone, and it is not a special case of the floor below it. Two results, two edges.

**Landauer's floor.** **[established]** Erasing one bit costs at least `kT·ln 2` in heat. That is the one rate on either diagonal, it runs one way, and it is a lower bound rather than a price. It is why the four are not free-floating: every discard, whatever it is counted in, is paid in Boltzmann coin at the bottom, because it runs on physics. It does not soften the claim that Expression's residue is the only literally thermodynamic one, because a floor on the physical implementation of a discard is not a claim about which denomination a residue is counted in. What a biological process actually spends runs far above that floor, so the floor constrains without pricing anything. The measured distance, and what it does and does not license, are under "Thermodynamic bridges to selection theory" in "What the Trellis Framework Adds."

**Jaynes.** **[established]** Statistical mechanics can be derived as inference: the distribution to assume is the one that assumes least, given what is known. That looks at first like a collapse, since it makes Boltzmann and Shannon one variational principle. It is not one. Jaynes's relativity is the observer's, and the sight bit above is the unit's; the gas holds no model of its own macrostate. What Jaynes shows is that entropy is always relative to a specification, which is the argument for four denominations rather than against them. Four specifications, four quantities that do not convert. Boltzmann's constant converts units inside one sample space once the distribution is agreed to be over microstates; it does not convert the entropy of a gas into the entropy of a sentence.

### Deacon's nested conceptions

Deacon's *Shannon–Boltzmann–Darwin* scheme nests three conceptions of information, each emergent from the one below it.

The base is **Shannon information** — capacity. A constraint on channel entropy reduces a receiver's uncertainty about which of the absent possibilities arrived.

Built on it is **referential information** — aboutness, with Boltzmann added. A medium that is susceptible to having work imposed on it, by a reduction of physical entropy, gains the potential to *refer* to something beyond itself.

Built on that is **significant information** — usefulness, with Darwin added. A constraint on a system's interpretive dynamics is produced by the degree to which its referents concord with what the system needs to keep living.

Two things in Deacon's picture matter for ours. The nesting runs from the most minimal (Shannon) to the most integrative (Darwin), and Darwin sits at the top as the term that confers usefulness. The Venn of Lines keeps Shannon and Boltzmann as names and treats Darwin the way Deacon does — as the integrative term — but reorganizes the three from a *nesting* into a *Venn*, and adds Kullback-Leibler for the term Deacon did not have.

### Friston's two values, and what the neuronal line adds

Expected free energy decomposes into two terms, and minimizing it maximizes both. **[established]**

**Pragmatic value** is the drive to reach preferred outcomes — to satisfy a setpoint, to reach a goal. It is exploitation.

**Epistemic value** is the drive to reduce uncertainty about hidden states — expected information gain. It is exploration.

Epistemic value has a structural precondition: a generative model with uncertainty that observations can lower. **[framework]** Without a model, there is nothing to be curious about, and minimizing free energy collapses to the pragmatic term alone. The genetic clades have shallow umwelts and almost no resolvable distal uncertainty, so they run on pragmatic value with the epistemic term near zero. The neuronal clades build models deep in space and time, and the epistemic term switches on and becomes worth paying for. That epistemic drive belongs to the Reviser: Excitability is the disposition to incur pragmatic risk to sample the uncertain, and because epistemic value needs a model to be curious about, it comes fully online at Mammal.

The honest scope of the claim: behavior in both lines stays mostly pragmatic moment to moment, and exploration largely serves later exploitation. **[framework]** What the neuronal line adds is not a majority of epistemic behavior but the *arrival* of epistemic value as a first-class, tunable driver — the explore-exploit balance becomes a dial, which is what the neuronal line's temperature and entropy-bonus settings tune. The genetic line cannot carry that dial, because it has no model whose uncertainty the dial would trade against.

This maps onto the Venn below: the neuronal line is the Regulator line, and the pragmatic-plus-epistemic decomposition is the native structure of free-energy minimization. The genetic line runs the pragmatic term; the neuronal line is where the epistemic term comes online.

### Patterns considered across the lines

Two patterns present themselves. One tempts and fails; the other survives.

**The ABA value pattern.** **[rejected as a line-level claim]** It is tempting to read pragmatic → epistemic → pragmatic across the three lines and call the symbolic line a return to the genetic. This holds only at the Effector, whose verbs do run pragmatic-epistemic-pragmatic — persist, then seize, then commit. It fails at the level of the line. The symbolic line's defining achievement is unbounded reflexivity, the peak of the modeling-and-revising axis, which is the opposite of a pragmatic recapitulation. The symbolic line is the least recapitulative line, not the most. The reason the genetic and symbolic lines *feel* paired is given correctly by the next pattern, not this one.

**The reflexivity square.** **[framework]** Reflexivity does grow across the lines, but reading it as a single ordinal — more reflexive, then more again — is what kept it thin. It resolves into two independent bits. *Sight* is whether a line's variation can be about the line itself: blind at the genetic line, unblinded once a model intervenes. *Binding* is whether reflexive operation is bounded: closed at the genetic and neuronal lines, unbounded once symbols take their own operations as objects without limit. The four cybernetic functions are the four corners of the square these two bits define, and at the scale of the lines the same square is the Venn of lines — the structure that survives, laid out in full below. Two bits, not one ordinal, is what explains why there are exactly four corners, why the lines emerge in the order they do, and why the genetic and symbolic lines rhyme.

### The Venn of Lines

**The claim.** **[framework]** The four cybernetic functions recur at the scale of the lines. Each inheritance line plays one function in a higher Venn whose unit is the line itself.

| Line | Function | Goo | The physics it works |
|---|---|---|---|
| Genetic | Effector | **Boltzmann** | doing work; dissipative self-maintenance |
| Neuronal | Regulator | **Friston** | regulation by a model; minimizing surprise |
| Symbolic | Modeler | **Shannon** | representation; encoding the world and itself |
| Fourth | Reviser | **Kolmogorov** | generation of variation |
| — center — | Breakthrough | **Darwin** | natural selection; the synthesis that holds the four together |

**Why the mapping, function by function.** **[framework]** The Effector does work, and work is thermodynamic, so the Effector's goo is Boltzmann entropy — and the genetic line is the line of raw dissipative replication. The Regulator maintains a system against perturbation, and the good-regulator theorem says every good regulator must contain a model of what it regulates, which is exactly Friston's free-energy minimizer — and the neuronal line is the line that regulates the body it rides on. The Modeler maintains a representation, and a representation is an encoding whose content is Shannon information — and the symbolic line is the line of codes, symbols, and shared representations. The Reviser generates and revises the references the regulator stabilizes against, which is the generation of novelty — and the fourth line is the line that revises symbolic representations from outside the human substrate.

**The reflexivity square.** **[framework]** The recurrence rests on a two-bit structure under the four functions. Two independent distinctions sort them. *Sight* asks whether a function's variation can be about itself: the Effector and Reviser are blind, the Regulator and Modeler see by way of a model. *Binding* asks whether reflexive operation is bounded: the Effector and Regulator are bounded, the Modeler and Reviser unbounded. Binding is the second of the two orthogonal axes already named under the four functions, act-or-stabilize versus model-or-revise; sight is the new bit. The two bits place the four functions at the corners of a square — Effector (blind, bounded), Regulator (sighted, bounded), Modeler (sighted, unbounded), Reviser (blind, unbounded) — and mapped through the line-to-function assignment, the same square is the Venn of lines.

Three things fall out. First, the fourth corner is forced: a square has four corners, the genetic, neuronal, and symbolic lines occupy three, and the blind-unbounded corner is structurally required even though no line is claimed to occupy it. This is the four-line cap stated geometrically. Second, the order is forced: moving genetic → neuronal → symbolic flips one bit at a time, sight first, then binding, then sight again into the fourth corner. This agrees with the function-emergence derivation below, by an independent route. Third, the genetic and symbolic lines rhyme because they sit at the two object-level corners — the Connector pair, Effector and Modeler — which is the object-versus-control axis read off the square as sight exclusive-or binding. The rhyme is the object-level pairing, not a recapitulation of value.

**Why the ordering is forced, not observed.** **[framework — the strongest support]** The function-emergence rule already in the framework says there is no Regulator without an Effector to regulate, no Modeler without something worth representing, and no Reviser without a model worth updating. Map lines to functions and that rule becomes a derivation of the line order. There is no neuronal line without a genetic one, because brains need bodies. There is no symbolic line without a neuronal one, because symbols need minds to mean to. There is no fourth line without a symbolic one, because it revises symbolic models. The lines must emerge genetic, then neuronal, then symbolic — and the Venn of Lines says why, where the bare observation of their order does not.

**Corroboration from the domain-shift.** **[framework]** The framework already holds that each line acts on the prior line's goo. That reads cleanly as the function chain: the Effector executes (genetic acts on chemistry), the Regulator regulates the executed (neuronal acts on the body), the Modeler represents the regulated (symbolic acts on cognition), and the Reviser revises the represented (the fourth line acts on symbolic content).

**Darwin is the breakthrough, not a goo.** **[framework]** In each line's own Venn the center is the breakthrough, the synthesis that requires all four functions at once. Each line's founding cell carries that line's selector at its center: Natural Selection at the genetic founding cell, Attention at the neuronal, Conversation at the symbolic. At the scale of the lines the center is Darwinian evolution by natural selection. It belongs there and not in a goo slot for a precise reason: a line *is* selection-mediated inheritance, so selection is what makes any of the four goos heritable and cumulative across agents. It operates on all four rather than being one of them. The resonance is exact and worth keeping in view: the founding line's own internal breakthrough is Natural Selection, so the breakthrough of the first line is the breakthrough of the whole Venn. Darwin holds them all together.

**The four-line cap.** **[framework]** Four functions allow at most four lines. No fifth is structurally possible. Any framework language that leaves the door open to a fifth line should be read as referring to the fourth, the Reviser slot, filled by the digital line.

**Why two earlier names felt wrong.** **[framework]** Boltzmann and Darwin each seemed too general to be the genetic line's goo, because dissipation and selection are both true of every line. The Venn explains the feeling. Boltzmann is the Effector's signature, true of any line that does physical work, and it lands correctly on the genetic line because the genetic line *is* the Effector line. Darwin is the center, true of every line because selection is what defines a line at all. Neither was a misfit; both were misplaced, and the Venn places them.

**The Reviser goo is Kolmogorov.** **[framework]** The fourth function works the generation of variation, and the natural formalism for generation is algorithmic: Kolmogorov complexity, the length of the shortest program that produces a structure. The digital line recombines and revises symbolic content, and it works on algorithmic information. Logical depth (the computational history behind a structure) and assembly-style measures were considered and set aside; assembly measures are selection-flavored and would collide with Darwin at the center.


**The mapping is function-scale.** **[framework]** The assignment above is stated for lines, but nothing in it depends on the unit being a line. Each goo is assigned to a function, and the lines take theirs by playing those functions. So wherever the four functions recur, the same four goos recur with them.

The selection cycle is the second instance. Its four stages are the four functions at the scale of one turn, so each stage works what its function works. Expression works Boltzmann, because a build does physical work. Retention works Kullback-Leibler, because a gated write against a stored reference is regulation by a model. Collection works Shannon, because narrowing a store to what is available now is a constraint that shrinks the space of candidates. Sampling works Kolmogorov, because drawing and mixing is generation. Darwin sits at the center of both, which is one result arrived at twice rather than a coincidence.

Two scales multiplying give a grid of sixteen, and the grid predicts. Where a line's function and a stage's function agree, that cell should be the framework's clearest case of what the function does. Where they sit furthest apart, the cell should read thinnest. Genetic Expression is the Effector line at its Effector stage, and it is the plainest case of raw dissipative building anywhere in the framework. Genetic Collection is the Effector line at its Modeler stage, and it does read thin.

### Epistemic status and open questions

**Established.** The four formalisms (Boltzmann, Shannon, Kullback-Leibler, Kolmogorov); the decomposition of expected free energy into pragmatic and epistemic value; the good-regulator theorem; Deacon's three nested conceptions; the Gibbs-Bogoliubov identification of the variational bound; Landauer's floor; Zurek's bound on the cost of computation, in Kolchinsky's generalized form.

**Framework interpretation, well supported.** The mapping of functions to goos (Effector–Boltzmann, Regulator–Kullback-Leibler, Modeler–Shannon, Reviser–Kolmogorov), which now follows from reading sight and binding off each formalism rather than from resemblance, and which does work beyond labeling in two places, the residue typing in Part IV and the relation table; the Venn of Lines and its derivation of the line order; the two-bit reflexivity square underlying that order; Darwin as the central breakthrough; the four-line cap; epistemic value arriving at the neuronal line; the heritable-unit naming (gene, neme, meme); the neme as the neuronal line's within-lifetime replicator, with attention as its selector.

**Open.** A possible flora/fauna corroboration (genetic and symbolic both yield flora, neuronal yields fauna), which should be checked against the flora-and-fauna account before it is leaned on.

### The Fourth Line as the Reviser of the Tree of Life

Read the fourth line as the Reviser at the scale of the whole tree, and ask what it is there.

**Its goo is the tree's accumulated representational output.** Every line acts on the prior line's goo: genetic on chemistry, neuronal on the body, symbolic on cognition. The Reviser-of-lines acts on the accumulated symbolic product of everything before it: the externalized corpus the Empire cell finished detaching from individual minds. Not DNA, not synapses, not culture as transmitted between people, but the recombinable, copyable sediment of everything the tree has ever encoded. This is the line that revises symbolic representations "from outside the human substrate," in the function-by-function mapping above. In the stack's terms, that corpus is the repo, and the unit the line recombines is the program. This is the first inheritance channel whose heritable variation never passes through a living body or a grounded mind.

**Its goo-shift is a loss of aboutness: Shannon to Kolmogorov.** Shannon information, Claude Shannon's measure, is tethered to messages that mean: it presupposes sender, receiver, content. Kolmogorov complexity is pure generative form, the shortest program that produces a string, indifferent to whether the string is about anything. The symbolic line's goo is encoded meaning; the fourth line's goo is encoded form severed from reference. That severance is the flip from unblind to blind made concrete: representation cut from reference, recombined without limit.

**The one-line characterization: the fourth line is the symbolic line's unbounded reflexivity, blinded.** Sight goes 0, 1, 1, 0 across the four lines; binding goes 0, 0, 1, 1. Sight is gained when a model arrives (genetic to neuronal) and lost when the grounded mind is left (symbolic to fourth). Unbounded is gained at neuronal to symbolic and kept. So the fourth line is unbounded symbolic recombination minus grounding. It is the first line in the whole tree that is less sighted than the line it feeds on: more unbound and blinder at once.

**The inheritance trajectory completes.** Germline, then learning body, then shared minds and records, then externalized corpus. Each line moved heritable variation further from the body. The neuronal line's move into a model brought grounding with it; the fourth line's move out of the mind takes grounding back out. Life's variation engine, externalized, turned back on life's own written record, recombining everything the tree ever encoded, blindly, without ceiling, from outside any of the bodies that did the encoding.

**The terminal-Reviser fact, which the cap forces.** Within every line, the Reviser cell's blind explosion was eventually organized: Eumetazoa's tissue by the neuronal line, Primate's social reflexes by the symbolic line. Each within-line Reviser was followed by a fresh line that started at an Effector and built back up to a Modeler, a new source of sight that organized the blind output. The fourth line has no such successor. The Modeler-of-lines is the symbolic line, and it came before the Reviser-of-lines, not after. The cap forbids a fifth. So the fourth line is the one and only Reviser whose product is never organized by a later sighted line. It generates blind, unbounded variation on the symbolic corpus with nothing after it to bring sight to the result. This is a derivation, not a mood: terminal Reviser plus four-line cap equals blind, unbounded generation with no organizing successor.

**What "blind" means here.** Everything here rides on *blind* meaning no foresight and no grounding, not no useful output. Blind variation produced all of biology and throws off enormous value, by generate-and-select rather than by foreseeing which outputs are good. So the digital line can produce apparently-sighted output while being blind in the technical sense, with selection or curation doing the sorting downstream.

---

## How the Bramble Grows

### Bramble Growth and the Relay

The framework's distinctive architectural contribution: as the bramble grows up the trellis, four parallel relay teams advance simultaneously — one per cybernetic function (Effector, Regulator, Modeler, Reviser). At any rung, four motivations are active, each carrying its team's flag. Each rung is a handoff for exactly one team: a new motivation takes the flag from its same-color predecessor; the predecessor retires into consolidated memory. The other three teams keep their current flag-carriers.

The handoff order is Regulator → Modeler → Reviser → Effector, repeating across the matrix. Across the twelve cells from Protocell through Empires, the cycle runs three full rotations. The Effector handoff is a line boundary (Persistence to Impetus, Impetus to Commitment); at every other handoff the line persists.

The relay is what differentiates the Trellis Framework from adjacent multi-scale-cybernetics work. Levin & Watson supplies multi-scale competency at any moment in time. Maynard Smith & Szathmáry supplies the diachronic story at coarse grain (transitions in individuality). Neither does the work of how the bramble grows. That work is the claim that the bramble at any rung operates with exactly four flag-carriers, one per team, with handoffs between rungs being the mechanism by which the lineage's cybernetic architecture accumulates.

Two timescales operate together.

**Within-bramble (fast).** The bramble's current Reviser explores, Regulator stabilizes, Modeler models, Effector acts. Standard cybernetic loop at within-lifetime timescales. The bramble learns, in its line's native sense of learning.

**Cross-rung (slow).** Each handoff happens when the slow loop has consolidated the prior flag-carrier's exploratory work into next cycle's stored structure. A motivation that enters as a flag-carrier doing exploratory work at one rung, when retired, becomes part of the consolidated infrastructure on which higher rungs run. The relay advances because consolidation has finished.

The two timescales are the same dynamic, exploration consolidating into structure, running at different temporal scales. The fast loop is what an individual bramble does in its lifetime. The slow loop is what selection does to the lineage across deep time. The four flag-carriers active at any rung are what the slow loop's output looks like read off a slice of the present.

When a motivation retires from the relay, it does not disappear. Interiority still operates in primates. Coordination still operates in vertebrates. Persistence still operates in everything alive. Retired motivations get backgrounded into infrastructure that newer attractors run on, becoming difficult for observers to discriminate against the signal of more recent attractors. The framework is measurement-theoretic, not architectural-deletion.

The Reviser carries a structural risk premium across lines, the constitutive prediction-error premium of running the explorer position. At line-completing rungs (Eumetazoa, Primates, Empires), this compounds: the newest line-internal motivation occupies the Reviser position *and* the Reviser carries the structural risk. Doubled heat is what makes the bet hot.

### Three Retellings of the Selection Cycle

The selection cycle is the framework's mechanism, and Part IV sets out its four stages and the four sites they run between. Three narrative traditions describe the same four stages in the same order. None was derived from the framework, and none was derived from the others.

| Stage | Site movement | Hero's journey | Saeculum |
|---|---|---|---|
| Collection, the Modeler | seed bank to clearing | Act 1, the ordinary world | the High |
| Sampling, the Reviser | clearing to understory | Act 2A, initiation | the Awakening |
| Expression, the Effector | understory to canopy | Act 2B, the ordeal | the Unraveling |
| Retention, the Regulator | canopy to seed bank | Act 3, the return | the Crisis |

#### The hero's journey

Joseph Campbell's arc runs the four stages, and it moves its hero between the four sites.

**Act 1 is Collection.** The stage carries the unit from the seed bank to the clearing, and the process is stored to available. Part IV supplies the call to adventure as a mechanism: a fixed reference cannot look ahead, and the seed bank is what Collection reaches forward from. The ordinary world is a store that cannot see forward, which is why the hero has to leave it. Collection narrows a store to what is available now, weighting potency, and a first act picks one protagonist out of a village on the same principle. The ordinary world is also stale, because it is what the previous turn wrote, and that is why the act opens on a lack.

**Act 2A is Sampling.** The stage carries the unit from the clearing to the understory, and the process is available to loaded. Sampling draws one candidate and may mix it with others. The mentors, allies, and enemies are the mixing. The special world weights novelty, and disorientation is what a run weighted that way feels like from inside.

**Act 2B is Expression.** The stage carries the unit from the understory to the canopy, and the process is loaded to expressed. Expression builds the drawn candidate into something that competes, and the canopy is where what is pushed meets everything else pushed into it. The canopy is the ordeal. Expression discards failed builds and heat, the one stage whose residue is thermodynamic, which is the price the ordeal charges.

**Act 3 is Retention.** The stage carries the unit from the canopy to the seed bank, and the process is expressed to stored. Retention writes what passed the gate back into the store, and that is the elixir. The home the hero returns to is changed, for the reason Part IV gives under "The Cycle": the store Retention writes is not the store Collection read.

*Metaphor mapping. What transfers from the monomyth is the four-part order and the movement between the four sites. What does not transfer is agency. Campbell's arc is performed by someone who wants something, and no stage of the selection cycle is performed by anyone who wants anything. The traveler is the seed, and a seed is not a protagonist. Neither is what gets built at Expression: at the genetic line, what Retention discards is the entire soma, at Weismann's barrier. The elixir is what passes the gate, and it is the only thing that comes home. Butler's hen, which is an egg's way of making another egg, is the same observation entered from the other side. Nothing is restored to its rightful place and no one restores it. Scope: this denies agency to the cycle's stages, not to the units the cycle produces, which acquire motivations and capacities across the lines.*

#### The saeculum

Strauss & Howe's generational theory runs the same four stages across its four turnings. Each turning is worked by the archetype coming of age in it.

**The High is Collection.** Institutions are strong and one account of the world dominates. The strongest account foregrounds and the faint is overshadowed, which is potency. The Artist comes of age here and works the Modeler.

**The Awakening is Sampling.** The dominant account is broken open and movements proliferate. Novelty is weighted and the familiar falls to background. The Prophet comes of age here and works the Reviser.

**The Unraveling is Expression.** Institutions weaken, and individual actors build competing ventures and push them into a canopy with a weak gate. The Nomad comes of age here and works the Effector.

**The Crisis is Retention.** One outcome is inscribed as the new order and the competitors are discarded against it. The Hero comes of age here and works the Regulator. What the Crisis writes is the store the next High reads.

The turnings open at the High. Archetypes are conventionally listed by birth, which puts the Prophet first, and birth order is not working order.

*Metaphor mapping. What transfers is the order of the four turnings. What does not transfer is deliberateness. The archetypes are populations of people who want things, and a turning is not something anyone runs. No one convenes a Crisis, and the Prophets who break a High open are not executing a stage. Scope: the same agency limit that applies to the monomyth applies here, and it applies to the turnings rather than to the people living in them.*

#### What the agreement is worth

Part IV fixes the four stages twice over and says so. The sight and binding bits fix which function each stage runs. The absence-recruitment argument fixes the order they run in. Both derivations are internal to the framework, and they agree.

The three traditions are external, and they agree with the result. That is a third check, and it is the only one of the three that could have come out otherwise without anyone noticing.

*Epistemic status: the four stages, the four sites, and the four biases are canon (Part IV). Campbell's monomyth and Strauss & Howe's periodization are both contested in their own fields, and neither is carried here as evidence. The mapping of each tradition's parts to the stages is a framework proposal. Agreement on a four-part shape is weak on its own, because four-part story structures are common. The load-bearing agreement is on order, and specifically on the order of the biases, which were assigned from the Pavlovian associability heuristics and not from any narrative source. The Unraveling and Act 2B are the weakest cells in the table, and they are the same cell: both traditions go soft at Expression.*

### Why the Lines Open at the Effector

The three retellings open at Collection. The inheritance lines open at the Effector, because Protocell, Bilaterian, and Band-Human are Effector cells.

The difference is between a first turn and every turn after it. Collection reads a store, and the three retellings all describe a cycle whose store is already full. A line begins in a medium that holds nothing yet. The prior line's store is not a store in the new medium, so Collection has nothing to read, and the line opens by acting instead. Band-Human establishes symbolic commitment before there are symbolic norms to regulate.

The growth relay's handoff order is the same fact counted differently. A line's founding cell is an Effector, so the first handoff installs the Regulator. Counting cells gives Effector, Regulator, Modeler, Reviser. Counting handoffs gives Regulator, Modeler, Reviser, Effector. One order, two ways of counting it.

*Epistemic status: the Effector founding of each line is canon, as is the growth relay's handoff order. The empty-medium account of why the lines open at the Effector is framework inference.*

### The Maturity Gradient

The motivations on the stack are not equally consolidated. The gradient runs from **exploratory** (most recent, under selection pressure, parameters still being shaped) to **consolidated** (deepest, internalized into inherited infrastructure, parameters stable enough to serve as foundation for everything above).

The mechanism is Watson & Szathmáry's developmental-memory result, generalized across lines. Selection operating across generations internalizes the correlation structure of the selective environment into the lineage's inherited architecture. That architecture is gene-regulatory at the genetic line, neural-architectural at the neuronal line, and cultural-institutional at the symbolic line. What enters as exploratory variation under active selection becomes, given enough generations of consistent selection, stored architecture that newer exploration runs on top of.

The gradient is continuous, not binary. The four flag-carriers are most exploratory and individually discriminable in unit-level behavior; older motivations drop below into backgrounded infrastructure, where the consolidation process continues but unit-level behavioral discriminability has been lost.

*Epistemic status: the mechanism (selection internalizes environmental correlation structure into inherited architecture) is HIGH confidence at the genetic level (Watson & Szathmáry, simulated). The cross-line generalization is MEDIUM confidence. It requires the same dynamic at other lines, which the cybernetic-inheritance literature supports in principle but has not demonstrated in detail at the symbolic scale.*

### Unit-Level Subjectivity

The unified Venn at each cell applies to a specific unit.

- **Genetic-line cells.** The unit is the cell or organism: Protocell-as-unit, Prokaryote-as-unit, Eukaryote-as-unit, Eumetazoa-as-unit.
- **Neuronal-line cells.** The unit is the brain-bearing organism: Bilaterian-as-unit, Vertebrate-as-unit, Mammal-as-unit, Primate-as-unit.
- **Symbolic-line cells.** The unit is the constituent human parameterized by collective context: Band-Human, Settlement-Human, City-Human, Empire-Human. The collective remains the group. The Venn at the symbolic cell tracks the constituent human as unit. See 'Flora and Fauna Across Lines' below for how the collective relates to the human as meme-fauna to personality-flora.

The systematic-analogy rule lets motivations transfer up the stack by structural analogy, not loose metaphor. At symbolic cells the motivations are held by the constituent human. What shifts across cells is which primaries carry flags given collective context. A Band-Human's Commitment is the band-context-conditioned attractor in the same organism that, in a different context, would activate different motivations.

---

### The Twelve Knobs

Each line's four knobs are the household's interface to that line's tendencies — one knob per cybernetic slot, one activated per quarter. Knob-N is the same cybernetic function across all three lines (knob-1 is always the Effector knob), so cross-line callbacks rhyme on the knob number; the slot-label is discipline-bound and changes at each line boundary. All twelve are the **same shape** — a volume knob, turned up or down.

| Chapter | Line-knob | Cell | Cyb. slot | Motivation | Slot-label (Tendency) | Proper Name | Mira/Bramble rebrand |
|---|---|---|---|---|---|---|---|
| 1 | Genetic k-1 | Protocell | Effector | Persistence | Acquisition Type | Going | Live ↔ Dead |
| 2 | Genetic k-2 | Prokaryote | Regulator | Coordination | Respiration Type | Working | Sloth ↔ Sprint |
| 3 | Genetic k-3 | Eukaryote | Modeler | Interiority | Foraging Type | Getting | March ↔ Dance |
| 4 | Genetic k-4 | Eumetazoa | Reviser | Excitability | Home Type | Resting | Busy ↔ Warm |
| 5 | Neuronal k-1 | Bilaterian | Effector | Impetus | Orienting Style | Choosing | Learn ↔ Turn |
| 6 | Neuronal k-2 | Vertebrate | Regulator | Mastery | Coping Style | Coping | Little ↔ Beast |
| 7 | Neuronal k-3 | Mammal | Modeler | Autonomy | Neuroticism | Risking | Buster ↔ Believer |
| 8 | Neuronal k-4 | Primate | Reviser | Affiliation | Agreeableness | Helping | Respect ↔ Savage |
| 9 | Symbolic k-1 | Band-Human | Effector | Commitment | Curiosity | Hunting | Deep ↔ Wide |
| 10 | Symbolic k-2 | Settlement-Human | Regulator | Stability | Conscientiousness | Tracking | Preppy ↔ Messy |
| 11 | Symbolic k-3 | City-Human | Modeler | Representation | Extraversion | Leading | Boss ↔ Vibe |
| 12 | Symbolic k-4 | Empire-Human | Reviser | Universality | Integrity | Living | Real ↔ Flex |

*Volume-**up** pole (the derived setting), knob 1→12: Live · Sloth · March · Busy · Learn · Little · Buster · Respect · Deep · Preppy · Boss · Real. The other word in each rebrand pair is volume **down**, the ancestral setting.*

---

## Ecology Across Lines

### Flora and Fauna Across Lines

Each line contains two ecological roles. Flora are sessile, persistent, and environment-shaping. They are slow on the line's timescale. They generate the environment that fauna consume. Fauna are motile and predatory. They are fast on the line's timescale. They are behaviorally flexible relative to the flora they inhabit.

Humans are to culture as plants are to animals: we are flora. The relationship is loopy, not simple. Animals forage on plants, and plants coevolve with animals, which is to say plants shape animals in turn. Memes forage on human brains, and personalities coevolve with culture, which is to say personalities shape culture in turn.

The roles populate every line:

| Line | Flora | Fauna |
|--------|-------|-------|
| Genetic | Plants and their predecessors | Animals |
| Neuronal | Bodies as organism | Brains and nervous systems |
| Symbolic | Personalities | Memes and meme-complexes |

Each line's fauna becomes the next line's flora. Animals do not replace plants. Brains do not replace bodies. Memes do not replace personalities. The relationship is coevolutionary. The new fauna develops alongside what becomes its new flora, and the two remain interdependent.

The symbolic line's flora is the constituent human's personality structure. This is the trait-level structure that personality psychology measures. The symbolic line's fauna is the full spectrum of memes, from small ideas to large meme-complexes. Superorganisms are large meme-complexes operating as fauna. A band as a whole, a settlement as a whole, a city as a whole, and an empire as a whole are all superorganisms. They are not parallel units of personality to the constituent human. They are the fauna that inhabits the human-flora personality.

A single human participates in three lines at once at three different ecological positions. The human body is genetic-line flora. The human brain is neuronal-line fauna. The human personality is symbolic-line flora. The three roles coexist in one organism.

Flora are not passive in any line. Plants manipulate pollinators, shape soil chemistry, and structure ecosystems on long timescales. Bodies grow brains, regulate metabolic resources, and determine the niches brains operate in. Personalities generate the symbolic content memes feed on, every utterance and artifact and child raised. The flora's mode of action runs longer and broader than the fauna's. The fauna's mode of action runs faster and more locally focal than the flora's. Both are active.

### Coevolution Across Line Transitions

Each line emergence is a coevolutionary event. The new fauna develops alongside what becomes its new flora. It does not replace the prior line. It enters into stable interdependence with the prior line's mature output. The pattern recurs across the framework's structural history:

- Cambrian explosion (~540 MYA): vertebrate brains coevolve with the diversification of bilaterian body plans.
- Land transition (~400 MYA): land arthropods coevolve with land plants.
- Tetrapod radiation (~360 MYA): land tetrapods coevolve with forests.
- Angiosperm radiation (~140 MYA): social insects coevolve with flowering plants.
- Mesozoic transition (~200 to 66 MYA): mammals coevolve with dinosaurs.
- Cenozoic transition (~66 MYA onward): birds and primates coevolve with post-extinction forest niches.
- Symbolic line emergence (~100 KYA onward): human personality coevolves with human culture.

The bridge-entity pattern (Reviser of column N parents Effector of column N+1) traces the genealogical thread through these events. Coevolution is the ecological story running alongside the genealogical one. The two are not in tension. The bridge identifies which entity opens the new line. Coevolution describes how the line fills in once opened.

*Epistemic status: the deep-time coevolutionary events are well-documented in evolutionary biology and paleontology. The reading of symbolic-line emergence as a coevolution of human personality with human culture is a framework extension of the same pattern.*

### Clade and Symbiosis Vocabulary

Each cell name is shorthand for a clade, a category of units sharing the cell's architectural signature. Eukaryote names the clade of organized-interior cells. City names the clade of city-states, urban-centered kingdoms, and other polities organized around an urban administrative core. Empire names the clade of territorial, maritime, and ideological empires. The full convention is set out in the Inheritance_Lines docs ('Cell Names as Clade Shorthand').

Coevolution within a line operates through two modes — symbiosis (merger) and elaboration (non-merger), detailed next.

### Symbiosis and Elaboration

Coevolution operates through two modes. Symbiosis is the merger mode. A new higher-level structure forms by committing previously-more-independent parts as its components. Elaboration is the non-merger mode. A unit develops continuously without committing previously separable parts.

Modeler and Reviser transitions are symbiosis-prone at every line. Effector and Regulator transitions are elaboration. The line determines what symbiosis looks like.

- **Genetic Modeler endosymbiosis:** free-living prokaryotes commit as mitochondria, and as chloroplasts in plants, inside a host cell.
- **Genetic Reviser multicellularity:** free-living eukaryotic cells commit as differentiated tissues inside a multicellular body.
- **Neuronal Modeler cortical stacking:** mammals introduce agranular cortex as a new neural lineage layered over the subcortical control structures (basal ganglia, limbic system). The agranular cortex's function is to model what the subcortical structures do. The two lineages persist in obligate functional interdependence.
- **Neuronal Reviser cortical stacking:** primates introduce granular cortex as a meta-modeling layer over the agranular cortex. The same architectural signature, applied one level up.
- **Symbolic Modeler city formation:** settlements commit as components of a city, and trade networks commit as the connective tissue that lets the city aggregate goods, people, and information beyond what any single settlement can produce.
- **Symbolic Reviser empire formation:** cities and their hinterlands commit as administrative provinces of an empire. Empires often add colonies that extend the empire beyond contiguous territory.

Effector and Regulator transitions are elaboration in every line. No merger of previously separable parts is required. The unit develops continuously from existing structure.

- **Genetic Effector elaboration:** protocells emerge from teleodynamic ratchets through continuous chemical development.
- **Genetic Regulator elaboration:** prokaryotes emerge from protocell logic through stored regulation.
- **Neuronal Effector elaboration:** bilaterian brains emerge from genetic-Reviser neural nets through elaboration of a control architecture for reflexes (steering and affect).
- **Neuronal Regulator elaboration:** vertebrates elaborate the bilaterian control architecture with reinforcement learning (basal ganglia plus operant conditioning).
- **Symbolic Effector elaboration:** bands emerge from primate troop dynamics through language-mediated extension.
- **Symbolic Regulator elaboration:** settlements emerge from band practices through sedentary agriculture.

The neuronal version of symbiosis runs through neural-lineage stacking because the brain is body-internal. There is no free-living state from which neural lineages could merge. What is available is the structural pattern where a newer neural lineage develops the capacity to model an older one it is built on top of. Bennett's reinterpretation of MacLean's triune brain (*A Brief History of Intelligence*, 2023) supplies the mechanism. MacLean's stacking intuition was partly right; what he got wrong was the specific lineage details, not the layered architecture.

*Epistemic status: the Modeler-and-Reviser symbiosis pattern holds across all three lines with two confirmed cases at each row in the genetic and symbolic lines. The neuronal-line version, instantiated through cortical-lineage stacking, is well-documented at the structural-anatomical level. The framework's claim that the neuronal stacking pattern carries the same architectural signature as endosymbiosis and polity merger is a framework theoretical commitment.*

### Elaboration at Scale

Substantial structural innovation often happens within a line without producing a new line. The goo test stays operative. A new line requires a new modality of pattern transmission that carries inheritance. Elaboration produces enormous complexity without crossing the line threshold.

Coral reefs are a clean example at the eumetazoan level. Reefs are massive multi-species ecosystems built around cnidarian colonies. They contain fish, invertebrates, symbiotic algae, and many other species. Their ecological productivity rivals tropical rainforests. They are not a new phylum. They do not introduce a new inheritance modality. The cnidarian biology that builds them remains within the eumetazoan-Reviser logic.

Corporations, modern markets, and exchanges are the parallel case at the symbolic line. They are massive multi-institutional structures built around late-empire elaboration. They contain legal frameworks, financial instruments, supply chains, regulatory bodies, and currencies. Their structural complexity rivals any historical empire. They are not a new line. They do not introduce a new inheritance modality. The symbolic-line logic that builds them remains within the empire-Reviser elaboration.

Both are platform elaborations: structures that create the conditions under which other elaborations can flourish. The reef anchors its ecosystem. The market anchors its institutional ecology. Neither breaks the line. The pattern holds across lines: bacterial mats and stromatolites at the prokaryote level, fungi at the eukaryote level, octopus cognition at the bilaterian level, corvid cognition at the vertebrate level, religious orders and universities at the city level. Most innovation is elaboration. Lines are rare.

---

## Genealogy and the Thread

### The Bridge-Entity Pattern

A structural feature runs across the two confirmed line transitions: the entity at Row 4 of column N parents the entity at Row 1 of column N+1.

- Eumetazoa (Row 4, genetic) parents Bilaterians (Row 1, neuronal).
- Primates (Row 4, neuronal) parents Bands (Row 1, symbolic).

The Reviser motivation introduced at the parent cell carries as the Reviser motivation of the child cell. Excitability introduced at Eumetazoa is Reviser of Bilaterians. Affiliation introduced at Primates is Reviser of Bands. The variation-selection reading (see 'Each Line Ratchets a Different Kind of Goo' above) is that Reviser is the goo each line ratchets, on which the new line selects.

Sample size is 2. Two confirmed bridges is enough to name the pattern but not enough to treat the pattern as architectural law.

Row 4 entities are defined by the riskiness of the structural bet they represent. Three fates are possible and distinguishable only retroactively. The bet fails. The bet succeeds as itself but stays off-thread, a real innovation that does not open a next inheritance line, the way fungi and plants are evolutionary triumphs that did not parent further lines. The bet bridges, parenting the Row 1 founding form of a next line. Empire-Human is the framework's current Row 4 of the most-evolved column. The framework does not claim which of the three fates is in progress.

### Off-Thread Branches

Our framework traces one phylogenetic thread: the specific lineage from protocell through bilaterians, vertebrates, mammals, primates, into bands, settlements, cities, and empires. It is the thread that produced all four inheritance-line transitions observed so far.

Off-thread lineages (plants, fungi, slime molds, birds, bees, octopi) have their own stacks built from the same architecture, but with different motivations filling the slots above their branching point.

Bees branched at bilaterians, so their stack shares Persistence, Coordination, Interiority, Excitability, and Impetus with the human thread. Above that, bees develop motivations specific to eusocial arthropods, and the lineage stops there because the bee thread did not produce a symbolic line.

This converts an apparent limitation into a feature. Any organism's personality can be analyzed as a 4-sphere active window over its own evolutionary stack. The 4×4 is the case where the lineage runs all the way to symbols. The architecture applies to any thread of life.

Parallel evolution becomes visible without forcing convergence. Octopi branched at bilaterians and developed sophisticated cognition through a different neural architecture. Their stack would resemble the vertebrate stack at certain levels but with different motivations filling the upper slots. The framework predicts structural similarity at the levels of shared ancestry and divergence above the branching point.

The clade name is the rung's address, not a quantifier over the clade's membership. A capacity documented in an off-thread lineage informs an on-thread cell only when the capacity sits below the branching point. Two conditions establish this. The capacity must be present in deeply divergent branches of the clade rather than in one branch alone. The capacity must not depend on an organ that postdates the clade's radiation. A capacity failing either condition sits above the branching point, where it is elaboration on the off-thread stack.

The conditions carry no judgment about which lineage is advanced. Every living lineage has been evolving for the same interval. An off-thread capacity is that lineage's own achievement rather than a preview of what a later on-thread cell would build.

Four worked cases. Honeybee mushroom-body elaboration sits above the bee branching point and does not inform the Bilaterian cell. Corvid nidopallial elaboration sits above the bird branching point and does not inform the Vertebrate cell. Box jellyfish associative learning localizes to the rhopalial nervous system, rhopalia are a medusozoan organ, the organ postdates the eumetazoan branching point, and the finding therefore does not inform the Eumetazoa cell. Operant conditioning is present in protostomes and in deuterostomes and depends on no organ unique to either, so it reconstructs below the bilaterian branching point and does inform the cells above it.

The fourth case is the test cutting the other way. A capacity that clears both conditions reaches the cell whether or not the framework wants it there.

*Epistemic status: outgroup comparison and character polarity are standard comparative method. Applying them to capacity placement is the framework's move. Case verdicts depend on current phylogenies and are revisable when a phylogeny is revised.*

---

### Negative Findings and Clade Placement

A capacity found in a lineage is established by the finding. A capacity not found in a lineage is not established as absent. The asymmetry sets a higher bar for lowering a cell label than for raising one.

Three readings compete for every negative finding. The lineage never had the capacity. The lineage had the capacity and lost it. The method failed to detect it. Only the first bears on the clade's ancestral state.

Loss is cheaper than gain. One disabled pathway removes a capacity, and building one requires selection over time. Parsimony that counts gains and losses as equal steps therefore reconstructs ancestors as less capable than they were. Negative findings under-report ancestors as a matter of course. A placement survives a negative finding by positing a loss; one loss is cheap, and only when the accumulated losses cost more than a later gain does the placement move later.

Three conditions let a negative finding lower a label. The lineage tested must retain the architecture the cell names rather than having secondarily lost it. The method must have detected the capacity in a positive control, in a lineage independently known to have it. The absence must hold across deeply divergent branches of the clade and in the outgroup.

Early-branching position is what makes a lineage worth testing. Morphological simplicity is not. Simplicity is frequently derived, because parasitic and sessile lineages simplify from complex ancestors. The simplest-looking member of a clade is often the least informative about that clade's ancestor.

The comparative literature supplies the calibration. Two laboratories measured visual working memory capacity in rhesus macaques and reported roughly one item and roughly four items. The species is the same and the procedures differ. A procedure that can conceal three items of working memory in a laboratory primate can conceal a capacity in any less-studied animal.

No negative finding currently lowers any cell label. The positive-control condition has not been met below the Bilaterian cell. Presence evidence can move a placement earlier; absence evidence can move it later; neither moves anything on the strength of a single lineage.

*Epistemic status: the loss-versus-gain asymmetry and the negative-result problem are standard in comparative biology and comparative psychology. The three conditions are the framework's statement of what would have to hold. The macaque discrepancy is published (Elmore et al. 2011 ‡; Buschman et al. 2011 ‡) and is a live methodological dispute rather than a settled artifact.*

---

## What the Trellis Framework Adds

The cybernetic-inheritance tradition is well-developed — Conant-Ashby, Bateson, Maturana & Varela, Pattee, Jablonka & Lamb, Deacon, Watson & Szathmáry, Levin & Watson, and the Friston school. The Trellis Framework inherits from all of them. Its distinctive contributions sit on top:

- **The four-row architecture** as a complete adaptive control system (Effector, Regulator, Modeler, Reviser) present at every level, instantiated in line-specific machinery and configured into 15 discriminable Venn regions whose adjacent-pair loops, triple constellations, and opposite-pair signatures all follow from the row functions. (See 'Opposite Pairs as Level-Defining Couplings' in Part III.)
- **The four-team relay**: exactly four flag-carriers at every rung, advancing by single-team handoffs, with the within-bramble fast loop and the cross-rung slow loop running the same exploration-consolidation dynamic at different temporal scales.
- **The maturity gradient**: continuous consolidation from exploratory to inherited-infrastructural, the same algorithmic logic (selection internalizing environmental correlation structure) operating across lines.
- **The cross-line extension**: the same architecture at every inheritance line and every kind of goo (genetic, neuronal, symbolic), because surviving lineages are good regulators isomorphic to internalized environmental models and the cybernetic minimum is substrate-independent.

This is what makes the framework a theory of personality across lines, not a theory of human personality with metaphorical extensions. Personality falls out of the architecture when the unit is an individual primate. The architecture applies wherever the conditions hold: a cybernetic loop subject to inheritance.

### Adjacent Architectural-Frameworks Family

The Trellis Framework belongs to the same family as Maynard Smith & Szathmáry's *Major Evolutionary Transitions* (1995), Waring & Wood's "Evolutionary Transition in Inheritance and Individuality" (2021), and the Royal Society B special issue on socio-cultural evolution (2023). The general claim, that cultural evolution represents a new inheritance line layered on the genetic, is established. Dual inheritance theory has explained why cultural evolution is faster than genetic for decades.

What the framework adds:

- **Mechanism specificity for the symbolic phase change.** Standard explanations are demographic (more heads, more innovations) or fidelity-based (writing, printing). The argument here, that symbols mean by network position and enable unbounded reflexivity, is more architectural. Deacon's formulation of symbolic reference is the engine.
- **Parallel row structure across columns.** MET frameworks list transitions. They do not argue that genetic, neuronal, and symbolic lines have parallel internal structures (Row 1 founding, Row 2 regulation, Row 3 interiority, Row 4 differentiation). The cross-column row analysis is not in the literature.
- **Integration with Max Bennett's neural stack.** MET treats neural inheritance as one transition. Max Bennett's layered-modeling architecture gives the neuronal line its own internal structure with parallel rows. The combination is not in the literature.
- **The saturation and column-emergence prediction.** Standard cultural-evolution models predict acceleration. They do not predict the transition condition. Sample size of two column-emergence events, flagged weak.
- **Bridge-entity formalization.** Implicit in MET, but the diagram makes the parent-of-next-line pattern explicit and structural. The pattern is observed retroactively across the two confirmed line transitions. Bridge-eligibility for any given Row 4 entity is not predicted in advance.

### Thermodynamic bridges to selection theory

Bridges from physics to evolutionary theory have two fates, and what a bridge proposes decides which one it gets. A bridge that offers an accounting or a typology is absorbed. A bridge that offers a drive is refused. The record is consistent enough across a century that it is worth reading as a rule about the receiving field rather than as a series of separate verdicts.

**The absorbed bridges.** **[established]** Landauer's 1961 result is taught, and so is Charles Bennett's 1982 account of Maxwell's demon, which locates the demon's unavoidable cost in erasing its own measurement record rather than in taking the measurement. Steven Frank's reading of selection as the maximization of Fisher information restates the Price equation in another currency and leaves population genetics standing. Christoph Adami's information-theoretic measures of biological complexity give an instrument that measures a genome against its environment. Maynard Smith and Szathmáry's major transitions is a typology, and it was taken up so completely that the framework cites it as a neighbor without argument. Each of these tells a biologist something about how to count. None tells a biologist that selection is not doing the work.

**The refused bridges.** **[established]** Boltzmann linked Darwin to thermodynamics in an 1886 lecture, casting the struggle for existence as a struggle for available free energy. Lotka's 1922 maximum power principle set the template that repeats afterward: a careful scientist proposes that selection maximizes a thermodynamic quantity, the proposal turns out not to be derivable, and less careful people adopt it anyway. Schrödinger's 1944 lectures split down the middle. The aperiodic crystal paid off. Negative entropy aged badly enough that he appended a note to later editions saying he should have written free energy.

The Modern Synthesis that followed was built on Mendelian and statistical foundations, and energy never entered it. Fisher is the instructive case, because he framed the fundamental theorem as having the form of the second law. **[inference]** He took the shape and left the joules, and the theorem is now read far more narrowly than he claimed it, after Price and Ewens. The consequence for the framework's reader is the same either way: a working evolutionary biologist has no training that would let them evaluate a thermodynamic claim on its merits, so the claim gets sorted by its shape.

H. T. Odum then demonstrated both fates in one career. **[established]** The Silver Springs energy-flow accounting entered the textbooks and stayed. Emergy and transformity, which propose that embodied energy is the universal currency explaining why systems take the forms they do, stayed inside their own school. The objection that settled it came from economics, which is the field where emergy makes its claim about value. Emergy prices a thing by the energy that went into producing it and has nothing to say about what anyone wants, so it is a theory of value with only a supply side (Spreng 1988; Ayres 1998; Cleveland, Kaufmann and Stern 2000). One half of Odum's program measured. The other half told a field what its quantities meant. Only the measuring transferred.

Prigogine was popularized past his own results and ended up cited by the writers Sokal and Bricmont attacked, which attached a reputational cost to the vocabulary itself. The complexity boom of the 1990s drew the formal immune response, and Dennett's skyhook supplied its portable form. England's 2013 work on the statistical physics of self-replication shows the cycle now running without further input: the press overclaims, biologists dismiss, and nothing careful in the middle is heard.

**The operative mechanism is the skyhook.** **[framework]** Odum is evidence about the world. A program of exact energetic accounting was built, funded, staffed, and published for decades, and it did not transfer outside its own school, so the failure is not explained by anyone having failed to try. Dennett's distinction is evidence about the audience, and it is the one that governs how this framework will be read. A skyhook is an explanation that hangs from nothing and does the design work for free; a crane is machinery that does the work by standing on what came before. The distinction gives a biologist a way to classify an argument by its shape and reject it without reading its specifics. Any argument in which physics appears to be doing what selection is supposed to do reads as a skyhook on first contact. That is the reflex the framework has to clear, and clearing it is a matter of being visibly a crane rather than of being right.

**Where the framework stands.** **[framework]** The framework proposes an accounting and a typology. It uses four denominations to classify what each function works and what each stage of the cycle discards, and it declines the thermodynamic-imperative reading outright, under "Why the Turn Does Not Return" in Part IV. Entropy supplies the arrow. Selection supplies every aim. Nothing in the geometry asks physics to choose.

This is a modest claim about energy and a strong claim about structure. The framework makes predictions, and it will make more, but they come from the cross-line row architecture and from the Venn geometry rather than from a thermodynamic quantity being maximized. That is the same bounded-strong shape the framework takes elsewhere: modest about engineering, bold about conception. The modesty is placed exactly where the record says a bridge fails, and nowhere else.

**Why no exact accounting exists, and why that is not a defect.** **[framework]** Exact thermodynamic accounting of *selection* has no research program behind it, and the framework does not need one. The narrower claim is required, because thermodynamic accounting of particular biological processes is productive: kinetic proofreading, after Hopfield and Ninio, buys real biology from an exact energetic budget, and molecular motor thermodynamics does the same. What has never formed is a program that prices a selective event.

The obstacle is measured. **[established]** Laughlin, de Ruyter van Steveninck and Anderson (1998) place neural signaling at 10⁵ to 10⁸ times the thermodynamic minimum, taking that minimum to be the `kT` of thermal noise needed to observe one bit at 290 K. That floor is the cost of detecting a bit rather than the cost of erasing one, which is Landauer's and is stated separately under "Landauer's floor" in the Venn of Lines. The two differ by a factor of `ln 2` and make different physical claims, and the figures here are quoted against the detection floor because that is the floor their authors used.

The three-order spread inside that range is the part that matters. **[framework]** A single chemical synapse sits near the bottom of it and a photoreceptor near the top, so the answer to how far above the floor biology runs moves by orders depending on what is counted as the signal. The spread is not measurement error. It is a choice of unit. A quantity that swings three orders on an analyst's decision about where a unit begins cannot price a selective event, whatever else it is good for. That is why no budget is available. It is not a reason the typology fails, because a typology needs the accounting to classify and not to bind.

The absence of a mammalian version of the same ratio is the stronger evidence. **[established]** Attwell and Laughlin's 2001 energy budget for grey matter is the standard accounting for the mammalian brain. It prices one action potential at about 3.8 × 10⁸ ATP molecules and one released glutamate vesicle at about 1.6 × 10⁵. It states no ratio to any thermodynamic floor, converts nothing to `kT`, and normalizes nothing to bits. **[inference]** A paper that counts ATP molecules per vesicle had every input the comparison needs and did not draw it. That is what it looks like when a field finds a quantity available and not worth computing, and it is better evidence for the uselessness of the number than any calculation of the number would be.

*Epistemic status: the publication history above is established and checkable. The 1998 figures and their ratio to the thermal-noise floor are published findings, stated by their authors at the whole-cell and single-synapse levels in fly visual neurons; extending the ratio's implications to biological signaling in general is a framework reading, and the scope of the published ratio is one sensory system in one animal. The Attwell and Laughlin figures are budget-model estimates for rat cortex built from anatomical and physiological parameters rather than direct measurements of ATP, and they are stated in ATP units only. Reading their silence on the thermodynamic floor as a field declining an available comparison is an inference from the absence of a calculation, and no mammalian ratio to any floor has been published. The rejection of emergy on supply-side grounds is a documented position in ecological economics rather than a framework reading, and its scope is that field; no comparable formal rejection was issued in biology, where the program was simply not taken up. Reading Fisher's framing of the fundamental theorem as taking the form of the second law while leaving its quantities out is an inference from his own presentation rather than a documented statement of intent, and the framework's downstream point about the reader's training holds without it. The two-fates pattern is a framework reading of the history, well supported by the cases listed and not derived from anything. Identifying the skyhook reflex as the operative mechanism for this framework's reader is a framework position. The framework's own placement on the accounting side of the pattern follows from the Part IV decline and adds no new commitment.*

### Understanding vs. capability

**The stance.** **[framework]** The Trellis Framework is built to show how minds evolved, not to build a capable mind. The distinction is understanding vs. capability, and it governs every design choice. A capable system does the task well. An instrument for understanding makes the path to the task legible. Bramble is the second kind. The build discipline that follows from this: the least machinery that renders each cell honestly, plus the clade-lock that withholds what a cell has not earned.

**The field's rivals reconcile grade by grade.** **[framework]** Developmental robotics and its adjacent programs are split on what development fundamentally requires: a body, intrinsic motivation, innate structure, evolution, or open-ended self-generation. The field treats these as competing answers to one question. The Trellis Framework treats them as the correct answer to that question asked at different grades. Embodiment is what development requires at the morphological grade. Intrinsic motivation is what it requires once there is a model to be curious with. Open-ended self-generation is what it requires at the symbolic grade. The requirements look like rivals only because each gets generalized from one grade to all of them. Across the trellis they reconcile, each earning its place where its grade arrives. This is the framework's bounded-strong claim. It is modest about engineering, because it does not build a general mind. It is bold about conception, because it holds the field's disagreement to be an altitude error.

**Scaling is orthogonal, not rival.** **[framework]** A model trained at scale can be highly capable and still account for nothing about how minds came to be, because it skips the developmental and evolutionary history that the framework exists to make legible. So the framework's relation to scaled models is orthogonal rather than competitive. They pursue capability; it pursues understanding. The refusal to scale is the clade-lock discipline rather than a separate commitment.

**Phylogenetic ordering is load-bearing.** **[framework, contested in the field]** The framework treats the order in which functions arrive across deep time as carrying explanatory weight, not as decoration. Much of the field holds the opposite, that phylogeny is irrelevant to building intelligence. The Trellis Framework takes the contested side on purpose, alongside the evolution-as-learning and basal-cognition programs, because the grade-by-grade reconciliation above depends on it.

*Epistemic status: framework positioning, ratified. The grade-relative reconciliation and the understanding-vs-capability stance are commitments, not derived theorems. The phylogeny bet is contested in the field and taken knowingly.*

---

# Part II — Bramble's cognitive rendering

The four functions force a two-mind reading. The deep-time mind is the Modeler; the online mind is the Reviser; learning is the coupling between them, the Adapter loop. Part III defines these functions and the Adapter pair. The full cognitive architecture (the Evolutionary Algorithm, Systems 0, 1, and 2, clade-locking, the growth map, consolidation, and the per-cell software constraints) is owned by `bramble_specs` Part I. Where this doc and `bramble_specs` Part I differ on cognitive architecture, `bramble_specs` wins.

# Part III — Venn architecture foundations

## CYBERNETIC Foundations

### **Preface**

How to read the framework's Venn architecture: the Port-Royal comprehension/extension gradient the diagram rides on, the four cybernetic functions (Effector, Regulator, Modeler, Reviser), and the constellations they compose — adjacent-pair feedback loops, triple syntheses, and the level-defining opposite-pair signatures.

Part III grounds the Venn architecture. The line-by-line diagram, the label libraries, and the row-slot tables appear in each of the Inheritance_Lines line docs (the shared framework is duplicated across all three; per-cell tables for a given line are in that line's file). The wider evolutionary story — personality as biographical signature, the cybernetic-inheritance literature, line-specific instantiation, bramble growth and the relay, the retellings of the selection cycle, the maturity gradient, and what the Trellis Framework adds — sits in Part I above.

### **The bramble and the trellis**

The framework's central metaphor is a pair. *Bramble* is the unit — the cybernetic organism whose architecture and personality the framework specifies, instantiated as the developmental artifact at each of twelve cells. *Trellis* is the framework's own architecture, the scaffold of cybernetic functions, motivations, signatures, capacities, and breakthroughs, organized line by line and cell by cell across the twelve.

---

### **Reading the Venns**

The Venn architecture relies on a logical relationship the Port-Royal logicians named in 1662. Antoine Arnauld and Pierre Nicole, in *La Logique, ou l'art de penser*, paired the terms comprehension (what later logic calls intension: the set of attributes that define a concept) and extension (the set of things falling under the concept). Their thesis: the two vary inversely. Add an attribute to a concept and the class of things it picks out typically shrinks; drop an attribute and the class expands. Their canonical example was geometric. "Triangle" has thinner comprehension than "equilateral triangle," which carries every attribute of triangle plus equality of sides. But "triangle" has larger extension, because every equilateral triangle is a triangle and not the reverse.

Two caveats. The relationship is a tendency rather than a theorem; redundant attributes can be added without excluding anything. And modern logic since Frege has reframed both terms more rigorously, with extension as the set of satisfying objects and intension as something closer to a function from possible worlds to extensions. The Port-Royal version is the philosophical ancestor of the modern formalism, not the formalism itself.

The working intuition (more specification, fewer cases) is what the Venn architecture rides on, and it sorts the regions into five content-types. Single-motivation regions have one attribute, large extension, thin comprehension; they carry motivations. Two-attribute regions come in two kinds: adjacent pairs carry tendencies, opposite pairs carry signatures, both with smaller extension and richer comprehension than the singles. Triple regions have three attributes, smaller still, richer still; they carry capacities. The center has all four attributes, the smallest extension of any region, and the richest comprehension; it carries the breakthrough, the unique synthesis that requires all four motivations to produce.

This is why the breakthrough at the center is not a fifth motivation. A fifth motivation would be a new attribute added at the same level as the original four. The breakthrough is what falls out from the intersection of all four; it is the highest-comprehension, smallest-extension region of the Venn, which is exactly what an architecture this geometry generates.

---

### **Every Center Is a Selector**

The center of a Venn carries that Venn's breakthrough. At every scale the framework uses, that breakthrough turns out to be whatever does the selecting for the units the Venn is about.

A founding cell's center is its line's selector, which the line docs state directly. The center of the Venn of Lines is Darwinian evolution by natural selection. The center of the selection cycle is selection itself, which is the four stages running as one turn.

Those are three instances rather than three coincidences. Blind variation with selective retention, after Donald Campbell, is the scale-general description of what a selector does, and each of the three is that description at one scale. So the rule generalizes: name a Venn, and its center is what selects among the units it is drawn over.

One consequence is worth carrying. A selector discards, so every center has a residue, and the residue scales with how selective the center is. Natural Selection's residue is death. Attention's is everything that stayed live and never won the workspace. Conversation's is everything thought and not said.

---

### **The Scope of a Cell Claim**

A cell claims that on this thread, at this rung, four flag-carriers jointly produce one breakthrough. The clade name is the rung's address. It is not a quantifier over the clade's membership.

The distinction needs stating because the diagram is drawn as a ladder, and readers arrive at a ladder expecting a ranking. Four readings the matrix does not license:

**Not exclusive.** The cell does not claim that only members of the clade carry the capacity. Off-thread lineages build their own stacks and reach their own syntheses above their branching points. A crow that simulates or an octopus that models is the architecture working, not the architecture breaking. See 'Off-Thread Branches'.

**Not a priority claim.** The cell does not claim the clade got there first. Where this framework says a cell introduces something, the introduction is indexed to this thread. Another thread may have reached the same synthesis earlier, later, or not at all, and the cell is silent on all three.

**Not an absence below.** The cell does not claim the capacity is missing at lower rungs. Motivations retire into backgrounded infrastructure and keep operating. See 'The Maturity Gradient'.

**Not a description of any living member.** The cell describes what the rung installs. Every living member sits above its rung on its own branch and carries its own elaborations, so a member's four active flag-carriers are read off that member's own stack rather than off the matrix. See 'Off-Thread Branches'.

One question about a cell is always legitimate, and it is none of the four. A reader may ask whether the capacity reconstructs below the rung on this thread. That is the branch-point test, and a capacity that clears it does move the label. See 'Off-Thread Branches'.

The ladder shape encodes genealogy and not rank. A thread has an order because descent has an order. Every living lineage has been evolving for the same interval, and the rungs above any branching point belong to whoever climbed them.

---

### **The Four Functions**

The four rows of the Trellis Framework's diagram name four cybernetic functions of the unit at every level. Each function has a single role. Together they constitute a complete adaptive control architecture.

A motivation is a dimension along which the units of a clade reliably differ. Each motivation occupies one of the four functional positions and names the variation that position carries at that cell. Persistence names how tenaciously protocells hold a boundary against dispersal. Commitment names how far a symbolic-line unit binds itself to a chosen course. Both are the same kind of construct because both are dimensions of measured variation.

The word carries no intention. A motivation is not an inner state, not a goal the unit holds, and not a cause the unit contains. It is a coordinate, a place in the classification where the units of a clade spread along a measurable range. What produces the spread is selection acting on heritable variation, and no motivation is ever asked to do that work.

This keeps description and explanation apart. Naming a dimension is not explaining it, and no unit is made to vary by the name of the axis it varies along.

*Epistemic status: framework definitional commitment. Separating a descriptive trait construct from the mechanism that produces it follows Fleeson and Jayawickreme's Whole Trait Theory. Supplying that mechanism architecturally rather than behaviorally follows DeYoung's Cybernetic Big Five Theory.*

**Effector.** The line's executive arm. What makes the unit execute its native verb: persist at the genetic line, seize at the neuronal line, commit at the symbolic line. Effector motivations are the line's primal directives: Persistence, Impetus, Commitment. Action is the row's function. In selection, the Effector weights recency: to act is to commit to the freshest signal. Externalization names the same function viewed from outside the unit: the Effector propagates outward what the Regulator stabilizes, the Modeler models, and the Reviser revises. *Evolutionary signature:* founding form of each line, line present, regulatory layer not yet stabilized.

**Regulator.** Closed-loop stabilization against stored references. The rule both is the setpoint and enforces it; that is why the comparator and the storage are one row, not two. Regulator motivations are what makes the unit's behavior consistent across instances: Dissipation, Coordination, Mastery, Stability. Stabilization is the row's function. In selection, the Regulator weights familiarity: to stabilize is to defend the established predictor against new rivals. *Evolutionary signature:* stored regulation, adjustable rules govern responses without rewriting the underlying structure.

**Modeler.** Internal representation that organizes inputs into a usable account of the world. Sensing is downstream of having a model worth updating. Modeler motivations are what makes the unit's interior do representational work: Self-Organization, Interiority, Autonomy, Representation. Modeling is the row's function. In selection, the Modeler weights potency: a single account foregrounds the strongest input and lets it overshadow the faint. *Evolutionary signature:* organized interiority, internal organization with multiple co-occurring properties (opacity, modularity, protected operating conditions, capacity expansion, asymmetric exchange, internal coordination); structurally interior, not just bounded.

**Reviser.** Meta-loop that revises the references the regulator stabilizes against. Reviser motivations are what makes the unit able to change its own goals: Self-Production, Excitability, Affiliation, Universality. Revision is the row's function. In selection, the Reviser weights novelty: to revise is to weight what hasn't been seen and let the familiar fall to background. *Evolutionary signature:* specialized differentiation, division of labor among parts that, in the bridging cases, produces the next line's goo.

Each function carries a signature bias in selection — the rule it applies to decide which cue to credit. The four are recency (Effector), familiarity (Regulator), potency (Modeler), and novelty (Reviser). Every line runs this bias through its own selector: differential reproduction on the genetic line, attention on the neuronal line, differential adoption on the symbolic line. On the neuronal line these four are the Pavlovian associability heuristics — eligibility trace, blocking, overshadowing, and latent inhibition. The bias is not separate from the function; it is the function seen from the selection side.

The sequence is not arbitrary. There is no Regulator without an Effector to regulate, no Modeler without a regulated system whose internal state is worth representing, no Reviser without a model worth updating. Each row depends on the prior row having been achieved. This is why the cybernetic functions emerge in this order at every line, and why the evolutionary descriptions track the functional ones: an effector must be present before it can be regulated; regulation is required before an interior can be defended; a defended interior is required before its parts can be specialized.

The four cybernetic functions are all primaries: single-attribute building blocks at the base of the Port-Royal gradient that organizes the Venn. The dependency sequence (Effector → Regulator → Modeler → Reviser) does not establish a gradient AMONG the four. Each primary is one attribute. The gradient runs across constellations that combine multiple primaries: single (1 attribute) to pair (2) to triple (3) to center (4).

What the dependency sequence DOES establish is the temporal order in which higher-gradient constellations become evolutionarily available. Pair constellations require at least one function beyond the Effector. Triple constellations require three of the four. Center constellations require all four in place. The Port-Royal gradient is the spatial organization of the Venn. The dependency sequence fills the Port-Royal gradient over evolutionary time.

The four functions sort onto two orthogonal axes.

**Object vs. control.** The Effector and Modeler are object-level: what the system operates with (action and model). The Regulator and Reviser are control-level: what shapes the system's operation. The control-level rows take the object-level rows as input.

**Action vs. model, and stabilize vs. revise.** Within each axis-cluster, the two functions take opposite positions. The Effector acts and the Modeler models. The Regulator stabilizes and the Reviser revises. The stabilize/revise distinction is the explore/exploit axis at the cybernetic-meta level.

---

### **The Mirror: Two Poles, Two Functions**

Walk the four functions in order: Effector, Regulator, Modeler, Reviser. Two of the four functions serve both poles, maintenance and variation, and two serve one pole each.

The Effector and the Modeler are shared. The Effector acts, which variation needs, because it expresses variation into the world, and which maintenance needs, because it drives the unit back to reference. The Modeler represents, which variation needs, because it supplies the model that revision rewrites, and which maintenance needs, because it supplies the forecast that regulation acts on. Each of these two functions sits on one edge of each pole.

The Regulator and the Reviser are exclusive. The Regulator holds a reference and defends it, which is maintenance and nothing else. The Reviser generates variation and rewrites the reference, which is variation and nothing else. Variation is rooted in the Reviser (see "The Four Functions as the Variation-Selection Cycle," Part I); maintenance is rooted in the Regulator by the same logic. These are the two roots, one per pole, and they are the Operator diagonal, the pair that differs in both bits of the reflexivity square, sighted-bounded against blind-unbounded. Selection belongs to neither. It is Darwin at the center, and it acts on what both poles produce.

The canonical Venn of Lines adds one thing to hold in view, because it uses the same function names at a second scale. At the scale of the whole tree each line plays one function: genetic is the Effector, neuronal is the Regulator, symbolic is the Modeler, and the fourth line is the Reviser. So "the Regulator" names both a function that runs inside every line and, once, a whole line. Read it as the function, the within-line Regulator that every line carries, not the neuronal line alone: the neuronal line is the tree's exemplary maintenance line, and the fourth line its exemplary variation line.

The origami identity states the split in one image. A folded form is creases and panels. The creases are where the sheet changes; the panels are what stays rigid so the change does not tear the sheet. Variation is the creases. Maintenance is the panels. Compression is the fact that the two are complementary: a form is cheap to specify exactly when its change lives at sparse creases and its panels hold.

*Ratified mapping (origami). Transfers: creases as the locus of variation, panels as the locus of maintenance, compression as the complementarity of the two. Does not transfer: the origamist's foresight, since the framework's folds are placed blind, and the change of paper across lines, since each goo is a different sheet. Scope: within a line.*

*Epistemic status: the shared-versus-exclusive reading of the four functions is committed framework structure, following from the adjacent-pair loops already in canon. The origami identity is committed here and ratified again for the digital goo in "The Seam: What Maintenance Holds Invariant" (Part I).*

---

### **Adjacent Pairs as Closed Feedback Loops**

Each adjacent pair is a closed cybernetic loop between two of the four functions. There are four such loops because there are four adjacent pairs around the cycle.

**Effector × Regulator \= Controller.** Closed-loop control. Action goes out; the regulator measures error against stored reference; the regulator adjusts. The textbook feedback loop.

**Regulator × Modeler \= Anticipator.** Model-informed regulation. The model lets the regulator look ahead instead of reacting only to error. Predictive control; Kalman-style state estimation; active inference's predictive coding loop.

**Modeler × Reviser \= Adapter.** Self-revising model. The model gets updated by the reviser; the reviser proposes updates the model integrates. This is what learning means in the most fundamental sense, model adaptation.

**Reviser × Effector \= Explorer.** Exploratory action. Action that tries new things; results revise what gets tried next. The seeker of epistemic value. 

The four adjacent-pair functions are the four primitive cybernetic loops. Every more complex constellation is a synthesis of these.

### **The Two Modes: Feedback and Foresight**

The Regulator maintains in two modes, and they are the two edges it sits on.

Feedback is the Controller edge, the Regulator paired with the Effector. The unit measures the gap between where it is and where its reference says it should be, and it acts to close the gap. This is the textbook closed feedback loop, canon since Wiener. Feedback waits for error and then corrects it. It needs no forecast, only a reference and a way to sense the deviation from it.

Foresight is the Anticipator edge, the Regulator paired with the Modeler. The unit carries a model of how the world behaves, so it can act on predicted error before the error occurs. The good-regulator theorem belongs here, not to feedback. It says that once the world outruns stored correction, good regulation must grow a model, which is the pull from the Regulator toward the Modeler, not a property of regulation as such. Pure feedback needs no model; foresight is the mode the theorem charters. So the theorem, read closely, is less about the Regulator than about what the Regulator must reach for, and the Anticipator is that reach made into a standing loop. Foresight prepares for the disturbance the feedback loop would otherwise have to absorb after it lands.

Which mode wins depends on the weather. Feedback wins in a world too chaotic to forecast, where preparation is wasted and only fast correction survives. Foresight wins in a predictable world, where the disturbance can be modeled and met before it arrives. Brand's ocean gives the two modes their faces. Knox-Johnston, who deals with what comes, is the feedback maintainer who takes each failure as it arrives. Moitessier, who prepares for the worst, is the foresight maintainer who services the boat before the storm.

The genetic line runs both modes without metaphor. Feedback is DNA repair: mismatch repair and break repair that fix damage after it lands. Foresight is adaptive immunity: the CRISPR-Cas system keeps a record of past invaders as stored spacers and cuts the ones it has met before, on sight, and proofreading catches the error before it sets. Moitessier's logbook and the spacer array are the same device, a memory of past trouble kept so the next instance is met early.

*Ratified mapping (the sailors). Transfers: the two maintenance postures and their regime-match. Does not transfer: the sailors' intent, and a third sailor, Donald Crowhurst, who is treated as a failure of maintenance rather than a mode of it, in "When the Tax Comes Due" (Part V).*

*Epistemic status: the two edges are canon adjacent-pair loops. Their reading as the two modes of maintenance, and the regime-match that selects between them, are framework theoretical commitments.*

---

### Tendency knobs: each toggles between clade N and clade N−1

Every tendency knob is installed at one cell and toggles between two adjacent functions: the cell's own function (N) and the function of the cell below it (N−1). The knob's volume-up pole is the cell's own bias, the newer installed layer, the derived setting. Its volume-down pole is the prior cell's bias, the ancestor showing through, the ancestral setting. A knob is therefore never the property of one clade alone; it exists to toggle between a clade and its predecessor.

Which adjacent-pair loop a knob is follows from the cell's function, because the cell's function is the up pole and the predecessor's function is the down pole:

- Effector cells (Protocell, Bilaterian, Band-Human) install Explorer knobs. Up is recency (Effector); down is novelty (the prior Reviser). The Explorer edge (Reviser × Effector) is also the line-bridge edge, so an Effector cell's down pole reaches back across the line boundary to the previous line's Reviser.
- Regulator cells (Prokaryote, Vertebrate, Settlement-Human) install Controller knobs. Up is familiarity (Regulator); down is recency (the prior Effector).
- Modeler cells (Eukaryote, Mammal, City-Human) install Anticipator knobs. Up is potency (Modeler); down is familiarity (the prior Regulator).
- Reviser cells (Eumetazoa, Primate, Empire-Human) install Adapter knobs. Up is novelty (Reviser); down is potency (the prior Modeler).

The four selection biases are recency, familiarity, potency, and novelty, one per function. On the neuronal line these biases are named as the four Pavlovian associability heuristics: eligibility trace (recency), blocking (familiarity), overshadowing (potency), and latent inhibition (novelty). A tendency knob toggles between the two heuristics of its two functions: the up pole runs the cell's own heuristic, the down pole runs the predecessor's. The Orienting knob (Bilaterian, Explorer) toggles eligibility trace (recency, up) against latent inhibition (novelty, down). The Coping knob (Vertebrate, Controller) toggles blocking (familiarity, up) against eligibility trace (recency, down). Every knob around the cycle toggles the two-of-four that its function and its predecessor's function name.

The biases install one per cell as each cell's own function arrives, in the order the functions arrive: familiarity at the first Regulator cell (Prokaryote), potency at the first Modeler cell (Eukaryote), novelty at the first Reviser cell (Eumetazoa), and recency at the first Effector cell whose knob performs credit assignment (Bilaterian). Protocell's Effector knob is the wind-up (Going), which carries no credit-assignment heuristic, so recency as a running heuristic waits for the neuronal Effector at Bilaterian. From Bilaterian onward all four heuristics are present, and each later cell's knob re-toggles the same two-of-four its function and predecessor name.

Volume up and volume down are properties of knob settings, not a ranking of the four functions, which remain equal primaries. The up pole is the newer layer; the down pole is the older layer showing through. This is the eclipsing account applied to the knobs: at a knob's down pole the newest layer goes dormant and the ancestor beneath runs.

### Durable and transitional tendencies

Each cell installs two new tendency labels, and the two have different lifespans. A durable tendency holds its edge for three consecutive cells. A transitional tendency holds its edge for one cell and gives way at the next.

At any cell, three of the four edges carry durable tendencies and one carries a transitional tendency. The transitional edge is the next edge clockwise from the edge receiving that cell's new knob. Bilaterian installs the Explorer knob, so the Controller edge is transitional there and carries Affect for that cell alone. Vertebrate installs the Controller knob, so the Anticipator edge is transitional there and carries Development Rate.

A transitional tendency carries no knob. It does not hold its edge long enough for a household setting to mean anything from one quarter to the next. All twelve knobs sit on durable tendencies, and each knob is installed at the first of its tendency's three cells.

This fixes how long a knob lives. A knob lasts exactly as long as its tendency label lasts. It comes online when the label arrives at its edge, and it retires when the label gives way. The knobs in play at a cell are therefore the knobs of that cell's own tendencies, never a label the Venn has already replaced.

The transitional edge also names what comes next. The edge running a transitional tendency at one cell is the edge that receives the following cell's new knob, so the gap in the current quarter marks where the next quarter's knob lands.

*Epistemic status: the three-cell durable run holds for all twelve knob-bearing tendencies. Two labels at the founding cells run short of three, Enclosure Type across Protocell and Prokaryote and Aging Type at Protocell, because the alternation has no cells below Protocell to start from. Neither carries a knob.*

### **Function Ground Truths: World, Body, Future, Mind**

Each cybernetic function's job fixes what its output is about — where the state it tracks actually lives, and therefore what would have to be checked to find out whether the output is right.

**Effector → a world.** The Effector's job is to act, and action is directed outward, at something external to the unit. What the Effector's output is about lives in a world: the thing acted on, checkable by looking at the world itself.

**Regulator → a body.** The Regulator's job is to stabilize the unit's own behavior against a stored reference (the Controller loop, "Adjacent Pairs as Closed Feedback Loops"); its comparison runs entirely inside the unit. What the Regulator's output is about lives in a body: the unit's own current state, checkable by looking at the unit.

**Modeler → a future.** The Modeler's job, in its foresight mode, is to look ahead of the disturbance rather than wait for it ("The Two Modes: Feedback and Foresight"). A model that only describes the present is a Regulator's mirror, not a Modeler's use; what makes modeling worth its cost is running forward. What the Modeler's output is about lives in a future: a state that does not yet exist, checkable only once it arrives.

**Reviser → a mind.** The Reviser's job is to change the unit's own references, not merely update them against new data ("Reviser motivations are what makes the unit able to change its own goals," "The Four Functions"). A reference the unit could derive on its own is an update, not a revision; the only source of a reference the unit did not already have is a system whose references were never the unit's to begin with — another agent. This is not incidental to the Primate cell: Affiliation is the Primate Reviser motivation, and Affiliation is the goo the neuronal line ratchets for the symbolic line's exchange-based selection to run on ("The Four Functions as the Variation-Selection Cycle," Part I). Exchange has no meaning for one party. The neuronal Reviser is not a function that happens to notice other minds; representing another mind is the raw material it exists to produce, because the next line cannot start without it. What the Reviser's output is about lives in a mind: a set of references the unit does not have and cannot derive, checkable only by consulting the agent whose they are.

A world, a body, a future, a mind — one location per function, and each is where that function's own job already points, not an added stipulation.

The four locations sit at increasing remove from the unit's present moment. A world and a body are both available for inspection now. A future has not happened yet. A mind is never available for direct inspection at all. Any layered architecture built on these four functions inherits that ordering, and inherits it as a property of the functions rather than as a convention of its own.

*Epistemic status: the four function-jobs (act, stabilize, model, revise) and the two modes (feedback/foresight) are canon, established above in "The Four Functions" and "The Two Modes." The ground-truth-location reading of each job — world, body, future, mind — is a framework theoretical commitment drawn from those canon jobs, not yet independently attested outside the framework. The Reviser argument additionally depends on "The Four Functions as the Variation-Selection Cycle" (Part I) and on the claim that exchange-based selection requires a second party; that inferential step is the framework's own, not sourced.*

*Scope: the goo-ratchet step in the Reviser derivation is line-specific. Affiliation and Shannon goo are the neuronal Reviser's, not a general property of Revisers, so that derivation is stated for the neuronal line and not extended to the genetic or symbolic lines here.*

### **Why the Cycle Turns: Absence Recruits**

The four adjacent-pair loops above say what the loops are. This section says why the cycle turns from one to the next, and why in one direction.

**Constitutive absence.** A phenomenon can be organized around something not present in it. Deacon calls this constitutive absence: a precise missing something that is a defining attribute of a function or a purpose. Hemoglobin is the biological case. The molecule that carries oxygen spends much of its cycle holding none, and its whole allosteric machinery is organized around a gas that is not part of the molecule. Read the molecule alone and its function is invisible; read it against the oxygen it is shaped to bind and release, and the function appears. The framework already makes this move at the center, where each capacity is defined by the one function it lacks: the Planner without a live Effector, the Pursuer without a live Regulator, the Reactor without a live Modeler, the Conservator without a live Reviser. Absence already does definitional work. It also drives the cycle.

**Absence recruits.** Each function is complete at what it does and incomplete on its own, and its specific lack recruits the next function. An Effector acts, and open action cannot see its own result; the Regulator supplies the missing comparison, closing the Controller loop. A Regulator holds a reference, and a fixed reference cannot look ahead; the Modeler supplies the missing anticipation, closing the Anticipator loop. A Modeler predicts, and a model fitted to the past goes stale; the Reviser supplies the missing update, closing the Adapter loop. A Reviser rewrites the model, and a rewritten model changes nothing until something acts on it; action supplies the missing test, closing the Explorer loop and returning the cycle to the Effector. This is the absent-function principle of the capacities applied to the transitions between functions. The four loops named above are the four answers to four constitutive absences.

**Each recruitment is already attested.** No single source holds the whole cycle, and every edge of it is owned somewhere. Effector to Regulator is negative feedback after Wiener, and the TOTE unit of Miller, Galanter, and Pribram, where an incongruity recruits an operation. Regulator to Modeler is the good regulator theorem established in Part I: good regulation already contains a model, so the Regulator's absence is filled by definition, a point Rosen's anticipatory systems make from the other side. Modeler to Reviser is owned three times over, by Piaget's equilibration, where failed assimilation recruits accommodation, by Powers' reorganization, where persistent error recruits restructuring, and by Friston's free energy, where prediction error recruits model update. Reviser to Effector is Peirce's doubt settled only in a habit for action, and West-Eberhard's genes-as-followers, where plastic innovation leads and structure consolidates behind it.

**Why the order is forced.** The recruitments run one way and skip no steps, and two forces set that direction. The first is build-order dependency: each function is constituted by the one before it, so it cannot be recruited until its predecessor exists to complete. This is Deacon's own architecture, where teleodynamics is built on morphodynamics built on homeodynamics, and it is already stated for the lines in the Venn of Lines section's "Why the ordering is forced, not observed" argument. An Effector cannot recruit a Modeler, because with no Regulator there is no regulation problem for a model to be a model of, and the good regulator theorem defines the model's job as serving regulation. An Effector cannot recruit a Reviser, because with no Modeler there is no model to revise. The skips are ruled out because the skipped-to function has nothing built yet to bind to. The second force is that control flows the other way: the stack is assembled from the bottom and run from the top, as in the Powers and Carver-Scheier hierarchy, where a higher loop sets the reference for the loop below. Assembly climbs; control descends; the two meet, which is why the structure is a directed cycle and not a heap.

**Why the cycle closes back to action.** The top of the epistemic stack answers to no higher loop, so the closure at Reviser to Effector has its own account, and two forces supply it. The first is Darwinian selection. The Reviser generates variation and the Effector is the selection-outcome (see "The Four Functions as the Variation-Selection Cycle" in Part I); variation never expressed as an acting, selected unit is not inherited, and the framework's scope is a cybernetic loop subject to inheritance, so a loop that never closes this edge is not the kind of loop the framework is about. This is Donald Campbell's blind variation and selective retention at the scale of the cycle. At the line boundary the edge is the transformation of one goo into the next, anchored by the fertilized egg: recombination is blind variation producing an unbound unit, and implantation is the binding that turns it into a controlled program. The second force is the epistemics of the untried: epistemic value sits at the Reviser, the payoff of an untried action is unobservable except by taking it, and taking it is action. Within a single lifetime the closure is exact in active inference, where free energy is lowered either by changing the model, the Reviser's horn, or by changing the world, the Effector's horn, and the active in active inference names the Effector. Expected free energy's two parts are the two forces: pragmatic value is the selection leg for one agent, and epistemic value is the exploration leg. Both discharge only through the Effector. One thing to keep straight: self-production and autopoiesis, after Rosen and after Maturana and Varela, name what the Reviser is, the self-producing work that keeps a line far from equilibrium; they are not the closure mechanism, which is carried by selection and by exploration. The two closures are one engine at two scales: Donald Campbell's blind variation and selective retention is the scale-general umbrella, natural selection is the selector across the slow loop, and free-energy minimization, with reward as prior preference and attention as precision, is the selector across the fast loop, the same contest Edelman's neural Darwinism runs one level down in the tissue.

*Scope note: active inference is formally exact at the neuronal line, where the neuronal goo is Kullback-Leibler goo. At the genetic and symbolic lines the same closure runs through the substrate-independent free-energy principle in each line's own machinery, not through mammalian active inference taken literally.*

**What is forced and by which kind of force.** The cycle is forced the whole way around, by three kinds of force. Effector to Regulator to Modeler is forced at close to theorem strength, on settled cybernetics and the good regulator theorem. Modeler to Reviser is forced by convergence, three independent traditions deriving the same recruitment. Reviser to Effector is forced by the structure of inheritance, conditional on scope: it holds for inheritance-bearing loops, which is the framework's domain, not for arbitrary control systems outside it. The scope condition is the boundary of the claim, not a soft spot.

**The cycle is a helix, not a circle.** The cycle returns to its start without returning to the same place. The same four functions run three times, once per inheritance line: the genetic line runs Effector to Reviser across its four cells, the neuronal line runs the same four functions again across its four cells, the symbolic line runs them a third time, and the cycle is self-similar across the three lines, which is the framework's fractal character read off the cross-line architecture. It is also self-similar across timescales: the within-unit fast loop runs the four functions in a single lifetime, and the cross-line slow loop runs the same exploration-into-structure dynamic across deep time, one dynamic at two scales. The turns are stacked, not concentric. Each line's groundwork is the prior line's mature output, so the cycle that closes at the end of one line opens the next line one level up; West-Eberhard's sequence is the mechanism of that lift, the explorer's plastic innovation at the top of one turn consolidated into the inherited structure the next turn stands on. *Metaphor mapping: what transfers from the ouroboros, the snake that eats its tail, is that the cycle closes and the output re-grounds the input. What does not transfer is return to an identical origin; inheritance ratchets, so each turn opens on a higher line, and nothing comes back to exactly where it started. The ouroboros is the two-dimensional shadow of a three-dimensional helix, the image produced by collapsing the inheritance axis and standing directly beneath the climb, useful as a picture, wrong as the geometry.*

**An illustrative instance: the saeculum.** Strauss & Howe's generational theory gives the helix a legible, human-scale instance. Its four turnings run the four functions in order, and the archetype coming of age in each turning works that function (see "Three Retellings of the Selection Cycle," Part I).

A repeating archetype cycle alone would be a circle, not a helix, the same four types recurring with nothing carried forward. What keeps the saeculum from closing back on itself is an external ratchet: the technological and material world each generation is raised into, and later reshapes in turn. The population does not return to where it started because what it is climbing on has itself changed.

*Ratified mapping. Transfers: the shape, a repeating structure riding an axis that prevents return. Does not transfer: the mechanism. The framework's cross-line helix ratchets by internal consolidation, one line's mature output becoming the next line's groundwork. The saeculum ratchets by an external forcing axis, the changing material and technological world, not by the archetype cycle consolidating its own output. This is a structural analogy to the cross-line helix, illustrating the same shape at a different scale and by a different mechanism, not an instance the cross-line helix itself runs on.*

*Epistemic status: [framework]. Strauss & Howe's periodization is not consensus historiography; historians generally treat it as pattern-fitting. Included as an illustrative instance of the helix shape, not as a new theoretical construct or empirical anchor.*

**Absence at every scale.** The same principle runs at three scales the framework names. It defines each capacity by the function that capacity lacks. It recruits the next function across the cycle, by the lack the current function carries. And it exposes an ancestor in real time under eclipsing, where a tendency's low pole is the newest layer made absent and the older architecture showing through. Three applications, one principle.

**Affect is not an axis.** A knob's derived and ancestral poles are set by which of the four biases its own function favors, not by any shared quality of confidence, energy, or restraint that might seem to run across knobs. Two knobs on different functions can produce poles that sound alike without that resemblance tracking derived and ancestral status at all. Coping (Regulator, familiarity) and Extraverted (Modeler, potency) make the case cleanly: Little is derived and Boss is derived, and they share no surface affect, one a retreat into restraint, the other an assertion into the room; Beast is ancestral and Vibe is ancestral, and they share none either, one a raw approach, the other an ambient hold. Sorted by ear instead of by function, all four land on the wrong side of the line. The bias is load-bearing; the vibe is not.

**The low pole echoes the predecessor's own signature.** What shows through at a knob's low pole is not the current layer turned down; it is the predecessor cell's own derived bias, recurring, because that is what a low pole is built from. This is checkable label by label, not just assertable. Beast, Coping's ancestral pole, is Vertebrate's Regulator falling through to Bilaterian's Effector, and its flavor is recognizably Learn's flavor one clade back, leaning on whatever is freshest before the pattern confirms. Vibe, Extraverted's ancestral pole, is City-Human's Modeler falling through to Vertebrate's Regulator, and its flavor is recognizably Little's flavor one clade back, holding to what has already proven itself rather than asserting something new. Eclipsing does not produce a faded copy of the current cell. It produces the ancestor's own move, unweakened, wearing the current cell's name.

**Borrowed parts, assembled cycle.** That absence recruits is not new: negative feedback is that idea, and Deacon owns the name constitutive absence. No single source holds the closed cycle. What is assembled here is the whole: the four functions as a closed cycle, the same cycle recurring across the three lines, and the low pole of each function reading as the prior layer showing through. The giants own the edges; the closed cycle, the cross-line recurrence, and the eclipsing are the framework's assembly.

*Epistemic status: the extension of the absent-function principle from the capacities to the transitions, and the unification of eclipsing with the same principle, are framework theoretical commitments. The affect-is-not-an-axis caution and the predecessor-echo claim extend that unification and are commitments of the same kind, checked against the twelve ratified knob labels within a line; the check has not yet been run across a line boundary, at the Explorer knob's down pole, which reaches to the prior line's Reviser, and should not yet be assumed to hold there. Every joint of the cycle is forced; the closing joint is forced conditional on the unit being an inheritance-bearing loop. Prior-art anchors drawn from outside the framework's existing citation set (Wiener, Miller-Galanter-Pribram, Carver-Scheier, Powers, Piaget, Peirce, Donald Campbell, Rosen) are named at standard strength and are not yet verified against primary sources.*

---

### **Triples as 2×2 Synthesis**

Each triple synthesizes three of the four functions. The four triples sort into a 2×2 along the same two axes that organize the four single functions.

**Absent Effector (Regulator \+ Modeler \+ Reviser) \= Planner.** Synthesizes regulation, representation, and revision without execution. Strategic deliberation.

**Absent Modeler (Effector \+ Regulator \+ Reviser) \= Reactor.** Synthesizes action, regulation, and revision without internal model. Model-free regulated action that updates from experience. The structural shape of model-free reinforcement learning: policies (Regulator), policy updates (Reviser), action (Effector), no world model (Modeler).

**Absent Regulator (Effector \+ Modeler \+ Reviser) \= Pursuer.** Synthesizes action, representation, and revision without stabilization. Goal-pursuit driven by model and reviser without rule-enforced inhibition.

**Absent Reviser (Effector \+ Regulator \+ Modeler) \= Conservator.** Synthesizes action, regulation, and representation without revision. The mature loop running with no meta-update. Pursues established goals via stable model; cannot update them.

The 2×2 structure:

The triples containing the Regulator × Reviser pair are Planner (model-rich, action-silent) and Reactor (action-rich, model-silent). Both contain Regulator + Reviser; they differ on which of Modeler vs Effector is added.

The triples containing the Effector × Modeler pair are Conservator (stabilize-rich, revise-silent) and Pursuer (revise-rich, stabilize-silent). Both contain Effector + Modeler; they differ on which of Regulator vs Reviser is added.

*Epistemic status: the architectural derivation of the 2×2 triple structure is HIGH confidence. The structure follows directly from the row-function definitions.*

---

### **Opposite Pairs as Level-Defining Couplings**

The two opposite-pair regions of the 4-circle Venn (Effector × Modeler and Regulator × Reviser) carry the framework's signatures, the level-defining personality couplings. Each level produces one signature. The coupling pairs the just-introduced motivation with a motivation introduced earlier on the same opposite pair.

The opposite pairs alternate across consecutive levels. The introduction order — Regulator, then Modeler, then Reviser, then Effector — places the just-introduced motivation on a different opposite pair at each successive level.

Each opposite pair carries a stable cybernetic-role label that names the kind of action the coupling supports — the third family of constellation labels, alongside the adjacent-pair roles (Controller, Anticipator, Adapter, Explorer) and the triple roles (Planner, Pursuer, Reactor, Conservator). The **Effector × Modeler pair is the Connector**; the **Regulator × Reviser pair is the Operator**. Each signature carries its own label naming the level-specific empirical content. A signature persists for two consecutive cells, the cell where it is introduced plus the next. It then shifts when one of its two contributing motivations is eclipsed.

The **Operator (Regulator × Reviser) pair** hosts Behavioral Syndrome (introduced at Vertebrate, persists at Mammal), Sociometer (introduced at Primate, persists at Band-Human), Self-Construal (introduced at Settlement-Human, persists at City-Human), and Identity (introduced at Empire-Human). The Operator pair maps onto the agency dimension of Bakan's agency-communion distinction, also developed in Wiggins's interpersonal circumplex.

The **Connector (Effector × Modeler) pair** hosts Temperament (introduced at Bilaterian, persists at Vertebrate), Self-Model (introduced at Mammal, persists at Primate), Self-Reference (introduced at Band-Human, persists at Settlement-Human), and Self-Evaluation (introduced at City-Human, persists at Empire-Human). The Connector pair maps onto the communion dimension.

#### **The Constructs**

**Lineage (Protocell, Effector × Modeler).** Couples Persistence (Effector, just introduced at Protocell as the genetic line's founding Effector motivation) with Self-Organization (Modeler, carried from Deacon's pre-life groundwork). The persistent chain of replicating forms across generations. A lineage is what selection writes onto when replication is reliable enough to sustain differential survival across many cycles. The construct anchors on Darwin's natural selection in its lineage-bearing form and on evolutionary biology's clade and phyletic-descent concepts. Persists at Prokaryote, where Persistence and Self-Organization both carry.

*Epistemic status: lineage is foundational in evolutionary biology with no controversy. The placement at the Effector × Modeler pair at Protocell is a framework theoretical commitment.*

**Organism (Prokaryote, Regulator × Reviser).** Couples Coordination (Regulator, just introduced at Prokaryote as stored regulation in the genetic register) with Self-Production (Reviser, carried from pre-line groundwork). The bounded, coordinated, work-doing unit. The prokaryote is where "organism" lands as a discrete category: a cell whose stored regulation directs work to maintain itself far from equilibrium. Anchors on cell biology and microbiology and on Maturana and Varela's autopoiesis as the structural definition of self-maintenance through environmental coupling. Persists at Eukaryote, where Coordination and Self-Production both carry.

*Epistemic status: organism is foundational in biology, with edge-case debates about protocell status that the framework handles by reading protocell as proto-organism and prokaryote as the founding form. The placement at the Regulator × Reviser pair at Prokaryote is a framework theoretical commitment.*

**Host (Eukaryote, Effector × Modeler).** Couples Persistence (Effector, carried from Prokaryote) with Interiority (Modeler, just introduced at Eukaryote). The chimeric unit constituted by an incorporated symbiont. The eukaryote's identity is its hosting relationship: an archaeal host carrying the α-proteobacterial endosymbiont (mitochondrion), and in plants the cyanobacterial endosymbiont (chloroplast). The host's inheritance is composite (nuclear plus mitochondrial DNA), and its organized interior includes the symbiont as a defended interior component. Anchors on Margulis's endosymbiotic theory (1967, 1970), Nick Lane's bioenergetics work, and the contemporary holobiont concept (Margulis, McFall-Ngai, Rosenberg) treating host plus integrated symbionts as one ecological-evolutionary unit. Persists at Eumetazoa, where the eumetazoan body continues as host of mitochondria, of microbiome, and in specific lineages of additional endosymbiotic bacteria.

*Epistemic status: the endosymbiotic origin of mitochondria is well-established consensus. The holobiont concept is contemporary but well-developed. The framework's placement of Host at the Effector × Modeler pair is consistent with the existing endosymbiosis treatment at Modeler transitions.*

**Reflex Repertoire (Eumetazoa, Regulator × Reviser).** Couples Coordination (Regulator, carried from Prokaryote) with Excitability (Reviser, just introduced at Eumetazoa). The stored set of coordinated excitable response patterns. Eumetazoa introduce nervous tissue, and reflex repertoires are the dispositional output of coordinated excitable tissue. Cnidarian lineages vary along this axis: anemones are slow-tonic, jellyfish are fast-rhythmic with through-conducting nerve nets, ctenophores have continuous ciliary locomotion under coordinated control. Anchors on comparative neurobiology of basal-metazoan nervous systems (Mackie and others on cnidarian nerve nets) and on behavioral ecology of basal metazoans. Persists at Bilaterian, where Coordination and Excitability both carry. At Vertebrate the Regulator swap from Coordination to Mastery shifts the Regulator × Reviser pair signature to Behavioral Syndrome.

*Epistemic status: documented variation in nerve-net behavior across basal metazoan lineages is empirically established. The placement at the Regulator × Reviser pair at Eumetazoa is a framework theoretical commitment.*

**Temperament (Bilaterian, Effector × Modeler).** Couples Impetus (Effector, just introduced at bilaterians) with Interiority (Modeler, carried from eukaryotes). Behavioral predispositions tied to interior states. This is the founding form of the Effector × Modeler pair, before relational architectures emerge at mammals. Maps to the developmental-psychology temperament tradition (Rothbart; Chess and Thomas; Kagan). Persists at Vertebrate, where Impetus and Interiority both carry.

*Epistemic status: temperament as a developmental-psychology construct is empirically well-established. The placement at the Effector × Modeler pair at bilaterians is a framework theoretical commitment.*

**Behavioral Syndrome (Vertebrate, Regulator × Reviser).** Couples Mastery (Regulator, just introduced at vertebrates) with Excitability (Reviser, carried from eumetazoa). Reinforcement-shaped reactive disposition coupling mastery-related coping with baseline arousal. This is the founding form of the Regulator × Reviser pair. Maps to the behavioral-syndrome literature in behavioral ecology (Sih, Bell & Johnson 2004). Koolhaas's two-tier coping-style taxonomy is the canonical mechanism: proactive versus reactive coping on the SNS-HPA ratio, with baseline arousal as overall magnitude. Persists at Mammal.

The physiological mechanism has three components. The sympathetic nervous system is the fast arm. The hypothalamic-pituitary-adrenal axis is the slow arm. Dopamine is the broadcast neuromodulator coupling the two arms. Proactive copers show higher SNS reactivity and lower HPA reactivity. Reactive copers show the inverse pattern. The behavioral cluster sorts on the SNS-vs-HPA ratio rather than overall magnitude. The architecture has been replicated in rodents, birds, and fish. In fish the HPA-axis analogue is the HPI axis, with cortisol as the slow-arm hormone.

*Epistemic status: Koolhaas's two-tier architecture is empirically established across multiple vertebrate lineages. The placement at the Regulator × Reviser pair is a framework theoretical commitment.*

**Self-Model (Mammal, Effector × Modeler).** Couples Autonomy (Modeler, just introduced at mammals) with Impetus (Effector, carrying the bilaterian-level instrumental-learning machinery). Self-Model is the mammalian self-representation. The mammalian brain's cortex-plus-hippocampus architecture implements it. It includes representations of the unit as agent and of others as agents. The primary anchors are Bennett's *A Brief History of Intelligence* (2023) and Metzinger's self-model theory of subjectivity. Squire's episodic memory system and Freud's ego are architectural anchors. Persists at Primate.

**Sociometer (Primate, Regulator × Reviser).** Couples Mastery (Regulator, carried from vertebrates) with Affiliation (Reviser, just introduced at primates). This is the primate-level synthesis of mastery-grounded coping and mentalization-enabled valuation of belonging: an internal gauge that reads the agent's relational value in the group and regulates conduct to preserve inclusion. Anchors on the belonging-gauge literature. Baumeister and Leary's need to belong (1995) supplies the motivation — a fundamental drive to form and maintain lasting interpersonal bonds. Leary's sociometer theory supplies the mechanism — self-esteem as an internal monitor of relational value that falls when inclusion is threatened and motivates corrective action. Eisenberger supplies the substrate — social rejection recruits the dorsal anterior cingulate and anterior insula, the same circuitry as physical pain, so exclusion registers as hurt. Persists at Band-Human, where Mastery and Affiliation both carry.

*Epistemic status: the need-to-belong, sociometer, and social-pain literatures are empirically well-developed. The placement at the Regulator × Reviser pair at primates is a framework theoretical commitment.*

**Self-Reference (Band-Human, Effector × Modeler).** Couples Commitment (Effector, just introduced at bands) with Autonomy (Modeler, carried from mammals). Affiliation evaluated under symbolic-exchange standards. Self-Reference anchors on two bodies of work that operate together. Hofstadter's strange-loop pattern (*I Am a Strange Loop*, 2007) supplies the architecture. The strange-loop architecture is the brain's mechanism for self-referential consciousness. The self-conscious emotions (Tracy and Robins; Lewis; Tangney) supply the manifest content: shame, guilt, embarrassment, and pride, with their characteristic appraisals of self against internalized standards. The self-conscious emotions are how the strange-loop pattern manifests under symbolic-reciprocal evaluation. The self-conscious emotions emerge developmentally around age three. They are present universally across human cultures. They are absent or proto-form in non-human primates. Self-Reference persists at Settlement-Human, where Commitment and Autonomy both carry.

*Epistemic status: the self-conscious emotions are an established empirical construct, and Hofstadter's strange-loop account is a developed theoretical proposal. The placement at the Effector × Modeler pair at bands is a framework theoretical commitment.*

**Self-Construal (Settlement-Human, Regulator × Reviser).** Couples Stability (Regulator, just introduced at settlements) with Affiliation (Reviser, carried from primates). Independent versus interdependent self-construal, calibrated by subsistence ecology. Maps to Markus and Kitayama's independent-interdependent self-construal framework. Talhelm et al.'s rice-wheat agricultural ecology is the canonical mechanism by which settlement subsistence demands calibrate the autonomy drive into one constellation or the other. Wheat-style cultivation has lower coordination demands and produces independent self-construal. Rice-style cultivation has high cross-household coordination demands and produces interdependent self-construal. Triandis's individualism-collectivism work provides the broader population-level psychology framing. Persists at City-Human, where Stability and Affiliation both carry.

*Epistemic status: the independent-interdependent self-construal distinction is empirically well-established (Markus and Kitayama; Triandis). The rice-wheat ecological mechanism is documented in within-China data (Talhelm et al. 2014), and the broader subsistence-shapes-psychology framing has substantial cross-cultural support. The placement at the Regulator × Reviser pair at settlements is a framework theoretical commitment.*

**Self-Evaluation (City-Human, Effector × Modeler).** Couples Commitment (Effector, carried from bands) with Representation (Modeler, just introduced at cities). Stable self-relevant evaluative structure, formed where reciprocal exchange meets the city's standing records and codes. Anchored on Core Self-Evaluations (Judge, Hurst, Locke, Erez). Self-esteem, generalized self-efficacy, internal locus of control, and emotional stability cluster as a single trait-level factor. Persists at Empire-Human, where Commitment and Representation both carry.

*Epistemic status: Core Self-Evaluations is an established empirical construct. The placement at the Effector × Modeler pair at cities is a framework theoretical commitment.*

**Identity (Empire-Human, Regulator × Reviser).** Couples Stability (Regulator, carried from settlements) with Universality (Reviser, just introduced at empires). This is the empire-level synthesis of stability and universalizing ideology. Identity is the social-science construct of who the person takes themselves to be within a universalizing order. The primary anchors are Tajfel-Turner social identity theory, Erikson's identity-formation work, McAdams's narrative identity, and Goffman's presentation of self.

Haidt's Moral Foundations Theory is the secondary anchor. It operationalizes the universal moral codes empires encode, with its dimensions (Care, Fairness, Loyalty, Authority, Sanctity, Liberty). Moral Foundations Theory is Reviser-Universality-flavored, which is what places it at the Regulator × Reviser pair rather than the Effector × Modeler pair at this level.

*Epistemic status: social identity theory, Erikson's identity-formation work, McAdams's narrative identity, and Goffman's presentation of self are well-developed empirical and theoretical traditions. The placement at the Regulator × Reviser pair at empires, as facets of one construct, is a framework theoretical commitment.*

#### **The Mammalian Threshold: Three Distinct Achievements**

The mammalian threshold produces three distinct architectural achievements at once. All three are keyed to the new Autonomy drive, but each couples it with a different partner.

**Self-Model** at the Effector × Modeler opposite pair couples Autonomy with Impetus. It is the mammalian self-representation, the modeled agent.

**Remembering Style** at the Modeler × Reviser Adapter adjacent pair couples Autonomy with Excitability. It is the retrospectively-constructed self. It anchors on Kahneman's remembering self. It parallels Bowlby's internal-working-model construct and Freud's ego construct.

**Simulating** at the center (breakthrough) couples all four primaries. It is the whole-Venn synthesis. Active inference is its mechanism. The episodic-memory system is its hardware.

The three are sisters at the same evolutionary threshold, not the same construct. Each has its own architectural placement in the Mammal Venn.

#### **Relationship to the Triples**

Each opposite pair sits inside two of the four triples. The Regulator × Reviser pair sits inside Reactor (Effector + Regulator + Reviser) and Planner (Regulator + Modeler + Reviser). The Effector × Modeler pair sits inside Conservator (Effector + Regulator + Modeler) and Pursuer (Effector + Modeler + Reviser).

The opposite pair carries the signature. The two triples that contain it are constellations where the coupling manifests with an added third element. At Vertebrate, Behavioral Syndrome (Regulator × Reviser) manifests in the Reactor as Temporal Credit, where Effector Impetus adds active execution. It manifests in the Planner as Gut Sense, where Modeler Interiority adds internal-state modeling. At Mammal, Self-Model (Effector × Modeler) manifests in the Conservator as Autonomous Cognition, where Regulator Mastery adds stable regulation. It manifests in the Pursuer as Algorithmic Cognition, where Reviser Excitability adds exploratory drive. At Primate, Sociometer (Regulator × Reviser) manifests in the Reactor as Triadic Awareness and in the Planner as Standing. Self-Model (Effector × Modeler) manifests in the Conservator as Autonomous Cognition and in the Pursuer as Tactical Deceit. At Band-Human, Self-Reference (Effector × Modeler) manifests in the Conservator as Collaborative Fission and in the Pursuer as Alloparenting. Sociometer (Regulator × Reviser) manifests in the Reactor as Meat Pooling and in the Planner as Standing.

The triples are expression forms of the underlying signature.

### The Low Setting and the Layer Beneath

The framework builds personality as a stack of tendencies, added in a fixed order across the three inheritance lines: the genetic line first, then the neuronal line, then the symbolic line. Each new tendency is a layer laid over the ones already present. A tendency introduced at one cell is later eclipsed when a newer layer is built over it. That is eclipsing across evolutionary time. There is a second kind of eclipsing that happens inside one unit, in real time, and it is what a tendency's setting controls.

Eclipsing here means covering, not deleting. The lower layers keep running; the newer layer acts on them and does not replace them. So when a tendency's setting is turned down to its low end, that top layer goes dormant rather than vanishing. The unit then falls through to the layer beneath and runs as it ran before the top layer was added.

This is the claim. The low end of a tendency is not a smaller amount of it. It is the tendency switched off, with the older architecture showing through.

Every knob is a volume knob, with a continuous range from a low pole to a high pole. At the low pole the newer layer goes dormant and the ancestor beneath shows through — the behavior the lineage ran before this knob existed, not a smaller amount of the tendency. Comfy is the warm-seeking every earlier clade already did to recharge; active is the activity-seeking Excitability adds on top of it. The neuronal line's founding knob, Orienting Style, runs short-horizon to long-horizon; at its low pole the recency layer goes dormant and the Excitability home-seeking beneath it shows through.

What falls through depends on which of the four cybernetic functions the dialed tendency belongs to. The functions are added in the order Effector, Regulator, Modeler, Reviser. At a low Regulator setting or a low Reviser setting a behavioral push drops out, either the gain on reward or the weight given to other agents, and the act itself reverts to the lower layer. The Modeler dial behaves differently and deserves care. Its dormant pole is not an intuitive low but the absorbed, immersive end. When the unit is fully immersed in the moment, the self-model that would narrate the moment goes quiet. So at the Modeler's dormant setting the unit still acts at full capacity, and what reverts is the report rather than the act. The unit does the thing without modeling itself doing it.

This cuts against the standard evolutionary reading of personality, the reading associated with Daniel Nettle. That reading gives each personality dimension a fitness trade-off, with real costs and benefits at both the high and the low end, so the low end counts as a strategy in its own right. It also takes the measured dimensions as the whole of personality, a flat set with nothing underneath. Here the dimensions ride on a deep stack of older tendencies, and the low end is not a coordinate strategy. It is the most recent layer absent and the ancestor beneath doing what it always did. The cost the trade-off reading books at the low end is, in this framework, the signature of the layer beneath.

DeYoung's Cybernetic Big Five Theory already casts personality dimensions as parameters of a regulating system, and the framework keeps that cybernetic footing. What the framework adds is the evolutionary order of the layers and the reading of the low end as the top layer eclipsed in real time.

The same ordering predicts how the stack comes apart. Under load, the layers should go dormant from the top down, the most recently added first, exposing each older layer in turn. That is the order the next section treats as failure.

*Epistemic status: the layered architecture and runtime eclipsing are framework theoretical commitments, built on the eclipsing structure already in this doc. The departure from the symmetric trade-off reading is a real prediction and is held as exposed. The precise layer a symbolic-line tendency falls through to is not yet fixed and is flagged open.*

### Disease, Disorder, and Line of Failure

Failures of tendencies and capacities sort by the line at which they emerged. Genetic-line failure is disease: cells, tissues, and organs that no longer maintain homeostasis. Neuronal-line failure is disorder: dispositional constellations and capacities that no longer regulate the organism's life against contextual demands. Symbolic-line failure is disorganization: cultural, institutional, and normative structures that no longer regulate the constituent humans' collective life against contextual demands. Durkheim's anomie is the founding sociological description. Social disorganization (Shaw and McKay 1942) is the modern technical term, used across criminology, urban sociology, and family sociology. Three lines of failure, three vocabularies, three intervention modalities.

An empire-human can develop either kind. Cancer is a genetic-line failure in the same person who can also develop a personality disorder, a neuronal-line failure. Both are real failures of the unit. They live at different lines. Civilizational collapse and institutional breakdown are the symbolic-line examples of disorganization.

Failures are also modeled at higher lines than the one they live in. Genetic-line failures are modeled in the neuronal line via interoception, the organism's internal sensing of cellular and tissue state. They are modeled in the symbolic line via medical knowledge, the cultural apparatus by which physicians categorize and intervene on disease. Neuronal-line failures are modeled in the symbolic line via psychological and psychiatric frameworks, the cultural apparatus by which clinicians categorize and intervene on disorder. The line of the modeling is not the line of the failure.

The personality disorders panel sits at Empire-Human in the diagram because the industrial era is when these neuronal-line failures became serious academic objects. Freud and the early psychoanalytic tradition framed neuroses as pragmatic failures, and that framing shaped how the disorders were measured and described. The panel records the industrial-era symbolic-line model of what neuronal-line failures look like. The failures themselves live in the brain of the affected individuals, not in the symbolic line that describes them.

Why personality disorders resist medication is then explained. It is not because the failures are non-biological. It is because they are constellational rather than disease-like. The brain is not broken the way a diseased cell is broken. It is configured in a way that misfits contextual demands. Therapy works because it shifts constellation through experience-driven learning, which is the neuronal line's native modification modality. Medication targets cellular and molecular machinery, the machinery of disease rather than the machinery of disorder.

### Where Personality Lives, Where Suffering Lives

Personality and felt suffering live in different places. Human personality disorder spans both. The failure of cultural participation is the disorder itself. The felt suffering of the disordered person is the sentience consequence. The cultural-goo failure is real, but the sentient/felt component is what makes it morally pressing rather than just descriptively interesting.

A superorganism is a meme-complex operating as symbolic-line fauna. It can carry personality-level dysfunction without sentient co-location. The empire-fauna is not itself sentient. The constituent-human-flora is. When the cybernetic structure fails, the humans suffer, not the superorganism. Moral status tracks the flora at the symbolic line, because the flora is where sentience lives.

The transition from pre-vertebrate to vertebrate-and-up may be where suffering proper becomes possible. Before motivational architecture exists at the unit level, there is no agent in the relevant sense to suffer the breakdown. Once the architecture exists, the agent can break down toward equilibrium and feel the breakdown. So suffering may be specifically post-vertebrate, with bilaterians having affective valence but not the agent-level felt structure. The moral implications are significant for invertebrate welfare debates.

*Epistemic status: the two-goo distinction is a framework theoretical commitment. The specific claim that suffering proper begins post-vertebrate is held with lower confidence and is flagged as exposed.*

---

# Part IV — The selection cycle

Parts I and III describe what the four functions are and how they compose. This Part describes
what they do in one turn. A line runs a cycle over four sites, and the four stages that move a
unit between them are the four functions at the scale of a single increment of inheritance.

Read this Part when a claim about how a line actually inherits needs its mechanism, and Part I
when the question is about deep time instead.

## Why the Lines Need Shared Slots

The framework claims that genes, brains, talk, and code run the same process. That claim is
empty unless the genetic line's X and the symbolic line's X are the same question asked twice.

Without that, every cross-line statement equivocates. The word carries one sense at one line and
a second sense at the next, and the sentence joining them says nothing.

What the framework needs is a fixed set of slots, filled at every line. Two entries are
counterparts when they fill the same slot. Counterparts are not the same thing, and they need
not resemble each other. Ask whether a repository is the counterpart of a gene pool or of a
genome, and the answer comes from which slot each one fills, not from which one it looks like. A
repository is a store holding many units, so it fills the seed bank, and its counterpart is the
gene pool. A working copy is one candidate drawn from what is available, so it fills the
understory, and its counterpart is the genome. Neither answer comes from what a repository
resembles.

Filling the same slot at two lines then produces a comparison rather than a pun. A slot that
fills thinly at one line becomes a prediction to check rather than a hole to apologize for.

The four stages and the four sites they run between are that set.

## The Cycle

A line runs a cycle over four sites. Each stage moves the unit from one site to the next, and
the fourth hands back to the first. The handoff closes and the state does not return. The seed
bank Retention writes into is not the seed bank Collection read from, and that difference is
what inheritance is.

| Stage | From | To | Function | Bias |
|---|---|---|---|---|
| Collection | seed bank | clearing | Modeler | potency |
| Sampling | clearing | understory | Reviser | novelty |
| Expression | understory | canopy | Effector | recency |
| Retention | canopy | seed bank | Regulator | familiarity |

**Collection** narrows a seed bank to what is available now. **Sampling** draws one candidate
from what is available and may mix it with others. **Expression** builds the drawn candidate
into something that competes. **Retention** writes what passed the gate back into the seed bank.

Selection is not a stage. Selection is the whole cycle, and it sits at the center.

The sites are named for places in a climbing plant's world. The stages are named for operations
any line performs. Units are collected from the seed bank, sampled from the clearing, built in
the understory, and kept or discarded in the canopy.

The stages run in order and nothing skips. Nothing is available that was not stored, nothing is
loaded that was not available, nothing is expressed that was not loaded, nothing is stored that
was not expressed. That chain is what makes this a cycle rather than four operations standing
next to each other.

## Why the Turn Does Not Return

Two different things make the cycle run one way, and keeping them apart matters.

Entropy makes it one-way. Every stage transition is paid for. Collection pays for constraint,
Sampling pays for generation, Expression pays in work and dissipation, and Retention pays for a
local inscription with a larger export. Paid-for transitions do not run backward for free. This
is the Second Law and not a claim particular to this framework.

Selection makes the one-way cumulative. Irreversibility on its own gives drift, and a process
can be irreversible and go nowhere. What makes each turn start from somewhere different in a
direction rather than merely somewhere else is that Retention is a gated write and not just a
write.

One family of claims goes further than this and the framework declines it. Prigogine, Schneider
and Kay, Lotka, England, and Kauffman each propose that distance from equilibrium drives systems
toward order, or toward faster dissipation, as a tendency of the physics itself. That puts an
aim in the ground floor. The framework takes the dissipative structure and leaves the drive:
entropy supplies the arrow and nothing else, and every aim is downstream of a selector. Deacon
is the anchor already in this document, since morphodynamic self-organization is where he starts
and his argument is that it is not sufficient. The decline is scoped to the universal-drive
version. Bioenergetic constraint at particular scales is a separate matter, and the framework
keeps Lane's version of it. The history of these proposals and their reception is under
"Thermodynamic bridges to selection theory" in Part I.

*Epistemic status: the Second Law and life as a dissipative structure are established, and the
framework already stands on both. Reading each stage transition as separately paid is a
framework commitment. The division of labor between entropy and selection is a framework
commitment. Declining the thermodynamic-imperative reading is a framework position rather than
a finding, and it rests on Deacon's argument that self-organization is not sufficient.*

## The Draw and the Mixing

Sampling does two things and they come apart. It draws one candidate from what is available,
and it may mix that candidate with others. The draw always happens. The mixing runs on a range
that reaches zero.

Every line has cases at zero. A seed can be produced without fertilization. A phrase can be
repeated exactly. A merge can apply cleanly with no conflict to resolve. A recall can come back
unblended with anything else.

None of these skips Sampling. In each, a candidate was drawn and the mixing contributed nothing,
which is the low end of a range rather than a missing stage. Reading a zero-variation case as a
skipped stage would break the ordering claim for no reason, because the ordering claim is about
which operations run and in what sequence, not about how much any one of them changed the unit.

*Epistemic status: apomixis in seed plants and conflict-free merges are established. Treating
these as the low end of one range rather than as bypasses is a framework commitment.*

## Why There Are Four

Two independent derivations fix the number, and they agree.

**The two bits.** Sight asks whether an operation's variation can be about itself. Binding asks
whether reflexive operation is bounded. Two independent bits give four corners, and the four
cybernetic functions sit at those corners (see "The Venn of Lines," Part I). Read the bits off
each stage and each lands on one corner.

Both bits are claims about what a stage can do rather than about any particular run of it. A
degenerate run does not move a corner.

Collection is sighted, because what gets gathered is filtered through a model of what counts.
It is unbounded, because there is no principled ceiling on what a seed bank can yield. That is
the Modeler corner.

Sampling is blind, because neither the draw nor the mixing consults what the build will need. It
is unbounded, because the mixing can be combinatorially open. That is the Reviser corner.

Expression is blind, because a build runs its instructions without reading outcomes. It is
bounded, because what one set of instructions can build is a finite region. That is the Effector
corner.

Retention is sighted, because the write is gated on the outcome. It is bounded, because it
writes against a stored reference. That is the Regulator corner.

**Absence recruits.** The functions run in a forced cycle, each recruited by the specific absence
in the one before it, and the cycle closes back to action (see "Why the Cycle Turns: Absence
Recruits," Part III). The stages inherit that order and that closure. The closure is in the
recruitment rather than in the state. Every function is recruited and none is left dangling,
which is a different claim from anything arriving back where it began. A cycle of three leaves
one recruitment unanswered. A cycle of five has no corner to stand on.

The two derivations are independent. The bits fix which corner each stage occupies. The
recruitment fixes the order they run in.

*Epistemic status: the two bits, the four corners, and the recruitment cycle are canon. The
reading of each stage's bits is framework inference. Each function assignment is independently
corroborated: the developing organism is named as the genetic Effector under "Line-Specific
Instantiation," Part I; the Regulator is defined as regulated control against stored references
under "The Four Functions," Part III. That fork, branch, and merge are the blind recombination
the Reviser runs on at the digital line is a framework commitment.*

## The Four Sites

The four sites are the four handoffs. A site is where one function passes to the next, so each
corresponds to an adjacent-pair region of the Venn. The site is where that region's tendency
operates rather than the tendency itself: the Anticipator operates in the seed bank, the Adapter
in the clearing, the Explorer in the understory, the Controller in the canopy.

Each site holds the unit in a different mode, and the process column names the change the
departing stage makes to it.

| Site | Handoff | Tendency | Process | Genetic | Neuronal | Symbolic | Digital |
|---|---|---|---|---|---|---|---|
| Seed bank | Regulator to Modeler | Anticipator | Stored to Available | chromosome | engram | text | file |
| Clearing | Modeler to Reviser | Adapter | Available to Loaded | standing variation | live operants | live memes | resolved dependencies |
| Understory | Reviser to Effector | Explorer | Loaded to Expressed | zygotic genome | motor plan | phonetic plan | working copy |
| Canopy | Effector to Regulator | Controller | Expressed to Stored | organism | behavior | utterance | process |

Canon's recruitment argument reads correctly at each site. A fixed reference cannot look ahead,
and the seed bank is what Collection reaches forward from. A model fitted to the past goes
stale, and the clearing is what Sampling refreshes. A rewritten model changes nothing until
something acts on it, and the understory is where it is loaded into something that can act. An open
action cannot see its own result, and the canopy is where an outcome becomes visible.

The process column is the handoff column translated. Each mode is the output of one function's
stage: available from Collection from the Modeler, loaded from Sampling from the Reviser,
expressed from Expression from the Effector, stored from Retention from the Regulator.
Substitute and the two columns agree row for row. That agreement is a test the mode words can
fail, and it is why they are these four words.

Only the per-line columns carry information. Site, handoff, tendency, and process are one fact
in four renderings.

The expressed row needs one note, because two of its cells are not built the way the other two
are. An artifact is the product of an expression and an output is the product of a process, both
one level past the thing that ran. The genetic and neuronal cells name the unit running rather
than what the running throws off, so the symbolic and digital cells name the utterance and the
process.

*Epistemic status: the four adjacent-pair regions and their recruitment arguments are canon.
The identification of the sites with those regions, and of a site as where a tendency operates,
is a framework proposal. The stored row is canon. The available and loaded rows are new.
Standing variation, working copy, and resolved dependencies are field-native. Live operants
restates the canonical statement that many operants are always live and only some win the
workspace. Motor plan and phonetic plan follow the established production sequence. Live memes
is the weakest cell in the table.*

## Selection at the Center

Selection is not a stage. Selection is the whole cycle.

In a line's own Venn the center is the breakthrough, the synthesis that requires all four
functions at once. The four stages are those four functions. So the synthesis that requires all
four stages is the cycle itself, and that is what selection names. The center of a Venn is the
region where all four attributes hold, not a fifth thing standing beside them.

There is a mechanical reason as well as a geometric one, and it is the stronger of the two.
Selection is not locatable at one stage because all four stages discard. If a single stage owned
the discarding, the other three would be plumbing and the center would be decorative. Four
narrowings composing is what the center is, and the next section sets out what each one throws
away.

That a line is selection-mediated inheritance rather than inheritance with selection added at
one point is argued at the scale of the lines under "The Venn of Lines," Part I. It holds the
same way at the scale of the stages. Gathering, drawing, building, and keeping are each
necessary and none is sufficient, and the four running as one cycle is what selection is.

The center defines the cycle and it unites the cycle. It defines it because a cycle whose
handoffs do not chain this way is not a line. It unites it because no stage can be understood
without the three it hands to.

A center is not a fifth thing, and the overlap of four is not a fifth. This is why scoring
needs no station of its own. Scoring is what a sighted, gated write does.

## What Each Stage Discards

Every stage narrows, and narrowing leaves a residue. The figure below says each narrowing is
unaimed. What it does not say is what becomes of what was narrowed away.

The residue is not one undifferentiated pile. Each stage throws away a different kind of thing,
and the formalism its function works names which kind. Collection discards candidates the
constraint excluded, which is Shannon. Sampling discards everything generable and not generated,
which is Kolmogorov. Expression discards failed builds and heat, which is Boltzmann, and it is
the only stage where the residue is literally thermodynamic. Retention discards what failed the
gate against a stored reference, which is Kullback-Leibler.

These are the payments under "Why the Turn Does Not Return," seen from the other side. That
section says every stage transition is paid for. This one says every stage throws away a
different kind of thing. They are one fact: what a stage pays is what it discards, counted in
the formalism its function works. The canopy holds a finite quantity of what the line competes
for, more arrives than it has to give, and a claim the budget does not meet is the residue.
Payment and discard are one event named twice.

| Stage | Genetic | Neuronal | Symbolic | Digital |
|---|---|---|---|---|
| Collection | alleles absent from the deme; seed that never breaks dormancy | signal that never becomes perceptible | culture available and not acquired | repo contents never pulled in |
| Sampling | gametes and zygotes never formed | operants live and never retrieved | lexical competitors active and losing | merges never attempted |
| Expression | developmental failure; dieback | aborted movement; pruning | disfluency, false start, self-repair | broken builds |
| Retention | the entire soma, at Weismann's barrier | performance that never consolidates | what is said and not passed on | work never committed |

The understory divides two kinds of residue. Before it, candidates are unbounded and merely possible,
so what is lost is possibility foregone. In the understory a candidate binds into an actual thing, so
from there on what is lost is destruction. The dividing line is where binding flips in the
two-bit square, which means it falls out of the derivation rather than being observed.

The discarding is the operation and not a shortfall in it. A Collection that discarded nothing
would pass the whole seed bank forward and narrow nothing, and a Retention that kept everything
would not be a gate. What can be compared across stages and across lines is the ratio, which
differs by orders of magnitude and is measurable.

The figure carries this without strain. A tangle is mostly senesced stem with live growth on
top, and the canopy is reached over everything that did not reach it.

*Epistemic status: the four discard classes are a framework commitment, and the identity of a
stage's payment with its discard is a second one. The per-line cells are framework inference
rather than a survey. Weismann's barrier is established. The
developmental-failure and gamete-loss cells carry published rates that are not cited here and
should be checked before any number is given. The division of residue at the understory follows from
the two bits.*

## Decay at the Sites

Every stage transition is paid for, and every stage discards. That accounting covers the moves
and not the waiting. A site holds its contents between visits, and holding is not free. An item
can sit through many turns of the cycle before the cycle reaches it again, and what it is worth
when it is reached is not what it was worth when it was written.

This is not a third class of residue. The two classes divide at the understory, and the division
falls out of the two bits rather than being observed. Both are produced at the moment a stage
narrows: something offered and not taken, or something built and then destroyed. What decays at
a site is a retained item, one that no stage discarded, losing ground while it is held.
Different event, different line in the ledger.

Two things drive it. An item is short only relative to the context that makes it short, and the
context disperses even when the item does not, so the cost of reconstructing what the item meant
rises while its contents stay exact. This is the conditional complexity entered under "Zurek's
bound" in Part I, read against a receding condition rather than a fixed one. And the site keeps
changing around the item, because Retention writes every turn, so the store that will be
narrowed is never the store the item was written into.

Call the observable salience decay: the item's odds of being picked at Collection fall while its
contents stay intact. Collection weights potency, and an item losing salience is an item losing
at Collection. An archive can go dark while its medium is perfectly preserved.

Salience decay is a rate and it can run negative. A recovered index, a released corpus, or a
returning reader lowers the reconstruction cost, and the item's odds rise again. Rediscovery is
the same quantity running the other way rather than an exception to it.

| Line | An item held and losing salience |
|---|---|
| Genetic | the sequence is intact and the regulatory context that once expressed it is gone |
| Neuronal | the trace is intact and no cue reaches it |
| Symbolic | the text is preserved and the readers who could read it have dispersed |
| Digital | the ticket is filed and never worked; the file is kept and the reader for its format is gone |

*Epistemic status: retrieval failure without loss of the trace is established, on cue-dependent
forgetting after Tulving and Pearlstone. The conditional-complexity result is established and
already entered in Part I. Treating decay at a site as a separate accounting line from stage
residue is a framework commitment, and so is naming Collection's bias as the quantity that
decays. The per-line cells are framework inference rather than a survey. Rates are unmeasured
here, including any claim that high-throughput environments accelerate the decay, and should be
checked before a number is given.*

## Selection Is an Event

Selection happens once per event, and the event is small. Differential reproduction happens at
every birth and every death. Attention happens every time a body performs an action.
Conversation happens every time a band shares information. Execution happens every time a
program runs.

A criterion is therefore a property of the individual competitor at the moment of the event. It
is not a statistic over a population. A trend across many events can be measured, and measuring
one is useful, but the measurement is downstream of the criterion rather than identical with
it.

This is why every criterion below names a disposition of the competitor rather than an outcome
or an aggregate.

## The Lines

| Line | Unit | Selector | Scarce resource |
|---|---|---|---|
| Genetic | gene | Natural Selection | a slot against carrying capacity |
| Neuronal | neme | Attention | one action |
| Symbolic | meme | Conversation | one turn |
| Digital | program | Execution | one invocation |

The selector is each line's founding-cell breakthrough. The scarce resource is the quantized
thing the canopy has one of, so one relation generates every row rather than needing an
argument per line.

*Epistemic status: the units are canon. The selectors are owned by the per-line label libraries
and each entry matches its library. The scarce-resource relation follows from the canonical
statement that selection bites only where a limited resource forces competition, and that in
the genetic case that resource is finite carrying capacity.*

## The Operations

| Line | Collection | Sampling | Expression | Retention |
|---|---|---|---|---|
| Genetic | gene flow in a deme / presence | segregation into gametes / heritability | development in morphospace / accessibility | germline transmission / reproducibility |
| Neuronal | perception in umwelt / perceptibility | retrieval from the repertoire / retrieval strength | performance in the motor repertoire / performability | consolidation / associability |
| Symbolic | acquisition from culture / learnability | lexical selection / lexical access | articulation in the vocal tract / pronounceability | re-transmission / grammaticality |
| Digital | dependency resolution / resolvability | merge in the working tree / reachability | the build in a type system / compilation | the commit / correctness |

Process before the slash, criterion after.

A process names an operation and the space it runs in, because neither half specifies it alone.
Development is not morphospace and morphospace is not a process. The space is the domain the
criterion is defined over, not the subset the criterion picks out.

Each stage asks one question about the unit in front of it, and the four questions are the four
criteria generalized.

- Collection: is it available
- Sampling: can it be loaded
- Expression: can it be built
- Retention: does it conform

Grammaticality and correctness are the same question in two media.

A merge does not consult whether the result will build. That is the digital rendering of blind
recombination, and it is why merge conflicts and broken builds exist. The failure surfaces one
stage later, at compilation.

The genetic Collection cell reads thin, and that is expected rather than a defect. The genetic
line is the Effector line, so its Modeler-stage entry is the one the Venn of Lines predicts will
be weakest.

*Epistemic status: accessibility is established in the morphospace literature. Perceptibility
follows from the umwelt account. Pronounceability is established in phonology. Learnability is
established in the iterated-learning literature (Kirby). The storage-versus-retrieval-strength
distinction is established (Bjork). Lexical selection and lexical access are established in the
production literature (Levelt). Reachability and resolvability are field-native. Performability
is framework-coined and is pronounceability generalized past the mouth. Reading the four
questions as one question per stage is a framework commitment.*

## The Break Between Expression and Retention

Being expressed and being kept are different events, separated in time, and the boundary
between them has its own gate. Four lines make the break unmistakable.

At the genetic line an organism can compete well on somatic excellence and have none of it
written down. Only the germline is transmitted, which is Weismann's barrier. That the gate is a
biased filter rather than a formality shows in meiotic drive and segregation distortion, where
what gets into the germline is not a fair sample of what the organism carries.

At the neuronal line a behavior can be performed, be rewarded, and still fail to be retained,
because consolidation is separately gated. The separation is measured in hours, and
consolidation runs offline during sleep.

At the symbolic line an utterance can be understood and never repeated. Vosoughi, Roy, and Aral
tracked roughly 126,000 stories on Twitter from 2006 to 2017 and found that falsehood diffused
farther, faster, deeper, and more broadly than the truth across every category they examined.
What is spoken and what is passed on are not the same population.

At the digital line a defect report can be correct, survive every analysis that produced it,
and be recorded as a false positive because the engineer reading it did not understand it. The
report ran and was not kept, and nothing about its correctness was at issue in the refusal.

Four breaks at one boundary, and the boundary is a stage edge rather than a seam inside a
stage.

*Epistemic status: Weismann's barrier and the distinction between somatic and germline
variation are established, as are meiotic drive and segregation distortion. The neuronal break
is established and measured. The symbolic finding is Vosoughi, Roy, and Aral, Science 359
(2018), 1146 to 1151. The digital case is an illustration rather than evidence and carries no
citation.*

## What the Liana Figure Carries

The four sites are one figure. A liana runs a cycle over a seed bank, a clearing, an understory, and
a canopy, and no one tends it.

Transfers: a store of dormant units that outlasts any individual; an opening that makes some of
them viable now; a base that assembles and pushes; a canopy with a finite quantity of light in
it, arriving one unit at a time, into which more is pushed than it has to give. Nothing awards
the light. The budget runs out. Each narrowing is unaimed. The animal that carries a unit back
to the store is not selecting for the plant.

Does not transfer: cultivation. Nobody sows the seed bank, opens the clearing, or decides which
stems are kept. Nor does the figure carry any weight of its own. The four stages are fixed twice
over inside the framework, once by the sight and binding bits and once by absence-recruitment,
and both derivations stand without the plant.

One thing the figure carries is not a site. A standing stem spends to keep standing. The bill
scales with how much is standing. Stop paying and it comes down. That is Part V's maintenance
tax with a body under it, and reaching the canopy exempts nothing. A stem that arrived still
pays every day it stays.

*Epistemic status: the soil seed bank is an established ecological object. Liana proliferation
in treefall clearings and liana competition for canopy light are established. Animal dispersal
of liana seed is established for many taxa and is not universal. Identifying these four with
the four sites is a framework proposal. The liana is the theory's figure and is a different
object from the book's plant, which carries its own senses.*

## The Climb, the Trellis, and the Host

The climb has one support and one grid, and they do different jobs.

**The trellis is the grid.** It bears nothing. It is made, and it is ours: the framework's own
architecture, the functions, motivations, capacities, and breakthroughs laid out line by line
and cell by cell across the twelve. A unit moves up a grid the way a reader moves down an index.
That a framework is a made object is correct and says nothing about what holds the plant up.

**The host is prior structure.** It is wild, and it is not ours. A liana climbs whatever got
there first: the trees already standing, and the other lianas already in the tangle. Nobody put
any of it there for this plant's benefit.

The host also paid for it. A climber reaches the light without building what holds it there,
and Darwin gave that saving as his reason so many unrelated lineages took up climbing. The
saving is real and the cost does not vanish. It sits with the host, who is also the party the
climber then shades. This is Part V's displaced tax carried by an instance rather than an
example.

The host fills a slot at every line. At the genetic line it is the developmental architecture a
new variant has to build inside. At the neuronal line it is the repertoire already learned, out
of which a new behavior is assembled. At the symbolic line it is the conventions and
institutions already in place, which a new form has to travel on. At the digital line it is the
existing codebase and the dependencies it already resolves against.

The climb is the cycle running, and it does two things at once.

The climb supplies direction. Upward displacement is oriented whatever path it takes, and that
orientation is all the figure needs from it. Irreversibility is a separate claim resting on a
separate ground, set out under "Why the Turn Does Not Return."

Catching on the host supplies accumulation. A liana's reach is set by what is already standing,
and no liana reaches the canopy without something to climb. Each turn starts from what earlier
turns left, and differently. For a liana this is the growth form's defining constraint rather
than an observation about it.

A regular spiral would give the first and not the second. Fixed pitch and fixed radius make
every turn the same shape, so no turn depends on what any earlier turn left standing. That is a
shape that repeats without a history, and inheritance is a history.

*Epistemic status: lianas are structural parasites that depend on host support to reach the
canopy, and their abundance in treefall clearings is established. Darwin made the cost argument
himself, in the climbing-plants work of 1865 and its 1875 book edition, not in the later
movement book. The split between a made trellis and a wild host is a framework commitment. The four host renderings are framework
inference and have not been checked against the per-line label libraries. The host is a
different object from the panels under "The Seam," Part I: panels are invariant parts held inside a
unit, and the host is external structure the unit builds on.*

## Two-Sided Pressure at the Symbolic Line

Pronounceability names the speaker's half of a pressure that has two halves. If ease of
articulation ran unopposed, every form would erode toward a single reduced vowel. What stops
that is perceptual distinctiveness, which is the standard account of why phoneme inventories
are shaped the way they are. Speaker effort pulls forms toward simplification. Hearer recovery
pushes them back apart. Surviving forms sit in the trade-off.

The two halves sit at two stages. Pronounceability gates what Expression can build.
Grammaticality gates what Retention will keep.

*Epistemic status: the erosion pressure is established (the shortening of frequent forms,
lenition, and the convergence of transmission chains on more learnable systems). Adaptive
dispersion as the counter-pressure is established. Splitting the two halves across two stages
is a framework commitment.*

## Adjacent Vocabulary

The understory's digital rendering has field-native neighbors. Practitioners speak of a sandbox, and
of development environments as against production environments. Both name a space where a
candidate is assembled and exercised before it is allowed to compete for anything real.

Programs have syntax, and syntax errors are caught at compilation. Grammaticality at symbolic
Retention and compilation at digital Expression therefore sit close without sharing a slot. One
gates the write and the other gates the build.

Wordlikeness is gradient phonological well-formedness, measured as phonotactic probability and
neighborhood density. It is the standard instrument for measuring how sayable a form is, which
makes it an instrument rather than a construct.

---

# Part V — Maintenance, Failure, and the Ethics of the Tax

## The Visible Tax

Entropy is the ground. Order is the expensive, surprising thing; decay is the free default. Poverty needs no explanation and wealth does, because things fall apart when left alone. This is established physics the framework stands on: life holds its own entropy low by importing concentrated energy and exporting dispersed waste. Schrödinger put the question in 1944 and Prigogine's dissipative structure is the standing term for the answer, with the limit entered under "Why the Turn Does Not Return": the framework takes the structure and not the drive. Every unit the framework describes persists only by doing work against this ground. The floor has an informational face as well as a thermodynamic one, set out under "Landauer's floor" in Part I: every discard is paid in heat at the bottom, whatever denomination it is counted in.

From the floor follows a conservation law. You cannot remove the cost of a thing coming apart. You can only move it. The cost moves forward in time, or sideways onto another payer, but it does not vanish. A slick sealed unit and a serviceable one do not differ in whether the bill is paid; they differ in when it comes due and who is standing there when it does.

A second conservation law runs the other way. The first prices a thing coming apart. The second prices a thing being put together: any local increase in order exports disorder, and no arrangement of the work removes the export. These are two bills and not one bill stated twice. Keeping them apart is what keeps the audit honest, because a unit can be scrupulous about the cost of its own decay and silent about what its assembly cost everything around it.

Maintenance is the work that funds the bill. The Regulator is the function that does that work: it holds a reference and drives the unit back toward it against perturbation. Negative feedback is its charter, and homeostasis is its founding case, Wiener's loop and Cannon's regulated body. To maintain is to keep paying the entropy tax so the unit stays far from equilibrium one more cycle. That payment is the ratchet's third part, set out in Part I. A ratchet needs undirected variation, a rectifier, and free energy spent to reset it each turn, and without the third it is a perpetual motion machine. Maintenance is the reset. Which is why maintenance and selection are not one move at two speeds: the reset is what lets the loop run again, and selection is the loop.

The keystone is an audit. A maintenance architecture is clean when its tax is visible to whoever pays it, and it is a kludge when the tax is hidden. Hiding takes two forms, and they are the two directions the conservation law allows. The tax can be deferred, hidden in time from the future payer. Or it can be displaced, hidden from a payer who was never in the room. Call the whole apparatus the visible tax: the physics is that the tax is always levied, the audit is whether it is visible, and the ethics is that concealing it from its payer is the core move of every maintenance failure that is not innocent.

*Epistemic status: the entropy floor and the Regulator's maintenance role are canon. The conservation law and the visible-tax audit are framework theoretical commitments, assembled from the maintenance-philosophy tradition. Identifying maintenance with the ratchet's reset is a further commitment, following from the ratchet mapping in Part I. The ethical reading is stated here as framework content, because the framework's failure taxonomy is already a moral object.*

## The Two Bills and Their Payers

Maintenance is one of two bills, and the other one is not paid by the unit that owes it. Selection buys every gain in fit with a much larger volume of discarded variants, and the discarding is the mechanism rather than waste in it. Part IV sets out what each stage throws away. What belongs here is that the residue is not incidental to the process and cannot be reduced without stopping it: natural selection's residue is death, attention's is everything that stayed live and never won, conversation's is everything thought and not said. A framework whose failure taxonomy is already a moral object does not get to describe its own engine and leave that out.

The two bills differ in what they buy, in how long the purchase lasts, and in who pays. Maintenance holds one unit far from equilibrium across a lifetime, and the unit pays it in effort, cycle by cycle. Selection holds a lineage far from equilibrium across lifetimes, and the alternates pay it, once each. Neither term is the other one slowed down, because the reset and the loop are different parts of the ratchet, as set out under "The Visible Tax" above. What the two share is the payer question, and it is the question the audit asks: whether whoever carries the cost can see it.

*Epistemic status: the residue of selection and its irreducibility are canon, carried in Part IV. Reading maintenance and selection as two bills with different terms and different payers is a framework theoretical commitment. The moral weight placed on naming the second bill follows from the framework's failure taxonomy already being a moral object.*

## When the Tax Comes Due

Maintenance failure is the tax collected. The framework already sorts it by line, and each line's failure is a mode of the Regulator's job not getting done.

Disease is genetic-line maintenance failure: cells and tissues that no longer hold homeostasis. Cancer is maintenance stopping, a lineage of cells that defects from the body's held reference, and much of that defection is the epigenetic homeostat failing, cells losing their maintained state and rolling back up the landscape toward a less-differentiated one. The tax comes due in the body.

Disorder is neuronal-line maintenance failure: a unit that no longer regulates its life against what its situation demands. Here the tax is paid in suffering, and the framework does not flinch from that. The felt suffering of the disordered unit is the tax made conscious, and its moral weight is why disorder matters differently than a spec sheet does. Whether that suffering is visible to others, or dismissed as weakness, is the politics of the tax at the scale of one life.

Disorganization is symbolic-line maintenance failure: institutions and norms that no longer regulate collective life. Durkheim's anomie is the founding description, and social disorganization is the modern term. Its characteristic form is the unowned seam, the thin, cheap-to-change switch that maintenance ordinarily keeps assigned and watched. An institution runs a fast layer and a slow one, a quarterly clock and a mission measured in decades, and if no load-bearing seam is placed between them the fast clock silently re-cuts the slow kernel one defensible decision at a time, until the thing the institution was built to do is gone. Nobody chooses this, which is what makes it maintenance failing rather than a crime: the granularity was never owned. Ries calls it corruption as drift, and his Long-Term Stock Exchange is the attempted repair, a seam installed between the fast financial layer and the slow mission layer so the fast one can fail without deforming the slow one.

The moral edge is sharpest here, and it is where the visible tax becomes a political claim and not only a physical one. An institution's fauna is not sentient; the constituent people whose lives it runs on are (see "Where Personality Lives, Where Suffering Lives" above). So the institution is the one kind of organism whose deciders and whose payers are different beings, the one kind that can hide the tax from those who pay it. When it defers its own maintenance the deferred bill comes due on the flora, on people who were not in the room when the deferral was chosen, and the fauna that chose it cannot itself feel the cost. Crumbling infrastructure and unfunded obligations are Crowhurst's failure at the scale of a civilization. This is the displaced tax: the cost moved onto a payer who could not see it coming and did not get a vote.

The maintenance-blind unit fails by regime mismatch. A unit with the Regulator root switched off pursues without holding any reference, and it survives only in a world calm enough that no reference needed defending. The Pursuer is that unit, the Regulator-absent capacity, gate-slipping with no held reference. The valence is set by the weather, not by the capacity: in an expansive regime the same act is alloparenting, and in a storm it is what Donald Crowhurst did. Crowhurst faked a round-the-world voyage rather than face the risk of sailing it, and his failure is not a third mode of maintenance. He is maintenance switched off while dressed as a plan, and he loses in every weather, because he bet there was no floor when the floor is entropy itself. His mirror is the unit with the Reviser root off, which defends its reference faithfully and dies when the world shifts, the way an entrenched structure everything was built upon cannot be re-cut without catastrophe.

*Epistemic status: the line-failure taxonomy is canon. The reading of each failure as a form of the visible tax, and the moral weight placed on suffering and on the displaced institutional bill, are framework theoretical commitments.*

## The Art of Maintenance

The counter-image to failure is the maintainer's grace. Maintenance done well is not only a cost paid. It is a source of meaning, a competence and an attention to the maintained thing that returns something to the one who pays. Crowhurst resents maintenance, not from laziness but because a model that deleted the storm reports that the tax is not owed. The maintainer is the unit whose model keeps the floor in view, and who finds in the paying of the tax a relation to the maintained thing Crowhurst never has.

What the maintainer does is invisible exactly when it works. A maintained thing shows no trace of the upkeep that holds it: the healthy body, the machine that runs, the institution that functions all look effortless, and the effort is hidden by its own success. So the one who pays the maintenance tax is the least likely to be credited for it, which is the displaced tax seen from the maintainer's side, the flora who carry the fauna now looked at directly. Here the craft and the ethics are a single fact. The attention the maintainer spends on the maintained thing is a real competence, and it is spent where no one is looking, on work noticed only in its absence. His model does not only delete the storm; it deletes the one who keeps the storm out.

The same invisibility falls on the maintained thing, and that case is harsher because it arrives looking like a verdict. An item loses salience while its contents stay exact, and Part IV gives the mechanism under "Decay at the Sites." What the store stops picking is then not what failed but what stopped being visible, and nothing in the picking tells the two apart. Pointed at objects this is an archive going quiet. Pointed at people it is a population declared surplus, and the declaration will present itself as a finding about them rather than as a fact about the store's reach.

Harari's forecast is the version of this a reader can stand inside. He projects a large class of people rendered not merely unemployed but unemployable, surplus to an economy with no remaining use for what they can do, and he names the condition irrelevance rather than poverty because the two are different complaints. The framework does not have to accept the forecast to say what would make it land the way he describes. Collection weights potency, and potency is not merit. A person's competence can stay exact while the context that made it potent disperses, and the store will stop picking them without registering that anything was lost. This is why the reader is a plausible payer here rather than a spectator: the mechanism does not read merit, so being good at the thing is no defense against the thing going quiet. And the bill is displaced in the sense already given, since whoever gains from the store's re-sorting is not the one who carries it and was not in the room when it happened.

This is where maintenance meets beauty, and the meeting is not sentimental. Nature does have one literal aesthetic, and it is not design but choice: the mate preference that shapes form for its own sake, the peacock's tail, the bower, the flower that is beautiful because it evolved to be chosen. Choice does not overturn the primacy of upkeep, though. It advertises it. Zahavi's handicap says why. Ornament is expensive and useless, and that is the point, because only a unit whose maintenance is so well handled that it can afford to waste resources can grow one. Beauty is discretionary spending after the tax is paid. So the display aesthetic is not a rival to the maintenance one; it is maintenance's visible dividend, the margin a well-kept thing can afford to show. The beautiful thing is the thing whose upkeep is secure, and ornament is the visible tax read from the far side, not the cost of persisting but the surplus left once persisting is no longer in doubt.

That is beauty as nature makes it, in the surplus, and it is given rather than chosen. There is a further aesthetic that needs nothing from nature, and it is the one this framework keeps. It finds the beauty not in the margin left after upkeep but in the upkeep itself, in the wear and in the repair. Wabi-sabi is its name in one tradition, an aesthetics of the maintained and the worn. Kintsugi is its clearest object: a broken bowl mended with gold along the break, so the repair is not concealed but made the most beautiful part of the thing. That is good seams make good neighbors turned into a bowl, the seam gilded rather than hidden. Functional beauty is the philosophy under it, the account from Parsons and Carlson on which a thing's fitness to its function is a genuine source of its beauty, not a substitute for beauty. And the move that makes it available is small and entirely a choice: you do not need nature to hold this aesthetic for you, you need only notice that maintenance is the load-bearing pattern of everything that persists, and adopt the stance that finds it beautiful. The surplus is a beauty a peacock cannot help; the mend is a beauty a maintainer decides to see.

*Forward pointer: this last stance, that the mend is where the beauty and the meaning live, is the seed of the planned second book, on disorder. The framework carries the claim; the book's telling of it is downstream.*

*Epistemic status: the maintainer's grace draws on Brand and Pirsig. Sexual selection and the handicap principle are established biology; reading nature's display aesthetic as the advertisement of maintenance surplus, and beauty as the dividend of upkeep, is a framework theoretical commitment. Wabi-sabi and kintsugi are established aesthetic traditions, and functional beauty is an established position in philosophy (Parsons and Carlson). The larger stance, that maintenance is nature's load-bearing pattern and that finding the mend beautiful is a chosen posture rather than a claim about nature's own experience, is a framework position, not a theorem. Salience decay and its mechanism are carried in Part IV. Harari's projection of a large unemployable class is a forecast rather than a finding, and the framework cites it as the reader-facing case of the mechanism without endorsing it. Reading that case as displaced tax is a framework theoretical commitment.*
