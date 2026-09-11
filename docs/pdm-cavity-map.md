# PDM cavity map — MTA 0301370

**The build reference for the PDM.** Confirmed against the module and relays in
hand, 9–10 Sep 2026 `[bench]`. Part numbers and quantities are in
`docs/part-selection.md`.

| | |
|---|---|
| Grid | **6 rows x 10 columns = 60 cavities**, pitch 7.91 mm rows x 7.67 mm columns |
| Envelope | **107.6 x 72 x 60 mm lidded** `[datasheet]`, drawing at `parts/mta-0301370-dimensions.png` |
| Fuse | 2 cavities **within a column**, rows (1,2) (3,4) or (5,6), three per column |
| Relay | its own footprint and no more: **4-way = 2 x 2**, 6-way = 3 x 2. Bodies don't overhang |

**Numbering:** mating face, keyway up, left to right, top row first. So
`cavity = (row − 1) × 10 + column`.

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

**The relay block separates HOT from SWITCHED.** That's the property that
matters: a mis-landed feed wire would have to cross four columns of relays to put
F3 on permanent power.

⚠️ **#45 may move F4 and F5 to SWITCHED.** If it's adopted, they cross the relay
block and this layout gets redrawn. Settle #45 before populating.

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

All six relay positions are **4-way**. A 6-way relay fits, but it takes 6
cavities, so substituting one costs two spare fuse positions and reopens the
rotation question for that position.

**Every unwired cavity gets a plug**, all 18. The module seals at the wire-entry
face, so a relay on top doesn't close a hole underneath.

## Relay pins — and why rotation doesn't matter

Read off the relay `[bench 10 Sep]`: **contacts 30/87 on one diagonal, coil 85/86
on the other.**

```
        30 ─────── 86
         │  ╲   ╱  │
         │    ╳    │
         │  ╱   ╲  │
        85 ─────── 87
```

A 2 x 2 accepts the relay 180° round, and nothing prevents it. **It doesn't need
preventing.** Rotation maps contact to contact and coil to coil. The contacts are
SPNO (non-polar) and the `-R1` coil has no polarity, so **a relay fitted backwards
works.**

⚠️ **This holds only for `-R1` resistor relays.** A `-D1` diode relay fitted
backwards is a dead short across the coil. Check any new relay's coil with a DMM
both ways round before fitting. See `docs/part-selection.md`, *Coil suppression*.

### Cavity convention

The relay can rotate but the wires can't, so each 2 x 2 has its diagonals fixed.
For a relay on rows *r, r+1* and columns *c, c+1*:

| Cavity | Role |
|---|---|
| (r, c) upper-left | **30** contact |
| (r+1, c+1) lower-right | **87** contact |
| (r, c+1) upper-right | **86** COIL+ |
| (r+1, c) lower-left | **85** COIL− |

The knockoff moulding reads the second coil pin as 86 or possibly 88. The
geometry is what matters. Re-read the marking if a genuine Song Chuan is bought.

## Build rules

- **Write the map as you build.** Correct this file in place: cavity, circuit,
  wire colour, gauge. Two connectors on this project had to be renumbered after
  being read off a diagram instead of the part.
- **One wire per cavity.** The feed buses are star points outside the module
  (`SP_HOT`, `SP_SW`).
- **Depinning:** pull the TPA (`0301372`), then release both tangs.
