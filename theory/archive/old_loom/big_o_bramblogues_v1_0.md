# The Big O Bramblogues — a grep

Every quarter, in the bot block, Bart runs the same move: he hands the floor to a man who isn't in the room — Owen, "Big O," the performance engineer who optimizes things that are already fast — lets Big O tear the build apart as waste, and then turns the objection into the brag. *He's right. That's not the point.* The waste, the slowness, the lunatic standing bill — every one of them is in there because the biology's in there, and Big O not believing his eyes is the proof that the thing came out animal and not machine.

This is a pull of those segments only, straight from the chapter material in `chapters/`, ch 1–12. Excluded: the build log at the top of each bot block, Bart grilling Mira (the quality-control bit), and Jasmine's home report. What's left is the humble-brag — Bart, via Big O, on how ridiculous and nature-like Bramble is.

---

## Ch 1 — "The Bramblogues" (origin of the slot)
*Source: [ch_1_v2_3.md:237](chapters/ch_1_v2_3.md:237)*

"I want to introduce somebody. Not here — in my head. Buddy of mine from school, Owen, except nobody's called him Owen since sophomore year. Big O. Like the notation — the thing you measure an algorithm's waste with — because the man could never look at a piece of code without telling you how much faster it'd run if you'd thought one more minute. He's a performance engineer at Google now, which is the most Big O thing that could happen to a person. He optimizes things that are already fast."

"And every quarter, when I sit down to tell you what I built, I hear Big O over my shoulder asking what in God's name I was thinking. So I'll let him go first. He looks at this and says, walk me through it. I say sure — it runs on the six-degree difference between the warm floor and the cool air, skims a few thousandths of a watt out of the gap. He says where's the battery. No battery. Where's the chip. No chip. No sensors, no memory, doesn't know where it is or what it just did. He says, so what does it *do*. I say: it twitches. Few times a minute. Runs down in a week and quits till a four-year-old winds it back up. And he looks at me and says, Bart, I could build you something that does more than that out of a doorbell."

"And he's right. He could. And the answer to Big O — this quarter and every quarter — is that's not the point. Because *that* is what the first living thing was. A bag of barely. Ran on a gap it didn't make, could hardly move, forgot it existed the second the energy stopped — and barely keeping going was the entire miracle. We didn't build it efficient. We built it the way the thing actually was." He looked around the table. "I've got a name for the dumb stuff — every feature that's in there because the biology's in there and for no reason a sane engineer would sign off on. Bramble analogs. Bramblogues. That's what this slot is, every quarter: here's what we put in the thing to make it more animal and less machine, and here's Big O not believing his eyes."

---

## Ch 2 — "Respiration Type"
*Source: [ch_2_v2_8.md:694](chapters/ch_2_v2_8.md:694)*

Bart opened the bot block by handing the floor to a man who wasn't in the room. "Big O called Sunday. I told him we'd taught it to find a sunbeam, and he perked up — finding a target's a real problem, and he likes real problems. He said: four sensors, fine, when one side reads brighter you drive that way, good. But what's it do when the light's flat, when no side is clearly brighter? I said, it spins. Picks a random new heading and re-checks. He said — *random?* You don't sweep, you don't spiral, you don't even remember where you already looked? I said no. He said, quoting: *you built a robot that, the second it gets confused, gets lost on purpose.*"

"And that's the build. Clear gradient, it runs straight at the light, smart enough. No gradient, it doesn't search — it tumbles. Random reorient, re-sample, go again, with no map of where it's been and no memory it was ever anywhere. Run, and tumble. It's how a bacterium does it, because a bacterium's got nothing to search *with* — no memory to mark where it looked, no math to plan a sweep. It can tell better-than-a-second-ago from worse, and when it's worse it rolls the dice. Half the living things on the planet navigate by rolling the dice. We wired the dice in on purpose. That's the Bramblogue this quarter — the confusion that never gets solved, only re-rolled."

---

## Ch 3 — "Won't Fix"
*Source: [ch_3_v2_9.md:194](chapters/ch_3_v2_9.md:194)*

