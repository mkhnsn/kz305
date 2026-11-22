# Right-hand bar cluster — stop switch and starter button

Bench and in-situ readings on `RH`, the retained right-hand cluster. Opened as
its own capture sheet on **22 Nov 2026**, when a live fault on the built harness
turned out to be in this part rather than in the PDM.

⚠️ **THIS FILE RECORDS A SAFETY DEFECT THAT IS NOT YET FIXED.** As wired on
22 Nov 2026 the **kill switch cannot stop the engine.** See below.

## What the models assume about this cluster

The rebuild draws `RH` as three ways:

| Way | Label | Wire | Far end |
|---|---|---|---|
| 1 | `STOP IN (Br)` | `RH_IN`, YE 16 AWG | **PDM `c7 r2` (F2 OUT)** — live whenever the key is on |
| 2 | `LINK (Y/R)` | `YR_TRIG`, GY 16 AWG | **`K_COIL` pin 86 (`c3 r5`)** — the ignition relay's coil |
| 3 | `START OUT (BK)` | `RH_OUT`, YE 16 AWG | **`SOL` way 3** — the solenoid's yellow spade |

The assumption behind that is the stock switch table, `RUN = Br-Y_R, Push =
Y_R-BK` `[meter 15 Aug 2026]`: the kill switch closes **1 to 2**, and the button
then closes **2 to 3**. Way 2 is therefore supposed to be the *kill-switch
output*, and everything that stops the engine depends on it being so.

## ⛔ MEASURED 22 Nov 2026 — the BUTTON closes 1 to 2, not the kill switch

**With the kill switch OFF, pressing the start button closes way 1 to way 2.**

That is the whole fault, and it is sufficient on its own:

- Way 1 is permanently live off F2 with the key on, **upstream of the kill
  switch**.
- Way 2 is `K_COIL`'s coil.

So pressing the button energises `K_COIL` from F2, F3 power reaches `SP_YR`,
and both coils come alive. Release the button and the relay drops out and the
coils die.

### It accounts for every symptom reported

| Symptom | Cause |
|---|---|
| Engine fires on both cylinders while cranking, dies the instant the button is released | `K_COIL` is energised only while the button is held |
| No voltage at the coil feed with the key on, kill switch RUN, not cranking | the kill switch does **not** close 1 to 2, so nothing else energises `K_COIL` |
| Kill switch OFF, button pressed - a relay clicks but no crank | that click is `K_COIL`, fed from way 1; way 3 is not fed, so the solenoid does nothing |
| Kill switch RUN, button pressed - cranks | way 3 is fed, so the solenoid pulls in as designed |

### ⛔ What it means for the kill switch

**Way 2 is on the button's contact, and the kill switch reaches nothing.**
Cutting coil power at `K_COIL`'s trigger is the entire safety function of that
relay - see the `W_COIL_PWR` note in `kz305-rebuild.yml` - and it is not
connected to the kill switch. `docs/pre-ride-check.md` asks for the engine to
stop both ways on every ride; as wired, the kill-switch half of that check
cannot pass, and a spare relay will not fix it.

## ⚠️ OPEN — landing error or cluster internals?

**Not yet determined, and the two have different fixes.** A single row of the
truth table is confirmed; it does not distinguish:

- **A landing error at the new 3-way.** The cluster's conductors are crimped
  into the wrong ways. `docs/landing-map.md` lists `RH` among the connectors
  where way 1 is **not anchored** to any physical feature - the numbering is
  the model's list order - so an offset here is exactly the mistake that
  numbering invites. Fix is re-landing.
- **The cluster's own internals, or its pigtail.** The `[OPEN]` on `RH` in
  `kz305-rebuild.yml` records that the stock brown splice `SP_RH_BR` sits on
  the **cluster side** and feeds Br/W and Bl/W off the same node as the
  kill-switch brown, live off F2 and landing nowhere. A node upstream of the
  kill switch, inside this pigtail, is the other way to get this reading.
- **Dead kill-switch contacts.** Already known to be degraded: **kill 3 ohm,
  button 5 ohm, 8 ohm in series** `[meter 15 Aug 2026]`, with cleaning a
  planned build step the whole relay scheme depends on. A contact that has gone
  fully open reads the same as one that was never landed.

### The table to finish

Cluster UNPLUGGED from the harness, probing its own three pins:

| State | 1 to 2 | 1 to 3 | 2 to 3 |
|---|---|---|---|
| Kill OFF, button released | | | |
| Kill OFF, button PRESSED | **closed** `[22 Nov 2026]` | | |
| Kill ON, button released | | | |
| Kill ON, button pressed | | | |

**The reading that decides it:** which conductor closes to the brown with the
**kill switch ON and the button released**. That one is the kill-switch output
and belongs on way 2, feeding `K_COIL`; the one that closes only on the button
belongs on way 3, feeding the solenoid.

If **nothing** closes to brown on kill-ON alone, the kill switch's own contacts
are open and re-landing fixes nothing - clean them to the under-1-ohm
acceptance in the `rh_cluster` note and re-read.

### Also not recorded

- **How many conductors are actually in the pigtail**, three or four, and
  whether `SP_RH_BR` is still inside it. The `[OPEN]` above turns on this.
- **Contact resistance after cleaning.** The 15 Aug figures are pre-cleaning.

## Scope note

This is the first file in `measurements/` written against the **built** harness
rather than the old one. Everything else in this directory is archaeology on
what came off the bike; this is a reading on what is on it now.
