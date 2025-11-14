# FlowDelta — Incremental ETL Runner

FlowDelta helps you track deltas for ETL tasks.

## Quick Start

```python
from flowdelta import DeltaTracker

tracker = DeltaTracker(source="orders", checkpoint="cp1")
last = tracker.get_last_timestamp()
print("Last timestamp:", last)
```

## Creating a Scheduler

```python
from flowdelta import TaskScheduler

def job_run():
    return "job complete"

sched = TaskScheduler(interval=5, on_tick=job_run)
sched.start()
```

## Saving Data

```python
from flowdelta import Storage

s = Storage("/tmp/flow")
s.save_json("users", {"a": 1})
print(s.load_json("users"))
```

## Running a Delta

```python
from flowdelta import run_delta

run_delta("orders", since="2020-01-01")
```