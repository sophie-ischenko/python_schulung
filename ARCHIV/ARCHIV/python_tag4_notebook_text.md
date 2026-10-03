# Tag 4 – Notebook: Software-Architektur — Module aufteilen

**Tagesziel:** Das Skript wird in `db.py`, `game.py`, `main.py` zerlegt — Voraussetzung dafür, dass morgen die Konsole durch eine GUI ersetzt werden kann, ohne Datenbank- oder Kampflogik anzufassen.

**Zugehörige Code-Datei:** `tag4_code.py` — enthält alle Beispiele und Übungs-Starter. Die **Praxis am Ende** besteht heute ausnahmsweise aus **drei separaten Dateien** (`db.py`, `game.py`, `main.py`), die ebenfalls im Anschluss bereitgestellt werden.

**Einstieg (im Plenum):** *"Was passiert, wenn ihr in eurem aktuellen Skript nach der Kampflogik sucht — wie lange dauert die Suche?"* Trennung nach Verantwortlichkeit macht große Projekte handhabbar und ist Voraussetzung für die GUI morgen.

---

## 4.1 Module & Imports

**Definition:** Jede `.py`-Datei ist automatisch ein Modul. Mit `import modulname` oder `from modulname import funktion` werden Funktionen aus einer anderen Datei nutzbar.

**Warum wichtig:** Ein wachsendes Programm in einer einzigen Datei wird schnell unübersichtlich. Aufteilung nach Verantwortlichkeit (Datenbank, Spiellogik, Ablauf) macht Code wartbar.

**Syntax:**
```
import modulname
from modulname import funktion1, funktion2
```

**Merksatz:** *"Beim Import wird die gesamte Moduldatei einmal ausgeführt — Code außerhalb von Funktionen läuft dabei sofort mit."*

**Beispiel:** siehe `tag4_code.py`, Abschnitt "4.1 Beispiel"

### Übung 1: Die Werkzeugkiste (30 Min)
*Lernziel: Module anlegen, importieren und beim Laden beobachten.*

1. Legt eine Datei `mathe_helfer.py` an mit drei Funktionen: `ist_primzahl(zahl)`, `fakultaet(zahl)`, `ggt(a, b)` — jede mit Docstring (Was/Parameter/Rückgabewert)
2. Legt eine zweite Datei `main.py` an, importiert die Funktionen und ruft alle drei mit Testwerten auf
3. Baut testweise `print("Datei wurde geladen")` ganz oben in `mathe_helfer.py` ein (außerhalb jeder Funktion) — wann genau läuft diese Zeile?

→ Starter-Code: `tag4_code.py`, Abschnitt "Übung 1"

---

## 4.2 `__name__ == "__main__"`

**Definition:** `__name__` ist `"__main__"`, wenn eine Datei direkt gestartet wird, sonst trägt sie den Modulnamen. Der Schutzblock verhindert, dass Testcode beim bloßen Importieren mitläuft.

**Warum wichtig:** Ein Datenbank- oder Spiellogik-Modul soll beim Import keine Konsolen-Interaktion auslösen — nur die Datei, die tatsächlich gestartet wird, soll das Programm ausführen.

**Syntax:**
```
if __name__ == "__main__":
    ...
```

**Merksatz:** *"Module liefern (return), das Hauptprogramm zeigt (print/input) — die Trennung macht jede Datei einzeln testbar."*

**Beispiel:** siehe `tag4_code.py`, Abschnitt "4.2 Beispiel"

### Übung 2: Testbare Module (30 Min)
*Lernziel: Module unabhängig testbar machen.*

1. Ergänzt `mathe_helfer.py` um einen `if __name__ == "__main__":`-Block mit Testaufrufen aller drei Funktionen
2. Prüft: Beim Start von `main.py` erscheinen die Testausgaben aus `mathe_helfer.py` NICHT
3. Diskutiert: Warum ist das nützlich, wenn mehrere Leute im Team an unterschiedlichen Dateien arbeiten?

→ Starter-Code: `tag4_code.py`, Abschnitt "Übung 2"

---

## 4.3 Eigene Exceptions

**Definition:** Ein eigener Fehlertyp wird durch eine minimale Klasse erstellt, die von `Exception` erbt, und mit `raise` ausgelöst.

**Warum wichtig:** Für spielspezifische Regelverstöße (z.B. eine ungültige Aktionswahl) liefert ein eigener, sprechender Fehlertyp klarere Fehlermeldungen als ein generischer `ValueError` — das zahlt sich besonders in der GUI morgen aus.

**Syntax:**
```
class EigenerFehler(Exception):
    pass

raise EigenerFehler("Nachricht")
```

**Merksatz:** *"`class X(Exception)` ist reine Werkzeug-Syntax für Fehlertypen — kein OOP-Design im eigentlichen Sinn."*

**Beispiel:** siehe `tag4_code.py`, Abschnitt "4.3 Beispiel" (`UngueltigeAktionError`, `pruefe_aktion`)

### Übung 3: Der Ticket-Validator (30 Min)
*Lernziel: Eigene Exceptions definieren und gezielt abfangen.*

1. Eigene Exception `UngueltigesTicketError`
2. Funktion `pruefe_ticket(preis)`, die die Exception wirft, wenn `preis <= 0` oder `preis > 500`
3. Fangt den Fehler im Hauptprogramm ab und gebt eine passende Meldung aus

→ Starter-Code: `tag4_code.py`, Abschnitt "Übung 3"

---

## Praxis: Das Spiel in drei Dateien aufteilen (Gruppenarbeit, 2h)

**Gemeinsame Planung (im Plenum, 30 Min):**

```
db.py     → setup_db(), speichere_held_db(), get_top_5_helden()
game.py   → kampfrunde(), monster_greift_an(), pruefe_aktion(), UngueltigeAktionError
main.py   → Begrüßung, while-Schleife, input()/print(), ruft db.py und game.py auf
```

Die drei fertigen Dateien `db.py`, `game.py` und `main.py` werden separat bereitgestellt — sie zeigen die Ziel-Struktur.

**Eure Aufgabe:**
1. Legt drei Dateien `db.py`, `game.py`, `main.py` im selben Ordner an
2. Verschiebt euren bisherigen Code (aus Tag 1-3) entsprechend der Tabelle oben, korrigiert die Imports, testet nach jedem Verschiebungsschritt
3. Baut den `if __name__ == "__main__":`-Schutz in `main.py` ein
4. Baut `pruefe_aktion()` und `UngueltigeAktionError` aus Übung 3 in `game.py` ein und nutzt sie in der Aktions-Prüfung

**Zwischen-Check (15 Min):** Läuft das Spiel identisch wie vorher? Welche Import-Fehler traten auf und wie wurden sie gelöst?

---

**Tagesabschluss:** `main.py` enthält jetzt ausschließlich Ablauf und Konsolen-I/O — genau das wird morgen durch eine grafische Oberfläche ersetzt, ohne `db.py`/`game.py` anzufassen. **Ausblick:** Morgen tkinter-GUI.