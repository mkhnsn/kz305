# Part selection

What is chosen, what is in hand, and what is still open. **Current state only.**
The working-out, superseded options and dated history are in
`archive/part-selection-2026-09-10.md`. Where this file and
`models/kz305-rebuild.yml` disagree, the model wins.

| Part | Status |
|---|---|
| Regulator/rectifier | **Shindengen SH775, in hand** |
| PDM | **MTA `0301370`, in hand and checked** |
| Relays | **Song Chuan SCMR20 (`-R1`), ordered** from Cycle Terminal. Amazon knockoffs in hand for test-fitting |
| Wire | TXL, Prowire. **All 16 AWG** in the PDM; 14 and 12 where noted |
| Fuses | Ratings assigned, F1–F11, plus **7 spares populated in the block**. **Ordered** (Cycle Terminal): Mini blade + ATC 20 A / 30 A |
| Flasher | **Custom LED ELFR-1, ordered** 11 Sep (#11) |
| 6 AWG heavy cable | **Ordered** 11 Sep: welding cable + 1/4" lugs, fits the M6 studs (#42) |
| USB-C PD charger | Criteria set, part not selected (#64) |
| LED headlight | Not selected (#60) |
| Labels, grommets, diodes | **Ordered** 11 Sep: Rhino-compatible 6/9/12/19 mm, grommet kit, 1N4004 x125 |

---

## Regulator / rectifier — Shindengen SH775 (#12)

**In hand, 29 Aug 2026.** A used Polaris ORV takeoff, $45. Polaris `4012941`,
*"REGULATOR 3PH 35A SERIES 105C"* (alternate OEM number `710001103`).

- **A single-phase stator uses two of its three AC inputs.** This is standard
  practice on single-phase classics (routine on Nortons). The third input is left
  unterminated.
- **Series, not shunt.** It open-circuits the stator rather than burning the
  surplus, which is what makes the LED conversion comfortable.
- **DC+ runs heavy and direct to the battery**, fused at the battery end
  (`MF_RR`), not through the PDM. Series units are sensitive to resistance in
  that path. See `W_RR_OUT` in the model.
- **Connectors:** the Furukawa QLW pair from Cycle Terminal. `QLW-A-3F-GR` (AC,
  14 AWG sockets) and `QLW-A-B3F-B` (DC). See `docs/connector-order.md`.

**Open:**
- [ ] **Bench-test the unit before build.** It's used with an unknown history.
  Each AC leg must read infinity to ground, and it should hold 14.0–14.5 V on the
  bike.
- [ ] **The stator's rated output in watts** has never been read off anything.
  Only the 0.4 Ω and 75 V AC test values are known. This is what keeps
  `W_RR_OUT`'s 12 AWG provisional.

**Fitting rules:** target 14.0–14.5 V at 3,000–5,000 rpm, and check body
temperature. **Never** disconnect the regulator with the ignition on, or the
battery while running. Mount it where the airflow is.

*Not doing:* a three-phase conversion. It needs a new stator and rotor, fitment is
unproven, and the only argument for it (series regulation) is met by the SH775.

---

## PDM — MTA `0301370`

**In hand and checked, 9–10 Sep 2026** `[bench]`. The physical layout is in
**`docs/pdm-cavity-map.md`**, the build reference.

| | |
|---|---|
| Module | 60 sealed 2.8 mm cavities, **6 rows x 10 columns**, pitch 7.91 x 7.67 mm |
| Envelope | **107.6 x 72 x 60 mm lidded** — that's all of it; terminals and seals sit inside |
| Takes | MiniVal (standard Mini) fuses across 2 cavities; micro 280 relays, **4-way** (2 x 2) or 6-way (3 x 2) |
| Population | 11 fuses + 5 relays (6 relay positions), **42 wired cavities, 18 plugs** |

### Parts and quantities

Design quantities are on the `PDM` node in the model and are authoritative. The
order was placed 3 Sep and received complete from **ConnectorID**, an authorised
MTA distributor that stocks every line.

| Part | MTA PN | Design | In hand |
|---|---|---|---|
| Module | `0301370` | 1 | 1 |
| Cover | `0301371` | 1 | 1 |
| Secondary lock (TPA) | `0301372` | **6** — six per module | 8 |
| Terminal, 18–16 AWG | `1708338-L` | **41** | 100 |
| Terminal, 14–12 AWG | `1708339-L` | **1** (`W_MAIN_SW_FEED`) | 30 |
| Terminal, 22–20 AWG | `1708337-L` | 0 | 10 (spare, no use) |
| Wire seal, green | `4550747` | **42** | 60 |
| Wire seal, red | `4550748` | **0** — no 18 AWG left | 40 (spare) |
| Cavity plug | `4550750` | **18** | 40 |
| Mounting legs | `0300690` / `0300691` | — | 4 of one gender (see below) |

**Check:** 42 wire ends enter the module = 11 fuses x 2 + 5 relays x 4. One wire
per cavity. If a later edit breaks that equality, one side is wrong.

⚠️ **Reorders:** order the **`-L`** terminal part numbers (loose piece). Without
the suffix it's a reel of thousands.

### Settled at the bench `[bench 10 Sep 2026]`

- **Cover** closes over a populated block with both relay sizes. It's close on
  the 6-way.
- **Relay retention** is terminal friction, and that's accepted. If vibration
  ever lifts a relay, add a keeper to the lid.
- **Relays don't overhang** into neighbouring cavities. A relay costs its own
  footprint.
- **Relay rotation needs no key.** See `docs/pdm-cavity-map.md`.
- **Mounting legs were mis-picked:** both bags are correctly labelled but hold
  the same gender. Not chased. If the legs are ever used, re-order and check
  contents against the labels.

### Assembly rules

1. **Star the feed buses outside the module.** A sealed cavity takes one seal on
   one wire, so there's no daisy-chaining between cavities. `SP_HOT` and `SP_SW`
   are the two star points.
2. **Keep HOT and SWITCHED apart.** HOT at one end, SWITCHED at the other, with
   the relay block between. Interleaved, a mis-landed feed wire can put F3 on
   permanent power.
3. **Write the cavity map as you build.** Correct `docs/pdm-cavity-map.md` in
   place: cavity, circuit, colour, gauge.
4. **Depinning:** pull the TPA first, then release **two tangs**, one each side.
   The Aptiv `12094429` already owned works. See `docs/prowire-order.md`.

### Open
- [ ] **Where it mounts.** This sets the enclosure, the routing of 42 wires out
  of one face, and the bundle clamping that keeps the bend off the seals.
- [x] ~~**Crimp tools**~~. Owned for every terminal family: sealed MTA 280,
  HW090, MP630.
- [ ] **Pull-test the first crimp.**
- [x] ~~**#45** (hot/switched split)~~. **Settled 10 Sep: the split stays**, so
  the cavity map stands. A welded horn or beam relay is fixed by pulling it and
  fitting the spare. See `docs/pre-ride-check.md`.

---

## Wire seals

**All green `4550747` (2.2–3.0 mm).** Every cavity wire is 16 AWG TXL (2.26 mm
nominal) or 14 AWG TXL (2.59 mm). Red (1.2–2.1) was for 18 AWG, and there is none
left.

✅ **Green seal fit on 16 AWG TXL: very snug** `[bench 10 Sep]`. The wire
calipered **2.20–2.21 mm** against a 2.26 nominal, which puts it on green's
lower bound. The fit test is what counts, and it passed.

If a future spool ever feels loose in a green seal, move those circuits to 14 AWG,
which sits mid-band in green. That's **only partly funded**: 41 wires would need
about 42 `1708339-L` against the 30 in hand.

⚠️ **Seals are sized by insulation OD, so they're tied to the wire family.** GXL
or SXL in the same gauges have different ODs. Change the wire family and
re-check the seals. Don't substitute Aptiv Metri-Pack 280 seals: "280" names the
blade, not MTA's cavity bore.

---

## Relays — Song Chuan 303 `-R1`

`303-1AH-C-R1`, Ultra Micro 280, 20 A, SPNO, **4-way** (2 x 2 pins). Sold by
Cycle Terminal as `SCMR20`, which they list as the **resistor type**.
**Genuine relays are on order from Cycle Terminal** and replace the Amazon
knockoffs, which were used for test-fitting. The knockoffs are resistor type too
`[bench 10 Sep]`. Six positions, **six fitted**: five wired and `K_SPARE` sitting unwired in the sixth so the spare lives with the bike (decided 11 Sep). **Buy six.**

**On arrival:** read each coil with a DMM both ways round. Resistor type reads
the same in both directions; a diode doesn't. And read the pin marking: the
knockoff showed the second coil pin as 86 or possibly 88. **Carry a spare on the bike.** It's
the fix for a stuck horn or beam, and for a failed stop check
(`docs/pre-ride-check.md`).

**K_MAIN is the loaded one:** about 12 A sustained and 19 A peak on filament
lamps, against a 20 A relay. The others carry 0.1–7 A.

### Coil suppression

**Integral resistor, `-R1`** (1.1 kΩ across the coil, 91 mA), **not** the
`-D1` diode variant.

⚠️ **This is load-bearing, not a preference.** The pins are **30/87 on one
diagonal and 85/86 on the other**, so the footprint accepts a relay 180° round,
and with `-R1` that's harmless. A `-D1` fitted backwards is **a dead short
across the coil**, and you can't see it once seated.

**Standing rule for every relay bought from now on:** read the coil with a DMM
**both ways round** before fitting. A resistor reads the same both ways, a diode
does not. Anything that reads differently is a `-D1` and doesn't go in.

86 is COIL+ and 85 COIL− on every relay in the design. Build it that way even
though the part doesn't care.

**Starter solenoid (`SOL`):** a stock part with no integral option. It needs a
discrete diode, **cathode to the coil's positive feed**.
⛔ **Don't fit it until blocker 3 closes.** Which lead is COIL+ isn't known yet,
and a diode fitted backwards shorts the coil supply on every start press. See #46.

---

## Fuses — standard Mini blade

**MTA "MiniVal" is the industry-standard Mini (ATM/APM) fuse**: 16.2 x 11.1 x
4 mm body, 2.8 mm blade, standard colour code. Any reputable Mini blade fits.

| F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 A | 5 A | 10 A | 10 A | **15 A** | 5 A | 5 A | 7.5 A | 10 A | 7.5 A | 5 A |

Assigned 4 Sep (#41). **Sized for incandescent on purpose**, so the LED headlight
and USB charger can't move them. Per-fuse reasoning is on `PDM` in the model.

**Plus 7 spares, populated in the block's spare positions** (decided 11 Sep):
2 x 5 A, 2 x 7.5 A, 2 x 10 A, 1 x 15 A. Layout in `docs/pdm-cavity-map.md`.
So the kit needs **18 Mini fuses**: 7 x 5 A, 4 x 7.5 A, 5 x 10 A, 2 x 15 A.

- **Buy a quality kit** — Littelfuse, Bussmann or MTA. This harness exists because
  a joint on the main power path melted.
- ⚠️ **Don't buy by mistake:** MTA **uniVAL** (ATO size, won't seat) or
  **MiniVal Low Profile** (different body).
- MTA PNs: `0705110` 5 A · `0705120` 7.5 A · `0705130` 10 A · `0705140` 15 A.

---

## 6 AWG heavy cable (#42)

`W_BAT_SOL`, `W_SOL_SM`, `W_BAT_GND`, `W_ENG_GND`. **Not TXL**, since TXL stops
around 8 AWG. Use **fine-strand welding cable**, red and black, with tinned
copper lugs and adhesive heat-shrink boots.

**Ordered 11 Sep 2026:** Shirbly 6 AWG welding cable, 10 ft red + 10 ft
black; SELTERM 6 AWG 1/4" tinned copper lugs, 25. Both relay studs and the
motor terminal are **M6** `[bench 11 Sep]`, and a 1/4" (6.35 mm) hole fits M6.
Battery-post and star-bus lug sizes not yet read; the 1/4" lugs likely cover
them too.

- [ ] Adhesive heat-shrink boots for the lugs - not yet ordered (the 19 mm
  printed labels are not boots).

⚠️ `W_ENG_GND` carries the whole cranking return. It's not a signal earth.

---

## USB-C PD charger (#64)

Replaces the stock accessory circuit, which was a permanently live, unfused feed
with its earths never connected. **One circuit on F10: switched, individually
fused, grounded to the star bus.**

**Criteria:**
- 12 V in, PD out, **20–45 W**.
- ⚠️ **Must tolerate the charging system**, not just the battery: 14.0–14.5 V
  running, with transients if the battery is ever disconnected.
- **Sealed 090**, like every other connection.
- **A capped socket or a captive lead.** An open USB-C socket on a bike collects
  water and grit.

**Switched, not always-hot.** The bike has no parasitic load today, and a phone
left plugged in overnight flattens a 10 Ah battery. Moving F10's input to
`SP_HOT` is a one-wire change if that's ever wanted.

F10 is already 7.5 A, sized for a 45 W unit's ~4.4 A plus capacitive inrush.
Prefer a slow-blow characteristic if the chosen unit specifies one.

---

## Flasher (#11)

Required because the bike is going **full LED**. It needs a **load-independent**
solid-state unit. Load is only 2–4 W per side, so capacity isn't the deciding
factor.

**Ordered 11 Sep 2026: Custom LED ELFR-1** (the plug-in version, not the QD), $25.99, arriving Tuesday. Stays open on #11 until bench-tested with the LED signals.

The shortlist it was chosen from:

| | |
|---|---|
| **Custom LED ELFR-1-QD** | $24.99, US stock, 0.05–10 A, 1/4" QD spades, 2-wire (needs no ground), 1-year warranty |
| **SHIN YO 3-pin** (Highsider 208-070) | ~$20, 5 mA–15 A, adjustable rate, hazard function. **US stock thin**; EU sellers carry it |
| Walk-in backup | Novita EP35, ~$15 at AutoZone. 3-terminal, needs the ground, clicks |

- **Run the flasher ground wire regardless.** It costs nothing now and means
  opening the loom later.
- ⚠️ **No vendor publishes reverse-polarity protection.** Verify B+/load
  orientation with a meter before first power-up.
- *Avoid:* CF13/CF14 generics (mirrored pinouts that look identical, and
  reversed kills them), and the discontinued motogadget mo.flash.

---

## Sources

- [Shindengen — regulators/rectifiers](https://www.shindengen.com/products/electro/motorcycle/reg/)
- [Norton Owners Club — Shindengen SH775 regulators](https://www.nortonownersclub.org/forum/shindengen-sh775-regulators)
- [Access Norton — single-phase on a three-phase regulator](https://www.accessnorton.com/NortonCommando/single-phase-open-regulator-rectifier.26142/)
- [Eastern Beaver — motorcycle rectifiers](https://www.easternbeaver.com/motorcycle-rectifiers/)
- MTA power and modular solutions catalogue — filed at `parts/MTA_Power_modular_solutions_2019_v1.1.pdf` (module part numbers only)
- MTA `0301370` dimensioned drawing — filed at `parts/mta-0301370-dimensions.png`
- [MTA 0301370 at ConnectorID](https://www.connectorid.com/products/mta-0301370-sealed-power-distribution-module-280-footprint)
- [0301370 module, cover 0301371, secondary lock 0301372 — Miunske](https://katalog.miunske.com/en/product-catalogue/fuses/combinable-fuseholder/free-configuable-central-electric/id-0301370)
- [Littelfuse ISO micro relay datasheet](https://www.littelfuse.com/assetdocs/iso-micro-relays-datasheet?assetguid=63d22cee-8589-4d39-894c-c99a4fd82919)
- [Custom LED ELFR-1-QD](https://www.customled.com/products/elfr-1-qd-electronic-led-flasher-relay)
- [Highsider SHIN YO 3-pin flasher relay](https://www.jpcycles.com/product/highsider-shin-yo-3-pin-universal-flasher-relay)
- [Novita EP35 vendor sheet](https://www.novitatech.com/?q=aftermarket%2Fproducts%2Felectronic-flashers%2Fep35)
- [KZRider — turn signals, EP35 testing](https://kzrider.com/forum/4-electrical/610321-turn-signals-for-dummies?start=12)

The full source list, including every option passed over, is in the archive.
