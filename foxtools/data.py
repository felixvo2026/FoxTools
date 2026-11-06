import json
import os

class JsonData:
    """A class to manage your Json File."""
    def __init__(self, path, extension=".json", auto_save=False):
        self.path = self.set_path(path, extension)
        self.data = self.create_file()
        self.auto_save_bool = auto_save

    def __str__(self):
        return f"JsonData (path={self.path}, data={self.data})"

    def auto_save(self):
        if self.auto_save_bool:
            self.save()
        

    def set_path(self, path, extension):
        """Add the file extension to the file name."""
        if not path.endswith(extension):
            path += extension
        return path

    def create_file(self):
        """Create the File, if it doesn't exist."""
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

        return self.read_file()

    def read_file(self):
        """Read the Json File and return the content."""
        with open(self.path, "r") as f:
            return json.load(f)

    def set(self, key, value):
        """Add key, value pair to the File."""
        self.data[key] = value
        self.auto_save()

    def get(self, key):
        """Return the value of the key."""
        return self.data.get(key, None)

    def save(self):
        """Save the File finally."""
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def delete(self, key):
        """Delete a pair of the file."""
        if key == "*" and not key in self.data.keys:
            self.data.clear()
        else:
            self.data.pop(key, None)
        self.auto_save()

    def exists(self, key):
        """Return a boolean, which say if a key in the file."""
        return key in self.data

    def keys(self):
        """Return a list of all keys."""
        return list(self.data.keys())

    def values(self):
        """Return a list of all values."""
        return list(self.data.values())

    def items(self):
        """Return a list of all items."""
        return list(self.data.items())

    def update(self, new_data):
        """Update the file with dictionary."""
        self.data.update(new_data)
        self.auto_save()

    def clear(self):
        """Clear the File."""
        self.data.clear()
        self.auto_save()

    def reload(self):
        """Reload the file content."""
        self.data = self.read_file()
        self.auto_save()

    def delete_file(self):
        """Delete the Json File"""
        if os.path.exists(self.path):
            os.remove(self.path)
            self.data.clear()

class JsonDataManager:
    def __init__(self, directory):
        self.directory = directory
        self.data_files = {}

        if not os.path.exists(directory):
            os.makedirs(directory)

    def __str__(self):
        return f"JsonDataManager (directory={self.directory}, data_files={list(self.data_files.keys())})"

    def get_data(self, filename):
        if filename not in self.data_files:
            path = os.path.join(self.directory, filename)
            self.data_files[filename] = JsonData(path)
        return self.data_files[filename]

    def add_data(self, filename):
        if filename not in self.data_files:
            path = os.path.join(self.directory, filename)
            self.data_files[filename] = JsonData(path)

    def save_all(self):
        for data in self.data_files.values():
            data.save()

    def reload_all(self):
        for data in self.data_files.values():
            data.reload()

    def delete_all(self):
        for data in self.data_files.values():
            data.delete_file()

    def delete_self(self):
        self.delete_all()
        if os.path.exists(self.directory):
            os.rmdir(self.directory)