# Night One

---

## Personality as Biographical Signature

What makes trait talk apply to bacteria and not to thermostats?

I want to spend the whole first night on that.  It looks like a small question and it is not.  Everything in this course sits on the answer, and if the answer is wrong then the rest of it is decoration.

Start with the thermostat.  I spent eleven years designing systems that hung off them and I can tell you what is inside one.

Take the round dial off the wall of a house built before about 1980 and open it up.  There is a coil in there made of two metals bonded together along their whole length.  The two metals grow at different rates when they warm up.  Bonded, they cannot grow independently, so the coil winds and unwinds as the room changes.  Fixed to the free end of the coil is a small glass bulb with a bead of mercury in it and two contacts sealed into one end.  When the coil turns far enough the bulb tips, the mercury runs downhill and bridges the contacts, and the circuit closes.  The burner lights.  That is the whole instrument.  There is nothing else in there.

Now name the parts.

1. The coil is the **sensor**.  It reports the room.
2. The tipping point of the bulb is the **comparator**.  It is comparing the room against something.
3. The something is the dial you set, and that is the **goal**.
4. The circuit to the burner is the **effector**.  It changes the room.

Sensor, comparator, effector, goal.  Four functions, one loop, and the loop closes because the burner changes the room that the coil is reading.  It is worth seeing them once in a thing you can hold in your hand, because from here on they will mostly be in things you cannot.

Before you decide a thermostat is too stupid to be worth the argument, look at the other thing in there.  On a great many of them there is a small wire resistor mounted next to the coil, with a lever beside it and an amperage scale printed on the plate.  That is the heat anticipator, and it works by lying to the instrument.  The resistor sits in the same circuit as the burner.  So while the burner is running, the resistor is warming the coil directly, from six inches away, a little.  The coil therefore reads the room as warmer than the room actually is, and it shuts the burner off early.

Why would anybody want that?  Because the radiator is still hot when the burner stops.  There is stored heat in the iron and the water, and that heat is going into the room whether you want it or not, and if you wait for the room to actually reach seventy before you quit, you will end up at seventy-three.  Then you undershoot on the way back down.  The house swings.  The anticipator makes the thermostat quit early by exactly the amount the coasting heat is about to supply, and you set the lever to match the current draw of your particular burner, which is stamped on the burner.

So there is a small standing prediction in that instrument about what is going to happen after it stops acting.  A model of the near future, made of one resistor and set with a lever.  I am not going to make more of that than it deserves.  But if your objection to the thermostat is that it cannot anticipate anything, the objection is wrong, and it is wrong in the hardware, and it was wrong in 1953.

Now the bacterium.

Take *E. coli*, one species, swimming in a gradient of some attractant.  It has receptors in the membrane that bind the attractant and report occupancy inward.  That is the sensor.  It has flagella that turn one way to drive a straight run and the other way to fly apart and tumble the cell into a new heading at random.  That is the effector.  Between them is the comparison, and the comparison is the interesting part, because the cell is not comparing concentration against a setpoint.  It is comparing concentration now against concentration a few seconds ago.  It carries the few seconds ago in the methylation state of the receptors, which lags the binding.  When the cell is swimming up-gradient, now is better than before, and it suppresses tumbling and keeps going.  When it is swimming down-gradient it tumbles and tries a new direction.  The goal is the state it drifts back toward when nothing is changing.

If you have ever tuned a loop that hunts, you already know what the cell is doing.  It is running the error signal through an integrator with a time constant on it, and the time constant is what lets a system with no memory to speak of act on a trend instead of a level.  The cell has been doing it a good deal longer than we have.  Berg's tracking work is where I would send you for the actual numbers — Berg and Brown, *Nature*, 1972, and the small book, *E. coli in Motion*, Springer, 2004.

So: sensor, comparator, effector, goal.  The same four functions, in wildly different machinery, at wildly different cost.  By the parts list, the thermostat and the bacterium are the same kind of thing.

And they are not, and everyone knows they are not, and the place it shows is in the adjectives.

Bacteriologists describe strains with trait words and have for decades.  Cooperative and exploitative are the strongest of them and they are not loose talk at all — a strain of *Pseudomonas aeruginosa* that makes siderophores and shares the iron it scavenges is doing something a strain that consumes the siderophores and makes none is not doing, the difference is measurable in a flask, and the freeloaders win locally and lose when they get too common.  Griffin, West and Buckling ran that in *Nature* in 2004.  West and colleagues laid the theory out in *Nature Reviews Microbiology* in 2006.  Sociable is nearly as solid, because quorum sensing is a real mechanism you can knock out.  Bold and sluggish are looser, and I want to say so rather than let them ride on the back of the good ones.  But they are used, they are used consistently, and a working bacteriologist knows what you mean.

