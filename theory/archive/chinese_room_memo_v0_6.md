# The Chinese Room: Collection, Selection, and Retention Across the Lines

*Tier 4. Pre-canon memo. Not a compliance baseline. v0.6, replaces v0.5.*

---

## Purpose

This memo develops a three-stage architecture for how a line's heritable units
are built, sorted, and kept. It arrives at that architecture through a thought
experiment that holds the four cybernetic functions fixed and asks what is left
free to vary across the lines.

The memo contains two things that promote differently. The three-stage
architecture, the contest structure at its center, the table they produce, and
the survey results that test them are candidates for Part I. The office
rendering is an expository device and is not canon material at any tier. The
division is stated again at the end.

---

## The Device

Four analysts sit in a sealed room. Each runs one of the four cybernetic
functions. Candidates enter through one wall. Reports leave through the other.

The premise is that the analysts do not change. A Regulator applies blocking to
whatever arrives and emits a redundancy number, and it does this identically
whether the room sits inside a cell, a brain, a conversation, or a compute
cluster. The function is line-invariant.

If the analysts are held fixed, then everything that differs across the lines
must be at the walls, and the room has two of them. Three questions follow, one
per stage, and they are the only three the device permits:

1. What builds a candidate able to enter the room at all, and what governs which
   ones can be built?
2. What happens to the candidates once they are inside?
3. What happens to a report once it leaves, and what governs which ones survive?

The first question is **collection**, and it is the input wall. The second is
**selection**, and it is the room. The third is **retention**, and it is the
output wall. The device forces both boundaries, because the walls are those
boundaries.

The stages are an input, a process, and an output, in that order. Nothing is
selected that was not built. Nothing is retained that did not win the room.

### Why the Premise Holds With Two Walls

Line-invariance survives only if the scoring criterion sits outside the room. It
does. The four biases are the same at every line. What varies is what is on the
far side of the output wall doing the receiving: an environment counting
descendants, an outcome delivering reward, a hearer understanding or failing to,
a machine running the program or crashing. The room stages the contest. The
walls decide what enters and what survives.

This is a strengthening of the premise rather than a qualification of it. A
criterion that lived inside the room would be a fifth analyst, and the framework
has four.

---

## Mapping of the Device

The borrowed element is the sealed room and nothing else. What transfers is the
pair of walls: two hard boundaries that separate what varies by line from what
does not, and that force the analyst to say which side of which wall a given
phenomenon sits on.

What does not transfer is the argument the room was built to carry. The original
device concerns understanding and semantics. This memo makes no claim about
whether the analysts understand anything, and the room carries no weight on
questions of sentience. The framework's sentience commitments live in the
flora-and-fauna account and are untouched by this device.

Two further disanalogies, stated so they are not smuggled in. The original room
holds one operator following an arbitrary rulebook. This room holds four
analysts whose procedures are not arbitrary but are the four functions the
framework already commits to. And the original room's operator is the whole
system. Here the room is a unit inside a line, and the line continues on both
sides of both walls.

Scope: the device is a reasoning aid for separating line-invariant machinery
from line-specific channels. It is not an argument about anything.

---

## The Four Functions and Their Biases

Each function carries a signature bias in the selection race, the rule it applies
to decide which cue to credit. The four are recency for the Effector, familiarity
for the Regulator, potency for the Modeler, and novelty for the Reviser. On the
neuronal line these are the Pavlovian associability heuristics: eligibility trace,
blocking, overshadowing, and latent inhibition. The bias is not separate from the
function. It is the function seen from the selection side.

Two of the four are often collapsed, and keeping them apart is load-bearing for
everything below. Recency is a clock measure. Novelty is a density measure, and
it has no time argument in it. The most improbable event in a record can be its
oldest, and no amount of elapsed time makes it less improbable.

The biases run at the selection stage and only there. The evidence for that scope
statement is in the survey results below, and it is the sharpest empirical result
this memo carries.

---

## The Four Quantities

Given one observation, the four analysts compute four different numbers.

| Function | Quantity | What it measures |
|---|---|---|
| Effector | elapsed time | how close to now |
| Regulator | redundancy | whether existing predictors already account for it |
| Modeler | magnitude | how large the effect |
| Reviser | improbability | how far into the tail |

No one of these is derivable from any other, and every pair comes apart under a
real case. A recurring seasonal peak is high magnitude and low improbability. An
instrument fault is high improbability and low magnitude. A twenty-year-old crash
is high on both and old. A well-instrumented quantity is high redundancy at any
timestamp.

The published record in machine learning shows the recency and novelty pair
separating under pressure. The exploration bonus in Upper Confidence Bound is a
function of how often an option has been sampled and contains no clock. When the
problem became non-stationary, the field did not tune that bonus. It published
discounted and sliding-window variants as separate algorithms, adding a clock to
a counter, and the regret bounds changed. Two quantities that were one thing
would not have required two algorithms.

Mutual underivability is the load-bearing property. It is what distinguishes four
accounts of one phenomenon from four names for one quantity, and it is the test
applied in the survey sections below.

*Epistemic status: the four quantities are established and routinely computed
under these names in statistics and machine learning. Their mutual
underivability is an inference from the cases above and is well supported. The
identification of each quantity with one cybernetic function is a framework
commitment.*

---

## The Contest

The room becomes informative when the four analysts are given the same input and
made to compete for a scarce resource. This is the selection stage, and it is the
whole of what happens inside.

