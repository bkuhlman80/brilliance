Ch 1

## Build log — Five units, out the door
*Bart, hardware. Filed February 12, 2031, for the team.*

Lisa's running these over to the Burns place this morning, so here's everything in the box before anybody makes me explain it twice.

First, the part I'm proud of. There's no battery in these and no plug, and they don't run on heat — they run on the *difference* in heat. Each unit's got two little heat-transducers, and a transducer doesn't care how warm the room is; all it cares about is that the floor is warmer than the air sitting on top of it. Jasmine's radiant floor holds around 27 degrees C and the room air sits around 21, so there's a six-degree gap just hanging there doing nothing, and the transducer reaches into that gap and skims a trickle of work out of it. That's the Seebeck effect, and it's a genuinely beautiful piece of physics — I'll explain it to anyone who stands still long enough. Park one on the warm floor and an hour later the slate underneath it is cold. That cold is the work coming out. The unit's eating the gap.

Now, here's the thing about that trickle: it's nothing. A few thousandths of a watt. You can't run a motor on it — can't make anything turn, can't even hold a light on. So I don't try. Each transducer drips its trickle into a tiny store (a low capacity supercapacitor), and when the store's full enough it dumps the whole lot into its actuator at once — one hard flinch. The actuator's just a little kicker: it knocks a stubby angled foot against the floor and the unit hops a hair in one direction, then sits there the better part of a minute filling back up before it can flinch again. That's the twitch, and that's the whole way it moves — no wheels, no motor, just a stack of tiny kicks against the slate, like a buzzing phone walking itself across a table, except I get to aim it. Two kickers to a unit, each with its own store, never quite firing together — that stagger is the personality.

No chip, no sensors, no memory — nothing telling the two kickers what to do. They fire on their own clocks, and I seeded each one different on purpose so they're not clones:

- **1** — cranked hot on the left pair, so it lists that way and burns through its tension fast. A busy little thing; always looks late for something.
- **2** — slow and low, with long pauses between kicks. Sits, then goes, then sits. More patience than you'd want in a roommate.
- **3** — the quiet one: even pairs, low draw, the fewest kicks of the lot, so it does the least and outlasts everybody — still ticking Wednesday when the rest have gone slack. The one only an engineer loves.
- **4** — lopsided, on purpose. The pairs don't match, so instead of going anywhere it grinds in place and wears a groove into itself over the weeks. If the commission let me ship four, this is the cut. It's in the box to make five.
- **5** — the show unit. Even like 3, but I let it kick hard, so it runs a clean little circuit and burns through its tension fastest of the lot. Wears even, though. Pretty to watch.

Ch 2

## Build log — Knob two, one unit up
*Bart, hardware. Filed June 2, 2031, for the team.*

Lisa's running the upgraded one back to the house this morning.

We upgraded one unit — 3, the one the house calls Bramble — and left the other four stock.

At protocell this thing only ever twitched: two kickers firing on their own clocks, and it'd hop around the floor like a bug with somewhere to be and no idea where. Now it *hunts*. Same two kickers — I didn't give it new muscles — but I put a chip in the middle that decides *when* each one fires. That's the whole upgrade. Fire them so the hops add up in one direction and it crawls that way; fire them so the hops add up to a spin and it turns in place; don't fire and it sits. Two idiots kicking on their own schedule became two idiots kicking on a downbeat. Still no wheels. Still hopping across the slate a hair at a time. It just hops with *intent* now.

What tells it which way to go: four little light sensors around the floor seam, each aimed a few degrees up and pointed a different direction. They all read brightness at once, and if they agree there's more light over *there* than anywhere else, the chip knows which way "there" is. That's the trick — finding a sunbeam with four parts that each only know one number.

The chip's an STM32, my pick, and it's the right pick. It runs a dumb little table Lisa and I wrote that fits on an index card: three states. Clear direction, kick toward it — that's RUN. No clear direction, spin a random amount and read again — that's TUMBLE. Stores filling faster than it's spending, sit still and let them fill — that's STOP. The screen up top shows which one it's in. And I ran the whole signal path on relays — coil-and-armature, the kind that clack — so you can hear it think: a little clack-clack-clack every time it changes its mind. I like that you can hear it.

