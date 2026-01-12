#!/usr/bin/env python
"""Test 2: TaskScheduler - Corrected Version"""
import sys
import os
import traceback
from io import StringIO

# Add parent directory to path so we can import flowdelta
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_taskscheduler():
    """Test the corrected TaskScheduler example from corrected_readme.md"""
    print("=" * 70)
    print("TEST 2: TaskScheduler (Corrected)")
    print("=" * 70)
    
    try:
        from flowdelta import TaskScheduler
        
        # Track calls
        call_count = [0]
        
        def job_run():
            call_count[0] += 1
            return f"job complete {call_count[0]}"
        
        # Corrected parameters
        sched = TaskScheduler(frequency=1, handler=job_run, max_runs=3)
        print(f"✓ Created scheduler with frequency=1s, max_runs=3")
        
        # Verify attributes
        assert sched.frequency == 1, "frequency should be 1"
        assert sched.max_runs == 3, "max_runs should be 3"
        print(f"✓ Scheduler attributes are correct")
        
        # Start the scheduler (will take ~3 seconds)
        sched.start()
        print(f"✓ Scheduler executed successfully")
        
        # Verify it ran the correct number of times
        assert call_count[0] == 3, f"Expected 3 runs, got {call_count[0]}"
        print(f"✓ Handler called correct number of times: {call_count[0]}")
        
        print("✓ PASSED: TaskScheduler\n")
        return True
    except Exception as e:
        print("✗ FAILED: TaskScheduler")
        traceback.print_exc()
        print()
        return False

if __name__ == "__main__":
    success = test_taskscheduler()
    sys.exit(0 if success else 1)
