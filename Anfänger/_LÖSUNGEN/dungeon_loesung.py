"""
Tag 10 - Option 2: Das Mini-DnD / Text-Adventure ("Python Dungeon") - Loesung
================================================================================
Enthaelt die Basisversion sowie Beispielumsetzungen der optionalen
Erweiterungen:
- Zweite Waffe (Bogen) mit anderem Schadensbereich
- Inventar (Liste) fuer gesammelte Gegenstaende
- Fluchtchance: Fliehen gelingt nur mit einer Zufallswahrscheinlichkeit
"""

import random  # Erlaubt Zufallszahlen: random.randint(min, max)

# --- Schritt 1: ASCII-Art-Vorlagen ---

SWORD = """
      /| ________________
O|===|* >________________>
\\|
"""

BOW = """
     __
    /  \\
   /    \\  --->
   \\    /
    \\__/
"""

DRAGON = """
  <>=======()
  (/\\___/\\)   /\\_/\\
  |      |   ( o.o )
  ( ^_^* )    > ^ <
 [ROAARRR! Wer stoert meine Ruhe?]
"""

TREASURE = """
  ._________________.
  | [T R E A S U R E]|
  |  ############### |
  |_________________|
 [Glueckwunsch! Du hast gewonnen!]
"""

# --- Schritt 2: Werte initialisieren ---

player_hp = 100
dragon_hp = 80
potions = 3
inventar = []


def main():
    global player_hp, dragon_hp, potions, inventar
    print(DRAGON)
    print("Du betrittst die Hoehle des Python-Drachen!")

    waffenwahl = input("Waehle deine Waffe - [1] Schwert oder [2] Bogen: ")
    waffenname = "Bogen" if waffenwahl == "2" else "Schwert"
    inventar.append(waffenname)

    while player_hp > 0 and dragon_hp > 0:
        print(f"\nDeine HP: {player_hp} | Drachen-HP: {dragon_hp} | Traenke: {potions}")
        print(f"Inventar: {inventar}")
        print("[1] Angreifen")
        print("[2] Heiltrank trinken (+30 HP)")
        print("[3] Fliehen")

        wahl = input("Deine Aktion: ")

        if wahl == "1":
            # Waffen unterscheiden sich im Schadensbereich
            if waffenname == "Bogen":
                schaden = random.randint(5, 35)
                print(BOW)
            else:
                schaden = random.randint(10, 25)
                print(SWORD)
            dragon_hp = dragon_hp - schaden
            print(f"Treffer! Du fuegst dem Drachen {schaden} Schaden zu.")

        elif wahl == "2":
            if potions > 0:
                player_hp = player_hp + 30
                potions = potions - 1
                print("Du trinkst einen Heiltrank. +30 HP.")
            else:
                print("Keine Traenke mehr uebrig!")
            continue

        elif wahl == "3":
            # Flucht gelingt nur mit 50% Wahrscheinlichkeit
            fluchtchance = random.randint(1, 100)
            if fluchtchance <= 50:
                print("Die Flucht gelingt! Du entkommst der Hoehle.")
                break
            else:
                print("Die Flucht misslingt! Der Drache versperrt den Weg.")

        # Gegenangriff des Drachen (wenn er noch lebt)
        if dragon_hp > 0:
            drachen_schaden = random.randint(12, 22)
            player_hp = player_hp - drachen_schaden
            print(f"Der Drache speit Feuer und fuegt dir {drachen_schaden} Schaden zu!")

    # Spielende auswerten
    if dragon_hp <= 0:
        print(TREASURE)
        inventar.append("Schatz")
        print("Der Drache ist besiegt! Du pluenderst den Schatz.")
    elif player_hp <= 0:
        print("\nDu wurdest im Kampf besiegt... Versuche es naechstes Mal wieder!")


if __name__ == "__main__":
    main()
