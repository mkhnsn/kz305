# KZ305-B1 — Wiring Diagram Reference

Last updated: 2026-08-15 (added 15 Aug bench findings: points lead colors, neutral switch)

Source: *Kawasaki Z250/KZ305 Service Manual 1979–1982*, printed page 255
(PDF page 261), in the 1981 KZ305-A supplement.

Diagram title as printed: **"KZ305-A1, A2, B1, C1, D1 Wiring Diagram
(U.S. and Canadian Models)"** — the B1 is named explicitly, so this is the
correct diagram for this bike. There is no separate B1 wiring diagram; the
B1 supplement's appendix (printed 298) lists no wiring section, and the
KZ305-D supplement (printed 303) also points back to page 255.

## Image files

| File | Use |
|---|---|
| `KZ305-B1-wiring-diagram.png` | 300 dpi, rotated upright. Everyday reference. |
| `KZ305-B1-wiring-diagram-600dpi.png` | 600 dpi, rotated upright. Zoom in on trace routing and connector detail. |

The original page is printed sideways; both files are rotated so the title
reads normally. **The image is the authority** — the tables below are a
convenience transcription and were read off a 40-year-old scan.

---

## Wire color codes

| Code | Color |
|---|---|
| BK | Black |
| Bl | Blue |
| Br | Brown |
| G | Green |
| Gy | Gray |
| LG | Light Green |
| O | Orange |
| R | Red |
| W | White |
| Y | Yellow |

Two-color leads are named primary-then-secondary: a yellow wire with thin
red stripes is "yellow/red" (Y/R). If red were the main color it would be
"red/yellow" (R/Y). This convention is from the base manual, printed 33,
item 18, and matters because Y/R and R/Y are different wires that both
appear in these tables.

---

## Switch continuity tables

Read as: in the given switch position, the listed wires are connected to
each other.

### Ignition switch

Columns as printed: Battery (W) · Ignition (Br) · Tail 1 (R/BK) · Tail 2 (R)

| Position | Connected |
|---|---|
| **ON** | W ↔ Br, and R/BK ↔ R |
| **OFF** | — none — |
| **LOCK** | — none — |
| **P (PARK)** | W ↔ R (single long bar spanning the full table) |

✅ **METER-CONFIRMED 15 Aug 2026.** All six pin pairs tested in all four
positions with the switch unplugged from the harness. The transcription above is
correct as printed — no corrections needed. Full matrix in "Bench findings".

Park feeds the tail circuit from the battery with ignition dead — worth
keeping in mind when rewiring, since a modern fuse block layout often drops
this function by accident.

### Left handlebar

**Dimmer switch** — columns R/BK · Bl · R/Y

| Position | Connected |
|---|---|
| HI | R/BK ↔ Bl |
| LO | Bl ↔ R/Y |

Blue is the common terminal in both positions, which makes Bl the feed and
R/BK / R/Y the two beam outputs. ⚠️ Verify with a meter during harness
mapping — this is the one table where the scan is marginal, and getting the
common wrong would put both filaments on at once. **Still unresolved as of
13 Aug 2026** — the bench photos show the harness-side connector, not the
switch internals. See "Physical harness inspection" below.

**Turn signal switch** — columns G · O · Gy

| Position | Connected |
|---|---|
| R | O ↔ Gy |
| L | G ↔ O |

Orange is the common (flasher feed); green and gray are the two sides.

**Horn button** — columns BK · ground

| Position | Connected |
|---|---|
| Push | BK ↔ ground |

Horn switches the ground side, not the feed.

### Right handlebar

**Starter button** — columns Y/R · BK

| Position | Connected |
|---|---|
| Push | Y/R ↔ BK |

**Engine stop switch** — columns Br · Y/R

| Position | Connected |
|---|---|
| RUN | Br ↔ Y/R |
| OFF | — none — |

Note the shared Y/R: the stop switch feeds the starter button, so the
starter can't crank with the kill switch off. Preserve that interlock in
any rebuild.

