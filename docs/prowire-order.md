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

## 4. Splice hardware — SETTLED

**Step-down insulated butt splices, yellow-to-blue.** That is the right choice
and the arithmetic backs it: two 16 AWG conductors together are about 2 mm²,
which is 14 AWG equivalent, so the pair goes in the **yellow** (12–10) barrel and
the single leg in the **blue** (16–14). A straight blue-to-blue would not close
on the pair.

⚠️ **Blue-to-red is now the rarer case.** With the harness all 16 AWG, the only
places a 16-to-18 step-down applies are joints onto retained pigtails. Order a
few, not a handful.

| Item | Qty |
|---|---|
| Step-down butt splice, **yellow-to-blue** | 35 + spares — **45** |
| Step-down butt splice, blue-to-red | ~6 |

## 5. Heat shrink and sleeving — Prowire

Adhesive-lined dual wall, over every splice. Sizing is simple now the harness is
one gauge — every conductor is 2.4 mm and every splice barrel is a yellow butt
splice:

| Item | For | Qty |
|---|---|---|
| Adhesive-lined 3:1, **1/2 in** | over a yellow-barrel step-down splice | ~12 ft |
| Adhesive-lined 3:1, **3/16 in** | single-wire ends, terminal necks | ~8 ft |
| Braided sleeving or split loom, 1/2 in — trunk | | 10 ft |
| Braided sleeving or split loom, 1/4 in — branches | | 25 ft |

Buy roughly double on the adhesive shrink — a splice that has to be redone
consumes two lengths.

**Already in hand:** HD nickel-plated ring terminals, cloth harness tape.

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