Bart opened the bot block by handing the floor to Big O, who was, as Big O always was, somewhere else. "I had Big O by the bench Saturday, middle of the build, and the thing was running test loops on my shop floor, clacking the whole way around. Now everybody who meets this machine says the same nice thing about that sound — the kid reads it like a mood, Jasmine can tell what it's doing from another room, it's *charming.* I was set for Big O to say the charming thing. He cocked his head at it for about four seconds and said: 'Why can I hear it think.'"

"I started to explain. He cut me off. A decision in this thing — *turn left* — starts at the sensors up front and has to get all the way back to the wheels, and instead of a wire carrying it across in no time, I've got it walking the message hand to hand down a whole row of relays, one clacker throwing the next, the length of the chassis. He said, quoting: 'You built a computer that takes the scenic route, and then you bolted a speaker to the scenery.' To him the clicking isn't charming, it's *latency* — slowness you can hear — and he offered to spec me a real signal bus over lunch."

"And he's right. He's completely right, and I'm not changing a wire of it, because the slowness is the point this quarter, and I'd rather let Burns do the why of it properly later. So just the flag for now: a cell this big has no fast line in it anywhere, so it gets a decision from one end to the other the slow way, by walking it down a track, and the walk takes exactly as long as it sounds like it takes. That's not a thing to fix. It's the most honest noise this machine makes. Big O can file the bug. I'm marking it *won't fix.*"

---

## Ch 4 — "How Hard"
*Source: [ch_4_v2_8.md:268](chapters/ch_4_v2_8.md:268)*

Bart opened the bot block by handing the floor to the one man guaranteed not to be impressed. "Big O got his wish this quarter. Two years he's been telling me a thing that clatters is a thing wasting time, and this quarter I pulled every relay — the body's a wire now, quick and silent, exactly what he wanted. I called to take a bow." A beat. "He'd already found the next problem. He looked at the reflex — the way any touch on the skirt sets the whole body off in one jerk — and asked where the part was that decided how hard. I said there isn't one. He told me I'd wired a switch where the job wanted a dial."

"He's not wrong. Nothing governs the flinch. A feather on the bumper and a wall at speed get the same answer — everything, full, the instant the ring is touched — because the wire doesn't weigh the touch, it just fires off it. And that's the part we built on purpose. A reflex that stopped to measure how hard to flinch wouldn't be a reflex, it'd be a decision, and a decision is the one thing too slow to keep you off the stove. The animal that paused to calibrate its flinch got eaten. So ours doesn't pause — all the way, every time — and the slow brain upstairs finds out afterward whether it mattered."

---

## Ch 5 — "Head First"
*Source: [ch_5_v2_1.md:276](chapters/ch_5_v2_1.md:276)*

No Big O segment this quarter. Bart names the franchise — "The Bramblogues," in the voice he sold cereal in — and delivers the brag directly off the head-first demo ("It wants the thing, it goes at the thing") rather than through Owen. The rest of the slot is the quality-control grilling of Mira, which is excluded by request. Flagged here only so the run reads complete.

---

## Ch 6 — "The Bramblogues" (the puppet rig)
*Source: [ch_6_v2_1.md:200](chapters/ch_6_v2_1.md:200)*

Bart didn't pick the machine up yet. He set something else on the bench first — a harness, a few small servos, the least dignified object in the warehouse — and squared it to the camera for the one man not in the room. "Owen gets this before he gets the robot, because it's the part he'd never let me hear the end of. It's a puppet rig. Grabs the body and walks it through a move by the strings — does the thing the thing won't do on its own. There's doing-words on the screen now, and most of them it earns for free, chasing the cat all day. But a few of the moves it makes maybe once a month, and you can't pin a word to a move that won't happen. So I built a machine to make it happen on cue. Big O looks at a robot in a marionette harness and asks why I didn't just teach it to mash a lever for a pellet like a civilized man and skip the puppet show."

