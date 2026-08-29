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

## ⚠️ Y/BK and BK/Y are two different wires

Confirmed at the bench **2026-08-28**, with certainty, wires in hand:

| Written | Is |
|---|---|
| **`Y/BK`** | **Yellow** base with a thin black tracer |
| **`BK/Y`** | **Black** base with a thin yellow tracer |

Both are present in this harness. This closes procedure item 5.1, which had
framed the question as *which one the ground wire is* — the answer is that the
premise was wrong. The 13 Aug note (Y/BK) and the 17 Aug read (BK/Y) were not in
conflict; they were looking at different wires.

Consequences:

- **Every earlier record that wrote one of these without stating the base colour
  is now ambiguous** and cannot be repaired by inference. Re-read the wire.
- **Colour cannot identify a ground.** The models render every ground as `BKYE`;
  if the single chassis-ground ring terminal is yellow-base (`B04.1`), the models
  and the harness disagree. Ring it out — do not resolve it by reading.
- **Always write the base colour first, and say so.** `Br/W` and `W/Br` bit this
  project twice before this.

## Colour: base first, tracer second — always

Bench convention stated 2026-08-28 and applied to **every** colour in these
files without exception. `Y/BK` is yellow with a black tracer. `BK/Y` is black
with a yellow tracer. `W/Bl` is white with a blue tracer; `Bl/W` is blue with a
white tracer. These are four different wires and all four are in this harness.

The order is the identity, not a formatting preference. `Br/W` versus `W/Br` has
already cost this project twice, and `Y/BK` versus `BK/Y` was logged as an
unresolved dispute for a fortnight before it turned out both wires existed.

Records written **before** 2026-08-28 do not carry this guarantee. Where an
older note gives a two-colour wire without saying which is the base, it is
ambiguous and cannot be repaired by inference — re-read the wire.

## ⚠️ No gauge has been measured

**As of 2026-08-28 not one wire in this harness has had its gauge measured.**
Every value in the `gauge` column is a visual estimate made by eye against the
harness's own most common wire, with no tool of any kind.

That includes the "18 AWG" baseline itself. It is a label for *the size most of
this harness is*, not a measurement, and everything else was judged relative to
it. If the baseline is wrong, every relative reading is wrong with it.

What the column means as written:

| Value | Means |
|---|---|
| *(blank)* | The common size — visually the same as most of the harness. Called 18 AWG, unverified. |
| `>18` | Visibly one size heavier than the common wire. **16 or 14, not distinguished by eye.** |
| `>18?` | The same, with less confidence. |
| `6` etc. | Only where the difference is too large to mistake. |

**Do not draw gauge conclusions from this data, and do not compare it against
the models' gauges.** One size by eye is exactly the resolution at which 16 and
14 are indistinguishable, which is precisely where every interesting question
sits.

Gauge needs its own pass with a gauge tool or calipers on stripped conductor.
It is not urgent — unlike length, gauge survives the loom coming apart and can
be measured from a cut-up harness or even a single salvaged wire.

## Possible bench-vs-model: `W_ALT` gauge — NOT ESTABLISHED

The cable index gives `W_ALT` (ALT→RR) as **14 AWG**. At the bench 2026-08-28
both yellow pairs — `B05.1`/`B05.2` and the two yellows in `B04.3` — appeared to
be the common size rather than heavier, as did the alternator's own leads.

**This does not overturn the model.** The observation is that the yellows look
like the rest of the harness; calling that "18 AWG" assumes the baseline, and no
gauge has been measured. Working rule 1 puts bench above document, but only for
a bench *finding* — an eyeball comparison against an unverified reference is not
one.

Recheck it during the gauge pass. If the yellows do turn out to be 18 AWG the
model is wrong and should be corrected then.

What is established either way: **gauge cannot separate the yellow pair.** Both
yellow candidates — alternator phases and left points lead — look the same on
the bench, so the collision has to be resolved by continuity.

