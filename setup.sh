#!/bin/bash
# FlowDelta Setup Script
# This script bootstraps the environment and runs examples

set -e

echo "=========================================="
echo "FlowDelta Setup & Demo"
echo "=========================================="
echo

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Step 1: Create virtual environment
echo "Step 1: Creating virtual environment..."
if [ -d ".venv" ]; then
    echo ".venv already exists, skipping creation"
else
    python -m venv .venv
    echo "✓ Virtual environment created"
fi
echo

# Step 2: Activate and upgrade pip
echo "Step 2: Upgrading pip..."
if [ -f ".venv/bin/python" ]; then
    PYTHON=".venv/bin/python"
    PIP=".venv/bin/pip"
else
    PYTHON=".venv/Scripts/python.exe"
    PIP=".venv/Scripts/pip.exe"
fi

$PIP install --upgrade pip setuptools
echo "✓ Pip upgraded"
echo

# Step 3: Install requirements (none for this project, but included for completeness)
echo "Step 3: Installing requirements..."
if [ -f "requirements.txt" ]; then
    $PIP install -r requirements.txt
    echo "✓ Requirements installed"
else
    echo "No requirements.txt found, skipping"
fi
echo

# Step 4: Run the integration test
echo "Step 4: Running integration test..."
echo "=========================================="
echo
$PYTHON test_files/test_integration.py
TEST_RESULT=$?
echo
echo "=========================================="
echo

if [ $TEST_RESULT -eq 0 ]; then
    echo "✓ Setup completed successfully!"
    echo "✓ All corrected examples run without errors"
    echo
    echo "To run individual tests, use:"
    echo "  ./run_tests.sh"
else
    echo "✗ Setup failed! Some tests did not pass."
    exit 1
fi
