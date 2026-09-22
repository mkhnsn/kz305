#!/usr/bin/env python3
"""Draw the rebuild harness by BRANCH rather than by circuit: what shares a
trunk segment, what leaves at each breakout, and how thick the bundle is.

    .venv/bin/python3 tools/branch_map.py       > docs/branch-map.md
    .venv/bin/python3 tools/branch_map.py --svg > docs/branch-map.svg

The WireViz drawings are schematics - they say what connects to what and
deliberately say nothing about physical routing. This is the other view: the
one you need to cut sleeve and tape a loom, which is entirely about where each
wire runs and what it runs beside.

Node positions come from tools/cut_list.py POSITIONS, and the wires from the
model, so this cannot drift from the cut list. A node placed `est` there is
`est` here, and a segment carrying one is marked.

Every conductor is placed on the trunk by its two ends: a wire between two
nodes occupies the trunk between their breakouts, and the bundle at any point
is every wire whose span covers it. A wire with both ends at one breakout -
the PDM jumpers, the headlight-shell splices - never enters the trunk and is
counted in that breakout's drop instead.
"""

import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import cut_list as cl  # noqa: E402
from build import load  # noqa: E402

DROPBOX_DIR = cl.DROPBOX_DIR

# Insulation OD, mm. Both are in the repo: 16 AWG TXL was calipered 2.20-2.21
# at four points (docs/part-selection.md, 10 Sep); 14 AWG TXL is 2.59-2.70 and
# the worst case is taken. W_ALT is the one non-TXL run - M22759/16 ETFE at
# 2.36, a thinner wall (docs/prowire-order.md).
OD_MM = {"16 AWG": 2.21, "14 AWG": 2.70, "12 AWG": None, "6 AWG": None}
OD_OVERRIDE = {"W_ALT": 2.36}

# Bundle OD is ESTIMATED, not measured: D = d * sqrt(N / PACKING) for N round
# conductors of diameter d, the usual approximation for a randomly packed
# round bundle. Mixed gauges go in by area. Change PACKING here if a real
# bundle measures differently - nothing downstream hard-codes it.
PACKING = 0.75

# Expanded diameters: only 1/4" is recorded - "about 9.5 mm, which covers up to
# roughly 8 conductors" (docs/prowire-order.md). The 1/2" and 3/4" bounds below
# are back-read from that document's own sizing of the old harness (9 mm to
# 1/2", 14-15 mm to 3/4") and are NOT vendor figures. Measure before trusting
# either at its limit.
SLEEVE = [(9.5, '1/4"'), (13.0, '1/2"'), (19.0, '3/4"')]


# What is at each trunk position, for a heading a human can read. Sources are
# measurements/trunk-map.md's breakout table and the POSITIONS entries.
PLACE = {
    0:    "the headlight junction (datum)",
    400:  "right bar",
    430:  "left bar",
    460:  "coil splice, under the tank",
    650:  "brakes and condenser",
    730:  "alternator",
    835:  "PDM, battery, regulator",
    880:  "flasher",
    1360: "the tail fan, where the trunk ends",
}

# What was bought, docs/prowire-order.md section 5, so the table can check
# itself against the order rather than leaving the reader to.
SLEEVE_ORDERED_FT = {'1/4"': 35, '1/2"': 10, '3/4"': 10}


def sleeve_for(od_mm):
    """Sized on the DISPLAYED diameter, so the table cannot show 13.0 mm
    against a sleeve the next row up."""
    od_mm = round(od_mm, 1)
    for bound, size in SLEEVE:
        if od_mm <= bound:
            return size
    return f'over 3/4" - {od_mm:.1f} mm'


def od_of(name, gauge):
    if name in OD_OVERRIDE:
        return OD_OVERRIDE[name]
    return OD_MM.get(gauge)


def bundle_od(members):
    """Estimated bundle OD from a list of (name, gauge). None if any conductor
    has no recorded OD - a guessed diameter is worse than an absent one."""
    area = 0.0
    for name, gauge in members:
        d = od_of(name, gauge)
        if d is None:
            return None, None
        area += 3.141592653589793 * (d / 2) ** 2
    if not area:
        return 0.0, 0.0
    od = 2 * (area / PACKING / 3.141592653589793) ** 0.5
    return area, od


