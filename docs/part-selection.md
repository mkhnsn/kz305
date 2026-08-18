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

### The market reality, and it is worse than the SH775 warning suggests

The models already flag that the popular SH775-class **series** upgrade is
three-phase only. Research widens that considerably: **essentially the entire
modern MOSFET regulator market is three-phase.** Eastern Beaver's Shindengen
lineup — FH020AA, FH027EA, FH014AA, FH027BA and the SH847 — is three-phase
throughout. None of it fits this bike, however often "just fit a MOSFET R/R" is
offered as universal advice.

🛑 **Every option that does fit is still a SHUNT regulator.** None of them cure
the problem that cutting load with LEDs makes a shunt unit dump *more* surplus
as heat. A modern unit runs cooler than the 44-year-old original, but the
LED heat trade is unchanged. Mount it in airflow and check body temperature on
the bench run, not just voltage.

### Candidates that actually fit single-phase

| Option | ~Price | Notes |
|---|---|---|
| **Podtronics single-phase 12 V** | $75 | The classic-bike standard — British twins are single-phase, so this is a purpose-built part rather than an adaptation. High-output version suits 180 W stators. Needs cooling fins and airflow. |
| **Boyer Bransden Power Box** | $170 | Single-phase, 180 W. Older units lacked reverse-polarity protection; resolved on current production, so confirm which you are buying. |
| **Tympanium** | — | Smaller, no cooling fins, mounts under the battery carrier. Availability is poor and it is little seen now. |
| **Rick's 10-317** | $109 | Direct-fit OEM-style replacement listed for the KZ305. New, plug-and-play, but still an SCR shunt — a fresh stock part, not an upgrade. |
| **Rick's Hot Shot** | — | MOSFET, runs cooler, direct-fit versions come with factory plugs. **Fitment for the KZ305 is NOT confirmed** — their site has no single-phase or KZ305 listing for the Hot Shot line. |

### Recommendation

**Call Rick's first: 603-329-9901.** If a Hot Shot exists for the KZ305 it is
the best answer — MOSFET, direct fit, factory connectors — and heat is the
thing this bike is least able to afford. If not, **Podtronics single-phase**:
cheapest of the credible options, purpose-built for single-phase, and long
proven on bikes with the same charging architecture.

Rick's 10-317 is the right choice only if the goal is a working stock bike
rather than an improved one.

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
- [motogadget mo.flash](https://www.motogadget.com/en-us/products/mo-flash) (discontinued)
- [Highsider SHIN YO 3-pin flasher relay](https://www.jpcycles.com/product/highsider-shin-yo-3-pin-universal-flasher-relay)
- [SHIN YO 3-pin, EU stock](https://cafe4racer.eu/en/flasher-relays-for-motorcycle-motorbikes/1010-shin-yo-3-pin-universal-flasher-relay-12v-4054783211647.html)
- [Kellermann flasher relay R1](https://www.kellermann-online.com/en/flasher-relay-r1/123.965)
- [KZRider — LED flasher relays frying](https://www.kzrider.com/forum/4-electrical/612048-led-flasher-relays-frying)
- [Rick's Motorsport Electrics — Hot Shot series](https://ricksmotorsportelectrics.com/l/hot-shot-series)
- [Rick's 10-317 for KZ305](https://www.svspowersports.com/products/ricks-replacement-regulator-rectifier-10-317)
- [Podtronics single-phase 12 V](https://www.britishbikebits.com/podtronics-solid-state-rectifier-regulater-bsa-triumph-single-phase-12v)
- [Regulator/rectifier guide — types, brands, faults](https://granttiller.com/regulator-rectifiers-alternators)