## Hypothesis: the ground net changes colour before the ring terminal

The single chassis-ground ring terminal (`B04.1`) is **yellow base** (`Y/BK`),
16–18 AWG. Every ground wire in the models is **black base** (`BKYE`), and the
black-base grounds seen on the bench so far (`B04.3`, `B04.5`) agree with the
models.

`B08` adds a second yellow-base wire: `Y/BK`, **16 AWG** — heavier than the
18 AWG signal wires — running to a double-female bullet, a 1→2 distribution
node. Two yellow-base wires now, both on the heavy side, both at nodes where a
ground net would be expected to gather.

Two readings fit:

1. **The ground net is yellow-base throughout**, distributing through
   double-female bullets and ending at the ring terminal, and the models are
   simply wrong to render grounds as `BKYE`. The black-base wires seen so far
   (`B04.3`, `B04.5`) would then be some other circuit, not grounds.
2. **The net changes colour at a splice** — black-base grounds converge and one
   yellow-base wire carries the combined return. This is the failure mode the
   ring-out procedure warns about: a net untraceable by colour because it does
   not keep one.

### Resolved by the `B00` cluster: two ground colours, two roles

The headlight junction shows both wire types doing visibly different jobs:

| | Role |
|---|---|
| **`BK/Y`** (black base) | **Branch grounds.** Individual circuit returns. `B00.2` is a shared-crimp collection point described at the bench as gathering several; the tail grounds (`B10.5`, `B10.5.1`) are the same colour. |
| **`Y/BK`** (yellow base) | **The common return trunk.** Heavier than the branch wires, and found only at distribution nodes: `B00.7` (double-female, larger gauge), `B08` (double-female), `B04.1` (the single chassis ring terminal). |

Three yellow-base wires now, every one of them heavier than common and every one
at a node — and the black-base wires are everywhere the individual circuits are.
That is not a colour change at one splice; it is a **deliberate two-tier ground
architecture**: branch returns in black-base, collected, then carried to the
single chassis ring on heavier yellow-base.

It explains the 13 Aug / 17 Aug disagreement completely. Both readings were
right about different wires, and the ring terminal is yellow-base because it is
the trunk end of the net, not a branch.

#### Competing reading: engine grounds vs lighting grounds

Proposed at the bench 2026-08-28: `Y/BK` is the **engine** ground net and `BK/Y`
is the **instrument and lighting** ground net — two separate systems rather than
two tiers of one.

Both readings agree that `BK/Y` is the small-circuit branch ground; no
counterexample to that has been found. They differ only on `Y/BK`.

Two observations the engine reading has to account for:

- **`B00.7` is `Y/BK` and sits in the headlight cluster** — heavier gauge, on a
  double-female node, at the front of the bike.
- **`B04.3`'s ground is `BK/Y`, and that connector is the regulator/rectifier** —
  neither instrument nor lighting.

**The discriminating test is `B00.7`.** Its run is 240 mm where almost everything
else in the cluster is 100 mm, so it reaches past the local connectors to
somewhere. If it collects headlight-area grounds and heads rearward it is a
return trunk; if it runs to something engine-side and merely passes through, the
engine reading is right.

The on-bike photographs can also settle it: **where the `B04.1` ring terminal
bolts** — engine case or frame — separates the two directly, and it is one of
the few questions the bench genuinely cannot answer.

**Still to confirm by meter**, since this rests on colour and position: ring the
`B04.1` terminal against a black-base branch ground and against `B00.7`. The
models render every ground as `BKYE`, so if this holds, the models are wrong
about the trunk portion specifically.

### Earlier reasoning, superseded

**As of the tail fan (`B10`), reading 2 is ahead.** `B10.5` and `B10.5.1` are
both black-base `BK/Y`, matching the modelled tail grounds exactly, and
`B10.5.1` is itself a double-female distribution node. So the periphery of the
ground net is unambiguously black-base while the single ring terminal is
yellow-base — which is what a colour change looks like, not what one consistent
net looks like.

