#!/usr/bin/env python3
"""Write out/index.html -- a landing page linking every rendered drawing.

Pages serves out/ as-is, and ./render puts no index in it, so the site root
would otherwise 404. Generated rather than hand-written for the same reason as
the cable index: a hand-written list of sheets goes stale the moment
models/factory/sheets.yml gains one.

    .venv/bin/python3 tools/make_index.py

Runs after ./render, reads harness.yml for the model list and out/ for what
actually landed there -- a format dropped from the manifest disappears from the
page without anything here having to know.
"""

import argparse
import html
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build import load_manifest  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# What each rendered format is FOR, in the order a person wants them: the
# interactive page first, because that is the one worth opening on a phone at
# the bench, and the print/vector copies after it.
FORMATS = [
    ("html", "Interactive", "pan, zoom, net tracing, BOM linkage"),
    ("svg", "SVG", "vector, scales to any print size"),
    ("png", "PNG", "raster, drops into notes and messages"),
    ("bom.tsv", "BOM", "tab-separated, opens in a spreadsheet"),
]


def git(*args, default=""):
    """Best-effort git lookup -- the page still builds outside a checkout."""
    try:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return default


def provenance() -> tuple:
    """Commit and build time. CI supplies both; locally they come from git.

    The commit is the point: a drawing is only evidence if you can say which
    models produced it, and the rendered files carry no version of their own.
    """
    sha = os.environ.get("GITHUB_SHA") or git("rev-parse", "HEAD", default="")
    when = git("log", "-1", "--format=%cd", "--date=format:%Y-%m-%d %H:%M", default="")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    return sha, when, repo


def sheets_for(out_dir: Path, stem: str, ext: str) -> list:
    """Per-sheet files are `<stem>.<sheet>.<ext>`; the whole-model file is
    `<stem>.<ext>`. Only the sheeted models have the former."""
    return sorted(
        p for p in out_dir.glob(f"{stem}.*.{ext}") if p.name != f"{stem}.{ext}"
    )


def sheet_name(path: Path, stem: str, ext: str) -> str:
    return path.name[len(stem) + 1 : -(len(ext) + 1)]


def render_model(out_dir: Path, name: str, spec: dict) -> str:
    stem = spec["output"]
    rows = []
    for ext, label, blurb in FORMATS:
        whole = out_dir / f"{stem}.{ext}"
        if not whole.exists():
            continue
        size = f"{whole.stat().st_size / 1024:.0f} KB"
        rows.append(
            f'      <li><a href="{html.escape(whole.name)}">{label}</a>'
            f"<span class=blurb>{blurb}</span>"
            f"<span class=size>{size}</span></li>"
        )

    sheets = ""
    # Sheets are listed once, from the svg set -- png mirrors it exactly, and
    # two identical lists of nine subsystems is noise, not information.
    per_sheet = sheets_for(out_dir, stem, "svg")
    if per_sheet:
        links = []
        for p in per_sheet:
            sheet = sheet_name(p, stem, "svg")
            png = out_dir / f"{stem}.{sheet}.png"
            alt = f' <a class=alt href="{html.escape(png.name)}">png</a>' if png.exists() else ""
            links.append(
                f'<li><a href="{html.escape(p.name)}">{html.escape(sheet)}</a>{alt}</li>'
            )
        sheets = (
            "      <p class=sheetlabel>Per-sheet drawings</p>\n"
            f"      <ul class=sheets>{''.join(links)}</ul>\n"
        )

    return (
        f"    <section>\n"
        f"      <h2>{html.escape(name)}</h2>\n"
        f"      <ul class=formats>\n" + "\n".join(rows) + "\n      </ul>\n"
        f"{sheets}"
        f"    </section>"
    )


