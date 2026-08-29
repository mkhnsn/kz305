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
the bench, so the collision had to be resolved by continuity.

**It was, on 2026-08-28.** `B05.1` and `B05.2` each ring through to a slot in the
`B04.3` 4P, and are not continuous with each other. So `B05` is the alternator
phase pair (`W_ALT`) and `B04.3` is the regulator/rectifier connector. The left
points and condenser leads are elsewhere and remain unlocated.

That also promotes a bench-vs-model conflict from "if this is RR" to a real one:
the model gives `W_RR_OUT` as **white**, and the confirmed R/R connector carries
**brown**. Unlike the gauge questions this one does not depend on any
unmeasured quantity — it is a colour read off the wire in a connector whose
identity is now established.

**⚠️ Superseded 2026-08-29.** This conflict is not real. The R/R does not drive
the brown wire — its cavity is unpopulated on the R/R half, and the DC output
leaves on a `W/R` bullet outside the connector. See the overturned-conclusion
note under *The charging output feeds the switched-ignition net*.

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

### RESOLVED 2026-08-28 by meter: two separate ground nets

Reference lead clipped to the `B04.1` chassis-ground ring terminal:

| Probe | Colour | Reading |
|---|---|---|
| `B00.7` | `Y/BK` yellow base | **0.2 Ω** |
| `B08` | `Y/BK` yellow base | **0.2 Ω** |
| `B00.2` | `BK/Y` black base | **open** |
| `B10.5` | `BK/Y` black base | **open** |
| `B04.3` (R/R ground) | `BK/Y` black base | **open** |
| `B04.5` | `BK/Y` black base | **open** |

Clean split along base colour, no ambiguity:

- **Net A — `Y/BK`, yellow base.** `B04.1` (the chassis ring), `B00.7`, `B08`.
  Continuous, low resistance.
- **Net B — `BK/Y`, black base.** `B00.2`, `B10.5`, `B04.3`, `B04.5`. **Open to
  the chassis ring entirely.**

This settles the question shelved earlier in favour of the **two-nets** reading.
The competing "two tiers of one net" reading — branch grounds collected onto a
heavier common return — is **disproved**: a common return would have rung
continuous, and every black-base point is open.

### This contradicts the documents

`docs/kz305-b1-wiring.md` (13 Aug) records *"exactly one ring terminal on the
entire harness … everything returns through that one point."* The meter says
otherwise: the black-base net does not return through `B04.1`. By working rule 1
the bench value stands and the document needs correcting.

It also means the models are wrong in a structural way, not merely a cosmetic
one. They render every ground as `BKYE` returning to a single `GND_CHASSIS`.
There are two nets, they are different colours, and only one of them reaches
that ring.

### What this means for the star ground

The rebuild's headline change is a star-ground bus, and this defines what it
replaces: not one marginal ring terminal but a **distributed earth** spread over
component mounting points, on a frame that is being powder-coated.

Every component currently earthing through its own mounting hardware needs a
**new ground wire back to the bus** — wire that does not exist in the harness
today and appears nowhere in the models, because the models draw all of it as
`BKYE` returning to a single `GND_CHASSIS` that Net B never reaches.

That is a scope addition, not a detail. The count of those wires is the count of
Net B earth points, which is not yet known.

### What is still unknown

- **Is Net B one net or several — answered 2026-08-28.** One net. Reference on
  `B10.5` with probes re-zeroed: `B04.3` **0.0 Ω**, `B00.2` **0.2 Ω**,
  `B04.5` **0.3 Ω**. Every black-base point is continuous with every other,
  spanning tail to `B04` to the headlight junction.

  So Net B is a single harness-wide return net that leaves through the child
  harnesses to earth at several component mounting points — parallel earth paths
  onto one net, rather than several independent grounds.

  **Good news for the star ground:** it is one net to re-terminate, not four.
- **Where does Net B ground — answered 2026-08-28.** It does not return through
  the main harness at all. Net B reaches earth through the **child harnesses**:
  component pigtails that ground at whatever they are bolted to — some to the
  engine block, some to the frame, others elsewhere. That is why every black-base
  point reads open with the harness on the bench; its returns are all outside it.

  So the harness has **one ring terminal but many earth points**, and the earth
  points are distributed across component mounting hardware rather than
  collected. Each has to be traced through its own child harness as those get
  worked — the main harness cannot answer for any of them.
