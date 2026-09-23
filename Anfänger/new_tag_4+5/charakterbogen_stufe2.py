# charakterbogen_stufe2.py
# Lösung Stufe 2 – Listen
# Basis: Lösung Stufe 1 + Aufgaben 5–11
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

# ===== Stufe 2 / Aufgabe 5: Gruppe =====
gefaehrte1 = input("\nWie heißt dein erster Gefährte? ")
gefaehrte2 = input("Und der zweite? ")
gruppe = [name, gefaehrte1, gefaehrte2]
print(r"""
   o     o     o
  /|\   /|\   /|\
  / \   / \   / \
""")
print(f"Eure Gruppe hat {len(gruppe)} Mitglieder.")
print(f"Der Letzte in der Reihe ist {gruppe[-1]} – und hat natürlich die Fackel vergessen!")

# ===== Aufgabe 6: Trank getrunken (pop) =====
letztes = inventar.pop()    # entfernt das letzte Element UND gibt es zurück
print(r"""
     _
    | |
   (   )
   |~~~|
   |___|
""")
print(f"Du kramst im Rucksack, packst '{letztes}' und verschlingst es. *GLUCK GLUCK*")
print(f"Geschmack: Drache mit einem Hauch von Socke. Übrig im Rucksack: {inventar}")

# ===== Aufgabe 7: Sortiertes Inventar (sort, reverse) =====
inventar.sort()      # Achtung: Großbuchstaben kommen vor Kleinbuchstaben!
print("\nDer Ordnungs-Zwerg sortiert (A-Z):    ", inventar)
inventar.reverse()
print("Der Chaos-Kobold dreht alles um (Z-A):", inventar)

# ===== Aufgabe 8: Besitze ich das? (in) =====
suche = input("\nWonach wühlst du im Rucksack? ")
gefunden = suche in inventar
print(f"Es raschelt und klimpert... Ist '{suche}' im Rucksack? -> {gefunden}")
print(f"(Datentyp des Ergebnisses: {type(gefunden)})")

# ===== Aufgabe 9: Beute-Ausschnitt (Slicing) =====
anzahl = int(input("\nWie viele Dinge passen an deinen Gürtel? "))
guertel = inventar[0:anzahl]
boden = inventar[-2:]
print("Griffbereit am Gürtel:      ", guertel)
print("Ganz unten im Rucksack:     ", boden)

# ===== Aufgabe 10: Ausrüstung tauschen (Hilfsvariable) =====
hilf = inventar[0]
inventar[0] = inventar[-1]
inventar[-1] = hilf
print(r"""
    _/\_
   ( oo )   hihihi!
   /|__|\
""")
print(f"Ein Taschendieb-Kobold hat '{inventar[0]}' und '{inventar[-1]}' vertauscht!")
print(f"Dein Inventar sieht jetzt so aus: {inventar}")

# ===== Aufgabe 11: Zwei Listen verbinden (+) =====
beute = [input("\nDer Drache lässt etwas fallen – was? "), input("Und noch etwas? ")]
inventar = inventar + beute
print(r"""
      /\    /\
     /  \__/  \    RAWR!
    ( o      o )
     \  ====  /
      \______/
""")
print(f"Du sammelst {beute} ein. Dein Rucksack quillt über: {len(inventar)} Dinge!")

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
