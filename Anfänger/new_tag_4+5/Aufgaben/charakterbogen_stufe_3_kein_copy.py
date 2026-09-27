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

"""
Erweiterung 3: Kombiaufgaben und der Faktor Zufall (Datei4)

So ist die Datei aufgebaut:
  - Jede AUFGABE steht als Kommentar an der Stelle, an der sie gelöst wird.
  - Direkt darunter kommt dein Lösungscode.
"""


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

# Lass den Nutzer für Wurf 1 ENTER drücken (nutze input() ohne die Eingabe zu speichern)
# HIER (input("ENTER für Wurf 1 ..."))

# Würfle eine zufällige Zahl von 1 bis 6 (random.randint) und speichere sie in 'wurf1'
# HIER

# Gib das passende Würfelbild aus der Liste wuerfel_bilder aus. 
# Achtung: Listen beginnen bei 0! Du musst also (wurf1 - 1) als Index nutzen.
# HIER

# Gib mit einem f-String aus: "Der Würfel rollt... und zeigt eine {wurf1}! {zufälliger Spruch aus wuerfel_sprueche}"
# Nutze random.choice(), um einen zufälligen Spruch auszuwählen.
# HIER


# Kurze Frage an dich selbst:
# Wieso wird der input() Befehl hier genutzt, obwohl wir die Eingabe gar nicht speichern?
# Deine Antwort:
#
ä

# Wiederhole das Ganze für Wurf 2
# HIER (input...)
# HIER (wurf2 = ...)
# HIER (print Bild...)
# HIER (print Spruch...)


# Wiederhole das Ganze für Wurf 3
# HIER (input...)
# HIER (wurf3 = ...)
# HIER (print Bild...)
# HIER (print Spruch...)


# Speichere die drei Würfe in einer Liste namens 'wuerfe'
# HIER

# Berechne den Durchschnitt: Summe der Würfe ( sum() ) geteilt durch die Anzahl der Würfe ( len() )
# HIER (durchschnitt = ...)

# Gib deine Würfe (die Liste) aus
# HIER

# Gib in einem f-String die Summe, den höchsten, den niedrigsten und den Durchschnitt aus.
# HIER


# ===== Aufgabe 13: Angriffsserie =====
kampfrufe = [
    "Für Ruhm und Käse!",
    "Nimm DAS, du Pilz!",
    "Mein Schwert hat Hunger!",
    "Ich wollte eigentlich Bäcker werden!",
]
print("\n*** Angriffsserie ***")

# Berechne angriff1: Eine zufällige Zahl zwischen 1 und 'waffe' + (staerke // 2)
# HIER

# Gib einen zufälligen Kampfruf (random.choice) und den berechneten Schaden aus
# HIER (print(f"{...} -> {angriff1} Schaden"))

# Berechne angriff2 auf dieselbe Weise und gib ihn samt Kampfruf aus
# HIER
# HIER

# Berechne angriff3 auf dieselbe Weise und gib ihn samt Kampfruf aus
# HIER
# HIER

# Speichere die drei Angriffe in einer Liste namens 'angriffe'
# HIER

# Sortiere die Liste 'angriffe' (aufsteigend: der schwächste Treffer steht dann auf Index 0, der stärkste auf -1)
# HIER

# Gib den stärksten Treffer (letztes Element) und den schwächsten Treffer (erstes Element) mit einem f-String aus.
# HIER


# ===== Aufgabe 14: Abschluss – der vollständige Charakterbogen =====
# (Dies ersetzt die einfache Ausgabe ganz am Ende deines bisherigen Codes)
print(r"""
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
""")

print("\n===== CHARAKTERBOGEN =====")
# Berechne gold_pro_kopf: gold geteilt durch die Anzahl der Gruppenmitglieder
# HIER

# Drucke den Kopfteil des Bogens (32-mal "=" über und unter "CHARAKTERBOGEN")
# HIER (print("\n" + "=" * 32))
# HIER (print("        CHARAKTERBOGEN"))
# HIER (print("=" * 32))

# Gib Name, Klasse und Stufe in einer Zeile aus
# HIER

# Gib Stärke, Geschick und Intelligenz in einer Zeile aus
# HIER

# Gib Lebenspunkte und Rüstungsklasse aus
# HIER

# Gib Schaden und Mana aus
# HIER

# Gib die Gruppe aus. Nutze ', '.join(gruppe), um die Namen mit Kommas hübsch zu verbinden!
# HIER (print(f"\nGruppe ({len(gruppe)}): {', '.join(gruppe)}"))

# Gib das Inventar samt Anzahl der Dinge aus
# HIER

# Gib die Fähigkeiten aus
# HIER

# Gib die Würfelstatistik aus (wuerfe Liste, Summe, Max, Min, Durchschnitt gerundet)
# HIER

# Gib den stärksten und schwächsten Treffer der Angriffsserie aus
# HIER

# Gib das Gold und das Gold pro Kopf aus (beides auf 2 Nachkommastellen gerundet)
# HIER

# Drucke die Abschluss-Linie ("=" * 32)
# HIER

# Gib zum Abschluss die Datentypen von stufe, gold und inventar aus (mit type())
# HIER