Each analyst's report is denominated in one quantity. A reader who computes a
different quantity does not receive a weak signal from that report. He receives a
blank. A baseline forecast, read by someone computing improbability, says that
nothing here is improbable, which is the empty message in his units. A
decades-old anomaly, read by someone computing elapsed time, is old and therefore
zero.

The analysts read each other. Attendance follows legibility rather than
preference, and legibility is forced by the arithmetic. An analyst can translate,
converting a redundancy claim into an improbability claim so that it can be read
at all, but translation between quantities that do not convert is lossy by
construction.

Under a scarce resource with any mechanism that compounds success, the contest
converges. One report is read and three are not, and the system loses a function.
The four outcomes are the four capacities, each named by the function it lacks: a
system that stops reading its Reviser is a Conservator, one that stops reading its
Regulator is a Pursuer, one that stops reading its Modeler is a Reactor, and one
that stops reading its Effector is a Planner.

The capacities are therefore selection-stage properties of the unit, and they
remain regions of the unit's own Venn. Nothing outside the room produces them.
This is consistent with Part III, which owns the capacities as three-motivation
regions of the geometry.

The winning report is what leaves through the output wall.

*Epistemic status: the contest structure and the derivation of the four
capacities from illegibility are framework commitments and are mechanism rather
than illustration. Their consistency with the Part III derivation is a check
passed, not an independent argument.*

---

## Three Stages

### Collection

**Collection is the construction of a competitor.** It is not the intake of a
unit, and reading it as intake is the error that made this stage hard to describe.

Development builds a phenotype that can compete for carrying capacity. Perception
builds a percept a candidate behavior can be conditioned on. Ritualized
acquisition builds a token that can carry a role. The build turns source into an
executable. In every case the channel takes a stored recipe and produces
something able to enter a contest, and the criterion governs which of those can
be built at all.

This is why no line's collection channel takes in units. Development does not
collect genes. Perception does not collect nemes. The channel is upstream of the
unit's expression, not upstream of the unit's arrival.

| Line | Collection channel | What it builds |
|---|---|---|
| Genetic | development in morphospace | a phenotype |
| Neuronal | perception in umwelt | a percept |
| Symbolic | ritualized acquisition in a language | a token that can carry a role |
| Digital | the build in a type system | an executable |

A channel names a process and the space it runs in, because neither half
specifies the channel alone. Development is not morphospace and morphospace is
not a process. The space is the domain the criterion is defined over, not the
subset the criterion picks out, which is why it belongs here and not in the
criterion column. Grammaticality picks the well-formed strings out of a language;
it does not pick a language.

The digital channel has adjacent field-native vocabulary worth keeping in view.
Practitioners speak of a sandbox, and of development environments as against
production environments. Both name a space where a candidate is assembled and
exercised before it is allowed to compete for anything real.

#### Three Variables in the Space

Three things vary independently here, and blending them produces a question that
cannot be answered.

The **universal space** is fixed. Physical and geometric limits on form are
absolute. The space of possible languages does not change because a language
does.

The **occupied region** moves. Realized morphospace expands. A primate umwelt is
not a bilaterian one. A language accumulates lexicon and notation. Limits that
apply to particular lineages rather than to all organisms are historically
contingent and documented as breakable.

The **grain** belongs to the unit, not to the space. A learner who tracks less
detail may discover structure a finer-grained learner misses. That is a fact
about resolution and it does not bear on the extent of anything.

One scope condition on the genetic entry. Reading an unoccupied region of a drawn
morphospace as an unavailable region is unsound, because such spaces are
typically non-metric, their axes carry different units, and emptiness is
ambiguous between not producible and not sampled. The inference is sound only
where a generative model defines the conceivable set in advance. The space at
this line is the output of such a model, not a plotted diagram.

*Epistemic status: the umwelt is established and already canon. Morphospace in
its model-generated form is established in theoretical morphology, and its
axis-arbitrariness in drawn form is an established criticism. A language and a
type system as the two upper spaces are framework proposals.*

#### Accessibility Is Graded

The collection criterion is not a fitness score, and it is also not a binary
gate. Both readings are wrong and the second one was this memo's.

Work on genotype-to-phenotype maps measures accessibility as a continuous
quantity: how large a neutral network is, how reachable a phenotype is under
mutation, how readily a generative system produces a given form. Some forms are
produced readily, some rarely, some never. The evidence that this layer is real
and distinct is that functional RNA structures match neutral-network-size
expectations rather than selective-optimization expectations, which is to say
that producibility rather than fitness predicts which structures appear.

What separates the criterion from a fitness score is therefore not gradedness. It
is which layer the number describes. A rarely-produced form is rare at the point
of production. A disadvantageous form is common at production and removed
afterward. Those are different layers with different measurements, and the
distinction has been given a formal treatment: the fitness landscape over
phenotypes is separable from the fitness landscape along the developmentally
admissible path, with stasis occurring at path peaks that need not be landscape
peaks.

*Epistemic status: accessibility as a measured, graded layer is established in
the genotype-phenotype map literature. Its formal separation from fitness is
demonstrated. Whether the separation holds in practice across evolutionary
biology generally is actively contested, and one substantial camp argues the
distinction collapses because producibility is itself partly a product of past
selection. The framework takes the separable reading, which is a commitment
against a live opposition rather than a settled result.*

#### Where the Criterion Comes From

Each line's criterion is the boundary against that line's own pre-line
groundwork. Canon already holds that every line has pre-line groundwork, and that
a line's groundwork is the prior line's mature output. The collection criterion
states that boundary from the upper line's side.

