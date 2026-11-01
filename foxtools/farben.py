
import random


def rgb(rot, gruen, blau):
    """Erstellt eine RGB-Farbe."""
    werte = (rot, gruen, blau)

    if any(not isinstance(wert, int) or isinstance(wert, bool) or not 0 <= wert <= 255 for wert in werte):
        raise ValueError("RGB-Werte müssen ganze Zahlen zwischen 0 und 255 sein!")

    return werte


def hex_rgb(hex_code):
    """Wandelt einen HEX-Code in RGB um."""
    hex_code = hex_code.lstrip("#")

    if len(hex_code) != 6:
        raise ValueError("Ungültiger HEX-Code!")

    try:
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        raise ValueError("Ungültiger HEX-Code!") from None


def rgb_hex(farbe):
    """Wandelt RGB in einen HEX-Code um."""
    if len(farbe) != 3 or any(
        not isinstance(wert, int) or isinstance(wert, bool) or not 0 <= wert <= 255
        for wert in farbe
    ):
        raise ValueError("Ungültige RGB-Farbe!")

    return "#{:02X}{:02X}{:02X}".format(*farbe)


def random_color():
    """Erzeugt eine zufällige RGB-Farbe."""
    return tuple(random.randint(0, 255) for _ in range(3))


def invert(farbe):
    """Invertiert eine RGB-Farbe."""
    return tuple(255 - wert for wert in farbe)


def gray(farbe):
    """Berechnet den Grauwert einer RGB-Farbe."""
    rot, gruen, blau = farbe
    return round(0.299 * rot + 0.587 * gruen + 0.114 * blau)

def is_dark(farbe):
    """Prüft, ob eine RGB-Farbe dunkel ist."""
    return gray(farbe) < 128