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
| **Net B earth points — count and locate** | Net B earths through the child harnesses at component mounting points, not through the main harness. **The count of these is the count of new ground wires the star bus needs.** Drawing the rebuild's circuits is converting them one at a time: the pod, both meter lamps, four signal lamps, the tail and the headlight now have drawn grounds. ⚠️ The largest is `GND_ENG` — the engine strap carries **cranking current**, and the frame is being powder coated. |
| **Hidden `Br/W` junction** | `B01.2`/`B00.11`/`B06.5` ring continuous but `B00.11` is one wire. A splice joins them under the tape, inferred and never seen. Find it in Step 3. (#8) |
| **Hidden Net A splice** | Same argument: three endpoints (`B04.1` ring, `B00.7`, `B08`), each holding exactly one wire. Also never seen. (#8) |
| **`B04` `B05` `B06` wire counts** | Not visible under tape. Children sum to **10, 2 and 8**. ⚠️ `B06` was recorded as 9 until 2 Sep 2026 — it is 1+1+1+1+4. An inflated prediction is a silent false negative: a real 9-conductor bundle, i.e. one hidden splice, would have read as a clean match. A mismatch is another splice. (#8) |
| **A SEVENTH double-female — `B10.5.1`** | ⚠️ Found in review 2 Sep 2026. The "all six closed" sweep listed `B03` `B08` `B00.5` `B00.7` `B00.8` `B00.11` — but `B10.5.1`'s own note calls it *"third 1-to-2 distribution node found (with `B03` and `B08`)"*, and it was never in the set. `BK/Y` at the tail fan, so **Net B** — which makes its unknown consumers ground-side and feeds straight into the star-ground count. Nothing records whether its slots were populated or what mated it. |
| **Points and condenser leads** | The trunk's yellow pair turned out to be the alternator, so these are somewhere else and have never been found. (#8) |
| **Starter relay coil polarity** | ⛔ *"`COIL-` grounds directly"* is **withdrawn** — the assembly has two bullet leads and no ground of any kind. Which lead is `COIL+`, and where the return actually goes, needs the meter. `SOL`'s way numbers are still the diagram's, not the part's. |
| **Gauge pass** | No wire gauge has been measured at all; every value is a visual estimate. **Off the critical path for buying wire** since the rebuild specifies TXL independently — but still needed to understand the old harness. Also carries the 16 AWG insulation-OD check for the MTA seal. (#38) |
| **`B04.3` blade width** | Caliper across a spade, for part selection, before the connector is bagged. (#37) |
| **`Br/W` resistance** | Continuity closed on item 0b but ohms were never recorded. Re-read `B01.2`↔`B06.5` — the >1 Ω rule makes every ring-out a fault survey. |
| **`B00.2`'s splice count** | Logged as *"a common ground collection with several splices downstream"*. **Several was never a number.** Two are now named — both meter lamp grounds — so it is *at least* two. |
| **The headlight's ground** | Drawn `BK/Y`, presumably onto `B00.2`. Never recorded as a mate. |
| `B06.4` melting — **design input** | Kept though the harness is being replaced: the mechanism was a gauge step at a bullet on the main power path, so a new build reproduces the fault if it reproduces the topology. **Sharper since 2 Sep** — the node hangs off the relay's BATTERY stud, two connections from the post. Not a condition question. |

### Closed

| Item | |
|---|---|
| `B00.x` measured | 2026-08-28 — 12 branches |
| Ground net: two tiers or two nets? | 2026-08-28 by meter — two separate nets |
| Is Net B one net or several? | 2026-08-28 — one net |
| Still-mated connectors | 2026-08-28 — `B06.3/.4/.5` recorded before separating |
| `B05` ↔ `B04.3` continuity | 2026-08-28 — `B05` is the alternator pair |
| `B03` second cavity | 2026-08-28 — folded into the empty-slots item |
| `B10.5.1` breakout | 2026-08-28 — 60 mm |
| Fuse box scope | 2026-08-28 — the blade block replaces box and pigtail |
| `Bl/W` direction | 2026-08-29 — settled with the TAIL fuse orientation |
| Fuse holder 3 orientation | 2026-08-29 — `Br/W` in, `R/Bl` out |
| `W_IGN_FEED` route | 2026-08-29 — the 20 A MAIN's terminals were backwards |
| Left-bar 6P brown | 2026-08-29 — it feeds nothing; a dead way |
| Unidentified nets | 2026-09-02 — **every branch's net is named** |
| **Empty double-female slots** | 2026-09-02 — **all six**. `B00.7`/`B00.8`/`B08` never connected (29 Aug); `B03` = the coil feed splice; `B00.5` = the front brake switch; `B00.11` = the two meter lamps |
| **Starter relay assembly** | 2026-09-02 — mapped visually. Accessory feed is **battery-live**, `Y/R` Net 2 is the coil feed, the `W/R` node is on the assembly. Coil polarity remains, above |
| **On-bike photo folder** | 2026-09-02 — sifted. Closed four items in one sitting and located four modelled splices |
| **Lengths (issue #2)** | 2026-09-02 — 46 branches, 48 taped, `breakout_mm` complete. The irreversible gate is passed |

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
