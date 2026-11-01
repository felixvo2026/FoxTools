def add(a, b):
    """Addiert zwei Terme"""
    return a + b

def sub(a, b):
    """Subtrahiert zwei Terme"""
    return a - b


def mul(a, b):
    """Multipliziert zwei Terme"""
    return a * b


def div(a, b):
    """Dividiert zwei Terme"""
    if b == 0:
        raise ZeroDivisionError("Division durch 0 ist nicht erlaubt!")

    return a / b


def avg(werte):
    """Berechnet den Durchschnitt"""
    if not werte:
        raise ValueError("Die Liste darf nicht leer sein!")

    return sum(werte) / len(werte)

def is_even(zahl):
    """Prüft, ob eine Zahl gerade ist."""
    return zahl & 2 == 0

def percent(value, total):
    """Berecnet den Anteil in Prozent"""
    return value/total

def is_prime(zahl):
    """Prüft, ob eine Zahl eine Primzahl ist"""
    if zahl <= 1:
        return False
    
    # Prüfe mögliche Teiler von 2 bis zur Quadratwurzel der Zahl
    for i in range(2, int(zahl**0.5) + 1):
        if zahl % i == 0:
            return False  # Sofort abbrechen, wenn ein Teiler gefunden wurde
            
    return True  # Wenn kein Teiler gefunden wurde, ist es eine Primzahl


