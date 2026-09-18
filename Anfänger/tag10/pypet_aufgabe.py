"""
Tag 10 - Option 1: Das Retro-Tamagotchi ("PyPet")
====================================================
Aufgabe: Dieses Geruest ist schon lauffaehig - aber die Aktionen "Spielen"
(Option 2) und "Schlafen" (Option 3) fehlen noch! Nur "Fuettern" (Option 1)
ist bereits fertig eingebaut.

Deine Aufgabe: Ergaenze an der markierten Stelle
(# HIER: Weitere Logik fuer Option 2 und 3 einbauen!) die passenden
elif-Zweige.

Erinnerung:
- Fuettern:  +20 Energie, -20 Hunger   (schon vorhanden)
- Spielen:   +20 Laune,   -10 Energie, +10 Hunger
- Schlafen:  +50 Energie, +10 Hunger

Tipp: 'global hunger, energie, laune' am Anfang von main() sorgt dafuer,
dass du innerhalb der Funktion die Variablen von aussen veraendern darfst.

ACHTUNG: Dieses Programm nutzt input(). Fuehre es am besten direkt als
Skript aus: python pypet_aufgabe.py

Optionale Ideen zum Weiterbauen, wenn die Grundversion laeuft (siehe auch
'pypet_loesung.py' fuer ein Beispiel, wie man sie umsetzen koennte):
- TODO: Eine vierte Aktion, z. B. "Streicheln" (nur +Laune, keine anderen Effekte)
- TODO: Eine eigene ASCII-Art fuer einen Zwischenzustand, z. B. PET_TIRED,
  wenn die Energie unter 20 faellt
- TODO: Ein Highscore-Zaehler, der mitzaehlt, wie viele Runden das
  Haustier ueberlebt hat
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

PET_DEAD = """
   /\\_/\\
  ( x.x )
   > o <
 [Oh nein! Dein Haustier ist weggelaufen...]
"""

# --- Schritt 2: Das Code-Geruest (Starter-Kit) ---

# Werte initialisieren
hunger = 50
energie = 50
laune = 50


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
    else:
        print(PET_HAPPY)


def main():
    global hunger, energie, laune
    print("Willkommen bei PyPet - Deinem digitalen Haustier!")

    while True:
        zeige_status(hunger, energie, laune)

        # Pruefen auf Game Over
        if hunger >= 100 or energie <= 0:
            print("Das Spiel ist aus.")
            break

        print("\nWas moechtest du tun?")
        print("[1] Fuettern (+20 Energie, -20 Hunger)")
        print("[2] Spielen (+20 Laune, -10 Energie, +10 Hunger)")
        print("[3] Schlafen (+50 Energie, +10 Hunger)")
        print("[q] Beenden")

        wahl = input("Deine Wahl: ").lower()

        if wahl == "q":
            print("Tschuess!")
            break
        elif wahl == "1":
            hunger = hunger - 20
            energie = energie + 20
        # HIER: Weitere Logik fuer Option 2 und 3 einbauen!

        # Werte-Begrenzung (nicht unter 0, nicht ueber 100)
        hunger = max(0, min(hunger, 100))
        energie = max(0, min(energie, 100))
        laune = max(0, min(laune, 100))


if __name__ == "__main__":
    main()
