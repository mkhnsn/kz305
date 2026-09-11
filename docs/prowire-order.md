# Prowire order sheet

Generated from `models/kz305-rebuild.yml`, 4 Sep 2026. Quantities are
**order** quantities, not design quantities — see the note at the foot.

## Outstanding after order Q25134 — `TXL-14-4`, ~8 ft

`W_ALT` went back to 14 AWG on 6 Sep because the Furukawa QLW 250 at the
regulator will not take anything smaller. That re-added a SKU the 4 Sep
consolidation had removed, and the order had already closed.

**Not chased, and it blocks nothing.** In order:

**RESOLVED 6 Sep 2026 — 8 ft of M22759/16-14 yellow from Corsa Technic**, not
TXL. MIL-spec ETFE Tefzel: same 2.0 mm² conductor and 19/27 stranding, but a
**2.36 mm OD against TXL 14's 2.59–2.70** and a 150 °C rating against 125.

⚠️ **It is the only non-TXL run in the harness**, and the thinner wall is the
thing to watch — any seal sized for TXL 14 will be loose on it. It meets exactly
one sealed interface, the Furukawa QLW at the regulator, whose kit seals are
stated for 2–3 mm² wire. 2.36 mm sits inside that. Confirm at assembly.

⚠️ **ETFE is tougher to strip than XLPE** — right die, and check for nicked
strands.

⚠️ **It cannot delay the build.** The charging circuit is among the last things
connected, and its connectors are in the Corsa Technic order which has not been
placed either. There is no sequence where this is the long pole.

### If a substitute is ever needed

The two AC leads are **isolated in their own connector at the regulator and touch
nothing else in the harness**, and the factory model records that the two AC legs
are **interchangeable** into a single-phase bridge — so swapping them is harmless.

Yellow is there to match stock, not to disambiguate: the scheme has no role for AC
phases, and its own note flags yellow as colliding with the ignition role. Spare
14 AWG white would serve at no real cost, though the order only leaves about 5 ft
of it against ~6 ft needed.

### Everything else still covers

`12 AWG BK` now carries `W_GND_MAIN` as well as `W_RR_GND` — two conductors
against 10 ft ordered. `16 AWG YE` drops from 10 conductors to 8 against 50 ft.

## 1. TXL wire — 11 SKUs, all 16 AWG above 14

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

## 4. Splice hardware — Molex Versakrimp PARALLEL splices

**Changed 5 Sep 2026 from step-down butt splices.** Parallel "shorty" splices
take every wire at a node in from the *same* end and crimp once, so one splice
serves a whole node instead of a cascade of two-into-ones.

**About $10 against $25.20**, and 14 crimps instead of 35.

⚠️ **It also makes the drawing honest.** `SP_HOT` and `SP_SW` are modelled as
single nodes with a note that the cascade was a build form. With a parallel
splice they *are* single nodes — the model and the bench now agree.

### Sizing — from the published bore, by circle packing

The splice datasheets give the **bore ID**, which beats inferring capacity from
the AWG rating. 16 AWG TXL's conductor bundle is **1.29 mm** OD — matching the
1.29–1.45 mm measured off the stock harness.

Minimum bore to insert N conductors, from optimal circle-in-circle packing plus
10% for actually getting them in:

| N | Ideal | Practical |
|---|---|---|
| 2 | 2.58 | 2.84 |
| 3 | 2.78 | **3.06** |
| 4 | 3.11 | 3.43 |
| 5 | 3.48 | 3.83 |
| 9 | 4.68 | 5.15 |

| Splice | Molex | OD | Bore ID | Wall | Takes |
|---|---|---|---|---|---|
| 22-18 | `19207-0001` | 3.30 | 1.50 | 0.90 | 1 |
| 16-14 | `19205-0001` | 4.10 | 2.30 | 0.90 | **1** |
| **12-10** | **`19205-0003`** | 5.70 | **3.30** | 1.20 | **3** |
| **8 GA** | **`19205-0004`** | 7.50 | **4.20** | 1.65 | **5** |

⚠️ **Drop the 16-14 entirely.** Its 2.30 mm bore will not take two 16 AWG
conductors — they need 2.84 mm. A 16-14 *butt* splice takes one wire per end,
which is a different geometry. Even `SP_TAIL`'s two wires go in a 12-10.

**Two independent methods agree on 3 per 12-10 barrel**: 85% fill by area, and
circle packing by diameter. Four is geometrically possible (3.11 vs 3.30) but
leaves 0.19 mm of total clearance, which is not something you insert stranded
ends into.

### Which barrel per node

| Splice | Wires | Barrel |
|---|---|---|
| eight 3-wire nodes + `SP_TAIL` | 2–3 | **12-10** |
| `SP_SIG_L` `SP_SIG_R` | 4 | **8 GA** |
| `SP_HOT` | 5 | **8 GA** |
| `SP_SW` | 9 | **6 GA** — see below |
| `SP_POD_GND` | 4 | — inside the retained pod pigtail |

