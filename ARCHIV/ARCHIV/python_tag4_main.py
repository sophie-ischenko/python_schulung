"""
TAG 4 - DUNGEON DUEL - main.py
Zustaendig fuer Ablaufsteuerung und Konsolen-Ein-/Ausgabe.
Ruft ausschliesslich db.py und game.py auf - enthaelt selbst keine
Datenbank- oder Kampfberechnungs-Logik.
"""

from db import setup_db, speichere_held_db, get_top_5_helden
from game import kampfrunde, monster_greift_an, pruefe_aktion, UngueltigeAktionError


def main():
    """Fuehrt einen kompletten Kampf im Dungeon-Duel-Konsolenspiel aus."""
    setup_db()
    print("Willkommen bei DUNGEON DUEL")
    held_name = input("Wie heisst dein Held? ")

    held_hp, monster_hp = 100, 50
    level, besiegte_monster, runde = 1, 0, 0

    while True:
        eingabe_text = input("Aktion (1=Angriff, 2=Verteidigen): ")
        try:
            aktion = int(eingabe_text)
            pruefe_aktion(aktion)
        except ValueError:
            print("Bitte nur Zahlen eingeben!")
            continue
        except UngueltigeAktionError as e:
            print(e)
            continue

        runde += 1
        monster_hp, schaden = kampfrunde(monster_hp, aktion)
        print(f"Du fuegst {schaden} Schaden zu! (Monster HP: {max(monster_hp, 0)})")

        if monster_hp <= 0:
            besiegte_monster += 1
            print(f"Monster besiegt nach {runde} Runden!")
            speichere_held_db(held_name, level, besiegte_monster)
            print("Top 5 Helden:", get_top_5_helden())
            break

        monster_schaden = monster_greift_an(aktion)
        held_hp -= monster_schaden
        print(f"Das Monster fuegt dir {monster_schaden} Schaden zu! (Deine HP: {max(held_hp, 0)})")

        if held_hp <= 0:
            print("Du wurdest besiegt...")
            break


if __name__ == "__main__":
    main()
