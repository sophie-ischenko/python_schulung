"""
Einführung in Python – Mini-Projekt: Der Begrüßungs-Bot (LÖSUNG)

Starten:
    python projekt.py

Selbsttest:
    python projekt.py test
"""

import sys


# ----------------------------------------------------------------
# Funktion 1: Begrüßung
# ----------------------------------------------------------------

def erstelle_begruessung(name):
    """Erstellt eine persönliche Begrüßung."""

    return f"Hallo {name}! Willkommen an Bord."


# ----------------------------------------------------------------
# Funktion 2: Passwort prüfen
# ----------------------------------------------------------------

def ist_passwort_sicher(passwort):
    """Gibt True zurück, wenn das Passwort mindestens 8 Zeichen hat."""

    return len(passwort) >= 8


# ----------------------------------------------------------------
# Hauptprogramm
# ----------------------------------------------------------------

def main():
    """Fragt Daten ab und führt das Programm aus."""

    print("=== START DES BOTS ===")

    benutzer_name = input("Wie heißt du? ")
    benutzer_passwort = input("Lege ein Passwort fest: ")

    text = erstelle_begruessung(benutzer_name)

    print(text)

    if ist_passwort_sicher(benutzer_passwort):
        print("Dein Passwort ist lang genug.")
    else:
        print("Dein Passwort ist zu kurz. Verwende mindestens 8 Zeichen.")

    print("=== ENDE ===")


# ----------------------------------------------------------------
# Selbsttest
# ----------------------------------------------------------------

def selbsttest():
    """Überprüft die beiden Funktionen mit verschiedenen Testwerten."""

    def ergebnis(name, erhalten, erwartet):
        if erhalten == erwartet:
            print(f"✓ {name}")
        else:
            print(
                f"✗ {name} "
                f"(erwartet {erwartet!r}, erhalten {erhalten!r})"
            )

    print("--- Begrüßungs-Bot: Selbsttest ---")

    ergebnis(
        "Begrüßung Ada",
        erstelle_begruessung("Ada"),
        "Hallo Ada! Willkommen an Bord."
    )

    ergebnis(
        "Begrüßung Ben",
        erstelle_begruessung("Ben"),
        "Hallo Ben! Willkommen an Bord."
    )

    ergebnis(
        "Passwort mit 10 Zeichen",
        ist_passwort_sicher("Python1234"),
        True
    )

    ergebnis(
        "Passwort mit genau 8 Zeichen",
        ist_passwort_sicher("Python12"),
        True
    )

    ergebnis(
        "Passwort mit 7 Zeichen",
        ist_passwort_sicher("Python1"),
        False
    )

    ergebnis(
        "Leeres Passwort",
        ist_passwort_sicher(""),
        False
    )


# ----------------------------------------------------------------
# Programmstart
# ----------------------------------------------------------------

if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        try:
            selbsttest()

        except Exception as fehler:
            print(
                f"✗ Selbsttest abgebrochen: "
                f"{type(fehler).__name__}: {fehler}"
            )
            print("  Vermutlich ist eine Funktion noch nicht fertig.")

    else:
        main()