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

### Actual cart, 4 Sep 2026 — **$144.51**

| Line | Ft | $ |
|---|---|---|
| `TXL-16-1` brown | 100 | 17.60 |
| `TXL-16-0` black | 100 | 22.90 |
| `TXL-16-4` yellow | 50 | 14.00 |
| `TXL-16-LB` light blue | 50 | 13.15 |
| `TXL-16-5` dark green | 50 | 15.60 |
| `TXL-16-8` gray | 50 | 12.45 |
| `TXL-16-2` red | 15 | 7.03 |
| `TXL-14-9` white | 10 | 5.46 |
| `TXL-12-2` red | 12 | 12.17 |
| `TXL-12-0` black | 10 | 16.03 |

The four extrapolated lines came in within a few percent of the 32%-drop
estimate, so the pattern holds across colours.

### ⚠️ Take light blue, not dark blue

Prowire stocks both within 3% of each other. **Dark blue and black are hard to
separate** in a headlight shell or under a seat with a torch — and black is
**ground-only** in this scheme precisely so a builder can trust it on sight.

Blue is 10 conductors and black is 19: the two biggest groups in the harness,
and the two you least want to confuse. The point of solid colours plus printed
labels is that the colour is readable *before* you read the label.

### `TXL-16-1` brown is backordered to 7 Sep

48,000 ft inbound, so it is a three-day wait rather than a supply problem.
⚠️ **Check whether it holds the whole order or ships split** — a second delivery
charge costs more than the three days are worth.

### The one line that cannot be fixed

**`TXL-12-0` at $1.501/ft, 10 ft minimum, for one 3 ft wire** — `W_RR_GND`, the
charging return. It cannot fold into another SKU: black is ground-only, and a
~20 A return will not go to 16 AWG. $15 for $4.50 of wire is simply the cost of
that circuit.

### 16 AWG black is cheaper than 18 AWG black

At the 100 ft tier: **$0.229 against $0.257.** The heavier wire costs less on the
highest-count colour, which is why consolidating came out a wash on cost rather
than a penalty.

## 2. Ring terminals — 22, and they do not fit on one stud

Every ground lands on `GND`, and each landing needs a ring:

| Gauge | Rings |
|---|---|
| 16 AWG | **19** |
| 12 AWG | 1 |
| 6 AWG (lugs) | 2 |

⚠️ **`GND` is drawn as "to bare chassis stud" and that is not buildable.**
Twenty-two rings will not stack on one post — the same objection that sent
`SP_SW` to a cascade, and worse here because two of them are 6 AWG lugs.

It needs a **ground bus bar** with several studs. And the choice is tied to
**#44**, still open: the engine strap carries **the whole cranking return, well
over 100 A**, and putting it on the same bar as nineteen signal grounds is
exactly what that issue says not to do.

**Do not buy ground hardware until #44 is decided.** Everything else here is
independent of it.

## 3. Heavy cable — 4 conductors, NOT TXL

TXL runs roughly 24 to 8 AWG, so 6 AWG is a different product. None of it enters
the PDM and all four terminate in lugs.

| Item | Qty |
|---|---|
| 6 AWG welding or battery cable, **RED** — `W_BAT_SOL`, `W_SOL_SM` | 6 ft |
| 6 AWG welding or battery cable, **BLACK** — `W_BAT_GND`, `W_ENG_GND` | 6 ft |
| Tinned lugs, 6 AWG, stud sizes to suit battery / solenoid / engine | 8 + spares |
| Adhesive heat-shrink boots for the lugs | 8 |

Fine-strand **welding** cable preferred for flexibility around the engine.

## 4. Splice hardware — SETTLED, with part numbers

**Molex uninsulated step-down butt splices**, and the arithmetic backs the
choice: two 16 AWG conductors are 2.0 mm² of copper but sit side by side, so they
need the **12–10** barrel, not the 16–14. The single leg goes in the 16–14 end.

| Item | Molex | $ | Qty |
|---|---|---|---|
| Step-down, **12-10 to 16-14** — the 2-into-1 | `19215-0023` | 0.72 | **45** |
| Step-down, 16-14 to 18-22 — retained pigtails only | `19215-0013` | 0.59 | 6 |

⚠️ **These are uninsulated**, so the adhesive shrink below is not optional — it is
the insulation *and* the strain relief.

## 5. Heat shrink — Sumitomo W5DL 3:1 dual wall

Sized against the real numbers. **One size covers all 35 splices**, not two as an
earlier draft said — every joint in this harness is the same 2-into-1 on the same
barrel, including the `SP_HOT` and `SP_SW` cascades.

| Need | Over | Down to | Size | Item |
|---|---|---|---|---|
| **35 splices** | 6.4 mm barrel | 2.4 mm wire | **3/8″** | `W5DL-3/8-0` |
| Ring terminal necks | ~4 mm | 2.4 mm wire | **3/16″** | `W5DL-3/16-0` |