New since February, all told: two stores instead of one — a big slow new battery and the same little fast one beside it. Now the supercap dumps its whole charge at once and then fills back up off the battery; two solar panels down the long sides; the floor-transducers carried over from the protocell, still skimming warmth off the slate; a converter that takes whatever's coming in — sun, warmth, both at once, it doesn't care which — and tops the stores; the chip; the relays; four sensors; and a second knob next to the crank — the Effort knob, Lisa's word for it.

The Effort knob's the same shape as the crank — same as all of them will be. The crank you wind and it drains back down across the week; this one you set and it stays where you put it. All it does is pick which store Bramble spends from. Effort volume down draws the big slow battery and he runs even — a patter of hops he'll keep up all day, never quick, never quits. Effort volume up draws the little fast one and he runs in bursts — sits, fires off a flurry of hops quick as you like, then stops dead to refill off the slow store before he can go again. Aerobic or anaerobic is the mechanism under it, the way Lisa describes it; same bot, two ways to spend. The fast spend burns through a charge quicker — you don't get as far per drop in bursts — so leave the volume up and you'll be chasing a sunbeam sooner. Which way the house leaves it set is the house's business. I built both.

Won't work on anything soft — a rug would eat the hops — but the kitchen's slate, so: every sunny morning, watch it do zoomies.

It won't need cranking on Sundays anymore — the panels and the floor feed the stores, the stores run Bramble, he goes all day on his own. The crank's just an emergency starter now: it spins a little dynamo I added, so a few turns put enough back into a dead bot to wake him up when there's no sun to be had.

Ch 3

## Build log — Five into one
*Bart, hardware. Filed September 1, 2031, for the team.*

This one I did myself — took the lot to the bench Friday and had the weekend on it, so I'm running it back this morning.

Now the fun part, and there's a lot of it this quarter, because this is the first time Bramble's a real machine instead of a bug.

It's got wheels. Finally. Last quarter I told you hopping was a lousy way to travel and I had a fix coming — here it is. New chassis, thirty centimeters, low and round, dome on top, near enough a small Roomba, and I dropped Bramble — last quarter's whole prokaryote unit — into the middle of it for the brains. Then the wheels, and this is the part I'm proud of: I didn't buy any. I used the four leftover protocells — 1, 2, 4, and 5, the ones that didn't make the cut — one at each corner. Pulled 4 out from under the toaster, towel and all. Each one still kicks exactly the way it always did; I just aimed its kickers at a ratchet on a wheel axle instead of at the floor, so now every kick clicks the wheel forward a notch instead of hopping the whole of Bramble. Two kickers per old protocell, two pawls per wheel, four wheels — and here's the part I like: nothing's shared, no driveshaft, no differential. Each wheel's its own little engine. So the brains drive it the same way they drove the kicks last quarter, just spread over four wheels now instead of two: fire them all forward and it goes straight, lean on the left side harder than the right and it comes around. It rolls now. Smooth-ish — it's still a stack of clicks under there, but four wheels' worth blur into something that passes for driving, and it beats the hopping by a mile.

The kid had names for all five of them. There's one machine now, and four of her bugs are the wheels. She'll work that out on her own time. Not my department. I'm calling him PacMan, for the record — a thing that goes around all day eating dots earns the name.

It earns the Roomba name, too — I put a real vacuum on the underside and a bin inside that holds about a day of floor dust. And here's where Burns made my weekend hard. Any sane machine, you'd charge on a pad: set it down, done. Burns won't have it. So instead Bramble carries his dust to a dock — a little box that plugs into the wall — dumps the dust through a port on his belly, and the dock pays the energy back through the same port. And here's the part I like: you can't just hand these transducers warmth — they've never run on warmth, not once, not since the protocell floor; they run on a difference, a warm side and a cool side and the gap between. So the dock makes the gap. There's an air compressor in there feeding a vortex tube — a plain pipe, no moving parts, you push compressed air in the side and hot comes screaming out one end and cold out the other, which still reads like a magic trick — and it lays the hot stream on one face of the transducer and the cold on the other and lets Bramble drink up the difference. And before anybody calls that free: it isn't. The compressor's eating wall current the whole time; the tube only splits what the wall already paid for — and it drones the whole time it's plugged in, so rather than set a pump humming by the dishwasher all day I hung it outside the back door and ran the air line in through a hole in the wall. What sits by the dishwasher is the quiet end of a hose coming in from the cold. 