Nobody says a thermostat is bold.  Not as a joke, and not carelessly, and not in a trade journal.

That is the fact to be explained.  Both systems have the loop.  Only one of them takes the adjective.  So the loop is not what licenses the adjective, and if you are keeping a list of things that turn out not to be sufficient, put the loop at the top of it.

Here is what I think an adjective is doing.

A trait word is a distributional summary.  When you say a strain is bold, you are not describing an event.  You are making a claim about how that strain tends to behave across a range of situations, and *tends to* is a word about a distribution.  Say it the other way: you are giving somebody a compressed bet about what the strain will do in situations neither of you has watched yet.

Work it through with numbers.  I am going to make the numbers up so the division stays clean.  The real ones are in Berg and they are messier.

Put a strain in a gradient and count how many times a cell tumbles in ten minutes.  Say you get 38.  That is 3.8 tumbles a minute.  Do the same with a second strain and get 114, which is 11.4 a minute.  The second strain is changing its mind three times as often as the first.

Now.  What do you have?

You have two numbers.  You do not yet have an adjective.  If I hand you 3.8 tumbles a minute and nothing else, the honest report is *3.8 tumbles a minute*, and no adjective is available to you, because there is nothing for the number to be high or low with respect to.

Get the rest of the strains.  Say the species runs from about 3 to about 14 across everything anybody has catalogued.  Now 3.8 is near the bottom of that range, and the word for a cell that commits to a heading and stays with it is bold, and the word has earned something.  It has earned a position.  *Bold* now means *low in the tumbling distribution for this species*, and every bit of the meaning is coming from the other strains.

That is the load-bearing point of the night, so I will put it plainly.  A trait adjective is a position in a distribution.  No distribution, no position.  No position, no adjective — you are left holding a measurement.

Which raises the only question left, which is where the distribution comes from.

It comes from inheritance, and it takes four things to make it, and all four have to be there.

1. **Parameters get passed to successors.**  Variation persists past the individual instead of dying with it.
2. **Which successors there are depends on how the parameters worked out.**  This is what makes the spread structured instead of drifting into noise.
3. **Combinations that worked get kept whole.**  You see the same constellations of settings turn up again down the line, which is what makes a type a type.
4. **New variants keep arriving.**  Otherwise the spread narrows and eventually there is nothing left to be a position within.

Take away any one of them and the reference distribution goes.  Take away the reference distribution and the adjective goes with it.

Now go back to the thermostat and ask which of the four it has.

None of them.  There is no thermostat lineage.  No thermostat passes anything to another thermostat.  The spread across models on the shelf is real — they genuinely differ, in swing, in anticipator range, in how tightly they hold — but that spread is a record of purchasing decisions and tooling changes and what the die-caster could do that year.  Honeywell did not stop making a model because it failed to reproduce.  Somebody in a meeting decided.  The variation is a catalog, and a catalog is not a distribution in the sense we need, because nothing in it was selected by how well it ran.

So the loop is present and the biography is absent.  Trait adjectives describe systems that have histories.  A thermostat has a manufacturing date.

I want to sit on the word *biography* for a minute, because I think it is doing more work here than it looks like it is.

Every line that has this structure has evolved a genre for compressing it, and the genres all have the same shape.  People get obituaries.  Bacterial strains get strain reports.  Codebases get postmortems.  Civilizations get historiographies.  A piece of plant equipment gets a failure history, which is the same document with the adjectives taken out and the dates left in, and if you have ever had to read forty years of one you know it is a character sketch whether or not anybody meant it to be.  Different names.  Same form.  A short list of characterizing adjectives summarizing how the unit tended across the range of situations it happened to occupy.

Which makes a personality assessment a bet on the obituary.  You are guessing, in advance, which adjectives the eventual compression is going to land on.  That is all an assessment is and I think it is worth knowing that is what you are doing.

And things without biographies get the other genre instead.  Hurricanes get meteorological summaries.  Thermostats get spec sheets.  That is not a demotion.  It is the document that fits what they actually are, and the fact that we reach for it without thinking is the intuition this whole night has been trying to put a mechanism under.

