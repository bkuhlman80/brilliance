Ch 1

## Build log — Five units, out the door

And none of it happens unless you wind it up first. The crank arms a little escapement — call it the part that gives each kick permission to fire. The heat's the muscle; the crank's the say-so. This is the Going knob — Lisa's word — and it's a volume knob you wind up: wind it and Going volume's up and the unit's alive; leave it slack and Going volume's down and it sits dead on a warm floor all day. And every flinch nibbles a notch off its tension, so across about a week of kicking the Going volume drains down and it quits until somebody winds it again — six turns of the key, about a week of running. Takes both, is the point: Jasmine's floor to move it, the Going knob wound up to let it. Lose either and it's a paperweight.

I still haven't worked out how the personality knob reads here. Contract says every robot's got one, and so far all I've got is a crank — and I keep wanting to treat it like it's just on or off, you crank it or you don't. But it isn't: wind it and it drains back down through the week, so it's a volume that runs from full up to all the way down and every day a notch lower. That's a knob, same as any other's going to be — just a volume knob on how much the thing goes. I haven't got the name for what it's the volume of yet. I will.

Ch 2

## Build log — Knob two, one unit up
*Bart, hardware. Filed June 2, 2031, for the team.*

It's getting crowded down there, though — two knobs now, plus a screen, panels, a converter, sensors round the seam, and I've still got ten knobs to find room for. And hopping's a lousy way to travel: it gets where it's going, but it lurches the whole way. I've got a fix in mind for next quarter.

## Part of Something

Lisa moved them on.

"Knob two. Bart, you start."

Bart stood. He had been sitting. He picked up Bramble — Mira gave it up without ceremony — and turned it so the second knob faced the team.

"The knob has been on Bramble for ten weeks. Nobody has been calling it the *commission's knob*. I put a volume knob on it — Effort. One knob. Effort volume down runs him off the slow battery — the long even crawl, aerobic, the mechanism. Effort volume up runs him off the supercap — the burst, then the sit-and-refill, anaerobic. One store or the other; turning the knob hands the spending from one to the next."

He turned the Effort volume up to anaerobic and Bramble wiggled nearly out of his hands. Bart turned it back down to aerobic. The screen blinked once during the swap and returned to STOP.

"That is the knob. That is genetic knob two."

He set Bramble down.

"What matters in this segment is that this knob is the same *shape* as knob one — the same shape they'll all be. A knob does the one thing: up and down, and the whole way between. The crank's only quirk is that its volume slides down on its own across the week, so the household winds it back up; this one you set and it stays put. I spent a month sure the crank was a different *kind* of control. It isn't."

He gestured at the new knob.

"This one you turn up or down, and Bramble holds it there until the household moves it. That's the whole of the difference between the two — not the shape of the knob, but what its volume is the volume *of.*"

He paused.

"Two knobs, one shape, and it'll be one shape all the way out — twelve volume knobs on a board, each the volume of a different behavior. Cheryl asked whether the knobs would all be the same, and the answer's coming back yes: the same knob every quarter, up and down, only ever a new thing riding it. Knob one is the volume of *going* — whether the thing runs at all. Knob two's the volume of how it spends the running. Knob three's going to be the volume of something else, and so on down to twelve."

He sat down. 

"Software side. The Effort knob's setting is one bit of information. Aerobic or anaerobic. The microcontroller reads it at startup and on a change interrupt — Bart wired the interrupt so the FSM doesn't have to poll. But the bit doesn't touch the FSM at all. The seeking logic is identical either way: same sensors, same RUN, TUMBLE, STOP, the same light gradient computed the same way. What the bit selects is downstream of the decision to move — which store the power governor draws from when Bramble acts. Aerobic, it pulls a capped sustained current off the battery. Anaerobic, it dumps the supercap and then throttles to nothing until the battery has topped it back up. Bramble decides where to go the same way regardless. The knob decides how he pays for going."

She paused.

"That is the knob."

She looked at the room.

"Bart."

Bart said, "Yes."

"You can do the worry."

Bart stood. He had sat down for a stretch of about three minutes. He stood again.

"OK. The worry I have been carrying since last quarter... Alone." He put up his finger and gazed at the camera and the narrator heard herself discharge the Burns laugh. 

"I want to sharpen the worry, and then I want to say what I have been doing about it, which is so far not much."

He looked at Burns. Burns nodded.

