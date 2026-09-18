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

# ⚔️ Python Fortgeschrittene
## Dungeon Duel — D&D-Edition

Ein 5-Tage-Kurs: vom monolithischen Skript zum fertigen Spiel mit GUI & Datenbank

---

## 🎯 Gesamtziel der Woche

Aus einem einzigen Konsolen-Skript entsteht Tag für Tag ein sauber strukturiertes **Kampfspiel im D&D-Stil** mit grafischer Oberfläche und Datenbank-Anbindung — **Dungeon Duel**.

---

## 🗺️ Die Woche im Überblick

| Tag | Ausbaustufe | Kernthema |
|---|---|---|
| **1** | Monolithischer Konsolen-Kampf | Variablen, if/elif/else, while, try/except |
| **2** | Funktionen, Charakter in JSON | Funktionen, return, Dateien, JSON |
| **3** | Charaktere & Kämpfe in SQLite | SQLite, Security, Context Manager |
| **4** | Aufgeteilt in Module | Software-Architektur, Imports |
| **5** | Grafische Oberfläche | tkinter, Event-Handling, Abschluss |

---

## 📈 Der rote Faden

**Tag 1** → **Tag 2** → **Tag 3** → **Tag 4** → **Tag 5**

Ein Block Code → aufgeräumt mit Funktionen + JSON → Datenbank statt Datei → in Module aufgeteilt → Konsole durch GUI ersetzt

> Weil Datenbank- und Kampflogik von Anfang an unabhängig von Konsolen-I/O geschrieben werden, lässt sich am Ende die komplette Oberfläche austauschen — **ohne** eine Zeile Kampf- oder Datenbankcode anzufassen.

---

<!-- _class: lead -->

# 📅 Heute: Tag 1
## Der monolithische Kampf

---

## 🎯 Tagesziel

Am Ende des Tages steht ein lauffähiger **Konsolen-Kampf**:

- Ein Held mit Lebenspunkten (HP) tritt gegen ein Monster an
- Bei jeder Runde wird gewürfelt, ob der Angriff trifft
- Schaden wird abgezogen
- Der Kampf endet, sobald eine Seite 0 HP erreicht

---

## ⚠️ Wichtige Regel für heute

Wir verzichten heute **bewusst komplett** auf eigene Funktionen (`def`).

Wir schreiben alles als **ein langes Skript** von oben nach unten (monolithisch)

**Warum?**
- Kontrollstrukturen isoliert verstehen
- Morgen den „Schmerz" spüren, der zum Aufräumen mit Funktionen motiviert

---

## 🕐 Tagesablauf

| Zeit | Block | Thema |
|---|---|---|
| 09:00–09:15 | Einstieg | Begrüßung, Setup & Tagesüberblick |
| 09:15–10:30 | Block 1 | Variablen, Datentypen, Typumwandlung |
| 10:45–12:30 | Block 2 | Kontrollstrukturen (if/elif/else) |
| 13:30–14:30 | Block 3 | Die while-Schleife |
| 14:45–15:45 | Block 4 | Fehlerbehandlung (try/except) |
| 16:00–17:30 | Block 5 | Praxis: Den Kampf zusammenbauen |

---

## 📘 Block 1 — Variablen & Datentypen

**Definition:** Eine Variable ist ein benannter Speicherplatz für einen Wert. Python erkennt den Datentyp automatisch (dynamische Typisierung).

**Warum wichtig:** `input()` liefert **immer** einen String — jede Berechnung im Spiel braucht die richtige Umwandlung.

```python
held_hp = 100                 # int
kritische_chance = 0.15       # float
eingabe = input("...")        # IMMER str
aktion = int(eingabe)         # jetzt eine echte Zahl
```

> 💡 *input() lügt nie über den Typ — es ist immer str.*

---

## ✏️ Übung: Der fehlerhafte Warenkorb (30 Min)

1. `input()` nach Produktname, Preis pro Stück, Anzahl
2. Gesamtsumme berechnen (`preis * anzahl`) und ausgeben
3. Wo braucht ihr `float()` und `int()`, damit korrekt gerechnet wird?

---

## 📘 Block 2 — if/elif/else

**Definition:** Vergleichsoperatoren liefern `True`/`False`. `if`/`elif`/`else` steuert die Ausführung.

```python
if wurf == 1:
    return "patzer"
elif wurf >= ruestung:
    return "treffer"
else:
    return "verfehlt"
```

> 💡 *Ein `=` speichert, zwei `==` vergleichen.*

---

## ✏️ Übung: Der strenge Türsteher (40 Min)

1. Alter abfragen
2. Unter 18 → „Du kommst hier nicht rein!"
3. 18–20 → Frage nach „Muttizettel"
4. Ab 21 → „Willkommen im Club, VIP!"

---

## 📘 Block 3 — Die while-Schleife

**Definition:** Wiederholt einen Codeblock, solange eine Bedingung `True` ist.

```python
while monster_hp > 0:
    runde += 1
    monster_hp -= 10
```

**Warum wichtig:** Ein Kampf dauert eine unbekannte Anzahl Runden.

> 💡 *Vergisst man die Bedingung zu verändern → Endlosschleife.*

---

## ✏️ Übung: Der nervige Papagei (30 Min)

1. `while True:`-Schleife fordert bei jedem Durchlauf zur Eingabe auf
2. Antwortet immer mit demselben Text
3. Beendet sich nur bei `"Halt die Klappe"` (mit `break`)

---

## 📘 Block 4 — try/except

**Definition:** Fängt einen definierten Fehlertyp ab, statt das Programm abstürzen zu lassen.

```python
try:
    aktion = int(eingabe)
except ValueError:
    print("Bitte nur 1 oder 2 eingeben!")
    continue
```

> 💡 *Gezielt `except ValueError` statt pauschal `except Exception`.*

---

## ✏️ Übung: Der unzerstörbare Taschenrechner (40 Min)

1. Zwei Zahlen abfragen, teilen
2. `ValueError` bei Buchstaben abfangen, `continue`
3. **Zusatz:** Division durch 0 gezielt abfangen

---

## 🛠️ Block 5 — Praxis: Den Kampf zusammenbauen

**Live-Coding (30 Min):** Held vs. Monster, HP, Runden, Angriff/Verteidigen — Startpunkt für Dungeon Duel

**Gruppenarbeit (45 Min):**
- Absturzsicherheit prüfen
- Kritischer Treffer bei Wurf 20 → doppelter Schaden
- Wo muss `runde += 1` stehen?

---

<!-- _class: lead -->

## ✅ Tagesabschluss

Fehlerprüfung, Kampflogik und Rundenzähler kleben in **einem Block**.

### 🔮 Ausblick: Morgen räumen wir mit Funktionen auf
und geben dem Spiel ein Gedächtnis (JSON) — **Tag 2**
