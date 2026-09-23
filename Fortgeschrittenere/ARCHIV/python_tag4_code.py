"""
TAG 4 - DUNGEON DUEL
Code-Begleitdatei zum Notebook "Tag 4 - Software-Architektur - Module aufteilen"

Enthaelt: Theorie-Beispiele (4.1-4.3) und Uebungs-Starter mit TODOs.
Die finale Praxis-Aufteilung in db.py / game.py / main.py folgt als
separate Dateien im Anschluss.
"""


# =============================================================
# 4.1 BEISPIEL: Module & Imports
# =============================================================

# Angenommen, dies waere der Inhalt einer Datei "helpers.py":
#
#     def verdopple(zahl):
#         """Verdoppelt eine Zahl. Parameter: zahl (int/float). Rueckgabewert: gleicher Typ."""
#         return zahl * 2
#
#     def formatiere_hp(hp):
#         """Formatiert einen HP-Wert als Anzeige-String. Parameter: hp (int). Rueckgabewert: str."""
#         return f"{hp} HP"
#
# In einer anderen Datei "main.py" wuerde man importieren mit:
#
#     import helpers
#     ergebnis = helpers.verdopple(5)
#
#     # oder gezielt:
#     from helpers import verdopple, formatiere_hp
#     print(formatiere_hp(80))


# =============================================================
# UEBUNG 1: Die Werkzeugkiste (30 Min)
# Lernziel: Module anlegen, importieren, Ladezeitpunkt beobachten
# =============================================================

# Datei "mathe_helfer.py":
#
# def ist_primzahl(zahl):
#     TODO: Docstring (Was/Parameter/Rueckgabewert)
#     TODO: prueft, ob zahl eine Primzahl ist -> bool
#
# def fakultaet(zahl):
#     TODO: Docstring
#     TODO: berechnet zahl! (z.B. per Schleife) -> int
#
# def ggt(a, b):
#     TODO: Docstring
#     TODO: groesster gemeinsamer Teiler von a und b -> int
#
# print("Datei wurde geladen")   # <- beobachtet, WANN diese Zeile ausgefuehrt wird!
#
#
# Datei "main.py":
#
# from mathe_helfer import ist_primzahl, fakultaet, ggt
# print(ist_primzahl(7))
# print(fakultaet(5))
# print(ggt(12, 18))


# =============================================================
# 4.2 BEISPIEL: __name__ == "__main__"
# =============================================================

def verdopple(zahl):
    """Verdoppelt eine Zahl. Parameter: zahl (int/float). Rueckgabewert: gleicher Typ."""
    return zahl * 2


if __name__ == "__main__":
    print(verdopple(21))   # laeuft NUR, wenn diese Datei direkt gestartet wird


# =============================================================
# UEBUNG 2: Testbare Module (30 Min)
# Lernziel: Module unabhaengig testbar machen
# =============================================================

# Ergaenzt "mathe_helfer.py" um:
#
# if __name__ == "__main__":
#     TODO: alle drei Funktionen (ist_primzahl, fakultaet, ggt) mit Testwerten aufrufen
#     TODO: Ergebnisse mit print() ausgeben
#
# Testet: Beim Ausfuehren von main.py duerfen diese Testausgaben NICHT erscheinen,
# nur beim direkten Start von mathe_helfer.py selbst.


# =============================================================
# 4.3 BEISPIEL: Eigene Exceptions
# =============================================================

class UngueltigeAktionError(Exception):
    """Wird ausgeloest, wenn eine Aktion ausserhalb der gueltigen Optionen liegt."""
    pass


def pruefe_aktion(aktion):
    """
    Prueft, ob eine Aktion gueltig ist (1=Angriff, 2=Verteidigen).

    Parameter:
        aktion (int): gewaehlte Aktion

    Rueckgabewert:
        int: die geprueften Aktion, falls gueltig

    Loest aus:
        UngueltigeAktionError, falls aktion nicht 1 oder 2 ist
    """
    if aktion not in (1, 2):
        raise UngueltigeAktionError("Aktion muss 1 (Angriff) oder 2 (Verteidigen) sein")
    return aktion


try:
    pruefe_aktion(5)
except UngueltigeAktionError as e:
    print(f"Ungueltige Eingabe: {e}")


# =============================================================
# UEBUNG 3: Der Ticket-Validator (30 Min)
# Lernziel: Eigene Exceptions definieren und gezielt abfangen
# =============================================================

# class UngueltigesTicketError(Exception):
#     TODO: kurze Docstring-Beschreibung
#     pass
#
# def pruefe_ticket(preis):
#     TODO: Docstring
#     TODO: wirft UngueltigesTicketError, wenn preis <= 0 oder preis > 500
#     TODO: gibt preis zurueck, falls gueltig
#
# try:
#     pruefe_ticket(-10)
# except UngueltigesTicketError as e:
#     print(f"Ungueltiges Ticket: {e}")


# =============================================================
# PRAXIS-PLANUNG: Aufteilung in drei Dateien
# =============================================================
# db.py     -> setup_db(), speichere_held_db(), get_top_5_helden()
# game.py   -> kampfrunde(), monster_greift_an(), pruefe_aktion(), UngueltigeAktionError
# main.py   -> Begruessung, while-Schleife, input()/print(), ruft db.py und game.py auf
#
# Die fertigen drei Dateien folgen im Anschluss als separate Code-Dateien
# (db.py, game.py, main.py) - nutzt sie als Referenz/Zielbild fuer eure
# eigene Aufteilung.
