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

import cut_list as cl  # noqa: E402
import label_schedule as ls  # noqa: E402
from build import load  # noqa: E402

DROPBOX_DIR = cl.DROPBOX_DIR

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
    w("## By component — what lands on each part\n")
    w("The assembly view: stand at one part and this is everything that arrives there.\n")
    for node in sorted(landings):
        conn = conns.get(node) or {}
        trunk, branch, bas, src = place(node)
        w(f"### `{node}` — {part_full(node, conn)}\n")
        bits = []
        if conn.get("subtype"):
            bits.append(str(conn["subtype"]))
        if src:
            bits.append(f"Sits at **{trunk} mm** from the datum, {branch} mm out ({bas}) — {src}.")
        for b in bits:
            w(b + "\n")
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