| Line | Pre-line groundwork | What the criterion excludes |
|---|---|---|
| Genetic | pre-biotic thermodynamic ratchets | chemistry that cannot be assembled into a form |
| Neuronal | the genetic line's mature output | associations the genome did not prepare |
| Symbolic | pre-symbolic indexical and iconic signaling | strings with no grammar to be grammatical against |
| Digital | the symbolic line's mature output | notation that will not compile |

Preparedness is the entry that makes this more than a restatement. Preparedness is
the genetic line's constraint on what the neuronal line is permitted to collect,
which is the seam between two lines and not a fact about either one alone. The
other three read the same way once this one is read that way.

This also disposes of a case that would otherwise look like a gap. A craft
tradition passed by mimicry is transmitted iconically and indexically, and canon
already files pre-symbolic indexical and iconic reference as the symbolic line's
pre-line groundwork. Such a tradition is not a symbolic unit the criterion fails
to cover. It is below the line, and it enters only if it is recoded.

#### Where the Criterion Installs

A collection criterion installs at a line's Reviser cell and constrains the line
above it from below. A selection criterion installs at a line's Effector cell and
runs upward through that same line. The two have opposite addresses and opposite
directions of travel.

| Installs at | Criterion | Constrains |
|---|---|---|
| Autogen | accessibility | the genetic line |
| Eumetazoa | preparedness | the neuronal line |
| Primate | grammaticality | the symbolic line |
| Empire-Human | compilation | the digital line |

The criterion is what installs. The space it ranges over installs nowhere,
because a space is not a position in the geometry. This is why the collection
stage adds no column to the Venn even though it adds a stage to the architecture.

Two consequences follow and both are checks rather than costs. The genetic
criterion installs below the genetic line, at the teleodynamic, which canon
carries forward into the founding cell's Reviser slot as Self-Production. And the
digital line's Reviser cell installs a criterion for a line that does not exist,
which is the four-line cap surfacing from a direction it had not surfaced from
before.

#### Operating a Collection Channel

A collection channel can be operated, and the symbolic line supplies the worked
mechanism.

The symbolic channel is ritualized language learning. Its ancestral high-cost form is
ritual proper, and its streamlined modern form is the exaggerated, redundant,
gesture-heavy speech register adults use with infants. These are one channel at
two costs rather than two channels.

The mechanism is saturation. A brain that computes indexical correlations well
gets caught on individual sign-to-object associations. Ritual defeats that with
extreme repetition, which drives those associations to redundancy ceiling until
each one carries no information. What survives the flattening is the system of
relationships among the tokens, which is the only thing left with a nonzero
number on it.

In this memo's terms, that is saturating the Regulator so that the Modeler's
object becomes the only legible thing in the room. It is a procedure for changing
what is admissible without changing any analyst.

Ritual also supplies indexical ballast for abstractions that cannot be pointed
at. A marriage or a peace has no referent available to the senses, and the
ceremony grounds it in tokens that do.

*Epistemic status: the account of ritual as a forced symbol-discovery procedure
is established as its author's position. Reading it as Regulator saturation is a
framework interpretation. The symbolic line is the only line with a worked
mechanism at this stage.*

### Selection

Selection is what the four biases do. It is the contest among candidates that
were built, run over a scarce resource, scored by a criterion.

Three things must be named at this stage and they are distinct. The **channel**
is the scarce resource that forces the contest. The **criterion** is what scores
the winner. Who does the selecting is derivable from the channel and is not a
separate column: the global workspace means the producing agent selects its own
output, a conversational floor means a different agent selects it, and a carrying
capacity means no agent selects at all.

Selection is the stage the framework is most trying to explain. Collection and
retention earn their places by being the two things selection is most often
confused with.

### Retention

Retention is whether a winner is written down.

Winning and being kept are different events, separated in time, and the gap
between them has its own criterion. Three lines make the gap unmistakable.

At the genetic line a phenotype can win selection outright and contribute nothing
heritable, because somatic change does not enter the germline. The retention
criterion is heritability, and the gap between selection and retention is the
reason acquired characteristics are not inherited.

At the neuronal line a behavior can win the workspace, be rewarded, and still
fail to be retained, because consolidation is separately gated. The three-part
sequence is already canon: attention runs the contest, reward scores it, and
consolidation writes the winner down. The separation is a separation in time, and
at this line it is measured in hours. Consolidation runs offline, during sleep,
after the day's contests have closed.

At the digital line a defect report can be correct, survive every analysis that
produced it, and be recorded as a false positive because the engineer reading it
did not understand it. The report won and was not kept, and nothing about its
correctness was at issue in the refusal.

The retention channel is the pool a winner is written into, and canon's
four-level stack already names all four: the gene pool, the agent's learned
repertoire, a culture, a repository. The channel is the pool and not the trace
that inscribes a single unit. At the neuronal line the repertoire is the channel
and the engram is the trace, the same distinction that separates the gene pool
from a chromosome. Naming the channel after the trace is the error canon warns
about, reaching one row down and naming a thing after what it is written on.

#### The Symbolic Retention Criterion

The symbolic retention criterion is re-transmission. What survives is what is
passed on again, and the field's finding is that traditions persist not by being
better retained or more accurately transferred but by being transmitted over and
over.

