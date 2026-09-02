# KZ305 harness

Wiring documentation and a replacement harness design for a **1982 Kawasaki
KZ305-B1**. Two WireViz models are kept side by side so that every change from
stock is a visible diff rather than an accident:

| Model | What it is |
|---|---|
| `models/factory/*.yml` | The **as-built** factory harness, split by subsystem. Reference only — nothing gets built from it. Carries no wire lengths by design, so it renders without a BOM. |
| `models/kz305-rebuild.yml` | The **replacement** harness actually being built. DRAFT — see its header for open blockers. |

`models/kz305-common.yml` holds the shared part library (connector and cable
definitions as YAML anchors) so the two models can never disagree about what a
part is.

## Render

```sh
./render              # build every model into out/
./render factory      # build one
./render --list       # show models and their source files
make                  # same as ./render
```

Outputs land in `out/` and are gitignored — `models/` is the source of truth,
and anything in `out/` is one command away from being regenerated.

## Published drawings

**<https://mkhnsn.github.io/kz305/>** — every drawing, re-rendered and
republished on each push to `main`. The interactive pages are the ones worth
opening at the bench: pan, zoom, click a wire to trace its net across sheets.

Published straight from CI rather than committed, so the site cannot show a
drawing that no longer matches the models. `tools/make_index.py` builds the
landing page from `harness.yml` and from whatever actually landed in `out/`,
which is why a new sheet appears there without anyone editing a list.

Needs a Python venv:

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

`render` finds `.venv` on its own; there is no activation step.

