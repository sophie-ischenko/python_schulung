# charakterbogen_stufe3.py
# Lösung Stufe 3 – Kombiaufgaben mit random
# Basis: Lösung Stufe 2 + Aufgaben 12–14
#
# Tipp: ASCII-Art steht in r"""...""" (raw string), damit Backslashes \ nicht
# als Sonderzeichen interpretiert werden.

import random    # holt die "Werkzeugkiste" random – Imports stehen immer ganz oben
# random.seed(42)  # <- Einkommentieren: Dann würfelt jeder im Kurs exakt dieselben Zahlen!


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

# ===== Stufe 3 / Aufgabe 12: Würfelwürfe (mit random) =====
# Die sechs Würfelseiten als Liste von ASCII-Bildern (Index 0 = Seite 1, ...)
wuerfel_bilder = [
    "+-------+\n|       |\n|   o   |\n|       |\n+-------+",
    "+-------+\n| o     |\n|       |\n|     o |\n+-------+",
    "+-------+\n| o     |\n|   o   |\n|     o |\n+-------+",
    "+-------+\n| o   o |\n|       |\n| o   o |\n+-------+",
    "+-------+\n| o   o |\n|   o   |\n| o   o |\n+-------+",
    "+-------+\n| o   o |\n| o   o |\n| o   o |\n+-------+",
]
wuerfel_sprueche = [
    "Der Würfel kullert unter den Tisch und kommt mit Staub im Haar zurück.",
    "Irgendwo lacht ein Gott der Zufälle.",
    "Die Katze schaut zu. Sie urteilt nicht. Sie urteilt doch.",
    "Der Spielleiter murmelt etwas von 'fairen Würfeln'.",
]

print("\n*** Die Würfel des Schicksals ***")

input("ENTER für Wurf 1 ...")
wurf1 = random.randint(1, 6)         # ganze Zahl von 1 bis 6 – beide Grenzen inklusive!
print(wuerfel_bilder[wurf1 - 1])     # -1, weil Listen bei 0 anfangen
print(f"Der Würfel rollt... und zeigt eine {wurf1}! {random.choice(wuerfel_sprueche)}")

input("ENTER für Wurf 2 ...")
wurf2 = random.randint(1, 6)
print(wuerfel_bilder[wurf2 - 1])
print(f"Der Würfel rollt... und zeigt eine {wurf2}! {random.choice(wuerfel_sprueche)}")

input("ENTER für Wurf 3 ...")
wurf3 = random.randint(1, 6)
print(wuerfel_bilder[wurf3 - 1])
print(f"Der Würfel rollt... und zeigt eine {wurf3}! {random.choice(wuerfel_sprueche)}")

wuerfe = [wurf1, wurf2, wurf3]
durchschnitt = sum(wuerfe) / len(wuerfe)
print(f"\nDeine Würfe: {wuerfe}")
print(f"Summe: {sum(wuerfe)} | Höchster: {max(wuerfe)} | Niedrigster: {min(wuerfe)} | Durchschnitt: {durchschnitt:.2f}")

# ===== Aufgabe 13: Angriffsserie =====
kampfrufe = [
    "Für Ruhm und Käse!",
    "Nimm DAS, du Pilz!",
    "Mein Schwert hat Hunger!",
    "Ich wollte eigentlich Bäcker werden!",
]
print("\n*** Angriffsserie ***")
# Achtung: random.randint(1, waffe) klappt nur, wenn waffe >= 1 ist (in Stufe 4 sichern wir das ab)
angriff1 = random.randint(1, waffe) + staerke // 2
print(f"{random.choice(kampfrufe)}  ->  {angriff1} Schaden")
angriff2 = random.randint(1, waffe) + staerke // 2
print(f"{random.choice(kampfrufe)}  ->  {angriff2} Schaden")
angriff3 = random.randint(1, waffe) + staerke // 2
print(f"{random.choice(kampfrufe)}  ->  {angriff3} Schaden")

angriffe = [angriff1, angriff2, angriff3]
angriffe.sort()      # aufsteigend: vorne der schwächste, hinten der stärkste Treffer
print(f"Stärkster Treffer: {angriffe[-1]} | Schwächster Treffer: {angriffe[0]}")

# ===== Aufgabe 14: Abschluss – der vollständige Charakterbogen =====
# (ersetzt die einfache Ausgabe aus dem Ausgangscode)
gold_pro_kopf = gold / len(gruppe)
print("\n" + "=" * 32)
print("        CHARAKTERBOGEN")
print("=" * 32)
print(f"Name: {name} | Klasse: {klasse} | Stufe: {stufe}")
print(f"Stärke: {staerke} | Geschick: {geschick} | Intelligenz: {intelligenz}")
print(f"Lebenspunkte: {lebenspunkte} | Rüstungsklasse: {ruestungsklasse}")
print(f"Schaden: {schaden} | Mana: {mana}")
print(f"\nGruppe ({len(gruppe)}): {', '.join(gruppe)}")     # ', '.join(liste) klebt die Namen zusammen
print(f"Inventar ({len(inventar)} Dinge): {inventar}")
print(f"Fähigkeiten: {faehigkeiten}")
print(f"\nWürfelstatistik {wuerfe}: Summe {sum(wuerfe)}, Max {max(wuerfe)}, Min {min(wuerfe)}, Ø {durchschnitt:.2f}")
print(f"Stärkster Treffer: {angriffe[-1]} | Schwächster Treffer: {angriffe[0]}")
print(f"\nGold: {gold:.2f} (pro Kopf: {gold_pro_kopf:.2f})")
print("=" * 32)
print(f"Typ von stufe: {type(stufe)}, von gold: {type(gold)}, von inventar: {type(inventar)}")