That is also why I set the scope of this book where I did, and I would rather state the criterion than have you infer it.  Everything here applies to units that carry pattern forward into successors through some coupling with an environment.  It does not apply to thermostats, hurricanes, or rocks.  Not because they feel like the wrong kind of thing, which is a reason I do not trust, but because they transmit nothing to a successor, so there is no line for selection to write onto, so there is no distribution, so there is no position, so there is no adjective.

One consequence of that, and I want to be careful about how far I take it.

The criterion does not say biological.  It says inheritance-bearing.  So if you find an engineered thing that satisfies all four conditions, the argument licenses trait talk about it, and it licenses it by the same route it licensed bacteria and not by some softer extension.  Code is the case I have actually looked at.  Repositories fork.  Forks carry the parameters of the parent and then diverge.  Which forks are still there in five years depends on which ones worked, whole configurations get lifted from one project into another intact, and new variants arrive constantly and from everywhere.  All four conditions, in something nobody grew.  I do not think this is a metaphor and I have not been able to make it come out as one.

There will be other cases.  I have not checked them and I am not going to pretend I have.  The criterion is above; apply it yourself and see what happens.  If it turns out I have the criterion wrong, the place it will break first is condition 2, because that is the one that is easy to fake — it is easy to build something that looks like it is being selected when it is only being chosen.

So, the whole night in one line.

*Personality is the biographical signature of a cybernetic loop subject to inheritance.*

Two conditions.  A loop, and a line.  Where both hold, the adjectives apply and they are doing real work.  Where either one fails, you have a machine that works and nothing to describe.

---

## Vocabulary

Five words.  I am putting them here, ahead of the machinery they belong to, because you will hit all five before I get around to building any of it, and it is easier to carry a definition than to guess at one.

### What I Mean by Ratchet

Feynman worked through a machine that exists to show you why this word is a trap.  It is in the *Lectures*, volume one, chapter forty-six, 1963.  Smoluchowski had the objection first, in 1912, and Feynman says so.

Here is the machine.  A wheel with sawteeth cut into it.  A spring holds a pawl down into the teeth.  Turn the wheel one way and the pawl rides up over the sloped face of each tooth and drops into the next one.  Turn it the other way and the pawl catches on the vertical face and the wheel stops.  You have one of these in your socket wrench.

Now run an axle from that wheel out to a paddle sitting in a box of gas.  Molecules hit the paddle from both sides, at random, equally.  No net push in either direction.  But the pawl only lets the wheel go one way.  So the random kicks ought to accumulate into rotation, and you could tie a thread to the axle and lift a weight with it, and you would be lifting that weight out of a gas that is all one temperature.  Heat in, work out, nothing else.  If that worked, the heating bill for this building would be zero and I would have had a different career.

It does not work, and the reason it does not work is the entire content of the word.

The pawl is in the gas too.  It is getting kicked exactly as hard as the paddle is.  A pawl holds only as long as its spring keeps it seated, so every so often a molecule knocks the pawl up off a tooth at the same moment the wheel is being pushed backward, and the wheel slips back one tooth.  Work out the two rates at a single temperature and they come out equal.  Forward by ratchet, backward by slip, exactly canceling.  The wheel jitters and goes nowhere forever.

To get net motion out of it you have to hold the pawl colder than the paddle.  And holding any part of a system colder than what surrounds it is not free.  I spent a career on that bill.

So a ratchet has three parts and not two.

1. **Undirected variation.**  The kicks.  Both directions, no preference, no plan.
2. **A rectifier.**  The pawl.  Lets one direction through and blocks the other.
3. **A paid reset.**  Whatever it costs to keep the pawl in a condition to do its job.

When I use the word ratchet I mean all three.  Most uses mean the first two.  The third one is the one that gets dropped, and it is worth knowing why it gets dropped, because the reason is going to come back in this course more than once: it is a recurring cost with nothing to show for it.  It does not produce the motion.  It only makes the motion possible.  Those are different things and only one of them is easy to put on a page.  I have never seen the second one on a budget line and I have looked.

The three parts do not sit together.  The Reviser is the variation.  The gate at Retention is the rectifier.  The maintenance tax is the paid reset.  So when I call something a ratchet I am not pointing at a function.  I am pointing at a whole loop, and at the fact that somebody is paying for it.

**One word on the word, before we go on.**