✅ **METER-CONFIRMED 15 Aug 2026** — topology matches as printed, interlock
verified. ⚠️ But the contacts are degraded enough to stop the starter working;
see "Bench findings".

---

## Components on the diagram

**Ignition (points, battery-and-coil):** two ignition coils (LEFT and
RIGHT), two sets of contact breaker points, two capacitors, two spark
plugs.

**Charging:** alternator (single-phase AC, yellow leads), combined
regulator/rectifier.

**Starting:** starter motor, starter relay, battery 12 V 10 AH.

**Protection:** main fuse 12 V 20 A, plus a multi-position fuse block.

**Switches:** ignition switch, front brake light switch, rear brake light
switch, neutral switch, left and right handlebar clusters.

**Other:** flasher (turn signal relay), horn, junction/6P connectors,
"Meter Accessory Leads" pickup points.

---

## Bulb ratings from the diagram

| Lamp | Rating |
|---|---|
| Headlight | 12 V 50/35 W (sealed beam) |
| Tail / brake light | 12 V 8/27 W |
| Turn signals, front and rear, each | 12 V 23 W |
| License plate light | 12 V 8 W |
| Speedometer light | 12 V 3.4 W |
| Tachometer light | 12 V 3.4 W |
| Neutral indicator | 12 V 3.4 W |
| High beam indicator | 12 V 3.4 W |
| Right turn indicator | 12 V 3.4 W |
| Left turn indicator | 12 V 3.4 W |

Total indicator and instrument load is ~20 W across six 3.4 W bulbs —
worth counting when sizing the LED conversion, because removing it shifts
that much extra load onto the shunt regulator.

---

## Physical harness inspection — 13 Aug 2026

Harness laid out flat on the bench and photographed in detail. What the
photos confirm, and what they don't.

### Confirmed against the bike

| Finding | Evidence |
|---|---|
| **Harness P/N `26001-12348`** | Woven cloth tag, "MADE IN JAPAN". A second tag appears on another branch. Read both under good light and log them — this identifies the harness variant independent of the diagram's A1/A2/B1/C1/D1 grouping. |
| **Fuse block matches the diagram** | Three glass fuses in the original black box, feeds in white, blue, and red. Consistent with the 20 A main plus 10 A × 2 on printed 255. Use as the baseline when laying out the 6-circuit blade block. |
| **Alternator is single-phase** | Short taped stub terminating in two yellow bullets — the stator pair, physically confirmed. Rotor confirmed permanent-magnet, hands-on 18 Aug 2026. ~~Three-phase R/R units (SH775 etc.) stay off the table.~~ **Corrected 18 Aug 2026** — a single-phase stator connects to any two of a three-phase regulator's three AC inputs, so the SH775 is back on the table and is now the leading candidate. See `docs/part-selection.md`. |
| **Single chassis ground** | ⚠️ **SUPERSEDED 28 Aug 2026 — see the ring-out correction below.** Recorded here 13 Aug as one ring terminal, *yellow/black*, with everything returning through it. The ring terminal and its colour are right; "everything returns through it" is wrong. |

### Condition

Consistent with the water-in-the-sleeve finding that condemned the harness:

- Green corrosion on **both** starter relay studs
- HT lead insulation chalked and cracking
- Bullet housings clouded, oil-soaked, brittle

### Still open

- **Dimmer switch common** (Bl vs. R/BK / R/Y) is *not* resolved by these
  photos. The continuity is internal to the left handlebar cluster; the
  photos show the harness-side connector only. Six-wire white connector —
  green, orange, gray, blue, and two reds — is probably the left-bar 6P,
  but this has to come off a meter on the switch itself.

### ⚠️ Do not map colors from photographs

Scoped to photographs and to this document — **not** to colours read off the
wire in hand. The camera shifts them: white reads as tan and blue/white as gray
in several shots, an artefact of lighting and white balance. **Ring out every
wire end-to-end** during mapping rather than transcribing colours out of a photo
or out of this file. A hands-on colour call at the bench is a primary source and
is recorded as given.

