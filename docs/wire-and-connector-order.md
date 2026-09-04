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

### ⚠️ Four SKUs exist for a single conductor

A whole spool for one wire is the cost problem that folded the palette from
eleven colours to eight in the first place. Two can be removed for nothing:

| SKU | Wire | Fix |
|---|---|---|
| **14 AWG RD** | `W_MAIN_IN` | **Move to 12 AWG RD**, already on the list. Upsizing the battery-to-fuse feed costs nothing and it never enters the PDM, so the seal table does not care. |
| **16 AWG GN** | `W_HEAD_LO` | **Move to 18 AWG GN** — but only once #60 gives the LED headlight's measured draw. Do not downsize a beam feed on an assumption. |
| 14 AWG BN | `W_SW_BUS` | **Keep.** It carries the whole switched load, and the model kept it at 14 AWG deliberately for margin on the main switched path. |
| 12 AWG BK | `W_RR_GND` | **Keep.** Charging return, same current as the feed, and black is ground-only so it cannot share another colour's spool. |

### ⚠️ Two gauges are provisional — order them last

- **12 AWG** (`W_RR_OUT`, `W_RR_BATT`, `W_RR_GND`) is inherited, not calculated.
  It follows the stator's rated output, which has never been read off anything —
  **#59**.
- **16 AWG BU / GN** beam feeds follow the LED headlight's measured draw — **#60**.

Neither blocks the other sixteen SKUs.

### ⚠️ Resolve #61 by asking, not by calipering

The 16 AWG seal margin — 2.26 mm nominal against green's 2.2 mm lower bound,
**0.06 mm** — was filed as "caliper the delivered spool". That is
chicken-and-egg: 24 conductors of 16 AWG enter the PDM, so a miss would change
the order after it arrives.

**Ask Prowire for the actual insulation OD of their 16 AWG TXL before ordering.**
It costs an email and settles the question for free. Caliper on arrival anyway,
but do not make the buy blind.

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
