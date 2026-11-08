
import sys
import platform as pf
import os


def python_version():
    """Gibt die Python-Version zurück."""
    return sys.version.split()[0]


def os_name():
    """Gibt das Betriebssystem zurück."""
    return pf.system()


def platform():
    """Gibt detaillierte Plattforminformationen zurück."""
    return pf.platform()


def cwd():
    """Gibt den aktuellen Arbeitsordner zurück."""
    return os.getcwd()


def user():
    """Gibt den aktuellen Benutzernamen zurück."""
    return os.getlogin()


def cpu():
    """Gibt den Prozessornamen zurück."""
    return pf.processor()