So Bramble will trade trash for the heat difference through a dirty little hole instead of charging clean off a pad. It's worse engineering every way you can measure, and Burns says that's exactly the point — life doesn't run on induction. Fine. It's his commission. I built him his dirty hole.

Relays everywhere now, long runs of them, because the body's big and spread out and a signal's got to walk all the way from the sensors up front to the wheels out back. The clack's a proper cascade these days — you can hear it think across the room. Still like that you can hear it.

It still doesn't have a brain — Burns is clear about that, and for once I agree with him. It's a cart that remembers the moves it usually makes. But it rolls, it cleans, it feeds itself. A year ago it was five things twitching on a warm floor; now it's one thing that drives. I'll call that a good weekend.

Ch 4

## Build log — the Action knob, the wires go in
*Bart, hardware. Filed December 1, 2031, for the team.*

Lisa's running the upgraded one back to the house this morning.

Now the fun part, because the dying is also the thing I fixed.

Here's why he died: nothing was watching the tank. He had a store, he spent the store, and he had no idea ever how much was left — so he'd run himself flat in the middle of a job, no warning, every time. So I gave him a gauge. A real one, watches the charge the way you'd watch a fuel needle, and Lisa wrote the part that reads the needle — how much is left, how fast it's going down — and shifts what he cares about while there's still plenty in the tank: let the charge dip and feeding climbs to the top of the pile, so he stops coasting toward flat and tops up the next time he's at the dock instead of rolling past it. One wrinkle, and it's Burns's, still: the dock didn't get any friendlier over the fall. It still won't give him a single watt unless he shows up with a full bin to dump — no trade, no warmth, same dirty hole. So it's not just how-low, it's how-low-and-have-I-got-anything-to-pay-with; an empty bin gets turned away, so when the charge dips he works a load up first instead of rolling onto the dock with nothing. She built that in too. He feeds before empty now instead of finding empty the hard way, and he never rolls up to the dock with nothing to trade. Three months of Jasmine bending down to a dead robot, gone. She won't notice it's gone, which is how you know it worked.

And here's the part I'm proud of. It's got wires. First wires in any of these — a net of nerve-thread strung all through the body off a bumper ring round the skirt. Here's the trick, because everybody's first question is going to be how a thing with no boss in it answers all at once: it doesn't decide to. The net runs straight from the ring to the brushes and the suction and every wheel, so a touch on the skirt doesn't go up to the board to get thought about — it runs the net and lands on all of them together. Nudge the ring and it answers before you've finished nudging it: brushes stop, suction drops, the whole chassis shies back a thumb's width, all of it, faster than the board could ever get a word in. There's no controller doing the gathering. The wire is the gathering. The thinking still runs upstairs on Lisa's board, slow, same as ever; this is under that — a straight reflex that never asks permission, quick and dumb and total.

Which means I pulled the relays. All of them. Two quarters I told you I liked that you could hear it think, the clack, the cascade across the room — and the body's gone quiet now, because the wires are too fast to make a sound, and I'll be honest, I miss it. The bench is quiet. I kept one relay in a drawer. Don't tell Lisa.

Bramble can eat bigger, now — wider mouth, more pull, and a little compactor behind the intake that crushes what he swallows before he stores it, so he takes up a berry now instead of smearing it around the floor for a long minute. The compactor thumps when it fires. You feel it through the slate. That's about the only noise left in the thing.

Here's one I didn't build; the cold did it. Run it on the fast spend these January mornings and it will sit longer between bursts than it did in the fall — fires its flurry, stops to refill, takes its sweet time finding the second wind. It's the battery. A cold store gives back slower, so the quick tank takes longer to top off between bursts, so the fast spend goes sluggish when the kitchen's cold. Nothing's wrong with it, nothing to fix; it's just January. Mira's decided he's sulking. I told her it was cold. She heard me out and kept thinking he's sulking.

Ch 5

## Build log — Off the dock, onto legs
*Bart, hardware. Filed March 3, 2032, for the team.*

New body went home this morning. I carried it in, set it on the kitchen slate, and it walked off toward the window on its own four legs like it had been living there a year. The vacuum's still in the corner running its rounds — we didn't stop it.

