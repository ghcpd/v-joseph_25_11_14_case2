#!/usr/bin/env bash
set -euo pipefail

if [ ! -f .venv/bin/python ]; then
  echo "Virtual environment not found. Run ./setup.sh first." >&2
  exit 1
fi

source .venv/bin/activate
for test_file in test_files/*.py; do
  echo "Running $test_file"
  python "$test_file"
done
