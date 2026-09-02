# Step 3 — unwrap the loom and ring out every circuit

Session plan for issue #8. Written before the session so the order is decided
while nothing is at stake.

## ✅ Lengths are done — the irreversible gate is cleared

Checked 2 Sep 2026 against `measurements/harness-lengths.csv`:

| | |
|---|---|
| Rows | 52 — **46 branches**, plus 4 starter-relay rows and 2 superseded |
| Method | **48 taped**, 4 eyeball (all on the relay subassembly) |
| `breakout_mm` | **complete — every row** |
| `length_mm` | complete except `SOL.2` and `SOL.4`, both on the relay |

**Nothing about unwrapping is blocked.** Issue #2's `irreversible` label was
about exactly this gate and it is passed.

Two caveats that are not blockers:

- **Every row is `provisional`; none was re-measured.** The log's own rule is
  append, never overwrite, so a second pass is possible later — but it will be
  on a harness that has been unwrapped and possibly cut, so a disagreement
  afterwards is not resolvable. Accept the numbers as they stand.
- **`SOL.2` and `SOL.4` are eyeball.** The relay is on the bench and a tape
  costs a minute. Do it before it goes back in a box.

## ⚠️ The one thing to do before cutting any tape

**The datum survives, but check it first.** `breakout_mm` is measured from a
paint mark on the **wire bundle**, not on the tape — chosen in August precisely
so it would survive this session. Confirm the mark is still legible and still on
the bundle before the tape comes off. If it has faded, re-mark it against the
tape line *while the tape is still there*, because afterwards there is nothing
to reference.

Photograph the wrapped trunk end to end first, with a rule in frame.

## What this session is actually for

Not "check the map" — three specific things the outside-in method **structurally
could not see**, plus everything else that turns up.

### 1. Two splices that are known to exist and have never been seen

Both were inferred by conductor arithmetic, not observed. Each is a real
physical object under the tape.

| Splice | Joins | Why it must exist |
|---|---|---|
| **`Br/W`** | `B01.2` · `B00.11` · `B06.5` | All three ring continuous, but `B00.11` is **one wire with both receptacle slots empty**. One wire cannot reach three endpoints. |
| **Net A** | `B04.1` ring · `B00.7` · `B08` | Three endpoints, **each holding exactly one wire**. Same argument. |

**Where to look.** `Br/W`'s endpoints sit at ~0 mm (`B00.11`, forward of the
datum), 400 mm (`B01`) and 835 mm (`B06`), so the joint is somewhere in that
span. Net A's sit at ~0 mm (`B00.7`), 650 mm (`B04`) and 975 mm (`B08`).

**Record for each:** position along the trunk in mm from the datum, physical
form (shared crimp, soldered and taped, crimped butt splice), conductor count in
and out, and whether the gauge changes across it. **A gauge step at a splice is
the `B06.4` mechanism**, so it is a design finding if present, not a detail.

### 2. Three wire counts that are hidden under tape

| Branch | Children sum to | Meaning of a mismatch |
|---|---|---|
| `B04` | 10 | **more wires than children = another splice** |
| `B05` | 2 | |
| `B06` | 9 | |

Count them as the tape comes off, before the bundle relaxes and wires move.

### 3. ~~`B00.11`'s two legs~~ — WITHDRAWN, unwrapping cannot see them

This section claimed Step 3 could trace `B00.11`'s consumers by watching where
they run inside the trunk. **That is wrong and it is withdrawn.**

`B00.11` is a single *harness* wire ending in a double-female bullet. Its two
consumers plugged into it **from outside** — they are component leads or child
harnesses, not conductors in the main loom. Unwrapping the trunk cannot reveal
a wire that was never in the trunk.

The same applies to every one of the empty double-females. **Step 3 does not
answer any of them**, and the earlier note in `measurements/README.md` saying it
answers this one was the error, not the rule.

What is left is what the parked list already said: the photographs, and the
components themselves.

### 4. Leads that have never been located at all

**The left points lead and both condenser leads.** The trunk's yellow pair
turned out to be the alternator — proven by continuity on 28 Aug — so the
ignition leads are somewhere else entirely and no one has found them. They are
in the harness or they are not; this session decides which.

## ⚠️ The finding this session is most likely to produce, and it is not a fault

**A wire's tape exit is not necessarily its electrical breakout.** A conductor
can run inside the bundle well past the point where it leaves the wrap. Every
`breakout_mm` in the log is the *exit* position, because that is all the outside
could see.

If unwrapping shows a branch's conductors separating from the trunk somewhere
other than where they emerged, **the trunk map's number is describing the wrong
event**. Record both: keep the measured exit, add the true breakout, and say
which is which. Do not overwrite — that is the same append rule as everywhere
else, and here the old number is still the one that reproduces the tape.

## Method

- **Ohms, not beeps.** A corroded conductor still beeps. Harness wire should be
  milliohms; **anything over about 1 Ω is a damaged conductor**, so every
  ring-out doubles as a fault survey. Record the value.
- **REL-zero the leads** and note when you did.
- **Scrape before you trust a high reading** — the log already contains one
  rejected reading that was oxide on a probe tip.
- **Colour base first, tracer second**, always, and say so.
- Work in **one branch at a time** and close it out in the log before starting
  the next. A half-recorded branch on a bench full of loose wire is how the
  `Y/BK` / `BK/Y` fortnight started.

## Recording

| Finding | Goes to |
|---|---|
| Splice found | `measurements/README.md` + a `trunk-map.md` parked-item closure |
| Wire counts | `harness-lengths.csv`, the `wire_count` column on `B04`/`B05`/`B06` |
| Breakout corrections | **append** a new row; keep the old |
| New connector or terminal | `connector-inventory.csv` |
| Continuity values | `README.md` net map |
| Anything that contradicts a model | Note it, **do not redraw at the bench** |

That last rule matters. This session will produce contradictions — the last
three sessions each did — and the models have a working rule that the bench
outranks the document. Applying it needs the whole picture, not a wire in one
hand.

## Stop conditions

Stop and reassess rather than pushing on if:

- **A splice turns out to be somewhere no length in the log can describe.** That
  means the branch tree is wrong, not just incomplete.
- **A wire count exceeds its children by more than one.** One extra is a splice;
  several is a subsystem nobody has transcribed.
- **The datum mark is gone.** Everything downstream of that is unanchored.

## What closing #8 unblocks

- Both hidden splices, which are the last inferred-rather-than-seen objects in
  the factory model
- The `B04`/`B05`/`B06` wire counts
- The points and condenser leads
- The remaining unidentified nets — `B00.5`, `B04.4`, `R/Bl`'s harness side
- And the reason to do it before more design work: **the rebuild is at 49 of 56
  live connectors and rests on a factory model that still contains two objects
  nobody has looked at.**
