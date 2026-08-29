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
