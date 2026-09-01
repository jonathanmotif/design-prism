#!/usr/bin/env bash
# Push design-prism to GitHub. Run after creating the empty repo at:
# https://github.com/jonathanmotif/design-prism

set -euo pipefail
cd "$(dirname "$0")"

if ! git remote get-url origin &>/dev/null; then
  git remote add origin https://github.com/jonathanmotif/design-prism.git
fi

echo "Pushing to origin main..."
git push -u origin main

echo "Done: https://github.com/jonathanmotif/design-prism"
