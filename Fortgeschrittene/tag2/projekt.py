"""Tag 2 – Mini-Projekt: Reiseplaner (STARTER)

Ein kleines Konsolenprogramm zur Verwaltung von Reisen.

Themen:

- Listen
- Tupel
- Dictionaries
- Sets
- sorted()
- Schleifen
- Bedingungen
- verschachtelte Daten
- Funktionen

Ziel:

Am Ende soll das Programm einige Reisen anzeigen
und einfache Informationen daraus berechnen.

STARTEN
========

Normales Programm:

    python projekt.py

Selbsttest:

    python projekt.py test
"""

import sys


# ----------------------------------------------------------------
# Daten
# ----------------------------------------------------------------

REISEN = {
    "Paris": {
        "land": "Frankreich",
        "tage": 4,
        "aktivitaeten": [
            "Eiffelturm",
            "Louvre",
            "Seine",
        ],
        "kategorien": {"Kultur", "Stadt", "Essen"},
    },
    "Rom": {
        "land": "Italien",
        "tage": 5,
        "aktivitaeten": [
            "Kolosseum",
            "Vatikan",
            "Trevi-Brunnen",
        ],
        "kategorien": {"Kultur", "Geschichte", "Essen"},
    },
    "Lissabon": {
        "land": "Portugal",
        "tage": 3,
        "aktivitaeten": [
            "Altstadt",
            "Straßenbahn",
            "Belem",
        ],
        "kategorien": {"Stadt", "Meer", "Essen"},
    },
}


# ----------------------------------------------------------------
# Aufgabe 1
# ----------------------------------------------------------------

def reisebereich(reisen):
    """
    Gibt die kürzeste und längste Reise zurück.

    Beispiel:

    (3, 5)
    """

    # TODO:
    #
    # Erstelle eine Liste mit allen Tageszahlen.
    #
    # Verwende min() und max().
    #
    # Gib beide Werte als Tupel zurück.

    pass


# ----------------------------------------------------------------
# Aufgabe 2
# ----------------------------------------------------------------

def laengste_reise(reisen):
    """
    Findet die Stadt mit der längsten Reise.

    Rückgabe:

    ("Rom", 5)
    """

    # TODO:
    #
    # Erstelle zwei Variablen:
    #
    # - längste Stadt
    # - längste Dauer
    #
    # Laufe mit einer Schleife durch die Reisen.
    #
    # Vergleiche die Anzahl der Tage.
    #
    # Speichere die Reise, wenn sie länger ist.
    #
    # Gib Stadt und Tage als Tupel zurück.

    pass


# ----------------------------------------------------------------
# Aufgabe 3
# ----------------------------------------------------------------

def alle_kategorien(reisen):
    """
    Gibt alle unterschiedlichen Kategorien zurück.

    Beispiel:

    ["Essen", "Geschichte", "Kultur", "Meer", "Stadt"]
    """

    # TODO:
    #
    # Erstelle ein leeres Set.
    #
    # Laufe durch alle Reisen.
    #
    # Hole die Kategorien der Reise.
    #
    # Füge die Kategorien zum Set hinzu.
    #
    # Sortiere das Ergebnis mit sorted().
    #
    # Gib die sortierte Liste zurück.

    pass


# ----------------------------------------------------------------
# Aufgabe 4
# ----------------------------------------------------------------

def reise_anzeigen(stadt, reisen):
    """
    Gibt eine Reise übersichtlich aus.

    Beispiel:

    === Paris ===
    Land: Frankreich
    Dauer: 4 Tage

    Aktivitäten:
    - Eiffelturm
    - Louvre
    - Seine

    Kategorien:
    - Essen
    - Kultur
    - Stadt
    """

    # TODO:
    #
    # Hole die Reise aus dem Dictionary.
    #
    # Gib Stadt, Land und Tage aus.
    #
    # Gib anschließend alle Aktivitäten aus.
    #
    # Gib anschließend alle Kategorien aus.
    #
    # Die Kategorien sollen sortiert sein.

    pass


# ----------------------------------------------------------------
# Hauptprogramm
# ----------------------------------------------------------------

def main():

    print("=== Reiseplaner ===")
    print()

    # Alle Städte anzeigen

    print("Reiseziele:")

    for stadt in sorted(REISEN):
        print("-", stadt)

    # Längste Reise

    stadt, tage = laengste_reise(REISEN)

    print()
    print("Längste Reise:")
    print(f"{stadt} mit {tage} Tagen")

    # Reisebereich

    minimum, maximum = reisebereich(REISEN)

    print()
    print("Reisedauer:")
    print(f"Kürzeste Reise: {minimum} Tage")
    print(f"Längste Reise: {maximum} Tage")

    # Kategorien

    kategorien = alle_kategorien(REISEN)

    print()
    print("Kategorien:")

    for kategorie in kategorien:
        print("-", kategorie)

    # Einzelne Reise anzeigen

    print()
    print("Beispielreise:")

    reise_anzeigen("Paris", REISEN)


# ----------------------------------------------------------------
# Selbsttest
# ----------------------------------------------------------------

def selbsttest():

    ergebnisse = [
        (
            "Reisebereich",
            reisebereich(REISEN),
            (3, 5),
        ),
        (
            "Längste Reise",
            laengste_reise(REISEN),
            ("Rom", 5),
        ),
        (
            "Kategorien",
            alle_kategorien(REISEN),
            [
                "Essen",
                "Geschichte",
                "Kultur",
                "Meer",
                "Stadt",
            ],
        ),
    ]

    for name, erhalten, erwartet in ergebnisse:

        if erhalten == erwartet:
            print(f"✓ {name}")

        else:
            print(
                f"✗ {name} → "
                f"erwartet {erwartet!r}, "
                f"erhalten {erhalten!r}"
            )


# ----------------------------------------------------------------
# Start
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

    else:

        main()