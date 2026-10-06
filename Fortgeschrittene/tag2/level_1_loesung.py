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


def erste_messwerte(messwerte):
    neue_liste = []

    for messwert in messwerte:
        if len(neue_liste) < 3:
            neue_liste.append(messwert)

    return neue_liste


def messwerte_ueber_20(messwerte):
    neue_liste = []

    for messwert in messwerte:
        if messwert > 20:
            neue_liste.append(messwert)

    return neue_liste


def messwerte_zaehlen(messwerte):
    return len(messwerte)


def messwert_hinzufuegen(messwerte, neuer_wert):
    neue_liste = list(messwerte)
    neue_liste.append(neuer_wert)

    return neue_liste


def kleinster_messwert(messwerte):
    return min(messwerte)


def groesster_messwert(messwerte):
    return max(messwerte)


def sortiere_messwerte(messwerte):
    return sorted(messwerte)


def eindeutige_stationen(stationen):
    return sorted(set(stationen))


def station_anzeigen(station):
    return station["name"]


def temperatur_anzeigen(station):
    return station["temperatur"]


def station_mit_temperatur(name, temperatur):
    return {
        "name": name,
        "temperatur": temperatur
    }


def durchschnitt(messwerte):
    return sum(messwerte) / len(messwerte)

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