*Ratchet* is a noun everywhere I have found it.  Feynman's is a toothed wheel.  Muller's is an effect in a population.  The people who study how a technique gets passed from one generation to the next call it a ratchet effect, and on the occasions when they need a verb they say *ratcheting up*, which means very nearly the opposite of what I need.  So I am using it as a plain verb.  I made the verb because I wanted one and there was nobody to ask.  I do not claim it is standard.

What the verb takes as its object is slack, and slack is the next thing I have to define.  When I say a line ratchets its slack I mean *takes it up and holds it there*.  I do not mean *increases it*.

### What I Mean by Slack

Every ratchet works on slack.  That is the whole job.  You have a strap over a load and there is play in it, and you work the handle, and each stroke takes up some of the play, and the pawl is there so the play does not come back while you go around to the other side.  Nothing about that is a figure of speech yet.  That is a strap.

I am going to use *slack* for the quantity each line takes up.  It is a borrowed word doing new work and I will say plainly what I mean by it.

**Slack is how much room a thing has to be otherwise.**

If you have had a mechanics course, the neighborhood is degrees of freedom, and you can carry that with you.  If you have had a statistics course, be careful, because in there the phrase means something else entirely and I am not going to make it worse by using it twice.

Count the ways the molecules in a sealed jar could be arranged and still leave the thermometer reading the same.  That count is slack.  Count the sentences somebody could have handed you before you knew the grammar that rules most of them out.  That is slack too, in a different unit and with nothing in common but the shape.  Every line has a quantity of that shape.  Every line takes it up.  And — this is the part to hold onto, because a great deal later depends on it — no line's slack converts into any other's.

The same four functions turn up at every line — Effector, Regulator, Modeler, Reviser — built out of whatever that line has on hand to build with.  The functions do not change.  What is loose does.  So a line is a machine for taking up one kind of slack, and what makes one line different from another is the slack and not the architecture.

Four lines, four kinds, four units of account.  I will do the first one slowly and the rest of them faster, because after the first you will see that I am asking the same four questions each time: what is loose, what would you count to find out how loose, what takes it up, and what does the taking-up cost.

**The genetic line takes up Boltzmann slack.**

What is loose is the arrangement of matter and energy.  Left alone, a warm thing and a cold thing come to the same temperature, a stack comes apart, a concentration spreads out.  What you count is arrangements: how many different ways the parts could sit and still give you the same reading from outside.  A great many ways means a great deal of slack.  Very few ways means very little.  That count is the thermodynamic entropy, and the Second Law says that in a closed box the count goes up and does not come back down on its own.

What takes it up is a living thing.  It holds its own arrangement narrow by pulling in energy that is concentrated and pushing out waste that is not, and it does this every second of its existence without a day off.  What it costs is everything the organism eats and everything it burns, which is why an animal that stops eating stops being narrow fairly quickly.

You already know this one from a building.  Hold a room at seventy in July.  Heat comes back through the walls, the glass, and around the door, all day, every day, and you pay to move it out all day, every day.  Stop paying and the room is outdoors by suppertime.  There is no condition the building reaches where the bill stops.  A cell is that arrangement on a longer contract.

**The neuronal line takes up Friston slack.**

What is loose here is the fit between what a unit expects and what shows up.  What you would count is how far off the expectation ran — and I have to tell you that the quantity you would actually want is not something anyone can compute, so the formalism substitutes a ceiling on it and works with that instead.  The ceiling has a name, variational free energy, and it has the useful property that pushing the ceiling down pushes the thing underneath it down too.

What takes it up is a nervous system, and it has two moves and it uses both.  Change the model until it matches the world.  Change the world until it matches the model.  Either one closes the gap; most animals are doing both at once and most of the time.  What it costs is a brain, which is metabolically the most expensive tissue an animal can carry, and which it pays for whether or not anything happens that day.

The building version is a control loop that hunts.  You can retune the controller, or you can go fix the ductwork that made the loop hunt in the first place.  Both close the gap.  One is cheaper and one is permanent and the argument about which to do has been going on in mechanical rooms since before I got there.

I should say one thing here that I am not going to say about the other three.  Read as a description, this quantity is a redescription and not a cause, and that is the man's own reading of it, not my objection to him.  Nothing gets explained by saying a unit minimizes it.  What does the explaining is selection, which kept the units that ran the gap narrower.  I am using the quantity as a unit of account and not as an engine, and if you catch me later treating it as an engine, I have made a mistake.

**The symbolic line takes up Shannon slack.**

