# Prowire order sheet

Generated from `models/kz305-rebuild.yml`, 4 Sep 2026. Quantities are
**order** quantities, not design quantities — see the note at the foot.

## 1. TXL wire — 10 SKUs, all 16 AWG above 14

⚠️ **Solid colours only.** No tracer wire; identification is printed heat-shrink
plus `docs/label-schedule.md`.

**The harness is all 16 AWG.** A stripped stock conductor measures 1.29–1.45 mm
against 16 AWG's 1.291 mm nominal `[bench 4 Sep 2026]` — Kawasaki used 16, and
the "common size is 18 AWG" label it replaced was never measured. Consolidating
to match collapsed **15 SKUs to 10** and left **one cavity seal** instead of two.

### Prowire tier structure — the break is at 50 ft

| | 10 ft | 25 ft | **50 ft** | 100 ft |
|---|---|---|---|---|
| 16 BK | .480 | .450 | **.304** | .229 |
| 16 RD | .469 | .439 | **.297** | .223 |
| 16 BU | .415 | .389 | **.263** | .196 |

**A consistent 32% unit drop at 50 ft.** 25 ft of 16 BK is $11.25 and 50 ft is
$15.20 — twice the wire for 1.35x the money. ⚠️ **If a line needs more than about
25 ft, buy 50.** Minimum is 10 ft, not 25.

### The order

| Gauge | Colour | Item | Cond. | Need | **Buy** | $ |
|---|---|---|---|---|---|---|
| 16 | BN | `TXL-16-1` | 21 | ~63 ft | **100** | ~19 |
| 16 | BK | `TXL-16-0` | 19 | ~57 ft | **100** | 22.90 |
| 16 | YE | `TXL-16-4` | 10 | ~30 ft | **50** | ~14 |
| 16 | BU | `TXL-16-LB` | 10 | ~30 ft | **50** | 13.15 |
| 16 | GN | `TXL-16-5` | 10 | ~30 ft | **50** | ~16 |
| 16 | GY | `TXL-16-8` | 9 | ~27 ft | **50** | ~15 |
| 16 | RD | `TXL-16-2` | 4 | ~12 ft | 15 | ~7 |
| 14 | WH | `TXL-14-9` | 2 | ~5 ft | 10 | ~5 |
| 12 | RD | `TXL-12-2` | 3 | ~10 ft | 12 | 11.39 |
| 12 | BK | `TXL-12-0` | 1 | ~3 ft | 10 | 15.01 |

**≈ $140**, and the two 100 ft lines are deliberate — at $0.229/ft the second
50 ft costs $7.70, which is the cheapest insurance in this build.

⚠️ **Three lines are estimated.** I have real tier tables only for 16 BK, RD, BU
and TAN; GN, GY, YE and BN are extrapolated from the consistent 32% pattern.
Check them in the cart.

### The one line that cannot be fixed

**`TXL-12-0` at $1.501/ft, 10 ft minimum, for one 3 ft wire** — `W_RR_GND`, the
charging return. It cannot fold into another SKU: black is ground-only, and a
~20 A return will not go to 16 AWG. $15 for $4.50 of wire is simply the cost of
that circuit.

### 16 AWG black is cheaper than 18 AWG black

At the 100 ft tier: **$0.229 against $0.257.** The heavier wire costs less on the
highest-count colour, which is why consolidating came out a wash on cost rather
than a penalty.

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
