import os
from flowdelta.storage import Storage


def test_write_read_json(tmp_path):
    path = str(tmp_path / "flow")
    s = Storage(path, mkdir=True)
    s.write_json("users", {"a": 1})
    assert s.read_json("users") == {"a": 1}
