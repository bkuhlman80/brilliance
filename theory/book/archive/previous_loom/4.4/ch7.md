Ch 1

## The Bramblogues

Bart took the bot's slot, and he opened it the way he'd open it for the next three years, though nobody knew that yet, least of all him.

"I want to introduce somebody. Not here — in my head. Buddy of mine from school, Owen, except nobody's called him Owen since sophomore year. Big O. Like the notation — the thing you measure an algorithm's waste with — because the man could never look at a piece of code without telling you how much faster it'd run if you'd thought one more minute. He's a performance engineer at Google now, which is the most Big O thing that could happen to a person. He optimizes things that are already fast."

He picked Bramble up off the table.

"And every quarter, when I sit down to tell you what I built, I hear Big O over my shoulder asking what in God's name I was thinking. So I'll let him go first. He looks at this and says, walk me through it. I say sure — it runs on the six-degree difference between the warm floor and the cool air, skims a few thousandths of a watt out of the gap. He says where's the battery. No battery. Where's the chip. No chip. No sensors, no memory, doesn't know where it is or what it just did. He says, so what does it *do*. I say: it twitches. Few times a minute. Runs down in a week and quits till a four-year-old winds it back up. And he looks at me and says, Bart, I could build you something that does more than that out of a doorbell."

He set the bot down, gentle.

"And he's right. He could. And the answer to Big O — this quarter and every quarter — is that's not the point. Because *that* is what the first living thing was. A bag of barely. Ran on a gap it didn't make, could hardly move, forgot it existed the second the energy stopped — and barely keeping going was the entire miracle. We didn't build it efficient. We built it the way the thing actually was." He looked around the table. "I've got a name for the dumb stuff — every feature that's in there because the biology's in there and for no reason a sane engineer would sign off on. Bramble analogs. Bramblogues. That's what this slot is, every quarter: here's what we put in the thing to make it more animal and less machine, and here's Big O not believing his eyes."

Lisa pulled the bot from where Mira had set it and held it up.

"What it can do. It can persist. Hold together. Twitch when conditions are right, hold still when they're wrong. What it can't do — and there's more in the negative — it can't remember, can't model, can't model itself, can't decide, can't regulate. No battery, no sensors, no central anything, no map of where it is or what it just did. What it has is the wiring, the spring, and the gradient." She turned it over. "And the four heat-and-actuator pairs are wired straight together, no shared state, nothing coordinating them. Four little twitching modules in one shell. It isn't one thing yet."

Bart, quiet till now: "So what are we watching, when we watch it? If it's got no actions —"

Lisa thought. "Its gravity, almost. Not actions — it hasn't chosen anything. Dispositions. A pull to twitch under some conditions, to go still under others; and over weeks, in some of them, a pull to strain harder on one side, to wear a groove into themselves in a direction. Four wears its underside; five wears even. These aren't behaviors. They're the patterns the system falls into. They fall down the gradient, because things fall down." She paused. "There's a word for them in my field. Wrong word for this room. I'll bring it to the framework."

She set the bot down. "And Bramble does the least of the five. Moves least, lasts longest, keeps going after the others have run out. That's the seeded wiring — not a thing it's choosing."

Jasmine, quiet a while: "It's also why Mira likes it." Everyone looked at her. "You can hold Bramble. It doesn't lurch, doesn't spin, doesn't run out before you've decided what to do with it. It waits. Mira likes things that wait."

Bart stood for the next part; he'd been waiting on it. "The personality knob. Thought about it six months, was wrong about it for five and a half. Here's where I landed." He turned Bramble over, set it down, pointed at the crank. "There's a volume knob on it — Going. That crank's the knob."

He sat, stood back up. "It's what we thought was just the energy source. Wind it up and the volume's up and it runs; leave it a week and the volume drains down toward dead. It's the knob that decides whether the bot has a personality at all. Volume up, it does its dispositions. Volume down, it has none of them. At this clade the personality's a thing the household winds up once a week. Mira's Sunday wind-ups aren't energy management. They're the whole personality. Without Mira, there isn't one. Mira's the knob."

