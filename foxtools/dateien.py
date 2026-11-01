
from pathlib import Path


def create(pfad):
    """Erstellt eine neue Datei."""
    pfad = Path(pfad)
    pfad.touch(exist_ok=False)


def read(pfad):
    """Liest eine Datei aus."""
    return Path(pfad).read_text(encoding="utf-8")


def write(pfad, text):
    """Überschreibt den Inhalt einer Datei."""
    Path(pfad).write_text(text, encoding="utf-8")


def append(pfad, text):
    """Fügt Text am Ende einer Datei hinzu."""
    with open(pfad, "a", encoding="utf-8") as datei:
        datei.write(text)


def exists(pfad):
    """Prüft, ob eine Datei existiert."""
    return Path(pfad).is_file()


def delete(pfad):
    """Löscht eine Datei."""
    pfad = Path(pfad)

    if not pfad.is_file():
        raise FileNotFoundError("Datei wurde nicht gefunden!")

    pfad.unlink()

def size(pfad):
    """Gibt die Größe einer Datei in bytes zurück"""
    return Path(pfad).stat().st_size