⚠️ **1/4″ will NOT go over a splice.** Supplied ID is 6.3 mm against a 6.4 mm
barrel — it is the one size that looks right and isn't.

⚠️ **3/8″ recovers to 3.43 mm against a 2.4 mm wire**, so it does not close
tight on the single leg. **That is what the adhesive is for** — dual-wall glue
flows and fills the 1 mm gap. It is the correct choice anyway, because nothing
in the 3:1 range both clears the barrel and closes on the wire.

Sold in 4 ft lengths: 35 splices × ~40 mm ≈ 5 ft, so **3 lengths of 3/8″**
(~$24) and **2 of 3/16″** (~$14). Buy the spare — a splice redone consumes two.

⚠️ **Their table has a typo**: 1/8″ is listed recovering to 0.06 mm. The inch
column says 0.023″, which is **0.58 mm**. Every other row converts correctly.

## 5b. Flexo Clean Cut sleeving — no hot knife needed

Cuts with scissors, does not fray. Sized from bundle diameter, `d × √N × 1.15`,
and the footage derived from the **48 branch lengths measured off the old
harness** rather than estimated.

### The split is lopsided — it is almost all 1/4″

| | Branches | Raw need |
|---|---|---|
| 1/4″ | **48 of 50** | 20.1 ft |
| 1/2″ | 2 | 1.0 ft |

The old harness's branches are mostly 1–3 conductors. **1/4″ Clean Cut expands to
about 9.5 mm**, which covers up to roughly 8 conductors, so it swallows nearly
everything that leaves the trunk.

### The trunk is not one size

It thins out toward the back:

| Section | Conductors | OD | Sleeve |
|---|---|---|---|
| Front — headlight, both clusters, instruments, front signals | ~25–30 | 14–15 mm | **3/4″** |
| Rear — tail, brake, rear signals, flasher | ~10 | 9 mm | **1/2″** |

### Order

| Item | Ft | $ |
|---|---|---|
| `CCP025BK` 1/4″ | **35** | 15.30 |
| `CCP050BK` 1/2″ | **10** | 6.71 |
| `CCP075BK` 3/4″ | **10** | 8.40 |

≈ **$30**, and it retires the hot-knife line entirely.

**Margin is 1.6× on branches and 1.5× on the trunk**, for two reasons beyond
ordinary waste:

- ⚠️ **The old harness had no star ground.** The rebuild adds ~19 ground returns
  that run alongside existing branches, so every branch gets one conductor
  fatter than the measured geometry.
- Sleeving overlaps at each breakout, so 48 branches means 48 overlaps.

⚠️ **Check the spool pricing before buying by the foot.** Clean Cut lists "as low
as" rates and offers 50/75/100 ft spools, so a **50 ft spool of 1/4″ may beat
35 ft loose** — the same tier trap as the wire, where assuming a flat rate cost
$120.

## 6. Inline fuse holders — MP630, NOT a Prowire line

`MF` and `MF_RR` both take the **Metri-Pack 630 pull-to-seat ATC holder**,
`MP630 1214 ATC Set` — housing, cover, seal and loose terminals, about $5.75
each. All four wires are in the terminal's 12–14 AWG band:

| Holder | Wire | Gauge |
|---|---|---|
| `MF` | `W_MAIN_IN` | 12 AWG |
| `MF` | `W_MAIN_OUT` | 14 AWG |
| `MF_RR` | `W_RR_OUT` | 12 AWG |
| `MF_RR` | `W_RR_BATT` | 12 AWG |

⚠️ **They take ATC (regular blade) fuses, not MiniVal.** The PDM is MiniVal
throughout, so the build carries **two fuse form factors** and they do not
interchange. Buy an **ATC 20 A and ATC 30 A** separately from the MiniVal kit.

⚠️ **Pull-to-seat**: the wire threads through the seal and housing *before* it is
crimped, then pulls back to lock. Same discipline as the MTA cavities and the
printed labels — **seal on, label on, crimp last.** A crimped terminal will not
pass back through.

Buy a couple of spare `MP630-1214 F` terminals at $0.48 — cheap insurance on a
pull-to-seat joint you cannot redo without withdrawing the lead.

## 8. Tools

- **MTA 280 crimper** for the `1708338-L` terminals already in hand. The die
  matters more on a sealed terminal because the seal must sit right behind the
  crimp.
- **090-series crimper** for the connector order (#37).
- ⚠️ **Pull-test the first crimp.** 16 AWG is 1.0 mm², mid-range in
  `1708338-L`'s 1.0–2.0 mm² band, so it should be clean — the 10 `1708337-L` in
  the box are the fallback if not.

## These are ORDER quantities

Design quantities are in the model and are roughly a third of these. The margin
covers crimps that get redone, the build-in-place approach where wires are
trimmed on the bike rather than cut to a list, and a design that has moved
several times since the MTA order and may move again.

Gauges are sized for **incandescent** lamps, so nothing here changes if the LED
conversion is deferred.