Memorability is the wrong criterion at this cell and it fails in an instructive
way. It is a selection-stage property asked to do retention-stage work. The
evidence that the two come apart is direct. Threat-related content wins in recall
chains and does not win when people merely choose whether to share. Content that
violates one ontological expectation is well remembered and rated highly
unbelievable. Falsehood was found seventy percent more likely to be retweeted
than truth, with onward transmission tracking novelty and emotional response
rather than accuracy. The problem of never being re-transmitted even once is
named separately in that literature from the problem of degrading across a long
chain.

Retention at this line is community-relative rather than item-intrinsic. The same
item persists differently in different communities, and transmission chains
converge on the receiving population's prior regardless of what was put in.

#### Institutional Retention

The upper two lines share a property the lower two do not. Where a formal
institution does the retaining, the account changes: retention runs on
externalized storage and routinized frequency rather than on any property of the
item or of individual memory.

This is visible from both directions. At the digital line the evidence standard
that licenses a write varies by domain and is defended on cost, skills, tooling,
and regulation as much as on evidence. At the symbolic line the field treats
institutional retention as a distinct regime and states plainly that no single
account unifies canon, legal precedent, citation, curricula, archives, and
recordkeeping.

The framework reads this as a fact about the two upper lines rather than as a gap
in two table cells. It is also a place where the three-stage architecture would
supply something the surveyed literature says it does not have.

*Epistemic status: the dissociation between winning an exchange and being passed
on is established and measured. Re-transmission as the symbolic retention
criterion is a framework proposal that follows from those measurements.
Institutional retention as a shared property of the upper two lines is an
inference from two surveys.*

### Personnel at the Walls

The rendering staffs both walls, and the staffing carries a structural claim.

At the input wall is an IT department. It builds what can be built and refuses
what cannot, and it makes no judgment about quality. A compiler is the purest
instance: it will not tell you whether your program is any good, and it will
absolutely refuse to build it if the types do not check.

At the output wall is an executive layer. It ratifies what the room decided. It
does not run the contest and it does not rescore the reports. It decides whether
the winner is written into the pool.

The two departments have opposite line profiles, and this is the sharpest thing
the staffed rendering can show that the table cannot.

The executives grow more agentive going up the lines. At the genetic line the
gene pool has no board, and heritability is a physical fact about germlines. At
the neuronal line consolidation has no board either, and it runs while the unit
is asleep. At the symbolic and digital lines there are real bodies with real
deliberation, and they get it wrong for reasons that have nothing to do with the
merits of what they are refusing.

The IT department runs the other way. At the digital line it is a named
department with a build system. At the symbolic line grammaticality lives in the
medium rather than in any agent. At the genetic line there is nobody there at
all.

What transfers from the executives is the separateness of the ratification event
and not deliberation. Three of the four lines have no decision to make and still
have the event. Putting the deliberative and non-deliberative cases in one slot
is what makes it visible that they are the same event.

Neither department appears in the table. Who collects is derivable from the
collection criterion and who retains from the retention criterion, on the same
principle that already makes the selector derivable from the selection channel.
They are personnel in the rendering, not columns in the architecture.

### What the Device Forces

The room's walls force both seams.

The input wall forces the collection seam. Inside versus outside is collection
versus everything after, and the device establishes that seam cleanly.

The output wall forces the selection-and-retention seam. The design constraint
for a device at this seam was that it must make visible a proposal that carries
the vote and is then never ratified. The output wall is that device: the winning
report leaves the room and then meets a separate body that may or may not write
it down, and the two events are separated in time. The digital and symbolic
survey results supply the instances.

---

## What the Three-Stage Split Resolves

**Three homeless phenomena get a place.** Grammaticality, preparedness, and
accessibility are real, consequential, and are not fitness differences. Without a
collection stage there is nowhere in the framework to put them, and the pressure
is to misfile them as selection criteria, which makes both worse.

The cost of that misfiling is documented outside the framework. In developmental
biology the number of vertebrae in the mammalian neck was for decades a textbook
case of a form development cannot build, until a pleiotropy mechanism reclassified
it as a form that is built and then removed. The correction was to move it from
one stage to the other, and the field states the correction in those terms.

**One vocabulary collision resolves without deletion.** Canon applies the word
selector at more than one point of the loop, and the resulting statements read as
contradictory when they are describing different stages. The three-stage split
gives each statement a home. No document needs a claim struck.

**The biases get a scope statement with evidence behind it.** They run at
selection. The six survey results below discriminate this rather than assert it.

**An asymmetry becomes statable.** What is never built never enters the
population and is therefore invisible to selection. Selection can only score what
got in. This is why the collection criterion cannot be recovered by studying
selection outcomes, and the surveyed literature reaches the same verdict on its
own methodological grounds: an unoccupied region is ambiguous between not
producible and not sampled, and the ambiguity is not resolvable from the
distribution of outcomes.

---

## The Table

| Line | Collection channel | Collection criterion | Selection channel | Selection criterion | Retention channel | Retention criterion |
|---|---|---|---|---|---|---|
| Genetic | development in morphospace | accessibility | carrying capacity | differential reproduction | the gene pool | heritability |
| Neuronal | perception in umwelt | preparedness | the global workspace | reward | the repertoire | consolidation |
| Symbolic | ritualized language learning | grammaticality | the conversational floor | comprehension | tradition and the corpus | re-transmission |
| Digital | the build in a type system | compilation | compute | correct execution | the repo | the commit |

Three notes on cells that would otherwise invite a wrong reading.

