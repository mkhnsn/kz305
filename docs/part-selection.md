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

### Fallback: generic 3-pin electronic flasher (CF14 / JL-02 style)

$5–10 and always available. Electrically fine for this bike given the load
numbers above. What is given up is sealing, a known brand, and any spec sheet
worth trusting — on a part that costs $15 less than the Shin YO and is a
five-minute swap if it fails. A defensible choice, not a false economy.

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

### Recommended: Shindengen SH775

A **series (open) type**. When the battery is charged it *disconnects* the
stator rather than shorting it, so the stator stops producing current it does
not need.

That is the difference that matters here. A shunt regulator makes the stator
windings themselves the load, so cutting electrical load with LEDs pushes more
surplus into heat. A series regulator removes the load entirely — **both the
regulator and the stator run cooler, and the LED heat problem is cured at
source rather than mitigated.**

Rated about 30 A, far above anything this bike will ask for.

**Caveats, honestly:**

- Only two of three rectifier legs are used, so real capacity is below the
  rating. Irrelevant at this bike's load, but true.
- **Counterfeits are widespread.** Buy from a known source — Roadstercycle is
  the name that recurs. Suspiciously cheap "OEM" listings are fakes.
- One forum participant raised unconfirmed doubt about whether the series
  control circuitry monitors voltage differential across the AC phases. Field
  reports say it works; nobody has shown a datasheet either way.
- Physically larger than a Podtronics.
- Lithium-friendly, which the shunt units are not — worth noting if a lithium
  battery is ever on the cards.

### Fallback: single-phase shunt units

If off-label use is unappealing, the purpose-built single-phase parts are all
**shunt** type and none of them cure the heat trade:

| Option | ~Price | Notes |
|---|---|---|
| **Podtronics single-phase 12 V** | $75 | Classic-bike standard, purpose-built for single-phase. Needs fins and airflow. |
| **Boyer Power Box** | $170 | 180 W. Confirm current production for reverse-polarity protection. |
| **Tympanium** | — | Compact, no fins. Poor availability. |
| **Rick's 10-317** | $109 | Direct-fit KZ305, but a fresh *stock* SCR shunt. |
| **Rick's Hot Shot** | — | MOSFET **shunt** — cooler regulator, but it does nothing for the stator. KZ305 fitment unconfirmed. |

⚠️ **A MOSFET shunt is not a substitute for a series unit.** It improves the
regulator's own survival through lower forward drop, but it shorts the stator
exactly as an SCR does, so the stator sees the same treatment.

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

## Sources

- [Eastern Beaver — motorcycle rectifiers](https://www.easternbeaver.com/motorcycle-rectifiers/)
- [Shindengen — regulators/rectifiers](https://www.shindengen.com/products/electro/motorcycle/reg/)
- [Norton Owners Club — Shindengen SH775 regulators](https://www.nortonownersclub.org/forum/shindengen-sh775-regulators)
- [Access Norton — single-phase open regulator rectifier](https://www.accessnorton.com/NortonCommando/single-phase-open-regulator-rectifier.26142/)
- [motogadget mo.flash](https://www.motogadget.com/en-us/products/mo-flash) (discontinued)
- [Highsider SHIN YO 3-pin flasher relay](https://www.jpcycles.com/product/highsider-shin-yo-3-pin-universal-flasher-relay)
- [SHIN YO 3-pin, EU stock](https://cafe4racer.eu/en/flasher-relays-for-motorcycle-motorbikes/1010-shin-yo-3-pin-universal-flasher-relay-12v-4054783211647.html)
- [Kellermann flasher relay R1](https://www.kellermann-online.com/en/flasher-relay-r1/123.965)
- [KZRider — LED flasher relays frying](https://www.kzrider.com/forum/4-electrical/612048-led-flasher-relays-frying)
- [Rick's Motorsport Electrics — Hot Shot series](https://ricksmotorsportelectrics.com/l/hot-shot-series)
- [Rick's 10-317 for KZ305](https://www.svspowersports.com/products/ricks-replacement-regulator-rectifier-10-317)
- [Podtronics single-phase 12 V](https://www.britishbikebits.com/podtronics-solid-state-rectifier-regulater-bsa-triumph-single-phase-12v)
- [Regulator/rectifier guide — types, brands, faults](https://granttiller.com/regulator-rectifiers-alternators)
- [Electrex RR20 — GPZ305 / Z305LTD, three yellow leads](https://www.electrexworld.co.uk/acatalog/RR20_-_Regulator_Rectifier_GPZ305_GPZ400_GPZ600R.html)
- [EX305 / GPZ305 stator 21003-1073](https://www.theolouwesmotors.com/product/21003-1073-stator-generator-kaw-gpz305-ex305-b1/)
- [Rewinding single-phase to three-phase — feasibility](https://www.eng-tips.com/threads/how-to-rewind-a-stator-from-one-phase-to-three-phase.346823/)
