
def reverse(text):
    """Dreht einen Text um."""
    return text[::-1]


def count(text):
    """Zählt die Zeichen eines Textes."""
    return len(text)


def words(text):
    """Zählt die Wörter eines Textes."""
    return len(text.split())


def clean(text):
    """Entfernt Leerzeichen am Anfang und Ende."""
    return text.strip()


def upper(text):
    """Wandelt Text in Großbuchstaben um."""
    return text.upper()


def lower(text):
    """Wandelt Text in Kleinbuchstaben um."""
    return text.lower()

def contains(text, suche):
    """Prüft ob ein Wort in einem Text vorkommt."""
    return suche.lower() in text.lower()
