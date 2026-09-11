# Part selection — flasher and regulator/rectifier

Research for issues #11 and #12, 18 Aug 2026. Nothing here is ordered or
committed; the models still carry `part TBD`.

Two constraints drive both choices and are already confirmed on the bench:

- **The alternator is single-phase.** Two yellow leads, 0.4 Ω across the pair
  (spec 0.36–0.54 Ω, printed 159), about 75 V AC at 4,000 rpm.
- **The stock flasher socket is 2-pin.** Brown in, orange out, **no ground
  terminal** — confirmed off the diagram 17 Aug 2026.

---

## Flasher (#11)

Rewiring the flasher socket is acceptable, so the choice is **not** constrained
to a 2-wire unit. Run the ground wire and pick on merit.

### The load numbers make this an easy choice

With full LED, only one side flashes at a time, so the flasher carries roughly
**2–4 W** — two signals plus the dash indicator. Every candidate below is
specified ten times above that or more. Capacity is simply not the deciding
factor here, which frees the choice up considerably.

That also reframes the KZRider "relays frying" thread. The unit that failed was
rated 42 W — nowhere near its limit on a load like this. What killed it was a
**dead short in the rear light assembly**, and the poster's cheap relay worked
fine once the wiring was corrected. A short kills whatever is fitted.

So the real selection criteria are:

1. **Load independence** — mandatory, or LED signals flash fast or not at all
2. **Adjustable rate** — useful if any incandescent survives the conversion
3. **Sealing and build** — this lives on a motorcycle, and it is the one place
   where $20 buys something $5 does not

### Recommended: SHIN YO 3-pin universal (Highsider 208-070)

About **$20**. Load 5 mA to 15 A, 0.06 W to 180 W, adjustable flash rate,
includes a universal harness, and has a hazard-flash function. Recommended on
KZRider for this family of bikes.

⚠️ **US stock is thin** — out of stock at both RevZilla and J&P Cycles as of
18 Aug 2026. Available from EU sellers (cafe4racer, Tonnycat).

### US-orderable alternative, researched 19 Aug 2026: Custom LED ELFR-1

**$22.49**, in stock, engineered and assembled in New Jersey, 1-year warranty
and an explicit money-back guarantee to run any 2-wire application at DOT
rate. Load **0.05–10 A (0.6–120 W)** — the only candidate whose published spec
matches the issue #11 requirement verbatim. Silent solid-state, near-zero
turn-on delay, holds a constant rate on LED now and incandescent on revert.

It is a **2-wire relay** (red = +12 V switched, black = load, explicitly
polarized) that plugs into 2- or 3-wire OEM connectors — a 3rd ground pin is
simply left unused, because **the relay needs no ground**. The flasher ground
wire still goes in the rebuild loom (it costs one wire and keeps 3-pin parts
on the table forever), but this pick does not depend on it. The ELFR-1-QD
variant ($24.99) has 1/4" quick-disconnect spades, better suited to a
hand-built harness than the OEM-connector version.

If the Shin Yo cannot be had from a US seller when ordering time comes, this
is the pick: comparable spec, better availability, actual warranty and a
company that answers email. Order whichever of the two is in stock.

### Backup: Novita EP35 — the walk-in option

~**$12–18** at AutoZone / Advance Auto, same-day anywhere in the US. 3-terminal
ISO (31 = ground, 49 = B+, 49a = load), 1/4" spades, rated 1–4 lamps up to
162 W / 13.5 A, and Novita's own sheet says **LED, incandescent, or mixed**.
It is also the unit the KZ community has actually bench-tested on this bike
family (KZRider) and found sensitive to very light loads. Costs: it needs the
dedicated ground (which the rebuild runs anyway), and it clicks — relay-style
output. Near-zero-risk fallback if the ELFR-1 disappoints. An earlier draft of
this section dismissed the EP34/35 off Tridon's Australian catalogue sheet;
Novita's US sheet and the KZRider testing supersede that read.

Also surveyed and passed over:

- **SuperBrightLEDs LF1-S-FLAT** — $9.99, 0.05–10 A, 12 V. Right spec on
  paper, but the listed lifespan is **400 working hours**, which is a
  consumable, not a component.
- **Kellermann R2** — the premium answer (~$35–50, 0.5–85 W, load-independent,
  replaces 2- and 3-pole relays, tiny). Beautiful part; EU-distributed with
  thin US stock, and nothing on this bike justifies doubling the spend over
  the ELFR-1.
- **TST Industries Gen 2** — 2-pin, adjustable rate, $21.99, well-regarded
  sportbike vendor. Current range and minimum load unpublished, no polarity
  documentation, modern-bike fitment chart. Weaker paper than the ELFR-1 at
  the same price.
- **Kuryakyn 2994** — 2-pin spades, solid-state, max 200 W claimed. Good
  cruiser-community track record, weakest documentation of the name brands.
- **CF18** — 8-pin automotive (Toyota/Lexus) form factor. Wrong socket.

⚠️ **Reverse-polarity protection is published by NONE of these vendors** —
including the recommended ones. Treat every candidate as unprotected: add an
install-time step to verify B+/load orientation with a meter before first
power-up. The KZ 2-pin socket makes swapped insertion physically possible on
spade-style units. Custom LED is the vendor most likely to answer the
protection question by phone or email before purchase.

### Fallback: generic 3-pin electronic flasher (CF14 / JL-02 style)

$5–10 and always available. Electrically workable for this bike given the
load numbers above, but demoted below the EP35 for a documented failure mode:
**CF13 and CF14 have mirrored B/E pinouts and look identical**, and reversed
B/E kills the unit — the exact opposite of polarity protection. Budget units
also derate sharply after ~10 s and run a fixed 88 cpm, on the fast side. At
$15 for the EP35 there is no reason to be here.

### Not recommended: motogadget mo.flash

Previously the recommendation here, on the strength of being 2-wire and needing
no ground. **Withdrawn for two independent reasons:** it is **$46**, and it is
**discontinued** — sold out at Revival Cycles and marked by RevZilla as not
returning. Availability alone rules it out regardless of the price.

### Run the flasher ground wire regardless

Free at build time, impossible later without opening the loom, and both
recommended options need it.

---

## Regulator / rectifier (#12)

### CORRECTION, 18 Aug 2026 — the series option was never actually closed

Everything in this project up to now has said that series regulators are
three-phase only and therefore do not fit this bike. **That was wrong**, and it
was wrong in the direction that cost the most: it ruled out the one part that
solves the LED heat problem properly.

**A single-phase stator connects to ANY TWO of a three-phase regulator's three
AC inputs.** This is standard practice on single-phase classics — Nortons in
particular, where it is the routine SH775 fitment — with long-term field
reports, and manufacturers reportedly accept the configuration. One rider
reports fifteen years on it, noting the spare input leg is effectively a
built-in redundancy.

The three-phase parts are still three-phase parts. What was wrong was the
inference that a single-phase stator cannot drive one.

### SUPERSEDED, 19 Aug 2026 — SH775 ordered

**IN HAND, 29 Aug 2026 — the Polaris ORV takeoff SH775 has arrived and is
ready to fit.** The regulator decision is closed; what remains is the bench test
before build and the connector question immediately below.

> **Open, and cheap to close:** does this takeoff include its mating pigtails?
> Salvage units are often cut with a tail of harness still attached. If it does,
> "still to order: the two mating pigtails" below is already satisfied and the
> Eastern Beaver order shrinks to crimps and DC wire. Check before ordering.

**A used takeoff SH775 was found on eBay for $45 and ordered.** That is the
"used / salvage from a wrecked Polaris" row in the source table below, at the
bottom of its range — below the Podtronics price. The decision block that
follows is kept for the reasoning, but its premise (SH775 costs $179–285) no
longer holds, and the same override written for the OEM discount route applies:

- Fit the SH775 from the start; the Podtronics is not bought at all
- Two of the three AC inputs take the stator pair; the third stays unterminated
- Temperature measurement becomes validation rather than a decision gate
- Run the DC pair heavy gauge and direct to the battery, fused at the battery
  end — **open check**: the rebuild model currently routes DC+ to the PDM main
  stud; reconcile before cutting wire
- **Bench-test the used unit before build** — unknown history, but a regulator
  either works or does not, and it is testable (each AC leg to ground reads
  infinity; verify 14.0–14.5 V behavior on the bike)

