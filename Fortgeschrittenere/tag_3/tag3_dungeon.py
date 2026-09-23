"""
TAG 3 - DUNGEON DUEL (Praxis-Skelett, ohne Loesung)
Ersetzt die JSON-Speicherung aus Tag 2 durch SQLite und baut eine
Heldenbestenliste. Fuellt die TODOs aus.
"""

import random
import sqlite3


def setup_db(pfad="dungeon.db"):
    """
    Legt die Tabelle 'helden' an, falls sie noch nicht existiert.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        None
    """
    # TODO: Verbindung herstellen (sqlite3.connect)
    # TODO: CREATE TABLE IF NOT EXISTS helden (name TEXT, level INTEGER, besiegte_monster INTEGER)
    # TODO: commit() und close()
    pass


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
    # TODO: with sqlite3.connect(pfad) as conn: ...
    # TODO: INSERT mit ?-Platzhaltern
    # TODO: try/except sqlite3.Error
    pass


def get_top_5_helden(pfad="dungeon.db"):
    """
    Liest die fuenf Helden mit dem hoechsten Level aus.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        list[tuple]: z.B. [("Aria", 5), ("Finn", 4), ...]
    """
    # TODO: SELECT name, level FROM helden ORDER BY level DESC LIMIT 5
    # TODO: fetchall() zurueckgeben
    pass


def kampfrunde(monster_hp, aktion):
    """
    Berechnet den Effekt einer Spieleraktion auf die Monster-HP.
    (identisch zu Tag 2)

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
            # TODO: speichere_held_db() aufrufen
            # TODO: Top-5-Bestenliste holen und formatiert ausgeben
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


# =============================================================
# BONUS: Migration einer alten charakter.json
# =============================================================
# TODO: json.load() der alten charakter.json aus Tag 2
# TODO: Werte per speichere_held_db() einmalig in die neue DB uebertragen
