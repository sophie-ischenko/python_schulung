import random

# =============================================================
# PRAXIS: Kampf-Grundgeruest (lauffaehig)
# =============================================================

INTRO_TEXT = """
--------------------------------------------------
Willkommen bei DUNGEON DUEL
Ein wildes Monster erscheint! Kaempfe um dein Leben!
--------------------------------------------------
"""

print(INTRO_TEXT)
held_name = input("Wie heisst dein Held? ")
print(f"Viel Erfolg im Kampf, {held_name}!\n")

held_hp = 100
monster_hp = 50
runde = 0

while True:
    runde += 1
    eingabe_text = input("Aktion waehlen (1 = Angriff, 2 = Verteidigen): ")

    try:
        aktion = int(eingabe_text)
    except ValueError:
        print("Fehler: Bitte nur 1 oder 2 eingeben!")
        continue

    if aktion == 1:
        schaden = random.randint(5, 20)
        # TODO (Erweiterung Kritischer Treffer): wenn random.randint(1, 20) == 20,
        # Schaden verdoppeln und "KRITISCHER TREFFER!" ausgeben
        monster_hp -= schaden
        print(f"Du greifst an und fuegst {schaden} Schaden zu! (Monster HP: {max(monster_hp, 0)})")
    elif aktion == 2:
        print("Du gehst in Verteidigungsstellung.")
    else:
        print("Ungueltige Aktion! Waehle 1 oder 2.")
        continue

    if monster_hp <= 0:
        print("GEWONNEN! Du hast das Monster besiegt!")
        print(f"Du hast {runde} Runden gebraucht.")
        break

    monster_schaden = random.randint(5, 15)
    if aktion == 2:
        monster_schaden = monster_schaden // 2   # Verteidigen halbiert den Schaden
    held_hp -= monster_schaden
    print(f"Das Monster greift an und fuegt dir {monster_schaden} Schaden zu! (Deine HP: {max(held_hp, 0)}, Monster HP: {max(monster_hp, 0)})")

    if held_hp <= 0:
        print("Du wurdest besiegt...")
        break


# =============================================================
# GRUPPENARBEIT: Erweiterungen (45 Min)
# =============================================================
# 1. Testet: ist das Spiel wirklich absturzsicher?
# 2. Kritischer Treffer einbauen (siehe TODO oben im Angriffs-Zweig)
# 3. Denksport: Wo muss "runde += 1" stehen, damit ungueltige Aktionen
#    (z.B. Eingabe 3) NICHT als Runde zaehlen? Baut das um.