- **`B04.5` reads high for its path length.** With probes re-zeroed on Net B,
  `B04.3` reads 0.0 Ω from `B10.5` — most of the length of the harness — while
  `B04.5` reads 0.3 Ω over a comparable path from the same reference. Both are
  under the procedure's 1 Ω damage threshold so neither is condemned, but 0.3 Ω
  against 0.0 Ω on similar runs points at a marginal crimp or bullet contact at
  `B04.5`. Worth a re-read and a look at the terminal.

- **Net A's 0.2 Ω readings predate the re-zero.** `B00.7` and `B08` were measured
  before the probes were re-zeroed on Net B, so that 0.2 Ω may be lead offset
  rather than wire. Re-read Net A now that the meter is zeroed; if it drops to
  0.0 Ω the net is clean, and if it holds at 0.2 Ω that is real resistance in a
  three-point net and worth explaining.

## Condition findings are out of scope; design findings are not

The harness is being replaced with a new build, so the **condition** of the old
one does not matter: aged crimps, marginal contacts and per-joint resistance are
all discarded with the wire. Fault-survey readings are not worth chasing for
their own sake, and the procedure's >1 Ω rule is not a gate on anything here.

What still matters is anything the old harness reveals about **design** — a
fault the new build would inherit by copying the layout:

- `B06.4`'s melting sat at a gauge step on a bullet junction carrying the main
  power path. Reproduce that topology and it heats again, in new wire.
- The distributed Net B earth is a design property, not wear, and is exactly
  what the star ground replaces.

The test for whether a fault finding is worth recording: **would building a
brand-new harness to the same drawing reproduce it?** If yes it is a design
input; if no it died with the old wire.

## Double-female bullet terminals: one harness wire, two empty slots

Six branches end in a double-female bullet terminal — `B03`, `B08`, `B00.5`,
`B00.7`, `B00.8`, `B00.11`. In every case the **harness contributes one wire**
into the crimp, and the terminal presents two receptacle slots that are **both
empty**.

They are fan-out points where up to two external male bullets plugged in. Those
males were unplugged at teardown, before this project's tagging existed, and
what went into each slot **is not recorded anywhere**.

This is the one place a real gap exists in the map, and no bench work closes it:
the information left with the teardown. Two partial routes back:

- **The on-bike photographs**, which predate the teardown.
- **The components and child harnesses themselves** — a male bullet of the right
  colour on a component narrows it, though it will not disambiguate two
  same-colour candidates.

Recording the slots as empty is itself the finding. A later reader must not
mistake an unpopulated node for a node with nothing to say.

### Consequence: the Br/W net has a hidden internal junction

`B01.2`, `B00.11` and `B06.5` all ring continuous on Br/W. `B00.11` holds one
wire with both slots empty, and **one wire cannot reach three endpoints**.

Therefore a splice or shared crimp joins those runs **inside the harness, under
the tape**. Its location is unknown. Step 3 should find it, and now knows to
look — which is exactly the kind of thing the procedure warns gets missed when
the loom is unwrapped after the ring-out instead of before it.

## Net consolidation, 2026-08-28

Taken with **every pigtail disconnected**, so nothing rings through a component
or the fuse box.

| Colour | Result |
|---|---|
| **W/R** | `B04.6` ↔ `B06.4` **0.1 Ω — one net.** The main power path: `B06.4`'s node feeds the starter relay and the fuse box. |
| **W/Bl** | `B00.8` ↔ `B09` **0.3 Ω — one net**, seen at the headlight junction and at 1060 mm on the trunk. |
| **Y/R** | `B03` ↔ `B01.2` **0.2 Ω**; `B06.1` **open to both**. **Two independent Y/R nets.** |

### The net map as it stands

Ten nets across eight colours, all read with every pigtail disconnected:

| Net | Points | Circuit |
|---|---|---|
| **Br** | `B00.1` `B00.3` `B00.5` `B01.2` `B01.3` `B02.3` `B04.3` `B04.4` `B07.2` | switched-ignition bus (9 points) |
| **W/R** | `B04.6` `B06.4` | main power path |
| **W/Bl** | `B00.8` `B09` | unidentified |
| **Y/R 1** | `B03` `B01.2` | kill-switch output to the coils (`SP_YR`) |
| **Y/R 2** | `B06.1` | separate circuit, **missing from the models** |
| **Bl 1** | `B00.6` `B04.2` `B10.4` | brake (`SP_BRAKE` confirmed) |
| **Bl 2** | `B02.2` `B06.5` | fused headlight supply to the dimmer |
| **BK 1** | `B02.1` `B01.3` | horn button return |
| **BK 2** | `B06.2` `B01.2` | starter trigger |
| **Gn** | `B00.1` `B00.10` `B02.3` `B10.3` | left turn |
| **Gy** | `B00.1` `B00.4` `B02.3` `B10.1` | right turn |

