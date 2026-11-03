# Module
from . import mathe
from . import pygame_tools
from . import zufall
from . import texte
from . import farben
from . import dateien
from . import system
from . import data


# Mathe
from .mathe import add, sub, mul, div, avg, is_even, percent, is_prime, multiply, Clamp, round_to, distance

# Pygame
from .pygame_tools import center_window, main_close

# Zufall
from .zufall import zahl, wahl, mix, name, ja_nein

# Texte
from .texte import reverse, count, words, clean, upper, lower, contains

# Farben
from .farben import rgb, hex_rgb, rgb_hex, random_color, invert, gray, is_dark

# Dateien
from .dateien import create, read, write, append, exists, delete, sizeof

# System
from .system import python, os_name, platform, cwd, user, cpu

# Data
from .data import JsonData