What is loose is the message.  Before there is any code, a signal could be anything, which is another way of saying it tells you nothing.  What you count is how surprised you should be by the next thing that comes down the wire, averaged over everything that could come — highest when everything is equally likely, and falling as soon as some things become more likely than others.

What takes it up is a constraint.  A word, a grammar, a convention, a rule nobody wrote down about what you do not say at a meeting.  Each one rules out messages that were previously legitimate, and the space of what can be sent gets smaller, and a signal starts carrying something because it might have been otherwise and wasn't.  What it costs is everything spent keeping the constraint alive: teaching it, repeating it, correcting people, and doing it again next generation because nobody is born knowing it.

Take a building code.  Before the code the set of buildings you may put up is enormous and a good number of them fall down or burn.  The code cuts that set to something much smaller, and what is left is a set two strangers who will never meet can agree about in advance.  A drawing standard does it to drawings.  That is what a symbol is: a cut in the space of the permissible, which is the only reason a signal carries anything at all.

**The digital line takes up Kolmogorov slack.**

What is loose is the distance between a thing and the shortest procedure that will produce it.  What you count is the length of that procedure.  A structure with pattern in it has a short one.  A structure with no pattern in it has none shorter than itself.  And in the general case you cannot compute the shortest — you can only ever say you have not found a shorter one yet, which is a genuinely odd property for a measure to have and I do not want to slide past it.

You know this one from a drawing set.  A set of drawings is not the building.  It is the shortest thing you can hand a crew that gets you the building.  Twelve identical floors compress down to one floor with *typical* written on it.  A one-off with no two rooms alike does not compress at all, and for a building like that you cannot beat handing over the building, give or take the cost of saying *here*.

What takes it up is execution.  A procedure that runs gets copied into other procedures; one that never runs is dropped, the way a detail nobody ever built stops turning up in the next job.  And a shorter procedure that does the same work gets copied more, because it is cheaper to run and cheaper to carry.  What it costs is the machine, the power, and somebody keeping both of them going.

All four lines are doing the same thing at the line level.  Keep what worked, lose what did not, repeat.  What differs is what was loose, the machinery that takes it up, and how long one turn takes.  That is why the four lines are genuinely different and not one story told over, and it is also why the same four functions keep showing up in all of them.

**Now the part I would rather you heard from me than worked out later.**

Those four are not four settings on one dial.  They are four different units of account, and there is no exchange rate.  You cannot settle a thermodynamic debt with symbolic slack.  You cannot pay for a narrower model with a shorter program.  That is not a hole in the theory that somebody will patch later — it is the reason the lines are lines at all, because if the four converted freely there would be one line with four settings and nothing to explain.  Non-convertibility is an ordinary property of a unit of account.  Feet do not convert into pounds and nobody files that as a defect of feet.

Three of those four I am confident about.  The fourth I am reasoning by analogy from the other three, and the piece I have not settled is what does the selecting on the digital line.  I have a candidate and I have not been able to talk myself the whole way into it.  Somebody should look at that properly, and it will not be me.

*The first of those four is Deacon's and I am taking it whole — the Shannon-Boltzmann-Darwin paper, 2007.  The second one is two claims stacked and I would rather hand them to you separated.  The formalism is real, it is not mine, and nobody argues about the mathematics.  Reading it as the stuff an entire line works on is my move, and it is the kind of move that is easy to make and hard to check.  The trait surface under it is measured and I am not the one who measured it — Sih, Bell and Johnson, 2004, and Koolhaas on coping styles.  The third one is mine outright.  I think it follows from the same principle, and I have not found anybody who has said so, which is either because it is obvious or because it is wrong.  The fourth one is the one I am least sure of and I would rather tell you now than let you find it out on your own.  The formalism is not in doubt — Solomonoff had it in 1960, Kolmogorov in 1964, Chaitin in 1966, three men separately, which usually means the idea was sitting there waiting.  What is mine is reading it as the goo of an entire line.  And the piece I have not settled is what does the selecting.  I have named Execution and I have not managed to talk myself the whole way into it.*

---

### Flora and Fauna Across Lines

Every line has two ecological roles in it, and I am going to start with the case where I am not being figurative at all.

At the genetic line, flora are plants and fauna are animals, and I mean that the way a botanist means it.  Flora sit still.  They persist, they build the place everything else lives in, and they work on a slow clock.  Fauna move.  They eat, they are quick, and they are flexible in a way the flora they live on is not.  A stand of trees makes a forest and the forest is the condition of everything in it.  Nothing about that needs me.