Plus the two ground nets: **Net A** `Y/BK` (`B04.1` `B00.7` `B08`) and **Net B**
`BK/Y` (`B00.2` `B10.5` `B04.3` `B04.5`), open to each other.

Green and grey are structurally identical, as a symmetric signal pair should be:
left-bar switch → headlight-junction two-into-one crimp → instrument cluster →
tail.

**Three of eight colours carry more than one circuit** — Y/R, blue and black.
Colour is not identity in this harness, and that now rests on measurement rather
than on the warning in the models.

### Brown is a single net with nine harness endpoints

Reference on `B00.1`'s brown, all pigtails disconnected:

| Point | | Point | |
|---|---|---|---|
| `B00.3` ignition 4P | 0.0 Ω | `B02.3` left 6P | 0.0 Ω |
| `B00.5` | 0.0 Ω | `B04.3` R/R 4P | 0.0 Ω |
| `B01.2` RH_4P | 0.1 Ω | `B04.4` | 0.7 Ω |
| `B01.3` horn | 0.1 Ω | `B07.2` flasher feed | 0.0 Ω |

One net, no splits — unlike Y/R. This is the switched-ignition distribution bus,
and it corresponds to the models' `SP_BR`, which feeds `FBRK`, `RBRK`,
`FLASHER`, `FUSE_A` and `IND_N` from `IGN`. The bench net reaches **nine**
harness points against the model's six branches, the extras being the horn feed,
the two bar-switch connectors and `B00.5`.

`B04.4` reads 0.7 Ω against 0.0–0.1 Ω everywhere else. Under the 1 Ω threshold
and a condition matter rather than a design one, so not pursued — recorded only
so the outlier is not mistaken for a transcription slip.

#### ~~The charging output feeds the switched-ignition net~~ — OVERTURNED 2026-08-29

##### OVERTURNED 2026-08-29 — read the section below with this first

The argument in this section is **wrong**, and it is worth understanding how,
because the reasoning looked airtight.

It ran: the alternator is single phase, so the R/R connector's four wires are
two AC in, DC out and ground; there is **no spare pin**; therefore brown is the
DC output. Every step follows — except the premise.

At the bench 2026-08-29, with the mirror-image orientation explicitly accounted
for, **the R/R half of the 4P has no wire in the brown cavity.** It is populated
on three cavities only: `Y`, `BK`, `Y`. The harness's brown lands on an empty
mate. There *is* a spare pin, so the argument never had a fourth wire to force
brown into.

The component is a **Shindengen SH221-12**, identified at the bench, and it is
**stock**. It carries four leads — in physical order off the body, `Y` `BK` `Y`
`W/R` — and only three of them enter the 4P. The `W/R` leaves to a **male
bullet** outside the connector.

The "no spare" argument does hold, but on **the component's leads**, not on the
connector's cavities: two AC in, one ground, one lead remaining on a
single-phase unit. **`W/R` is the DC output.**

That lands it on the known **main power path** — `W/R` is `B04.6` ↔ `B06.4`,
0.1 Ω, feeding the starter relay and the fuse box — which is an ordinary
charging circuit and makes the models' `W_RR_OUT` (white, `RR`→`SOL`) broadly
**correct**, not wrong on both counts as claimed below.

**What survives unchanged:** the brown at `B04.3` really is continuous 0.0 Ω
with the switched-ignition net. That was a meter reading and it stands. What
falls is the inference that the R/R *drives* it.

**What is still open:**

- ~~**Ring the R/R's `W/R` bullet to `B04.6`/`B06.4`.**~~ **CLOSED 2026-08-29
  by elimination, and continuity could never have closed it anyway** — two
  unmated halves prove nothing, two mated halves prove only that they touch.

  The harness holds **exactly two `W/R` terminals**: `B04.6` (female) and
  `B06.4` (male). The R/R's DC lead is a **male** bullet, so it can mate only a
  female, and `B04.6` is the only one in the harness. `B04.6` and `B04.3` also
  share a breakout point (`B04` + 200 mm), so the R/R's two connections leave
  the loom together — which closes the loophole that the lead might reach a
  child harness instead.

  So the circuit is: **R/R → `B04.6` → the `W/R` net → `B06.4`'s double-female
  node → starter relay + fuse box.**

  **This restores the models.** `W_RR_OUT` is drawn white, `RR`→`SOL`, and
  `B06.4`'s node feeds the starter relay. The models were right; the 28 August
  reading was inverted. The bench-vs-model conflict on `W_RR_OUT` is not a
  conflict and should not be carried into the rebuild as one.

  This rests on the candidate list being complete, which is a property of the
  branch tagging. **If an untagged `W/R` female bullet ever turns up, this
  reopens.**
