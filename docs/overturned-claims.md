# Overturned claims

Every claim this project asserted and later withdrew, with the class of
evidence that produced the wrong version and the class that corrected it.

This is the empirical basis for the evidence ranking used in
`docs/verification-plan.md` and `docs/claims-register.md`. The ranking is
**not** a prior about what ought to be reliable — it is this table.

The model notes no longer carry these histories. They state what is
currently held true, with one evidence tag. The working-out lives in
`archive/models-2026-09-02/`.

## The record

| # | Claim as asserted | Wrong by | Corrected by | Date closed |
|---|---|---|---|---|
| 1 | The fuse box has an internal bus; one 10A carries the bike | scan | bench | 28 Aug 2026 |
| 2 | Y/BK and BK/Y are the same wire recorded two ways | scan | bench | 28 Aug 2026 |
| 3 | The harness returns through one chassis ring terminal | scan | meter | 28 Aug 2026 |
| 4 | The chassis ring lead is 6 AWG | inherit | bench | 28 Aug 2026 |
| 5 | The brown bus is energised through the right-bar branch | scan | meter | 28 Aug 2026 |
| 6 | The R/R output is brown, onto the switched bus | arith | bench | 29 Aug 2026 |
| 7 | …therefore charging returns through the ignition switch | arith | bench | 29 Aug 2026 |
| 8 | The 20A MAIN is W in, W/R out | guess | meter | 29 Aug 2026 |
| 9 | The TAIL fuse is R/Bl in, Br/W out | guess | arith | 29 Aug 2026 |
| 10 | Bl/W is a feed *into* the right-bar branch | scan | bench | 29 Aug 2026 |
| 11 | The horn button has a ground-side wire (W_HORN_GND) | scan | bench | 29 Aug 2026 |
| 12 | The left-cluster 6P carries Bl; the way list is over-subscribed | scan | bench | 29 Aug 2026 |
| 13 | Instrument 6P cavity 5 is plain R | scan | bench | 29 Aug 2026 |
| 14 | The ignition switch's TAIL1 pin is R/BK | scan | bench | 29 Aug 2026 |
| 15 | The meter lamps are fed plain R off the tail net | scan | photo | 2 Sep 2026 |
| 16 | …and therefore light in PARK | scan | photo | 2 Sep 2026 |
| 17 | Both brake switches are fed Br/W from the right bar | scan | bench | 2 Sep 2026 |
| 18 | The starter relay's COIL− grounds directly | bench | bench | 2 Sep 2026 |
| 19 | The accessory feed is switched | scan | bench | 2 Sep 2026 |
| 20 | The W/R bullet node is on the fuse-box pigtail | bench | bench | 2 Sep 2026 |
| 21 | A white-and-black bundle runs to the tachometer | photo | photo | 2 Sep 2026 |
| 22 | Seven Net B grounds land on the Net A chassis ring | inherit | review | 2 Sep 2026 |

`inherit` means the claim was never established at all — it was carried
across from the diagram or from an earlier note and never questioned.
`guess` means the record said at the time that it was a guess.

## What the record says

**Twelve of the twenty-two were produced by the scan.** Reading the 600 dpi
diagram is by a wide margin this project's largest single source of
withdrawn claims, and the failures are not random: **five of the twelve are
base-versus-tracer** (#2, #13, #14, #15, #17). At 600 dpi a thin tracer
stroke and a broken stroke are the same handful of pixels. The scan is
reliable for topology and unreliable for colour.

**The meter has never produced a withdrawn claim.** Every entry in the
"corrected by" column that reads `meter` or `bench` has stood since.

**Two failures came from arguing rather than looking.** #6 and #7 rest on
one inference — four ways, four functions, no spare pin — and every
measurement behind it was correct. The premise was false because an
unpopulated cavity is invisible from the harness side. This is the origin
of the standing rule that **both halves of every multi-way connector get
read.**

**`photo` is under-tested, not proven.** It has one failure (#21, caught the
same day) and two successes (#15, #16). Two of the corrections credited to
it are the *only* evidence for those claims. It sits above `scan` in the
ranking on a sample of three, and should not be read as being anywhere near
`meter` — see the Session A block in `docs/verification-plan.md`, which
exists to convert those into meter readings.

**Two claims were wrong because a correction reached some files and not
others** (#18 and #22 were both found in review, not at the bench). Both had
been correctly withdrawn elsewhere in the repo first. Fixing the instance
and not the class is this project's second failure mode, and unlike the
first it is not about evidence at all.
