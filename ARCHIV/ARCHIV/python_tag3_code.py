"""
TAG 3 - DUNGEON DUEL
Code-Begleitdatei zum Notebook "Tag 3 - Umzug auf eine SQLite-Datenbank"

Enthaelt: Theorie-Beispiele, Uebungs-Starter (mit TODOs) und die fertige
SQLite-Anbindung fuer Dungeon Duel.

Hinweis: Fuer die Uebungen 1-3 (Kunden-Register) wird eine separate Datei
"kunden.db" verwendet, fuer die Praxis am Ende "dungeon.db".
"""

import sqlite3


# =============================================================
# 3.1 BEISPIEL: SQLite Grundlagen
# =============================================================

def setup_db(pfad="dungeon.db"):
    """
    Legt die Tabelle 'helden' an, falls sie noch nicht existiert.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        None
    """
    conn = sqlite3.connect(pfad)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS helden (
            name TEXT,
            level INTEGER,
            besiegte_monster INTEGER
        )
    """)
    conn.commit()
    conn.close()


# setup_db()   # einmal ausfuehren, um dungeon.db zu erzeugen


# =============================================================
# UEBUNG 1: Kunden-Register Teil 1 (45 Min)
# Lernziel: Datenbankdateien per Skript anlegen und mit DB Browser pruefen
# =============================================================

# def setup_kunden_db(pfad="kunden.db"):
#     TODO: Verbindung herstellen, Tabelle "users" anlegen
#     Spalten: name (TEXT), alter_jahre (INTEGER), guthaben (REAL)
#     conn.commit() und conn.close() nicht vergessen!
#
# setup_kunden_db()
#
# Danach: kunden.db im DB Browser for SQLite oeffnen,
# manuell 2 Testzeilen anlegen, "Write Changes" klicken


# =============================================================
# 3.2 BEISPIEL: INSERT, Security & Context Manager
# =============================================================

# GEFAEHRLICHE VARIANTE (nur zur Demo, NICHT verwenden!):
# eingabe = input("Heldenname zum Loeschen: ")
# cursor.execute(f"DELETE FROM helden WHERE name = '{eingabe}'")
# -> Eingabe  Aria' OR '1'='1  wuerde ALLE Zeilen loeschen (SQL-Injection)

def speichere_held_db(name, level, besiegte_monster, pfad="dungeon.db"):
    """
    Speichert einen abgeschlossenen Kampf als neue Zeile.

    Parameter:
        name (str): Heldenname
        level (int): aktuelles Level
        besiegte_monster (int): Anzahl besiegter Monster
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        None
    """
    try:
        with sqlite3.connect(pfad) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO helden (name, level, besiegte_monster) VALUES (?, ?, ?)",
                (name, level, besiegte_monster)
            )
    except sqlite3.Error as e:
        print(f"Fehler beim Speichern: {e}")


# speichere_held_db("Aria", 3, 12)   # Testaufruf


# =============================================================
# UEBUNG 2: Kunden-Register Teil 2 (50 Min)
# Lernziel: Sicheres Einfuegen mit Context Manager und Fehlerbehandlung
# =============================================================

# def add_user(name, alter_jahre, guthaben, pfad="kunden.db"):
#     TODO: with sqlite3.connect(pfad) as conn: ...
#     TODO: INSERT mit ?-Platzhaltern fuer alle drei Werte
#     TODO: try/except sqlite3.Error drumherum
#
# while True:
#     name = input("Name (oder 'ende'): ")
#     if name == "ende":
#         break
#     alter_jahre = int(input("Alter: "))
#     guthaben = float(input("Guthaben: "))
#     add_user(name, alter_jahre, guthaben)
#
# Danach: 3 Nutzer eintragen, im DB Browser mit F5 aktualisieren und pruefen


# =============================================================
# 3.3 BEISPIEL: SELECT, ORDER BY, LIMIT
# =============================================================

def get_top_kunden(pfad="kunden.db"):
    """
    Liest die drei Kunden mit dem hoechsten Guthaben aus.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        list[tuple]: z.B. [("Anna", 150.5), ("Tom", 50.0)]
    """
    with sqlite3.connect(pfad) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, guthaben FROM users ORDER BY guthaben DESC LIMIT 3")
        return cursor.fetchall()


# for eintrag in get_top_kunden():
#     print(f"Name: {eintrag[0]} | Guthaben: {eintrag[1]}EUR")


# =============================================================
# UEBUNG 3: Kunden-Register Teil 3 (45 Min)
# Lernziel: Gefilterte Daten abfragen und formatiert aufbereiten
# =============================================================

# def get_richest_user(pfad="kunden.db"):
#     TODO: fetchone() + ORDER BY guthaben DESC LIMIT 1
#
# def get_users_sorted_by_age(pfad="kunden.db"):
#     TODO: fetchall() + ORDER BY alter_jahre ASC
#
# TODO: beide Funktionen aufrufen und Ergebnisse mit print() formatiert ausgeben


# =============================================================
# PRAXIS: Dungeon Duel mit SQLite (lauffaehig)
# =============================================================

def get_top_5_helden(pfad="dungeon.db"):
    """
    Liest die fuenf Helden mit dem hoechsten Level aus.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        list[tuple]: z.B. [("Aria", 5), ("Finn", 4), ...]
    """
    with sqlite3.connect(pfad) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, level FROM helden ORDER BY level DESC LIMIT 5")
        return cursor.fetchall()


def kampfrunde(monster_hp, aktion):
    """
    Berechnet den Effekt einer Spieleraktion auf die Monster-HP.
    (identisch zu Tag 2 - siehe dortige Code-Datei)

    Parameter:
        monster_hp (int): aktuelle HP des Monsters
        aktion (int): 1 = Angriff, 2 = Verteidigen

    Rueckgabewert:
        tuple[int, int]: (neue Monster-HP, verursachter Schaden)
    """
    import random
    if aktion == 1:
        schaden = random.randint(5, 20)
        return monster_hp - schaden, schaden
    return monster_hp, 0


def spiel_starten():
    """Fuehrt einen kompletten Kampf mit SQLite-Speicherung aus. Keine Parameter, keine Rueckgabe."""
    setup_db()
    print("Willkommen bei DUNGEON DUEL")
    held_name = input("Wie heisst dein Held? ")

    held_hp = 100
    monster_hp = 50
    level = 1
    besiegte_monster = 0
    runde = 0

    while True:
        runde += 1
        eingabe_text = input("Aktion (1=Angriff, 2=Verteidigen): ")
        try:
            aktion = int(eingabe_text)
        except ValueError:
            print("Bitte nur Zahlen eingeben!")
            continue

        monster_hp, schaden = kampfrunde(monster_hp, aktion)
        print(f"Du fuegst {schaden} Schaden zu! (Monster HP: {max(monster_hp, 0)})")

        if monster_hp <= 0:
            besiegte_monster += 1
            print(f"Monster besiegt nach {runde} Runden!")
            speichere_held_db(held_name, level, besiegte_monster)
            print("Top 5 Helden:", get_top_5_helden())
            break

        import random
        monster_schaden = random.randint(5, 15)
        if aktion == 2:
            monster_schaden = monster_schaden // 2
        held_hp -= monster_schaden
        print(f"Das Monster fuegt dir {monster_schaden} Schaden zu! (Deine HP: {max(held_hp, 0)})")

        if held_hp <= 0:
            print("Du wurdest besiegt...")
            break


# spiel_starten()   # zum Testen einkommentieren


# =============================================================
# GRUPPENARBEIT: Heldenbestenliste einbauen (60 Min)
# =============================================================
# 1. setup_db(), speichere_held_db() und get_top_5_helden() in euer
#    eigenes Spiel (aus Tag 1/2) einbauen
# 2. Bei jedem Sieg speichere_held_db() aufrufen
# 3. Formatierte Top-5-Ausgabe nach dem Kampf
# 4. Testet mehrere Runden, prueft die Datenbank im DB Browser
# 5. Diskutiert: JSON (Tag 2) vs. SQLite - was ist einfacher, was umstaendlicher?
# 6. BONUS: Einmalige Migration einer alten charakter.json in die neue DB
