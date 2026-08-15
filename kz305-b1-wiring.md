# KZ305-B1 — Wiring Diagram Reference

Last updated: 2026-08-13 (added physical harness inspection findings)

Source: *Kawasaki Z250/KZ305 Service Manual 1979–1982*, printed page 255
(PDF page 261), in the 1981 KZ305-A supplement.

Diagram title as printed: **"KZ305-A1, A2, B1, C1, D1 Wiring Diagram
(U.S. and Canadian Models)"** — the B1 is named explicitly, so this is the
correct diagram for this bike. There is no separate B1 wiring diagram; the
B1 supplement's appendix (printed 298) lists no wiring section, and the
KZ305-D supplement (printed 303) also points back to page 255.

## Image files

| File | Use |
|---|---|
| `KZ305-B1-wiring-diagram.png` | 300 dpi, rotated upright. Everyday reference. |
| `KZ305-B1-wiring-diagram-600dpi.png` | 600 dpi, rotated upright. Zoom in on trace routing and connector detail. |

The original page is printed sideways; both files are rotated so the title
reads normally. **The image is the authority** — the tables below are a
convenience transcription and were read off a 40-year-old scan.

---

## Wire color codes

| Code | Color |
|---|---|
| BK | Black |
| Bl | Blue |
| Br | Brown |
| G | Green |
| Gy | Gray |
| LG | Light Green |
| O | Orange |
| R | Red |
| W | White |
| Y | Yellow |

Two-color leads are named primary-then-secondary: a yellow wire with thin
red stripes is "yellow/red" (Y/R). If red were the main color it would be
"red/yellow" (R/Y). This convention is from the base manual, printed 33,
item 18, and matters because Y/R and R/Y are different wires that both
appear in these tables.

---

## Switch continuity tables

Read as: in the given switch position, the listed wires are connected to
each other.

### Ignition switch

Columns as printed: Battery (W) · Ignition (Br) · Tail 1 (R/BK) · Tail 2 (R)

| Position | Connected |
|---|---|
| **ON** | W ↔ Br, and R/BK ↔ R |
| **OFF** | — none — |
| **LOCK** | — none — |
| **P (PARK)** | W ↔ R (single long bar spanning the full table) |

Park feeds the tail circuit from the battery with ignition dead — worth
keeping in mind when rewiring, since a modern fuse block layout often drops
this function by accident.

### Left handlebar

**Dimmer switch** — columns R/BK · Bl · R/Y

| Position | Connected |
|---|---|
| HI | R/BK ↔ Bl |
| LO | Bl ↔ R/Y |

Blue is the common terminal in both positions, which makes Bl the feed and
R/BK / R/Y the two beam outputs. ⚠️ Verify with a meter during harness
mapping — this is the one table where the scan is marginal, and getting the
common wrong would put both filaments on at once. **Still unresolved as of
13 Aug 2026** — the bench photos show the harness-side connector, not the
switch internals. See "Physical harness inspection" below.

**Turn signal switch** — columns G · O · Gy

| Position | Connected |
|---|---|
| R | O ↔ Gy |
| L | G ↔ O |

Orange is the common (flasher feed); green and gray are the two sides.

**Horn button** — columns BK · ground

| Position | Connected |
|---|---|
| Push | BK ↔ ground |

Horn switches the ground side, not the feed.

### Right handlebar

**Starter button** — columns Y/R · BK

| Position | Connected |
|---|---|
| Push | Y/R ↔ BK |

**Engine stop switch** — columns Br · Y/R

| Position | Connected |
|---|---|
| RUN | Br ↔ Y/R |
| OFF | — none — |

Note the shared Y/R: the stop switch feeds the starter button, so the
starter can't crank with the kill switch off. Preserve that interlock in
any rebuild.

---

## Components on the diagram

**Ignition (points, battery-and-coil):** two ignition coils (LEFT and
RIGHT), two sets of contact breaker points, two capacitors, two spark
plugs.

**Charging:** alternator (single-phase AC, yellow leads), combined
regulator/rectifier.

**Starting:** starter motor, starter relay, battery 12 V 10 AH.

**Protection:** main fuse 12 V 20 A, plus a multi-position fuse block.

**Switches:** ignition switch, front brake light switch, rear brake light
switch, neutral switch, left and right handlebar clusters.

