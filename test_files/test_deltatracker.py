#!/usr/bin/env python
"""Test 1: DeltaTracker - Corrected Version"""
import sys
import os
import traceback

# Add parent directory to path so we can import flowdelta
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_deltatracker():
    """Test the corrected DeltaTracker example from corrected_readme.md"""
    print("=" * 70)
    print("TEST 1: DeltaTracker (Corrected)")
    print("=" * 70)
    
    try:
        from flowdelta import DeltaTracker

        # Corrected parameters
        tracker = DeltaTracker(source_name="orders", checkpoint_id="cp1")
        last = tracker.last_timestamp()
        print(f"✓ Last timestamp: {last}")
        
        # Verify return type
        assert isinstance(last, str), "last_timestamp() should return a string"
        print(f"✓ Return type is correct: {type(last).__name__}")
        
        # Test with initial_timestamp
        tracker2 = DeltaTracker(source_name="users", checkpoint_id="cp2", initial_timestamp="2024-01-15")
        last2 = tracker2.last_timestamp()
        print(f"✓ Initial timestamp: {last2}")
        assert last2 == "2024-01-15", "initial_timestamp should be used"
        
        print("✓ PASSED: DeltaTracker\n")
        return True
    except Exception as e:
        print("✗ FAILED: DeltaTracker")
        traceback.print_exc()
        print()
        return False

if __name__ == "__main__":
    success = test_deltatracker()
    sys.exit(0 if success else 1)
