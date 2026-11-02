#!/usr/bin/env bash
# Re-fetch nutrisen.eu into a work directory, then run build.py to regenerate the static mirror.
# Usage: tools/fetch.sh <workdir>   (then: python3 tools/build.py <workdir> <outdir>)
set -euo pipefail
W=${1:?workdir}; mkdir -p "$W/raw" "$W/pages"
PAGES=("" medical agriculture agriculture/how-does-it-work agriculture/test-your-field agriculture/from-lab-to-field impressum datenschutzerklarung)
URLS=(); for p in "${PAGES[@]}"; do URLS+=("https://www.nutrisen.eu/$p${p:+/}"); done
URLS+=(https://www.nutrisen.eu/wp-includes/js/wp-emoji-release.min.js https://www.nutrisen.eu/wp-includes/js/wp-emoji-loader.min.js
       https://www.nutrisen.eu/wp-content/plugins/gutenberg/build/styles/block-library/common.min.css
       https://www.nutrisen.eu/wp-content/plugins/gutenberg/build/styles/block-library/classic.min.css
       https://www.nutrisen.eu/wp-content/uploads/go-x/u/ce941c87-b345-45ee-88f0-afa6135ec36f/image-1200x1863.jpg)
( cd "$W/raw" && wget --mirror --page-requisites --no-parent --domains=www.nutrisen.eu,nutrisen.eu -e robots=off \
    --wait=0 --tries=3 --timeout=30 --restrict-file-names=unix \
    --reject-regex='(/feed/?$|/comments/feed|/wp-json|xmlrpc|\?replytocom|/wp-login|/wp-admin|\?p=[0-9]+)' "${URLS[@]}" )
for p in "${PAGES[@]}"; do mkdir -p "$W/pages/$p"; curl -sSfL -o "$W/pages/$p/index.html" "https://www.nutrisen.eu/$p${p:+/}"; done
echo "fetched into $W; now run: python3 tools/build.py $W <outdir>"
