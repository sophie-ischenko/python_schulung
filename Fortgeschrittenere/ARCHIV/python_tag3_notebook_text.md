# Tag 3 – Notebook: Umzug auf eine SQLite-Datenbank

**Tagesziel:** Wir ersetzen JSON durch eine echte relationale Datenbank und bauen eine **Bestenliste der stärksten Helden**. Zusätzlich: professionelles Tooling (DB Browser), Security (SQL-Injection), Context Manager.

**Zugehörige Code-Datei:** `tag3_code.py` — enthält alle Beispiele, Übungs-Starter und die SQLite-Anbindung von Dungeon Duel als kommentierte, lauffähige Datei.

---

## 3.1 SQLite Grundlagen

**Definition:** SQLite ist eine dateibasierte, in Python fest eingebaute Datenbank. `connect()` öffnet die Datenbankdatei, ein `cursor` führt SQL-Befehle aus.

**Warum wichtig:** Eine JSON-Datei speichert immer nur einen Zustand auf einmal. Eine Datenbank kann beliebig viele Zeilen (z.B. jeden einzelnen Kampf) dauerhaft und durchsuchbar speichern.

**Syntax:**
```
conn = sqlite3.connect("datei.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ... (...)")
conn.commit()
conn.close()
```

**Merksatz:** *"IF NOT EXISTS macht CREATE TABLE gefahrlos wiederholbar — die Funktion kann bei jedem Programmstart erneut aufgerufen werden."*

**Tooling:** "DB Browser for SQLite" zum Öffnen und Inspizieren der `.db`-Datei — installiert es vor dem Kurstag, falls noch nicht vorhanden.

**Beispiel:** siehe `tag3_code.py`, Abschnitt "3.1 Beispiel" (Funktion `setup_db`)

### Übung 1: Kunden-Register Teil 1 (45 Min)
*Lernziel: Datenbankdateien per Skript anlegen und mit externen Tools prüfen.*

1. Schreibe eine Funktion `setup_db()` in einer neuen Datei `kunden_app.py`
2. Sie soll eine Verbindung zu `kunden.db` herstellen und eine Tabelle `users` anlegen: Spalten `name` (TEXT), `alter_jahre` (INTEGER), `guthaben` (REAL)
3. Führe das Skript aus, dann öffne `kunden.db` im DB Browser und lege manuell 2 Testzeilen an ("Write Changes" nicht vergessen)

→ Starter-Code: `tag3_code.py`, Abschnitt "Übung 1"

---

## 3.2 INSERT, Security & Context Manager

**Definition:** `INSERT` fügt eine neue Zeile ein. `?`-Platzhalter übergeben Werte sicher getrennt vom SQL-Befehl. Der Context Manager (`with sqlite3.connect(...)`) übernimmt `commit()` automatisch.

**Warum wichtig — Sicherheit:** Werden Eingaben direkt per f-String in den SQL-Befehl eingesetzt, kann eine bösartige Eingabe wie `Aria' OR '1'='1` den Befehl umschreiben und z.B. alle Zeilen löschen (**SQL-Injection**). `?`-Platzhalter verhindern das zuverlässig.

**Syntax:**
```
with sqlite3.connect("datei.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tabelle (spalte1, spalte2) VALUES (?, ?)", (wert1, wert2))
```

**Merksatz:** *"Werte gehören immer als Tupel hinter das SQL-Statement, nie direkt hineingeschrieben — `?` ist Pflicht, kein Stil."*

**Live-Demo im Plenum (nicht selbst nachbauen, nur anschauen):**
```
eingabe = input("Heldenname zum Loeschen: ")
cursor.execute(f"DELETE FROM helden WHERE name = '{eingabe}'")   # GEFAEHRLICH
```
Eingabe `Aria' OR '1'='1` löscht alle Zeilen — Anlass für die `?`-Platzhalter-Regel.

**Beispiel:** siehe `tag3_code.py`, Abschnitt "3.2 Beispiel" (Funktion `speichere_held_db`)

### Übung 2: Kunden-Register Teil 2 (50 Min)
*Lernziel: Sicheres Einfügen mit Context Manager und Fehlerbehandlung.*

1. Schreibe `add_user(name, alter_jahre, guthaben)` in `kunden_app.py`
2. Nutze zwingend den `with sqlite3.connect(...)`-Context-Manager und `?`-Platzhalter
3. Umhülle die Ausführung mit `try/except sqlite3.Error`
4. Baue eine `while`-Schleife, die Nutzer befragt und `add_user()` aufruft
5. Trage 3 Nutzer ein, prüfe im DB Browser (F5 zum Aktualisieren)

→ Starter-Code: `tag3_code.py`, Abschnitt "Übung 2"

---

## 3.3 SELECT, ORDER BY, LIMIT

**Definition:** `SELECT` liest Zeilen aus. `ORDER BY spalte ASC/DESC` sortiert, `LIMIT n` begrenzt die Anzahl. `fetchone()` liefert eine Zeile, `fetchall()` alle.

**Warum wichtig:** Für eine Bestenliste soll die Datenbank selbst sortieren und begrenzen, statt dass wir alle Daten laden und in Python nachbauen, was SQL bereits kann.

**Syntax:**
```
cursor.execute("SELECT spalte FROM tabelle ORDER BY spalte DESC LIMIT n")
ergebnisse = cursor.fetchall()
```

**Merksatz:** *"fetchone() kann None liefern (Tabelle leer) — immer prüfen, bevor man das Ergebnis entpackt."*

**Beispiel:** siehe `tag3_code.py`, Abschnitt "3.3 Beispiel" (Funktion `get_top_kunden`)

### Übung 3: Kunden-Register Teil 3 (45 Min)
*Lernziel: Gefilterte Daten abfragen und formatiert aufbereiten.*

1. Schreibe `get_richest_user()` mit `fetchone()` + `ORDER BY guthaben DESC LIMIT 1`
2. Schreibe `get_users_sorted_by_age()` mit `fetchall()` + `ORDER BY alter_jahre ASC`
3. Rufe beide auf und gib die Ergebnisse formatiert aus

→ Starter-Code: `tag3_code.py`, Abschnitt "Übung 3"

---

## Praxis: Das Spiel auf SQLite umbauen (Gruppenarbeit, 60 Min)

Die fertige SQLite-Anbindung für **Dungeon Duel** steht in `tag3_code.py`, Abschnitt "Praxis: Dungeon Duel mit SQLite" — lauffähig und kommentiert.

**Aufgaben:**
1. Baut Verbindung, Tabellenerstellung und `speichere_held_db()` in euer Spiel ein
2. `get_top_5_helden()`: sortiert nach `level DESC`, `LIMIT 5`
3. Ruft die Bestenliste nach jedem Sieg auf und gebt sie formatiert aus
4. Mehrere Testrunden spielen, Datenbank-Inhalt im DB Browser kontrollieren
5. Diskutiert: Was ist gegenüber JSON (Tag 2) umständlicher, was einfacher?
6. Bonus: Schreibt eine einmalige Migrations-Funktion, die eine alte `charakter.json` einliest und in die DB überträgt

---

**Tagesabschluss:** Jeder abgeschlossene Kampf landet jetzt als neue Zeile in der Datenbank — die Historie bleibt erhalten, nicht nur der letzte Wert. Datenbank-Code, Kampflogik und Konsolen-I/O liegen aber noch ungeordnet in einer Datei. **Ausblick:** Morgen Software-Architektur — Aufteilung in Module.