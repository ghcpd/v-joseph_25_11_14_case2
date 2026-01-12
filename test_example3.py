#!/usr/bin/env python
"""Test Example 3: Saving Data"""
import sys
import traceback
import tempfile
import os

def test_example_3():
    print("=" * 60)
    print("TEST 3: Saving Data")
    print("=" * 60)
    try:
        from flowdelta import Storage

        # Use a temp directory to avoid permission issues
        with tempfile.TemporaryDirectory() as tmpdir:
            s = Storage(tmpdir, mkdir=True)
            s.save_json("users", {"a": 1})
            result = s.load_json("users")
            print(result)
            print("✓ PASSED")
            return True
    except Exception as e:
        print("✗ FAILED")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_example_3()
    sys.exit(0 if success else 1)