- **Pull the SH221-12 pinout** and confirm on paper that three pins are
  populated and the fourth lead is DC out — closing it from the component side
  too.
- **Why does a stock harness run brown into a cavity the stock R/R never
  populates?** Likely a housing shared across model variants, or a sense lead
  unused here. Unresolved, and not a fault.

**The lesson for the rest of this pass:** "the pin count accounts for every
function" is an argument about a *drawing*, not an observation of a *harness*.
Both halves of a connector have to be looked at. An unpopulated cavity is
invisible from the harness side, and it will silently invert a conclusion.

**Design consequence — withdrawn.** The claim below that every charging amp
passes through the ignition switch contacts does not hold, and the rebuild
should not be designed around it.


`B04.3` is the confirmed R/R connector and its brown wire rings 0.0 Ω to the
ignition switch's brown output.

The alternator is **single phase**, so the connector's four wires are fully
accounted for: two AC leads in, DC out, ground. There is no spare pin, and
therefore brown is the **DC output** — not a sense or field wire.

So charging current returns to the battery *through the ignition switch*:

```
R/R  --brown-->  switched-ignition net  -->  ignition switch (ON: W <-> Br)  -->  battery
```

which the switch table in `docs/kz305-b1-wiring.md` supports directly: **ON**
closes `W` ↔ `Br`, battery to ignition.

**This makes `W_RR_OUT` wrong in the models on both counts.** It is drawn as
white and running `RR`→`SOL`; on the bench it is brown and lands on the brown
switched net. Bench beats document, and unlike the gauge questions this rests on
nothing unmeasured — a continuity reading between two identified connectors.

**Design consequence:** every amp the alternator produces passes through the
ignition switch contacts. That is a real current path for the rebuild to
consider rather than reproduce unexamined, and it is exactly the sort of thing
that only shows up by ringing the harness rather than reading the drawing.

### Blue is two nets

| Net | Points | |
|---|---|---|
| **Blue 1 — brake** | `B00.6` · `B04.2` · `B10.4` | Front brake switch output at the headlight junction, into the `B04.2` two-into-one crimp (`SP_BRAKE` confirmed), on to the tail lamp. |
| **Blue 2 — headlight supply** | `B02.2` · `B06.5` | A fused feed from the fuse box reaching the left-bar junction. |

Blue 2 settles what `B02.2` is: not a brake wire — it is open to that net — but a
**fused supply arriving at the left switch**, where the dimmer sits
(`R/BK` · `Bl` · `R/Y`). It is the headlight feed into the dimmer common.

**Design consequence — this bears on the headlight relay decision.** Headlight
current is fed through a fuse to the handlebar switch and switched there, so the
full lamp load passes through the bar switch contacts. That is the standard
argument for adding a relay, and it is now established from the harness rather
than assumed. It does not settle procedure item 5.6, which asks which *pin* is
the dimmer common and is a switch-side test.

### Probe hygiene: scrape before you trust a high reading

Two readings this session came back high and wrong — `B03`↔`B01.2` drifted
30→12 Ω and remeasured at 0.2 Ω; `B02.2`↔`B06.5` read 23 Ω and remeasured at
0.1 Ω after the terminal face was scraped.

Corroded contact surfaces do not matter for a harness being replaced, but they
**actively produce false readings**, and 10–100 Ω is the band the procedure
reserves for a path through a filament. A dirty terminal can therefore imitate a
load and turn one net into two in the record.

Clean the contact before probing, and treat any reading in the tens of ohms as
suspect until re-read on fresh metal. This is a measurement-reliability rule,
not a condition check.

### Black is two nets, and both identify

| Net | Points | Circuit |
|---|---|---|
| **Black 1** | `B02.1` (left-bar junction) · `B01.3` (horn) | **Horn button return.** The switch table gives the horn button as `BK` ↔ ground, and the button is on the left switch — so this is the horn's return leg up to it. |
| **Black 2** | `B06.2` (starter relay branch) · `B01.2` (RH_4P) | **Starter trigger.** The right bar carries the start button; the switch table gives Push = `Y/R` ↔ `BK`, and the docs record COIL+ as the `BK` lead from the start button. Start button to relay coil. |

