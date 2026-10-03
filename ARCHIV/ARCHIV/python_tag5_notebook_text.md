# Tag 5 – Notebook: Die grafische Oberfläche (GUI) mit tkinter

**Tagesziel:** Dungeon Duel bekommt ein Fenster mit HP-Anzeigen, Aktions-Buttons und Bestenliste — unter Wiederverwendung von `db.py` und `game.py` aus Tag 4. Abschluss mit Präsentationen.

**Zugehörige Code-Dateien:** `tag5_code.py` (Beispiele & Übungs-Starter) und `gui.py` (fertige Praxis-Anwendung, nutzt `db.py`/`game.py` aus Tag 4 unverändert).

**Einstieg:** Bisher tippt man Befehle blind in eine schwarze Konsole. Eine GUI (Graphical User Interface) zeigt Buttons, HP-Balken und Beschriftungen — für Endnutzer deutlich zugänglicher, gerade bei einem Kampfspiel, wo man die eigenen und gegnerischen HP auf einen Blick sehen möchte. `tkinter` ist in Python fest eingebaut und eignet sich gut für kleine bis mittlere Desktop-Anwendungen wie unser Spiel.

---

## 5.1 tkinter Grundlagen

**Definition:** `tkinter` ist Pythons eingebaute GUI-Bibliothek. Ein Hauptfenster (`Tk()`) enthält Widgets (`Label`, `Button`, …), `mainloop()` hält das Fenster offen und wartet auf Ereignisse.

**Warum wichtig:** Eine grafische Oberfläche zeigt HP, Buttons und Status auf einen Blick — deutlich zugänglicher als reine Konsolentexte.

**Syntax:**
```
fenster = tk.Tk()
widget = tk.Label(fenster, text="...")
widget.pack()
fenster.mainloop()
```

**Merksatz:** *"`command=funktion` ohne Klammern — wir übergeben die Funktion selbst, nicht ihr sofortiges Ergebnis."*

**Beispiel:** siehe `tag5_code.py`, Abschnitt "5.1 Beispiel"

### Übung 1: Der digitale Klickzähler (35 Min)
*Lernziel: Fenster, Label und Button verknüpfen.*

1. Baue ein Fenster mit einem `Label`, das "Klicks: 0" anzeigt, und einem `Button` "Klick mich"
2. Schreibe eine Funktion `erhoehe_klicks()`, die bei jedem Klick den Text des Labels aktualisiert (`label.config(text=f"Klicks: {zahl}")`)
3. Nutze dafür eine Variable, die außerhalb der Funktion existiert und mit `global` innerhalb verändert wird — diskutiert kurz, warum das hier pragmatisch nötig ist (GUI-Callbacks erhalten keine Parameter automatisch)

→ Starter-Code: `tag5_code.py`, Abschnitt "Übung 1"

---

## 5.2 Entry & Event-Handling

**Definition:** `Entry` ist ein Eingabefeld, dessen Wert mit `.get()` als String abgerufen wird. Statt einer `while`-Schleife reagiert das Programm event-gesteuert: `mainloop()` ruft bei jedem Klick die hinterlegte `command`-Funktion auf.

**Warum wichtig:** In der Konsole wartete `while True:` aktiv auf die nächste Eingabe. In der GUI übernimmt das die Ereignisschleife — die komplette Ablauflogik verteilt sich auf mehrere kleine Callback-Funktionen.

**Syntax:**
```
eingabefeld = tk.Entry(fenster)
wert = eingabefeld.get()
```

**Merksatz:** *"Keine while-Schleife mehr nötig — jeder Klick löst genau eine Callback-Funktion aus."*

**Beispiel:** siehe `tag5_code.py`, Abschnitt "5.2 Beispiel"

### Übung 2: Der GUI-Taschenrechner (40 Min)
*Lernziel: Eingabefelder auslesen und mit Fehlerbehandlung verarbeiten.*

1. Baue zwei `Entry`-Felder und einen Button "Addieren"
2. Beim Klick: beide Werte mit `int()` umwandeln (mit `try/except`!), Summe berechnen, in einem Label anzeigen
3. Bonus: Ein zweiter Button "Zurücksetzen", der beide Eingabefelder leert (`entry.delete(0, tk.END)`) und das Ergebnis-Label zurücksetzt

→ Starter-Code: `tag5_code.py`, Abschnitt "Übung 2"

