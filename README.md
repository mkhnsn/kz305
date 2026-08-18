# KZ305 harness

Wiring documentation and a replacement harness design for a **1982 Kawasaki
KZ305-B1**. Two WireViz models are kept side by side so that every change from
stock is a visible diff rather than an accident:

| Model | What it is |
|---|---|
| `models/kz305-factory.yml` | The **as-built** factory harness. Reference only — nothing gets built from it. Carries no wire lengths by design, so it renders without a BOM. |
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

Needs a Python venv with WireViz 0.4.1:

```sh
python3 -m venv .venv && .venv/bin/pip install wireviz
```

`render` finds `.venv` on its own; there is no activation step.

## Why `build.py` instead of plain `wireviz`

WireViz's `--prepend` concatenates files as raw text, and YAML resolves
duplicate top-level keys last-wins. Two files that each define `connections:`
therefore render only the second one's — silently, exit 0, with a warning. A
harness built from that BOM would be missing real wires.

`build.py` merges at the data level and makes four things hard errors:

- a connector or cable name defined in two files
- a duplicate key inside one file
- a component left out of every connection set (WireViz only warns, then drops
  it from both the drawing *and* the BOM)
- an unknown output format code

Add `--dump FILE` to see the merged YAML that WireViz actually received.

Subsystem files can be split into `models/factory/` and `models/rebuild/`; the
manifest globs already point there, and `./render` proves nothing was dropped.

## Layout

```
harness.yml     which files make up which model, and the render defaults
render          entry point; build.py does the merging
models/         harness models + shared part library  <- source of truth
docs/           bench findings, transcriptions, procedures
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

Watch for colour collisions the models flag: black serves three roles (right
points lead, starter trigger, chassis ground), yellow serves two (left points
lead, alternator phases), and Kawasaki's LG and G both render as `GN`.
