"""Tag 2 – Mini-Projekt: Messdaten-Analyse – LÖSUNG

Themen:
- Listen
- Tupel
- Dictionaries
- Sets
- sorted()
- verschachtelte Datenstrukturen

Starten:      python projekt_loesung.py
Selbsttest:   python projekt_loesung.py test
"""

import sys


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
    """Berechnet den Durchschnitt einer Liste von Messwerten."""
    return sum(messwerte) / len(messwerte)


# ---------------------------------------------------------------- Funktion 2
def station_auswerten(name, messdaten):
    """
    Gibt Minimum, Maximum und Durchschnitt
    einer Station als Tupel zurück.
    """
    temperaturen = messdaten[name]["temperaturen"]

    kleinster = min(temperaturen)
    groesster = max(temperaturen)
    durchschnitt = berechne_mittelwert(temperaturen)

    return kleinster, groesster, durchschnitt


# ---------------------------------------------------------------- Funktion 3
def stationen_mit_hoher_temperatur(messdaten, grenzwert):
    """
    Gibt die Namen der Stationen zurück,
    deren Durchschnittstemperatur mindestens den Grenzwert erreicht.
    """
    ergebnis = []

    for name in messdaten:
        temperaturen = messdaten[name]["temperaturen"]
        durchschnitt = berechne_mittelwert(temperaturen)

        if durchschnitt >= grenzwert:
            ergebnis.append(name)

    return sorted(ergebnis)


# ---------------------------------------------------------------- Funktion 4
def gemeinsame_sensoren(messdaten, station_a, station_b):
    """Gibt die Sensoren zurück, die beide Stationen verwenden."""
    sensor_a = messdaten[station_a]["sensoren"]
    sensor_b = messdaten[station_b]["sensoren"]

    gemeinsame = sensor_a & sensor_b

    return sorted(gemeinsame)


# ---------------------------------------------------------------- Funktion 5
def alle_sensoren(messdaten):
    """Gibt alle unterschiedlichen Sensoren sortiert zurück."""
    alle = set()

    for station in messdaten:
        sensoren = messdaten[station]["sensoren"]

        for sensor in sensoren:
            alle.add(sensor)

    return sorted(alle)


# ---------------------------------------------------------------- Funktion 6
def stationen_sortiert(messdaten):
    """Gibt die Stationsnamen alphabetisch sortiert zurück."""
    return sorted(messdaten)


# ---------------------------------------------------------------- Funktion 7
def zusammenfassung(messdaten):
    """
    Erstellt für jede Station eine Zusammenfassung.

    Rückgabe:
    {
        "Nord": {
            "min": 18.4,
            "max": 20.3,
            "mittelwert": 19.266666666666668
        },
        ...
    }
    """
    ergebnis = {}

    for name in messdaten:
        temperaturen = messdaten[name]["temperaturen"]

        ergebnis[name] = {
            "min": min(temperaturen),
            "max": max(temperaturen),
            "mittelwert": berechne_mittelwert(temperaturen),
        }

    return ergebnis


# ---------------------------------------------------------------- Ausgabe
def station_anzeigen(name, messdaten):
    """Gibt eine Station mit ihren Messdaten aus."""

    daten = messdaten[name]
    temperaturen = daten["temperaturen"]
    sensoren = sorted(daten["sensoren"])

    kleinster, groesster, durchschnitt = station_auswerten(
        name,
        messdaten,
    )

    print()
    print(f"Station: {name}")
    print(f"Temperaturen: {temperaturen}")
    print(f"Minimum:      {kleinster:.1f} °C")
    print(f"Maximum:      {groesster:.1f} °C")
    print(f"Durchschnitt: {durchschnitt:.2f} °C")
    print(f"Sensoren:     {', '.join(sensoren)}")


def alle_station_anzeigen(messdaten):
    """Gibt alle Stationen alphabetisch sortiert aus."""

    for name in sorted(messdaten):
        station_anzeigen(name, messdaten)


# ---------------------------------------------------------------- Hauptprogramm
def main():
    messdaten = MESSDATEN

    while True:
        print()
        print("=== Messdaten-Analyse ===")
        print("1 - Stationen anzeigen")
        print("2 - Station auswerten")
        print("3 - Stationen alphabetisch anzeigen")
        print("4 - Gemeinsame Sensoren vergleichen")
        print("5 - Alle verwendeten Sensoren anzeigen")
        print("6 - Stationen über Temperaturgrenze")
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
            print()

            for name in stationen_sortiert(messdaten):
                print(name)

        elif auswahl == "4":
            station_a = input("Erste Station: ").strip()
            station_b = input("Zweite Station: ").strip()

            if station_a not in messdaten or station_b not in messdaten:
                print("Mindestens eine Station wurde nicht gefunden.")
            else:
                sensoren = gemeinsame_sensoren(
                    messdaten,
                    station_a,
                    station_b,
                )

                print()
                print("Gemeinsame Sensoren:")

                for sensor in sensoren:
                    print(sensor)

        elif auswahl == "5":
            sensoren = alle_sensoren(messdaten)

            print()
            print("Alle verwendeten Sensoren:")

            for sensor in sensoren:
                print(sensor)

        elif auswahl == "6":
            eingabe = input("Temperaturgrenze: ").strip()

            try:
                grenzwert = float(eingabe)

                stationen = stationen_mit_hoher_temperatur(
                    messdaten,
                    grenzwert,
                )

                print()

                if stationen:
                    print("Stationen über der Grenze:")

                    for name in stationen:
                        print(name)
                else:
                    print("Keine Station erreicht die Grenze.")

            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        elif auswahl == "0":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Auswahl.")


# ---------------------------------------------------------------- Selbsttest
def selbsttest():
    """Prüft die wichtigsten Funktionen."""

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
            "Auswertung Nord",
            tuple(
                round(wert, 2)
                for wert in station_auswerten(
                    "Nord",
                    MESSDATEN,
                )
            ),
            (18.4, 20.3, 19.27),
        ),
        (
            "Stationen ab 20 °C",
            stationen_mit_hoher_temperatur(
                MESSDATEN,
                20,
            ),
            ["Sued"],
        ),
        (
            "Gemeinsame Sensoren Nord/Sued",
            gemeinsame_sensoren(
                MESSDATEN,
                "Nord",
                "Sued",
            ),
            ["feuchtigkeit", "temperatur"],
        ),
        (
            "Alle Sensoren",
            alle_sensoren(MESSDATEN),
            ["druck", "feuchtigkeit", "licht", "temperatur"],
        ),
        (
            "Stationen sortiert",
            stationen_sortiert(MESSDATEN),
            ["Nord", "Sued", "West"],
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