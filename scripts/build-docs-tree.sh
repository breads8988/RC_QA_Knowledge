#!/usr/bin/env bash
#
# Build ./docs as a tree of symlinks (plus a few auto-generated pages) pointing
# at the numbered knowledge folders (00_Project_Info, 01_SRS, ...). This lets
# MkDocs build the website WITHOUT moving any files, so the Obsidian vault and
# the Claude skills keep working against the repo root. ./docs is generated and
# git-ignored — never edit it by hand; edit the real folders at the repo root.
#
# Special case: 01_SRS holds Figma screenshots (figma/*.png) and, later,
# written SRS pages (epic.md). MkDocs only shows markdown in the menu, so this
# script AUTO-GENERATES a gallery page per feature that embeds its Figma images.
# Result: any feature (now or future) shows up on the site automatically —
# just drop images into 01_SRS/<feature>/figma/ and rebuild. No manual work.
#
# Run automatically by the Makefile (make serve / build / deploy) and by CI.
# Written for bash 3.2 (macOS default): no arrays under `set -u`.
set -euo pipefail
shopt -s nullglob

# Move to repo root (this script lives in scripts/).
cd "$(dirname "$0")/.."

rm -rf docs
mkdir docs

# Homepage: reuse the repo README.
if [ -f README.md ]; then
  ln -s ../README.md docs/index.md
fi

# ---------------------------------------------------------------------------
# 01_SRS — generate a Figma gallery page per feature (see header comment).
# ---------------------------------------------------------------------------
build_srs() {
  local src="01_SRS"
  [ -d "$src" ] || return 0

  mkdir -p "docs/$src"
  {
    echo "# SRS — Software Requirements"
    echo
    echo "Reference screens (Figma) and written requirements, grouped by feature."
  } > "docs/$src/index.md"

  local feat name title base md img has_md has_figma
  for feat in "$src"/*/ ; do
    [ -d "$feat" ] || continue
    name="$(basename "$feat")"

    has_md=0
    for md in "$feat"*.md; do
      if [ -f "$md" ]; then has_md=1; break; fi
    done
    has_figma=0
    for img in "${feat}figma"/*.png "${feat}figma"/*.jpg "${feat}figma"/*.jpeg; do
      if [ -f "$img" ]; then has_figma=1; break; fi
    done

    # Skip a feature that has neither written pages nor screenshots.
    if [ "$has_md" -eq 0 ] && [ "$has_figma" -eq 0 ]; then continue; fi

    mkdir -p "docs/$src/$name"

    # Symlink any real markdown (e.g. epic.md written later) so it shows too.
    for md in "$feat"*.md; do
      [ -f "$md" ] || continue
      base="$(basename "$md")"
      ln -s "../../../$src/$name/$base" "docs/$src/$name/$base"
    done

    # If there are screenshots, symlink the figma folder and build a gallery.
    if [ "$has_figma" -eq 1 ]; then
      ln -s "../../../$src/$name/figma" "docs/$src/$name/figma"
    fi

    title="$(echo "$name" | tr '_' ' ')"
    {
      echo "# ${title} — Screens (Figma)"
      echo
      if [ "$has_figma" -eq 1 ]; then
        for img in "${feat}figma"/*.png "${feat}figma"/*.jpg "${feat}figma"/*.jpeg; do
          [ -f "$img" ] || continue
          base="$(basename "$img")"
          # Angle brackets keep spaces in filenames valid in Markdown.
          echo "![${base}](<figma/${base}>)"
          echo
        done
      else
        echo "_No Figma screens yet for this feature._"
      fi
    } > "docs/$src/$name/index.md"
  done
}

build_srs

# ---------------------------------------------------------------------------
# Every other numbered top-level folder: plain whole-folder symlink.
# ---------------------------------------------------------------------------
for dir in [0-9][0-9]_*/ ; do
  name="${dir%/}"
  [ -d "$name" ] || continue
  [ "$name" = "01_SRS" ] && continue          # handled above
  ln -s "../$name" "docs/$name"
done

echo "docs/ tree rebuilt:"
find docs -maxdepth 3 | sort
