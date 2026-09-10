# PDM cavity map — MTA 0301370

✅ **CONFIRMED 9 Sep 2026 with the module in hand** `[bench]`. The grid is
**6 rows x 10 columns**, and a MiniVal spans **two rows within one column** —
rows (1,2), (3,4) or (5,6). Both assumptions this map was built on hold, so the
layout below stands as drawn.

✅ **RELAY FIT CONFIRMED 10 Sep 2026 with relays in hand** `[bench]`. Micro 280
relays come in **two sizes — 4-way (a 2 x 2 of cavities) and 6-way (3 x 2)** — and
both were bought and both fit. They seat as this map draws them, and **the bodies
do not overhang into a neighbouring relay's cavities**: the module was loaded up
solid with relays (unpinned) and every one seated. **A relay costs its own way
count and nothing more.**

**Module envelope: 107.6 x 72 x 60 mm with the lid on** `[datasheet]` — the
manufacturer's dimensioned drawing (`parts/mta-0301370-dimensions.png`). The
9 Sep bench calipers read 108 x 71 x 60, so the two agree to within a
millimetre; use the datasheet figures for enclosure and mounting layout.
**Cavity pitch: 7.91 mm rows, 7.67 mm columns** — a near-square grid `[bench]`.

## The grid

**6 rows × 10 columns = 60 cavities.** That factorisation is the one that makes
both of the catalogue's capacity claims fall out at once:

- a **fuse** spans 2 cavities *within a column* → 3 per column × 10 = **30 MiniVal** ✓
- a **relay** spans its own way count and no more — **4-way = 2 x 2, 6-way =
  3 x 2** `[bench 10 Sep]`. The catalogue's **10 micro relays** reads as the
  6-way case (10 x 6 = 60) rather than a physical ceiling on 4-way relays; this
  design needs six, so the gap never has to be resolved.

Numbering is **mating face, keyway up, left to right, top row first** — the
project convention, stated before the first terminal per the rule that cost two
connectors a renumber. So `cavity = (row − 1) × 10 + column`.

## Layout

```
        c1       c2      c3   c4     c5   c6       c7       c8       c9      c10
 r1   F1 IN    spare   ┌──────────┐┌──────────┐   F2 IN    F7 IN   F10 IN    spare
 r2   F1 OUT   spare   │  K_MAIN  ││   K_LO   │   F2 OUT   F7 OUT  F10 OUT   spare
 r3   F4 IN    spare   └──────────┘└──────────┘   F3 IN    F8 IN   F11 IN    spare
 r4   F4 OUT   spare   ┌──────────┐┌──────────┐   F3 OUT   F8 OUT  F11 OUT   spare
 r5   F5 IN    spare   │  K_COIL  ││  K_HORN  │   F6 IN    F9 IN    spare    spare
 r6   F5 OUT   spare   └──────────┘└──────────┘   F6 OUT   F9 OUT   spare    spare
                       ┌──────────┐┌──────────┐
                       │   K_HI   ││  SPARE   │   (rows 3-4 and 5-6 of c3-c6)
                       └──────────┘└──────────┘

      ──── HOT ────   ──── 6 relays ────   ──────── SWITCHED ────────
```

Each relay is **2 rows x 2 columns**. Three stack per column-pair, so six relays
fit in **four columns** — c3–c4 and c5–c6.

**The relay block still separates HOT from SWITCHED**, which is the property that
matters: a mis-landed feed wire would have to cross four columns of relays to put
F3 on permanent power.

## Counts

| | |
|---|---|
| **Fuse positions** | **18** — c1–c2 gives 6, c7–c10 gives 12 |
| Fuses used | 11 |
| **Spare fuse positions** | **7** |
| Relay positions | 6 |
| Relays fitted | 5, one spare |
| **Wired cavities** — 11 fuses x2 + 5 live relays x4 | **42** |
| **Cavity plugs** — 60 less wired | **18** |

All six relay positions are **4-way**. A 6-way relay fits the module fine
`[bench]` but takes 6 cavities, so substituting one costs two of the spare fuse
positions.