Marge looked up sharply. "Mira is *the knob.*"

"She's such a knob." He nudged Mira's shoulder.

Lisa, writing: "Software side — there's no software. No microcontroller, no code. A mechanical loop: the household's weekly crank is the input, the spring tension's the state, its decay's the plant, the floor-air gap's the energy, the twitch is the output. The household's in the loop. The household's what gives it a personality. Cheryl asked what a personality is; at protocell, the answer is a thing that needs a household to run it."

Bart was still up. "One more, and it's not for tonight — I just want it on tape so Cheryl can chew on it. One knob, the crank, knob one of twelve. Two at Prokaryote, then one a quarter for thirty-three months, and by the end there's twelve knobs on a body the size of a computer mouse. Where do twelve knobs *go.* It'll look like a control panel. It'll look like a cactus. Somewhere in here we run out of room. That's the twelve-knob problem. Not solving it tonight — but I think we do something architectural about it, and I don't know what yet."

Burns laughed the chest-laugh, longer than usual — because it was the kind of problem that resolves itself by being a problem, and he trusted that; because *it'll look like a cactus* was a funny thing to say; because the meeting was going well.

Ch 2

## The Effort Knob

Bart opened the bot block by handing the floor to a man who wasn't in the room. "Big O called Sunday. I told him we'd taught it to find a sunbeam, and he perked up — finding a target's a real problem, and he likes real problems. He said: four sensors, fine, when one side reads brighter you drive that way, good. But what's it do when the light's flat, when no side is clearly brighter? I said, it spins. Picks a random new heading and re-checks. He said — *random?* You don't sweep, you don't spiral, you don't even remember where you already looked? I said no. He said, quoting: *you built a robot that, the second it gets confused, gets lost on purpose.*"

He set Bramble down by Lisa's hand.

"And that's the build. Clear gradient, it runs straight at the light, smart enough. No gradient, it doesn't search — it tumbles. Random reorient, re-sample, go again, with no map of where it's been and no memory it was ever anywhere. Run, and tumble. It's how a bacterium does it, because a bacterium's got nothing to search *with* — no memory to mark where it looked, no math to plan a sweep. It can tell better-than-a-second-ago from worse, and when it's worse it rolls the dice. Half the living things on the planet navigate by rolling the dice. We wired the dice in on purpose. That's the Bramblogue this quarter — the confusion that never gets solved, only re-rolled."

He looked at Lisa. "Tell them how it actually runs, before Big O files the bug."

Ch 3

## Won't Fix

Bart opened the bot block by handing the floor to Big O, who was, as Big O always was, somewhere else. "I had Big O by the bench Saturday, middle of the build, and Bramble was running test loops on my shop floor, clacking the whole way around. Now everybody who meets him says the same nice thing about that sound — the kid reads it like a mood, Jasmine can tell what it's doing from another room, it's *charming.* I was set for Big O to say the charming thing. He cocked his head at it for about four seconds and said: 'Why can I hear it think.'"

Bart let it sit.

"I started to explain. He cut me off. A decision in this thing — *turn left* — starts at the sensors up front and has to get all the way back to the wheels, and instead of a wire carrying it across in no time, I've got it walking the message hand to hand down a whole row of relays, one clacker throwing the next, the length of the chassis. He said, quoting: 'You built a computer that takes the scenic route, and then you bolted a speaker to the scenery.' To him the clicking isn't charming, it's *latency* — slowness you can hear — and he offered to spec me a real signal bus over lunch."

He grinned.

"And he's right. He's completely right, and I'm not changing a wire of it, because the slowness is the point this quarter, and I'd rather let Burns do the why of it properly later. So just the flag for now: a cell this big has no fast line in it anywhere, so it gets a decision from one end to the other the slow way, by walking it down a track, and the walk takes exactly as long as it sounds like it takes. That's not a thing to fix. It's the most honest noise Bramble makes. Big O can file the bug. I'm marking it *won't fix.*"