The digital selection criterion is correct execution. The digital line's
founding-cell breakthrough is Execution, and a program that runs is retained and
copied while code that never runs is pruned. Correct execution scores Fidelity,
the digital line's Effector motivation, the way differential reproduction scores
Persistence. Fidelity itself is not the criterion. Each line's first motivation
names what is selected for, not what does the scoring, and no other line's
criterion appears anywhere in its own motivation library.

The symbolic collection channel is ritualized acquisition, and joint attention is
not a candidate for it. Canon carries joint attention as the extension of the
neuronal selector across the line boundary, which places it on the selection
side. Filing it as a collection channel would commit the vocabulary collision
this memo exists to resolve.

The retention channel column is canon's pool row and adds nothing to it.

---

## The Hypothesis Under Test

The framework predicts that a mature field studying one line's selection
criterion in real time should sort into four camps rather than converge, because
the criterion is the one point at which all four functions must be reconciled
into a single verdict, and each camp is a faithful account of one of them.

This predicts non-convergence, and non-convergence has two possible causes that
must be told apart.

**Complementary accounts** measure four different quantities, none derivable from
the others. This is the outcome the framework predicts.

**Notational variants** measure one quantity in different coordinates, with a
transformation between them. A dispute can persist for decades after formal
equivalence has been demonstrated, so persistence alone is not evidence of a real
partition. This outcome counts against the mapping rather than for it.

Mutual underivability separates the two. Any survey of a candidate literature
must ask whether any two accounts are formally equivalent or intertranslatable,
and a pair that is equivalent counts as one function rather than two.

A field reporting that its accounts do not share a definition of the phenomenon
is reporting mutual illegibility, which is the prediction rather than a
disqualification. Reports denominated in different quantities do not read as weak
signals to each other. They read as blanks, and a field in that condition
describes itself as answering different questions.

### The Discriminating Result

The prediction is specific to the selection stage. Six literatures have now been
surveyed under a procedure that named no expected count, named no theories, named
no researchers, and asked each field to report its own structure. Three sit at a
line's selection criterion. Three sit off it.

| Survey | Line | Stage | How the accounts sort |
|---|---|---|---|
| Syntactic ambiguity | symbolic | selection criterion | by bias, four camps |
| Reward signaling | neuronal | selection criterion | by bias, four camps |
| Software correctness | digital | selection criterion | by bias, four camps |
| Cell fate determination | genetic | collection | by level |
| Limits on realized form | genetic | collection | by level |
| Cultural transmission | symbolic | retention | by locus |

The three selection surveys partition by the quantity each account credits. The
three off-stage surveys partition by something else entirely: what supplies an
instruction as against what registers it, ontogeny as against lineage history as
against physics, and whether the determining property lives in the item, the
transmitter, the receiver, the relationship, the population, or the institution.

This is discriminating and it is the strongest evidence in the memo. If the
four-function mapping were something an analyst could impose on any mature
literature, the off-stage surveys would have yielded to it as readily. Two of
them were commissioned to validate criteria rather than to test the partition,
and neither returned one.

The scope statement follows. The biases run where there is a contest. Collection
has no contest, because a form that is never built is not outcompeted. Retention
has a ratification rather than a contest. Selection is the only stage where four
analysts compete over one verdict, and it is the only stage whose literatures
partition four ways.

*Epistemic status: three positive cases and three negative cases, all from
surveys run under the anti-hypothesis procedure. The negative cases are the
load-bearing ones, because they were not sought as negative results. The
inference from six literatures to a general claim about stages is a framework
commitment and would be strengthened by a retention survey at a lower line, where
no institutional layer is present.*

---

## Worked Test Case: Comprehension at the Symbolic Line

Four accounts of syntactic ambiguity resolution are currently live and the field
does not expect one to win.

**Filing.** Symbolic line, selection stage, selection criterion. One comprehender
processing one sentence in real time.

| Account | Claim | Function | Fit |
|---|---|---|---|
| Surprisal | processing cost is the negative log probability of the word given context | Reviser | identity |
| Good-enough and noisy-channel | the parse is often not completed, and an initial misreading is never corrected | Regulator | strong |
| Self-organizing and dynamical | no discrete candidates; a landscape settles, and locally coherent fragments create traps | Modeler | good |
| Unrestricted race | competing structures are built in parallel and the fastest to complete is adopted | Effector | moderate |

The Surprisal link is not an analogy. Surprisal is negative log probability. The
Reviser's quantity is improbability. These are the same number, arrived at
independently in two fields.

The Good-enough link turns on what the account omits rather than what it asserts.
It is the theory in which surprise fails to drive revision, and its signature
evidence is that readers misremember a garden-path sentence long afterward, never
having corrected the initial commitment. A loop that runs without meta-update is
the Regulator holding its reference against a challenger.

The Race link is the weak one and is marked as such. The Effector reading is
sound, since the race commits immediately to whatever completed first and pays
later. The recency bias specifically is carried by the analogy rather than by the
mechanism, since the race is decided by construction speed and not by how recent
anything is. The field itself names this gap.

**The Modeler and Reviser accounts are reported to overlap empirically.** This is
predicted rather than anomalous. Modeler and Reviser are adjacent on the ring and
meet at the Adapter, so two accounts built on potency and novelty should share
territory. A clean separation would have been the surprising result.

**Scale statement.** All four accounts describe one comprehender processing one
sentence. The table describes a line's inheritance across deep time. The functions
are scale-general, so mapping accounts-of-comprehension onto functions is
legitimate. Mapping them onto the line's selection stage would not be. The two
claims must not merge, and this qualification applies to every case below.

