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
    return zahl % 2 == 0

def percent(value, total):
    """Berecnet den Anteil in Prozent"""
    if total == 0:
        raise ValueError("Der Gesamtwert darf nicht 0 sein.")
    return (value / total) * 100

def is_prime(zahl):
    """Prüft, ob eine Zahl eine Primzahl ist"""
    if zahl <= 1:
        return False
    
    # Prüfe mögliche Teiler von 2 bis zur Quadratwurzel der Zahl
    for i in range(2, int(zahl**0.5) + 1):
        if zahl % i == 0:
            return False  # Sofort abbrechen, wenn ein Teiler gefunden wurde
            
    return True  # Wenn kein Teiler gefunden wurde, ist es eine Primzahl


def multiply(a):
    """Multipliziert eine Zahl mit einem Faktor."""
    return lambda b: a * b

class Clamp:
    """Überschreibt eine Zahl, sodass sie innerhalb eines bestimmten Bereichs bleibt."""
    def __init__(self, zahl, min, max):
        if not min <= zahl <= max:
            raise ValueError("Zahl ist nicht innerhalb der Begrenzungen.")

        self.min = min
        self.max = max
        self._zahl = zahl

    def __str__(self):
        return f"Clamp(zahl={self._zahl}, min={self.min}, max={self.max})"

    @property
    def zahl(self):
        return self._zahl

    @zahl.setter
    def zahl(self, newZahl):
        if self.min <= newZahl <= self.max:
            self._zahl = newZahl
        else:
            raise ValueError("Zahl ist nicht innerhalb der Begrenzungen.")

def round_to(value, digits):
    return round(value, digits)

def distance(point1, point2):
    """Berechnet die Distanz zwischen zwei Punkten im 2D-Raum."""
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

pi = 3.141592653589793 # Mathematische Konstante Pi (π)

def sqrt(value):
    """Berechnet die Quadratwurzel einer Zahl."""
    if value < 0:
        raise ValueError("Die Quadratwurzel einer negativen Zahl ist nicht definiert.")
    return value ** 0.5

def circle_area(radius):
    """Berechnet die Fläche eines Kreises basierend auf dem Radius."""
    if radius < 0:
        raise ValueError("Der Radius darf nicht negativ sein.")
    return pi * (radius ** 2)

def circle_circumference(radius):
    """Berechnet den Umfang eines Kreises basierend auf dem Radius."""
    if radius < 0:
        raise ValueError("Der Radius darf nicht negativ sein.")
    return 2 * pi * radius