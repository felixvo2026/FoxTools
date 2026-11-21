import re

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
    """Rundet eine Zahl auf eine bestimmte Anzahl von Nachkommastellen."""
    return round(value, digits)

def distance2(point1, point2):
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

def distance3(point1, point2):
    """Berechnet die Distanz zwischen zwei Punkten im 3D-Raum."""
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2) ** 0.5

def ggt(a, b):
    """Berechnet den größten gemeinsamen Teiler (ggt) von zwei Zahlen."""
    while b != 0:
        a, b = b, a % b
    return a

def kgV(a, b):
    """Berechnet das kleinste gemeinsame Vielfache (kgV) von zwei Zahlen."""
    if a == 0 or b == 0:
        raise ValueError("Das kgV ist für 0 nicht definiert.")
    
    return abs(a * b) // ggt(a, b)

def absbetrag(x):
    """Gibt den absoluten Betrag einer reellen Zahl zurück."""
    if x >= 0:
        return x
    return -x


def calculate(x):
    if not x or x == 0:
        return 0

    # Eingabe bereinigen
    expr = str(x).replace(" ", "").replace(",", ".").replace("**", "^")

    # Tokens extrahieren (Zahlen inkl. Dezimalstellen und Operatoren)
    tokens = re.findall(r"\d+(?:\.\d+)?|[+\-*/^()]", expr)

    if not tokens:
        return 0

    def parse_expression(index):
        # 1. Ebene: Addition und Subtraktion (niedrigste Priorität)
        val, index = parse_term(index)
        while index < len(tokens) and tokens[index] in ("+", "-"):
            op = tokens[index]
            right, index = parse_term(index + 1)
            val = val + right if op == "+" else val - right
        return val, index

    def parse_term(index):
        # 2. Ebene: Multiplikation und Division
        val, index = parse_power(index)
        while index < len(tokens) and tokens[index] in ("*", "/"):
            op = tokens[index]
            right, index = parse_power(index + 1)
            if op == "*":
                val *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("Division durch Null")
                val /= right
        return val, index

    def parse_power(index):
        # 3. Ebene: Potenzen (rechtsassoziativ: 2^3^2 = 2^(3^2))
        val, index = parse_factor(index)
        if index < len(tokens) and tokens[index] == "^":
            right, index = parse_power(index + 1)
            val **= right
        return val, index

    def parse_factor(index):
        # 4. Ebene: Zahlen, Vorzeichen und Klammern (höchste Priorität)
        token = tokens[index]

        # Negative oder positive Vorzeichen am Anfang (z. B. -5 oder -(2+3))
        if token == "-":
            val, index = parse_factor(index + 1)
            return -val, index
        if token == "+":
            return parse_factor(index + 1)

        # Klammern auflösen
        if token == "(":
            val, index = parse_expression(index + 1)
            if index >= len(tokens) or tokens[index] != ")":
                raise ValueError("Fehlende schließende Klammer ')'")
            return val, index + 1

        # Normale Zahl
        try:
            return float(token), index + 1
        except ValueError:
            raise ValueError(f"Unerwartetes Zeichen: {token}")

    result, final_index = parse_expression(0)

    if final_index != len(tokens):
        raise ValueError("Ungültige Syntax im Ausdruck")

    # Gibt eine Ganzzahl zurück, falls kein Nachkommawert existiert (z. B. 4 statt 4.0)
    return int(result) if result.is_integer() else result



testdaten = [
    3 + 4 * (3+3),
    2+8,
    2**104,
    2 + (1/5)
]

for daten in testdaten:
    print(calculate(str(daten)))
