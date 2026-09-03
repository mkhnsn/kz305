# Verification plan — proving the model against the real harness

Written 2 Sep 2026, after a design review found several claims withdrawn in one
file and left standing in another. The problem it addresses is not that
individual findings are wrong — most are well evidenced — but that **nothing
recorded which claim rested on which kind of evidence**, so nobody could tell
what still needed proving.

`docs/claims-register.md` is now generated from the repo and answers that
mechanically. Regenerate it after any model change:

```sh
.venv/bin/python3 tools/claims_register.py > docs/claims-register.md
```

## What the register says today

**328 marked claims**, after the 2 Sep notes cleanup folded out the duplicate
restatements. The distribution:

| Evidence | n | |
|---|---|---|
| `unstated` | 172 | 47 in `measurements/`, 20 in `models/`, rest are `[OPEN]` |
| `meter` | 130 | |
| `bench` | 15 | |
| `photo` | 9 | |
| `arith` | 1 | |
| `scan` | 1 | |

**70 standing claims rest on scan, photograph or unstated evidence** while
asserting something is settled — down from 137, and the drop is duplicate
restatements rather than claims that got tested.

⚠️ The 47 `unstated` lines in `measurements/` are the remaining gap: that
directory was not part of the notes cleanup and does not carry evidence tags.

The `unstated` majority is the actionable part. This project is good at
recording *what* it concluded and inconsistent at recording *how* — and "how"
is the only thing that says whether a claim needs re-testing.

## Evidence classes, ranked by this project's own failure record

Not a prior. This is the observed record, enumerated in
`docs/overturned-claims.md`.

| Class | Record |
|---|---|
| `meter` | **No continuity reading has ever been overturned.** |
| `bench` | Wire or part in hand. The base-colour-first convention exists to keep this class clean. |
| `arith` | Sound where the premises hold — **the premises are the risk.** `B06`'s child sum was wrong by one and would have hidden a splice. |
| `photo` | **Mixed and under-tested.** One in-session failure: white read as grey in a crowded shell. `docs/kz305-b1-wiring.md` bans colour reads from photographs outright, and that rule was not applied to the 2 Sep closures. |
| `scan` | **Twelve failures**, five of them base-versus-tracer. 600 dpi cannot resolve a tracer. |

⚠️ **The asymmetry worth fixing.** Enumerating the record on 2 Sep put the scan's
failure count at **twelve**, not the five previously carried — the earlier number
was remembered rather than counted. The photograph rule still has a sample of
three: one failure, two successes, and it has withdrawn nothing. The photo reads
that happened not to collide with an existing measurement were kept without being
tested, and five of them are load-bearing. That is what Session A is for.

## ⚠️ Ordering — what must happen before what

Three constraints, and only the first is currently recorded:

1. **Lengths before cutting.** Done — issue #2 closed, 46 branches, 48 taped.
2. **Sessions A and B before Session D.** Every reading that needs the loom
   *intact* has to be taken before it is unwrapped. Unwrapping is irreversible
   and there is no second chance at a continuity path through an assembled
   harness.