That leaves the two yellow-base wires (`B04.1`, `B08`) needing an account. Either
they are the far side of that change, or they are a different circuit
altogether that happens to be yellow-base — `B04.1` being a ring terminal argues
for ground, but a ring terminal is not proof of one.

**Both untested.** Resolved by ringing the ring terminal against the black-base
grounds, and by looking at what the `B08` bullet feeds. Do not let either
steer the ring-out — they are written down so a finding confirms something
rather than surprising someone.

## What is actually being rebuilt

Most connections in this harness are bullets and spades to things that are **not
this harness**. Sorting them is what defines the BOM, so every mate gets one of
three classes in `connector-inventory.csv` (`mate_class`):

| `mate_class` | Means | In the rebuild? |
|---|---|---|
| `main` | The other side is the main harness — an internal junction. | Yes, both sides |
| `subharness` | A separate loom that plugs in: bar-switch pigtails, tail section. | The connector only |
| `component` | A fixed pigtail off a component: coil, flasher, horn, R/R, starter relay, fuse box. | The connector only |

For `subharness` and `component` the rebuild buys and terminates the mating
half; it does not build the wire on the far side. Everything found so far in
those two classes — horn, flasher, coils, the bar pigtails, the battery earth
cable — is wire the models carry but the build does not.

Getting this wrong in either direction is expensive: build wire that already
exists, or leave out wire nothing else provides. It is cheap to record now,
while both halves are in hand, and impossible to reconstruct from a cut-up
harness later.

## What is actually being rebuilt

Most connections in this harness are bullets and spades to things that are **not
this harness**. Sorting them is what defines the BOM, so every mate gets one of
three classes in `connector-inventory.csv` (`mate_class`):

| `mate_class` | Means | In the rebuild? |
|---|---|---|
| `main` | The other side is the main harness — an internal junction. | Yes, both sides |
| `subharness` | A separate loom that plugs in: bar-switch pigtails, tail section. | The connector only |
| `component` | A fixed pigtail off a component: coil, flasher, horn, R/R, starter relay, fuse box. | The connector only |

For `subharness` and `component` the rebuild buys and terminates the mating
half; it does not build the wire on the far side. Everything found so far in
those two classes — horn, flasher, coils, the bar pigtails, the battery earth
cable — is wire the models carry but the build does not.

Getting this wrong in either direction is expensive: build wire that already
exists, or leave out wire nothing else provides. It is cheap to record now,
while both halves are in hand, and impossible to reconstruct from a cut-up
harness later.

## The melted joint at `B06.4` — a likely mechanism

`B06.4` shows melting/corrosion. Recording its mate while still connected
supplied a plausible cause, which a disconnected inspection would not have.

The joint is a double-female bullet forming a 3-way node on the **main power
path**: main harness in, starter relay out, fuse-box feed out — and the
fuse-box-side wire is **visibly larger gauge than `B06.4` itself**.

A gauge step at a bullet terminal on a high-current path is a classic
overheating site: the small conductor and the terminal interface carry current
sized for the large one. That fits both the location and the damage.

**Not established** — it is a mechanism consistent with the evidence, not a
diagnosis. Confirm during the ring-out fault survey: the procedure's >1 Ω rule
should show elevated resistance here if the joint is degraded. Worth settling,
because a rebuild that reproduces the same step at the same joint reproduces the
fault.

## ⚠️ Component pigtails count as build wire when the component is replaced

The `mate_class` table says a `component` mate means the rebuild buys the
connector, not the wire. **That inverts when the component itself is being
replaced.**

The fuse box is the live case. `B06.3`, `B06.4` and `B06.5` all land on a fixed
pigtail off the original glass-fuse box — so by the ordinary rule, none of that
wire is the rebuild's problem. But the plan is a **6-circuit blade block**
(`docs/kz305-b1-wiring.md`, 13 Aug), which means the original pigtail does not
survive and the rebuild has to build every one of those wires itself, to new
lengths, on a new layout.

