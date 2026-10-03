"""Einführung in Python – Erste Aufgaben (STARTER)

Kurze Wiederholung der Python-Grundlagen.

Bearbeite die Stellen mit TODO.

Starten:
    python aufgaben.py
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

    # TODO:
    # Gib exakt den Text "Hallo Welt!" zurück.

    pass


# ----------------------------------------------------------------
# Aufgabe 2: addiere
# ----------------------------------------------------------------

def addiere(zahl1, zahl2):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""

    # TODO:
    # Addiere zahl1 und zahl2.
    # Gib das Ergebnis mit return zurück.

    pass


# ----------------------------------------------------------------
# Aufgabe 3: berechne_alter
# ----------------------------------------------------------------

def berechne_alter(geburtsjahr, aktuelles_jahr):
    """Berechnet das Alter anhand von Geburtsjahr und aktuellem Jahr."""

    # TODO:
    # Ziehe das Geburtsjahr vom aktuellen Jahr ab.
    # Gib das Ergebnis mit return zurück.

    pass


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