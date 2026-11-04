# FoxTools 🦊

FoxTools ist eine kleine Python-Bibliothek mit wiederverwendbaren Hilfsfunktionen für Mathematik, Zufall, Texte, Farben, Dateien und Systeminformationen. Zusätzlich enthält sie Hilfsfunktionen für Pygame und eine einfache JSON-Datenverwaltung.

## Voraussetzungen

- Python 3.9 oder höher
- Für die Pygame-Funktionen zusätzlich [Pygame](https://www.pygame.org/)

## Installation

Repository herunterladen und im Projektordner installieren:

```bash
git clone https://github.com/felixvo2026/FoxTools.git
cd FoxTools
python -m pip install .
```

Für die Pygame-Funktionen Pygame separat installieren:

```bash
python -m pip install pygame
```

## Schnellstart

```python
import foxtools

print(foxtools.add(3, 5))            # 8
print(foxtools.zahl(1, 10))          # Zufällige Ganzzahl zwischen 1 und 10
print(foxtools.reverse("Hallo"))     # ollaH
print(foxtools.rgb_hex((255, 128, 0)))  # #FF8000
```

## Module und Beispiele

### Mathematik

```python
from foxtools import mathe

print(mathe.avg([2, 4, 6]))          # 4.0
print(mathe.is_prime(7))             # True
print(mathe.distance((0, 0), (3, 4)))  # 5.0
```

### Zufall

```python
from foxtools import zufall

print(zufall.wahl(["Apfel", "Birne", "Banane"]))
print(zufall.ja_nein())
```

### Texte

```python
from foxtools import texte

print(texte.words("Hallo FoxTools"))  # 2
print(texte.contains("Hallo Welt", "welt"))  # True
print(texte.random_string(8))
print(texte.random_password(15)) # Passwörter sind nicht sicher, nur zum Testen !!!
```

### Farben

```python
from foxtools import farben

farbe = farben.rgb(255, 128, 0)
print(farben.rgb_hex(farbe))          # #FF8000
print(farben.hex_rgb("#FF8000"))      # (255, 128, 0)
```

### Dateien

```python
from foxtools import dateien

dateien.write("notiz.txt", "Hallo!")
print(dateien.read("notiz.txt"))
```

### JSON-Daten

```python
from foxtools import JsonData

daten = JsonData("einstellungen")
daten.set("sprache", "de")
daten.save()

print(daten.get("sprache"))           # de
```

### Systeminformationen

```python
from foxtools import system

print(system.python())
print(system.os_name())
print(system.cwd())
```

### Pygame

Die Pygame-Hilfsfunktionen benötigen eine separate Pygame-Installation.

```python
import pygame
import foxtools

pygame.init()
foxtools.center_window()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    running = foxtools.main_close()
    pygame.display.update()

pygame.quit()
```

## Lizenz

FoxTools ist unter der [MIT-Lizenz](LICENSE) veröffentlicht.
