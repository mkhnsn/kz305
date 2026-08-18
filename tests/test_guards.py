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
    # A model that rendered nothing would still exit 0 without this.
    assert (tmp_path / "kz305-factory.svg").exists()
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

    assert (split_dir / "h.svg").read_bytes() == (whole_dir / "h.svg").read_bytes()


def test_every_sheet_renders(tmp_path):
    """Each per-subsystem sheet must render on its own."""
    import yaml
    manifest = yaml.safe_load((ROOT / "harness.yml").read_text())
    sheets = [n for n in manifest["models"] if n.startswith("sheet-")]
    assert sheets, "no sheets defined in the manifest"
    result = render(*sheets, "-o", tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    for name in sheets:
        assert (tmp_path / f"{name}.svg").exists(), f"{name} produced no drawing"
