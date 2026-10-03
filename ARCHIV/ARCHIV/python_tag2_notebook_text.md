# Tag 2 – Notebook: Refactoring & Speicherung (JSON)

**Tagesziel:** Wir räumen das Skript von gestern mit **Funktionen** auf und geben dem Spiel ein Gedächtnis: Der Charakter wird dauerhaft in einer **JSON-Datei** gespeichert.

**Zugehörige Code-Datei:** `tag2_code.py` — enthält alle Beispiele, Übungs-Starter und das refactorte Kampf-Grundgerüst mit Charakterspeicherung als kommentierte, lauffähige Datei.

**Einstieg:** Recap Tag 1 — schaut euch euer Skript von gestern noch einmal an. Fehlerprüfung, Kampflogik und Rundenzähler kleben in einem Block. Heute lösen wir das auf.

---

## 2.1 Funktionen & Parameter

**Definition:** Eine Funktion ist ein benannter, wiederverwendbarer Codeblock, der eine klar abgegrenzte Aufgabe erfüllt. Parameter sind Platzhalter für Werte, die beim Aufruf übergeben werden.

**Warum wichtig:** Ohne Funktionen wiederholt sich Logik (z.B. Schaden würfeln) an mehreren Stellen im Code — jede Änderung müsste dann mehrfach gepflegt werden.

**Syntax:**
```
def funktionsname(parameter1, parameter2):
    """Kurzbeschreibung: Was / Parameter / Rückgabewert"""
    anweisungen
```

**Merksatz (gilt für den Rest des Kurses):** *"Jede Funktion beantwortet drei Fragen: Was macht sie? Was nimmt sie entgegen? Was gibt sie zurück?"*

**Beispiel:** siehe `tag2_code.py`, Abschnitt "2.1 Beispiel" (Funktion `begruesse`)

### Übung 1: Der smarte Kaffeevollautomat (40 Min)
*Lernziel: Funktionen definieren und Werte von außen hineinreichen.*

1. Schreibe eine Funktion `braue_kaffee(kaffee_art, zucker_wuerfel)` — beginne mit einer Docstring-Beschreibung nach dem Muster aus 2.1
2. Die Funktion simuliert den Brühvorgang mit zwei `print()`-Ausgaben
3. Wenn `zucker_wuerfel` größer als 3 ist, ergänze: *"Achtung: Sehr süß!"*
4. Rufe die Funktion dreimal mit unterschiedlichen Werten auf

→ Starter-Code: `tag2_code.py`, Abschnitt "Übung 1"

---

## 2.2 Rückgabewerte (return)

**Definition:** `return` beendet eine Funktion sofort und übergibt einen Wert an die aufrufende Stelle, statt ihn nur anzuzeigen.

**Warum wichtig:** `print()` gibt einen Wert nur auf dem Bildschirm aus — danach ist er für das Programm "weg". `return` macht das Ergebnis weiterverarbeitbar, z.B. um es später statt auf der Konsole in einem GUI-Label anzuzeigen (Tag 5).

**Syntax:**
```
def funktionsname(parameter):
    ...
    return ergebnis
```

**Merksatz:** *"print() zeigt, return liefert. Logik-Funktionen sollten fast immer return nutzen, Anzeige-Funktionen print."*

**Beispiel:** siehe `tag2_code.py`, Abschnitt "2.2 Beispiel" (Funktion `wuerfle_schaden`)

### Übung 2: Der Passwort-Prüfer (45 Min)
*Lernziel: Strikte Trennung von Logik (return) und Ausgabe (print).*

1. Schreibe eine Funktion `check_password(password)`. **Kein `print()` in der Funktion!**
2. Kürzer als 8 Zeichen -> `"schwach"`, enthält "123" -> `"sehr schwach"`, sonst -> `"stark"`
3. `while`-Schleife fragt, speichert das Ergebnis in einer Variable, gibt es mit `print` aus, bei `"stark"` mit `break` beenden

→ Starter-Code: `tag2_code.py`, Abschnitt "Übung 2"

---

## 2.3 Dateien & with

