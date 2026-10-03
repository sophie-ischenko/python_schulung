"""Einführung in Python – Mini-Projekt: Der Begrüßungs-Bot (STARTER)

Das erste kleine Programm, das mehrere Python-Grundlagen kombiniert.

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

    # TODO:
    # Baue diesen Text zusammen:
    #
    # Hallo Ada! Willkommen an Bord.
    #
    # Dabei soll der übergebene Name eingesetzt werden.
    #
    # Du kannst einen f-String verwenden:
    #
    # return f"Hallo {name}! Willkommen an Bord."

    pass


# ----------------------------------------------------------------
# Funktion 2: Volljährigkeit prüfen
# ----------------------------------------------------------------

def ist_volljaehrig(alter):
    """Gibt True zurück, wenn das Alter mindestens 18 beträgt."""

    # TODO:
    # Prüfe, ob alter größer oder gleich 18 ist.
    # Gib das Ergebnis mit return zurück.

    pass


# ----------------------------------------------------------------
# Hauptprogramm
# ----------------------------------------------------------------

def main():
    """Fragt Daten ab und führt das Programm aus."""

    print("=== START DES BOTS ===")

    benutzer_name = input("Wie heißt du? ")
    benutzer_alter = int(input("Wie alt bist du? "))

    text = erstelle_begruessung(benutzer_name)

    print(text)

    if ist_volljaehrig(benutzer_alter):
        print("Du bist volljährig. Du darfst alle Funktionen nutzen.")
    else:
        print("Du bist noch nicht volljährig. Eingeschränkter Modus aktiv.")

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
        "Volljährig (25)",
        ist_volljaehrig(25),
        True
    )

    ergebnis(
        "Volljährig (18)",
        ist_volljaehrig(18),
        True
    )

    ergebnis(
        "Volljährig (17)",
        ist_volljaehrig(17),
        False
    )

    ergebnis(
        "Volljährig (12)",
        ist_volljaehrig(12),
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