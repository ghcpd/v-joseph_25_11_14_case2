# FlowDelta — Incremental ETL Runner (Corrected)

Quick notes:
- This README reflects the actual implementation in `flowdelta/`.
- Import class and functions from their modules (`flowdelta.delta`, `flowdelta.scheduler`, `flowdelta.storage`).

## Quick Start

```python
from flowdelta.delta import DeltaTracker

# DeltaTracker takes `source_name` and `checkpoint_id` positional arguments.
tracker = DeltaTracker("orders", "cp1")
last = tracker.last_timestamp()
print("Last timestamp:", last)
```

## Creating a Scheduler

```python
from flowdelta.scheduler import TaskScheduler

def job_run():
    print("job complete")

# TaskScheduler uses `frequency` and `handler` as parameters, with optional `max_runs`.
sched = TaskScheduler(frequency=5, handler=job_run, max_runs=1)
sched.start()
```

## Saving Data

```python
from flowdelta.storage import Storage

# Storage takes a path and an optional mkdir flag.
s = Storage("./flowtmp", mkdir=True)
s.write_json("users", {"a": 1})
print(s.read_json("users"))
```

## Running a Delta

```python
from flowdelta.delta import run_delta

# run_delta has signature (source_name, since_timestamp, verbose=False)
run_delta("orders", "2020-01-01", verbose=True)
```

## Notes
- If you prefer `from flowdelta import ...` to work, add an `__init__.py` to export the modules.
- For tests, use `pytest` and set `frequency=0` for fast scheduling tests.