3. **The ground count before the frame goes to the coater.** Masking depends on
   knowing which mounting points get a wire, and that count is still being
   converted branch by branch. **Either the count finishes first or the frame
   waits** (#54).

## Session A — meter, harness intact

**Needs:** Fluke 87V, REL-zeroed, harness assembled. **This session gates
Session D.**

| Test | Settles | Acceptance |
|---|---|---|
| Starter relay `Y/R` against each coil terminal | Which lead is `COIL+`; the withdrawn "grounds directly" claim | Identifies the terminal |
| `B06.1` against the ground net, and against `B10.5` | Where the coil return goes, and which ground net | Continuity or open, with ohms |
| Tach `Br/W` against `B00.11`, `B00.4`, `B10.2` | Confirms the meter lamp closure by meter rather than photo | Continuous to `B00.11` only |
| Rear brake feed against the brown net and the `Br/W` net | Confirms `B04.4` by meter | Continuous to brown |
| `B00.5` brown against both nets | Confirms the front brake feed by meter | Continuous to brown |
| `B01.2` ↔ `B06.5` ohms | The `Br/W` resistance never recorded | **>1 Ω is a damaged conductor** |
| `B01.4` to `INSTR_6P` way 4 | Closes the neutral lead's "pending ring-out" | Continuous |
| Every point on both ground nets, against each other | Re-proves the Net A / Net B split the whole ground rework rests on | Net B open to the chassis ring |

**Why this session matters most:** it converts the five 2 Sep photo closures
into `meter` claims. They are currently the largest block of load-bearing
findings on the project's second-weakest evidence class.

## Session B — calipers and a gauge tool

**Needs:** digital calipers, wire gauge tool or micrometer. Also gates Session D
for anything gauge-related.

- **The gauge pass** (#38) — no wire on this harness has ever had its gauge
  measured. Every value is an eyeball estimate against an unverified 18 AWG
  baseline.
- **16 AWG TXL insulation OD** against the green seal's 2.2 mm lower bound —
  **0.06 mm margin**, and the seal is what makes the module waterproof.
- **`B04.3` blade width** (#37), and terminal width plus depth on each retained
  connector — the five-member "small" family has **no measurements at all**.
- **The starter relay's two heavy cables** — that is the circuit that melted and
  the gauge step is the finding. Currently eyeball, and the relay is on the bench.

## Session C — photographs, at a desk

- **`B10.5.1`** — the seventh double-female, never sifted for and never in the
  "all six" closure. `BK/Y` at the tail fan, so **Net B**, so its consumers are
  ground-side and feed the star-ground count.
- **`B00.11`'s second consumer**, if the meter does not settle it in Session A.
- **Both harness tags** (#7) — photograph before unwrapping; tags come off with
  tape, and the part number decides whether a third dead way is likely or
  surprising.

## Session D — Step 3, unwrap the loom

**Irreversible. Runs after A and B.** Full plan in
`docs/step3-ringout-session.md`.

- The two hidden splices — `Br/W` and Net A — inferred from conductor arithmetic
  and never seen.
- `B04` / `B05` / `B06` wire counts. ⚠️ **Re-derive all three at the bench**;
  `B06` was recorded as 9 and is 8, and an inflated prediction silently absorbs a
  hidden splice.
- The points and condenser leads, never located.
- `SP_R` — now a one-consumer node. Is there a physical junction there at all?

## Session E — parts in hand

- **Identify the retained connector series** (#37). Five interfaces, zero part
  numbers, and it gates *ordering* rather than assembly — the longest lead item
  in the project.
- **`SOL`'s way numbers** off the housing, not the diagram. `IGN` and `FUSE_4P`
  both needed renumbering once actually read.
- **Bullet genders** for the relay's `Y/R` and `BK`, which are recorded but
  unordered.

## What can never be verified

Worth stating plainly so it stops being chased.

**The mating halves of the empty double-females are gone.** They left the bike at
teardown and were not recorded. Six of the seven have an account — three by
oxidation evidence, four from photographs — but *account* is not *measurement*,
and no future session can promote them.

`B10.5.1` is the exception only in that it has not been tried yet.

**Consequence:** where a consumer cannot be identified, the rebuild either
reproduces the provision deliberately or drops the circuit deliberately. A
circuit missing from the transcription is a circuit that will not exist on the
bike, and that has to become a decision rather than an omission.

## Acceptance — what "verified" means here

- **Ohms, not beeps.** A corroded conductor still beeps. >1 Ω is a damaged
  conductor.
- **REL-zero the leads**, and record that you did.
- ⚠️ **Except at the two 6 AWG ground joints**, where 0.1 Ω is 15 V at 150 A.
  Those need a **millivolt drop measured while cranking** (#44).
- **Colour base first, tracer second**, always, and say which.
- **Record the evidence class in the note**, so the register can grade it. That
  single habit is what would have prevented this review's largest findings.
