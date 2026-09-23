"""
TAG 3 - AUFGABEN (ohne Loesung)
Kunden-Register in drei Teilen. Verwendet eine eigene Datenbankdatei
"kunden.db" (nicht die Spiel-Datenbank "dungeon.db").
Die zugehoerige Theorie steht im Jupyter-Notebook "tag3_theorie.ipynb".
"""

import sqlite3


# =============================================================
# UEBUNG 1: Kunden-Register Teil 1 (45 Min)
# Lernziel: Datenbankdateien per Skript anlegen und mit DB Browser pruefen
# =============================================================
#
# 1. Schreibe setup_kunden_db(): Verbindung zu "kunden.db" herstellen,
#    Tabelle "users" anlegen mit Spalten:
#    name (TEXT), alter_jahre (INTEGER), guthaben (REAL)
#    conn.commit() und conn.close() nicht vergessen!
# 2. Fuehre das Skript aus
# 3. Oeffne kunden.db im DB Browser for SQLite, lege manuell 2 Testzeilen
#    an, klicke "Write Changes"


def setup_kunden_db(pfad="kunden.db"):
    # TODO: Docstring
    # TODO: Verbindung herstellen
    # TODO: CREATE TABLE IF NOT EXISTS users (...)
    # TODO: commit() und close()
    pass


# TODO: setup_kunden_db() aufrufen


# =============================================================
# UEBUNG 2: Kunden-Register Teil 2 (50 Min)
# Lernziel: Sicheres Einfuegen mit Context Manager und Fehlerbehandlung
# =============================================================
#
# 1. Schreibe add_user(name, alter_jahre, guthaben)
#    - with sqlite3.connect(pfad) as conn: ...
#    - INSERT mit ?-Platzhaltern fuer alle drei Werte
#    - try/except sqlite3.Error drumherum
# 2. while-Schleife: befragt Nutzer (Name/Alter/Guthaben), ruft add_user() auf,
#    beendet bei Eingabe "ende" als Name
# 3. Trage 3 Nutzer ein, pruefe im DB Browser (F5 zum Aktualisieren)


def add_user(name, alter_jahre, guthaben, pfad="kunden.db"):
    # TODO: Docstring
    # TODO: with sqlite3.connect(...) as conn: ...
    # TODO: INSERT mit ?-Platzhaltern
    # TODO: try/except sqlite3.Error
    pass


# TODO: while-Schleife zum Eintragen mehrerer Nutzer


# =============================================================
# UEBUNG 3: Kunden-Register Teil 3 (45 Min)
# Lernziel: Gefilterte Daten abfragen und formatiert aufbereiten
# =============================================================
#
# 1. get_richest_user(): fetchone() + ORDER BY guthaben DESC LIMIT 1
# 2. get_users_sorted_by_age(): fetchall() + ORDER BY alter_jahre ASC
# 3. Beide aufrufen, Ergebnisse formatiert mit print() ausgeben


def get_richest_user(pfad="kunden.db"):
    # TODO: Docstring
    # TODO: fetchone() + ORDER BY guthaben DESC LIMIT 1
    pass


def get_users_sorted_by_age(pfad="kunden.db"):
    # TODO: Docstring
    # TODO: fetchall() + ORDER BY alter_jahre ASC
    pass


# TODO: beide Funktionen aufrufen und Ergebnisse formatiert ausgeben
