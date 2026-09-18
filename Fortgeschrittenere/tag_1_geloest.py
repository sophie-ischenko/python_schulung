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
    eingabe_text = input("Aktion wählen (1 = Angriff, 2 = Verteidigen): ")

    try:
        aktion = int(eingabe_text)
    except ValueError:
        print("Fehler: Bitte nur 1 oder 2 eingeben!")
        continue # Springt nach oben, BEVOR die Runde gezählt wird

    if aktion not in [1, 2]:
        print("Ungültige Aktion! Wähle 1 oder 2.")
        continue # Springt nach oben, BEVOR die Runde gezählt wird

    # Ab hier wissen wir: Die Eingabe ist gültig! Jetzt erst die Runde zählen.
    runde += 1 

    if aktion == 1:
        schaden = random.randint(5, 20)
        
        # NEU: Kritischer Treffer (Gruppenaufgabe 2)
        if random.randint(1, 20) == 20:
            schaden = schaden * 2
            print("💥 KRITISCHER TREFFER! 💥")
            
        monster_hp -= schaden
        print(f"Du greifst an und fügst {schaden} Schaden zu! (Monster HP: {max(monster_hp, 0)})")
        
    elif aktion == 2:
        print("🛡️ Du gehst in Verteidigungsstellung.")

    # Prüfen, ob das Monster tot ist
    if monster_hp <= 0:
        print(f"🎉 🎉 🎉 DU HAST DAS MONSTER BESIEGT! 🎉 🎉 🎉")
        print(f"Du hast {runde} Runden gebraucht.")
        break

    # Monster greift an
    monster_schaden = random.randint(5, 15)
    if aktion == 2:
        monster_schaden = monster_schaden // 2   # Verteidigen halbiert den Schaden
        
    held_hp -= monster_schaden
    print(f"Das Monster greift an und fügt dir {monster_schaden} Schaden zu! (Deine HP: {max(held_hp, 0)})\n")

    # Prüfen, ob der Held tot ist
    if held_hp <= 0:
        print("💀 Du wurdest besiegt... 💀")
        break