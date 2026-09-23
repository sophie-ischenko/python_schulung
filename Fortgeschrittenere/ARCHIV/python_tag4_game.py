"""
TAG 4 - DUNGEON DUEL - game.py
Zustaendig fuer die Kampflogik. Enthaelt bewusst KEIN input()/print() fuer
Benutzerinteraktion - nur Berechnung und Validierung per return/raise.
"""

import random


class UngueltigeAktionError(Exception):
    """Wird ausgeloest, wenn eine Aktion ausserhalb der gueltigen Optionen liegt."""
    pass


def pruefe_aktion(aktion):
    """
    Prueft, ob eine Aktion gueltig ist.

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


def monster_greift_an(aktion):
    """
    Berechnet den Gegenangriff des Monsters.

    Parameter:
        aktion (int): die zuletzt gewaehlte Spieleraktion (2 = Verteidigen halbiert Schaden)

    Rueckgabewert:
        int: verursachter Schaden am Helden
    """
    schaden = random.randint(5, 15)
    if aktion == 2:
        schaden = schaden // 2
    return schaden


if __name__ == "__main__":
    # Testet dieses Modul unabhaengig, ohne dass main.py laufen muss
    print(kampfrunde(50, 1))
    print(monster_greift_an(2))
    try:
        pruefe_aktion(9)
    except UngueltigeAktionError as e:
        print(e)
