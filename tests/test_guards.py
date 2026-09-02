# -*- coding: utf-8 -*-
"""End-to-end checks on ./render.

These exist to keep the pinned WireViz fork honest. Every guard below is
enforced by the fork rather than by build.py, so a repin that changed or lost
`--strict` / `--merge` would quietly stop protecting the BOM. Asserting the
exit code here is what catches that: a guard that no longer fails the build is
indistinguishable from a clean run.
"""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
COMMON = ROOT / "models" / "kz305-common.yml"
FACTORY_DIR = ROOT / "models" / "factory"
FACTORY = sorted(FACTORY_DIR.glob("*.yml"))

ORPHAN = """
connectors:
  ORPHAN_FOR_TEST: {type: Nowhere, pinlabels: [p]}
"""

CLASH = """
connectors:
  SP_BR: {type: Splice}
"""

DUPLICATE_KEY = """
connectors:
  A: {type: X, pinlabels: [p]}
  A: {type: Y, pinlabels: [p]}
"""


def render(*args):
    return subprocess.run(
        [sys.executable, str(ROOT / "build.py"), *map(str, args)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


def render_files(tmp_path, *sources, fmt="s"):
    return render(
        "--common", COMMON, "-O", "out", "-o", tmp_path, "-f", fmt, *sources
    )


def write(tmp_path, name, text):
    path = tmp_path / name
    path.write_text(text)
    return path


def test_every_model_in_the_manifest_renders(tmp_path):
    result = render("-o", tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    # A model that rendered nothing would still exit 0 without this. The
    # factory model defines `sheets:`, so its graphical outputs are per-sheet
    # files; the whole-harness HTML page carries every sheet.
    assert (tmp_path / "kz305-factory.backbone.svg").exists()
    assert (tmp_path / "kz305-factory.html").exists()
    assert (tmp_path / "kz305-rebuild.svg").exists()


def test_factory_renders_without_a_bom(tmp_path):
    # The factory model carries no lengths by design. WireViz has no "length
    # unknown" state, so a BOM would print 0 m and read as measured.
    render("factory", "-o", tmp_path)
    assert not (tmp_path / "kz305-factory.bom.tsv").exists()


def test_rebuild_produces_a_bom(tmp_path):
    render("rebuild", "-o", tmp_path)
    assert (tmp_path / "kz305-rebuild.bom.tsv").exists()


def test_component_in_no_connection_set_fails_the_build(tmp_path):
    orphan = write(tmp_path, "orphan.yml", ORPHAN)
    result = render_files(tmp_path, *FACTORY, orphan)
    assert result.returncode != 0
    assert "ORPHAN_FOR_TEST" in result.stdout + result.stderr


def test_name_defined_in_two_files_fails_the_build(tmp_path):
    clash = write(tmp_path, "clash.yml", CLASH)
    result = render_files(tmp_path, *FACTORY, clash)
    assert result.returncode != 0
    assert "SP_BR" in result.stdout + result.stderr


def test_duplicate_key_within_a_file_fails_the_build(tmp_path):
    dup = write(tmp_path, "dup.yml", DUPLICATE_KEY)
    result = render_files(tmp_path, dup)
    assert result.returncode != 0
    # Reported against the file being edited, not the merged text.
    assert "line 4" in result.stdout + result.stderr


def test_unknown_format_code_fails_the_build(tmp_path):
    result = render("factory", "-o", tmp_path, "-f", "hz")
    assert result.returncode != 0
    assert "'z'" in result.stdout + result.stderr


def test_split_across_files_matches_a_single_file(tmp_path):
    """Splitting a model across files must not change what gets built."""
    # Concatenating the subsystem files by hand is only valid because none of
    # them repeat a top-level key -- which is exactly what --merge exists to
    # stop mattering. Both routes must reach the same drawing.
    parts = [write(tmp_path, f"part_{i}.yml", p.read_text())
             for i, p in enumerate(FACTORY)]

    split_dir, whole_dir = tmp_path / "split", tmp_path / "whole"
    split_dir.mkdir()
    whole_dir.mkdir()

    assert render("--common", COMMON, "-O", "h", "-o", split_dir, "-f", "s",
                  *parts).returncode == 0
    assert render("--common", COMMON, "-O", "h", "-o", whole_dir, "-f", "s",
                  *FACTORY).returncode == 0

    # The factory sources define `sheets:`, so the drawing is per-sheet files.
    split_svgs = sorted(p.name for p in split_dir.glob("h.*.svg"))
    whole_svgs = sorted(p.name for p in whole_dir.glob("h.*.svg"))
    assert split_svgs and split_svgs == whole_svgs
    for name in split_svgs:
        assert (split_dir / name).read_bytes() == (whole_dir / name).read_bytes()


def test_every_sheet_renders(tmp_path):
    """Every sheet named in the sheet mapping must come out as a drawing."""
    import yaml
    sheets = yaml.safe_load(
        (FACTORY_DIR / "sheets.yml").read_text())["sheets"]
    assert sheets, "no sheets defined in models/factory/sheets.yml"
    result = render("factory", "-o", tmp_path, "-f", "s")
    assert result.returncode == 0, result.stdout + result.stderr
    for name in sheets:
        svg = tmp_path / f"kz305-factory.{name}.svg"
        assert svg.exists(), f"sheet {name} produced no drawing"


def test_component_missing_from_the_sheet_mapping_fails_the_build(tmp_path):
    """The sheet mapping is exhaustive: a new component that nobody assigned
    (or chained to an assigned one) must fail, not silently land somewhere."""
    stray = write(tmp_path, "stray.yml", """
connectors:
  STRAY_FOR_TEST: {type: Nowhere, pinlabels: [a, b]}
cables:
  W_STRAY_FOR_TEST: {wirecount: 1, gauge: 18 AWG}
connections:
  - - STRAY_FOR_TEST: [1]
    - W_STRAY_FOR_TEST: [1]
    - STRAY_FOR_TEST: [2]
""")
    result = render_files(tmp_path, *FACTORY, stray)
    assert result.returncode != 0
    assert "STRAY_FOR_TEST" in result.stdout + result.stderr


def test_index_links_every_rendered_drawing(tmp_path):
    """The published index is generated, so nothing fails loudly when it goes
    wrong -- a renamed output just drops off the page and the site quietly
    stops linking a drawing that rendered fine."""
    assert render("-o", tmp_path).returncode == 0
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "make_index.py"), "-o", str(tmp_path)],
        capture_output=True, text=True, cwd=ROOT,
    )
    assert result.returncode == 0, result.stdout + result.stderr

    index = (tmp_path / "index.html").read_text(encoding="utf-8")
    rendered = [
        p.name for p in tmp_path.iterdir()
        if p.name != "index.html" and p.suffix in {".html", ".svg", ".png", ".tsv"}
    ]
    assert rendered, "nothing rendered to index"
    missing = [n for n in rendered if n not in index]
    assert not missing, f"rendered but not linked from index.html: {missing}"


