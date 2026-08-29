# Switch bench tests

Readings taken on switch clusters unplugged from the harness.

## Dimmer switch — CLOSES procedure item 5.6

Left-bar cluster, unplugged. Bench session **2026-08-28**.

| Pair | HI | LO |
|---|---|---|
| `R/BK` ↔ `Bl` | **0.1 Ω** | open |
| `Bl` ↔ `R/Y` | open | **0.1 Ω** |
| `R/BK` ↔ `R/Y` | open | open |

**`Bl` is the common.** It is the only pin present in both positions.

| Pin | Role |
|---|---|
| `Bl` | common — supply in |
| `R/BK` | HI beam output |
| `R/Y` | LO beam output |

Open since 13 Aug. Getting it wrong lights both filaments at once, and it was
blocking the headlight relay decision.

### Corroborated by the harness net map

`Bl` being the supply agrees with what was measured from the harness side on the
same day, independently: **Blue Net 2** runs from the fuse box (`B06.5`) to
`B02.2` at the left-bar junction, and the fuse box labels holder 2 **HEAD**.

So the path is complete and every leg of it was established separately:

```
HEAD fuse (10 A) --> Bl --> dimmer common --> R/BK (HI)  or  R/Y (LO) --> headlight
```

### This settles holder 2's orientation

`Bl` is the dimmer's **supply**, so it is downstream of the HEAD fuse. Therefore
on fuse holder 2, **`Bl` is the output and `Bl/W` the input** — resolved without
further readings, and consistent with the 17 Aug note calling `Bl/W` "the feed
into the branch" rather than a tap out of it.

### Note: the wiper bridges both outputs during switchover

`R/BK` ↔ `R/Y` is open in both settled positions but **blips closed while the
switch is moving**. A make-before-break wiper: both beam outputs are momentarily
tied, so both filaments see supply for the instant of the change.

Not a fault, and normal for the type. Recorded because it matters to the relay
design — a two-relay scheme must tolerate a momentary both-energised condition
rather than assume the outputs are mutually exclusive.
