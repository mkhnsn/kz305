# Bench check sheet — 15 Aug 2026

Conditions: bike stripped, harness laid out on the bench, engine block separate.
Everything below is a static continuity check. Nothing here needs the engine,
the chassis, or the bike running.

## Rules for this session

1. **Null the meter leads first.** Short the probes, note the reading, subtract
   it from everything. **Leads = 0.4 Ω — use REL to zero them out**, and re-zero
   after changing probes or clips. At single-digit ohms the leads are a real
   fraction of the measurement.
2. **Record actual ohms, not beeps.** A continuity beeper hides 4 Ω, and 4 Ω is
   the difference between a working relay coil and one that never pulls in.
3. **Unplug the thing under test from the harness.** Parallel paths through the
   harness are almost certainly how the original scan transcription went wrong.
4. **Do not trust wire colors.** Ring every lead end-to-end. Forty years of oil
   has shifted them — white reads tan, blue/white reads gray.
5. **Record blind, compare after.** The "what the scan says" column is what you
   are *testing*, not confirming. Fill your column first, then compare.

---

## Check 1 — Starter relay coil ground  (TBD #1) — ✅ CLOSED 15 Aug 2026

**Resolved from the factory diagram at 600 dpi: direct ground, no interlock.**
Skip unless you want to upgrade it from diagram to meter, in which case the
procedure below still stands.

**Setup:** harness on bench. Starter relay **UNPLUGGED** — its ~3–5 Ω coil
otherwise bridges the two small leads and fakes continuity.

**Step A — identify the leads.** Ring each small relay lead to the right-bar
starter button. The one that reads through is **COIL+** (BK). The other is
**COIL−**.

  COIL+ identified as: ______________

**Step B — ring COIL− to each target:**

| Target | Reading | Meaning if it reads through |
|---|---|---|
| Single Y/BK chassis ground ring terminal | ______ Ω | **Direct ground** — loom correct as drawn |
| Neutral switch lead | ______ Ω | **Shared-wire interlock** — topology changes |

Exactly one should read through.

- Both read through → stop. The neutral switch lead would be tied to ground,
  defeating the interlock. More likely a misidentified lead.
- Neither reads through → COIL− goes somewhere not yet modeled. Trace it.

---

## Check 2 — Ignition switch  (TBD #3) — ✅ DONE 15 Aug 2026, matches scan

**Setup:** switch unplugged from harness. Four pins: W, Br, R/BK, R.

Test **every pair in every position** — six pairs, four positions. Checking only
the expected pairs is how a bad transcription survives.

| Pair | OFF | LOCK | ON | PARK |
|---|---|---|---|---|
| W ↔ Br | open | open | **0.5 Ω** | open |
| W ↔ R/BK | open | open | open | open |
| W ↔ R | open | open | open | **closed** |
| Br ↔ R/BK | open | open | open | open |
| Br ↔ R | open | open | open | open |
| R/BK ↔ R | open | open | **closed** | open |

✅ The 0.5 Ω on W↔Br is leads (0.4 Ω). Actual contact ~0.1 Ω — healthy.

**What the scan says (unconfirmed):** ON = W↔Br *and* R/BK↔R · OFF = none ·
LOCK = none · PARK = W↔R only.

Watch for: any continuity at all in OFF or LOCK, and whether PARK really is
W↔R *alone*. Park feeds tail from the battery with ignition dead — a modern
fuse block drops that function by accident.

---

## Check 3 — Right handlebar cluster  (TBD #3) — ✅ DONE 15 Aug 2026, interlock OK, contacts BAD

**Setup:** cluster unplugged. Three pins: Br, Y/R, BK. Two independent switches
share Y/R, so test all four combinations.

| Pair | OFF, released | OFF, pressed | RUN, released | RUN, pressed |
|---|---|---|---|---|
| Br ↔ Y/R | open | open | closed | closed |
| Br ↔ BK | open | **open** | open | **~8 Ω** |
| Y/R ↔ BK | open | ~5 Ω | open | ~5 Ω |

🛑 Interlock verified, but 8 Ω in series will not pull the relay in. Clean both
switch contacts and re-measure before building.

**What the scan says (unconfirmed):** RUN = Br↔Y/R · Push = Y/R↔BK.

**Predictions worth testing explicitly:**
- Y/R↔BK should close on push in *either* kill position — the button is its own
  switch.
- Br↔BK should close **only** in RUN + pressed. That series path *is* the
  interlock.
- ⚠️ **OFF + pressed must read Br↔BK OPEN.** If it reads through, the kill/start
  interlock is broken and the `RH` note in the loom file is wrong.

---

## Check 4 — Left dimmer common  (open since 13 Aug)

Not a stage-1 circuit, but the cluster is in your hand and this has been open
for two days.

**Setup:** left cluster unplugged. Three pins: R/BK, Bl, R/Y.

| Pair | HI | LO |
|---|---|---|
| R/BK ↔ Bl | | |
| Bl ↔ R/Y | | |
| R/BK ↔ R/Y | | |

The pin appearing in **both** positions is the common (the feed). The scan reads
Bl as common, but flags this as the one marginal table.

⚠️ Getting the common wrong puts both filaments on at once.

---

## Opportunistic — only while the harness is off the bike

- [ ] **Second harness tag.** One reads `26001-12348`. A second tag on another
      branch has not been logged. Read both under good light: ______________
- [ ] **Neutral switch residual 4 Ω** — split the path to locate it:
      switch terminal → case nearby = ______ Ω (the switch contact itself,
      runs in oil, a few ohms may just be the switch);
      case → starter ground point = ______ Ω (should be milliohms).

---

## Results → where they land

| Check | Updates |
|---|---|
| 1 | `W_SOL_GND` note in the loom; topology if shared-wire |
| 2 | `IGN` connector note; `docs/kz305-b1-wiring.md` ignition table |
| 3 | `RH` connector note; `docs/kz305-b1-wiring.md` right-bar table |
| 4 | `docs/kz305-b1-wiring.md` dimmer table + closes its "Still open" item |

Report readings back and they get encoded with date and method, same as the
points leads.