*Epistemic status: the four accounts and their current standing are the field's
own characterization. The Surprisal identification is established by inspection of
the two definitions. The remaining three mappings are framework interpretations at
the confidence levels marked.*

---

## Worked Test Case: Reward at the Neuronal Line

A survey of the debate over the midbrain dopamine signal returns five live
accounts, with the field reporting no convergence and increasingly describing
them as complementary descriptions of a heterogeneous system.

**Filing.** Neuronal line, selection stage, selection criterion. One animal
learning, over seconds to sessions.

| Account | Claim | Function | Fit |
|---|---|---|---|
| Reward prediction error and temporal difference | the signal is the discrepancy between received and predicted reward | Regulator | identity |
| Causal contingency and model-based | the signal carries stimulus-to-stimulus structure independent of value | Modeler | good |
| Salience, novelty, and uncertainty | the signal tracks unsigned importance, novelty, and reward uncertainty | Reviser | strong |
| Incentive salience, effort, and vigor | the signal drives approach and sets the rate of ongoing behavior | Effector | strong |

The Regulator link is the strongest single mapping in this memo. Prediction error
asks whether existing predictors already account for the outcome, which is the
Regulator's quantity by definition, and the account was established by running the
Regulator's own signature experiment on the mechanism. Dopamine was shown to obey
blocking, and optogenetic activation at the time of an otherwise blocked reward
unblocked learning about a redundant cue.

One guard. Prediction error is not surprisal. Prediction error is a signed
residual in reward units and surprisal is a negative log probability in bits. A
rare event delivering exactly what the model predicted conditional on occurrence
is high surprisal and zero prediction error. The two come apart, which is what
mutual underivability requires and what keeps the Regulator and Reviser mappings
from collapsing into one.

The Effector link repairs the weak leg of the symbolic case. Vigor is denominated
in reward rate and in the opportunity cost of time, and dopamine transients have
been reported to follow a striatal gradient of reward time horizons running from
fractions of a second to hundreds of seconds. That is a clock rather than an
analogy.

**Five accounts onto four functions, with the Effector doubled.** Incentive
salience and vigor are separated by timescale and by pathway, and both sit at the
action channel. This is the cost of the mapping and it is stated rather than
smoothed. The field's own hardest dichotomy, learning against motivation, falls on
this boundary: three evaluative accounts on one side and the action account alone
on the other. The Effector is the only function whose output is a body doing
something, so it is the only one that should surface as a performance account
rather than a learning account.

**The named collapse condition.** A reconciling proposal holds that the signal is
a feature-specific vector prediction error rather than a single scalar, which
would make every channel a prediction error in different coordinates. That is the
notational-variant outcome and would count against the mapping. The field names
the experiment: cell-type and projection-resolved recording together with
manipulation. It has not been run.

**A negative result worth recording.** A comprehensive survey of the neuronal
line's central evaluative signal returned no account of what is built for scoring
in the first place. All five accounts are about scoring. That is consistent with
collection and selection being separate stages studied by separate literatures.

*Epistemic status: the five accounts and their standing are the field's own
characterization. The prediction-error identification is established by
inspection. The remaining mappings are framework interpretations. The Effector
doubling is a stated cost and is not resolved.*

---

## Worked Test Case: Correct Execution at the Digital Line

A survey of how correctness is established for software returns seven claim
types, no field-wide convergence, and an explicit finding that the approaches do
not share a definition of correctness.

**Filing.** Digital line, selection stage, selection criterion. One project over
years, and one field over five decades.

Four of the seven are accounts of the selection criterion, and they land on the
four cells of the digital line.

| Approach | Claim | Cell | Function | Fit |
|---|---|---|---|---|
| Operational-profile and statistical testing | behavior is acceptable on inputs sampled by their frequency in expected use | Computer | Effector | strong |
| Static analysis | the code is free of known defect patterns on all paths | Network | Regulator | strong |
| Proof, model checking, design verification | an abstraction of the system provably satisfies its specification | Model | Modeler | strong |
| Fuzzing, property-based, and metamorphic testing | behavior holds under inputs no one specified and no oracle covers | Agent | Reviser | strong |

Three of these are close to definitional against the digital line's own labels.
Model checking verifies a finite-state abstraction and its documented blind spot
is the gap between model and code, which is the Abstraction motivation and its
failure mode in one sentence. Metamorphic testing infers from relations where no
ground truth is available, which is what the Abduction breakthrough names. The
static-analysis literature's central finding is a Consensus problem in the Network
cell's own vocabulary: a true report that nobody understands is recorded as a
false positive, and analyses producing hard-to-read output were abandoned rather
than fixed.

**The split within testing is principled and is defended on the survey's own
terms.** The survey groups by claim everywhere except here, where it groups by
mechanism. Operational-profile testing samples inputs by their frequency in
expected use. Fuzzing deliberately samples where the distribution does not go.
These are opposite sampling strategies over one input space and they are
separately named in the field. Applying the survey's stated principle consistently
splits them.

**Two of the seven are not selection accounts, and they fill the other two
stages.** Types and compilation are the collection gate: a program that fails to
type-check is not outcompeted, it is never built, and the survey reports that
developers treat compilation as certification. Human review and runtime monitoring
are retention: they decide whether a finding is written down and whether a
deployed system keeps running.

