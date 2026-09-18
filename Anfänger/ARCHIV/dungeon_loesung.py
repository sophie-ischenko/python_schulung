"""
Tag 10 - Option 2: Das Mini-DnD / Text-Adventure ("Python Dungeon")
======================================================================
Musterloesung / Beispielumsetzung der "Ideen zum Weiterbauen":
- Zweite Waffe (Dolch: geringerer, aber verlaesslicherer Schaden) zur
  Auswahl zu Spielbeginn
- Ein Inventar (Liste), das nach jedem gewonnenen Treffer zufaellig einen
  Fund sammeln kann
- Eine Fluchtchance: Fliehen gelingt nur mit einer Wahrscheinlichkeit von
  50%, sonst greift der Drache trotzdem an

ACHTUNG: Dieses Programm nutzt input(). Fuehre es am besten direkt als
Skript aus: python dungeon_loesung.py
"""

import random

# --- Schritt 1: ASCII-Art-Vorlagen ---

SWORD = """
      /| ________________
O|===|* >________________>
      \\|
"""

DAGGER = """
      /|--
O|===|*
      \\|--
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

# --- Schritt 2: Das Code-Geruest, erweitert ---

player_hp = 100
dragon_hp = 80
potions = 3
inventar = []

MOEGLICHE_FUNDE = ["Goldmuenze", "Drachenschuppe", "Alte Karte", "Rubin"]


def waehle_waffe():
    print("\nWelche Waffe waehlst du?")
    print("[1] Schwert (10-25 Schaden, hohe Varianz)")
    print("[2] Dolch (8-14 Schaden, verlaesslicher)")
    wahl = input("Waffe: ")
    if wahl == "2":
        return "dolch"
    return "schwert"


def main():
    global player_hp, dragon_hp, potions, inventar
    print(DRAGON)
    print("Du betrittst die Hoehle des Python-Drachen!")

    waffe = waehle_waffe()

    while player_hp > 0 and dragon_hp > 0:
        print(f"\nDeine HP: {player_hp} | Drachen-HP: {dragon_hp} | Traenke: {potions}")
        print(f"Inventar: {inventar}")
        print("[1] Angreifen")
        print("[2] Heiltrank trinken (+30 HP)")
        print("[3] Fliehen")

        wahl = input("Deine Aktion: ")

        if wahl == "1":
            if waffe == "dolch":
                schaden = random.randint(8, 14)
                print(DAGGER)
            else:
                schaden = random.randint(10, 25)
                print(SWORD)
            dragon_hp = dragon_hp - schaden
            print(f"Treffer! Du fuegst dem Drachen {schaden} Schaden zu.")

            # Chance auf einen Fund im Inventar
            if random.randint(1, 100) <= 40:
                fund = random.choice(MOEGLICHE_FUNDE)
                inventar.append(fund)
                print(f"Du findest nebenbei: {fund}!")

        elif wahl == "2":
            if potions > 0:
                player_hp = player_hp + 30
                potions = potions - 1
                print("Du trinkst einen Heiltrank. +30 HP.")
            else:
                print("Keine Traenke mehr uebrig!")
                continue

        elif wahl == "3":
            if random.random() < 0.5:
                print("Die Flucht gelingt! Du rennst schreiend davon... Spiel vorbei.")
                break
            else:
                print("Die Flucht misslingt - der Drache verstellt dir den Weg!")

        # Gegenangriff des Drachen (wenn er noch lebt)
        if dragon_hp > 0:
            drachen_schaden = random.randint(12, 22)
            player_hp = player_hp - drachen_schaden
            print(f"Der Drache speit Feuer und fuegt dir {drachen_schaden} Schaden zu!")

    # Spielende auswerten
    if dragon_hp <= 0:
        print(TREASURE)
        print("Der Drache ist besiegt! Du pluenderst den Schatz.")
        print(f"Gesammeltes Inventar: {inventar}")
    elif player_hp <= 0:
        print("\nDu wurdest im Kampf besiegt... Versuche es naechstes Mal wieder!")
        print(f"Gesammeltes Inventar: {inventar}")


if __name__ == "__main__":
    main()
