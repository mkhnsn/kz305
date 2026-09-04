# Prowire order sheet

Generated from `models/kz305-rebuild.yml`, 4 Sep 2026. Quantities are
**order** quantities, not design quantities — see the note at the foot.

## 1. TXL wire — 17 SKUs

⚠️ **Solid colours only.** The rebuild uses no tracer wire; identification is
printed heat-shrink plus `docs/label-schedule.md`. Do not substitute a striped
wire for a missing solid.

**Prowire sells by the foot.** The 25/50/100 ft steps in an earlier draft of this
sheet were an assumption about spools and they were wrong — they cost **$120** on
their own. Order the footage, not a spool.

Prices below are per foot as quoted 4 Sep 2026.

| Gauge | Colour | Item | $/ft | Cond. | **Order ft** | **$** |
|---|---|---|---|---|---|---|
| 18 | BK | `TXL-18-0` | 0.257 | 16 | **75** | 19.28 |
| 18 | BN | `TXL-18-1` | 0.228 | 12 | **45** | 10.26 |
| 18 | GY | `TXL-18-8` | 0.175 | 9 | **35** | 6.12 |
| 18 | GN | `TXL-18-5` | 0.211 | 9 | **35** | 7.38 |
| 18 | YE | `TXL-18-4` | 0.254 | 2 | 10 | 2.54 |
| 18 | BU | `TXL-18-LB` | 0.288 | 2 | 10 | 2.88 |
| 16 | BN | `TXL-16-1` | 0.234 | 8 | **30** | 7.02 |
| 16 | BU | `TXL-16-LB` | 0.263 | 8 | **30** | 7.89 |
| 16 | YE | `TXL-16-4` | 0.414 | 6 | 20 | 8.28 |
| 16 | RD | `TXL-16-2` | 0.439 | 4 | 15 | 6.58 |
| 16 | BK | `TXL-16-0` | 0.450 | 3 | 12 | 5.40 |
| 16 | GN | `TXL-16-5` | 0.461 | 1 | 8 | 3.69 |
| 14 | WH | `TXL-14-9` | 0.510 | 2 | 8 | 4.08 |
| 14 | YE | `TXL-14-4` | 0.613 | 2 | 10 | 6.13 |
| 14 | BN | `TXL-14-1` | 0.542 | 1 | 6 | 3.25 |
| 12 | RD | `TXL-12-2` | 0.949 | 3 | 12 | 11.39 |
| 12 | BK | `TXL-12-0` | 1.501 | 1 | 6 | 9.01 |

**≈ $121** for 89 conductors, against $242 for the same wire in spool steps.

### Where the money actually is

⚠️ **The heavy gauges are 43% of a spool-step order for 9 of 89 conductors.**
`12 AWG BK` alone is **$1.50/ft** — 3.3x the red, 6x the 18 AWG grey — and it
exists for **one wire**, `W_RR_GND`. In spool steps that single conductor cost
$37.52. At 6 ft it costs $9.01.

Colour also moves the price 2–3x *within* a gauge: 16 AWG brown is $0.234 and
16 AWG green is $0.461.

### Three optional cuts

| Cut | Saves | Cost |
|---|---|---|
| **`W_ALT` → drop `14 AWG YE`** if the stator has its own pigtail like the pod does | $6.13 | none, if true — **check the stator first** |
| **`W_HEAD_LO` → 18 AWG GN**, dropping the `16 AWG GN` SKU | $3.69 | 18 AWG is ~10 A rated and the beam is 4.2 A on filament over a short run |
| **The three 16 AWG BK grounds → 18 AWG BK**, dropping that SKU | ~$2.30 | horn ground is 2 A, headlight 4.2 A — both comfortable on 18 |

All three together: **≈ $109**, and two fewer SKUs.

### ⚠️ Do not shave below this

Getting to $100 means cutting into the margin, and **a re-order costs more in
shipping than the wire saved.** The margin above is roughly 1.5x the estimate,
which covers crimps that get redone and the build-in-place approach where wire is
trimmed on the bike rather than cut to a list.

### ⚠️ `TXL-16-1` brown is backordered

Flagged at 50 ft in the cart and likely at 30 ft too. That may split the
shipment and add a second delivery charge — worth asking for a lead time before
checkout rather than after.

## 2. Heavy cable — 4 conductors, NOT TXL

TXL runs roughly 24 to 8 AWG, so 6 AWG is a different product. None of it enters
the PDM and all four terminate in lugs.

| Item | Qty |
|---|---|
| 6 AWG welding or battery cable, **RED** | 6 ft |
| 6 AWG welding or battery cable, **BLACK** | 8 ft |
| Tinned copper lugs, 6 AWG — sizes to suit the battery, solenoid and engine studs | 8 + spares |
| Adhesive heat-shrink boots for the lugs | 8 |

Fine-strand **welding** cable is preferred over battery cable for flexibility
around the engine. `W_ENG_GND` carries the whole cranking return.

## 3. Splice heat-shrink — adhesive-lined, dual wall

The two feed buses are cascades, so the physical joint count is much higher than
the splice count in the drawing:

| | |
|---|---|
| Splice nodes in the model | 14 |
| **Physical 2-into-1 joints** | **38** |
| Less `SP_POD_GND`, which is inside the retained pod pigtail | −3 |
| **To build** | **35** |

`SP_SW` alone is 8 joints and `SP_HOT` is 4.

| Item | Qty |
|---|---|
| Adhesive-lined 3:1, **1/4 in** — over a 2-into-1 on 18/16 AWG | ~6 ft |
| Adhesive-lined 3:1, **3/8 in** — the heavier bus joints | ~3 ft |
| Adhesive-lined 3:1, **1/8 in** — single-wire ends and terminal necks | ~6 ft |

Buy roughly double. A splice that has to be redone consumes two lengths.

## 4. Labels

`docs/label-schedule.md` — **two per wire, each naming the far end.** With no
tracers, these *are* the identification scheme.

⚠️ The generated schedule currently lists **205** labels because it counts every
cable in the model. Subtract the 13 retained-pigtail conductors: **about 178
labels for 89 wires.**

⚠️ **Printable heat-shrink is usually a printer-specific consumable**, not a
generic Prowire line. Check whether they stock printable sleeve or whether this
needs a Brady/Dymo-type cartridge instead — this is the one line most likely not
to be orderable here.

## 5. Loom and protection

| Item | Qty |
|---|---|
| Braided sleeving or split loom, 1/2 in — main trunk | 10 ft |
| Braided sleeving or split loom, 1/4 in — branches | 25 ft |
| Harness tape, non-adhesive cloth type | 2 rolls |

Trunk extent is about 1.4 m; branches are short and numerous.

## 6. Tools — check before ordering elsewhere

- **MTA 280 crimper** for the `1708338-L` / `1708339-L` terminals already in
  hand. Open-barrel, and the correct die matters more on a sealed terminal
  because the seal has to sit right behind the crimp.
- **090-series crimper** for the connector order (#37).
- A **pull tester** is not needed, but ⚠️ **pull-test the first 18 AWG crimp by
  hand** — 18 AWG is 0.82 mm², which sits in the gap between MTA's stated CSA
  bands, and 10 `1708337-L` are in the box as the fallback.

---

## These are ORDER quantities

Design quantities are in the model and are roughly a third of these. The margin
covers crimps that get redone, the build-in-place approach where wires are
trimmed on the bike rather than cut to a list, and a design that has moved
several times since the MTA order and may move again.

Gauges are sized for **incandescent** lamps, so nothing here changes if the LED
conversion is deferred.
