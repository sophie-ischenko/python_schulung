"""
Tag 2 – Aufgaben (STARTER)

Thema: Datenstrukturen

Heute arbeiten wir mit:

- Listen
- for-Schleifen
- append()
- Tupeln
- Dictionaries
- Sets
- sorted()
- einfachen verschachtelten Daten

Die Aufgaben werden Schritt für Schritt schwieriger.

Starte die Datei:
Am Ende siehst du, welche Aufgaben schon stimmen (✓ / ✗).
"""


def check(name, erhalten, erwartet):
    """
    Vergleicht Ergebnis und Erwartung
    und gibt ✓ oder ✗ aus.
    """
    if erhalten == erwartet:
        print(f"✓ {name}")
    else:
        print(
            f"✗ {name} → "
            f"erwartet {erwartet!r}, "
            f"erhalten {erhalten!r}"
        )


# ---------------------------------------------------------------- Aufgabe 1

def erste_messwerte(messwerte):
    """
    Gibt die ersten drei Messwerte zurück.

    Beispiel:

    erste_messwerte([18, 21, 19, 23])

    Ergebnis:

    [18, 21, 19]
    """
    # TODO:
    # Erstelle eine leere Liste.

    pass


# ---------------------------------------------------------------- Aufgabe 2

def messwerte_ueber_20(messwerte):
    """
    Gibt alle Messwerte zurück,
    die größer als 20 sind.

    Beispiel:

    messwerte_ueber_20([18, 21, 19, 23])

    Ergebnis:

    [21, 23]
    """
    # TODO:
    # Erstelle eine leere Liste.
    #
    # Gehe durch die Messwerte.
    # Prüfe

    pass


# ---------------------------------------------------------------- Aufgabe 3

def messwerte_zaehlen(messwerte):
    """
    Zählt, wie viele Messwerte vorhanden sind.

    Beispiel:

    messwerte_zaehlen([18, 21, 19, 23])

    Ergebnis:

    4
    """


    pass


# ---------------------------------------------------------------- Aufgabe 4

def messwert_hinzufuegen(messwerte, neuer_wert):
    """
    Fügt einen neuen Messwert hinzu.

    Die ursprüngliche Liste soll nicht verändert werden.

    Beispiel:

    messwert_hinzufuegen([18, 21, 19], 23)

    Ergebnis:

    [18, 21, 19, 23]
    """
    # TODO:
    # Erstelle eine Kopie der Liste (messwerte).
    #
    # Tipp:
    # Verwende list(messwerte)
    #
    # Füge den neuen Wert mit append() hinzu.
    #
    # Gib die neue Liste zurück.

    pass


# ---------------------------------------------------------------- Aufgabe 5

def kleinster_messwert(messwerte):
    """
    Gibt den kleinsten Messwert zurück.

    Beispiel:

    kleinster_messwert([18, 21, 16, 23])

    Ergebnis:

    16
    """


    pass


# ---------------------------------------------------------------- Aufgabe 6

def groesster_messwert(messwerte):
    """
    Gibt den größten Messwert zurück.

    Beispiel:

    groesster_messwert([18, 21, 16, 23])

    Ergebnis:

    23
    """

    pass


# ---------------------------------------------------------------- Aufgabe 7

def sortiere_messwerte(messwerte):
    """
    Sortiert die Messwerte aufsteigend.

    Beispiel:

    sortiere_messwerte([23, 18, 21, 16])

    Ergebnis:

    [16, 18, 21, 23]
    """


    pass


# ---------------------------------------------------------------- Aufgabe 8

def eindeutige_stationen(stationen):
    """
    Entfernt doppelte Stationsnamen.

    Beispiel:

    ["Nord", "Sued", "Nord", "West"]

    Ergebnis:

    ["Nord", "Sued", "West"]

    Tipp:
    Ein Set enthält jeden Wert nur einmal.
    """
    # TODO:
    # Wandle die Liste in ein Set um.
    #
    # Verwende danach sorted(),
    # damit eine sortierte Liste entsteht.

    pass


# ---------------------------------------------------------------- Aufgabe 9

def station_anzeigen(station):
    """
    Gibt den Namen einer Station
    aus einem Dictionary zurück.

    Beispiel:

    station = {
        "name": "Nord",
        "temperatur": 18.5
    }

    Ergebnis:

    "Nord"
    """
    # TODO:
    # Hole den Wert mit dem Schlüssel "name".

    pass


