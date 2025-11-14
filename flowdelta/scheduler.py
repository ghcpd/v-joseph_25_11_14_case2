import time

class TaskScheduler:
    def __init__(self, frequency: int, handler, *, max_runs=1):
        self.frequency = frequency
        self.handler = handler
        self.max_runs = max_runs

    def start(self):
        for _ in range(self.max_runs):
            self.handler()
            time.sleep(self.frequency)