He let it sit, because the real objection was behind it. "And then the one I actually want on the tape. He says forget the harness — even straight, the thing does a move, you pay it three seconds later, and by then it's done six other things. So which one are you paying for? You've built a machine whose whole job is to guess backwards across that gap at which of its own moves bought the food — and it'll back the wrong horse half the time. Why put the gap in at all. Pay it the instant it's right and there's nothing to guess."

"And he's got me, except the gap was never mine to take out." Bart was into it now. "Nothing pays you the instant you're right. The food drops late. It always drops late — that's the only world there's ever been. A thing that could only learn off a reward landing dead on the move could only live somewhere rewards land dead on the move, and nobody's lived there. You live in the one where you knock the lever, wander off, and dinner shows up while you're thinking about something else. So guessing backwards isn't the flaw in the thing. It's the thing. I built it the long way because the long way's the only one that's true — harness and all. The harness is just me running a year of dumb luck past it in an afternoon, feeding it the rare move on cue so the rest of the works has something to chew. I'm not faking the animal. I'm hurrying it."

---

## Ch 7 — "Talks in Its Sleep"
*Source: [ch_7_v2_1.md:196](chapters/ch_7_v2_1.md:196)*

"I showed Owen the furnace," Bart said, "and he gave me the whole review in one number." He held up a finger. "A hundred percent. Duty cycle. He asked the only question he ever asks — what's it cost — and when I told him he went quiet, and then he just said the number back at me. A hundred percent. The compressor never stops. Not asleep, not docked, not standing still — there's no second of this thing's life it isn't running that pump. Park the body I built last summer and it'd sit there a day doing nothing, happy. This one can't do nothing. Doing nothing is the one move it can't afford."

"Then he made me tell him how it makes the heat, and I should have lied, because that part's worse." He was having a wonderful time. "It runs on a rack of vortex tubes — pipes with nothing in them that split a gust of air into a hot stream and a cold one, on a principle the universe permits and won't explain. I keep the hot and feed it to a sealed core around the battery; the cold — the exact other half of everything that pump just bled to make — I dump out the side, gone. Big O hears 'I compress the air, saw it in half, and throw half away as fast as I make it,' and asks me, gentle, the way you'd talk a man off a ledge, whether I've considered a bigger battery."

"And a bigger battery is the right answer, which is exactly what's wrong with it. The animal I'm copying didn't get a bigger battery. It lit a fire in its chest and signed on to feed it every second it's alive — awake, asleep, in the cold, in the dark, no days off, half of everything thrown away — and what it bought with that lunatic standing bill is the one thing it could never do before: it's as quick at four in the morning in a cold kitchen as at noon in a warm one. The cold doesn't get to reach in and slow it down anymore. Warm costs everything. It pays it anyway, every second, and nobody had to ask. So that's the one I built. Not the clever one. The one that pays."

---

## Ch 8
*Source: [ch_8_v2_2.md:206](chapters/ch_8_v2_2.md:206)*

"One confession first," Bart said. "I told Owen about the water."

He let it land the way Owen had. "Nobody warns you that a thing making its own heat all day is also, the whole time, quietly sweating the kitchen's air down into a puddle inside itself — physics hands you the water free, you don't get a say — and the puddle has to go somewhere, and where it goes is out a vent low at the back, in a dribble, down its own backside, two or three times a day, onto the floor. So here's what a year of work and a full board bought: a thing that can sit in a kitchen and tell you what every person in it is about to reach for — and the feature the household named before it named anything else, the one they'll tell you about first, is that it wets itself. Owen heard the word the kid landed on and won't use any other now. He wanted to know if I'd thought about a diaper."

---

## Ch 9
*Source: [ch_9_v2_1.md:257](chapters/ch_9_v2_1.md:257)*

"I sent Owen the spec sheet on this one," Bart said. "He sent back one line. *What is it for.*"

