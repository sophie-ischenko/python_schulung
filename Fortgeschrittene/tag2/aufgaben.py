"""
Tag 2 – Aufgaben (STARTER)

Thema: Datenstrukturen und Messdaten.

Heute arbeiten wir mit:

- Listen
- Tupeln
- Dictionaries
- Sets
- sorted()
- verschachtelten Datenstrukturen

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
def hohe_messwerte(messwerte, grenzwert):
    """
    Gibt alle Messwerte zurück,
    die mindestens den Grenzwert erreichen.

    Beispiel:

    hohe_messwerte([17.5, 21.0, 19.5, 23.0], 20)

    Ergebnis:

    [21.0, 23.0]

    Tipp:
    Erstelle eine neue Liste und füge nur die
    passenden Messwerte hinzu.
    """
    # TODO:
    # Erstelle eine neue leere Liste.
    #
    # Gehe mit einer for-Schleife durch die Messwerte.
    #
    # Prüfe:
    # Ist der aktuelle Messwert größer oder gleich
    # dem Grenzwert?
    #
    # Wenn ja:
    # Füge ihn mit append() zur neuen Liste hinzu.
    pass


# ---------------------------------------------------------------- Aufgabe 2
def messwerte_zaehlen(messwerte):
    """
    Zählt, wie oft jeder Messwert vorkommt.

    Rückgabe: Dictionary

    Beispiel:

    messwerte_zaehlen([20, 21, 20, 19, 21, 20])

    Ergebnis:

    {
        20: 3,
        21: 2,
        19: 1
    }

    Im Dictionary ist:

    Schlüssel → Messwert
    Wert      → Anzahl der Vorkommen
    """
    # TODO:
    # Erstelle ein leeres Dictionary.
    #
    # Gehe mit einer for-Schleife durch die Messwerte.
    #
    # Prüfe mit "in", ob der Messwert bereits
    # ein Schlüssel im Dictionary ist.
    #
    # Wenn ja:
    # Erhöhe den vorhandenen Wert um 1.
    #
    # Wenn nein:
    # Lege den Messwert mit dem Wert 1 an.
    pass


# ---------------------------------------------------------------- Aufgabe 3
def eindeutige_stationen(stationen):
    """
    Entfernt doppelte Stationsnamen
    und gibt sie sortiert zurück.

    Beispiel:

    ["Nord", "Sued", "Nord", "West", "Sued"]

    wird zu:

    ["Nord", "Sued", "West"]

    Tipp:
    Ein Set enthält jeden Wert nur einmal.
    """
    # TODO:
    # Wandle die Liste in ein Set um.
    #
    # Dadurch werden doppelte Werte entfernt.
    #
    # Verwende anschließend sorted(),
    # damit du wieder eine sortierte Liste erhältst.
    pass


# ---------------------------------------------------------------- Aufgabe 4
def gemeinsame_sensoren(a, b):
    """
    Gibt die Sensoren zurück,
    die beide Stationen verwenden.

    Beispiel:

    a:
    ["temperatur", "druck", "feuchtigkeit"]

    b:
    ["temperatur", "licht", "feuchtigkeit"]

    Gemeinsame Sensoren:

    ["feuchtigkeit", "temperatur"]
    """
    # TODO:
    # Wandle beide Listen in Sets um.
    #
    # Verwende & für die Schnittmenge.
    #
    # Eine Schnittmenge enthält nur Werte,
    # die in beiden Sets vorkommen.
    #
    # Verwende anschließend sorted(),
    # damit das Ergebnis eine sortierte Liste ist.
    pass


# ---------------------------------------------------------------- Aufgabe 5
def sortiere_messwerte(messwerte, absteigend=False):
    """
    Sortiert Messwerte aufsteigend oder absteigend.

    Die ursprüngliche Liste soll dabei
    NICHT verändert werden.

    Beispiel:

    sortiere_messwerte([21, 18, 23])

    Ergebnis:

    [18, 21, 23]

    Mit:

    absteigend=True

    ergibt sich:

    [23, 21, 18]

    Tipp:
    Verwende sorted().

    sorted() erstellt eine neue sortierte Liste.

    Das ist anders als list.sort(),
    denn sort() verändert die ursprüngliche Liste.
    """
    # TODO:
    # Verwende sorted().
    #
    # Der Parameter reverse kann bestimmen,
    # ob aufsteigend oder absteigend sortiert wird.
    #
    # reverse=False → aufsteigend
    # reverse=True  → absteigend
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

    Die Daten bestehen aus Tupeln:

    ("Nord", 18.4)

    Dabei ist:

    "Nord" → Stationsname
    18.4   → Messwert
    """
    # TODO:
    # Erstelle ein leeres Dictionary.
    #
    # Gehe mit einer for-Schleife durch messdaten.
    #
    # Du kannst dabei zwei Variablen verwenden:
    #
    # for station, messwert in messdaten:
    #
    # Prüfe, ob die Station bereits im Dictionary
    # vorhanden ist.
    #
    # Falls nicht:
    # Lege für diese Station eine leere Liste an.
    #
    # Anschließend füge den Messwert mit append()
    # zur passenden Liste hinzu.
    pass