"Two knobs in, and they're one shape — same as all twelve will be. The two knobs together take up about — counting the surfaces — about six square centimeters of chassis real estate. That is not a problem yet, because the chassis is six and a half centimeters across at the widest and these are the only two knobs on it. By knob twelve, the surfaces are — if we keep the same form factor for each knob — about thirty-six square centimeters. We cannot fit thirty-six square centimeters of knob on a creature. We are going to need an architectural answer to *where the knobs go* and we don't have one."

He looked at Lisa.

"I feel like Lisa has something."

Lisa groaned, "I have part of something. Not the whole something."

She pulled a small sheaf of paper from the canvas bag at her feet. The top page was a sketch. She did not pass it around. She held it up so the room could see the shape and then she set it back down on her own side of the table.

"Here is the part I have been designing. It's a memory board. A small physical addition that will fit on the next chassis. The board has four slots. Each slot can hold one knob. The board is designed to learn how the knob is worked by its environment, and once it has that learned, the knob's function can migrate to the board."

Bart said, "Wait, what."

Lisa said, "Once the board has learned the knob's function, Bramble no longer has to carry the knob. The knob can be — retired."

She let the word sit.

"The board should fix your real estate problem. Knobs that retire don't take up surface area."

Bart looked at her. Lisa looked at him.

"You're working on something bigger."

"I'm working on something."

"What."

"I don't have it yet."

"What is the shape of it."

"I don't have the shape yet."

"Lisa."

"Bart."

"You have a sketch. You just put a sketch on the table that was the wrong sketch. You have another sketch in the bag."

Lisa looked at the bag. She looked at Bart. She looked at the room.

"I have something I have been chewing on. I don't want to show it. It isn't ready. If I put it on the table now we will spend the meeting on it and it is not — I do not have it where I can put it on a table yet. I want to keep chewing. I would like to chew with you. I would like to spend the next quarter working on it with you, off-record, between meetings, not in front of the room. If we get somewhere by the quarter after we put it on the table then. If we don't, we don't, and I keep chewing."

Bart said, "You're sure."

"I'm sure."

"I won't push."

"You can push at lunches. You can't push here."

"OK."

He looked at the board sketch on Lisa's side of the table. He did not pick it up.

"The board is good. The board solves the real-estate piece. I will take the board. We co-pitch the board itself when it installs. Bart-side I will be sizing the board's slots for whatever the form factor of the migrated knob is. Lisa-side, you are doing the migration logic — how a knob's function moves from chassis-surface to slot-on-board."

"Yes."

"OK. And you and I are going to work on the bigger thing between meetings."

"Off the record."

"No whiteboard at the meeting."

"Nothing in the room."

He paused.

"OK."

He sat down. He had been standing for the worry-sharpening and the board-pitch and the back-and-forth. He sat down now. Burns watched him sit. Burns had not said anything across the back-and-forth. Burns had, halfway through, set both his palms on the table flat, and had kept them there. He kept them there now. The palms-flat-and-still was, for Burns, a way of being in a room where he was not the engine of the room. He had spent the back-and-forth letting Bart and Lisa run it. He had, at no point, stepped in to laugh it off.

Cheryl was on tape. The tape had it.

Lisa said, "Five-minute break before the Trellis block. Stretch."

She turned off the camcorder. The red light went out.

The room moved. Bart picked up the schematic from Lisa's side of the table and looked at it without saying anything. Marge got up and turned on the kettle. The kettle had not been on yet. The water started to make the small ascending sound. Burns went to the door of the warehouse and propped it open with the wooden wedge the team kept by the door for this purpose; the warehouse had cooled across the meeting and Burns wanted air. Jasmine slid off her stool and stretched. Mira stayed in her seat with Bramble in her hand. The screen read STOP. She did not turn the knob. She held the bot on her open palm and watched it.

The parking-lot lights came on. Outside the wide pull-up garage door, the lot had gone from late afternoon to early evening across the meeting. The lights at the perimeter of the lot — the tall pole lights, dusk-triggered, that did not come on until past eight in August — had clicked on somewhere in the back half of the meeting, and nobody had noticed at the time, because the long August evening had kept the warehouse bright enough inside that nobody had been looking outside. The light was now half industrial fluorescence and half pole-light amber, and the line between them ran across the gravel about thirty feet from the pull-up door.

It was six twenty. The Trellis block was the next block. The kettle was starting to whistle.