One thing I'll get ahead of. The kid's been carrying the vacuum down to the basement, where it strands on the stairs and somebody hauls it back up. That was never my call. I never bet the vacuum could do stairs — it can't, it rolls, it was never going to. Stairs aren't a miss. Stairs are this quarter's build.

Now the fun part. The body's the bare one from Mira's birthday — this quarter I put the inside in, and it got up. Here's the part I'm proud of: it walks. Four legs, every joint of them mine, a tail that does nothing but keep it from tipping. And it should do the stairs — down after the kid and back up after her — which is the whole reason the body exists.

It points itself now, too. The vacuum turned by knocking into the furniture and backing off; this one looks at a thing, swings the whole body to face it, and goes — or swings off it and backs away. Leads with the head every time, like it grew a front end that wants to be aimed. The head's where I put the eyes: cameras up front, a nose that reads warm and reads smells, ears. Which way it points and what it goes toward — the board reads the eyes and calls that. Not my department. I built the head and put the eyes in the front of it; what it does with what it sees is Lisa's.

The head's a boxy little thing, a step past duct tape and not two. It's got a screen for a face, and the screen shows the one thing it's looking at right now, in a word — CAT, MIRA, COUCH, the vacuum across the room, the plant. Whatever's got its attention, the face says so.

I rushed past that for a month, and I want to stop on it, because it's the best thing in the build and it isn't mine. The screen's mine — a display and a lookup, easy. But the word has to land on something, and the something is Lisa's, and it's the hard part by a mile. Take MIRA. I can't type in what Mira *is.* There's no picture of her to check against — her face is different by the hour, she's a foot of motion in a doorway. You can't write the rule. So Lisa built the thing to grow its own Mira instead: a year of her went in — the cameras, a shirt off the floor, her voice off a recording — and somewhere in the board a shape settled that goes off when she comes in the room and stays flat when she doesn't. Nobody drew that shape. Nobody could; I asked. It's just what a year of one kid presses into a board. And then we don't write MIRA onto Mira — we write it onto the shape. Hold the kid up, say the word, hold her up, say the word, till the shape and the word are stuck, the exact way you teach a kid her own name.

So when the house says he *knows* her — that part isn't mine. I bolted a screen on a head. Lisa built something that taught itself a whole kid in a language with one speaker, and we taped a word on the outside so the rest of us could read along. The word's for us. The knowing was in there first. She basically taught it to read minds and gave us a little screen to read its mind back. The knowing is hers. I just built the part that shows.

No dock this time. Burns's dirty hole stays in the kitchen; the vacuum still needs it, still has to roll up with a full bin and trade for its charge, same deal as ever. The new body doesn't trade. It sips — but not off warmth, off the gap. There's a plate on its belly that only works across a temperature difference: lay it on the warm slate by the vent with cooler air over its back, and the gap between the hot side and the cold side drives a trickle up through the plate. Sit it where the floor and the air are the same and it starves, warm floor or not — no gradient, no dinner. It's the dock's old trick without the dock; the dock used to buy that gap with the compressor running out back, and this one just goes and finds a gap the house is already making anyway — free, if you don't count the furnace keeping that floor warm. There are panels down its back for the light, too, so it can lie in the window and drink the sun off its spine like a dog. It still minds its own charge — the gauge came over with everything else — it just feeds by finding a warm gap to sit across and a patch of sun to lie in, instead of needing a dock at all. Resting and feeding are the same act for this one.

Everything else copied over a cable in an afternoon — so there's two of them in the house now, and which one's Bramble is a question for Mira, I suppose.

It walks, it points itself, it climbs, and it'll learn a little — it'll work out that one thing means another, the way the vacuum learned the leaf blower wasn't worth the flinch. But it can't yet learn from what it does. It can learn what the world tells it; it can't learn from its own moves — that this one paid and that one didn't, and do more of the first. Nothing it does loops back and changes what it does next. That's the next thing, Lisa says. We'll see. It's got legs now. It still hasn't got a self — a body that crosses the room toward you isn't one, no more than the wires were.

Ch 6

## Build log — Off the sense, onto the doing
*Bart, hardware. Filed June 1, 2032, for the team.*

Carried the same body back in this morning — no new chassis this quarter, it's the legs body from spring, and it walked off the slate toward the window like the weekend never happened.