# ---------------------------------------------------------------- Aufgabe 7
def min_max(messwerte):
    """
    Gibt den kleinsten und größten Messwert
    als Tupel zurück.

    Beispiel:

    min_max([18.4, 21.7, 16.2, 23.1])

    Ergebnis:

    (16.2, 23.1)

    Das Ergebnis ist ein Tupel mit zwei Werten:

    (kleinster, größter)
    """
    # TODO:
    # Verwende min() für den kleinsten Wert.
    #
    # Verwende max() für den größten Wert.
    #
    # Gib beide Werte gemeinsam als Tupel zurück.
    pass


# ---------------------------------------------------------------- Aufgabe 8
def durchschnittswerte(stationen):
    """
    Berechnet den Durchschnitt der Temperaturen
    jeder Station.

    Eingabe:

    [
        {
            "name": "Nord",
            "temperaturen": [18.0, 20.0]
        },
        {
            "name": "Sued",
            "temperaturen": [22.0, 24.0]
        }
    ]

    Rückgabe:

    {
        "Nord": 19.0,
        "Sued": 23.0
    }

    Die Daten sind verschachtelt:

    Liste
        ↓
    Dictionary
        ↓
    Liste

    Beispiel:

    station["name"]

    holt den Namen.

    station["temperaturen"]

    holt die Liste mit den Temperaturen.
    """
    # TODO:
    # Erstelle ein neues leeres Dictionary.
    #
    # Gehe mit einer for-Schleife durch die Stationen.
    #
    # Hole den Namen:
    #
    # station["name"]
    #
    # Hole die Temperaturen:
    #
    # station["temperaturen"]
    #
    # Berechne den Durchschnitt:
    #
    # Summe der Temperaturen / Anzahl der Temperaturen
    #
    # Speichere das Ergebnis unter dem Namen
    # der Station im neuen Dictionary.
    pass


if __name__ == "__main__":

    print()
    print("==========================================")
    print("   TAG 2: DATENSTRUKTUREN")
    print("==========================================")

    # ---------------------------------------------------------------- Aufgabe 1

    check(
        "1 hohe_messwerte",
        hohe_messwerte(
            [17.5, 21.0, 19.5, 23.0, 18.0],
            20
        ),
        [21.0, 23.0],
    )

    # ---------------------------------------------------------------- Aufgabe 2

    check(
        "2 messwerte_zaehlen",
        messwerte_zaehlen(
            [20, 21, 20, 19, 21, 20]
        ),
        {
            20: 3,
            21: 2,
            19: 1
        },
    )

    # ---------------------------------------------------------------- Aufgabe 3

    check(
        "3 eindeutige_stationen",
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

    # ---------------------------------------------------------------- Aufgabe 4

    check(
        "4 gemeinsame_sensoren",
        gemeinsame_sensoren(
            [
                "temperatur",
                "druck",
                "feuchtigkeit"
            ],
            [
                "temperatur",
                "licht",
                "feuchtigkeit"
            ],
        ),
        [
            "feuchtigkeit",
            "temperatur"
        ],
    )

    # ---------------------------------------------------------------- Aufgabe 5

    check(
        "5a sortiere_messwerte (auf)",
        sortiere_messwerte(
            [
                21.4,
                18.7,
                23.1,
                19.5,
                17.9,
                22.0
            ]
        ),
        [
            17.9,
            18.7,
            19.5,
            21.4,
            22.0,
            23.1
        ],
    )

    check(
        "5b sortiere_messwerte (ab)",
        sortiere_messwerte(
            [
                21.4,
                18.7,
                23.1,
                19.5,
                17.9,
                22.0
            ],
            absteigend=True,
        ),
        [
            23.1,
            22.0,
            21.4,
            19.5,
            18.7,
            17.9
        ],
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
        min_max(
            [18.4, 21.7, 16.2, 23.1]
        ),
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

    print()
    print("==========================================")
    print("   TESTS ABGESCHLOSSEN")
    print("==========================================")