# Module
from . import mathe, pygame_tools, zufall, texte, farben, dateien, system

# Mathe
from .mathe import add, sub, mul, div, avg

# Zufall
from .zufall import zahl, wahl, mix, name, ja_nein

# Texte
from .texte import reverse, count, words, clean, upper, lower, contains

# Farben
from .farben import rgb, hex_rgb, rgb_hex, random_color, invert, gray, is_dark

# Dateien
from .dateien import create, read, write, append, exists, delete, size

# System
from .system import python, os_name, platform, cwd, user, cpu

#pygame_help
from .pygame_tools import main_close, center_window