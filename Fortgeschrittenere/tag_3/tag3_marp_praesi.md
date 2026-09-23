---
marp: true
theme: default
paginate: true
size: 16:9
---

# ⚔️ Dungeon Duel
## Tag 3: Umzug auf eine SQLite-Datenbank

Python Fortgeschrittene – D&D-Edition

---

## Tagesziel

- JSON ersetzen durch eine **echte Datenbank**
- **Bestenliste der staerksten Helden** bauen
- Professionelles Tooling, Security, Context Manager

---

## Tagesablauf

| Zeit | Block |
|---|---|
| 09:15–10:30 | SQLite Basics, DB-Tooling & Tabellen |
| 10:45–12:30 | INSERT, Security & Context Manager |
| 13:30–15:00 | SELECT, ORDER BY, LIMIT |
| 15:15–17:30 | Praxis: SQLite & Heldenbestenliste |

---

## Warum eine Datenbank statt JSON?

- JSON speichert **immer nur einen** Zustand
- Datenbank: beliebig viele Zeilen, dauerhaft & durchsuchbar
- Jeder Kampf wird zu **einer Zeile** – Historie bleibt erhalten

---

## 3.1 SQLite Grundlagen

```python
conn = sqlite3.connect("dungeon.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS helden (
        name TEXT, level INTEGER, besiegte_monster INTEGER
    )
""")
conn.commit()
conn.close()
```

🛠️ Tooling: **DB Browser for SQLite** zum Reinschauen

---

## ⚠️ SQL-Injection – Live-Demo

```python
eingabe = input("Heldenname zum Loeschen: ")
cursor.execute(f"DELETE FROM helden WHERE name = '{eingabe}'")
```

Eingabe `Aria' OR '1'='1` → **loescht ALLE Zeilen!**

---

## 3.2 Die sichere Loesung: `?`-Platzhalter

```python
with sqlite3.connect("dungeon.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO helden (name, level, besiegte_monster) VALUES (?, ?, ?)",
        (name, level, besiegte_monster)
    )
```

- `with` = Context Manager → `commit()` automatisch
- `?` = Werte werden sicher getrennt uebergeben

---

## 3.3 SELECT, ORDER BY, LIMIT

```python
cursor.execute(
    "SELECT name, level FROM helden ORDER BY level DESC LIMIT 5"
)
top5 = cursor.fetchall()
```

- `fetchone()` = eine Zeile (oder `None`!)
- `fetchall()` = alle Zeilen als Liste

---

## Praxis: Heldenbestenliste

```python
def get_top_5_helden(pfad="dungeon.db"):
    with sqlite3.connect(pfad) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name, level FROM helden ORDER BY level DESC LIMIT 5"
        )
        return cursor.fetchall()
```

---

## Gruppenarbeit (60 Min)

1. `setup_db()`, `speichere_held_db()`, `get_top_5_helden()` einbauen
2. Bestenliste nach jedem Sieg formatiert ausgeben
3. Diskutiert: JSON vs. SQLite – was ist einfacher/umstaendlicher?
4. **Bonus:** alte `charakter.json` einmalig migrieren

---

## Tagesabschluss

- Jeder Kampf = eigene Zeile in der DB ✅
- Historie bleibt erhalten ✅
- **Problem:** Alles noch in einer Datei

**Morgen:** Aufteilung in Module (`db.py`, `game.py`, `main.py`) 🧩
