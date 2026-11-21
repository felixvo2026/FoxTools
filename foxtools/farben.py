
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

def brint(farbe, *string, end="\n"):
    """Schreibt einen Text in der gewünschten Farbe (Englisch) in das Terminal."""
    farbe = farbe.upper()
    farben = {
        "BLACK": "\033[0;30m",
        "RED": "\033[0;31m",
        "GREEN": "\033[0;32m",
        "BROWN": "\033[0;33m",
        "BLUE": "\033[0;34m",
        "PURPLE": "\033[0;35m",
        "CYAN": "\033[0;36m",
        "LIGHT_GRAY": "\033[0;37m",
        "DARK_GRAY": "\033[1;30m",
        "LIGHT_RED": "\033[1;31m",
        "LIGHT_GREEN": "\033[1;32m",
        "YELLOW": "\033[1;33m",
        "LIGHT_BLUE": "\033[1;34m",
        "LIGHT_PURPLE": "\033[1;35m",
        "LIGHT_CYAN": "\033[1;36m",
        "LIGHT_WHITE": "\033[1;37m",
        "BOLD": "\033[1m",
        "FAINT": "\033[2m",
        "ITALIC": "\033[3m",
        "UNDERLINE": "\033[4m",
        "BLINK": "\033[5m",
        "NEGATIVE": "\033[7m",
        "CROSSED": "\033[9m",
        "END": "\033[0m"
    }

    farbe = farben[farbe]

    reset = "\033[00m"
    ausgabe = "" 
    for teil in string:
        ausgabe += str(teil) + " "
    print(f"{farbe}{ausgabe}{reset}", end=end)