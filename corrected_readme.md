# FlowDelta — Incremental ETL Runner

FlowDelta is a tiny helper library for running incremental ETL jobs. It currently ships three building blocks:

* `flowdelta.delta.DeltaTracker` to keep track of the last processed timestamp.
* `flowdelta.scheduler.TaskScheduler` to repeatedly execute a callable.
* `flowdelta.storage.Storage` to persist JSON payloads.

## Environment setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

All examples below assume the commands are executed from the repository root with the virtual environment activated (or by explicitly invoking `.venv/bin/python`).

## Quick start: tracking a delta

```python
from flowdelta.delta import DeltaTracker

tracker = DeltaTracker("orders", "cp1")
last = tracker.last_timestamp()
print("Last timestamp:", last)
```

## Scheduling a repeating task

```python
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
```

## Saving and loading JSON payloads

```python
from flowdelta.storage import Storage

store = Storage("./.flowdelta_data", mkdir=True)
store.write_json("users", {"a": 1})
print(store.read_json("users"))
```

## Running a delta task

```python
from flowdelta.delta import run_delta

result = run_delta("orders", "2020-01-01", verbose=True)
print(result)
```