# ---------------------------------------------------------------- Aufgabe 10

def temperatur_anzeigen(station):
    """
    Gibt die Temperatur einer Station zurück.

    Beispiel:

    station = {
        "name": "Nord",
        "temperatur": 18.5
    }

    Ergebnis:

    18.5
    """


    pass


# ---------------------------------------------------------------- Aufgabe 11

def station_mit_temperatur(name, temperatur):
    """
    Erstellt ein Dictionary für eine Station.

    Beispiel:

    station_mit_temperatur("Nord", 18.5)

    Ergebnis:

    {
        "name": "Nord",
        "temperatur": 18.5
    }
    """
    # TODO:
    # Erstelle ein Dictionary.
    #
    # Es soll zwei Schlüssel enthalten:
    #
    # "name"
    # "temperatur"

    pass


# ---------------------------------------------------------------- Aufgabe 12

def durchschnitt(messwerte):
    """
    Berechnet den Durchschnitt
    einer Liste von Messwerten.

    Beispiel:

    durchschnitt([18, 20, 22])

    Ergebnis:

    20.0
    """
    # TODO:
    # Addiere alle Messwerte.
    #
    # Teile die Summe die Anzahl der Elemente.


    pass


if __name__ == "__main__":

    print()
    print("==========================================")
    print("   TAG 2: DATENSTRUKTUREN")
    print("==========================================")

    # ---------------------------------------------------------------- Aufgabe 1

    check(
        "1 erste_messwerte",
        erste_messwerte(
            [18, 21, 19, 23, 17]
        ),
        [18, 21, 19],
    )

    # ---------------------------------------------------------------- Aufgabe 2

    check(
        "2 messwerte_ueber_20",
        messwerte_ueber_20(
            [18, 21, 19, 23, 17, 25]
        ),
        [21, 23, 25],
    )

    # ---------------------------------------------------------------- Aufgabe 3

    check(
        "3 messwerte_zaehlen",
        messwerte_zaehlen(
            [18, 21, 19, 23]
        ),
        4,
    )

    # ---------------------------------------------------------------- Aufgabe 4

    check(
        "4 messwert_hinzufuegen",
        messwert_hinzufuegen(
            [18, 21, 19],
            23
        ),
        [18, 21, 19, 23],
    )

    # ---------------------------------------------------------------- Aufgabe 5

    check(
        "5 kleinster_messwert",
        kleinster_messwert(
            [18, 21, 16, 23]
        ),
        16,
    )

    # ---------------------------------------------------------------- Aufgabe 6

    check(
        "6 groesster_messwert",
        groesster_messwert(
            [18, 21, 16, 23]
        ),
        23,
    )

    # ---------------------------------------------------------------- Aufgabe 7

    check(
        "7 sortiere_messwerte",
        sortiere_messwerte(
            [23, 18, 21, 16]
        ),
        [16, 18, 21, 23],
    )

    # ---------------------------------------------------------------- Aufgabe 8

    check(
        "8 eindeutige_stationen",
        eindeutige_stationen(
            [
                "Nord",
                "Sued",
                "Nord",
                "West",
                "Sued"
            ]
        ),
        [
            "Nord",
            "Sued",
            "West"
        ],
    )

    # ---------------------------------------------------------------- Aufgabe 9

    check(
        "9 station_anzeigen",
        station_anzeigen(
            {
                "name": "Nord",
                "temperatur": 18.5
            }
        ),
        "Nord",
    )

    # ---------------------------------------------------------------- Aufgabe 10

    check(
        "10 temperatur_anzeigen",
        temperatur_anzeigen(
            {
                "name": "Nord",
                "temperatur": 18.5
            }
        ),
        18.5,
    )

    # ---------------------------------------------------------------- Aufgabe 11

    check(
        "11 station_mit_temperatur",
        station_mit_temperatur(
            "Nord",
            18.5
        ),
        {
            "name": "Nord",
            "temperatur": 18.5
        },
    )

    # ---------------------------------------------------------------- Aufgabe 12

    check(
        "12 durchschnitt",
        durchschnitt(
            [18, 20, 22]
        ),
        20.0,
    )

    print()
    print("==========================================")
    print("   TESTS ABGESCHLOSSEN")
    print("==========================================")