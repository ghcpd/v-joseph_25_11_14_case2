# FlowDelta — Incremental ETL Runner (Corrected)

FlowDelta helps you track deltas for incremental ETL tasks by providing helpers for checkpoints, scheduling, storage, and delta execution.

## Quick Start

```python
from flowdelta.delta import DeltaTracker

# DeltaTracker expects (source_name, checkpoint_id) and exposes `.last_timestamp()`.
tracker = DeltaTracker("orders", "cp1")
last = tracker.last_timestamp()
print("Last timestamp:", last)
```

## Creating a Scheduler

```python
from flowdelta.scheduler import TaskScheduler

def job_run():
    print("job complete")

# frequency is the wait time between runs; max_runs defaults to 1.
sched = TaskScheduler(frequency=0, handler=job_run, max_runs=1)
sched.start()
```

## Saving Data

```python
from flowdelta.storage import Storage

# Storage will auto-create the directory when mkdir=True.
s = Storage("tmp_flow_storage", mkdir=True)
s.write_json("users", {"a": 1})
print(s.read_json("users"))
```

## Running a Delta

```python
from flowdelta.delta import run_delta

resp = run_delta("orders", "2020-01-01", verbose=True)
print("Delta response:", resp)
```
