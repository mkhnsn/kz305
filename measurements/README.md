# Measurements

Raw bench data, kept separate from the models. The models are *derived*: a
measurement is evidence, and evidence does not get edited to agree with a
drawing.

## Why lengths are not catalogued on the schematic

`out/kz305-factory.svg` labels every cable with its designator, so it is
tempting to annotate lengths onto it. Don't. A WireViz drawing is a
**schematic** — it shows what connects to what, and deliberately says nothing
about physical routing. Lengths are the opposite: they are almost entirely
about physical topology, specifically *where along the trunk each branch breaks
out*. That is what reproduces the harness shape, and the schematic cannot
express it.

There are also two places where the schematic and the physical harness do not
correspond one-to-one:

- **One designator can be several physical segments.** `W_RH_BR` runs through
  the confirmed 1→3 splice inside the right-bar branch. On the bench that is
  more than one thing to measure.
- **Parts of the harness have no designator at all yet.** Lighting, horn and
  instruments are not transcribed (#9). Those branches still have to be
  measured now, before the loom is cut up, whether or not they are modelled.

So the log below keys on **physical branch IDs**, and carries the model
designators as a cross-reference rather than as the identity.

## The three artefacts

| File | What it is |
|---|---|
| `harness-lengths.csv` | The log. Append-only. |
| `trunk-map.md` | Breakout order and distances along the trunk. |
| `cable-index.md` | Generated cross-reference of model designators to endpoints. |

Regenerate the index after any model change:

```sh
.venv/bin/python3 tools/cable_index.py > measurements/cable-index.md
```

## Branch IDs

`B01`, `B02`, … assigned in **Step 0 of the ring-out procedure**, written on
the tape tags. The tag on the harness and the ID in this file are the same
string. That is the whole point of tagging before measuring — you cannot record
a measurement of something that has no name.

Number them in the order you tag them. Do not renumber later; a gap in the
sequence costs nothing and a renumber invalidates every photograph.

## Re-measuring: append, never overwrite

Measurements get redone. When one does:

1. Add a **new row** with the new value and today's date.
2. Change the **old row's** `status` to `superseded`.
3. Say why in `notes` — "first measure pulled the bend straight", "string
   slipped", "disagreed with B14".

**Never edit a value in place.** Two measurements that disagree are a finding,
not a mistake to tidy away — the BK/Y colour dispute is only resolvable because
both readings survived. A length that quietly changed between sessions is a
length nobody can trust.

## Columns

| Column | |
|---|---|
| `branch_id` | `B01` — matches the tape tag |
| `from`, `to` | Tagged endpoints. Use the tag names, not descriptions. |
| `model_cables` | Space-separated `W_*` designators this covers, or blank if not modelled yet |
| `colour`, `gauge` | As read off the wire in hand |
| `breakout_mm` | Distance from the datum to where this branch leaves the trunk |
| `length_mm` | Path length of the branch, breakout to connector face |
| `method` | `string` (laid in the groove), `tape`, or `estimate` |
| `measured_on` | ISO date |
| `status` | `provisional`, `confirmed`, `superseded` |
| `notes` | Anything that would change how the number is read |

## Rules that make the numbers usable later

- **Record the datum in `trunk-map.md` before the first measurement.** Every
  `breakout_mm` is meaningless without it.
- **Measure along the path**, not point to point — string in the groove, mark,
  then measure the string.
- **Do not stretch the harness straight.** It was built with bends in it.
- **Record raw.** Service loop is added at build time. Bake slack in here and
  the real number is lost.
- **`confirmed` means measured twice**, by preference on different days.
