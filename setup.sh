#!/usr/bin/env bash
set -euo pipefail

# Create virtualenv and install dependencies
python -m venv .venv
# Activate venv depending on shell
if [ -f ".venv/bin/activate" ]; then
    # POSIX shell
    source .venv/bin/activate
elif [ -f ".venv/Scripts/activate" ]; then
    # Windows bash
    source .venv/Scripts/activate
fi

pip install --upgrade pip
pip install -r requirements.txt

# Run a small script that exercises the corrected README examples
echo "Running corrected README examples..."
.venv/bin/python - << 'PYCODE' || .venv/Scripts/python - << 'PYCODE'
from flowdelta.delta import DeltaTracker, run_delta
from flowdelta.scheduler import TaskScheduler
from flowdelta.storage import Storage

tracker = DeltaTracker("orders", "cp1")
print("Last:", tracker.last_timestamp())

def job_run():
    print("job complete")

sched = TaskScheduler(frequency=0, handler=job_run, max_runs=1)
sched.start()

s = Storage("./flowtmp", mkdir=True)
s.write_json("users", {"a": 1})
print(s.read_json("users"))

print(run_delta("orders", "2020-01-01", verbose=True))
PYCODE
