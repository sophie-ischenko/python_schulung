"""Tag 2 – Mini-Projekt: Messdaten-Analyse (STARTER)

Ein Konsolenprogramm zur Auswertung von Messdaten
verschiedener Messstationen.

Die Daten liegen als verschachteltes Dictionary direkt im Programm.

In diesem Projekt werden kombiniert:

- Listen
- Tupel
- Dictionaries
- Sets
- sorted()
- Schleifen
- Bedingungen
- verschachtelte Datenstrukturen

Das Projekt ist bewusst etwas größer als die einzelnen Übungen.

Die einzelnen Funktionen bauen aufeinander auf.


STARTEN
========

Normales Programm:

    python projekt.py

Selbsttest:

    python projekt.py test
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
    """Berechnet den Durchschnitt einer nicht leeren Liste."""

    # TODO:
    # 1. Alle Werte mit sum() addieren.
    # 2. Durch die Anzahl der Werte mit len() teilen.
    # 3. Ergebnis zurückgeben.

    pass


# ---------------------------------------------------------------- Funktion 2

def temperatur_bereich(messwerte):
    """
    Gibt den kleinsten und größten Messwert als Tupel zurück.

    Beispiel:

    [18.4, 21.7, 16.2]

    wird zu:

    (16.2, 21.7)
    """

    # TODO:
    # Verwende min() und max().
    #
    # Gib beide Werte gemeinsam als Tupel zurück.

    pass


# ---------------------------------------------------------------- Funktion 3

def temperatur_spanne(messwerte):
    """
    Berechnet die Temperaturspanne einer Station.

    Die Temperaturspanne ist:

    größter Wert - kleinster Wert
    """

    # TODO:
    # 1. Bestimme den kleinsten Wert.
    # 2. Bestimme den größten Wert.
    # 3. Berechne die Differenz.
    # 4. Gib die Differenz zurück.

    pass


# ---------------------------------------------------------------- Funktion 4

def waermste_station(messdaten):
    """
    Findet die Station mit dem höchsten Durchschnitt.

    Rückgabe:

    (
        stationsname,
        durchschnitt
    )

    Beispiel:

    ("Sued", 22.43)
    """

    # TODO:
    #
    # Erstelle zunächst Variablen für:
    #
    # - bisher höchste Durchschnittstemperatur
    # - Name der bisher wärmsten Station
    #
    # Laufe anschließend durch alle Stationen.
    #
    # Für jede Station:
    #
    # 1. Temperaturen aus dem Dictionary holen.
    # 2. Durchschnitt berechnen.
    # 3. Prüfen, ob dieser Durchschnitt höher ist.
    # 4. Falls ja, Namen und Durchschnitt speichern.
    #
    # Am Ende beide Werte als Tupel zurückgeben.

    pass


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

    Die Sensoren sollen alphabetisch sortiert sein.
    Auch die Stationsnamen innerhalb der Listen sollen
    alphabetisch sortiert sein.
    """

    # TODO:
    #
    # Erstelle ein leeres Dictionary.
    #
    # Laufe durch alle Stationen.
    #
    # Hole die Sensoren der jeweiligen Station.
    #
    # Für jeden Sensor:
    #
    # - Wenn der Sensor noch nicht im Dictionary existiert:
    #   Erstelle eine neue Liste.
    #
    # - Füge anschließend den Stationsnamen hinzu.
    #
    # Sortiere am Ende die Stationsnamen jeder Sensor-Liste.
    #
    # Gib das Dictionary zurück.

    pass


# ---------------------------------------------------------------- Funktion 6