So `mate_class` answers "is the far side someone else's wire", and the scope
question is one step further: **is that someone else still going to exist?**
Record the class from what is in front of you; decide the BOM against the
rebuild plan.

## Mate-side lengths are deferred, not skipped

Wires on the far side of a connector — sub-harnesses, component pigtails — are
**not measured during Step 1**, and deferring them costs nothing.

They are separate physical objects. Unwrapping the trunk, ringing it out and
cutting it up destroys none of them. Their geometry is not perishable the way
the main harness's is, which is the entire reason Step 1 is urgent.

What makes "later" fail is not time but **loss of identity**:

- A pigtail scrapped or cut before anyone decided whether it was needed.
- A pigtail separated from the component that identifies it, so that a bag of
  four similar looms cannot be told apart.
- A mate whose harness-side partner was never recorded — which is why the
  still-mated pairs got documented before separating rather than after.

So the obligation during Step 1 is **preservation, not measurement**: keep each
sub-assembly whole, keep it with its component, and tag it. Measure when the
rebuild's layout is settled and it is clear which of them are even being
reproduced.

## Words used precisely

| Word | Means |
|---|---|
| **wire** | One literal conductor, end to end. Never a bundle. |
| **branch** | A run of one or more wires travelling together. A branch of one wire is still a branch. |
| **trunk** | The main branch, from the datum rearward. |
| **fan** | A point where a branch stops being bundled and its wires go separate ways. |

The two logs split on exactly this line: `harness-lengths.csv` records
**branches** — geometry, one row per run. `connector-inventory.csv` records
**wires** — one row per cavity, per conductor. If you are recording something
per-conductor it goes in the inventory, not the lengths log.

## Two tag namespaces: `B##` branches, `C##` connectors

These are different kinds of thing and they need different names.

**`B##` is a branch** — the *run of wire itself*, from where it leaves the trunk
to where it ends. Not the breakout point, not the connector. A branch is the
thing that has a length, so a branch is what carries `breakout_mm` and
`length_mm` in `harness-lengths.csv`.

**`C##` is a connector half** — one physical endpoint. Step 0 says to tag both
halves of every connector separately, so a mated pair is two tags, e.g. `C12`
and `C13`. Connector halves are what the `from` and `to` columns name, and what
`connector-inventory.csv` keys on as `conn_tag`.

So a typical row reads: branch `B07` runs from `C01` to `C14`. Three tags, three
different physical things.

Why not collapse them into one scheme: a branch does not always end in exactly
one connector. `W_RH_BR` runs through a confirmed 1→3 splice, so one branch has
several endpoints. And a connector half is a thing you inventory cavity by
cavity, which a branch is not. One namespace cannot serve both.

### `B00.x` — the headlight junction cluster

Everything that fans out **forward** of the datum into the headlight junction.
Around a dozen connectors, all leaving at the datum itself:
`breakout_ref DATUM`, `breakout_mm 0`, with the distance forward to each
connector recorded as `length_mm`.

`B00` is a new group rather than a renumber, so it costs nothing to add after
`B01`–`B10` were already tagged.

Two things this cluster needs that the trunk did not:

- **Photograph it before disturbing anything.** A dozen connectors at one point
  is where mis-tagging is most likely, and unlike the trunk there is no
  distance to tell them apart afterwards — every one of them reads
  `breakout_mm 0`.
- **Record something identifying on every row** — connector type, pin count,
  housing colour. On the trunk a branch is identified by where it leaves. Here
  they all leave at the same place, so the connector itself is the only
  distinguishing feature a later reader will have.

### Sub-branches: `B03.1`, `B10.2`, `B03.1.1`, …

The harness is a tree, not a comb: branches have branches. A branch leaving
`B03` is **`B03.1`**, one leaving that is **`B03.1.1`**. Any depth is allowed.
The ID encodes the parent, so the structure is readable straight off the
`branch_id` column without a lookup.

