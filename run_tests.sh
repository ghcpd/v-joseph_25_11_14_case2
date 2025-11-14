#!/usr/bin/env bash
set -euo pipefail

# Ensure venv exists; if not, create it
if [ ! -d ".venv" ]; then
    python -m venv .venv
    if [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate
    elif [ -f ".venv/Scripts/activate" ]; then
        source .venv/Scripts/activate
    fi
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Run tests using venv
.venv/bin/python -m pytest test_files || .venv/Scripts/python -m pytest test_files
