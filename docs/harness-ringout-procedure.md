# Old harness — ring-out and measurement procedure

The old harness is the best source you have. It outranks the 44-year-old scan
and it outranks every note in this repo. It is also the ONLY length reference
for a bike that is in pieces with the engine out.

It is going in the bin, so you are allowed to destroy it — **but only in the
right order.** Steps 0–2 are non-destructive and every later step can wipe out
data you cannot recover.

---

## Before you start

**Meter:** Fluke 87V. Short the probes, hit **REL**. Re-zero after swapping
probes for clips — clip leads read higher than points, and that difference will
otherwise land in your records.

**Also want:** masking tape and a marker, a flexible tape measure, a length of
string, a long jumper lead with clips on both ends, and a camera.

**One rule throughout:** colour proposes, the meter disposes. Use colour to pick
which ends are *worth* probing, never to decide what connects to what.

> ⚠️ **Wires change colour at in-sleeve splices.** Confirmed 17 Aug inside the
> **right-bar switchgear branch** — not seen in the main trunk. Elsewhere is
> unknown rather than clean, since nothing else has been unwrapped yet.
>
> One confirmed case is enough to invalidate colour-based shortcuts everywhere:
> if a wire is green at one end and grey at the other, no amount of probing green
> ends will ever find its partner. So the sequence below still takes **the loom
> off early** rather than at the end — but expect the right-bar branch to be
> where it actually bites.

---

## Step 0 — Tag every end  ·  NON-DESTRUCTIVE

Tag with tape and marker before touching anything else, using **two separate
number series** — they name different kinds of thing:

- **`B01`, `B02`, …** on each **branch** — the run of wire itself, tagged near
  where it leaves the trunk. A branch is what has a length, so `B##` is what
  carries `breakout_mm` and `length_mm`.
**Connectors need no tag of their own.** A connector is named by the branch it
terminates — `B04.3` *is* the R/R connector — so the branch tags already
identify every connector on the harness. Where one branch ends in more than one
separable terminal, suffix with a letter (`B01.3a`, `B01.3b`); a multi-way
housing is one connector however many wires it carries.

The far half of a mated pair needs no tag either: it belongs to a component or a
child harness, not to this loom, and `mates_to` names it in words.

The string on the tape and the ID in `measurements/` are the same string — that
is what makes a measurement traceable to a physical thing. Number each series in
tagging order. Do not renumber later; a gap costs nothing, a renumber
invalidates every photograph.

The breakout point itself gets no tag: it is identified by the branch leaving
there plus its distance from the datum.

Then photograph: the whole harness laid out with tags visible, and each
connector face-on with the pins showing. (The reference doc has been asking for
face-on connector shots since 13 Aug — this is that.)

> Do this first because you cannot record a connection between two things that
> have no names. Once branches get moved around, "the brown one near the middle"
> stops meaning anything.

---

## Step 1 — Lengths  ·  NON-DESTRUCTIVE  ·  **DO THIS BEFORE ANYTHING ELSE**

Everything after this step can destroy lengths permanently.

1. Lay the harness in its natural shape. Do not stretch it straight — it was
   built with bends in it.
2. Pick a datum and write it down. The main junction or the fuse box is the
   obvious choice.
3. Measure the **trunk** first, then each branch from its **breakout point** to
   the connector face.
4. Measure **along the path**, not point to point. Lay string in the groove of
   the harness, mark it, then measure the string against the tape.
5. Record where each branch leaves the trunk, as a distance from the datum.
   That is what actually determines the shape of the new harness — branch
   lengths alone will not reproduce it.

Record into **`measurements/harness-lengths.csv`**, one row per branch, and the
datum plus breakout order into **`measurements/trunk-map.md`**. The scheme,
including how to redo a measurement without destroying the first one, is in
`measurements/README.md`.

Record raw measurements. Add service loop at build time, not here — bake slack
into the record and you will never know what the real number was.

