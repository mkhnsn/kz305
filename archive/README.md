# Archive

`kz305-bench-loom.yml` — superseded 16 Aug 2026.

The stage-1 bench loom modelled a subset of the harness with the upgrades
already baked in, which mixed "what the factory did" with "what we are
changing". That is how the coil-feed defect got in: the loom fed the coils
from a fused PDM circuit in parallel with the kill switch, so the engine
stop switch would not have stopped a running engine.

Replaced by the factory/rebuild split, where every deviation is a visible
diff rather than an accident:

    kz305-common.yml    shared part specs + confirmed bench data
    kz305-factory.yml   as-built reference
    kz305-rebuild.yml   the replacement harness

Every confirmed measurement from this file was migrated to kz305-common.yml
before archiving. Kept for provenance only. Do not build from it.

---

`part-selection-2026-09-10.md` — archived 10 Sep 2026.

The full working-out behind part selection (flasher, regulator, PDM, seals,
suppression, fuses), about 1300 lines, with every superseded decision left
inline. It was replaced by a current-state `docs/part-selection.md` because a
bench-side reader could not find the part number under the history. Nothing
here is current. Where the two disagree, `docs/part-selection.md` and the model
win.
