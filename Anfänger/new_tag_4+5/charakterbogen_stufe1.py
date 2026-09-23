# charakterbogen_stufe1.py
# Lösung Stufe 1 – Variablen, Datentypen, Eingaben
# Basis: Ausgangscode (charakterbogen.py) + Aufgaben 1–4
#
# Tipp: ASCII-Art steht in r"""...""" (raw string), damit Backslashes \ nicht
# als Sonderzeichen interpretiert werden.


print(r"""
   ____________________________
  |                            |
  |   D U N G E O N   D U E L  |
  |____________________________|
       ||                ||
       ||                ||
""")

# ===== Ausgangscode: Eingaben (str, int) =====
name = input("Name deines Helden: ")
klasse = input("Klasse (z.B. Magier, Krieger): ")
stufe = int(input("Stufe: "))

# Attribute als int
staerke = int(input("Stärke: "))
geschick = int(input("Geschick: "))
intelligenz = int(input("Intelligenz: "))

# Berechnungen
lebenspunkte = 10 + stufe * 6 + staerke
ruestungsklasse = 10 + geschick // 2   # // = ganzzahlige Division
gold = 50.5                            # float

# ===== Aufgabe 1: Schaden berechnen =====
waffe = int(input("\nWie viel Schaden macht deine Waffe? "))
schaden = waffe + staerke // 2
print(r"""
      /\
      ||
      ||
      ||
   ___||___
      ||
      ()
""")

print(f"{name} schwingt die Waffe: *WUMMS* -> {schaden} Schaden!")
# String * int wiederholt den Text: je mehr Schaden, desto längeres AAAAAU
print("Der Goblin hinter dir schreit: AU" + "A" * schaden + "!")

# ===== Aufgabe 2: Manapunkte =====
mana = intelligenz * 3
print(r"""
      *
     /\
    /  \
   /* * \
  /______\
 ==========
   (o  o)
    \__/
""")
print(f"{name} hat {mana} Manapunkte.")
print("Manabalken: [" + "~" * (mana // 3) + "]")
print(f"Das reicht für {mana // 5} Feuerbälle oder {mana // 2} Mal Kerzen anzünden.")

# ===== Aufgabe 3: Typ-Experiment =====
# Zum Ausprobieren: Zeile einkommentieren, Programm starten, Fehlermeldung lesen:
# ankuendigung = name + stufe    # TypeError: can only concatenate str (not "int") to str
ankuendigung = name + ", Stufe " + str(stufe)   # str() macht aus der Zahl einen Text
print(r"""
   __________
  /__________\====<   TÖRÖÖÖÖÖ!
""")
print(f"Der Herold verkündet: 'Hört, hört! Es naht {ankuendigung}!'")

# ===== Ausgangscode: Listen =====
inventar = ["Schwert", "Fackel", "Heiltrank"]
faehigkeiten = [klasse + "-Angriff", "Ausweichen"]

# Inventar erweitern
inventar.append(input("\nWas findest du in der Truhe? "))
inventar.insert(0, "Rucksack")

# Etwas verkaufen
verkauft = input("Was verkaufst du? ")
inventar.remove(verkauft)
gold = gold + 12.75

# ===== Aufgabe 4: Gold teilen =====
gruppengroesse = int(input("\nWie viele Abenteurer teilen sich die Beute? "))
print(r"""
    _____
   (_____)
    /   \
   | $$$ |
    \___/
""")
print(f"Ehrlich geteilt (/):  {gold / gruppengroesse:.2f} Gold pro Kopf")
print(f"Zwergen-Teilung (//): {gold // gruppengroesse} Gold pro Kopf")   # float // int ergibt float
print(f"Der Rest (%):         {gold % gruppengroesse:.2f} Gold landen in der Tavernenkasse. Prost!")

# ===== Ausgangscode: Ausgabe (um Schaden und Mana ergänzt) =====
print("\n===== CHARAKTERBOGEN =====")
print(f"Name: {name} | Klasse: {klasse} | Stufe: {stufe}")
print(f"Stärke: {staerke} | Geschick: {geschick} | Intelligenz: {intelligenz}")
print(f"Lebenspunkte: {lebenspunkte} | Rüstungsklasse: {ruestungsklasse}")
print(f"Schaden: {schaden} | Mana: {mana}")
print(f"Gold: {gold:.2f}")
print(f"Inventar ({len(inventar)} Dinge): {inventar}")
print(f"Fähigkeiten: {faehigkeiten}")
print(f"Typ von stufe: {type(stufe)}, von gold: {type(gold)}, von inventar: {type(inventar)}")
