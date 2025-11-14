import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from flowdelta.delta import DeltaTracker

tracker = DeltaTracker("orders", "cp1", initial_timestamp="2023-12-31")
assert tracker.last_timestamp() == "2023-12-31"
print("tracker test: ok")
