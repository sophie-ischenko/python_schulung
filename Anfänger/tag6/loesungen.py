# R1
einkauf = ["Brot", "Milch", "Eier"]
einkauf.append("Äpfel")
print(f"Anzahl: {len(einkauf)}")

# R2
highscores = ["Anna", "Berta", "Chris"]
highscores[1] = "Ben"
print(highscores)

# R3
temps = [21.5, 24.0, 19.8, 25.4, 22.1]
print(f"Min: {min(temps)}, Max: {max(temps)}")

# R4
todos = ["Wäsche waschen", "Kochen", "Müll rausbringen"]
erledigt = todos.pop()
print(f"Erledigt: {erledigt}, Noch offen: {todos}")

# R5
teilnehmer = ["Zorro", "Aaron", "Xenia", "Berta"]
teilnehmer.sort(reverse=True)
print(teilnehmer)

# R6
hausverbot = ["Max", "Moritz"]
print("Max" in hausverbot)

# A1
alter = int(input("Alter: "))
print("Volljährig" if alter >= 18 else "Nicht volljährig")

# A2
pw = input("Passwort: ")
print("Willkommen" if pw == "kittycat" else "Zutritt verweigert")

# A3
zahl = int(input("Zahl: "))
print("Gerade" if zahl % 2 == 0 else "Ungerade")

# B4
heim = int(input("Heim-Tore: "))
gast = int(input("Gast-Tore: "))
if heim > gast: print("Heim siegt")
elif gast > heim: print("Gast siegt")
else: print("Unentschieden")

# B5
pkt = int(input("Punkte: "))
if pkt < 50: print("Durchgefallen")
elif pkt < 90: print("Bestanden")
else: print("Sehr gut")

# B6
datum = input("Datum: ")
if datum == "24.12.": print("Heiligabend")
elif datum == "31.12.": print("Silvester")
elif datum == "01.01.": print("Frohes neues Jahr")
else: print("Normaler Tag")

# C7
duck_neffen = ["Tick", "Trick", "Track"]
name = input("Name: ")
print("Neffe!" if name in duck_neffen else "Unbekannt")

# C8
geschlossen = True
name = input("Name: ")
print("Willkommen" if not (geschlossen and name != "VIP") else "Nur für Gäste")

# C9
alter = int(input("Alter: "))
begleiter = input("Erwachsener dabei? (ja/nein): ")
if alter >= 12 or begleiter == "ja": print("Viel Spaß!")
else: print("Zutritt verweigert")

# C10
pw = input("Passwort: ")
pin = input("PIN: ")
gesperrt = False
if pw == "tresor123" and pin.startswith("99") and not gesperrt: print("Tresor offen!")
else: print("Zugang verweigert!")

# C11: Bußgeldkatalog (orientiert an der Tabelle)
v = int(input("Überschreitung in km/h: "))
if v <= 10: bußgeld = 48.50
elif v <= 15: bußgeld = 68.50
elif v <= 20: bußgeld = 88.50
elif v <= 25: bußgeld = 128.50
elif v <= 30: bußgeld = 178.50
elif v <= 40: bußgeld = 228.50
elif v <= 50: bußgeld = 348.50
elif v <= 60: bußgeld = 508.50
elif v <= 70: bußgeld = 633.50
else: bußgeld = 738.50
print(f"Das Bußgeld beträgt: {bußgeld} €")



name = "Gandalf"
klasse = "Magier"
stufe = 4
mana = 20
lebenspunkte = 30
gold = 100
staerke = 14
schaden = 12

# ===== Sicherheitsnetz =====
print("\n*** Teile die Beute ***")
anzahl = int(input("An wie viele Leute wird das Gold (100) verteilt? "))

if anzahl > 0:
    print(f"Jeder bekommt {gold / anzahl} Gold.")
else:
    print("Durch 0 teilen? Netter Versuch. Du behältst das Gold einfach selbst.")

# ===== Klassen-Begrüßung =====
print("\n*** Die Gilde begrüßt dich ***")
if klasse.lower() == "magier":
    print(f"{name} murmelt: 'Abrakadabra... wo war nochmal mein Zauberstab?'")
elif klasse.lower() == "krieger":
    print(f"{name} brüllt: 'ICH HAUE ZUERST!'")
elif klasse.lower() == "schurke":
    print(f"{name} flüstert: 'Ich habe dein Gold nicht.'")
else:
    print(f"'{klasse}'? Die Gilde kennt das noch nicht, aber das Freibier gilt trotzdem!")

# ===== Titel nach Stufe =====
if stufe < 3:
    titel = "Novize"
elif stufe < 6:
    titel = "Abenteurer"
elif stufe < 10:
    titel = "Veteran"
else:
    titel = "Legende"
print(f"\nDer Torwächter ruft: 'Willkommen, {titel} {name}!'")

# ===== Zauber wirken =====
antwort = input(f"\nDu hast {mana} Mana. Feuerball wirken (kostet 15)? (ja/nein) ")
if (antwort.lower() == "ja" or antwort.lower() == "j") and mana >= 15:
    mana -= 15
    print(f"FEUERBALL! Du hast noch {mana} Mana.")
elif antwort.lower() in ["ja", "j"]:
    print("Zu wenig Mana. Der Goblin klatscht höflich.")
else:
    print("Strategisch zurückgehalten.")

# ===== Truhe mit Falle =====
truhenwurf = random.randint(1, 4)
if truhenwurf == 1:
    fallenschaden = random.randint(1, 6)
    lebenspunkte -= fallenschaden
    print(f"KLICK! Eine Pfeilfalle! Du verlierst {fallenschaden} Lebenspunkte.")
elif truhenwurf == 2:
    gold -= 5
    print("Ein Mimic! Du rennst weg und verlierst 5 Gold.")
else:
    fund = random.randint(5, 25)
    gold += fund
    print(f"Glitzer, glitzer! Du findest {fund} Gold.")

# ===== Angriffswurf =====
gegner_rk = random.randint(8, 18)
angriffswurf = random.randint(1, 20)
trefferwert = angriffswurf + (staerke // 2)

print(f"\nDu greifst einen Goblin an (RK {gegner_rk}). Wurf: {angriffswurf} + Bonus = {trefferwert}")

if angriffswurf == 20:
    print("KRITISCHER TREFFER!")
    print(f"Du machst {schaden * 2} Schaden.")
elif angriffswurf == 1:
    print("PATZER! Du stolperst über deinen Umhang.")
elif trefferwert >= gegner_rk:
    print(f"Treffer! Der Goblin verliert {schaden} Lebenspunkte.")
else:
    print("Daneben!")

# ===== Gesundheitszustand =====
if lebenspunkte > 50: 
    zustand = "strotzt vor Kraft"
elif lebenspunkte > 25: 
    zustand = "hat ein paar Kratzer"
else: 
    zustand = "sieht aus, als hätte ein Ork ihn als Kissen benutzt"

print(f"\nGesundheitszustand: {name} {zustand}.")