"""
Tag 10 - Option 2: Das Mini-DnD / Text-Adventure ("Python Dungeon")
======================================================================
Dieses Geruest ist bereits vollstaendig lauffaehig - Angreifen, Heiltrank
und Fliehen funktionieren schon, inklusive Gegenangriff des Drachens mit
random.randint() fuer Zufallsschaden.

Deine Aufgabe fuer heute: Erweitere das Spiel nach eigenem Geschmack.
Ein paar Ideen (siehe auch 'dungeon_loesung.py' fuer eine Beispielumsetzung):
- TODO: Eine zweite Waffe mit anderem Schadensbereich, zwischen der du
  waehlen kannst
- TODO: Ein Inventar (Liste), in dem du gesammelte Gegenstaende speicherst
- TODO: Eine Fluchtchance: "Fliehen" gelingt nur mit einer gewissen
  Zufallswahrscheinlichkeit, sonst greift der Drache trotzdem an

ACHTUNG: Dieses Programm nutzt input(). Fuehre es am besten direkt als
Skript aus: python dungeon_aufgabe.py
"""

import random  # Erlaubt Zufallszahlen: random.randint(min, max)

# --- Schritt 1: ASCII-Art-Vorlagen ---

SWORD = """
      /| ________________
O|===|* >________________>
      \\|
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

# --- Schritt 2: Das Code-Geruest (Starter-Kit) ---

player_hp = 100
dragon_hp = 80
potions = 3


def main():
    global player_hp, dragon_hp, potions
    print(DRAGON)
    print("Du betrittst die Hoehle des Python-Drachen!")

    while player_hp > 0 and dragon_hp > 0:
        print(f"\nDeine HP: {player_hp} | Drachen-HP: {dragon_hp} | Traenke: {potions}")
        print("[1] Angreifen (Schwert)")
        print("[2] Heiltrank trinken (+30 HP)")
        print("[3] Fliehen")

        wahl = input("Deine Aktion: ")

        if wahl == "1":
            # Zufaelligen Schaden berechnen
            schaden = random.randint(10, 25)
            dragon_hp = dragon_hp - schaden
            print(SWORD)
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
            print("Du rennst schreiend davon... Spiel vorbei.")
            break

        # Gegenangriff des Drachen (wenn er noch lebt)
        if dragon_hp > 0:
            drachen_schaden = random.randint(12, 22)
            player_hp = player_hp - drachen_schaden
            print(f"Der Drache speit Feuer und fuegt dir {drachen_schaden} Schaden zu!")

    # Spielende auswerten
    if dragon_hp <= 0:
        print(TREASURE)
        print("Der Drache ist besiegt! Du pluenderst den Schatz.")
    elif player_hp <= 0:
        print("\nDu wurdest im Kampf besiegt... Versuche es naechstes Mal wieder!")


if __name__ == "__main__":
    main()
