#!/usr/bin/env bash
set -euo pipefail

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

python - <<'PY'
from flowdelta.delta import DeltaTracker

tracker = DeltaTracker("orders", "cp1")
last = tracker.last_timestamp()
print("Last timestamp:", last)
PY

python - <<'PY'
from flowdelta.scheduler import TaskScheduler
import datetime

runs = []

def job_run():
    stamp = datetime.datetime.utcnow().isoformat(timespec="seconds")
    runs.append(stamp)
    print("tick", stamp)

scheduler = TaskScheduler(frequency=0.1, handler=job_run, max_runs=2)
scheduler.start()
print("Ran", len(runs), "times")
PY

rm -rf ./.flowdelta_data
python - <<'PY'
from flowdelta.storage import Storage

store = Storage("./.flowdelta_data", mkdir=True)
store.write_json("users", {"a": 1})
print(store.read_json("users"))
PY

python - <<'PY'
from flowdelta.delta import run_delta

result = run_delta("orders", "2020-01-01", verbose=True)
print(result)
PY
