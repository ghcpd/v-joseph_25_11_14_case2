#!/usr/bin/env python
"""Test Example 4: Running a Delta"""
import sys
import traceback

def test_example_4():
    print("=" * 60)
    print("TEST 4: Running a Delta")
    print("=" * 60)
    try:
        from flowdelta import run_delta

        run_delta("orders", since="2020-01-01")
        print("✓ PASSED")
        return True
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_example_4()
    sys.exit(0 if success else 1)
