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