def test_no_angle_brackets_in_model_text(tmp_path):
    """A '>' in a note silently breaks the graphviz HTML label.

    WireViz renders notes into HTML-like labels, so a bare '>' - most easily
    written as an arrow, 'A -> B' - is parsed as a tag delimiter. The label is
    truncated mid-cell and graphviz fails with a syntax error pointing at
    whatever word happens to sit near the break, which says nothing about the
    real cause. This cost a debugging round on 29 Aug 2026.

    The quoted '-->' used as a connection-set marker is legitimate and skipped.
    """
    offenders = []
    for path in [COMMON, *FACTORY, ROOT / "models" / "kz305-rebuild.yml"]:
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            code = line.split("#", 1)[0]
            if "'-->'" in code or '"-->"' in code:
                continue
            if ">" in code:
                offenders.append(f"{path.relative_to(ROOT)}:{lineno}: {line.strip()}")
    assert not offenders, (
        "'>' in model text breaks the graphviz HTML label and fails the render "
        "with a misleading syntax error. Write arrows as words, or use a comma:\n"
        + "\n".join(offenders)
    )


COLOUR_TOKENS = {
    "BK": "BK", "BN": "BN", "BU": "BU", "GN": "GN", "GY": "GY", "OG": "OG",
    "RD": "RD", "WH": "WH", "YE": "YE", "VT": "VT", "PK": "PK", "TQ": "TQ",
    "BL": "BU", "BR": "BN", "GR": "GY", "OR": "OG", "R": "RD", "W": "WH",
    "Y": "YE", "G": "GN", "O": "OG", "BLW": "BUWH",
    # Light green is a DIFFERENT wire from green on this bike, but WireViz has
    # no distinct code for it and renders both GN - so the guard cannot tell
    # them apart either. Kept as a known limitation rather than a silent one.
    "LG": "GN",
}


