"""Einführung in Python – Erste Aufgaben (LÖSUNG)

Musterlösungen für die Grundlagenaufgaben.
"""


def check(name, erhalten, erwartet):
    """Vergleicht Ergebnis und Erwartung und gibt ✓ oder ✗ aus."""
    if erhalten == erwartet:
        print(f"✓ {name}")
    else:
        print(f"✗ {name} → erwartet {erwartet!r}, erhalten {erhalten!r}")


# ----------------------------------------------------------------
# Aufgabe 1: hallo_welt
# ----------------------------------------------------------------

def hallo_welt():
    """Gibt den Text 'Hallo Welt!' zurück."""

    return "Hallo Welt!"


# ----------------------------------------------------------------
# Aufgabe 2: addiere
# ----------------------------------------------------------------

def addiere(zahl1, zahl2):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""

    return zahl1 + zahl2


# ----------------------------------------------------------------
# Aufgabe 3: berechne_alter
# ----------------------------------------------------------------

def berechne_alter(geburtsjahr, aktuelles_jahr):
    """Berechnet das Alter anhand von Geburtsjahr und aktuellem Jahr."""

    return aktuelles_jahr - geburtsjahr


# ----------------------------------------------------------------
# Automatischer Test
# ----------------------------------------------------------------

if __name__ == "__main__":
    print("--- Erste Python-Schritte ---")

    check(
        "1 hallo_welt",
        hallo_welt(),
        "Hallo Welt!"
    )

    check(
        "2a addiere (5 + 3)",
        addiere(5, 3),
        8
    )

    check(
        "2b addiere (10 + 20)",
        addiere(10, 20),
        30
    )

    check(
        "3a berechne_alter (2000 in 2026)",
        berechne_alter(2000, 2026),
        26
    )

    check(
        "3b berechne_alter (1995 in 2030)",
        berechne_alter(1995, 2030),
        35
    )