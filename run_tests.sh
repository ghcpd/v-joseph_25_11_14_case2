#!/bin/bash
# FlowDelta Test Runner
# This script runs all tests to verify the corrected documentation

set -e

echo "=========================================="
echo "FlowDelta Test Suite"
echo "=========================================="
echo

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Determine the Python executable
if [ -f ".venv/bin/python" ]; then
    PYTHON=".venv/bin/python"
elif [ -f ".venv/Scripts/python.exe" ]; then
    PYTHON=".venv/Scripts/python.exe"
else
    PYTHON="python"
fi

echo "Using Python: $PYTHON"
echo

# Run individual tests
echo "Running individual unit tests..."
echo "=========================================="
echo

$PYTHON test_files/test_deltatracker.py || EXIT_CODE=$?
$PYTHON test_files/test_taskscheduler.py || EXIT_CODE=$?
$PYTHON test_files/test_storage.py || EXIT_CODE=$?
$PYTHON test_files/test_run_delta.py || EXIT_CODE=$?

echo
echo "Running integration test..."
echo "=========================================="
echo

$PYTHON test_files/test_integration.py || EXIT_CODE=$?

echo
echo "=========================================="
echo "Test suite completed"
echo "=========================================="

exit ${EXIT_CODE:-0}
