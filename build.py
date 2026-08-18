#!/usr/bin/env python3
"""Render the harness models listed in harness.yml.

All of the merging and validation lives in WireViz itself now -- see FORK.md in
the pinned fork for --merge and --strict. What remains here is the project
layer: reading the manifest so that no flags have to be remembered, and
resolving each model's source globs.

    ./render               # build everything
    ./render factory       # build one model
    ./render --list        # show what is defined

Flags still override the manifest for one-off renders:

    ./render --common models/kz305-common.yml -O scratch -f s some/*.yml
"""

import argparse
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

import wireviz.wireviz as wv
from wireviz import wv_merge, wv_yaml
from wireviz.wv_errors import DuplicateKeyError, UnreferencedComponentsError, WireVizError

MANIFEST = "harness.yml"
FORMAT_CODES = {"g": "gv", "h": "html", "p": "png", "s": "svg", "t": "tsv"}


def load(path: Path, common: str) -> dict:
    """Load one source file with the shared templates prepended, so that YAML
    anchors defined there resolve inside it."""
    prepended_lines = common.count("\n") + 1
    text = common + "\n" + path.read_text(encoding="utf-8")
    try:
        return wv_yaml.safe_load(text, strict=True) or {}
    except DuplicateKeyError as e:
        # Report the line in the file being edited, not in the merged text.
        sys.exit(
            f"error: {path}: duplicate key {e.key!r} at line "
            f"{e.line - prepended_lines}"
        )
    except yaml.YAMLError as e:
        sys.exit(f"error: {path}: {e}")


def resolve_formats(codes: str) -> tuple:
    unknown = sorted(set(codes) - set(FORMAT_CODES))
    if unknown:
        sys.exit(
            f"error: unknown format code(s) {''.join(unknown)!r}; "
            f"valid codes are {''.join(FORMAT_CODES)} "
            f"({', '.join(f'{k}={v}' for k, v in FORMAT_CODES.items())})"
        )
    return tuple(OrderedDict.fromkeys(FORMAT_CODES[c] for c in codes))


def build(name, sources, common_path, output_name, output_dir, formats, dump=None):
    """Merge `sources` into one harness and render it. Exits nonzero on any
    condition that would otherwise produce a quietly incomplete BOM."""
    if not sources:
        sys.exit(f"error: model {name!r} matched no source files")

    common = common_path.read_text(encoding="utf-8") if common_path else ""
    try:
        merged = wv_merge.merge([(str(p), load(p, common)) for p in sources])
    except WireVizError as e:
        sys.exit(f"error: {e}")

    label = f"[{name}] " if name else ""
    print(
        f"{label}{len(merged.get('connectors', {}))} connectors, "
        f"{len(merged.get('cables', {}))} cables, "
        f"{len(merged.get('connections', []))} connection sets "
        f"from {len(sources)} file(s)"
    )

    if dump:
        dump.write_text(yaml.safe_dump(merged, sort_keys=False), encoding="utf-8")

    # strict=True makes WireViz raise on a component that no connection set
    # references. Such a component is dropped from both the drawing and the
    # BOM, so it would never get built.
    try:
        wv.parse(
            merged,
            output_formats=formats,
            output_dir=output_dir,
            output_name=output_name,
            strict=True,
        )
    except UnreferencedComponentsError as e:
        one = len(e.components) == 1
        sys.exit(
            f"error: {', '.join(e.components)} {'appears' if one else 'appear'} in "
            f"no connection set, so {'it is' if one else 'they are'} absent from "
            f"the drawing AND the BOM and would never get built.\n"
            f"Connect {'it' if one else 'them'}, or move to the documented gap list."
        )

    print(f"{label}wrote {output_dir / output_name}.[{'|'.join(formats)}]")


def load_manifest(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        sys.exit(f"error: {path}: {e}")
    if not data.get("models"):
        sys.exit(f"error: {path} defines no `models:`")
    return data


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "targets",
        nargs="*",
        help=f"model names from {MANIFEST} (default: all of them), "
        f"or source files when -O is given",
    )
    ap.add_argument("--manifest", type=Path, default=Path(MANIFEST))
    ap.add_argument("--list", action="store_true", help="list models and exit")
    ap.add_argument("--common", type=Path, help="override the shared template file")
    ap.add_argument("-O", "--output-name", help="one-off render: treat targets as files")
    ap.add_argument(
        "-o", "--output-dir", type=Path, help="default: output_dir from the manifest"
    )
    ap.add_argument("-f", "--format", help="WireViz format codes (default: per model)")
    ap.add_argument("--dump", type=Path, help="also write the merged YAML here")
    args = ap.parse_args()

    # One-off mode: -O means "these targets are files, render them as one model".
    if args.output_name:
        build(
            name=None,
            sources=[Path(t) for t in args.targets],
            common_path=args.common,
            output_name=args.output_name,
            output_dir=args.output_dir or Path("."),
            formats=resolve_formats(args.format or "hps"),
            dump=args.dump,
        )
        return

    if not args.manifest.exists():
        sys.exit(
            f"error: no {args.manifest} here. Either run from the project root, "
            f"or render explicitly with -O NAME file.yml ..."
        )
    manifest = load_manifest(args.manifest)
    models = manifest["models"]
    root = args.manifest.parent

    if args.list:
        for name, spec in models.items():
            found = sorted({p for g in spec["sources"] for p in root.glob(g)})
            print(f"{name:12s} -> {spec['output']}.[{spec.get('formats', 'hps')}]")
            for p in found:
                print(f"    {p}")
            if not found:
                print("    (no source files matched)")
        return

    unknown = [t for t in args.targets if t not in models]
    if unknown:
        sys.exit(
            f"error: unknown model(s) {', '.join(unknown)}. "
            f"{args.manifest} defines: {', '.join(models)}"
        )

    out_dir = args.output_dir or root / manifest.get("output_dir", ".")
    out_dir.mkdir(parents=True, exist_ok=True)

    common_path = args.common or (
        root / manifest["common"] if manifest.get("common") else None
    )

    for name in args.targets or models:
        spec = models[name]
        # Sorted+deduped so render order never depends on the shell or the OS.
        sources = sorted({p for g in spec["sources"] for p in root.glob(g)})
        build(
            name=name,
            sources=sources,
            common_path=common_path,
            output_name=spec["output"],
            output_dir=out_dir,
            formats=resolve_formats(args.format or spec.get("formats", "hps")),
        )


if __name__ == "__main__":
    main()