Open to each other, 0.1 Ω and 0.2 Ω internally.

Both identifications are **corroborated from two independent directions** — bench
continuity, and switch tables transcribed weeks earlier from a different source.
Neither was used to steer the other.

This also closes two of the four black roles the models warn about. The
remaining two — right points lead and chassis ground — are not on these nets, so
they live on child harnesses or on wires not yet reached.

### Y/R is two nets, and the models have one

`Y/R` Net 1 — `B03` and `B01.2` (RH_4P) — is consistent with `SP_YR`: the
kill-switch output reaching the coils via the right-bar 4P.

`Y/R` Net 2 — `B06.1`, on the branch that serves the starter relay and fuse box
— is open to both. It is a **separate circuit that happens to share the colour**.

The cable index carries one `YERD` net only (`W_COIL_L_FEED`, `W_COIL_R_FEED`,
`W_RH_YR1`, `W_RH_YR2`, `W_RH_YR_OUT`, all through `SP_YR`). A second Y/R
circuit exists on the bench and is **missing from the models entirely**.

This is the third distinct colour collision found, after black (four roles) and
yellow (alternator vs points). The pattern is now unmistakable: **this harness
reuses colours across unrelated circuits, and any identification resting on
colour alone is unsafe** — including identifications in the models themselves.

### A rejected reading, kept

The first `B03` ↔ `B01.2` reading drifted from 30 Ω down through 12 Ω rather
than settling. It was rejected at the bench as bad probe contact and the
remeasure gave 0.2 Ω. **Both are recorded.** The rule against overwriting a
measurement applies to continuity as much as to length — a drifting reading is
evidence about the probe or the terminal, and deleting it leaves the next reader
unable to tell a clean result from a tidied-up one.

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

## Connectors are named by their branch — there is no `C##` series

A connector is identified by **the branch it terminates**. `B04.3` is the
regulator/rectifier connector; `B01.2` is the right-bar 4P. No second tag, and
no second sticker on the harness.

This works because the branch tree was mapped deep enough that almost every
branch ends in exactly one connector. Where it does not, suffix with a letter:

- **`B01.3a`, `B01.3b`** — the horn branch ends in two *individual* spade
  terminals, which are two separable connectors, not one housing.
- A multi-way housing is **one** connector however many wires it carries.
  `B02.3` is a single 6P, not six of anything.

Record the letter suffix only where a branch genuinely has more than one
terminal. Most rows need no `terminal` value at all.

