"""Tag 2 – Mini-Projekt: Reiseplaner (LÖSUNG)

Lösung zum Starter-Projekt.

Themen:

- Listen
- Tupel
- Dictionaries
- Sets
- sorted()
- Schleifen
- Bedingungen
- verschachtelte Datenstrukturen
"""

import sys


# ---------------------------------------------------------------- Daten

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


# ---------------------------------------------------------------- Funktion 1

def reisedauer(tage):
    """Gibt die Reisedauer als Text zurück."""

    return f"{tage} Tage"


# ---------------------------------------------------------------- Funktion 2

def reisebereich(reisen):
    """
    Gibt die kürzeste und längste Reise als Tupel zurück.
    """

    tage = []

    for reise in reisen.values():
        tage.append(reise["tage"])

    return min(tage), max(tage)


# ---------------------------------------------------------------- Funktion 3

def durchschnittliche_reisedauer(reisen):
    """Berechnet die durchschnittliche Reisedauer."""

    tage = []

    for reise in reisen.values():
        tage.append(reise["tage"])

    return sum(tage) / len(tage)


# ---------------------------------------------------------------- Funktion 4

def laengste_reise(reisen):
    """
    Findet die Reise mit den meisten Tagen.

    Rückgabe:

    (stadt, tage)
    """

    laengste_stadt = None
    laengste_tage = 0

    for stadt, reise in reisen.items():

        tage = reise["tage"]

        if tage > laengste_tage:
            laengste_tage = tage
            laengste_stadt = stadt

    return laengste_stadt, laengste_tage


# ---------------------------------------------------------------- Funktion 5

def kategorie_report(reisen):
    """
    Erstellt eine Übersicht der Kategorien.
    """

    report = {}

    for stadt, reise in reisen.items():

        kategorien = reise["kategorien"]

        for kategorie in kategorien:

            if kategorie not in report:
                report[kategorie] = []

            report[kategorie].append(stadt)

    for kategorie in report:
        report[kategorie] = sorted(report[kategorie])

    return dict(sorted(report.items()))


# ---------------------------------------------------------------- Funktion 6

def staedte_nach_reisedauer(reisen):
    """
    Gibt die Städte nach ihrer Reisedauer
    absteigend sortiert zurück.
    """

    reisedauern = {}

    for stadt, reise in reisen.items():

        reisedauern[stadt] = reise["tage"]

    sortierte_staedte = sorted(
        reisedauern,
        key=reisedauern.get,
        reverse=True,
    )

    return sortierte_staedte


# ---------------------------------------------------------------- Funktion 7

def reise_zusammenfassung(stadt, reisen):
    """
    Erstellt eine Zusammenfassung einer Reise.
    """

    reise = reisen[stadt]

    zusammenfassung = {
        "stadt": stadt,
        "land": reise["land"],
        "tage": reise["tage"],
        "aktivitaeten": reise["aktivitaeten"],
        "kategorien": sorted(reise["kategorien"]),
    }

    return zusammenfassung


# ---------------------------------------------------------------- Ausgabe

def reise_anzeigen(stadt, reisen):
    """Gibt eine Reise übersichtlich aus."""

    zusammenfassung = reise_zusammenfassung(
        stadt,
        reisen,
    )

    print()
    print(f"=== {zusammenfassung['stadt']} ===")
    print(f"Land: {zusammenfassung['land']}")
    print(f"Dauer: {zusammenfassung['tage']} Tage")

    print("Aktivitäten:")

    for aktivitaet in zusammenfassung["aktivitaeten"]:
        print(f"- {aktivitaet}")

    print("Kategorien:")

    for kategorie in zusammenfassung["kategorien"]:
        print(f"- {kategorie}")


def alle_reisen_anzeigen(reisen):
    """Gibt alle Städte alphabetisch sortiert aus."""

    staedte = sorted(reisen)

    for stadt in staedte:
        reise_anzeigen(stadt, reisen)


def kategorien_anzeigen(reisen):
    """Gibt alle Kategorien und ihre Städte aus."""

    report = kategorie_report(reisen)

    print()

    for kategorie, staedte in report.items():

        print(f"{kategorie}:")

        for stadt in staedte:
            print(f"- {stadt}")

        print()


# ---------------------------------------------------------------- Hauptprogramm

def main():

    reisen = REISEN

    while True:

        print()
        print("=== Reiseplaner ===")
        print("1 - Alle Reisen anzeigen")
        print("2 - Eine Reise anzeigen")
        print("3 - Längste Reise anzeigen")
        print("4 - Städte nach Reisedauer sortieren")
        print("5 - Kategorien anzeigen")
        print("6 - Reisebereich anzeigen")
        print("0 - Programm beenden")

        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":

            alle_reisen_anzeigen(reisen)

        elif auswahl == "2":

            stadt = input("Stadt: ").strip()

            if stadt in reisen:
                reise_anzeigen(stadt, reisen)
            else:
                print("Reiseziel nicht gefunden.")

        elif auswahl == "3":

            stadt, tage = laengste_reise(reisen)

            print()
            print("Längste Reise:")
            print(f"{stadt} mit {tage} Tagen")

        elif auswahl == "4":

            staedte = staedte_nach_reisedauer(reisen)

            print()
            print("Städte nach Reisedauer:")

            for stadt in staedte:
                print(stadt)

        elif auswahl == "5":

            kategorien_anzeigen(reisen)

        elif auswahl == "6":

            minimum, maximum = reisebereich(reisen)

            print()
            print("Reisedauer:")
            print(f"Kürzeste Reise: {minimum} Tage")
            print(f"Längste Reise:  {maximum} Tage")

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
            "Reisedauer",
            reisedauer(4),
            "4 Tage",
        ),
        (
            "Reisebereich",
            reisebereich(REISEN),
            (3, 5),
        ),
        (
            "Durchschnittliche Reisedauer",
            round(
                durchschnittliche_reisedauer(REISEN),
                2,
            ),
            4.0,
        ),
        (
            "Längste Reise",
            laengste_reise(REISEN),
            ("Rom", 5),
        ),
        (
            "Kategorie Report",
            kategorie_report(REISEN),
            {
                "Essen": [
                    "Lissabon",
                    "Paris",
                    "Rom",
                ],
                "Geschichte": [
                    "Rom",
                ],
                "Kultur": [
                    "Paris",
                    "Rom",
                ],
                "Meer": [
                    "Lissabon",
                ],
                "Stadt": [
                    "Lissabon",
                    "Paris",
                ],
            },
        ),
        (
            "Städte nach Reisedauer",
            staedte_nach_reisedauer(REISEN),
            [
                "Rom",
                "Paris",
                "Lissabon",
            ],
        ),
        (
            "Zusammenfassung Paris",
            reise_zusammenfassung(
                "Paris",
                REISEN,
            ),
            {
                "stadt": "Paris",
                "land": "Frankreich",
                "tage": 4,
                "aktivitaeten": [
                    "Eiffelturm",
                    "Louvre",
                    "Seine",
                ],
                "kategorien": [
                    "Essen",
                    "Kultur",
                    "Stadt",
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
                "  (Vermutlich ist eine Funktion "
                "noch nicht fertig.)"
            )

    else:

        main()