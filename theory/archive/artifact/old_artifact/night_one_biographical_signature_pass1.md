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