### Right-bar 4P — a connector the rebuild must reproduce (29 Aug 2026)

Most stock connectors are archival: the fuse box, the R/R and their housings are
all replaced by new parts with their own terminations. **The right-bar 4P is
not.** The rebuild retains the right-bar switchgear, so the new harness has to
mate that pigtail.

- It is the **smaller** of the two four-way rectangular series in this harness —
  **not** the same part as the R/R's 4P (`B04.3`).
- The harness half carries **male spades**; `B06.5` at the fuse box is the same
  series in the opposite gender, and is the sample to measure without
  disturbing the switchgear.
- **Nothing has been measured on it** — no terminal width, no depth, no series
  identification. Do that before ordering, and do not borrow `B04.3`'s 5.96 mm
  blade or 24.5 mm depth; they are a different part.
- Housing marks: a `4` and a small flower logo. A part-identification lead only.

**The left-bar 6P (`B02.3`) is the same series in a 6-way size**, confirmed
29 Aug 2026, and it is reproduced too. So the rebuild needs, from one family:

| | Way count | Harness-side terminals |
|---|---|---|
| `B01.2` right bar | 4 | male spades |
| `B02.3` left bar | **5 of 6 used** — do not buy a 6-way for it | male spades |
| `B06.5` fuse box | 4 | female — **not** reproduced, but it is the measurable sample |

That is three members of one series across the harness, in both genders, which
makes identifying it worth real effort rather than a nicety. **No dimension has
been measured on any of them.**

The instrument 6P (`B00.1`) has not been examined as a part yet.

**Still to order: the two mating pigtails** — 3-pin AC + 2-pin DC, Shindengen
spec, covered under "Connectors" below. Eastern Beaver preferred for correct
terminal crimps and DC-side wire gauge.

### DECISION (superseded 19 Aug 2026, see above) — fit a shunt unit now, measure, upgrade only if the number says so

**Fit a Podtronics single-phase ($75), mount it in real airflow, and measure the
body temperature.** Buy the SH775 only if the measurement says to.

The reasoning is that the heat problem, while real, has **never been quantified
on this bike**. What is known: a shunt regulator makes the stator the load, and
cutting draw with LEDs increases the surplus it must burn. What is not known:
by how much, on a stator whose rated output has never been read off anything.
Spending $180–285 to pre-empt an unmeasured problem is the wrong order of
operations when the instrument to measure it is already on the bench.

**The instrument exists.** The Fluke 87V does type-K thermocouple temperature;
it needs an 80BK-A probe (already on the shopping list under the dynamic tests).
So this is a measurement, not a guess.

**Decision rule:** record the regulator body temperature at 3,000–5,000 rpm in
still air. Compare it against that unit's own rating rather than an absolute
number. Sustained operation near the rating is the trigger to upgrade; a
comfortable margin means the $75 part was the right answer and $200 was saved.

### Upgrade path — Shindengen SH775

Polaris part **4012941**, catalogued by Polaris itself as *"REGULATOR 3PH 35A
**SERIES** 105C"* — which confirms the series type and the 105 degC rating from
the manufacturer rather than a forum.

**ORDERED 19 Aug 2026 — used takeoff, eBay, $45** (the used/salvage row below).
The "priced out at $179–285" framing that follows is retained for the record:
the $95 Roadstercycle deal that recurs in forum posts is historical; they no
longer list it. At new-part prices this was the part to move to only if the
temperature measurement called for it; at $45 it goes in from the start.

| Source | Price | |
|---|---|---|
| OEM dealer (Partzilla etc.) | $179–285 | Genuine, warranted |
| Used / salvage from a wrecked Polaris | $40–80 | Genuine part, unknown history — but a regulator either works or does not, and it is testable |
| Aftermarket "SH775" clones | $26–65 | Unverifiable |

⚠️ On the clones — the counterfeit warning in the Norton forums is specifically
about fakes sold **as genuine at genuine prices**. A $30 unit openly listed as
aftermarket is not pretending to be anything. That does not make it good; it
means the fraud risk and the quality risk are separate questions, and only the
second one applies. Nobody has published a teardown either way.

### Open — OEM discount route, asked 18 Aug 2026 (now moot for the first unit)

**Update 19 Aug 2026:** the used $45 unit is ordered, so this route no longer
gates anything. If it lands anyway, it becomes the cheap way to a **spare** —
worth having on a part this counterfeited (see below on a second regulator).

Dealer pricing on the genuine part has been asked after through a Polaris
contact. **Assume it is not available and build to the decision above**; if it
does come through, it overrides that decision outright — a genuine SH775 at
discount beats a $75 shunt, and the series design cures the heat problem rather
than mitigating it. Update this file if it lands.

**Ask for: 4012941** — "REGULATOR, 3PH, 35A, SERIES, 105C". Check whether it
has superseded; **710001103** appears as an alternate OEM number.

If the discount is deep, a second regulator is cheap insurance on a part that
is otherwise $179–285 and increasingly counterfeited.

#### Connectors — correction, they are not scarce

An earlier version of this file said the mating connector was unobtainable
outside a dealer parts system. **That was wrong**, and the reasoning behind it
was wrong too.

The connector is not Polaris's choice. It comes on the regulator, so it is
**Shindengen's** spec — which is why reasoning from how Polaris builds harnesses
points at the wrong vendor, however sound that reasoning is about Polaris.

The SH775 uses **two** connectors:

| Side | Pins | Carries |
|---|---|---|
| AC | 3 | the three stator phases — **this bike uses any two** |
| DC | 2 | battery positive (fused) and ground |

Mating pigtails are sold openly as "3-way connector for Shindengen MOSFET type
SH775" and fit the whole FH009/FH010/FH011/FH012/FH020 family as well —
**$16–22** on Amazon, eBay and Walmart. Eastern Beaver also supplies Shindengen
R/R connectors and is the better source if correct terminal crimps and wire
gauge matter, which on the DC side they do.

So the connector is a $20 catalogue item, not a scarcity problem. Getting an OEM
sealed pigtail through the discount is still nice — correct seals and gauge for
little money — but it is convenience, not necessity.

**If it lands, what changes:**

- Fit the SH775 from the start; the Podtronics is not bought at all
- Two of the three AC inputs take the stator pair — already the plan
- Temperature measurement becomes validation rather than a decision gate
- Run the DC pair **heavy gauge and direct to the battery, fused at the
  battery end**; series regulators are sensitive to resistance in that path

### Design the harness so the upgrade stays cheap

This is the part that matters at build time, and it costs nothing:

- Give the R/R its **own serviceable connector**, sized for the higher current,
  rather than splicing it into the loom.
- Bring **both stator leads and the DC pair to that connector** so swapping to a
  three-AC-input unit means a new pigtail, not opening the harness.
- Leave physical room and a mounting point for a unit the size of an SH775,
  which is larger than a Podtronics.
- Mount wherever the airflow actually is — that decision is worth more than the
  choice between the two parts.

Done that way, the upgrade later is a twenty-minute job, and the measurement
decides it rather than a forum consensus.

⚠️ **The one option that costs nothing at all** is worth naming even though it
is already decided against: a halogen headlight restores the load the regulator
wants to see and makes the whole problem disappear. FULL LED is a deliberate
choice, and this is its actual price. Noting it for completeness, not to
reopen it.

### Why single-phase options are so thin

The market answer is unsatisfying but real: single-phase means old and small.
Modern bikes need 350–600 W and are three-phase throughout, so that is where
the development money goes. Even the largest single-phase market — Harley —
is served by three-phase *conversion* kits; Compu-Fire's own 55402 series
regulator is a 40 A three-phase unit for their three-phase upgrade, not a
single-phase part.

Which is precisely why the two-of-three-inputs trick matters: it is how a
single-phase bike reaches the modern parts bin without changing anything
mechanical.

### Converting to three-phase — considered and NOT recommended

Three-phase is what the modern R/R market serves, so the question is fair:
what would it take to join it?

**Decided: NOT doing this, 18 Aug 2026.** The correction above removes the only
genuine argument for it — a series regulator no longer requires converting.

**It takes a new stator and a new rotor.** A three-phase R/R needs a
three-phase stator, and the rotor's magnet arrangement has to suit the winding.
This is not a wiring change — it is engine work.