def wire_spans(doc):
    """name -> (trunk_lo, trunk_hi, [nodes], gauge, colour) for every wire that
    gets built. Retained pigtails and the withdrawn W_SOL_GND are left out -
    they are not wire this harness cuts."""
    cables = doc["cables"]
    cable_ends = cl.ends(doc)
    out, unplaced = {}, {}
    for name, cable in cables.items():
        cable = cable or {}
        if cable.get("ignore_in_bom"):
            continue
        if "DO NOT BUILD" in str(cable.get("notes") or ""):
            continue
        nodes = sorted({s[0] for l, r in (cable_ends.get(name) or [])
                        for s in (l, r) if s})
        if not nodes:
            continue
        missing = [n for n in nodes if n not in cl.POSITIONS]
        if missing:
            unplaced[name] = missing
            continue
        trunk = [cl.POSITIONS[n][0] for n in nodes]
        colours = cable.get("colors") or []
        out[name] = (min(trunk), max(trunk), nodes,
                     cable.get("gauge"), colours[0] if colours else "")
    return out, unplaced


def breakouts(spans):
    """Every trunk position that has something at it, with the nodes there."""
    pts = {}
    for lo, hi, nodes, _, _ in spans.values():
        for n in nodes:
            pts.setdefault(cl.POSITIONS[n][0], set()).add(n)
    return dict(sorted(pts.items()))


def segments(spans, pts):
    """Between each pair of adjacent breakouts, the wires running through."""
    marks = sorted(pts)
    out = []
    for a, b in zip(marks, marks[1:]):
        members = sorted(n for n, (lo, hi, *_) in spans.items() if lo <= a and hi >= b)
        out.append((a, b, members))
    return out


def drops(spans, pts):
    """At each breakout, the wires leaving the trunk there, by node. A wire
    counts at both of its ends."""
    out = {}
    for mm, nodes in pts.items():
        per_node = {}
        for n in sorted(nodes):
            members = sorted(k for k, v in spans.items() if n in v[2])
            if members:
                per_node[n] = members
        out[mm] = per_node
    return out


def md(doc, spans, pts, segs, drop):
    o = []
    w = o.append
    w("# Branch map — rebuild harness\n")
    w("Generated by `tools/branch_map.py`. Do not edit by hand.\n")
    w("The WireViz drawings are **schematics** — they say what connects to what and "
      "deliberately say nothing about physical routing. This is the other view, and it is "
      "the one the build needs: **which wires travel together**, so a branch can be cut, "
      "sleeved and taped as a unit.\n")
    w("Positions are `tools/cut_list.py`'s `POSITIONS`, so this cannot drift from the cut "
      "list. A wire is placed on the trunk by its two ends and occupies everything between "
      "them; a wire with both ends at one breakout never enters the trunk and is counted "
      "only in that breakout's drop.\n")
    w("⚠️ **Conductor counts are exact; diameters are not.** The count is from the model. "
      f"The OD is estimated as `D = d × √(N / {PACKING})` from the recorded insulation ODs "
      "— 16 AWG TXL calipered **2.20–2.21 mm**, 14 AWG TXL **2.59–2.70** (worst case taken), "
      "`W_ALT` **2.36** as the one ETFE run. Measure a real bundle before trusting a sleeve "
      "at its limit.\n")

    peak = max(segs, key=lambda s: len(s[2]))
    w("## The trunk\n")
    w(f"**Peak: {len(peak[2])} conductors between {peak[0]} and {peak[1]} mm** — immediately "
      "before the PDM breakout, where everything from the front and the bars has gathered "
      "and nothing has left yet. The trunk is thickest at its back end, not its front.\n")
    w("| From | To | Conductors | Area mm² | Est. OD | Sleeve |")
    w("|---|---|---|---|---|---|")
    for a, b, members in segs:
        pairs = [(m, spans[m][3]) for m in members]
        area, od = bundle_od(pairs)
        if od is None:
            w(f"| {a} | {b} | {len(members)} | ? | ? | ? |")
        else:
            w(f"| {a} | {b} | **{len(members)}** | {area:.0f} | {od:.1f} mm | {sleeve_for(od)} |")
    w("")

    need = {}
    for a, b, members in segs:
        pairs = [(m, spans[m][3]) for m in members]
        _, od = bundle_od(pairs)
        if od is None:
            continue
        need[sleeve_for(od)] = need.get(sleeve_for(od), 0) + (b - a)
    w("### Against the order\n")
    w("Trunk only — the branch drops are almost all 1/4\" and are counted in "
      "`docs/prowire-order.md`, which sized them off the old harness's 50 branches.\n")
    w("| Sleeve | Trunk run | Ordered | |")
    w("|---|---|---|---|")
    for size in ['1/4"', '1/2"', '3/4"']:
        mm_needed = need.get(size, 0)
        ft = SLEEVE_ORDERED_FT.get(size, 0)
        ok = "✅" if ft * 304.8 >= mm_needed else "⚠️ short"
        w(f"| {size} | {mm_needed} mm ({mm_needed / 304.8:.1f} ft) | {ft} ft | {ok} |")
    w("")
    w("⚠️ **This splits the front differently from that document**, which put the whole "
      "front on 3/4\". The bundle does not reach 3/4\" until the right bar joins it at "
      "400 mm: datum to right bar is 20 conductors, which is 1/2\" work. Sleeving it 3/4\" "
      "would leave the headlight run loose in its sleeve.\n")

    w("## What leaves at each breakout\n")
    w("Wires are listed at **both** ends, so a wire from the headlight shell to the PDM "
      "appears at 0 mm and at 835 mm. `W_` prefixes are dropped.\n")
    for mm in sorted(drop):
        per_node = drop[mm]
        total = len({m for ms in per_node.values() for m in ms})
        label = PLACE.get(mm) or ", ".join(sorted(per_node))
        w(f"### {mm} mm — {label}\n")
        w(f"{total} conductor{'s' if total != 1 else ''} across {len(per_node)} "
          f"node{'s' if len(per_node) != 1 else ''}.\n")
        w("| Node | Off trunk | Basis | Conductors | Wires |")
        w("|---|---|---|---|---|")
        for n in sorted(per_node):
            _, branch_mm, bas, src = cl.POSITIONS[n]
            names = ", ".join("`" + m.removeprefix("W_") + "`" for m in per_node[n])
            w(f"| `{n}` | {branch_mm} mm | {bas} | {len(per_node[n])} | {names} |")
        w("")
    return "\n".join(o)