Now I am going to stretch those two words onto three more lines, and I want to say up front that it is a stretch, because it is.  What I am claiming carries over is the relation and not the biology: something slow that makes the conditions, something fast that lives off them, and neither one able to do without the other.

**At the neuronal line the body is the flora and the brain is the fauna.**  The body is slow, persistent, and it builds the conditions — it grows the brain, it decides what the brain is allowed to spend, it sets which niches the brain will ever operate in.  The brain is fast and local and it forages on what the body provides.

**At the symbolic line, personalities are the flora and memes are the fauna.**  And that one is going to sit badly for a minute, so let me put it plainly before I soften it.  You are not the animal in this picture.  You are the ground.  The ideas are the animals, and they are grazing on you.

I did not get there first and I do not want credit for it.  Pollan spends a book asking whether he planted the potato or whether the potato arranged for him, and the whole trick of it is walking around to the far side and looking back — the bee thinks it is robbing the flower, and from a certain distance it is obvious the flower is running the bee.  Once you have read a hundred pages of that you cannot unsee it, and I am simply doing it again with ideas instead of apples.  *The Botany of Desire*, 2001, if you want the good version.

The relation is loopy and not one-way, which is the part people drop.  Animals forage on plants, and plants have been shaping animals right back for a very long time — the flower makes the bee as surely as the bee makes the flower.  Memes forage on people, and people shape the memes in the same motion.  Neither side is the author.

So:

| Line | Flora | Fauna |
|--------|-------|-------|
| Genetic | Plants | Animals |
| Neuronal | Bodies | Brains and nervous systems |
| Symbolic | Personalities | Memes and meme-complexes |

The digital line has the pair too, and its bond is thinner than any of these and gets thinner the further up you go.  That one needs a longer conversation than it can have tonight and it gets one later.

Three things about the table before we leave it.

**One.  Nothing on the right replaces anything on the left.**  Animals did not replace plants.  Brains did not replace bodies.  Memes have not replaced personalities and are not going to.  The new fast thing develops alongside what becomes its slow thing, and after that they cannot be separated.

**Two.  The flora is not passive, and I want to be firm about this because the word sounds passive.**  Plants manipulate pollinators, run soil chemistry, and organize whole ecosystems on a schedule nobody watching for an afternoon would notice.  Bodies grow brains and hold the purse.  Personalities generate every bit of the symbolic material the memes live on — every sentence said out loud, every object made, every child raised.  What separates the two roles is not activity.  It is *tempo and reach*.  The flora acts slowly and across a wide front.  The fauna acts fast and at one point.  Both of them are working the whole time.

**Three, and this is the one worth carrying out of the room.**  One person is in all three lines at once, in a different role in each.  Your body is genetic-line flora.  Your brain is neuronal-line fauna.  Your personality is symbolic-line flora.  That is not a paradox and it is not a trick of wording.  It is what it looks like when three inheritance systems run through the same animal at three different speeds, and each one sorts that animal into whichever role it is slow or fast relative to.

Which lets me say something about groups that I could not say before.  A band, a settlement, a city, an empire — these are large meme-complexes, and they are **fauna**.  They are not bigger people.  They are not a second kind of person standing beside you with a personality of its own to compare against yours.  They are the animals that live on the ground you are.  When an institution seems to want things you do not want, nothing mystical has happened.  Something fast is foraging on something slow.

---

### What a Clade Is

When I put a name in a box later on, I mean a kind and not a specimen.

The name picks out a representative form, the way *typical* on a drawing means this floor and every floor built like it.  What the name covers has variety inside it, and some of that variety will not match the description in every particular.  That is not sloppiness in the naming.  It is what a name for a kind does.

I say this once here so I do not have to keep saying it every time a name shows up, and because the first objection anybody raises to a diagram of this sort is to find one member of a category that does not fit and hold it up.  It will not fit.  Categories are like that.

---

### The Four Sites, in Brief

A turn of inheritance moves a unit through four places, and it is held differently in each.

1. The **seed bank** holds what is stored.
2. The **clearing** holds what is available now.
3. The **understory** holds what has been taken up but not yet acted on.
4. The **canopy** holds what has been expressed and is out competing.

The four stages are the handoffs between those places, not the places themselves, and the full treatment goes with the selection cycle rather than here.

I will not pretend the words are not a forest.  They are.  I had a stand of them out the back for thirty years and the arrangement is genuinely the arrangement, so I kept it.
