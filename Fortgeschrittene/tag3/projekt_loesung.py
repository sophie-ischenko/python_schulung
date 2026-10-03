
"""Tag 3 – Mini-Projekt: Haushaltsbuch (LÖSUNG)

Einnahmen und Ausgaben erfassen und als JSON speichern.

Einnahmen werden positiv gespeichert.
Ausgaben werden negativ gespeichert.

Das Programm kann:
- Buchungen erfassen
- Buchungen dauerhaft als JSON speichern
- einen Monat auswerten
- alle Buchungen anzeigen
- fehlerhafte Eingaben abfangen

Starten:
    python projekt_loesung.py

Selbsttest:
    python projekt_loesung.py test
"""

import json
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Datei
# ---------------------------------------------------------------------------

DATEI = Path(__file__).parent / "haushaltsbuch.json"


# ---------------------------------------------------------------------------
# JSON laden
# ---------------------------------------------------------------------------

def laden(pfad=DATEI):
    """
    Lädt die Buchungsliste aus einer JSON-Datei.

    Fehlt die Datei oder enthält sie ungültiges JSON,
    wird eine leere Liste zurückgegeben.
    """

    try:
        with open(
            pfad,
            encoding="utf-8",
        ) as datei:
            return json.load(datei)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# ---------------------------------------------------------------------------
# JSON speichern
# ---------------------------------------------------------------------------

def speichern(buchungen, pfad=DATEI):
    """Speichert die Buchungsliste als gut lesbares JSON."""

    with open(
        pfad,
        "w",
        encoding="utf-8",
    ) as datei:

        json.dump(
            buchungen,
            datei,
            ensure_ascii=False,
            indent=2,
        )


# ---------------------------------------------------------------------------
# Buchung hinzufügen
# ---------------------------------------------------------------------------

def buchung_hinzufuegen(
    buchungen,
    datum_text,
    kategorie,
    betrag_text,
    beschreibung="",
):
    """
    Prüft die Eingaben und hängt eine Buchung an die Liste an.

    datum_text:
        Format TT.MM.JJJJ

    betrag_text:
        Zahl, zum Beispiel:
        "2500"
        "-45.90"
        "-45,90"

        Positive Werte sind Einnahmen.
        Negative Werte sind Ausgaben.

    Rückgabe:
        Die neu erstellte Buchung.

    Bei ungültigen Eingaben:
        ValueError
    """

    # -----------------------------------------------------------------------
    # Datum prüfen
    # -----------------------------------------------------------------------

    teile = datum_text.split(".")

    if len(teile) != 3:
        raise ValueError(
            "Das Datum muss das Format TT.MM.JJJJ haben."
        )

    tag = teile[0]
    monat = teile[1]
    jahr = teile[2]

    if (
        len(tag) != 2
        or len(monat) != 2
        or len(jahr) != 4
    ):
        raise ValueError(
            "Das Datum muss das Format TT.MM.JJJJ haben."
        )

    if (
        not tag.isdigit()
        or not monat.isdigit()
        or not jahr.isdigit()
    ):
        raise ValueError(
            "Das Datum darf nur Zahlen enthalten."
        )

    # -----------------------------------------------------------------------
    # Kategorie prüfen
    # -----------------------------------------------------------------------

    kategorie = kategorie.strip()

    if not kategorie:
        raise ValueError(
            "Die Kategorie darf nicht leer sein."
        )

    # -----------------------------------------------------------------------
    # Betrag prüfen
    # -----------------------------------------------------------------------

    betrag_text = betrag_text.replace(",", ".")

    try:
        betrag = float(betrag_text)

    except ValueError:
        raise ValueError(
            "Der Betrag muss eine Zahl sein."
        )

    if betrag == 0:
        raise ValueError(
            "Der Betrag darf nicht 0 sein."
        )

    # -----------------------------------------------------------------------
    # Buchung erstellen
    # -----------------------------------------------------------------------

    buchung = {
        "datum": datum_text,
        "kategorie": kategorie,
        "betrag": betrag,
        "beschreibung": beschreibung.strip(),
    }

    buchungen.append(buchung)

    return buchung


# ---------------------------------------------------------------------------
# Monatsauswertung
# ---------------------------------------------------------------------------

