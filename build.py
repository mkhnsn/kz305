#!/usr/bin/env python3
"""Merge subsystem WireViz files into one harness and render it.

Why this exists: WireViz's --prepend concatenates raw text, and YAML resolves
duplicate top-level keys last-wins. Two files that each define `connections:`
therefore produce a drawing containing only the second one's -- silently, with
exit 0 and a warning. A harness built from that BOM is missing real wires.

This tool merges at the data level instead:
  * duplicate connector/cable NAMES across files are an error, never last-wins
  * duplicate keys WITHIN a file are an error (PyYAML also silently drops those)
  * a component left out of every connection set is an error, not a warning

Each subsystem file is loaded with the shared template file textually prepended,
so YAML anchors resolve per-file and every subsystem stays independently
renderable on its own.

Normally driven by ./render, which reads harness.yml and builds every model
listed there, so no flags need remembering:

    ./render               # build everything
    ./render factory       # build one model
    ./render --list        # show what is defined

Flags still override the manifest for one-off renders:

    ./render --common kz305-common.yml -O scratch -f s some/*.yml
"""

import argparse
import io
import sys
from collections import OrderedDict
from contextlib import redirect_stdout
from pathlib import Path

import yaml

import wireviz.wireviz as wv

# Keys merged by union; every other top-level key must be defined by exactly one file.
MERGE_DICT = ("connectors", "cables")
MERGE_LIST = ("connections", "additional_bom_items")
# Anchor definitions live here; WireViz ignores it, and so do we.
TEMPLATE_KEY = "templates"

MANIFEST = "harness.yml"
FORMAT_CODES = {"g": "gv", "h": "html", "p": "png", "s": "svg", "t": "tsv"}


# Lines of shared template text prepended to the file currently being loaded,
# so reported line numbers point into the subsystem file the author is editing.
_PREPENDED_LINES = 0


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of silently
    keeping the last one."""


def _no_duplicates(loader, node, deep=False):
    # Check the keys written literally in this mapping, BEFORE flatten_mapping
    # merges the anchor in. A subsystem overriding an anchor field (`<<: *coil`
    # then `subtype: ...`) is legitimate; the same key typed twice is not.
    seen = set()
    for key_node, _ in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            continue
        key = key_node.value
        if key in seen:
            raise yaml.YAMLError(
                f"duplicate key {key!r} at line "
                f"{key_node.start_mark.line + 1 - _PREPENDED_LINES} "
                f"(YAML would silently keep only the last one)"
            )
        seen.add(key)
    # Hand off to SafeConstructor, which resolves `<<` merge keys.
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def load(path: Path, common: str) -> dict:
    """Load one subsystem file with the shared templates prepended."""
    global _PREPENDED_LINES
    _PREPENDED_LINES = common.count("\n") + 1
    text = common + "\n" + path.read_text(encoding="utf-8")
    try:
        data = yaml.load(text, Loader=StrictLoader) or {}
    except yaml.YAMLError as e:
        sys.exit(f"error: {path}: {e}")
    data.pop(TEMPLATE_KEY, None)
    return data


def merge(sources: dict[Path, dict]) -> dict:
    merged: dict = {}
    owner: dict[tuple[str, str], Path] = {}  # (section, name) -> file that defined it
    errors: list[str] = []

    for path, data in sources.items():
        for key, value in data.items():
            if key in MERGE_DICT:
                section = merged.setdefault(key, {})
                for name, body in value.items():
                    if name in section:
                        errors.append(
                            f"{key[:-1]} {name!r} defined in both "
                            f"{owner[(key, name)]} and {path}"
                        )
                        continue
                    section[name] = body
                    owner[(key, name)] = path
            elif key in MERGE_LIST:
                merged.setdefault(key, []).extend(value)
            else:
                if key in owner:
                    errors.append(
                        f"top-level {key!r} defined in both {owner[key]} and {path}; "
                        f"it must appear in exactly one file"
                    )
                    continue
                merged[key] = value
                owner[key] = path

    if errors:
        sys.exit("error: name collisions across subsystem files:\n  - " + "\n  - ".join(errors))
    return merged


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
    """Merge `sources` into one harness and render it. Returns nothing; exits
    nonzero on any condition that would silently produce an incomplete BOM."""
    if not sources:
        sys.exit(f"error: model {name!r} matched no source files")

    common = common_path.read_text(encoding="utf-8") if common_path else ""
    merged = merge({p: load(p, common) for p in sources})

    label = f"[{name}] " if name else ""
    print(
        f"{label}{len(merged.get('connectors', {}))} connectors, "
        f"{len(merged.get('cables', {}))} cables, "
        f"{len(merged.get('connections', []))} connection sets "
        f"from {len(sources)} file(s)"
    )

    if dump:
        dump.write_text(yaml.safe_dump(merged, sort_keys=False), encoding="utf-8")

    # WireViz reports unreferenced components on stdout as a warning. Capture it
    # and promote it to a build failure: a component in no connection set is
    # dropped from both the drawing and the BOM, so it would never get built.
    buf = io.StringIO()
    with redirect_stdout(buf):
        wv.parse(
            merged,
            output_formats=formats,
            output_dir=output_dir,
            output_name=output_name,
        )
    out = buf.getvalue()
    sys.stdout.write("".join(
        line + "\n" for line in out.splitlines()
        if line.strip() and not line.startswith("Warning: Unknown")
    ))

    if "not referenced in any connection set" in out:
        sys.exit(
            f"error: the components above are in no connection set. WireViz drops "
            f"them from the drawing AND the BOM, so they would never get built.\n"
            f"Connect them, or move them to the documented gap list."
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