⚠️ **Measure branches that are not modelled yet too.** Lighting, horn and
instruments are still untranscribed (#9), but the loom gets cut up long before
that is finished. A branch with no `W_*` designator still gets a `B##` tag and a
row; the designator can be filled in later, the length cannot.

---

## Step 2 — Connector inventory  ·  NON-DESTRUCTIVE

For every tagged connector, one row per cavity.

| Conn tag | Type / pin count | Cavity | Wire colour | Gauge |
|---|---|---|---|---|
| | | | | |

Note the **base colour first** on every two-colour wire. Br/W and W/Br are
different wires, and this project has already been bitten by that twice.

---

## Step 3 — Unwrap the loom  ·  **DESTRUCTIVE** — but it has to come before ring-out

Lengths are recorded, so the loom has done its job. Take the tape off the trunk
and photograph what is underneath as you go.

Doing this *before* the ring-out rather than after is the whole difference
between a map you can trust and one with silent holes in it. With the sleeve
off, splices are visible objects you can record directly instead of anomalies
you have to infer from continuity data that was never designed to reveal them.

Record every splice — **including the colour on each leg**, since they change:

| Splice | Position (mm from datum) | Colour in | Colours out | Ways |
|---|---|---|---|---|
| | | | | |

---

## Step 4 — Ring out the connectivity

**Colour narrows the search, but it CANNOT close it.** Same-colour ends are the
cheap candidates — start there. But every end that does not find a partner among
them is a wire that changes colour at a splice, and those need an exhaustive
sweep against *all* remaining ends. Step 3 tells you where to expect them.

**Completeness check — this is the one that catches what you missed.** Every
wire end must terminate somewhere. Count your ends in Step 2, tick each one off
as it gets a partner, and at the finish **every end must be accounted for.**
Leftovers are not stray wires; they are unmapped splices. Do not stop until the
count closes.

**Record ohms, not beeps.** A corroded conductor still beeps. A harness wire
should be milliohms — anything over about **1 Ω is a damaged conductor**, so
this pass doubles as a fault survey and will likely explain which circuits had
already stopped working.

| From (tag/cavity) | To (tag/cavity) | Colour at each end | Ω | Via splice? |
|---|---|---|---|---|
| | | | | |

⚠️ **Never record a circuit by colour alone.** With colour-changing splices in
play, "the green one" is not an identity — it is a description of one end.

---

## Step 5 — The specific questions blocking the models

These are worth doing deliberately rather than hoping they fall out of Step 3.

**0. RIGHT-BAR BRANCH MAP.** ✅ **CLOSED 17 Aug 2026** — resolved by unsleeving
the branch rather than by ring-out. Y/R + Y/R merge in a 2→1 splice; Br expands
in a 1→3 splice to Br, Br/W, Bl/W; BK runs straight through. The wire-count
mismatch is fully explained and the Y/R shared node is confirmed. Bl/W was then
traced to a fuse, making it the **feed into** the branch, not a tap out of it.
See `docs/kz305-b1-wiring.md`. **Br/W remains unidentified** — now item 0b.

**0b. FUSE BOX RING-OUT + Br/W SWEEP — do this one first.** One session closes
three open items: which holder is `FUSE_A`, the diagram-vs-bench feed conflict,
and where Br/W goes.

*Setup:* fuse box on the bench and disconnected from everything. Zero the leads
with REL (they read 0.4 Ω). **Pull every fuse before probing** — with fuses in,
the holders are bridged and every reading is meaningless.

**A. Inventory before probing.** Photograph the box with a paint-pen mark on one
end so "holder 1" means the same thing next session. Record each holder's
printed rating and whether the fuse is intact. Record the wire colour at each
terminal. The ring-out that follows establishes which holder feeds what, which
colour alone cannot tell you regardless of how clearly it reads.

**B. Is the input a common bus or separate feeds?** Fuses out, probe input
terminal 1 ↔ 2, 1 ↔ 3, 2 ↔ 3.

- **All closed (< 1 Ω)** → common input node, matching the diagram's single red
  wire branching to both 10 A fuse tops.
- **Any open** → separate feeds, matching the 13 Aug note of three feeds in
  white, blue and red.

This settles the conflict the two documents cannot settle between themselves.

**C. Which holder is `FUSE_A`?** Fuses out. Clip the reference lead to the
**Bl/W** wire that mates with the right-bar branch, and probe each holder's
**output** terminal in turn. Exactly one should read < 1 Ω. That holder is
`FUSE_A`, and its rating and neighbours are the first hard data for the PDM
cavity map.

**D. Where does Br/W go?**

🛑 **Unmate the 4P first, and clip the reference to the Br/W pin on the
MAIN-HARNESS side.** Br, Br/W and Bl/W are all one net through the 1→3 splice,
so probing the switch side rings out the entire branch and tells you nothing.
The unmated main-harness side is the only place the question is answerable.

Then sweep **every** free end in the harness — fuse terminals, lamp sockets,
connector pins, ground eyes. **Do not narrow by colour.** A colour change is the
whole reason this end is hard to find, so colour cannot also be the search key.

**Record the resistance, not just continuity.** The value identifies the load
before you can even see it:

| Reading | Means |
|---|---|
| < 1 Ω | direct wire — the far end is a connector, splice or switch |
| ~1–5 Ω | through a coil — horn, relay coil, solenoid |
| ~10–100 Ω | through a filament — a lamp, and the wattage narrows which |
| open everywhere | the far end is unmated, cut, or inside a component |

Log **every** hit, not just the first. If Br/W lands on another in-sleeve splice
it will show several, and a partial answer recorded as complete is worse than no
answer.

**1. Ground net base colour — BK/Y or Y/BK?**
Your own two records disagree: the 17 Aug hands-on read says BK/Y and was
recorded as "pretty sure", the 13 Aug note says Y/BK. The diagram reads
yellow-primary, but the scan is the weakest of the three sources. Only the hedge
is being re-checked here, not your eyes — a cut end shows base against stripe
unambiguously and closes it in one look.
Answer: ______________

**2. Fuse box mapping.** The one place the scan and the bench notes actively
conflict — the diagram shows both 10 A fuses sharing a common red feed, the
13 Aug note describes three feeds in white, blue and red. The box is on your
bench, so ring it out. For each holder, record the input wire, the output wire,
and where each goes.

| Fuse | Rating | Input colour | Output colour | Feeds |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**3 & 4. Br/W, Bl/W and the two Y/R wires** — all four are answered by item 0
above. Do that first and these fall out of it.

**5. Second harness tag.** One reads `26001-12348`. A second tag on another
branch has never been logged, and it identifies the harness variant.
Answer: ______________

**6. Dimmer common.** Open since 13 Aug. This one is **on the switch, not the
harness** — cluster unplugged, three pins R/BK · Bl · R/Y, find the pin that
appears in both HI and LO. Getting it wrong lights both filaments at once, and
it blocks the headlight relay decision.

| Pair | HI | LO |
|---|---|---|
| R/BK ↔ Bl | | |
| Bl ↔ R/Y | | |
| R/BK ↔ R/Y | | |

---

## Step 6 — Final sweep

Re-walk the unwrapped trunk against your Step 4 table. Anything on the harness
that does not appear in the table is something you have not explained yet.

---

## What comes back to the models

| Step | Updates |
|---|---|
| 1 | Lengths throughout `models/kz305-rebuild.yml`; unblocks the BOM |
| 2 | Connector pinouts in `models/kz305-factory.yml` |
| 3 | **Splice nodes** — the factory model currently draws every circuit as one wire end to end. Each colour-changing splice needs a real node in the drawing, or the model is wrong about what the harness physically is |
| 4 | The connection map |
| 5.1 | Settles the BK/Y vs Y/BK dispute |
| 5.2 | Fuse assignments → PDM cavity map, the last original TBD |
| 5.3 | Front brake switch → closes the Br/W and Bl/W unknowns |
| 5.6 | Dimmer common → unblocks the headlight relay decision |