def stationen_nach_durchschnitt(messdaten):
    """
    Gibt die Stationsnamen nach ihrer Durchschnittstemperatur
    absteigend sortiert zurück.

    Beispiel:

    ["Sued", "Nord", "West"]

    Die wärmste Station steht also zuerst.
    """

    # TODO:
    #
    # Erstelle zunächst ein Dictionary mit:
    #
    # Stationsname → Durchschnittstemperatur
    #
    # Beispiel:
    #
    # {
    #     "Nord": 19.27,
    #     "Sued": 22.43,
    #     "West": 18.67
    # }
    #
    # Sortiere anschließend die Stationsnamen nach
    # ihrer Durchschnittstemperatur.
    #
    # Hinweis:
    # Für diese Aufgabe reicht sorted() zusammen mit
    # einer Schleife über die Stationen.
    #
    # Wenn du bereits weißt, wie key= funktioniert,
    # darfst du es verwenden.
    #
    # Wenn nicht, kannst du die Aufgabe zunächst
    # mit einer einfacheren Lösung bearbeiten.

    pass


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

    Die Sensoren sollen sortiert zurückgegeben werden.
    """

    # TODO:
    #
    # 1. Station aus dem Dictionary holen.
    # 2. Temperaturen holen.
    # 3. Durchschnitt berechnen.
    # 4. Temperaturspanne berechnen.
    # 5. Sensoren holen und sortieren.
    # 6. Alles in einem neuen Dictionary speichern.
    # 7. Dictionary zurückgeben.

    pass


# ---------------------------------------------------------------- Ausgabe

def station_anzeigen(name, messdaten):
    """Gibt eine Station mit ihren wichtigsten Daten aus."""

    # TODO:
    #
    # Verwende station_zusammenfassung().
    #
    # Gib anschließend übersichtlich aus:
    #
    # - Name
    # - Temperaturen
    # - Mittelwert
    # - Temperaturspanne
    # - Sensoren

    pass


def alle_station_anzeigen(messdaten):
    """Gibt alle Stationen alphabetisch sortiert aus."""

    # TODO:
    #
    # Stationen mit sorted() sortieren.
    #
    # Für jede Station station_anzeigen() aufrufen.

    pass


def sensoren_anzeigen(messdaten):
    """Gibt eine Übersicht der Sensoren und ihrer Stationen aus."""

    # TODO:
    #
    # Verwende sensor_report().
    #
    # Gib für jeden Sensor die zugehörigen Stationen aus.

    pass


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

        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":

            alle_station_anzeigen(messdaten)

        elif auswahl == "2":

            name = input("Stationsname: ").strip()

            if name in messdaten:
                station_anzeigen(name, messdaten)
            else:
                print("Station nicht gefunden.")

        elif auswahl == "3":

            name, durchschnitt = waermste_station(messdaten)

            print()
            print("Wärmste Station:")
            print(f"{name} mit {durchschnitt:.2f} °C")

        elif auswahl == "4":

            stationen = stationen_nach_durchschnitt(messdaten)

            print()
            print("Stationen nach Durchschnittstemperatur:")

            for name in stationen:
                print(name)

        elif auswahl == "5":

            sensoren_anzeigen(messdaten)

        elif auswahl == "0":

            print("Programm beendet.")
            break

        else:

            print("Ungültige Auswahl.")


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
            tuple(
                [
                    waermste_station(MESSDATEN)[0],
                    round(
                        waermste_station(MESSDATEN)[1],
                        2,
                    ),
                ]
            ),
            ("Sued", 22.43),
        ),
        (
            "Sensor Report",
            sensor_report(MESSDATEN),
            {
                "druck": ["Nord", "West"],
                "feuchtigkeit": ["Nord", "Sued"],
                "licht": ["Sued"],
                "temperatur": ["Nord", "Sued", "West"],
            },
        ),
        (
            "Stationen nach Durchschnitt",
            stationen_nach_durchschnitt(MESSDATEN),
            ["Sued", "Nord", "West"],
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
            print(f"✓ {name}")

        else:
            print(
                f"✗ {name} → "
                f"erwartet {erwartet!r}, "
                f"erhalten {erhalten!r}"
            )


# ---------------------------------------------------------------- Start

if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "test":

        try:
            selbsttest()

        except Exception as fehler:

            print(
                f"✗ Selbsttest abgebrochen: "
                f"{type(fehler).__name__}: {fehler}"
            )

            print(
                "  (Vermutlich ist eine Funktion noch nicht fertig.)"
            )

    else:

        main()