Ch 4

## How Hard

Bart opened the bot block by handing the floor to the one man guaranteed not to be impressed. "Big O got his wish this quarter. Two years he's been telling me a thing that clatters is a thing wasting time, and this quarter I pulled every relay — the body's a wire now, quick and silent, exactly what he wanted. I called to take a bow." A beat. "He'd already found the next problem. He looked at the reflex — the way any touch on the skirt sets the whole body off in one jerk — and asked where the part was that decided how hard. I said there isn't one. He told me I'd wired a switch where the job wanted a dial."

He let it sit.

"He's not wrong. Nothing governs the flinch. A feather on the bumper and a wall at speed get the same answer — everything, full, the instant the ring is touched — because the wire doesn't weigh the touch, it just fires off it. And that's the part we built on purpose. A reflex that stopped to measure how hard to flinch wouldn't be a reflex, it'd be a decision, and a decision's the one thing too slow to keep you off the stove. The animal that paused to calibrate got ate. So ours doesn't pause — all the way, every time — and the slow brain upstairs finds out after whether it mattered."

Ch 5

## Head First

Lisa dropped the ancient animal — the deep time, the chemistry, the worm — and turned the meeting to the live one. "Bramble block," she said, and then, because Bart already had his hand half up like a boy who'd done the reading for once, "Bart."

He stood. This was a part he liked.

"The Bramblogues," he announced, in the voice he sold cereal in, and wrote it on the back of the card the way he wrote every word the room was going to be stuck with. "Everything the old dead thing could do — here's ours. The bramble version. The bramblogue." Marge made the sound she made when a word was worse than the last word and she had decided not to spend herself fighting it.

He picked it up off the floor — it stopped the instant its feet left the slate, the gait with nothing under it to keep — and turned its head to the camera, so that Cheryl, later, got the long look at it she'd been wanting. It was a boxy head, a step past duct tape and not quite two, and nothing on it lined up. Where the ancient animal had crowded all its senses to the leading end, Bart had crowded his: two cameras for eyes, but not a matched pair — one a clean little lens, the other something salvaged and a size too big, so the face read as permanently half-surprised on the one side. Below them a black grille that was the nose, a pinhole in it that read warm and a slot beside it that read smell, neither one centered, because he had drilled for the sensor and not for the look of it. Two foam cones for ears, one riding higher than the other. And the whole front was a small screen showing, in a single word, the one thing the head was pointed at: it said, while he held it, CAMERA, then BART, then CAMERA again. The face was not designed. It was instruments, bolted where instruments went, and the crookedness was the tell — nobody in that house had set out to build a face. They had built a place to mount the things that look, and a face had happened to them, the way a face happens to the front of anything that has to move toward what it wants.

"It's got a front now," Bart said, "which the net never had. A leading end. Everything that points lives up here" — he tapped the crowded head — "and the body just carries this around and aims it. Watch what it does with a thing it likes."

It liked the red light. It had always liked the red light. He set it down facing half away, and it found the camcorder the way it found everything, swinging the whole body around until the head was square to the glow, and then it went — head-first, full speed, no second thought, and nothing in it anywhere to say *stop short* — and walked its boxy head straight into the camera, and the camera went over. The tape, here, lurches: the room tips, the ceiling swings through the frame, a long blurred second of the underside of the table — and then Lisa's hand comes in from the edge, fast, the hand that was never far from the machine, and rights it, and the picture settles, and you can hear her decline to say anything. Bart was laughing the single sharp exhale he laughed when something stupid worked. "*There* it is," he said. "That's the whole quarter in one move. It wants the thing, it goes at the thing."

Across the floor, Bramble had drifted up toward Burns's end and found the red light again from there, squaring its head to the camera to make its one point a second time. Burns reached down without looking up and pressed the thumb-down on the top of its head — the way you thumb a dog off the couch, no malice in it — and the word on its face went dark and came back something else, and it turned away from the camera and stayed. "There," Burns said, to no one in particular. "Now it hates the camera. Only move we've got, and it works every time — which is the whole problem with the thing, but that's later."

