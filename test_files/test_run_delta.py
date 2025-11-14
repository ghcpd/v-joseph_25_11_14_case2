from flowdelta.delta import run_delta


def test_run_delta_returns_status_ok():
    res = run_delta("orders", "2025-01-01")
    assert res == {"status":"ok", "from":"2025-01-01"}
