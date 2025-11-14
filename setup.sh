#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT=$(cd "$(dirname "$0")" && pwd -P)
cd "$PROJECT_ROOT"

# Create venv if missing
if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

# Activate venv and install requirements
# NOTE: this script is POSIX/Bash — Windows users can run it from Git Bash or adapt for powershell
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Run smoke tests
python -c "from flowdelta.delta import DeltaTracker; print(DeltaTracker(\"orders\", \"cp1\").last_timestamp())"
python -c "from flowdelta.delta import run_delta; print(run_delta(\"orders\", \"2020-01-01\", verbose=True))"
python -c "from flowdelta.storage import Storage; s=Storage(\"tmp_flow\", mkdir=True); s.write_json(\"users\", {\"a\":1}); print(s.read_json(\"users\"))"
python -c "from flowdelta.scheduler import TaskScheduler; x = []; TaskScheduler(0, lambda: x.append(1), max_runs=1).start(); print('ran', x)"

echo "Setup complete. Use .venv for running examples and tests."