✅ **Rotor confirmed permanent-magnet**, hands-on 18 Aug 2026. No field coil,
no brushes.

#### Path 1 — donor from the same engine family (the only realistic bolt-in)

The later **EX305 / GPZ305 (1983-88) is three-phase.** Its regulator carries
three yellow leads (Electrex RR20), and its stator is Kawasaki 21003-1073. Same
305 twin family, one generation later.

🛑 **Whether that stator and rotor physically fit the KZ305-B1 cases and crank
is UNVERIFIED, and it is the entire question.** Settle it with a parts-catalogue
cross-reference of stator, rotor and cover part numbers before spending
anything. Note also that Electrex flags the Z305 LTD as possibly needing a
*different* regulator (RR26) — so this family spans both architectures, which
is exactly why part numbers must be checked rather than assumed.

#### Path 2 — custom rewind

Possible only if the stator's slot count divides evenly by three with groups
120 degrees apart. Frequently it does not, and the answer from rewinders in
that case is a flat "can't be done with that stator". Requires counting the
actual slots and poles on this stator, and the rotor still has to suit.
$200-400 before the regulator.

#### Why not to do it

**Three-phase is common because modern bikes need 350-600 W.** This one, after
the LED conversion, needs perhaps 60-100 W. Three-phase solves a problem this
bike does not have.

| | Single-phase | Three-phase conversion |
|---|---|---|
| Regulator | $75 Podtronics | $165 MOSFET / SH775-class |
| Stator + rotor | already fitted | $300-500, fitment unproven |
| Risk | none, proven parts | you are the test case, on the charging system |

**The argument that used to carry it has evaporated.** The case for converting
was that a series regulator cures the LED heat problem and series units are
three-phase. The first half is still true; the second half was the error
corrected above. An SH775 on two of three inputs delivers the series benefit
for about $165 and no engine work at all.

Nothing else about conversion pays: more output this bike will never use, at
several hundred dollars and an unproven fitment.

### Before ordering

- **Confirm the stator's rated output in watts.** The 180 W universal units are
  assumed comfortably above this bike's load, but the figure has not been read
  off anything — only the 0.4 Ω and 75 V AC test values are confirmed.
- ~~Confirm where the DC output lands.~~ **CLOSED.** It is W/R onto the main
  power net at B04.6, established by elimination [arith 29 Aug 2026] — the
  harness holds exactly two W/R terminals and a male bullet can only mate the
  female. See `models/factory/charging.yml`. ⚠️ It reopens if an untagged W/R
  female bullet is ever found.

### Fitting rules, whichever unit is chosen

- Target **14.0–14.5 V at 3,000–5,000 rpm**, and check body temperature.
- **Never** disconnect the regulator with the ignition on.
- **Never** disconnect the battery while running.
- Each yellow lead must read infinity to ground.

---

## PDM — Metri-Pack 280 array, or MTA modular (1 Sep 2026)

Direction under consideration: rather than buying a sealed RTMR-style module,
build the fuse/relay block from **Metri-Pack 280** terminals — the MP280 inline
fuse holder scaled up to an array — or assemble it from the **MTA modular**
family. Both are live; they are compared at the foot of this section.

> **Correction, same day.** This section first evaluated **Metri-Pack 630** and
> was wrong about the series. The reasoning it rested on — that an ATO fuse
> blade, an ISO mini relay pin and a 630 male are all the same 6.3 mm blade — is
> true, but 630 is a 12–10 AWG terminal and this harness runs its branches on
> 16–18 AWG. **280 is the right family**, and the rest of this section is
> rewritten to it. The 630 note is not worth preserving; what survives from it
> is the busbar argument, which applies to any DIY array and is kept below.

### What 280 actually mates

| | |
|---|---|
| Blade | **2.8 mm** |
| Wire range | **22–14 AWG** — the range this harness uses |
| Inline rating | up to **30 A**, intermittently 35 A |
| Fuse it takes | **MINI / ATM / APM** — *not* the larger ATO |
| Relay it takes | **ISO 280 "micro"** relays, also 2.8 mm |

**The fuse-and-relay-on-one-terminal idea survives the correction**, just on
different parts. Mini blade fuses and ISO 280 micro relays both present 2.8 mm
blades, so a 280 receptacle takes either, and a position's role is still decided
by what gets pushed into it. ISO 280 micro relays are commonly **20 A** with
**35 A** versions available — against a worst case of ~6.6 A at `K_MAIN`, every
position in this design is comfortably inside a 20 A part.

**And the gauge problem disappears.** 22–14 AWG is exactly where this harness
lives, so the terminals crimp properly onto real branch wire. That was the
objection that killed 630, and it was the whole objection.

### Still true: bus the feed side, don't build it from crimps

The one thing a bought block gives you that an array of discrete terminals does
not is **a stamped internal busbar**. Without it every fuse input needs its own
wire back to a common point — N crimps and N joints on the main power path.

**That is the `B06.4` failure mechanism rebuilt on purpose.** The old harness
melted at a bullet where a gauge step met the 20 A MAIN circuit, and it is filed
as a *design* finding precisely because a new build reproduces it if it
reproduces the topology.

⚠️ **This applies to MTA too, and it is the thing to check on the datasheet.**
MTA's own literature notes that most modules have **no common power — each
terminal is wired separately for maximum flexibility.** That flexibility is
exactly the busbar problem in a different package. Bussed modules do exist;
choosing them is the difference between a distribution block and a tidy row of
individual crimps.

So whichever route: **solid bus on the input side.** Which suits the hybrid
split decided the same day, because it needs **two** buses anyway:

| Bus | Fed from | Serves |
|---|---|---|
| HOT | main stud | F1 ign sw feed, F4 horn pwr, F5 headlamp pwr |
| SWITCHED | `K_MAIN` output | F2 kill feed, F3 coil pwr |

### Sealing

Sealed MP280 terminals and housings are standard and Eastern Beaver sells
weatherproof MP280 fuse holders off the shelf, so unlike 630 there is no
tension here between sealing and gauge — sealed 280 already covers 22–14 AWG.
Sealing at the **enclosure** (gasketed lid, sealed entry) is still worth
preferring for a multi-position block: it is how production fuse boxes are
built, and it keeps fuses serviceable.

### The three routes, honestly

| | What it is | Against it |
|---|---|---|
| **DIY MP280 array** | Terminals in a housing you lay out | You fabricate the bus, the retention and the enclosure. Most work, most control. |
| **MTA modular** | Purpose-built modules that combine into one covered unit via frames and brackets — mini/maxi fuses, micro/mini/high-power relays, mixed in one module | Check bussing per module; most are individually wired. Way count set by which modules exist. |
| **Ready-made sealed panel** | Sealed MINI/MICRO fuse & relay panels on MP280, already bussed, sold as one part | Least control over way count — the constraint that pushed this project toward custom in the first place. |

**MTA is the strongest fit for the stated goal.** The reason to go custom here
was never fabrication for its own sake — it was that five relay positions is the
top of what RTMR-style units are scoped for, and the star-ground count is still
unknown and still growing. A system explicitly designed so modules can be added
or removed as a design changes answers that directly, without making the busbar,
the enclosure and the retention into three separate problems to solve.

### Candidate part: MTA 0301370 (looked at 1 Sep 2026)

A sealed MTA module, **60 sealed 2.8 mm cavities on the 280 footprint**, which
the maker states as *"30 MiniVal fuses or 10 Micro 280 relays or mixed relays
and MiniVal fuses."*

**This confirms the mix-and-match property from the manufacturer rather than by
inference** — the same cavity takes a fuse or a relay, and the population is
chosen at build time. It is the exact property this section was reaching for.

#### It is three part numbers, not one

| | |
|---|---|
| `0301370` | module / footprint |
| `0301371` | cover |
| `0301372` | secondary lock |

**Envelope: 107.6 x 72 x 60 mm** with the lid on, from the manufacturer's
dimensioned drawing (`parts/mta-0301370-dimensions.png`). The module in hand
measured 108 x 71 x 60 on 9 Sep, which agrees. That is the box the enclosure and
mounting have to swallow. ⚠️ It is the **whole** module dimension — the terminal
and its seal sit *inside* that 60 mm, not below it.

#### Capacity against this design

⚠️ **Superseded by the measured map** — kept because the conclusion held. The
1 Sep arithmetic assumed a relay occupies roughly three fuse positions (30 ÷ 10):

