
````
# FlowDelta — Incremental ETL Runner (Corrected)

FlowDelta helps you track deltas for ETL tasks.

---

## Quick Start (Corrected)

```python
from flowdelta.delta import DeltaTracker

tracker = DeltaTracker("orders", "cp1")
last = tracker.last_timestamp()
print("Last timestamp:", last)
````

---

## Creating a Scheduler (Corrected)

```python
from flowdelta.scheduler import TaskScheduler

def job_run():
    print("job complete")

# frequency=5 seconds, handler=job_run, run only once
sched = TaskScheduler(5, job_run, max_runs=1)
sched.start()
```

---

## Saving Data (Corrected)

```python
from flowdelta.storage import Storage

# create directory automatically
s = Storage("/tmp/flow", mkdir=True)

s.write_json("users", {"a": 1})
print(s.read_json("users"))
```

---

## Running a Delta (Corrected)

```python
from flowdelta.delta import run_delta

resp = run_delta("orders", "2020-01-01", verbose=True)
print(resp)
```

```