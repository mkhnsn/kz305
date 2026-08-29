# Fuse box

Original three-holder glass-fuse box. Bench session **2026-08-28**, box
disconnected from the harness with **every fuse pulled** — with fuses in, the
holders are bridged and every reading is meaningless.

Closes procedure items **5.2** (fuse mapping) and **0b part C** (which holder is
`FUSE_A`), which together feed the PDM cavity map — described in the docs as the
last original TBD.

## Holders

Numbered **top to bottom as the box sits**, marked with a paint pen so the
numbering survives to the next session.

| Holder | Rating | Printed label | Terminal A | Terminal B |
|---|---|---|---|---|
| 1 | 20 A | **MAIN** | white | `W/R` |
| 2 | 10 A | **HEAD** | blue | `Bl/W` |
| 3 | 10 A | **TAIL** | `R/Bl` | `Br/W` |

The box carries its own circuit names. That is stronger evidence than the
44-year-old scan and it agrees with the bench net map on every wire that appears
in both.

## Cross-reference to the harness net map

| Fuse wire | Harness net | Established |
|---|---|---|
| `W/R` | main power path — `B04.6`, `B06.4` | continuity, 2026-08-28 |
| blue | Blue Net 2 — `B02.2` (left-bar/dimmer), `B06.5` | continuity, 2026-08-28 |
| `Br/W` | Br/W net — `B01.2` (RH_4P), `B00.11`, `B06.5` | continuity, item 0b |
| `Bl/W` | feed into the right-bar branch | docs, 17 Aug |
| `R/Bl` | also at `B00.3` (ignition switch 4P) | not yet rung |
| white | mates `B06.3` | continuity, 2026-08-28 |

Every one of these was identified from the harness side **before** the labels
were read, and none of them contradicts a label.

## Open: which terminal of each holder is the input

Recorded as A and B rather than in/out, because that has not been measured.
**A is the left terminal and B the right**, as the box sits with the paint mark
up — a reading order, not an electrical one.

A colour convention was proposed at the bench: the striped leg is the fused
output, since holder 1 runs white→`W/R` and holder 2 blue→`Bl/W`, both "same
base, add a tracer". **Holder 3 breaks it** — `R/Bl`→`Br/W` changes base colour
entirely — so the convention cannot be what is happening there.

The net map also pulls the two holders in opposite directions:

- **Holder 3 fits A-in / B-out.** `R/Bl` also appears at `B00.3`, the ignition
  switch, whose table carries the Tail 1 and Tail 2 circuits. A switched tail
  feed in, fused `Br/W` out to the lamps.
- **Holder 2 looks reversed.** Blue was measured as the supply reaching the
  left-bar dimmer; if blue were the input the dimmer would sit on unfused power.
  `Bl/W` in — matching the 17 Aug note calling it "the feed into the branch" —
  and blue out is the more coherent reading.

Holders may simply be oriented differently from each other; the wires are routed
to suit the loom, not to suit a convention. **Measure it.**

### Measured: there is no internal bus — CLOSES item 0b part B

Every terminal traced individually with fuses out; all six are open to each
other. The three holders are electrically independent.

**The diagram is wrong and the 13 Aug bench note is right.** The scan shows both
10 A fuses sharing a common red feed branching from one wire; there is no such
node. Three separate feeds, as the 13 Aug note described. Working rule 1 applies
and the models should follow the bench.

### Consequence: the box alone cannot say which terminal is the input

With no bus and no fuses, nothing inside the box distinguishes an input from an
output. That has to come from the harness side, and the test is: **which pin is
fed from a live source upstream of the fuse.**

For each fuse-box pin, ring its harness-side partner against the known nets:

| Holder | Pins | Harness-side reading needed |
|---|---|---|
| 2 HEAD | blue / `Bl/W` | Blue Net 2 is `B02.2`+`B06.5` and does not include `W/R`. `Bl/W` (`B01.1` ↔ `B06.5`) has never been rung. Do that, then ring both against the `W/R` main net. |
| 3 TAIL | `R/Bl` / `Br/W` | `R/Bl` appears at `B00.3`, the ignition switch, which takes battery on white and outputs the tail circuits — so `R/Bl` is very likely the input. Confirm by ringing `B06.5`'s `R/Bl` to `B00.3`'s. |

Holder 1 is settled by the net map without further readings: white mates
`B06.3`, and `W/R` is the main power net feeding the starter relay. White in
from the solenoid, `W/R` out to the main bus.

## Finding: the melted joint is the 20 A MAIN output

`B06.4` — the wire showing melting and corrosion — is `W/R`, and `W/R` is the
**20 A MAIN circuit**. The highest-current circuit in the bike, melting at a
bullet junction where a larger conductor meets a smaller one.

This is a **design** finding rather than a condition one: a new harness built to
the same topology puts the same step at the same place on the same 20 A circuit.

## Scope note

The rebuild plans a **6-circuit blade block**, so this box and its fixed pigtail
do not survive. The mapping here is the baseline for laying that block out, not
a set of wires to reproduce.
