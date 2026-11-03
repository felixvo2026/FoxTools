import json
import os

class JsonData:
    def __init__(self, path, extension=".json"):
        self.path = self.set_path(path, extension)
        self.data = self.create_file()

    def set_path(self, path, extension):
        if not path.endswith(extension):
            path += extension
        return path

    def create_file(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

        return self.read_file()

    def read_file(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def delete(self, key):
        self.data.pop(key, None)

    def exists(self, key):
        return key in self.data

    def keys(self):
        return list(self.data.keys())

    def values(self):
        return list(self.data.values())

    def items(self):
        return list(self.data.items())

    def update(self, new_data):
        self.data.update(new_data)

    def clear(self):
        self.data.clear()

    def reload(self):
        self.data = self.read_file()