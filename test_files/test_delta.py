import os
from flowdelta.delta import DeltaTracker


def test_last_timestamp_default():
    t = DeltaTracker("a", "b")
    assert t.last_timestamp() == "1970-01-01"


def test_last_timestamp_initial():
    t = DeltaTracker("a", "b", initial_timestamp="2020-01-01")
    assert t.last_timestamp() == "2020-01-01"
