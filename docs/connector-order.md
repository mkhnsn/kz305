# Cycle Terminal / Corsa Technic order — HW 090

Derived from `models/kz305-rebuild.yml`, 6 Sep 2026.

⚠️ **Both halves of every connector are needed.** The rebuild standardises on
sealed 090 (#37), so the stock housings get cut off the retained pigtails and a
new connector goes on each end. That is a one-way door on parts that are getting
hard to find — deliberate, not a side effect.

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
- **The Shindengen `FH009`–`FH020` R/R pigtails**, 3-pin AC + 2-pin DC. Currently
  assigned to Eastern Beaver; if Corsa Technic carries them, that is one fewer
  order and one fewer shipping charge.