---

## 5.3 Zustand in der GUI

**Definition:** Werte, die über mehrere Klicks hinweg erhalten bleiben müssen (z.B. HP), werden in Variablen außerhalb der Callback-Funktionen gehalten und dort mit `global` verändert. `Toplevel` öffnet ein zusätzliches Fenster.

**Warum wichtig:** Callback-Funktionen erhalten keine Parameter von `mainloop()` — Zustand muss deshalb "von außen" zugänglich sein, solange wir bei der funktionalen, klassenlosen Herangehensweise bleiben.

**Syntax:**
```
zustand = startwert

def callback():
    global zustand
    zustand = neuer_wert
    label.config(text=str(zustand))
```

**Merksatz:** *"enumerate(liste, start=1) zählt beim Durchlaufen automatisch mit — praktisch für Platzierungsnummern ohne eigenen Zähler."*

**Beispiel:** siehe `tag5_code.py`, Abschnitt "5.3 Beispiel" (`zeige_bestenliste`)

### Übung 3: Die Ampel-Simulation (30 Min)
*Lernziel: Globalen Zustand über mehrere Klicks hinweg verwalten.*

1. Fenster mit einem Label (großer Text, z.B. `font=("Arial", 40)`) und einem Button "Weiter"
2. Bei jedem Klick wechselt die Anzeige reihum: "🔴 Rot" → "🟡 Gelb" → "🟢 Grün" → wieder "🔴 Rot" …
3. Nutzt eine globale Zustandsvariable (z.B. eine Liste mit den drei Zuständen + einen Index), um zu wissen, welche Farbe als Nächstes dran ist

→ Starter-Code: `tag5_code.py`, Abschnitt "Übung 3"

---

## Praxis: Dungeon Duel als GUI (Gruppenarbeit, 2h)

Das fertige GUI-Grundgerüst steht in `gui.py` — es importiert `db.py` und `game.py` aus Tag 4 **unverändert**.

**Gemeinsam durchgehen (10 Min):** Warum `lambda: runde_ausfuehren(1)` statt `runde_ausfuehren(1)` in `command=`? (`command=` erwartet eine parameterlose Funktion — `lambda` verpackt den Aufruf mit festem Parameter.)

**Eure Aufgaben:**
1. GUI selbst nachbauen (Kopie von `gui.py`), mehrere Runden kämpfen, Bestenliste prüfen
2. **Kritische Treffer** aus Tag 1 wieder einbauen, im `status_label` anzeigen
3. **"Neuer Kampf"-Button** nach Sieg/Niederlage, der HP zurücksetzt und einen neuen Kampf startet
4. Bonus: Rundenzahl live als eigenes Label anzeigen
5. Bonus: HP-Label des Helden rot färben, sobald die HP unter 30 fallen (`held_hp_label.config(fg="red")`)

**Ziel:** Ein komplett grafisches Kampfspiel, das exakt dieselbe Kampf- und Datenbanklogik wie gestern nutzt — nur die Konsole wurde durch Fenster, HP-Anzeigen und Buttons ersetzt.

---

## Abschluss (17:00-17:30)

**Kurze Präsentationen (20 Min):** Wer möchte, zeigt kurz seine/ihre GUI-Erweiterung.

**Rückblick auf die Woche:**
- Tag 1: Ein Skript, alles in einem Block
- Tag 2: Aufgeräumt mit Funktionen, Charakter in JSON
- Tag 3: Persistente Datenbank statt Datei, Heldenbestenliste
- Tag 4: Saubere Trennung in Module
- Tag 5: Grafische Oberfläche auf derselben Basis

**Zentrale Erkenntnis für die Gruppe:** Weil `db.py` und `game.py` von Anfang an unabhängig von der Konsolen-Ein-/Ausgabe geschrieben wurden, ließ sich die komplette Oberfläche austauschen, ohne eine einzige Zeile Kampflogik oder Datenbankcode anzufassen — das ist der praktische Nutzen sauberer Architektur.

**Feedback-Runde & Ausblick:** Mögliche nächste Schritte für Interessierte: OOP (Klassen für Held/Monster statt globaler Variablen), weitere tkinter-Widgets (Canvas für Grafiken, Progressbar für HP-Balken statt Text), mehrere Monster-Typen, Inventar-System, Packaging als ausführbare Datei.