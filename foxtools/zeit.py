import datetime
import time

def time_now():
    """Gibt Uhrzeit und Datum zurück."""
    return datetime.datetime.now()

def timer(func, *args, **kwargs):
    """Misst wie lange eine Funktion braucht."""
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start

def format_duration(seconds):
    """Gibt die Sekundenanzahl in Stunden, Minuten und Sekunden zurück."""
    try:
        seconds = float(seconds)
    except:
        raise ValueError("Input must be a float")
    
    minutes = int((seconds % 3600) // 60)
    rest = round(seconds % 60, 2)  
    hours = int(seconds // 3600)

    if rest.is_integer():
        rest = int(rest)

    if hours > 0:
        if all([minutes > 1, hours > 1, rest == 1]):
            return f"{hours} Stunden, {minutes} Minuten und {rest} Sekunde"
        if all([minutes == 1, hours > 1, rest > 1]):
            return f"{hours} Stunden, {minutes} Minute und {rest} Sekunden"
        if all([minutes == 1, hours > 1, rest == 1]):
            return f"{hours} Stunden, {minutes} Minute und {rest} Sekunde"
        if all([minutes > 1, hours == 1, rest > 1]):
            return f"{hours} Stunde, {minutes} Minuten und {rest} Sekunden"
        if all([minutes > 1, hours == 1, rest == 1]):
            return f"{hours} Stunde, {minutes} Minuten und {rest} Sekunde"
        if all([minutes == 1, hours == 1, rest > 1]):
            return f"{hours} Stunde, {minutes} Minute und {rest} Sekunden"
        if all([minutes == 1, hours == 1, rest == 1]):
            return f"{hours} Stunde, {minutes} Minute und {rest} Sekunde"
        return f"{hours} Stunden, {minutes} Minuten und {rest} Sekunden"

    if minutes == 1 and rest > 1:
        return f"{minutes} Minute und {rest} Sekunden"
    if minutes > 1 and rest == 1:
            return f"{minutes} Minuten und {rest} Sekunde"
    if minutes == 1 and rest == 1:
            return f"1 Minute und 1 Sekunden"
    return f"{minutes} Minuten und {rest} Sekunden"