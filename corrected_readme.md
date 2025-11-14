# FlowDelta — Incremental ETL Runner (Corrected)
FlowDelta helps you track deltas for ETL tasks. The README examples have been corrected to reflect the actual API.

## Quick Start
```python
from flowdelta.delta import DeltaTracker

# Create a new tracker (use `source_name` and `checkpoint_id` for clarity):
tracker = DeltaTracker(source_name="orders", checkpoint_id="cp1")
last = tracker.last_timestamp()  # method is `last_timestamp()` in the implementation
print("Last timestamp:", last)
```

## Creating a Scheduler
```python
from flowdelta.scheduler import TaskScheduler

# A simple job that prints a message
def job_run():
    print("job complete")

# The scheduler constructor expects `frequency` and `handler`. Set `max_runs` to avoid long-running loops in examples
sched = TaskScheduler(frequency=5, handler=job_run, max_runs=1)
sched.start()
```

## Saving Data
```python
import os
from flowdelta.storage import Storage

# Use a local test path (e.g. tmp_flow) and let Storage create the directory with mkdir=True
storage_path = os.path.join(os.getcwd(), "tmp_flow")
s = Storage(storage_path, mkdir=True)
s.write_json("users", {"a": 1})
print(s.read_json("users"))
```

## Running a Delta
```python
from flowdelta.delta import run_delta

# The function takes (source_name, since_timestamp, verbose=False)
print(run_delta("orders", "2020-01-01", verbose=True))
```

Notes:
- The package does not re-export symbols at the top-level, so import submodules explicitly (e.g. `from flowdelta.delta import DeltaTracker`).
- Use platform-appropriate paths (or construct them with `os.path`) for cross-platform examples.
- Many API elements have changed names — prefer the forms above to match implementation.
