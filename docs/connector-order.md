# Cycle Terminal / Corsa Technic order — HW 090

Derived from `models/kz305-rebuild.yml`, 6 Sep 2026.

⚠️ **Both halves of every connector are needed.** The rebuild standardises on
sealed 090 (#37), so the stock housings get cut off the retained pigtails and a
new connector goes on each end. That is a one-way door on parts that are getting
hard to find — deliberate, not a side effect.

## Two orders — 6 Sep 2026

Corsa Technic is out of stock on 6-way and 8-way HW female housings, and those
are also what the junction connectors mate into. Cycle Terminal covers the gap.

⚠️ **Prefer the larger housings if Cycle Terminal has them.** Splitting `LH` and
`INSTR_6P` across 3-ways works, but it puts **two identical 3-way connectors on
the same component** — cross-pluggable, and on `LH` a swap crosses switched power
with the flasher output. One housing per component removes the hazard entirely.

### Cycle Terminal

| Item | Qty | For |
|---|---|---|
| HW090 **8-way female** housing | **4** | mating half for each `HW.JC-8P` |
| HW090 **14-way female** housing | **1** | mating half for `HW.JC-14P-1` |
| HW090 **8-way** pair (socket + pin) | 1 | `LH` left cluster |
| HW090 **6-way** pair | 1 | `INSTR_6P` pod |
| HW090 **4-way** pair | 1 | `IGN` ignition switch |

⚠️ **The junction's mating half must match its way count** — the bussed half is
one housing and cannot be split across smaller connectors. This is why the
8-way shortage blocks the junctions and not just the clusters.

⚠️ **Check whether CT's housings ship with terminals and seals.** Their listings
often do; Corsa's are sold as kits. Do not double-buy.

### Corsa Technic

| Item | Qty | For |
|---|---|---|
| `HW.JC-8P` junction | **4** | `SP_GND` — 3 needed, 4th for spare |
| `HW.JC-14P-1` junction | **1** | `SP_SW` |
| HW090 **3-way** pair | 1 | `RH` right cluster |
| `QLW-3S-2` grey | 1 | R/R **AC**, 14 AWG sockets |
| `QLW-3S-1` black | 1 | R/R **DC** |
| HW090 terminals | **100** | 77 needed |
| HW090 wire seals | **100** | 77 needed |
| HW090 cavity plugs | 20 | 3 needed in `SP_SW` |
| QLW 250 cavity plugs | 6 | 2 needed |
| ISO 280 micro relay, integral diode | **6** | 5 fitted + PDM spare, #46 |

### Terminal count

| | |
|---|---|
| `IGN` 4 + `INSTR_6P` 6 + `RH` 3 + `LH` 8, **both halves** | 42 |
| Junction mating halves — `SP_GND` 24, `SP_SW` 11 | 35 |
| **Total** | **77 — buy 100** |

The bussed halves take no terminals. Terminals are shared across the MT / HM / HW
sealed 090 families, so buy them wherever is convenient.

### If Cycle Terminal is also short on 6/8-way

The parallel splices already bought from Prowire cover both junctions —
**25 × 12-10, 10 × 8 GA, 5 × 6 GA**. `SP_GND` becomes about three 6 GA splices and
`SP_SW` one. Nothing is blocked.

⚠️ **The cost is serviceability, and it lands hardest on `SP_GND`** — blocker 2's
ground count is *not final*, so that bus is the one most likely to gain a wire.
`SP_SW` has the weaker case now that F10 and F11 have landed.

## R/R connectors — IDENTIFIED, 6 Sep 2026

**Furukawa QLW 250 series**, and the part numbers match exactly across Corsa
Technic and Cycle Terminal — two independent vendors agreeing is better
identification than either alone.

| | Furukawa P/N | Corsa kit | Role |
|---|---|---|---|
| Grey | `QLW-A-3F-GR` | `QLW-3S-2` | **AC** — 3 ways, 2 used, 1 plugged |
| Black | `QLW-A-B3F-B` | `QLW-3S-1` | **DC** — 3 ways, 2 used, 1 plugged |

Colour is the keying: it is what stops AC being plugged into DC. 6.3 mm contacts,
34 A, single-wire sealed.

Cycle Terminal also sells them as a pair — `QLW-3F Set`, $16.95, with 6 terminals,
5 seals and a cavity plug — against roughly $15.90 for the two Corsa kits.

### ⚠️ The AC side will not take 16 AWG

Both vendors give the range as **2.00–8.00 mm² (12–14 AWG)**. `W_ALT` is 16 AWG =
**1.23 mm²**, below the minimum. The terminal will not crimp on it and the seal
will not close on its insulation.

| Wire | Gauge | mm² | |
|---|---|---|---|
| `W_ALT` | 16 AWG | 1.23 | ⚠️ **below minimum** |
| `W_RR_OUT` | 12 AWG | 3.31 | OK |
| `W_RR_GND` | 12 AWG | 3.31 | OK |

**Check Corsa's socket and seal dropdowns first** — the listing offers selectable
sizes, so a 16 AWG socket may exist for this housing. If not, run `W_ALT` at
14 AWG; see its note in the model for why that costs less than the 4 Sep
gauge-matching decision implies.

### ⚠️ Cavity plugs

Both connectors run 2 of 3 ways. Corsa's kits list housing + 3 contacts +
3 seals and **no plug**; Cycle Terminal's set includes one. Two plugs are needed
either way — `AC3` is deliberately unterminated and the DC side has a spare way.
