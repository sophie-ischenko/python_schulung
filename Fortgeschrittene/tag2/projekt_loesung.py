"""
Tag 2 – Mini-Projekt: Messdaten-Analyse

LÖSUNG

Ein Konsolenprogramm zur Auswertung von Messdaten
verschiedener Messstationen.

Themen:

- Listen
- Tupel
- Dictionaries
- Sets
- sorted()
- Schleifen
- Bedingungen
- verschachtelte Datenstrukturen
- Funktionen
"""


import sys


# ---------------------------------------------------------------- Daten

MESSDATEN = {
    "Nord": {
        "temperaturen": [18.4, 19.1, 20.3],
        "sensoren": {"temperatur", "feuchtigkeit", "druck"},
    },
    "Sued": {
        "temperaturen": [22.1, 23.4, 21.8],
        "sensoren": {"temperatur", "licht", "feuchtigkeit"},
    },
    "West": {
        "temperaturen": [17.9, 18.7, 19.4],
        "sensoren": {"temperatur", "druck"},
    },
}


# ---------------------------------------------------------------- Funktion 1

def berechne_mittelwert(messwerte):
    """
    Berechnet den Durchschnitt einer nicht leeren Liste.
    """

    summe = sum(messwerte)
    anzahl = len(messwerte)

    durchschnitt = summe / anzahl

    return durchschnitt


# ---------------------------------------------------------------- Funktion 2

def temperatur_bereich(messwerte):
    """
    Gibt den kleinsten und größten Messwert als Tupel zurück.

    Beispiel:

    [18.4, 21.7, 16.2]

    wird zu:

    (16.2, 21.7)
    """

    kleinster = min(messwerte)
    groesster = max(messwerte)

    return (kleinster, groesster)


# ---------------------------------------------------------------- Funktion 3

def temperatur_spanne(messwerte):
    """
    Berechnet die Temperaturspanne einer Station.

    Die Temperaturspanne ist:

    größter Wert - kleinster Wert
    """

    kleinster = min(messwerte)
    groesster = max(messwerte)

    span = groesster - kleinster

    return span


# ---------------------------------------------------------------- Funktion 4

def waermste_station(messdaten):
    """
    Findet die Station mit dem höchsten Durchschnitt.

    Rückgabe:

    (
        stationsname,
        durchschnitt
    )
    """

    waermste_name = None
    hoechster_durchschnitt = None

    for name in messdaten:

        station = messdaten[name]

        temperaturen = station["temperaturen"]

        durchschnitt = berechne_mittelwert(
            temperaturen
        )

        if (
            hoechster_durchschnitt is None
            or durchschnitt > hoechster_durchschnitt
        ):
            hoechster_durchschnitt = durchschnitt
            waermste_name = name

    return (
        waermste_name,
        hoechster_durchschnitt
    )


# ---------------------------------------------------------------- Funktion 5

def sensor_report(messdaten):
    """
    Erstellt eine Übersicht über alle verwendeten Sensoren.

    Rückgabe:

    {
        "druck": ["Nord", "West"],
        "feuchtigkeit": ["Nord", "Sued"],
        "licht": ["Sued"],
        "temperatur": ["Nord", "Sued", "West"]
    }
    """

    ergebnis = {}

    for station_name in messdaten:

        station = messdaten[station_name]

        sensoren = station["sensoren"]

        for sensor in sensoren:

            if sensor not in ergebnis:
                ergebnis[sensor] = []

            ergebnis[sensor].append(station_name)

    for sensor in ergebnis:

        ergebnis[sensor] = sorted(
            ergebnis[sensor]
        )

    return ergebnis


# ---------------------------------------------------------------- Funktion 6

def stationen_nach_durchschnitt(messdaten):
    """
    Gibt die Stationsnamen nach ihrer Durchschnittstemperatur
    absteigend sortiert zurück.

    Die wärmste Station steht zuerst.
    """

    durchschnittswerte = {}

    for name in messdaten:

        station = messdaten[name]

        temperaturen = station["temperaturen"]

        durchschnitt = berechne_mittelwert(
            temperaturen
        )

        durchschnittswerte[name] = durchschnitt

    sortierte_stationen = sorted(
        durchschnittswerte,
        key=durchschnittswerte.get,
        reverse=True,
    )

    return sortierte_stationen


# ---------------------------------------------------------------- Funktion 7

def station_zusammenfassung(name, messdaten):
    """
    Erstellt eine Zusammenfassung für eine Station.

    Rückgabe:

    {
        "name": "Nord",
        "mittelwert": 19.27,
        "spanne": 1.9,
        "sensoren": [
            "druck",
            "feuchtigkeit",
            "temperatur"
        ]
    }
    """

    station = messdaten[name]

    temperaturen = station["temperaturen"]

    sensoren = station["sensoren"]

    mittelwert = berechne_mittelwert(
        temperaturen
    )

    spanne = temperatur_spanne(
        temperaturen
    )

    sortierte_sensoren = sorted(
        sensoren
    )

    ergebnis = {
        "name": name,
        "mittelwert": mittelwert,
        "spanne": spanne,
        "sensoren": sortierte_sensoren,
    }

    return ergebnis


# ---------------------------------------------------------------- Ausgabe

