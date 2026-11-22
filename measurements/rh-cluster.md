# Right-hand bar cluster — stop switch and starter button

Readings on `RH`, the retained right-hand cluster, as rewired on the **built**
harness. Opened 22 Nov 2026; corrected the same day — see *What this is not*.

⚠️ **THE STARTER HAS NO INTERLOCK.** It cranks with the run/stop switch in
either position. That is the defect; it is not fixed.

## The defect

**The starter cranks in either position of the run/stop switch** `[bike,
22 Nov 2026]`, and at the cluster, **pressing the start button closes way 1 to
way 2 with the kill switch OFF** `[meter, 22 Nov 2026]`.

Way 1 is `RH_IN` from **PDM `c7 r2` (F2 OUT)** — live whenever the key is on,
and **upstream of the kill switch**. So the button is taking its feed from the
brown rather than from the kill-switch output, and the kill switch gates
nothing on the starter side.

### The ignition side is fine

**The kill switch does stop the engine** `[bike, 22 Nov 2026]`. Whatever way 2
carries in this build, it reaches the **solenoid trigger** and not `K_COIL`'s
coil — if it drove `K_COIL`, pressing the button with the kill switch OFF would
energise the coils and the kill switch could not stop anything.

So the model's way assignment does not describe the build. The rebuild draws:

| Way | Model's label | Model's far end |
|---|---|---|
| 1 | `STOP IN (Br)` | PDM `c7 r2` (F2 OUT) |
| 2 | `LINK (Y/R)` | `K_COIL` pin 86 (`c3 r5`) |
| 3 | `START OUT (BK)` | `SOL` way 3, the yellow spade |

On the bike, way 2 behaves as the **start output**. Ways 2 and 3 are evidently
not carrying what the drawing says, and `docs/landing-map.md` already records
`RH` way 1 as **not anchored** to any physical feature — the numbering is the
model's list order, with no keyway, latch or printed number read off the part.

## Why it matters — the kill switch was the only interlock

The stock cluster's 15 Aug reading is `RUN = Br-Y_R, Push = Y_R-BK,
**interlock holds**`: the kill switch fed the start button, so STOP cut the
starter as well as the coils. That interlock is gone.

Nothing else replaces it on this bike:

- **The neutral switch is not a crank interlock** — "Indicator only, NOT a
  crank interlock" `[meter 15 Aug 2026]`, and the factory starting circuit has
  no neutral interlock either.
- There is no clutch switch.

**So the bike will crank in gear with the run/stop switch at STOP.** That is
the hazard, and it is the whole of it — the ignition kill still works, so this
is a cranking hazard rather than a runaway one.

## The fix

The start button has to be fed from the **kill-switch output**, not from the
brown. At the cluster that means the button's input comes off the downstream
side of the kill switch, so the wire to `SOL`'s yellow spade is live only with
the switch at RUN.

Which of these it is has not been established, and they have different fixes:

- **A landing error at the new 3-way** — the conductors are crimped into the
  wrong ways. Fix is re-landing. Way 1 being unanchored is exactly the error
  that numbering invites.
- **A node inside the cluster pigtail upstream of the kill switch** — which is
  what the `SP_RH_BR` `[OPEN]` on `RH` describes: the stock brown splice sits
  on the cluster side and feeds legs off the same node as the kill-switch
  brown, live off F2. Fix is cutting back or capping.
- **The rewiring itself** — the button was deliberately or accidentally fed
  from the brown during the rebuild.

### The table to finish

Cluster UNPLUGGED from the harness, probing its own three pins:

| State | 1 to 2 | 1 to 3 | 2 to 3 |
|---|---|---|---|
| Kill OFF, button released | | | |
| Kill OFF, button PRESSED | **closed** `[22 Nov 2026]` | | |
| Kill ON, button released | | | |
| Kill ON, button pressed | | | |

**The reading that decides it:** which conductor closes to the brown with the
**kill switch ON and the button released**. That is the kill-switch output, and
the button's feed belongs on it.

Also worth recording while it is apart: **how many conductors are in the
pigtail**, three or four, and whether `SP_RH_BR` is still inside it. The
`[OPEN]` on `RH` turns on that.

## ⚠️ One reading still unexplained

Earlier the same day: **no voltage at the coil feed with the key on and the
kill switch at RUN, not cranking** — which is why the engine fired only while
the starter was held. That cannot be true at the same time as *the kill switch
stops the engine*, since both describe the kill switch driving `K_COIL`.

Either something changed between the two readings, or one of them was taken in
a different switch state than recorded. **Not resolved, and not guessed at.**
It is the one thing that would say whether there is a second fault on the
ignition side or only the one on the starter side.

## Also not recorded

**Contact resistance after cleaning.** The cluster measured **kill 3 ohm,
button 5 ohm, 8 ohm in series** on 15 Aug 2026, pre-cleaning, with cleaning a
planned build step the whole relay scheme depends on. Acceptance is under
1 ohm per contact, REL-zeroed.

## What this is not

**Corrected 22 Nov 2026.** This file first recorded the defect as *the kill
switch cannot stop the engine*, reasoning from the 1-to-2 reading plus the
model's way-2 assignment. The kill switch does stop the engine; the way-2
assignment is what is wrong. The defect is on the starter side only, and the
severity is a missing crank interlock rather than a missing ignition kill.

## Scope note

This is the first file in `measurements/` written against the **built** harness
rather than the old one. Everything else in this directory is archaeology on
what came off the bike; this is a reading on what is on it now.
