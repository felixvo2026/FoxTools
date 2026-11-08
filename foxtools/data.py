import json
import os

class JsonData:
    """Eine Klasse zum Managen einer Json-Datei."""
    def __init__(self, path, auto_save=False):
        self.path = self.set_path(path, ".json")
        self.data = self.create_file()
        self.auto_save_bool = auto_save

    def __str__(self):
        """Gibt die grundlegenge Informationen des Objekts zurück."""
        return f"JsonData (path={self.path}, data={self.data})"

    def auto_save(self):
        """Speichert die Daten automatisch, wenn auto_save bei der Initialiserung auf True gesetzt wurde."""
        if self.auto_save_bool:
            self.save()
        

    def set_path(self, path, extension):
        """Fügt die Dateiendung hinzu, falls sie noch nicht existiert."""
        if not path.endswith(extension):
            path += extension
        return path

    def create_file(self):
        """Erstellt dei Datei, falls sie noch nicht existiert."""
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

        return self.read_file()

    def read_file(self):
        """Gibt den Inhalt der Datei zurück."""
        with open(self.path, "r") as f:
            return json.load(f)

    def set(self, key, value):
        """Fügt ein Schlüsselwertpaar hinzu."""
        self.data[key] = value
        self.auto_save()

    def get(self, key):
        """Gibt den Inhalt des dazugehörigen Schlüssels zurück."""
        return self.data.get(key, None)

    def save(self):
        """Speichert die Datei."""
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def delete(self, key):
        """Löscht Werte aus der Datei."""
        if key == "*" and not key in self.data.keys():
            self.data.clear()
        else:
            self.data.pop(key, None)
        self.auto_save()

    def exists(self, key):
        """Prüft, ob ein Wert in der Datei existiert."""
        return key in self.data

    def keys(self):
        """Gibt eine Liste von allen Schlüsseln zurück."""
        return list(self.data.keys())

    def values(self):
        """Gibt eine Liste von allen Werten zurück."""
        return list(self.data.values())

    def items(self):
        """Gibt eine Liste von allen Items."""
        return list(self.data.items())

    def update(self, new_data):
        """Update the file with dictionary."""
        self.data.update(new_data)
        self.auto_save()

    def clear(self):
        """Löscht den gesamten Inhalt der Datei."""
        self.data.clear()
        self.auto_save()

    def reload(self):
        """Lädt erneut den Dateiinhalt."""
        self.data = self.read_file()
        self.auto_save()

    def delete_file(self):
        """Löscht die Datei."""
        if os.path.exists(self.path):
            os.remove(self.path)
            self.data.clear()

class JsonDataManager:
    """Eine Klasse zum Managen mehrerer Json-Dateien."""
    def __init__(self, directory):
        self.directory = directory
        self.data_files = {}

        if not os.path.exists(directory):
            os.makedirs(directory)

    def __str__(self):
        """Gibt grundlegene Informationen des Objekts zurück."""
        return f"JsonDataManager (directory={self.directory}, data_files={list(self.data_files.keys())})"

    def get_data(self, filename):
        """Gibt eine Datei nach ihrem Namen zurück."""
        if filename not in self.data_files:
            path = os.path.join(self.directory, filename)
            self.data_files[filename] = JsonData(path)
        return self.data_files[filename]

    def add_data(self, filename):
        """Fügt eine Datei hinzu."""
        if filename not in self.data_files:
            path = os.path.join(self.directory, filename)
            self.data_files[filename] = JsonData(path)

    def save_all(self):
        """Speichert alle Dateien."""
        for data in self.data_files.values():
            data.save()

    def reload_all(self):
        """Lädt alle Dateien erneut."""
        for data in self.data_files.values():
            data.reload()

    def delete_all(self):
        """Löscht alle Dateien."""
        for data in self.data_files.values():
            data.delete_file()

    def delete_self(self):
        """Löscht den Ordner und alle Dateien."""
        self.delete_all()
        if os.path.exists(self.directory):
            os.rmdir(self.directory)