## Still needed from the part

### ✅ The 4-way relay's PINS are a 2 x 2 — predicted by the pitch, confirmed on the bench

Song Chuan 303 pins are 8.1 x 7.8 mm apart. Against the measured pitch:

    8.1 / 7.91 = 1.02 pitches
    7.8 / 7.67 = 1.02 pitches

**Both land on adjacent cavities.** The four pins occupy a clean 2 x 2 block, not
the 3 x 2 an earlier draft of this map implied — and relays in hand seat that way
`[bench 10 Sep]`. The larger **6-way relay takes a 3 x 2**, also as drawn. This
map's six positions are all **4-way**; swapping any one for a 6-way costs two
more cavities and eats into the spare fuse positions, so it is a decision, not a
drop-in.

#### ✅ The body does NOT steal a neighbour's cavities

An earlier draft read the **16 x 15 mm body over a ~8 mm pin block** as
overhanging into surrounding cavities, and inferred **4 pinned + 2 blocked** from
the catalogue's 10-relay figure — i.e. that a 4-way relay secretly costs six.
**That inference was wrong.** A 2 x 2 of this grid is 15.8 x 15.3 mm — the body
is the same size as its own footprint, so neighbouring relays butt against each
other rather than over each other. Loading the module solid with relays confirmed
it: every one seated `[bench 10 Sep]`. The catalogue's 10 is the **6-way** case,
not a tax on the 4-way.

Consequences, all of which favour this design:

- A **4-way relay costs 4 cavities**, not 6. The Counts table below was already
  drawn that way and now stands on the part rather than on an assumption.
- There are **no unused-in-footprint cavities** to reason about — every cavity is
  either wired or free for a plug.
- **The orientation question is closed.** It was only ever open because six
  cavities could be 3 x 2 or 2 x 3; the 6-way is a 3 x 2, and this map's relays
  are 4-way anyway.

- [x] ~~**Confirm two relays can sit adjacent.**~~ **RESOLVED 6 Sep 2026** from
      the vendor's product photo of a populated `0301370`: a **row of relays sits
      shoulder to shoulder** along one edge with fuses filling the rest. The
      six-relay layout stands.
      Cycle Terminal's *"Only 1 Relay per housing! You cannot fit 2 relays side by
      side"* turns out to be specific to **their 4-circuit MP280 box** — 8
      cavities where one relay body spans most of the housing — and not a property
      of micro 280 relays. `[photo 6 Sep 2026]`
      The photo also shows relays **grouped at one end with fuses in the
      remainder**, which is the arrangement this map already assumes.
- [x] ~~Confirm 6 × 10, and that fuses pair rows (1,2) (3,4) (5,6).~~ **Both confirmed 9 Sep 2026** `[bench]`.
- [x] ~~**Confirm the relay footprint and its orientation.**~~ **RESOLVED 10 Sep
      2026** `[bench]` — relays of both sizes in hand, 4-way (2 x 2) and 6-way
      (3 x 2). Both seat as drawn and neither overhangs a neighbour.
- [ ] **Which cavity of the 4-way 2 x 2 is 30 / 85 / 86 / 87.** Four cavities,
      four pins, so nothing is spare — but until the pin roles are read off the
      relay, the relay rows above name a footprint, not a pinout. **This is now
      the only thing the relay block still owes.**
- [x] ~~Whether the moulding fixes fuse positions.~~ **Confirmed** — fuses pair
      (1,2) (3,4) (5,6) within a column, three per column, exactly as assumed.

⚠️ **All 18 unwired cavities need plugs.** The module seals at the wire-entry
face, so a relay body on top does not close a hole in the bottom. With the
footprint settled at four cavities there is no separate under-body population to
count: 60 cavities less 42 wired is **18**, the figure in the Counts table.

## Build rule

Write the map down **as it is built**, correcting this file in place — cavity,
circuit, wire colour, gauge. This project has had to renumber two connectors
after reading them off a diagram rather than off the part.
