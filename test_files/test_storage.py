import os
from flowdelta.storage import Storage


def test_write_and_read_json(tmp_path):
    d = tmp_path / "flowtmp"
    path = str(d)
    s = Storage(path, mkdir=True)
    s.write_json("users", {"a": 1})
    assert s.read_json("users") == {"a": 1}

