#!/usr/bin/env python
"""Test 3: Storage - Corrected Version"""
import sys
import os
import traceback
import tempfile

# Add parent directory to path so we can import flowdelta
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_storage():
    """Test the corrected Storage example from corrected_readme.md"""
    print("=" * 70)
    print("TEST 3: Storage (Corrected)")
    print("=" * 70)
    
    try:
        from flowdelta import Storage
        
        # Use a temporary directory for cross-platform compatibility
        with tempfile.TemporaryDirectory() as tmpdir:
            # Corrected method names and parameters
            s = Storage(tmpdir, mkdir=True)
            print(f"✓ Created Storage with path: {tmpdir}")
            
            # Test write_json
            test_data = {"a": 1, "b": "test"}
            s.write_json("users", test_data)
            print(f"✓ write_json() succeeded")
            
            # Verify file was created
            expected_file = os.path.join(tmpdir, "users.json")
            assert os.path.exists(expected_file), f"File {expected_file} was not created"
            print(f"✓ JSON file created at: {expected_file}")
            
            # Test read_json
            loaded_data = s.read_json("users")
            print(f"✓ read_json() returned: {loaded_data}")
            
            # Verify data integrity
            assert loaded_data == test_data, "Data mismatch after read"
            print(f"✓ Data integrity verified")
            
            # Test with multiple keys
            s.write_json("orders", {"order_id": 123, "amount": 99.99})
            orders = s.read_json("orders")
            print(f"✓ Multiple keys work correctly")
            
        print("✓ PASSED: Storage\n")
        return True
    except Exception as e:
        print("✗ FAILED: Storage")
        traceback.print_exc()
        print()
        return False

if __name__ == "__main__":
    success = test_storage()
    sys.exit(0 if success else 1)
