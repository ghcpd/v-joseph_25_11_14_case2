#!/usr/bin/env python
"""Test 4: run_delta - Corrected Version"""
import sys
import os
import traceback

# Add parent directory to path so we can import flowdelta
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_run_delta():
    """Test the corrected run_delta example from corrected_readme.md"""
    print("=" * 70)
    print("TEST 4: run_delta (Corrected)")
    print("=" * 70)
    
    try:
        from flowdelta import run_delta
        
        # Corrected parameter name
        result = run_delta("orders", since_timestamp="2020-01-01", verbose=True)
        print(f"✓ run_delta() returned: {result}")
        
        # Verify return type and structure
        assert isinstance(result, dict), "run_delta should return a dict"
        print(f"✓ Return type is correct: {type(result).__name__}")
        
        # Verify response structure
        assert "status" in result, "Response should have 'status' key"
        assert "from" in result, "Response should have 'from' key"
        print(f"✓ Response structure is correct")
        
        # Verify values
        assert result["status"] == "ok", f"Expected status 'ok', got {result['status']}"
        assert result["from"] == "2020-01-01", f"Expected from '2020-01-01', got {result['from']}"
        print(f"✓ Response values are correct")
        
        # Test without verbose
        result2 = run_delta("users", since_timestamp="2024-01-01")
        print(f"✓ run_delta() without verbose works")
        
        print("✓ PASSED: run_delta\n")
        return True
    except Exception as e:
        print("✗ FAILED: run_delta")
        traceback.print_exc()
        print()
        return False

if __name__ == "__main__":
    success = test_run_delta()
    sys.exit(0 if success else 1)