WireViz is pinned to the [unstable-studios fork](https://github.com/unstable-studios/WireViz),
at a release tag rather than a branch. The fork adds `--strict` and
`--merge`, which `build.py` depends on (see below), plus the layout and output
features the models use: `rankdir: TB` with transposed node tables, native
`sheets:` splitting, and interactive HTML output (pan/zoom, net tracing across
sheets, BOM rows that highlight their component in the drawing).

## Why the fork, and why `build.py`

Stock WireViz's `--prepend` concatenates files as raw text, and YAML resolves
duplicate top-level keys last-wins. Two files that each define `connections:`
therefore render only the second one's — silently, exit 0, with a warning. A
harness built from that BOM would be missing real wires.

The fork's `--merge` combines sources at the **data level** instead, and its
`--strict` refuses to drop input silently. Between them they raise:

| Guard | Raised by |
|---|---|
| A connector or cable name defined in two files | `DuplicateComponentError` |
| A duplicate key inside one file | `DuplicateKeyError` |
| A component left out of every connection set | `UnreferencedComponentsError` |
| A setting given different values in two files | `ConflictingValueError` |
| An unknown output format code | `build.py` |

`build.py` adds only the last row. It is the project layer on top of the fork:
it reads `harness.yml` so no flags have to be remembered, resolves each model's
source globs, and reports line numbers against the file being edited rather than
against the merged text. The merging and every other guard live in WireViz.

Add `--dump FILE` to see the merged YAML that WireViz actually received.

## Part numbers and the BOM

The rebuild model renders with `t`, so `out/kz305-rebuild.bom.tsv` is generated
from the drawing rather than maintained by hand. Procurement detail lives on the
components themselves.

**Per-component fields** — `manufacturer`, `mpn`, `pn`, `supplier`, `spn`. Each
appears as a BOM column only once something uses it, so unfilled fields cost
nothing:

```yaml
RR:
  manufacturer: Shindengen
  mpn: SH775
  pn: "4012941"
```

⚠️ Quote bare-numeric part numbers. `0301370` unquoted is parsed as an integer
and the leading zero is lost.

**`additional_components`** carries the things a component needs but that are not
themselves connectors or wire — covers, secondary locks, terminals, seals,
cavity plugs. They become their own BOM lines against the parent's designator.

**Quantities can derive from the drawing** via `qty_multiplier`, which is what
makes the BOM self-correcting rather than a second thing to keep in sync:

| Multiplier | Gives |
|---|---|
| `populated` | pins actually connected |
| `unpopulated` | `pincount` minus those |
| `pincount` | every way, used or not |

Cables also take `wirecount`, `terminations`, `length`, `total_length`.

The worked example is `RR`. It is a 5-pin part with `AC3` deliberately
unterminated, so `populated` yields **4 terminals** and `unpopulated` yields
**1 cavity plug** — and if `AC3` is ever connected, both numbers move on their
own.

**Where this does not reach.** `PDM`'s terminal and plug counts are hand-entered
(42 and 18), because the model gives it **10 logical ways** — one per circuit —
while the physical MTA `0301370` has **60 cavities**. The multipliers work off
`pincount`, so they would compute against the wrong number. Those two figures
have to be reconciled against the cavity map when it is written; see
`docs/part-selection.md`.

Unknown part numbers are written into the `subtype` as `MPN TBD` rather than
left blank, so the BOM doubles as the procurement gap list.

## Wire labels

The rebuild uses **solid colours only** — no tracer wire — so a printed
heat-shrink label is a wire's identity, not a convenience. `docs/label-schedule.md`
is generated, never hand-written:

```sh
.venv/bin/python3 tools/label_schedule.py > docs/label-schedule.md
```

Two labels per wire, and **each names the far end** — that is the question you
have when you are holding one end of a wire in a loom. The `W_` prefix is
dropped: every wire has it, so it carries no information, and heat shrink on
18 AWG has very little room.

⚠️ **The label and the cavity seal both go on before the terminal is crimped.**
Both slide on from the wire end and a crimped terminal will not pass either.
Order: label, seal, strip, crimp, shrink. Getting it wrong means cutting the
terminal off and starting that wire again.

## Tests

```sh
pytest tests/
```

End-to-end checks on `./render`: that every model in the manifest renders, that
the factory model produces no BOM and the rebuild model does, and that each
guard actually **exits nonzero**. That last part is the point — every guard is
enforced by the pinned fork, so a repin that lost `--strict` or `--merge` would
quietly stop protecting the BOM, and a guard that no longer fails the build is
indistinguishable from a clean run. CI runs these on every push.

## Sheets

`models/factory/sheets.yml` assigns every component of the factory model to a
subsystem sheet, using the fork's native `sheets:` feature. Each system gets
its own drawing the way a factory manual splits them — that is what makes a
wiring diagram readable, far more than any layout setting.

A connection crossing sheets is drawn on the cable's sheet and ends in a stub —
a reduced copy of the far connector typed `⇒ <sheet>` — so each sheet reads on
its own: the starting sheet shows the start button as a stub of the controls
sheet, the way a factory manual cross-references. png/svg come out as
`kz305-factory.<sheet>.<ext>`; the HTML is a single interactive page carrying
every sheet, and hovering a wire traces its net across sheet boundaries.

Unlike the old `sheet-*` models (which re-rendered overlapping file subsets
with `strict: false`), the sheets are views of the one validated harness:
strict stays on, and a component missing from the sheet mapping — or from
every connection set — fails the build rather than silently vanishing.

## Layout

`models/style.yml` sets `rankdir: TB` for every model. GraphViz places nodes by
graph topology, not by position on the bike, so it cannot reproduce a factory
plate — but TB takes the drawings from unprintable ribbons to something like
2:1 or 3:1. The fork transposes connector and cable tables under TB (pins on
the top/bottom edges), so wires attach on the faces the graph flows through
instead of routing through node bodies — the problem that forced an earlier
revert to LR. style.yml also sets `sort_wires`, `wirelabel_detail`, and
`mate_labels`; see the comments there.

## Layout

```
harness.yml     which files make up which model, and the render defaults
render          entry point; build.py does the merging
models/         harness models + shared part library  <- source of truth
  factory/      the factory harness, one file per subsystem
  style.yml     shared drawing style, merged into every model
docs/           bench findings, transcriptions, procedures
measurements/   raw bench data: lengths, trunk map, generated cable index
tools/          small generators (cable index)
parts/          order guides and shopping lists
out/            rendered drawings and BOMs (generated, gitignored)
archive/        superseded work, kept for provenance
```

## Working rules

These govern every edit to the models:

1. **Bench findings override the document, never the reverse.** A confirmed
   bench value is never adjusted to match the diagram.
2. **Colours come from a meter, a stamped part, the factory diagram, or the
   wire in hand** — not from photographs, which shift under lighting and white
   balance, and not from the 40-year-old scan where a stripe colour is ambiguous.
3. **Open questions stay open.** They are logged as TBD and never silently
   resolved by guessing.
4. **Validate every edit by rendering.** `./render` must exit 0.

Watch for colour collisions the models flag. The 28 Aug ring-out turned that
warning into a measurement: **three of the eight colours rung carry more than one
circuit**. Black serves four roles (right points lead, starter trigger, chassis
ground, horn button return — the starter trigger and the horn return are now
separated from each other by continuity), yellow
serves two (left points lead, alternator phases, separated by continuity, *not*
by gauge), blue serves two (brake feed, fused headlight supply), and Y/R serves
two — one of which appears in no model. Kawasaki's LG and G both render as `GN`.
Identification by colour alone is unsafe here, including in the models.