CSS = """
:root {
  --bg: #fbfaf8; --fg: #1a1a1a; --muted: #6b6b6b; --rule: #e2ded8;
  --link: #8a3324; --card: #ffffff;
}
:root:not([data-theme=light]) {}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme=light]) {
    --bg: #16161a; --fg: #e8e6e3; --muted: #9a9793; --rule: #2e2e34;
    --link: #e08b6f; --card: #1d1d22;
  }
}
:root[data-theme=dark] {
  --bg: #16161a; --fg: #e8e6e3; --muted: #9a9793; --rule: #2e2e34;
  --link: #e08b6f; --card: #1d1d22;
}
* { box-sizing: border-box; }
body {
  margin: 0; padding: 3rem 1.25rem 5rem; background: var(--bg); color: var(--fg);
  font: 16px/1.6 ui-sans-serif, -apple-system, "Segoe UI", Roboto, sans-serif;
}
main { max-width: 46rem; margin: 0 auto; }
h1 { font-size: 1.5rem; margin: 0 0 .25rem; letter-spacing: -.01em; }
.sub { color: var(--muted); margin: 0 0 2.5rem; }
h2 {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .09em;
  color: var(--muted); margin: 0 0 .75rem; font-weight: 600;
}
section {
  background: var(--card); border: 1px solid var(--rule); border-radius: 10px;
  padding: 1.25rem 1.4rem; margin-bottom: 1.25rem;
}
a { color: var(--link); }
ul { list-style: none; margin: 0; padding: 0; }
.formats li {
  display: flex; align-items: baseline; gap: .6rem;
  padding: .45rem 0; border-bottom: 1px solid var(--rule);
}
.formats li:last-child { border-bottom: 0; }
.formats a { font-weight: 600; text-decoration: none; }
.formats a:hover { text-decoration: underline; }
.blurb { color: var(--muted); font-size: .85rem; flex: 1; }
.size { color: var(--muted); font-size: .78rem; font-variant-numeric: tabular-nums; }
.sheetlabel {
  font-size: .78rem; color: var(--muted); margin: 1.1rem 0 .5rem;
  text-transform: uppercase; letter-spacing: .09em; font-weight: 600;
}
.sheets { display: flex; flex-wrap: wrap; gap: .4rem; }
.sheets li {
  border: 1px solid var(--rule); border-radius: 6px; padding: .3rem .6rem;
  font-size: .875rem;
}
.sheets a { text-decoration: none; }
.sheets a:hover { text-decoration: underline; }
.alt { color: var(--muted); font-size: .78rem; margin-left: .35rem; }
footer {
  max-width: 46rem; margin: 2.5rem auto 0; color: var(--muted); font-size: .82rem;
  border-top: 1px solid var(--rule); padding-top: 1rem;
}
code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .85em; }
@media (max-width: 32rem) {
  body { padding-top: 2rem; }
  .formats li { flex-wrap: wrap; gap: .35rem .6rem; }
  .blurb { flex-basis: 100%; }
}
"""


def build_page(out_dir: Path, manifest: dict) -> str:
    sections = [
        render_model(out_dir, name, spec) for name, spec in manifest["models"].items()
    ]
    sha, when, repo = provenance()
    short = sha[:8] if sha else "unknown"
    link = (
        f'<a href="https://github.com/{html.escape(repo)}/commit/{html.escape(sha)}">'
        f"<code>{short}</code></a>"
        if repo and sha
        else f"<code>{short}</code>"
    )
    built = f" &middot; rendered {html.escape(when)}" if when else ""
    return f"""<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8>
<meta name=viewport content="width=device-width, initial-scale=1">
<title>KZ305 harness drawings</title>
<style>{CSS}</style>
</head>
<body>
<main>
  <h1>KZ305 harness drawings</h1>
  <p class=sub>Rendered from the models in this repository. Regenerated on every
  push to main &mdash; the YAML under <code>models/</code> is the source of truth,
  never these files.</p>
{chr(10).join(sections)}
</main>
<footer>
  Built from {link}{built}.
</footer>
</body>
</html>
"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", type=Path, default=ROOT / "harness.yml")
    ap.add_argument("-o", "--output-dir", type=Path,
                    help="default: output_dir from the manifest")
    args = ap.parse_args()

    manifest = load_manifest(args.manifest)
    out_dir = args.output_dir or args.manifest.parent / manifest.get("output_dir", ".")
    if not out_dir.is_dir():
        sys.exit(f"error: no {out_dir}/ to index -- run ./render first")

    index = out_dir / "index.html"
    index.write_text(build_page(out_dir, manifest), encoding="utf-8")
    print(f"wrote {index}")


if __name__ == "__main__":
    main()
