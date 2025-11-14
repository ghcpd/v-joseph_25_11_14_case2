from flowdelta.scheduler import TaskScheduler


def test_scheduler_calls_handler_three_times():
    calls = []
    def h():
        calls.append(1)

    sched = TaskScheduler(frequency=0, handler=h, max_runs=3)
    sched.start()
    assert len(calls) == 3