def svg(spans, pts, segs, drop):
    """Trunk to scale across the top, with each breakout's drops stacked in a
    lane of its own below it. Lanes are evenly spaced rather than sitting under
    their tick, because three breakouts fall within 60 mm of each other at the
    bars and their labels would otherwise overlap - a leader line ties each
    lane back to its tick."""
    marks = sorted(pts)
    W = 1560
    x0, x1 = 80, W - 80
    span_mm = marks[-1] - marks[0]
    scale = (x1 - x0) / span_mm
    top = 210          # trunk centreline
    bend = top + 74    # where leaders turn toward their lane
    stack0 = bend + 40  # first box in each lane
    BOX_H, BOX_GAP = 24, 8
    colw = (x1 - x0) / len(marks)

    def X(mm):
        return x0 + (mm - marks[0]) * scale

    def lane(i):
        return x0 + (i + 0.5) * colw

    peak_n = max(len(m) for _, _, m in segs)
    deepest = max(len(drop[mm]) for mm in marks)
    H = int(stack0 + deepest * (BOX_H + BOX_GAP) + 96)

    def half(n):
        return max(3.0, 26.0 * (n / peak_n))

    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
      f'viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif">')
    a(f'<rect width="{W}" height="{H}" fill="#fbfbf9"/>')
    a('<text x="80" y="48" font-size="25" fill="#222">KZ305 rebuild — branch map</text>')
    a('<text x="80" y="74" font-size="13.5" fill="#666">Which wires travel together. '
      'Trunk thickness is conductor count; distances are mm from the headlight datum.</text>')
    a('<text x="80" y="94" font-size="13.5" fill="#666">Drops are positioned to scale but '
      'drawn in even lanes, so a lane sits near its tick rather than exactly under it.</text>')

    # --- trunk ---------------------------------------------------------
    for aa, bb, members in segs:
        n = len(members)
        h = half(n)
        wpx = X(bb) - X(aa)
        a(f'<rect x="{X(aa):.1f}" y="{top - h:.1f}" width="{wpx:.1f}" '
          f'height="{2 * h:.1f}" fill="#4a6fa5" fill-opacity="0.85" stroke="#2d456a" stroke-width="1"/>')
        mx = (X(aa) + X(bb)) / 2
        a(f'<text x="{mx:.1f}" y="{top + 5:.1f}" font-size="15" fill="#fff" '
          f'text-anchor="middle" font-weight="bold">{n}</text>')
        pairs = [(m, spans[m][3]) for m in members]
        _, od = bundle_od(pairs)
        # a narrow segment has no room for the caption; the table carries it
        if od and wpx > 92:
            a(f'<text x="{mx:.1f}" y="{top - h - 11:.1f}" font-size="12" fill="#555" '
              f'text-anchor="middle">{od:.1f} mm · {sleeve_for(od)}</text>')

    # --- ticks, leaders and lanes ---------------------------------------
    for i, mm in enumerate(marks):
        x, cx = X(mm), lane(i)
        a(f'<line x1="{x:.1f}" y1="{top - 42}" x2="{x:.1f}" y2="{top + 42}" '
          'stroke="#222" stroke-width="1.5"/>')
        a(f'<text x="{x:.1f}" y="{top - 50}" font-size="13.5" fill="#222" '
          f'text-anchor="middle" font-weight="bold">{mm}</text>')
        per_node = drop[mm]
        if not per_node:
            continue
        ybot = stack0 + len(per_node) * (BOX_H + BOX_GAP) - BOX_GAP
        a(f'<path d="M {x:.1f} {top + 42} L {x:.1f} {bend} L {cx:.1f} {bend} '
          f'L {cx:.1f} {stack0}" fill="none" stroke="#9a9a9a" stroke-width="1"/>')
        # a spine behind the stack, so a tall lane still reads as one group
        a(f'<line x1="{cx:.1f}" y1="{stack0}" x2="{cx:.1f}" y2="{ybot:.1f}" '
          'stroke="#dcdcdc" stroke-width="1"/>')
        place = PLACE.get(mm, "")
        if place:
            a(f'<text x="{cx:.1f}" y="{bend - 10}" font-size="12" fill="#666" '
              f'text-anchor="middle">{place}</text>')
        y = stack0
        for n in sorted(per_node):
            cnt = len(per_node[n])
            dash = ' stroke-dasharray="4,3"' if cl.POSITIONS[n][2] == "est" else ""
            bw = colw - 18
            a(f'<rect x="{cx - bw / 2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{BOX_H}" '
              f'rx="4" fill="#fff" stroke="#8a8a8a" stroke-width="1"{dash}/>')
            a(f'<text x="{cx:.1f}" y="{y + 16.5:.1f}" font-size="12.5" fill="#222" '
              f'text-anchor="middle">{n} · {cnt}</text>')
            y += BOX_H + BOX_GAP

    fy = H - 52
    a(f'<text x="80" y="{fy}" font-size="12.5" fill="#555">Solid box = both ends measured on '
      'the old harness (tape). Dashed = at least one end placed by where the part sits (est). '
      'The number after a node is conductors in that drop.</text>')
    a(f'<text x="80" y="{fy + 20}" font-size="12.5" fill="#555">Sleeve sizes follow '
      'docs/prowire-order.md, where only the 1/4&#8221; figure (9.5 mm expanded) is recorded. '
      'Bundle OD is estimated, not measured — see docs/branch-map.md.</text>')
    a('</svg>')
    return "\n".join(o)