**This case supplies the retention device.** The survey reports that a true
defect report which is not understood is commonly labeled a false positive, that
the first few reports dominate whether a tool is trusted at all, and that a tool
upgrade surfacing more real errors was received as a problem rather than a result.
Those are proposals that carry the vote inside the room and are refused outside
it, for reasons unrelated to their correctness. The reverse case brackets the seam
from the other side: code that met its specification, passed every gate, was
committed and shipped, and failed because the environmental assumption was wrong.

**A note on the wall itself.** The oldest dispute in this literature is whether a
proof can establish anything about a running program, on the ground that
algorithms are abstract objects and programs are causal models running on physical
machines. That is an argument about what the analysts can reach, and it has run
without resolution since 1988. It is the closest thing in any surveyed literature
to the device's own premise, and it is recorded here as a resemblance rather than
as support.

**The named collapse condition.** The survey reports that the persistence of the
disagreement is mostly non-evidential, driven by cost, skills, tooling, and
regulation. If verification becomes cheap enough and the partition dissolves, the
four camps were an artifact of economics rather than of function. That is the test
and the field names it.

*Epistemic status: the seven approaches and their standing are the field's own
characterization. The four-way mapping onto the digital cells is a framework
interpretation. The testing split is an inference from the survey's stated
grouping principle and is well supported. The retention material is reported
finding rather than interpretation.*

---

## Criterion Survey: Cell Fate at the Genetic Line

A survey of how cell fate is determined returns six live accounts and reports
that they largely do not compete over one question.

**Filing.** Genetic line, collection stage. One cell in one embryo, over hours to
days. Somatic and within-lifetime, and not the genetic line's selector.

The six accounts sort by what supplies an instruction, what registers it, and what
constrains the outcome, which is a sorting by level rather than by bias. The
survey's own verdict is that most apparent controversy is a category difference
and that three distinct senses of determination are in use: autonomy under
transplantation, stability within a basin of attraction, and instructive
causation. The survey's first recommendation is to specify which sense is meant
before comparing claims, which is what this device exists to force.

**One of the six is the room rather than a camp.** The gene-regulatory-network and
attractor-landscape account is described by the survey as orthogonal to the
others, the machinery that integrates and stabilizes whatever the other accounts
supply. That is the room, and the other accounts are what arrives at its walls.
Separately, the network account and the landscape account are formally the same
object, which is why they occupy one slot.

**A four-function reading of the remaining accounts is available and it is not a
claim about this stage.** Mechanical inputs credit the cell's instantaneous forces
and contacts. Inductive and positional signaling credits what neighbors and
gradients already establish. Cytoplasmic determinants credit the interior contents
inherited at division and override position. Stochastic fluctuation amplified by
reaction and diffusion credits the rare event. Those readings are consistent, but
development is itself a unit that runs four functions, and the functions are
scale-general. The mapping is evidence that development is a cybernetic system. It
is not evidence that the collection stage runs a contest, and this memo does not
use it as such.

**What this case does establish.** The field's staging is competence, then
specification, then determination, then differentiation, with the first reversible
and the third not. A literature that never saw this memo produced a three-stage
architecture with the same seams in the same order, and named its first stage for
a condition on the receiver rather than for a score.

**One thing the survey leaves genuinely unsettled and the framework does not need
resolved.** Whether mechanical input is instructive or permissive in living
tissue is contested, and the two readings place it at different stages. The
framework's position is that the distinction is the right one to be arguing about
and that the field lacks an instrument for stating it, which is the diagnosis this
memo offers rather than a claim about which answer is correct.

*Epistemic status: the six accounts, the staging vocabulary, and the
network-landscape equivalence are the field's own characterization. The
four-function reading is a framework interpretation about development as a unit,
scoped away from any claim about the collection stage.*

---

## Criterion Survey: Limits on Realized Form at the Genetic Line

A survey of what limits realized biological form relative to conceivable form
returns six accounts, no agreed count, no agreed term, and no shared definition.

**Filing.** Genetic line, collection stage. Lineages over evolutionary time.

The accounts sort by level: individual development, lineage history, and physics
independent of any organism. Two of the six are not about the collection stage at
all. Functional and selective limits describe forms that are built and then
removed, which is the selection stage. Physical and geometric limits describe the
universal space rather than any lineage's position in it.

**No established term exists for the set of forms a lineage cannot produce.** At
least a dozen partly overlapping usages are in circulation, and the field
acknowledges the confusion explicitly, to the point of a published satirical
coinage whose stated purpose was to observe that the vocabulary had become comic.
The framework therefore takes accessibility, which is the term used by the camp
that has formalized the distinction rather than the term used most often.

**The distinction between unavailable and disadvantageous is the field's central
fault line, and the contest over it is the finding.** It is stated explicitly in
the canonical treatments, used tacitly in nearly all empirical work, declared
hopelessly muddled in one influential critique, declared a false dichotomy by a
substantial current camp on the ground that producibility is itself partly a
product of past selection, and re-formalized as genuinely separable by
genotype-phenotype map theorists. The framework takes the separable reading, which
is a commitment against live opposition.

**The framework's asymmetry claim is the field's own methodological verdict.**
Inferring a limit from the distribution of realized forms alone is judged unsound
in general and sound only where a generative model defines the conceivable set in
advance. The named reasons are axis-arbitrariness in drawn morphospaces,
phylogenetic non-independence, sampling and preservation bias, and the ambiguity
between not producible and not sampled. That is the memo's claim that the
collection criterion cannot be recovered by studying selection outcomes, reached
independently and for the field's own reasons.

