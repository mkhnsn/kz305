#!/usr/bin/env python3
"""Where every wire lands, as a PHYSICAL part rather than a node name.

    .venv/bin/python3 tools/landing_map.py > docs/landing-map.md

docs/label-schedule.md already gives both ends of every wire, but it gives
them as `RR-1` and `PDM-5`. At the bench that is not enough: you are holding a
wire and a crimper, and you need to know that `RR-1` is AC1 on the Shindengen
SH775 in the box where the battery used to be, and that `PDM-5` is cavity
c1 r4 on the MTA 0301370.

Everything here is resolved from something that already exists:

  the model          part type, subtype, manufacturer, MPN, pin labels, and
                     the terminals each connector takes
  cut_list.POSITIONS where the part sits, and whether that was measured
  cut_list.cavity_of PDM and relay cavity names
  label_schedule     which cable ends on which connector pin

so this cannot say anything the cut list, the label schedule and the BOM do
not already agree on.

SPLICE FORM IS NOT REPEATED HERE. What each splice physically is - a parallel
crimp, a sealed junction, the stock bullet at B03 - and when it can be crimped
is the cut list's splices section, which is the authority. This map names the
node and points there.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import branch_map as bm  # noqa: E402
import cut_list as cl  # noqa: E402
import label_schedule as ls  # noqa: E402
from build import load  # noqa: E402

DROPBOX_DIR = cl.DROPBOX_DIR

# HOW YOU FIND WAY 1 ON THE PHYSICAL PART. Only where this repo actually
# records it. Everything absent from here has a way numbering that is a list
# order in the model and nothing else - see "Way 1 is not anchored" below.
# A guessed orientation is worse than a blank one: it reads like a fact and
# wires the harness backwards.
ORIENTED = {
    "IGN": "Mating face, keyway up, left to right, top row first — the ways ARE physical cavities.",
    "INSTR_6P": "Mating face, keyway up, top row first, 3 rows of 2; harness side female. "
                "Stock cavity order, read at the bench 29 Aug 2026.",
    "PDM": "The part's own printed numbers, c1–c10 left to right FROM THE WIRE SIDE, top row "
           "first; cavity = (row−1)×10 + column. No keyway. See docs/pdm-cavity-map.md — and note "
           "that from the fuse side, the side facing you on the bike, c10 is on the LEFT.",
}
RELAY_ORIENT = ("Pin numbers are moulded into the relay (30 / 85 / 86 / 87). Its cavities in the "
                "block follow docs/pdm-cavity-map.md.")

# The order convention is harness side FEMALE, component side MALE
# (docs/connector-order.md). These are where a RETAINED part fixes the gender
# instead, so the convention does not hold and the harness side is forced.
GENDER_FORCED = {
    "SOL": "Forced by the relay: its Y/R lead is a FEMALE bullet and its BK a MALE one, so the "
           "harness side is Y/R male and BK female — the one place a harness-side pin is male. "
           "See #65.",
    "ALT": "Bullets on the stator's own stub; gender NOT RECORDED (#65).",
    "CAP_L": "The condenser bracket's pigtail ends in MALE bullets, so the harness side is female.",
    "CAP_R": "The condenser bracket's pigtail ends in MALE bullets, so the harness side is female.",
}

# One node in the model, more than one housing in the hand.
SPLIT_HOUSING = {
    "RR": "TWO HOUSINGS, one node here. Ways 1–3 (AC1/AC2/AC3) are the GREY Furukawa "
          "QLW-A-3F-GR; ways 4–5 (DC+/GND) are the BLACK QLW-A-B3F-B. Colour is the keying — it "
          "is what stops AC being plugged into DC. Each runs 2 of 3 ways and takes a cavity plug. "
          "⚠️ Which cavity of the black housing is DC+ and which is GND is NOT RECORDED.",
}

# A subtype is often "<the part> - <a paragraph about it>". The part is the
# bit before the first dash; the paragraph belongs in the parts table, not in
# a column you scan.
def head(text, limit=46):
    first = str(text or "").split(" - ")[0].strip()
    return first if len(first) <= limit else first[: limit - 1].rstrip() + "…"


def part_short(node, conn):
    """What to call this thing in a table read a hundred times: its part number
    where it has one, otherwise what kind of thing it is. Never the subtype -
    five relays all reading "Song Chuan 303-1AH-C-R1" is noise, and the node
    name beside it is what tells them apart. Full identity is in the parts
    table, once."""
    conn = conn or {}
    mpn = conn.get("mpn")
    if mpn:
        maker = conn.get("manufacturer")
        return f"{maker} {mpn}" if maker else str(mpn)
    return str(conn.get("type") or node)


def part_full(node, conn):
    """The parts-table line: kind, part number, and the head of the subtype."""
    conn = conn or {}
    typ = str(conn.get("type") or node)
    bits = []
    mpn = conn.get("mpn")
    if mpn:
        maker = conn.get("manufacturer")
        bits.append(f"{maker} {mpn}" if maker else str(mpn))
    sub = head(conn.get("subtype"))
    if sub and sub not in bits:
        bits.append(sub)
    return " — ".join([typ] + bits) if bits else typ


def is_splice(conn):
    return str((conn or {}).get("type") or "").lower() == "splice"


def terminal(node, pins, conn):
    """The cavity or pin a wire actually goes into. PDM and relay cavities come
    from the cut list so the two cannot disagree about which hole is which."""
    labels = (conn or {}).get("pinlabels") or []
    out = []
    for p in pins:
        cav = cl.cavity_of(node, p)
        if cav:
            out.append(cav)
            continue
        if isinstance(p, int) and 1 <= p <= len(labels):
            out.append(f"{p} — {labels[p - 1]}")
        else:
            out.append(f"way {p}")
    return " / ".join(out)


def place(node):
    if node not in cl.POSITIONS:
        return "", "", "", ""
    trunk, branch, bas, src = cl.POSITIONS[node]
    return trunk, branch, bas, src


def terminals_for(conn):
    """The terminal parts the model says this connector takes, if any."""
    out = []
    for comp in (conn or {}).get("additional_components") or []:
        if str(comp.get("type") or "").lower().startswith("terminal"):
            maker = comp.get("manufacturer")
            mpn = comp.get("mpn")
            ident = " ".join(x for x in (maker, mpn) if x)
            sub = head(comp.get("subtype"), 70)
            out.append(" — ".join(x for x in (ident, sub) if x))
    return out


def zone(node):
    """Roughly where on the bike, from the trunk breakout the part hangs off.
    Names come from branch_map.PLACE so the two drawings agree."""
    if node not in cl.POSITIONS:
        return ""
    trunk, branch, _, _ = cl.POSITIONS[node]
    place = bm.PLACE.get(trunk)
    if not place:
        return f"{trunk} mm along the trunk"
    return f"{place}, {branch} mm out" if branch else place


def ways_of(node, conn, landings):
    """Declared ways, and the conductors landing on them. They differ where one
    landing legitimately takes two leads - GND's SIGNAL BUS stud is the case -
    so both are shown rather than one being quietly wrong."""
    declared = len((conn or {}).get("pinlabels") or []) or None
    return declared, len(landings.get(node) or [])


def needs_anchor(node, conn, declared):
    """A single conductor has no pinout to get wrong. Everything else does,
    and the risk rises with the way count."""
    if str((conn or {}).get("type") or "").lower() == "splice":
        return False
    if (declared or 0) <= 1:
        return False
    return orientation(node, conn) is None


def orientation(node, conn):
    if node in ORIENTED:
        return ORIENTED[node]
    if str((conn or {}).get("type") or "").lower() == "relay":
        return RELAY_ORIENT
    return None


# The sealed-090 order convention governs exactly the four housings that order
# buys both halves of. It says nothing about a Furukawa pair sold as a mating
# set, or an MTA block, or a bullet whose gender a retained part already fixed -
# so it is not quoted at them.
HW090_ORDER = {"RH", "LH", "INSTR_6P", "IGN"}
GENDER_BY_PART = {
    "RR": "Fixed by the part - the Furukawa QLW housings mate as sold, grey to grey and black to "
          "black. The 090 order convention does not reach this one.",
    "PDM": "Fixed by the part - MTA sealed 2.8mm terminals into the block's own cavities.",
    "MF": "Fixed by the part - Metri-Pack 630 pull-to-seat, terminals into the holder.",
    "MF_RR": "Fixed by the part - Metri-Pack 630 pull-to-seat, terminals into the holder.",
    "MF_TDR": "Fixed by the part - Metri-Pack 630 pull-to-seat, terminals into the holder.",
}


def gender(node, conn):
    if node in GENDER_FORCED:
        return GENDER_FORCED[node]
    if node in GENDER_BY_PART:
        return GENDER_BY_PART[node]
    if str((conn or {}).get("type") or "").lower() == "relay":
        return "Fixed by the part - the relay's blades into its cavities in the block."
    if node in HW090_ORDER:
        return ("Harness side FEMALE, component side MALE - docs/connector-order.md, so a "
                "disconnected harness has no exposed live pin.")
    return None


def collect(doc):
    """node -> [(wire, pins, colour, gauge, far_node, far_pins)], built wires only."""
    cables = doc["cables"]
    landings = {}
    for name, ln, lp, rn, rp in ls.ends(doc.get("connections", []), cables):
        cab = cables.get(name) or {}
        if cab.get("ignore_in_bom"):
            continue
        if "DO NOT BUILD" in str(cab.get("notes") or ""):
            continue
        colours = cab.get("colors") or []
        colour = colours[0] if colours else ""
        gauge = cab.get("gauge") or ""
        for near, npins, far, fpins in ((ln, lp, rn, rp), (rn, rp, ln, lp)):
            landings.setdefault(near, []).append(
                (name, npins, colour, gauge, far, fpins))
    return landings


def main():
    doc = load(cl.REBUILD, cl.COMMON.read_text(encoding="utf-8"))
    conns = doc.get("connectors") or {}
    landings = collect(doc)

    o = []
    w = o.append
    w("# Landing map — rebuild harness\n")
    w("Generated by `tools/landing_map.py`. Do not edit by hand.\n")
    w("`docs/label-schedule.md` gives both ends of every wire as `RR-1` and `PDM-5`. "
      "This resolves those to the **physical part and the hole in it**: what the thing is, "
      "what its MPN is, which cavity, and where it sits on the bike.\n")
    w("Positions and cavity names come from `tools/cut_list.py`, the part identity and pin "
      "labels from the model, so this cannot disagree with the cut list, the label schedule "
      "or the BOM.\n")
    w("⚠️ **A splice's physical form is not repeated here.** What each `SP_` node actually is "
      "— a parallel crimp, a sealed junction, the stock bullet at B03 — and when it can be "
      "crimped is the **splices section of `docs/cut-list.md`**, which is the authority.\n")

    # ---- the parts -----------------------------------------------------
    w("## The parts\n")
    w("Every node a wire lands on. `Where` is mm from the headlight datum, then mm out "
      "along the branch. `Basis` is `tape` where both were measured on the old harness "
      "and `est` where the part is placed by where it sits.\n")
    w("| Node | What it physically is | Where | Basis | Lands |")
    w("|---|---|---|---|---|")
    for node in sorted(landings):
        conn = conns.get(node) or {}
        trunk, branch, bas, src = place(node)
        what = part_full(node, conn)
        if is_splice(conn):
            what += " — form and crimp order in the cut list"
        where = f"{trunk} mm, {branch} out" if trunk != "" else "—"
        src_txt = f"<br>*{src}*" if src else ""
        w(f"| `{node}` | {what}{src_txt} | {where} | {bas or '—'} | {len(landings[node])} |")
    w("")

    # ---- terminals the model names --------------------------------------
    rows = []
    for node in sorted(landings):
        for t in terminals_for(conns.get(node)):
            rows.append((node, t))
    if rows:
        w("### What to crimp on\n")
        w("Only where the model names a terminal. Everything else takes the sealed 090 "
          "terminal that ships with its housing — `docs/connector-order.md`.\n")
        w("| Node | Terminal |")
        w("|---|---|")
        for node, t in rows:
            w(f"| `{node}` | {t} |")
        w("")

    # ---- by wire ---------------------------------------------------------
    w("## Every wire, both ends\n")
    w("`W_` prefixes are dropped, as on the labels.\n")
    w("| Wire | Colour | Gauge | Lands on | In | And on | In |")
    w("|---|---|---|---|---|---|---|")
    # Which end is listed first is alphabetical by node - stable, and it does
    # not matter: both ends are on the row.
    by_wire = {}
    for node, items in landings.items():
        for name, npins, colour, gauge, far, fpins in items:
            by_wire.setdefault(name, {})[node] = (npins, colour, gauge, far, fpins)
    for name in sorted(by_wire):
        pairs = sorted(by_wire[name])
        a_node = pairs[0]
        npins, colour, gauge, far, fpins = by_wire[name][a_node]
        b_node = far
        a_conn, b_conn = conns.get(a_node) or {}, conns.get(b_node) or {}
        w(f"| `{ls.short(name)}` | {colour} | {gauge} "
          f"| `{a_node}` {part_short(a_node, a_conn)} | {terminal(a_node, npins, a_conn)} "
          f"| `{b_node}` {part_short(b_node, b_conn)} | {terminal(b_node, fpins, b_conn)} |")
    w("")

    # ---- by component ----------------------------------------------------
    w("## By component — the pinout of each part, and where it sits\n")
    w("Stand at one part: what it is, roughly where on the bike, which way is which, and "
      "everything that arrives there.\n")

    need = []
    for node in sorted(landings):
        conn = conns.get(node) or {}
        declared, _ = ways_of(node, conn, landings)
        if needs_anchor(node, conn, declared):
            need.append((declared or 0, node))
    need.sort(reverse=True)

    w("⚠️ **WAY 1 IS ANCHORED ON FOUR OF THESE AND NOWHERE ELSE.** `IGN` and `INSTR_6P` by a "
      "keyway, `PDM` by its printed numbers, the relays by the pin numbers moulded into them. On "
      "every other multi-way connector the numbering below is **this model's list order and "
      "nothing else** — no keyway, latch or printed number has been recorded for it. For the "
      "housings we fit ourselves that numbering is ours to define, but it still has to be "
      "defined against a feature you can see, and that has not been done.\n")
    w("**Pick a feature, write it down, then crimp.** Nothing here is guessed, which is why the "
      "line says nothing rather than something plausible. A single-conductor node has no pinout "
      "to get wrong and is not counted below.\n")
    w("Needing an anchor, worst first — the more ways, the more ways to be wrong:\n")
    w("| Ways | Node | Part |")
    w("|---|---|---|")
    for ways, node in need:
        w(f"| **{ways}** | `{node}` | {part_short(node, conns.get(node) or {})} |")
    w("")

    w("### Every connector\n")
    w("**Ways** is what the model declares; **wires** is what lands. They differ where one "
      "landing takes two leads — `GND`'s SIGNAL BUS stud is the case, not an error.\n")
    w("| Node | Part | Ways | Wires | Roughly where | Way 1 |")
    w("|---|---|---|---|---|---|")
    for node in sorted(landings):
        conn = conns.get(node) or {}
        if str(conn.get("type") or "").lower() == "splice":
            continue
        declared, wired = ways_of(node, conn, landings)
        if node == "PDM":
            ways_txt = "60 cavities"
            wired_txt = f"{wired} here + 20 under the relays"
        else:
            ways_txt = str(declared) if declared else "—"
            wired_txt = str(wired)
        if orientation(node, conn):
            flag = "✅ anchored"
        elif (declared or 0) <= 1:
            flag = "— single conductor"
        else:
            flag = "⚠️ not anchored"
        w(f"| `{node}` | {part_short(node, conn)} | {ways_txt} | {wired_txt} "
          f"| {zone(node) or '—'} | {flag} |")
    w("")
    w("Splices are left out of that table — they have no pinout, and the cut list's splices "
      "section is the authority on what each one physically is.\n")
    for node in sorted(landings):
        conn = conns.get(node) or {}
        trunk, branch, bas, src = place(node)
        w(f"### `{node}` — {part_full(node, conn)}\n")
        if conn.get("subtype"):
            w(str(conn["subtype"]) + "\n")
        if src:
            z = zone(node)
            where = f"**{z}.** " if z else ""
            w(f"{where}Harness geometry: {trunk} mm from the datum, {branch} mm out ({bas}) — "
              f"{src}.\n")
        if node in SPLIT_HOUSING:
            w("⚠️ " + SPLIT_HOUSING[node] + "\n")
        g = gender(node, conn)
        if g:
            w(f"**Gender:** {g}\n")
        how = orientation(node, conn)
        if how:
            w(f"**Way 1:** {how}\n")
        elif str(conn.get("type") or "").lower() != "splice":
            w("⚠️ **Way 1 is not anchored** — the numbering below is this model's list order, not "
              "a physical feature of the part. Fix it to something visible before crimping.\n")
        w("| In | Wire | Colour | Gauge | Comes from |")
        w("|---|---|---|---|---|")
        items = sorted(landings[node], key=lambda r: (terminal(node, r[1], conn), r[0]))
        for name, npins, colour, gauge, far, fpins in items:
            far_conn = conns.get(far) or {}
            w(f"| {terminal(node, npins, conn)} | `{ls.short(name)}` | {colour} | {gauge} "
              f"| `{far}` {part_short(far, far_conn)} |")
        w("")

    text = "\n".join(o)
    print(text)

    if DROPBOX_DIR.is_dir():
        (DROPBOX_DIR / "landing-map.md").write_text(text + "\n", encoding="utf-8")
        print(f"copied the landing map to {DROPBOX_DIR}", file=sys.stderr)
    else:
        print(f"no {DROPBOX_DIR} - landing map not copied", file=sys.stderr)


if __name__ == "__main__":
    main()