def main():
    doc = load(cl.REBUILD, cl.COMMON.read_text(encoding="utf-8"))
    spans, unplaced = wire_spans(doc)
    pts = breakouts(spans)
    segs = segments(spans, pts)
    drop = drops(spans, pts)

    want_svg = "--svg" in sys.argv
    text = svg(spans, pts, segs, drop) if want_svg else md(doc, spans, pts, segs, drop)
    print(text)

    if unplaced:
        for name, missing in sorted(unplaced.items()):
            print(f"unplaced node on built wire {name}: {', '.join(missing)}", file=sys.stderr)

    name = "branch-map.svg" if want_svg else "branch-map.md"
    if not DROPBOX_DIR.is_dir():
        print(f"no {DROPBOX_DIR} - {name} not copied", file=sys.stderr)
        return
    (DROPBOX_DIR / name).write_text(text + "\n", encoding="utf-8")
    if want_svg and shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", "1800", "-o", str(DROPBOX_DIR / "branch-map.png")],
                       input=text.encode("utf-8"), check=True)
        print(f"copied branch-map.svg and branch-map.png to {DROPBOX_DIR}", file=sys.stderr)
    else:
        print(f"copied {name} to {DROPBOX_DIR}", file=sys.stderr)


if __name__ == "__main__":
    main()