### `SP_SW` is one crimp on a 6 GA

Nine wires need **4.68 mm ideal / 5.15 mm practical**. The 8 GA bore is 4.20 mm
and will not take them — but the **6 GA** estimates at 5.1–5.3 mm from two
independent methods, which clears it.

⚠️ **Prowire's note says the `Sargent 4235 CT` only covers up to 8 ga**, with
6 ga needing the `Molex 19294-0008`. That is moot here — the bolt-cutter-style
lug crimper already on the bench handles the larger barrels, and it is needed
anyway for the eight 6 AWG battery and engine lugs.

⚠️ **The 6 GA bore is an ESTIMATE, not a datasheet figure** — the last
extrapolation on this page was wrong by 0.9 mm. If it measures under 5.15 mm,
fall back to two 8 GA crimps with one link wire:

    A:  K_MAIN 87 in + 3 branches + link   = 5 wires
    B:  link + 4 branches                  = 5 wires

Buy a few 6 GA either way; they are pennies and the fallback costs nothing.

### Order

| Item | Molex | Qty | $ |
|---|---|---|---|
| Parallel splice **12-10 GA** | `19205-0003` | **25** | 4.55 |
| Parallel splice **8 GA** | `19205-0004` | **10** | 5.49 |
| Parallel splice **6 GA** | — | **5** | ~2.75 |

≈ **$13**, against $25.20 for step-down butt splices — and **13 crimps** rather
than 35: nine 12-10, three 8 GA, one 6 GA.

⚠️ **Make the first crimp a deliberate test** anyway. The 10% insertion allowance
is a convention, not a datasheet figure.

⚠️ **Do not buy the 595-piece kit** at $163.

⚠️ **These are uninsulated**, so the adhesive shrink is the insulation *and* the
strain relief — more so than with a butt splice, because every wire exits one
side and the barrel's far end has nothing holding it.

## 5. Heat shrink — Sumitomo W5DL 3:1 dual wall

**3/8″ covers every splice.** A 12-10 barrel is ~6 mm and a 5-wire bundle is
~6.2 mm; 3/8″ supplies at 9.5 mm, so it clears both.

| Need | Size | Item | Qty |
|---|---|---|---|
| 14 splices | **3/8″** | `W5DL-3/8-0` | 2 × 4 ft |
| Ring terminal necks | **3/16″** | `W5DL-3/16-0` | 2 × 4 ft |

Parallel splices are "shorty" and there are 15 rather than 35 joints, so this
drops from 3 lengths of 3/8″ to 2.

⚠️ **1/4″ still will not go over a splice** — 6.3 mm supplied against a ~6 mm
barrel plus wall. It remains the size that looks right and isn't.

⚠️ **Their table has a typo**: 1/8″ is listed recovering to 0.06 mm. The inch
column says 0.023″ = **0.58 mm**. Every other row converts correctly.

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

### Buy loose — the spool is not a break, checked 5 Sep 2026

    35 ft loose @ $0.437/ft  = $15.29
    100 ft spool             = $43.20   ($0.432/ft)

**A 1.1% discount.** The spool costs $27.91 more for 65 ft you do not need, and
only wins if the loose rate ever exceeds $1.23/ft.

⚠️ **The tier lesson from the wire does not transfer.** TXL drops **32% at the
50 ft break**, which is what makes "buy up to the break" right there. Clean Cut
is essentially flat-priced. The rule is **check the tiers**, not *buy up to the
break* — generalising the wrong one would have cost $28 here.

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
  ⚠️ MTA's own `9602455` hand crimp tool is listed for **UNSEALED** 280/480/630
  terminals. These are sealed. **Do not order it on the series match alone.**
- **090-series crimper** for the connector order (#37).
- ⚠️ **Pull-test the first crimp.** 16 AWG is 1.0 mm², mid-range in
  `1708338-L`'s 1.0–2.0 mm² band, so it should be clean — the 10 `1708337-L` in
  the box are the fallback if not.

### Depinning the MTA module `[bench 10 Sep 2026]`

**Tool: Aptiv `12094429`, already owned.** It fits MTA's F280.

1. **Pull the TPA** (`0301372`) first. Nothing moves while it's seated.
2. **Release both tangs**, one on each side of the terminal. A single blade takes
   two passes.

Inspect the tangs on anything you pull. A bent tang holds less well and can let
the wire back out under vibration. Re-form it or use a new terminal. A
double-bladed extractor would do both tangs at once; ConnectorID's `CID280ET`
is worth asking about if you ever order one.

## These are ORDER quantities

Design quantities are in the model and are roughly a third of these. The margin
covers crimps that get redone, the build-in-place approach where wires are
trimmed on the bike rather than cut to a list, and a design that has moved
several times since the MTA order and may move again.

Gauges are sized for **incandescent** lamps, so nothing here changes if the LED
conversion is deferred.
