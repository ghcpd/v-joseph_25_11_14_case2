import pathlib
import shutil
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from flowdelta.storage import Storage

root = tempfile.mkdtemp(prefix="flowdelta_")
try:
    store = Storage(root, mkdir=True)
    store.write_json("users", {"a": 1})
    assert store.read_json("users") == {"a": 1}
    print("storage test: ok")
finally:
    shutil.rmtree(root)
