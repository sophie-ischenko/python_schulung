---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-size: 26px;
  }
  h1 {
    color: #4a2f6b;
  }
  h2 {
    color: #7a4fb5;
  }
  table {
    font-size: 22px;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# 🧹 Dungeon Duel
## Tag 2 — Refactoring & Speicherung (JSON)

---

## 🔁 Recap Tag 1

- Ein monolithischer Konsolen-Kampf in **einem** Skript
- Variablen, if/elif/else, while, try/except
- Held vs. Monster, Runden, Angriff/Verteidigen

**Problem:** Alles steht in einem langen Block — jede Änderung ist mühsam, nichts wird gespeichert.

---

## 🎯 Warum wir heute aufräumen müssen

- Logik wiederholt sich (z.B. Schadensberechnung)
- Kein Gedächtnis: Nach jedem Programmende ist der Charakter weg
- **Heute:** Funktionen zum Aufräumen + JSON zum Speichern

## 🎯 Tagesziel

Wir räumen das Skript von gestern mit **Funktionen** auf und geben dem Spiel ein Gedächtnis: Der Charakter wird dauerhaft in einer **JSON-Datei** gespeichert.

---

## 🕐 Tagesablauf

| Zeit | Block | Thema |
|---|---|---|
| 09:00–09:15 | Einstieg | Recap Tag 1 & Warum wir aufräumen müssen |
| 09:15–10:30 | Block 1 | Funktionen & Parameter |
| 10:45–12:30 | Block 2 | Rückgabewerte (return) |
| 13:30–15:00 | Block 3 | Dateien, Dictionaries & JSON |
| 15:15–17:30 | Block 4 | Praxis: Kampf refactoren & Charakter speichern |

---

## 📘 Block 1 — Funktionen & Parameter

**Definition:** Ein benannter, wiederverwendbarer Codeblock mit Parametern als Platzhalter für übergebene Werte.

```python
def begruesse(name, klasse):
    """Gibt eine Begrüßung für einen neuen Helden aus."""
    print(f"Willkommen, {name} der/die {klasse}!")

begruesse("Aria", "Kriegerin")
```

> 💡 *Jede Funktion beantwortet drei Fragen: Was macht sie? Was nimmt sie entgegen? Was gibt sie zurück?*

---

## ✏️ Übung: Der smarte Kaffeevollautomat (40 Min)

1. Funktion `braue_kaffee(kaffee_art, zucker_wuerfel)` mit Docstring
2. Zwei `print()`-Ausgaben simulieren den Brühvorgang
3. Bei `zucker_wuerfel > 3`: „Achtung: Sehr süß!"
4. Dreimal mit unterschiedlichen Werten aufrufen

---

## 📘 Block 2 — Rückgabewerte (return)

**Definition:** `return` beendet eine Funktion sofort und übergibt einen Wert an die aufrufende Stelle.

```python
def wuerfle_schaden(minimum, maximum):
    """Simuliert einen Schadenswurf in einem Bereich."""
    return random.randint(minimum, maximum)

schaden = wuerfle_schaden(5, 20)
```

> 💡 *print() zeigt, return liefert. Logik-Funktionen nutzen return, Anzeige-Funktionen print.*

---

## ✏️ Übung: Der Passwort-Prüfer (45 Min)

1. `check_password(password)` — **kein print() in der Funktion!**
2. Kürzer als 8 Zeichen → „schwach", enthält „123" → „sehr schwach", sonst → „stark"
3. Schleife fragt, gibt Ergebnis aus, bei „stark" `break`

---

## 📘 Block 3 — Dateien, Dictionaries & JSON

**Dateien:** `open()` + `with` schließt automatisch, auch bei Fehlern.

**JSON:** wandelt ein Dictionary in speicherbaren Text um und zurück.

```python
with open(pfad, "w", encoding="utf-8") as datei:
    json.dump(held, datei)      # Dictionary -> Datei
geladen = json.load(datei)      # Datei -> Dictionary
```

> 💡 *CSV/Text für einzelne Werte, JSON für zusammengehörige Datenpakete.*

---

## ✏️ Übung: Das Rollenspiel-Inventar (45 Min)

1. `{"gold": 100, "tränke": 3}` als `savegame.json` speichern
2. Speicher-Code auskommentieren, Datei bleibt bestehen
3. Inventar laden, Schwert (50 Gold) kaufen, aktualisieren, wieder speichern
4. Zweimal ausführen, Gold-Stand prüfen

---

## 🛠️ Block 4 — Praxis: Kampf refactoren & Charakter speichern

**Live-Coding (30 Min):** `kampfrunde()` als Funktion — der erste Schritt weg vom monolithischen Skript

**Gruppenarbeit (60 Min):**
- `lade_charakter()` mit `FileNotFoundError`-Abfangen
- `speichere_charakter(held)`
- Level/besiegte Monster in Begrüßung anzeigen, bei Sieg speichern

**Profi-Challenge:** Level-System — alle 3 Siege ein Levelaufstieg, max. HP +10

---

<!-- _class: lead -->

## ✅ Tagesabschluss

JSON überschreibt immer nur **einen** Charakter — keine Historie.

### 🔮 Ausblick: Morgen ersetzen wir JSON durch SQLite
mit einer **Heldenbestenliste** — **Tag 3**