def monatsauswertung(buchungen, jahr, monat):
    """
    Wertet einen Monat aus.

    Rückgabe:

    {
        "einnahmen": 2000.0,
        "ausgaben": 850.5,
        "saldo": 1149.5,
        "nach_kategorie": {
            "Miete": 800.0,
            "Essen": 50.5
        }
    }

    Ausgaben werden als positive Zahlen dargestellt.
    """

    einnahmen = 0.0
    ausgaben = 0.0
    nach_kategorie = {}

    for buchung in buchungen:

        datum = buchung["datum"]
        teile = datum.split(".")

        buchungsmonat = int(teile[1])
        buchungsjahr = int(teile[2])

        if (
            buchungsjahr != jahr
            or buchungsmonat != monat
        ):
            continue

        betrag = buchung["betrag"]

        if betrag > 0:
            einnahmen += betrag

        else:
            ausgabe = betrag * -1
            ausgaben += ausgabe

            kategorie = buchung["kategorie"]

            if kategorie in nach_kategorie:
                nach_kategorie[kategorie] += ausgabe
            else:
                nach_kategorie[kategorie] = ausgabe

    saldo = einnahmen - ausgaben

    return {
        "einnahmen": round(einnahmen, 2),
        "ausgaben": round(ausgaben, 2),
        "saldo": round(saldo, 2),
        "nach_kategorie": nach_kategorie,
    }


# ---------------------------------------------------------------------------
# Auswertung anzeigen
# ---------------------------------------------------------------------------

def auswertung_anzeigen(auswertung):
    """Gibt eine Monatsauswertung übersichtlich aus."""

    print()
    print("=== Monatsauswertung ===")
    print()

    print(
        f"Einnahmen: {auswertung['einnahmen']:>10.2f} €"
    )

    print(
        f"Ausgaben:  {auswertung['ausgaben']:>10.2f} €"
    )

    print(
        f"Saldo:     {auswertung['saldo']:>10.2f} €"
    )

    print()

    if auswertung["nach_kategorie"]:
        print("Ausgaben nach Kategorie:")

        for kategorie in sorted(
            auswertung["nach_kategorie"]
        ):
            summe = auswertung["nach_kategorie"][kategorie]

            print(
                f"  {kategorie:<15} "
                f"{summe:>10.2f} €"
            )

    else:
        print("Keine Ausgaben vorhanden.")


# ---------------------------------------------------------------------------
# Alle Buchungen anzeigen
# ---------------------------------------------------------------------------

def buchungen_anzeigen(buchungen):
    """Gibt alle gespeicherten Buchungen aus."""

    print()
    print("=== Buchungen ===")

    if not buchungen:
        print("Keine Buchungen vorhanden.")
        return

    for buchung in buchungen:
        print(
            f"{buchung['datum']} | "
            f"{buchung['kategorie']:<15} | "
            f"{buchung['betrag']:>8.2f} € | "
            f"{buchung['beschreibung']}"
        )


# ---------------------------------------------------------------------------
# Hauptprogramm
# ---------------------------------------------------------------------------

def main():
    """Startet das Haushaltsbuch."""

    buchungen = laden()

    while True:
        print()
        print("=== Haushaltsbuch ===")
        print()
        print("1 - Buchung erfassen")
        print("2 - Monatsauswertung")
        print("3 - Alle Buchungen anzeigen")
        print("0 - Beenden")
        print()

        auswahl = input("Auswahl: ").strip()

        # -------------------------------------------------------------------
        # Buchung erfassen
        # -------------------------------------------------------------------

        if auswahl == "1":
            print()
            print("Neue Buchung")
            print()

            datum = input(
                "Datum (TT.MM.JJJJ): "
            ).strip()

            kategorie = input(
                "Kategorie: "
            ).strip()

            betrag = input(
                "Betrag (+ Einnahme / - Ausgabe): "
            ).strip()

            beschreibung = input(
                "Beschreibung: "
            ).strip()

            try:
                buchung = buchung_hinzufuegen(
                    buchungen,
                    datum,
                    kategorie,
                    betrag,
                    beschreibung,
                )

                speichern(buchungen)

                print()
                print("Buchung gespeichert.")
                print(buchung)

            except ValueError as fehler:
                print()
                print(f"Fehler: {fehler}")

        # -------------------------------------------------------------------
        # Monatsauswertung
        # -------------------------------------------------------------------

        elif auswahl == "2":
            print()
            print("Monatsauswertung")

            monat_text = input(
                "Monat (MM.JJJJ): "
            ).strip()

            teile = monat_text.split(".")

            if (
                len(teile) != 2
                or len(teile[0]) != 2
                or len(teile[1]) != 4
                or not teile[0].isdigit()
                or not teile[1].isdigit()
            ):
                print(
                    "Bitte den Monat im Format MM.JJJJ eingeben."
                )
                continue

            monat = int(teile[0])
            jahr = int(teile[1])

            if monat < 1 or monat > 12:
                print(
                    "Der Monat muss zwischen 01 und 12 liegen."
                )
                continue

            auswertung = monatsauswertung(
                buchungen,
                jahr,
                monat,
            )

            auswertung_anzeigen(auswertung)

        # -------------------------------------------------------------------
        # Alle Buchungen
        # -------------------------------------------------------------------

        elif auswahl == "3":
            buchungen_anzeigen(buchungen)

        # -------------------------------------------------------------------
        # Beenden
        # -------------------------------------------------------------------

        elif auswahl == "0":
            print()
            print("Programm beendet.")
            break

        else:
            print()
            print("Ungültige Auswahl.")


