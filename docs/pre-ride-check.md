# Pre-ride check

## Stop the engine both ways — every ride

With the engine running:

1. **Kill switch to OFF.** The engine must stop. Kill switch back to RUN.
2. Restart. **Key to OFF.** The engine must stop.

Both have to work **on their own**.

**Why:** there is no mechanical break in the ignition power any more. The kill
switch drives `K_COIL`, and the key drives `K_MAIN`, and the engine stops only
when one of those relay contacts opens. One welded relay is harmless because
the other method still works, but you only notice it if you use that other
method. A weld in the one you don't normally use sits there unnoticed until the
second relay welds too, and then nothing electrical stops the engine short of
pulling F3. This check finds the first weld while it's still harmless.

**If either one fails:** don't ride. Pull the relay for the method that
failed (`K_COIL` for the kill switch, `K_MAIN` for the key) and fit the spare.

**Last resort, if both have failed while riding:** clutch in, brake to a stop,
then let the clutch out in gear to stall it.

## A horn or headlight beam that won't switch off

That relay has welded (`K_HORN`, `K_HI` or `K_LO`). The key won't clear it,
because F4 and F5 are fed hot. **Pull that relay from the PDM and fit the
spare.** Don't pull F4 or F5: F5 feeds both beams.

**Carry a spare relay:** Song Chuan `303-1AH-C-R1`, the resistor type. Check it
with a DMM both ways round across 85/86 before relying on it. A diode relay
reads differently in each direction and shorts if fitted backwards. See
`docs/part-selection.md`, *Coil suppression*.