**The far half needs no tag either.** It is not part of this harness — it is a
component or a child harness, and `mates_to` names it in words ("fuse box
pigtail", "headlight pigtail"). Tagging both halves would only matter if both
halves were being rebuilt, and they are not.

## Cavity numbering — stated 2026-08-29, before the first inventory row

`connector-inventory.csv` carries one row per cavity, and a cavity number is
worthless without a rule for which cavity is number 1. The rule, in order:

1. **Use the housing's own molded numbers** wherever it has them. A part that
   is later identified has to agree with its datasheet, and renumbering a
   connector after the fact means re-reading every wire in it.
2. **Where the housing carries no numbers**, view it from the **mating face**
   — the end that plugs in, the same face `length_mm` is measured to — with the
   **latch or keyway UP**, and number **left to right, top row first**.

```
Viewed from the mating face, latch up:

  [1][2][3]
  [4][5][6]
     ^latch
```

### A moulded mark is not a moulded cavity number

Rule 1 means **numbers that label the cavities** — one per cavity, reading in
sequence, sitting next to the holes. Most housings also carry moulding marks
that are nothing of the kind:

| Mark | What it is |
|---|---|
| A lone digit | The **mould-tool cavity** — which cavity of the injection mould made this part. Nothing to do with the wire positions. |
| A letter in a circle, or a logo | Maker's mark. |
| A symbol in a diamond or triangle | Resin / material identification. |

`B04.3` carries all three — a diamond-hashtag, a `5`, and a circled `T` — on a
**four**-way housing. The `5` proves itself: a 4-cavity connector has no cavity
5. It is a part-identification lead, not a position.

The test: a real cavity numbering has **as many numbers as there are cavities**,
and they sit **at** the cavities. One number floating on the face is a mould
mark. When in doubt, treat it as a mould mark, use the latch-up rule, and record
the marks verbatim in `notes` — they are the best lead on the part number, and
they cost nothing to keep.

Every row says which rule applied, in `notes`: `cavity rule: molded` or
`cavity rule: latch-up`. The two can disagree, and a later reader holding the
datasheet needs to know which one they are looking at without guessing.

**Where the housing has no latch and no keyway**, say so and describe the
orientation used in words on every row of that connector — an unkeyed housing
has no intrinsic up, so the number means nothing without the description.

### ⚠️ Never orient by the moulded marks

**The keyway or latch is the only datum.** Moulded marks are cast wherever the
tool put them and they are not consistent between connectors, so "labels the
right way up" is not an orientation rule.

Proven on this harness, 2026-08-29:

| Connector | With the keyway UP, its marks read |
|---|---|
| `B04.3` R/R 4P | **upright** |
| `B06.5` fuse-box 4P | **upside down** |

Two connectors, same harness, same session, opposite answers. `B04.3`'s row was
originally written as though keyway-up and labels-upright were two independent
references agreeing; they agreed **by coincidence**. Had `B04.3` been the one
with inverted marks and the marks been trusted, its cavity map would have come
out rotated 180° — swapping the brown against the ground, and the two yellows
against each other.

Record the marks verbatim, as a part-identification lead. Never orient by them.

### Inventory columns

| Column | |
|---|---|
| `branch_id` | The branch this connector terminates — `B04.3`. The connector's identity; there is no separate connector tag. |
| `terminal` | Letter suffix only where one branch ends in more than one separable terminal (`B01.3a`, `B01.3b`). Blank otherwise. |
| `type` | What the connector physically is — `4P rect`, `male bullet`, `spade`, `ring`. |
| `pin_count` | Cavities in the housing, **populated or not**. An empty cavity is a finding; see the double-female bullets. |
| `cavity` | Position per the rule above. Blank on a single-terminal connector. |
| `colour` | The wire in that cavity, **base colour first**. |
| `gauge` | Visual estimate only — see the gauge warning above. Blank means the common size. |
| `mates_to` | The far half, **in words**: `fuse box pigtail`, `headlight pigtail`. The far half carries no tag. |
| `mate_class` | `component`, `subharness`, or `open` where nothing was found mated. |
| `model_connector` | The models' connector name (`RR`, `RH_4P`), or blank if not modelled. |
| `recorded_on` | ISO date. |
| `status` | `provisional`, `confirmed`, `superseded`. Same append-never-overwrite rule as lengths. |
| `notes` | The cavity rule used, plus anything that changes how the row reads. |

**Depth belongs here, once per connector type** — mating face to the back of the
body, the constant that turns a `length_mm` into a cut length. Record it in
`notes` on the first row of each type rather than in every lengths row.

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
per-wire colour and gauge belong in `connector-inventory.csv`, keyed by the
branch. `B10` is that case.

**The breakout point itself gets no ID.** It is identified by the branch that
leaves there plus its `breakout_mm`. Two branches leaving at the same point
simply share a `breakout_mm` value. Splices found under the loom in Step 3 are
recorded in that step's own table.

Number each series in the order you tag them. Do not renumber later; a gap in
the sequence costs nothing and a renumber invalidates every photograph.

### The tape tag is the identity — correct the log, not the harness

Where the log and the tape disagree about a branch's ID, **the tape is right by
definition**. `branch_id` is defined as the tag on the run; a log ID with no
sticker behind it refers to nothing, and re-labelling the harness to match a
spreadsheet invalidates every photograph taken so far.

This happened on 2026-08-29. The two alternator yellows were logged as
`B05.1`/`B05.2` by flattening the bench tagging — a flattening that was recorded
at the time as deliberate, with an explicit *"confirm against the tape tags"*.
The tape reads **`B05.1.1`/`B05.1.2`**, and no `B05.2` sticker exists anywhere on
the harness. The log moved.

**An implied parent needs no tag.** `B05.1.1`/`B05.1.2` imply a `B05.1` that is
not on the harness and never will be: the two yellows separate at the fork where
`B05`'s tape ends, so the intermediate level has zero length and nothing to
measure. Record it as `breakout_ref` and say in `notes` that no such tag exists,
so a later reader does not go hunting for one.

Deeper-than-necessary tags are worth **nothing to fix and something to change**.
Leave them.

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
- **`confirmed` means measured twice**, by preference on different days. It is
  about the *measurement*, not the identification. A branch whose circuit has
  been proved by continuity is still `provisional` if its length was measured
  once — record the identification in `model_cables` and `notes`, never by
  promoting `status`.
