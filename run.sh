#!/usr/bin/env bash
set -euo pipefail

PORT=${1:-8000}

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required to run the static server" >&2
  exit 1
fi

python3 -m http.server "$PORT"