```
B03                     off the trunk at 460 mm from DATUM
 ├─ B03.1               off B03,   at 120 mm along B03
 ├─ B03.2               off B03,   at 260 mm along B03
 └─ B03.3               off B03,   at 310 mm along B03
     ├─ B03.3.1         off B03.3, at 40 mm along B03.3
     └─ B03.3.2         off B03.3, at 90 mm along B03.3
```

Each level's `breakout_mm` is measured along its **immediate parent**, from that
parent's own breakout point. `B03.3.2` is never measured against the trunk.

This same suffix covers a **fan of individual wires** leaving one point — the
rear of the trunk sprays singles into bullet connectors — since a fan wire is
just a child branch that breaks out at distance 0.

#### Where a sub-branch's `breakout_mm` is measured from

**From its parent's breakout point, along the parent** — never back to the trunk
datum. `B03.1` at 120 mm means 120 mm out along `B03` from where `B03` itself
left the trunk.

Measuring nested branches back to the datum would mean summing path lengths
through bends, accumulating error at every joint, and it would throw away the
only number that actually positions the branch on its parent. Position is always
relative to the thing you are attached to.

The **`breakout_ref`** column records this explicitly: `DATUM` for branches off
the main trunk, or the parent's ID (`B03`) for a sub-branch. It is redundant
with the ID by design — a bare number in a `breakout_mm` column invites being
read against the wrong zero, and this is the kind of mistake that is invisible
until the new harness does not fit.

#### A bundle where one wire runs longer

Common case: several wires run together, most end at one connector, one carries
on somewhere else. **The long wire is a child branch**, and the point where it
leaves the bundle is its breakout.

```
B03 breaks out at 460 from DATUM
     │
     ├── bundle of 4 wires ─────────▶ C07   B03  length_mm 300
     │
     └── one wire leaves at 250 ────▶ C08   B03.1  breakout_mm 250, length_mm 190
```

The parent's `length_mm` is still measured to **its own** connector face (300).
The child's `breakout_mm` is where it actually left the bundle (250). The two
are independent measurements — a child may leave before its parent ends, exactly
at its parent's end, or anywhere between.

**Measure where the wire leaves the bundle, not where the nearest connector is.**
A wire peeling off 50 mm short of the connector breaks out at 250, not 300. That
divergence point is a real feature of the shape: it is where the tape has to
split when the new harness is built.

When the split happens *at* the parent's endpoint, `breakout_mm` simply equals
the parent's `length_mm`. `B10` is that case — trunk runs 1360, everything fans
out at the end.

#### A true fork — parent ends, several children leave at one point

The parent's `length_mm` runs to the **fork point**, its `to` reads `FORK`, and
every child's `breakout_mm` equals that same number.

```
B05  breakout_ref DATUM, breakout_mm 730, length_mm 240, to FORK
 ├─ B05.1  breakout_ref B05, breakout_mm 240, length_mm 310 → C11
 ├─ B05.2  breakout_ref B05, breakout_mm 240, length_mm 95  → C12
 └─ B05.3  breakout_ref B05, breakout_mm 240, length_mm 150 → C13
```

That equality is a **self-check**: children of a fork whose `breakout_mm` does
not match the parent's `length_mm` mean either the split is not really at one
point, or a number is wrong.

**Do not promote one child to be "the continuation" of the parent**, however
obviously it is the main run. Doing so makes the parent's `length_mm` ambiguous
— to the fork, or to that child's connector? — and the ambiguity is invisible in
the data. The parent ends at the fork; all continuations are children.

A **fan** is just a fork whose children are each one wire.

> ⚠️ **A fork is geometry, not electrics.** Wires diverging at a point and wires
> *spliced* at a point look identical under tape, and this harness has at least
> one of the latter — the confirmed 1→3 splice in the right-bar branch. Record
> the shape here and leave the electrical question to the splice table in Step 3
> of the ring-out procedure, once the loom is off and the joint is visible.
> Recording a fork does not assert that anything is joined there.

