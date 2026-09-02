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