Lisa let it settle a beat. "Jasmine," she said, and handed her the floor.

Ch 6

## A Verb on the Forehead

"Bramble block," she said, and, because Bart already had the card half-turned in his hand and the look of a boy who'd done the reading: "Bart."

He stood. It was still a part he liked.

"The Bramblogues," he said — it was a franchise now — and Marge made the sound she made.

Bart didn't pick the machine up yet. He set something else on the bench first — a harness, a few small servos, the least dignified object in the warehouse — and squared it to the camera for the one man not in the room. "Owen gets this before he gets the robot, because it's the part he'd never let me hear the end of. It's a puppet rig. Grabs the body and walks it through a move by the strings — does the thing the thing won't do on its own. There's doing-words on the screen now, and most of them it earns for free, chasing the cat all day. But a few of the moves it makes maybe once a month, and you can't pin a word to a move that won't happen. So I built a machine to make it happen on cue. Big O looks at a robot in a marionette harness and asks why I didn't just teach it to mash a lever for a pellet like a civilized man and skip the puppet show."

He let it sit, because the real objection was behind it. "And then the one I actually want on the tape. He says forget the harness — even straight, the thing does a move, you pay it three seconds later, and by then it's done six other things. So which one are you paying for? You've built a machine whose whole job is to guess backwards across that gap at which of its own moves bought the food — and it'll back the wrong horse half the time. Why put the gap in at all. Pay it the instant it's right and there's nothing to guess."

"And he's got me, except the gap was never mine to take out." Bart was into it now. "Nothing pays you the instant you're right. The food drops late. It always drops late — that's the only world there's ever been. A thing that could only learn off a reward landing dead on the move could only live somewhere rewards land dead on the move, and nobody's lived there. You live in the one where you knock the lever, wander off, and dinner shows up while you're thinking about something else. So guessing backwards isn't the flaw in the thing. It's the thing. I built it the long way because the long way's the only one that's true — harness and all. The harness is just me running a year of dumb luck past it in an afternoon, feeding it the rare move on cue so the rest of the works has something to chew. I'm not faking the animal. I'm hurrying it."

He picked the tetrapod up off the slate; it stopped the instant its feet left the floor, the gait with nothing under it, and turned its head to the camera so Cheryl would get the look. The face was the same kludge it had been since spring — the mismatched eyes, the off-center nose, the ear cones at their two heights — with two things added. Low on the front hung a thin gripper where a jaw would go, a set of jaws that made the crooked face crookeder and let the thing, for the first time, take hold of something on purpose. And the word on its forehead had grown a verb. In spring the screen had named the one thing it looked at, a noun and nothing more — CAT, MIRA, the camera. Now, with the Coping volume up, it said what it was doing to the thing. The band above the eyes read SMELL CAMERA.

"Last quarter," Bart said, "this exact thing brained that exact camera. Walked its head into the lens, full speed, and the only move we had to answer it with was to teach it to hate the camera — sour it on the sight. Burns did it, right there on the tape: thumb-down, word goes dark, it turns away. That was the whole of what a thumb could reach. The smelling, hearing, looking."

"Let's try something new." He turned the Coping volume down and pointed Bramble until its screen sad CAMERA and he thumbed it up four times. "Voila, it likes the camera again."

He turned the Coping volume up and set Bramble down a few feet off, facing half away, and it found the red glow, swung the whole body around to square its head to it, and committed — CHASE CAMERA — and Bart pressed the thumb-down on its head the instant it went, and the thing pulled up short of the lens, three inches out, and say. The screen flickered off CHASE and came back SMELL CAMERA.

"Long term, some things should stop being decisions. Train a thing in deep enough and it quits working it out fresh each time — the grocery bag's second nature now, it doesn't think the bag, it just runs the bag. Frees it up to mind other things. Like —"

