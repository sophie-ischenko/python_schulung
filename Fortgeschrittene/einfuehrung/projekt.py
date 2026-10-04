"""
Einführung in Python – Mini-Projekt: Der Begrüßungs-Bot (STARTER)

Das erste kleine Programm, das mehrere Python-Grundlagen kombiniert.

In diesem Projekt lernst du:

- eigene Funktionen schreiben
- Parameter verwenden
- Werte mit return zurückgeben
- f-Strings verwenden
- Bedingungen mit if und else prüfen
- len() verwenden
- True und False verwenden
- ein Modul importieren
- Argumente beim Programmstart auswerten

Starten:
    python projekt.py

Selbsttest:
    python projekt.py test


Was ist sys?

sys ist ein Modul aus der Python-Standardbibliothek.
Es stellt Informationen und Funktionen rund um das laufende
Python-Programm bereit.

Mit

    import sys

laden wir das Modul.

Hier verwenden wir sys.argv.

sys.argv enthält die Argumente, die beim Start des Programms
übergeben wurden.

Wenn du zum Beispiel schreibst:

    python projekt.py test

enthält sys.argv ungefähr:

    ["projekt.py", "test"]

Das erste Element ist der Name des Programms.
Das zweite Element ist das zusätzliche Argument "test".

Damit können wir erkennen, ob das Programm normal gestartet
oder der Selbsttest angefordert wurde.
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
# Funktion 2: Passwort prüfen
# ----------------------------------------------------------------

def ist_passwort_sicher(passwort):
    """Gibt True zurück, wenn das Passwort mindestens 8 Zeichen hat."""

    # TODO:
    # Prüfe, ob das Passwort mindestens 8 Zeichen lang ist.
    #
    # len(passwort) gibt die Anzahl der Zeichen zurück.
    #
    # Beispiel:
    #
    # len("Python12") ergibt 8
    #
    # Vergleiche die Länge mit 8.
    # Das Ergebnis des Vergleichs ist automatisch True oder False.
    #
    # Gib das Ergebnis mit return zurück.

    pass


# ----------------------------------------------------------------
# Hauptprogramm
# ----------------------------------------------------------------

   
def main():
    """
        Hauptprogramm.
    
        Hier befindet sich die eigentliche Programmlogik.
        `main()` wird beim normalen Start des Programms ausgeführt.
    
        Die Tests stehen bewusst nicht hier.
        Sie befinden sich in `selbsttest()`, damit wir das Programm
        und seine Tests getrennt voneinander starten können.
    """

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


# Die Tests stehen hier in einer eigenen Funktion.
#
# Warum?
#
# In diesem Projekt kann das Programm auf zwei verschiedene Arten
# gestartet werden:
#
#     python projekt.py
#
#     → normales Programm
#
# oder:
#
#     python projekt.py test
#
#     → nur die Tests
#
# Dafür brauchen wir eine Funktion, die alle Tests bündelt.
# Diese Funktion heißt `selbsttest()`.
#
# Später prüfen wir mit `sys.argv`, ob beim Programmstart
# das Wort "test" angegeben wurde.
#
# Dadurch können wir gezielt `selbsttest()` aufrufen, ohne
# das normale Hauptprogramm zu starten.


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

    # sys.argv enthält die Argumente, die beim Start des
    # Python-Programms mitgegeben wurden.
    #
    # Normaler Start:
    #
    #     python projekt.py
    #
    # Dann enthält sys.argv nur den Dateinamen.
    #
    # Start mit Selbsttest:
    #
    #     python projekt.py test
    #
    # Dann enthält sys.argv zusätzlich "test".

    if len(sys.argv) > 1 and sys.argv[1] == "test":

        # Wenn das erste zusätzliche Argument "test" ist,
        # wird der Selbsttest gestartet.

        try:
            selbsttest()

        except Exception as fehler:

            # Falls beim Selbsttest ein Fehler auftritt,
            # wird das Programm nicht einfach mit einem
            # langen Traceback beendet.
            #
            # Stattdessen geben wir eine verständliche
            # Fehlermeldung aus.

            print(
                f"✗ Selbsttest abgebrochen: "
                f"{type(fehler).__name__}: {fehler}"
            )

            print("  Vermutlich ist eine Funktion noch nicht fertig.")

    else:

        # Wenn kein "test"-Argument angegeben wurde,
        # startet das normale Hauptprogramm.

        main()