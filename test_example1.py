#!/usr/bin/env python
"""Test Example 1: Quick Start - DeltaTracker"""
import sys
import traceback

def test_example_1():
    print("=" * 60)
    print("TEST 1: Quick Start - DeltaTracker")
    print("=" * 60)
    try:
        from flowdelta import DeltaTracker

        tracker = DeltaTracker(source="orders", checkpoint="cp1")
        last = tracker.get_last_timestamp()
        print("Last timestamp:", last)
        print("✓ PASSED")
        return True
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_example_1()
    sys.exit(0 if success else 1)