| | Count | Cavities |
|---|---|---|
| Relays — `K_MAIN` `K_COIL` `K_HORN` `K_HI` `K_LO` | 5 | ~30 |
| Fuses — F1–F6 | 6 | 12 |
| **Used** | | **~42 of 60** |

Both inputs turned out wrong and the error cancelled: a 4-way relay takes **4**
cavities rather than ~6 `[bench 10 Sep]`, and the design grew to **11 fuses**
rather than 6. The real figure is **42 of 60** — the same number by a different
route. See `docs/pdm-cavity-map.md` for the authoritative counts.

Roughly **30% spare**, which is the right shape for this project: the circuit
count is still growing as the undrawn branches land, and that headroom is the
whole reason for going modular rather than buying a fixed RTMR unit.

#### ⚠️ Two things to confirm before ordering

- **Cavity plugs for the ~18 unused ways.** A sealed connector is only sealed if
  every cavity is filled. Unused ways need blanking plugs or the module's rating
  is void — and on a bike that died of water in the sleeve, that is the failure
  mode, not a technicality. Confirm the plug part number is available and order
  them with the module.
- **Seal-to-gauge range.** Sealed MP280 uses a cable seal sized to the wire.
  Confirm the seals cover **16–18 AWG**, which is what these branches are, and
  that the right seal is ordered per gauge rather than one size for everything.

#### Revising the busbar concern — it is smaller than stated above

60 individually sealed cavities means **no internal bus**: every terminal is its
own crimped wire. That is what the general warning above is about, and it is
true of this part.

**But the count that matters is the number of junctions, not the number of
crimps**, and for this design it is **two**:

| Junction | Feeds |
|---|---|
| HOT | F1 in, F4 in, F5 in, `K_MAIN` 30 |
| SWITCHED | F2 in, F3 in, `K_HORN` 86, dimmer common |

Two four-way junctions, not one per fuse. That is a small, ordinary thing to
solve — a pair of short busbars or stud blocks outside the module, or a bussed
MTA power-input module alongside this one. **It does not argue against the
part.** The earlier warning was written against a DIY array where the feed
genuinely does fan out per position; applied here it overstates the problem, and
the two-bus arrangement the hybrid split already calls for absorbs it.

### Are any MTA modules bussed? Read off the catalogue, 1 Sep 2026

Catalogue filed at `parts/MTA_Power_modular_solutions_2019_v1.1.pdf`.

**Yes — and the bussed module is the wrong one for this bike.** Three findings,
and they compound.

#### 1. `0301697` is genuinely bussed, and the schematic says exactly how

One `+` input feeds a single common bus. Thirteen fuse positions hang off it —
5 MaxiCompact above, 5 MiniVal below, 3 M8Compact to the right — each with its
own output. That is a real single-input bussed fuse block, not a row of
independent holders.

#### 2. But it holds no relays, and it is not waterproof

`0301697` is 5 MiniVal + 5 MaxiCompact + 3 M8Compact. **All fuses.** There is no
relay position in it, so it cannot be the block — at best it could be a fuse
section alongside one.

And it sits on the catalogue's **MODULES** pages, not the **WATERPROOF MODULES**
pages. The waterproof range is `0301370`, `0301491`, `0301568`, `0301569` — plus
`0301373` and `0301374`, which the catalogue describes as *"same module with
integrated mounting brackets"*, i.e. bracket variants of the two they follow,
**not bussed versions**. None of the waterproof modules shows a bus.

#### 3. ⚠️ And it is ONE bus, which this design cannot use

The schematic shows a single `+` common to all thirteen positions. **The hybrid
split needs two independent buses** — HOT for F1/F4/F5, SWITCHED for F2/F3 — and
a single-bus module cannot provide them. Two modules would, at 13 positions each
where this design needs 3 and 2.

So bussing exists in the MTA range, but every place it appears it is attached to
something this bike does not want: fuses without relays, no sealing, and one
common feed where the architecture requires two.

#### What that settles

**`0301370` remains the pick**, and the two feed buses get made outside it. That
is the conclusion the previous section already reached on the junction count —
two four-way junctions, not one per fuse — and the catalogue does not offer a
better answer.

**Worth considering: the buses may already exist as parts this build needs.**
The HOT junction is electrically the main fuse's output; the SWITCHED junction
is `K_MAIN`'s pin 87. If `MF` is mounted in a holder with a stud output, that
stud *is* the HOT bus, and a small stud block off `K_MAIN` 87 is the switched
one. Neither is a new part so much as a terminal already in the circuit doing a
second job — which keeps the joint count down, and joint count on the main power
path is the whole `B06.4` lesson.

Elsewhere in the catalogue, bussing appears on the **MidiVal / MegaVal** side —
the clip-together multiple fuse block, and the configurable C-MEC/PDU units with
*"bussed MidiVal and MegaVal fuses"*. Those are high-current parts, relevant to
`MF` and `MF_RR` if a holder is wanted for them, not to the branch circuits.

### DECIDED 1 Sep 2026 — point-to-point the buses at assembly

Accepted: the two feed junctions get wired by hand rather than bought as a
busbar. That closes the bussing question and **settles `0301370` as the module**,
since bussing was the only argument standing against it.

Three rules make it safe, and the first is not obvious.

#### 1. Star it outside the module — do not daisy-chain the cavities

The tempting shape is a jumper from one fuse's input cavity to the next. **It
does not work in a sealed module.** A daisy chain needs two wires at the first
cavity — the feed in and the jumper out — and a sealed MP280 cavity takes **one
cable seal on one wire**. Double-crimping into it defeats the sealing that is the
entire reason for choosing a waterproof module.

So: **one wire per cavity, always**, and the junction happens outside the module
at a single star point per bus. Feed wires run from that point into their
cavities individually.

Ampacity is not the constraint either way — MP280 is a 30 A terminal and the
whole switched side is under 10 A — so this is about the seal, not the current.

#### 2. Keep HOT and SWITCHED physically apart in the layout

Put all HOT-fed positions at one end of the module and all SWITCHED-fed
positions at the other. **Do not interleave them.**

The reason is the `K_COIL` safety property. If a feed wire is ever landed in the
wrong cavity, an interleaved layout makes that a plausible slip — and bridging
SWITCHED to HOT puts F3 on permanent power, which is the exact failure the
hybrid split exists to prevent: a welded `K_COIL` would then leave the engine
running with the key out and the kill switch powerless. Physical separation
makes the mistake hard to make and easy to see.

#### 3. Record the cavity map before populating

`0301370` has 60 cavities and no printed circuit names. Which cavity is which is
knowledge that exists only in whoever wired it, and this project already has a
file's worth of evidence about what that costs — the stock harness had to have
its connectors renumbered to physical cavities twice after being read off a
diagram.

Write the map down as it is built, in the same form as
`measurements/connector-inventory.csv`: cavity number, circuit, wire colour,
gauge. State the numbering rule first, before the first terminal goes in.

### MTA associated components — part numbers and design quantities

Part numbers from the MTA connection-system datasheet, **corroborated against
distributor listings 3 Sep 2026** — the catalogue filed at
`parts/MTA_Power_modular_solutions_2019_v1.1.pdf` is a 13-page marketing
overview and carries **module part numbers only**, so none of the accessories
below appear in it.

⚠️ **`0300690` and `0300691` are listed with opposite genders by different
distributors.** You need two of each, so order both part numbers at qty 2 and
the disagreement is harmless — do not order four of one.

| Part | MTA PN | Qty | |
|---|---|---|---|
| Module, 60 cavity waterproof | `0301370` | 1 | |
| Top cover | `0301371` | 1 | |
| Secondary lock | `0301372` | **6** | ⚠️ six per module, not one |
| Mounting leg | `0300690` | 2 | gender disputed — see above |
| Mounting leg | `0300691` | 2 | |
| Terminal, 18–16 AWG | `1708338-L` | 40 | 16x 18 AWG + 24x 16 AWG |
| Terminal, 14–12 AWG | `1708339-L` | 2 | ⚠️ was missing entirely until 3 Sep |
| Wire seal, red | `4550748` | 16 | 18 AWG |
| Wire seal, green | `4550747` | 26 | 16 AWG and 14 AWG |
| Cavity plug | `4550750` | 18 | 60 less 42 populated |

#### Where the quantities come from — derived, 3 Sep 2026