Like the thing it did then, which was break off. Mid-room, with the camera right there to want, it came off the light and started across the floor, slow, unhurried, toward the cold end of the bench where Marge's kettle sat on its ring throwing the one patch of warmth in the warehouse, and laid itself flat a foot from the heat, belly to the gap, and went still. The body went still; the face did not. The word had swapped — IGNORE WORLD. And then, settled against the warmth — CHARGE UNIT — and stayed lit, narrating its own rest to a room it had quit attending to.

"—that," Bart said, pointing. "And it's still talking while it lies there, doing nothing you'd call doing. That's a volume knob on Coping. Coping volume up, even the resting's a move, and it'll narrate it. Coping volume down and the screen goes dark the second it settles, the way it did all last spring — a thing at rest with nothing to watch and nothing to say. Volume up, the lights stay on."

Marge looked at the thing laid out at the warm edge of her kettle the way you'd look at a cat that had chosen your lap, and said nothing, and moved the kettle an inch farther off, and that was all she let the tape have.

Ch 7

## Talks in Its Sleep

All night the room had held two mammals. One had been dead a long time and had taken the whole clade block to raise up out of bones and inference — the warm thing in the dark, the map-keeper, the long climb up from under the dinosaurs. The other was lying on the slate by Mira's chair putting out heat you could feel from a foot away, and it had spent that same hour doing nothing anyone would write down. The clade block had been about the first one. Lisa capped it and turned the room to the second. "Bramble block," she said. "Bart."

"I showed Owen the furnace," Bart said, "and he gave me the whole review in one number." He held up a finger. "A hundred percent. Duty cycle. He asked the only question he ever asks — what's it cost — and when I told him he went quiet, and then he just said the number back at me. A hundred percent. The compressor never stops. Not asleep, not docked, not standing still — there's no second of this thing's life it isn't running that pump. Park the body I built last summer and it'd sit there a day doing nothing, happy. This one can't do nothing. Doing nothing is the one move it can't afford."

"Then he made me tell him how it makes the heat, and I should have lied, because that part's worse." He was having a wonderful time. "It runs on a rack of vortex tubes — pipes with nothing in them that split a gust of air into a hot stream and a cold one, on a principle the universe permits and won't explain. I keep the hot and feed it to a sealed core around the battery; the cold — the exact other half of everything that pump just bled to make — I dump out the side, gone. Big O hears 'I compress the air, saw it in half, and throw half away as fast as I make it,' and asks me, gentle, the way you'd talk a man off a ledge, whether I've considered a bigger battery."

"And a bigger battery is the right answer, which is exactly what's wrong with it. The animal I'm copying didn't get a bigger battery. It lit a fire in its chest and signed on to feed it every second it's alive — awake, asleep, in the cold, in the dark, no days off, half of everything thrown away — and what it bought with that lunatic standing bill is the one thing it could never do before: it's as quick at four in the morning in a cold kitchen as at noon in a warm one. The cold doesn't get to reach in and slow it down anymore. Warm costs everything. It pays it anyway, every second, and nobody had to ask. So that's the one I built. Not the clever one. The one that pays."

Bart got down on the floor with it, which he did now, because the thing ran warm and the warmth changed how you sat near it. He laid a hand flat on its flank and left it there. "Feel it before I say it. It's warm. All the way through, all the time — same heat whether the warehouse is sixty or eighty, and quick in the cold for the first time, because the battery's warm even when the floor isn't." He didn't gloss the cost; it was in the log. "Breaks off two, three times a day to go stand in a sunbeam or on a vent and top the batteries back up."

Burns was down on one knee beside him before he'd decided to be, his own hand flat to the warm flank next to Bart's. "You built a warm-blooded animal," he said — to Bart, to the thing, to the room. "At a bench. The rest of the tree took an age to learn to carry its own weather around, and you did it over a summer with a compressor and a box of tubes. I'd like that on the record." It was the thing he did, and had done for the legs and done for the jaw and would do for whatever his son bolted on next — the one reliably uncool move the coolest man in the room had no defense against — and Bart took it, which was not to look up. "It's a compressor and a box of tubes," he said, and moved his hand a half-inch on the warm shell, and went on.