def _canon(label):
    """'Bl/W' -> 'BUWH', 'Br' -> 'BN'. None if the label is not a colour.

    Accepts a bare colour ('Br/W'), a colour with a role after it
    ('Br STOP IN'), or a role with the colour parenthesised ('BATT (W)').
    The last form is why IGN is covered - without it a connector whose ways
    are named by function would sit outside the guard entirely, which is
    exactly where a renumber does its damage unseen.
    """
    if "(" in label and ")" in label:
        label = label[label.index("(") + 1:label.index(")")]
    else:
        label = label.split()[0]
    parts = label.replace("-", "/").split("/")
    out = ""
    for part in parts:
        key = part.strip().upper()
        if key not in COLOUR_TOKENS:
            return None
        out += COLOUR_TOKENS[key]
    return out


def test_cable_colour_matches_the_pin_it_lands_on(tmp_path):
    """A cable must match the colour its pin is labelled with.

    WireViz cannot catch this: pin 2 exists whatever colour lands on it, so
    renumbering a connector's ways silently repoints every connection that
    referenced it BY INDEX - including ones in other files, and including the
    other model when the connector comes from a shared anchor. That happened on
    29 Aug 2026 when FUSE_4P was renumbered to physical cavities and the
    references in lighting.yml and controls.yml were missed. The render was
    clean and every test passed; the drawing was simply wrong.

    Only connectors whose pinlabels are ALL colours are checked, which is the
    junctions and switches where a way list is a colour map.

    Uses build.py's own merge rather than concatenating the sources: duplicate
    top-level keys resolve last-wins, which is precisely the bug build.py
    exists to prevent, and a check built on it silently sees one file.
    """
    sys.path.insert(0, str(ROOT))
    import build
    from wireviz import wv_merge

    common = COMMON.read_text(encoding="utf-8")

    def merged(sources):
        return wv_merge.merge([(str(p), build.load(p, common)) for p in sources])

    # ** FACTORY ONLY, SINCE 1 Sep 2026. ** This guard's premise is that a way
    # list is a colour map, and that holds for the factory model - it records
    # what the bike HAD, so a pin labelled "R/BK HI" must carry an R/BK wire.
    #
    # It stopped holding for the rebuild when that model went to SOLID COLOURS
    # on a function-based scheme. At the RETAINED stock switchgear - IGN, RH,
    # LH - the far half is the original pigtail in factory colours while the
    # harness side is new wire on the new scheme, so the two deliberately
    # disagree at the joint. RH is the sharpest case: its stock START OUT is
    # BLACK, and under the new scheme black is ground only, so matching the
    # stock colour would reproduce the exact trap the factory model warns
    # about - a starter trigger that looks like an earth.
    #
    # Listing those as `acknowledged` would have buried a deliberate scheme in
    # an exceptions dict. The rebuild's equivalent invariant is different and
    # is enforced by test_rebuild_has_no_colour_collisions_on_a_connector.
    docs = {
        "factory": merged(FACTORY),
    }

    # Discrepancies that are DELIBERATE and documented in the model notes. This
    # project leaves a contradiction drawn rather than guessing a fix, so the
    # guard has to allow those - but each is re-asserted below, so an entry
    # cannot outlive the conflict it describes.
    # Empty is the goal state, and it has been reached once already: the
    # W_IGN_FEED / MF conflict lived here until 29 Aug 2026, when a ring-out
    # showed the fuse's two terminals were assigned backwards and the cable was
    # right all along. Add an entry only for a discrepancy the model is
    # DELIBERATELY leaving drawn, with the reason.
    acknowledged = {}

    problems, seen = [], set()
    for model, doc in docs.items():
        colour_maps = {}
        for name, spec in (doc.get("connectors") or {}).items():
            labels = (spec or {}).get("pinlabels")
            if not labels:
                continue
            canon = [_canon(str(l)) for l in labels]
            if all(canon):
                colour_maps[name] = canon
        assert colour_maps, f"{model}: no colour-mapped connectors - guard is a no-op"

        cables = {n: (c or {}).get("colors") for n, c in (doc.get("cables") or {}).items()}

        for conn_set in doc.get("connections") or []:
            entries = [e for e in conn_set if isinstance(e, dict)]
            cable = next((n for e in entries for n in e if n in cables), None)
            if cable is None or not cables.get(cable):
                continue
            wire = "".join(cables[cable])
            for entry in entries:
                for name, pins in entry.items():
                    if name not in colour_maps:
                        continue
                    for pin in pins:
                        if not isinstance(pin, int):
                            continue
                        expected = colour_maps[name][pin - 1]
                        if expected == wire:
                            continue
                        if (model, cable, name, pin) in acknowledged:
                            seen.add((model, cable, name, pin))
                            continue
                        problems.append(
                            f"[{model}] {cable} ({wire}) lands on {name} pin {pin}, "
                            f"which is labelled {expected}"
                        )

    assert not problems, "cable colour disagrees with the pin's label:\n" + "\n".join(problems)

    stale = set(acknowledged) - seen
    assert not stale, (
        "these conflicts are listed as acknowledged but no longer occur - the "
        "model was fixed and the list was not:\n"
        + "\n".join(f"  [{m}] {c} on {n} pin {p}" for m, c, n, p in sorted(stale))
    )


