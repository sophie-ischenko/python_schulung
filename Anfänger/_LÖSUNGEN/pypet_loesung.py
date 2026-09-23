"""
Tag 10 - Option 1: Das Retro-Tamagotchi ("PyPet") - Loesung
=============================================================
Enthaelt die Pflichtaufgabe (Spielen & Schlafen ergaenzen) sowie
Beispielumsetzungen der optionalen Erweiterungen:
- Vierte Aktion "Streicheln" (nur +Laune)
- ASCII-Art fuer den muede-Zustand (PET_TIRED)
- Runden-Zaehler als kleiner Highscore
"""

# --- Schritt 1: ASCII-Art-Vorlagen ---

PET_HAPPY = """
   /\\_/\\
  ( ^.^ )
   > ^ <
 [Miau! Mir geht es super!]
"""

PET_HUNGRY = """
   /\\_/\\
  ( o.o )
   > v <
 [Magen knurrt... Hunger!]
"""

PET_TIRED = """
   /\\_/\\
  ( -.- )
   > . <
 [Zzz... so muede...]
"""

PET_DEAD = """
   /\\_/\\
  ( x.x )
   > o <
 [Oh nein! Dein Haustier ist weggelaufen...]
"""

# --- Schritt 2: Werte initialisieren ---

hunger = 50
energie = 50
laune = 50
runden = 0


def zeige_status(hunger, energie, laune):
    print("\n--- STATUS ---")
    print(f"Hunger:  {hunger}/100")
    print(f"Energie: {energie}/100")
    print(f"Laune:   {laune}/100")

    # ASCII Art je nach Zustand ausgeben
    if hunger > 80:
        print(PET_HUNGRY)
    elif hunger >= 100 or energie <= 0:
        print(PET_DEAD)
    elif energie < 20:
        print(PET_TIRED)
    else:
        print(PET_HAPPY)


def main():
    global hunger, energie, laune, runden
    print("Willkommen bei PyPet - Deinem digitalen Haustier!")

    while True:
        zeige_status(hunger, energie, laune)

        # Pruefen auf Game Over
        if hunger >= 100 or energie <= 0:
            print(f"Das Spiel ist aus. Du hast {runden} Runden ueberlebt.")
            break

        print("\nWas moechtest du tun?")
        print("[1] Fuettern (+20 Energie, -20 Hunger)")
        print("[2] Spielen (+20 Laune, -10 Energie, +10 Hunger)")
        print("[3] Schlafen (+50 Energie, +10 Hunger)")
        print("[4] Streicheln (+15 Laune)")
        print("[q] Beenden")

        wahl = input("Deine Wahl: ").lower()

        if wahl == "q":
            print(f"Tschuess! Du hast {runden} Runden ueberlebt.")
            break
        elif wahl == "1":
            hunger = hunger - 20
            energie = energie + 20
        elif wahl == "2":
            laune = laune + 20
            energie = energie - 10
            hunger = hunger + 10
        elif wahl == "3":
            energie = energie + 50
            hunger = hunger + 10
        elif wahl == "4":
            laune = laune + 15

        runden = runden + 1

        # Werte-Begrenzung (nicht unter 0, nicht ueber 100)
        hunger = max(0, min(hunger, 100))
        energie = max(0, min(energie, 100))
        laune = max(0, min(laune, 100))


if __name__ == "__main__":
    main()
