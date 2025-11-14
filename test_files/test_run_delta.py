from flowdelta.delta import run_delta


def test_run_delta_return():
    r = run_delta("orders", "2020-01-01")
    assert r["status"] == "ok"
    assert r["from"] == "2020-01-01"
