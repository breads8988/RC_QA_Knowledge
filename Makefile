# RC QA Knowledge — docs website (MkDocs Material)
#
# One-time setup:   make install
# Preview locally:  make serve     -> open http://127.0.0.1:8000
# Build static site: make build     -> output in ./site
# Publish to web:   make deploy    -> GitHub Pages (gh-pages branch)

VENV   := .venv
PY     := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip
MKDOCS := $(VENV)/bin/mkdocs

# Silence mkdocs-material's stderr "MkDocs 2.0" campaign banner (console-only,
# never in the built site).
export NO_MKDOCS_2_WARNING := true

.PHONY: install links serve build deploy clean

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-docs.txt

links:
	./scripts/build-docs-tree.sh

serve: links
	$(MKDOCS) serve

build: links
	$(MKDOCS) build

deploy: links
	$(MKDOCS) gh-deploy --force

clean:
	rm -rf docs site
