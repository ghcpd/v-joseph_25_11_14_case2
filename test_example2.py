#!/usr/bin/env python
"""Test Example 2: Creating a Scheduler"""
import sys
import traceback

def test_example_2():
    print("=" * 60)
    print("TEST 2: Creating a Scheduler")
    print("=" * 60)
    try:
        from flowdelta import TaskScheduler

        def job_run():
            return "job complete"

        sched = TaskScheduler(interval=5, on_tick=job_run)
        sched.start()
        print("✓ PASSED")
        return True
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_example_2()
    sys.exit(0 if success else 1)
