# FlowDelta — Incremental ETL Runner

FlowDelta helps you track deltas for ETL tasks.

## Quick Start

```python
from flowdelta import DeltaTracker

tracker = DeltaTracker(source_name="orders", checkpoint_id="cp1")
last = tracker.last_timestamp()
print("Last timestamp:", last)
```

## Creating a Scheduler

```python
from flowdelta import TaskScheduler

def job_run():
    return "job complete"

sched = TaskScheduler(frequency=5, handler=job_run, max_runs=3)
sched.start()
```

## Saving Data

```python
from flowdelta import Storage
import tempfile

# Use a temporary directory for cross-platform compatibility
with tempfile.TemporaryDirectory() as tmpdir:
    s = Storage(tmpdir, mkdir=True)
    s.write_json("users", {"a": 1})
    print(s.read_json("users"))
```

## Running a Delta

```python
from flowdelta import run_delta

result = run_delta("orders", since_timestamp="2020-01-01", verbose=True)
print(result)
```

## API Reference

### DeltaTracker

```python
DeltaTracker(source_name: str, checkpoint_id: str, *, initial_timestamp=None)
```

**Parameters:**
- `source_name` (str): Name of the source to track
- `checkpoint_id` (str): Unique identifier for the checkpoint
- `initial_timestamp` (str, optional): Initial timestamp value (default: None)

**Methods:**
- `last_timestamp()` → str: Returns the last recorded timestamp (or "1970-01-01" if none exists)

### TaskScheduler

```python
TaskScheduler(frequency: int, handler, *, max_runs=1)
```

**Parameters:**
- `frequency` (int): Time interval in seconds between runs
- `handler` (callable): Function to execute on each tick
- `max_runs` (int, optional): Maximum number of times to run (default: 1)

**Methods:**
- `start()`: Starts the scheduler and runs the handler

### Storage

```python
Storage(path, *, mkdir=False)
```

**Parameters:**
- `path` (str): Directory path for storing files
- `mkdir` (bool, optional): Create the directory if it doesn't exist (default: False)

**Methods:**
- `write_json(key: str, data: dict)`: Serialize and save data as JSON
- `read_json(key: str)` → dict: Load and deserialize JSON data

### run_delta

```python
run_delta(source_name: str, since_timestamp: str, verbose: bool = False) → dict
```

**Parameters:**
- `source_name` (str): Name of the source to run delta for
- `since_timestamp` (str): Start timestamp (format: "YYYY-MM-DD")
- `verbose` (bool, optional): Print debug information (default: False)

**Returns:**
- dict: Status object with "status" and "from" keys
