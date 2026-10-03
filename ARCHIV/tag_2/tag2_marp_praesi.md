---
marp: true
theme: default
paginate: true
size: 16:9
---

# ⚔️ Dungeon Duel
## Tag 2: Refactoring & Speicherung (JSON)

Python Fortgeschrittene – D&D-Edition

---

## Tagesziel

- Kampf-Skript von Tag 1 mit **Funktionen** aufraeumen
- Charakter (Name, HP, Level) dauerhaft als **JSON** speichern
- Erstes echtes "Spielgedaechtnis"

---

## Tagesablauf

| Zeit | Block |
|---|---|
| 09:15–10:30 | Funktionen & Parameter |
| 10:45–12:30 | Rueckgabewerte (return) |
| 13:30–15:00 | Dateien, Dictionaries & JSON |
| 15:15–17:30 | Praxis: Kampf refactoren & Charakter speichern |

---

## 2.1 Funktionen & Parameter

- Benannter, wiederverwendbarer Codeblock
- Parameter = Platzhalter fuer Werte beim Aufruf

```python
def begruesse(name, klasse):
    print(f"Willkommen, {name} der/die {klasse}!")
```

> Jede Funktion beantwortet: **Was? Womit? Was zurueck?**

---

## 2.2 Rueckgabewerte (return)

- `print()` zeigt – `return` liefert
- Nur mit `return` bleibt ein Ergebnis **weiterverwendbar**

```python
def wuerfle_schaden(minimum, maximum):
    return random.randint(minimum, maximum)

schaden = wuerfle_schaden(5, 20)
```

---

## 2.3 Dateien & with

```python
with open("pfad", "w", encoding="utf-8") as datei:
    datei.write(text)
```

- `with` schliesst die Datei **automatisch**
- Modi: `"r"` lesen · `"w"` schreiben (ueberschreibt!) · `"a"` anhaengen

---

## 2.4 JSON

```python
json.dump(daten, datei)      # Dictionary -> Datei
geladen = json.load(datei)   # Datei -> Dictionary
```

- Speichert **zusammengehoerige Datenpakete** (Name + HP + Level)
- `FileNotFoundError` beim ersten Start abfangen!

---

## Praxis: Kampf refactoren

```python
def kampfrunde(monster_hp, aktion):
    if aktion == 1:
        schaden = random.randint(5, 20)
        return monster_hp - schaden, schaden
    return monster_hp, 0
```

Kampflogik raus aus dem grossen Block, rein in eine Funktion.

---

## Praxis: Charakter speichern

```python
def lade_charakter(pfad="charakter.json"):
    try:
        with open(pfad, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except FileNotFoundError:
        return {"level": 1, "besiegte_monster": 0}
```

---

## Gruppenarbeit (60 Min)

1. `lade_charakter()` / `speichere_charakter_state()` einbauen
2. Begruessung zeigt Level & besiegte Monster
3. Bei Sieg: `besiegte_monster` erhoehen & speichern
4. **Profi-Challenge:** alle 3 Siege → Level-Up, HP +10

---

## Tagesabschluss

- Kampflogik ist jetzt in Funktionen gekapselt ✅
- Charakter uebersteht einen Neustart ✅
- **Problem:** JSON kennt nur *einen* Charakter, keine Historie

**Morgen:** Umzug auf SQLite → echte Bestenliste 🏆
