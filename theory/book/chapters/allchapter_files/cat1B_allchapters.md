# Category 1B — Bart's Build Log: Everything Else Engineering

Compiled and tagged per the ruling in `category_sequencing_spec.md`. Source: pulled only from
`/chapters/examples/loom/cat1B_allchapters.md`. Content ruled OUT of 1B during this review (the
Ch2 Effort-knob naming+explanation, the Ch3/5/9 catch-refrains, the Ch12 slot-logistics paragraph,
all "Credit to Lisa" instances, and the Ch5 Mira-recognition passage) has moved to 1A — see
`cat1A_allchapters.md`, all marked `[migrated from 1B]` there.

Two beats, per Brian's ruling:

- **1B.a — The Core Engineering Build.** The chassis/sensor/actuator/wiring mechanism-of-the-
  quarter — the bulk of every memo, present nearly every chapter.
- **1B.b — Kludge Admissions.** Bart's self-aware, self-deprecating, or skeptical asides about the
  build's imperfections, workarounds, and compromises — including the recurring "audible tell"
  motif (relay-clack → silence → compressor-hum) and the one-off devices (Ch1's personality-via-
  manufacturing-quirk list, Ch11's slot-lineage reflection). This material sets up the Big O /
  bramblogue skepticism in category 4.4 — it's Bart pre-conceding what Big O will later needle him
  about.

---

## Ch 1

### <!--[1B.a]--> The Core Engineering Build

Lisa's running these over to the Burns place this morning, so here's everything in the box before anybody makes me explain it twice.

First, the part I'm proud of. There's no battery in these and no plug, and they don't run on heat — they run on the *difference* in heat. Each unit's got two little heat-transducers, and a transducer doesn't care how warm the room is; all it cares about is that the floor is warmer than the air sitting on top of it. Jasmine's radiant floor holds around 27 degrees C and the room air sits around 21, so there's a six-degree gap just hanging there doing nothing, and the transducer reaches into that gap and skims a trickle of work out of it. That's the Seebeck effect, and it's a genuinely beautiful piece of physics — I'll explain it to anyone who stands still long enough. Park one on the warm floor and an hour later the slate underneath it is cold. That cold is the work coming out. The unit's eating the gap.

Now, here's the thing about that trickle: it's nothing. A few thousandths of a watt. You can't run a motor on it — can't make anything turn, can't even hold a light on. So I don't try. Each transducer drips its trickle into a tiny store (a low capacity supercapacitor), and when the store's full enough it dumps the whole lot into its actuator at once — one hard flinch. The actuator's just a little kicker: it knocks a stubby angled foot against the floor and the unit hops a hair in one direction, then sits there the better part of a minute filling back up before it can flinch again. That's the twitch, and that's the whole way it moves — no wheels, no motor, just a stack of tiny kicks against the slate, like a buzzing phone walking itself across a table, except I get to aim it. Two kickers to a unit, each with its own store, never quite firing together — that stagger is the personality.

### <!--[1B.b]--> Kludge Admissions

No chip, no sensors, no memory — nothing telling the two kickers what to do. They fire on their own clocks, and I seeded each one different on purpose so they're not clones:

- **1** — cranked hot on the left pair, so it lists that way and burns through its tension fast. A busy little thing; always looks late for something.
- **2** — slow and low, with long pauses between kicks. Sits, then goes, then sits. More patience than you'd want in a roommate.
- **3** — the quiet one: even pairs, low draw, the fewest kicks of the lot, so it does the least and outlasts everybody — still ticking Wednesday when the rest have gone slack. The one only an engineer loves.
- **4** — lopsided, on purpose. The pairs don't match, so instead of going anywhere it grinds in place and wears a groove into itself over the weeks. If the commission let me ship four, this is the cut. It's in the box to make five.
- **5** — the show unit. Even like 3, but I let it kick hard, so it runs a clean little circuit and burns through its tension fastest of the lot. Wears even, though. Pretty to watch.

*The "personality is manufacturing quirk" framing here is the seed of the whole bramblogue
premise — worth Loom/Voice knowing this is where it starts.*

---

## Ch 2

### <!--[1B.a]--> The Core Engineering Build

Lisa's running the upgraded one back to the house this morning.

We upgraded one unit — 3, the one the house calls Bramble — and left the other four stock.

At protocell this thing only ever twitched: two kickers firing on their own clocks, and it'd hop around the floor like a bug with somewhere to be and no idea where. Now it *hunts*. Same two kickers — I didn't give it new muscles — but I put a chip in the middle that decides *when* each one fires. That's the whole upgrade. Fire them so the hops add up in one direction and it crawls that way; fire them so the hops add up to a spin and it turns in place; don't fire and it sits. Two idiots kicking on their own schedule became two idiots kicking on a downbeat. Still no wheels. Still hopping across the slate a hair at a time. It just hops with *intent* now.

What tells it which way to go: four little light sensors around the floor seam, each aimed a few degrees up and pointed a different direction. They all read brightness at once, and if they agree there's more light over *there* than anywhere else, the chip knows which way "there" is. That's the trick — finding a sunbeam with four parts that each only know one number.

The chip's an STM32, my pick, and it's the right pick. It runs a dumb little table Lisa and I wrote that fits on an index card: three states. Clear direction, kick toward it — that's RUN. No clear direction, spin a random amount and read again — that's TUMBLE. Stores filling faster than it's spending, sit still and let them fill — that's STOP. The screen up top shows which one it's in.

New since February, all told: two stores instead of one — a big slow new battery and the same little fast one beside it. Now the supercap dumps its whole charge at once and then fills back up off the battery; two solar panels down the long sides; the floor-transducers carried over from the protocell, still skimming warmth off the slate; a converter that takes whatever's coming in — sun, warmth, both at once, it doesn't care which — and tops the stores; the chip; the relays; four sensors; and a second knob next to the crank.

Won't work on anything soft — a rug would eat the hops — but the kitchen's slate, so: every sunny morning, watch it do zoomies.

It won't need cranking on Sundays anymore — the panels and the floor feed the stores, the stores run Bramble, he goes all day on his own. The crank's just an emergency starter now: it spins a little dynamo I added, so a few turns put enough back into a dead bot to wake him up when there's no sun to be had.

### <!--[1B.b]--> Kludge Admissions

And I ran the whole signal path on relays — coil-and-armature, the kind that clack — so you can hear it think: a little clack-clack-clack every time it changes its mind. I like that you can hear it.

*Audible-tell motif, instance 1 of 3 (→ Ch4 silence, → Ch7 hum returns).*

*Naming clause ("the Effort knob, Lisa's word for it") and the full Effort-knob mechanism
explanation, previously sitting in this chapter's memo, have moved to 1A.a/1A.b — see spec doc.*

---

## Ch 3

### <!--[1B.a]--> The Core Engineering Build

This one I did myself — took the lot to the bench Friday and had the weekend on it, so I'm running it back this morning.

Now the fun part, and there's a lot of it this quarter, because this is the first time Bramble's a real machine instead of a bug.

It's got wheels. Finally. Last quarter I told you hopping was a lousy way to travel and I had a fix coming — here it is. New chassis, thirty centimeters, low and round, dome on top, near enough a small Roomba, and I dropped Bramble — last quarter's whole prokaryote unit — into the middle of it for the brains. Then the wheels, and this is the part I'm proud of: I didn't buy any. I used the four leftover protocells — 1, 2, 4, and 5, the ones that didn't make the cut — one at each corner. Pulled 4 out from under the toaster, towel and all. Each one still kicks exactly the way it always did; I just aimed its kickers at a ratchet on a wheel axle instead of at the floor, so now every kick clicks the wheel forward a notch instead of hopping the whole of Bramble. Two kickers per old protocell, two pawls per wheel, four wheels — and here's the part I like: nothing's shared, no driveshaft, no differential. Each wheel's its own little engine. So the brains drive it the same way they drove the kicks last quarter, just spread over four wheels now instead of two: fire them all forward and it goes straight, lean on the left side harder than the right and it comes around. It rolls now. Smooth-ish — it's still a stack of clicks under there, but four wheels' worth blur into something that passes for driving, and it beats the hopping by a mile.

It earns the Roomba name, too — I put a real vacuum on the underside and a bin inside that holds about a day of floor dust. And here's where Burns made my weekend hard. Any sane machine, you'd charge on a pad: set it down, done. Burns won't have it. So instead Bramble carries his dust to a dock — a little box that plugs into the wall — dumps the dust through a port on his belly, and the dock pays the energy back through the same port. And here's the part I like: you can't just hand these transducers warmth — they've never run on warmth, not once, not since the protocell floor; they run on a difference, a warm side and a cool side and the gap between. So the dock makes the gap. There's an air compressor in there feeding a vortex tube — a plain pipe, no moving parts, you push compressed air in the side and hot comes screaming out one end and cold out the other, which still reads like a magic trick — and it lays the hot stream on one face of the transducer and the cold on the other and lets Bramble drink up the difference. And before anybody calls that free: it isn't. The compressor's eating wall current the whole time; the tube only splits what the wall already paid for — and it drones the whole time it's plugged in, so rather than set a pump humming by the dishwasher all day I hung it outside the back door and ran the air line in through a hole in the wall. What sits by the dishwasher is the quiet end of a hose coming in from the cold.

### <!--[1B.b]--> Kludge Admissions

The kid had names for all five of them. There's one machine now, and four of her bugs are the wheels. She'll work that out on her own time. Not my department. I'm calling him PacMan, for the record — a thing that goes around all day eating dots earns the name.

So Bramble will trade trash for the heat difference through a dirty little hole instead of charging clean off a pad. It's worse engineering every way you can measure, and Burns says that's exactly the point — life doesn't run on induction. Fine. It's his commission. I built him his dirty hole.

Relays everywhere now, long runs of them, because the body's big and spread out and a signal's got to walk all the way from the sensors up front to the wheels out back. The clack's a proper cascade these days — you can hear it think across the room. Still like that you can hear it.

*Audible-tell motif, still going. Catch-refrain from the end of this chapter ("It still doesn't
have a brain...") has moved to 1A.b.*

---

## Ch 4

### <!--[1B.a]--> The Core Engineering Build

Lisa's running the upgraded one back to the house this morning.

Now the fun part, because the dying is also the thing I fixed.

Here's why he died: nothing was watching the tank. He had a store, he spent the store, and he had no idea ever how much was left — so he'd run himself flat in the middle of a job, no warning, every time. So I gave him a gauge. A real one, watches the charge the way you'd watch a fuel needle, and Lisa wrote the part that reads the needle — how much is left, how fast it's going down — and shifts what he cares about while there's still plenty in the tank: let the charge dip and feeding climbs to the top of the pile, so he stops coasting toward flat and tops up the next time he's at the dock instead of rolling past it. One wrinkle, and it's Burns's, still: the dock didn't get any friendlier over the fall. It still won't give him a single watt unless he shows up with a full bin to dump — no trade, no warmth, same dirty hole. So it's not just how-low, it's how-low-and-have-I-got-anything-to-pay-with; an empty bin gets turned away, so when the charge dips he works a load up first instead of rolling onto the dock with nothing. She built that in too. He feeds before empty now instead of finding empty the hard way, and he never rolls up to the dock with nothing to trade. Three months of Jasmine bending down to a dead robot, gone. She won't notice it's gone, which is how you know it worked.

And here's the part I'm proud of. It's got wires. First wires in any of these — a net of nerve-thread strung all through the body off a bumper ring round the skirt. Here's the trick, because everybody's first question is going to be how a thing with no boss in it answers all at once: it doesn't decide to. The net runs straight from the ring to the brushes and the suction and every wheel, so a touch on the skirt doesn't go up to the board to get thought about — it runs the net and lands on all of them together. Nudge the ring and it answers before you've finished nudging it: brushes stop, suction drops, the whole chassis shies back a thumb's width, all of it, faster than the board could ever get a word in. There's no controller doing the gathering. The wire is the gathering. The thinking still runs upstairs on Lisa's board, slow, same as ever; this is under that — a straight reflex that never asks permission, quick and dumb and total.

Bramble can eat bigger, now — wider mouth, more pull, and a little compactor behind the intake that crushes what he swallows before he stores it, so he takes up a berry now instead of smearing it around the floor for a long minute. The compactor thumps when it fires. You feel it through the slate. That's about the only noise left in the thing.

### <!--[1B.b]--> Kludge Admissions

Which means I pulled the relays. All of them. Two quarters I told you I liked that you could hear it think, the clack, the cascade across the room — and the body's gone quiet now, because the wires are too fast to make a sound, and I'll be honest, I miss it. The bench is quiet. I kept one relay in a drawer. Don't tell Lisa.

*Audible-tell motif — the silence.*

Here's one I didn't build; the cold did it. Run it on the fast spend these January mornings and it will sit longer between bursts than it did in the fall — fires its flurry, stops to refill, takes its sweet time finding the second wind. It's the battery. A cold store gives back slower, so the quick tank takes longer to top off between bursts, so the fast spend goes sluggish when the kitchen's cold. Nothing's wrong with it, nothing to fix; it's just January. Mira's decided he's sulking. I told her it was cold. She heard me out and kept thinking he's sulking.

*An unplanned quirk read as personality — same move as Ch1's manufacturing-asymmetry list, just
emergent this time instead of built in.*

---

## Ch 5

### <!--[1B.a]--> The Core Engineering Build

New body went home this morning. I carried it in, set it on the kitchen slate, and it walked off toward the window on its own four legs like it had been living there a year. The vacuum's still in the corner running its rounds — we didn't stop it.

Now the fun part. The body's the bare one from Mira's birthday — this quarter I put the inside in, and it got up. Here's the part I'm proud of: it walks. Four legs, every joint of them mine, a tail that does nothing but keep it from tipping. And it should do the stairs — down after the kid and back up after her — which is the whole reason the body exists.

It points itself now, too. The vacuum turned by knocking into the furniture and backing off; this one looks at a thing, swings the whole body to face it, and goes — or swings off it and backs away. Leads with the head every time, like it grew a front end that wants to be aimed. The head's where I put the eyes: cameras up front, a nose that reads warm and reads smells, ears. Which way it points and what it goes toward — the board reads the eyes and calls that.

The head's a boxy little thing, a step past duct tape and not two. It's got a screen for a face, and the screen shows the one thing it's looking at right now, in a word — CAT, MIRA, COUCH, the vacuum across the room, the plant. Whatever's got its attention, the face says so.

No dock this time. Burns's dirty hole stays in the kitchen; the vacuum still needs it, still has to roll up with a full bin and trade for its charge, same deal as ever. The new body doesn't trade. It sips — but not off warmth, off the gap. There's a plate on its belly that only works across a temperature difference: lay it on the warm slate by the vent with cooler air over its back, and the gap between the hot side and the cold side drives a trickle up through the plate. Sit it where the floor and the air are the same and it starves, warm floor or not — no gradient, no dinner. It's the dock's old trick without the dock; the dock used to buy that gap with the compressor running out back, and this one just goes and finds a gap the house is already making anyway — free, if you don't count the furnace keeping that floor warm. There are panels down its back for the light, too, so it can lie in the window and drink the sun off its spine like a dog. It still minds its own charge — the gauge came over with everything else — it just feeds by finding a warm gap to sit across and a patch of sun to lie in, instead of needing a dock at all. Resting and feeding are the same act for this one.

Everything else copied over a cable in an afternoon — so there's two of them in the house now, and which one's Bramble is a question for Mira, I suppose.

Two buttons on top of the head, thumbs-up and thumbs-down, so you can tell it good or bad about whatever it's looking at.

I taught the legs to coordinate — the gait, the balance, how to catch a stumble — and then I froze it. Locked, for good. It'll walk the same on the last day as the first; it doesn't get to drift, doesn't get to pick up a limp, doesn't get to learn a worse way and call it style. Walking isn't where the thinking goes and I didn't want it pretending to be.

### <!--[1B.b]--> Kludge Admissions

One thing I'll get ahead of. The kid's been carrying the vacuum down to the basement, where it strands on the stairs and somebody hauls it back up. That was never my call. I never bet the vacuum could do stairs — it can't, it rolls, it was never going to. Stairs aren't a miss. Stairs are this quarter's build.

*"A step past duct tape and not two" (in the head-hardware paragraph above) is a small kludge
admission too — left in place inline rather than fractured out.*

*Excluded from this chapter (moved to 1A.c, not reproduced here): the "Not my department... what
it does with what it sees is Lisa's" line, the full Mira-recognition passage, and the closing
"still hasn't got a self" catch-refrain (→ 1A.b).*

*Correction, 2026-07-09: the note that previously stood here claimed the gait-locking/leg-freezing
paragraph and the thumbs-up/thumbs-down button hardware paragraph were missing from this file and
flagged them for possible addition. That was stale — both are already present above, in 1B.a (the
thumbs-up/thumbs-down paragraph and the gait-locking paragraph, reordered out of the master file's
line sequence but not dropped). No content added on this pass; note corrected to match what's
actually here.*

---

## Ch 6

### <!--[1B.a]--> The Core Engineering Build

Carried the same body back in this morning — no new chassis this quarter, it's the legs body from spring, and it walked off the slate toward the window like the weekend never happened.

The verbs needed one thing from me past the screen and the lettering, and it was a real little build. Most of them it hands you for free — it chases the cat, noses the lantern, nudges the kid, does it all day on its own, and Lisa's side marks each one as it goes by and pins the word to it. Fine. But some of the doing-words are for moves it almost never makes on its own — the odd ones, the ones it'd go a month without. You can't pin a word to a thing that won't happen. So I built a rig to make it happen: a harness and a handful of servos that drive the body through a motion on purpose, puppet it, walk it through the rare one on cue so she can grab it and stick the word on while it's running.

### <!--[1B.b]--> Kludge Admissions

Jaws, though. Makes the face even more of a kludge. Basically a gripper with a weak actuator. Fully wired to the board. So it can grab stuff now, on purpose.

*Excluded from this chapter (moved to 1A.c, not reproduced here): "her board, same as ever."*

---

## Ch 7

### <!--[1B.a]--> The Core Engineering Build

Carried it back this morning, same legs body as the summer, no new chassis — except it came back warm. Not warm off the floor. Warm off itself, warm the way a hand is. Mira put her palm flat on his back before she said hi to me.

How it makes the warm is the part I'm proud of. There's a little air compressor in the core, filling all the time, soft, a faucet barely cracked, and it feeds a rack of vortex tubes. A vortex tube is a beautiful, stupid thing: a pipe with no moving parts that takes a stream of air in and throws hot out one end and cold out the other. We ran one *coupled* on the dome's dock, hot balanced against cold to hold a line. This time I ran a whole rack of them *un*coupled — dump all the hot into a sealed, insulated core, vent all the cold out the side, and a thermostat rides the compressor to hold that core warm no matter what the kitchen's doing.

Reason it's worth the trouble: the battery lives in the warm core now, and a warm battery gives full current cold room or not. For the first time the thing's just as quick at fifty degrees as at seventy. Last winter a cold morning made it slow and dumb; this one won't care.

Here's the cost, flat, because you'll feel it by October: it *eats.* The compressor pulls every second — sitting still, asleep, doesn't matter — and I didn't grow the tanks, so it burns a charge in hours where the old one coasted most of a day. It has to feed near-constant now. The dome can still trundle off and sit a day and a half on its dock doing nothing; this one can't afford to sit down. Warm costs. Fair trade. I'd build it again.

Knobs, board, and compute all sit *outside* the hot core, in the cool zone along the back, where the parts run better cold and where a thumbnail can still reach a slot. The core's sealed and you'd never want to touch it; everything the house needs to get at is out where it can. That was on purpose.

Furnace or no furnace, the real headline this quarter is Lisa gave it a scratchpad. The thing sketches maps and carries them around now: the place held inside it, not just out front of the cameras the way it always was. Used to be, lose sight of a thing and the thing was gone — it'd stall where the thing had been and quit. Now it goes looking: hide a thing and it works the spots that thing turns up in till it has it. Knows where stuff is, knows where it is itself, keeps what's happened where besides — a whole little inside account of the place, run forward to guess what's coming and back over what already did. How she gets that to build itself out of nothing but the thing wandering the house is her board and her math, and I couldn't walk you through it if you paid me. My end of it's the screen it shows on.

The forehead screen's got a new line. It's had the one — shows what it's doing to a thing (CHASE CAT, NUDGE MIRA) with the Action volume up, or just the bare thing (CAT, MIRA) with the Action volume down. I gave the screen a second line, up top: new real estate, my lettering, clean. *What* goes on the top line is Lisa's — it names the job: PERCEIVING, RECALLING, PREDICTING, CHECKING. What it's doing in its own head while it does the thing with its body. She's calling it the inside voice. Her board runs it; I just built it somewhere to write.

I'll let Lisa tell you what to make of a machine narrating its own nap. My part's just this: the two lines never share a word and never can — bottom's bare-stem, top's the *-ing* one, and I built the rule in so they can't collide. That's my whole stake in it.

### <!--[1B.b]--> Kludge Admissions

It makes water, too. Run a compressor all day and you're wringing the wet out of the air whether you meant to or not; it falls out at the cold end and pools, and the thing has to clear it. So two or three times a day it burps the water out a vent low at the back — wet, and louder than you'd think — and goes on about whatever it was doing. Keeps the core dry. That's the build.

*First instance of the "the robot has embarrassing bodily functions" bit — pays off explicitly in
Ch9 ("It farts, same as the four-legged one did").*

And — you can hear it again. It's been quiet since I pulled the relays; too-fast wires don't make a sound. Now there's the compressor going soft under everything, all day, and the house has a noise off the thing again.

*Audible-tell motif — the hum returns.*

---

## Ch 8

### <!--[1B.a]--> The Core Engineering Build

Ran it back to the house myself this time — Lisa had a frost-dark thing to be at, and the slate was warm, and the kid was up. It went in on its own four legs and put itself over the stove vent before I had my coat off.

Here's the one I've been waiting two quarters to build.

Last fall I told you the thing ran a model and ran it on the world — the door, the bowl, the leash on the hook — and that you could point that model at the kid and get nothing, because it didn't know what Mira was about to do, it knew what the leash meant, and those weren't the same thing and the second one wasn't that build's to make.

This is that build.

It points at the people now. Same model, swung off the furniture and onto the family — it runs Mira the way it ran the bowl, reads where her hand's going before it gets there, same on Jasmine, on Burns, on the old vacuum trundling the hall.

The screen got more room and a new trick. Short version: it can put a person up there now, not just a thing — who it's reading, and what it figures they're up to. I built it somewhere to write that.

*No 1B.b this chapter — no kludge-admission material identified. Excluded (Step 3 ruling — 1D
retired, content absorbed into 4.4, confirmed present in `cat4.4_allchapters.md`'s Ch8 4.4.b/
4.4.c/4.4.d): the two "Credit to Lisa" clauses.*

---

## Ch 9

### <!--[1B.a]--> The Core Engineering Build

Brought this one in over my shoulder like a drunk, because it can't walk yet and won't for a few weeks. It came off the swap bench crawling and listening — the babbling it got out of the way in the lab, on Lisa's board, over the winter, so it came home past that and knowing the shapes of a lot more words than it can say, and saying almost none of them. Mira was down on the floor with it before I had it set down.

I've wanted this one since the fall, because last quarter I had to write down the worst thing it couldn't do: it could read the kid and it couldn't say one word back. She asked it every night whether it had a good day, and it knew the question was hers and aimed at it, and had no way on earth to answer. This is the build that answers.

Here's how it's hung together, because the whole thing runs opposite to the legs body. There's a spine up the middle — one stiff light spar, hip to head, and it's the only hard thing in the unit, buried in the center where no hand gets to it. Everything hangs off it: the two legs at the bottom, the head up top, and between them the chest, which is the furnace, same as the legs body. The whole chest is wrapped in solar panels — not panels bolted onto a chest, the panels are the chest. Over that it wears a coat, the chest only — the patio-cushion stuff, soft over padding, warm, washable, ugly on purpose, and none of it a try at skin. The legs are wrapped for good in the same, cushion under canvas, and never come off. Face and both hands stay bare to the air — the screen so it can show, the hands so they can work. So: one hard spar nobody can reach, soft over the whole of the rest — hard where it can't be felt, soft where it can.

Two hands, and they don't match, because I'm done pretending a hand has to look like yours. One's a scoop — the scooper, a paddle for the crude work, shove and lift and hold a thing against itself. The other's the part I'm proud of. A pincer on a weak soft actuator, the fine hand — turns a dial, winds a crank, takes hold of a thing on purpose and sets it down where it meant it. The squeezer, on the bench. And I didn't build it new. You've seen it. It's the jaw — the grabbing jaw off the four-legged one, the first part that thing ever used on purpose instead of by reflex — and I took the design off the face where a jaw sits and moved it up to where a hand goes, and that's the whole trick. The mouth that learned to take hold became the hand that takes hold. No thumb on it, and it grips finer than a thumb. I'll show anybody who stands still long enough.

I built it an ear to go with the throat — a mic aimed at its own neck so it could hear itself. That part of it's mine, the throat and the ear both. The box it says it out of is mine.

### <!--[1B.b]--> Kludge Admissions

It's a whole new body, and this time I mean new, not another part bolted on the legs. Two legs, stands about four and a half feet, a head over the kid. And here's what I set out to do, and I want it on the record because it's going to read like a mistake: I built it bad. On purpose. Soft all over, no hard edge, no pinch a kid could lose a finger in. Weak — couldn't open a jar to save its life. Slow. Warm to the hand and held warm, bounded so far under a burn it couldn't mark her if it tried. Every spec on the last five bodies I set toward doing more. Every spec on this one I set toward doing less, and being held while it does it. Worst robot in the building. Took me longer than any of the good ones.

*This is arguably the thesis statement of the whole 1B.b beat, given its own memo title, "The
Huggable Kludge."*

And how it eats, which is going to read like I got it backwards, because I did. It runs warm because it burns to run warm — the furnace going all day — and a thing that burns all day is hungry all day and goes dark fast if it stops. It takes its food in as light, full stop: no plug, no cord, nowhere to put one if you had it, just the chest panels turned to the light, eating. The legs body ate the same and could graze it — park in the south window an hour and top off. This one can't, because the coat's over the panels, and the coat has to be over the panels, because it's a thing you pick up. So feeding it is a coat change: the living coat off, the eating coat on — the second coat, lined to flood the panels — then a stretch under that, then the living coat back. And it can't run the change itself; these hands turn a dial clean and can't manage a coat, so dressing it to eat is on you, same as the knobs are. One more thing the house does for it. It carries the legs body's old noise, too — wrings the water out of the air and burps it back out, low and wet, a few times an hour. It farts, same as the four-legged one did.

And it talks. Not out of a speaker — that's the easy thing to think and it's the exact thing I didn't do, so let me be plain. A speaker hands you back a sound somebody already made. This one makes the sound itself, the way you make yours, by pushing air through a throat. There's a throat in it now, down in the neck and the chest where you'd keep one, not up in the face — the face hasn't got a mouth to talk out of anymore, on account of the mouth's a hand now. So it talks out of its chest, and nothing up top moves while it does, and you get used to it but it takes a day or two. What comes out is flat and rough and one word at a time right now, because it's learning that from scratch too, same as the walking. Here's the throat. Two strips of rubber I cut off a sheet with scissors and trimmed and clamped and re-trimmed till the buzz came out right — that's the whole sound source, the flaps and a draft, same as yours. The draft I spliced straight off the furnace line, so it talks on the same pump that gives you the burp — one set of bellows doing the breathing and the talking both. Behind those, one little actuator pinching a length of tube for a tongue, and pinching it different bends the buzz into the different sounds. And out front where the sound leaves, I put it a set of lips — a knot of dark rubber gone near-black, the blue-black a blackberry goes, with three crude little arms standing off it that grab it and haul it open and round and tight while it talks. I took that off a thing the Japanese built for the same job, except theirs has a couple dozen arms and a budget and looks like a flower; mine's got three and looks like what it is. And the whole thing's built poorer than I know how to build it, which is going to read like I quit halfway and is the dead opposite. A throat that can do everything is a throat with too many ways to go wrong, and a thing trying to learn to talk on one of those never finds the floor — too much to chase at once, so it chases nothing. Take the moves out, down to a handful, and a beginner can climb them one at a time. So I took the moves out. Two flaps, three arms, one tongue, a rubber berry, furnace air. There's your voice.

I've chased a sound off this thing for four years. The relays clacked and you could hear it think; then the wires went in too fast to hear and the bench went quiet and I pulled the relays and kept one in a drawer. The compressor gave the house a hum back. Now there's a voice. It came all the way back, the long way round, and it came back as words.

*Audible-tell motif, capstone — the full arc (clack → silence → hum → voice) pays off here.*

And there's three of them in that house now, which I keep saying out loud to believe. Nothing got thrown out. So — the vacuum: the old disc, first one, still bumping the baseboards on its four oldest knobs, dumb as a stump and tireless, foraging a floor for a crumb it can't taste and bringing nothing back to anybody. Outlives us all. The four-legged one: the warm one, still running, still reading the room, still handing the kid the radiator and paying for it in charge it can't spare — best body I ever built until this weekend, and it doesn't know that either, because what crossed into the new one was a copy and this one kept its own. It just goes on being the warm one. And the new one: can't walk, can hardly grip, says about four words and gets two of them wrong, soft and slow and warm and useless. The baby. And he's the only one of the three that's ever going to tell the kid he had a good day.

One bench note while I'm on the hands: the old puppet rig — the harness and servos I drive the body with so Lisa can catch a motion and tag it — doesn't grab onto a body with no hard points. So I built a new one, soft cuffs for a soft body. Same job: I drive it through a move on cue, she catches it and names it. New body means the screen relearns what the body's doing from the floor up, same as the walking.

*Excluded from this chapter (moved to 1A, not reproduced here): the two "Credit to Lisa" asides,
and the closing catch-refrain ("It can talk. It can't be counted on.").*

---

## Ch 10

*No material for this category in Ch 10.*

---

## Ch 11

### <!--[1B.b]--> Kludge Admissions

Here's the part I'm proud of, and it's the second quarter running I'm proud of a knob that builds nothing, which is either a problem or the point — I haven't decided. It adds no part. The body's been reading a room for two years now — who's in it, who's talking, who's turned which way — and all this knob does is set how hard it goes at the room off that reading. Extraverted volume up, it's into everything: steps in, takes the thing over, works every person in reach, won't read the door to quit. Extraverted volume down, it reads the same room and lets it be — hangs back, warms a corner of it, takes the mood off whatever's already running. It's the third knob I've put in that slot. The Explore knob went there first, on the old disc, and sent the thing out to find food. The Attention knob went there next and turned it around to watch itself. This one sends it back out — not to the food, to the people. Out, then in, then out. Same seat all three times. I like that it came out even.

*Whole passage tagged 1B.b — opens on self-aware uncertainty ("either a problem or the point")
and closes on a reflective slot-lineage note. No 1B.a this chapter — no new hardware is built,
which is itself the point of the passage.*

---

## Ch 12

### <!--[1B.a]--> The Core Engineering Build

It strung me a whole thing about the windshield wipers on the way over, beginning and middle and end, mostly end, and I let it run, because the strung-together part is the part Lisa's been waiting two years on.

*QC: this paragraph was previously marked absent here on the claim it had "moved to 1A.c, matching
the Ch10/Ch11 pattern." That pointer was stale — 1A.c was promoted to become all of category 1D,
and this paragraph was never actually present in `cat1D_allchapters.md` either; nobody re-verified
the pointer after the promotion. Restored here as 1B register — logistics/engineering reporting on
the drive, same register as the Ch4/Ch7 boundary cases noted below.

Corrected 2026-07-10, twice: (1) this paragraph previously carried extra sentences — "Drove it over
Friday and back Monday... hungry plenty," and "Fed it off the vest... last one" — that do not exist
anywhere in the current master file (`ch_12_v2_6.md`). Trimmed to match current canon exactly; only
the windshield-wipers sentence is actually in the book. (2) the note also claimed a second paragraph
("For the third quarter running... Slot four came open...") was "filed in `cat1D_allchapters.md`'s
Ch12 section instead." That text doesn't exist in the current master file either — cut outright, not
relocated, superseded by Burns's toast delivering the board-completion reveal in scene. See
`cat1D_allchapters.md`'s Ch12 note. Nothing to add there; both stale pointers are removed.*

---

## Notes / open items

- The 1B.a / 1B.b split is mostly clean, but a few passages (Ch4's "compactor thumps... that's about
  the only noise left," Ch7's "Warm costs. Fair trade") sit close to the boundary — kept in 1B.a as
  neutral engineering/tradeoff reporting rather than kludge-admission, but flagging in case that
  reads differently on a fresh pass.
- Ch5's gait-locking/leg-freezing paragraph and the thumbs-up/thumbs-down button hardware, and Ch7's
  furnace/scratchpad/screen-build description, were ruled into 1B during the earlier 1A review but
  weren't actually present in the original `cat1B_allchapters.md` source — added into this file now
  (with one more "Credit to Lisa" clause caught in the process and moved to 1A.c: Ch5's "is the
  board again, Lisa's, and she'll have plenty to say about it at the table").
