# Trunk map

Branch lengths alone will not reproduce the harness. **Where each branch leaves
the trunk** is what determines its shape, so that gets recorded here.

## Datum

Pick one and write it down **before measuring anything**. The fuse box or the
main junction is the obvious choice. Every `breakout_mm` in
`harness-lengths.csv` is measured from it, and a datum recorded afterwards is a
datum nobody can verify.

> **Datum:** The **headlight junction** — the connector cluster at the front of
> the harness where the majority of branches land.
>
> **Recorded:** 2026-08-28
>
> **Zero point within the cluster:** the **front end of the taped trunk** — the
> point where the trunk tape stops and the branches fan out into the junction.
> Marked with paint pen and photographed. `breakout_mm = 0` is this mark.
>
> Chosen over a connector face because it is a feature of the harness itself: it
> survives connectors being cut off, and it stays meaningful when the loom is
> unwrapped in Step 3 — the tape line is still visible as the boundary of the
> wrapped section, and the paint mark is on the wire bundle, not on the tape.
>
> Everything forward of this mark (the fan-out into the headlight connectors)
> has **negative** distance and is recorded as branch length, not breakout.
>
> **Direction:** all `breakout_mm` values increase **rearward** along the trunk,
> away from the headlight.

## Breakout order

Working from the datum along the trunk. Fill in as measured; the sketch matters
more than neatness.

| mm from datum | Branch ID | Goes to | Notes |
|---|---|---|---|
| 400 | `B01` | right-bar junction — 4P, fuse feed, horn, neutral switch | zero-length fork, 4 children |
| 430 | `B02` | left-bar junction — 6P, plus a blue bullet and a black spade | zero-length fork, 3 children. Separate breakout, confirmed at the bench — not a shared fan-out with `B03` |
| 460 | `B03` | | separate breakout, confirmed at the bench — not a shared fan-out with `B02` |
| 650 | `B04` | | |
| 730 | `B05` | | |
| 835 | `B06` | | |
| 880 | `B07` | | |
| 975 | `B08` | | |
| 1060 | `B09` | | |
| 1360 | `B10` | tail section — lights etc. | **trunk ends here.** Fans out into individual wires to bullet connectors, all of equal length. Per-wire detail in `connector-inventory.csv` |

Measured 2026-08-28. **Method:** cloth seamstress tape laid along the bundle,
following the path — `tape` in the CSV. **Read to the nearest 5 mm throughout**,
including the rows that happen to land on a whole centimetre — `B01` at 400 is a
5 mm-resolution reading, not a rounded one. Destinations still to be filled in.

## Trunk extent

The taped trunk runs from the datum to **1360 mm**, where the tape ends. Both
ends of the wrapped section are therefore fixed points: the datum is its front
end, `B10` sits at its rear end. That span is the backbone of the harness and
the one dimension every other measurement hangs off.

**Note the 0–400 mm gap.** Nothing breaks out for the first 400 mm rearward of
the datum. That is a long bare trunk run and it is a real feature of the harness
shape, not a missing row.

## Parked items

Deliberately set aside, not forgotten. Clear before calling Step 1 done.

| Item | What is needed |
|---|---|
| ~~`B00.x`~~ | **Done 2026-08-28** — 12 branches measured. |
| ~~Ground net: two tiers or two nets?~~ | **Closed 2026-08-28 by meter** — two separate nets. `Y/BK` (Net A) rings 0.2 Ω to the chassis ring; every `BK/Y` point (Net B) is open to it. |
| **Net B earth points — count and locate** | Answered in kind 2026-08-28: Net B earths through the child harnesses, at component mounting points — some engine block, some frame. Not through the main harness. Each must be traced through its own child harness as that harness is worked. **The count of these is the count of new ground wires the star bus needs**, and it is not yet known. |
| ~~Is Net B one net or several?~~ | **Closed 2026-08-28** — one net. All four black-base points mutually continuous (0.0–0.3 Ω from `B10.5`). |
| **Still-mated connectors** | `B06.3`, `B06.4`, `B06.5` are still plugged into something. **Photograph and record the mate BEFORE separating** — that connectivity is free Step 4 data and is lost the moment they come apart. |
| `B06.4` melting — **design input** | Kept even though the harness is being replaced: the mechanism was a gauge step at a bullet on the main power path, so a new build reproduces the fault if it reproduces the topology. Not a condition question. |
| ~~`B05` ↔ `B04.3` continuity~~ | **Closed 2026-08-28** — both yellows ring through to slots in the `B04.3` 4P and are not continuous with each other. `B05` is the alternator phase pair (`W_ALT`); `B04.3` is the regulator/rectifier connector. |
| **Br/W resistance** | Item 0b closed on continuity but ohms were not recorded. Re-read `B01.2`↔`B06.5` for value — the procedure's >1 Ohm rule makes every ring-out a fault survey. |
| **Hidden Br/W junction** | `B01.2`/`B00.11`/`B06.5` ring continuous but `B00.11` is one wire with both slots empty — so a splice joins them under the tape. Find it in Step 3. |
| **Empty double-female slots** | Six nodes (`B03` `B08` `B00.5` `B00.7` `B00.8` `B00.11`) each present two empty receptacles. What plugged in was lost at teardown. Only the on-bike photos and the components themselves can narrow it. |
| `B03` second cavity | Whether the second cavity of the double-female bullet is occupied, and by what. Step 2. |
| ~~`B10.5.1` breakout~~ | **Closed 2026-08-28** — leaves the shared crimp at `B10.5`'s end; `breakout_mm` = 60. |
| **Fuse box scope** | `B06.3/.4/.5` land on a fixed pigtail off the original glass-fuse box, but the plan is a 6-circuit blade block. Decide whether the rebuild terminates to the old pigtail or rebuilds those wires — it changes what needs measuring there. |
| **Gauge pass** | No wire gauge has been measured at all — every `gauge` value is a visual estimate. Needs a gauge tool or calipers on stripped conductor. Not urgent: gauge survives the loom coming apart. |
| `B04.3` blade width | Caliper across a spade. Needed for part selection before the connector is bagged. |
| `B04` wire count | Not visible under tape. Children sum to 10 — verify in Step 3. |
| On-bike photo folder | Record its path in the Photographs section below. |

## Trunk sketch

Keep it crude. What it has to capture is order and distance, not appearance.

```
DATUM
  |
  |--- 0 mm ----- B__  ..........
  |
  |--- ___ mm --- B__  ..........
  |
  |--- ___ mm --- B__  ..........
  |
  v
```

## Photographs

Whole harness laid out with tags visible, plus each connector face-on. The
photographs are what make this map re-readable in six months — the table alone
will not be enough.

### On-bike photos — the routing fallback

A folder of photographs of the harness **installed on the bike, before anything
was disconnected**, exists outside this repo. It is large and unindexed, so it
is a last resort rather than a working reference.

It is nonetheless the **only** remaining source for physical routing: where a
branch ran, what it passed under, which side of the frame it took. Once the
harness came off the bike that information left with it, and no amount of bench
measurement recovers it. Reach for the folder when a question is specifically
about routing or component position — not for anything a measurement or a meter
can answer.

> **Folder location:** ____________________________________________

Worth recording the path above even without indexing the contents. A fallback
nobody can find is not a fallback.