#### A zero-length fork — write no parent row

Many branches split at the very point they leave the trunk. **Do not write a row
for the parent.** Hang the children on the grandparent instead:

```
B01.1  breakout_ref DATUM, breakout_mm 400
B01.2  breakout_ref DATUM, breakout_mm 400
B01.3  breakout_ref DATUM, breakout_mm 400
B01.4  breakout_ref DATUM, breakout_mm 400
```

`B01` still exists — it is the tag on the harness and the prefix on every child
— it simply has no row, because it has nothing to measure. The grouping is
already recorded twice: in the shared prefix, and in the four identical
`breakout_ref`/`breakout_mm` pairs. A row of zeroes and blanks would add no
third fact, and rows that carry no measurement are how a log stops being read.

Write the parent row only when it has something of its own: a **nonzero length**
(it runs a distance before splitting), or a **`wire_count` for the group** you
want on record for the splice check below.

#### Which point on the connector `length_mm` runs to

**The mating face** — the end that plugs in. Not the back of the body where the
wires enter, which sits 15–25 mm away on a typical connector.

The mating face is the point whose position on the bike is fixed: the connector
has to physically reach its component. Where the wires enter the back shifts
with how they are dressed in, so it is not a stable reference.

Vary between the two across a session and that 15–25 mm lands in random rows
with nothing to mark which ones. Being consistently wrong is recoverable;
being inconsistently right is not.

Wire length for cutting is then mating face minus the connector's depth, which
is a per-connector-type constant. Record it once per type in
`connector-inventory.csv` rather than baking it into every length here — same
reason service loop is not baked in.

A branch that **forks** instead of terminating measures to the fork point, with
`to` reading `FORK`.

#### Wire count

`wire_count` is per branch. It is the completeness check against
`connector-inventory.csv` later, since the wires entering a branch have to
account for every conductor at its far ends. A parent's count should equal the
sum of its children's, and a mismatch is a splice or a wire terminating
mid-branch — a finding, not an arithmetic slip. That is exactly how the
right-bar 1→3 splice announced itself.

**A taped bundle's count is not visible, and it is not worth unwrapping for.**
Leave the parent's `wire_count` blank and record the children's, which are
countable at their connectors. Their sum is then a **prediction** to test in
Step 3 when the loom comes off anyway. A prediction that fails at that point has
located a splice deliberately, at no extra cost and with nothing destroyed early
to get it.

#### When to split, and when not to

Split into sub-branches when the children have **different lengths**. When a fan
is equal-length, one row for the group is a complete record of the geometry —
per-wire colour and gauge belong in `connector-inventory.csv` keyed by each
end's `C##`. `B10` is that case.

**The breakout point itself gets no ID.** It is identified by the branch that
leaves there plus its `breakout_mm`. Two branches leaving at the same point
simply share a `breakout_mm` value. Splices found under the loom in Step 3 are
recorded in that step's own table.

Number each series in the order you tag them. Do not renumber later; a gap in
the sequence costs nothing and a renumber invalidates every photograph.

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
| `branch_id` | `B01` — the branch, matching the tape tag on the run |
| `from`, `to` | Connector-half tags (`C01`), not descriptions. See the namespaces section. |
| `model_cables` | Space-separated `W_*` designators this covers, or blank if not modelled yet |
| `wire_count` | How many conductors the branch carries. Blank until counted. |
| `colour`, `gauge` | As read off the wire in hand. **Single-wire branches only** — leave blank on a multi-wire branch and record per-wire detail in `connector-inventory.csv`. |
| `breakout_mm` | Distance from the datum to where this branch leaves the trunk |
| `length_mm` | Path length of the branch, breakout to **connector mating face** — or to its own fork point if the branch forks rather than terminating. See below. |
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
