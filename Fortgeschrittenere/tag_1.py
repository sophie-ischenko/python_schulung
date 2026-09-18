import random

INTRO_TEXT = """
--------------------------------------------------
⚔️  Willkommen bei DUNGEON DUEL  ⚔️
Ein wildes Monster erscheint! Kämpfe um dein Leben!
--------------------------------------------------
"""

print(INTRO_TEXT)
held_name = input("Wie heißt dein Held? ")
print(f"Viel Erfolg im Kampf, {held_name}!\n")

held_hp = 100
monster_hp = 50
runde = 0

while True:
    runde += 1
    eingabe_text = input("Aktion wählen (1 = Angriff, 2 = Verteidigen): ")

    try:
        aktion = int(eingabe_text)
    except ValueError:
        print("Fehler: Bitte nur 1 oder 2 eingeben!")
        continue

    if aktion == 1:
        schaden = random.randint(5, 20)
        monster_hp -= schaden
        print(f"Du greifst an und fügst {schaden} Schaden zu! (Monster HP: {max(monster_hp, 0)})")
    elif aktion == 2:
        print("Du gehst in Verteidigungsstellung.")
    else:
        print("Ungültige Aktion! Wähle 1 oder 2.")
        continue

    if monster_hp <= 0:
        print(f"🎉 🎉 🎉 DU HAST DAS MONSTER BESIEGT! 🎉 🎉 🎉")
        print(f"Du hast {runde} Runden gebraucht.")
        break

    monster_schaden = random.randint(5, 15)
    if aktion == 2:
        monster_schaden = monster_schaden // 2   # Verteidigen halbiert den Schaden
    held_hp -= monster_schaden
    print(f"Das Monster greift an und fügt dir {monster_schaden} Schaden zu! (Deine HP: {max(held_hp, 0)})")

    if held_hp <= 0:
        print("💀 Du wurdest besiegt... 💀")
        break
