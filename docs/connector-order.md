# Cycle Terminal / Corsa Technic order — HW 090

Derived from `models/kz305-rebuild.yml`, 6 Sep 2026.

⚠️ **Both halves of every connector are needed.** The rebuild standardises on
sealed 090 (#37), so the stock housings get cut off the retained pigtails and a
new connector goes on each end. That is a one-way door on parts that are getting
hard to find — deliberate, not a side effect.

## Order quantities

Derived from the model. **Buy spares on terminals, seals and plugs** — a bad
crimp on a sealed or pull-to-seat terminal is not recoverable.

### HW 090 connectors — one SOCKET kit **and** one PIN kit each

The stock housings get cut off, so both ends of every connection are new.

| Node | Ways | Socket kit | Pin kit | Terminals |
|---|---|---|---|---|
| `IGN` ignition switch | 4 | 1 | 1 | 8 |
| `INSTR_6P` pod | 6 | 1 | 1 | 12 |
| `RH` right cluster | 3 | 1 | 1 | 6 |
| `LH` left cluster | 8 | 1 | 1 | 16 |
| | | | | **42** |

⚠️ **Check 3-way and 8-way exist in HW090.** If not: `RH` takes a 4-way with one
cavity plugged; `LH` falls back to the stock split (see below).

### Junctions

| For | Part | Qty | Terminals |
|---|---|---|---|
| `SP_GND` | `HW.JC-8P` | **4** | 24 |
| `SP_SW` | `HW.JC-14P-1` | **1** | 11 |
| | | | **35** |

⚠️ **Four `HW.JC-8P`, not three.** Three gives 24 positions for 19 grounds, two
jumper pairs and a lead — **exactly full, no spare**. Blocker 2's ground count is
not final, and a fourth is $6.

⚠️ **Check whether the junction ships with its mating housing.** The bussed half
takes no terminals; the wires land in a separate housing that needs its own.

### R/R — Furukawa QLW 250

| Part | Furukawa | Qty | Role |
|---|---|---|---|
| `QLW-3S-2` | `QLW-A-3F-GR` grey | 1 | AC — 2 of 3 ways |
| `QLW-3S-1` | `QLW-A-B3F-B` black | 1 | DC — 2 of 3 ways |

⚠️ **Select 14 AWG sockets and the matching seal size.** 14 AWG is the smallest
the housing takes, which is what forced `W_ALT` back up from 16.

### Terminals, seals, plugs

| Item | Need | **Buy** |
|---|---|---|
| HW090 terminals | 77 | **100** |
| HW090 wire seals | 77 | **100** |
| HW090 cavity plugs | 3 (`SP_SW`) | **20** |
| QLW 250 cavity plugs | 2 | **6** |

Terminals are shared across the MT / HM / HW sealed 090 families, so one part
number covers everything.

### Relays — if Corsa carries them

**6 × ISO 280 micro, 20 A, integral flyback diode** (#46). Five fitted, one for
the PDM's spare position. Sourced from nobody yet, so worth pricing here rather
than becoming another order.

⚠️ **Integral diode makes 85/86 polarity mandatory** — wired backwards it is a
dead short across the coil.

## Multi-way connectors

| Node | Ways used | Housing | Note |
|---|---|---|---|
| `IGN` ignition switch | 4 | **4-way** | |
| `INSTR_6P` pod | 6 | **6-way** | |
| `RH` right cluster | 3 | **3-way**, or 4-way with a plug | |
| `LH` left cluster | 8 | **8-way** | ⚠️ see below |

### ⚠️ `LH` — consolidate, or reproduce the stock split?

The model draws eight conductors at the left cluster. Stock split them across
**three** connections: five in the 6P, blue on its own flying bullet (`B02.2`),
and the horn black on a spade (`B02.1`) — plus `W_LH_GND`, which is new.

Since the stock housings are being cut off anyway, **one 8-way HW090 replaces all
of it**: one sealed disconnect instead of a connector, a bullet, a spade and a
ring.

That is the "solid" answer and it is what this list assumes. The alternative is
reproducing the stock arrangement for originality, which costs three interfaces
and a bullet the rebuild otherwise bans.

## Junctions — #44

| For | Part | Qty | Ways |
|---|---|---|---|
| `SP_GND` signal ground bus | `HW.JC-8P` | **3**, or 4 for spare | 8, all tied, 22 A |
| `SP_SW` switched bus | `HW.JC-14P-1` | **1** | 14 as 7+7, 22 A |

⚠️ **Check whether the junction ships with its mating housing.** Cycle Terminal's
listing says *"you will receive the Junction/splice connector only"* — the bussed
half. The wires land in a separate mating housing that needs its own terminals
and seals.

⚠️ **24 positions for 19 grounds, two jumper pairs and a lead is exactly full.**
Buy the fourth `HW.JC-8P` — blocker 2's ground count is not final.

## Terminals and seals

| | Count |
|---|---|
| Multi-way connectors, both halves | 42 |
| Junction mating halves | ~35 |
| **Total** | **~77 — buy 100** |

Terminals are shared across the MT / HM / HW sealed 090 families, so one part
number covers everything and one crimp die does the job.

## ⚠️ The seal is the one real risk in this order

HW090 seals are designed around Japanese OEM wire — AVSS 1.0 mm² runs about
**2.0–2.2 mm** insulation OD. **TXL 16 AWG is 2.26–2.40 mm.**

That is the same failure mode as the MTA cavity seals, and here it would affect
**every seal in the order**. A seal that will not close on the insulation leaves
an unsealed cavity in a connector chosen specifically because it is sealed.

**Ask for the seal's insulation-diameter range before ordering 100 of them**, or
buy ten first and try one. This is the cheapest check on the list and the most
expensive thing to get wrong.

## Also worth pricing here, to save a second shipment

- **Cavity plugs** for any unused ways.
- **The five ISO 280 micro relays** with integral flyback diode (#46) — not yet
  sourced from anyone.
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
