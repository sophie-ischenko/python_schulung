
"""Tag 3 – Aufgaben (LÖSUNG)

Thema:
Dateien lesen und schreiben, CSV, JSON,
Fehlerbehandlung und pathlib.

Die Aufgaben arbeiten mit kleinen Beispieldateien
im Ordner "beispieldateien".

Starte die Datei:
    python aufgaben_loesung.py

Am Ende siehst du, welche Aufgaben stimmen (✓ / ✗).
"""

import csv
import json
from pathlib import Path


# ---------------------------------------------------------------------------
# Pfad zu den Beispieldateien
# ---------------------------------------------------------------------------

BEISPIELORDNER = Path(__file__).parent / "beispieldateien"


def check(name, erhalten, erwartet):
    """Vergleicht Ergebnis und Erwartung und gibt ✓ oder ✗ aus."""
    if erhalten == erwartet:
        print(f"✓ {name}")
    else:
        print(
            f"✗ {name} → "
            f"erwartet {erwartet!r}, "
            f"erhalten {erhalten!r}"
        )


# ---------------------------------------------------------------- Aufgabe 1
def zeilen_zaehlen(pfad):
    """Zählt die nicht-leeren Zeilen einer Textdatei."""

    anzahl = 0

    with open(pfad, encoding="utf-8") as datei:
        for zeile in datei:
            if zeile.strip():
                anzahl += 1

    return anzahl


# ---------------------------------------------------------------- Aufgabe 2
def summe_aus_csv(pfad, spalte):
    """Addiert alle Zahlen einer CSV-Spalte."""

    summe = 0

    with open(
        pfad,
        encoding="utf-8",
        newline="",
    ) as datei:

        reader = csv.DictReader(datei)

        for zeile in reader:
            wert = float(zeile[spalte])
            summe += wert

    return summe


# ---------------------------------------------------------------- Aufgabe 3
def sichere_zahl(text, standard=None):
    """
    Wandelt Text in eine Zahl um.

    Beispiel:
        "3,5" -> 3.5

    Bei ungültiger Eingabe wird der Standardwert zurückgegeben.
    """

    text = text.replace(",", ".")

    try:
        return float(text)
    except ValueError:
        return standard


# ---------------------------------------------------------------- Aufgabe 4
def json_speichern(daten, pfad):
    """Speichert Daten als gut lesbares JSON."""

    with open(
        pfad,
        "w",
        encoding="utf-8",
    ) as datei:

        json.dump(
            daten,
            datei,
            ensure_ascii=False,
            indent=2,
        )


def json_laden(pfad, standard=None):
    """
    Lädt eine JSON-Datei.

    Wenn die Datei fehlt oder kein gültiges JSON enthält,
    wird der Standardwert zurückgegeben.
    """

    try:
        with open(
            pfad,
            encoding="utf-8",
        ) as datei:

            return json.load(datei)

    except FileNotFoundError:
        return standard

    except json.JSONDecodeError:
        return standard


# ---------------------------------------------------------------- Aufgabe 5
def pruefe_betrag(betrag):
    """
    Gibt den Betrag zurück.

    Ist der Betrag nicht größer als 0,
    wird ein ValueError ausgelöst.
    """

    if betrag <= 0:
        raise ValueError(
            "Der Betrag muss größer als 0 sein."
        )

    return betrag


# ---------------------------------------------------------------- Aufgabe 6
def dateiendungen_zaehlen(ordner):
    """
    Zählt die Dateien in einem Ordner nach Dateiendung.

    Unterordner werden ignoriert.

    Beispiel:
        {
            ".csv": 1,
            ".json": 2,
            ".txt": 2
        }
    """

    zaehler = {}

    ordner = Path(ordner)

    for datei in ordner.iterdir():

        if not datei.is_file():
            continue

        endung = datei.suffix.lower()

        if endung in zaehler:
            zaehler[endung] += 1
        else:
            zaehler[endung] = 1

    return zaehler


# ---------------------------------------------------------------------------
# Selbsttest
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("=== Tag 3 – Aufgaben (LÖSUNG) ===")
    print()
    print(f"Beispieldateien: {BEISPIELORDNER}")
    print()

    # -----------------------------------------------------------------------
    # Aufgabe 1
    # -----------------------------------------------------------------------

    notizen = BEISPIELORDNER / "notizen.txt"

    check(
        "1 zeilen_zaehlen",
        zeilen_zaehlen(notizen),
        4,
    )

    # -----------------------------------------------------------------------
    # Aufgabe 2
    # -----------------------------------------------------------------------

    ausgaben = BEISPIELORDNER / "ausgaben.csv"

    check(
        "2 summe_aus_csv",
        summe_aus_csv(ausgaben, "betrag"),
        45.0,
    )

    # -----------------------------------------------------------------------
    # Aufgabe 3
    # -----------------------------------------------------------------------

    check(
        "3a sichere_zahl",
        sichere_zahl("3,5"),
        3.5,
    )

    check(
        "3b sichere_zahl (Fehler)",
        sichere_zahl("abc", standard=0),
        0,
    )

    # -----------------------------------------------------------------------
    # Aufgabe 4
    # -----------------------------------------------------------------------

    daten = BEISPIELORDNER / "daten.json"

    geladene_daten = json_laden(daten)

    check(
        "4a json_laden",
        geladene_daten,
        {
            "name": "Jörg",
            "werte": [1, 2, 3],
        },
    )

    fehlende_datei = (
        BEISPIELORDNER / "gibt_es_nicht.json"
    )

    check(
        "4b json fehlt",
        json_laden(
            fehlende_datei,
            standard=[],
        ),
        [],
    )

    kaputte_datei = (
        BEISPIELORDNER / "kaputt.json"
    )

    check(
        "4c json kaputt",
        json_laden(
            kaputte_datei,
            standard={},
        ),
        {},
    )

    # json_speichern testen
    gespeicherte_datei = (
        BEISPIELORDNER / "test_gespeichert.json"
    )

    json_speichern(
        {
            "name": "Jörg",
            "werte": [1, 2, 3],
        },
        gespeicherte_datei,
    )

    check(
        "4d json_speichern",
        json_laden(gespeicherte_datei),
        {
            "name": "Jörg",
            "werte": [1, 2, 3],
        },
    )

    # Testdatei wieder entfernen
    if gespeicherte_datei.exists():
        gespeicherte_datei.unlink()

    # -----------------------------------------------------------------------
    # Aufgabe 5
    # -----------------------------------------------------------------------

    try:
        pruefe_betrag(-5)
        ergebnis = "keine Exception"
    except ValueError:
        ergebnis = "ValueError"

    check(
        "5a pruefe_betrag(-5)",
        ergebnis,
        "ValueError",
    )

    check(
        "5b pruefe_betrag(10)",
        pruefe_betrag(10),
        10,
    )

    # -----------------------------------------------------------------------
    # Aufgabe 6
    # -----------------------------------------------------------------------

    check(
        "6 dateiendungen_zaehlen",
        dateiendungen_zaehlen(BEISPIELORDNER),
        {
            ".csv": 1,
            ".json": 2,
            ".txt": 1,
        },
    )

    print()
    print("=== Selbsttest beendet ===")