### Photos still wanted

- Left handlebar switch cluster
- Right handlebar switch cluster
- Any connector shot face-on with the pins visible

---

## Bench findings — 15 Aug 2026

Measured on the bike. These override the transcription above.

**Meter: Fluke 87V.** Test leads read **0.4 Ω**. The ignition switch and neutral
switch readings below were taken **un-zeroed**, so they carry a +0.4 Ω offset and
are noted as corrected where it matters. Later readings are REL-zeroed and read
directly. Re-zero after changing probes or clips — lead resistance drifts.

⚠️ **Resolution floor:** the 87V's lowest resistance range is 600.0 Ω at 0.1 Ω
resolution. Sub-0.1 Ω bonds cannot be resolved. A good ground reads 0.0–0.1 Ω
and that is the *floor*, not a measurement — do not treat 0.0 Ω as proof of a
perfect bond, and do not chase differences at that level. For the star ground
bus, "reads 0.0–0.1 Ω REL-zeroed" is the acceptance criterion.

**Deferred tests this meter already covers** — no extra instruments needed:

- **Regulator body temperature** (the shunt-regulator check under "Notes for the
  harness rebuild") — 87V does type-K thermocouple temperature. Needs an 80BK-A
  style bead probe.
- **Charging voltage at 3,000–5,000 rpm** — use MIN MAX to capture the peak
  hands-free while blipping the throttle, rather than trying to read a moving
  display. Target 14.0–14.5 V.
- **Actual bus current** — the 10 A range can verify the real coil and
  switched-bus draw instead of the ~6 A estimate used in the notes above.

**Project state:** bike is stripped. Harness laid out on the bench, engine block
separate. Continuity and switch-table work is *easier* in this state; anything
dynamic (crank test, charging voltage at rpm, regulator temperature) is deferred
until reassembly.

### Contact breaker lead colors — CONFIRMED

Read off the factory-stamped plates on the points module, not from the scan:

| Lead | Color | Serves |
|---|---|---|
| `W_PTS_L` | Yellow (Y) | LEFT cylinder |
| `W_PTS_R` | Black (BK) | RIGHT cylinder |

Both leads carry a **factory braided jacket — do not strip it.**

⚠️ This puts Y on two circuits (left points lead, alternator phases) and BK on
three (right points lead, starter trigger, chassis ground). Identify these by
endpoint, never by color.

### Neutral switch — CONFIRMED single conductor

One wire, grounding through the engine case.

Switch lead to starter ground point (top of engine):

| Gearbox | Before cleaning | After cleaning (15 Aug 2026) |
|---|---|---|
| Neutral | ~40 Ω | 4 Ω |
| In gear | open | open |

Cleaning the switch threads and the ground stud took the path from ~40 Ω to
4 Ω (**~3.6 Ω lead-corrected**). That 10× drop confirms the original reading was **surface contamination,
not a failing switch** — worth remembering for every other ground point on this
powder-coated frame.

⚠️ **The residual ~3.6 Ω is fine for indicator duty, marginal for anything else.**
The 3.4 W indicator draws ~0.28 A, so 4 Ω costs ~1.1 V — the lamp lights, a bit
dim. But a starter relay coil is only ~3–5 Ω, so 4 Ω in series roughly halves
pull-in current. If the coil ground turns out to be shared-wire (below), this
4 Ω must come down or move behind a relay.

To locate the remaining 4 Ω, split the path and re-measure:

1. Switch terminal → engine case a few inches away = the switch contact itself.
   These run immersed in oil and a few ohms here may simply be the switch.
2. Case near the switch → starter ground point = the case/stud path. This one
   should be milliohms; anything meaningful is still contamination.

Null the meter leads first (short the probes, note the reading, subtract it).
At 4 Ω the leads are already ~10% of what you are measuring.

⚠️ **This does not by itself close the starter relay coil ground question.** A
single-wire neutral switch can still gate a relay coil if COIL− ties to that
same wire at a junction — the wire count rules out an *isolated* interlock, not
a *shared-wire* one.

### Starter relay coil ground — CONFIRMED direct

Read off the factory diagram at 600 dpi, at the starter relay, and corroborated
by bench observation of the harness.

- The **neutral switch is an isolated branch**: one wire out of the top running
  up to the neutral indicator, and its own hatched ground symbol directly below
  the switch. It grounds through the engine case and has no path to the relay.
- The relay's two small coil leads run **up and left** toward the fuse/battery
  area — a separate run from the neutral switch entirely.
- COIL+ is the **BK** lead from the starter button, consistent with the
  right-bar table (Push = Y/R ↔ BK) and with Br → kill → Y/R → button → BK.
- COIL− lands on the chassis ground net.

**Conclusion: SOL COIL− grounds directly. There is no crank interlock in this
circuit,** and `W_SOL_GND` in the loom is correct as drawn.

⚠️ Not readable off the scan: the **stripe color** of the COIL− lead. Y/R and
Y/BK are indistinguishable at this scan quality, and the two are different wires
under the primary-then-secondary convention. This does not affect the rebuild —
the star ground bus uses new BK wire regardless — but do not quote a stock color
for that lead from this document. A ring-out on the bench would settle it and
would upgrade this finding from diagram to meter.

### Ignition switch — CONFIRMED by meter

Switch unplugged from the harness. All six pin pairs, all four positions.

| Pair | OFF | LOCK | ON | PARK |
|---|---|---|---|---|
| W ↔ Br | open | open | **0.5 Ω** | open |
| W ↔ R/BK | open | open | open | open |
| W ↔ R | open | open | open | **closed** |
| Br ↔ R/BK | open | open | open | open |
| Br ↔ R | open | open | open | open |
| R/BK ↔ R | open | open | **closed** | open |

Matches the scan transcription exactly. OFF and LOCK are fully dead — no sneak
paths. PARK is W↔R alone, so the park-feeds-tail function is intact and must
survive the fuse block redesign.

✅ **The 0.5 Ω on W↔Br is test leads, not the switch.** Leads measure 0.4 Ω, so
the contact itself is **~0.1 Ω** — healthy. That is ~0.6 V at a 6 A coil load,
fine for a switch this age. No action needed, and no concern for the stage-2
bus either.

### Right handlebar cluster — CONFIRMED by meter, but contacts are bad

Cluster unplugged from the harness.

| Pair | OFF, released | OFF, pressed | RUN, released | RUN, pressed |
|---|---|---|---|---|
| Br ↔ Y/R | open | open | closed | closed |
| Br ↔ BK | open | **open** | open | **~8 Ω** |
| Y/R ↔ BK | open | ~5 Ω | open | ~5 Ω |

**Topology matches the scan exactly**, and the two predictions hold: Y/R↔BK
closes on push regardless of kill position (the button is its own switch), and
Br↔BK closes only in RUN + pressed.

✅ **Interlock verified.** OFF + pressed reads Br↔BK **open**. No crank with the
kill switch off.

🛑 **The contact resistance is a stop-ship.** Splitting the series path:
button ≈ 5 Ω, kill switch ≈ 8 − 5 ≈ 3 Ω. The arithmetic being self-consistent
says these are real contact readings, not probe artifacts.

This path carries the starter relay coil current. With a ~4 Ω coil and 8 Ω of
switch in series, the coil sees roughly **4 V of a 12 V supply and the relay
will not pull in.** Symptom on a finished bike: press start, nothing happens,
and every obvious suspect — battery, solenoid, motor, grounds — tests fine.

**Clean both switches before the harness is built.** Bar switches come apart;
clean and burnish the contacts. Target well under 0.5 Ω each, then re-measure
Br↔BK in RUN + pressed. Do not build this into the loom at 8 Ω.

### Ignition coil feed — Y/R, downstream of the kill switch (diagram)

Read off the factory diagram at 600 dpi at the coil block.

Both ignition coils are fed from a **Y/R** bus running across the top of the coil
pair. That is the same Y/R that appears as a pin on the right-bar 4-pin
connector — it is *not* internal to the cluster:

```
Br (switched) --> kill switch --> Y/R --+--> both ignition coils
                                        +--> start button --> BK --> relay coil
```

**The engine stop switch works by cutting coil power.** The two Y/R wires at the
switch end are the kill-switch output and the starter-button input, landing on
that one shared connector pin, which then runs out to the coils.

🛑 **The stage-1 loom does not do this.** `W_COIL_FEED` runs from PDM F2 to the
coil splice, *parallel* to the kill switch rather than downstream of it. As
drawn, the kill switch gates the starter only and **will not stop a running
engine** — a safety defect, not a cosmetic one.

Also corroborated here: the LEFT coil primary runs to a **yellow** lead down to
the left contact breaker, the RIGHT coil to a **black** lead. Third independent
agreement with the stamped plates and the loom.

### Right-bar wire inventory — 15 Aug 2026

| Location | Wires |
|---|---|
| 4-pin connector | Br, **Br/W**, Y/R, BK |
| Switch end | Br, Y/R, Y/R, BK |
| Loose at connector end | **Bl/W**, not in the 4-pin |

The two Y/R at the switch end reconcile with the single Y/R connector pin if both
land on that pin — consistent with Y/R being the shared node. That leaves **Br/W
and Bl/W unexplained**, and means the right-bar branch carries at least one
circuit the loom does not model (`RH` is three pins: Br, Y/R, BK).

### Diagram transcription — rear section, 17 Aug 2026

Read at 600 dpi. Structure is legible here; exact stripe colours are not, and
per the standing rule they must come off a meter.

**Main ground bus.** A single bus runs the length of the rear branch and
terminates at a chassis ground symbol. Every rear lamp grounds to it.

⚠️ **COLOUR DISPUTED — BK/Y vs Y/BK.** These are different wires under the
primary-then-secondary rule, so this is not a spelling quibble.

| Source | Date | Reads |
|---|---|---|
| Physical harness, hands-on | 17 Aug | **BK/Y** — black, yellow stripe ("pretty sure") |
| Physical inspection notes | 13 Aug | Y/BK — yellow, black stripe |
| Factory diagram, 600 dpi | 17 Aug | yellow-primary, i.e. Y/BK |

Recorded as **BK/Y** in the models: newest, hands-on, and bench beats document.
But it was hedged, and two prior records disagree.

**To settle it:** the 17 Aug read is the one to trust — newest, hands-on, and
bench beats document — but it was logged as "pretty sure" and the 13 Aug note
says the opposite. A cut end shows base against stripe unambiguously and
confirms which of the two notes to keep. Do not settle this from the scan;
the diagram renders bicolour wires as base-plus-dashes and the dash colour is
exactly what forty years of paper aging degrades.

**Tail / brake light (12V 8/27W)** has three connections:

| Lead | Function |
|---|---|
| RED | tail filament feed |
| BLUE / cyan | brake filament feed |
| Y/BK | ground |

The blue brake feed ties the rear lamp to the **Bl/W** lead found loose at the
right cluster on 15 Aug, and to the light-blue lead on the front brake switch.
Brake circuit = blue. Tail circuit = red. That is now coherent across three
separate reads of the drawing.

**Flasher ("Turn Signal Light Relay") is 2-PIN** — brown in, orange out. No
ground terminal, which confirms the rebuild note: the stock harness has no
ground run to the flasher, so an electronic 3-pin unit needs a new wire.

**Turn signal circuits** use O (orange) as the common from the flasher, with G
(green) and Gy (grey) as the two sides — matching the left-bar transcription.
Green is visible in the rear bullet block.

**Electric accessory leads** are present as a tap point in the rear branch.

⚠️ **What this section does NOT give:** which 10A fuse feeds which circuit.

### Diagram transcription — fuse block, 17 Aug 2026

Two 10A fuses, and both are fed from a **common red input node** — a single red
wire branches to both fuse tops. That structure is clear. The output colours are
not readable at this scan quality.

⚠️ **Possible conflict with the physical inspection.** The 13 Aug bench notes
record the original fuse box as "three glass fuses, feeds in white, blue and
red". The diagram shows the two 10A fuses sharing one red feed, which does not
obviously reconcile with three differently-coloured feeds. Do not resolve this
from either document — **the original fuse box is on the bench.** Ring it out.

### Right-bar branch — MAPPED by unsleeving, 17 Aug 2026

First in-sleeve splice actually opened up. Four leads leave the switch housing
directly, with no connector at the switch end.

| At the switch | Inside the branch | At the 4P |
|---|---|---|
| Y/R + Y/R | **2→1 splice**, continues as Y/R | Y/R |
| Br | **1→3 splice** → Br, Br/W, Bl/W | Br + Br/W (Bl/W leaves on a bullet) |
| BK | straight through | BK |

**The wire-count mismatch is fully explained.** Four leads at the switch become
four pins at the connector plus one bullet, because two Y/R merge while one Br
expands to three.

✅ **Y/R shared node confirmed.** Kill-switch output and starter-button input
are the same net, and that net carries the coil feed out of the branch. The
models had this right.

🛑 **Br/W and Bl/W are NOT the front brake switch.** Both sit on the *same net*
as the kill-switch feed, and a switch output cannot live on its own feed node —
it would light the brake lamp whenever the ignition was on. The 15 Aug
hypothesis is dead.

**The front brake switch is not in this harness section at all.** Confirmed
17 Aug: it has its own pair of bullets, **blue and brown** — plain colours, not
Br/W and Bl/W. That reconciles cleanly with the diagram (brownish + light blue
at the switch) and with the tail lamp (blue feeds the brake filament). Brake
circuit: **Br in, Bl out.** Settled.

⚠️ **Which leaves Br/W and Bl/W completely unexplained.** They are live switched
feeds heading somewhere, and there is now no candidate for either. Two unknown
circuits leaving the right bar.

**This is a build-stopper, not a curiosity.** Whatever they feed still needs
feeding on the new harness. Miss them and two circuits are simply absent — and
because both sit on the switched-brown net, the fault will look like "that
thing doesn't work with the key on" with no obvious wiring error to find.

Trace both: the Bl/W bullet's other half, and where Br/W goes past the 4P.

### Diagram transcription — instruments and accessory leads, 17 Aug 2026

**Electric Accessory Leads** are a **blue-family wire plus a black** — a switched
power pickup and a ground. This was briefly the leading candidate for the
right-bar Bl/W. ❌ **Wrong** — see below; Bl/W traces to a fuse, and the accessory
leads are a separate blue-family circuit.

**Instrument lamps** (speedo, tacho) take a **red feed and a black ground**. Red
being the tail-circuit colour fits — instrument lighting comes on with the
position lights.

**Indicator lamps** (right turn, high beam, neutral, left turn — four 3.4 W)
land on a **6P connector**.

⚠️ **Ground symbols on this diagram are schematic, not physical.** The drawing
shows chassis-ground symbols at the front of the bike, which would suggest local
ground points. The 13 Aug physical inspection found **exactly one ring terminal
on the whole harness**, and this section used to conclude that every one of those
returns therefore runs back to that single ring.

**CORRECTED 28 Aug 2026 by meter — that conclusion was wrong, and the diagram was
closer to the truth than this document was.** Working rule 1 applies: the bench
value stands and the document changes.

There are **two ground nets**, and they are open to each other:

- **Net A**, `Y/BK` (yellow base). Small. It reaches the ring terminal.
- **Net B**, `BK/Y` (black base). A single harness-wide return net spanning the
  tail to the headlight junction — and **open to the ring terminal entirely**.

Net B does not return through the main harness at all. It reaches earth through
the **child harnesses**, at whatever each component is bolted to. So the harness
has **one ring terminal but many earth points**, distributed across component
mounting hardware. That is much closer to the local ground symbols the diagram
draws than to the single-point reading recorded here.

It still changes the star-ground design, and by more than the old reading did:
every component earthing through its own mounting needs a **new ground wire back
to the bus** — wire that does not exist in this harness and appears in neither
model. The count of them is the count of Net B's earth points, which is not yet
known. See `measurements/README.md` and the `GND_NETB` notes on the backbone
sheet.

**No Br/W identified here.** Still unexplained.

### Bl/W traced — it is the FEED, 17 Aug 2026

Bl/W runs from the right-bar splice **straight to a fuse**. That reverses the
direction everything was being reasoned about.

The right bar is not a set of taps hanging off a bus. It is a **distribution
point fed from a fuse**:

```
fuse --Bl/W--> right-bar splice --+--Br----> kill switch
                                  +--Br----> 4P, onward into the harness
                                  +--Br/W--> 4P, onward into the harness
```

**Why this matters more than the identification.** One 10 A fuse is protecting
the kill switch, both ignition coils (via the Y/R node), the starter trigger,
**and** whatever Br and Br/W feed onward. That is the entire run-critical half of
the bike behind a single fuse — and possibly some non-critical loads sharing it,
which is exactly the arrangement where a failed accessory takes the engine out.

**First real fuse-assignment data.** This is the start of the answer to the PDM
cavity map, the last of the four original TBDs.

⚠️ **Still unknown, and both matter:**

- **Which** of the two 10 A holders this is. Load grouping depends on it.
- **Where Br/W goes.** It is a live fused circuit feeding something unidentified,
  and it is now the last unexplained wire in this branch.

### Still open after this session

- ~~Starter relay coil ground~~ — **RESOLVED, see above.**
- **Dimmer switch common** — unchanged from 13 Aug, still needs a meter.
- **Right cluster contact cleaning** — must happen before harness build; re-measure after.
- ~~Coil feed routing~~ — **RESOLVED in the rebuild model.** PDM F2 now feeds
  the kill switch, whose output drives the `K_COIL` relay; the relay passes coil
  power to `SP_YR` and on to both coils. Cutting the kill switch therefore drops
  the coils, which the parallel arrangement did not do.
- **Unidentified Br/W and Bl/W at the right cluster.** Neither is in the diagram
  transcription, the color-code table, or the loom. Leading candidate for both:
  the front brake light switch, which the diagram lists as its own component and
  which sits physically at the right lever perch. Ring each out against the three
  known pins in every switch state — no continuity to any of them means a
  separate switch sharing the branch. Note Br/W vs W/Br, and Bl/W vs W/Bl, are
  different wires under the primary-then-secondary rule.
- **PDM cavity map** — pending part selection.

---

## Notes for the harness rebuild

- **Shunt regulator.** The stock unit is an open-circuit type that dumps
  surplus output as heat. Cutting load with LEDs makes it work *harder*,
  not easier. Verify 14.0–14.5 V at 3,000–5,000 rpm on the bench run and
  check the regulator body temperature, not just the voltage.
- **Never** disconnect the regulator/rectifier with the ignition on, and
  never disconnect the battery while running. Either damages the unit.
- **Grounds are chassis returns** throughout — the horn, the lamps, and the
  starter all rely on frame ground. Powder coat is an insulator, so every
  ground point on the returning frame needs masking or scraping back to
  bare metal.
- **Stator check values** (from the electrical chapter, printed 159):
  coil resistance 0.36–0.54 Ω, output about 75 V AC at 4,000 rpm across the
  yellow leads, and each yellow lead must read infinity to ground.
- **Ignition coil values** (printed 161): primary 3.6–5.4 Ω,
  secondary 11–17 kΩ.
- **Capacitor spec:** 0.24 ± 0.02 µF, 1,000 W VDC.

---

## Related diagrams in the same manual

Not applicable to this bike, but present if a cross-reference is ever
useful:

| Diagram | Printed page | PDF page |
|---|---|---|
| Z250-A1/A2/A3/B1/B2 (European and General Export) | 179 | 185 |
| Z250-A4/B3 (General Export) | 278 | 284 |
