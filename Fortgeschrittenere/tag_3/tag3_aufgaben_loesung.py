"""
TAG 3 - AUFGABEN LOESUNG
Vollstaendig geloeste Version von aufgaben.py (Kunden-Register).
"""

import sqlite3


# =============================================================
# UEBUNG 1: Kunden-Register Teil 1
# =============================================================

def setup_kunden_db(pfad="kunden.db"):
    """
    Legt die Tabelle 'users' an, falls sie noch nicht existiert.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        None
    """
    conn = sqlite3.connect(pfad)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            alter_jahre INTEGER,
            guthaben REAL
        )
    """)
    conn.commit()
    conn.close()


setup_kunden_db()


# =============================================================
# UEBUNG 2: Kunden-Register Teil 2
# =============================================================

def add_user(name, alter_jahre, guthaben, pfad="kunden.db"):
    """
    Fuegt einen neuen Kunden in die Datenbank ein.

    Parameter:
        name (str): Kundenname
        alter_jahre (int): Alter in Jahren
        guthaben (float): aktuelles Guthaben
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        None
    """
    try:
        with sqlite3.connect(pfad) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, alter_jahre, guthaben) VALUES (?, ?, ?)",
                (name, alter_jahre, guthaben)
            )
    except sqlite3.Error as e:
        print(f"Fehler beim Speichern: {e}")


while True:
    name = input("Name (oder 'ende'): ")
    if name == "ende":
        break
    alter_jahre = int(input("Alter: "))
    guthaben = float(input("Guthaben: "))
    add_user(name, alter_jahre, guthaben)


# =============================================================
# UEBUNG 3: Kunden-Register Teil 3
# =============================================================

def get_richest_user(pfad="kunden.db"):
    """
    Liest den Kunden mit dem hoechsten Guthaben aus.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        tuple | None: (name, alter_jahre, guthaben) oder None, falls leer
    """
    with sqlite3.connect(pfad) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, alter_jahre, guthaben FROM users ORDER BY guthaben DESC LIMIT 1")
        return cursor.fetchone()


def get_users_sorted_by_age(pfad="kunden.db"):
    """
    Liest alle Kunden sortiert nach Alter aufsteigend.

    Parameter:
        pfad (str): Pfad zur Datenbankdatei

    Rueckgabewert:
        list[tuple]: [(name, alter_jahre, guthaben), ...]
    """
    with sqlite3.connect(pfad) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, alter_jahre, guthaben FROM users ORDER BY alter_jahre ASC")
        return cursor.fetchall()


reichster = get_richest_user()
if reichster:
    print(f"Reichster Kunde: {reichster[0]} mit {reichster[2]}EUR")
else:
    print("Noch keine Kunden vorhanden.")

print("\nAlle Kunden nach Alter sortiert:")
for kunde in get_users_sorted_by_age():
    print(f"  {kunde[0]} ({kunde[1]} Jahre) - {kunde[2]}EUR")
