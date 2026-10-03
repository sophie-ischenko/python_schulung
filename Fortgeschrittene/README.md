# Python-Kurs: 5 Tage mit Mini-Projekten (ohne Klassen)

**Voraussetzung:** Programmiergrundlagen bis einschließlich Funktionen (Tag 1 frischt alles auf und baut es aus).
**Technik:** Nur Python 3.10+ und ein Editor (IDLE, Thonny oder VS Code). Alles nutzt die Standardbibliothek (inkl. `tkinter`), **keine Internetverbindung nötig**.
**Stil:** Es werden **keine eigenen Klassen** geschrieben – alles besteht aus Funktionen, Listen, Dictionaries und Dateien. (`tkinter` benutzt zwar intern Objekte wie `Label` und `Button`, du definierst aber keine eigenen.)

## Überblick

| Tag | Thema | Mini-Projekt |
|---|---|---|
| 1 | Willkommen in der Code-Akademie: Datentypen, Eingaben, Strings, Listen, Funktionen | **Operation Code-Knacker** (Galgenmännchen im Terminal) |
| 2 | Datenstrukturen vertiefen: Listen, Tupel, Dictionaries, Sets, Comprehensions | Kontaktbuch |
| 3 | Dateien, CSV/JSON, Fehlerbehandlung, Module | Haushaltsbuch |
| 4 | Standardbibliothek (datetime, collections, re) und Fenster mit tkinter | **Python-Quiz-Show** (Fenster, Countdown, Fragen aus JSON) |
| 5 | Qualität: Debugging, Tests mit `assert`, argparse, logging | Datei-Organizer |

## Inhalt je Tag

| Datei | Wer | Zweck |
|---|---|---|
| `theorie.md` | Teilnehmende | Theorie (Definition → Warum wichtig → Syntax → Beispiel → Merksatz) mit Beispielen und Erklärungen, Beschreibung der Aufgaben und des Projekts |
| `aufgaben.py` | Teilnehmende | Übungen mit TODOs; Selbstprüfung mit ✓ / ✗ beim Start |
| `projekt.py` | Teilnehmende | Mini-Projekt als Gerüst mit TODOs; `python projekt.py test` prüft die Funktionen |
| `aufgaben_loesung.py`, `projekt_loesung.py` | Trainerin | Lauffähige Musterlösungen |

Zusätzlich:
- **Tag 1:** `start_demo.py` – der Agentenausweis-Generator zum Vorführen am Anfang des Tages.
- **Tag 4:** `gui_aufgaben.py` (3 tkinter-Aufgaben), `beispiel_pomodoro.py` (Pomodoro-Timer zum gemeinsamen Durchgehen) und `fragen.json` (die Fragen der Quiz-Show, beliebig erweiterbar).
- **Tag 5:** statt `aufgaben.py` / `projekt.py` eigene Dateien (siehe `tag5/theorie.md`): `debugging_aufgabe.py`, `funktionen.py` + `test_funktionen.py`, `kommandozeile.py`, `organizer.py` + `test_organizer.py` + `testdaten_erzeugen.py`.

## Tagesablauf (8 Stunden, Vorschlag)

| Zeit | Inhalt |
|---|---|
| 09:00–10:30 | Theorie mit Live-Beispielen |
| 10:45–12:15 | Übungsaufgaben (`aufgaben.py`) |
| 13:15–14:00 | Besprechung der Lösungen |
| 14:00–16:30 | Mini-Projekt (`projekt.py`) |
| 16:30–17:00 | Vorstellung, Fragen, Ausblick auf morgen |

### Tag 1 im Detail (Einstieg mit Story)

| Zeit | Inhalt |
|---|---|
| 09:00–09:30 | Start-Demo: `start_demo.py` laufen lassen, gemeinsam erklären (Abschnitt 0 der Theorie) |
| 09:30–10:30 | Theorie 1–5: `print`, Datentypen, `input` verarbeiten, Strings |
| 10:45–12:15 | Mission 1 (Agentenausweis) und Mission 2 (Geheimschrift) |
| 13:15–14:00 | Theorie 6–8: Listen, Funktionen, Passwort-Check |
| 14:00–14:45 | Mission 3 (Listen) und Mission 4 (Funktionen) |
| 14:45–16:30 | Mini-Projekt Operation Code-Knacker |
| 16:30–17:00 | Spielrunde im Plenum: wer knackt den Code in den wenigsten Versuchen? |

### Tag 4 im Detail

| Zeit | Inhalt |
|---|---|
| 09:00–10:15 | Standardbibliothek (Theorie Teil 1) und `aufgaben.py` |
| 10:30–12:15 | tkinter-Grundlagen (Teil 2) und `gui_aufgaben.py` |
| 13:15–14:00 | Pomodoro-Beispiel gemeinsam durchgehen (`after`, Canvas, Zustand im Dictionary) |
| 14:00–16:30 | Mini-Projekt Quiz-Show |
| 16:30–17:00 | Quiz-Duell im Plenum, Bonusideen sammeln |

## Hinweise für die Trainerin

- Die Starter-Dateien (`aufgaben.py`, `gui_aufgaben.py`, `projekt.py`, `test_funktionen.py`, `kommandozeile.py`, `organizer.py`) werden aus den Lösungsdateien erzeugt. Wenn du eine Lösung änderst, aus dem Kursordner `python _werkzeuge/starter_erzeugen.py` ausführen. Marker: `# >>> Hinweis` … `# <<<`.
- Alle Lösungen und Selbsttests wurden durchlaufen; die Starter geben vor der Bearbeitung ✗ aus.
- Tag 4: `tkinter` ist bei Python für Windows/macOS dabei, unter Linux evtl. `python3-tk` vorab installieren (`python -c "import tkinter"` zum Testen). Die Selbsttests mit Fenster werden ohne Bildschirm übersprungen.
- Tag 4: Die Quiz-Show liest `fragen.json` und schreibt `highscore.json` in den Ordner der Datei. Zum Zurücksetzen `highscore.json` löschen.
- Tag 5: Tests sind einfache Funktionen mit `assert` und einem kleinen Test-Läufer am Dateiende. Das Muster funktioniert später unverändert mit `pytest`.
- Schnelle Teilnehmende: Zusatzaufgaben (★) und Bonusideen am Ende jeder `theorie.md`.