**Limits that apply to particular lineages are documented as breakable and limits
that apply to all organisms are treated as absolute.** That is the universal and
occupied distinction, in the field's vocabulary, with worked cases on both sides.

*Epistemic status: the terminological finding and the methodological verdict are
established and are the field's own. The status of the availability distinction is
established as contested. The framework's adoption of the separable reading is a
commitment, and the strongest support for it is a formal separation of the fitness
landscape over phenotypes from the fitness landscape along the developmentally
admissible path.*

---

## Criterion Survey: Cultural Transmission at the Symbolic Line

A survey of what determines whether a cultural item survives repeated
transmission returns at least a dozen accounts under three incompatible top-level
taxonomies, with no agreed count.

**Filing.** Symbolic line, retention stage. One item across many transmission
events.

The accounts sort by where the determining property lives: in the item, in the
transmitter, in the receiver, in the relationship, in the population structure, or
in the institution. That is a sorting by locus rather than by bias, and the survey
reports the locus dispute as genuine and unresolved.

**The selection and retention seam is measured rather than argued here.** The
field decomposes transmission into choosing to receive, encoding and retrieving,
and choosing to transmit, and the phases dissociate. Threat-related content wins
in recall chains and loses when people merely choose whether to share. Content
that violates one ontological expectation is well remembered and rated highly
unbelievable. Falsehood was found substantially more likely to be passed on than
truth, with onward transmission tracking novelty and emotional response rather
than accuracy. The problem of never being re-transmitted even once is named
separately from the problem of degrading across a long chain.

**Retention at this line is community-relative.** The founding cross-cultural
claim for item-intrinsic transmission advantage narrowed under replication, with
one content bias found in one national sample and absent in another. Transmission
chains converge on the receiving population's prior regardless of what was put in,
a result with a proven formal equivalence to a standard sampling algorithm.

**Institutional retention is a distinct regime and the field says so.** Where an
institution retains, the invoked mechanism is externalized storage and routinized
frequency rather than any property of the item or of individual memory. The survey
states that no single account unifies canon, legal precedent, citation, curricula,
archives, and recordkeeping, and names this a gap.

*Epistemic status: the phase dissociations and the cross-cultural narrowing are
established and measured. The convergence-to-prior equivalence is proven.
Re-transmission as the retention criterion is a framework proposal following from
those measurements. The reading of institutional retention as a shared property of
the upper two lines rests on two surveys.*

---

## Method for Further Surveys

Two kinds of survey are commissioned and they answer to different requirements.

**A test case** asks whether a literature partitions by function. It requires a
repeatable event that can be measured rather than a historical transition
reconstructed from traces, multiple accounts currently live with the field not
expecting convergence, and accounts competing over one event. A field reporting
that its accounts define the phenomenon differently satisfies the third
requirement rather than failing it, so long as the accounts are about one event.

**A criterion survey** asks whether a framework term matches field vocabulary and
whether a claimed distinction is real. It does not require a repeatable event and
does not require four camps. A criterion survey that returns a partition is filed
as a test case as well.

**The procedure is the same for both and it is not optional.** The survey is
commissioned before any mapping is attempted. The brief must not state how many
accounts are expected, must not name theories or researchers, and must ask the
field to report its own count. The brief must ask whether any two accounts are
formally equivalent. The brief must ask whether the accounts define the phenomenon
the same way. The mapping is attempted only after the survey returns, and against
what the survey reports.

**Filing.** Record each survey's line, stage, and level of organization. A survey
at a different stage or level is filed separately rather than pooled. Record
surveys that return no partition alongside those that do, because the negative
cases are what make the positive ones discriminating.

**The next candidate.** The foundations of statistical inference sit at the Model
cell of the digital line, where no case currently sits. The camps have not
converged in a century, the field does not expect them to, and the accounts are
formally comparable enough that intertranslatability can be tested rather than
argued. A retention survey at the genetic or neuronal line would be the strongest
complement to it, because both would test the stage result where no institutional
layer is present.

---

## Promotion Path

**Promotable.** The three-stage architecture. The two-wall device and its
input-process-output logic. Collection as the construction of a competitor. The
collection channel as a process and the space it runs in. Accessibility as a
graded layer separable from fitness. The criterion as the boundary against a
line's pre-line groundwork, installing at the Reviser cell and constraining from
below. The three variables in the space. The contest structure and the derivation
of the four capacities from illegibility. The derivability of the selector from
the selection channel, and of the collector and the retainer from their criteria.
The table. The six surveys, their filing, and the stage result they discriminate.

**Not promotable at any tier.** The office rendering, including the IT
department, the executives, and the naps. It is an expository device and its
natural home is book material. The structural claim it carries, that agency at the
two walls varies inversely across the lines, is separable from the rendering and
travels with the architecture.

**Retire this memo** when the architecture lands in Part I and the rendering is
routed to the book. Nothing here is intended to survive as a standing document.

---

*Epistemic status of the memo as a whole: the four functions and their biases are
established canon. The three-stage architecture is a framework proposal
originating here, now supported by six surveyed literatures, three at the
selection stage and three off it. The stage result, that literatures partition by
function only at selection, is the memo's strongest claim and rests on three
positive and three negative cases. All six sit at scales far below the one the
table describes, which limits what they confirm. Two document edits follow from
this memo: the digital selection criterion, and the vocabulary collision on the
word selector.*
