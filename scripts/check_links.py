#!/usr/bin/env python3
"""Check that every link in the vault resolves to a real file.

Checks three kinds of reference found in the notes:

  1. wiki-links      [[note]] / [[path/note|alias]]        (also inside YAML frontmatter)
  2. wiki-embeds     ![[path/image.png]]
  3. path references `01_Features/<domain>/<slug>/screens/x.png` in inline code

Fenced code blocks are skipped entirely (they hold examples, not real links).
Wiki-links inside inline code are skipped too — conventions.md quotes broken
links on purpose as counter-examples. Inline code is where path references are
checked instead, so both cases stay honest.

Usage:
    python scripts/check_links.py              # exit 1 if anything is unresolved
    python scripts/check_links.py --baseline 22  # exit 1 only above the baseline
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

# Folders that are generated, vendored, or not part of the vault.
SKIP_DIRS = {".git", ".venv", ".obsidian", "docs", "site", "node_modules", "plans"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
WIKI_RE = re.compile(r"(!?)\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(<?([^)<>]+?)>?\)")
# A vault path starts with a numbered top-level folder: 00_Project_Info/, 01_Features/, ...
# Screenshot file names contain spaces, so the tail must allow them.
VAULT_PATH_RE = re.compile(r"^\d{2}_[A-Za-z_]+/.+$")
# Docs and templates spell out placeholders instead of real targets — not links.
PLACEHOLDER_CHARS = ("<", ">", "…", "{{", "*")

MD_EXTS = {".md", ".base", ".canvas"}


def is_placeholder(ref: str) -> bool:
    return any(c in ref for c in PLACEHOLDER_CHARS)


def vault_files(root: Path) -> list[Path]:
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            out.append(Path(dirpath) / name)
    return out


def build_index(files: list[Path], root: Path) -> tuple[set[str], dict[str, list[str]]]:
    """Return (set of relative paths, map of bare filename -> relative paths)."""
    rel_paths = set()
    by_name: dict[str, list[str]] = {}
    for f in files:
        rel = f.relative_to(root).as_posix()
        rel_paths.add(rel)
        by_name.setdefault(f.name, []).append(rel)
        if f.suffix in MD_EXTS:  # Obsidian resolves [[note]] without the extension
            by_name.setdefault(f.stem, []).append(rel)
    return rel_paths, by_name


def strip_inline_code(line: str) -> tuple[str, list[str]]:
    """Split a line into (text without inline code, list of inline-code spans)."""
    spans = INLINE_CODE_RE.findall(line)
    return INLINE_CODE_RE.sub(" ", line), spans


def resolve_wiki(target: str, rel_paths: set[str], by_name: dict[str, list[str]]) -> bool:
    # Inside a markdown table the alias pipe is escaped (`[[note\|alias]]`), so the
    # captured target keeps a trailing backslash.
    target = target.rstrip("\\").strip()
    if not target or target.startswith(("http://", "https://")):
        return True
    if target.endswith("/"):
        return False  # a link to a folder never resolves in Obsidian
    if "/" in target:
        candidates = [target, target + ".md"]
        return any(c in rel_paths for c in candidates)
    return target in by_name


def resolve_path(ref: str, root: Path) -> bool:
    p = root / ref
    if ref.endswith("/"):
        return p.is_dir()
    return p.exists()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=int, default=0,
                    help="known-broken count to tolerate (migration safety net)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    files = vault_files(root)
    rel_paths, by_name = build_index(files, root)

    problems: list[str] = []
    for f in sorted(files):
        if f.suffix != ".md":
            continue
        rel = f.relative_to(root).as_posix()
        in_fence = False
        for lineno, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            text, code_spans = strip_inline_code(line)

            for bang, target in WIKI_RE.findall(text):
                if is_placeholder(target):
                    continue
                if not resolve_wiki(target, rel_paths, by_name):
                    kind = "embed" if bang else "link"
                    problems.append(f"{rel}:{lineno}  unresolved {kind}  [[{target}]]")

            for span in code_spans:
                if is_placeholder(span) or not VAULT_PATH_RE.match(span):
                    continue
                if not resolve_path(span, root):
                    problems.append(f"{rel}:{lineno}  missing path      {span}")

            # Ordinary markdown links to files in the vault. MkDocs resolves these
            # relative to the page, so they break in a way wiki-links do not.
            for target in MD_LINK_RE.findall(text):
                target = target.split("#")[0].strip()
                if (not target or is_placeholder(target)
                        or target.startswith(("http://", "https://", "mailto:", "#"))):
                    continue
                # A bare word with no separator and no extension cannot name a file —
                # it is a template placeholder such as [<KEY>](<url>).
                if "/" not in target and "." not in target:
                    continue
                if not (f.parent / target).resolve().exists():
                    problems.append(f"{rel}:{lineno}  missing md link   {target}")

    if not args.quiet:
        for p in problems:
            print(p)
    print(f"\n{len(problems)} unresolved reference(s) "
          f"across {sum(1 for f in files if f.suffix == '.md')} markdown files "
          f"(baseline: {args.baseline})")

    return 1 if len(problems) > args.baseline else 0


if __name__ == "__main__":
    sys.exit(main())
