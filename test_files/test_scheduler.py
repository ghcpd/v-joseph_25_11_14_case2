from flowdelta.scheduler import TaskScheduler


def test_scheduler_runs_handler_once():
    calls = []
    def handler():
        calls.append(1)

    TaskScheduler(0, handler, max_runs=1).start()
    assert len(calls) == 1
