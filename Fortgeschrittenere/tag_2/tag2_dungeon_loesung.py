"""
TAG 2 - DUNGEON DUEL LOESUNG
Vollstaendig funktionsfaehige Version von dungeon.py, inklusive
Profi-Challenge (Levelaufstieg alle 3 besiegten Monster).
"""

import random
import json


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


def lade_charakter(pfad="charakter.json"):
    """
    Laedt den gespeicherten Charakter, oder erstellt einen neuen Standard-Charakter.

    Parameter:
        pfad (str): Pfad zur Speicherdatei

    Rueckgabewert:
        dict: z.B. {"level": 1, "besiegte_monster": 0}
    """
    try:
        with open(pfad, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except FileNotFoundError:
        return {"level": 1, "besiegte_monster": 0}


def speichere_charakter_state(held, pfad="charakter.json"):
    """
    Speichert den aktuellen Charakterzustand.

    Parameter:
        held (dict): Charakterdaten
        pfad (str): Zieldatei

    Rueckgabewert:
        None
    """
    with open(pfad, "w", encoding="utf-8") as datei:
        json.dump(held, datei)


def spiel_starten():
    """Fuehrt einen kompletten Kampf mit Charakterspeicherung aus."""
    charakter = lade_charakter()
    print(f"Willkommen zurueck! Level {charakter['level']}, {charakter['besiegte_monster']} besiegte Monster.")

    held_name = input("Wie heisst dein Held? ")
    held_hp = 100
    monster_hp = 50
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
            print(f"Monster besiegt nach {runde} Runden!")
            charakter["besiegte_monster"] += 1

            # Profi-Challenge: alle 3 besiegten Monster ein Levelaufstieg
            if charakter["besiegte_monster"] % 3 == 0:
                charakter["level"] += 1
                print(f"Level Up! Du bist jetzt Level {charakter['level']}.")

            speichere_charakter_state(charakter)
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
