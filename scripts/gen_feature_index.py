#!/usr/bin/env python3
"""Read every feature hub's frontmatter; render it, or check it.

Two jobs, one source of truth (the hubs):

  --write <path>   render the feature table as markdown. The docs site needs
                   this because MkDocs cannot render 00_Project_Info/features.base.
  --check          CI guard: every feature hub must have a non-empty entity,
                   every code must be unique, and every entity note must exist.

No third-party dependencies: the frontmatter this vault writes is a fixed, small
subset of YAML, so it is parsed here rather than pulling in pyyaml.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FEATURES = ROOT / "01_Features"
ENTITIES = ROOT / "00_Project_Info" / "entities"

LINK = re.compile(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]")


def parse_frontmatter(text: str) -> dict | None:
    """Parse the leading --- block. Supports scalars, [a, b] and '- item' lists."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    data: dict = {}
    key = None
    for raw in text[4:end].split("\n"):
        if raw.startswith("  - ") and key:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(raw[4:].strip().strip('"'))
            continue
        m = re.match(r"^([A-Za-z_][\w]*):\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip().strip('"') for v in inner.split(",")] if inner else []
        elif val == "":
            data[key] = []
        else:
            data[key] = val.strip('"')
    return data


def hubs() -> list[tuple[Path, dict]]:
    out = []
    for p in sorted(FEATURES.rglob("*.md")):
        fm = parse_frontmatter(p.read_text(encoding="utf-8"))
        if fm and fm.get("type") == "feature":
            out.append((p, fm))
    return out


def entity_names(fm: dict) -> list[str]:
    names = []
    for v in fm.get("entity") or []:
        m = LINK.search(v)
        if m:
            names.append(m.group(2) or m.group(1))
    return names


def entity_targets(fm: dict) -> list[str]:
    return [m.group(1) for v in (fm.get("entity") or []) if (m := LINK.search(v))]


def render(base: str = ".") -> str:
    """base = the output file's folder, as a vault-relative path. Links are made
    relative to it so they work both in the repo and in the copied docs tree."""
    rows = hubs()
    by_domain: dict[str, list] = {}
    for p, fm in rows:
        by_domain.setdefault(fm.get("domain") or "(standalone)", []).append((p, fm))

    out = [
        "# Feature Registry",
        "",
        "Generated from each feature hub's frontmatter by `scripts/gen_feature_index.py`.",
        "In Obsidian the same data is live in `00_Project_Info/features.base`.",
        "",
    ]
    for domain in sorted(by_domain, key=lambda d: (d == "(standalone)", d)):
        out += [
            f"## {domain}",
            "",
            "| Feature | Code | Platform | Actor | Entity | Status |",
            "| ------- | ---- | -------- | ----- | ------ | ------ |",
        ]
        for p, fm in sorted(by_domain[domain], key=lambda r: r[0].stem):
            ents = ", ".join(entity_names(fm)) or "—"
            href = os.path.relpath(p.relative_to(ROOT).as_posix(), base)
            out.append(
                f"| [{p.stem}]({href}) | `{fm.get('code', '')}` | "
                f"{fm.get('platform', '')} | {fm.get('actor', '')} | {ents} | {fm.get('status', '')} |"
            )
        out.append("")
    out.append(f"_{len(rows)} features._")
    return "\n".join(out) + "\n"


def check() -> int:
    rows = hubs()
    problems: list[str] = []
    warnings: list[str] = []
    seen: dict[str, str] = {}

    for p, fm in rows:
        rel = p.relative_to(ROOT).as_posix()
        code = fm.get("code")
        if not code:
            problems.append(f"{rel}: no code")
        elif code in seen:
            problems.append(f"{rel}: code {code} already used by {seen[code]}")
        else:
            seen[code] = rel

        if not fm.get("entity"):
            # An unanswered question is allowed to sit in the vault, but only when it
            # is written down in the hub itself — never silently.
            if fm.get("entity_pending"):
                warnings.append(f"{rel}: entity unconfirmed — {fm['entity_pending']}")
            else:
                problems.append(f"{rel}: empty entity — impact analysis cannot find this feature")
        for target in entity_targets(fm):
            if not (ENTITIES / f"{target}.md").exists():
                problems.append(f"{rel}: entity link [[{target}]] has no note in 00_Project_Info/entities/")

        for prop, suffix in (("srs", "_srs"), ("ac", "_ac"), ("tc", "_tc")):
            expected = p.parent / f"{p.stem}{suffix}.md"
            if expected.exists() and prop not in fm:
                problems.append(f"{rel}: {expected.name} exists but the hub has no {prop}: property")

    for w in warnings:
        print(f"WARN  {w}")
    for p in problems:
        print(f"ERROR {p}")
    print(f"\n{len(problems)} problem(s), {len(warnings)} warning(s) "
          f"across {len(rows)} feature hubs")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", metavar="PATH", help="render the markdown table to PATH")
    ap.add_argument("--check", action="store_true", help="validate hub metadata (CI guard)")
    ap.add_argument("--base", default=".", metavar="DIR",
                    help="vault-relative folder the output lives in; links are made relative to it")
    args = ap.parse_args()

    if args.check:
        return check()
    if args.write:
        out = Path(args.write)
        out.parent.mkdir(parents=True, exist_ok=True)
        text = render(base=args.base)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {args.write}")
    else:
        print(render(args.base), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