**One terminal and one seal per wire.** A relay pin is a cavity that a terminated
wire enters from below, exactly like a fuse leg, so relay positions cost
terminals — they are not free because the relay plugs in from the top.

##### The drawing converges on the part

Two independent derivations now agree to the wire:

    walking the connection sets   ->  42 wire-ends enter the module
    11 fuses x 2 + 5 relays x 4   ->  42 cavities exist to receive them

and **no cavity carries more than one wire**, which a sealed cavity requires —
it takes one seal on one wire. That equality is the check on both numbers. If a
later edit breaks it, one of them is wrong.

They did not agree before `SP_HOT` and `SP_SW` were drawn (#50): the nine
fuse-input wires existed nowhere, standing in as four abstract "bus ways", and
two cavities carried two wires each.

Gauge split of the 42: **18 AWG x16, 16 AWG x24, 14 AWG x2.**

Only **two** 14 AWG legs still enter the block — `K_MAIN`'s 30 and 87.
`W_MAIN_OUT` now terminates outside it, on `SP_HOT`.

##### ⚠️ These are DESIGN quantities, not order quantities

Order over. Crimps get wasted, and if the 16 AWG spool misses green's 2.2 mm
bound those circuits move to 14 AWG, which needs `1708339-L` instead. Green seals
survive that; the terminal does not — so hedge on terminals, the cheapest line in
the order.

✅ **The hedge was not needed.** 16 AWG TXL measured **2.20–2.21 mm** on 10 Sep
against a 2.26 nominal — on the bound rather than 0.06 above it — but **a green
seal test-fitted on that wire is very snug**, so the gauge stays 16 AWG. The 30
`1708339-L` remain the funded fallback. See *Wire seals*.

| Part | Design | Suggested order |
|---|---|---|
| `1708338-L` | 40 | 100 |
| `1708339-L` | 2 | 30 |
| `1708337-L` | 0 | 10 — insurance for the 18 AWG band gap below |
| `4550747` green | 26 | 60 |
| `4550748` red | 16 | 40 |
| `4550750` plug | 18 | 40 |

Everything still sits inside the ordered quantities — the design has moved four
times since the order was placed and has not once threatened a line.

An unplugged cavity means the module is not sealed, which is the entire reason
this part was chosen.

#### Supplier — checked 3 Sep 2026

**ConnectorID (connectorid.com) is an authorised MTA distributor and carries
every line**, so the block can be a single order.

| Part | Stock / price seen | |
|---|---|---|
| `0301370` module | listed | |
| `0301371` cover | listed | |
| `0301372` secondary lock | $0.52, MOQ 1 | listing independently states **"6 pcs required per module"** |
| `0300690` | 732 in stock, $1.14 | |
| `0300691` | 629 in stock, $1.14 | |
| `1708338-L` | loose piece, MOQ 1 | |
| `1708339-L` | listed | |
| `4550748` red seal | $0.45 | |
| `4550750` cavity plug | listed | |
| `4550747` green seal | ⚠️ **has a product page but did not appear on the wire-seals collection listing — confirm stock before ordering** | this is the largest seal line |

##### Order placed 3 Sep 2026, shipped complete 4 Sep — ConnectorID

**All eleven lines in one box, red seals included.** The listing read *"in stock"*
and *"0 available"* simultaneously and the cart accepted it anyway; the seals
shipped. That was a display artefact, not a backorder — recorded because the
warning below was written when it looked like a real shortage.

| Part | Design | Ordered | Cover |
|---|---|---|---|
| `0301370` module | 1 | 1 | |
| `0301371` cover | 1 | 1 | |
| `0301372` secondary lock | 6 | 8 | |
| `0300690` bracket | 2 | 2 | |
| `0300691` bracket | 2 | 2 | |
| `1708338-L` terminal 18–16 | 38 | 100 | 2.6x |
| `1708339-L` terminal 14–12 | 2 | 30 | 15x |
| `1708337-L` terminal 22–20 | 0 | 10 | insurance — see below |
| `4550747` green seal | 26 | 60 | 2.3x |
| `4550748` red seal | 14 | 40 | 2.9x |
| `4550750` cavity plug | 20 | 40 | 2.0x |

The invoice labels `0300690` **male** and `0300691` **female**, agreeing with
Express Technology and against the ConnectorID page title. Two of each were
ordered, so it never had to be settled.

###### Why there are ten terminals in the box for a part the design does not use

`1708337-L` covers 0.35–0.75 mm². **18 AWG is 0.82 mm²** — above that band and
below `1708338-L`'s 1.0 mm². MTA's own AWG labelling calls `1708338-L` the 18–16
terminal, so it is the right part, but the CSA figures are evidently nominal band
edges rather than hard limits.

**Pull-test the first 18 AWG crimp** when the Prowire spool arrives. If it is
loose, these ten are the fallback and save a reorder.

###### On arrival — receiving check

**✅ Checked 10 Sep 2026, order received** `[bench]`.

- [x] ~~**`1708338-L` is loose pieces.**~~ **Confirmed** — loose bagged, not a
      reel. Applies to every new terminal in the order.
- [x] ~~**Count the secondary locks — eight**, six of which are required.~~
      **Eight received**, so two spare.
- [x] ~~**Red seals present.**~~ **Confirmed.**
- [ ] ⛔ **Two each of `0300690` and `0300691` — MIS-PICKED.** Both bags are
      **labelled correctly** but **both contain the same gender foot**, so the
      shipment is four of one and none of the other.
      **Not chased and not blocking** — the legs may not be used at all, and the
      mounting route is undecided (see *Enclosure and mounting*).
      ⚠️ **This does NOT settle the gender dispute.** The whole point of ordering
      both part numbers was that distributors list them with opposite genders;
      one bag's contents contradict its label, and **which one is wrong is not
      determinable from this shipment.** If the legs are ever used, order again
      and check contents against labels on arrival — the disagreement is still
      live, and a correct label is now known not to guarantee correct contents.

###### With the module in hand — ✅ settled 9–10 Sep 2026

**Cover, retention and mounting — checked 10 Sep 2026** `[bench]`:

- ✅ **The cover `0301371` closes over a populated block**, with both relay
  sizes. Clearance is **close on the taller 6-way** but genuinely adequate; the
  4-way has room to spare. The relay body is 23.7 mm inside a 60 mm lidded
  envelope.
- ✅ **Relay retention is terminal friction, and that is accepted.** Nothing in
  the module or the cover clamps a relay down — the pins hold it.
  **Decided: build it that way.** If vibration turns out to lift a relay, the fix
  is **a keeper added to the lid**, which is a change to one part and can be made
  after the harness is built. It does not gate anything now.
- ✅ **"Wire exit depth" was a phantom requirement — withdrawn 10 Sep 2026.** An
  earlier draft of this file claimed the enclosure had to allow an unmeasured
  depth below the mating face before the wires could turn. **It does not.** The
  wire comes out of the bottom cleanly and nothing in the module prevents it
  bending 90° immediately `[bench]`. The terminal and seal seat *within* the
  60 mm. **The envelope is complete as drawn.**

  What the enclosure actually has to allow is not a module dimension at all:

  - **Bundle cross-section.** 42 wires at 2.0–2.6 mm OD leaving one 107.6 x 72 mm
    face. Turned 90°, they fan and stack, and the bundle's thickness — not any
    per-wire depth — is what the enclosure has to clear. That number falls out of
    the routing, which depends on where the module is mounted.
  - **Strain relief at the seal.** A bend taken *at* the cavity mouth puts shear
    on the crimp and can distort the seal lip, which is the one thing keeping
    water out. This is a **clamp-the-bundle** requirement, not a clearance one —
    support the loom so the connector is not the thing holding the bend.

  ⚠️ Neither is measurable until the mounting location is chosen. **The enclosure
  is blocked on that decision, not on a measurement.**

Grid pitch and relay footprint alignment, the last piece of #10 that needed the
part rather than arithmetic, are both read off the bench:

- **Pitch 7.91 mm rows x 7.67 mm columns**, grid 6 x 10 `[bench 9 Sep]`.
- **Micro 280 relays come in two sizes — 4-way (2 x 2 of cavities) and 6-way
  (3 x 2)** — and a relay costs its own way count and nothing more. The bodies do
  **not** overhang into neighbouring cavities. Relays in hand of both sizes seat
  as the map draws them, and a module loaded solid with relays took every one
  `[bench 10 Sep]`. So #51's premise — that a 4-way relay occupies six cavities
  because the body blocks two — is retired, and with it the alignment constraint
  that came from needing six *contiguous* cavities. This design uses six 4-way
  positions.

Write the cavity map down as it is built, in the form of
`measurements/connector-inventory.csv` — cavity number, circuit, wire colour,
gauge — and state the numbering rule before the first terminal goes in.

##### `4550748` red — the stock scare, and why the analysis still stands

Red showed as unavailable at order time and shipped anyway. The reasoning below
is kept because it is about the DESIGN, not the stock level, and it decides what
to do if red is ever genuinely short. Red is the **18 AWG** seal and the design
needs 14.

**There is no substitute inside the MTA range.** The three seals are red
1.2–2.1, green 2.2–3.0, grey 3.1–3.7. 18 AWG TXL is 1.98 mm, which only red
covers — grey is nowhere near and green starts above it.

**Do not substitute a Delphi/Aptiv Metri-Pack 280 seal either.** "280" names the
2.8 mm blade, not the cavity. The seal has to seal against *MTA's* cavity wall,
and its outside profile is that manufacturer's geometry. A seal that fits the
wire and not the bore leaves the module unsealed while looking assembled.

###### ⚠️ Do NOT solve this by moving 18 AWG to 16 AWG

It is the tempting fix — green is in stock and covers 16 AWG — and it is
backwards. It would put **every wire in the block on the one seal with the
marginal fit**, and the two margins fail in opposite directions:

| Seal | Wire | Margin | Fails if the wire runs |
|---|---|---|---|
| red | 18 AWG, 1.98 mm | 0.12 mm to the **upper** bound | **fat** |
| green | 16 AWG, 2.26 mm | 0.06 mm to the **lower** bound | **thin** |

TXL is a thin-wall product, so running thin is the more plausible direction —
which is precisely what green is exposed to. Consolidating onto green doubles
down on the riskier of the two. Keep the split, and buy red from a second
supplier: TME, Express Technology or Miunske all list MTA.

Red does not gate the build start either. Seals go on before the terminal is
crimped, so the 16 and 14 AWG circuits and the whole mechanical assembly can
proceed while red is on backorder.

##### ⚠️ Order the `-L` suffix on terminals

ConnectorID lists `1708338` **twice** — once as a **reel** and once as
`1708338-L`, a **loose piece with MOQ 1**. The `-L` is the one you want. Dropping
the suffix buys a reel of thousands.

##### ⚠️ The bracket gender conflict is on ConnectorID's own site

Their URL slug for `0300690` reads `mounting-bracket-male` while the page title
reads *"Mounting Bracket Female"*. Other distributors disagree with each other
too. **Order two of each part number** and the question never has to be settled.

#### ⚠️ These are DESIGN quantities, not order quantities

Order well over. The count rises when #50 lands, crimps get wasted, and the
16 AWG seal margin is unresolved (#61).

**Green seals survive the seal question either way** — if the 16 AWG spool misses
green's 2.2 mm bound those circuits move to 14 AWG, which is also green. What
changes is the *terminal*: `1708338-L` becomes `1708339-L`. So hedge on
terminals, which are the cheapest line in the order, not on seals.

| Part | Design | Suggested order |
|---|---|---|
| `1708338-L` | 30 | 100 |
| `1708339-L` | 5 | 30 |
| `1708337-L` | 0 | 10 — insurance for the 18 AWG band gap below |
| `4550747` green | 21 | 60 |
| `4550748` red | 16 | 40 |
| `4550750` plug | 25 | 40 |

An unplugged cavity means the module is not sealed, which is the entire reason
this part was chosen.

#### Terminals — sized by conductor CSA

| MTA PN | Range | |
|---|---|---|
| `1708337-L` | 0.35–0.75 mm² (22–20 AWG) | |
| **`1708338-L`** | **1.0–2.0 mm² (18–16 AWG)** | **← this harness's branches** |
| `1708339-L` | 2.5–4.0 mm² (14–12 AWG) | if any heavy leg enters the block |

#### Wire seals — RESOLVED 1 Sep 2026 by the TXL decision

Seals are sized by **insulation OD, not gauge**, so this could not be settled
until the wire family was. **Wire decided: TXL from Prowire** — thin-wall XLPE,
125 °C, SAE J1128.

| AWG | TXL nominal OD | Seal | Margin to nearest bound |
|---|---|---|---|
| 18 | 0.078 in / **1.98 mm** | `4550748` red (1.2–2.1) | 0.12 mm |
| 16 | 0.089 in / **2.26 mm** | `4550747` green (2.2–3.0) | **0.06 mm** |
| 14 | 0.102 in / **2.59 mm** | `4550747` green | 0.39 mm |
| 12 | 0.127 in / **3.23 mm** | `4550749` grey (3.1–3.7) | 0.13 mm |

So the block needs **two seal part numbers**, red and green. Grey is not needed:
12 AWG is the charging pair and runs direct to the battery, never entering the
module.

**⚠️ 16 AWG clears green's lower bound by 0.06 mm** on the published nominal.
That is inside ordinary manufacturing tolerance on an extruded wall, so the table
above was always a prediction rather than a measurement.

##### ✅ CLOSED 10 Sep 2026 — the seal is snug on the wire `[bench]`

**A green seal was test-fitted on this exact 16 AWG TXL and is very snug.**
That closes it. The seal has real radial interference on the wire, which is the
property that matters and the one the caliper number was only a proxy for.

Kept for the record, because the numbers are useful if the wire family ever
changes:

Prowire 16 AWG TXL, calipered at four points: **2.20, 2.21, 2.21, 2.20 mm.**

| | OD | Margin to green's 2.2 mm bound |
|---|---|---|
| Published nominal | 2.26 mm | 0.06 mm |
| **Measured** | **2.20–2.21 mm** | **0.00–0.01 mm** |

So the wire runs at the bottom of tolerance rather than at nominal, and sits on
green's stated bound. **The fit test says that does not matter** — 2.2 is a
working limit, not a failure point, and the seal grips there as designed.

⚠️ **Basis, stated precisely:** both the caliper reading and the fit test were on
a **previous batch of the same part number**, not on the spool the harness will
be built from. Judged sufficient. If a future spool ever feels loose in a green
seal, this is the paragraph to come back to — and the fallback below is the
answer, already funded.

##### The 16 → 14 AWG fallback — not needed, kept because it is paid for

If a future spool ever misses the bound, the 24 sixteen-gauge circuits move to
**14 AWG** at 2.59 mm — **0.39 mm inside green**, mid-band. This was anticipated
at order time:

| | Design | Ordered | Needed if all 24 move |
|---|---|---|---|
| `4550747` green seal | 26 | 60 | 26 — **unchanged**, green covers both |
| `1708339-L` terminal (14–12) | 2 | **30** | 26 — **fits, 4 spare** |

**The terminals were deliberately over-ordered 15× against design for exactly
this.** Green seals survive the change; the terminal does not, and that was the
line hedged. What is *not* covered is the wire itself — a new Prowire order in
the affected colours, and 14 AWG is stiffer in a block where every wire turns
through 90° under the mating face.

⚠️ 14 AWG has its own band-edge story: at 2.08 mm² it falls between
`1708338-L`'s 1.0–2.0 and `1708339-L`'s 2.5–4.0, the same gap 18 AWG sits in.
MTA's own AWG labelling calls `1708339-L` the 14–12 terminal and the two existing
14 AWG legs already use it, so this is settled by precedent rather than by CSA.

#### ⚠️ 6 AWG is not TXL and cannot be

TXL covers roughly **24 down to 8 AWG**. The three heavy cables — `W_BAT_SOL`
(battery to starter relay), `W_SOL_SM` (relay to motor) and `W_BAT_GND` — are
**6 AWG**, outside the range. They are battery/starter cable: a different
product, different insulation, much larger OD.

**Not specified yet**, and none of the decisions above carry over to it. None of
it enters the PDM, and all three terminate in lugs rather than 280 terminals, so
neither the seal nor the terminal choice applies. It needs its own line in the
order.

**The seal PN is coupled to the wire family, not just the gauge.** GXL or SXL in
these same gauges would push 18 AWG out of red and into green. If the wire
choice ever changes, the seals change with it — which is the kind of dependency
that is invisible at order time and expensive at build time.

#### ⚠️ 18 AWG sits in a gap between MTA's stated CSA bands

`1708337-L` covers 0.35–0.75 mm² and `1708338-L` covers 1.0–2.0 mm². **18 AWG is
0.82 mm², which is above the first and below the second.** MTA's own AWG labels
resolve it — they call `1708338-L` the *18–16 AWG* terminal — so that is the
part to use, and the CSA figures are evidently nominal band edges rather than
hard limits. Worth a **pull test on the first crimp** rather than assuming.

### 6 AWG heavy cable — settled 4 Sep 2026

`W_BAT_SOL`, `W_SOL_SM`, `W_BAT_GND` and `W_ENG_GND`. **Not TXL** — TXL runs
roughly 24 to 8 AWG and 6 is outside it. None of these enters the PDM and all
four terminate in lugs rather than 280 terminals, so none of the seal or terminal
decisions carries over.

**Buy welding or battery cable**, red and black, with tinned copper lugs and
adhesive heat-shrink boots. There is nothing to determine here: the gauge is set
by the cranking current, the lugs are set by the stud sizes, and both are
standard. Fine-strand welding cable is preferred over battery cable for
flexibility around the engine.

⚠️ **`W_ENG_GND` carries the whole cranking return** — the starter grounds through
its case into the engine, so this strap is not a signal earth. See `GND_ENG`.

### Coil suppression — settled 4 Sep, **variant revised 6 Sep 2026**

**Buy relays with integral coil suppression.** A relay coil is an inductor;
opening it produces a reverse spike of several hundred volts.

Stock had nothing to absorb it because stock had no relays and no semiconductors.
This harness adds five relays, a solid-state flasher, a series regulator and a
USB PD converter — **every one of those is a semiconductor that did not exist on
the bike before.**

Integral rather than discrete: it is a catalogue option at no meaningful cost, it
cannot be forgotten at assembly, and it cannot be wired backwards the way a loose
diode can.

#### ⚠️ Superseded: this section originally said *diode*. It is **resistor**.

The 4 Sep text specified an integral **flyback diode**, which makes 85/86
polarity mandatory — a diode-suppressed relay fitted backwards is a dead short
across the coil. When the part was identified on 6 Sep the Song Chuan 303 turned
out to offer both, and **`-R1` (1.1 kΩ resistor, 91 mA, no polarity constraint)
is the pick** over `-D1` (1N4007, anode on 85, 80 mA, polarity critical).

The reasoning is on `K_MAIN` in `models/kz305-rebuild.yml` and is a **build**
argument, not an electrical one: the design already has the polarity right, so
with six relays and a builder working from labels, a wrong-way diode relay is a
dead short while a wrong-way resistor relay simply works. The extra 11 mA buys
that. What the suppression protects survives a 40 V spike comfortably.

**86 is COIL+ and 85 is COIL− on every relay here** regardless — the design is
drawn that way and should be built that way. With `-R1` a reversal is merely
harmless rather than destructive, which is the point.

⚠️ **`-R1` became load-bearing on 10 Sep 2026.** The relay's pins read
**30/87 on one diagonal, 85/86 on the other** `[bench]`, which means the 2 x 2
footprint accepts the relay 180° round with no electrical consequence — and that
is *only* true for a resistor. A `-D1` fitted backwards is a dead short across
the coil. So this is no longer a preference between two acceptable variants:
**a diode relay in this module is a latent short.**

✅ The relays in hand, knockoffs included, are **resistor type** `[bench 10 Sep]`.
The rule stands for every relay bought after them: test the coil of any relay of
unknown provenance with a DMM both ways round — a resistor reads the same in both
directions, a diode does not.

The starter solenoid is a stock part with no integral option — fit a discrete
diode across its coil, cathode to the Y/R feed.

### USB-C PD charger — replaces the stock accessory circuit

**Decided 3 Sep 2026.** The factory accessory provision is not reproduced in any
form. What it actually was: an `R/W` feed **bolted to the battery stud**,
permanently live and unfused for two inches, running to a second fuse box — with
**both of its earth points never connected to anything** [bench 2 Sep 2026]. A
live wire with no return, provisioned and left that way for 44 years.

One circuit replaces it: **F10, switched, individually fused, with a real ground
to the star bus.**

#### Why switched rather than always-hot

⚠️ **This bike has no parasitic load at all today** — points ignition, no ECU, no
clock, no alarm. A PD charger left hot would be the first one, and a phone left
plugged in overnight will flatten a 10 Ah battery. Making it hot by default would
rebuild the exact fault this circuit exists to correct.

It is a **one-wire change at the PDM** if always-on charging is ever wanted —
move F10's input from `SP_SW` to `SP_HOT`. Worth knowing it is cheap; not worth
doing by default.

#### Selection criteria

- **12 V input, PD output.** 20–45 W is the sensible range for a bike. More
  output means more input current and a bigger fuse for no real gain.
- ⚠️ **It must tolerate the charging system, not just the battery.** Target is
  14.0–14.5 V running, and a permanent-magnet alternator with the battery
  disconnected can transient well above that. The SH775 being a **series**
  regulator helps — it open-circuits the stator rather than shunting it.
- **Sealing follows the hybrid connector policy**: sealed if it lives on the bar
  or anywhere exposed, stock-style bullets acceptable only if it sits inside the
  headlight shell or under the seat. Water in the sleeve killed the original
  harness.
- **A socket with a cap or a captive lead**, not an open receptacle. An
  unoccupied USB-C socket on a motorcycle collects water and grit.

#### ⚠️ Sizing F10 — inrush, not just running current

Input current is roughly **output watts ÷ (12 V × efficiency)**, so a 45 W unit
draws about **4.4 A** in. But a PD converter has a **capacitive input**, and a
fuse chosen on running current alone can nuisance-blow at switch-on. Size for
inrush, and prefer a slow-blow characteristic if the chosen unit specifies one.

**Its own fuse, not shared.** A USB socket is the circuit most likely to meet a
failed cable or a passenger's unknown device, and that must not take the
instruments with it.

#### Fuses — MiniVal IS the standard Mini blade fuse

**Any reputable Mini / ATM / APM blade fuse fits.** MTA's "miniVAL" is their
brand name for the industry-standard part, not a proprietary body — confirmed
3 Sep 2026 against MTA's own automotive fuse catalogue:

| | miniVAL per MTA | Standard Mini (ATM/APM) |
|---|---|---|
| Body | 16.2 x 11.1 x 4 mm | same |
| Blade width | **2.8 mm** | same — this is the "280" in the module's footprint |
| Colour code | 2A grey · 3A violet · 4A pink · 5A light brown · 7.5A brown · 10A red · 15A blue · 20A yellow · 25A white · 30A green | identical |

The colour code being standard matters at the bench: rating is readable at a
glance without pulling the fuse, on a block that will be mounted and sealed.

⚠️ **Two MTA parts to NOT buy by mistake:**

- **uniVAL** — MTA's *standard/ATO* size fuse, 19 x 20 x 4.5 mm on a 5.25 mm
  blade. Physically larger and will not seat in a 280 cavity. The names are one
  letter apart in a catalogue that lists them side by side.
- **MiniVal Low Profile** — a separate MTA line with a different body. Sold under
  a similar name by the same distributors.

So buy a **variety kit** now rather than specific values. **Ratings were
assigned 4 Sep 2026 (#41, closed)** — F1–F11, listed on `PDM` in
`models/kz305-rebuild.yml` — but a kit still costs less than one wrong guess, and
the split is under review in #45.

⚠️ **Do not cheap out on the fuses themselves.** This harness exists because a
joint on the main power path melted. No-name blade fuses vary in blade plating
and hold-current accuracy; Littelfuse, Bussmann or MTA cost a few dollars more
across the whole set.

MTA's own part numbers, if you want them to match the block:
`0705090` 2 A · `0705100` 3 A · `0705101` 4 A · `0705110` 5 A · `0705120` 7.5 A ·
`0705130` 10 A · `0705140` 15 A · `0705150` 20 A · `0705160` 25 A · `0705170` 30 A

✅ **Orderable. All eleven ratings were assigned 4 Sep 2026** (#41):

| F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 A | 5 A | 10 A | 10 A | **15 A** | 5 A | 5 A | 7.5 A | 10 A | 7.5 A | 5 A |

⚠️ **Sized for INCANDESCENT on purpose.** The bike may run filament lamps before
the LED conversion, so every rating covers the stock load. **That is why the LED
headlight (#60) and the USB PD charger (#64) do not gate this** — their draw can
only be lower, and a rating sized for the heavier load stays correct either way.
Reasoning per fuse is on `PDM` in `models/kz305-rebuild.yml`.

#### Why the terminal and plug counts are still provisional

Two reasons, and neither is arithmetic:

1. `qty_multiplier` cannot help. It works off `pincount`, and `PDM` carries **10
   logical ways** against the module's **60 cavities**.
2. **The model draws the relays as separate parts wired to the `PDM`, but they
   physically seat in it.** So `W_HORN_PWR`, `W_COIL_PWR`, `W_HEAD_SUPPLY`,
   `W_HI_PWR`, `W_LO_PWR`, `W_MAIN_SW_FEED` and `W_SW_BUS` are not harness wires
   at all — they are the point-to-point jumpers inside the block. Until that is
   reconciled, no terminal count taken off this drawing is trustworthy.

32 terminals counts pins (5 relays × 4 + 6 fuses × 2) rather than cavities. The
**18 plugs figure is now firm** `[bench 10 Sep]`: a 4-way relay occupies four
cavities with no unpopulated ways under the body, so there is no separate
under-body population to cover and no path to the feared 28. What is still
provisional here is the *terminal* count, for reason 2 above — the jumpers.

### Open before committing

- **Which MTA modules are bussed.** The single most load-bearing question, per
  the busbar argument above. Get it off the datasheet, not off a retailer page.
- **Crimp tooling.** MP280 open-barrel dies, for the gauges in play.
- **Fuse family follow-through.** Committing to 280 commits the bike to **MINI**
  fuses throughout. Not a drawback, but it should be deliberate — it sets what
  spares get carried.
- **Enclosure and mounting.** Sets the footprint, so it comes before layout.
  The module is **107.6 x 72 x 60 mm lidded and that is the whole of it** — the
  terminals and seals are inside it, and the wires can turn 90° straight out of
  the bottom face with nothing in the way `[bench 10 Sep]`.
  What is open is **where it mounts**, which then sets the bundle routing and the
  clamping that keeps the bend off the seals. ⚠️ The MTA mounting legs are **not
  committed to** — the shipment was mis-picked and the legs may not be used at
  all.
- ~~**Relay retention against vibration.**~~ ✅ **Settled 10 Sep 2026** — it is
  terminal friction, and that is accepted. Fallback if it ever lifts: a keeper in
  the lid, addable after the build.

## Sources

- [Eastern Beaver — motorcycle rectifiers](https://www.easternbeaver.com/motorcycle-rectifiers/)
- [Shindengen — regulators/rectifiers](https://www.shindengen.com/products/electro/motorcycle/reg/)
- [Norton Owners Club — Shindengen SH775 regulators](https://www.nortonownersclub.org/forum/shindengen-sh775-regulators)
- [Access Norton — single-phase open regulator rectifier](https://www.accessnorton.com/NortonCommando/single-phase-open-regulator-rectifier.26142/)
- [motogadget mo.flash](https://www.motogadget.com/en-us/products/mo-flash) (discontinued)
- [Highsider SHIN YO 3-pin flasher relay](https://www.jpcycles.com/product/highsider-shin-yo-3-pin-universal-flasher-relay)
- [SHIN YO 3-pin, EU stock](https://cafe4racer.eu/en/flasher-relays-for-motorcycle-motorbikes/1010-shin-yo-3-pin-universal-flasher-relay-12v-4054783211647.html)
- [Kellermann flasher relay R1](https://www.kellermann-online.com/en/flasher-relay-r1/123.965)
- [Kellermann flasher relay R2](https://www.kellermann-online.com/en/flasher-relay-r2/123.970)
- [Custom LED ELFR-1](https://www.customled.com/products/elfr-1-electronic-led-flasher-relay)
- [Custom LED ELFR-1-QD](https://www.customled.com/products/elfr-1-qd-electronic-led-flasher-relay)
- [Custom LED flasher relay family](https://www.customled.com/collections/electronic-led-flasher-relays)
- [Novita EP35 vendor sheet](https://www.novitatech.com/?q=aftermarket%2Fproducts%2Felectronic-flashers%2Fep35)
- [KZRider — turn signals, EP35 testing](https://kzrider.com/forum/4-electrical/610321-turn-signals-for-dummies?start=12)
- [TST Industries LED flasher relay Gen 2](https://tstindustries.com/products/tst-led-flasher-relay-gen2)
- [Kuryakyn 2994](https://www.revzilla.com/motorcycle/kuryakyn-universal-10-amp-led-flasher-relay)
- [CF14 pinout-mirroring failure mode](https://electronics.alibaba.com/buyingguides/cf14-flasher-relay-guide-choose-right-for-led-turn-signals)
- [SuperBrightLEDs LF1-S-FLAT](https://www.superbrightleds.com/electronic-led-flasher-relays-for-motorcycle-universal-flat-motorcycle-flasher)
- [Tridon EP34 vendor sheet](https://www.tridon.com.au/products/Tridon/35/478/flashers-and-relays/2000/flasher-relays-electronic/1756/EP34)
- [KZRider — LED flasher relays frying](https://www.kzrider.com/forum/4-electrical/612048-led-flasher-relays-frying)
- [Rick's Motorsport Electrics — Hot Shot series](https://ricksmotorsportelectrics.com/l/hot-shot-series)
- [Rick's 10-317 for KZ305](https://www.svspowersports.com/products/ricks-replacement-regulator-rectifier-10-317)
- [Podtronics single-phase 12 V](https://www.britishbikebits.com/podtronics-solid-state-rectifier-regulater-bsa-triumph-single-phase-12v)
- [Regulator/rectifier guide — types, brands, faults](https://granttiller.com/regulator-rectifiers-alternators)
- [Electrex RR20 — GPZ305 / Z305LTD, three yellow leads](https://www.electrexworld.co.uk/acatalog/RR20_-_Regulator_Rectifier_GPZ305_GPZ400_GPZ600R.html)
- [EX305 / GPZ305 stator 21003-1073](https://www.theolouwesmotors.com/product/21003-1073-stator-generator-kaw-gpz305-ex305-b1/)
- [Rewinding single-phase to three-phase — feasibility](https://www.eng-tips.com/threads/how-to-rewind-a-stator-from-one-phase-to-three-phase.346823/)
- [Metri-Pack series overview and FAQs](https://www.whiteproducts.com/metripack-faqs.php)
- [MP280 sealed MINI fuse holder kit](https://ceautoelectricsupply.com/product/metri-pack-280-series-mini-fuse-holder-kit/)
- [Weatherproof triple MP280 fuse holder — Eastern Beaver](https://www.easternbeaver.com/product/aptiv-triple-metri-280/)
- [Sealed MINI/MICRO fuse & relay panel, ISO 280, bussed](https://www.delcity.net/store/fuses-fuse-accessories/panels-terminal-strip-connectors/sealed-mini/iso-280-relay-30-amp-bussed/)
- [ISO 280 micro relay, 35 A](https://m.delcity.net/store/NO-ISO!280-Micro-Relay/p_932455.h_932457)
- [Omron G8V micro 280 relay datasheet — terminal layout](https://www.mouser.com/datasheet/2/307/en-g8v-843959.pdf)
- [Littelfuse ISO micro relay datasheet](https://www.littelfuse.com/assetdocs/iso-micro-relays-datasheet?assetguid=63d22cee-8589-4d39-894c-c99a4fd82919)
- [MTA modular fuse & relay holding system](https://www.12voltplanet.co.uk/mta-modular-fuse-relay-holding-system.html)
- MTA power and modular solutions catalogue — filed at `parts/MTA_Power_modular_solutions_2019_v1.1.pdf`
- [MTA 0301370 — 60 sealed 2.8 mm cavities, 280 footprint](https://www.connectorid.com/products/mta-0301370-sealed-power-distribution-module-280-footprint)
- [0301370 module, cover 0301371, secondary lock 0301372](https://katalog.miunske.com/en/product-catalogue/fuses/combinable-fuseholder/free-configuable-central-electric/id-0301370)