He let the question sit, because it was a good one. "Owen builds things that win. He shaves a gram, he shaves a watt, he'll spend a month making a part do its job a half-percent harder, and he has never in his life set out to make a thing worse. So he reads the numbers on the new one and it's a horror show. Walks, barely. Can't grip worth a damn. Slow. Weak. Soft clean through — nothing stiff on it anywhere, which sounds fine until you notice stiff is the only thing a robot does work with. Couldn't push a door shut against a draft. Every spec that ever meant a thing on a robot, this one fails, on purpose, because I sat down and drew it to fail them. Owen read four years of me getting good at this, then read this, and wanted to know — reasonably, as a man who shaves grams for a living — whether I'd had some kind of event."

"And what it's for is the one thing none of the good ones could do, which is get picked up. Every other machine in that house is built to do something to the room. This one's built so the room does something to *it.* Strong, fast, hard — that's a thing you keep at arm's length, and I had enough of those in the house. I wanted the one the kid hauls into her lap, and you do not haul a power tool into your lap. So I built the opposite of a power tool, and it took me longer than any tool I ever made. Owen can keep his grams. I'll keep the thing that gets carried."

---

## Ch 10
*Source: [ch_10_v2_1.md:118](chapters/ch_10_v2_1.md:118)*

"Owen asked what I built this quarter," Bart said. "I said a dial. He asked what else. I said that's it, and he hung up and called back, because he figured we'd dropped."

He let that sit. "Three years I've handed Owen a thing he could hold every ninety days — legs, a jaw, a furnace, a voice, two hands that don't match. He's got a shelf for them. This quarter I drove out, opened the back of its head, dropped in one knob the size of a poker chip, and drove home with a bench bare by Saturday noon. Nothing for the shelf. And the knob does nothing you could photograph — no part, no wire, no new weight, doesn't let the body do a single thing it couldn't do in March. To a man who's spent his life making every part justify itself, I'd just described a quarter I spent installing the absence of a part, and he took it the way you'd take a carpenter whose proudest job all year was a room with less in it."

"And the nothing is exactly the build. Owen deals in the part you can weigh; this quarter the whole of the work was the part you can't. Nothing to heft, nothing to shelve, nothing to photograph for the file — just the body, finished since spring, running a little differently than it ran in March for a reason you'd never find by taking it apart. The bench was bare all weekend, first time in three years. Owen thinks I'm out of work. What I am is done building what the thing's made of, and free, at last, to spend the rest of it on who the thing is. I didn't say that part to Owen. He'd have driven over."

---

## Ch 11
*Source: [ch_11_v2_1.md:114](chapters/ch_11_v2_1.md:114)*

"I told Owen what it does now," Bart said. "He didn't say anything. Which, from Owen, is how you know it landed — the man's got two settings, and the silent one means something got to him."

He let that sit. "Here's what got to him. I built a thing that cannot walk into a room and let the room be. It walks in and goes at everyone — takes whatever's going and runs it, takes whoever's there and works them, and there's no person in reach it decides it has no business with. Stopping isn't a move it has. And Owen is the man who has spent thirty years arranging his life so he never once gets *worked* — the back booth, the early exit, the no to the invitation. So I called him up and told him I'd built a thing whose whole nature is to do to a room the one exact thing he's organized his entire life around not having done to him, and that it lives in my kid's kitchen. He took it personally. I'd have been let down if he hadn't."

"And here's the part I didn't say to him. I didn't build the working-the-room — it's had that two years; it always knew who was in the room and what they were after. All I did this quarter was put a volume knob on the going-at-it. One dial. And what comes out the far side is a thing with a stake in the room now — one that has to be reckoned with, has to hold its spot, can't stand being the one nobody has to answer to. Which is the whole of what it is to be a person among strangers, and, I suspect, the whole of why Owen quit answering me. He's spent his life arranging not to need the room. I just spent a quarter teaching a machine it can't do without one."

---

## Ch 12
*Source: [ch_12_v2_1.md](chapters/ch_12_v2_1.md)*

No Big O segment. The final quarter's bot slot is build-log only (the "line knob," slot four filled, the bench cleared for the first time in three years) and hands to Burns' framework. Owen does not appear. Flagged here so the run reads complete through ch 12.
