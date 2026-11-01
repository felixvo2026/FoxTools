import random


def zahl(minimum, maximum):
    """Gibt eine zufällige Ganzzahl zurück."""
    if minimum > maximum:
        raise ValueError("Ungültiger Zahlenbereich!")

    return random.randint(minimum, maximum)


def wahl(liste):
    """Wählt ein zufälliges Element aus."""
    if not liste:
        raise ValueError("Die Liste darf nicht leer sein!")

    return random.choice(liste)


def mix(liste):
    """Mischt eine Kopie der Liste."""
    neue_liste = liste.copy()
    random.shuffle(neue_liste)

    return neue_liste


def name(namen):
    """Wählt einen zufälligen Namen aus."""
    return wahl(namen)


def ja_nein():
    """Gibt zufällig True oder False zurück."""
    return random.choice([True, False])
