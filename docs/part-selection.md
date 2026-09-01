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
- **Confirm where the DC output lands.** `models/kz305-factory.yml` models it
  as returning to the battery stud, which is NOT confirmed off the scan (#15).

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

### Open before committing

- **Which MTA modules are bussed.** The single most load-bearing question, per
  the busbar argument above. Get it off the datasheet, not off a retailer page.
- **Crimp tooling.** MP280 open-barrel dies, for the gauges in play.
- **Fuse family follow-through.** Committing to 280 commits the bike to **MINI**
  fuses throughout. Not a drawback, but it should be deliberate — it sets what
  spares get carried.
- **Enclosure and mounting.** Sets the footprint, so it comes before layout.
- **Relay retention against vibration**, for whichever route.

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
- [MTA power and modular solutions catalogue (PDF)](https://www.mta.it/flex/files/1/d/9/D.f3e6d7122b09b483f4c2/MTA_Power_modular_solutions_2019_v1.1.pdf)
