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
| 8-way | **5** | 1 | `LH` — one pair. **Four females are surplus** |
| 14-way | **1** | — | **surplus** |

⚠️ **The junction mating halves are not used.** Four 8-way females and the 14-way
female were ordered to mate the `HW.JC` sealed junctions. `SP_SW` and `SP_GND` are
parallel splices instead (19 Sep 2026) — the junctions are too bulky to dress on
the bike. The housings go on the shelf; **their terminals and seals are the spares
pool**, below.

#### Terminals and seals come WITH the housings — 6 Sep 2026

Cycle Terminal includes exactly one way's worth per housing, so the kits above
supply **88 terminals and 88 seals against the 42 needed**:

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

The surplus junction halves are all female, so the kits carry a deep pile of female
spares and **no male spare at all**:

| | Female | Male |
|---|---|---|
| Needed | 21 | 21 |
| Supplied by the kits | 67 | 21 |
| **Spare** | **46** | **0** |

Every male terminal that ships gets used. A ruined male crimp means a re-order;
a ruined female one comes out of the forty-six already in the box.

| Consumable | Qty | Why |
|---|---|---|
| HW090 terminals — **MALE** | **15** | zero spare included |
| HW090 terminals — female | **10** | 46 already spare; not needed |
| HW090 wire seals | **15** | not gendered, 46 already spare |
| HW090 cavity plugs | **20** | **none needed** — the nine were all for the junctions, and every housing still in use is full |

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
| `HW.JC-8P` bussed junction | 4 — **not used**, see above |
| `HW.JC-14P-1` bussed junction | 1 — **not used** |
| M22759/16-14 yellow, `W_ALT_A` / `W_ALT_B` | 8 ft |

⚠️ **The relays were not in it.** They move to the Cycle Terminal cart below.

### Terminal count

| | |
|---|---|
| `IGN` 4 + `INSTR_6P` 6 + `RH` 3 + `LH` 8, both halves | 42 |
| **Total** | **42** |

Terminals are shared across the MT / HM / HW
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

Both vendors give the range as **2.00–8.00 mm² (12–14 AWG)**. `W_ALT_A` / `W_ALT_B` is 16 AWG =
**1.23 mm²**, below the minimum. The terminal will not crimp on it and the seal
will not close on its insulation.

| Wire | Gauge | mm² | |
|---|---|---|---|
| `W_ALT_A` / `W_ALT_B` | 16 AWG | 1.23 | ⚠️ **below minimum** |
| `W_RR_OUT` | 12 AWG | 3.31 | OK |
| `W_RR_GND` | 12 AWG | 3.31 | OK |

**Check Corsa's socket and seal dropdowns first** — the listing offers selectable
sizes, so a 16 AWG socket may exist for this housing. If not, run `W_ALT_A` / `W_ALT_B` at
14 AWG; see its note in the model for why that costs less than the 4 Sep
gauge-matching decision implies.

### ⚠️ Cavity plugs

Both connectors run 2 of 3 ways. Corsa's kits list housing + 3 contacts +
3 seals and **no plug**; Cycle Terminal's set includes one. Two plugs are needed
either way — `AC3` is deliberately unterminated and the DC side has a spare way.
