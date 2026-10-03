
"""Tag 2 – Aufgaben (STARTER)
Thema: Datenstrukturen und Messdaten.

Listen, Tupel, Dictionaries, Sets, sorted()
und verschachtelte Datenstrukturen.

Starte die Datei: Am Ende siehst du, welche Aufgaben schon stimmen (✓ / ✗).
"""


def check(name, erhalten, erwartet):
    """Vergleicht Ergebnis und Erwartung und gibt ✓ oder ✗ aus."""
    if erhalten == erwartet:
        print(f"✓ {name}")
    else:
        print(f"✗ {name} → erwartet {erwartet!r}, erhalten {erhalten!r}")


# ---------------------------------------------------------------- Aufgabe 1
def hohe_messwerte(messwerte, grenzwert):
    """Gibt alle Messwerte zurück, die mindestens den Grenzwert erreichen."""
    # TODO:
    # Erstelle eine neue Liste.
    # Füge nur Messwerte hinzu, die mindestens den Grenzwert erreichen.
    pass


# ---------------------------------------------------------------- Aufgabe 2
def messwerte_zaehlen(messwerte):
    """Zählt, wie oft jeder Messwert vorkommt. Rückgabe: Dictionary."""
    # TODO:
    # Erstelle ein Dictionary zum Zählen.
    # Prüfe, ob der Messwert bereits im Dictionary vorhanden ist.
    # Wenn ja, erhöhe den Wert um 1.
    # Wenn nein, lege ihn mit dem Wert 1 an.
    pass


# ---------------------------------------------------------------- Aufgabe 3
def eindeutige_stationen(stationen):
    """Entfernt doppelte Stationsnamen und gibt sie sortiert zurück."""
    # TODO:
    # Verwende ein Set, um doppelte Stationsnamen zu entfernen.
    # Gib das Ergebnis anschließend mit sorted() sortiert zurück.
    pass


# ---------------------------------------------------------------- Aufgabe 4
def gemeinsame_sensoren(a, b):
    """Gibt die Sensoren zurück, die beide Stationen verwenden."""
    # TODO:
    # Wandle beide Listen in Sets um.
    # Ermittle die Schnittmenge mit &.
    # Gib das Ergebnis mit sorted() als Liste zurück.
    pass


# ---------------------------------------------------------------- Aufgabe 5
def sortiere_messwerte(messwerte, absteigend=False):
    """
    Sortiert Messwerte aufsteigend oder absteigend.

    Die ursprüngliche Liste soll dabei nicht verändert werden.
    """
    # TODO:
    # Verwende sorted().
    # Wenn absteigend True ist, soll in absteigender Reihenfolge
    # sortiert werden.
    pass


# ---------------------------------------------------------------- Aufgabe 6
def gruppiere_messwerte(messdaten):
    """
    Gruppiert Messwerte nach Station.

    Eingabe:
    [
        ("Nord", 18.4),
        ("Sued", 22.1),
        ("Nord", 19.1)
    ]

    Rückgabe:
    {
        "Nord": [18.4, 19.1],
        "Sued": [22.1]
    }
    """
    # TODO:
    # Erstelle ein Dictionary.
    # Für jede Station soll eine Liste mit ihren Messwerten entstehen.
    pass


# ---------------------------------------------------------------- Aufgabe 7
def min_max(messwerte):
    """Gibt (kleinster, größter) Messwert als Tupel zurück."""
    # TODO:
    # Verwende min() und max().
    # Gib beide Werte gemeinsam als Tupel zurück.
    pass


# ---------------------------------------------------------------- Aufgabe 8
def durchschnittswerte(stationen):
    """
    Berechnet den Durchschnitt der Temperaturen jeder Station.

    Eingabe:
    [
        {"name": "Nord", "temperaturen": [18.0, 20.0]},
        {"name": "Sued", "temperaturen": [22.0, 24.0]}
    ]

    Rückgabe:
    {
        "Nord": 19.0,
        "Sued": 23.0
    }
    """
    # TODO:
    # Die Daten sind verschachtelt:
    # Liste → Dictionary → Liste
    #
    # Erstelle ein neues Dictionary.
    # Berechne für jede Station den Durchschnitt ihrer Temperaturen.
    pass


if __name__ == "__main__":
    # ---------------------------------------------------------------- Aufgabe 1
    check(
        "1 hohe_messwerte",
        hohe_messwerte([17.5, 21.0, 19.5, 23.0, 18.0], 20),
        [21.0, 23.0],
    )

    # ---------------------------------------------------------------- Aufgabe 2
    check(
        "2 messwerte_zaehlen",
        messwerte_zaehlen([20, 21, 20, 19, 21, 20]),
        {20: 3, 21: 2, 19: 1},
    )

    # ---------------------------------------------------------------- Aufgabe 3
    check(
        "3 eindeutige_stationen",
        eindeutige_stationen(
            ["Nord", "Sued", "Nord", "West", "Sued"]
        ),
        ["Nord", "Sued", "West"],
    )

    # ---------------------------------------------------------------- Aufgabe 4
    check(
        "4 gemeinsame_sensoren",
        gemeinsame_sensoren(
            ["temperatur", "druck", "feuchtigkeit"],
            ["temperatur", "licht", "feuchtigkeit"],
        ),
        ["feuchtigkeit", "temperatur"],
    )

    # ---------------------------------------------------------------- Aufgabe 5
    check(
        "5a sortiere_messwerte (auf)",
        sortiere_messwerte(
            [21.4, 18.7, 23.1, 19.5, 17.9, 22.0]
        ),
        [17.9, 18.7, 19.5, 21.4, 22.0, 23.1],
    )

    check(
        "5b sortiere_messwerte (ab)",
        sortiere_messwerte(
            [21.4, 18.7, 23.1, 19.5, 17.9, 22.0],
            absteigend=True,
        ),
        [23.1, 22.0, 21.4, 19.5, 18.7, 17.9],
    )

    # ---------------------------------------------------------------- Aufgabe 6
    check(
        "6 gruppiere_messwerte",
        gruppiere_messwerte(
            [
                ("Nord", 18.4),
                ("Sued", 22.1),
                ("Nord", 19.1),
                ("West", 17.9),
                ("Sued", 23.0),
            ]
        ),
        {
            "Nord": [18.4, 19.1],
            "Sued": [22.1, 23.0],
            "West": [17.9],
        },
    )

    # ---------------------------------------------------------------- Aufgabe 7
    check(
        "7 min_max",
        min_max([18.4, 21.7, 16.2, 23.1]),
        (16.2, 23.1),
    )

    # ---------------------------------------------------------------- Aufgabe 8
    check(
        "8 durchschnittswerte",
        durchschnittswerte(
            [
                {
                    "name": "Nord",
                    "temperaturen": [18.0, 20.0],
                },
                {
                    "name": "Sued",
                    "temperaturen": [22.0, 24.0],
                },
                {
                    "name": "West",
                    "temperaturen": [17.0, 19.0],
                },
            ]
        ),
        {
            "Nord": 19.0,
            "Sued": 23.0,
            "West": 18.0,
        },
    )