def test_rebuild_has_no_colour_collisions_on_a_connector():
    """No two circuits on one connector may share a colour in the rebuild.

    This is the invariant that replaces the pinlabel check for the rebuild,
    and it is what makes SOLID COLOURS safe without tracers. Identification
    rests on printed labels, but colour still has to catch the swap that a
    missing or illegible label would otherwise allow - the starter trigger
    landing on the ground bus, a HOT feed into a SWITCHED fuse position.

    Same net on one connector is not a collision: a splice, a bus and the two
    sides of a fuse are all legitimately one colour.
    """
    sys.path.insert(0, str(ROOT))
    import build
    from wireviz import wv_merge

    common = COMMON.read_text(encoding="utf-8")
    doc = wv_merge.merge(
        [
            (
                str(ROOT / "models" / "kz305-rebuild.yml"),
                build.load(ROOT / "models" / "kz305-rebuild.yml", common),
            )
        ]
    )

    # Components where one colour on many ways is correct by construction.
    #   GND / SP_*  - one net by definition
    #   MF / MF_RR  - a fuse is symmetric; its two terminals are one circuit
    #   BATT        - battery positive is one net
    #   SOL         - 6 AWG battery cable comes in red and black only, so
    #                 W_BAT_SOL and W_SOL_SM are both RD. They are lugs on
    #                 separate studs and cannot physically be interchanged.
    exempt = {"GND", "SP_YR", "SP_HEAD", "MF", "MF_RR", "BATT", "SOL"}

    cables = {n: (c or {}).get("colors") for n, c in (doc.get("cables") or {}).items()}
    connectors = doc.get("connectors") or {}

    by_connector = {}
    for conn_set in doc.get("connections") or []:
        entries = [e for e in conn_set if isinstance(e, dict)]
        for idx, entry in enumerate(entries):
            cable = next(iter(entry))
            if cable not in cables or not cables[cable]:
                continue
            colour = "".join(cables[cable])
            for offset in (-1, 1):
                j = idx + offset
                if not 0 <= j < len(entries):
                    continue
                name, pins = next(iter(entries[j].items()))
                if name not in connectors:
                    continue
                slot = by_connector.setdefault(name, {}).setdefault(colour, set())
                for pin in pins:
                    slot.add((pin, cable))

    assert by_connector, "guard is a no-op - no connector/cable pairs found"

    problems = []
    for name, colours in sorted(by_connector.items()):
        if name in exempt:
            continue
        for colour, uses in sorted(colours.items()):
            # One colour arriving on two different pins FROM TWO DIFFERENT
            # CABLES is the ambiguity that matters. Two other cases are fine:
            #   - the same colour twice on ONE pin is a single net, such as a
            #     feed in and a tap out of a distribution stud;
            #   - ONE multi-conductor cable spanning several pins, where the
            #     wires are told apart by position within the cable rather
            #     than by colour. W_ALT is the case in hand - a single-phase
            #     alternator's two yellow phases, which are AC and therefore
            #     interchangeable anyway.
            pins = {pin for pin, _ in uses}
            designators = {cable for _, cable in uses}
            if len(pins) > 1 and len(designators) > 1:
                detail = ", ".join(
                    f"{cable} on pin {pin}" for pin, cable in sorted(uses)
                )
                problems.append(f"{name}: {colour} lands on several pins - {detail}")

    assert not problems, (
        "two circuits share a colour on one connector, which solid-colour "
        "wiring cannot afford:\n  " + "\n  ".join(problems)
    )
