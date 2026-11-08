import bcrypt
import secrets

def hash_password(password):
    """Verschlüsselt ein Passwort."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def check_password(password, hashed):
    """Prüft, ob ein Passwort übereinstimmt."""
    try:
        return bcrypt.checkpw(password.encode(), hashed.encode())
    except:
        return False

def create_password(length=12):
    """Erstellt ein sicheres Password mit Mindestlänge 8."""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()-_=+"
    all_chars = lowercase + uppercase + digits + symbols

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]
    password.extend(secrets.choice(all_chars) for _ in range(length - len(password)))
    secrets.SystemRandom().shuffle(password)

    return "".join(password)