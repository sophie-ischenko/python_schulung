"""
TAG 3 - DUNGEON DUEL LOESUNG
Vollstaendig funktionsfaehige Version von dungeon.py mit SQLite-Anbindung
und Heldenbestenliste, inklusive Bonus-Migration aus charakter.json.
"""

import random
import sqlite3
import json
import os


def setup_db(pfad="dungeon.db"):
    """
    Legt die Tabelle 'helden' an, falls sie noch nicht existiert.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        None
    """
    with sqlite3.connect(pfad) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS helden (
                name TEXT,
                level INTEGER,
                besiegte_monster INTEGER
            )
        """)


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

    Parameter:
        monster_hp (int): aktuelle HP des Monsters
        aktion (int): 1 = Angriff, 2 = Verteidigen

    Rueckgabewert:
        tuple[int, int]: (neue Monster-HP, verursachter Schaden)
    """
    if aktion == 1:
        schaden = random.randint(5, 20)
        return monster_hp - schaden, schaden
    return monster_hp, 0


def migriere_json_charakter(json_pfad="charakter.json", db_pfad="dungeon.db"):
    """
    Uebertraegt einen alten JSON-Charakter (aus Tag 2) einmalig in die SQLite-DB.

    Parameter:
        json_pfad (str): Pfad zur alten charakter.json
        db_pfad (str): Pfad zur Ziel-Datenbank

    Rueckgabewert:
        bool: True bei erfolgreicher Migration, False wenn keine Datei gefunden wurde
    """
    if not os.path.exists(json_pfad):
        return False
    with open(json_pfad, "r", encoding="utf-8") as datei:
        charakter = json.load(datei)
    speichere_held_db("Migrierter Held", charakter["level"], charakter["besiegte_monster"], db_pfad)
    return True


def spiel_starten():
    """Fuehrt einen kompletten Kampf mit SQLite-Speicherung aus."""
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

            print("\nTop 5 Helden:")
            for platz, (name, lvl) in enumerate(get_top_5_helden(), start=1):
                print(f"  {platz}. {name} - Level {lvl}")
            break

        monster_schaden = random.randint(5, 15)
        if aktion == 2:
            monster_schaden = monster_schaden // 2
        held_hp -= monster_schaden
        print(f"Das Monster fuegt dir {monster_schaden} Schaden zu! (Deine HP: {max(held_hp, 0)})")

        if held_hp <= 0:
            print("Du wurdest besiegt...")
            break


if __name__ == "__main__":
    spiel_starten()
