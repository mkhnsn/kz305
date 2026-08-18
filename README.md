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

Needs a Python venv:

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

`render` finds `.venv` on its own; there is no activation step.

WireViz is pinned to the [unstable-studios fork](https://github.com/unstable-studios/WireViz),
at an exact commit rather than a branch. The fork adds `--strict`, which
`build.py` depends on — see below.

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
