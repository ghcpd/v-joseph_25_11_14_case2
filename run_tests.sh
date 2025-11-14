#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d ".venv" ]]; then
  echo ".venv not found; run ./setup.sh first" >&2
  exit 1
fi

# Ensure the repository root is in PYTHONPATH so the namespace package can be imported.
export PYTHONPATH="$(pwd)"
./.venv/bin/python -m test_files.test_flowdelta
