from flowdelta.delta import DeltaTracker


def test_last_timestamp_default():
    tracker = DeltaTracker("orders", "cp1")
    assert tracker.last_timestamp() == "1970-01-01"
