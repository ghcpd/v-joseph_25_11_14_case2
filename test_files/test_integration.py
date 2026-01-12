#!/usr/bin/env python
"""
Integration Test - Run all corrected examples from corrected_readme.md
"""
import sys
import os
import traceback
import tempfile

# Add parent directory to path so we can import flowdelta
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_all_examples():
    """Test all examples from the corrected README"""
    print("\n" + "=" * 70)
    print("INTEGRATION TEST: All Corrected README Examples")
    print("=" * 70 + "\n")
    
    all_passed = True
    
    # Example 1: Quick Start
    print("EXAMPLE 1: Quick Start")
    print("-" * 70)
    try:
        from flowdelta import DeltaTracker

        tracker = DeltaTracker(source_name="orders", checkpoint_id="cp1")
        last = tracker.last_timestamp()
        print("Last timestamp:", last)
        print("✓ PASSED\n")
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        print()
        all_passed = False
    
    # Example 2: Creating a Scheduler
    print("EXAMPLE 2: Creating a Scheduler")
    print("-" * 70)
    try:
        from flowdelta import TaskScheduler

        def job_run():
            return "job complete"

        sched = TaskScheduler(frequency=1, handler=job_run, max_runs=2)
        sched.start()
        print("✓ PASSED\n")
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        print()
        all_passed = False
    
    # Example 3: Saving Data
    print("EXAMPLE 3: Saving Data")
    print("-" * 70)
    try:
        from flowdelta import Storage

        # Use a temporary directory for cross-platform compatibility
        with tempfile.TemporaryDirectory() as tmpdir:
            s = Storage(tmpdir, mkdir=True)
            s.write_json("users", {"a": 1})
            result = s.read_json("users")
            print(result)
        print("✓ PASSED\n")
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        print()
        all_passed = False
    
    # Example 4: Running a Delta
    print("EXAMPLE 4: Running a Delta")
    print("-" * 70)
    try:
        from flowdelta import run_delta

        result = run_delta("orders", since_timestamp="2020-01-01", verbose=True)
        print(result)
        print("✓ PASSED\n")
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        print()
        all_passed = False
    
    print("=" * 70)
    if all_passed:
        print("✓ ALL EXAMPLES PASSED")
        print("=" * 70)
        return True
    else:
        print("✗ SOME EXAMPLES FAILED")
        print("=" * 70)
        return False

if __name__ == "__main__":
    success = test_all_examples()
    sys.exit(0 if success else 1)
