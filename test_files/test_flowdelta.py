#!/usr/bin/env python3
import shutil
import tempfile
from pathlib import Path

from flowdelta.delta import DeltaTracker, run_delta
from flowdelta.scheduler import TaskScheduler
from flowdelta.storage import Storage


def test_delta_tracker():
    tracker = DeltaTracker("orders", "cp1")
    assert tracker.last_timestamp() == "1970-01-01"


def test_task_scheduler():
    runs = []

    def handler():
        runs.append("ok")

    task = TaskScheduler(frequency=0, handler=handler, max_runs=1)
    task.start()
    assert runs == ["ok"]


def test_storage():
    tempdir = Path(tempfile.mkdtemp(prefix="flowdelta-test-"))
    try:
        store = Storage(str(tempdir), mkdir=True)
        payload = {"a": [1, 2, 3]}
        store.write_json("users", payload)
        assert store.read_json("users") == payload
    finally:
        shutil.rmtree(tempdir)


def test_run_delta():
    resp = run_delta("orders", "2020-01-01")
    assert resp["status"] == "ok"
    assert resp["from"] == "2020-01-01"


def main():
    test_delta_tracker()
    test_task_scheduler()
    test_storage()
    test_run_delta()
    print("test_flowdelta.py: all checks passed")


if __name__ == "__main__":
    main()