# ---------------------------------------------------------------------------
# Selbsttest
# ---------------------------------------------------------------------------

def selbsttest():
    """Prüft die wichtigsten Funktionen des Projekts."""

    def ergebnis(name, erhalten, erwartet):
        if erhalten == erwartet:
            print(f"✓ {name}")
        else:
            print(
                f"✗ {name} → "
                f"erwartet {erwartet!r}, "
                f"erhalten {erhalten!r}"
            )

    print("=== Selbsttest Haushaltsbuch ===")
    print()

    # -----------------------------------------------------------------------
    # Testdaten
    # -----------------------------------------------------------------------

    buchungen = []

    buchung_hinzufuegen(
        buchungen,
        "01.10.2026",
        "Gehalt",
        "2000",
    )

    buchung_hinzufuegen(
        buchungen,
        "03.10.2026",
        "Miete",
        "-800",
    )

    buchung_hinzufuegen(
        buchungen,
        "05.10.2026",
        "Essen",
        "-50,5",
        "Wocheneinkauf",
    )

    buchung_hinzufuegen(
        buchungen,
        "01.09.2026",
        "Essen",
        "-10",
    )

    ergebnis(
        "Anzahl Buchungen",
        len(buchungen),
        4,
    )

    # -----------------------------------------------------------------------
    # Monatsauswertung
    # -----------------------------------------------------------------------

    ergebnis(
        "Oktober",
        monatsauswertung(
            buchungen,
            2026,
            10,
        ),
        {
            "einnahmen": 2000.0,
            "ausgaben": 850.5,
            "saldo": 1149.5,
            "nach_kategorie": {
                "Miete": 800.0,
                "Essen": 50.5,
            },
        },
    )

    ergebnis(
        "leerer Monat",
        monatsauswertung(
            buchungen,
            2026,
            8,
        )["saldo"],
        0.0,
    )

    # -----------------------------------------------------------------------
    # Fehler
    # -----------------------------------------------------------------------

    fehlerfaelle = [
        (
            "falsches Datumsformat",
            (
                "1.10.2026",
                "X",
                "5",
            ),
        ),
        (
            "Betrag Text",
            (
                "01.10.2026",
                "X",
                "viel",
            ),
        ),
        (
            "Betrag 0",
            (
                "01.10.2026",
                "X",
                "0",
            ),
        ),
        (
            "leere Kategorie",
            (
                "01.10.2026",
                " ",
                "5",
            ),
        ),
    ]

    for name, daten in fehlerfaelle:
        try:
            buchung_hinzufuegen(
                [],
                *daten,
            )

            ergebnis(
                name,
                "kein Fehler",
                "ValueError",
            )

        except ValueError:
            ergebnis(
                name,
                "ValueError",
                "ValueError",
            )

    # -----------------------------------------------------------------------
    # Speichern und Laden
    # -----------------------------------------------------------------------

    testdatei = (
        Path(__file__).parent
        / "haushaltsbuch_test.json"
    )

    if testdatei.exists():
        testdatei.unlink()

    ergebnis(
        "laden ohne Datei",
        laden(testdatei),
        [],
    )

    speichern(
        buchungen,
        testdatei,
    )

    ergebnis(
        "speichern + laden",
        laden(testdatei),
        buchungen,
    )

    if testdatei.exists():
        testdatei.unlink()

    print()
    print("=== Selbsttest beendet ===")


# ---------------------------------------------------------------------------
# Programmstart
# ---------------------------------------------------------------------------

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
