"""
TAG 4 - DUNGEON DUEL - db.py
Zustaendig fuer ALLES rund um die Datenbank.
Enthaelt bewusst KEIN input()/print() fuer Benutzerinteraktion (siehe 4.2 Merksatz):
Funktionen hier liefern Daten per return oder speichern sie, mehr nicht.
"""

import sqlite3


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
    Speichert einen abgeschlossenen Kampf als neue Zeile in der Datenbank.

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


if __name__ == "__main__":
    # Testet dieses Modul unabhaengig, ohne dass main.py laufen muss
    setup_db()
    speichere_held_db("Testheld", 1, 1)
    print(get_top_5_helden())