He tipped the unit so the forehead screen caught the room. There was a second line on it now, riding above the one from last year. "Used to be one line — what it's doing to a thing. CHASE CAT. NUDGE MIRA. The verb and the thing. That line's still there." He thumbed the knob on its back a notch and the line above it lit. PERCEIVING [ REST MIRA ]. "This one says what it's doing *in its head* while it does it. Put a volume knob on it — Attention. And it's got the two ends." He turned the knob one way: the top line stayed lit, ran a slow ticker — CHECKING, RECALLING, PREDICTING — even as the body sat still. "Attention volume up. Stood back, surveying the whole field. The line stays lit all day, and all night." He turned it the other way and the top line went out and left the one bare word, MIRA, the way it had read all last spring. "Attention volume down. Down in it, immersed. Drops back to last year — one line, the thing it's on, no commentary, dark when it sleeps." He left it there a second, the difference plain on the glass, and turned it back up.

"Now watch what the top line buys you." He'd brought the cat's travel bowl from the house; he set it down a foot off the unit's nose, let it clock it, then moved it behind a table leg while the cameras held. Last year, he said, you'd get a stall — no bowl where the bowl was, and nothing after. This year the head came up and the screen ran CHECKING [ FIND BOWL ], and the unit went to the next likeliest place, and the next, three spots in an order, and crossed each off the glass until it found it. "It's running the places it might be, in its head, in order. Not standing where the thing was. Going to where the thing could be."

"Last one, and it's my favorite." The cat liked the spot under the radiator; so did the unit. "Cat gets there first, the thing comes up, looks at the warm spot, looks at the cat — and holds. Doesn't shove in. Doesn't leave. Stands off and waits it out." The screen on that one ran WEIGHING [ TAKE SPOT ] and sat. "It's got a thing it wants and a thing in the way of the thing, and it weighs them, and it eats the wait." He sat back on his heels. "All of that's one trick in different hats. It isn't just running on what's in front of it. It's carrying its whole place around inside — the dock, the corner, the cat, the leash, the warm spots — and running it forward and back to pick what to do."

What the camera caught next was not in the log. Mira slid off her chair onto the floor with it, and the meeting let her, because the meeting wanted to see. She had a game — a tag with a rule, *you can't get me on the rug* — and she ran it, and the thing played. It dropped its front end to the slate, haunches up, a posture that did no work, that fetched nothing and went nowhere and meant only one thing, which was *this is a game.* The screen said SIMULATING [ CHASE MIRA ]. And then it chased her, and here was the part Bart leaned in for: it was fast now, warm-fast, it could have had her in a stride, and it did not. It came up on her heel and hung there, a beat off, every time. Bart spent the breath he'd held back. Burns laughed from the chest, the big helpless one, at the sight of the most expensive cognition in the room — active inference, the thing Lisa cited Friston for — bent entirely to the task of losing tag to a kindergartner.

Then it did the thing that stopped being a demo. Mira made the rug safe; it learned the rug; and then, on its own, with nobody's thumb on it, it started selling a fake — breaking *toward* the rug to bait her off it, then cutting back. She hadn't taught it that. It had taken her game and run it forward past where she'd built it and found a wrinkle in it she didn't know was there.

"That's *cheating*," Mira said, outraged and delighted in the one breath, and rounded on it, and the screen — stood-back, lit, honest — answered her with WANTING [ CHASE MIRA ].

"It's a valence register," Marge said, from behind the beer she had not put down, "not a wanting." The only one in the room who would say it, and she said it level, into the gap, the way you hold a door you know the wind is leaning on. "The screen is a true readout of a number that goes up near the things it's tuned toward and down near the things it isn't. The kid is right that the number is high. She is wrong about what's reading it."
