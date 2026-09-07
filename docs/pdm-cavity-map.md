# PDM cavity map — MTA 0301370

⚠️ **PROVISIONAL.** The grid and the fuse row-pairing are read off product
photographs, not off the part. Confirm both before the first terminal goes in,
and correct this file rather than working around it.

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

- [ ] ⚠️ **Confirm two relays can sit ADJACENT.** Cycle Terminal's 4-circuit
      MP280 box carries an explicit warning: *"Only 1 Relay per housing! You
      cannot fit 2 relays side by side."* That is 8 cavities holding either 4
      fuses **or one relay** — so the relay body overhangs its four pins by a
      wide margin.
      This layout puts **two relays in every column-pair**, stacked. If the
      bodies foul, the six-relay plan collapses to three.
      **MTA's own catalogue says the 0301370 takes 10 micro relays**, which
      implies adjacency is designed in — 60 cavities over 10 relays is exactly
      the 6-cavity footprint assumed here. But that is inference from a capacity
      claim, and the CT warning is a direct observation on a different housing.
      ** THE RELAY'S NUMBERS ARE NOW KNOWN, so this is one measurement away. **
      Song Chuan 303: body **16 x 15 mm**, pins **8.1 x 7.8 mm** apart, blades
      2.8 x 0.8 mm. Measure the module's cavity PITCH and the answer falls out —
      a relay needs `ceil(16/pitch)` x `ceil(15/pitch)` cavities of clearance,
      and two abreast need twice the width.
      Settle it with the module in hand before the first terminal goes in.
- [ ] **Confirm 6 × 10**, and that fuses pair rows (1,2) (3,4) (5,6).
- [ ] **Which cavity of a relay footprint is 30 / 85 / 86 / 87**, and which two
      of the six are unused. Six cavities, four pins. Until this is read, the
      relay rows above name a footprint, not a pinout.
- [ ] **Whether the moulding fixes fuse positions** or a fuse can sit in any
      adjacent row pair. The layout assumes fixed pairs.

⚠️ **The 10 unused-in-footprint cavities still need plugs.** The module seals at
the wire-entry face, so a relay body on top does not close a hole in the bottom.
They are already inside the 20.

## Build rule

Write the map down **as it is built**, correcting this file in place — cavity,
circuit, wire colour, gauge. This project has had to renumber two connectors
after reading them off a diagram rather than off the part.
