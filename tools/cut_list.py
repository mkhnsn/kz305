#!/usr/bin/env python3
"""Cut list for the rebuild harness, bench end first.

    .venv/bin/python3 tools/cut_list.py > docs/cut-list.md

The model carries no lengths by design: the harness is built in place and
trimmed on the bike. What CAN be fixed at the bench is the PDM end - label,
seal and crimp happen there, and once a terminal is in a cavity the wire is
cut. So every wire needs a length to cut to BEFORE its first crimp, long
enough that the far end can still be trimmed on the bike.

Lengths come from the 28 Aug 2026 branch map (measurements/harness-lengths.csv,
measurements/trunk-map.md): every branch has a breakout distance from the
headlight datum along the trunk, and a branch length off the trunk. A wire's
route is the trunk distance between its two nodes' breakouts plus both branch
lengths. The PDM's breakout is 835 mm - the B06 fan-out, where the old fuse
box, starter relay and main feed left the trunk, beside the battery. Decided
15 Sep 2026. The PDM, the ATZ-7 and the regulator all sit in the old battery
box - decided 17 Sep 2026.

Node positions live in POSITIONS below, each with a basis tag. `tape` means
both the breakout and the branch were measured on the old harness; `est`
means a node the old harness did not have, or one whose lead length was not
taped, placed by where the part sits on the bike. Correct an `est` row here
when the part is mounted and re-run.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build import load  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
COMMON = ROOT / "models" / "kz305-common.yml"
REBUILD = ROOT / "models" / "kz305-rebuild.yml"

PDM_TRUNK_MM = 835  # B06 breakout - decided 15 Sep 2026

# Margin per wire, on top of the routed length. The PDM end is crimped at the
# bench and cannot move; the far end is trimmed on the bike. The build starts
# on the bench with nothing mounted, so the margin is loose: 500 mm covers a
# different path round the tank, a part that lands somewhere other than the
# table assumes, and a re-crimp at the far end. A wire whose two ends sit
# together at the PDM (route 0) is a bench jumper and gets MIN_CUT_MM only.
MARGIN_MM = 500
# Nothing is cut shorter than this, however short the route: a wire needs
# enough length to label, seal, crimp and dress.
MIN_CUT_MM = 300
ROUND_MM = 50

# node: (trunk_mm from the headlight datum, branch_mm off the trunk, basis, source)
P = PDM_TRUNK_MM
POSITIONS = {
    # --- at the PDM / battery, 835 mm ---------------------------------
    "PDM":      (P,    0,   "tape", "B06 fan-out"),
    "SP_HOT":   (P,    0,   "est",  "beside the PDM"),
    "SP_SW":    (P,    0,   "est",  "beside the PDM"),
    "SP_RLY":   (P,    0,   "est",  "beside the PDM"),
    "SP_HEAD":  (P,    0,   "est",  "beside the PDM - F5 out to both beam relays"),
    "SP_GND":   (P,    0,   "est",  "beside the PDM"),
    "K_MAIN":   (P,    0,   "tape", "in the PDM"),
    "K_COIL":   (P,    0,   "tape", "in the PDM"),
    "K_HORN":   (P,    0,   "tape", "in the PDM"),
    "K_HI":     (P,    0,   "tape", "in the PDM"),
    "K_LO":     (P,    0,   "tape", "in the PDM"),
    "MF":       (P,    150, "tape", "B06.3 / SOL.2 - between relay and PDM"),
    "SOL":      (P,    100, "tape", "B06.1 / B06.2 relay leads"),
    "BATT":     (P,    150, "tape", "SOL.1 battery cable"),
    "RR":       (P,    200, "est",  "in the old battery box with the PDM and battery - decided 17 Sep 2026"),
    "MF_RR":    (P,    150, "est",  "at the battery end of the charging pair"),
    "MF_TDR":   (P,    150, "est",  "at the battery positive post"),
    "SAE":      (P,    300, "est",  "capped under the side cover"),
    "GND":      (P,    200, "est",  "star bus plate - NOT PLACED, see blocker 2"),
    "USB":      (P,    300, "est",  "NOT PLACED - assumed under the seat"),
    "SM":       (P,    400, "est",  "starter motor terminal"),
    "GND_ENG":  (P,    400, "est",  "engine case bolt"),
    # --- headlight shell, datum 0 --------------------------------------
    "IGN":      (0,    100, "tape", "B00.3"),
    "INSTR_6P": (0,    100, "tape", "B00.1"),
    "HEAD":     (0,    100, "tape", "B00.9"),
    "FBRK":     (0,    100, "tape", "B00.5 / B00.6 - the switch's own pigtail comes down to the shell"),
    "SP_HI":    (0,    0,   "tape", "in the shell"),
    "SP_TAIL":  (0,    0,   "tape", "in the shell"),
    "SP_INSTR": (0,    0,   "tape", "in the shell"),
    "SP_MTR":   (0,    0,   "tape", "in the shell"),
    "SP_SIG_L": (0,    0,   "tape", "in the shell"),
    "SP_SIG_R": (0,    0,   "tape", "in the shell"),
    "LAMP_SPD": (0,    250, "est",  "meter lamp, pod"),
    "LAMP_TAC": (0,    250, "est",  "meter lamp, pod"),
    "SIG_FL":   (0,    300, "est",  "front signal stalk"),
    "SIG_FR":   (0,    300, "est",  "front signal stalk"),
    # --- bars ---------------------------------------------------------
    "RH":       (400,  160, "tape", "B01.2"),
    "HORN":     (400,  260, "tape", "B01.3"),
    "NSW":      (400,  900, "tape", "B01.4"),
    "LH":       (430,  200, "tape", "B02.3"),
    # --- under the tank -----------------------------------------------
    "SP_YR":    (460,  140, "tape", "B03"),
    "COIL_L":   (460,  300, "est",  "coil, from B03"),
    "COIL_R":   (460,  300, "est",  "coil, from B03"),
    "CAP_L":    (650,  300, "est",  "condenser at the points cover"),
    "SP_BRK_FEED": (650, 0, "est",  "B04 breakout"),
    "SP_BRAKE": (650,  0,   "est",  "B04 breakout, B04.2 blue merge"),
    "RBRK":     (650,  300, "est",  "rear brake switch, frame mounted"),
    "ALT":      (730,  320, "tape", "B05 + B05.1"),
    # --- rear ---------------------------------------------------------
    "FLASHER":  (880,  100, "tape", "B07"),
    "TAIL":     (1360, 250, "est",  "B10 fan + tail lamp lead"),
    "SIG_RL":   (1360, 350, "est",  "B10 fan + rear signal stalk"),
    "SIG_RR":   (1360, 350, "est",  "B10 fan + rear signal stalk"),
}

# PDM way -> cavity, from docs/pdm-cavity-map.md. cavity = (row-1)*10 + col.
PDM_CAVITY = {
    14: "c1 r1 (F1 IN)",   2: "c1 r2 (F1 OUT)",
    15: "c1 r3 (F4 IN)",   5: "c1 r4 (F4 OUT)",
    16: "c1 r5 (F5 IN)",   6: "c1 r6 (F5 OUT)",
    17: "c7 r1 (F2 IN)",   3: "c7 r2 (F2 OUT)",
    18: "c7 r3 (F3 IN)",   4: "c7 r4 (F3 OUT)",
    19: "c7 r5 (F6 IN)",   7: "c7 r6 (F6 OUT)",
    20: "c8 r1 (F7 IN)",  11: "c8 r2 (F7 OUT)",
    21: "c8 r3 (F8 IN)",  12: "c8 r4 (F8 OUT)",
    22: "c8 r5 (F9 IN)",  13: "c8 r6 (F9 OUT)",
    24: "c9 r1 (F10 IN)", 23: "c9 r2 (F10 OUT)",
    26: "c9 r3 (F11 IN)", 25: "c9 r4 (F11 OUT)",
}
# relay: (row, col) of its upper-left cavity; pins [30, 87, 86, 85] sit at
# (r,c) (r+1,c+1) (r,c+1) (r+1,c) - the diagonal rule in the cavity map.
RELAY_ORIGIN = {"K_MAIN": (1, 3), "K_LO": (1, 5), "K_HI": (3, 3),
                "K_COIL": (5, 3), "K_HORN": (5, 5)}
RELAY_PIN_OFFSET = {1: (0, 0), 2: (1, 1), 3: (0, 1), 4: (1, 0)}
RELAY_PIN_NAME = {1: "30", 2: "87", 3: "86", 4: "85"}


def cavity_of(node, pin):
    if node == "PDM":
        return PDM_CAVITY.get(pin, f"way {pin}")
    if node in RELAY_ORIGIN:
        r0, c0 = RELAY_ORIGIN[node]
        dr, dc = RELAY_PIN_OFFSET[pin]
        return f"c{c0 + dc} r{r0 + dr} ({node} {RELAY_PIN_NAME[pin]})"
    return None


def route_mm(a, b):
    ta, ba, _, _ = POSITIONS[a]
    tb, bb, _, _ = POSITIONS[b]
    return abs(ta - tb) + ba + bb


def basis(a, b):
    return "tape" if POSITIONS[a][2] == "tape" and POSITIONS[b][2] == "tape" else "est"


def round_up(mm):
    return int(math.ceil(mm / ROUND_MM) * ROUND_MM)


def ends(doc):
    cables = doc.get("cables") or {}
    out = {}
    for conn_set in doc.get("connections") or []:
        e = [x for x in conn_set if isinstance(x, dict)]
        for i, x in enumerate(e):
            name = next(iter(x))
            if name not in cables:
                continue
            left = next(iter(e[i - 1].items())) if i > 0 else None
            right = next(iter(e[i + 1].items())) if i + 1 < len(e) else None
            out.setdefault(name, []).append((left, right))
    return out


def main():
    common = COMMON.read_text(encoding="utf-8")
    doc = load(REBUILD, common)
    cables = doc["cables"]
    cable_ends = ends(doc)

    rows = []
    missing = set()
    for name, cable in cables.items():
        cable = cable or {}
        if cable.get("ignore_in_bom"):
            continue
        notes = str(cable.get("notes") or "")
        if "DO NOT BUILD" in notes:
            continue
        for left, right in cable_ends.get(name, []):
            if not left or not right:
                continue
            (a, pa), (b, pb) = left, right
            if a not in POSITIONS or b not in POSITIONS:
                missing.update(n for n in (a, b) if n not in POSITIONS)
                continue
            gauge = cable.get("gauge", "?")
            colour = "/".join(cable.get("colors") or [])
            route = route_mm(a, b)
            heavy = gauge == "6 AWG"
            if heavy:
                cut = None
            elif route == 0:
                cut = MIN_CUT_MM
            else:
                cut = round_up(route + MARGIN_MM)
            cav = cavity_of(a, pa[0]) or cavity_of(b, pb[0])
            near, far = (a, b) if cavity_of(a, pa[0]) else (b, a)
            # a jumper with both ends in the block: name the second cavity too
            if cavity_of(a, pa[0]) and cavity_of(b, pb[0]):
                far = cavity_of(b, pb[0])
            rows.append(dict(name=name, gauge=gauge, colour=colour, near=near,
                             far=far, cavity=cav, route=route, cut=cut,
                             basis=basis(a, b), heavy=heavy))
    if missing:
        sys.exit(f"nodes with no position: {sorted(missing)}")

    pdm = [r for r in rows if r["cavity"]]
    rest = [r for r in rows if not r["cavity"] and not r["heavy"]]
    heavy = [r for r in rows if r["heavy"]]

    def cav_key(r):
        c = r["cavity"]
        col = int(c[1:c.index(" ")])
        row = int(c[c.index("r") + 1:c.index(" (")])
        return (col, row)

    pdm.sort(key=cav_key)
    rest.sort(key=lambda r: (r["near"], r["name"]))

    out = []
    w = out.append
    w("# Cut list — rebuild harness\n")
    w("Generated by `tools/cut_list.py`. Do not edit by hand.\n")
    w(f"**PDM breakout: {PDM_TRUNK_MM} mm from the headlight datum**, the old B06 "
      "fan-out beside the battery. Decided 15 Sep 2026. The PDM, the battery and "
      "the regulator all sit in the old battery box. Decided 17 Sep 2026.\n")
    w("Every length is **route + margin, rounded up to 50 mm**, and the route is "
      "the 28 Aug branch map: trunk distance between the two ends plus each "
      "end's branch off the trunk. The PDM or relay end is crimped at the bench "
      "and does not move; **the far end is trimmed on the bike**, which is what "
      f"the {MARGIN_MM} mm margin is for - loose, because the build starts on the "
      "bench with nothing mounted. A wire with both ends at the PDM (route 0) is "
      f"a bench jumper and is cut to {MIN_CUT_MM} mm.\n")
    w("**Basis:** `tape` — both ends were measured on the old harness. `est` — "
      "at least one end is a part the old harness did not have, or one whose "
      "lead was not taped, placed by where it sits on the bike. The `est` rows "
      "carry the same margin; if a part ends up far from where the table assumes, "
      "fix `POSITIONS` in the tool and re-run before cutting that wire.\n")
    w("⚠️ **Cut one wire, label it, seal it, crimp the PDM end, then cut the "
      "next.** A cut wire with no label is the one that gets mixed up.\n")

    w("## PDM and relay cavities — cut before the bench crimp\n")
    w(f"{len(pdm)} wires, in cavity order, column by column.\n")
    w("| Cavity | Wire | Colour | Gauge | Far end | Route | **Cut** | Basis |")
    w("|---|---|---|---|---|---|---|---|")
    for r in pdm:
        w(f"| {r['cavity']} | `{r['name']}` | {r['colour']} | {r['gauge']} | "
          f"{r['far']} | {r['route']} | **{r['cut']}** | {r['basis']} |")
    w("")

    w("## Everything else — cut when the near end is terminated\n")
    w(f"{len(rest)} wires. Same rule: cut to this, crimp the near end, trim the far "
      "end on the bike.\n")
    w("| Wire | Colour | Gauge | From | To | Route | **Cut** | Basis |")
    w("|---|---|---|---|---|---|---|---|")
    for r in rest:
        w(f"| `{r['name']}` | {r['colour']} | {r['gauge']} | {r['near']} | {r['far']} | "
          f"{r['route']} | **{r['cut']}** | {r['basis']} |")
    w("")

    w("## Heavy cable — not cut at the bench\n")
    w("Bought long, cut on the bike with both lugs' landings in front of you. "
      "Route shown for ordering only.\n")
    w("| Wire | Colour | From | To | Route | Basis |")
    w("|---|---|---|---|---|---|")
    for r in heavy:
        w(f"| `{r['name']}` | {r['colour']} | {r['near']} | {r['far']} | {r['route']} | {r['basis']} |")
    w("")

    # stock check
    w("## Stock check — cut totals against the spools\n")
    totals = {}
    for r in pdm + rest:
        key = (r["gauge"], r["colour"])
        totals[key] = totals.get(key, 0) + r["cut"]
    stock_ft = {("16 AWG", "BG"): 100, ("16 AWG", "BK"): 100, ("16 AWG", "YE"): 50,
                ("16 AWG", "BU"): 50, ("16 AWG", "GN"): 50, ("16 AWG", "GY"): 50,
                ("16 AWG", "RD"): 15, ("14 AWG", "WH"): 10, ("12 AWG", "RD"): 12,
                ("12 AWG", "BK"): 10, ("14 AWG", "YE/YE"): 8}
    w("| Gauge | Colour | Cut total | Spool | Left |")
    w("|---|---|---|---|---|")
    for (g, c), mm in sorted(totals.items()):
        ft = stock_ft.get((g, c))
        m = mm / 1000
        if ft is None:
            w(f"| {g} | {c} | {m:.1f} m | ? | ? |")
        else:
            spool_m = ft * 0.3048
            flag = " ⚠️" if spool_m - m < 1 else ""
            w(f"| {g} | {c} | {m:.1f} m | {ft} ft ({spool_m:.1f} m) | {spool_m - m:.1f} m{flag} |")
    w("")
    print("\n".join(out))


if __name__ == "__main__":
    main()
