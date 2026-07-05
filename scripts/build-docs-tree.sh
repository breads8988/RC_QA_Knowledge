#!/usr/bin/env bash
#
# Build ./docs as a tree of symlinks pointing at the numbered knowledge folders
# (00_Project_Info, 01_SRS, ...). This lets MkDocs build the website WITHOUT
# moving any files, so the Obsidian vault and the Claude skills keep working
# against the repo root. ./docs is generated and git-ignored — never edit it
# by hand; edit the real folders at the repo root.
#
# Run automatically by the Makefile (make serve / build / deploy) and by CI.
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

# One symlink per numbered top-level knowledge folder (00_*, 01_*, ...).
for dir in [0-9][0-9]_*/ ; do
  name="${dir%/}"
  [ -d "$name" ] || continue
  ln -s "../$name" "docs/$name"
done

echo "docs/ tree rebuilt:"
ls -l docs
