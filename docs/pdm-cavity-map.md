# PDM cavity map — MTA 0301370

✅ **CONFIRMED 9 Sep 2026 with the module in hand** `[bench]`. The grid is
**6 rows x 10 columns**, and a MiniVal spans **two rows within one column** —
rows (1,2), (3,4) or (5,6). Both assumptions this map was built on hold, so the
layout below stands as drawn.

**Module: 108 x 71 x 60 mm with the lid on.**

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
        c1        c2   c3    c4   c5    c6   c7        c8       c9      c10
 r1   F1 IN   ┌──────────┐┌──────────┐┌──────────┐   F2 IN    F7 IN   F10 IN
 r2   F1 OUT  │  K_MAIN  ││   K_HI   ││  K_HORN  │   F2 OUT   F7 OUT  F10 OUT
 r3   F4 IN   └──────────┘└──────────┘└──────────┘   F3 IN    F8 IN   spare
 r4   F4 OUT  ┌──────────┐┌──────────┐┌──────────┐   F3 OUT   F8 OUT  spare
 r5   F5 IN   │  K_COIL  ││   K_LO   ││  SPARE   │   F6 IN    F9 IN   spare
 r6   F5 OUT  └──────────┘└──────────┘└──────────┘   F6 OUT   F9 OUT  spare

      ── HOT ──  ────────── 6 relays ──────────  ────── SWITCHED ──────
```

**The relay block physically separates HOT from SWITCHED.** A mis-landed feed
wire would have to cross six columns of relays to put F3 on permanent power,
which is the failure the split exists to prevent. That is stronger than merely
placing them at opposite ends.

Column 1 holds exactly three fuse positions and HOT needs exactly three. The
asymmetry is forced by the 3/7 fuse split — a symmetric layout leaves 6 positions
each side and SWITCHED needs seven.

## Counts

| | |
|---|---|
| Cavities mapped | 60 of 60 |
| **Wired** — 11 fuses × 2 + **5 live** relays × 4 | **42** |
| Cavity plugs — 60 less wired | **18** |
| Spare fuse positions | **1** (column 10, rows 5–6) |
| Spare relay position | 1 (columns 6–7, rows 4–6) |

The plug count is unchanged from the five-relay plan: the sixth relay is a
*reserved position*, not a populated one, so its six cavities were never wired
and were already inside the 20.

⚠️ **12 fuse positions is the ceiling with six relays** (60 − 36 = 24 = 12).
**Eleven are now used.** #49 was settled by fusing the two unfused branches
together on F11 rather than separately, which is what left a spare at all — see
`SP_RLY` for why one fuse and not two.

**One spare fuse position remains**, at column 10 rows 5–6. The next fused
circuit fills the block.

## Still needed from the part

⚠️ **The relay FOOTPRINT is the last open item** — how many cavities one covers,
and in what shape. This map assumes **3 rows x 2 columns = 6**, from the
catalogue's "30 MiniVal **or** 10 micro relays" over 60 cavities.

Adjacency is settled `[photo]` and the grid is settled `[bench]`. What remains is
one look with a relay in hand, which arrives with the Cycle Terminal order. If a
relay turns out to cover a different shape, only the relay block moves — the
fuse columns and the HOT/SWITCHED separation are unaffected.

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
