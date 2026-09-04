# Wire and connector order

Three suppliers, and only one of them is ready to order today.

| Supplier | Scope | Status |
|---|---|---|
| **Prowire** | TXL wire, splice heat-shrink, labels, loom | **ready** |
| **Eastern Beaver** | regulator/rectifier pigtails | **ready** |
| **Cycle Terminal** | OEM-style Japanese connectors | ⛔ **blocked on #37** |

---

## 1. Prowire — TXL wire

**18 SKUs.** Derived from the model, 4 Sep 2026: every cable's gauge and
colour, counted by conductor.

| Gauge | BK | RD | WH | BN | YE | GY | BU | GN |
|---|---|---|---|---|---|---|---|---|
| 12 AWG | 1 | 2 | — | — | — | — | — | — |
| 14 AWG | — | 1 | 2 | 1 | 2 | — | — | — |
| 16 AWG | 3 | 4 | — | 8 | 6 | — | 8 | 1 |
| 18 AWG | 20 | — | — | 13 | 3 | 11 | 3 | 10 |

### Suggested footage

⚠️ **These are estimates, not a cut list.** The model carries no lengths by
design — the harness is built in place on the bike and trimmed there. Lengths
are scaled from the old harness: 1.36 m trunk extent, 0.9 m longest branch,
and a front-to-back run of about 1.4 m.

| Gauge | Colour | Conductors | Est. | Order |
|---|---|---|---|---|
| 18 AWG | BK | 20 | 62 ft | **100 ft** |
| 18 AWG | BN | 13 | 41 ft | **100 ft** |
| 18 AWG | GY | 11 | 34 ft | **50 ft** |
| 18 AWG | GN | 10 | 31 ft | **50 ft** |
| 18 AWG | YE | 3 | 9 ft | 25 ft |
| 18 AWG | BU | 3 | 9 ft | 25 ft |
| 16 AWG | BN | 8 | 22 ft | **50 ft** |
| 16 AWG | BU | 8 | 22 ft | **50 ft** |
| 16 AWG | YE | 6 | 17 ft | 25 ft |
| 16 AWG | RD | 4 | 11 ft | 25 ft |
| 16 AWG | BK | 3 | 8 ft | 25 ft |
| 16 AWG | GN | 1 | 3 ft | 25 ft |
| 14 AWG | WH | 2 | 4 ft | 25 ft |
| 14 AWG | YE | 2 | 4 ft | 25 ft |
| 14 AWG | RD | 1 | 2 ft | 25 ft |
| 14 AWG | BN | 1 | 2 ft | 25 ft |
| 12 AWG | RD | 2 | 7 ft | 25 ft |
| 12 AWG | BK | 1 | 3 ft | 25 ft |

About **700 spool feet** for roughly 100 ft of actual wire. That ratio is the
minimum-spool tax, not waste — and it is the argument for the consolidations
below.

### 17 SKUs — one consolidated away

`W_MAIN_IN` was the only 14 AWG RD in the harness, so a whole spool bought one
wire. **Rounded up to 12 AWG RD**, which is already on the list for the charging
pair. Upsizing the shortest, highest-current feed on the bike costs nothing, and
it never enters the PDM so the seal table does not care.

Three single-conductor SKUs remain and all three stay: `W_SW_BUS` (14 AWG BN)
keeps its margin on the main switched path, `W_RR_GND` (12 AWG BK) cannot share
a spool because black is ground-only, and `W_HEAD_LO` (16 AWG GN) stays at 16 for
filament headroom.

### Gauges are settled — sized for INCANDESCENT

**Decided 4 Sep 2026.** The bike may run filament lamps for a while before the
LED conversion, so everything is sized for the STOCK load and rounded up. That is
the conservative direction, and it means **no gauge changes if the lamp decision
changes.**

Checked against the filament worst case, and nothing needed to move:

| Wire | Gauge | Filament load |
|---|---|---|
| `W_HEAD_HI` / `W_HEAD_LO` | 16 AWG | 4.2 A on a 50 W beam |
| `W_HEAD_SUPPLY`, `W_HI_PWR`, `W_LO_PWR` | 16 AWG | 7 A with both beams lit during the blip |
| `W_BRAKE` | 18 AWG | 2.25 A, 27 W |
| `W_SIG_*` | 18 AWG | 1.9 A each, 23 W |
| `W_TAIL_RUN` | 18 AWG | 0.7 A, 8 W |

**#61 is closed by decision.** Green seal on 16 AWG, no caliper pass. The margin
is 0.06 mm against a nominal and green is the intended fit; the risk did not
justify gating a wire order on it.

**12 AWG is settled too** — the stator is taken as 20 A, `MF_RR` at 30 A. See
#59.

## 2. Prowire — consumables

- **Adhesive-lined heat shrink for splices.** The rebuild has **14 splices**, and
  the two feed buses are cascades — `SP_HOT` is 3 splices and `SP_SW` is 7, so
  the physical count is about **24 joints**, not 14.
- **Printed heat-shrink labels.** The identification scheme depends entirely on
  these, because the rebuild uses solid colours with no tracers. See
  `docs/label-schedule.md` — **two per wire, naming the far end.**
- **Loom, braid or tape**, and adhesive heat-shrink for the branch breakouts.

## 3. Eastern Beaver — regulator/rectifier

**Ready to order.** Two mating pigtails for the SH775: **3-pin AC + 2-pin DC**,
Shindengen FH009–FH020 family, $16–22. Eastern Beaver preferred over a generic
listing for correct crimps and adequate DC-side gauge.

- AC3 is **deliberately unterminated** — the alternator is single-phase and
  connects to any two of the three inputs. It needs a **cavity plug**, not a
  wire.
- The DC pair runs heavy and direct to the battery with `MF_RR` at the battery
  end, because a series regulator is sensitive to resistance in the DC path.

## 4. Cycle Terminal — ⛔ blocked on #37

The rebuild **retains the switchgear, the instrument pod, the ignition switch and
both brake switches**, so the new harness has to mate their connectors. None of
those housings is identified by part number and **no dimension has been measured
on any of them**.

| Connector | Harness-side gender | Ways needed |
|---|---|---|
| `RH` right-bar 4P | male spades | 4 |
| `LH` cluster 6P | — | **5, not 6** — the stock brown feeds nothing |
| `INSTR_6P` pod | female | 6 |
| `IGN` switch 4P | — | 4 |
| Bullets | mixed | throughout |

⚠️ **`LH` needs five ways, not six.** Reproducing the stock way count would
rebuild a wire into a cavity the cluster does not populate.

⚠️ **The right-bar 4P and the fuse-box 4P are different parts** — same way count,
unrelated housings, different mould marks. Do not order one part number for both.

**This is a bench task and the parts are in hand.** Measure the housings, then
order. Ordering connectors against a guess is how the wrong series arrives.
