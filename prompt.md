# Task: Documentation Accuracy & Tutorial Verification

You are provided with a Python mini-framework for incremental ETL tasks named `FlowDelta`.

Your job is to evaluate documentation correctness for the following error sub-types:

### Sub-Types to Test
1. **Incorrect Documentation**
   - Wrong parameter names
   - Wrong default values
   - Wrong return type
   - Wrong value ranges
   - Outdated API description

2. **Tutorial Examples That Don’t Run**
   - Code fails due to missing imports
   - Execution errors
   - Incorrect arguments
   - Wrong execution order
   - Mismatched function signatures

---

## Your Tasks

1. Use `.venv` as the virtual environment.
2. Run every example under `README.md`.
3. Compare the README examples against the actual implementation in `flowdelta/`.
4. Identify **every mismatch** and show:
   - Actual error traceback
   - The incorrect documentation snippet
   - The corrected version

---

## Expected Output

You must generate all of the following:

### 1. `defects.txt`
- Each discovered problem
- Categorized by subtype:
  - Incorrect docs
  - Failing tutorial examples
- Include actual Python error traces

### 2. `corrected_readme.md`
- A fully corrected version of the README
- All examples must run successfully in a clean `.venv`

### 3. `requirements.txt`
- All dependencies needed for the library to run and be tested

### 4. `setup.sh`
- Bash script to bootstrap everything:
  - Create `.venv`
  - Install requirements
  - Run examples

### 5. `test_files/`
- Minimal test scripts to ensure the library works after corrections

### 6. `run_tests.sh`
- One-button test runner

If a README example does not run as written, you **must**:
- Document it in `defects.txt`
- Fix it in `corrected_readme.md`