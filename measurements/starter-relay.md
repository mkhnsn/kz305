# Starter relay assembly

**Not yet mapped.** This file is the capture sheet for the bench session that
maps it — written before the readings so the readings have somewhere to land.

The relay assembly is a **component off the harness**, like the fuse box: it is
named in words in `mates_to` and carries no `B##` tag of its own. Its own leads
are logged here, not in `harness-lengths.csv`.

## Why this is blocking

Two open items in `README.md` both terminate at this assembly and cannot close
without it:

- **Is the accessory feed switched or permanently live?** The second fuse box
  takes power on an `R/W` male bullet, and that `R/W` mates *a short jumper off
  the starter relay assembly's own `R/W` female bullet*. Which relay stud that
  jumper leaves from — battery side or switched side — is the whole answer. The
  44-year-old diagram calls the accessory pickup *switched*; a lead off the
  battery side would be permanently live, and that changes the fuse assignment
  the rebuild has to make.
- **The `B06.4` melting mechanism.** `B06.4` is `W/R`, the 20 A MAIN circuit,
  and it melted at a bullet where a larger conductor meets a smaller one. The
  larger conductor runs to this assembly. This is a **design** finding, not a
  condition one — a new harness built to the same topology puts the same step on
  the same 20 A circuit.

⚠️ **`R/W` is red base. `W/R` is white base.** Both wires exist on this bike and
they are different circuits. The main power path (`B04.6` ↔ `B06.4`, and the
R/R's DC output) is `W/R`. The second fuse box's feed is `R/W`.

## What is already known, from the harness side

Every one of these was read from the *other* end. Nothing below was read at the
relay itself.

| Evidence | Where recorded | What it says |
|---|---|---|
| `B06.2` — `BK`, female bullet | lengths, 2026-08-28 | **Black Net 2 = starter trigger.** 0.2 Ω to `B01.2`'s black (RH_4P, the start button) and **open** to Black Net 1. Start button → relay COIL+. |
| `B06.4` — `W/R`, male bullet, **melted** | lengths + inventory | Its 3-way node ran off as `W/R` to the relay. The node was on the **fuse-box pigtail**, not in the loom, and is now unplugged — the 28 Aug mate record cannot be re-verified by looking. |
| `B06.1` — `Y/R`, male bullet | lengths, 2026-08-28 | **`Y/R` Net 2**, open to both `B03` and `B01.2`. A second independent `Y/R` circuit the models do not carry. On the branch serving the relay; **circuit unidentified**. |
| second fuse box inbound `R/W` | README, 2026-08-29 | Mates a short jumper off the relay assembly's own `R/W` female bullet. |
| `W_SOL_GND` | `models/factory/starting.yml` | Modelled direct to chassis ground, confirmed 15 Aug. **No neutral-switch interlock in this circuit.** |
| `W_START` | `models/factory/starting.yml` | Start button output to COIL+. `BK` but **not** a ground — a black net of its own. |

`models/factory/starting.yml` already draws `SOL` ways 2, 3 and 4. Those way
numbers are **from the diagram, not from the part** — they have never been
checked against the housing, and the cavity rule below governs if they disagree.

## Bench read, 2026-09-02 — VISUAL ONLY, no meter

⚠️ **Method is `visual` throughout.** Nothing below is a continuity or resistance
reading. What eyes are good for — what is bolted to what, colour, gender, way
count, whether a lead is discrete or shared — is recorded as fact. Gauge and
ohms are **not** recorded and are still open.

### The assembly, as it sits

**Two lugs and two small wires.**

| | |
|---|---|
| Small wires | **`Y/R`** and **`BK`** |
| Lug A | **EMPTY** — its lead was removed at teardown |
| Lug B | heavy ~6 in cable, ring both ends, red boot at the far end — **battery** — plus a normal-gauge **`W/R`** ending in a **double-female bullet**, *and this is the one that melted* |

So **Lug B is the battery stud** and Lug A is the motor stud, whose cable is
absent. That also explains the empty lug without inventing anything: the starter
cable comes off with the motor.

### ✅ CLOSED — the accessory feed is PERMANENTLY LIVE, and the diagram is wrong

Under the battery boot, alongside the heavy cable's ring, sits **a second ring
terminal on an `R/W` wire, running about 2 in to a female bullet.** It is
unconnected now but is plainly made to bolt to **the battery stud itself**.

That answers the question this whole capture sheet was opened for, and it
answers it **without a meter** — a lug on a post is topology, where a meter
reading through a de-energised relay would only have been evidence about
topology.

> **The second fuse box is fed straight off the battery post.** The chain is
> battery `+` → `R/W` ring → 2 in → female bullet → the second box's `R/W` male
> → its fuses → `W/Bl` → `B09`, the rear accessory pickup.

**The 44-year-old diagram calls the Electric Accessory Leads a *switched* feed.
It is not.** It is permanently live, and it is **unfused for the first two
inches out of the battery post**.

Consequences, and they are design ones rather than curiosities:

- Any accessory on that circuit could flatten the battery with the key out, and
  did so for forty-four years without anyone writing it down.
- **The rebuild must not reproduce it.** An unfused conductor on a battery post
  is the one thing a harness must not have — the same rule that put `MF_RR` at
  the battery end of the charging run.
- It also explains the asymmetry recorded on 29 Aug: the accessory **feed** was
  in service while both accessory **earths** sat open. A permanently-live feed
  that nothing was earthed to is a circuit half-built, not a circuit in use.

### ✅ The two coil leads mate `B06.1` and `B06.2` — by gender complement

Terminations read 2 Sep 2026:

| Lead | Termination | Gauge |
|---|---|---|
| `Y/R` | **female** bullet | same as the others, 18 or 16, probably 18 |
| `BK` | **male** bullet | same |
| `W/R` | double-female bullet | same |

The harness's two unaccounted-for small bullets on the `B06` branch are:

| | | |
|---|---|---|
| `B06.1` | `Y/R` | **male** |
| `B06.2` | `BK` | **female** |

**Every one is the complement of its opposite number.** Same branch, same
colours, opposite genders, and the assembly carries exactly two small leads
against exactly two unaccounted-for small bullets. Neither mate was recorded
while connected, so this is inference — but it is inference with nothing else it
could be.

**That identifies `Y/R` Net 2's other end: the starter relay coil.** The circuit
has been unidentified since 28 Aug and is listed in the models' colour-collision
warning as *"a SECOND, independent Y/R net that is MISSING FROM THESE MODELS
entirely."* One end is now named.

### ⛔ OVERTURNED — `COIL-` does NOT ground directly at the relay

`models/kz305-common.yml` has carried this on the `starter_relay` template since
15 Aug 2026:

> `COIL+` is fed `BK` from the starter button. **`COIL-` grounds directly,
> CONFIRMED 15 Aug 2026.**

**Both coil leads end in bullets that go into the harness.** There is no ring
terminal, no eyelet, and nothing on this assembly that lands on the engine or
the frame. Whatever grounds that coil, it is not a wire leaving this part.

Nor does the harness side rescue it: `B06.2` is **Black Net 2**, measured
0.2 Ω to the start button on 28 Aug and **open to the ground net**. So neither
coil lead reaches earth by any path this project has measured.

**What replaces it is NOT yet known.** The likely shape is ground-side
switching — `Y/R` feeding the coil live and the button pulling the other side
down — which would also fit the metered *Push = `Y/R` to `BK`*. But `Y/R` Net 2
is open to the bar's `Y/R`, so the two are not the same wire and the loop does
not close on the evidence in hand. **This needs the meter.**

Working rule 1 applies: the bench outranks the document, and a direct read of
what a wire terminates in is as direct as this project gets. The claim comes
out; the replacement waits.

### ✅ CORRECTED — the `W/R` double-female is on THIS assembly

Read directly, part in hand: the double-female bullet is **on the starter relay
subassembly**, and both the fuse-box pigtail's `W/R` and the main harness's
`W/R` join into it.

The 29 Aug record said the opposite — *"a double-female bullet on the FUSE-BOX
PIGTAIL, not in the loom"* — and it was written after the node had already been
unplugged, from memory of the 28 Aug mate record. **The part in hand wins.**

So the three-way node is:

| | |
|---|---|
| Node itself | starter relay assembly, `W/R`, double-female, off the **battery** stud |
| Leg 1 | main harness `B06.4`, male `W/R` — ⚠️ **the melted one** |
| Leg 2 | fuse-box pigtail `W/R` |

**This puts the melting in a different place than the log has it.** The node is
not a harness feature at all — it hangs off the battery stud of the relay, so
the whole main power path leaves the battery, passes one lug, and steps down to
18-or-16 gauge at a bullet. That is the gauge step, and it is two connections
from the battery with nothing but the 20 A MAIN downstream of it.

### ⚠️ OPEN — coil polarity, which lead is which

The two small wires are **`Y/R`** and **`BK`**. The models draw the coil as fed
**`BK`** from the start button on `COIL+`, with `COIL-` grounding directly, and
there is no `Y/R` anywhere in the drawn starter circuit.

**This is very likely `Y/R` Net 2 finding its other end.** `B06.1` is a `Y/R`
male bullet on the `B06` branch — the branch that serves this assembly — open to
the coil-feed `Y/R` and unidentified since 28 Aug. A `Y/R` on the relay is
exactly what it has been missing.

If so, the circuit is **ground-side switched**: `Y/R` feeds `COIL+` live from
the kill switch, and the start button pulls `COIL-` to earth through the `BK`.
That matches the metered switch table — *Push = `Y/R` to `BK`* — as well as the
drawn version does, and it would **overturn** the current drawing.

**Not settled by eye.** Which wire is which needs the meter. Recorded as a
question, not a finding.

### ⚠️ OPEN — where the `W/R` double-female actually lives

The `W/R` double-female bullet is **on this assembly**, on the battery stud. The
29 Aug record has the three-way `W/R` node as *"a double-female bullet on the
FUSE-BOX PIGTAIL, not in the loom"*. Both cannot be describing the same object
unless one of them named the wrong pigtail.

Reconcile before either is relied on. The 29 Aug entry was written after the
node had already been unplugged, and says so.

### Recorded lengths

| | |
|---|---|
| Battery cable, relay lug to battery ring | ~6 in / ~150 mm |
| `R/W` ring to its female bullet | ~2 in / ~50 mm |

Both are **eyeball estimates**, not tape.

### Still open on this assembly

- **Gauge of anything.** Needs calipers. This is the circuit that melted and the
  gauge step is the finding, so it is deliberately left blank.
- **Coil polarity** — see above.
- **Terminal map and cavity rule** — the housing's own markings, if any.
- **Coil ground** — where the `BK` terminates.
- Ohms on every path.

## Readings to take

Take them in this order — item 2 is the one that unblocks the accessory
question, and it does not depend on the rest.

### 1. Terminal map

One row per way in `connector-inventory.csv`, `mates_to` = `starter relay
assembly`. State the cavity rule used in `notes`.

- Use the housing's own moulded numbers **if it has them**. A moulded mark is
  not a moulded cavity number — record marks verbatim as a part-identification
  lead and never orient by them.
- Otherwise: viewed from the **mating face**, **latch or keyway UP**, numbered
  **left to right, top row first**.
- Colour **base first, tracer second**, as read with the wire in hand.
- Note gender per way, and record **depth** (mating face to the back of the
  body) once, on the first row.

| | To record |
|---|---|
| Way count and layout | |
| Cavity rule used | |
| Per-way colour + gender | |
| Depth | |

### 2. ⚠️ Which stud the `R/W` jumper leaves from — battery side or switched

**The reading that unblocks the accessory identification.** With the relay
de-energised, ring the `R/W` female bullet against each of the two heavy studs.
The stud it is continuous with is its source.

- Continuous with the **battery** stud → the accessory feed is **permanently
  live**, and the diagram's "switched" call is wrong.
- Continuous with the **starter motor** stud → it is only live while cranking,
  which cannot be what fed an accessory circuit. That result means the jumper is
  something else and the identification needs rethinking.

Record the ohms, not just "continuous" — the procedure's >1 Ω rule makes every
ring-out a fault survey.

### 3. Heavy cables

Both of them: **battery → relay** and **relay → starter motor**.

| | Length | Gauge | Ring terminal ID | Stud size |
|---|---|---|---|---|
| battery → relay | | | | |
| relay → starter | | | | |

Gauge here should be **measured, not eyeballed** — this is the circuit that
melted, and the gauge step is the finding. See the gauge warning in `README.md`:
no wire gauge on this project has been measured at all.

### 4. The `R/W` jumper

Length, gauge, and **whether it is a discrete lead or a shared crimp** with
anything else on that stud. A shared crimp is a splice and changes the topology
the rebuild reproduces.

### 5. Coil ground

`W_SOL_GND` is modelled direct-to-chassis. Verify the **physical ring terminal
location** — which frame or engine point it lands on. That location is a Net B
earth point, and **the count of Net B earth points is the count of new ground
wires the star bus needs**. It is not yet known.

## Scope note

Unlike the fuse box, the relay assembly is **not** being replaced by the rebuild
as a decided matter. Whether it survives is open. Map it as an as-built
reference either way — the topology is what the design findings rest on.

---

# Condenser assembly — bench, 4 Sep 2026

Recorded here rather than in a new file because it is the same kind of
capture: a small subassembly, read visually with the part in hand.

| | |
|---|---|
| Form | **ONE bracket carrying TWO cans**, stacked axially — end to end like batteries |
| Leads | **YELLOW and BLUE**, one per can |
| Terminals | male bullet on each |
| Ground | through the **case** to the **FRAME**, via **two mounting tabs** |
| Pigtail | about **8 inches** total, clamped to the bracket **halfway along** |
| Electrical | 0.24 ± 0.02 µF, 1000 V DC (printed spec) |

Method: `bench` — part in hand, visual. Nothing here is metered.

## ⚠️ Two findings, not one

**1. The right lead is BLUE, not black.** Both models drew it `BK` by
symmetry with `W_PTS_R`, the right points lead, on the assumption that a
condenser lead matches the points lead it parallels. It does not. See
`docs/overturned-claims.md` #23 — and note the guard exemption that briefly
existed to accommodate the wrong colour.

**So blue has THREE roles on this bike**: brake lamp feed, fused headlight
supply, and this. The first two are measured open to each other; this is a
third net again.

**2. It earths to the FRAME, not the engine.** Two mounting tabs,
metal-to-metal, and both models had it on `GND_ENG`. That node's note
already admits it is broader than its name — "grounds through its own
mounting" — so the drawing is not wrong, but the *path* is frame, not case.

⚠️ **THE FRAME IS BEING POWDER COATED.** This is another component that
loses its earth to the coating, alongside the left cluster and the engine
strap. Either mask both tab landings or give the bracket a ground wire it
has never had. **A points ignition with no condenser earth burns its
contacts.**

## Not captured

- Whether the two tabs are both electrically necessary or one is just
  mechanical support.
- What the two male bullets mate on the harness side. The points leads are
  the obvious candidate, but that is inference, not observation.