def station_anzeigen(name, messdaten):
    """Gibt eine Station mit ihren wichtigsten Daten aus."""

    daten = station_zusammenfassung(
        name,
        messdaten,
    )

    temperaturen = messdaten[name]["temperaturen"]

    print()
    print(f"Station:      {daten['name']}")
    print(f"Temperaturen:  {temperaturen}")
    print(
        f"Mittelwert:    "
        f"{daten['mittelwert']:.2f} °C"
    )
    print(
        f"Spanne:        "
        f"{daten['spanne']:.1f} °C"
    )
    print(
        f"Sensoren:      "
        f"{', '.join(daten['sensoren'])}"
    )


def alle_station_anzeigen(messdaten):
    """Gibt alle Stationen alphabetisch sortiert aus."""

    stationen = sorted(messdaten)

    for name in stationen:

        station_anzeigen(
            name,
            messdaten,
        )


def sensoren_anzeigen(messdaten):
    """Gibt eine Übersicht der Sensoren und ihrer Stationen aus."""

    report = sensor_report(
        messdaten
    )

    print()

    for sensor in sorted(report):

        stationen = report[sensor]

        print(
            f"{sensor}: "
            f"{', '.join(stationen)}"
        )


# ---------------------------------------------------------------- Hauptprogramm

def main():
    messdaten = MESSDATEN

    while True:

        print()
        print("=== Messdaten-Analyse ===")
        print("1 - Alle Stationen anzeigen")
        print("2 - Eine Station auswerten")
        print("3 - Wärmste Station anzeigen")
        print("4 - Stationen nach Durchschnitt sortiert")
        print("5 - Sensorübersicht anzeigen")
        print("0 - Programm beenden")

        auswahl = input(
            "Auswahl: "
        ).strip()

        if auswahl == "1":

            alle_station_anzeigen(
                messdaten
            )

        elif auswahl == "2":

            name = input(
                "Stationsname: "
            ).strip()

            if name in messdaten:

                station_anzeigen(
                    name,
                    messdaten,
                )

            else:

                print(
                    "Station nicht gefunden."
                )

        elif auswahl == "3":

            name, durchschnitt = (
                waermste_station(
                    messdaten
                )
            )

            print()
            print("Wärmste Station:")
            print(
                f"{name} "
                f"mit {durchschnitt:.2f} °C"
            )

        elif auswahl == "4":

            stationen = (
                stationen_nach_durchschnitt(
                    messdaten
                )
            )

            print()
            print(
                "Stationen nach "
                "Durchschnittstemperatur:"
            )

            for name in stationen:

                print(name)

        elif auswahl == "5":

            sensoren_anzeigen(
                messdaten
            )

        elif auswahl == "0":

            print(
                "Programm beendet."
            )

            break

        else:

            print(
                "Ungültige Auswahl."
            )


# ---------------------------------------------------------------- Selbsttest

def selbsttest():
    """Prüft die wichtigsten Funktionen des Projekts."""

    ergebnisse = [
        (
            "Mittelwert Nord",
            round(
                berechne_mittelwert(
                    MESSDATEN["Nord"]["temperaturen"]
                ),
                2,
            ),
            19.27,
        ),
        (
            "Temperaturbereich Nord",
            temperatur_bereich(
                MESSDATEN["Nord"]["temperaturen"]
            ),
            (18.4, 20.3),
        ),
        (
            "Temperaturspanne Nord",
            temperatur_spanne(
                MESSDATEN["Nord"]["temperaturen"]
            ),
            1.9,
        ),
        (
            "Wärmste Station",
            (
                waermste_station(
                    MESSDATEN
                )[0],
                round(
                    waermste_station(
                        MESSDATEN
                    )[1],
                    2,
                ),
            ),
            ("Sued", 22.43),
        ),
        (
            "Sensor Report",
            sensor_report(
                MESSDATEN
            ),
            {
                "druck": [
                    "Nord",
                    "West",
                ],
                "feuchtigkeit": [
                    "Nord",
                    "Sued",
                ],
                "licht": [
                    "Sued",
                ],
                "temperatur": [
                    "Nord",
                    "Sued",
                    "West",
                ],
            },
        ),
        (
            "Stationen nach Durchschnitt",
            stationen_nach_durchschnitt(
                MESSDATEN
            ),
            [
                "Sued",
                "Nord",
                "West",
            ],
        ),
        (
            "Zusammenfassung Nord",
            station_zusammenfassung(
                "Nord",
                MESSDATEN,
            ),
            {
                "name": "Nord",
                "mittelwert": 19.266666666666668,
                "spanne": 1.9,
                "sensoren": [
                    "druck",
                    "feuchtigkeit",
                    "temperatur",
                ],
            },
        ),
    ]

    for name, erhalten, erwartet in ergebnisse:

        if erhalten == erwartet:

            print(
                f"✓ {name}"
            )

        else:

            print(
                f"✗ {name} → "
                f"erwartet {erwartet!r}, "
                f"erhalten {erhalten!r}"
            )


# ---------------------------------------------------------------- Start

if __name__ == "__main__":

    if (
        len(sys.argv) > 1
        and sys.argv[1] == "test"
    ):

        try:

            selbsttest()

        except Exception as fehler:

            print(
                f"✗ Selbsttest abgebrochen: "
                f"{type(fehler).__name__}: {fehler}"
            )

            print(
                "  (Vermutlich ist eine Funktion "
                "noch nicht fertig.)"
            )

    else:

        main()