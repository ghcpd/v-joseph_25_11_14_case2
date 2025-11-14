import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from flowdelta.delta import run_delta

result = run_delta("orders", "2020-01-01", verbose=False)
assert result["status"] == "ok"
assert result["from"] == "2020-01-01"
print("run_delta test: ok")
