import json, os

class Storage:
    def __init__(self, path, *, mkdir=False):
        self.path = path
        if mkdir and not os.path.exists(path):
            os.makedirs(path)

    def write_json(self, key, data):
        fp = os.path.join(self.path, f"{key}.json")
        with open(fp, "w") as f:
            json.dump(data, f)

    def read_json(self, key):
        fp = os.path.join(self.path, f"{key}.json")
        with open(fp) as f:
            return json.load(f)