**Other:** flasher (turn signal relay), horn, junction/6P connectors,
"Meter Accessory Leads" pickup points.

---

## Bulb ratings from the diagram

| Lamp | Rating |
|---|---|
| Headlight | 12 V 50/35 W (sealed beam) |
| Tail / brake light | 12 V 8/27 W |
| Turn signals, front and rear, each | 12 V 23 W |
| License plate light | 12 V 8 W |
| Speedometer light | 12 V 3.4 W |
| Tachometer light | 12 V 3.4 W |
| Neutral indicator | 12 V 3.4 W |
| High beam indicator | 12 V 3.4 W |
| Right turn indicator | 12 V 3.4 W |
| Left turn indicator | 12 V 3.4 W |

Total indicator and instrument load is ~20 W across six 3.4 W bulbs —
worth counting when sizing the LED conversion, because removing it shifts
that much extra load onto the shunt regulator.

---

## Physical harness inspection — 13 Aug 2026

Harness laid out flat on the bench and photographed in detail. What the
photos confirm, and what they don't.

### Confirmed against the bike

| Finding | Evidence |
|---|---|
| **Harness P/N `26001-12348`** | Woven cloth tag, "MADE IN JAPAN". A second tag appears on another branch. Read both under good light and log them — this identifies the harness variant independent of the diagram's A1/A2/B1/C1/D1 grouping. |
| **Fuse block matches the diagram** | Three glass fuses in the original black box, feeds in white, blue, and red. Consistent with the 20 A main plus 10 A × 2 on printed 255. Use as the baseline when laying out the 6-circuit blade block. |
| **Alternator is single-phase** | Short taped stub terminating in two yellow bullets — the stator pair, physically confirmed. Three-phase R/R units (SH775 etc.) stay off the table. |
| **Single chassis ground** | Exactly one yellow/black ring terminal on the entire harness. Everything returns through that one point. This is the single failure point the star ground bus is meant to replace on a powder-coated frame. |

### Condition

Consistent with the water-in-the-sleeve finding that condemned the harness:

- Green corrosion on **both** starter relay studs
- HT lead insulation chalked and cracking
- Bullet housings clouded, oil-soaked, brittle

### Still open

- **Dimmer switch common** (Bl vs. R/BK / R/Y) is *not* resolved by these
  photos. The continuity is internal to the left handlebar cluster; the
  photos show the harness-side connector only. Six-wire white connector —
  green, orange, gray, blue, and two reds — is probably the left-bar 6P,
  but this has to come off a meter on the switch itself.

### ⚠️ Do not map colors from photographs

Forty years of oil has shifted the apparent colors: white reads as tan,
blue/white reads as gray in several shots. **Ring out every wire
end-to-end** during mapping rather than trusting the camera or this
document.

### Photos still wanted

- Left handlebar switch cluster
- Right handlebar switch cluster
- Any connector shot face-on with the pins visible

---

## Notes for the harness rebuild

- **Shunt regulator.** The stock unit is an open-circuit type that dumps
  surplus output as heat. Cutting load with LEDs makes it work *harder*,
  not easier. Verify 14.0–14.5 V at 3,000–5,000 rpm on the bench run and
  check the regulator body temperature, not just the voltage.
- **Never** disconnect the regulator/rectifier with the ignition on, and
  never disconnect the battery while running. Either damages the unit.
- **Grounds are chassis returns** throughout — the horn, the lamps, and the
  starter all rely on frame ground. Powder coat is an insulator, so every
  ground point on the returning frame needs masking or scraping back to
  bare metal.
- **Stator check values** (from the electrical chapter, printed 159):
  coil resistance 0.36–0.54 Ω, output about 75 V AC at 4,000 rpm across the
  yellow leads, and each yellow lead must read infinity to ground.
- **Ignition coil values** (printed 161): primary 3.6–5.4 Ω,
  secondary 11–17 kΩ.
- **Capacitor spec:** 0.24 ± 0.02 µF, 1,000 W VDC.

---

## Related diagrams in the same manual

Not applicable to this bike, but present if a cross-reference is ever
useful:

| Diagram | Printed page | PDF page |
|---|---|---|
| Z250-A1/A2/A3/B1/B2 (European and General Export) | 179 | 185 |
| Z250-A4/B3 (General Export) | 278 | 284 |