**Definition:** `open()` öffnet eine Datei zum Lesen (`"r"`) oder Schreiben (`"w"`). Der `with`-Block sorgt dafür, dass die Datei automatisch geschlossen wird — auch wenn ein Fehler auftritt.

**Warum wichtig:** Ohne dauerhafte Speicherung geht jeder Spielstand beim Beenden des Programms verloren.

**Syntax:**
```
with open("pfad", "modus", encoding="utf-8") as datei:
    ...
```

**Merksatz:** *"Immer `with` statt manuellem open()/close() — sonst riskiert man vergessene, gesperrte Dateien."*

**Beispiel:** siehe `tag2_code.py`, Abschnitt "2.3 Beispiel" (Funktion `schreibe_notiz`)

---

## 2.4 JSON

**Definition:** JSON wandelt ein Python-Dictionary in speicherbaren Text um (`json.dump`) und wieder zurück (`json.load`).

**Warum wichtig:** Ein Charakter besteht aus mehreren zusammengehörigen Werten (Name, HP, Level) — JSON speichert dieses ganze Paket in einer Datei, nicht nur eine einzelne Zahl.

**Syntax:**
```
json.dump(daten, datei)      # Dictionary -> Datei
geladen = json.load(datei)   # Datei -> Dictionary
```

**Merksatz:** *"CSV/reiner Text für einzelne Werte, JSON für zusammengehörige Datenpakete."*

**Beispiel:** siehe `tag2_code.py`, Abschnitt "2.4 Beispiel" (Funktion `speichere_charakter`)

### Übung 3: Das Rollenspiel-Inventar (45 Min)
*Lernziel: Daten laden, verändern und wieder speichern (Persistenz).*

1. Erstelle ein Dictionary `inventar = {"gold": 100, "tränke": 3}` und speichere es als `savegame.json` (mit `json.dump`)
2. Kommentiere diesen Code aus — die Datei existiert jetzt auf der Festplatte
3. Schreibe eine neue Logik: Inventar laden (`json.load`), fragen ob ein Schwert (50 Gold) gekauft wird, Dictionary aktualisieren (Gold abziehen, `"schwert": 1` hinzufügen), wieder speichern
4. Führe das Skript zweimal aus — prüfe, ob das Gold beim zweiten Start bei 50 liegt und nach erneutem Kauf auf 0 sinkt

→ Starter-Code: `tag2_code.py`, Abschnitt "Übung 3"

---

## Praxis: Den Kampf aufräumen & Charakter speichern (Gruppenarbeit, 60 Min)

Das fertige, refactorte Grundgerüst von **Dungeon Duel** steht in `tag2_code.py`, Abschnitt "Praxis: Kampf refactoren + Charakter speichern" — lauffähig und kommentiert.

**Gemeinsames Live-Coding zuerst (30 Min):** Die Logik von gestern wird in die Funktion `kampfrunde()` ausgelagert (siehe Code-Datei).

**Eure Aufgaben:**
1. Schreibe `lade_charakter()`: lädt `charakter.json`, gibt das Dictionary zurück, fängt `FileNotFoundError` ab (Standard-Charakter mit Level 1 bei erstem Start)
2. Schreibe `speichere_charakter(held)`: speichert das Dictionary als JSON
3. Einbau: Ruft `lade_charakter()` ganz am Anfang auf, gibt bei der Begrüßung Level und Anzahl besiegter Monster aus; wenn der Spieler gewinnt, wird `besiegte_monster` erhöht und gespeichert

**Profi-Challenge (optional):** Aktuell wird der Highscore/Charakter bei jedem Sieg einfach überschrieben. Baut ein einfaches Level-System: Alle 3 besiegten Monster ein Levelaufstieg, maximale HP erhöhen sich um 10.

---

**Tagesabschluss:** Unser Spiel ist jetzt aufgeräumt — Änderungen an der Kampflogik betreffen nur noch `kampfrunde()`, nicht mehr den ganzen Block. **Das Problem mit JSON:** Wir überschreiben immer nur einen einzigen Charakter-Eintrag, es gibt keine Historie mehrerer Kämpfe oder Spieler. **Ausblick:** Morgen ersetzen wir die kleine JSON-Datei durch eine echte SQLite-Datenbank, um eine echte Bestenliste zu erschaffen!