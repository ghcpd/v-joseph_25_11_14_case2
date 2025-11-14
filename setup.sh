#!/usr/bin/env bash
set -euo pipefail

# Create or refresh the virtual environment.
python3 -m venv .venv
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt

echo "Running the corrected FlowDelta snippets..."
./.venv/bin/python - <<'PY'
from flowdelta.delta import DeltaTracker, run_delta
from flowdelta.scheduler import TaskScheduler
from flowdelta.storage import Storage

# Quick start
tracker = DeltaTracker("orders", "cp1")
print("Quick Start last timestamp:", tracker.last_timestamp())

# Scheduler example
def job_run():
    print("Scheduled job complete")

sched = TaskScheduler(frequency=0, handler=job_run, max_runs=1)
sched.start()

# Storage example
storage_path = "tmp_flow_storage"
s = Storage(storage_path, mkdir=True)
s.write_json("users", {"a": 1})
print("Storage read:", s.read_json("users"))

# Delta run example
resp = run_delta("orders", "2020-01-01", verbose=True)
print("Delta response:", resp)
PY

rm -rf tmp_flow_storage
