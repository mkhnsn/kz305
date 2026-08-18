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

### Recommended: motogadget mo.flash

The deciding fact is that it is a **2-wire series device that needs no
ground**, so it drops into the stock 2-pin socket as-is.

| | |
|---|---|
| Wiring | 2 cables, series, no separate ground |
| Voltage | 5–18 V (also works on 6 V) |
| Load | min ~1 W, max 100 W |
| Protection | short-circuit proof, automatic overload protection |
| Build | fully encapsulated, waterproof and vibration resistant |
| Size | 18 × 13 × 9.5 mm, 4 g |

⚠️ **Check the minimum load against the lamps actually chosen.** Only one side
flashes at a time, so the load the flasher sees is *two* lamps plus the dash
indicator, not four. Micro LED signals at 0.5 W each put one side at about
1 W — sitting exactly on the stated minimum. Pick signals that keep per-side
load at 2 W or more, or verify the pair before committing.

### Alternative: SHIN YO 3-pin universal

Recommended on the KZRider forum for this family of bikes. 5 mA to 15 A,
180 W max, adjustable flash rate, which is useful if any incandescent survives
the conversion. Needs the ground wire.

### Premium alternative: Kellermann R1 / R2

Load-independent at a fixed 75 flashes/min, very small. Worth it only if
matching Kellermann signals.

### Run the flasher ground wire regardless

It costs nothing at build time and cannot be added later without opening the
loom. The mo.flash does not need it; the SHIN YO does. Running it keeps the
choice open right up until the part is fitted, and reversible for the next
owner.

### On cheap flashers frying

A KZRider thread on relays burning out is worth reading in full, because the
headline is misleading. The root cause in that case was **touching wires in the
rear light assembly** creating a short — the poster's cheap relay worked fine
once the wiring was corrected. The secondary finding still stands, though: one
of the failed units was rated only 42 W.

So the honest lesson is not "cheap relays fail". It is that a short will kill
whatever is fitted, and that short-circuit protection is cheap insurance on a
harness being built from scratch. The mo.flash has it.

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
- [motogadget mo.flash](https://www.motogadget.com/en-us/products/mo-flash)
- [Kellermann flasher relay R1](https://www.kellermann-online.com/en/flasher-relay-r1/123.965)
- [KZRider — LED flasher relays frying](https://www.kzrider.com/forum/4-electrical/612048-led-flasher-relays-frying)
- [Rick's Motorsport Electrics — Hot Shot series](https://ricksmotorsportelectrics.com/l/hot-shot-series)
- [Rick's 10-317 for KZ305](https://www.svspowersports.com/products/ricks-replacement-regulator-rectifier-10-317)
- [Podtronics single-phase 12 V](https://www.britishbikebits.com/podtronics-solid-state-rectifier-regulater-bsa-triumph-single-phase-12v)
- [Regulator/rectifier guide — types, brands, faults](https://granttiller.com/regulator-rectifiers-alternators)
