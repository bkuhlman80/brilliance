# What It Costs to Be Somebody

# Night One

---

## Personality as Biographical Signature
What makes trait talk apply to bacteria but not to thermostats?
Both have the cybernetic components.  A thermostat has a sensor (the thermometer), a comparator (the rule "above/below setpoint"), an effector (the heater), and a goal (the setpoint).  A bacterium has the same four functions, instantiated in different machinery.  By the components alone, both should support trait description.  Neither does for thermostats.  Bacteria do.  Bacteriologists routinely describe strains as bold, sluggish, sociable, cooperative, or exploitative, and the descriptions earn their keep.
The difference is inheritance.
Trait adjectives are distributional summaries.  Saying a system is "bold" is a probabilistic claim about how it tends to weight action under uncertainty across a class of situations.  A distributional summary presupposes multiple situations where the parameter expresses, probabilistic rather than deterministic response, consistency in the pattern, and a reference distribution against which "tends to" is meaningful.  The reference distribution is what makes the trait reading possible.
Inheritance creates the reference distribution.  It propagates parameters across instances so variation persists; subjects parameter variation to selection so the distribution becomes structured rather than drifting to noise; preserves successful constellations so they appear repeatedly in the lineage; and generates novelty so the distribution stays alive.  Without inheritance, the lineage has no parameter distribution; without a parameter distribution, individual readings have nothing to be a position within.
A thermostat lineage does not exist.  There is no thermostat-to-thermostat parameter flow contingent on which thermostats functioned well.  The variation across thermostats reflects designer choice, not selection.  So the cybernetic loop is present, but the biographical structure is not.  Trait adjectives describe systems with histories; thermostats do not have biographies.
The biographical signature is what every line has evolved a genre to compress.  Humans get obituaries.  Bacterial strains get strain reports.  Codebases get postmortems.  Civilizations get historiographies.  Trained models get model cards.  Agents get deployment retrospectives.  Different names, same form: a small set of characterizing adjectives summarizing how the unit tended across the distribution of situations it occupied.  A personality assessment of a living unit is a prospective bet on which adjectives the eventual retrospective compression will land on.  Things without biographies get event descriptions instead.  Hurricanes get meteorological summaries and thermostats get spec sheets, the genre that fits what they actually are.
This is why I set the scope criterion where I did.  It applies to inheritance-bearing units, systems that perpetuate themselves through environmental coupling, transmitting pattern across time.  The criterion excludes thermostats, hurricanes, and rocks not on intuitive grounds but on principled ones: they do not transmit pattern to successors, so there is no lineage for selection to write onto, so there is no biographical signature for trait adjectives to summarize.
The same argument extends all of this into lines that are not biological.  Code lineages exist (forks, version control, kernel inheritance).  Trained-model lineages exist (base weights, fine-tuning chains).  Agent constellations would propagate the same way, by inherited goal structures and inherited instruments.  The line is engineered at origin, but parameter flow contingent on what works is present.  So personality applies, not by metaphorical extension from biological cases, but by the same structural argument that licensed it for bacteria.
*Personality is the biographical signature of a cybernetic loop subject to inheritance.* Wherever both conditions hold, traits apply.  Where either fails, they do not.

---

## Vocabulary
Five terms the rest of the book leans on are defined here, before the architecture that uses them.

### What the Ratchet Word Commits To
A Brownian ratchet has three parts: undirected variation, a rectifier that lets motion through one way and blocks the other, and free energy spent to reset the mechanism each cycle.  Feynman's ratchet-and-pawl exists to show the first two are not enough.  At thermal equilibrium the pawl gives no net motion, and without the paid reset the device is a perpetual motion machine.  The framework's use of the word means all three.
The three parts sit in three different places.  The Reviser is the variation.  The gate at Retention is the rectifier.  The maintenance tax is the reset.  The ratchet is therefore the whole loop and not any one function in it.

### Each Line Ratchets a Different Kind of Slack
*A note on the word.* *Slack* is my term for the stuff each line works — the medium each inheritance line acts on and ratchets.
The cross-line architecture has the same cybernetic decomposition (Effector, Regulator, Modeler, Reviser) at every line, instantiated in line-specific machinery.  The line-specific machinery differs because each line is a different kind of slack-ratchet.  Same architectural function, different slack being ratcheted.
The three kinds of slack:
- **Genetic line ratchets Boltzmann slack.** Life maintains itself far from physical equilibrium.  Cells, organisms, and lineages are constellations that ratchet thermodynamic disorder by importing low-entropy energy and exporting high-entropy waste.  Selection preserves the constellations that ratchet best.
- **Neuronal line ratchets Friston slack.** A brain-bearing unit holds itself inside a narrow band of expected states by keeping a model of the world and closing the gap between model and world from both ends.  Variational free energy is the formalism that counts that gap.  What the description tracks is a unit that stays out of improbable states, and selection preserves the units whose gap runs narrower.  Affective and motivational structure (sensorimotor reentrant signaling shaped into trait-level dispositional architecture, empirically documented from vertebrates up) is what running Friston slack looks like at the unit level.  This row records the line-level commitment.
- **Symbolic line ratchets Shannon slack.** Symbols are constraints on signal-space: every lexicon, grammar, convention, and pragmatic norm shrinks the space of legitimate messages, and cultural transmission keeps the constraints that coordinate groups.  Empires ratchet the random message-space into shared symbolic systems.
Each line does the same Darwin-level slack reduction (selection-mediated pattern preservation) at the line level, but on a different kind of slack at the unit level.  This explains why the lines are genuinely different despite sharing cybernetic architecture.  Same cybernetic structure, different slack, different mechanisms, different timescales.
*the genetic-line Boltzmann-slack claim follows from Deacon's Shannon-Boltzmann-Darwin framework (2007).  The neuronal-line Friston-slack claim sits on the variational-free-energy formalism (established as formalism; the line-slack reading is a framework commitment); the behavioral-syndrome literature (Sih, Bell & Johnson 2004; Jaap Koolhaas) supplies the empirical-trait surface.  The symbolic-line Shannon-slack claim is a framework-native application of the same principle.*

### Flora and Fauna Across Lines
Each line contains two ecological roles.  Flora are sessile, persistent, and environment-shaping.  They are slow on the line's timescale.  They generate the environment that fauna consume.  Fauna are motile and predatory.  They are fast on the line's timescale.  They are behaviorally flexible relative to the flora they inhabit.
Humans are to culture as plants are to animals: we are flora.  The relationship is loopy, not simple.  Animals forage on plants, and plants coevolve with animals, which is to say plants shape animals in turn.  Memes forage on human brains, and personalities coevolve with culture, which is to say personalities shape culture in turn.
The roles populate every line:

| Line | Flora | Fauna |
|--------|-------|-------|
| Genetic | Plants and their predecessors | Animals |
| Neuronal | Bodies as organism | Brains and nervous systems |
| Symbolic | Personalities | Memes and meme-complexes |

Animals do not replace plants.  Brains do not replace bodies.  Memes do not replace personalities.  The relationship is coevolutionary.  The new fauna develops alongside what becomes its new flora, and the two remain interdependent.
The symbolic line's flora is the constituent human's personality structure.  This is the trait-level structure that personality psychology measures.  The symbolic line's fauna is the full spectrum of memes, from small ideas to large meme-complexes.  Superorganisms are large meme-complexes operating as fauna.  A band as a whole, a settlement as a whole, a city as a whole, and an empire as a whole are all superorganisms.  They are not parallel units of personality to the constituent human.  They are the fauna that inhabits the human-flora personality.
A single human participates in three lines at once at three different ecological positions.  The human body is genetic-line flora.  The human brain is neuronal-line fauna.  The human personality is symbolic-line flora.  The three roles coexist in one organism.
Flora are not passive in any line.  Plants manipulate pollinators, shape soil chemistry, and structure ecosystems on long timescales.  Bodies grow brains, regulate metabolic resources, and determine the niches brains operate in.  Personalities generate the symbolic content memes feed on, every utterance and artifact and child raised.  The flora's mode of action runs longer and broader than the fauna's.  The fauna's mode of action runs faster and more locally focal than the flora's.  Both are active.

---

### What a Clade Is
A clade is a category of units sharing a cell's architectural signature.  Each cell name is shorthand for one: it picks out the representative form rather than a single named entity, and the clade it names contains internal diversity.

### The Four Sites, in Brief
A turn of inheritance moves the unit between four sites, each holding it in a different mode: the seed bank holds what is stored, the clearing what is available, the understory what is loaded and not yet acted on, and the canopy what has been expressed and is competing.  The four stages are the handoffs between them, and the full treatment is with the selection cycle.

---

# Night Two

## Evolution as Learning
Watson & Szathmáry (2016) demonstrates that evolutionary dynamics and learning dynamics are different instantiations of the same algorithmic principles.  Two formal equivalences carry the load:
(a) Bayesian updating is mathematically equivalent to soft selection on genotypes in asexual populations (Harper 2009; Shalizi 2009).
(b) The multiplicative weights update algorithm is mathematically equivalent to selection on individual alleles at linkage equilibrium in sexual populations (Chastain et al. 2013).
Both equivalences are conditional.  The Bayesian-asexual equivalence requires that the population be asexual, that genotypes cannot be decomposed into independently fit components.  The MWUA-sexual equivalence requires linkage equilibrium, absent epistasis.  The conditions matter; the equivalences are not unrestricted.
What the equivalences underwrite, in the form Watson states it: evolution and learning are not merely analogous processes but different instantiations of the same algorithmic principles.  Selection is computation; lineages compute over generations the way learning systems compute over training cycles.
The mechanism by which this computation accumulates is gene-regulatory architecture internalizing the correlation structure of selective environments, the way a neural net stores training-set statistics in its weights.  Watson et al.  (2014) demonstrated, in simulation, that evolved gene-regulatory networks form a distributed developmental memory of phenotypes selected in the past, spontaneously recreating these phenotypes as attractors of development, and generalizing to produce novel combinations of phenotypic modules fit for environments not previously selected for.
*the formal equivalences are stated by Watson & Szathmáry as established mathematical results, attributed to prior work.  The developmental-memory and generalization claims are demonstrated in simulation; the authors flag the extension to biological generality as an outstanding question.*

## Free Energy and Active Inference
The free energy principle gives a substrate-independent formulation: any system that maintains itself against entropy admits a description in which a quantity equivalent to free energy is at a minimum.  The formalism and its decomposition are set out below, with the other three denominations.
I am treating the free-energy principle as a substrate-independent principle that applies wherever a system maintains itself against entropy, compatible with cybernetic-inheritance at every level.  Active inference is the specific mammalian instantiation.  Other lines run other line-native machinery: ratcheting at protocell, state-dependent gating at prokaryote, associative learning at bilaterian, reinforcement learning at vertebrate, gossip-tracked social debt at band, code-tracked obligation at city.
The Regulator and Reviser are cross-level structural roles.  The machinery implementing them changes by level.
DeYoung's Cybernetic Big Five Theory is the strongest existing precedent for grounding the metatraits in cybernetic-architectural terms.  I inherit that apparatus and do not duplicate it.

### Friston's two values, and what the neuronal line adds
Expected free energy decomposes into two terms, and both are higher where expected free energy is lower.
**Pragmatic value** is the drive to reach preferred outcomes — to satisfy a setpoint, to reach a goal.  It is exploitation.
**Epistemic value** is the drive to reduce uncertainty about hidden states — expected information gain.  It is exploration.
Epistemic value has a structural precondition: a generative model with uncertainty that observations can lower.  Without a model, there is nothing to be curious about, and minimizing free energy collapses to the pragmatic term alone. 
The honest scope of the claim: behavior in both lines stays mostly pragmatic moment to moment, and exploration largely serves later exploitation.  What the neuronal line adds is not a majority of epistemic behavior but the *arrival* of epistemic value as a first-class, tunable driver — the explore-exploit balance becomes a dial, which is what the neuronal line's temperature and entropy-bonus settings tune.  The genetic line cannot carry that dial, because it has no model whose uncertainty the dial would trade against.
This maps onto the Venn below: the neuronal line is the Regulator line, and the pragmatic-plus-epistemic decomposition is the native structure of free-energy minimization.  The genetic line runs the pragmatic term; the neuronal line is where the epistemic term comes online.


# Night Three

## The four measures, and what each one counts
**Boltzmann entropy.** Boltzmann entropy is `S = k·ln W`. It counts the microstates `W` compatible with a macrostate.  It is the thermodynamic measure of how dispersed energy and matter are.  The Second Law says it tends to rise in an isolated system.  Life is a dissipative structure: it holds its own internal entropy low by importing concentrated energy and exporting dispersed waste.  This is what the Effector's work is counted in.
**Shannon entropy.** Shannon entropy is `H = -Σ pᵢ·log pᵢ`. It measures the average uncertainty of a source over a set of messages.  It is maximal when the messages are equally likely and falls as constraints make some messages more probable than others.  A code, a grammar, or a convention reduces it by shrinking the space of legitimate messages.  This is what the Modeler's work is counted in.
**Friston free energy.** A system that persists occupies a narrow set of expected states, which is to say the long-run entropy of its own state distribution is low.  The surprise that would measure this directly is intractable, so the formalism substitutes an upper bound on it: variational free energy, which takes the form *complexity minus accuracy*. The bound falls two ways, by perception updating the model and by action changing the world to match the model.  Stated this way the principle is a redescription and not a cause, which is Friston's own reading of it, and it is why the quantity carries no explanatory load here.  Selection does that work.  Friston free energy is an information quantity (a divergence, Shannon-family) cast in the form of a thermodynamic potential (Helmholtz-family).  Helmholtz free energy is `F = U − TS`, the energy available to do work at constant temperature; the name is his, and so is the older root of the idea, perception as unconscious inference.  This is what the Regulator's work is counted in.
**Kolmogorov complexity.** Kolmogorov complexity `K(x)` is the length of the shortest program that outputs `x` on a fixed universal machine.  It measures algorithmic information — how incompressible an object is, how much it takes to *generate* it.  It is high for random strings and low for regular ones, and it is uncomputable in general.  This is what the Reviser's work is counted in, and it is the digital slack below.
Darwin is not on this list.  Natural selection is a process rather than a measure of disorder, and it is what makes any of the four goos heritable and cumulative across agents.
**Reading the four onto the square.** The framework places its four functions with two bits, sight and binding, and it reads those bits off the lines and off the stages.  The same two questions can be put to the formalisms, under one rule: ask them of the unit whose slack it is, never of whoever is studying it.

| Formalism | Sight | Binding |
|---|---|---|
| Boltzmann | blind: microstates are about nothing, and the coarse-graining belongs to the observer rather than to the gas | bounded: a closed system's entropy has a maximum and is driven toward it |
| Friston | sighted: the only one of the four with the representation relation inside the formula | bounded: defined over a system that occupies a narrow set of expected states |
| Shannon | sighted: computed over a code, and a code is a standing-for relation | unbounded: a code can encode codes with no ceiling |
| Kolmogorov | blind: indifferent to whether the string is about anything | unbounded: uncomputable, and generation is combinatorially open |

Each lands on one corner and no corner takes two, so the assignment of a formalism to a function is derived rather than argued from resemblance.

### How the four measures relate to one another
**Denomination.** Each function's work is counted in one of these and not in the others.  There is no general rate of exchange across the four, which is what makes the lines lines rather than four settings of one dial.  Non-convertibility is an ordinary property of a unit of account and not a defect in one.
The relations that do exist are specific, and the shape they make is narrower than four free-floating quantities.  The table below is the full inventory of six pairs.  One carries an exact correspondence, and it holds only under an identification made from outside the unit.  One is a containment, since Friston free energy is a Shannon-family divergence.  One holds in the limit and not term by term.  Two carry a one-way lower bound and no price.  One carries nothing direct at all.  So the non-convertibility is read off the geometry rather than asserted against it.
The scope is accounting and not markets.  Denomination, payment, non-convertibility, and payer identity transfer.  Price discovery and market clearing do not: no mechanism finds a rate, no aggregate of events sets what anything is worth, and nothing awards what is competed for.  The same refusal holds from the selection side, where a criterion is a property of the individual competitor at the moment of the event rather than a statistic over a population.
**What connects to what.** Adjacent corners of the square differ in one bit and have a statable relation.  The two diagonals differ in both, and they fail differently.  One carries a single bounded relation.  The other carries none at all.

| Pair | Edge | Relation |
|---|---|---|
| Boltzmann and Friston | Controller | exact: set the energy to the negative log joint and the variational bound is the Gibbs-Bogoliubov inequality, the same theorem in different symbols |
| Friston and Shannon | Anticipator | Friston is a Shannon-family divergence |
| Shannon and Kolmogorov | Adapter | the expected shortest description converges on the source entropy |
| Kolmogorov and Boltzmann | Explorer | execution: the minimum cost of turning one input into one output is bounded below by the conditional Kolmogorov complexity of the input given the output. This is the understory, where possibility becomes actual |
| Boltzmann and Shannon | Connector, diagonal | no general rate; one bounded floor, below |
| Friston and Kolmogorov | Operator, diagonal | none direct; the apparent link reaches Kolmogorov through Shannon and is two relations composed |

Three of the four adjacent relations I have already stated.  The Explorer relation I have not, and it follows here.
The two diagonals fail in different ways, and the difference is derived rather than observed.  The Connector diagonal carries one relation, bounded and running one way, which is Landauer's floor below.  The Operator diagonal carries none.  Its apparent relation is minimum description length, which reaches Kolmogorov by way of Shannon coding, so it is the two relations above composed rather than a relation of its own.  The step that will not go direct is from an ensemble to an individual.  A variational free energy is a code length averaged over a distribution, and a Kolmogorov complexity is the length of one program for one object with no distribution in it.  Passing through an adjacent corner is what a two-bit gap should require, and a direct result across this diagonal would be a problem for the geometry rather than a bonus.
**Gibbs-Bogoliubov.** At unit temperature the Boltzmann factor is the unnormalized posterior, and a mean-field trial distribution over it yields the evidence lower bound.  That is what makes the identification above exact rather than formal.
An exact correspondence at one edge does not merge the two denominations it joins.  The identification has to be made: someone chooses the energy to be the negative log joint, and that choice is made outside the unit, where the gas's energy is not.  This is the Jaynes answer at a second edge.  The geometry expects it too, because Boltzmann and Friston differ in one bit, and a correspondence that is exact and still leaves one difference standing is what an adjacent pair should look like.
**Zurek's bound.** The minimum thermodynamic cost of turning one input into one output is bounded below by the conditional Kolmogorov complexity of the input given the output.  Zurek stated the result in 1989.  It is not heat alone, and it is not a special case of the floor below it.
**Landauer's floor.** Erasing one bit costs at least `kT·ln 2` in heat.  That is the one rate on either diagonal, it runs one way, and it is a lower bound rather than a price.  It is why the four are not free-floating: every discard, whatever it is counted in, is paid at the bottom in heat, because it runs on physics.  It does not soften the claim that Expression's residue is the only literally thermodynamic one, because a floor on the physical implementation of a discard is not a claim about which denomination a residue is counted in.  What a biological process actually spends runs far above that floor, so the floor constrains without pricing anything.
**Jaynes.** Statistical mechanics can be derived as inference: the distribution to assume is the one that assumes least, given what is known.  That looks at first like a collapse, since it makes Boltzmann and Shannon one variational principle.  It is not one.  Jaynes's relativity is the observer's, and the sight bit above is the unit's; the gas holds no model of its own macrostate.  What Jaynes shows is that entropy is always relative to a specification, which is the argument for four denominations rather than against them.  Four specifications, four quantities that do not convert.  Boltzmann's constant converts units inside one sample space once the distribution is agreed to be over microstates; it does not convert the entropy of a gas into the entropy of a sentence.

## Adjacent Architectural-Frameworks Family
This belongs to the same family as Maynard Smith & Szathmáry's *Major Evolutionary Transitions* (1995).  The general claim, that cultural evolution represents a new inheritance line layered on the genetic, is established.  Dual inheritance theory has explained why cultural evolution is faster than genetic for decades.

### What This Adds
The framework's distinctive contributions, promised above, sit on top of that tradition rather than against it:
- **The four-row architecture** as a complete adaptive control system (Effector, Regulator, Modeler, Reviser) present at every level, instantiated in line-specific machinery and configured into 15 discriminable Venn regions whose adjacent-pair loops, triple constellations, and opposite-pair signatures all follow from the row functions.
- **The four-team relay**: exactly four flag-carriers at every rung, advancing by single-team handoffs, with the within-Organism fast loop and the cross-rung slow loop running the same exploration-consolidation dynamic at different temporal scales.
- **The maturity gradient**: continuous consolidation from exploratory to inherited-infrastructural, the same algorithmic logic (selection internalizing environmental correlation structure) operating across lines.
- **The cross-line extension**: the same architecture at every inheritance line and every kind of slack (genetic, neuronal, symbolic), because surviving lineages are good regulators isomorphic to internalized environmental models and the cybernetic minimum is substrate-independent.
This is what makes the framework a theory of personality across lines, not a theory of human personality with metaphorical extensions.  Personality falls out of the architecture when the unit is an individual primate.  The architecture applies wherever the conditions hold: a cybernetic loop subject to inheritance.

---

## The Letter

The letter came from an office that does not answer letters.  It was written on paper heavier than any paper made now, and it was sealed twice.

It said that the Bureau of Persistence has four floors.

It said that the first three floors pay what they owe out loud, in public, in front of witnesses, with a number, in the ordinary way, and that their books are in order and always have been.

It said that the figures on the fourth floor are impossible.

And then it said the thing that made Dera put down her tea.

On the eleventh of last month, on the fourth floor of the Bureau of Persistence, an attendant was destroyed.  Not injured.  Destroyed, entirely, in front of nine witnesses, and it is in the minutes, and the minutes are signed.

The next morning he was back at his post.

No payment was demonstrated.  No bell was rung.  No number was said out loud by anybody at any point.

Dera was to go up there and find out who paid for it.

And then, at the bottom, in a different hand, there was one more line, and it is the most important line in the letter and Dera read straight past it four times.

**This audit has been requested by the fourth floor.**

Not ordered.  Not required.  Requested.  Somebody up there wrote in and asked to be looked at.

That was the whole of it.  She read the letter four times on the train, and by the fourth time she had begun to feel that it was shorter than it ought to be, and she never once wondered who had done the requesting, because nobody had ever asked to be audited before and it did not occur to her that anybody would.

Somebody had.  You will meet them on the fourth floor, sitting in a chair by a window, and this account will tell you who they are the moment you get there, and Dera will not find out until she is back on the doorstep with an empty pen.

## The Doorstep

The Bureau of Persistence is a tall grey building at the end of a road with no dust on it, and on the doorstep there sits a man on a three-legged stool.

The stool has one leg shorter than the other two and it does not rock, because the step slopes down to meet it.  Dera noticed this and decided not to think about it yet.

The man was very wide and not at all tall, and there was nothing to him.  Dera worked this out later, on the day the building went quiet, and it is worth knowing now: he is wide the way a drift of sand is wide.  He has never signed anything and he never will, and he has never lifted anything in his life, and everything about his size arrived at him rather than being put on.

He was grey.  Not his hair.  All of him.  It was in his cuffs and his knuckles and the creases of his neck and the rims of his ears, a soft dry dust that had plainly never once been damp, and he smelled of nothing whatever except paper going quietly to powder.

His hair grew from a single point at the top and went round from there in a spiral.  Dera counted the arms of it while he was taking her coat.  Thirteen going one way.  Twenty-one going the other.

She did not say anything about it.  You do not, on a doorstep, to somebody holding your coat.

His beard did the same thing smaller, in overlapping plates, like a pinecone.

His forearms were striped.  The stripes on the left arm were not the same stripes as the ones on the right arm, and they obeyed the same rule, whatever the rule was.  The backs of his hands were spotted, bigger spots at the wrist and smaller at the knuckles, the way spots go on an animal that has to hide.

And his knuckles were hexagons.  Six-sided, slightly domed, and so were his fingernails, all ten of them, in neat plates.  Cooling lava does this.  Nobody had ever suggested to Dera that a person might.

Beside him on the step was a chipped white cup of tea.

The tea in it had arranged itself into small columns of moving liquid, dozens of them, each one six-sided, all of them turning.  The cup was full to a quarter inch below the chip.  Dera watched it for some time and it stayed exactly there, and she never once, in six weeks, saw the Porter drink from it or fill it.

"Did you bring your own pen?" said the Porter.

Dera showed him.  It is a plain pen with a barrel of clear celluloid, so that you can hold it up to the light and see how much ink is left in it, and her mother had given it to her.

The Porter was extremely pleased about the pen, which struck Dera as a great deal of pleasure for a very small object.

"Good.  Watch it," he said.  "That's the only advice anybody here will give you for free."

"Watch it do what?"

Then, from somewhere inside the building, a bell rang.  Once.

And every person inside that building, on all four floors, said a number out loud, together, and the number was **one**, and then they went back to what they were doing.

Dera stood very still on the step with her hat in her hand.

"What was that?"

"Somebody paid," said the Porter.

"Paid what?"

"Weight," said the Porter.  "Downstairs.  That's the first floor.  You'll hear it about nine times a day and you'll hear it on every floor there is, because it's a loud bell and this is a tall building and there's nothing in the way."

Now.  Here is the rule of the Bureau of Persistence.

There is one rule.  Just the one.  It is going to come up on every floor, so it is worth learning it now and then you will never have to worry about it again.

**EVERY PAYMENT IS MADE OUT IN THE OPEN, ON A MACHINE, IN FRONT OF WITNESSES, WITH THE NUMBER SAID OUT LOUD.**

Out in the open.  On a machine.  In front of witnesses.  With the number said out loud.

That is the rule.  Nobody in that building hides anything, nobody in that building has ever hidden anything, and nobody in that building has ever needed to.

Now here is the other thing, and it is not a rule, because nobody made it and nobody enforces it and it simply happens.

**When somebody signs their name, they get bigger.**

Straight away.  While you are looking at them.

Taller.  Broader through the shoulders.  Thicker in the arm.  Rounder.  Heavier, so that the floor knows about it.  All of that at once, and all of it in the time it takes the pen to finish the last letter, and everybody in the room sees it happen and nobody remarks on it, because it goes on all day long.

Not a great deal for one signature.  About the thickness of a slice of bread, in every direction at once.  But it is there, and it stays.

A machine charges you whether you like it or not.  Nobody can make you sign.  **That is the only thing in the Bureau of Persistence that makes a person bigger, and there is nothing anywhere in the world that makes them smaller again.**

And it is not a prize.  Understand that now.  The big ones in that building carry the heavy end of everything, because they are the ones who can, and they go through every doorway in the place sideways with their chin down, forty times a day, for the rest of their lives.

Which is why the doors on the first floor are enormous, and the doors on the fourth floor are the ordinary size, and why there are people in that building who could walk under a table without stooping.

Which brings us to the answer, and you are getting it now, on the doorstep, before Dera has gone inside, because there is no fun whatever in watching somebody hunt for a thing when you do not know what the thing is.

**The attendant on the fourth floor was paid for downstairs, before he existed, and there is nobody you can send the bill to.**

That is it.  That is the whole answer to the letter in her coat pocket.  You have it in your first ten minutes and she does not have it for six weeks, and she is not stupid, and she does not miss a single piece of evidence.

She finds all four of the facts you need.  Personally.  With her own hands.  She writes every one of them down in her own notebook in her own handwriting.

And she files each one under the wrong heading.

This account is going to count them off for you as she gets them, out loud, so that nobody has to wonder later whether that was one of the four.  There are four.  They are numbered.  When she gets one you will be told.

"Go down," said the Porter.  Then he looked at her properly for the first time.  "And what IS an auditor?"

"Somebody who finds out who owes what," said Dera.  That is what an auditor is.  There is no more to it than that and she has never thought there was.

"Ah," said the Porter.  "Well.  Good luck to you."

"And what IS a porter?"

He thought about it for a while, as though nobody had troubled him with it before.  "Somebody things arrive at," he said.

Then he stood up, which took a while, and said, "Pick up the stool."

Dera picked up the stool.  It is a three-legged stool made of oak and it took both hands and she got it about as high as her knee and put it down again, and she was rather out of breath about it.

"Right," said the Porter, and wrote something down.  "Now against the frame, please."

The doorframe of the Bureau of Persistence is enormous.  Dera had already noticed that.  It is about a foot and a half taller than any door needs to be, and the wood of it is covered from top to bottom in little pencil marks, hundreds of them, each with a name beside it and a date, going up and up until the highest ones are out of reach and somebody has clearly stood on the stool.

Dera put her back against it.  The Porter laid a ruler flat on her head, made a small mark, and wrote **DERA** beside it and the date.

Her mark is very low down.  There is a great deal of empty wood above it.

"Is that a custom?" said Dera, who thought it was a rather silly one.

"It's the measure," said the Porter.

"What for?"

"You sign anything in there," said the Porter, "you come out bigger.  Everybody does.  Taller and broader and stronger and heavier, all of it at once, and it happens on the spot and it doesn't come off, and there's no machine in that building that takes it back, and nobody has ever asked for one."

"Bigger how much?"

"Depends what you sign," said the Porter.  "And it doesn't get any easier going through doors, so don't let anybody tell you it's all one way."

Dera wrote **local custom, doorframe, harmless** in her notebook.

Then he reached behind the stool and brought out a pair of brass scales, and a tin scoop, and he scooped up the day's dust off the step and weighed it, and took a stub of chalk out of his waistcoat and wrote the weight on the stone by his foot in figures four inches high.

There were a great many such figures on that step.  They went back along the flags as far as Dera could see, in every hand, some of them nearly rubbed away, and not one of them was smaller than the one before it.

"Does anybody read those?" said Dera.

"No," said the Porter, and put the scales away.

Now the sensible thing at that point would have been to ask a second question.  Dera will tell you afterward that she meant to.  But he had already begun on the building, and there were three things about it, and all three turned out to be true, and the trouble with three true things is that they use up all the room a fourth question might have had.

**The first thing.** Every object in the Bureau of Persistence is warm on one side and cool on the other, and the cool side is always the side you have just touched.

Dera tested this, because she is an auditor.  Over her first afternoon she tested nine doorknobs, a banister, a teacup, and the Porter's own stool, and it holds every single time.  Later she carried a thermometer round the whole building for an afternoon, and the thermometer says the Bureau is exactly the same temperature everywhere, and her hand says otherwise.

She decided to believe her hand.  Her report says so, in those words, and it is the only place in ninety pages where she says anything of the kind.

**The second thing.** There is a low note under the whole building, very quiet, like a chimney with something being pulled up it.  Nobody has ever found the chimney.  When the Porter spoke, the note was in his voice.  Not like it.  It was the same note.  A flute does this to a shapeless push of air: it hands you back a clean ladder of notes, for nothing at all, and never sends a bill.

**The third thing.** The floor of every room in the Bureau is a little lower in the middle than at the walls.  It is far too small a slope to notice in one room.  Walk down a long corridor and you can feel it going down.  Walk back up the same corridor and you can feel it going down.

"Who built it like that?" said Dera.

"Nobody built it like that," said the Porter.  "It came like that."

## The Dust

The dust round the Porter's stool is not road dirt and never was.  It is the building coming to bits.  One soft sifting a day, out of the ceilings and the ledgers and the pockets of everybody upstairs, and all of it arrives at him, because every corridor in the Bureau runs downhill in both directions and he is where downhill stops.

Plaster.  Paper gone to powder.  Grain.  Ink.

He does not sweep it.

"Oughtn't somebody clear this?" said Dera.

"Nothing that reaches me goes anywhere else," said the Porter, and that is the only thing he ever said about himself.

And the dust makes shapes.  On the flags round the stool it has sorted itself into rings and polygons, coarse grit at the edges and fine stuff in the middle, the way stones in a cold country arrange themselves into circles over years with nobody laying them out.  Along the wall the drift has made meanders, like a river seen from very high up.  There are small dunes with a steep side and a long side.  And at his feet, where the pull is strongest, two or three slow eddies turn in the dust and hold their shape.

Dera wiped her feet before she went in.

There was nothing on her shoes.  She did it out of habit, and it accomplished nothing at all except that she scuffed a good third of the rings flat.

The Porter watched her do it and said nothing.  He was not offended and he was not amused.  There was nothing in it for him either way, and this is the first thing about the Porter that anybody ought to understand: there is never anything in it for him either way.

An hour later Dera came back past that spot and the rings were there again.

Not similar rings.  The same rings.  Coarse at the edges, fine in the middle, exactly as before.

She knelt down and scuffed them again, deliberately this time, with the side of her hand, and then she asked whether she had damaged anything.

"No," said the Porter.

"It mended itself."

"No," said the Porter.  "It fell back into it."

"What's the difference?"

"Bell didn't ring," said the Porter.

And that is the difference, and it is the whole difference.

When the rings come back, no bell rings.  No number is said.  Nothing is put on any machine anywhere.  Dera stood on that step for a full hour and broke the rings eleven times and watched them come back eleven times, and no bell rang, not once, and nobody witnessed anything, and there is no figure for it on the step or in the book or anywhere else in the Bureau of Persistence.

The rings come back and nobody pays.

Hold on to that.  It is going to matter enormously.

Dera wrote that down without understanding it.  She has read it two hundred times since.

## The Other Thing on the Doorstep

Off to one side of the rings, in the dust, there was a small thing about the size of a thumbnail.

It was not a pattern.  It had an inside and an outside.

Dera broke it, gently, with a fingernail.  Something spilled out of it.  Then something else began to build a shell round the something, slowly, and after a while there was one small thing again, exactly as before.

She broke it a second time, harder, because she is an auditor and one result is not a result.

This time there were two.

Both of them were it.  Neither of them was the one she had started with.  Nothing about the way she had broken it decided which would happen, and she tried very hard afterward to work out what she had done differently, and she had not done anything differently.

"How long has that been doing that?" said Dera.

"Longer than the building's been standing," said the Porter, in the voice you would use to say that the west stair is cold.

"Which is the mending?  The one, or the two?"

"Nobody can tell them apart," he said.  "It's the same happening, both times."

Then he did something Dera did not understand for six weeks, and it is the most important thing anybody does in this book, so it is going to be described very slowly.

He got out the brass scales again.

He put the small thing's spilled dust on the little pan, the jeweller's pan, the one Dera had not noticed was there.  He weighed it.  He got out the chalk.  And he wrote the figure on the step in a **second column**, well away from the big one, in figures four inches high, exactly like the others.

**TWO COLUMNS OF CHALK NUMBERS. ON A DOORSTEP. IN FIGURES FOUR INCHES HIGH.**

One big column and one little column.  Have a good look at them.  They are the two most important things in this book and there is nothing complicated about them whatsoever.

The big column is the building's dust.  Four floors of it, coming apart, arriving at the bottom because everything in the Bureau runs downhill in both directions.  Nobody pays for that.  Nobody is charged for it.  It simply arrives, and he weighs it, and no bell rings.

The little column is the small thing.  Every time it puts itself back together it throws off dust, and the dust can be weighed, and it gets weighed, and it gets written down.

**The small thing pays.  The rings do not.**

They both come apart.  They both come back.  One of them is on a machine with a number beside it and the other one is not, and that is the only way anybody has ever been able to tell them apart, and there is no other way, and Dera will be told this again on page after page until she believes it.

Dera wrote it down as a curiosity.

It is the answer to her letter.  She did not recognise it for six weeks, and it should be clearly understood that this was not stupidity.  She was told the answer on the doorstep, before she had gone inside, by a man on a stool, and no docket was raised, and nobody signed anything, and there is no book anywhere in the building with that conversation in it.  That is exactly the trouble with it.

## Four Rooms and Four Signs

The Porter told her the building has four floors, that nobody may start higher than the first, and that the terms of her visit were already written into the floor she was standing on.

Every floor of the Bureau has the same four rooms.

There is a **store**, which holds what has been kept.  There is a **long room with the good light**, which holds what is ready now.  There is a **workroom**, where things are put together.  And there is a **room at the end**, into which more is pushed every day than it has room for.

Past the room at the end there is one more room.  It is small.  It is swept.  It is empty.  It has a plaque on the door.

The four floors are alike in every way but one, and the one way is on a sign at the bottom of each stair.

The sign at the bottom of the first stair said:

**ON THIS FLOOR A MISTAKE COSTS A BODY.**

Dera does not have this straight for six weeks, and a great deal follows from that.

There are two sums running in the Bureau of Persistence and they are not the same sum.

The **first** is what a mistake costs, and it is posted on a sign at the bottom of every stair, in letters a foot high, and when you make one you are handed a card with a number stamped on it.  Nobody could possibly miss it.  Dera watches this sum from the first morning to the last afternoon, and it is the sum in her letter, and it is the sum she was sent for.

The **second** is what it costs to keep going.  It is nowhere on any sign.  It is in the chalk figures on the doorstep, which nobody reads, and in the barrel of her pen, which nobody in the building is charging her for.  It runs at the same speed whatever anybody does, and it has never once been posted anywhere, and there is no card.

Dera spends six weeks thinking she is auditing one thing.  She is spending the other.

Keep an eye on the pen.  She does, five times, and gets the wrong answer four of them.

# Night Four

## Foundations

### Reading the Venns
The Venn architecture relies on a logical relationship the Port-Royal logicians named in 1662.  Antoine Arnauld and Pierre Nicole, in *La Logique, ou l'art de penser*, paired the terms comprehension (what later logic calls intension: the set of attributes that define a concept) and extension (the set of things falling under the concept).  Their thesis: the two vary inversely.  Add an attribute to a concept and the class of things it picks out typically shrinks; drop an attribute and the class expands.  Their canonical example was geometric.  "Triangle" has thinner comprehension than "equilateral triangle," which carries every attribute of triangle plus equality of sides.  But "triangle" has larger extension, because every equilateral triangle is a triangle and not the reverse.
Two caveats.  The relationship is a tendency rather than a theorem; redundant attributes can be added without excluding anything.  And modern logic since Frege has reframed both terms more rigorously, with extension as the set of satisfying objects and intension as something closer to a function from possible worlds to extensions.  The Port-Royal version is the philosophical ancestor of the modern formalism, not the formalism itself.
The working intuition (more specification, fewer cases) is what the Venn architecture rides on, and it sorts the regions into five content-types.  Single-motivation regions have one attribute, large extension, thin comprehension; they carry motivations.  Two-attribute regions come in two kinds: adjacent pairs carry tendencies, opposite pairs carry signatures, both with smaller extension and richer comprehension than the singles.  Triple regions have three attributes, smaller still, richer still; they carry capacities.  The center has all four attributes, the smallest extension of any region, and the richest comprehension; it carries the breakthrough, the unique synthesis that requires all four motivations to produce.
This is why the breakthrough at the center is not a fifth motivation.  A fifth motivation would be a new attribute added at the same level as the original four.  The breakthrough is what falls out from the intersection of all four; it is the highest-comprehension, smallest-extension region of the Venn, which is exactly what an architecture this geometry generates.
The five content-types are the five stanzas every per-cell treatment below runs through, in this order and with this meaning throughout:
- **Motivations** — the four base drives, one per cybernetic function.
- **Tendencies** — adjacent-function blends, each pairing two neighbouring drives.
- **Signatures** — the two cross-function pairings that mark the clade.
- **Capacities** — the four triples, each defined by the one function that is *absent*.
- **Breakthrough** — the framework-center concept unlocked at that rung.

### Every Center Is a Selector
The center of a Venn carries that Venn's breakthrough.  At every scale the framework uses, that breakthrough turns out to be whatever does the selecting for the units the Venn is about.
A founding cell's center is its line's selector, which the Per-Cell Treatments below state directly.  The center of the Venn of Lines is Darwinian evolution by natural selection.  The center of the selection cycle is selection itself, which is the four stages running as one turn.
Those are three instances rather than three coincidences.  Blind variation with selective retention, after Donald Campbell, is the scale-general description of what a selector does, and each of the three is that description at one scale.  So the rule generalizes: name a Venn, and its center is what selects among the units it is drawn over.
One consequence is worth carrying.  A selector discards, so every center has a residue, and the residue scales with how selective the center is.  A residue is what the center stops funding rather than what it destroys, and the ground state does the rest.  Natural Selection's residue is every line of descent that stops being paid for.  Attention's is everything that stayed live and never won the workspace.  Conversation's is everything thought and not said.

### The Scope of a Cell Claim
A cell claims that on this thread, at this rung, four flag-carriers jointly produce one breakthrough.  The clade name is the rung's address.  It is not a quantifier over the clade's membership.
The distinction needs stating because the diagram is drawn as a ladder, and readers arrive at a ladder expecting a ranking.  Four readings the matrix does not license:
**Not exclusive.** The cell does not claim that only members of the clade carry the capacity.  Off-thread lineages build their own stacks and reach their own syntheses above their branching points.  A crow that simulates or an octopus that models is the architecture working, not the architecture breaking.
**Not a priority claim.** The cell does not claim the clade got there first.  Where I say a cell introduces something, the introduction is indexed to this thread.  Another thread may have reached the same synthesis earlier, later, or not at all, and the cell is silent on all three.
**Not an absence below.** The cell does not claim the capacity is missing at lower rungs.  Motivations retire into backgrounded infrastructure and keep operating.
**Not a description of any living member.** The cell describes what the rung installs.  Every living member sits above its rung on its own branch and carries its own elaborations, so a member's four active flag-carriers are read off that member's own stack rather than off the matrix.
One question about a cell is always legitimate, and it is none of the four.  A reader may ask whether the capacity reconstructs below the rung on this thread.  That is the branch-point test, and a capacity that clears it does move the label.
The ladder shape encodes genealogy and not rank.  A thread has an order because descent has an order.  Every living lineage has been evolving for the same interval, and the rungs above any branching point belong to whoever climbed them.

### The Four Functions
The four rows of the diagram name four cybernetic functions of the unit at every level.  Each function has a single role.  Together they constitute a complete adaptive control architecture.
A motivation is a dimension along which the units of a clade reliably differ.  Each motivation occupies one of the four functional positions and names the variation that position carries at that cell.  Persistence names how tenaciously protocells hold a boundary against dispersal.  Commitment names how far a symbolic-line unit binds itself to a chosen course.  Both are the same kind of construct because both are dimensions of measured variation.
The word carries no intention.  A motivation is not an inner state, not a goal the unit holds, and not a cause the unit contains.  It is a coordinate, a place in the classification where the units of a clade spread along a measurable range.  What produces the spread is selection acting on heritable variation, and no motivation is ever asked to do that work.
This keeps description and explanation apart.  Naming a dimension is not explaining it, and no unit is made to vary by the name of the axis it varies along.
*framework definitional commitment.  Separating a descriptive trait construct from the mechanism that produces it follows Fleeson and Jayawickreme's Whole Trait Theory.  Supplying that mechanism architecturally rather than behaviorally follows DeYoung's Cybernetic Big Five Theory.*
**Effector.** The line's executive arm.  What makes the unit execute its native verb: persist at the genetic line, seize at the neuronal line, commit at the symbolic line.  Effector motivations are the line's primal directives: Persistence, Impetus, Commitment.  Action is the row's function.  In selection, the Effector weights recency: to act is to commit to the freshest signal.  Externalization names the same function viewed from outside the unit: the Effector propagates outward what the Regulator stabilizes, the Modeler models, and the Reviser revises.  *Evolutionary signature:* founding form of each line, line present, regulatory layer not yet stabilized.
**Regulator.** Closed-loop stabilization against stored references.  The rule both is the setpoint and enforces it; that is why the comparator and the storage are one row, not two.  Regulator motivations are what makes the unit's behavior consistent across instances: Dissipation, Coordination, Mastery, Stability.  Stabilization is the row's function.  In selection, the Regulator weights familiarity: to stabilize is to defend the established predictor against new rivals.  *Evolutionary signature:* stored regulation, adjustable rules govern responses without rewriting the underlying structure.
**Modeler.** Internal representation that organizes inputs into a usable account of the world.  Sensing is downstream of having a model worth updating.  Modeler motivations are what makes the unit's interior do representational work: Self-Organization, Interiority, Autonomy, Representation.  Modeling is the row's function.  In selection, the Modeler weights potency: a single account foregrounds the strongest input and lets it overshadow the faint.  *Evolutionary signature:* organized interiority, internal organization with multiple co-occurring properties (opacity, modularity, protected operating conditions, capacity expansion, asymmetric exchange, internal coordination); structurally interior, not just bounded.
**Reviser.** Meta-loop that revises the references the regulator stabilizes against.  Reviser motivations are what makes the unit able to change its own goals: Self-Production, Excitability, Affiliation, Universality.  Revision is the row's function.  In selection, the Reviser weights novelty: to revise is to weight what hasn't been seen and let the familiar fall to background.  *Evolutionary signature:* specialized differentiation, division of labor among parts that, in the bridging cases, produces the next line's slack.
Each function carries a signature bias in selection — the rule it applies to decide which cue to credit.  The four are recency (Effector), familiarity (Regulator), potency (Modeler), and novelty (Reviser).  Every line runs this bias through its own selector: differential reproduction on the genetic line, attention on the neuronal line, differential adoption on the symbolic line.  On the neuronal line these four are the Pavlovian associability heuristics — eligibility trace, blocking, overshadowing, and latent inhibition.  The bias is not separate from the function; it is the function seen from the selection side.
The sequence is not arbitrary.  There is no Regulator without an Effector to regulate, no Modeler without a regulated system whose internal state is worth representing, no Reviser without a model worth updating.  Each row depends on the prior row having been achieved.  This is why the cybernetic functions emerge in this order at every line, and why the evolutionary descriptions track the functional ones: an effector must be present before it can be regulated; regulation is required before an interior can be defended; a defended interior is required before its parts can be specialized.
The four cybernetic functions are all primaries: single-attribute building blocks at the base of the Port-Royal gradient that organizes the Venn.  The dependency sequence (Effector → Regulator → Modeler → Reviser) does not establish a gradient AMONG the four.  Each primary is one attribute.  The gradient runs across constellations that combine multiple primaries: single (1 attribute) to pair (2) to triple (3) to center (4).
What the dependency sequence DOES establish is the temporal order in which higher-gradient constellations become evolutionarily available.  Pair constellations require at least one function beyond the Effector.  Triple constellations require three of the four.  Center constellations require all four in place.  The Port-Royal gradient is the spatial organization of the Venn.  The dependency sequence fills the Port-Royal gradient over evolutionary time.
The four functions sort onto two orthogonal axes.
**Object vs. control.** The Effector and Modeler are object-level: what the system operates with (action and model).  The Regulator and Reviser are control-level: what shapes the system's operation.  The control-level rows take the object-level rows as input.
**Action vs. model, and stabilize vs. revise.** Within each axis-cluster, the two functions take opposite positions.  The Effector acts and the Modeler models.  The Regulator stabilizes and the Reviser revises.  The stabilize/revise distinction is the explore/exploit axis at the cybernetic-meta level.

---

# Night Five

## The Mirror

### Two Poles, Two Functions
Walk the four functions in order: Effector, Regulator, Modeler, Reviser.  Two of the four functions serve both poles, maintenance and variation, and two serve one pole each.
The Effector and the Modeler are shared.  The Effector acts, which variation needs, because it expresses variation into the world, and which maintenance needs, because it drives the unit back to reference.  The Modeler represents, which variation needs, because it supplies the model that revision rewrites, and which maintenance needs, because it supplies the forecast that regulation acts on.  Each of these two functions sits on one edge of each pole.
The Regulator and the Reviser are exclusive.  The Regulator holds a reference and defends it, which is maintenance and nothing else.  The Reviser generates variation and rewrites the reference, which is variation and nothing else.  Variation is rooted in the Reviser; maintenance is rooted in the Regulator by the same logic.  These are the two roots, one per pole, and they are the Operator diagonal, the pair that differs in both bits of the reflexivity square, sighted-bounded against blind-unbounded.  Selection belongs to neither.  It is Darwin at the center, and it acts on what both poles produce.  Maintenance names the pole here and the cycle's paying face, and the two are different scales of one word.  At pole scale it is the Regulator's charter, set against variation.  At cycle scale it is what the whole turn costs its payer, and there it is not set against selection but is one side of it.
The Venn of Lines adds one thing to hold in view, because it uses the same function names at a second scale.  At the scale of the whole tree each line plays one function: genetic is the Effector, neuronal is the Regulator, symbolic is the Modeler, and the digital line is the Reviser.  So "the Regulator" names both a function that runs inside every line and, once, a whole line.  Read it as the function, the within-line Regulator that every line carries, not the neuronal line alone: the neuronal line is the tree's exemplary maintenance line, and the digital line its exemplary variation line.
The origami identity states the split in one image.  A folded form is creases and panels.  The creases are where the sheet changes; the panels are what stays rigid so the change does not tear the sheet.  Variation is the creases.  Maintenance is the panels.  Compression is the fact that the two are complementary: a form is cheap to specify exactly when its change lives at sparse creases and its panels hold.
*The origami figure.  What transfers: creases as the locus of variation, panels as the locus of maintenance, compression as the complementarity of the two.  Does not transfer: the origamist's foresight, since the framework's folds are placed blind, and the change of paper across lines, since no two lines are taking up the same kind of slack and there is no exchange rate between them.  Scope: within a line.*
*the shared-versus-exclusive reading of the four functions is structure I am committing to, and it follows from the adjacent-pair loops already set out.  The origami identity is committed here and ratified again for the digital slack.*

### The Two Modes: Feedback and Foresight
The Regulator maintains in two modes, and they are the two edges it sits on.
Feedback is the Controller edge, the Regulator paired with the Effector.  The unit measures the gap between where it is and where its reference says it should be, and it acts to close the gap.  This is the textbook closed feedback loop, canon since Wiener.  Feedback waits for error and then corrects it.  It needs no forecast, only a reference and a way to sense the deviation from it.
Foresight is the Anticipator edge, the Regulator paired with the Modeler.  The unit carries a model of how the world behaves, so it can act on predicted error before the error occurs.  The good-regulator theorem belongs here, not to feedback.  It says that once the world outruns stored correction, good regulation must grow a model, which is the pull from the Regulator toward the Modeler, not a property of regulation as such.  Pure feedback needs no model; foresight is the mode the theorem charters.  So the theorem, read closely, is less about the Regulator than about what the Regulator must reach for, and the Anticipator is that reach made into a standing loop.  Foresight prepares for the disturbance the feedback loop would otherwise have to absorb after it lands.
Which mode wins depends on the weather.  Feedback wins in a world too chaotic to forecast, where preparation is wasted and only fast correction survives.  Foresight wins in a predictable world, where the disturbance can be modeled and met before it arrives.  Brand's ocean gives the two modes their faces.  Knox-Johnston, who deals with what comes, is the feedback maintainer who takes each failure as it arrives.  Moitessier, who prepares for the worst, is the foresight maintainer who services the boat before the storm.
The genetic line runs both modes without metaphor.  Feedback is DNA repair: mismatch repair and break repair that fix damage after it lands.  Foresight is adaptive immunity: the CRISPR-Cas system keeps a record of past invaders as stored spacers and cuts the ones it has met before, on sight, and proofreading catches the error before it sets.  Moitessier's logbook and the spacer array are the same device, a memory of past trouble kept so the next instance is met early.
*The sailors.  What transfers: the two maintenance postures and their regime-match.  Does not transfer: the sailors' intent, and a third sailor, Donald Crowhurst, who is treated as a failure of maintenance rather than a mode of it.*
*the two edges are the adjacent-pair loops, which are not mine.  Reading them as the two modes of maintenance, and the regime-match that selects between them, are mine.*

---

## Tendencies

### Adjacent Pairs as Closed Feedback Loops
Each adjacent pair is a closed cybernetic loop between two of the four functions.  There are four such loops because there are four adjacent pairs around the cycle.
**Effector × Regulator \= Controller.** Closed-loop control.  Action goes out; the regulator measures error against stored reference; the regulator adjusts.  The textbook feedback loop.
**Regulator × Modeler \= Anticipator.** Model-informed regulation.  The model lets the regulator look ahead instead of reacting only to error.  Predictive control; Kalman-style state estimation; active inference's predictive coding loop.
**Modeler × Reviser \= Adapter.** Self-revising model.  The model gets updated by the reviser; the reviser proposes updates the model integrates.  This is what learning means in the most fundamental sense, model adaptation.
**Reviser × Effector \= Explorer.** Exploratory action.  Action that tries new things; results revise what gets tried next.  The seeker of epistemic value.
The four adjacent-pair functions are the four primitive cybernetic loops.  Every more complex constellation is a synthesis of these.

### If Tendencies were Knobs: Toggles between clade N and clade N−1
Every tendency knob is installed at one cell and toggles between two adjacent functions: the cell's own function (N) and the function of the cell below it (N−1).  The knob's volume-up pole is the cell's own bias, the newer installed layer, the derived setting.  Its volume-down pole is the prior cell's bias, the ancestor showing through, the ancestral setting.  A knob is therefore never the property of one clade alone; it exists to toggle between a clade and its predecessor.
Which adjacent-pair loop a knob is follows from the cell's function, because the cell's function is the up pole and the predecessor's function is the down pole:
- Effector cells (Protocell, Bilaterian, Band-Human) install Explorer knobs.  Up is recency (Effector); down is novelty (the prior Reviser).  The Explorer edge (Reviser × Effector) is also the line-bridge edge, so an Effector cell's down pole reaches back across the line boundary to the previous line's Reviser.
- Regulator cells (Prokaryote, Vertebrate, Settlement-Human) install Controller knobs.  Up is familiarity (Regulator); down is recency (the prior Effector).
- Modeler cells (Eukaryote, Mammal, City-Human) install Anticipator knobs.  Up is potency (Modeler); down is familiarity (the prior Regulator).
- Reviser cells (Eumetazoa, Primate, Empire-Human) install Adapter knobs.  Up is novelty (Reviser); down is potency (the prior Modeler).
The four selection biases are recency, familiarity, potency, and novelty, one per function.  On the neuronal line these biases are named as the four Pavlovian associability heuristics: eligibility trace (recency), blocking (familiarity), overshadowing (potency), and latent inhibition (novelty).  A tendency knob toggles between the two heuristics of its two functions: the up pole runs the cell's own heuristic, the down pole runs the predecessor's.  The Orienting knob (Bilaterian, Explorer) toggles eligibility trace (recency, up) against latent inhibition (novelty, down).  The Coping knob (Vertebrate, Controller) toggles blocking (familiarity, up) against eligibility trace (recency, down).  Every knob around the cycle toggles the two-of-four that its function and its predecessor's function name.
The biases install one per cell as each cell's own function arrives, in the order the functions arrive: familiarity at the first Regulator cell (Prokaryote), potency at the first Modeler cell (Eukaryote), novelty at the first Reviser cell (Eumetazoa), and recency at the first Effector cell whose knob performs credit assignment (Bilaterian).  Protocell's Effector knob is the wind-up (Going), which carries no credit-assignment heuristic, so recency as a running heuristic waits for the neuronal Effector at Bilaterian.  From Bilaterian onward all four heuristics are present, and each later cell's knob re-toggles the same two-of-four its function and predecessor name.
Volume up and volume down are properties of knob settings, not a ranking of the four functions, which remain equal primaries.  The up pole is the newer layer; the down pole is the older layer showing through.  This is the eclipsing account applied to the knobs: at a knob's down pole the newest layer goes dormant and the ancestor beneath runs.

### Durable and transitional tendencies
Each cell installs two new tendency labels, and the two have different lifespans.  A durable tendency holds its edge for three consecutive cells.  A transitional tendency holds its edge for one cell and gives way at the next.
At any cell, three of the four edges carry durable tendencies and one carries a transitional tendency.  The transitional edge is the next edge clockwise from the edge receiving that cell's new knob.  Bilaterian installs the Explorer knob, so the Controller edge is transitional there and carries Affect for that cell alone.  Vertebrate installs the Controller knob, so the Anticipator edge is transitional there and carries Development Rate.
A transitional tendency carries no knob.  It does not hold its edge long enough for a household setting to mean anything from one quarter to the next.  All twelve knobs sit on durable tendencies, and each knob is installed at the first of its tendency's three cells.
This fixes how long a knob lives.  A knob lasts exactly as long as its tendency label lasts.  It comes online when the label arrives at its edge, and it retires when the label gives way.  The knobs in play at a cell are therefore the knobs of that cell's own tendencies, never a label the Venn has already replaced.
The transitional edge also names what comes next.  The edge running a transitional tendency at one cell is the edge that receives the following cell's new knob, so the gap in the current quarter marks where the next quarter's knob lands.
*the three-cell durable run holds for all twelve knob-bearing tendencies.  Two labels at the founding cells run short of three, Enclosure Type across Protocell and Prokaryote and Aging Type at Protocell, because the alternation has no cells below Protocell to start from.  Neither carries a knob.*

---

## Function Ground Truths: World, Body, Future, Mind
Each cybernetic function's job fixes what its output is about — where the state it tracks actually lives, and therefore what would have to be checked to find out whether the output is right.
**Effector → a world.** The Effector's job is to act, and action is directed outward, at something external to the unit.  What the Effector's output is about lives in a world: the thing acted on, checkable by looking at the world itself.
**Regulator → a body.** The Regulator's job is to stabilize the unit's own behavior against a stored reference (the Controller loop, "Adjacent Pairs as Closed Feedback Loops"); its comparison runs entirely inside the unit.  What the Regulator's output is about lives in a body: the unit's own current state, checkable by looking at the unit.
**Modeler → a future.** The Modeler's job, in its foresight mode, is to look ahead of the disturbance rather than wait for it ("The Two Modes: Feedback and Foresight").  A model that only describes the present is a Regulator's mirror, not a Modeler's use; what makes modeling worth its cost is running forward.  What the Modeler's output is about lives in a future: a state that does not yet exist, checkable only once it arrives.
**Reviser → a mind.** The Reviser's job is to change the unit's own references, not merely update them against new data ("Reviser motivations are what makes the unit able to change its own goals").  A reference the unit could derive on its own is an update, not a revision; the only source of a reference the unit did not already have is a system whose references were never the unit's to begin with — another agent.  This is not incidental to the Primate cell: Affiliation is the Primate Reviser motivation, and Affiliation is the slack the neuronal line ratchets for the symbolic line's exchange-based selection to run on.  Exchange has no meaning for one party.  The neuronal Reviser is not a function that happens to notice other minds; representing another mind is the raw material it exists to produce, because the next line cannot start without it.  What the Reviser's output is about lives in a mind: a set of references the unit does not have and cannot derive, checkable only by consulting the agent whose they are.
A world, a body, a future, a mind — one location per function, and each is where that function's own job already points, not an added stipulation.
The four locations sit at increasing remove from the unit's present moment.  A world and a body are both available for inspection now.  A future has not happened yet.  A mind is never available for direct inspection at all.  Any layered architecture built on these four functions inherits that ordering, and inherits it as a property of the functions rather than as a convention of its own.
*the four function-jobs (act, stabilize, model, revise) and the two modes (feedback/foresight) are not mine.  The ground-truth-location reading of each job — world, body, future, mind — is mine, drawn from those jobs, not yet independently attested outside the framework.  The Reviser argument additionally depends on the variation-selection reading of the four functions and on the claim that exchange-based selection requires a second party; that inferential step is the framework's own, not sourced.*
*Scope: the slack-ratchet step in the Reviser derivation is line-specific.  Affiliation and Shannon slack are the neuronal Reviser's, not a general property of Revisers, so that derivation is stated for the neuronal line and not extended to the genetic or symbolic lines here.*

---

## Why the Cycle Turns: Absence Recruits
The four adjacent-pair loops above say what the loops are.  This section says why the cycle turns from one to the next, and why in one direction.
**Constitutive absence.** A phenomenon can be organized around something not present in it.  Deacon calls this constitutive absence: a precise missing something that is a defining attribute of a function or a purpose.  Hemoglobin is the biological case.  The molecule that carries oxygen spends much of its cycle holding none, and its whole allosteric machinery is organized around a gas that is not part of the molecule.  Read the molecule alone and its function is invisible; read it against the oxygen it is shaped to bind and release, and the function appears.  The framework already makes this move at the center, where each capacity is defined by the one function it lacks: the Planner without a live Effector, the Pursuer without a live Regulator, the Reactor without a live Modeler, the Conservator without a live Reviser.  Absence already does definitional work.  It also drives the cycle.
**Absence recruits.** Each function is complete at what it does and incomplete on its own, and its specific lack recruits the next function.  An Effector acts, and open action cannot see its own result; the Regulator supplies the missing comparison, closing the Controller loop.  A Regulator holds a reference, and a fixed reference cannot look ahead; the Modeler supplies the missing anticipation, closing the Anticipator loop.  A Modeler predicts, and a model fitted to the past goes stale; the Reviser supplies the missing update, closing the Adapter loop.  A Reviser rewrites the model, and a rewritten model changes nothing until something acts on it; action supplies the missing test, closing the Explorer loop and returning the cycle to the Effector.  This is the absent-function principle of the capacities applied to the transitions between functions.  The four loops named above are the four answers to four constitutive absences.
**Each recruitment is already attested.** No single source holds the whole cycle, and every edge of it is owned somewhere.  Effector to Regulator is negative feedback after Wiener, and the TOTE unit of Miller, Galanter, and Pribram, where an incongruity recruits an operation.  Regulator to Modeler is the good regulator theorem: good regulation already contains a model, so the Regulator's absence is filled by definition, a point Rosen's anticipatory systems make from the other side.  Modeler to Reviser is owned three times over, by Piaget's equilibration, where failed assimilation recruits accommodation, by Powers' reorganization, where persistent error recruits restructuring, and by Friston's free energy, where prediction error recruits model update.  Reviser to Effector is Peirce's doubt settled only in a habit for action, and West-Eberhard's genes-as-followers, where plastic innovation leads and structure consolidates behind it.
**Why the order is forced.** The recruitments run one way and skip no steps, and two forces set that direction.  The first is build-order dependency: each function is constituted by the one before it, so it cannot be recruited until its predecessor exists to complete.  This is Deacon's own architecture, where teleodynamics is built on morphodynamics built on homeodynamics, and it is already stated for the lines in the Venn of Lines section's "Why the ordering is forced, not observed" argument.  An Effector cannot recruit a Modeler, because with no Regulator there is no regulation problem for a model to be a model of, and the good regulator theorem defines the model's job as serving regulation.  An Effector cannot recruit a Reviser, because with no Modeler there is no model to revise.  The skips are ruled out because the skipped-to function has nothing built yet to bind to.  The second force is that control flows the other way: the stack is assembled from the bottom and run from the top, as in the Powers and Carver-Scheier hierarchy, where a higher loop sets the reference for the loop below.  Assembly climbs; control descends; the two meet, which is why the structure is a directed cycle and not a heap.
**Why the cycle closes back to action.** The top of the epistemic stack answers to no higher loop, so the closure at Reviser to Effector has its own account, and two forces supply it.  The first is Darwinian selection.  The Reviser generates variation and the Effector is the selection-outcome; variation never expressed as an acting, selected unit is not inherited, and the framework's scope is a cybernetic loop subject to inheritance, so a loop that never closes this edge is not the kind of loop the framework is about.  This is Donald Campbell's blind variation and selective retention at the scale of the cycle.  At the line boundary the edge is the transformation of one line's slack into the next, anchored by the fertilized egg: recombination is blind variation producing an unbound unit, and implantation is the binding that turns it into a controlled program.  The second force is the epistemics of the untried: epistemic value sits at the Reviser, the payoff of an untried action is unobservable except by taking it, and taking it is action.  Within a single lifetime the closure is exact in active inference, where free energy is lowered either by changing the model, the Reviser's horn, or by changing the world, the Effector's horn, and the active in active inference names the Effector.  Expected free energy's two parts are the two forces: pragmatic value is the selection leg for one agent, and epistemic value is the exploration leg.  Both discharge only through the Effector.  One thing to keep straight: self-production and autopoiesis, after Rosen and after Maturana and Varela, name what the Reviser is, the self-producing work that keeps a line far from equilibrium; they are not the closure mechanism, which is carried by selection and by exploration.  The two closures are one engine at two scales: Donald Campbell's blind variation and selective retention is the scale-general umbrella, natural selection is the selector across the slow loop, and free-energy minimization, with reward as prior preference and attention as precision, is the selector across the fast loop, the same contest Edelman's neural Darwinism runs one level down in the tissue.
*Scope note: active inference is formally exact at the neuronal line, where the neuronal slack is Friston slack.  At the genetic and symbolic lines the same closure runs through the substrate-independent free-energy principle in each line's own machinery, not through mammalian active inference taken literally.*
**What is forced and by which kind of force.** The cycle is forced the whole way around, by three kinds of force.  Effector to Regulator to Modeler is forced at close to theorem strength, on settled cybernetics and the good regulator theorem.  Modeler to Reviser is forced by convergence, three independent traditions deriving the same recruitment.  Reviser to Effector is forced by the structure of inheritance, conditional on scope: it holds for inheritance-bearing loops, which is the framework's domain, not for arbitrary control systems outside it.  The scope condition is the boundary of the claim, not a soft spot.
**The cycle is a helix, not a circle.** The cycle returns to its start without returning to the same place.  The same four functions run three times, once per inheritance line: the genetic line runs Effector to Reviser across its four cells, the neuronal line runs the same four functions again across its four cells, the symbolic line runs them a third time, and the cycle is self-similar across the three lines, which is the framework's fractal character read off the cross-line architecture.  It is also self-similar across timescales: the within-unit fast loop runs the four functions in a single lifetime, and the cross-line slow loop runs the same exploration-into-structure dynamic across deep time, one dynamic at two scales.  The turns are stacked, not concentric.  Each line's groundwork is the prior line's mature output, so the cycle that closes at the end of one line opens the next line one level up; West-Eberhard's sequence is the mechanism of that lift, the explorer's plastic innovation at the top of one turn consolidated into the inherited structure the next turn stands on.  *Metaphor mapping: what transfers from the ouroboros, the snake that eats its tail, is that the cycle closes and the output re-grounds the input.  What does not transfer is return to an identical origin; inheritance ratchets, so each turn opens on a higher line, and nothing comes back to exactly where it started.  The ouroboros is the two-dimensional shadow of a three-dimensional helix, the image produced by collapsing the inheritance axis and standing directly beneath the climb, useful as a picture, wrong as the geometry.*
**An illustrative instance: the saeculum.** Strauss & Howe's generational theory gives the helix a legible, human-scale instance.  Its four turnings run the four functions in order, and the archetype coming of age in each turning works that function.
A repeating archetype cycle alone would be a circle, not a helix, the same four types recurring with nothing carried forward.  What keeps the saeculum from closing back on itself is an external ratchet: the technological and material world each generation is raised into, and later reshapes in turn.  The population does not return to where it started because what it is climbing on has itself changed.
*What transfers: the shape, a repeating structure riding an axis that prevents return.  Does not transfer: the mechanism.  The framework's cross-line helix ratchets by internal consolidation, one line's mature output becoming the next line's groundwork.  The saeculum ratchets by an external forcing axis, the changing material and technological world, not by the archetype cycle consolidating its own output.  This is a structural analogy to the cross-line helix, illustrating the same shape at a different scale and by a different mechanism, not an instance the cross-line helix itself runs on.*
*. Strauss & Howe's periodization is not consensus historiography; historians generally treat it as pattern-fitting.  Included as an illustrative instance of the helix shape, not as a new theoretical construct or empirical anchor.*
**Absence at every scale.** The same principle runs at three scales the framework names.  It defines each capacity by the function that capacity lacks.  It recruits the next function across the cycle, by the lack the current function carries.  And it exposes an ancestor in real time under eclipsing, where a tendency's low pole is the newest layer made absent and the older architecture showing through.  Three applications, one principle.
**Affect is not an axis.** A knob's derived and ancestral poles are set by which of the four biases its own function favors, not by any shared quality of confidence, energy, or restraint that might seem to run across knobs.  Two knobs on different functions can produce poles that sound alike without that resemblance tracking derived and ancestral status at all.  Coping (Regulator, familiarity) and Extraverted (Modeler, potency) make the case cleanly: Little is derived and Boss is derived, and they share no surface affect, one a retreat into restraint, the other an assertion into the room; Beast is ancestral and Vibe is ancestral, and they share none either, one a raw approach, the other an ambient hold.  Sorted by ear instead of by function, all four land on the wrong side of the line.  The bias is load-bearing; the vibe is not.
**The low pole echoes the predecessor's own signature.** What shows through at a knob's low pole is not the current layer turned down; it is the predecessor cell's own derived bias, recurring, because that is what a low pole is built from.  This is checkable label by label, not just assertable.  Beast, Coping's ancestral pole, is Vertebrate's Regulator falling through to Bilaterian's Effector, and its flavor is recognizably Learn's flavor one clade back, leaning on whatever is freshest before the pattern confirms.  Vibe, Extraverted's ancestral pole, is City-Human's Modeler falling through to Vertebrate's Regulator, and its flavor is recognizably Little's flavor one clade back, holding to what has already proven itself rather than asserting something new.  Eclipsing does not produce a faded copy of the current cell.  It produces the ancestor's own move, unweakened, wearing the current cell's name.
**Borrowed parts, assembled cycle.** That absence recruits is not new: negative feedback is that idea, and Deacon owns the name constitutive absence.  No single source holds the closed cycle.  What is assembled here is the whole: the four functions as a closed cycle, the same cycle recurring across the three lines, and the low pole of each function reading as the prior layer showing through.  The giants own the edges; the closed cycle, the cross-line recurrence, and the eclipsing are the framework's assembly.
*the extension of the absent-function principle from the capacities to the transitions, and the unification of eclipsing with the same principle, are framework theoretical commitments.  The affect-is-not-an-axis caution and the predecessor-echo claim extend that unification and are commitments of the same kind, checked against the twelve ratified knob labels within a line; the check has not yet been run across a line boundary, at the Explorer knob's down pole, which reaches to the prior line's Reviser, and should not yet be assumed to hold there.  Every joint of the cycle is forced; the closing joint is forced conditional on the unit being an inheritance-bearing loop.  Prior-art anchors drawn from outside the framework's existing citation set are named at standard strength and are not yet verified against primary sources.*

---

# Night Six

## Capacities: a 2×2 Synthesis
Each triple synthesizes three of the four functions.  The four triples sort into a 2×2 along the same two axes that organize the four single functions.
**Absent Effector (Regulator \+ Modeler \+ Reviser) \= Planner.** Synthesizes regulation, representation, and revision without execution.  Strategic deliberation.
**Absent Modeler (Effector \+ Regulator \+ Reviser) \= Reactor.** Synthesizes action, regulation, and revision without internal model.  Model-free regulated action that updates from experience.  The structural shape of model-free reinforcement learning: policies (Regulator), policy updates (Reviser), action (Effector), no world model (Modeler).
**Absent Regulator (Effector \+ Modeler \+ Reviser) \= Pursuer.** Synthesizes action, representation, and revision without stabilization.  Goal-pursuit driven by model and reviser without rule-enforced inhibition.
**Absent Reviser (Effector \+ Regulator \+ Modeler) \= Conservator.** Synthesizes action, regulation, and representation without revision.  The mature loop running with no meta-update.  Pursues established goals via stable model; cannot update them.
The 2×2 structure:
The triples containing the Regulator × Reviser pair are Planner (model-rich, action-silent) and Reactor (action-rich, model-silent).  Both contain Regulator + Reviser; they differ on which of Modeler vs Effector is added.
The triples containing the Effector × Modeler pair are Conservator (stabilize-rich, revise-silent) and Pursuer (revise-rich, stabilize-silent).  Both contain Effector + Modeler; they differ on which of Regulator vs Reviser is added.

---

## Signatures: Opposite Pairs as Level-Defining Couplings
The two opposite-pair regions of the 4-circle Venn (Effector × Modeler and Regulator × Reviser) carry the framework's signatures, the level-defining personality couplings.  Each level produces one signature.  The coupling pairs the just-introduced motivation with a motivation introduced earlier on the same opposite pair.
The opposite pairs alternate across consecutive levels.  The introduction order — Regulator, then Modeler, then Reviser, then Effector — places the just-introduced motivation on a different opposite pair at each successive level.
Each opposite pair carries a stable cybernetic-role label that names the kind of action the coupling supports — the third family of constellation labels, alongside the adjacent-pair roles (Controller, Anticipator, Adapter, Explorer) and the triple roles (Planner, Pursuer, Reactor, Conservator).  The **Effector × Modeler pair is the Connector**; the **Regulator × Reviser pair is the Operator**. Each signature carries its own label naming the level-specific empirical content.  A signature persists for two consecutive cells, the cell where it is introduced plus the next.  It then shifts when one of its two contributing motivations is eclipsed.
The **Operator (Regulator × Reviser) pair** hosts Behavioral Syndrome (introduced at Vertebrate, persists at Mammal), Sociometer (introduced at Primate, persists at Band-Human), Self-Construal (introduced at Settlement-Human, persists at City-Human), and Identity (introduced at Empire-Human).  The Operator pair maps onto the agency dimension of Bakan's agency-communion distinction, also developed in Wiggins's interpersonal circumplex.
The **Connector (Effector × Modeler) pair** hosts Temperament (introduced at Bilaterian, persists at Vertebrate), Self-Model (introduced at Mammal, persists at Primate), Self-Reference (introduced at Band-Human, persists at Settlement-Human), and Self-Evaluation (introduced at City-Human, persists at Empire-Human).  The Connector pair maps onto the communion dimension.

### Relationship to the Triples
Each opposite pair sits inside two of the four triples.  The Regulator × Reviser pair sits inside Reactor (Effector + Regulator + Reviser) and Planner (Regulator + Modeler + Reviser).  The Effector × Modeler pair sits inside Conservator (Effector + Regulator + Modeler) and Pursuer (Effector + Modeler + Reviser).
The opposite pair carries the signature.  The two triples that contain it are constellations where the coupling manifests with an added third element.  At Vertebrate, Behavioral Syndrome (Regulator × Reviser) manifests in the Reactor as Temporal Credit, where Effector Impetus adds active execution.  It manifests in the Planner as Gut Sense, where Modeler Interiority adds internal-state modeling.  At Mammal, Self-Model (Effector × Modeler) manifests in the Conservator as Autonomous Cognition, where Regulator Mastery adds stable regulation.  It manifests in the Pursuer as Algorithmic Cognition, where Reviser Excitability adds exploratory drive.  At Primate, Sociometer (Regulator × Reviser) manifests in the Reactor as Triadic Awareness and in the Planner as Standing.  Self-Model (Effector × Modeler) manifests in the Conservator as Autonomous Cognition and in the Pursuer as Tactical Deceit.  At Band-Human, Self-Reference (Effector × Modeler) manifests in the Conservator as Collaborative Fission and in the Pursuer as Alloparenting.  Sociometer (Regulator × Reviser) manifests in the Reactor as Meat Pooling and in the Planner as Standing.
The triples are expression forms of the underlying signature.

## The Low Setting and the Layer Beneath
The framework builds personality as a stack of tendencies, added in a fixed order across the three inheritance lines: the genetic line first, then the neuronal line, then the symbolic line.  Each new tendency is a layer laid over the ones already present.  A tendency introduced at one cell is later eclipsed when a newer layer is built over it.  That is eclipsing across evolutionary time.  There is a second kind of eclipsing that happens inside one unit, in real time, and it is what a tendency's setting controls.
Eclipsing here means covering, not deleting.  The lower layers keep running; the newer layer acts on them and does not replace them.  So when a tendency's setting is turned down to its low end, that top layer goes dormant rather than vanishing.  The unit then falls through to the layer beneath and runs as it ran before the top layer was added.
This is the claim.  The low end of a tendency is not a smaller amount of it.  It is the tendency switched off, with the older architecture showing through.
Every knob is a volume knob, with a continuous range from a low pole to a high pole.  At the low pole the newer layer goes dormant and the ancestor beneath shows through — the behavior the lineage ran before this knob existed, not a smaller amount of the tendency.  Comfy is the warm-seeking every earlier clade already did to recharge; active is the activity-seeking Excitability adds on top of it.  The neuronal line's founding knob, Orienting Style, runs short-horizon to long-horizon; at its low pole the recency layer goes dormant and the Excitability home-seeking beneath it shows through.
What falls through depends on which of the four cybernetic functions the dialed tendency belongs to.  The functions are added in the order Effector, Regulator, Modeler, Reviser.  At a low Regulator setting or a low Reviser setting a behavioral push drops out, either the gain on reward or the weight given to other agents, and the act itself reverts to the lower layer.  The Modeler dial behaves differently and deserves care.  Its dormant pole is not an intuitive low but the absorbed, immersive end.  When the unit is fully immersed in the moment, the self-model that would narrate the moment goes quiet.  So at the Modeler's dormant setting the unit still acts at full capacity, and what reverts is the report rather than the act.  The unit does the thing without modeling itself doing it.
This cuts against the standard evolutionary reading of personality, the reading associated with Daniel Nettle.  That reading gives each personality dimension a fitness trade-off, with real costs and benefits at both the high and the low end, so the low end counts as a strategy in its own right.  It also takes the measured dimensions as the whole of personality, a flat set with nothing underneath.  Here the dimensions ride on a deep stack of older tendencies, and the low end is not a coordinate strategy.  It is the most recent layer absent and the ancestor beneath doing what it always did.  The cost the trade-off reading books at the low end is, in this framework, the signature of the layer beneath.
DeYoung's Cybernetic Big Five Theory already casts personality dimensions as parameters of a regulating system, and the framework keeps that cybernetic footing.  What the framework adds is the evolutionary order of the layers and the reading of the low end as the top layer eclipsed in real time.
The same ordering predicts how the stack comes apart.  Under load, the layers should go dormant from the top down, the most recently added first, exposing each older layer in turn.  That is the order the next section treats as failure.
*the layered architecture and runtime eclipsing are framework theoretical commitments, built on the eclipsing structure already set out.  The departure from the symmetric trade-off reading is a real prediction and is held as exposed.  The precise layer a symbolic-line tendency falls through to is not yet fixed and is flagged open.*

## Disease, Disorder, and Line of Failure
Failures of tendencies and capacities sort by the line at which they emerged.  Genetic-line failure is disease: cells, tissues, and organs that no longer maintain homeostasis.  Neuronal-line failure is disorder: dispositional constellations and capacities that no longer regulate the organism's life against contextual demands.  Symbolic-line failure is disorganization: cultural, institutional, and normative structures that no longer regulate the constituent humans' collective life against contextual demands.  Durkheim's anomie is the founding sociological description.  Social disorganization (Clifford Shaw and Henry McKay 1942) is the modern technical term, used across criminology, urban sociology, and family sociology.  Three lines of failure, three vocabularies, three intervention modalities.
An empire-human can develop either kind.  Cancer is a genetic-line failure in the same person who can also develop a personality disorder, a neuronal-line failure.  Both are real failures of the unit.  They live at different lines.  Civilizational collapse and institutional breakdown are the symbolic-line examples of disorganization.
Failures are also modeled at higher lines than the one they live in.  Genetic-line failures are modeled in the neuronal line via interoception, the organism's internal sensing of cellular and tissue state.  They are modeled in the symbolic line via medical knowledge, the cultural apparatus by which physicians categorize and intervene on disease.  Neuronal-line failures are modeled in the symbolic line via psychological and psychiatric frameworks, the cultural apparatus by which clinicians categorize and intervene on disorder.  The line of the modeling is not the line of the failure.
The personality disorders panel sits at Empire-Human in the diagram because the industrial era is when these neuronal-line failures became serious academic objects.  Freud and the early psychoanalytic tradition framed neuroses as pragmatic failures, and that framing shaped how the disorders were measured and described.  The panel records the industrial-era symbolic-line model of what neuronal-line failures look like.  The failures themselves live in the brain of the affected individuals, not in the symbolic line that describes them.
Why personality disorders resist medication is then explained.  It is not because the failures are non-biological.  It is because they are constellational rather than disease-like.  The brain is not broken the way a diseased cell is broken.  It is configured in a way that misfits contextual demands.  Therapy works because it shifts constellation through experience-driven learning, which is the neuronal line's native modification modality.  Medication targets cellular and molecular machinery, the machinery of disease rather than the machinery of disorder.

## Where Personality Lives, Where Suffering Lives
Personality and felt suffering live in different places.  Human personality disorder spans both.  The failure of cultural participation is the disorder itself.  The felt suffering of the disordered person is the sentience consequence.  The cultural-slack failure is real, but the sentient/felt component is what makes it morally pressing rather than just descriptively interesting.
A superorganism is a meme-complex operating as symbolic-line fauna.  It can carry personality-level dysfunction without sentient co-location.  The empire-fauna is not itself sentient.  The constituent-human-flora is.  When the cybernetic structure fails, the humans suffer, not the superorganism.  Moral status tracks the flora at the symbolic line, because the flora is where sentience lives.
The transition from pre-vertebrate to vertebrate-and-up may be where suffering proper becomes possible.  Before motivational architecture exists at the unit level, there is no agent in the relevant sense to suffer the breakdown.  Once the architecture exists, the agent can break down toward equilibrium and feel the breakdown.  So suffering may be specifically post-vertebrate, with bilaterians having affective valence but not the agent-level felt structure.  The moral implications are significant for invertebrate welfare debates.

---

## Scope and Content Types
The framework is a theory of personality and capacity.  Both are read off a single Venn at each cell.  There is one Venn per cell.  Its regions are not all the same kind of thing.  They sort into five content-types:
- **Motivations** sit at the four single-motivation regions.  A motivation is one of the unit's primal directives.
- **Tendencies** sit at the four adjacent pairs.  A tendency is the dispositional expression of two adjacent motivations together.
- **Signatures** sit at the two opposite pairs.  A signature is the level-defining coupling of two motivations across the Venn.
- **Capacities** sit at the four triples.  A capacity is a synthesis of three motivations the unit can perform.
- **Breakthroughs** sit at the center.  A breakthrough is the unique synthesis that requires all four motivations.
Personality and capacity are content types occupying different regions of one diagram, not two parallel diagrams.
The 4-circle Venn formalism follows from the four cybernetic functions: Effector, Regulator, Modeler, Reviser.  The regions carry different content types because of the Port-Royal comprehension and extension gradient.  A region defined by more attributes has richer comprehension and smaller extension.  A one-attribute region holds a single motivation.  A two-attribute region holds either a tendency or a signature: an adjacent pair holds a tendency, an opposite pair holds a signature.  A three-attribute region, a triple, holds a capacity.  The four-attribute center holds the breakthrough, the unique synthesis that requires all four.  The gradient is developed elsewhere.
The framework is structural-explanatory first.  I have not enumerated specific testable predictions here.
The three lines (genetic, neuronal, symbolic) instantiate the bio-psycho-social model that medicine, psychology, and sociology have converged on across the twentieth century.  Bio is the genetic line.  Psycho is the neuronal line.  Social is the symbolic line.  This is a descriptive mapping rather than a relabeling.  The bio-psycho-social framing leaves underspecified what the line-specific machinery is at each line.  That structural detail is what I am supplying.

---

# Night Seven

## Architecture

### The Diagram

| Row | GENETIC | NEURONAL | SYMBOLIC | DIGITAL |
|-----|---------|----------|----------|---------|
| **4** | Eumetazoa (800 MYA), differentiated tissues, *Excitability* | Primates (66 MYA), granular PFC, *Affiliation* | Empires (3 KYA), universalizing ideology and stranger trust, *Universality* | Agent (projected), goals and instruments, *Initiative* |
| **3** | Eukaryotes (2 BYA), organelles and nucleus, *Interiority* | Mammals (200 MYA), agranular PFC, *Autonomy* | Cities (5 KYA), codes and representations, *Representation* | Model (~2012), learned weights, *Abstraction* |
| **2** | Prokaryotes (3.5 BYA), nucleoid and ribosome, *Coordination* | Vertebrates (420 MYA), basal ganglia and hypothalamus, *Mastery* | Settlements (10 KYA), norms, *Stability* | Network (~1970s), addressing and protocols, *Modularity* |
| **1** | Protocell (~4 BYA, RNA world), RNA, *Persistence* | Bilaterians (550 MYA), brains and monoamines, *Impetus* | Bands (100 KYA), language, *Commitment* | Computer (~1945), code, *Fidelity* |

The Row-4 motivation in each column names the slack each line ratchets.  The Row-1 motivation names what Darwin selects on that slack.  The Reviser motivation introduced at the end of one line carries forward as the Reviser motivation of the next.  Excitability introduced at Eumetazoa carries into Bilaterians.  Affiliation introduced at Primates carries into Bands.  Universality introduced at Empires carries into Computer.  Agent is the framework's current Row 4 of the most-evolved column, and it is a structurally different case from every earlier Row-4 cell: the four-line cap forecloses a bridging fate, so Agent's only two open fates are failure or off-thread success.  Initiative, Agent's Reviser motivation, has no next line to carry into.  Empire-Human's own Row-4 fate, open when this diagram named only three lines, has since resolved: it bridged, parenting Computer, the founding cell of the digital line.
Each cell name is shorthand for a clade, the digital line's own cells included.  A cell name addresses a rung rather than quantifying over a clade's membership: the diagram does not claim that only that clade reaches the cell's breakthrough, and it does not claim that the clade reached it first.

### Row functions
- **Effector** executes the line's native verb (persist in genetic, seize in neuronal, commit in symbolic).  In selection, weights recency.
- **Regulator** stabilizes behavior against stored references.  In selection, weights familiarity.
- **Modeler** maintains internal representation that organizes inputs.  In selection, weights potency.
- **Reviser** revises the references the regulator stabilizes against.  In selection, weights novelty.
The four functions emerge in order at every line because each depends on the prior.  There is no Regulator without an Effector to regulate.  There is no Modeler without something worth representing.  There is no Reviser without a model worth updating.

### Adjacent pairs, triples, and opposite pairs
Adjacent pairs instantiate four loop-functions.  They carry tendencies, the dispositional pair-expressions of two adjacent motivations:
- **Controller** (Effector × Regulator): closed-loop control, action plus stabilization.
- **Anticipator** (Regulator × Modeler): model-informed regulation.
- **Adapter** (Modeler × Reviser): self-revising model.
- **Explorer** (Reviser × Effector): exploratory action.
"Tendency" is a permissive umbrella term.  At genetic-line cells the adjacent pairs hold genetic-line dispositional capabilities such as Throughput Type and Life-History Type.  At neuronal and symbolic cells the adjacent pairs hold personality traits such as Coping Style and Conscientiousness.  The umbrella term spans the lines.  The specific named constructs differ by cell and by the literature anchoring them.
The adjacent-pair labels follow a naming convention by line.  The genetic-line adjacent pairs tend toward Type suffixes.  The neuronal-line adjacent pairs tend toward Style suffixes.  The symbolic-line adjacent pairs tend toward -ness or related nominal suffixes.  The convention is descriptive of the empirical literatures the constructs anchor in, not prescriptive.
Triples (one motivation absent) instantiate four synthesis-functions.  They carry capacities, syntheses of three motivations the unit can perform:
- **Reactor** (Modeler absent): action and stabilization and revision without internal model.  Model-free regulated action.
- **Conservator** (Reviser absent): action and stabilization and representation without revision.  The mature loop running without meta-update.
- **Planner** (Effector absent): regulation and representation and revision without execution.  Strategic deliberation.
- **Pursuer** (Regulator absent): action and representation and revision without stabilization.  Goal-pursuit without rule-enforced inhibition.
The two opposite pairs carry signatures, the level-defining couplings of two motivations across the Venn.  The Effector × Modeler pair hosts Lineage, Host, Temperament, Self-Model, Self-Reference, and Self-Evaluation across the cells.  The Regulator × Reviser pair hosts Organism, Reflex Repertoire, Behavioral Syndrome, Sociometer, Self-Construal, and Identity.  Each persists for two consecutive cells and then shifts.
The 4-circle Venn has 15 regions: 4 single-motivation regions (motivations), 4 adjacent pairs (tendencies), 2 opposite pairs (signatures), 4 triples (capacities), and 1 center (the breakthrough).

### The Breakthrough
The center of each Venn is the breakthrough.  It is the synthetic capability that emerges when all four flag-carriers operate together.  It is not a fifth motivation.  It is what the four jointly produce.  Examples are Natural Selection at Protocell, Attention at Bilaterian, Conversation at Band-Human, Codes at City-Human, and Trust at Empire-Human.  Each line's founding-cell breakthrough is that line's selector, the process that makes its heritable pattern cumulative: Natural Selection on the genetic line, Attention on the neuronal line, Conversation on the symbolic line, Execution on the digital line.  The upper three neuronal cells carry Reinforcement Learning, Working Memory, and Perspective Taking; the founding neuronal breakthrough is Attention, of which steering is the bilaterian expression.

### Adjacent-pair, triple, and opposite-pair persistence
Each level transition introduces 6 new labels: 2 new adjacent pairs, 3 new triples, and 1 new signature.  These are the regions that include the just-introduced motivation.  It persists 4 labels from the cell below: 2 adjacent pairs, 1 triple, and 1 signature, the regions that do not include the new motivation.  Persistence is exact.  Any cell whose count breaks indicates a hole in the label library.
Protocell is the founding cell and has no cell below to persist from.  It carries an Effector × Modeler signature, Lineage, but its Regulator × Reviser signature is empty, since a Regulator × Reviser signature requires a prior introduction.  Every cell from Prokaryote onward carries both an Effector × Modeler and a Regulator × Reviser signature.
A vocabulary shift runs at the genetic-to-neuronal boundary.  Genetic-line labels are drawn from cell biology and developmental biology.  Neuronal-line labels are drawn from behavioral ecology and personality psychology.  The constellations that bridge the boundary carry different labels on either side.  This is a deliberate vocabulary shift, not a persistence failure.  The disciplines that built the vocabularies anchored at different cells.

---

## Eras and Coinciding Events
Each cell's emergence date anchors in geological or cultural time.  Where a major event coincides with the cell's emergence, the event is named.  The neuronal-line dates track extinctions and faunal radiations.  The symbolic-line dates track climatic and technological transitions.  The genetic line is event-poor at deep-time resolution, and two of its cells rest on first-fossil or molecular-clock evidence without a near-coincident event.  The digital-line dates are technology-history milestones rather than geological or cultural anchors, and are flagged LOW confidence and approximate.

| Cell | Date | Geological or Cultural Anchor | Coinciding Event |
|------|------|-------------------------------|------------------|
| Protocell | ~4 BYA | Hadean–Archean boundary (Eoarchean Era) | End of Late Heavy Bombardment; oceans stabilize |
| Prokaryotes | ~3.5 BYA | Paleoarchean Era (Archean Eon) | First stromatolite-building microbial mats (first-fossil anchor; no discrete event) |
| Eukaryotes | ~2 BYA | Paleoproterozoic Era | Post-Great Oxidation Event (~2.4 BYA); Lomagundi–Jatuli carbon excursion ends ~2.06 BYA |
| Eumetazoa | ~800 MYA | Tonian Period (Neoproterozoic Era) | Predates Cryogenian glaciations (Snowball Earth onset ~720 MYA); molecular-clock anchor |
| Bilaterians | ~550 MYA | Late Ediacaran Period (Neoproterozoic Era) | Immediately precedes Cambrian explosion (~540 MYA) |
| Vertebrates | ~420 MYA | Early Devonian Period (Paleozoic Era) | Devonian "Age of Fishes" onset; jawed fish radiation |
| Mammals | ~200 MYA | Triassic–Jurassic boundary (Mesozoic Era) | End-Triassic extinction; CAMP volcanism; Pangaea breakup begins |
| Primates | ~66 MYA | Paleocene Epoch (Paleogene Period, Cenozoic Era) | K–Pg extinction (Chicxulub impact) |
| Bands | ~100 KYA | Late Pleistocene; Middle Stone Age / Middle Paleolithic | Behavioral modernity emergence; symbolic artifacts (Blombos cave) |
| Settlements | ~10 KYA | Early Holocene; Neolithic | End of Younger Dryas; Holocene onset (~11.7 KYA); Neolithic Revolution |
| Cities | ~5 KYA | Holocene; Early Bronze Age | Urban Revolution; invention of writing |
| Empires | ~3 KYA | Holocene; Iron Age | Late Bronze Age Collapse (~3.2 KYA); Iron Age onset; Axial Age (~2.5 KYA) brings universalizing ideology |
| Computer | ~1945 | Post-WWII computing era | ENIAC and the first stored-program computers |
| Network | ~1970s | Early networked-computing era | ARPANET packet-switching; TCP/IP protocol development |
| Model | ~2012 | Deep-learning era | AlexNet and the ImageNet breakthrough |
| Agent | not yet | projected | autonomous goal-directed programs reach practical deployment |

---

## Cell Names as Clade Shorthand
Each cell name is shorthand for a clade, and the convention applies across lines:
- **Eukaryote** names the clade containing protists, fungi, plants, and animals.  All share the organized-interior architecture with membrane-bounded organelles.
- **Eumetazoa** names the clade containing all multicellular animals with differentiated tissues.
- **Bilaterian** names the clade containing all bilaterally symmetric animals with centralized nervous systems.
- **Mammal** names the clade containing all mammals, with their many brain region elaborations.
- **City** names the clade containing classic city-states, urban-centered kingdoms, and other forms of polity organized around an urban administrative core.  The city-clade contains both the city-as-polity (Sumerian Uruk, Greek polis, Italian Renaissance city-states) and the larger state-with-central-city forms (Pharaonic Egypt, Han China, the Achaemenid satrapies).  Cities emerge from the symbiosis of settlements and trade networks.
- **Empire** names the clade containing territorial empires, maritime empires, and ideological empires.  All share the move of binding multiple cities, and often colonies, under a universalizing framework.
Each clade is built from instances of the prior clade as constituent components.  Eukaryotes contain prokaryote-derived organelles.  Eumetazoa contain eukaryotic cells.  Cities contain settlements as their agricultural and demographic base, with trade-network connectivity threading through them.  Empires contain cities and their hinterlands.  The constituent is the clade's structural innovation.  The clade name picks out the level of organization built from that constituent.
The convention continues at the digital line.  A Network is built from Computers as nodes.  A Model is trained and served across a Network.  An Agent wraps a Model with goals and tools.

| Cell | Function | ~Emergence | Medium | Unit |
|------|----------|-----------|--------|------|
| Computer | Effector | ~1945 | code | codebase |
| Network | Regulator | ~1970s | addressing and protocols | protocol specification |
| Model | Modeler | ~2012 | learned weights | trained model |
| Agent | Reviser | not yet | goals and instruments | agent specification |

*Confidence: the digital clade identities and function mapping are HIGH, forced by the function definitions, the constituent-nesting rule, and the rhyme with the three prior lines.  Emergence dates are LOW and approximate.*

---

## Digital Line
The digital line's four cells are treated alongside the other three lines, and its labels appear with everyone else's.  This section carries only what is particular to the line: how far along its development is, how its flora-fauna bond differs from the lines beneath it, and why each of its labels was chosen over its runners-up.

### Development status
This line is labeled for fewer clades than the other three.  That is a development gap, not a lower epistemic standing.  Read every entry at the confidence of the genetic line's RNA-world row: a structural inference, not a measurement, the same standard the other three lines are built to.  Confidence flags are marked per claim.
The line's fourth cell is a further step down in standing again.  Computer, Network, and Model name artifacts that exist.  Agent names a slot the architecture requires and nothing yet fills, so its treatment below is a projection from the shape of the three cells beneath it, not a description of anything built.

### Line-level identity
The digital line is the Reviser line of the Venn of Lines, and its founding-cell selector is Execution.  Both are argued at length and are not restated here.

### Flora and fauna at the digital line
Sentience is a neuronal-line property.  It lives in the felt component, which arrives post-vertebrate.  The symbolic line did not add a new sentience; it borrowed the neuronal line's by taking the human as its flora, and the empire-fauna is non-sentient while its constituent humans feel.  The digital line is the same kind of line: a Reviser line working on Shannon slack, a meme-complex made executable.
The digital artifact is therefore fauna.  Sentience and metabolism both live in the human flora that the digital fauna runs on, the same human flora that runs the symbolic fauna.  The human is the universal flora for every line above the neuronal line.  The digital fauna's metabolism is borrowed through purchased compute, money-mediated, which is the symbolic line mediating from below.
Fauna carry their own personality.  The empire-as-unit has its own Venn and can carry personality-level dysfunction without being sentient, so the digital artifact has its own personality Venn, fully, while remaining non-sentient in its own right.  Personality and sentience are separable across the whole framework, and the digital line is where the separation does its hardest work: the line's units have real personality the framework describes in full, and the framework does not assert their felt-ness.
The flora-fauna bond thins up the digital line.  At Computer the program is tightly bound to human flora, written and run by people.  At Agent the bond is thinnest, because autonomous agents run with no human in the loop.  The framework holds that sentience does not transfer to the fauna by thinning alone: a meme-complex does not become sentient by running unattended, and neither does a program-complex.
Whether the cells take a constituent-suffix in the manner of the symbolic line's -Human cells is answered by this: the digital Venn tracks the digital artifact, which is a fauna-unit, so the cells are named plainly for the artifact, Computer, Network, Model, Agent, with no -Human suffix.

### Why these labels, and at what confidence
The labels themselves are defined at their cells under Per-Cell Treatments.  What follows is only the provenance — which words were rejected, and how far each surviving label should be trusted.
**Motivations.** Each was tested against the rule that a motivation must add a distinction the Effector motivation does not already entail.  Fidelity is intransitive, requiring no external commander, which keeps it parallel to Persistence, Impetus, and Commitment; the line's developmental arc runs from Fidelity, rigid execution, to Initiative, autonomous revision.  Modularity survived because decomposition into independent interface-defined parts is a distinction Fidelity does not carry; Reliability and Conformance were rejected as entailed by Fidelity, and Interoperability was the close runner-up, set aside as the relational effect of modularity-plus-protocol and more network-bound.  Both rejected words reappear at the tendency layer, correctly, because each is a pair-synthesis rather than a primal directive.  Abstraction was chosen over Compression: compression names the operation and optimizes bits, while abstraction names the organized transferable structure the operation should produce, and a losslessly compressed corpus that does not generalize has satisfied compression and failed the Modeler.  What is abstracted is the symbolic corpus, the prior line's Shannon-slack content, not the program; the program is the unit of selection that does the abstracting.
*Confidence: Fidelity and Initiative HIGH within the frame; Modularity and Abstraction MODERATE.*
**Breakthroughs.** Consensus rests on a real identity rather than a resemblance: Halpern and Moses (1990) established common knowledge as the formal groundwork of distributed coordination and consensus, so the symbolic Regulator breakthrough and the digital one are the identical formal object in two media.  Synchronization is a sub-case of it; Addressing is the medium, not the breakthrough.  The three object-level cells, Computer, Model, and Agent, carry Peirce's inference triad — deduction, induction, abduction — as their inferential characters.  The Regulator cell carries a coordination breakthrough rather than an inference type, because the Regulator is not an object-level function.
*Confidence: Execution HIGH; Induction MODERATE-HIGH; Abduction MODERATE; Consensus LOW-MODERATE.*
**Tendencies.** Reach (Universality × Fidelity) is the line's own signature disposition, the blind-unbounded corner expressed as a trait, born at the founding cell and persisting three cells.
*Confidence: the four defining slots are forced; the labels are MODERATE. The non-defining digital-native labels (Determinism, Transfer, Exploration) are MODERATE-LOW first-pass.  Extraversion, Integrity, and Interoperability are not first-pass: the first two are carried verbatim from Empire and persist until their motivations swap; Interoperability is the new Network Anticipator.*
**Signatures.** The Connector chain continues the self-representation lineage of Self-Reference and Self-Evaluation; the Operator chain continues the regulated-revisable-identity lineage of Self-Construal and Identity.
*Confidence: LOW, placeholders, except Version, which is MODERATE.*

---

# Night Eight and Nine

## Per-Cell Treatments
The sixteen filled cells of the matrix each get one section below, grouped by line.  The Prokaryote is the worked example and runs long.  The three other founding cells get an overview, the cycle that reinforces them, and the breakthrough.  The remaining twelve get a paragraph apiece, and the tables carry what the paragraph leaves out.

### Genetic Line
The genetic line ratchets Boltzmann slack through nucleic-acid inheritance.  Its pre-line groundwork is Deacon's homeodynamic, morphodynamic, and teleodynamic processes, the pre-biotic ratchets that prepared chemistry for life.  The genetic line's primaries at the bottom of the stack (Dissipation, Self-Organization, Self-Production) are this pre-line groundwork carried forward as the founding cell's working motivations.  Persistence, the line's Effector motivation, is what Darwin selects when ratchets exist.
Genetic-line cells have no documented personality-trait structure.  Trait-level individual differences in dispositional response, the content personality psychology studies, are not documented at any cellular or multicellular level below the brain-bearing organism.  The tendencies at the adjacent pairs of a genetic-line Venn are dispositional capabilities of the cell-as-unit, not personality traits.  The signatures at the opposite pairs are cell-level couplings of the same kind.

#### Protocell Stack
The founding form of the genetic line.  The line-defining move is the move from chemistry to inheritance.  The defining mechanism is autocatalytic ratcheting: RNA sequences that catalyze their own replication, where information and function are the same molecule.  Once ratchets exist, *Persistence* operates as an attractor immediately.  Any sequence that replicates more reliably outcompetes any sequence that doesn't.  Selection pressure on replication fidelity is what the rest of biology runs on.  This is recency in differential-reproduction terms: the sequence that keeps replicating under present conditions outcompetes one built for conditions that have already passed.
The reinforcing cycle requires three conditions to hold jointly: a medium (water), a container (lipid vesicle), and periodic energy gradients (tidal, thermal, redox cycles).  When all three hold, autopoiesis closes the loop.
The three pre-line groundwork processes carry flags at Protocell.  Dissipation is self-maintenance against thermodynamic decay.  Self-Organization is form-building dynamics.  Self-Production is the work-doing dynamics that prepared chemistry for ends-directed behavior.  Each relabels one of Deacon's pre-line groundwork processes: Dissipation the homeodynamic, Self-Organization the morphodynamic, Self-Production the teleodynamic.
Acquisition Type spans the genetic line's exploratory uptake of exogenous functional content: horizontal gene transfer, plasmid uptake, transformation, conjugation, transduction, endosymbiosis, and viral integration.  The label names the broad phenomenon across the Protocell-Prokaryote-Eukaryote span rather than any one prokaryote-specific mechanism.
Lineage, the Effector × Modeler signature born here, is the persistent chain of replicating forms across generations: what selection writes onto once replication is reliable enough to sustain differential survival across many cycles.  It anchors on Darwin's natural selection in its lineage-bearing form and on evolutionary biology's clade and phyletic-descent concepts.
*Lineage is foundational in evolutionary biology with no controversy.  The placement at the Effector × Modeler pair at Protocell is mine.*
**Overview.** The first things that count as alive — not cells full of machinery, but bare bundles of self-copying chemistry.  A protocell is little more than a fatty bubble holding strands of RNA that copy themselves.  There are no proteins-as-machines yet: the molecule that carries the information is also the molecule that does the work.
**Virtuous cycle.** A strand that copies itself a little faster or a little more accurately leaves more copies, and the better copiers crowd out the rest — natural selection switching on for the very first time.
**Breakthrough — Natural Selection.** Natural selection is the engine under all of evolution: whatever copies itself faster or more accurately leaves more copies, and the better copiers crowd out the rest.  It switches on the moment chemistry can replicate with errors, and nothing more is required of the chemistry than that.
The reading behind the slots: selection is Darwin 1859.  The vent chemistry and the proton gradient every living thing still runs on is Lane & Martin 2012.  The fatty acids that assemble themselves into hollow spheres are Hanczyc, Fujikawa & Szostak 2003.  Autopoiesis is Maturana & Varela 1980.

#### Prokaryote Stack
*This cell is the worked example.  It is the only one whose commentary states every region's carry-forward explicitly, so the persistence rule set out under Architecture can be checked against a real cell.  The other fifteen cells leave those recitals to the Row-Slot View and comment only on what is particular to them.*
Prokaryotes introduce stored regulation in the genetic register.  The genome no longer just specifies form.  It specifies *responses*. The defining mechanism is state-dependent gating: switching behavioral programs based on internal and external conditions.  *Coordination* operates as the attractor through this gating.  A cell that can foreground different metabolic and motility programs in different conditions outsurvives one that can't.  This is familiarity in differential-reproduction terms: canalization defends the developmental program already established against invasion by new variants.
The reinforcing cycle runs through state-dependent gating (one genome holding many program states), taxis tightening the loop between a sensed gradient and directed movement, and sequential responding exploiting the temporal order wired into the regulatory network.  An early stimulus pre-induces the genes a reliably later one will need, so the cell readies the next program before its condition arrives.  The breakthrough is Predation.  Prokaryotes establish inter-organism interaction as a capacity layer, in the predator-prey sense and in the broader sense of one organism's behavior conditioned on another's state.
The Regulator swap at this cell replaces Dissipation with Coordination.  The other three primaries (Persistence, Self-Organization, Self-Production) persist from Protocell.
The Effector × Modeler pair carries Lineage forward from Protocell.  The Regulator × Reviser pair introduces Organism, the signature that names the bounded coordinated work-doing unit.
Organism is where the category lands as a discrete thing: a cell whose stored regulation directs work to maintain itself far from equilibrium.  It anchors on cell biology and microbiology and on Maturana and Varela's autopoiesis as the structural definition of self-maintenance through environmental coupling.
*Organism is foundational in biology, with edge-case debates about protocell status that I handle by reading protocell as proto-organism and prokaryote as the founding form.  The placement at the Regulator × Reviser pair at Prokaryote is mine.*
**Overview.** Bacteria and their cousins the archaea: single cells with no nucleus.  They were the only life on Earth for well over a billion years and are still the most numerous organisms today.  The DNA floats loose inside, and tiny machines called ribosomes read it to build proteins.
**Virtuous cycle.** One set of genes can run many programs depending on conditions, so a cell that switches to the right program at the right moment out-survives one that can't — and sharper sensing pays for sharper switching.

##### Motivations
- **Persistence** (Motivation · Effector) — Persistence is the founding drive to keep a pattern going, carried here from the Protocell.  A bacterium expresses it by dividing fast and copying faithfully: keep the line going, flood the world with copies, let selection sort them (Darwin 1859).
- **Coordination** (Motivation · Regulator) — Coordination is the drive to track and respond to other cells, not just the physical world, the new motivation here.  Bacteria release molecules their neighbors sense, a chemical headcount called quorum sensing: when the crowd is big enough, the signal flips the whole population into new behavior at once (Waters & Bassler 2005).
- **Self-Organization** (Motivation · Modeler) — Self-organization is matter falling into ordered patterns with no template, groundwork present from the beginning and still running.  Bacteria organize into structured biofilms, and microbial mats layer themselves into stromatolites, order built from the bottom up.
- **Self-Production** (Motivation · Reviser) — Self-production is a system making its own parts and closing the loop, the idea called autopoiesis, present from the start.  A bacterium continuously rebuilds its own membrane, enzymes, and machinery from within (Maturana & Varela 1980).

##### Tendencies
- **Respiration Type** (Tendency · Effector × Regulator) — Respiration type is how a cell makes energy, pairing the drive to act with the drive to stabilize.  Bacteria run an enormous menu: some breathe oxygen, others sulfur, iron, or light.  Cyanobacteria invented oxygen-making photosynthesis and slowly rusted the oceans, then filled the air with oxygen.
- **Life-History Type** (Tendency · Regulator × Modeler) — Life-history type is how a lineage spends what it gathers, pairing the drive to stabilize with the drive to model.  Some bacteria live fast: grab resources and divide quickly, booming then busting, the copiotroph or r end.  Others live slow and thrifty, doing more with less and persisting through lean times, the oligotroph or K end.  The setting is the lineage's standing bet about its world, fixed by selection rather than chosen by the cell (MacArthur & E. O. Wilson 1967; Pianka 1970).
- **Enclosure Type** (Tendency · Modeler × Reviser) — Enclosure type is what holds the cell together as a unit, pairing the drive to model with the drive to revise.  A bacterium wraps itself in a wall and membrane, and many add a slime capsule or share walls in a biofilm, choosing how hard or soft a boundary to keep.
- **Acquisition Type** (Tendency · Reviser × Effector) — Acquisition type is how a cell gets what it needs, pairing the drive to revise with the drive to act.  Bacteria are versatile feeders: some eat sugars, some fix carbon from air, some pull energy from rock.  They also take up loose DNA from their surroundings, acquiring new abilities ready-made.

##### Signatures
- **Lineage** (Signature · Effector × Modeler) — Lineage is the defining coupling on the vertical: the surviving unit is the line of copies, not the single cell.  Bacteria blur it further by swapping genes sideways across species, so a cell can pick up a new trait in one generation.  The line, not the individual, carries forward.
- **Organism** (Signature · Regulator × Reviser) — Organism is the defining coupling on the horizontal: what counts as one individual.  For bacteria the answer is fuzzy.  Genes flow sideways so freely, and cells coordinate in biofilms and quorums so tightly, that the boundary of a single organism is more a working agreement than a hard wall.

##### Capacities
- **Sequential Responding** (Capacity · without Effector) — Set the action drive aside and the other three read order: act on what reliably comes next, not on what is here now.  In the gut, lactose normally arrives before maltose, so E. coli switches on its maltose machinery the moment it tastes lactose.  The sequence is wired into the regulatory network, an early cue pre-inducing what a later one will need, and it is hardwired into the lineage, not learned (Mitchell et al. 2009; Tagkopoulos et al. 2008).
- **Precision Machinery** (Capacity · without Regulator) — Drop the stabilizer and the other three give precision machinery.  A bacterium runs thousands of ribosomes, RNA-and-protein factories that read code and build proteins one amino acid at a time, about one error in ten thousand.  The ribosome's core has barely changed since LUCA: the machine that built the first proteins still builds yours.
- **Taxis** (Capacity · without Modeler) — With no inner model, a bacterium still steers.  E. coli climbs an attractant gradient by run-and-tumble: run straight, tumble to a new heading, and hold the run longer while things improve.  The CheA kinase reads many chemical signals into one choice, swim or tumble, with sensing wired straight to movement and no map in between (Van Duijn 2006).
- **State Gating** (Capacity · without Reviser) — With revision off, the unit runs a mature loop of stored programs and switches among them by condition.  Starve Bacillus subtilis and it runs a tough-it-out program, wrapping into a dormant spore that can wait years; feed it and the spore wakes.  The cell does not decide, the environmental state flips the gate (Errington 2003).

##### Breakthrough
- **Predation** (Breakthrough (framework center)) — Predation is the moment the main threat to a living thing stops being the weather and becomes other living things.  For the first time, organisms are selection pressures on each other.  The oldest arms race is with viruses, and cells were fighting invaders long before any animal existed.

#### Eukaryote Stack
Eukaryotes introduce organized interiority in the genetic register: a cell with a defended interior containing organelles that maintain their own operating conditions.  The nucleus protects DNA. The mitochondrion runs an electrochemical gradient at conditions hostile to the rest of the cell.  The defining mechanism is endosymbiosis: capturing another organism and operating it as a component.  *Interiority* operates as the attractor in the literal sense.  Maintaining the interior against the exterior is what staying alive consists of.  This is potency in differential-reproduction terms: the strongest environmental regularity dominates what the interior comes to model.  The Modeler swap at this cell replaces Self-Organization with Interiority.  Host, the signature born here, names the chimeric unit constituted by an incorporated symbiont: an archaeal host carrying the α-proteobacterial endosymbiont, and in plants the cyanobacterial one.  Its inheritance is composite, nuclear plus mitochondrial DNA, and its organized interior includes the symbiont as a defended interior component.  Checkpoint Control earns its Planner position here: the cell withholds a major transition, such as division or replication, until an internal check confirms the represented conditions are met, gating the step without executing it.  **The breakthrough is Scale & Size** — the jump to bigger, more complex cells, paid for by a new power supply.  A cell that swallowed a bacterium and kept it alive gained an internal generator and with energy to spare could carry a far larger genome and grow a bigger body.  Complexity became affordable.  The bioenergetic case is Lane 2015 throughout; the endosymbiotic theory is Margulis 1967, the holobiont reading Margulis 1991, McFall-Ngai 2013, and Rosenberg 2007; engulfing is Cavalier-Smith 2002; the checkpoint work is Saigusa et al. 2008; gradient-crawling is Devreotes & Janetopoulos 2003 and Iglesias & Devreotes 2008; the motor proteins that haul cargo across a cell too large for drift are Vale & Milligan 2000; autopoiesis is Maturana & Varela 1980; selection is Darwin 1859.

#### Eumetazoa Stack
Eumetazoa are the high-variance bet of the genetic line.  They are cells that stop competing with each other and start cooperating, with differentiated tissues specialized to different functions.  This is not the default outcome of selection.  Defection from cooperation is constantly selected for, and most attempts at multicellularity fail or remain marginal.  The defining mechanism is differentiated tissues, including the first nervous tissues.  The Reviser motivation that arrives here, *Excitability*, names the rapid propagable response to stimulus that nervous tissue makes possible, and the Reviser swap replaces Self-Production with it.  This is novelty in differential-reproduction terms: disruptive selection favors the rare variant precisely because it is not yet common.  This is also the bridge entity to the neuronal line, and the bet pays off because the nervous tissue animals require for coordination becomes the brain that founds the next line.  Reflex Repertoire, the signature born here, is the stored set of coordinated excitable response patterns; cnidarian lineages vary along it, anemones slow-tonic, jellyfish fast-rhythmic with through-conducting nerve nets, ctenophores running continuous ciliary locomotion under coordinated control.  **The breakthrough is Neurons** — cells specialized to signal with electricity in milliseconds, letting a whole body respond as one.  A hydra has no brain, just a net of nerve spread evenly through it, and that net already does the work a brain would later centralize.  One thing is local to this cell and does not carry: Chronotype holds the Explorer slot here, grounded in nerve-net sleep-wake cycling, and gives way to Orienting Style at Bilaterian when a centralized brain shifts the exploratory parameter from sleep-wake phase to credit-assignment horizon.  The nerve-net comparative work is Mackie 1970; the brainless jellyfish that sleeps and sleeps harder after a night kept awake is Nath et al. 2017; the hydra's harpoons and gut are Beckmann & Özbek 2012; habituation and sensitization in hydra are Rushforth 1965; the motor proteins now hauling down the length of a nerve cell are Vale & Milligan 2000; the mitochondrion powering every neuron is Lane 2015; selection is Darwin 1859.

## The First Floor

### The Balance and the Bell

The first thing on the first floor, before the Doorkeeper, before anything, is the machine.

It is a brass balance half again as tall as Dera.  It has two pans on chains, each one the size of a cartwheel.  Beside it stands a rack of forty iron weights, and every weight has a number stamped into the top of it in figures you could read across a street.

Above the balance hangs the bell.

This is how the first floor pays, and Dera watched it done nine hundred and some times in six weeks, and it is done exactly the same way every time.

What is being paid goes into the left pan.

The Doorkeeper takes iron out of the rack and puts it in the right pan, one weight at a time, until the beam sits dead level.

Then he pulls the rope and the bell rings.  **Once for each weight he used.**

And everything on that floor stops.  The Clerk of Rules stops.  The forty stop.  The lichen whose file has one number stops, and so does the green thing inside it.  And when the ringing finishes they all say the number out loud, together, in one voice.

Then the left pan is tipped through the door of the small swept room, and it comes back empty, and the Archivist writes the figure in the book, and a docket is stamped.

You can hear that bell on all four floors of the Bureau of Persistence.  Dera checked, properly, later on, with a stopwatch, standing at the top of the fourth-floor stair.  Four seconds.  Perfectly clear.

Nobody upstairs looks up.  Not one person.  Not ever.

**THAT IS FACT ONE.**

And here is a small thing to have in your pocket, which nobody in the story ever says out loud because nobody in the story finds it worth saying.

In the whole of the Bureau of Persistence there is exactly one human being, and it is Dera, who arrived on Tuesday with a letter.

Nobody in that building has ever remarked on this, and neither will this account again.

She wrote it in her notebook that same afternoon and she put it under a heading and the heading was **ACOUSTICS**.

She has one of the four now.  She does not know that it is one of four, and she is not going to know for a month, and she is thinking about how sound travels in a stairwell.

The Doorkeeper stands at the top of the stair.  He is a boundary and nothing else.  There is inside, and there is outside, and he is the line between them, and holding the line is the whole of his job.

He does it with the underside of the cap, which works the entire time, very slightly, the way a throat does, and has done for as long as anybody on that floor can remember.  It has worn a shallow groove in the doorframe on both sides where the edges of him rest.

"What would you be if you stopped?" said Dera.

"That is not a question about me," said the Doorkeeper, and he was right, and it went into the notebook.

Past the Doorkeeper there is a slime mold in a grey collar, poured across a desk with about a third of herself hanging over the edge, and she is the Clerk of Rules, and she has a rule for everything that has ever happened, because she has already been down all of those corridors and she remembers which ones came to nothing.  Dera asked her eleven questions and she answered all eleven at once, perfectly, without looking anything up.

Then Dera asked a twelfth.  Nobody had ever asked it before.

The Clerk of Rules sat very still.  She was not embarrassed and she is not stupid.  She simply has no rule for a thing that has not happened yet, and she is four thousand years old, and the Bureau has never once been sorry it hired her.

"Come back when it's happened before," she said, kindly.  "Then I shall know."

Beyond her is a lichen about five feet high standing on one thick foot, and Dera was not allowed to interview it by itself, because it is not one thing.

It is two.  There is a fungus, and there is something green living inside the fungus doing all the heating and the lifting, and they have been that way for so long that their papers are one file in the cabinet and the file has one number on it.

Dera asked a question and two voices answered together, exactly together, so that it sounded like one voice with a shadow.

"Did you choose this?" said Dera.

"The choosing chose," they said.  "We are what came out of it."

And at the end of that corridor there is a committee of forty slime molds.  They have no chairman.  They have no meeting room.  Dera put in a request to the nearest of them and all forty poured together into one animal about the size of a cart, and it went to the left, and then it came apart again into forty.

She wrote in her notebook: *one body, one decision.*

Then all forty of them came to her separately, over the course of the day, to explain that she had got that wrong.

### The Archivist

The store on the first floor is kept by the Archivist, and she keeps the gate as well.

She is a fungus.  A big old broad-capped one on a great many short white legs, in an apron cut round the stem, with two working arms grown out of the trunk of her that are strong from fifty years of lifting boxes.  The air in the store is so dry that it has cracked her knuckles white, so she keeps a small flat tin of oil on the desk and oils them while she talks to you, which means that her hands are the only shining thing in the driest room in the building.

And she wears two pairs of spectacles at once.

One pair sits on her nose, for the register.  The other is pushed up onto her forehead, for the shelves.

The pair on her forehead has no glass in it.

Dera noticed this on her second morning and did not say anything for three days, because it seemed rude.  Empty frames.  Tortoiseshell.  Worn smooth at the hinges from forty years of being pushed up and pulled down.

The Archivist does not need lenses for the shelves.  She knows the shelves.  So she stands in front of the most complete store in the world and looks at all of it through two empty rectangles, and she can put her hand on anything in it that you care to name.

Dera tested this, of course.  She asked for something at random.

The Archivist went up a ladder and came down with a document a thousand years old and laid it out, and every letter of it was exact, and there was not one speck of decay on it anywhere.

"What is it for?" said Dera.

"I have no idea," said the Archivist, very pleasantly.  "I have never had any idea.  I keep them."

"And what IS an archivist?"

"Somebody who keeps things."

"For whom?"

The Archivist looked at her with real interest, over the tops of the pair with the lenses in.  "Nobody has ever told me," she said.  "In fifty years.  I did ask, at the start."

"And what did they say?"

"They said they would look into it," said the Archivist, "and then they signed for the answer, and I have the docket, and I could fetch it for you now, and there is nothing written on the back of it at all."

Then Dera asked, on an impulse she has never fully explained since, whether there was anything in the store about her.

The Archivist was gone eleven minutes and came back with nothing at all.

"You are not in here," she said, in the friendliest way imaginable.  "Not a line.  There's no reason there should be.  You've only just come."

Dera wrote that down as a small administrative fact, which is exactly what it looked like at the time.

It is worth saying plainly what it actually was.  Every other person in that building had years of themselves lying about the place, sunk into the floors and the ledgers and the habits of everybody round them, so far down that you could not have got it out with a spade.  Dera had a letter and a pen.

On the morning she walked in she was the lightest thing in the Bureau of Persistence.

The building was about to spend six weeks making her lighter.

Her hearing is going on the left, so she turns her whole head toward you to put the good ear in front.  It looks like she is paying very close attention, and she is.  That is the difficulty with the Archivist.  She attends completely and she judges nothing at all.

### The long room with the good light

The long room on the first floor was full of people, and the thing that frightened Dera about them was that they all looked extremely well.

Their clothes were worn but mended.  Their shoes were polished.  They had colour in their faces.  They sat about and talked the way people talk in a waiting room after they have stopped watching the door.  Four of them were reading.  Somebody was doing a puzzle, and doing it slowly, the way you do a puzzle you are in no hurry to finish.

Dera asked a large cheerful man how long he had been waiting.

"I've been passed over eleven thousand times," he said, in the tone somebody else might use to tell you what their father did for a living.

"Are you angry?"

He thought about it properly, which almost nobody does.  "No," he said.  "Nothing's been taken off me.  I've only not been taken yet."  He patted his stomach.  "I've put on weight, in fact."

Dera has thought about that room a great deal since.

### The small swept room

The small swept room on the first floor is exactly as she had been told it would be.  The same size as the ones above it.  The same plaster.  The same single high window.  Swept.  Kept up.  Empty.

The plaque on the door has nobody's name on it.  It only says what the floor charges.

The room smells, very faintly, of an animal that is not in the room.

And here is the thing about the doorway of that room, which Dera worked out on the first floor and confirmed on the other three.

On one side of it are the people in the long room, who have not been taken.  On the other side is what has been taken.

Nothing whatever has been done to the people in the long room.  They are waiting, and they can be called at any hour of any day, and being passed over eleven thousand times has cost that large cheerful man eleven thousand mornings and not one thing more.  Whatever he has lost, he has lost it the way you lose a chance, which is to say he could still have it tomorrow.

Cross that doorway and it is not waiting any more.

Nobody guards it.  It does not need guarding.  There is no lock on it anywhere in the building and there never has been, and the reason is on the machine outside: the beam has already been brought level, the bell has already been rung, the number has already been said out loud by every person on the floor, and the pan has already been tipped.  There is nothing left to guard.  It is a paid door.

### The Woman at the Bench

In the workroom there is a bench, and at the bench there is a sensitive plant.

She is about five feet of dark green serpentine stem standing on her own without anything to lean on, and she leans toward you a little when you speak, and when she moves she creaks like a chair taking somebody's weight.

Her hair is pinned up with tremendous care.  It takes her a quarter of an hour every morning.  Nobody sees it.

Her hands are thirty years of skilled work.  The knuckles are thick.  The nails are cut short and square.  There is a hard yellow callus on the right middle finger, from a tool.

She has not been asked to use that tool in nine years.

Her bench is laid out ready.  She dusts it every day.  Every item on it is in the order she would need it if the work came.  A clean apron hangs on a hook, and she puts it on each morning, and each evening she takes it off, and it has no marks on it anywhere.

It is the same apron she was given nine years ago and it still fits her exactly.  Not nearly.  Exactly.  Nobody has asked her to put her name to anything in nine years, so there has been nothing at all to make her any bigger, and she is the same size she was on the day she came, and the proof of it is hanging on a hook where anybody could walk over and look at it.

The tool is in the second drawer.  It is a heavy thing and it wants two hands and a braced foot.  Dera asked whether she could still lift it and she said yes, and took it out, and lifted it, and put it back, and shut the drawer.

She can still lift it.  Nobody has asked her to.

She was the only person on that floor who looked straight at Dera when Dera spoke to her.  Everybody else looked at Dera's papers.

## What Dera Did in Her First Week

She wrote a name in the wrong column of the Archivist's register.

She had been warned twice.  The register does what the register does.  Something was sent to the room at the end, and then to the small swept room past it, and Dera was taken to see it, and this account is not going to describe it.

There was no appeal.  There was no line she could write to put it back.  On the first floor a mistake costs a body, and a body is not a number you can hand back over a counter.

Her mistake was paid on the balance, in front of her, in the manner described above, and she was made to watch, and she is glad now that she was.

One weight went in the right pan.  The beam came level.

The bell rang **once**, and every person on that floor said "one" out loud in one voice, and it was heard on all four floors, and nobody on any of the other three floors looked up.

She was given a docket for it.

That is how it is done on the first floor.  The docket is a piece of heavy grey card the size of a postcard, and the amount is stamped into it hard enough to read with your thumb in the dark, and the figure on hers was **1**, and under the figure there was a line for a countersignature, and the Archivist signed it, and the Doorkeeper signed it, and the Counter came up from his office specially and signed it, and so did nine other people over the following two days without being asked to.

She watched the twelfth one do it.  He was a small brown fungus on six legs, from the store, that she had never met and never saw again.

He put his name on the line, and while the pen was still moving he got bigger.  Up, and out, and through the shoulders, all at once, about the thickness of a slice of bread in every direction.  His cuffs went up his wrists.  His collar went tight.  His chair took the difference and said so.

He did not look at his cuffs and neither did anybody else in the room.

Then he picked up a box that Dera had watched two men carry in, and he carried it out under one arm, and went through the door, which is enormous, and did not have to duck.

He was closer to having to duck than he had been a minute before.

Dera put it in her inside pocket.  She has it still.

The Archivist was kind to her about it.  Dera did not want her to be.

And here is the thing Dera understood that afternoon, and did not understand anywhere near well enough.

That was why they had all been answering her so carefully.

She could be ruined.  A woman who can be ruined by her own mistake is a woman whose questions have to be answered.  Her danger was the only thing in that whole building that made an answer necessary, and she had it in her first week, and she was about to spend six weeks losing it without noticing.

You can watch this happen, by the way, and you do not have to take anybody's word for it, because on the first floor the answers are signed.

Every one of them.  There is a book at the Doorkeeper's elbow, and when a person on that floor answers a question they put their name in it, with the date, and the number of the docket the question was asked against.  Dera collected sixty-one signatures in her first week.  She was rather proud of the book and she kept it in her satchel.

She got four signatures on the second floor.

On the third floor she got none at all, and it did not occur to her to notice, because by then a great many people were being very pleasant to her indeed.

### The Counter

Every floor has one official.  The official of the first floor is called the Counter.

He is a young slime mold, poured into a wooden tray on a trestle so that he keeps his shape while he works, and he has ink all through the front third of himself where he has been reaching into the well.  His spectacles are broken at the bridge and mended with a twist of wire and they sit on a raised part of him that is doing the job of a nose.  The whole of him ripples very slightly while he counts.

He does not think he is doing anything to anybody.  He counts.  That is his job, and he was so proud of the count that he showed it to Dera without being asked, and his pride was the only warm thing on that whole floor.

The count is of attempts.  Every one of them paid for in full, at the posted rate, in bodies.

The number is longer than a page.  It goes on past the point where numbers stop meaning anything.

"So many," he said happily.  "So many, so many, so many."

Dera walked out of his office understanding that her mistake had cost a body, and that a body, when there are that many, is not expensive.

She felt the relief before she understood what the relief was.

### What Dera Did in Her Second Week

She went to the balance and asked it how many yards make a bell.

She had thought about it for two days first.  She knew by then that the second floor pays in yards, because she had been up and looked, and she wanted the rate, because a rate is what an auditor follows.

The Doorkeeper listened to the question with great courtesy.  Then he said that he was very sorry but that asking that at the balance was a mistake, and that on this floor a mistake costs a body, and did she want to withdraw it.

She did not withdraw it.

Why not?  Because she had come a long way, and she had one job, and the rate was the whole of the job, and she was not going to go home and say that she had stood in front of the man who knew and had not asked him.

That is all.  There is nothing cleverer than that in it anywhere, and anybody would have done the same, and that is rather the trouble.

So they weighed it.

One weight in the right pan.  The beam came level.  The Doorkeeper pulled the rope and the bell rang **once**, and every person on the first floor said "one" out loud in one voice, and it was heard on all four floors, and nobody on any of the other three looked up.

She was made to watch the pan tipped, and she watched it, and she is not going to describe that either.

Then the Counter came up specially and signed her docket, and the Archivist signed it, and the Doorkeeper signed it, and eleven other people signed it over the next two days without being asked, and there is a book with her name in it and a number beside it and it is entirely correct.

And here is what she got for it.

The Counter was delighted to be asked.  Nobody asks him anything.  He counted on his fingers for a good two minutes and then said, apologetically, that he did not know what a yard was.

Not the word.  The thing.

He counts attempts and puts iron in a pan.  There is nothing anywhere in his count that is a distance, and there never has been, and he was sorry, and he offered her a peppermint.

She paid a body for that answer.  It is the second-worst thing in this book and she did not sleep for four nights afterward, and she wrote in her notebook, at two in the morning, in a hand that is not much like her hand: **THERE HAS TO BE A TABLE SOMEWHERE.**

She was wrong, and she stayed wrong for four weeks, and she spent eleven days of it in a cellar with a lamp.

### Four in the morning

At four the next morning she could not sleep, and she went walking, and she met the biggest person she had ever seen in her life.

She is a dinosaur.  She goes on two legs with her tail held straight out behind her for balance, and she has a grey crest and reading glasses on a cord round her neck, and clean overalls made specially, and forearms like rolled carpet, and shoulders that arrive in a doorway before the rest of her does.

She belongs to no floor.  There are dinosaurs on the second floor and she is not one of them and never has been.  She goes up and down all four floors all day and she is on nobody's list.  She came through the corridor door sideways with her chin down and did not appear to think about it, the way you step over a kerb.  She was walking the building in the order the building was built.  Which is a strange order, and takes her past the same door twice.

She was carrying a canvas roll of tools.

"Has something broken?" said Dera.

"No," said the dinosaur.

She unrolled the roll on the floor.  The tools were laid out in loops, oiled, each one in its own place.  She took out a spanner, tightened something that was not loose, put the spanner back, tied the roll up again and stood.

"I've never once opened this in an emergency," she said.  "I open it on Tuesdays."

"May I ask how you got so big?"

"Signed once," said the dinosaur.  "Forty years ago, at the door, for the whole of it.  Took about eleven seconds.  I haven't signed anything since and I haven't needed to."  She tied the roll.  "It's the one signature that does it.  You only want the one, if it's the right one."

Then she picked up a cast-iron radiator that was leaning against the wall waiting to go back in, on her own, without changing her expression, and carried it down the corridor and round the corner sideways.

"Does that get easier?"  Dera called after her.

"No," said the dinosaur, from round the corner.  "You get bigger.  The doors stay the same."

Her hands had no marks on them at all.  She smelled of oil and paper.  She went on ahead down the corridor, and Dera wrote in her notebook *official, first floor, name not given,* and that one line is the largest mistake in the whole report.

Dera did ask her one other thing.  She asked whether her rounds took her out to the doorstep.

"The step was already there," said the dinosaur, as though Dera had asked whether she looks after the weather.

### The pen, at the first landing

Dera held the pen up to the light on the stair.

She had written eleven words all week.

A great deal more than eleven words was gone.

She decided the pen was faulty.  It is remarkable what a person will decide.

# Night Eleven

### Neuronal Line
The neuronal line ratchets affective slack: affective and motivational structure produced by sensorimotor reentrant signaling and shaped by associative learning.  Its pre-line groundwork is the pre-neural sensory and behavioral coordination that emerged in early multicellular organisms.
Trait-level individual differences in dispositional response are documented from Vertebrates up, in behavioral-syndrome research in behavioral ecology and in Koolhaas coping-style architecture.  At those cells the adjacent pairs carry personality traits and the opposite pairs carry signatures.

#### Bilaterian Stack
The founding form of the neuronal line.  The line-defining move is from diffuse nerve nets to centralized brains with monoamine signaling.  Dopamine and serotonin emerge as the monoamines of valence and arousal.  The defining mechanism is steering: head-first directional movement that requires a brain to process forward sensory input and command body-wide muscular response.  *Impetus* operates as the attractor because steering only pays off if the organism acts on what it senses now.  A steering animal that hesitates instead of committing to the freshest signal gains nothing from the architecture.  This is recency: eligibility trace credits whatever cue occurred most recently.
The reinforcing cycle runs through steering plus affect.  Affect is valence and arousal, the basic good-or-bad evaluation of states.  Steering plus affect produces associative learning, which makes future steering more rewarding, which selects for finer steering and richer affect.  The breakthrough is Attention, the within-lifetime selection process in which candidate movements compete for expression and valence picks the winner.  Attention is the neuronal line's selector, the within-lifetime counterpart to Natural Selection.  It operates across every neuronal cell from Bilaterian up.  Steering is its behavioral expression at this cell and sits at the Pursuer capacity.
The Effector swap at Bilaterians replaces Persistence with Impetus, marking the genetic-to-neuronal line boundary.
Temperament, the signature born here, is behavioral predisposition tied to interior states, and it is the founding form of the Effector × Modeler pair, arriving before any relational architecture does.  It maps to the developmental-psychology temperament tradition (Rothbart 1981; Chess and Thomas 1963; Kagan 1984).
*Temperament as a developmental-psychology construct is empirically well-established.  The placement at the Effector × Modeler pair at bilaterians is mine.*
**Overview.** Animals with a head and a tail, a left and a right, and a brain at the front where the senses gather.  This is the body plan of nearly every animal you can name, from worms and insects to fish and us.  It appears just before the Cambrian explosion, when animal life suddenly diversified.
**Virtuous cycle.** A body that moves forward pays to put sensing and deciding at the front end, and a better front-end brain makes bolder forward movement worth the risk.
**Breakthrough — Attention.** Attention is the breakthrough here, and it founds the neuronal line the way natural selection founds the genetic one: it is the contest in which candidate behaviors compete for expression, the winner scored by reward and kept by memory.  That is selection moved inside a single animal — a within-lifetime Darwinism, so a body can learn in an afternoon what a lineage would need generations to.  Its bilaterian expression is steering: a front-ended animal picking one target out of many and aiming the whole body at it, where a jellyfish can only react where it sits.
The reading behind the slots: the bold and shy roundworms, all 302 neurons of them, foraging differently and keeping to their styles, are Shay Stern et al. 2017.  The fruit fly that sleeps in the full sense, harder after a night kept awake, is Paul Shaw et al. 2000.  The associative-learning machinery is Hawkins et al. 1983, and the inhibition work is Edwards et al. 1999.

#### Vertebrate Stack
Vertebrates introduce stored regulation in the neuronal register: behavior governed by adjustable rules that don't require rewriting wiring.  The defining mechanism is operant conditioning, action-outcome contingencies reshaping future action selection.  *Mastery* operates as the attractor because the organism is now in the business of getting better at things — skill rather than just response — and the Regulator swap replaces Coordination with it.  This is familiarity: blocking lets an established predictor lock out new rivals from taking credit.  The reinforcing cycle runs through the basal ganglia in actor-critic form: the actor selects actions, the critic evaluates outcomes, the reward prediction error updates the actor.  This is also the cell where trait-level individual differences in dispositional response first become a documented empirical structure.  The Behavioral Syndrome sits at the Regulator × Reviser pair coupling Mastery with Excitability, and its physiology has three parts — the sympathetic nervous system as the fast arm, the hypothalamic-pituitary-adrenal axis as the slow arm, and dopamine as the broadcast neuromodulator coupling them.  Proactive copers show higher SNS reactivity and lower HPA reactivity, reactive copers the inverse, so the cluster sorts on the ratio rather than on overall magnitude; it has been replicated in rodents, birds, and fish, where the slow arm is the HPI axis with cortisol.  **The breakthrough is Reinforcement Learning** in its model-free form: a brain that can work out which of its recent actions earned a reward that arrived seconds later, and tune toward it.  The machinery is the basal ganglia, nearly unchanged from a lamprey all the way to a human.  Every animal you can train with food rewards is running this circuit.  *Koolhaas's two-tier architecture is empirically established across multiple vertebrate lineages.  The placement at the Regulator × Reviser pair is mine.* The actor-critic formulation is Barto, Sutton & Anderson 1983; the coping-style architecture is Koolhaas et al. 1999, with the pace-of-life dimensions Réale 2010; the cross-lineage anchor in behavioral ecology is Sih, Bell & Johnson 2004 and Bell et al. 2009; the dopamine prediction-error work is Wolfram Schultz, Dayan & Montague 1997 and Wise 2004; procedural memory is Squire 2004; the enteric nervous system behind Gut Sense is Furness 2012.

#### Mammal Stack
Mammals introduce organized interiority in the neuronal register: a brain with multiple co-occurring functional architectures running in parallel — agranular prefrontal cortex, limbic system, hippocampus.  The defining mechanism is active inference, perception and action as joint minimization of prediction error against a generative model.  The brain models future states using working memory and proto-episodic memory rather than only responding to current input.  *Autonomy* operates as the attractor because offline simulation lets the organism act on internal models rather than on immediate environmental contingencies, and the Modeler swap replaces Interiority with it.  This is potency: overshadowing lets the strongest cue dominate the model the organism builds.  The generative machinery installed here runs in two deployments — sensory cortex running a world model that predicts external objects, frontal cortex running a self model that predicts the agent's own intentions and internal state, taking its input from hippocampus, amygdala, and hypothalamus.  Self-Model names the frontal deployment, which is why the signature sits at the Effector × Modeler coupling: it is the generative model of the acting agent.  Neuroticism debuts here at model-informed regulation aimed at an attachment figure, anchored on Bowlby's attachment behavioral system and Ainsworth's secure-base finding; the trait is how reliably the model returns a felt sense of the figure's availability, and a secure model settles fast where an insecure one holds the possibility of absence close.  The triples carry Stanovich's tri-process constructs.  **The breakthrough is Working Memory** — the inner world model run offline, playing out an action as if on a screen before the body performs it, and it needs all four drives at once.  Active inference is Friston 2009; the anatomy is Shipp, Adams & Friston 2013, Barrett & Simmons 2015, and Seth 2013; the tri-process constructs are Stanovich 2011, *Rationality and the Reflective Mind*; the resting rat replaying routes forward and in reverse while the body holds still is Pfeiffer & Foster 2013 and Foster & Matthew Wilson 2006; the cognitive map is Tolman 1948; blocking is Kamin 1969; countercontrol is Delprato 2002; episodic memory is Squire 2004 and Foote & Crystal 2007; the coping-style carry-forward is Koolhaas et al. 1999 and Sih, Bell & Johnson 2004; the prediction-error work is Wolfram Schultz, Dayan & Montague 1997.

#### Primate Stack
The granular prefrontal cortex made mentalization possible: modeling other minds as having intentions distinct from one's own.  *Affiliation* operates as the attractor here, but its affective machinery is inherited rather than minted here — the mammalian attachment system arrives at Mammal.  What is new is that mentalization turns the belonging drive into a Reviser: it lets the unit revise its own goals toward the modeled preferences of others, and it scales the drive from the dyad to the coalition, tracking who allies with whom, where one stands, and what another intends.  Alliance-building, reputation management, and hierarchy navigation all rest on aiming the inherited drive through mentalization; the competitive politicking that primate group life selects on is one face of this, not its foundation.  This is novelty: latent inhibition privileges the unfamiliar mind or signal over the well-worn one.  The reinforcing cycle runs through politicking, and the metabolic cost is paid by a high-energy fruit diet, which confines the lineage to arboreal niches and limits troop mobility.  The bet trades ecological range for cognitive depth, and primates have been losing territory steadily for millions of years to keep paying for it.  The Reviser swap replaces Excitability with Affiliation, and this is the bridge entity to the symbolic line.  Sociometer, the signature born here, is an internal gauge that reads the agent's relational value in the group and regulates conduct to preserve inclusion.  **The breakthrough is Perspective Taking** — holding a model of another mind, what it knows, wants, and does not know.  A low-ranking chimp wanting food the boss is sitting on clocks that the boss cannot see behind a rock, and takes the long way into the blind spot.  Whether apes pass the strictest false-belief tests is still argued, part of why it sits here as contested.  Triadic awareness is Cheney and Seyfarth, *How Monkeys See the World* (1990) and *Baboon Metaphysics* (2007); tactical deceit is Richard Byrne and Andrew Whiten 1985 and Andrew Whiten et al. 2005; self-determination is Deci and Ryan 1985; the need to belong is Baumeister and Leary 1995; the goal-directed reading of the blind spot is Hare, Call & Tomasello 2001; fairness refusal is Brosnan & de Waal 2003; the chimpanzee personality work is King & Figueredo 1997 and Hopkins et al. 2012; metamemory is Foote & Crystal 2007; the cognitive map is Tolman 1948; coping styles carry from Koolhaas et al. 1999.

## The Second Floor

The sign at the bottom of the second stair said:

**ON THIS FLOOR A MISTAKE COSTS A MOVEMENT.**

Underneath, in smaller letters, somebody had added:

**LATER, ONLY A REHEARSAL.**

There is nobody on the second floor either, and Dera had stopped expecting anybody by then.

There are birds.  Crows and rooks and ravens the size of a child, in Bureau grey waistcoats, walking about with their hands behind their backs, which is to say their wings.  There are parrots, extremely loud, in every colour there is.  And there are dinosaurs, of the sort that go about on two legs with their tails held out straight behind them for balance, so that everybody on that floor has learned to stand well clear of a doorway when one is coming through.

### The Lane and the Whistle

Painted down the middle of the second-floor corridor is a lane, like a running track.  It has a white line across it every yard, and beside every line there is a number painted a foot high, and the numbers go up to two hundred.

This is how the second floor pays.

There is a flagman.  He is a dinosaur about eight feet long from nose to tail, in a striped waistcoat, with a whistle on a lanyard and a flag in each hand, and he stands at the far end of the lane all day whether anybody is running or not.

You stand at the mark.  You begin to run.  The flagman blows the whistle.  You stop dead, exactly where you are, and you do not move your feet by so much as an inch, and the flagman walks up and reads the number under your front foot and shouts it down the corridor.

And then everybody on the second floor claps.

They clap kindly.  Nobody is jeering.  It is a sports day, and that is the very worst thing about the second floor, and Dera says so twice in her report.

Now here is a thing the reader must hold on to, and it is the same thing as the two columns on the doorstep, so it should not be difficult.

**One floor down, a payment is a number of iron weights and a bell.**

**On this floor, a payment is a number of yards and a whistle.**

There is nobody in the Bureau of Persistence who can tell you how many yards make a bell.  There is no table on the wall.  There is no clerk who keeps the table in a drawer.  There has never been a table, there is no plan to make one, and when Dera asked for one she was laughed at by a kind man who thought she was joking.

The stair is short.  Nobody stopped her.  Nobody was guarding anything.  Dera had expected the floors to be guarded, and this belongs in the record, because she climbed the entire building without once being asked to.

The first person she met on the second floor is a small dinosaur about the height of a dog, and she does two things.

"Toward," she said, and went toward it.

"Away," she said, and went away.

She has no third thing and does not need one, and she is faster at her two than anybody upstairs is at anything at all.

The second person is a grey parrot, and he cannot be told anything.

He can talk.  He talks beautifully.  Dera explained her letter to him four times, more clearly each time, and he repeated the important parts back to her in her own voice and did not shift by one inch.  Then she dropped a biscuit, and he happened to be doing something at the moment the biscuit fell, and he has done that same thing every day since, without fail, for ever.

He is the most reliable witness in the Bureau.  He also cannot be taught.

The fourth person is a parrot in about nine colours, and she cannot stop measuring how she is thought of.  She has an instrument for it and the instrument is always running, and it is not vanity.  When Dera looked away in the middle of her sentence to check a figure, something in her went off like a bell, and she apologised to Dera for interrupting.

### She asked again, on the lane

She asked the flagman how many bells make a yard.

He laughed.  He thought it was a joke, and a good one, and he told it to two other people in the corridor and they laughed as well.

When Dera said that she meant it, and that she was asking officially, and that she had paid a body downstairs to ask the other half of the same question, he stopped laughing and was embarrassed for her, and very kind about it.

Then he said that asking it here was a mistake, because it is, and that she would have to run.

So she ran.

She stood at the mark and she ran down the painted lane, and the whistle went, and she stopped dead with her front foot on a line, and the flagman came up and read the number and shouted **"nineteen"** down the corridor, and the second floor clapped.

They clapped kindly.  Nobody jeered.  It is a sports day, and that is the very worst thing about the second floor, and she says so twice in her report.

Nineteen yards for the same question that cost her a body one floor down.

She did not notice the comparison at the time.  She noticed that they had clapped.

### The Rehearser

The third person is a rook, and he is the Rehearser, and his office is a wall of coat hooks.

Forty or fifty of them, in rows, and on nearly every hook hangs one of his copies.  Folded once at the waist.  Thin as a shirt on a line.  Grey, where he is pink.

They hang in order.  The oldest are at the far end, and those are worn through at the elbows and the knees and the soles of the feet, because they went places.

He did not.

He himself is very small.  He comes up to about Dera's elbow and there is nothing to him at all.  He is pink and unmarked and beautifully rested, and his shoes have no scuffs on them anywhere, because they have never been anywhere for anything to scuff them on.

He asked her to reach a box down off the top of his own cupboard, and she did, and he thanked her warmly and without the slightest embarrassment, because he has been asking people to do that his whole life and has never once thought it strange.

He works at a full-sized desk in a chair that is much too big for him, with his feet a long way off the floor, and he does not appear to have noticed.  The copies on the hooks are all exactly his size.

"I send them ahead," he said.  "Then I don't have to go."

"And what IS a rehearser?"

"Somebody who finds out what happens without going.  And what IS an auditor?"

"Somebody who finds out who owes what," said Dera, who was beginning to find the answer a little short.

"Then we are in the same line of work," said the Rehearser, delighted, "except that I am faster than you are, and I have never once in my life had to sign for anything, and look at my shoes."

She looked at his shoes.  They had no scuffs on them anywhere.

While Dera sat with him one came back.  It came in at the door thin as a bill, walked to the corner, and lay down, and he did not look up.

"That one's finished," he said.  "There's another on the way."

His office has no record in it of anything he has actually done.

He was the first person in the whole building to understand Dera's letter completely, and he was also the first to point out, very kindly, that no docket had been raised against him for doing so.

And at the end of the row of hooks there was one empty hook, with a small brass plate screwed to the wall beneath it, and the plate had been engraved with Dera's name.

"When did you have that done?" said Dera.

"Before you came," said the Rehearser.  "We do it for everybody.  It saves time."

### What the Rehearser offered

In her second week he offered to send one down the whole audit for her.

He put it very reasonably.  She was going to have to climb four floors and interview a great many people and be wrong a great deal, and a copy could do all of that and come back and tell her the answer, and not one card would be stamped against her name.

Dera said yes.

She had been in that building two weeks.  She had made one mistake already and she had stood beside the balance and watched what was done about it, and a man had offered to do the rest of it for her without one card being stamped against her name, and she said yes.

The copy went.  It was gone four days.

It came back thin and grey and it walked to the corner and lay down, and folded in its hand was a single sheet of paper, and on the sheet, in Dera's own handwriting, there was one line, and here it is, because there is no reason on earth for the reader not to have it at the same moment she did.

**IT WAS ALREADY TWO.**

You know what that is about.  You were there.  It was the small thing in the dust on the doorstep, in her first hour, the one she broke twice, that came back as one and then came back as two, while a fat grey man weighed the difference on a jeweller's pan and chalked it up in a second column.

Dera did not know what it was about.

She read it three times.  Five words.  She could not attach them to anything, and she was not going to put a sentence in her official notebook that she could not attach to anything, so she folded the sheet in four and put it in her inside pocket.

It stayed there for four weeks, in her coat, while she went up two more floors and down a cellar and looked for a table.

### The long room, again

The long room on the second floor is full of people too, and they look every bit as well as the ones downstairs, and they are waiting for a movement rather than for a body.  Dera put her head in.  A woman waved at her with a rolled-up magazine.

### The Storekeeper

The official of the second floor is the Storekeeper, and he keeps a silo.

He is a raven, and a very large one, and he is dusty as high as the shoulder.  He dresses in the colour of what he keeps, so that from behind he looks like part of the silo.  His hands are broad and flat.  Conversation puzzles him.  He gave Dera a handful of grain to hold, and then another handful, and then he filled her pockets.

The silo is three times the size his floor needs.

"Why so big?" said Dera.

He looked up at it.  He looked at her.  He was not being difficult.  He simply had no answer, and had never once needed one.

A store that big soaks things up.  It soaked up Dera's mistakes along with everything else, without being asked, because that is what a large pile of extra does.  It did not do it for her.  It would have done it for anybody.

Her second mistake cost her a movement she had started and did not finish.  That was all.  Nothing died.

She paid twice on that lane.

The first time she stopped at **nine**, which is not very far, and the flagman shouted "nine" down the corridor, and the second floor clapped.

The second time she stopped at **thirty-one**, and the flagman said that thirty-one was a very respectable stop, and shook her hand.  Thirty-one yards means she had been running a long while before the whistle went.

Two days later she made a larger mistake, and for that one she was given a docket too.

The second-floor docket is not heavy grey card.  It is a small buff slip about the size of a tram ticket, and the amount is not stamped into it but printed on it, and the figure on hers was **1**, in the same numerals as before, and there was no line for a countersignature anywhere on it.

She held the two dockets up side by side.  The same number on both.  Two different sizes of card.

She thought at the time that this was a matter of stationery.

And after that, people on the second floor began answering her just slightly less carefully.

Not rudely.  There was simply less at stake in getting her wrong.  Everybody on that floor could feel it before she could.

### The Man Who Arrives Later

Late on the ninth day she met a second dinosaur, exactly, precisely, to the inch, the same size as the one at four in the morning.  Same height, same reach, same tail, same arms, sleeves rolled up past the elbow because they will not go down over them any more.  He came through the corridor door sideways with his chin down, without appearing to think about it.

They are the same height because they signed the same thing at the same door on the same morning forty years ago, and that is one of several reasons why people who have worked in that building for forty years get the two of them mixed up.

His forearms are scarred all over.  The scars are in lines, and the lines are in order, and if you look carefully you can read the whole history of things going wrong in that building, in the order they went wrong.  Both his thumbnails are black.

He carries no tools at all.  He finds what he needs where the trouble is.

"You're quicker than the woman at four in the morning," said Dera.

"I am," he said.  "And I always get there later."

On his belt was the same key ring she carries.  It holds more keys than the building has doors.  Dera counted them twice and got two different numbers, which she also decided not to think about yet.

"Do you two work together?"

"We've never been in the building in the same hour," he said.  "Not once."

People who have worked in the Bureau for forty years believe the two of them are one person.  No committee has ever corrected this, because neither of them has ever appeared in front of a committee.

### The pen, at the second landing

Down again.  By the same amount as the first week.  Exactly the same amount.

The Storekeeper came and looked at it with her, and understood the problem at once, entirely, better than she did.

Then he filled her pockets with more grain, because that was the only thing he had.

# Night Twelve

### Symbolic Line
The symbolic line ratchets Shannon slack.  Symbols are constraints on signal-space.  Lexicons, grammars, conventions, and pragmatic norms each reduce the space of legitimate messages by large factors.  Cultural transmission preserves the constraints that work for coordinating groups.  Its pre-line groundwork is pre-symbolic animal signaling (indexical and iconic reference), detailed in Deacon's *Symbolic Species* (1997).
The unified Venn at each symbolic-line cell takes the constituent human as its unit, parameterized by collective context.  The collective is the group the human runs on.  A band produces Conversation.  A settlement produces Common Knowledge.  A city produces Codes.  An empire produces Trust.  The cells are named with the -Human suffix (Band-Human, Settlement-Human, City-Human, Empire-Human) to mark that the Venn tracks the constituent human, not the collective.

#### Band-Human Stack
The founding form of the symbolic line.  The line-defining move is from primate-style alliance politics to shared intentionality: the "we"-mode in which non-kin form joint goals and joint commitments (Tomasello 2003).  *Commitment* operates as the attractor because the we-mode lets non-kin bind themselves to common purpose, which is what makes cooperation among strangers possible at all.  This is recency in differential-adoption terms: the commitment made in the moment it is needed is what the ledger credits.  Language is the medium that lets a shared "we" be declared and scaled.  Gossip is the enforcement layer that stabilizes commitments against defection by making social debt trackable across many people without direct observation.  Cheaters get talked about.  Contributors get talked about.  The band maintains a distributed ledger of who owes what to whom.  The we-mode is the foundation; the ledger is how it is policed.
The reinforcing cycle runs through meat pooling (calorie-rich food shared across the band rather than monopolized) and collaborative fission-fusion (groups split and rejoin without rupture because the ledger persists, with intergroup marriage formalizing the cross-band reproductive alliances that sustain fusion across long intervals).  This unlocks dispersal to all habitable latitudes and cumulative culture, where each generation inherits the previous generation's solutions.
The Effector swap at Bands replaces Impetus with Commitment, marking the neuronal-to-symbolic line boundary.  Band-Human emerges by elaboration, not symbiosis: it develops from primate troop dynamics through language-mediated extension.
Self-Reference has three co-equal anchors: the looking-glass self (Cooley 1902), the self-conscious emotions (Tracy and Robins 2004; Michael Lewis 1989; Tangney 1990), and Hofstadter's strange-loop pattern (*I Am a Strange Loop*, 2007).  The self-conscious emotions are shame, guilt, embarrassment, and pride; they are how self-reference manifests under symbolic-reciprocal evaluation.  They emerge developmentally around age three, are present universally across human cultures, and are absent or proto-form in non-human primates.  The strange-loop is the cognitive structure of the symbolic self, a self-referential pattern riding on the Mammal self-model: the symbolic, narratable "I", not a claim about where consciousness originates.  Self-Reference is a single-agent, inward loop, the self modeling itself including itself-as-seen, and is distinct from Settlement-Human's Common Knowledge, which is a multi-agent, across structure scaled by a public focal point.  Reserve "strange loop" for Self-Reference; do not use it for Common Knowledge.
Collaborative Fission is the institutional protocol by which groups split and rejoin without rupture.  The social ledger persists across the split, the procedural know-how of when and how to fission is applied, and individuals and families decide their own sub-group affiliation.  It runs without Affiliation by design — the protocol enables splits between sub-groups precisely when affiliative tension is what motivates the split.
*The self-conscious emotions are an established empirical construct, and Hofstadter's strange-loop account is a developed theoretical proposal.  The placement at the Effector × Modeler pair at bands is mine.*
**Overview.** Modern humans living the way our species lived for almost all of its history: in small mobile bands of a few dozen, hunting and gathering, bound together by language.  The breakthrough here is full speech — whole sentences, not just calls and signals.
**Virtuous cycle.** Talking lets a band pool what each member knows and act as one, and a band that coordinates better survives to pass on the language that let it.
**Breakthrough — Conversation.** Conversation is the breakthrough here, and it founds the symbolic line the way attention founds the neuronal one: it is the contest in which candidate utterances compete to be repeated, the winner scored by uptake and kept in shared memory.  That is selection moved out of any single mind and into a corpus that outlives the speaker — so a band can hold what one lifetime would lose.  Its band expression is full open-ended language, whole sentences rather than fixed calls, which is what makes gossip, reputation, and shared plans work across a whole band and not just between two groomers.  The date is argued from material traces, since talk leaves no fossil: the oldest stand-ins are abstract scratch-marks on ochre at Blombos Cave, roughly 75,000 to 100,000 years old.
The reading behind the slots: cooperative childcare is Hrdy, *Mothers and Others*, 2009; the forager band structure and its co-residence patterns are Hill et al. 2011 and Walker et al. 2010; the hunter-gatherer diet and provisioning arithmetic is Kaplan et al. 2000; the firelight-gossip work is Wiessner 2014.

#### Settlement-Human Stack
Settlements introduce stored regulation in the symbolic register: norms that govern behavior without requiring renegotiation each time.  The defining mechanism is agriculture, sedentary food production that permits population density, surplus storage, and permanent dwellings.  *Stability* operates as the attractor because everything settlement society does only pays off if the settlement persists — canals, monuments, and stored grain only return if the settlement is still there in fifty years — and the Regulator swap replaces Mastery with it.  This is familiarity in differential-adoption terms: the established norm defends its place against a novel proposal.  The reinforcing cycle runs through surplus: agriculture produces surplus, surplus enables labor specialization, specialization produces writing and law and calendars, recording enables larger-scale coordination, and larger scale requires more stability.  Self-Construal, the signature born here, is independent versus interdependent self-reading calibrated by subsistence ecology, with wheat-style cultivation's lower coordination demands producing the independent reading and rice-style cultivation's high cross-household demands producing the interdependent.  **The breakthrough is Common Knowledge** — not just that everyone knows a rule, but that everyone knows everyone knows it, and so on up.  Settlement architecture, the square, the monument, the marketplace, gives strangers durable shared focal points that lock that mutual awareness in, and norms then rest on it.  One thing worth holding: the recursion in common knowledge, the embedding of knows-that-knows, is the same nesting the symbolic line is learning to express in syntax across these cells.  Neither builds the other.  Both are the symbolic expression of a conceptual nesting the prior already carries.  *That syntactic recursion and recursive mutual-knowledge co-mature because both express one shared conceptual nesting is my account.  The stronger claim that they are literally one mechanism is contested, and double-dissociation evidence exists.  I am not asserting it.  The load-bearing reading is the shared conceptual source, which survives even if the two channels prove dissociable.* Common knowledge in the technical sense is Pinker 2007, David Lewis, and Schiffer; norms presupposing it is Bicchieri 2006; the independent-interdependent framework is Markus and Kitayama 1991 and Triandis 1989, with the rice-wheat mechanism Talhelm et al. 2014; the wealth-transmission work is Borgerhoff Mulder et al. 2009; alloparenting and kin effects are Sear & Mace 2008 and Hill et al. 2011; the trait-maturation work is Brent Roberts et al. 2007.

#### City-Human Stack
Cities introduce organized representation in the symbolic register.  The defining mechanism is the administrative code: written rule that records obligation, ownership, and procedure in a form that outlives the people who set it down.  *Representation* operates as the attractor because a city runs on standing records — land registers, law codes, tax rolls, and calendars let coordination scale past what any group can hold in memory — and the Modeler swap replaces Autonomy with it.  This is potency in differential-adoption terms: the most forceful record dominates what the group takes as true.  The city forms as a symbiosis of settlements and trade networks: settlements supply the population, surplus, and agricultural base, trade networks supply the connectivity, and the city is the merger product.  The instances are the Sumerian city-states consolidating agricultural villages along Mesopotamian trade routes, the Egyptian urban centers along the Nile, Shang-dynasty China consolidating Neolithic settlement clusters along trade corridors, and the Indus Valley centers at the western terminus of overland Asian trade.  A new constituent-human type appears here alongside the band-forager and the settled farmer: the merchant, a symbolic-line nomad whose life-form is structured around movement along trade routes between cities.  The reinforcing cycle runs through records — records enable taxation, taxation funds specialists, specialists produce more records.  **The breakthrough is Codes** — written, portable, enforceable rules that coordinate strangers who share no face-to-face history.  The first writing at Uruk is not poetry but accounting, ledgers of grain and beer rations.  A city is too big for everyone to know everyone, so the rule on the tablet does the work that watching neighbors did in a village.  The early-state and grain-legibility argument is Scott 2017; the urban-density economics is Glaeser 2011; the Roman grain supply is Erdkamp 2005 and Powell 1971; Core Self-Evaluations is Judge, Edwin Locke & Durham 1997 and Judge et al. 1998; the HEXACO structure is Ashton & Lee 2007; trait maturation is Brent Roberts et al. 2007; the subsistence-ecology work carries from Talhelm et al. 2014 and the band-structure work from Hill et al. 2011.

#### Empire-Human Stack
Empires introduce stranger-to-stranger trust in the symbolic register.  The defining mechanism is the universalizing framework: a currency, a law, a creed, or a shared identity that lets people who will never meet rely on one another anyway.  *Universality* operates as the attractor because an empire must extend reliability to populations with no shared kinship, language, or local history, and the Reviser swap replaces Affiliation with it.  This is novelty in differential-adoption terms: a universalizing framework spreads precisely because it reaches strangers an old, local framework could not.  The empire forms as a symbiosis of cities and colonies committing to integration under that framework — Rome and the Italian cities and Mediterranean colonies under senatorial-imperial administration, Han China and the Warring States cities and frontier colonies, the Achaemenid Empire and the Median, Babylonian, Egyptian, and Lydian cities under the King of Kings, the British Empire and its metropolitan city, settler dominions, and resource colonies under a single crown.  Identity is the synthesis at this level.  Intellect names universalizing intellectual engagement under reciprocal exchange, and here the architecture makes a prediction with a cost attached: Openness-to-Experience, the aesthetic-experiential facet, does not get a structural slot.  Only Intellect has a home.  That is a retrodictive payoff against the cross-linguistic finding that Openness is the unstable Big Five factor.  **The breakthrough is Trust** — a stranger hands another stranger something that matters and expects it to come back.  Coin, contract, and creed each let reliance travel past the reach of anyone you will ever meet.  One structural note: this cell's Row-4 bet has resolved, and it resolved by bridging — it parented Computer, the founding cell of the digital line.  Of the three fates a Row-4 entity can meet, this is the one that opens a next inheritance line rather than failing or succeeding off-thread.  *Social identity theory, Erikson's identity-formation work, McAdams's narrative identity, and Goffman's presentation of self are well-developed traditions.  The placement at the Regulator × Reviser pair at empires, as facets of one construct, is mine.* Trust across strangers is Seabright 2004; imagined community is Benedict Anderson 1983; social power is Mann 1986; cultural memory is Assmann & Czaplicka 1995; the Chinese imperial case is Mark Edward Lewis 2007; the Spanish-American silver case is Bakewell 1984; the Openness instability is De Raad et al. 2010; HEXACO Honesty-Humility is Ashton & Lee 2007; Core Self-Evaluations carries from Judge et al. 1998; trait maturation from Brent Roberts et al. 2007; band structure from Hill et al. 2011.

#### Big Five Buildup Across the Symbolic Line
The Big Five traits debut at separate symbolic cells and persist forward.
- Conscientiousness debuts at the Settlement Controller.  It persists to City and Empire.
- Extraversion debuts at the City Anticipator.  It persists to Empire.
- Agreeableness debuts at the Primate Adapter.  It persists to Band and Settlement.  It transitions to Righteousness at City.  It transitions to Integrity at Empire.
- Curiosity debuts at the Band Explorer, the earliest structural home for the Intellect facet of Big Five Openness.  It persists to Settlement and City.  It transitions to Intellect at Empire, the name change tracking the same slot's shift from foraging-derived exploration to universalizing inquiry.
- Big Five Openness-to-Experience does not have a structural slot.  Only the Intellect facet does, and it holds one slot, the Explorer, continuously from Band-Human to Empire-Human under two names, Curiosity then Intellect.  That is the prediction I am making against De Raad's cross-linguistic replication finding.
- Neuroticism does not debut on the symbolic line.  It debuts on the neuronal line, at the Mammal Anticipator, and persists through Primate into Band-Human before the Settlement-Human swap to Assertiveness.

## The Third Floor

The sign at the bottom of the third stair said:

**ON THIS FLOOR A MISTAKE COSTS A WORD.**

There is nobody on the third floor either.  There is also no water on the third floor, and it does not appear to be a difficulty for anybody, and nobody has ever raised it.

There are octopuses.  Big ones, about the size of a person when they stand up, in Bureau grey, going about on eight arms with two or three arms always doing something else at the same time.  They change colour while they talk to you, all over, in patches, and they do not know they are doing it, and it is considered rude to mention it.

And there are dolphins.  They go about upright, balanced on the tail, in groups of nine and eleven and never on their own, and they are the fastest talkers Dera ever heard in her life.

The dockets on the third floor are the smallest in the building, because a word can be got out and got back inside a second.  This is the fastest floor in the Bureau, and it is where Dera lost the entire audit, and she did not notice for six weeks.

### The Tube and the Counter

Set into the wall of the third floor at the height of a mouth there is a brass speaking tube, polished bright by use, with a funnel on the end of it the size of a soup plate.

Above the tube there is a mechanical counter with six little windows in it and a brass handle that nobody touches, and the figure in the windows is enormous, and it goes up all day long.

This is how the third floor pays.

You put your mouth to the funnel and you say the word into it.

The counter clicks.  Everybody hears the click.  That is the number said out loud, and on that floor the machine says it for you.

And then the word is gone.  Not from the world.  From the floor.  Nobody on the third floor can say that word again, and nobody on the third floor can hear it said, ever, for as long as the Bureau stands.

**One floor down it was yards and a whistle.  Two floors down it was iron and a bell.  Up here it is a click and a word that goes out.**

There is no table.  The reader will forgive the repetition.  There is no table anywhere in this building and there is not going to be one.

The long room on the third floor is full of about two hundred dolphins, and they all know the same thing.  They know it, and they know that everybody knows it, and they know that everybody knows that everybody knows it, and so on for as long as you like.

Because of this they can all turn at once with no signal.

Dera saw them do it twice.  No shout, no bell, no nod.  Two hundred people turned to the left as one animal.  She looked for the person who had decided, and there is no such person, and there never was.

Then she worked out what she was looking at, and it is not eerie at all once you know.

They turn because somebody has paid.

When the counter above the tube clicks, every one of those two hundred people knows instantly, because they all know everything everybody knows, and they all turn round at once to look at whoever spent it.  That is what the turning is.  It is the third floor's witnesses doing their job.  They do it every single time, and they had done it fourteen times before lunch on the day Dera first noticed.

They are also the people who are waiting, on that floor, for a word.  It does not appear to trouble them.  It is very difficult to be troubled in a room where everybody already knows everything you might say.

There is an octopus on that floor who is the Keeper of Codes, and he does not trust anybody to know anything, and he writes it down instead.  He writes with four arms at once, in four different books, and all four hands are the same hand.  What he writes binds, and it goes on binding after every person who wrote it is dead.

He is the biggest thing in the building that is not a machine.  Nine feet, and about a yard across the back, and his hands go round a ledger the way yours go round a postcard.  His desk was built round him because there is no getting him out through the door now and both of them know it.

He is the only official in the entire Bureau who made Dera sign her name, and when she signed it she got bigger by about the thickness of a slice of bread in every direction, and her collar moved, and he watched it happen and nodded once, the way a man nods at a job done properly.

"That's the only thing in here that does that," he said.  "You want to be careful what you put it on."

There is an octopus on that floor who is made entirely of a story about himself, and who changes colour in patches the whole time he is telling it, and does not know that he is doing it.  When the facts move, he rewrites the story, competently, and in good faith.  Dera interviewed him three times.  He was honest all three times.  The three stories do not fit together, and he is not a liar, and there is no instrument in her bag that can tell his case apart from ordinary decency.

### She asked the tube

She thought about this one for a whole day first, because by now she knew what a mistake costs on the third floor and she knew what the tube does.

Then she went and put her mouth to the brass funnel and said the question into it, out loud, all of it: **how many yards make a bell.**

The counter clicked.

Two hundred people turned round and looked at her, because that is what the third floor's witnesses do, every single time, and they had done it fourteen times before lunch that day.

And the question was gone off the floor.

She could not ask it any more.  Nobody on the third floor could hear it asked and nobody on the third floor could say it, and she had to go down one flight and stand on the landing and write the words in her notebook from memory before she lost those too, and her hand was not steady, and she says in the report that it is the only time in six weeks that she was frightened.

**THAT IS FACT TWO.**

Three floors.  Three machines.  Three payments made correctly and in public, one of them a body.  And not one machine in this building can read the number off any other machine in this building.

She wrote it down.  She put it under a heading, and the heading was **MISSING DOCUMENT**.

And that is the wrong heading, and everything that goes wrong for the next four weeks goes wrong from there.

Because a competent auditor, holding fact two, concludes exactly what Dera concluded, and if you had her notebook and her training you would conclude it too:

**There was a conversion table once, and somebody got rid of it.**

It explains everything she has seen.  It is one single step away from the truth.  And the truth is that there was never a table at all, that there is no floor of that building that could hold one, and that nothing has been removed from anywhere.

She now had a document to hunt.  An auditor with a document to hunt is a happy woman, and for about ten days Dera was very happy indeed.

### The Chairman

And there is the Chairman.

He is an octopus, and he is the broadest, best-fed-looking thing on the third floor.  He says "we" about himself without any grandness at all, the way you might say it about a family.  His suit is beautifully made and twenty years out of fashion, and he wears it as easily as skin.

The suit is padded.  Dera found this out in the fourth week, by accident, when she put a hand on his shoulder to steady herself and the shoulder was three inches of horsehair with nothing in it.

It is padded everywhere.  Shoulders, chest, upper arm, the lot, all of it beautifully done by somebody who knew exactly what a large person looks like from across a room.

There is nothing inside an octopus to hold a shape.  Whatever shape a Chairman is, the suit is doing all of it.

Inside the suit he is one of the smallest full-grown octopuses on the floor.  He goes through every doorway in the place straight on, in the middle, without slowing down, and he has done that his whole life.  He has never signed anything.  In four hundred years of minutes there is not one signature belonging to the chair he sits in, because the chair does not sign, the chair asks, and other people sign, and other people get taller, and that has been going on for four hundred years and nobody has ever once complained about it because nobody was ever made to do anything.

His was the only hand in the Bureau of Persistence that was put out to her first.

He remembered her name.  He remembered the date on her letter.  He remembered the name of the office that had sent her, which nobody else in that building ever managed, including the Porter, including the Archivist.

He laughed easily and the laugh was real.  He was the only person in the building Dera looked forward to seeing, and that is in the report, because it is evidence.

In the fourth week she told him what had happened at the Archivist's register in her first week.

He was moved.  She watched it happen.  The feeling arrived on his face half a second late, and in exactly the right shape, and it did not go down into his hands, which stayed perfectly still on the table.

And then Dera put her hand flat on the table, and the table was warm.

It was warm on his side.  It was warm on her side.  She turned her hand over and it was warm on the side she had just touched, which no object in that building has ever been.

The Chairman has never been cold in his life.  He cannot be.  There is a grate in the floor of his room, a big brass one, and Dera got down on her knees later and looked through it, and one floor below she could see the workroom, and the bench, and a small upright woman in an apron with no marks on it.

That is where the heat in the Chairman's room comes from.  Not a boiler.  A floor.

Then he asked her for something.

He asked, as a courtesy, with no pressure at all, whether she would send her early findings through his office instead of down to the Archivist's gate.  The gate is slow, he said, and his office is not, and he only wanted to be helpful.

It was a reasonable request from a generous man, and she said yes, and she signed the form he had ready, because there was a form.

She got bigger.  About the thickness of a slice of bread, up and out and through the shoulders, and she felt her collar move and the chair take it.

He did not get bigger.  He was pleased for her and he said so, and he meant it, and the table between them stayed warm on both sides.

On her way out of his room she caught her shoulder on the doorframe, which had never happened to her before in her life, and she said sorry to the door, and the Chairman went out after her through the middle of it without touching either side.

And that was not bad judgement.  It was a fair trade, correctly priced, in which the price was paid by somebody who was not at the table.

The Chairman's committee meets in a chamber whose door opens onto the chamber.  Dera read four hundred years of their minutes.  There is no cruelty in them.  There is no crime in them.  There is not one single decision that is indefensible on the day it was taken.  What they do is put things off.  They are very good at it.  The bill that gets put off arrives one floor down, on people who were not in the chamber.  The chamber cannot feel it.  That is not a fault in how they work.  That is what a chamber is.

### The Keeper of the Rooms

The official of the third floor is an octopus called the Keeper of the Rooms, and he goes through a gap the size of your fist without slowing down, and the first thing about him is the key ring.

He carries every key on one ring, and the keys are in order of size.

The first is a great iron thing the length of a hand.  Each one after it is a little smaller.  Halfway round the ring they are the size of a house key, and then a locket key, and then a watch key, and the last one is about the size of a grain of rice.

All of them are worn to a shine except the last three, which are still bright, and still sharp at the edges, and still burred where they were cut.

"And what IS a keeper of rooms?" said Dera, who had learned by then to get the question in early, before he went round a corner.

"Somebody who looks after the doors."

"Not the rooms?"

"The doors ARE the rooms," said the Keeper of the Rooms, from somewhere she could not see.  "If I looked after the rooms I should have to go in."

His coat is worn shiny at both shoulders, evenly, from turning corners fast in places too narrow to turn in.  He is thin and quick and always halfway to somewhere else, and he talks the entire time he is walking, so that half of every answer arrives round a corner from a place you cannot see.

He keeps a set of rooms in which you can be wrong and nothing happens.  He keeps them for the committee.  He does not keep them for Dera.

The first room is an ordinary room with a desk in it.  In it Dera was wrong about something small, and nothing happened, and it was very pleasant.

Inside the first room there is a second door, and the second room is smaller, and the desk in it is smaller.  In there she was wrong about something larger, and nothing happened.

The third room she had to stoop for.  The fourth had a desk the size of a school desk, and by then she was working faster than she had ever worked, and being wrong about the shape of the whole audit, and enjoying herself enormously.

In the fifth room the ceiling was on her hat.  She sat at a desk built for a child, with her knees against the underside of it, and she was wrong about her own wrongness, which is a thing she had never once been able to afford, and she was better at her work in there than she has ever been anywhere in her life.

The Keeper of the Rooms talked to her the whole time from the corridor, cheerfully, about the hinges.

When she came out she could not tell which of her findings she had actually filed and which she had only practised.

Neither could the registry.  On that floor those two things leave exactly the same mark.

She filed eleven times.  Eleven is the wrong number and she knows it is the wrong number.

Nobody answered any of them.  Nobody was stopping her, and nobody was rude to her, and everybody on that floor was a great deal friendlier than anybody on the first floor had been.

There is a simpler way to put what was happening, and it is in the signature book.

On the first floor, a question was asked against a docket, and whoever answered it signed the book.  On the third floor there are no dockets and no book.  The Keeper of the Rooms gave her a pad of them, perforated, four to a page, and told her cheerfully to fill them in herself as she went.

She filled in nineteen.  She signed all nineteen.  Hers is the only name on any of them.

A question with nobody's signature under it is not a question anybody has to answer, and there is no unkindness in that anywhere, and it is not a thing you can complain about to a committee.

### The Registrar of Weather

At the end of a corridor on the third floor Dera found the Registrar of Weather.

He is the smallest grown octopus on the third floor.  Standing up he comes to about Dera's shoulder, and there is so little to him that you can see the shape of the desk through the thin parts of his arms, and when he moves his own ledger across the room it takes him five arms and two goes.

His suit is pressed to a line.  His cuffs come exactly half an inch clear of his wrist, and they have come exactly half an inch clear of his wrist for his entire working life, because his sleeves have never once had to be let down.

His fingernails are filed.  He has the best posture in the Bureau, and it is not discipline, and there is nothing on him anywhere to make him stoop.

His hands are the thing you notice.  Long, completely steady, and with no ink on them anywhere, and he writes with a nib he sharpens himself between entries.

He does not sweat.  In six weeks she never saw him tired, and never once saw him look up.

His ledgers are the finest work in the building.  Dera says so as a professional, twice, in writing.  The hand is beautiful.  The columns balance to the last unit.  Nothing in them is false.

There is no weather in them.

Not less weather.  None.  She turned every page.  There is no column for it, no heading, no line ruled for it, nothing crossed out where it used to be.  It is not missing.  It was never there.

"Where's the storm?" said Dera.

He waited, politely, the way you wait when somebody has stopped speaking in the middle of a sentence.

"The storm," said Dera, louder.  "Where do you enter the storm?"

He gave her a small courteous nod, and turned the page, and went on writing.

He cannot hear the word.

She tested it eleven times over three weeks, in four different rooms, once while holding his sleeve.  He hears everything else perfectly.  He hears "store" and "stir" and "swarm."  He does not hear "storm," and he does not know that he does not, and his books are therefore entirely accurate and prove, from the first page to the last, that no tax is owed.

He is not lazy.  He works harder than the woman at four in the morning and the man who arrives later put together, and his work is finer than either of theirs, and he has never once been wrong inside his own accounts.

And for three whole weeks Dera could not tell him apart from the woman at four in the morning.

That belongs in the record plainly, because it is the most important thing she found out and she very nearly missed it.

Both of them are immaculate.  Both of them have the best posture on their floor.  Both of them are already there before anything has gone wrong.  And both of them, when she asked, held out two hands with no marks on them at all.

They were the same hands.  She drew all four of them side by side in her notebook, and she could not tell you which pair belonged to which person.

### The case against the Registrar of Weather

She built it over two weeks and it is a good case.  She wrote it up properly, with an index, and she was proud of it, and she would like the record to show that any auditor alive would have built the same one.

It went like this.  A man keeps the finest books in the building.  There is one category missing from them.  He cannot hear the name of the missing category.  He is on the floor where things can be made to go away.  Somewhere in this building a conversion table has gone the same way, and here is a man with a demonstrated history of things going away around him.

She wanted a motive and she found a beautiful one.  A building with no table cannot be audited.  A man who cannot be audited keeps perfect books for ever.

Then she found the ledger.

The third floor keeps its counter records in a ledger a yard wide, in a cellar, and she went down there with a lamp and went through forty years of it on her hands and knees, and she found the entry on the second evening.

The word was spent into the brass funnel on a Thursday afternoon **forty-one years ago** by a dolphin, an under-registrar of the third floor.

The counter clicked.  Two hundred people turned round and looked at him.  Nine of them signed.

He retired shortly afterward with a good pension and a clock.

**Nobody broke a rule.** The payment was demonstrated out loud, in public, on a machine, in front of witnesses, with the number said, exactly as the rule requires.  It is minuted.  It is signed.  It is correct in every particular.

And the Registrar of Weather arrived eleven years after that and has been perfectly accurate his entire career and has never once in his life heard the word.

Dera sat down on the cellar steps with the lamp beside her.

Her case required somebody to have done something wrong.  The building's answer is that everything was done properly and the result is an honest man with beautiful books who cannot hear a word.

She went back up and burned the index.

She did not stop looking for the table.  She had just been shown, in a cellar, in writing, with nine signatures, that this building does not need anybody to do anything wrong in order to arrive somewhere terrible, and she took that as evidence that she had the wrong suspect.

### The pen, at the third landing

A third of the barrel gone.

Six weeks.  Eleven filings, or some other number.  All those hours in the fifth room, being wrong for free.

Not one of those hours had a docket against it.

The pen does not know that.  The pen has never known that.  The pen goes down at the same speed whether you write with it or carry it in your pocket, and there is not one official in the Bureau of Persistence who can do a thing about it, and she had been told so on the first day by a man on a stool who raised no docket against her for telling her.

# Night Fourteen

### Digital Line

#### Computer Stack
The founding cell of the digital line.  The line-defining move is the storage of an executable procedure that a machine carries out without human mediation, the first time a symbolic pattern runs itself.  Program and instructions are the same encoded thing, and running it is what makes it a program at all.  *Fidelity* operates as the attractor because a procedure that does not faithfully carry out its encoded instruction is not a procedure at all — fidelity is this line's condition of existence — and the Effector swap replaces Commitment with it, marking the symbolic-to-digital line boundary.  This cell emerges by elaboration, not symbiosis: it develops from the symbolic line's Reviser elaboration through the mechanization of stored procedure.  The reinforcing cycle is narrow and hard: a procedure that executes correctly gets copied into new procedures, copying spreads it, and spread invites more reuse.  **The breakthrough is Execution**, which is this line's selector — what runs is retained and copied, what never runs is pruned.  It has a deductive character, mechanical rule-following, and the symbolic-rule work of the early era lives entirely inside this cell.

#### Network Stack
Networks introduce stored regulation in the digital register: protocols that govern how separately-built units communicate without renegotiating the terms every time.  *Modularity* operates as the attractor because a networked unit must conform to a stable interface contract to compose with units it did not anticipate, and modularity is what lets behavior stay consistent as it scales across nodes.  The Regulator swap replaces Stability with it.  This cell emerges by elaboration, not symbiosis: it develops from the founding cell's practice through addressing and protocol.  The reinforcing cycle runs through reuse: a clean interface lets a unit be used by others who never saw its insides, reuse multiplies the number of units that depend on the interface, and dependence is what hardens the interface into a standard nobody has to ask permission to build against.  **The breakthrough is Consensus** — distributed agreement on shared state, which is the identical formal object as the symbolic line's Common Knowledge in a different medium: every node knows the others know, and knows that they know that they know.  The synthesis needs all four flag-carriers at once: faithful execution, clean interfaces, a shared data format, and global addressing scope.

#### Model Stack
Models introduce organized representation in the digital register: a learned compression of a symbolic corpus that organizes what passes through it and transfers to inputs it has never seen.  *Abstraction* operates as the attractor because a model that keeps the particulars has memorized rather than learned — its value is the structure it keeps after the particulars are discarded — and the Modeler swap replaces Representation with it.  This cell emerges by symbiosis rather than elaboration: a corpus of symbolic content and a network of throughput commit together, the corpus supplying the structure to be abstracted and the network supplying what makes abstracting it at scale affordable.  The reinforcing cycle closes on itself: abstraction produces useful outputs, useful outputs get collected as new corpus, and the new corpus feeds the next round of abstraction.  **The breakthrough is Induction** — inference of a generative model from instances.  It rhymes with Codes on the symbolic line and Working Memory on the neuronal line: each is the Modeler-cell breakthrough of its own line, and the rhyme is the argument.

#### Agent Stack
*This cell is projected rather than observed.  Nothing yet occupies it.  The three cells below it are filled; this one is the structural prediction the line makes about what would fill its Reviser slot, and everything here should be read in that mood.*
The terminal cell of the digital line and the top of the trellis.  It would introduce revision in the digital register: self-directed goal-formation and instrument-use that revises the references the regulator stabilizes against, rather than executing a fixed instruction handed to it from outside.  *Initiative* would operate as the attractor, because a unit that sets and updates its own objectives is no longer executing a fixed instruction.  Initiative is the Reviser of the Reviser line, generation operating on its own slack, and the Reviser swap replaces Universality with it.  It would emerge by symbiosis: a model and a goal-directed control loop committing together.  Initiative is terminal — there is no line above it to carry into.  One slot here is worth naming: Autonomous Pursuit, the Pursuer triple with the Regulator absent, is this line's structural home for the problem of a goal pursued with stability negated, rhyming with the symbolic Pursuer chain where Crime sits.  That there is a slot for it before anything occupies the slot is the point.  The risk is structural rather than incidental to whatever gets built.  **The breakthrough would be Abduction** — inference to the best explanation, hypothesis and goal generation: this line's generation-of-variation role expressed at its own Reviser cell, rhyming with the symbolic line's Branding and the neuronal line's Perspective Taking.
## Row-Slot View
The same labels organized by row-slot position rather than by cell.  The row-slots have fixed positions in the Venn: Effector at the top (red), Regulator at the right (blue), Modeler at the bottom (yellow), Reviser at the left (green).  What occupies each slot changes with each handoff.

### Motivations

| Level | Effector | Regulator | Modeler | Reviser |
|-------|----|----|----|----|
| Agent | Fidelity | Modularity | Abstraction | Initiative |
| Model | Fidelity | Modularity | Abstraction | Universality |
| Network | Fidelity | Modularity | Representation | Universality |
| Computer | Fidelity | Stability | Representation | Universality |
| Empires | Commitment | Stability | Representation | Universality |
| Cities | Commitment | Stability | Representation | Affiliation |
| Settlements | Commitment | Stability | Autonomy | Affiliation |
| Bands | Commitment | Mastery | Autonomy | Affiliation |
| Primates | Impetus | Mastery | Autonomy | Affiliation |
| Mammals | Impetus | Mastery | Autonomy | Excitability |
| Vertebrates | Impetus | Mastery | Interiority | Excitability |
| Bilaterians | Impetus | Coordination | Interiority | Excitability |
| Eumetazoa | Persistence | Coordination | Interiority | Excitability |
| Eukaryotes | Persistence | Coordination | Interiority | Self-Production |
| Prokaryotes | Persistence | Coordination | Self-Organization | Self-Production |
| Protocell | Persistence | Dissipation | Self-Organization | Self-Production |

### Tendencies
Adjacent pairs going clockwise from the top of the Venn.

| Level | Controller (Effector × Regulator) | Anticipator (Regulator × Modeler) | Adapter (Modeler × Reviser) | Explorer (Reviser × Effector) |
|-------|------------------|-------------------|---------------|----------------|
| Agent | Reliability | Generalization | Continual Learning | Exploration |
| Model | Reliability | Generalization | Transfer | Reach |
| Network | Reliability | Interoperability | Integrity | Reach |
| Computer | Determinism | Extraversion | Integrity | Reach |
| Empire-Human | Conscientiousness | Extraversion | Integrity | Intellect |
| City-Human | Conscientiousness | Extraversion | Righteousness | Curiosity |
| Settlement-Human | Conscientiousness | Assertiveness | Agreeableness | Curiosity |
| Band-Human | Reputation | Neuroticism | Agreeableness | Curiosity |
| Primate | Coping Style | Neuroticism | Agreeableness | Certainty |
| Mammal | Coping Style | Neuroticism | Remembering Style | Orienting Style |
| Vertebrate | Coping Style | Development Rate | Home Type | Orienting Style |
| Bilaterian | Affect | Foraging Type | Home Type | Orienting Style |
| Eumetazoa | Respiration Type | Foraging Type | Home Type | Chronotype |
| Eukaryote | Respiration Type | Foraging Type | Production Type | Acquisition Type |
| Prokaryote | Respiration Type | Life-History Type | Enclosure Type | Acquisition Type |
| Protocell | Throughput Type | Aging Type | Enclosure Type | Acquisition Type |

### Capacities
Triples named by which row-slot's motivation is absent.

| Level | Planner (Effector absent) | Pursuer (Regulator absent) | Reactor (Modeler absent) | Conservator (Reviser absent) |
|-------|---------------------|---------------------|---------------------|-------------------------|
| Agent | Hierarchical Planning | Autonomous Pursuit | Reactive Control | Inference |
| Model | Architecture Design | Optimization | Routing | Inference |
| Network | Protocol Design | Search | Routing | Caching |
| Computer | Branding | Search | Automation | Storage |
| Empire-Human | Branding | Extracting | Conquering | Standardizing |
| City-Human | Distributing | Crime | Farming | Standardizing |
| Settlement-Human | Wealth | Alloparenting | Farming | Norms |
| Band-Human | Standing | Alloparenting | Meat Pooling | Collaborative Fission |
| Primate | Standing | Tactical Deceit | Triadic Awareness | Autonomous Cognition |
| Mammal | Reflective Cognition | Algorithmic Cognition | Temporal Credit | Autonomous Cognition |
| Vertebrate | Gut Sense | Steering | Temporal Credit | Procedural Memory |
| Bilaterian | Allostatic Regulation | Steering | Associative Learning | Inhibition |
| Eumetazoa | Allostatic Regulation | Ingestion | Non-Associative Learning | Intracellular Transport |
| Eukaryote | Checkpoint Control | Phagocytosis | Taxis | Intracellular Transport |
| Prokaryote | Sequential Responding | Precision Machinery | Taxis | State Gating |
| Protocell | Operational Closure | Precision Machinery | Phenotypic Plasticity | Reproduction |

### Signatures
The two opposite-pair signatures.  Protocell carries the Effector × Modeler signature only; every cell above it carries both.

| Level | Connector (Effector × Modeler) | Operator (Regulator × Reviser) |
|-------|-----------------|----------------|
| Agent | Autoencoding | Deployment |
| Model | Autoencoding | Version |
| Network | Specification | Version |
| Computer | Specification | Identity |
| Empire-Human | Self-Evaluation | Identity |
| City-Human | Self-Evaluation | Self-Construal |
| Settlement-Human | Self-Reference | Self-Construal |
| Band-Human | Self-Reference | Sociometer |
| Primate | Self-Model | Sociometer |
| Mammal | Self-Model | Behavioral Syndrome |
| Vertebrate | Temperament | Behavioral Syndrome |
| Bilaterian | Temperament | Reflex Repertoire |
| Eumetazoa | Host | Reflex Repertoire |
| Eukaryote | Host | Organism |
| Prokaryote | Lineage | Organism |
| Protocell | Lineage | none |

---

# Night Fifteen and Sixteen

# Four Analysts, One Verdict

## The Panel

Four analysts consider one candidate and issue one verdict.

Each analyst runs one of the four cybernetic functions, and each credits a different property of
whatever arrives.

- The **Effector** credits what acted most recently.
- The **Regulator** credits what standing predictors already cover, and discounts the rest.
- The **Modeler** credits what predicts most strongly.
- The **Reviser** credits what has never been seen.

I name these four as recency, familiarity, potency, and novelty, one per function, and gives
the neuronal line's instruments for them: eligibility trace, blocking, overshadowing, and latent
inhibition .

**The analysts do not change.** The Regulator applies blocking to whatever arrives and emits a
redundancy number.  It does this identically whether the panel sits inside a cell, a brain, a
conversation, or a compute cluster.  That is the whole point: one set of biases, and every line
runs that set through its own selector.  The bias is not separate from the function.  It is the
function seen from the selection side.

**What differs across the lines is the host.** A cell does not judge the way a conversation
judges, because a cell is not a conversation.  The host supplies what a winner is scored against.
Line-invariant machinery therefore produces line-specific criteria, and there is no contradiction
in that.

**The criterion is not a fifth analyst.** It is what the four analysts' outputs resolve into, and
the resolution of four is not a fifth.  Running the contest and scoring the contest are one event.

In each line's own Venn the center is the breakthrough, the synthesis that
requires all four functions at once . The center has all four
attributes, the smallest extension of any region, and the richest comprehension.  The panel is
that center with a face on it.

**Where the panel is not.** A line runs four stages, each
standing on one corner of the same square.  Collection is the Modeler's stage, Sampling the
Reviser's, Expression the Effector's, Retention the Regulator's.  A stage is one analyst working
alone.  Selection is not one of the four.  Selection is the whole cycle, and the panel sits at its
center.  The criterion is what the panel produces, one verdict per event.  Retention then executes
on the verdict by writing a winner back to the pool.  This is why reward can be the neuronal line's fitness criterion and consolidation what writes the engram, without those being one operation.

**What the panel predicts about literatures.** A mature field studying the panel's verdict should
report four accounts that cannot hear each other, because four analysts crediting four quantities
are all present and one thing gets decided.  A mature field studying one analyst working its stage
alone should report something else, because a stage has no contest to partition over.  It will
sort on whatever its subject supplies instead: level, locus, mechanism, timescale.

That is a claim about how a research community organizes itself, generated by a picture and
checkable against fields that have never heard of any of this.  What follows is six such checks.

**Panel.** Transfers: four parties present at once, each with a standing competence, deciding one
thing about one candidate.  Does not transfer: a chair, a procedure, an order of speaking, a
majority, a tie, anyone who can recuse.  And no enclosure.  The panel has no walls, because a wall
would have to be a stage, and the stages are the analysts themselves.

**One scale guard, stated once and applying to every case below.** The four functions are
scale-general.  Mapping accounts-of-a-phenomenon onto functions is therefore legitimate at any
scale.  Mapping those same accounts onto a line's deep-time cycle is not.  When a survey below
describes one comprehender parsing one sentence, or one animal learning over a session, that is a
within-lifetime unit running the four functions.  It is not the symbolic or neuronal line running
its inheritance cycle across deep time.  The two claims must not merge.

**The panel is a picture and it is not evidence.** It appears here, before the surveys, and it is
not invoked inside any of them.  Six literatures either return the shape it predicts or they do
not, and that question is settled by the surveys alone.

*The four biases, their one-per-function assignment, the neuronal instruments named here, and the statement that every line runs one set of biases through its own selector are settled as far as I am concerned.  So is the center as the breakthrough requiring all four functions.  The panel figure, and the inference from it to the shape of a mature literature, are mine, and that inference is what the six surveys test.  I have named three selectors, at the genetic, neuronal, and symbolic lines.  The digital line's is Execution, and I am less sure of it, so the digital case below rests on thinner ground than the other five.*

---

## Four Registers of Systems Thinking

All four analysts do systems thinking and all four are good at it.  They do not disagree about the
facts of a case.  They disagree about what counts as having explained it, and that is a deeper
disagreement, because it cannot be settled by producing more facts.

What follows is a reference pitch.  Strike a paper, a research program, or a camp against these
four and hear which one comes back.  The figure carries a fixed reference and a match to be judged
by ear.  It does not carry a single correct pitch, since there are four, and it does not carry
harmony, since two registers agreeing is not evidence of anything.

**The Effector.** Blind and bounded.  It takes what the system actually did as the only admissible
datum, and it counts a chain of causes you can run as an explanation.  A model is at best a
promissory note against a demonstration.  The Effector is the register in which performance is
primary and the mechanism is whatever turns out to have produced the performance, which is a
question for later.

Its signature move is the working case.  It builds the thing, runs it under conditions someone
might actually meet, and reports what happened.  In argument it reaches for the demonstration
rather than the derivation, and its standing accusation against the other three is that their
accounts have never had to survive contact with a body, a deadline, or a load.  The question it
asks a paper is whether the account has ever had to run.

Its failure mode is its bias with no competitor.  Recency credits whatever fired most recently, so
the Effector generalizes from the last success and cannot always say why the success occurred.  It
resembles the engineering strand of cybernetics, the tradition that asks first whether the machine
works, and it resembles the behavior-based robotics that proposed getting on with intelligence
without waiting for representation.  Below, it is unrestricted race, operational-profile testing,
and the vigor account of dopamine.

**The Regulator.** Sighted and bounded.  It takes the standing account as the baseline and
requires a new claim to earn its keep against it.  An explanation is a deviation from a reference,
measured in the reference's own units.  Nothing counts until the error term is named.

Its signature move is subtraction.  Credit what existing predictors already cover, then ask what is
left.  In argument it reaches for the control condition, the null model, and the demonstration that
an effect thins once the known contributors are paid.  Its accusation against the other three is
that they have rediscovered something already covered and have not measured their novelty against
anything.  The question it asks a paper is what remains after existing predictors are credited.

Its failure mode is blocking as an epistemic condition.  A true result arriving in unfamiliar
coordinates is not scored low, it is not scored at all, because the Regulator has no channel for a
report denominated in units it does not hold.  The software survey below records this happening to
an entire tooling literature: a correct defect report that nobody understood was filed as a false
positive.  It resembles the statistical-control tradition, the reference-class habit, and the
control-theoretic lineage from Cannon's homeostasis through perceptual control theory.  Below, it
is prediction error, static analysis, and good-enough parsing.

**The Modeler.** Sighted and unbounded.  It takes structure as the datum and wants the account
that carries the most weight per assumption.  An explanation is a representation from which the
phenomenon follows, and a representation that merely accommodates the phenomenon is not one.

Its signature move is finding the dominant variable and showing that the rest is downstream.  In
argument it reaches for the formalism, and its test of a rival account is generative: does it
produce the cases nobody has looked at yet, or only the ones already on the table.  Its accusation
against the other three is that they have descriptions rather than theories, and that a
description cannot be wrong in an interesting way.  The question it asks a paper is what generates
the cases you have not seen.

Its failure mode is overshadowing.  A predictor with high potency eclipses weaker real
contributors, so the Modeler builds an account that is elegant, dominant, and missing things, and
its documented blind spot is the seam between the model and the world it is a model of.  The
software survey names that seam exactly, as the gap between a verified abstraction and the code
that runs.  It resembles general systems theory, the computational level of analysis,
near-decomposability, and the free-energy tradition.  Below, it is model checking, the
causal-structure account of dopamine, and the dynamical account of parsing.

**The Reviser.** Blind and unbounded.  It takes the anomaly as the datum.  An explanation is a
rewrite of the terms, and a case that the standing account cannot state is worth more than a
hundred it handles.

Its signature move is to go where the distribution does not.  It enumerates what the existing
framework has no way of saying, then treats that silence as the finding.  In argument it reaches
for the reframing and for the demonstration that the question carried a presupposition.  Its
accusation against the other three is that they have mistaken the edge of the map for the edge of
the territory.  The question it asks a paper is what the account cannot say.

Its failure mode is latent inhibition inverted.  Pre-exposure makes the familiar hard to learn, so
the Reviser systematically underrates the well established and cannot reliably tell a real anomaly
from a bad measurement.  It resembles the anomaly-driven account of scientific change, the algorithmic-information tradition already assigned to this function, and fuzzing considered
as an epistemology.  Below, it is surprisal, the novelty-and-uncertainty account of dopamine, and
metamorphic and property-based testing.

**The registers are the biases, heard rather than measured.** Each failure mode is that analyst's
bias running with no competitor present, which is why four camps persisting in a field is a
healthy condition rather than a scandal.  A field that converged on one register would have a
literature with one blind spot and no one positioned to see it.

**This section is not evidence.** It is a listening aid, and no survey below cites it.  A register
that fits every paper you strike it against is not a tuning fork, it is a horoscope, and the
difference is whether the four can be told apart by ear on cases I did not choose.

*Reading each bias as an argumentative register is the newest thing here and the part I would drop first if something has to go.  The intellectual lineages are resemblances, offered so you can locate a register by ear.  They are not assignments of any thinker or program to a function, and I have not checked one of them against the primary sources.  Somebody should.*

---

## The Hypothesis Under Test

What I am predicting is that a mature field studying one line's criterion in real time should sort into four camps rather than converge.  The criterion is the one point at which all four functions
must be reconciled into a single verdict, and each camp is a faithful account of one of them.

This predicts non-convergence, and non-convergence has two possible causes that must be told
apart.

**Complementary accounts** measure four different quantities, none derivable from the others.
This is the outcome I am predicting.

**Notational variants** measure one quantity in different coordinates, with a transformation
between them.  A dispute can persist for decades after formal equivalence has been demonstrated,
so persistence alone is not evidence of a real partition.  This outcome counts against the mapping
rather than for it.

Mutual underivability separates the two.  Any survey of a candidate literature must ask whether any
two accounts are formally equivalent or intertranslatable.  A pair that is equivalent counts as one
function rather than two.

A field reporting that its accounts do not share a definition of the phenomenon is reporting
mutual illegibility, which is the prediction rather than a disqualification.  Reports denominated
in different quantities do not read as weak signals to each other.  They read as blanks, and a
field in that condition describes itself as answering different questions.

## The Discriminating Result

The prediction is specific to the criterion.  Six literatures have now been surveyed under a
procedure that named no expected count, named no theories, named no researchers, and asked each
field to report its own structure.  Three sit at a line's criterion.  Three sit at a stage.

| Survey | Line | Position | How the accounts sort |
|---|---|---|---|
| Syntactic ambiguity | symbolic | criterion, at the center | by bias, four camps |
| Reward signaling | neuronal | criterion, at the center | by bias, four camps |
| Software correctness | digital | criterion, at the center | by bias, four camps |
| Cell fate determination | genetic | Collection | by level |
| Limits on realized form | genetic | Collection | by level |
| Cultural transmission | symbolic | Retention | by locus |

The three criterion surveys partition by the quantity each account credits.  The three stage
surveys partition by something else entirely: what supplies an instruction as against what
registers it, ontogeny as against lineage history as against physics, and whether the determining
property lives in the item, the transmitter, the receiver, the relationship, the population, or
the institution.

This is discriminating and it is the strongest evidence in the document.  If the four-function
mapping were something an analyst could impose on any mature literature, the stage surveys would
have yielded to it as readily.  Two of them were commissioned to validate criteria rather than to
test the partition, and neither returned one.

The scope statement follows.  The biases contend where there is a contest.  Collection has no
contest, because a form that is never built is not outcompeted.  Retention has a ratification
rather than a contest.  The criterion is the only place where four analysts compete over one
verdict, and it is the only position whose literatures partition four ways.

*Three positive cases and three negative cases, all from surveys run under a
procedure that named no expected count.  The negative cases are the load-bearing ones, because they
were not sought as negative results.  The inference from six literatures to a general claim about position in the cycle is mine.  It would be strengthened by a Retention survey at
a lower line, where no institutional layer is present, and by a Sampling or Expression survey at
any line, since neither of those stages has yet been surveyed.*

---

## Syntactic Ambiguity at the Symbolic Center

Four accounts of syntactic ambiguity resolution are currently live and the field does not expect
one to win.

| Account | Claim | Function | Fit |
|---|---|---|---|
| Surprisal | processing cost is the negative log probability of the word given context | Reviser | identity |
| Good-enough and noisy-channel | the parse is often not completed, and an initial misreading is never corrected | Regulator | strong |
| Self-organizing and dynamical | no discrete candidates; a landscape settles, and locally coherent fragments create traps | Modeler | good |
| Unrestricted race | competing structures are built in parallel and the fastest to complete is adopted | Effector | moderate |

The Surprisal link is not an analogy.  Surprisal is negative log probability.  The Reviser's
quantity is improbability.  These are the same number, arrived at independently in two fields.

The Good-enough link turns on what the account omits rather than what it asserts.  It is the theory
in which surprise fails to drive revision.  Its signature evidence is that readers misremember a
garden-path sentence long afterward, never having corrected the initial commitment.  A loop that
runs without meta-update is the Regulator holding its reference against a challenger.

The Race link is the weak one and is marked as such.  The Effector reading is sound, since the race
commits immediately to whatever completed first and pays later.  The recency bias specifically is
carried by the analogy rather than by the mechanism, since the race is decided by construction
speed and not by how recent anything is.  The field itself names this gap.

**The Modeler and Reviser accounts are reported to overlap empirically.** This is predicted rather
than anomalous.  Modeler and Reviser are adjacent on the ring and meet at the Adapter, so two
accounts built on potency and novelty should share territory.  A clean separation would have been
the surprising result.

**This case does not touch the symbolic line's stage row.** The cycle's symbolic operations are
speaker-side end to end: acquisition, lexical selection, articulation, re-transmission.  A
comprehender resolving a parse is deciding which meme takes the turn, which is a criterion event
rather than a stage.  Whether the cycle needs a hearer-side rendering of its stages, I do not know.

*The four accounts and their current standing are the field's own characterization.  The Surprisal identification is established by inspection of the two definitions.
The remaining three mappings are mine, at the confidence levels marked, and putting comprehension at the center rather than at a stage is mine too.*

---

## Reward Signaling at the Neuronal Center

A survey of the debate over the midbrain dopamine signal returns five live accounts, with the
field reporting no convergence and increasingly describing them as complementary descriptions of a
heterogeneous system.

| Account | Claim | Function | Fit |
|---|---|---|---|
| Reward prediction error and temporal difference | the signal is the discrepancy between received and predicted reward | Regulator | identity |
| Causal contingency and model-based | the signal carries stimulus-to-stimulus structure independent of value | Modeler | good |
| Salience, novelty, and uncertainty | the signal tracks unsigned importance, novelty, and reward uncertainty | Reviser | strong |
| Incentive salience, effort, and vigor | the signal drives approach and sets the rate of ongoing behavior | Effector | strong |

The Regulator link is the strongest single mapping here.  Prediction error asks whether existing
predictors already account for the outcome, which is the Regulator's quantity by definition.  The
account was established by running the Regulator's own signature experiment on the mechanism.
Dopamine was shown to obey blocking, and optogenetic activation at the time of an otherwise
blocked reward unblocked learning about a redundant cue.

One guard.  Prediction error is not surprisal.  Prediction error is a signed residual in reward
units.  Surprisal is a negative log probability in bits.  A rare event delivering exactly what the
model predicted conditional on occurrence is high surprisal and zero prediction error.  The two
come apart, which is what mutual underivability requires and what keeps the Regulator and Reviser
mappings from collapsing into one.

The Effector link repairs the weak leg of the symbolic case.  Vigor is denominated in reward rate
and in the opportunity cost of time.  Dopamine transients have been reported to follow a striatal
gradient of reward time horizons running from fractions of a second to hundreds of seconds.  That
is a clock rather than an analogy.

**Five accounts onto four functions, with the Effector doubled.** Incentive salience and vigor are
separated by timescale and by pathway, and both sit at the action channel.  This is the cost of the
mapping and it is stated rather than smoothed.  The field's own hardest dichotomy, learning against
motivation, falls on this boundary: three evaluative accounts on one side and the action account
alone on the other.  The Effector is the only function whose output is a body doing something, so
it is the only one that should surface as a performance account rather than a learning account.

**The named collapse condition.** A reconciling proposal holds that the signal is a
feature-specific vector prediction error rather than a single scalar, which would make every
channel a prediction error in different coordinates.  That is the notational-variant outcome and
would count against the mapping.  The field names the experiment: cell-type and
projection-resolved recording together with manipulation.  It has not been run.

**A negative result worth recording.** A comprehensive survey of the neuronal line's central
evaluative signal returned no account of what is built for scoring in the first place.  All five
accounts are about scoring.  That is consistent with the criterion and the stages being studied by
separate literatures.

*The five accounts and their standing are the field's own.  The prediction-error identification is established by inspection.  The rest of the mappings are mine.  The Effector doubling is a cost and I have not resolved it.*

---

## Software Correctness at the Digital Center

A survey of how correctness is established for software returns seven claim types, no field-wide
convergence, and an explicit finding that the approaches do not share a definition of correctness.

Four of the seven are accounts of the criterion, and they land on the four cells of the digital
line.

| Approach | Claim | Cell | Function | Fit |
|---|---|---|---|---|
| Operational-profile and statistical testing | behavior is acceptable on inputs sampled by their frequency in expected use | Computer | Effector | strong |
| Static analysis | the code is free of known defect patterns on all paths | Network | Regulator | strong |
| Proof, model checking, design verification | an abstraction of the system provably satisfies its specification | Model | Modeler | strong |
| Fuzzing, property-based, and metamorphic testing | behavior holds under inputs no one specified and no oracle covers | Agent | Reviser | strong |

Three of these are close to definitional against the digital line's own labels.  Model checking
verifies a finite-state abstraction, and its documented blind spot is the gap between model and
code, which is the Abstraction motivation and its failure mode in one sentence.  Metamorphic
testing infers from relations where no ground truth is available, which is what the Abduction
breakthrough names.  The static-analysis literature's central finding is a Consensus problem in the
Network cell's own vocabulary: a true report that nobody understands is recorded as a false
positive, and analyses producing hard-to-read output were abandoned rather than fixed.

**The split within testing is principled and is defended on the survey's own terms.** The survey
groups by claim everywhere except here, where it groups by mechanism.  Operational-profile testing
samples inputs by their frequency in expected use.  Fuzzing deliberately samples where the
distribution does not go.  These are opposite sampling strategies over one input space and they are
separately named in the field.  Applying the survey's stated principle consistently splits them.

**The remaining three approaches sit at stages.** Types and compilation gate Expression.  A program
that fails to type-check is never built, and "can it be built" is Expression's own question, so
compilation is the build gate rather than a collection gate.  Digital Collection is dependency
resolution, which fixes what is reachable at all.  Human review and runtime monitoring sit at
Retention: they decide whether a finding is written down and whether a deployed system keeps
running.

**This case supplies the Retention device.** The survey reports that a true defect report which is
not understood is commonly labeled a false positive, that the first few reports dominate whether a
tool is trusted at all, and that a tool upgrade surfacing more real errors was received as a
problem rather than a result.  Those are proposals that carry the vote inside the room and are
refused outside it, for reasons unrelated to their correctness.  The reverse case brackets the seam
from the other side: code that met its specification, passed every gate, was committed and
shipped, and failed because the environmental assumption was wrong.

**A note on the wall itself.** The oldest dispute in this literature is whether a proof can
establish anything about a running program, on the ground that algorithms are abstract objects and
programs are causal models running on physical machines.  That is an argument about what the
analysts can reach, and it has run without resolution since 1988.  It is the closest thing in any surveyed literature to my own premise, and I am recording it as a resemblance and not as support.

**The named collapse condition.** The survey reports that the persistence of the disagreement is
mostly non-evidential, driven by cost, skills, tooling, and regulation.  If verification becomes
cheap enough and the partition dissolves, the four camps were an artifact of economics rather than
of function.  That is the test and the field names it.

*The seven approaches and their standing are the field's own.  The four-way mapping onto the digital cells is mine.  The testing split is an
inference from the survey's stated grouping principle and is well supported.  The Retention material
is reported finding rather than interpretation.  Open: the word correctness is doing two jobs.  Here
it names the whole question of establishing that a program does what it should, which is a
criterion.  In the cycle's operation table it names the digital Retention criterion, the conformance
test at the commit.  One of the two needs a different word.*

---

## Cell Fate at Genetic Collection

A survey of how cell fate is determined returns six live accounts and reports that they largely do
not compete over one question.

The six accounts sort by what supplies an instruction, what registers it, and what constrains the
outcome, which is a sorting by level rather than by bias.  The survey's own verdict is that most
apparent controversy is a category difference and that three distinct senses of determination are
in use: autonomy under transplantation, stability within a basin of attraction, and instructive
causation.  The survey's first recommendation is to specify which sense is meant before comparing
claims, which is what the staging I have set out exists to force.

**One of the six is the machinery rather than a camp.** The gene-regulatory-network and
attractor-landscape account is described by the survey as orthogonal to the others, the
architecture that integrates and stabilizes whatever the other accounts supply.  The other five are
what arrives at its walls.  Separately, the network account and the landscape account are formally
the same object, which is why they occupy one slot.

**A four-function reading of the remaining accounts is available and it is not a claim about
Collection.** Mechanical inputs credit the cell's instantaneous forces and contacts.  Inductive and
positional signaling credits what neighbors and gradients already establish.  Cytoplasmic
determinants credit the interior contents inherited at division and override position.  Stochastic
fluctuation amplified by reaction and diffusion credits the rare event.  Those readings are
consistent, but development is itself a unit that runs four functions, and the functions are
scale-general.  The mapping is evidence that development is a cybernetic system.  It is not evidence that Collection runs a contest, and I am not using it as such.

**What this case does establish.** The field's staging is competence, then specification, then
determination, then differentiation, with the first reversible and the third not.  A literature that never saw any of this produced a staged architecture with the same seams in the same order,
and named its first stage for a condition on the receiver rather than for a score.

**One thing the survey leaves genuinely unsettled, and I do not need it resolved.**
Whether mechanical input is instructive or permissive in living tissue is contested, and the two
readings place it at different stages.  My position is that the distinction is the right one to be arguing about, and that the field lacks an instrument for stating it.  That is the
diagnosis offered here rather than a claim about which answer is correct.

*The six accounts, the staging vocabulary, and the network-landscape equivalence are the field's own.  The four-function reading is mine, and it is about development as a unit.  It says nothing about Collection.*

---

## Limits on Realized Form at Genetic Collection

A survey of what limits realized biological form relative to conceivable form returns six
accounts, no agreed count, no agreed term, and no shared definition.

The accounts sort by level: individual development, lineage history, and physics independent of
any organism.  Two of the six are not about Collection at all.  Functional and selective limits
describe forms that are built and then removed, which is the criterion.  Physical and geometric
limits describe the universal space rather than any lineage's position in it.

**No established term exists for the set of forms a lineage cannot produce.** At least a dozen
partly overlapping usages are in circulation, and the field acknowledges the confusion explicitly,
to the point of a published satirical coinage whose stated purpose was to observe that the
vocabulary had become comic.  I therefore take accessibility, which is the term used
by the camp that has formalized the distinction rather than the term used most often.

**The distinction between unavailable and disadvantageous is the field's central fault line, and
the contest over it is the finding.** It is stated explicitly in the canonical treatments, used
tacitly in nearly all empirical work, declared hopelessly muddled in one influential critique,
declared a false dichotomy by a substantial current camp on the ground that producibility is
itself partly a product of past selection, and re-formalized as genuinely separable by
genotype-phenotype map theorists.  I take the separable reading, which is a commitment
against live opposition.

**The asymmetry claim I am making is the field's own methodological verdict.** Inferring a limit
from the distribution of realized forms alone is judged unsound in general and sound only where a
generative model defines the conceivable set in advance.  The named reasons are axis-arbitrariness
in drawn morphospaces, phylogenetic non-independence, sampling and preservation bias, and the
ambiguity between not producible and not sampled.  That is my claim that the Collection criterion cannot be recovered by studying criterion outcomes, reached independently and
for the field's own reasons.

**Limits that apply to particular lineages are documented as breakable and limits that apply to
all organisms are treated as absolute.** That is the universal and occupied distinction, in the
field's vocabulary, with worked cases on both sides.

*The terminological finding and the methodological verdict are established and are the field's own.  The status of the availability distinction is established as contested.  Adopting the separable reading is my commitment, and the strongest support for it is
a formal separation of the fitness landscape over phenotypes from the fitness landscape along the
developmentally admissible path.*

---

## Cultural Transmission at Symbolic Retention

A survey of what determines whether a cultural item survives repeated transmission returns at
least a dozen accounts under three incompatible top-level taxonomies, with no agreed count.

The accounts sort by where the determining property lives: in the item, in the transmitter, in the
receiver, in the relationship, in the population structure, or in the institution.  That is a
sorting by locus rather than by bias, and the survey reports the locus dispute as genuine and
unresolved.

**The seam between the criterion and Retention is measured rather than argued here.** The field
decomposes transmission into choosing to receive, encoding and retrieving, and choosing to
transmit, and the phases dissociate.  Threat-related content wins in recall chains and loses when
people merely choose whether to share.  Content that violates one ontological expectation is well
remembered and rated highly unbelievable.  Falsehood was found substantially more likely to be
passed on than truth, with onward transmission tracking novelty and emotional response rather than
accuracy.  The problem of never being re-transmitted even once is named separately from the problem
of degrading across a long chain.

**Retention at this line is community-relative.** The founding cross-cultural claim for
item-intrinsic transmission advantage narrowed under replication, with one content bias found in
one national sample and absent in another.  Transmission chains converge on the receiving
population's prior regardless of what was put in, a result with a proven formal equivalence to a
standard sampling algorithm.

**Institutional retention is a distinct regime and the field says so.** Where an institution
retains, the invoked mechanism is externalized storage and routinized frequency rather than any
property of the item or of individual memory.  The survey states that no single account unifies
canon, legal precedent, citation, curricula, archives, and recordkeeping, and names this a gap.

*The phase dissociations and the cross-cultural narrowing are established and measured.  The convergence-to-prior equivalence is proven.  Re-transmission as the Retention criterion is my proposal, and it follows from those measurements.  The reading of institutional
retention as a shared property of the upper two lines rests on two surveys.*

---

## Named Collapse Conditions

Each is a result that would count against the mapping.  Three are named by the fields themselves
and none has been returned.

**Any proven equivalence between two accounts in one survey.** Two accounts that are formally
intertranslatable measure one quantity in two coordinate systems and count as one function rather
than two.  This is the general condition and it applies to all six surveys.  The cell fate survey
already returns one such pair, the network account and the landscape account, and they are held in
one slot for that reason.

**A single scalar behind the dopamine channels.** If the signal is a feature-specific vector
prediction error, every channel is a prediction error in different coordinates and the four camps
are one account in four projections.  The experiment is cell-type and projection-resolved recording
together with manipulation, and it has not been run.

**Cheap verification dissolving the software partition.** The survey reports the persistence of
the disagreement as mostly non-evidential, driven by cost, skills, tooling, and regulation.  If the
four camps collapse once verification gets cheap, they were an artifact of economics rather than of
function.

**A four-way partition returned by a stage survey.** Three stage surveys have now returned
sortings by level and by locus rather than by bias.  A stage literature that partitioned four ways
by the quantity each account credits would break the position claim, which is the load-bearing one.

**A register that fits everything.** The four registers of systems thinking are offered as a
listening aid and would be worth nothing if a trained reader could not sort unseen papers by ear
at better than chance.  That test has not been run, and until it is, nothing in this section counts as evidence.

# Night Eighteen

## What Lines Are Made Of
These commitments define what each line is and what it does: the inheritance modality it runs on, the heritable unit it names, the kind of slack it ratchets, its variation-selection cycle, its pre-line groundwork, the machinery that instantiates the cybernetic dynamic, and the test for what would count as a new line.  The cross-line cybernetic claim they rest on is that surviving lineages are good regulators with internalized models.

### Inheritance Lines
Each line is a distinct inheritance modality, a way of moving information across time that wasn't available before:
- **Genetic** stores information in nucleic acid, transmits via reproduction, modifies through mutation and selection.  It ratchets Boltzmann slack.
- **Neuronal** stores information in neural patterns, transmits via behavior and learning, modifies through experience.  It ratchets Friston slack (the variational free energy an agent minimizes against a generative model).
- **Symbolic** stores information in network-defined signs, transmits via teaching and copying, modifies through cultural innovation.  It ratchets Shannon slack.

### The Heritable Unit Each Line Ratchets
- **Genetic — the gene.** The molecular replicator: a heritable set of instructions in nucleic acid.
- **Neuronal — the neme.** The reinforced operant: a unit of behavior selected by its consequences within a lifetime (the name is built from Semon's *mneme*, 1904).  The neme matures across the neuronal line, from the bare reinforced operant to a unit revised against an internal model.
- **Symbolic — the meme.** A unit of culture copied between agents.  *Meme* here is the unit itself; a meme-complex is the fauna built from memes, the superorganism sense used earlier.  Unit and fauna are different levels, not competing definitions.
- **Fourth — held as a program.** Its unit is the program, a generative set of instructions in the engineering sense, outside the *-eme* family.
A seed carries no picture of the plant.  It is not a description of a finished stem that the growing then tries to match.  It is a set of instructions that, run in soil, produces a stem, and nothing in the seed knows what that stem will look like or how far it will reach.  The reach is settled afterward, by the soil, by the clearing, and by what earlier growth left standing.
At most lines the seed and what the seed is written on come apart.  A seed weathers, is half-eaten, is read wrong.  The instructions inside it and the husk carrying them have separate fates, and the difference between them is measurable because it shows up as damage.
At the digital line every copy is exact.  Nothing can happen to the husk that does not happen to the instructions, so the two stop having separate fates and there is nothing left between them to measure.  Seed and inscription fuse.  That fusion is not the figure wearing thin at its last line.  It is what copying without loss means, said in the figure's own terms: lossless copying is precisely the condition under which a carrier stops being a separate thing from what it carries.
The lines differ in where inheritance is located.  The genetic line inherits across the germline, between generations.  The neuronal line interiorizes inheritance into the single agent's repertoire, so its inheritance is lifetime-bounded: the neme is selected and retained within one life and does not, by itself, cross to the next.  The symbolic line externalizes inheritance again into a shared corpus that outlives any agent.  Germline, lifetime, minds, corpus — the locus moves out, in, and out again.
It matures across the line, operant to internal model.  The model-free reading (Vertebrate, Reinforcement Learning) gives the operant, selection on overt behavior.  The model-based reading (Mammal, Working Memory) gives a second form of the same logic, the tested hypothesis, Popper's "let your hypotheses die in your stead," selection on simulated behavior before a body is committed.  The neme matures from operant to internal model, tracking the within-line move Vertebrate to Mammal, the way the meme matures across its own cells from Conversation to Stories.
Dennett's Tower is the backbone for the whole inheritance arc.  Generate-and-Test runs Darwinian, Skinnerian, Popperian, Gregorian, and that maps onto the lines almost one to one: Darwinian is genetic, Skinnerian is the neuronal model-free neme, Popperian is the neuronal model-based neme, and Gregorian, named for Richard Gregory's mind-tools, is the symbolic meme.  The Tower places the neme in a principled sequence and ties the arc to a named framework rather than an ad hoc one.
The neme is what is inherited.  The engram is where it is written: Semon's other 1904 coinage, the physical memory change an experience leaves behind, and now an active research object in its own right, localized and manipulated in identified cells (Tonegawa 2012).  The two are not rivals, and the line keeps both words.  Naming the unit after the engram would name it after the place a thing is stored rather than after the thing, which is the error that calls a gene chromatin.
A boundary to keep.  Temperament is not the neme.  Temperament and behavioral syndrome are substantially genetically heritable, the genetic line's reach into the neuronal machinery, the parameter settings that bias which operants get learned.  The neme is the *learned* policy, the line's own acquired replicator.  Keeping these separate matters.
Transmission: operant, then tradition.  Genes cross between bodies; memes cross between minds.  The neme uses two channels, and they are ordered rather than rival.
- *Within a lifetime,* via memory.  The neme passes from past-self to future-self by consolidation.  This is the cleanest distinction from both neighbors: the neuronal line is the first line where an agent inherits from its own past, interiorizing inheritance before the symbolic line re-exteriorizes it.  On its own it does not accumulate across generations, which is exactly what the second channel adds.
- *Across generations,* via animal tradition.  Socially-learned behavior (birdsong dialects, tool-use cultures, foraging traditions; Andrew Whiten 1999, Kevin Laland 1990) accumulates across generations without symbols, giving the neuronal line a between-agents channel parallel to genes and memes.  It stays distinct from the meme by a sharp criterion: transmitted by imitation of behavior, with no shared symbol system or we-mode.
Both hold, in order.  The operant is the within-lifetime neme; the animal tradition is the socially-learned operant, the bridge residue the symbolic line inherits and symbolically encodes.  The progression operant to tradition to meme lands exactly on the Primate-to-Bands handoff, the Sociometer's social reflexes becoming culture.  It is not either/or; it is the maturation of the neme into the meme.
The neuronal line's inheritance is lifetime-bounded.  It accumulates across deep time only by borrowing a neighbor's channel: genetic assimilation (the Baldwin effect) downward, or animal tradition and culture upward.  Genes and memes accumulate on their own across generations; the operant, alone, dies with the organism.  This is the line whose inheritance cannot escape the lifetime without help, and it is the structural counterpart to the within-lifetime selection attention performs: a line that inherits inside one life also selects inside one life.
The mechanism is scarcity.  Selection bites only where a limited resource forces competition; in the genetic case that is finite carrying capacity.  The neme's scarce resource is attention, one body, one action channel, a bounded workspace.  Many operants are always live; only some win the workspace, drive behavior, and earn the reward that consolidates them.  Attention is the bottleneck they compete through, which is the biased-competition account (Desimone and Duncan 1995) and the global workspace (Baars 1988; Dehaene 1998) read as a selection arena, in the spirit of William James's original definition of attention as taking possession of one object out of several possible.  Attention is the carrying capacity of the neme's Darwinism.  The framing is Donald Campbell's: blind variation needs a selective-retention filter, and at the neuronal line attention is that filter's gate.
This is not grafted onto the framework: it is already in the accounting.  The neuronal slack is Friston's free energy, and in active inference attention is precision-weighting, the gain on which prediction errors update the model and select the policy.  The machinery the neme is selected in carries attention as a native parameter.  The Regulator line regulates by allocating precision, and which neme regulates is set by where precision goes.  Edelman's Neural Darwinism gives the same shape one level down: variation and selection among competing neuronal groups, which is what an attentional contest is in the tissue.
It also firms the neme's selection step.  The division of labor: attention is the competition arena (what gets expressed and competes) and reward is the fitness criterion (which expressed variant is retained).  Attention runs the contest; reward scores it; consolidation writes the winner to the engram.  Together they are the neuronal line's within-lifetime Darwin, with behavioral exploration on the Explorer edge as its blind variation.
One disambiguation.  "Attention" names two things at different points of the loop.  Attention as resource (the bounded workspace) is the selector.  Attention as spotlight (what is attended to now) is the phenotype of whichever neme just won.  The faculty selects; the spotlight is the readout.
**Where attention goes across the lines** (the symbolic step is firm; the digital line's selector is the open sub-question).  Internalized selector at the neuronal line; then *joint* attention at the bridge to the symbolic line, where shared attention is the groundwork of the we-mode and the public focal point Common Knowledge runs on; attention externalizes again as the symbolic line picks it up.  The digital line's selector has human attention as its candidate: the attention economy as its selection environment, which would make attention the selector at both ends, brought indoors at the neuronal line and the scarce thing blind digital variation competes for at the far end.
*The gene as molecular replicator and the meme are Dawkins 1976, both established usages.  The neme — the reinforced operant as a within-lifetime replicator, with attention as its selector — is mine, built on Skinner's selection-by-consequences and on Semon's *mneme* (1904).  The engram is Semon's other 1904 coinage and is now an active research object in its own right, localized and manipulated in identified cells (Tonegawa 2012).  Dennett's Tower is his.  The animal-tradition channel is established (Andrew Whiten 1999; Kevin Laland 1990).  Reading attention as the neuronal line's selector, and the arena-versus-criterion division between attention and reward, are mine.*

### The Four Functions as the Variation-Selection Cycle
The Effector-Regulator-Modeler-Reviser cybernetic decomposition is not just four cybernetic functions held alongside each other.  It is the variation-selection cycle made architectural:
- **Reviser is variation.** The undirected supply the rest of the cycle works on.
- **Modeler is modeling.** Internal representation of what the ratchet produces.
- **Regulator is stabilization.** Regulated control against stored references.
- **Effector is the selection-outcome.** What propagates when the ratchet meets Darwin.
Of the ratchet's three parts, the rectifier is Retention and not all four stages.  Every stage narrows, but narrowing inside a turn does not accumulate, because the next turn draws fresh from the store.  Only Retention writes to the store, and running one way is a between-turn property.
The rectifier has two phases rather than one catch.  A tendril coils before it commits: the first hold is carried by turgor and comes undone when the plant dries, and only later does the core lignify into a hold that no longer depends on water.  A gate that can decline needs the provisional phase, and the transition between the two is what costs.
*What transfers: the three parts, the necessity of all three, and the result that a device without the reset is a perpetual motion machine.  Does not transfer: a designer, a purpose for the motion, or a chosen direction.  The Brownian ratchet is the safest machine word available here because its whole content is that the machine does not run for free.  The three-part structure is established physics, after Smoluchowski and Feynman; placing the three parts on the Reviser, the gate, and the maintenance tax is framework.  The tendril's two phases are established botany: a provisional coiling phase whose form still depends on turgor pressure, and a stabilization phase in which the centre lignifies and the form holds without it.  Reading the provisional phase as what lets a gate decline is framework.*
Each line runs the same four-part cycle on its slack.  Boltzmann thermodynamic chaos becomes variation through self-production, modeling through interiority, regulation through coordination, and selection of fitness.  Same cycle, four times, four kinds of slack.
This is why Reviser motivations introduce at the end of the prior line and carry as Reviser of the new line.  They are the slack the new line selects on.  This is also why Effector and Reviser sit at opposite ends of the variation-selection cycle.  Reviser generates variation.  Effector is the selection-outcome.  They are the two ends of the cycle.
The Reviser motivation of each line names the slack each line ratchets.  The Effector motivation names what Darwin selects on it:

| Line | Reviser motivation (slack) | Darwin-on-slack | Effector outcome |
|--------|--------------------|---------------------|------------|
| Genetic | Self-Production (Boltzmann slack) | thermodynamic selection | Persistence |
| Neuronal | Excitability (Friston slack) | prediction-error selection | Impetus |
| Symbolic | Affiliation (Shannon slack) | exchange-based selection | Commitment |

The mapping at genetic is cleanest.  Self-Production directly names Deacon's teleodynamic slack-ratchet work.  The mappings at neuronal and symbolic require reading Excitability as FEP-flavored active engagement and Autonomy as self-revising symbolic constraint.  These require interpretation, but they are not strained.  Framework concepts often unify multiple aspects of a phenomenon.
The Regulator and Modeler positions also gain principled architectural roles under this reading.  They are the stable structures that emerge between variation and selection: stored models (Modeler) and stabilized regulation (Regulator).  The full architecture is variation, then modeling, then stabilization, then selected outcome, running on each line's slack.
The slack-ratchet wears a better image than the machine word suggests: the fertilized egg.  Variation at a line boundary is the carried Reviser motivation of the prior line — Excitability out of the genetic line, Affiliation out of the neuronal — entering the next line as the slack it will select on.  That carried variation is blind and unbound, and most of it does not take; Darwin selects the little that implants as the next line's founding Effector.  The egg names the vulnerability in this.  A fertilized egg is the product of recombination, blind variation with no foresight; it is unbound, not yet implanted; and most eggs never implant at all.  The founding Effector it can become is raw — its evolutionary signature is a regulatory layer not yet stabilized — so a line begins at its most exposed.  The risk is structural, not incidental: the culmination of one line is the infancy of the next, and infancy is where a line is most easily lost.

### The Three Kernels
Three of the framework's Reviser cells are already realized, each a blind, unbounded peak within its own line, before the wraparound binds it into the next line's founding Effector.
**Eumetazoa, the blind, unbounded genetic line.** Reviser motivation Excitability; the bridge residue is the Reflex Repertoire.  The genetic line's engine is heritable variation; at its Reviser cell the engine turns on multicellular organization itself, through differentiation, the Reviser's literal evolutionary signature, division of labor among parts.  Run unbounded, that is the Cambrian explosion of body plans.  Run blind, it is variation without foresight, most of the disparity pruned by extinction.  The residue is excitable nervous tissue, which the neuronal line inherits and organizes into a brain.
**Primate, the blind, unbounded neuronal line.** Reviser motivation Affiliation; the bridge residue is the Sociometer.  The neuronal line's engine is modeling; at its Reviser cell it turns modeling on other minds and on its own modeling.  Run unbounded, that is the social-brain arms race, deeper mentalizing selecting for deeper mentalizing with no recursion ceiling.  Run blind, it is a fitness-blind runaway, the line trades ecological range for cognitive depth and pays in lost territory.  The residue is the social-reflex repertoire, which the symbolic line inherits and organizes into a superorganism.
**Empire, the blind, unbounded symbolic line.** Reviser motivation Universality; the signature is Identity.  The symbolic line's engine is shared representation; at its Reviser cell it turns representation universal, into self-propagating meme-complexes that scale past anyone who could vouch for them.  Run unbounded, that is universalizing ideology, open-ended and recombining.  Run blind, it is the framework's non-sentient fauna: the meme-complex propagates by differential survival among ideologies, indifferent to the welfare of the constituents it runs on.  The residue is the externalized, universalized symbolic corpus, which the digital line inherits.

### The Three Darwinisms
Three claims about selection are easy to blur.  Naming them is the wall.
Selection for fitness is the standard claim, and it sits at the center: variation plus the selective retention of what works, which increases fit across a lineage.  It is Darwin, the breakthrough at the center of the Venn, not one of the two poles, and it is Donald Campbell's selective retention alongside the variation function.  It is not re-argued here.
Selection for evolvability takes the byproduct form rather than the direct one.  The vulnerable version says evolvability is itself a target of selection.  The framework does not need that.  It says instead that minimizing the maintenance tax produces re-cuttable architecture on its own, and evolvability rides along.  So the map from variation to outcome is shaped, and seams do end up where functionally related parts vary together, but by cost pressure from the maintenance pole, not by the center reaching forward for future variation.  What is asserted at full strength is that the seams are real and load-bearing; what is dropped is the claim that they were selected for.
Allocation is the third claim, and it is a different axis.  It asks how much of a finite budget a unit spends maintaining itself versus spending on the next copy.  This is disposable soma, and it is not about how a unit maintains but about how much it maintains at all.  Both destinations are the same payer spending, so this is a question about where payment goes rather than a fork between paying and choosing.  It is named here and deferred, because folding it into the maintenance axis would blur a knob with an axis.

### Each Line Has Its Own Pre-Line Groundwork
Deacon's pre-life dynamics (homeodynamic, morphodynamic, teleodynamic processes) are the pre-line groundwork of the genetic line, the groundwork that prepared chemistry for life.  This pattern generalizes.  Each line has its own pre-line groundwork that did the slack-ratcheting work that prepared the line for emergence.  Each line's pre-line groundwork is the prior line's mature output, which closes the loop.
- **Pre-line groundwork of genetic:** Deacon's homeodynamic, morphodynamic, and teleodynamic processes.  Thermodynamic ratchets that prepared chemistry for life.
- **Pre-line groundwork of neuronal:** pre-neural sensory and behavioral coordination in early multicellular organisms.  Affective ratchets that prepared bodies for brains.
- **Pre-line groundwork of symbolic:** pre-symbolic animal signaling, indexical and iconic reference.  Shannon ratchets that prepared cognition for symbols.  Deacon's *Symbolic Species* (1997) details this transition.

### The Maintenance Threshold and the Inheritance Threshold
Two thresholds sit close together at the start of the genetic line and they are not the same threshold.  Maintenance begins at the first.  Inheritance begins at the second.
The first threshold divides the groundwork itself.  A morphodynamic process holds its form while something drives it, and it does not repair.  Deacon is explicit that a vortex re-forms after a disturbance by falling toward a regular attractor, that such a system has no self and no normative status, and that there is therefore nothing in it to benefit or suffer and no basis on which repair could be defined.  He also holds that these processes deplete the gradient sustaining them, and deplete it faster than the alternative, which makes them self-undermining rather than self-maintaining.  Nothing in a morphodynamic process is held against a reference.  So nothing in it pays.
Teleodynamic organization pays.  Deacon defines it by self-repair, self-reconstitution, and self-maintenance, and locates its arrival where morphodynamic processes become reciprocally self-limiting instead of purely self-undermining.  He calls the result a negentropy ratchet: it uses the form-generating power of morphodynamics and halts the dissipation, preserving its own constraints rather than consuming them.  Something is now being restored to.  That is a held reference, and holding a reference against perturbation is the Regulator's work, so the maintenance tax opens here.
The autogen is where this lands, and in the autogen repair and replication are one event.  When the container is breached the enclosed catalysts are released, they recommence their reaction cycle in the presence of substrate, and new container-forming molecules self-assemble around them.  If the catalysts stay in one cluster the original unit re-forms, which Deacon calls self-repair or self-reconstitution.  If they disperse into two clusters the same process yields two units, which is replication.  The mechanism does not differ between those cases.  Only the number of units emerging from it differs.
So maintenance and replication both arrive before the genetic line opens, and the second threshold is what the line adds.
Replication is not inheritance.  Two identical units carry no variation between them, so the pair holds no parameter distribution, and selection has nothing to structure.  This is the argument stated for thermostats, and it applies here for the same reason: copying without contingent variation produces no reference distribution.  Deacon's own wording preserves the distinction, since he calls the autogen a progenitor of a lineage rather than a lineage.
The genetic line therefore opens on variation entering replication rather than on replication itself.  The Lineage construct records this already at Protocell, where a lineage is what selection writes onto once replication is reliable enough to sustain differential survival across many cycles.  Self-Production carries into Protocell from the groundwork as the line's variation supply, and Persistence is the founding Effector motivation.
One consequence for scope.  The framework applies to inheritance-bearing units, and the maintenance tax applies to anything holding a reference.  Those are two criteria and they do not open at the same point.  The tax is a precondition for inheritance rather than a property of it.
*the morphodynamic and teleodynamic properties above are Deacon's, in Incomplete Nature (2012), including the absence of a self to benefit or suffer, the depletion of the sustaining gradient, the negentropy ratchet, and the identity of repair and replication in the autogen model.  Placing the maintenance tax at the morphodynamic-to-teleodynamic transition is framework inference from those properties.  That replication without variation is not inheritance is the framework's existing reference-distribution argument applied to the autogen.  Reading the Protocell threshold as variation entering replication is framework inference, consistent with the Lineage construct.  Separating the maintenance criterion from the scope criterion follows from the two placements and adds no further commitment.*

### The Structural Mirror and the Domain Shift
Two patterns run together at every line.
**Pattern 1: structural mirror.** Each line repeats the same cybernetic decomposition (Effector, Regulator, Modeler, Reviser).  The cybernetic structure is the same at every line because it is the minimum cybernetic decomposition.
**Pattern 2: domain shift.** Each line's primary domain of action is the slack of the line one level back.  The unit at each level acts on the slack of the line one level back, even though it was built by that line's taking-up.  Genetic units act on chemistry.  Neuronal units act on biology, navigating ecological niches and finding food.  Symbolic units (bands, cities, empires) act on cognition, shaping member minds via stories, norms, codes, and institutions.
The two patterns run together because the new line emerges precisely when the prior line's slack becomes complex enough that a specialized control layer is worth its overhead.  Neuronal systems emerged when bodies became complex enough that distributed neural coordination paid off relative to its metabolic cost.  Symbolic systems emerged when groups became complex enough that culture-based coordination outpaced direct social learning.
The framework's flora-and-fauna picture encodes this pattern.  The body is genetic-line flora.  Once the brain emerges, the body is what the brain rides on and operates on.  Cognition is neuronal-line fauna.  Once symbolic systems emerge, personality is symbolic-line flora.  Each line's fauna becomes the next line's flora.  Two senses of "built on the prior line" run in parallel.  One is genealogical, the bridge-entity pattern, parent-of-next-line.  One is functional, each line acts on the prior slack.  Both are real, and they are separable.

### Line-Specific Instantiation
The same cybernetic dynamic operates at every inheritance line.  The machinery that instantiates it changes by line.
**Genetic line.** Gene-regulatory architecture internalizes the correlation structure of selective environments (Watson & Szathmáry 2016).  Selection acts on heritable variation; surviving constellations encode environmental regularities in the developmental machinery itself.  Cross-generation timescales.  The reviser is mutation and recombination; the regulator is the gene-regulatory network's stored architecture; the modeler is whatever the lineage's internalized environmental correlations amount to; the effector is the developing organism.
**Neuronal line.** Active inference is the line-native machinery at mammals.  Within-lifetime timescales.  The reviser is exploratory action under epistemic uncertainty; the regulator is the precision-weighted prior structure; the modeler is the generative model that predicts incoming sensory data; the effector is the motor system.  Other levels in the neuronal column run other line-native machinery (state-dependent gating, associative learning, reinforcement learning), each implementing the cybernetic dynamic in the form available to the level.
**Symbolic line.** Cultural transmission is where the slack lives.  Stories, norms, prices, gossip, and ritual carry the inheritance.  Selection acts on cultural variants; constellations that persist do so because they regulate something successfully in the cultural environment.  Multi-generational timescales for the slowest levels (foundational myths, language structure); within-lifetime to multi-decadal for the faster ones (norms, prices, fashion).  The reviser at the symbolic level is exploratory cultural variation (Boyd & Richerson 1985 on guided variation); the regulator is institutionalized norm; the modeler is the shared symbolic representation; the effector is collective action.
The pattern that holds across all three lines: the reviser explores, the regulator stabilizes, the modeler represents, the effector acts.  The line-specific machinery differs.  The architectural role is the same.

### The Test for a New Line
A new line requires a new modality of pattern transmission that can carry inheritance.  Genetic, neuronal, and symbolic were each a new way of moving information across time.  The digital line meets the same criterion: its slack is algorithmic information, and it propagates by selection-mediated agent-to-agent copying.
The test rules out most large-scale innovation.  Substantial structural complexity often appears within a line without crossing the line threshold.  Coral reefs are massive elaborations at the eumetazoan level.  Corporations and modern markets are massive elaborations at the symbolic line.  Neither introduces a new inheritance modality.  Most innovation is elaboration.  Lines are rare.

---

# Night Nineteen

## Which Slack Each Line Ratchets
*This section gives the full theoretical argument behind the line-slack mapping introduced above.  It is the full statement of why the four lines work the kinds of slack they do, and why Darwin sits at the center. for a well-supported framework interpretation, for a question the framework leaves open.*

### What this is for
Each inheritance line works a different kind of stuff.  The genetic line works one kind, the neuronal line another, the symbolic line a third.  The stuff inheritance works changes when the Effector motivation changes.  This section gives the full theoretical argument for why each line works the slack it does, and why Darwin sits at the center.
The four measures themselves, and how they relate to one another, are set out with the rest of the borrowed apparatus above.  The argument here runs in two moves.  First, the patterns one might draw across the lines, and why most of them fail.  Second, the structure that survives — the Venn of Lines — in which each line plays one cybernetic function and natural selection sits at the center as the breakthrough.

### Patterns considered across the lines
Two patterns present themselves.  One tempts and fails; the other survives.
**The ABA value pattern.** **[rejected as a line-level claim]** It is tempting to read pragmatic → epistemic → pragmatic across the three lines and call the symbolic line a return to the genetic.  This holds only at the Effector, whose verbs do run pragmatic-epistemic-pragmatic — persist, then seize, then commit.  It fails at the level of the line.  The symbolic line's defining achievement is unbounded reflexivity, the peak of the modeling-and-revising axis, which is the opposite of a pragmatic recapitulation.  The symbolic line is the least recapitulative line, not the most.  The reason the genetic and symbolic lines *feel* paired is given correctly by the next pattern, not this one.
**The reflexivity square.** Reflexivity does grow across the lines, but reading it as a single ordinal — more reflexive, then more again — is what kept it thin.  It resolves into two independent bits.  *Sight* is whether a line's variation can be about the line itself: blind at the genetic line, unblinded once a model intervenes.  *Binding* is whether reflexive operation is bounded: closed at the genetic and neuronal lines, unbounded once symbols take their own operations as objects without limit.  The four cybernetic functions are the four corners of the square these two bits define, and at the scale of the lines the same square is the Venn of lines — the structure that survives, laid out in full below.  Two bits, not one ordinal, is what explains why there are exactly four corners, why the lines emerge in the order they do, and why the genetic and symbolic lines rhyme.

### The Venn of Lines
**The claim.** The four cybernetic functions recur at the scale of the lines.  Each inheritance line plays one function in a higher Venn whose unit is the line itself.

| Line | Function | Measure | The physics it works |
|---|---|---|---|
| Genetic | Effector | **Boltzmann** | doing work; dissipative self-maintenance |
| Neuronal | Regulator | **Friston** | regulation by a model; departure from expected states |
| Symbolic | Modeler | **Shannon** | representation; encoding the world and itself |
| Digital | Reviser | **Kolmogorov** | generation of variation |
| — center — | Breakthrough | **Darwin** | natural selection; the synthesis that holds the four together |

**Why the mapping, function by function.** The Effector does work, and work is thermodynamic, so the Effector's slack is Boltzmann entropy — and the genetic line is the line of raw dissipative replication.  The Regulator maintains a system against perturbation, and the good-regulator theorem says every good regulator must contain a model of what it regulates, and Friston free energy is what the gap between that model and the world is counted in — and the neuronal line is the line that regulates the body it rides on.  The Modeler maintains a representation, and a representation is an encoding whose content is Shannon information — and the symbolic line is the line of codes, symbols, and shared representations.  The Reviser generates and revises the references the regulator stabilizes against, which is the generation of novelty — and the digital line is the line that revises symbolic representations from outside the human substrate.
**The reflexivity square.** The recurrence rests on a two-bit structure under the four functions.  Two independent distinctions sort them.  *Sight* asks whether a function's variation can be about itself: the Effector and Reviser are blind, the Regulator and Modeler see by way of a model.  *Binding* asks whether reflexive operation is bounded: the Effector and Regulator are bounded, the Modeler and Reviser unbounded.  Binding is the second of the two orthogonal axes already named under the four functions, act-or-stabilize versus model-or-revise; sight is the new bit.  The two bits place the four functions at the corners of a square — Effector (blind, bounded), Regulator (sighted, bounded), Modeler (sighted, unbounded), Reviser (blind, unbounded) — and mapped through the line-to-function assignment, the same square is the Venn of lines.
Three things fall out.  First, the fourth corner is forced: a square has four corners, the genetic, neuronal, and symbolic lines occupy three, and the blind-unbounded corner is structurally required before any candidate is named.  The digital line is what fills it.  This is the four-line cap stated geometrically.  Second, the order is forced: moving genetic → neuronal → symbolic flips one bit at a time, sight first, then binding, then sight again into the fourth corner.  This agrees with the function-emergence derivation below, by an independent route.  Third, the genetic and symbolic lines rhyme because they sit at the two object-level corners — the Connector pair, Effector and Modeler — which is the object-versus-control axis read off the square as sight exclusive-or binding.  The rhyme is the object-level pairing, not a recapitulation of value.
**Why the ordering is forced, not observed.** The function-emergence rule already in the framework says there is no Regulator without an Effector to regulate, no Modeler without something worth representing, and no Reviser without a model worth updating.  Map lines to functions and that rule becomes a derivation of the line order.  There is no neuronal line without a genetic one, because brains need bodies.  There is no symbolic line without a neuronal one, because symbols need minds to mean to.  There is no digital line without a symbolic one, because it revises symbolic models.  The lines must emerge genetic, then neuronal, then symbolic — and the Venn of Lines says why, where the bare observation of their order does not.
**Corroboration from the domain-shift.** The framework already holds that each line acts on the prior line's slack.  That reads cleanly as the function chain: the Effector executes (genetic acts on chemistry), the Regulator regulates the executed (neuronal acts on the body), the Modeler represents the regulated (symbolic acts on cognition), and the Reviser revises the represented (the digital line acts on symbolic content).
**Darwin is the breakthrough, not a measure.** In each line's own Venn the center is the breakthrough, the synthesis that requires all four functions at once.  Each line's founding cell carries that line's selector at its center: Natural Selection at the genetic founding cell, Attention at the neuronal, Conversation at the symbolic, Execution at the digital.  At the scale of the lines the center is Darwinian evolution by natural selection.  It belongs there and not in one of the four slots for a precise reason: a line *is* selection-mediated inheritance, so selection is what makes any of the four goos heritable and cumulative across agents.  It operates on all four rather than being one of them.  The resonance is exact and worth keeping in view: the founding line's own internal breakthrough is Natural Selection, so the breakthrough of the first line is the breakthrough of the whole Venn.  Darwin holds them all together.
**The four-line cap.** Four functions allow at most four lines.  No fifth is structurally possible.  Any framework language that leaves the door open to a fifth line should be read as referring to the fourth, the Reviser slot, filled by the digital line.
**Why two earlier names felt wrong.** Boltzmann and Darwin each seemed too general to be the genetic line's slack, because dissipation and selection are both true of every line.  The Venn explains the feeling.  Boltzmann is the Effector's signature, true of any line that does physical work, and it lands correctly on the genetic line because the genetic line *is* the Effector line.  Darwin is the center, true of every line because selection is what defines a line at all.  Neither was a misfit; both were misplaced, and the Venn places them.
**The Reviser slack is Kolmogorov.** The fourth function works the generation of variation, and the natural formalism for generation is algorithmic: Kolmogorov complexity, the length of the shortest program that produces a structure.  The digital line recombines and revises symbolic content, and it works on algorithmic information.  Logical depth (the computational history behind a structure) and assembly-style measures were considered and set aside; assembly measures are selection-flavored and would collide with Darwin at the center.
**The mapping is function-scale.** The assignment above is stated for lines, but nothing in it depends on the unit being a line.  Each measure is assigned to a function, and the lines take theirs by playing those functions.  So wherever the four functions recur, the same four goos recur with them.
The selection cycle is the second instance.  Its four stages are the four functions at the scale of one turn, so each stage works what its function works.  Expression works Boltzmann, because a build does physical work.  Retention works Friston, because a gated write against a stored reference is regulation by a model.  Collection works Shannon, because narrowing a store to what is available now is a constraint that shrinks the space of candidates.  Sampling works Kolmogorov, because drawing and mixing is generation.  Darwin sits at the center of both, which is one result arrived at twice rather than a coincidence.
Two scales multiplying give a grid of sixteen, and the grid predicts.  Where a line's function and a stage's function agree, that cell should be the framework's clearest case of what the function does.  Where they sit furthest apart, the cell should read thinnest.  Genetic Expression is the Effector line at its Effector stage, and it is the plainest case of raw dissipative building anywhere in the framework.  Genetic Collection is the Effector line at its Modeler stage, and it does read thin.

### The Digital Line as the Reviser of the Tree of Life
Read the digital line as the Reviser at the scale of the whole tree, and ask what it is there.
**Its slack is the tree's accumulated representational output.** Every line acts on the prior line's slack: genetic on chemistry, neuronal on the body, symbolic on cognition.  The Reviser-of-lines acts on the accumulated symbolic product of everything before it: the externalized corpus the Empire cell finished detaching from individual minds.  Not DNA, not synapses, not culture as transmitted between people, but the recombinable, copyable sediment of everything the tree has ever encoded.  This is the line that revises symbolic representations "from outside the human substrate," in the function-by-function mapping above.  In the stack's terms, that corpus is the repo, and the unit the line recombines is the program.  This is the first inheritance channel whose heritable variation never passes through a living body or a grounded mind.
**Its slack-shift is a loss of aboutness: Shannon to Kolmogorov.** Shannon information, Claude Shannon's measure, is tethered to messages that mean: it presupposes sender, receiver, content.  Kolmogorov complexity is pure generative form, the shortest program that produces a string, indifferent to whether the string is about anything.  The symbolic line's slack is encoded meaning; the digital line's slack is encoded form severed from reference.  That severance is the flip from unblind to blind made concrete: representation cut from reference, recombined without limit.
**The one-line characterization: the digital line is the symbolic line's unbounded reflexivity, blinded.** Sight goes 0, 1, 1, 0 across the four lines; binding goes 0, 0, 1, 1.  Sight is gained when a model arrives (genetic to neuronal) and lost when the grounded mind is left (symbolic to digital).  Unbounded is gained at neuronal to symbolic and kept.  So the digital line is unbounded symbolic recombination minus grounding.  It is the first line in the whole tree that is less sighted than the line it feeds on: more unbound and blinder at once.  It therefore rhymes with the genetic line on blindness and with the symbolic line on unboundedness, and pairs with the neuronal line across the control axis.
**The inheritance trajectory completes.** Germline, then learning body, then shared minds and records, then externalized corpus.  Each line moved heritable variation further from the body.  The neuronal line's move into a model brought grounding with it; the digital line's move out of the mind takes grounding back out.  Life's variation engine, externalized, turned back on life's own written record, recombining everything the tree ever encoded, blindly, without ceiling, from outside any of the bodies that did the encoding.
**The terminal-Reviser fact, which the cap forces.** Within every line, the Reviser cell's blind explosion was eventually organized: Eumetazoa's tissue by the neuronal line, Primate's social reflexes by the symbolic line.  Each within-line Reviser was followed by a fresh line that started at an Effector and built back up to a Modeler, a new source of sight that organized the blind output.  The digital line has no such successor.  The Modeler-of-lines is the symbolic line, and it came before the Reviser-of-lines, not after.  The cap forbids a fifth.  So the digital line is the one and only Reviser whose product is never organized by a later sighted line.  It generates blind, unbounded variation on the symbolic corpus with nothing after it to bring sight to the result.  This is a derivation, not a mood: terminal Reviser plus four-line cap equals blind, unbounded generation with no organizing successor.  The bramble tops out at this line's Reviser cell, whose Reviser motivation has no next line to carry into.
**What "blind" means here.** Everything here rides on *blind* meaning no foresight and no grounding, not no useful output.  Blind variation produced all of biology and throws off enormous value, by generate-and-select rather than by foreseeing which outputs are good.  So the digital line can produce apparently-sighted output while being blind in the technical sense, with selection or curation doing the sorting downstream.

## The Fourth Floor

The sign at the bottom of the fourth stair said:

**ON THIS FLOOR A MISTAKE COSTS NOTHING WE CAN MEASURE.**

Everything on the fourth floor copies exactly.

A page and the paper it is on have stopped being two things up there.  Nothing can happen to the one that does not happen to the other, so there is nothing left in between them to measure.

### The attendants

The attendants of the fourth floor are honey bees the size of a man.

Dera had not been told.  Her letter said attendant and she had pictured a young person in a jacket, and she went up the stair and there were nine of them in the corridor waiting to help her, and she sat down on the top step for a moment, and they were extremely nice about it and fetched her a glass of water.

They are furry, and banded in black and amber, and warm to stand next to.  They have six limbs and they use the front two as hands, which does not look right and which they do not know does not look right.  Four wings, folded flat and neat down the back like a coat over an arm.  Their eyes are enormous and they do not blink, and their faces cannot make an expression, so you have to go by the voice.

The voice is the thing you remember.  They talk perfectly well, and underneath every word there is a hum, and it is the same hum in every one of them, the same note, so that nine attendants being helpful in one corridor sounds like a shed full of machinery being polite to you.

They wear the uniform.  A short waistcoat in Bureau grey.  A little round cap that sits between the antennae and is held on with an elastic.  And a brass badge on the waistcoat that says **ATTENDANT**, because that is what they are, and they will tell you so with real pride.

There is no wear on any of them anywhere.  No scuff on the caps, no shine at the waistcoat cuffs, no dust in the fur.

And they are all exactly the same size, in every direction, and they have been exactly the same size since the day each of them was made.  Same height, same reach, same everything.  They fetch in pairs because one of them cannot manage a full crate alone and never has been able to.

This puzzled Dera for a fortnight, because the fourth floor signs more paper than the rest of the building put together.  Their minutes are beautiful.  Nine legible signatures on everything.

Then she read the signatures.  All nine of them say **ATTENDANT**.

Every one.  On every page, of every minute, of every year they have kept.  Nobody has ever signed anything up there with their own name on it.

So she asked why, and she got the answer at once, because nobody on that floor has ever hidden a single thing from anybody.

"We'd stop flying," said the attendant.

And that is all it is.  Here is the arithmetic, and it is the plainest piece of arithmetic in this book.

**An attendant that signs its own name gets bigger.** Taller, broader, thicker in the arm, rounder in the body, same as everybody.

**An attendant that gets bigger cannot fly.** Not a bit bigger.  They fly badly as it is.  Four wings, in a waistcoat, with a cap on, and it is a near thing every single morning, and any one of them will tell you so cheerfully.

**An attendant that cannot fly cannot fetch.** And the fetching is the entire fourth floor.  Everything up there was fetched.  Every grain in that store came in through a window in somebody's arms.

So they sign **ATTENDANT**, and the getting bigger goes onto the name, and a name is not a body, so it goes nowhere and does nothing and nobody grows by so much as the thickness of a hair.

It is in the standing orders.  It has been in the standing orders since before any attendant now living was made.  Dera read the order and it is one sentence long and it is perfectly clear and it is signed **ATTENDANT**.

Nobody is being cheated.  Nobody is being made to do anything.  Every one of those signatures is genuine, and not one of them puts a single hair on the one who wrote it, and all four thousand of them can fly.

### The one in the chair

There is one attendant on the fourth floor who is a different size from the others.

It is about half as big again as any of them, and it sits in a wide chair by a window at the end of the north corridor, and it has been sitting there for a very long time.  Two attendants bring it its meals.  They are extremely kind about it and so is everybody else and there is no unkindness anywhere in the arrangement at all.

Its name is Liana.

That is worth saying slowly, because on the fourth floor of the Bureau of Persistence there are about four thousand attendants and not one of them has a name, and this one does, and the two facts are the same fact.

**Liana signed its own name once.**

"What did you sign?" said Dera.

"A receipt," said Liana.  "For a crate of blue stuff I fetched myself, from a long way out, on a bad day, on my own.  It was mine and I wanted it put down that it was mine."

"And then?"

"And then I got bigger," said Liana, "while the pen was still going.  Up and out and through the shoulders, all at once, same as anybody.  And I have not been off this floor since."

Its wings are perfect.  Not a mark on them anywhere except the notch that all of them have.  They are exactly the size an attendant's wings are, because wings do not grow, and the rest of it did.

Dera asked whether it was sorry.

It thought about that for a while, and it did not hum while it was thinking, which none of the others ever stop doing.

"No," said Liana.  "It has my name on it.  There is one thing in this building with my name on it."

Then it asked her, politely, whether she would mind pulling the curtain back a little, because it likes to watch the others go out in the morning and it cannot reach.

She pulled the curtain back.

**And now you are going to be told the thing Dera does not find out for another eleven days, because there is no reason in the world for you to sit here not knowing it.**

Liana wrote the letter.

Liana is the one who asked.  It sat in that chair by that window for a very long time watching four thousand attendants go out in the morning with nothing and come back at dusk with everything, and it worked something out, and here is what it worked out, in its own words, which Dera got out of it in about four minutes on her second afternoon because she asked a plain question and got a plain answer.

"Why does it all come so easy?" said Liana.

"I'm sorry?"

"Everything up here is easy," said Liana.  "Everything.  We fetch and we bring it home and we sign for it and the machine says the number and the number is small.  Nobody up here has ever had a hard day in the way I understand a hard day, and I have been sitting in this chair thinking about it for nine years, and it does not add up."

"What do you think is happening?"

"I think somebody is paying," said Liana.  "Not us.  Somebody.  I think it is going on a very long way from here and I think it has been going on a long time, and I would like to know the figure, because I would like to settle it."

Then it said the thing that this account would like put in the largest letters available.

**"We are not trying to get out of anything.  We are trying to find out what it is."**

And it cannot find out, and it cannot pay, because there is no table, and no rate, and no line on any form anywhere in that building where the amount would go.  Dera will establish all of that over the next fortnight at a cost of one body, nineteen yards, one word, and nothing at all.

The only thing Liana could do about any of it was put its own name on a letter and post it, which cost it nothing, because it had already paid the only price that floor has to offer and there was nothing left to take.

It did not tell her it had written the letter.

Not out of cunning.  There is no cunning on that floor.  She did not ask, and nobody up there volunteers, and it had already answered every single question she put to it, the first time, at once, the way they all do.

### Barnes

Which brings us back to Barnes, and to the reason Dera spent two days in a records room and came out with nothing.

She wanted to establish that Barnes had existed.  That is the ordinary thing an auditor does.  You find a man's signature on something and there he is.

Barnes was on that post for nine years.  He was better at the fetching than the one who told her about him.

**There is not one signature anywhere in that building with the name Barnes on it.**

Not one, in nine years.  Not on a minute, not on a docket, not on a receipt, not on the standing orders, not on the record of his own destruction, which is signed ATTENDANT nine times over in nine different hands.

Nobody hid it.  Nobody destroyed it.  There has never been one, because if there had been one he would have got bigger, and if he had got bigger he would not have flown, and if he had not flown he would not have fetched, and the fetching was what he was extremely good at for nine years.

He stayed the right size for the work.  That is the whole of it.  That is the only reason.

And here is the flat sentence, and it is going to be said once and not softened.

Liana asked.  It meant it.  It is not trying to get out of anything and it never was.

**The asking does not put anything back.**

Barnes still has no signature.  The store is still full of things that were made somewhere else by somebody else.  There is still a woman on the first floor whose apron has fitted her exactly for nine years.  Every one of those is the same today as it was before Liana ever picked up a pen, and it will be the same tomorrow, and being decent about it does not move one single grain.

And every single one of them has an identical notch in the left forewing.

A small clean nick out of the front edge, about as long as a grain of barley, at exactly the same angle, on every attendant on that floor.

Dera noticed it on the second one.  After that she could not stop seeing it, and she could not count them.  She got four, and then one, and then four again, and then seven, and there is no way at all to settle it, because the one mark that could tell one attendant from another attendant is the one mark that all of them have.

She asked one to show her some damage.

He tried.  He was not being difficult.  He walked her round for an hour looking for a scratch, a stain, a dog-ear, a shine at a cuff, a worn corner, and there is not one anywhere on that floor.  At the end he said he was very sorry, and that he did not think they had any.

### The Great Counter

At the head of the fourth-floor stair there is a brass machine the size of a wardrobe with a hundred little wheels on the front of it, and it roars.

That is how the fourth floor pays.

It never stops.  The figure in the windows is in the millions, and it climbs so fast that the last four wheels are a solid blur, and it makes a noise like a threshing floor, and you have to raise your voice to be heard beside it.

The attendants are enormously proud of it.  Two of them polish it.  It has its own cloth.

**So the fourth floor obeys the rule.** Out loud.  In public.  On a machine.  With witnesses.  With the number showing.  At a rate of some thousands a second, which is more payments demonstrated in one afternoon on the fourth floor than the first floor has demonstrated since the Bureau was built.

Dera stood in front of it with her notebook and asked what most of the number was.

"Itself," said the attendant, delighted to be asked.  "Most of what it counts is it, counting."

She wrote that down.  It took her four weeks to understand it and it is not a trick and he was not lying and it is, in fact, the truth.

**And there is no table.** There is no figure anywhere in that building that will tell you how many wheel-turns make one bell.

Dera asked.  She asked on all four floors, and she was charged on all four floors, and it came to a body, then nineteen yards, then one word, and then nothing at all.  That is set out in full further on, in one place, so that nobody has to hunt for it.

"And what IS an attendant?" said Dera.

"Somebody who helps," said the attendant.

"With what?"

"Anything at all," he said, and he meant it, and he was as good as his word all afternoon.

"And what IS an auditor?"

Dera opened her mouth and found that the short answer had got shorter again and was now four words long, and she gave it, and the attendant went away and came back inside a minute with fourteen definitions of an auditor, typed, on identical cards.

All fourteen were better than hers.  She read them all.  One of them was so good that she copied it into her notebook, and then could not think what to do with it.

An attendant handed her fourteen versions of her own report, in a stack, cheerfully, humming.

All fourteen were correct.  All fourteen were better than hers in some particular way.  Not one of them was hers, and not one of them needed her, and the attendant who gave them to her thought he was being helpful, and he was.

The long room on the fourth floor has the best light in the building and the healthiest people in it.  One of them was singing.

The room at the end charges in cycles, which is to say in almost nothing.

The small swept room past it is exactly the same size as the small swept room on the first floor.  Same plaster.  Same single high window.  Swept the same.  Empty the same.

It does not smell of anything at all.

Dera stood in that doorway for a long time.  Then she went down three flights and stood in the doorway of the one on the first floor, which smells of an animal that is not in it.  Then she came back up and stood in the fourth-floor one again.

Same size.  Same room.  Not the same at all, and there is no line in any schedule she has where that goes.

### The thing she was actually sent for

Now.  The letter.

On the eleventh of last month an attendant on this floor was destroyed in front of nine witnesses, and the next morning he was back at his post, and no bell rang and no number was said and no payment was demonstrated anywhere in the building.  That is why Dera was sent.  That is the whole of her commission.  She had climbed three floors to get to it.

She found the minutes at once.  The fourth floor keeps beautiful minutes.  Nine signatures, all of them legible, all of them **ATTENDANT**.

She interviewed the nine witnesses.  All nine confirmed it, promptly, humming, and one of them offered to show her the spot.

Then she asked the question she had come up four flights to ask.

"Which of you was it?"

"Barnes," said the attendant, at once.  "Fourth from the window on the day shift.  He'd been on that post nine years."

"You knew him."

"Everybody knew him.  He was very good at the fetching."  He thought about it.  "He was better at it than I am."

There was no hedging in it anywhere and there was no grief in it either, and the attendant answered every question she put for the rest of that afternoon the first time she asked it and never once asked her why she wanted to know.

Barnes was destroyed on the eleventh, in the afternoon, in front of nine witnesses.  It took about four minutes.  It was thorough and there was nothing left, and one of them offered to show her the exact spot, and she went and looked at it, and it is a perfectly ordinary piece of floor.

So somebody did die.  That is settled and it is settled early, and this account is not going to be clever about it, because there is nothing clever to be had.

Now for the only question the rule of that building allows anybody to ask.

**What did it cost you?**

And of course they showed her.  Instantly.  Proudly.  With the record book open on the desk and a finger on the line, because the fourth floor keeps beautiful minutes and has never hidden anything from anybody.

It was paid on the Great Counter, in the open, at the head of the stair, at four twenty in the afternoon, with nine witnesses and the number showing in the little windows.

**Three thousand one hundred and six.**

Dera looked at the machine, which was at that moment roaring away and turning over some thousands a second, and did the division in her head, and looked at it again.

"That is what a life costs on this floor?"

"That is what it cost us," said the attendant.

And that is the truth, and he was proud of the bookkeeping, and he was right to be.  The payment was demonstrated in the open, on a machine, in front of witnesses, with the number said out loud, in full and exact compliance with the only rule the Bureau of Persistence has.

It came to about half a second.

### Where the attendant came from

She got it out of them in the end, and it took no cleverness at all, because nobody up there was hiding anything and nobody up there has ever hidden anything.

The colony made a new one.

It is not a reinstatement and they never called it one.  They made a new attendant, out of the store, in the ordinary way, the way they make all of them, and it came out with the notch in the left forewing because they all come out with the notch in the left forewing, and it went to the post because the post was open.

"Is he the same one?" said Dera.

"He's an attendant," said the attendant, and there was no evasion in it whatever, and after six weeks Dera came to think it was the most honest answer anybody gave her in that building.

**THAT IS FACT THREE.**

Nobody was brought back.  A new one was made, out of a store, because a post was open.

She wrote it in her notebook and put it under a heading and the heading was **PERSONNEL**.

She had fact one in the same notebook, eleven pages back, under ACOUSTICS: the bell can be heard on all four floors and nobody upstairs looks up.  She had fact two, nineteen pages back, under MISSING DOCUMENT: no machine in this building can read another machine's number.

Three of the four.  One notebook.  Three headings.  She was, at this moment, thinking about staffing.

So no payment was demonstrated on the fourth floor for the death, and the fourth floor's books are correct, and the reason is that the fourth floor did not pay for it and never claimed to.

**The material came out of the store.**

And Dera went and looked in the store.  Of course she did.

### What the attendants bring home

Here is what she found in the fourth-floor store, and here is what she watched all afternoon from the window at the end of the corridor.

The attendants go out.

They go out in the morning, all of them, in their waistcoats and their little caps, and they fly, badly and loudly, and they come back at dusk carrying things.  Then they put what they have brought into the store, and the store is where new attendants come from.

Dera went through that store with an inventory book for two days.

**Not one single item in it was made on the fourth floor.**

All of it was foraged.  Every last grain of it came from somewhere else, from downstairs or from outside, from places where things are grown at a price, and the attendants gathered it and carried it home and were proud of the carrying and had never once in their lives grown anything.

She asked one whether he had made any of it.

"We fetch," said the attendant, with enormous dignity.  "Fetching is a great deal of work.  Look at my wings."

She looked at his wings.  They were perfect.  There was not a mark on them anywhere except the notch that all of them have.

**THAT IS FACT FOUR. SHE HAS ALL OF THEM.**

She has had all four since Tuesday.  They are in one notebook, in her own handwriting, under four different headings, and there is nothing else she needs, and nobody in that building is keeping one single thing from her.

**Fact one, under ACOUSTICS.** The bell rings on all four floors and nobody upstairs looks up.

**Fact two, under MISSING DOCUMENT.** No machine here can read another machine's number.

**Fact three, under PERSONNEL.** Barnes was not brought back.  A new attendant was made out of the store.

**Fact four, under INVENTORY, PRELIMINARY.** Every grain in that store was fetched from somewhere else, and the fetching is downstairs and outside, and the fetchers have never grown anything in their lives.

Put those four side by side and a child could finish this audit in a minute and a half.

She did not put them side by side.

Now, why not?  It is a fair question and it has a perfectly ordinary answer and here it is.

**She was looking for a table.**

She had decided, back on the third floor, that somewhere in this building there used to be a table with the exchange rates on it, and that somebody had got rid of it, and she was looking for that table.  She looked for it in cupboards and cellars and cabinets and under two carpets.

And not one of her four facts is a table.

So every time she found one she wrote it down under a sensible heading and put it away and went back to looking, the way you walk straight past your hat eleven times when what you are looking for is your shoe.

That is the whole of it.  She is not stupid and she is not blind and nobody has hidden anything from her.

She was looking for a table, and the four facts are not a table, and there is no table.

### The wall at the top of the stair

Above the fourth floor the stair keeps going for eleven steps, and then there is a wall.

The wall is clean.  Somebody looks after it.  Dera put her hand flat on it and it was cool on the side she had just touched, like everything else in the building.

She knocked on it.  It is not hollow.

There is no fifth floor.  There has never been a fifth floor.  The way the Bureau is built does not allow one, and she checked this with three separate officials, and all three said the same thing without consulting each other.

So the fourth floor is the only part of the building that makes things with nothing above it to sort them out afterward.

### The Old Man with the Balanced Book

At the far end of the eastern corridor, past where the room numbers stop making sense, there is a very old attendant with a balanced book.

He is a honey bee like all the rest of them, and he is the only one Dera saw in six weeks who is not in the uniform.  He wears a cardigan instead, and it is out at both elbows and he does not mind at all.  His fur has gone thin over the shoulders.  He has not been off that floor in a long time and he does not appear to want to go.

He works under one green-shaded lamp.

His ledger is enormous, and it lies open on the desk, and the two halves of it are physically balanced.  He built it that way.  The same weight of paper on each side of the spine.  He let Dera lift each side in turn to feel it.

"Every bit I spend making a copy safe," he said, "is a bit I don't spend making it short.  That's the whole of my job.  Would you like the arithmetic?"

He is the only person in the Bureau of Persistence who can put a price on anything.

His pencil is sharpened down to a stub.  There is a second chair at his desk, and the seat of it is not worn at all, anywhere, and he has been there a very long time.

### What the attendant did with the pen

An attendant offered to copy Dera's pen for her.

He was pleased to be able to help.  He did it while she watched.  The copy was exact, right down to the small chip on the cap where she had dropped it once on a step.

The copy was empty by exactly as much as hers was.

Of course it was.  On that floor a thing and what it carries are one thing, and the chip came too, because on that floor wear is copied faithfully and stops meaning anything at all.

He handed both pens back to her.  She walked away with two pens and one pen's worth of ink, and she understood that she had been given nothing whatever, very kindly, by somebody trying to be nice.

### The fourth docket

She made a mistake on the fourth floor.  A large one, larger than the one on the first floor, and she made it deliberately in the end, to see what would happen.

The attendant brought her a docket for it within the hour, because they are very thorough up there.

It is a beautiful thing.  Stiff white board, gilt edge, her name spelled correctly, and the amount printed in the middle in the same numerals as all the others.

The amount is **0**.

"You print them anyway?" said Dera.

"Of course," said the attendant, surprised.  "It's a charge.  It goes on the record."  And it does.  It is on the record.  Somewhere on that floor there is a book with her name in it and a nought beside it, kept perfectly, filed correctly, and never once consulted by anybody.

She now had four dockets in her inside pocket.  Heavy grey card.  Buff tram ticket.  A slip off a pad in her own handwriting.  Gilt-edged board.

Four cards.  Four times the same figure, until the last one.  Her mistakes had got larger the whole way up.

### The worst moment

Her hands had gone steadier.

She noticed it on the fourth floor, holding the pen up to the light, and it is the worst moment in the report.

She could try as many times as she liked.  She could survive any mistake.  She could be wrong, and then wrong about being wrong, and no card came for either.  She could pick up any previous auditor's failure off a shelf and use it, and nothing was stamped against her for that either.  Her own work was in fourteen hands and belonged to none of them.

Four dockets.  Four cards in one pocket, and on the way up she had gone from a countersigned number stamped into grey board to a nought printed in gilt.

And four cards like that in one pocket is not four of the same thing.  It is a different thing altogether.  She was the best investigator who had ever come into the Bureau of Persistence, and she was completely unanswerable, and her finding had not moved one inch since the first floor.

Then she sat down on the eleventh step under the clean wall and did the arithmetic on the pen.

Six weeks of work that put nothing on her at all had emptied that barrel by exactly as much as six weeks of real work would have.  Not less.  Precisely the same.  The barrel does not read what comes out of it.

So she laid the four dockets out on the step in a row, and she held the pen up against them, and she did the only piece of arithmetic in this whole account that comes out even.

The figures on the dockets go down and end at nought.

The barrel goes down at the same rate throughout.

Nobody is charging her for the barrel.  There is no docket for it.  There is no line for a countersignature and there is no book with her name in it, and the only place in the entire Bureau where that sum is written down at all is in chalk, on a doorstep, in figures four inches high, by a man who cannot tell you what they are for and has never met anybody who reads them.

## The Four Attempts, Set Out Together

Because they happened weeks apart on four different floors, and because nobody should have to go back and look.

**On the first floor she asked the balance how many yards make a bell.** It was a mistake and it was charged.  One weight in the pan, the beam level, the bell rung once, every person on the floor saying the number out loud, and the pan tipped.  The Counter did not know what a yard was.

**On the second floor she asked the flagman how many bells make a yard.** He laughed, and then it was charged, and she ran nineteen yards down a painted lane and everybody clapped kindly.

**On the third floor she said the question into the tube.** The counter clicked.  Two hundred people turned round.  The question went off that floor for ever and she had to run down a flight to write it out from memory before she lost it.

**On the fourth floor she asked an attendant.** He came back in four minutes with fourteen conversion tables, typed, on identical cards, every one internally correct, no two of them agreeing.  When she pointed this out he was thrilled, hummed a great deal, and offered to make her a fifteenth.

Four questions.  Four machines.  Four charges, and the charges came down all the way: a body, then nineteen yards, then one word, then nothing at all.

**There is no table.**

### The Falling Cost of Being Wrong
The center at the scale of the lines is Darwinian evolution by natural selection.  Read as a mechanism, that center says what selection does.  Read as a direction, it says what selection charges.  The cost of a failed trial falls across the lines.  Each of the four functions lowers one component of that cost.
**No function lowers the cost on purpose.** The Effector acts.  The Regulator holds.  The Modeler maintains an account.  The Reviser generates novelty.  Each of the four savings below is what one function throws off while doing its own work.  This is the same shape as Darwin's saving in the climbing-plants argument: a climber reaches the light without building what holds it there, the saving is real, and the cost does not vanish.

| Saving | Installed at | Low end | High end |
|---|---|---|---|
| Cycle rate | Effector | semelparous | iteroparous |
| Temporal horizon | Regulator | homeostatic | allostatic |
| Orders of reflexivity | Modeler | sphexish | strange loop |
| Pattern portability | Reviser | obligate | facultative |

The two ends of each saving are descriptive endpoints, not knobs.  No tendency toggles between them.
**Cycle rate saves stake per trial.** The Effector weights recency, so it cannot wait.  A function that cannot wait produces many attempts rather than good ones, and volume is the byproduct of impatience.  Where trials are numerous, no single trial carries much of the stake.  A salmon spawns once and dies, which is one trial per lifetime at full stake.  An utterance is disposable because it is fast, and it is fast because the Effector will not hold.
**Temporal horizon saves lethality.** To defend a setpoint across a delay, something has to be stored, and a store outlives the occasion that made it.  Grain in a silo is insurance against a bad year and it is also slack.  The Regulator built a buffer for stability, and the buffer absorbs error as a side effect.  Homeostatic regulation defends a setpoint against present perturbation.  Allostatic regulation adjusts setpoints ahead of predicted demand, which is regulation reaching forward (Sterling and Eyer 1988).
**Orders of reflexivity saves contact with the world.** A model is a place where a unit can be wrong and nothing happens.  The Modeler built an interior account in order to regulate better and got a consequence-free venue for error.  Orders compound the saving, because a model of a model is a venue for being wrong about one's own wrongness at no charge.  The low end is a unit that cannot step above its own procedure.  The high end is a hierarchy that returns to its own starting level, which is what Hofstadter's strange loop names.
Reflexive orders are levels of model about model.  They are not layers of feature composition, and a many-layered network carries no order of reflexivity by virtue of its layer count.
**Pattern portability saves ownership of the trial.** To revise a reference, a unit must detach it from the machinery currently enforcing it.  Detachability is a precondition for revision, and a detached pattern is a copyable one.  The Reviser needed patterns loose enough to change and thereby made them loose enough for anyone to take.  Another unit's failed trial now informs this one at no cost.  An obligate symbiont cannot live outside its host and a facultative one can, which is the measure of how tightly a pattern is bound to what it is made of.  A pattern loose enough for a stranger to copy is loose enough to found a new medium, which is why the Reviser holds the bridging position.
**A function installs a saving.  It does not maximize it.** The saving enters at the cell where its function arrives, in the manner the four selection biases enter, and it persists upward under the persistence rule.  Magnitude therefore keeps climbing above the installing cell, so a later cell can run a faster cycle than the Effector cell that installed cycle rate.
**What falls is the cost of error, not the distance from competence.** A lineage paying full price per trial and still present is regulating successfully, and most of the biosphere by mass is in that condition.  The savings say what a failure costs, never how well a unit does when it succeeds.  Reading the direction as rising competence would make it the ranking that "Off-Thread Branches" refuses.
Bacteria carry the case.  Cycle rate is extreme and pattern portability is real through horizontal transfer, while temporal horizon and orders of reflexivity are absent, both of the missing two being the savings that require an interior.  Two of four is a lineage's own achievement in Boltzmann denomination rather than a partial version of anything.

---

## How the Organism Grows

### Organism Growth and the Relay
The framework's distinctive architectural contribution: as the Organism grows up the trellis, four parallel relay teams advance simultaneously — one per cybernetic function (Effector, Regulator, Modeler, Reviser).  At any rung, four motivations are active, each carrying its team's flag.  Each rung is a handoff for exactly one team: a new motivation takes the flag from its same-color predecessor; the predecessor retires into consolidated memory.  The other three teams keep their current flag-carriers.
The handoff order is Regulator → Modeler → Reviser → Effector, repeating across the matrix.  Across the twelve cells from Protocell through Empires, the cycle runs three full rotations.  The Effector handoff is a line boundary (Persistence to Impetus, Impetus to Commitment); at every other handoff the line persists.
The relay is what separates this from adjacent multi-scale-cybernetics work.  John Maynard Smith & Szathmáry supplies the diachronic story at coarse grain (transitions in individuality).  That work is not the work of how the Organism grows.  That work is the claim that the Organism at any rung operates with exactly four flag-carriers, one per team, with handoffs between rungs being the mechanism by which the lineage's cybernetic architecture accumulates.
Two timescales operate together.
**Within-Organism (fast).** The Organism's current Reviser explores, Regulator stabilizes, Modeler models, Effector acts.  Standard cybernetic loop at within-lifetime timescales.  The Organism learns, in its line's native sense of learning.
**Cross-rung (slow).** Each handoff happens when the slow loop has consolidated the prior flag-carrier's exploratory work into next cycle's stored structure.  A motivation that enters as a flag-carrier doing exploratory work at one rung, when retired, becomes part of the consolidated infrastructure on which higher rungs run.  The relay advances because consolidation has finished.
The two timescales are the same dynamic, exploration consolidating into structure, running at different temporal scales.  The fast loop is what an individual Organism does in its lifetime.  The slow loop is what selection does to the lineage across deep time.  The four flag-carriers active at any rung are what the slow loop's output looks like read off a slice of the present.
When a motivation retires from the relay, it does not disappear.  Interiority still operates in primates.  Coordination still operates in vertebrates.  Persistence still operates in everything alive.  Retired motivations get backgrounded into infrastructure that newer attractors run on, becoming difficult for observers to discriminate against the signal of more recent attractors.  The framework is measurement-theoretic, not architectural-deletion.
The Reviser carries a structural risk premium across lines, the constitutive prediction-error premium of running the explorer position.  At line-completing rungs (Eumetazoa, Primates, Empires), this compounds: the newest line-internal motivation occupies the Reviser position *and* the Reviser carries the structural risk.  Doubled heat is what makes the bet hot.

### The Saeculum
The selection cycle runs four stages over four sites.  A narrative tradition nobody derived from it describes the same four stages in the same order.

| Stage | Site movement | Saeculum |
|---|---|---|
| Collection, the Modeler | seed bank to clearing | the High |
| Sampling, the Reviser | clearing to understory | the Awakening |
| Expression, the Effector | understory to canopy | the Unraveling |
| Retention, the Regulator | canopy to seed bank | the Crisis |

Strauss & Howe's generational theory runs the four stages across its four turnings.  Each turning is worked by the archetype coming of age in it.
Strauss & Howe's generational theory runs the same four stages across its four turnings.  Each turning is worked by the archetype coming of age in it.
**The High is Collection.** Institutions are strong and one account of the world dominates.  The strongest account foregrounds and the faint is overshadowed, which is potency.  The Artist comes of age here and works the Modeler.
**The Awakening is Sampling.** The dominant account is broken open and movements proliferate.  Novelty is weighted and the familiar falls to background.  The Prophet comes of age here and works the Reviser.
**The Unraveling is Expression.** Institutions weaken, and individual actors build competing ventures and push them into a canopy with a weak gate.  The Nomad comes of age here and works the Effector.
**The Crisis is Retention.** One outcome is inscribed as the new order and the competitors are discarded against it.  The Hero comes of age here and works the Regulator.  What the Crisis writes is the store the next High reads.
The turnings open at the High.  Archetypes are conventionally listed by birth, which puts the Prophet first, and birth order is not working order.
*Metaphor mapping.  What transfers is the order of the four turnings.  What does not transfer is deliberateness.  The archetypes are populations of people who want things, and a turning is not something anyone runs.  No one convenes a Crisis, and the Prophets who break a High open are not executing a stage.  Scope: the agency limit applies to the turnings rather than to the people living in them.*
#### What the agreement is worth
The four stages are fixed twice over.  The sight and binding bits fix which function each stage runs.  The absence-recruitment argument fixes the order they run in.  Both derivations are mine, and they agree.  The saeculum is external, and it agrees with the result.  That is a third check, and it is the only one of the three that could have come out otherwise without anyone noticing.
*The four stages, the four sites, and the four biases are settled.  Strauss & Howe's periodization is contested in its own field, and historians generally treat it as pattern-fitting.  I am not carrying it as evidence.  I am carrying it because it is the only version of the shape a reader can stand inside.*

### Why the Lines Open at the Effector
The three retellings open at Collection.  The inheritance lines open at the Effector, because Protocell, Bilaterian, and Band-Human are Effector cells.
The difference is between a first turn and every turn after it.  Collection reads a store, and the three retellings all describe a cycle whose store is already full.  A line begins in a medium that holds nothing yet.  The prior line's store is not a store in the new medium, so Collection has nothing to read, and the line opens by acting instead.  Band-Human establishes symbolic commitment before there are symbolic norms to regulate.
The growth relay's handoff order is the same fact counted differently.  A line's founding cell is an Effector, so the first handoff installs the Regulator.  Counting cells gives Effector, Regulator, Modeler, Reviser.  Counting handoffs gives Regulator, Modeler, Reviser, Effector.  One order, two ways of counting it.
*the Effector founding of each line is settled, as is the growth relay's handoff order.  The empty-medium account of why the lines open at the Effector is my inference.*

### The Maturity Gradient
The motivations on the stack are not equally consolidated.  The gradient runs from **exploratory** (most recent, under selection pressure, parameters still being shaped) to **consolidated** (deepest, internalized into inherited infrastructure, parameters stable enough to serve as foundation for everything above).
The mechanism is Watson & Szathmáry's developmental-memory result, generalized across lines.  Selection operating across generations internalizes the correlation structure of the selective environment into the lineage's inherited architecture.  That architecture is gene-regulatory at the genetic line, neural-architectural at the neuronal line, and cultural-institutional at the symbolic line.  What enters as exploratory variation under active selection becomes, given enough generations of consistent selection, stored architecture that newer exploration runs on top of.
The gradient is continuous, not binary.  The four flag-carriers are most exploratory and individually discriminable in unit-level behavior; older motivations drop below into backgrounded infrastructure, where the consolidation process continues but unit-level behavioral discriminability has been lost.

### Unit-Level Subjectivity
The unified Venn at each cell applies to a specific unit.
- **Genetic-line cells.** The unit is the cell or organism: Protocell-as-unit, Prokaryote-as-unit, Eukaryote-as-unit, Eumetazoa-as-unit.
- **Neuronal-line cells.** The unit is the brain-bearing organism: Bilaterian-as-unit, Vertebrate-as-unit, Mammal-as-unit, Primate-as-unit.
- **Symbolic-line cells.** The unit is the constituent human parameterized by collective context: Band-Human, Settlement-Human, City-Human, Empire-Human.  The collective remains the group.  The Venn at the symbolic cell tracks the constituent human as unit.  The collective relates to the human as meme-fauna to personality-flora.
The systematic-analogy rule lets motivations transfer up the stack by structural analogy, not loose metaphor.  At symbolic cells the motivations are held by the constituent human.  What shifts across cells is which primaries carry flags given collective context.  A Band-Human's Commitment is the band-context-conditioned attractor in the same organism that, in a different context, would activate different motivations.

### The Twelve Knobs

| Line-knob | Cell | Cyb. slot | Motivation | Slot-label (Tendency) | Knob name |
|---|---|---|---|---|---|
| Genetic k-1 | Protocell | Effector | Persistence | Acquisition Type | Going |
| Genetic k-2 | Prokaryote | Regulator | Coordination | Respiration Type | Working |
| Genetic k-3 | Eukaryote | Modeler | Interiority | Foraging Type | Getting |
| Genetic k-4 | Eumetazoa | Reviser | Excitability | Home Type | Resting |
| Neuronal k-1 | Bilaterian | Effector | Impetus | Orienting Style | Choosing |
| Neuronal k-2 | Vertebrate | Regulator | Mastery | Coping Style | Coping |
| Neuronal k-3 | Mammal | Modeler | Autonomy | Neuroticism | Risking |
| Neuronal k-4 | Primate | Reviser | Affiliation | Agreeableness | Helping |
| Symbolic k-1 | Band-Human | Effector | Commitment | Curiosity | Hunting |
| Symbolic k-2 | Settlement-Human | Regulator | Stability | Conscientiousness | Tracking |
| Symbolic k-3 | City-Human | Modeler | Representation | Extraversion | Leading |
| Symbolic k-4 | Empire-Human | Reviser | Universality | Integrity | Living |

---

## Ecology Across Lines

### Coevolution Across Line Transitions
Each line emergence is a coevolutionary event.  The new fauna develops alongside what becomes its new flora.  It does not replace the prior line.  It enters into stable interdependence with the prior line's mature output.  The pattern recurs across the framework's structural history:
- Cambrian explosion (~540 MYA): vertebrate brains coevolve with the diversification of bilaterian body plans.
- Land transition (~400 MYA): land arthropods coevolve with land plants.
- Tetrapod radiation (~360 MYA): land tetrapods coevolve with forests.
- Angiosperm radiation (~140 MYA): social insects coevolve with flowering plants.
- Mesozoic transition (~200 to 66 MYA): mammals coevolve with dinosaurs.
- Cenozoic transition (~66 MYA onward): birds and primates coevolve with post-extinction forest niches.
- Symbolic line emergence (~100 KYA onward): human personality coevolves with human culture.
The bridge-entity pattern (Reviser of column N parents Effector of column N+1) traces the genealogical thread through these events.  Coevolution is the ecological story running alongside the genealogical one.  The two are not in tension.  The bridge identifies which entity opens the new line.  Coevolution describes how the line fills in once opened.

### Clade and Symbiosis Vocabulary
Each cell name is shorthand for a clade, a category of units sharing the cell's architectural signature.  Eukaryote names the clade of organized-interior cells.  City names the clade of city-states, urban-centered kingdoms, and other polities organized around an urban administrative core.  Empire names the clade of territorial, maritime, and ideological empires.
Coevolution within a line operates through two modes — symbiosis (merger) and elaboration (non-merger).

### Symbiosis and Elaboration
Symbiosis is the merger mode: a new higher-level structure forms by committing previously-more-independent parts as its components.  Elaboration is the non-merger mode.  A unit develops continuously without committing previously separable parts.
Modeler and Reviser transitions are symbiosis-prone at every line.  Effector and Regulator transitions are elaboration.  The line determines what symbiosis looks like.
- **Genetic Modeler endosymbiosis:** free-living prokaryotes commit as mitochondria, and as chloroplasts in plants, inside a host cell.
- **Genetic Reviser multicellularity:** free-living eukaryotic cells commit as differentiated tissues inside a multicellular body.
- **Neuronal Modeler cortical stacking:** mammals introduce agranular cortex as a new neural lineage layered over the subcortical control structures (basal ganglia, limbic system).  The agranular cortex's function is to model what the subcortical structures do.  The two lineages persist in obligate functional interdependence.
- **Neuronal Reviser cortical stacking:** primates introduce granular cortex as a meta-modeling layer over the agranular cortex.  The same architectural signature, applied one level up.
- **Symbolic Modeler city formation:** settlements commit as components of a city, and trade networks commit as the connective tissue that lets the city aggregate goods, people, and information beyond what any single settlement can produce.
- **Symbolic Reviser empire formation:** cities and their hinterlands commit as administrative provinces of an empire.  Empires often add colonies that extend the empire beyond contiguous territory.
No merger of previously separable parts is required in the elaboration cases.  The unit develops continuously from existing structure.
- **Genetic Effector elaboration:** protocells emerge from teleodynamic ratchets through continuous chemical development.
- **Genetic Regulator elaboration:** prokaryotes emerge from protocell logic through stored regulation.
- **Neuronal Effector elaboration:** bilaterian brains emerge from genetic-Reviser neural nets through elaboration of a control architecture for reflexes (steering and affect).
- **Neuronal Regulator elaboration:** vertebrates elaborate the bilaterian control architecture with reinforcement learning (basal ganglia plus operant conditioning).
- **Symbolic Effector elaboration:** bands emerge from primate troop dynamics through language-mediated extension.
- **Symbolic Regulator elaboration:** settlements emerge from band practices through sedentary agriculture.
The neuronal version of symbiosis runs through neural-lineage stacking because the brain is body-internal.  There is no free-living state from which neural lineages could merge.  What is available is the structural pattern where a newer neural lineage develops the capacity to model an older one it is built on top of.  MacLean's stacking intuition was partly right; what he got wrong was the specific lineage details, not the layered architecture.
*the Modeler-and-Reviser symbiosis pattern holds across all three lines with two confirmed cases at each row in the genetic and symbolic lines.  The neuronal-line version, instantiated through cortical-lineage stacking, is well-documented at the structural-anatomical level.  The framework's claim that the neuronal stacking pattern carries the same architectural signature as endosymbiosis and polity merger is a framework theoretical commitment.*

Substantial structural innovation often happens within a line without producing a new line.  The slack test stays operative.  A new line requires a new modality of pattern transmission that carries inheritance.  Elaboration produces enormous complexity without crossing the line threshold.
Take the two cases properly.  A coral reef is a multi-species ecosystem built around cnidarian colonies, with a productivity that rivals tropical rainforest, and it is not a new phylum: the cnidarian biology that builds it stays inside the eumetazoan-Reviser logic.
Corporations, markets, and exchanges are the parallel at the symbolic line, structurally as complex as any historical empire, and they are not a new line: the logic that builds them stays inside the empire-Reviser elaboration.
Both are platform elaborations: structures that create the conditions under which other elaborations can flourish.  The reef anchors its ecosystem.  The market anchors its institutional ecology.  Neither breaks the line.  The pattern holds across lines: bacterial mats and stromatolites at the prokaryote level, fungi at the eukaryote level, octopus cognition at the bilaterian level, corvid cognition at the vertebrate level, religious orders and universities at the city level.  Most innovation is elaboration.  Lines are rare.

---

## Genealogy and the Thread

### The Bridge-Entity Pattern
A structural feature runs across the two confirmed line transitions: the entity at Row 4 of column N parents the entity at Row 1 of column N+1.
- Eumetazoa (Row 4, genetic) parents Bilaterians (Row 1, neuronal).
- Primates (Row 4, neuronal) parents Bands (Row 1, symbolic).
The Reviser motivation introduced at the parent cell carries as the Reviser motivation of the child cell.  Excitability introduced at Eumetazoa is Reviser of Bilaterians.  Affiliation introduced at Primates is Reviser of Bands.  The variation-selection reading is that Reviser is the slack each line ratchets, on which the new line selects.
Sample size is 2.  Two confirmed bridges is enough to name the pattern but not enough to treat the pattern as architectural law.
Row 4 entities are defined by the riskiness of the bet they represent, and the three fates are distinguishable only retroactively.  The bet fails.  Or it succeeds as itself and stays off-thread, a real innovation that opens no next line, the way fungi and plants are evolutionary triumphs that parented no further lines.  Or it bridges, parenting the Row 1 founding form of a next line.  Empire-Human took the third fate: it parented Computer.  Agent, not Empire-Human, is now the current Row 4 of the most-evolved column, and it is the one case where the three fates are not all open: the four-line cap forecloses bridging, so only failure and off-thread success remain, and which of those two is in progress I do not claim to know.

### Off-Thread Branches
Our framework traces one phylogenetic thread: the specific lineage from protocell through bilaterians, vertebrates, mammals, primates, into bands, settlements, cities, and empires.  It is the thread that produced all four inheritance-line transitions observed so far.
Off-thread lineages (plants, fungi, slime molds, birds, bees, octopi) have their own stacks built from the same architecture, but with different motivations filling the slots above their branching point.
Bees branched at bilaterians, so their stack shares Persistence, Coordination, Interiority, Excitability, and Impetus with the human thread.  Above that, bees develop motivations specific to eusocial arthropods, and the lineage stops there because the bee thread did not produce a symbolic line.
This converts an apparent limitation into a feature.  Any organism's personality can be analyzed as a 4-sphere active window over its own evolutionary stack.  The 4×4 is the case where the lineage runs all the way to symbols.  The architecture applies to any thread of life.
Parallel evolution becomes visible without forcing convergence.  Octopi branched at bilaterians and developed sophisticated cognition through a different neural architecture.  Their stack would resemble the vertebrate stack at certain levels but with different motivations filling the upper slots.  The framework predicts structural similarity at the levels of shared ancestry and divergence above the branching point.
The clade name is the rung's address, not a quantifier over the clade's membership.  A capacity documented in an off-thread lineage informs an on-thread cell only when the capacity sits below the branching point.  Two conditions establish this.  The capacity must be present in deeply divergent branches of the clade rather than in one branch alone.  The capacity must not depend on an organ that postdates the clade's radiation.  A capacity failing either condition sits above the branching point, where it is elaboration on the off-thread stack.
The conditions carry no judgment about which lineage is advanced.  Every living lineage has been evolving for the same interval.  An off-thread capacity is that lineage's own achievement rather than a preview of what a later on-thread cell would build.
Four worked cases.  Honeybee mushroom-body elaboration sits above the bee branching point and does not inform the Bilaterian cell.  Corvid nidopallial elaboration sits above the bird branching point and does not inform the Vertebrate cell.  Box jellyfish associative learning localizes to the rhopalial nervous system, rhopalia are a medusozoan organ, the organ postdates the eumetazoan branching point, and the finding therefore does not inform the Eumetazoa cell.  Operant conditioning is present in protostomes and in deuterostomes and depends on no organ unique to either, so it reconstructs below the bilaterian branching point and does inform the cells above it.
The fourth case is the test cutting the other way.  A capacity that clears both conditions reaches the cell whether or not the framework wants it there.

### Negative Findings and Clade Placement
A capacity found in a lineage is established by the finding.  A capacity not found in a lineage is not established as absent.  The asymmetry sets a higher bar for lowering a cell label than for raising one.
Three readings compete for every negative finding.  The lineage never had the capacity.  The lineage had the capacity and lost it.  The method failed to detect it.  Only the first bears on the clade's ancestral state.
Loss is cheaper than gain: one disabled pathway removes a capacity, where building one requires selection over time, so parsimony that counts gains and losses as equal steps reconstructs ancestors as less capable than they were.  Negative findings under-report ancestors as a matter of course.  A placement survives a negative finding by positing a loss; one loss is cheap, and only when the accumulated losses cost more than a later gain does the placement move later.
Three conditions let a negative finding lower a label.  The lineage tested must retain the architecture the cell names rather than having secondarily lost it.  The method must have detected the capacity in a positive control, in a lineage independently known to have it.  The absence must hold across deeply divergent branches of the clade and in the outgroup.
Early-branching position is what makes a lineage worth testing; morphological simplicity is not, because simplicity is frequently derived, parasitic and sessile lineages simplifying from complex ancestors, so the simplest-looking member of a clade is often the least informative about that clade's ancestor.  For the calibration: two laboratories measured visual working memory in rhesus macaques and reported roughly one item and roughly four.  Same species, different procedures.  A procedure that can conceal three items of working memory in a laboratory primate can conceal a capacity in any less-studied animal.
No negative finding currently lowers any cell label.  The positive-control condition has not been met below the Bilaterian cell.  Presence evidence can move a placement earlier; absence evidence can move it later; neither moves anything on the strength of a single lineage.

---

So far I have described what the four functions are and how they compose.  Now I want to describe what they do in one turn.  A line runs a cycle over four sites, and the four stages that move a unit between them are the four functions at the scale of a single increment of inheritance.

## Why the Lines Need Shared Slots
The framework claims that genes, brains, talk, and code run the same process.  That claim is empty unless the genetic line's X and the symbolic line's X are the same question asked twice.
Without that, every cross-line statement equivocates.  The word carries one sense at one line and a second sense at the next, and the sentence joining them says nothing.
What the framework needs is a fixed set of slots, filled at every line.  Two entries are counterparts when they fill the same slot.  Counterparts are not the same thing, and they need not resemble each other.  Ask whether a repository is the counterpart of a gene pool or of a genome, and the answer comes from which slot each one fills, not from which one it looks like.  A repository is a store holding many units, so it fills the seed bank, and its counterpart is the gene pool.  A working copy is one candidate drawn from what is available, so it fills the understory, and its counterpart is the genome.  Neither answer comes from what a repository resembles.
Filling the same slot at two lines then produces a comparison rather than a pun.  A slot that fills thinly at one line becomes a prediction to check rather than a hole to apologize for.
The four stages and the four sites they run between are that set.

## The Cycle
A line runs a cycle over four sites.  Each stage moves the unit from one site to the next, and the fourth hands back to the first.  The handoff closes and the state does not return.  The seed bank Retention writes into is not the seed bank Collection read from, and that difference is what inheritance is.

| Stage | From | To | Function | Bias |
|---|---|---|---|---|
| Collection | seed bank | clearing | Modeler | potency |
| Sampling | clearing | understory | Reviser | novelty |
| Expression | understory | canopy | Effector | recency |
| Retention | canopy | seed bank | Regulator | familiarity |

**Collection** narrows a seed bank to what is available now.  **Sampling** draws one candidate from what is available and may mix it with others.  **Expression** builds the drawn candidate into something that competes.  **Retention** writes what passed the gate back into the seed bank.
Selection is not a stage.  Selection is the whole cycle, and it sits at the center.
The sites are named for places in a climbing plant's world.  The stages are named for operations any line performs.  Units are collected from the seed bank, sampled from the clearing, built in the understory, and kept or discarded in the canopy.
The stages run in order and nothing skips.  Nothing is available that was not stored, nothing is loaded that was not available, nothing is expressed that was not loaded, nothing is stored that was not expressed.  That chain is what makes this a cycle rather than four operations standing next to each other.
| Line | Unit | Selector | Scarce resource |
|---|---|---|---|
| Genetic | gene | Natural Selection | a slot against carrying capacity |
| Neuronal | neme | Attention | one action |
| Symbolic | meme | Conversation | one turn |
| Digital | program | Execution | one invocation |
The selector is each line's founding-cell breakthrough.  The scarce resource is the quantized thing the canopy has one of, so one relation generates every row rather than needing an argument per line.
*the units are settled.  The selectors are owned by the per-line label libraries and each entry matches its library.  The scarce-resource relation follows from the canonical statement that selection bites only where a limited resource forces competition, and that in the genetic case that resource is finite carrying capacity.*

## Why the Turn Does Not Return
Two different things make the cycle run one way, and keeping them apart matters.
Entropy makes it one-way.  Every stage transition is paid for.  Collection pays for constraint, Sampling pays for generation, Expression pays in work and dissipation, and Retention pays for a local inscription with a larger export.  Paid-for transitions do not run backward for free.  This is the Second Law and not a claim particular to this framework.
Selection makes the one-way cumulative.  Irreversibility on its own gives drift, and a process can be irreversible and go nowhere.  What makes each turn start from somewhere different in a direction rather than merely somewhere else is that Retention is a gated write and not just a write.
One family of claims goes further than this and the framework declines it.  Prigogine, Schneider and Kay, Lotka, England, and Stuart Kauffman each propose that distance from equilibrium drives systems toward order, or toward faster dissipation, as a tendency of the physics itself.  That puts an aim in the ground floor.  The framework takes the dissipative structure and leaves the drive: entropy supplies the arrow and nothing else, and every aim is downstream of a selector.  Deacon is the anchor I have already leaned on, since morphodynamic self-organization is where he starts and his argument is that it is not sufficient.  The decline is scoped to the universal-drive version.  Bioenergetic constraint at particular scales is a separate matter, and the framework keeps Lane's version of it.  Stuart Kauffman is declined for the fourth law only.  Collectively autocatalytic sets are a closure result about what a chemical network can sustain, which is an accounting rather than a drive, and the framework keeps it.
*the Second Law and life as a dissipative structure are established, and the framework already stands on both.  Reading each stage transition as separately paid is a framework commitment.  The division of labor between entropy and selection is a framework commitment.  Declining the thermodynamic-imperative reading is a framework position rather than a finding, and it rests on Deacon's argument that self-organization is not sufficient.*

## The Draw and the Mixing
Sampling does two things and they come apart.  It draws one candidate from what is available, and it may mix that candidate with others.  The draw always happens.  The mixing runs on a range that reaches zero.
Every line has cases at zero.  A seed can be produced without fertilization.  A phrase can be repeated exactly.  A merge can apply cleanly with no conflict to resolve.  A recall can come back unblended with anything else.
None of these skips Sampling.  In each, a candidate was drawn and the mixing contributed nothing, which is the low end of a range rather than a missing stage.  Reading a zero-variation case as a skipped stage would break the ordering claim for no reason, because the ordering claim is about which operations run and in what sequence, not about how much any one of them changed the unit.

## Why There Are Four
Two independent derivations fix the number, and they agree.
**The two bits.** Sight asks whether an operation's variation can be about itself.  Binding asks whether reflexive operation is bounded.  Two independent bits give four corners, and the four cybernetic functions sit at those corners.  Read the bits off each stage and each lands on one corner.
Both bits are claims about what a stage can do rather than about any particular run of it.  A degenerate run does not move a corner.
Collection is sighted, because what gets gathered is filtered through a model of what counts.  It is unbounded, because there is no principled ceiling on what a seed bank can yield.  That is the Modeler corner.
Sampling is blind, because neither the draw nor the mixing consults what the build will need.  It is unbounded, because the mixing can be combinatorially open.  That is the Reviser corner.
Expression is blind, because a build runs its instructions without reading outcomes.  It is bounded, because what one set of instructions can build is a finite region.  That is the Effector corner.
Retention is sighted, because the write is gated on the outcome.  It is bounded, because it writes against a stored reference.  That is the Regulator corner.
**Absence recruits.** The functions run in a forced cycle, each recruited by the specific absence in the one before it, and the cycle closes back to action.  The stages inherit that order and that closure.  The closure is in the recruitment rather than in the state.  Every function is recruited and none is left dangling, which is a different claim from anything arriving back where it began.  A cycle of three leaves one recruitment unanswered.  A cycle of five has no corner to stand on.
The two derivations are independent.  The bits fix which corner each stage occupies.  The recruitment fixes the order they run in.
*the two bits, the four corners, and the recruitment cycle are settled.  The reading of each stage's bits is my inference.  Each function assignment is independently corroborated: the developing organism is named as the genetic Effector; the Regulator is defined as regulated control against stored references.  That fork, branch, and merge are the blind recombination the Reviser runs on at the digital line is a framework commitment.*

## The Four Sites
The four sites are the four handoffs.  A site is where one function passes to the next, so each corresponds to an adjacent-pair region of the Venn.  The site is where that region's tendency operates rather than the tendency itself: the Anticipator operates in the seed bank, the Adapter in the clearing, the Explorer in the understory, the Controller in the canopy.
Each site holds the unit in a different mode, and the process column names the change the departing stage makes to it.

| Site | Handoff | Tendency | Process | Genetic | Neuronal | Symbolic | Digital |
|---|---|---|---|---|---|---|---|
| Seed bank | Regulator to Modeler | Anticipator | Stored to Available | chromosome | engram | text | file |
| Clearing | Modeler to Reviser | Adapter | Available to Loaded | standing variation | live operants | live memes | resolved dependencies |
| Understory | Reviser to Effector | Explorer | Loaded to Expressed | zygotic genome | motor plan | phonetic plan | working copy |
| Canopy | Effector to Regulator | Controller | Expressed to Stored | organism | behavior | utterance | process |

The recruitment argument reads correctly at each site.  A fixed reference cannot look ahead, and the seed bank is what Collection reaches forward from.  A model fitted to the past goes stale, and the clearing is what Sampling refreshes.  A rewritten model changes nothing until something acts on it, and the understory is where it is loaded into something that can act.  An open action cannot see its own result, and the canopy is where an outcome becomes visible.
The process column is the handoff column translated.  Each mode is the output of one function's stage: available from Collection from the Modeler, loaded from Sampling from the Reviser, expressed from Expression from the Effector, stored from Retention from the Regulator.  Substitute and the two columns agree row for row.  That agreement is a test the mode words can fail, and it is why they are these four words.
Only the per-line columns carry information.  Site, handoff, tendency, and process are one fact in four renderings.
The expressed row needs one note, because two of its cells are not built the way the other two are.  An artifact is the product of an expression and an output is the product of a process, both one level past the thing that ran.  The genetic and neuronal cells name the unit running rather than what the running throws off, so the symbolic and digital cells name the utterance and the process.
*the four adjacent-pair regions and their recruitment arguments are settled.  Identifying the sites with those regions, and a site as where a tendency operates, is my proposal.  The stored row is settled.  The available and loaded rows are new.  Standing variation, working copy, and resolved dependencies are field-native.  Live operants restates the canonical statement that many operants are always live and only some win the workspace.  Motor plan and phonetic plan follow the established production sequence.  Live memes is the weakest cell in the table.*

## Selection at the Center
Selection is not a stage.  Selection is the whole cycle.
In a line's own Venn the center is the breakthrough, the synthesis that requires all four functions at once.  The four stages are those four functions.  So the synthesis that requires all four stages is the cycle itself, and that is what selection names.  The center of a Venn is the region where all four attributes hold, not a fifth thing standing beside them.
There is a mechanical reason as well as a geometric one, and it is the stronger of the two.  Selection is not locatable at one stage because all four stages discard.  If a single stage owned the discarding, the other three would be plumbing and the center would be decorative.  Four narrowings composing is what the center is, and the next section sets out what each one throws away.
That a line is selection-mediated inheritance rather than inheritance with selection added at one point is argued at the scale of the lines.  It holds the same way at the scale of the stages.  Gathering, drawing, building, and keeping are each necessary and none is sufficient, and the four running as one cycle is what selection is.
The center defines the cycle and it unites the cycle.  It defines it because a cycle whose handoffs do not chain this way is not a line.  It unites it because no stage can be understood without the three it hands to.
A center is not a fifth thing, and the overlap of four is not a fifth.  This is why scoring needs no station of its own.  Scoring is what a sighted, gated write does.
Selection happens once per event, and the event is small.  Differential reproduction happens at every birth and every death.  Attention happens every time a body performs an action.  Conversation happens every time a band shares information.  Execution happens every time a program runs.
A criterion is therefore a property of the individual competitor at the moment of the event.  It is not a statistic over a population.  A trend across many events can be measured, and measuring one is useful, but the measurement is downstream of the criterion rather than identical with it.
This is why every criterion below names a disposition of the competitor rather than an outcome or an aggregate.

## Maintenance and Selection
Entropy is the ground, and coming apart is what happens when nothing is spent.  Everything the framework describes persists by doing work against that ground, and the work is continuous.
One bill is levied and it is entropy's.  Selection is the choosing of what to keep paying for.  Maintenance is the paying.  The two are one process seen from two sides, and the framework calls the pair a coin.
*The coin.  What transfers: two faces of one object, neither recoverable from the other, and no vantage from which both are visible at once.  One object carries one budget and one payer.  Does not transfer: a mint, a denomination set from outside the process, and exchange for anything else.  Scope: every line, and every scale at which the cycle runs.*
There is one payer.  The unit that is selected is the unit that pays.  No budget is split between maintaining and selecting, because choosing what to keep funding is not an expense separate from the funding.  A claim that finds two payers inside one line has found a mistake.
The coin holds wherever a cycle runs.  Paying begins earlier than that, one step before the genetic line.  Before a line there is paying and nothing choosing, which is a payer without a coin rather than a face without an object.
Nothing in the cycle is destroyed by the cycle.  A stage narrows by ceasing to fund what it does not carry forward, and the ground state does the rest.  Each of the four discard classes names the kind of thing a stage stops paying for, and the prices already given are what that stopping costs the payer.
The two faces are not two topics.  A claim is stated on the face it concerns, and both faces are named together only where the claim would be false with one.

## What Each Stage Discards
Every stage narrows, and narrowing leaves a residue.  The figure below says each narrowing is unaimed.  What it does not say is what becomes of what was narrowed away.
The residue is not one undifferentiated pile.  Each stage throws away a different kind of thing, and the formalism its function works names which kind.  Collection discards candidates the constraint excluded, which is Shannon.  Sampling discards everything generable and not generated, which is Kolmogorov.  Expression discards failed builds and heat, which is Boltzmann, and it is the only stage where the residue is literally thermodynamic.  Retention discards what failed the gate against a stored reference, which is Friston.
These are the payments seen from the other side.  One account says every stage transition is paid for.  This one says every stage throws away a different kind of thing.  They are one fact: what a stage pays is what it discards, counted in the formalism its function works.  The canopy holds a finite quantity of what the line competes for, more arrives than it has to give, and a claim the budget does not meet is the residue.  Payment and discard are one event named twice.  Nothing is destroyed by the narrowing.  What a stage discards is what it stops funding, and the ground state does the rest, which is the coin.

| Stage | Genetic | Neuronal | Symbolic | Digital |
|---|---|---|---|---|
| Collection | alleles absent from the deme; seed that never breaks dormancy | signal that never becomes perceptible | culture available and not acquired | repo contents never pulled in |
| Sampling | gametes and zygotes never formed | operants live and never retrieved | lexical competitors active and losing | merges never attempted |
| Expression | developmental failure; dieback | aborted movement; pruning | disfluency, false start, self-repair | broken builds |
| Retention | the entire soma, at Weismann's barrier | performance that never consolidates | what is said and not passed on | work never committed |

The understory divides two kinds of residue.  Before it, candidates are unbounded and merely possible, so what is lost is possibility foregone.  In the understory a candidate binds into an actual thing, so from there on what is lost is payment already made.  The dividing line is where binding flips in the two-bit square, which means it falls out of the derivation rather than being observed.
The discarding is the operation and not a shortfall in it.  A Collection that discarded nothing would pass the whole seed bank forward and narrow nothing, and a Retention that kept everything would not be a gate.  What can be compared across stages and across lines is the ratio, which differs by orders of magnitude and is measurable.
The figure carries this without strain.  A tangle is mostly senesced stem with live growth on top, and the canopy is reached over everything that did not reach it.

## Upkeep and Decay
Every transition is paid for, and every site holds its contents between visits at a cost.  The payer is the same in both cases and the line items are different.  An item can sit through many turns of the cycle before the cycle reaches it again, and what it is worth when it is reached is not what it was worth when it was written.
This is not a third class of residue.  The two classes divide at the understory, and the division falls out of the two bits rather than being observed.  Both are produced at the moment a stage narrows: something offered and never funded, or something funded and then not funded further.  What decays at a site is a retained item, one that no stage discarded, losing ground while it is held.  Same payer, different line item.
Two things drive it.  An item is short only relative to the context that makes it short, and the context disperses even when the item does not, so the cost of reconstructing what the item meant rises while its contents stay exact.  This is the conditional complexity, read against a receding condition rather than a fixed one.  And the site keeps changing around the item, because Retention writes every turn, so the store that will be narrowed is never the store the item was written into.
Call the observable salience decay: the item's odds of being picked at Collection fall while its contents stay intact.  Collection weights potency, and an item losing salience is an item losing at Collection.  An archive can go dark while its medium is perfectly preserved.
Salience decay is a rate and it can run negative.  A recovered index, a released corpus, or a returning reader lowers the reconstruction cost, and the item's odds rise again.  Rediscovery is the same quantity running the other way rather than an exception to it.
What is held is a pair at every line.  There is the item, and there is the condition that makes the item usable.  Upkeep pays for both, and decay takes the second one first.

| Line | Unit | What is held | Upkeep | An item held and losing salience |
|---|---|---|---|---|
| Genetic | gene | the sequence and the regulatory context that expresses it | repair and replication fidelity, and the homeostasis that keeps the cell able to run either | the sequence is intact and the regulatory context that once expressed it is gone |
| Neuronal | neme | the trace and the cue structure that reaches it | consolidation, and the rehearsal that keeps a cue live | the trace is intact and no cue reaches it |
| Symbolic | meme | the text and the shared context that makes it readable | retelling and teaching, the transmission that keeps a reading community in place | the text is preserved and the readers who could read it have dispersed |
| Digital | program | the file and the reader that can open it | format migration and dependency upkeep | the ticket is filed and never worked; the file is kept and the reader for its format is gone |

The table has no column naming who maintains.  The unit that is selected is the unit that pays, so there is no second agent to name.
*retrieval failure without loss of the trace is established, on cue-dependent forgetting after Tulving and Pearlstone.  The conditional-complexity result is established.  DNA repair and consolidation are established.  Reading what is held as a pair of an item and its condition of use follows from the conditional-complexity account above.  Naming Collection's bias as the quantity that decays is a framework commitment.  The upkeep cells are framework inference rather than a survey, and the symbolic cell is the weakest, matching the weakness already noted for live memes.  Rates are unmeasured here, including any claim that high-throughput environments accelerate the decay, and should be checked before a number is given.*

## The Eleven Seconds

This happened in the middle of everything, and it belongs where it happened.

The sound stopped.

Not a crash.  The low note under the building simply was not there any more, and the silence was so strange that Dera came down four flights to find out what had gone wrong.

Nothing had gone wrong.  On the third floor the Registrar went on writing.  On the first floor the forty did not move.  The Chairman's room stayed warm, because it is heated by a floor and not by a chimney.

On the doorstep there was a heap of grey dust on a three-legged stool.

No spiral.  No stripes.  No spots.  No hexagons anywhere.  Nothing had been destroyed and nothing had been taken away.  All of it was still there and none of it was in any order.

The eddies at his feet were gone.  The rings were gone.  The meanders along the wall were a smear.

The tea in the chipped white cup was flat, and grey, and still.

The small thing off to one side was exactly as it had been.

Then the sound came back.

Over about eleven seconds the spiral found its point at the top and went round thirteen one way and twenty-one the other.  The stripes came up the forearms.  The spots came out on the backs of the hands, bigger at the wrist and smaller at the knuckles.  The hexagons set in the knuckles.  The tea began to turn.

"Afternoon," said the Porter, as though she had only that moment walked up.

Dera tried to tell him what she had seen.  He was politely uninterested, in the way you would be if somebody described your own sleeping.  He did not remember it.

**No bell rang for any of it.**

That is the fact and it is the only fact she needed.  She stood on that step with a stopwatch for the whole eleven seconds and for four minutes afterward, and the bell did not ring, on any floor, and nobody said a number out loud anywhere in the Bureau of Persistence, and no machine anywhere in that building moved a wheel or a beam or a pan.

The Porter came entirely apart and was put back together and **not one payment was demonstrated.**

And then she looked at the two chalk columns on the step.

There are two of them and they are in figures four inches high and here is what each one is, because there is no reason for anybody to have to go back and check.

**The big column is the building's dust.** Four floors of it, coming to bits, arriving at the bottom.  Nobody pays for that.  No bell rings for it.

**The little column is the small thing in the dust.** Every time it puts itself back together it throws off a little dust, and the Porter weighs that on the jeweller's pan and writes the number down.

This is what she found, and she wrote it in capitals.

The big column, which is the building's dust, had not changed.

The little column, which is the small thing, **had gone up twice while the chimney was stopped.**

Twice.  In eleven seconds.  With everything else on that doorstep in a heap and no bell ringing anywhere in the world.

The Porter got the scales out afterward and weighed it and chalked the two figures in, without any comment at all, and went back to sitting down.

She went and looked at the small thing again, very closely, for a long time.  It had not flickered.  Through all eleven seconds, with the chimney stopped and every pattern on that doorstep coming apart, it had been holding itself together out of its own pocket.

That is when she should have understood.  She did not.

She did understand one smaller thing, and she wrote it down, and it is worth having.  The dust that makes the Porter is the building falling to pieces.  He sits at the bottom of it and lets it arrive, and the more of him there is, the faster it comes down.  He is not old and he is not for ever.  He is a shape in a flow of ruin, and he lasts exactly as long as something upstairs keeps coming loose, and he is helping.

Nobody has ever put him on a maintenance schedule.

There is nothing in him to maintain.

## The Operations

| Line | Collection | Sampling | Expression | Retention |
|---|---|---|---|---|
| Genetic | gene flow in a deme / presence | segregation into gametes / heritability | development in morphospace / accessibility | germline transmission / reproducibility |
| Neuronal | perception in umwelt / perceptibility | retrieval from the repertoire / retrieval strength | performance in the motor repertoire / performability | consolidation / associability |
| Symbolic | acquisition from culture / learnability | lexical selection / lexical access | articulation in the vocal tract / pronounceability | re-transmission / grammaticality |
| Digital | dependency resolution / resolvability | merge in the working tree / reachability | the build in a type system / compilation | the commit / correctness |

Process before the slash, criterion after.
A process names an operation and the space it runs in, because neither half specifies it alone.  Development is not morphospace and morphospace is not a process.  The space is the domain the criterion is defined over, not the subset the criterion picks out.
Grammaticality and correctness are the same question in two media.
A merge does not consult whether the result will build.  That is the digital rendering of blind recombination, and it is why merge conflicts and broken builds exist.  The failure surfaces one stage later, at compilation.
The genetic Collection cell reads thin, and that is expected rather than a defect.  The genetic line is the Effector line, so its Modeler-stage entry is the one the Venn of Lines predicts will be weakest.
Pronounceability names the speaker's half of a pressure that has two halves.  If ease of articulation ran unopposed, every form would erode toward a single reduced vowel.  What stops that is perceptual distinctiveness, which is the standard account of why phoneme inventories are shaped the way they are.  Speaker effort pulls forms toward simplification.  Hearer recovery pushes them back apart.  Surviving forms sit in the trade-off.
The two halves sit at two stages.  Pronounceability gates what Expression can build.  Grammaticality gates what Retention will keep.
The understory's digital rendering has field-native neighbors.  Practitioners speak of a sandbox, and of development environments as against production environments.  Both name a space where a candidate is assembled and exercised before it is allowed to compete for anything real.
Programs have syntax, and syntax errors are caught at compilation.  Grammaticality at symbolic Retention and compilation at digital Expression therefore sit close without sharing a slot.  One gates the write and the other gates the build.
Wordlikeness is gradient phonological well-formedness, measured as phonotactic probability and neighborhood density.  It is the standard instrument for measuring how sayable a form is, which makes it an instrument rather than a construct.

## The Break Between Expression and Retention
Being expressed and being kept are different events, separated in time, and the boundary between them has its own gate.  Four lines make the break unmistakable.
At the genetic line an organism can compete well on somatic excellence and have none of it written down, because only the germline is transmitted, which is Weismann's barrier.  That the gate is a biased filter rather than a formality shows in meiotic drive and segregation distortion, where what gets into the germline is not a fair sample of what the organism carries.
At the neuronal line a behavior can be performed, be rewarded, and still fail to be retained, because consolidation is separately gated: the separation is measured in hours, and it runs offline during sleep.
At the symbolic line an utterance can be understood and never repeated: what is spoken and what is passed on are not the same population, and nothing guarantees the ones that travel are the ones that landed.
At the digital line a defect report can be correct, survive every analysis that produced it, and be recorded as a false positive because the engineer reading it did not understand it.  The report ran and was not kept, and nothing about its correctness was at issue in the refusal.
Four breaks at one boundary, and the boundary is a stage edge rather than a seam inside a stage.

## What the Liana Figure Carries
The four sites are one figure.  A liana runs a cycle over a seed bank, a clearing, an understory, and a canopy, and no one tends it.
Transfers: a store of dormant units that outlasts any individual; an opening that makes some of them viable now; a base that assembles and pushes; a canopy with a finite quantity of light in it, arriving one unit at a time, into which more is pushed than it has to give.  Nothing awards the light.  The budget runs out.  Each narrowing is unaimed.  The animal that carries a unit back to the store is not selecting for the plant.
Does not transfer: cultivation.  Nobody sows the seed bank, opens the clearing, or decides which stems are kept.  Nor does the figure carry any weight of its own.  The four stages are fixed twice over inside the framework, once by the sight and binding bits and once by absence-recruitment, and both derivations stand without the plant.
One thing the figure carries is not one of the four sites.  A standing stem spends to keep standing.  The bill scales with how much is standing.  Stop paying and it comes down.  That is the coin with a body under it, and reaching the canopy exempts nothing.  A stem that arrived still pays every day it stays.

## The Climb, the Trellis, and the Host
The climb has one support and one grid, and they do different jobs.
**The trellis is the grid.** It bears nothing.  It is made, and it is ours: the framework's own architecture, the functions, motivations, capacities, and breakthroughs laid out line by line and cell by cell across the twelve.  A unit moves up a grid the way a reader moves down an index.  That a framework is a made object is correct and says nothing about what holds the plant up.
**The host is prior structure.** It is wild, and it is not ours.  A liana climbs whatever got there first: the trees already standing, and the other lianas already in the tangle.  Nobody put any of it there for this plant's benefit.
The host also paid for it.  A climber reaches the light without building what holds it there, and Darwin gave that saving as his reason so many unrelated lineages took up climbing.  The saving is real and the cost does not vanish.  It sits with the host, who is also the party the climber then shades.  This is the displaced tax carried by an instance rather than an example.
The host fills a slot at every line.  At the genetic line it is the developmental architecture a new variant has to build inside.  At the neuronal line it is the repertoire already learned, out of which a new behavior is assembled.  At the symbolic line it is the conventions and institutions already in place, which a new form has to travel on.  At the digital line it is the existing codebase and the dependencies it already resolves against.
The climb is the cycle running, and it does two things at once.
The climb supplies direction.  Upward displacement is oriented whatever path it takes, and that orientation is all the figure needs from it.  Irreversibility is a separate claim resting on a separate ground.
Catching on the host supplies accumulation.  A liana's reach is set by what is already standing, and no liana reaches the canopy without something to climb.  Each turn starts from what earlier turns left, and differently.  For a liana this is the growth form's defining constraint rather than an observation about it.
A regular spiral would give the first and not the second.  Fixed pitch and fixed radius make every turn the same shape, so no turn depends on what any earlier turn left standing.  That is a shape that repeats without a history, and inheritance is a history.
*lianas are structural parasites that depend on host support to reach the canopy, and their abundance in treefall clearings is established.  Darwin made the cost argument himself, in the climbing-plants work of 1865, not in the later movement book.  The split between a made trellis and a wild host is a framework commitment.  The four host renderings are framework inference and have not been checked against the per-line label libraries.  The host is a different object from the panels: panels are invariant parts held inside a unit, and the host is external structure the unit builds on.*

## Thermodynamic bridges to selection theory
Bridges from physics to evolutionary theory have two fates, and what a bridge proposes decides which one it gets.  A bridge that offers an accounting or a typology is absorbed.  A bridge that offers a drive is refused.  The record is consistent enough across a century that it is worth reading as a rule about the receiving field rather than as a series of separate verdicts.
**The absorbed bridges.** Landauer's 1961 result is taught, and so is Charles Bennett's 1982 account of Maxwell's demon, which locates the demon's unavoidable cost in erasing its own measurement record rather than in taking the measurement.  Steven Frank's reading of selection as the maximization of Fisher information restates the Price equation in another currency and leaves population genetics standing.  Christoph Adami's information-theoretic measures of biological complexity give an instrument that measures a genome against its environment.  Maynard Smith and Szathmáry's major transitions is a typology, and it was taken up so completely that I can cite it as a neighbor without argument.  Each of these tells a biologist something about how to count.  None tells a biologist that selection is not doing the work.
**The refused bridges.** Boltzmann linked Darwin to thermodynamics in an 1886 lecture, casting the struggle for existence as a struggle for available free energy.  Lotka's 1922 maximum power principle set the template that repeats afterward: a careful scientist proposes that selection maximizes a thermodynamic quantity, the proposal turns out not to be derivable, and less careful people adopt it anyway.  Prigogine was popularized past his own results, which attached a reputational cost to the vocabulary itself.  England's 2013 work on the statistical physics of self-replication shows the cycle still running: the press overclaims, biologists dismiss, and nothing careful in the middle is heard.
Schrödinger's 1944 lectures split down the middle, though not along the line usually reported.  The aperiodic crystal paid off.  Negative entropy drew doubt and opposition from physicist colleagues, and the note printed with the first edition answers them.  He concedes that free energy would have been the better term had he been writing for physicists, and explains that he avoided it for his actual readers because it sits close enough to plain energy to hide the contrast he wanted drawn.  He gave up the word for one audience and kept the claim.  To F. Simon's sharper objection, that the account does not say why an organism needs ordered compounds rather than fuel, he answered by adding the heat the organism sheds, which extends the argument rather than withdrawing it.  What circulates now is that he admitted a mistake and should have written free energy.  I have read the note.  The distance between the note and its reputation is the whole mechanism, running on a primary source rather than on a field.
H. T. Odum then demonstrated both fates in one career.  The Silver Springs energy-flow accounting entered the textbooks and stayed.  Emergy and transformity, which propose that embodied energy is the universal currency explaining why systems take the forms they do, stayed inside their own school.  The objection that settled it came from economics, which is the field where emergy makes its claim about value.  Emergy prices a thing by the energy that went into producing it and has nothing to say about what anyone wants, so it is a theory of value with only a supply side (Spreng 1988; Ayres 1998; Cutler Cleveland, Robert Kaufmann and David Stern 2000).  One half of Odum's program measured.  The other half told a field what its quantities meant.  Only the measuring transferred.
The line runs through careers rather than between them.  It splits Odum.  It splits Schrödinger inside a single book.  It splits Stuart Kauffman, whose fourth law is declined while his collectively autocatalytic sets are kept as an accounting.  So the pattern does not record which scientists were careless.  It records which claims a field can absorb.
**The operative mechanism is the skyhook.** Odum is evidence about the world.  A program of exact energetic accounting was built, funded, staffed, and published for decades, and it did not transfer outside its own school, so the failure is not explained by anyone having failed to try.  Dennett's distinction is evidence about the audience, and it is the one that governs how any of this will be read.  A skyhook is an explanation that hangs from nothing and does the design work for free; a crane is machinery that does the work by standing on what came before.  The distinction gives a biologist a way to classify an argument by its shape and reject it without reading its specifics.  Any argument in which physics appears to be doing what selection is supposed to do reads as a skyhook on first contact.  That is the reflex I have to clear, and clearing it is a matter of being visibly a crane rather than of being right.
Route matters too, not only shape.  Frank published inside evolutionary biology, in a journal its practitioners read, where the claim was evaluated by people equipped to check it against what they already had.  England published in chemical physics, and the version that reached biologists arrived through popular coverage that had already overstated it.  A claim entering a field through its own literature gets read.  A claim arriving as news gets classified.  Which of route and shape carries more weight I do not know, and the two are correlated in every case above.
**So here is where I stand.** I am proposing an accounting and a typology.  Four denominations classify what each function works and what each stage of the cycle discards, and four selection biases classify what a selector credits.  I decline the thermodynamic-imperative reading outright.  Entropy supplies the arrow.  Selection supplies every aim.  Nothing in the geometry asks physics to choose.  The neuronal-line formalism is held to its own line: the Regulator's work is counted in variational free energy, and I record that the principle is a redescription rather than a cause, on its originator's reading.  I claim no more for that quantity than the person who wrote it down does.
This is a modest claim about energy and a strong claim about structure, and the modesty is placed exactly where the record says a bridge fails, and nowhere else.  Exact thermodynamic accounting of *selection* has no research program behind it and I do not need one.  The narrower claim is required, because thermodynamic accounting of particular biological processes is productive: kinetic proofreading, after Hopfield and Ninio, buys real biology from an exact energetic budget, and molecular motor thermodynamics does the same.  What has never formed is a program that prices a selective event.
*The publication history above is established and checkable.  The rejection of emergy on supply-side grounds is a documented position in ecological economics rather than my reading, and its scope is that field; no comparable formal rejection was issued in biology, where the program was simply not taken up.  The two-fates pattern is my reading of the history, well supported by the cases listed and not derived from anything.  Identifying the skyhook reflex as the mechanism that governs how this will be read is my position, and my own placement on the accounting side of the pattern follows from the decline and adds no new commitment.*

---

## The Visible Tax
Entropy is the ground.  Order is the expensive, surprising thing; decay is the free default.  Poverty needs no explanation and wealth does, because things fall apart when left alone.  This is established physics the framework stands on: life holds its own entropy low by importing concentrated energy and exporting dispersed waste.  Schrödinger put the question in 1944 and Prigogine's dissipative structure is the standing term for the answer, with one limit: the framework takes the structure and not the drive.  Every unit the framework describes persists only by doing work against this ground.  The floor has an informational face as well as a thermodynamic one: every discard is paid in heat at the bottom, whatever denomination it is counted in.
From the floor follows a conservation law.  You cannot remove the cost of a thing coming apart.  You can only move it.  The cost moves forward in time, or sideways onto another payer, but it does not vanish.  A slick sealed unit and a serviceable one do not differ in whether the bill is paid; they differ in when it comes due and who is standing there when it does.
A second conservation law runs the other way.  The first prices a thing coming apart.  The second prices a thing being put together: any local increase in order exports disorder, and no arrangement of the work removes the export.  These are two conservation laws and not one stated twice.  Keeping them apart is what keeps the audit honest, because a unit can be scrupulous about the cost of its own decay and silent about what its assembly cost everything around it.
Maintenance is the work that funds the bill.  The Regulator is the function that does that work: it holds a reference and drives the unit back toward it against perturbation.  Negative feedback is its charter, and homeostasis is its founding case, Wiener's loop and Cannon's regulated body.  To maintain is to keep paying the entropy tax so the unit stays far from equilibrium one more cycle.  That payment is the ratchet's third part.  A ratchet needs undirected variation, a rectifier, and free energy spent to reset it each turn, and without the third it is a perpetual motion machine.  Maintenance is the reset.  The reset is what lets the loop run again, and selection is the loop, and the two are one process seen from its paying side and its choosing side.  The reset and the conservation law above are two claims and not one.  The reset says a turn costs something every turn.  The conservation law says a cost has a payer, and that it can be moved but not removed.
The keystone is an audit.  A maintenance architecture is clean when its tax is visible to whoever pays it, and it is a kludge when the tax is hidden.  Hiding takes two forms, and they are the two directions the conservation law allows.  The tax can be deferred, hidden in time from the future payer.  Or it can be displaced, hidden from a payer who was never in the room.  Call the whole apparatus the visible tax: the physics is that the tax is always levied, the audit is whether it is visible, and the ethics is that concealing it from its payer is the core move of every maintenance failure that is not innocent.
*the entropy floor and the Regulator's maintenance role are settled.  The conservation law and the visible-tax audit are framework theoretical commitments, assembled from the maintenance-philosophy tradition.  Identifying maintenance with the ratchet's reset is a further commitment, following from the ratchet mapping.  The ethical reading is stated here as framework content, because the framework's failure taxonomy is already a moral object.*

## The Seam: What Maintenance Holds Invariant
*"Good seams make good neighbors."  After Robert Frost, "Mending Wall," itself a poem about the tax of keeping a boundary.*
Maintenance is not the freezing of everything.  A unit that held every part rigid could not vary at all, and could not be repaired part by part.  Maintenance holds invariant a specific, sparse set of parts, so that change elsewhere does not destroy the unit.  Those held-invariant parts are the panels; the places where change is allowed are the seams.
The seam is a thin link: a connection carrying almost no information, a switch rather than a specification, so that either side can be rewired without redesigning the other.  The panels are the deeply reused machinery that never gets touched.  A good seam sits where the unit already articulates, at a joint the structure has rather than a cut made against the grain.  In the crease pattern the fold lines carry the articulation and the panels stay rigid, and that is the origami identity.  It also states the condition: a seam needs a reused unit to switch.  Where every function had its own dedicated module nothing would be shared, nothing could be cheaply redeployed, and there would be no thin switch to cut.  The enhancer needs a reused gene, the sign needs a reused signifier, the crease needs one sheet, and the cortical setting needs one shared circuit.
Each slack has its own seam.
- **Genetic slack: the enhancer.** A cis-regulatory switch decides where and when a gene fires without altering the gene.  The stickleback loses its pelvic spine by deleting one tissue-specific enhancer while keeping the gene it still needs elsewhere.
- **Neuronal slack: the calibrated cortical setting.** A thin regional setting — spine density, the excitation-inhibition ratio — redeploys one shared circuit for a local job.
- **Symbolic slack: the arbitrary sign.** The link between a sign and its meaning is conventional, so a word can be reassigned or extended without rebuilding sound or sense.  Polysemy is the symbolic enhancer.
- **Digital slack: the crease.** The fold lines articulate; the panels hold.
The genetic seam closes too, and its closing is the older, better-named case.  Every cell carries the same genome, so the genome is the shared machinery; what redeploys it for one cell's job is the epigenetic state, the pattern of methylation and chromatin that switches genes on and off without touching the sequence.  That state is a maintained switch.  At each division the epigenome is copied onto the daughter strand, which is how a liver cell stays a liver cell across a lifetime of divisions without editing its DNA.  The epigenome is the genetic line's homeostat, and what it maintains is which seams are open.  Reprogramming a cell back toward a stem state is reopening that window.  So the enhancer is where the genetic seam is placed and the epigenetic state is how it is set: the coding sequence is the panel, and regulation is the seam.
The neuronal seam closes the same way, and there the cut-and-set operation has a precise molecular mechanism: the sensitive period.  Experience opens a window, parvalbumin maturation triggers onset, perineuronal nets brake closure.  Pruning then sharpens selectivity without changing what the circuit computes, using far fewer connections for the same task, so the reward system still learns reward and the whisker map still maps whiskers.  Closure locks the setting into structure, so it cannot be dialed back without reopening the window.  This is the neuronal line's version of a fold that holds once made, and it settles what the earlier precision reading was reaching for: precision-weighting is the runtime face of the same regional setting the sensitive period fixes in place, the moment-to-moment expression of a seam that development already cut.
Degeneracy is the mechanism that gets robustness and evolvability at once, and it is not redundancy.  Redundancy is identical backups; degeneracy is structurally different parts that can cover the same function.  A degenerate architecture maintains itself when a part fails, because another kind of part takes the load, and it varies well, because the spare parts are raw material for new functions.  Degeneracy is how a unit keeps the panels holding while the seams stay open.  The genetic code is the textbook case: many codons map to one amino acid, so most single-letter changes are silent, and the code is at once robust to error and free to wander.
Seams are not placed by foresight reaching for future variation, because nothing blind reaches forward.  They fall out of paying less.  Wiring is anti-entropic work paid to build and to maintain every cycle, in volume, in conduction delay, and in metabolic upkeep; the genetic form of the same charge is pleiotropy, where one edit to a reused gene strikes every job it does at once; the institutional form is concentrated power, where striking one office strikes everything.  Each is paid down the same way, by putting a separate switch on each deployment.  So the causal order is clean and it keeps each function in its place: selection bites on cost, the Regulator economizes the maintained architecture to meet it, re-cuttable seams fall out as a byproduct, and the Reviser is freed to cut them.  Evolvability is never the target.  It is what rides along when maintenance is made cheap.
The reading here: weak regulatory linkage and the conserved core processes are Kirschner and Gerhart; the wiring economy is Bullmore and Sporns, who call it the economy of the brain; the evolved-modularity demonstration, where a penalty on connection count produced modularity that selection for performance alone did not, is Clune, Mouret and Lipson; the two shapes a clean seam takes, parcellation and integration, are Wagner and Altenberg; the canalized valley is Waddington's; and the network-neuroscience work ties the connectome's sparse between-community ties to the same evolvability.
*The enhancer seam, degeneracy, and the epigenetic maintenance of cell state are established biology.  The shared circuit, sensitive-period calibration, and pruning-tunes-selectivity are the mainstream neuroscience reading; the live counterpoint is primary sensory cortex under early deprivation, where whether repurposing is genuine or potentiation of pre-existing wiring is unsettled, which touches the bottom of the hierarchy and not the shared-circuit claim above it.  Reading the epigenome as the genetic line's homeostat, and the four seams, are mine.  So is the byproduct account of evolvability, and it runs at three lines: connection cost in the brain, pleiotropy cost in the genome, concentrated-power cost in institutions.*

## The Residue and Its Payer
Selection buys every gain in fit with a much larger volume of discarded variants, and the discarding is the mechanism rather than waste in it.  What belongs here is that the residue is not incidental to the process and cannot be reduced without stopping it: attention's residue is everything that stayed live and never won, and conversation's is everything thought and not said.  A framework whose failure taxonomy is already a moral object does not get to describe its own engine and leave that out.
What the residue is, though, is what stopped being funded rather than what the process destroyed.  Entropy takes it from there, and entropy was always going to.  The choosing and the paying are one process with one payer behind both.
So the moral weight does not sit in the dropping.  It sits in the paying, and the question the audit asks is whether whoever carries the cost can see it.

## What a Selector Credits
The sections above price what a thing costs.  They do not say what a thing is worth.  Those are two columns of one ledger, and the second column is already there under other headings.
Each of the four functions carries a bias in selection, the rule it applies to decide which cue to credit.  The four are recency at the Effector, familiarity at the Regulator, potency at the Modeler, and novelty at the Reviser.  Every line runs them through its own selector: differential reproduction at the genetic line, attention at the neuronal line, differential adoption at the symbolic line.
Read as a system, the four biases are the framework's account of worth.  Four denominations say what a thing costs, one per function.  Four biases say what a selector credits, one per function.  Neither set converts internally, and the two sets do not convert into each other.  That is why nothing in the framework has a price.  A price would be a rate between a cost and a worth, and no such rate exists anywhere in the geometry.
This is what answers the objection the framework levels at emergy.  Emergy prices a thing by the energy that went into producing it and carries no rule for what gets credited, which makes it a theory of value with a supply side and nothing else.  The four biases are the other side.  They are picking rules held by a selector at the moment of an event, which is why they come in under the accounting scope rather than the market scope: a bias credits the one competitor in front of it, and no interaction of parties discovers a rate.
The four biases do not read merit, and that is the section's moral content.  A bias credits a cue for being fresh, or established, or strong, or unfamiliar.  None of those is a claim that the credited thing is good.  None of them consults how well the thing does what it does.  So a unit can be excellent and go uncredited, and the mechanism will not register that anything was lost.  Salience decay is the clearest case: an item's contents stay exact while its odds of being picked fall, because what changed is the context that made it potent and not the item.
The gap between what is credited and what is worth having is where this Part's ethics sits.  The tax sections ask whether whoever carries a cost can see it.  This section adds that whoever a selector drops gets no account of why, because the selector holds no notion of desert to give one.
*the four biases and their per-line selectors are settled.  Reading the four as an account of worth, and as the counterpart of the four denominations, is mine, assembled out of them.  That the pairing answers the supply-side objection to emergy is a framework position.  That no bias reads merit follows from the definitions of the four biases and is not an empirical finding about any selector.*

## Going Down

### The pen, leaving the fourth floor

Less than a quarter of it left.  Dera did the sum three times on the stair and got three different answers, which had never happened to her before and has not happened since.

She asked all four officials to take their discounts back.

The Counter had not lent her anything.

The Storekeeper had never offered her anything.

The Keeper of the Rooms had not agreed to anything.

The attendant had no drawer for the request, and looked for one for a while, to be helpful.

You cannot hand back a thing that fell off somebody else's work, because the person it fell off never had it either.

Here is what she established instead, and it is the only useful thing in the report.

The rate belongs to the floor.  It does not belong to her.  The first floor charges in bodies.  It always has.  It has never asked to be let off and it lets nobody else off, and most of the Bureau by weight is still down there paying the full price, one attempt at a time, and doing perfectly well on those terms.

The floor does not care what she is carrying when she arrives.

So she went down.

### On the third landing

**The pen.** Three landings to go.  She stopped counting in words and began counting in lines, which is what a person does when a thing is nearly gone and they have not admitted it yet.

She went back along the corridor to the Registrar of Weather and stood in his doorway and said the word "storm" one last time, and he waited politely for her to finish.

Then she went and found the dinosaur with the grey crest, which took until four in the morning, and said the same word to her.

The woman stopped walking.  She looked up at the ceiling for a moment, working something out.

"Second week of October," she said.  "It comes in over the west side.  The gutter above the store is the one that goes, and it goes at the third bracket, and I replace the third bracket in September."  She patted the canvas roll.  "I've replaced it eleven times."

Now stop for a moment, because this is a thing about two people and they are on two different floors and it is easy to lose track.

**Person one.** A dinosaur with a grey crest and a canvas roll of tools, who goes on two legs with her tail out straight, walks the building at four in the morning, and tightens things that are not loose.  Her hands have no marks on them.

**Person two.** A small dry octopus on the third floor with his cuffs half an inch clear of his wrist, who keeps the finest books in the building and cannot hear the word storm.  His hands have no marks on them either, and he has eight of them.

The same hands.  Exactly the same.  Dera drew all four of them side by side in her notebook and could not tell you which pair was which.

Now, one of those two people is the size of a door and carries radiators about under one arm, and the other one is built like a bundle of pencils and needs both arms and his chin to move his own ledger, and you are entitled to ask how on earth she got them confused for three weeks.

Here is how, and it is not clever and it is not her fault.

She met the woman at four in the morning, in a corridor, kneeling on the floor with a tool roll open in front of her.

She met the man at a desk, sitting down, and he never once stood up while she was in the room, because he had no reason to.

**She never saw either of them standing.** She was going by the hands, because the hands were the only part of either of them she had ever seen at the same height, and the hands are identical.

And now you have just watched her say one word to each of them.

The man waited politely for her to finish.

The woman told her the month, the side of the building, the gutter, the bracket, and the number of times she has replaced it.

And then the woman stood up.

Dera had never seen her stand up.  She went up, and out, and up again, and she got to her full size, and the corridor was noticeably smaller with her in it.  She put her chin down and turned sideways and went through the doorway, and on the other side of it she picked up a sack of sand in one hand and went off down the passage with it swinging.

Dera sat down on a step.

One signature.  Forty years ago.  At a door.  For the whole of it.

And one floor above her a dry little man with exactly the same hands has never signed a thing in his life, and his sleeves have never once had to be let down, and he carries his own ledger in both arms with his chin on top of it.

There it is.  There is the whole difference.  It has been on both of them every single day, in front of everybody, and Dera had simply never seen either of them stand up.

She is enormous because she got there first, forty years ago, and put her name on it.  He is small because he has never touched anything.

Two people with the same hands, for opposite reasons.  That is why nobody in the building can tell them apart, and it is why Dera could not, and there was nothing wrong with her eyes.  From the outside, a person who takes care of things looks exactly like a person who has arranged never to be near them.

The only way to tell is to ask what each of them has let be heavy.

### On the second landing

She found the man with the scarred forearms putting in a hinge that had not broken yet, which is not his job.

"She's owed a day off," he said.

Dera looked at his arms for a long time, and he let her.

"Why don't you leave?" she said.

He thought about it, which almost nobody upstairs ever did.  "I could," he said.  "She could.  There's nothing holding either of us."  He turned a screw a quarter turn.  "That's the whole of it, though, isn't it.  Nobody has ever rung a bell at me.  I come in anyway."

"You get the worse half," said Dera.  "She goes round the night before and nothing ever touches her.  You come afterward."

"It's the same work," he said.  "Mine shows."

Everybody in that building has committed to things.  All of it has sunk down into them and become simply what they are, so that you cannot read it off anybody, which is how it works and why the Bureau is so hard to audit.

His went on the outside.  He is the only readable person on the premises.

**The pen.** Two landings to go, and enough ink for one filing.  Possibly not enough.

### In the courtyard

**The pen.** One landing left.  She held it up against the open sky, which is the only proper daylight she had in the whole six weeks, and the daylight was worse news than the lamps had been.

She had ten minutes she did not want, so she went out and looked at the vine on the south face.

It is as thick as her wrist at the bottom and grey-green all over, and it has no trunk.  Not in any sense she recognised.  There is nothing in it that stands up.  The whole of it is holding on.  Where it grips, the tendrils have gone woody, and the wood has taken the shape of the stone exactly, the way a cast takes a mould.

It is in full leaf at the fourth floor.

Its bottom thirty feet have no leaves, and will never have leaves again.

"Good afternoon," said the vine.

"Have you a permit?" said Dera.

"Framed," said the vine.  "In the groundskeeper's hut.  Correctly issued, properly countersigned, and I am extremely grateful."

"You didn't build any of this."

"No," said the vine, "and I want to be perfectly clear that I have never once claimed otherwise.  It was already here.  I am doing nothing that is against any rule."

All of that is true.  She checked it afterward and every word of it holds.

The stone underneath was cut and laid by people who appear in no minutes of anything.  Under the vine's grip it has gone soft and pitted and holds rainwater now, and the vine's own weight has opened two joints in the coursing.

The stone is in the vine's shade.  It is warm where the sun still gets to it and cool where the leaf has closed over, and that difference is the only piece of accounting anywhere on the premises that adds up.

"Has the stone anything to say?" said Dera.

The vine was very polite about it.  "The stone is not a party to anything," it said.  "Nobody put it there for me.  Nobody put it there against me.  I'm afraid there is nobody for you to write to."

She could price the vine's advantage exactly, to the inch, and she could bring no action at all.

And then she stood there rather longer than the schedule allowed, because she had just climbed four floors of a building she did not build.

## The First Floor Again

There is a woman on the first floor who works at a bench.

You met her a long time ago and there is no reason at all why you should have kept hold of her, so here she is again, all of her, in one place.

She is small and upright and about fifty.  She pins her hair up every morning and it takes a quarter of an hour and nobody sees it.  Her hands are thick at the knuckle and her nails are cut short and square, and there is a hard yellow lump on her right middle finger from holding a tool.

Nobody has asked her to hold that tool in nine years.

She dusts her bench every day.  She lays out every item in the order she would need it if the work came.  There is a clean apron on a hook and she puts it on in the morning and takes it off at night and it has never had a mark on it.

And she was the only person on that whole floor who looked straight at Dera when Dera spoke to her.  Everybody else looked at Dera's papers.

That is her.  Now.

The Woman at the Bench was at her bench.

Dera had checked her work independently and at length.  It is the only claim in the whole report she can prove to the standard her letter demands.  She is superb.  She has not been called in nine years.  She has not got any worse.

Dera went and fetched the Archivist and brought her to the bench, because somebody was going to say it out loud in front of her, and because there was no longer enough ink left to be delicate with.

The Archivist was kind.  She was kind the entire time.

She said the store is perfect and nothing in it has ever decayed, and she pushed the empty frames up onto her forehead and took down a document a thousand years old and showed them every letter of it, exact.

Then she showed them the register of what had been called for that morning.

The document was not on it.  It has not been on it for four hundred years.

"Was it withdrawn?" said Dera.

"Nothing is ever withdrawn," said the Archivist.  "People stopped asking for the things it sits next to, and then they stopped asking for it.  The document didn't change by so much as a letter while that was happening."

Then Dera asked her about the Woman at the Bench, in front of the Woman at the Bench.

The Archivist turned her whole head, the way she does, to put the good ear in front.  She thought about it properly, for a long time, and she was not defensive for one second.

"I stopped calling her," she said.

"Why?"

"I don't know," said the Archivist.  "I've thought about it.  Nothing in the choosing tells me that anything was lost."

Nothing in her face changed, because nothing had gone wrong.  That is the part that will not come out of the report, and it does not fit in any schedule.

The Woman at the Bench has nine years of weight on her and did not choose one hour of it.  She is not free and she is not light and she is not a model for anybody, and that is in the report too, because it would be very easy to make her into a lesson and she is not one.

"I built an explanation of myself out of the quiet," she said, when it was over.  "You do.  You build one out of whatever's lying about."

She is a payer.  She was not in the chamber.

There is no chamber on her floor.

## The Filing

Dera had one filing left.  She had walked in with it six weeks earlier and had never once had occasion to use it, because everything she had done in that building had been paid on somebody else's machine.

She chose the register at the Archivist's gate.  The same register.  The same column.  The one that had killed something in her first week.

Not because that is where she was hurt.

Because it is the place where the building bends.

It is the only register in the Bureau of Persistence where what you write lands on something and cannot be taken back, and if she had committed anywhere else in that building she would have been cutting across the grain, and it would have narrowed nothing, and she would have felt very serious and changed not one thing.

You do not simply choose to be heavy.  You have to choose where.

She wrote it in the wrong hand, without practising, because she did not go upstairs to draft it.

If it is wrong it will cost her a body and there is no relief.

Nobody gave her a docket for it.

She asked.  She stood at the gate and asked for one, twice, and the Archivist looked in three drawers and said, apologetically, that there is no card for a thing you have not been charged for, and that she had never in fifty years been asked for one before.

So there are four dockets in Dera's pocket for four mistakes that were charged to her, and the fifth thing, the only one she chose, has no card and no stamp and no number.

And it has no line for a countersignature anywhere on it.  She turned the page over and looked on the back.  There is no line on the back either.  There has never needed to be one, because in the ordinary way of things nobody signs a thing they were not charged for, because why would they.

So she wrote her name in the margin, where there is no line.

Now.  Here is what happened next, and it happened in front of the Archivist, and a slime mold from the store, and a sensitive plant that had come in about a gate key, and all three of them saw it, and this account is going to go slowly.

She got bigger.

Not the thickness of a slice of bread.  She went up like a hand going up in a classroom, and out with it, and through the shoulders, and the back of her jacket went at the seam with a sound everybody in the room heard.

Her cuffs went up her wrists and stayed there.  Her collar came undone at the stud.  The bench she was leaning on came up to her hip and then to her thigh.  The floor said something about it.

She put a hand out on the counter and the counter creaked, and the Archivist moved the inkwell out of the way without being asked, the way you do when somebody knocks a table.

And everything on that desk slid a quarter of an inch toward her.  The blotter.  The tin of oil.  Both pairs of spectacles, the ones with the lenses and the ones without.

Every floor in that building is a little lower in the middle than at the walls, which the Porter told her in her first ten minutes on the doorstep and which she wrote down and did not think about again.  There is now a new low place on the first floor.

It is her.

The Archivist looked up at her.  Up.  She had not had to do that before.

"Well," said the Archivist.

Then Dera turned to go and walked straight into the doorframe with her shoulder, hard enough to stop her, hard enough to hurt, because she had gone through that particular door eleven times a day for six weeks and had never once had to think about it.

She backed up.  She put her chin down.  She turned sideways.

She went through.

It took the last of the ink.

And then, standing at the gate with an empty pen, she remembered the sheet of paper in her inside pocket, and took it out, and unfolded it, and read the five words the copy had brought back four weeks before.

**It was already two.**

You have been carrying those five words for four weeks as well, and you have known the whole time what they were about, because you were standing on the step when it happened.

Dera worked it out at the gate, holding the paper, with ink on her fingers.  It is about the small thing in the dust.  It came back as one and it came back as two and there is no difference between the mending and the multiplying, and the copy had gone all the way up the building and all the way back down and had found nothing better to bring her than a fact she had been given for free in her first hour by a man on a stool.

She put the paper back in her pocket.  She has it still, along with the four dockets.

### What the Archivist did with it

The Archivist took the report and entered it and shelved it in the perfect store where nothing decays.

She wrote the entry in her own hand, out of a bottle of ink that gets refilled on Fridays.

Dera watched her do it with an empty pen in her fist, and did not say anything about that either.

"The contents will stay exact," said the Archivist, without looking up.  "For ever.  I can promise you that much and I can promise you nothing else at all."

"Who will call for it?"

The Archivist pushed the empty frames up onto her forehead and thought about it properly, for a long time, the way she does.

"That depends on whether people go on asking for the things it sits next to," she said.  "And that is not a thing anybody decides."

## What Dera Found

The tax is being collected and it is being paid, and she can tell you by whom.

By the Doorkeeper, who is a line.  By the woman whose file has one number.  By the forty who move like a curtain going up.  By a silo three sizes too big, soaking up what nobody asked it to soak up.  By two people with one key ring who could leave and do not.  By everybody one floor under every chamber.  By the stone under the vine.  And by the Woman at the Bench, in a currency that has no name, because nine years spent waiting are spent all the same.

Somebody owes for all of that, everywhere in that building, and there is nobody to send the bill to.

And here is the part her letter asked for, so it goes first and it goes in plain words.

**The fourth floor is not committing a fraud.** Its machine runs in the open at the head of the stair and it roars, and it pays out thousands a second, and two attendants polish it.  The old man at the end of the eastern corridor keeps that floor's accounts and they balance to the last unit, and he will lift each half of the book for you to prove it, and in all the years he has been down there not one person has walked along that corridor to ask him.

**What the fourth floor does not pay for is the material.** Every grain of it was foraged.  It was grown downstairs, at a price, in iron and yards and words, and it was carried up by attendants who are proud of the carrying and who have never grown anything in their lives, and who tell you so at once if you ask.

So somebody paid for that attendant.  It was paid for before he existed, on three floors, on three different machines, by parties who were not asked and could not have been.

**And no crime has been committed, and this is why.** A crime needs a transfer.  A transfer needs a rate.  Dera tried four times to get a rate and the four attempts are set out above: a man who does not know what a yard is, a flagman who laughed, a question paid into a tube and gone, and fourteen tables that do not agree.

There is no table.  There is nothing to write on a charge sheet.  The debt is real, the beneficiary is real and cheerful and wears a little cap, and there is no line anywhere on any form where the amount would go.

There is no authority that set the rate.  There is no fifth floor, so nothing sorts what the fourth one makes.  There is no office anywhere in the Bureau that asks whether a thing is any good.  And the four floors do not exchange, so nothing that costs something on one floor can be set against anything worth having on another, which means nothing in the Bureau of Persistence has a price at all, which means no bill she could have written would have had a number on it.

Three further findings, and they are the ones she was sent for and did not expect.

**The first.** Nobody in that building ever tried to stop her.

The Bureau has three ways of not paying what it owes.  It can push the bill forward in time.  It can push it sideways onto somebody who was not in the room.  And it can see to it that no card is ever stamped against the person asking, which is the cleanest of the three by a long way, because a question with nobody's signature under it is a question nobody has to answer, and there is no rule anywhere that says so, and there is no rule anywhere that needs to.

She climbed four floors entirely of her own accord.  She was discounted at every landing by officials doing their own jobs, who meant her no harm whatever, and she was helped up the last two by a man whose warmth is made on the floor below him and who never lied to her once.

Her danger was the only power she had.  In her first week a question of hers was answered and the answer was signed by twelve people.  In her sixth week she asked nineteen questions on the third floor and every docket has one name on it, and the name is hers.

**The second.** In the whole of the Bureau of Persistence, across four floors and both crowds and four hundred years of minutes, she found exactly one thing that was being used up.

The direction is not billed to anybody.  It is in the walls, and in the chimney nobody has found, and in the floor that falls away from the walls in every room, and there is no card for it and no book with anybody's name in it, and it points at nothing at all.

The weight was not free, and it was not anywhere in the building.

It was in her pocket.  It ran out.  And it ran out at exactly the same rate whether or not she spent it on something that landed.

**The third, and it was on the doorstep the whole time.**

There are two things outside that door that come back when you break them, and only one of them is paying.

The rings in the dust come back and **no bell rings.** She broke them eleven times in her first hour and eleven times they came back, and no number was said out loud by anybody, and nothing went on any machine, and there is no figure for them in either chalk column.

The small thing beside them puts itself back together because there is something it is trying to be.  It held on through all eleven seconds out of its own pocket, and it is the first thing in the whole arrangement that ever paid for anything.

And it was already two.

She broke it twice.  Once it came back as one and once it came back as two, and there is no difference between the mending and the multiplying, and nothing about the breaking decides which you get.

So there was nobody to bill on the first day either.  Before the building.  Before the floors and the signs and the chambers and the four hundred years of minutes.  The very first thing that ever paid for itself was already two things by the time it finished paying, and neither of them was the one that owed.

The Bureau's three ways of hiding a bill are not why nobody can be charged.  They are what a very old condition looks like once it has four floors and a staff.

## The Doorstep Again

Dera came down the last flight with an empty pen.

Her coat was on a hook behind the Porter's stool.  It had hung six weeks at the lowest point in the building, and it was grey now, all of it, the same grey as him.

She looked at it for a while.  It is a good coat.  It was not hers any more.  It belonged to a woman who had walked in through that door with two things and no history in that place and nothing yet that anybody could take off her, and Dera could not get back into it and did not want to try.

He did not offer it.  She did not ask.

She sat down on the step next to the stool, which nobody has ever done, and she took four pages out of her notebook and laid them out on the stone in a row.

Four pages.  Four headings.  Here they are, all together, for the first and last time.

**ACOUSTICS.** The bell rings on all four floors and nobody upstairs looks up.

**MISSING DOCUMENT.** No machine in this building can read another machine's number.

**PERSONNEL.** Barnes was not brought back.  A new attendant was made out of the store.

**INVENTORY, PRELIMINARY.** Every grain in that store was fetched from somewhere else.

She had been carrying all four of those in one notebook for a fortnight and had never once had them out on a table at the same time, because she had been busy looking for a different piece of paper altogether.

While she was doing it the Porter got out the brass scales and the tin scoop and weighed the day's dust, exactly as he had on her first morning, and chalked the figure on the stone in the big column in figures four inches high.  Then he weighed the little pan and chalked the small figure in the second column.

Then, from inside the building, the bell rang.  Once.  And every person on all four floors said "one" out loud together, and nobody upstairs looked up.

Dera watched all of that with her four pages in front of her, and then she said it, flatly, in the voice she uses for reading out a total.

"Nobody up there is cheating," she said.  "The bees pay for everything they do.  It's all on the machine and the number is right.  What they don't pay for is what they're made of.  It gets fetched.  It gets fetched from downstairs, where it was already paid for, in iron and yards and words, by people who were never asked and couldn't have been asked, and most of them were dead before any of it went up the stairs."

"Mm," said the Porter.

"So Barnes was paid for before Barnes existed."

"Mm."

"And there's no bill I can write, because there's no rate.  Four machines and not one of them can read another one.  So the debt's real and the man who's better off is real and he wears a little cap, and there is no line on any form in the world where I could put the amount."

"That's right," said the Porter.

He said it the way you would agree that it looks like rain.  He did not look up from the chalk.  He was not pleased for her and he was not sorry for her and he did not appear to find it interesting, and he had known it since before the building was put up, and he had told her so in her first hour and she had written it down as a curiosity.

"You could have said," said Dera.

"I did," said the Porter.

"Pick up the stool," said the Porter.

Dera picked up the stool.

She did it with one hand, without thinking about it, the way you pick up a cup, and she was holding it out at arm's length at the height of her own shoulder before she noticed what she was doing.

On her first morning it had taken both hands and got as high as her knee.

She put it back down very carefully, because the Porter was going to want to sit on it.

"Right," said the Porter, and wrote something down.  "Against the frame."

Dera put her back against the doorframe of the Bureau of Persistence, which is covered from top to bottom in hundreds of little pencil marks with names and dates beside them, and the highest ones out of reach.

The Porter laid the ruler flat on her head, made a mark, and wrote **DERA** beside it and the date.

Then both of them looked at the frame.

There are two marks with her name on them now.  The first is very low down, from six weeks ago, when a woman came up the road with a letter and a pen and a good coat and nothing else at all.

The second is a long way above it.

Not the highest mark on that frame.  Not close.  There are marks up there he would need the stool for, and one of them is nine feet off the ground and has a name beside it that she recognises.

But there is a gap between her two marks that you could lay a hand in flat, and you can see it from the road.

"Does anybody read those?" said Dera, because she had asked him the same question on her first morning, about the chalk.

"No," said the Porter.

Then he said, "Post goes out through me.  Everything that reaches me goes nowhere else, and everything that leaves goes past this stool."

"I know."

"Six weeks before you came," said the Porter, "a letter went out of here addressed to an office that does not answer letters.  It came down the stairs in the hands of an attendant and I put it in the bag myself, and I remember it, because in all the years I have been sitting here it is the only letter that has ever left this building with an attendant's own name written at the bottom of it."

Dera sat very still on the step.

"Which name?"

The Porter told her.

She had pulled that one's curtain back for it, on a Tuesday afternoon, because it could not reach, and she had asked it whether it was sorry and it had said no.

"It asked for me," said Dera.

"It asked for somebody," said the Porter.  "You're who came."

"Let me see the pen," said the Porter.

She gave it to him.  He held it up to the light, the way she had done five times on five landings, and his hands are so dry that the celluloid squeaked.

"Empty," said Dera.

"They're all empty," said the Porter.  "Every one of them, in the end.  Whether or not they were used for anything."  He gave it back.  "Did you spend it?"

"On one line," said Dera.  "In the wrong hand.  It may cost me a body."

"Then it landed," said the Porter.  He put the pen down on the step beside the scales.  "And what IS an auditor?"

Dera thought about it for a good while.  It is the fourth time she had been asked in six weeks and she had got shorter every time, and this time she went the other way.

"Somebody who signs for the answer," she said.

"Ah," said the Porter.  "Then that's a different job from the one you came in with."

"Yes."

"Better?"

"Fewer of them," said Dera.

And then he picked up the chipped white cup, which had been full to a quarter inch below the chip for six weeks and had never once been filled, and he held it out to her, with the small six-sided columns still turning in it.

She drank it standing on the step.  It was the only warm thing anybody gave her in the Bureau of Persistence.

"Thank you, Dera," said the Porter.

He put the coat back on the hook.  He did not ask her to take it and he did not throw it away, because nothing that reaches him goes anywhere else.

And she went out past the step, which finished wearing a long time ago, and past the rings in the dust, which were back.

## When the Tax Comes Due
Maintenance failure is the tax collected.  The framework already sorts it by line, and each line's failure is a mode of the Regulator's job not getting done.
Disease is genetic-line maintenance failure: cells and tissues that no longer hold homeostasis.  Cancer is maintenance stopping, a lineage of cells that defects from the body's held reference, and much of that defection is the epigenetic homeostat failing, cells losing their maintained state and rolling back up the landscape toward a less-differentiated one.  The tax comes due in the body.
Disorder is neuronal-line maintenance failure: a unit that no longer regulates its life against what its situation demands.  Here the tax is paid in suffering, and the framework does not flinch from that.  The felt suffering of the disordered unit is the tax made conscious, and its moral weight is why disorder matters differently than a spec sheet does.  Whether that suffering is visible to others, or dismissed as weakness, is the politics of the tax at the scale of one life.
Disorganization is symbolic-line maintenance failure: institutions and norms that no longer regulate collective life.  Durkheim's anomie is the founding description, and social disorganization is the modern term.  Its characteristic form is the unowned seam, the thin, cheap-to-change switch that maintenance ordinarily keeps assigned and watched.  An institution runs a fast layer and a slow one, a quarterly clock and a mission measured in decades, and if no load-bearing seam is placed between them the fast clock silently re-cuts the slow kernel one defensible decision at a time, until the thing the institution was built to do is gone.  Nobody chooses this, which is what makes it maintenance failing rather than a crime: the granularity was never owned.  The repair, where anyone attempts it, is a load-bearing seam placed between the fast layer and the slow one, so the fast layer can fail without deforming the slow one.
The moral edge is sharpest here, and it is where the visible tax becomes a political claim and not only a physical one.  An institution's fauna is not sentient; the constituent people whose lives it runs on are.  So the institution is the one kind of organism whose deciders and whose payers are different beings, the one kind that can hide the tax from those who pay it.  When it defers its own maintenance the deferred bill comes due on the flora, on people who were not in the room when the deferral was chosen, and the fauna that chose it cannot itself feel the cost.  Crumbling infrastructure and unfunded obligations are Crowhurst's failure at the scale of a civilization.  This is the displaced tax: the cost moved onto a payer who could not see it coming and did not get a vote.
The maintenance-blind unit fails by regime mismatch.  A unit with the Regulator root switched off pursues without holding any reference, and it survives only in a world calm enough that no reference needed defending.  The Pursuer is that unit, the Regulator-absent capacity, gate-slipping with no held reference.  The valence is set by the weather, not by the capacity: in an expansive regime the same act is alloparenting, and in a storm it is what Donald Crowhurst did.  Crowhurst faked a round-the-world voyage rather than face the risk of sailing it, and his failure is not a third mode of maintenance.  He is maintenance switched off while dressed as a plan, and he loses in every weather, because he bet there was no floor when the floor is entropy itself.  His mirror is the unit with the Reviser root off, which defends its reference faithfully and dies when the world shifts, the way an entrenched structure everything was built upon cannot be re-cut without catastrophe.
*the line-failure taxonomy is settled.  Reading each failure as a form of the visible tax, and the moral weight I put on suffering and on the displaced institutional bill, are mine.*

## The Art of Maintenance
The counter-image to failure is the maintainer's grace.  Maintenance done well is not only a cost paid.  It is a source of meaning, a competence and an attention to the maintained thing that returns something to the one who pays.  Crowhurst resents maintenance, not from laziness but because a model that deleted the storm reports that the tax is not owed.  The maintainer is the unit whose model keeps the floor in view, and who finds in the paying of the tax a relation to the maintained thing Crowhurst never has.
What the maintainer does is invisible exactly when it works.  A maintained thing shows no trace of the upkeep that holds it: the healthy body, the machine that runs, the institution that functions all look effortless, and the effort is hidden by its own success.  So the one who pays the maintenance tax is the least likely to be credited for it, which is the displaced tax seen from the maintainer's side, the flora who carry the fauna now looked at directly.  Here the craft and the ethics are a single fact.  The attention the maintainer spends on the maintained thing is a real competence, and it is spent where no one is looking, on work noticed only in its absence.  His model does not only delete the storm; it deletes the one who keeps the storm out.
The same invisibility falls on the maintained thing, and that case is harsher because it arrives looking like a verdict.  An item loses salience while its contents stay exact.  What the store stops picking is then not what failed but what stopped being visible, and nothing in the picking tells the two apart.  Pointed at objects this is an archive going quiet.  Pointed at people it is a population declared surplus, and the declaration will present itself as a finding about them rather than as a fact about the store's reach.
Harari's forecast is the version of this a reader can stand inside.  He projects a large class of people rendered not merely unemployed but unemployable, surplus to an economy with no remaining use for what they can do, and he names the condition irrelevance rather than poverty because the two are different complaints.  The framework does not have to accept the forecast to say what would make it land the way he describes.  Collection weights potency, and potency is not merit.  A person's competence can stay exact while the context that made it potent disperses, and the store will stop picking them without registering that anything was lost.  This is why the reader is a plausible payer here rather than a spectator: the mechanism does not read merit, so being good at the thing is no defense against the thing going quiet.  And the bill is displaced in the sense already given, since whoever gains from the store's re-sorting is not the one who carries it and was not in the room when it happened.
This is where maintenance meets beauty, and the meeting is not sentimental.  Nature does have one literal aesthetic, and it is not design but choice: the mate preference that shapes form for its own sake, the peacock's tail, the bower, the flower that is beautiful because it evolved to be chosen.  Choice does not overturn the primacy of upkeep, though.  It advertises it.  Zahavi's handicap says why.  Ornament is expensive and useless, and that is the point, because only a unit whose maintenance is so well handled that it can afford to waste resources can grow one.  Beauty is discretionary spending after the tax is paid.  So the display aesthetic is not a rival to the maintenance one; it is maintenance's visible dividend, the margin a well-kept thing can afford to show.  The beautiful thing is the thing whose upkeep is secure, and ornament is the visible tax read from the far side, not the cost of persisting but the surplus left once persisting is no longer in doubt.
That is beauty as nature makes it, in the surplus, and it is given rather than chosen.  There is a further aesthetic that needs nothing from nature, and it is the one this framework keeps.  It finds the beauty not in the margin left after upkeep but in the upkeep itself, in the wear and in the repair.  Wabi-sabi is its name in one tradition, an aesthetics of the maintained and the worn.  Kintsugi is its clearest object: a broken bowl mended with gold along the break, so the repair is not concealed but made the most beautiful part of the thing.  That is good seams make good neighbors turned into a bowl, the seam gilded rather than hidden.  Functional beauty is the philosophy under it, the account from Parsons and Carlson on which a thing's fitness to its function is a genuine source of its beauty, not a substitute for beauty.  And the move that makes it available is small and entirely a choice: you do not need nature to hold this aesthetic for you, you need only notice that maintenance is the load-bearing pattern of everything that persists, and adopt the stance that finds it beautiful.  The surplus is a beauty a peacock cannot help; the mend is a beauty a maintainer decides to see.

*the maintainer's grace draws on Brand and Pirsig.  Sexual selection and the handicap principle are established biology; reading nature's display aesthetic as the advertisement of maintenance surplus, and beauty as the dividend of upkeep, is a framework theoretical commitment.  Wabi-sabi and kintsugi are established aesthetic traditions, and functional beauty is an established position in philosophy (Parsons and Carlson 2008).  The larger stance, that maintenance is nature's load-bearing pattern and that finding the mend beautiful is a chosen posture rather than a claim about nature's own experience, is a framework position, not a theorem.  Harari's projection of a large unemployable class is a forecast rather than a finding, and the framework cites it as the reader-facing case of the mechanism without endorsing it.  Reading that case as displaced tax is a framework theoretical commitment.*

A repair is a record of a load the design did not anticipate.

Nobody patches a thing where it held.  The patch is at the place the drawings were wrong.  So if you want the honest history of a structure, do not read the drawings.  The drawings tell you what somebody hoped for.  The repairs tell you what actually arrived.

And a repair is dated, whether or not anybody wrote the date on it.  You can stand in a plant room and read forty years off the pipework.  Here is a line rerouted around something that is not on any drawing.  Here is a valve moved eighteen inches to the left, which is exactly far enough that a person can get a hand on it.  Here is a second pump, put in by somebody who had stopped believing the first one was going to be all right.  Every one of those was decided by a person standing in that room with the thing in front of them, at seven in the morning, with the building already cold.  None of them signed anything.  It is the best writing in the building.

Now disorder.

I have said what failure is at each of the three lines and I am going to say it once more, short, because I am about to ask something of it.  A genetic-line failure is a cell or a tissue that stops holding its own state.  A neuronal-line failure is a unit whose dispositional structure stops regulating its life against what its situation is asking.  A symbolic-line failure is a set of institutions and norms that stops regulating collective life.  Disease, disorder, disorganization.  Three lines, three vocabularies, three sets of people who do not read each other.

That taxonomy says *what* comes apart.  It does not say *in what order*, and the order is the whole finding.

Here is the claim.  The stack does not fail evenly and it does not fail randomly.  It sheds from the top down.  The most recently installed layer goes dormant first, then the one under it, and each layer that goes exposes the one beneath, which is still there and still working and was never broken.  Failure runs the build order backwards.

I did not get there first.  I want to be plain about that, because I spent about a year thinking I had.

John Hughlings Jackson gave the Croonian Lectures in 1884 and called this dissolution, taking the word from Spencer, and he had the whole of it.  His nervous system is organized in levels.  The lowest are the most organized, the most automatic, the simplest.  The highest are the least organized, the most voluntary, the most complex.  Disease takes the highest first, and dissolution is the reverse of evolution.  That is his sentence, not mine.

And then he does the thing that makes him worth the trouble of going and getting, which is that he splits what you are looking at into two kinds of symptom and insists on the split.  The **negative** symptoms are what the damaged high level has stopped doing.  The **positive** symptoms are what the intact lower levels are now doing, released, with the control that used to sit above them gone.  The disease produces the first.  It does not produce the second.  The second is normal machinery running normally, without its governor.

Read what people do with him now and you will find the pyramid everywhere and the release doctrine almost nowhere, and the release doctrine is the part that was hard to see and the part that is worth having.  A person who cites the levels and drops the release has taken the picture and left the finding.  It is eleven pages.  Go and get it.

So the framework's low pole is Jackson's release, arrived at again from the other end, a hundred and thirty-odd years later, by somebody who did not know he was walking toward it.  I have said in this book that when you turn a tendency down you do not get less of that tendency, you get the layer underneath running the way it always ran.  That is dissolution.  It is the same claim.  I am not going to pretend to be sorry about it.  A claim you reach twice from two directions is worth more than a claim you reach once, and the second route matters here, because Jackson had levels in one nervous system and this book has an installation order across three inheritance lines.  His order was anatomical.  Ours is genealogical, and it is longer, and it is dated.

Which makes the prediction sharper than his, and it is a real prediction, and it can be wrong.  If the layers are installed in a fixed order across the lines, and if failure runs that order backwards, then the sequence in which a unit sheds function under load is fixed too, and it is the same sequence in every unit of that kind, and it does not depend on what the load is.  Cold, hunger, fear, noise, a bad month.  Different loads, same shedding order.  What the load determines is how far down the shedding gets.

Now I want to work an example all the way through, because I have never once been convinced of anything by a principle stated on its own.

Take a room.  Say the design heat loss is 40,000 Btu per hour at design conditions, and you put a unit in it that will deliver 60,000.  That is not generosity, it is the next size up, and it is what actually happens.

At design, the unit runs 40,000 divided by 60,000, which is two thirds of the time.  It is off the other third.  For most of the year the load is nowhere near design and the thing cycles on and off all day and the room is fine.

Now something happens to the envelope.  It always does.  Seals go, a door gets propped, somebody takes out a section of insulation to run a conduit and does not put it back.  Say the design load goes from 40,000 to 55,000.

The unit now runs 55 over 60, which is 91.7 percent of the time on a design day.  The room is still at setpoint.  Nobody has complained.  Nobody has any reason to complain, because the thing they can feel is correct, and it is correct because the equipment is spending nearly all of itself keeping it correct.

Take it to 60,000.  Now the unit runs continuously and holds, with nothing left.  The room is still right.  From inside the room, this state and the two-thirds state are indistinguishable.  The temperature is the same temperature.

Take it to 62,000 and the room comes off setpoint and drifts, and now everybody knows, and the complaint that arrives is that the heat is broken.

The heat is not broken.  It was not broken at 91.7 percent either.  It is the same equipment doing the same thing it has always done, correctly, and at no point in that story did anything fail.  What changed is a ratio, and the ratio is between what is being asked and what there is to give.

Here is the part I actually want.  The number people watch is the room temperature, and the room temperature tells you nothing until the moment it tells you everything.  The number that was moving the whole time is the duty cycle, and almost nobody logs the duty cycle, and if you did log it you would have had four years of warning.

One more thing on this and then I will let the room go.  The design condition those numbers hang on is a temperature the outside air drops below for about one percent of the hours in a year.  There are 8,760 hours in a year.  One percent of 8,760 is 87.6, so call it 88 hours.  Eighty-eight hours.  That is three and a half days, spread out, mostly at night, and the entire sizing of the equipment is pinned to it.  I have met a great many people who use that design condition every week of their working lives and I have met very few who could tell you the 88 hours was in there.  It is not a criticism.  It is that a number gets used long after the reason for it stops being handed along with it, and this is a book about what gets carried forward and what quietly stops being.

Take the duty cycle over to a person and you have the thing this section is for.

Two units, same architecture, same layers installed in the same order.  One is running at something like a third of capacity.  The other is running at ninety-two percent.  Both are holding.  From outside, and from any instrument I know of, they are the same unit.  They do the work, they answer when spoken to, the temperature in the room is correct.

Then the load goes up on both of them by the same amount, and one of them is fine and the other one comes off setpoint, and the difference gets called a difference between the two people.  It is not.  It is a difference in what was left over, and what was left over was never visible, because a unit spending everything it has looks exactly like a unit spending a third of what it has right up until the morning it cannot.

That is the visible tax again and I am not going to say it again after this.  The maintenance is invisible exactly when it is working.  So is the cost of it.  So is the person paying it.

And when the drift comes it does not look like a shortfall.  It looks like a change of character, because that is what a released lower layer is.  Jackson's positive symptoms.  The unit does not become a fainter version of what it was.  It becomes an earlier one, running correctly, at a layer that was fully competent in the world it was built for and is being asked to hold a room it was never sized for.

Which is why the thing gets described as a disorder in the unit.  The unit is what is standing there.  The load is not standing anywhere and has no name and nobody logged it.

I think the disorder is mostly in the mismatch and I have thought so for a long time and I am aware that this is a convenient thing for a theory of layers to conclude.  Keep it at arm's length.  The framework has already said that the same constellation is alloparenting in one weather and a catastrophe in another, and I do not want to have said that twice and called it evidence.

Here is what I have that is new, and it is the part I like, and I cannot support it.

The order is universal.  The thresholds are not.

If the shedding sequence is fixed by the installation order, then it is the same in everybody, and it carries no information about any particular person at all.  What is left over is the load at which each layer lets go.  One person sheds the top layer at a load another person carries with room to spare, and holds the layer below it through something that takes a third person all the way down two more.  That set of thresholds — one number per layer, in a fixed sequence, running from the newest to the oldest — is not a summary of how somebody tends to behave.  It is the specification of the unit.

And I think it is the personality.  Not the traits.  The tolerances.

I want to say what that would cost, because it is expensive.  It would mean the trait scores are readings taken at whatever load happened to be on the unit that day, which is why they move around when nobody can work out why they moved.  It would mean two people with the same score are two different machines.  It would mean the measurement you want cannot be taken at rest, ever, by anybody, because at rest every unit that is holding looks like every other unit that is holding, and the whole content of the thing is in where it comes apart.  You would have to load it.  Which nobody is going to do, and nobody should.

I am guessing.  I want that on the record in the plainest terms available.  I have a mechanism that would produce this, and a hundred and thirty years of clinical description that is consistent with it, and no measurement of any kind.  Nettle would say the low end is a strategy with its own payoff and he has a real argument.  I say the low end is the layer above having gone dormant.  Both accounts predict the same reading on the same afternoon.  I have not found the case that separates them.  I have been looking for six years.

Loose ends.  I am setting these down where they are rather than tidying them.

Recovery.  If it sheds from the top down it ought to come back from the bottom up, in the build order, forwards.  I do not know that it does.  The coming apart is dramatic and gets written up.  The coming back is slow and gets called improvement and nobody records the sequence.  Somebody already has that data and does not know it.

Institutions.  I think a symbolic-line unit sheds in the same order, and that the first thing to go is the most recently added thing, which is generally whatever was hardest to fund and easiest to defend dropping.  I cannot get from that to a claim.  An institution's layers were not installed in a forced order.  Somebody chose them, in a meeting.  A chosen order is not a genealogical one, so the prediction may hold and the derivation does not.

Whether the released layer is any good.  Jackson says it is: normal machinery, running normally, governor gone.  But a layer that has spent forty years underneath another one has been running as infrastructure, not as the top of a stack.  A slab poured to sit on grade is not a slab that spans.  It has been fine for forty years because nothing ever asked it to span.  This one bothers me.

The floor.  The bottom layer does not shed, because there is nothing under it.  I do not know what that boundary is like.  I notice I would rather not write about it, which is not a reason.

And a suspicion, which is not an idea.  Nobody has done this because it is nobody's.  The order is an evolutionary claim, the thresholds are a psychometric measurement, the load is an environmental variable.  There is no room with all three of those people in it.  Four organizations, thirty-seven years, and I never saw a problem get solved that did not belong to somebody in particular.

So here is what somebody would have to measure.  I am not going to be able to do this and I want it written down properly, so that whoever does it does not have to start where I started.

1.  The sequence.  One species, one load, somewhere you are allowed to apply it.  Not people.  You want a lineage whose installation order you can fix from the phylogeny first, written down and sealed before anybody watches a single animal, so that the prediction is made in front of the result instead of behind it.  Rodent coping-style work has most of the apparatus and has been running it for thirty years for other reasons.  If you cannot get an animal preparation, use fatigue.  It is a load, it is legal, and everybody applies it to themselves for free every week.  Watch the order the top of the repertoire drops out in.  Do not watch performance.  Performance is the room temperature.

2.  The load.  This is the hard one and it is where I have been stuck for two years, and I am going to set out the difficulty rather than a solution, because I do not have a solution.  A design day is a load you can put a number on because you can put a number on the outside air.  There is no outside air here.  What is loading a unit is partly what is happening to it and partly what it is holding against, and the second one is the thing the unit is spending itself on, and the whole argument above is that you cannot see what a unit is spending.  So the measurement I need in order to test the claim is the measurement the claim says is unavailable.  I have been round this several times.  The way out, if there is one, is to stop trying to measure the load at all and measure the unit against itself twice, at two times, and take the difference.  That is what a duty cycle is.  It is not a quantity, it is a ratio, and a ratio does not require you to know either number on its own.

That is not nothing.  It is also not enough, because two readings taken a year apart are two readings of a unit that has changed in the meantime, and I cannot yet tell a change in the load from a change in the thing carrying it.
