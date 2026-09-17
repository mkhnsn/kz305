# Cycle Terminal / Corsa Technic order — HW 090

Derived from `models/kz305-rebuild.yml`, 6 Sep 2026.

⚠️ **Both halves of every connector are needed.** The rebuild standardises on
sealed 090 (#37), so the stock housings get cut off the retained pigtails and a
new connector goes on each end. That is a one-way door on parts that are getting
hard to find — deliberate, not a side effect.

## Two orders — 6 Sep 2026

**All standard HW090 from Cycle Terminal. Only the specialty parts from Corsa.**

### ⚠️ Gender convention — decide before ordering

**Harness side FEMALE, component side MALE**, on every connection. A disconnected
harness then has no exposed live pins, which matters most at `IGN` and `LH` where
the harness side is fed from the PDM.

That convention also falls out naturally at the junctions: their bussed half is
**male**, so the wires land in a **female** housing — consistent with everything
else.

### Cycle Terminal — PLACED

✅ **Order placed.** It carries the HW090 housings and consumables below, the
Furukawa QLW pair, **the fuses** (MiniVal kit + ATC 20 A and 30 A) and **the
genuine Song Chuan relays** (`SCMR20`).

#### HW090 lines, all in stock 6 Sep 2026

| Item | Female | Male | For |
|---|---|---|---|
| 3-way | 1 | 1 | `RH` right cluster |
| 4-way | 1 | 1 | `IGN` ignition switch |
| 6-way | 1 | 1 | `INSTR_6P` pod |
| 8-way | **5** | 1 | `LH` **+ 4 junction mating halves** |
| 14-way | **1** | — | `SP_SW` junction mating half |

⚠️ **Five 8-way females, one 8-way male.** Four of the females are the mating
halves for the `HW.JC-8P` junctions and have no male partner to buy — the
junction *is* their partner. This is the line most likely to be mis-ordered.

✅ **The 14-way female is in stock**, which was the risk item: the
`HW.JC-14P-1` was already bought from Corsa and would have been stranded without
it. No extra `HW.JC-8P` is needed, and `SP_SW` stays a single junction rather
than two 8-ways jumpered.

#### Terminals and seals come WITH the housings — 6 Sep 2026

Cycle Terminal includes exactly one way's worth per housing, so the kits above
supply **88 terminals and 88 seals against the 77 needed**:

    3-way pair       3 x 2 =   6
    4-way pair       4 x 2 =   8
    6-way pair       6 x 2 =  12
    8-way pair       8 x 2 =  16
    8-way female x4  8 x 4 =  32
    14-way female   14 x 1 =  14
                             ---
                              88

**No loose terminals are required.** That retires the "buy 100" line entirely —
it was written before this was known.

#### ⚠️ Spares must be weighted MALE

The junction mating halves are all female — 35 of the 56 female terminals — so the
kits carry female spares and **no male spare at all**:

| | Female | Male |
|---|---|---|
| Needed | 56 | 21 |
| Supplied by the kits | 67 | 21 |
| **Spare** | **11** | **0** |

Every male terminal that ships gets used. A ruined male crimp means a re-order;
a ruined female one comes out of the eleven already in the box.

| Consumable | Qty | Why |
|---|---|---|
| HW090 terminals — **MALE** | **15** | zero spare included |
| HW090 terminals — female | **10** | 11 already spare; belt and braces |
| HW090 wire seals | **15** | not gendered, 11 already spare |
| HW090 cavity plugs | **20** | **8** needed — see below — and blocker 2 may change the ground count |

⚠️ **Eight cavity plugs are needed.** `SP_SW`'s 14-way runs 11 of
14. The four `SP_GND` junctions use **27 of 32** positions — nineteen returns, three
jumper pairs and the two `W_GND_MAIN` leads — so `SP_GND` takes five more plugs.
Eight in all, against twenty bought.

### Cycle Terminal — also the Furukawa R/R pair

| Item | Qty | For |
|---|---|---|
| `QLW-A-3F-GR` grey | 1 | R/R **AC** — ⚠️ **14 AWG** sockets |
| `QLW-A-B3F-B` black | 1 | R/R **DC** |

Cycle Terminal's `QLW-3F Set` bundles both at $16.95 with 6 terminals, 5 seals and
**a cavity plug**, which Corsa's kits do not include. Both connectors run 2 of
3 ways, so a second plug is still wanted.

### Corsa Technic — PLACED 6 Sep 2026

| Item | Qty |
|---|---|
| `HW.JC-8P` bussed junction | 4 |
| `HW.JC-14P-1` bussed junction | 1 |
| M22759/16-14 yellow, `W_ALT` | 8 ft |

⚠️ **The relays were not in it.** They move to the Cycle Terminal cart below.

### Terminal count

| | |
|---|---|
| `IGN` 4 + `INSTR_6P` 6 + `RH` 3 + `LH` 8, both halves | 42 |
| Junction mating halves — `SP_GND` 24, `SP_SW` 11 | 35 |
| **Total** | **77 — buy 100** |

The bussed halves take no terminals. Terminals are shared across the MT / HM / HW
sealed 090 families, so one part number covers every housing above.

#### Terminals and seals on TXL — accepted per the manufacturer's spec, 10 Sep 2026

The HW090 terminals and seals are used on the 16 AWG TXL as ordered, within the
vendor's stated range. Wire and seal sizing are not second-guessed beyond that
(#37, closed).

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
