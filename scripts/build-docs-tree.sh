#!/usr/bin/env bash
#
# Build ./docs as the MkDocs source tree from the vault folders at the repo root
# (00_Project_Info, 01_Features, 04_Templates). This lets MkDocs build the
# website WITHOUT moving any files, so the Obsidian vault and the Claude skills
# keep working against the repo root. ./docs is generated and git-ignored —
# never edit it by hand; edit the real folders at the repo root.
#
# The tree is COPIED, not symlinked. The roamlinks plugin walks docs/ to resolve
# [[wiki-links]] and does not follow symlinked directories, so a symlink tree
# left every wiki-link on the site unresolved.
#
# Two pages are generated because Obsidian-only formats do not render in MkDocs:
#   00_Project_Info/features.md   <- from each feature hub's frontmatter
#                                    (features.base is an Obsidian Bases file)
#   01_Features/index.md          <- the feature tree, for the site nav
#
# Run automatically by the Makefile (make serve / build / deploy) and by CI.
# Written for bash 3.2 (macOS default).
set -euo pipefail
shopt -s nullglob

cd "$(dirname "$0")/.."

rm -rf docs
mkdir docs

# Homepage: reuse the repo README. CLAUDE.md is the business layer — notes link
# to it, so it has to be a page on the site too.
[ -f README.md ] && cp README.md docs/index.md
[ -f CLAUDE.md ] && cp CLAUDE.md docs/CLAUDE.md

for dir in [0-9][0-9]_*/ ; do
  name="${dir%/}"
  cp -R "$name" "docs/$name"
done

# .base files are Obsidian-only; MkDocs would serve them as raw downloads.
find docs -name "*.base" -delete

# Registry page for the site, built from the same frontmatter Bases reads.
python3 scripts/gen_feature_index.py --write docs/00_Project_Info/features.md --base 00_Project_Info >/dev/null

# ---------------------------------------------------------------------------
# 01_Features/index.md — the feature tree. A folder is a FEATURE when it holds
# <name>_srs.md, otherwise it is a DOMAIN holding feature folders.
# ---------------------------------------------------------------------------
build_feature_index() {
  local src="01_Features"
  [ -d "$src" ] || return 0

  {
    echo "# Features"
    echo
    echo "Each feature owns one folder: its hub, SRS, acceptance criteria, test cases and screenshots."
    echo
  } > "docs/$src/index.md"

  local d name sub subname
  for d in "$src"/*/ ; do
    name="$(basename "$d")"
    if [ -f "$d$name-srs.md" ] || [ -f "$d${name}_srs.md" ]; then
      # standalone feature
      {
        echo "- **${name}** — [hub](${name}/${name}.md) ·"
        echo "  [SRS](${name}/${name}_srs.md)$([ -f "$d${name}_ac.md" ] && echo " · [AC](${name}/${name}_ac.md)")$([ -f "$d${name}_tc.md" ] && echo " · [TC](${name}/${name}_tc.md)")"
      } >> "docs/$src/index.md"
    else
      # domain
      echo "" >> "docs/$src/index.md"
      echo "## ${name}" >> "docs/$src/index.md"
      echo "" >> "docs/$src/index.md"
      for sub in "$d"*/ ; do
        subname="$(basename "$sub")"
        [ -f "$sub${subname}_srs.md" ] || continue
        {
          echo "- **${subname}** — [hub](${name}/${subname}/${subname}.md) ·"
          echo "  [SRS](${name}/${subname}/${subname}_srs.md)$([ -f "$sub${subname}_ac.md" ] && echo " · [AC](${name}/${subname}/${subname}_ac.md)")$([ -f "$sub${subname}_tc.md" ] && echo " · [TC](${name}/${subname}/${subname}_tc.md)")"
        } >> "docs/$src/index.md"
      done
    fi
  done
}

build_feature_index

echo "docs/ tree rebuilt:"
find docs -maxdepth 2 -name "*.md" | sort | head -20
