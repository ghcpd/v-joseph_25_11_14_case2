import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from flowdelta.scheduler import TaskScheduler

counter = {"runs": 0}

def handler():
    counter["runs"] += 1

scheduler = TaskScheduler(frequency=0, handler=handler, max_runs=3)
scheduler.start()
assert counter["runs"] == 3
print("scheduler test: ok")
