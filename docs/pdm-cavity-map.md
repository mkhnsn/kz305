# PDM cavity map — MTA 0301370

✅ **CONFIRMED 9 Sep 2026 with the module in hand** `[bench]`. The grid is
**6 rows x 10 columns**, and a MiniVal spans **two rows within one column** —
rows (1,2), (3,4) or (5,6). Both assumptions this map was built on hold, so the
layout below stands as drawn.

**Module envelope: 107.6 x 72 x 60 mm with the lid on** `[datasheet]` — the
manufacturer's dimensioned drawing (`parts/mta-0301370-dimensions.png`). The
9 Sep bench calipers read 108 x 71 x 60, so the two agree to within a
millimetre; use the datasheet figures for enclosure and mounting layout.
**Cavity pitch: 7.91 mm rows, 7.67 mm columns** — a near-square grid `[bench]`.

## The grid

**6 rows × 10 columns = 60 cavities.** That factorisation is the one that makes
both of the catalogue's capacity claims fall out at once:

- a **fuse** spans 2 cavities *within a column* → 3 per column × 10 = **30 MiniVal** ✓
- a **relay** spans 3 rows × 2 columns → 2 per column-pair × 5 = **10 micro relays** ✓

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

## Still needed from the part

### The relay's PINS are a 2 x 2 — confirmed by the pitch

Song Chuan 303 pins are 8.1 x 7.8 mm apart. Against the measured pitch:

    8.1 / 7.91 = 1.02 pitches
    7.8 / 7.67 = 1.02 pitches

**Both land on adjacent cavities.** The four pins occupy a clean 2 x 2 block, not
the 3 x 2 an earlier draft of this map implied.

⚠️ **But the body is 16 x 15 mm over a pin block only ~8 mm square**, so it
overhangs and blocks neighbouring cavities. The catalogue's **10 relays in 60
cavities = 6 cavities each** is consistent with that: **4 pinned, 2 blocked.**

### ⚠️ What is still open is the footprint's ORIENTATION

Six cavities can be **3 rows x 2 columns** or **2 rows x 3 columns**, and they
give different layouts:

| | Relays per column-group | Column-groups in 10 | Total |
|---|---|---|---|
| 3 rows x 2 cols | 2 | 5 | **10** ✅ matches the catalogue |
| 2 rows x 3 cols | 3 | 3 | 9 |

The 3 x 2 orientation is the one that yields the catalogue's ten, so this map
keeps it. **Confirm with a relay in hand** when the Cycle Terminal order lands.

If it turns out to be 2 x 3, only the relay block moves — the fuse columns and
the HOT/SWITCHED separation are unaffected.

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
- [ ] **Which cavity of a relay footprint is 30 / 85 / 86 / 87**, and which two
      of the six are unused. Six cavities, four pins. Until this is read, the
      relay rows above name a footprint, not a pinout.
- [x] ~~Whether the moulding fixes fuse positions.~~ **Confirmed** — fuses pair
      (1,2) (3,4) (5,6) within a column, three per column, exactly as assumed.

⚠️ **The 10 unused-in-footprint cavities still need plugs.** The module seals at
the wire-entry face, so a relay body on top does not close a hole in the bottom.
They are already inside the 20.

## Build rule

Write the map down **as it is built**, correcting this file in place — cavity,
circuit, wire colour, gauge. This project has had to renumber two connectors
after reading them off a diagram rather than off the part.