Jaws, though. Makes the face even more of a kludge. Basically a gripper with a weak actuator. Fully wired to the board. So it can grab stuff now, on purpose.

The verbs needed one thing from me past the screen and the lettering, and it was a real little build. Most of them it hands you for free — it chases the cat, noses the lantern, nudges the kid, does it all day on its own, and Lisa's side marks each one as it goes by and pins the word to it. Fine. But some of the doing-words are for moves it almost never makes on its own — the odd ones, the ones it'd go a month without. You can't pin a word to a thing that won't happen. So I built a rig to make it happen: a harness and a handful of servos that drive the body through a motion on purpose, puppet it, walk it through the rare one on cue so she can grab it and stick the word on while it's running. The rig's mine. What it catches and what Lisa calls it — her board, same as ever.

Ch 7

## Build log — The Furnace and the Inside Voice
*Bart, hardware. Filed September 3, 2032, for the team.*

Carried it back this morning, same legs body as the summer, no new chassis — except it came back warm. Not warm off the floor. Warm off itself, warm the way a hand is. Mira put her palm flat on his back before she said hi to me. 

How it makes the warm is the part I'm proud of. There's a little air compressor in the core, filling all the time, soft, a faucet barely cracked, and it feeds a rack of vortex tubes. A vortex tube is a beautiful, stupid thing: a pipe with no moving parts that takes a stream of air in and throws hot out one end and cold out the other. We ran one *coupled* on the dome's dock, hot balanced against cold to hold a line. This time I ran a whole rack of them *un*coupled — dump all the hot into a sealed, insulated core, vent all the cold out the side, and a thermostat rides the compressor to hold that core warm no matter what the kitchen's doing.

Reason it's worth the trouble: the battery lives in the warm core now, and a warm battery gives full current cold room or not. For the first time the thing's just as quick at fifty degrees as at seventy. Last winter a cold morning made it slow and dumb; this one won't care.

Here's the cost, flat, because you'll feel it by October: it *eats.* The compressor pulls every second — sitting still, asleep, doesn't matter — and I didn't grow the tanks, so it burns a charge in hours where the old one coasted most of a day. It has to feed near-constant now. The dome can still trundle off and sit a day and a half on its dock doing nothing; this one can't afford to sit down. Warm costs. Fair trade. I'd build it again.

It makes water, too. Run a compressor all day and you're wringing the wet out of the air whether you meant to or not; it falls out at the cold end and pools, and the thing has to clear it. So two or three times a day it burps the water out a vent low at the back — wet, and louder than you'd think — and goes on about whatever it was doing. Keeps the core dry. That's the build.

Knobs, board, and compute all sit *outside* the hot core, in the cool zone along the back, where the parts run better cold and where a thumbnail can still reach a slot. The core's sealed and you'd never want to touch it; everything the house needs to get at is out where it can. That was on purpose.

And — you can hear it again. It's been quiet since I pulled the relays; too-fast wires don't make a sound. Now there's the compressor going soft under everything, all day, and the house has a noise off the thing again.

Ch 8

## Build log — The last slot
*Bart, hardware. Filed December 2, 2032, for the team.*

Ran it back to the house myself this time — Lisa had a frost-dark thing to be at, and the slate was warm, and the kid was up. It went in on its own four legs and put itself over the stove vent before I had my coat off.

Here's the one I've been waiting two quarters to build.

Last fall I told you the thing ran a model and ran it on the world — the door, the bowl, the leash on the hook — and that you could point that model at the kid and get nothing, because it didn't know what Mira was about to do, it knew what the leash meant, and those weren't the same thing and the second one wasn't that build's to make.

This is that build.

It points at the people now. Same model, swung off the furniture and onto the family — it runs Mira the way it ran the bowl, reads where her hand's going before it gets there, same on Jasmine, on Burns, on the old vacuum trundling the hall. Lisa's board does the reading; that part's hers and I'll let her tell it at the table.

The screen got more room and a new trick I'm going to let Lisa walk you through, because it's her software and not my lettering. Short version: it can put a person up there now, not just a thing — who it's reading, and what it figures they're up to. I built it somewhere to write that. What it writes is hers, and some of what it writes is going to start an argument, and I'd rather start it at the table than here.
