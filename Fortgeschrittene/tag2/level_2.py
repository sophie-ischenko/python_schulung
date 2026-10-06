"""
Tag 2 – Level 2
Dictionaries, Sets und Tupel

Thema:
Datenstrukturen im Alltag

Wir arbeiten mit:

- Dictionaries
- Sets
- Tupeln
- Schleifen
- sorted()
- einfachen Kombinationen

Die Aufgaben bauen auf den Grundlagen aus Level 1 auf.
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


# ============================================================
# DICTIONARIES
# ============================================================


# ---------------------------------------------------------------- Aufgabe 1

def unter_10_euro(preise):
    """
    Gibt alle Produkte zurück,
    die weniger als 10 Euro kosten.

    Beispiel:

    {
        "Brot": 3.50,
        "Milch": 1.20,
        "Kaffee": 8.90,
        "Käse": 12.00
    }

    Ergebnis:

    ["Brot", "Kaffee", "Milch"]

    Die Produkte sollen alphabetisch sortiert sein.
    """
    # TODO:
    # Erstelle eine leere Liste.
    #
    # Gehe mit .items() durch das Dictionary.
    #
    # Prüfe den Preis.
    #
    # Wenn der Preis kleiner als 10 ist,
    # füge den Produktnamen hinzu.
    #
    # Sortiere die Liste am Ende.

    pass


# ---------------------------------------------------------------- Aufgabe 2

def teuerstes_produkt(preise):
    """
    Gibt den Namen des teuersten Produkts zurück.

    Beispiel:

    {
        "Brot": 3.50,
        "Kaffee": 8.90,
        "Käse": 12.00
    }

    Ergebnis:

    "Käse"
    """
    # TODO:
    # Verwende max().
    #
    # Vergleiche dabei die Preise
    # und nicht die Produktnamen.
    #
    # Tipp:
    # max(..., key=...)

    pass


# ---------------------------------------------------------------- Aufgabe 3

def preise_erhoehen(preise, prozent):
    """
    Erhöht alle Preise um einen bestimmten Prozentsatz.

    Beispiel:

    {
        "Brot": 2.00,
        "Milch": 1.00
    }

    Erhöhung: 10

    Ergebnis:

    {
        "Brot": 2.20,
        "Milch": 1.10
    }

    Das ursprüngliche Dictionary
    soll nicht verändert werden.
    """
    # TODO:
    # Erstelle ein neues Dictionary.
    #
    # Gehe mit .items() durch die Preise.
    #
    # Berechne den neuen Preis.
    #
    # Speichere ihn im neuen Dictionary.

    pass


# ============================================================
# SETS
# ============================================================


# ---------------------------------------------------------------- Aufgabe 4

def gemeinsame_filme(filme_a, filme_b):
    """
    Findet Filme, die zwei Personen
    beide gesehen haben.

    Beispiel:

    filme_a = {
        "Matrix",
        "Titanic",
        "Avatar"
    }

    filme_b = {
        "Avatar",
        "Matrix",
        "Inception"
    }

    Ergebnis:

    {"Matrix", "Avatar"}
    """
    # TODO:
    # Verwende die Schnittmenge von Sets.

    pass


# ---------------------------------------------------------------- Aufgabe 5

def noch_nicht_gelesen_wunschliste(wunschliste, gelesen):
    """
    Gibt Bücher zurück, die auf der Wunschliste
    stehen, aber noch nicht gelesen wurden.

    Beispiel:

    wunschliste = {
        "Harry Potter",
        "Dune",
        "1984",
        "Der Hobbit"
    }

    gelesen = {
        "1984",
        "Der Hobbit"
    }

    Ergebnis:

    {
        "Harry Potter",
        "Dune"
    }
    """
    # TODO:
    # Verwende die Differenz von Sets.

    pass


# ---------------------------------------------------------------- Aufgabe 6

def alle_gerichte(restaurant_a, restaurant_b):
    """
    Gibt alle verschiedenen Gerichte zurück,
    die zwei Restaurants anbieten.

    Beispiel:

    restaurant_a = {
        "Pizza",
        "Pasta",
        "Salat"
    }

    restaurant_b = {
        "Pizza",
        "Burger",
        "Salat"
    }

    Ergebnis:

    {
        "Pizza",
        "Pasta",
        "Salat",
        "Burger"
    }
    """
    # TODO:
    # Verwende die Vereinigung von Sets.

    pass


# ============================================================
# TUPEL
# ============================================================


# ---------------------------------------------------------------- Aufgabe 7

def personen_ab_18(personen):
    """
    Gibt die Namen aller volljährigen Personen zurück.

    Eine Person wird als Tupel gespeichert:

    ("Anna", 17)
    ("Ben", 25)
    ("Clara", 19)

    Ergebnis:

    ["Ben", "Clara"]

    Die Namen sollen alphabetisch sortiert sein.
    """
    # TODO:
    # Erstelle eine leere Liste.
    #
    # Gehe durch die Tupel.
    #
    # Entpacke:
    #
    # for name, alter in personen:
    #
    # Prüfe das Alter.
    #
    # Sortiere am Ende.

    pass


# ---------------------------------------------------------------- Aufgabe 8

def durchschnittsalter(personen):
    """
    Berechnet das durchschnittliche Alter.

    Beispiel:

    [
        ("Anna", 20),
        ("Ben", 30),
        ("Clara", 25)
    ]

    Ergebnis:

    25.0
    """
    # TODO:
    # Erstelle eine Variable für die Summe.
    #
    # Gehe durch die Tupel.
    #
    # Addiere jeweils das Alter.
    #
    # Teile am Ende durch die Anzahl der Personen.

    pass


# ---------------------------------------------------------------- Aufgabe 9

def sortiere_nach_alter(personen):
    """
    Sortiert Personen nach ihrem Alter.

    Beispiel:

    [
        ("Anna", 30),
        ("Ben", 20),
        ("Clara", 25)
    ]

    Ergebnis:

    [
        ("Ben", 20),
        ("Clara", 25),
        ("Anna", 30)
    ]
    """
    # TODO:
    # Verwende sorted().
    #
    # Sortiert werden soll nach
    # dem zweiten Element des Tupels.

    pass


# ============================================================
# GEMISCHT
# ============================================================


# ---------------------------------------------------------------- Aufgabe 10

def besucherzahlen(veranstaltungen):
    """
    Wandelt eine Liste von Tupeln
    in ein Dictionary um.

    Beispiel:

    [
        ("Konzert", 250),
        ("Theater", 120),
        ("Kino", 180)
    ]

    Ergebnis:

    {
        "Konzert": 250,
        "Theater": 120,
        "Kino": 180
    }
    """
    # TODO:
    # Erstelle ein leeres Dictionary.
    #
    # Gehe durch die Tupel.
    #
    # Speichere die Besucherzahl
    # unter dem Namen der Veranstaltung.

    pass


# ---------------------------------------------------------------- Aufgabe 11

def gemeinsame_teilnehmer(gruppe_a, gruppe_b):
    """
    Findet Personen, die an zwei Veranstaltungen
    teilgenommen haben.

    Die Teilnehmerlisten enthalten Tupel:

    gruppe_a = [
        ("Anna", 25),
        ("Ben", 30),
        ("Clara", 22)
    ]

    gruppe_b = [
        ("Ben", 30),
        ("David", 28),
        ("Anna", 25)
    ]

    Ergebnis:

    {"Anna", "Ben"}

    Es geht nur um die Namen.
    """
    # TODO:
    # Erstelle für beide Gruppen ein Set
    # mit den Namen.
    #
    # Verwende anschließend die Schnittmenge.

    pass


# ---------------------------------------------------------------- Aufgabe 12

def einkaufswert(einkauf, preise):
    """
    Berechnet den Gesamtpreis eines Einkaufs.

    einkauf:

    [
        ("Brot", 2),
        ("Milch", 3),
        ("Kaffee", 1)
    ]

    preise:

    {
        "Brot": 3.00,
        "Milch": 1.50,
        "Kaffee": 8.00
    }

    Ergebnis:

    23.50

    Erklärung:

    2 × 3.00 = 6.00
    3 × 1.50 = 4.50
    1 × 8.00 = 8.00

    Gesamt:

    18.50
    """
    # TODO:
    # Erstelle eine Variable für die Gesamtsumme.
    #
    # Gehe durch den Einkauf.
    #
    # Entpacke Produkt und Anzahl.
    #
    # Hole den Preis aus dem Dictionary.
    #
    # Berechne:
    #
    # Preis * Anzahl
    #
    # Addiere alles.

    pass


# ============================================================
# TESTS
# ============================================================

if __name__ == "__main__":

    print()
    print("==========================================")
    print("   DICTIONARIES")
    print("==========================================")

    check(
        "1 unter_10_euro",
        unter_10_euro(
            {
                "Brot": 3.50,
                "Milch": 1.20,
                "Kaffee": 8.90,
                "Käse": 12.00
            }
        ),
        [
            "Brot",
            "Kaffee",
            "Milch"
        ]
    )

    check(
        "2 teuerstes_produkt",
        teuerstes_produkt(
            {
                "Brot": 3.50,
                "Kaffee": 8.90,
                "Käse": 12.00
            }
        ),
        "Käse"
    )

    check(
        "3 preise_erhoehen",
        preise_erhoehen(
            {
                "Brot": 2.00,
                "Milch": 1.00
            },
            10
        ),
        {
            "Brot": 2.20,
            "Milch": 1.10
        }
    )


    print()
    print("==========================================")
    print("   SETS")
    print("==========================================")

    check(
        "4 gemeinsame_filme",
        gemeinsame_filme(
            {
                "Matrix",
                "Titanic",
                "Avatar"
            },
            {
                "Avatar",
                "Matrix",
                "Inception"
            }
        ),
        {
            "Matrix",
            "Avatar"
        }
    )

    check(
        "5 noch_nicht_gelesen_wunschliste",
        noch_nicht_gelesen_wunschliste(
            {
                "Harry Potter",
                "Dune",
                "1984",
                "Der Hobbit"
            },
            {
                "1984",
                "Der Hobbit"
            }
        ),
        {
            "Harry Potter",
            "Dune"
        }
    )

    check(
        "6 alle_gerichte",
        alle_gerichte(
            {
                "Pizza",
                "Pasta",
                "Salat"
            },
            {
                "Pizza",
                "Burger",
                "Salat"
            }
        ),
        {
            "Pizza",
            "Pasta",
            "Salat",
            "Burger"
        }
    )


    print()
    print("==========================================")
    print("   TUPEL")
    print("==========================================")

    check(
        "7 personen_ab_18",
        personen_ab_18(
            [
                ("Anna", 17),
                ("Ben", 25),
                ("Clara", 19)
            ]
        ),
        [
            "Ben",
            "Clara"
        ]
    )

    check(
        "8 durchschnittsalter",
        durchschnittsalter(
            [
                ("Anna", 20),
                ("Ben", 30),
                ("Clara", 25)
            ]
        ),
        25.0
    )

    check(
        "9 sortiere_nach_alter",
        sortiere_nach_alter(
            [
                ("Anna", 30),
                ("Ben", 20),
                ("Clara", 25)
            ]
        ),
        [
            ("Ben", 20),
            ("Clara", 25),
            ("Anna", 30)
        ]
    )


    print()
    print("==========================================")
    print("   GEMISCHT")
    print("==========================================")

    check(
        "10 besucherzahlen",
        besucherzahlen(
            [
                ("Konzert", 250),
                ("Theater", 120),
                ("Kino", 180)
            ]
        ),
        {
            "Konzert": 250,
            "Theater": 120,
            "Kino": 180
        }
    )

    check(
        "11 gemeinsame_teilnehmer",
        gemeinsame_teilnehmer(
            [
                ("Anna", 25),
                ("Ben", 30),
                ("Clara", 22)
            ],
            [
                ("Ben", 30),
                ("David", 28),
                ("Anna", 25)
            ]
        ),
        {
            "Anna",
            "Ben"
        }
    )

    check(
        "12 einkaufswert",
        einkaufswert(
            [
                ("Brot", 2),
                ("Milch", 3),
                ("Kaffee", 1)
            ],
            {
                "Brot": 3.00,
                "Milch": 1.50,
                "Kaffee": 8.00
            }
        ),
        18.50
    )

    print()
    print("==========================================")
    print("   TESTS ABGESCHLOSSEN")
    print("==========================================")