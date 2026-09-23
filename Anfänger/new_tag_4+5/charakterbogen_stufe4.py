# charakterbogen_stufe4.py
# Lösung Stufe 4 – if / elif / else
# Basis: Lösung Stufe 3 + Aufgaben 15–21
# (Stellen, die ab Stufe 4 anders aussehen als vorher, sind mit "Stufe 4:" markiert)
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
if waffe < 1:   # Stufe 4: random.randint(1, waffe) würde sonst später abstürzen
    print("Mit bloßen Fäusten? Wir rechnen mit Waffenschaden 1.")
    waffe = 1
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
if verkauft in inventar:   # Stufe 4: remove() stürzt ab, wenn es den Gegenstand nicht gibt
    inventar.remove(verkauft)
    gold = gold + 12.75
    print(f"Der Händler nimmt '{verkauft}' und gibt dir 12.75 Gold. Ein Schnäppchen!")
else:
    print(f"Der Händler kneift die Augen zusammen: '{verkauft}'? Das hast du gar nicht! Kein Handel.")

# ===== Aufgabe 4: Gold teilen =====
gruppengroesse = int(input("\nWie viele Abenteurer teilen sich die Beute? "))
if gruppengroesse < 1:   # Stufe 4: Teilen durch 0 wäre ein ZeroDivisionError
    print("Ohne Gruppe sammelt der Drache das Gold ein. Wir rechnen mit 1.")
    gruppengroesse = 1
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

# ===== Stufe 4 / Aufgabe 16: Klassen-Begrüßung (if / elif / else) =====
print("\n*** Die Gilde begrüßt dich ***")
if klasse.lower() == "magier":      # .lower() macht alles klein: "MAGIER" und "Magier" zählen gleich
    print(r"""
      /\
     /* \
    /____\
    (o  o)
""")
    print(f"{name} murmelt: 'Abrakadabra... wo war nochmal mein Zauberstab?'")
elif klasse.lower() == "krieger":
    print(r"""
  ._________.
  |    |    |
  |----+----|
  |    |    |
   \   |   /
    \__|__/
""")
    print(f"{name} brüllt: 'ICH HAUE ZUERST, FRAGEN STELLE ICH NIE!'")
elif klasse.lower() == "schurke":
    print(r"""
    ______
   /  __  \
  |  (oo)  |   psst...
   \__||__/
""")
    print(f"{name} flüstert: 'Ich habe dein Gold nicht. Wirklich. Schau nicht in meine Taschen.'")
else:
    print(f"'{klasse}'? So etwas kennt die Gilde noch nicht... aber das Freibier gilt trotzdem!")

# ===== Aufgabe 17: Titel nach Stufe (elif-Kette) =====
if stufe < 3:
    titel = "Novize"
elif stufe < 6:
    titel = "Abenteurer"
elif stufe < 10:
    titel = "Veteran"
else:
    titel = "Legende"
print(f"\nDer Torwächter ruft: 'Willkommen, {titel} {name}!'")

# ===== Aufgabe 18: Zauber wirken (and / or / in) =====
antwort = input(f"\nDu hast {mana} Mana. Feuerball wirken (kostet 15)? (ja/nein) ")
if antwort.lower() in ["ja", "j"] and mana >= 15:      # beide Bedingungen müssen stimmen
    mana = mana - 15
    print(r"""
     ) (
    ( ) )
     ) ( (
   (_____)   FUMP!
""")
    print(f"FEUERBALL! Du hast noch {mana} Mana.")
elif antwort.lower() in ["ja", "j"]:
    print("Nur ein trauriges Fünkchen... zu wenig Mana. Der Goblin klatscht höflich.")
else:
    print("Du steckst den Zauberstab wieder ein. Feigling? Nein: strategisch.")

# ===== Aufgabe 19: Truhe mit Falle (random + if / elif / else) =====
print("\nDu öffnest noch eine Truhe...")
truhenwurf = random.randint(1, 4)
if truhenwurf == 1:
    fallenschaden = random.randint(1, 6)
    lebenspunkte = lebenspunkte - fallenschaden
    print(f"KLICK! Eine Pfeilfalle! Du verlierst {fallenschaden} Lebenspunkte.")
elif truhenwurf == 2:
    gold = gold - 5
    print("Die Truhe hat Zähne! Ein Mimic! Du rennst weg und verlierst 5 Gold.")
else:
    fund = random.randint(5, 25)
    gold = gold + fund
    print(f"Glitzer, glitzer! Du findest {fund} Gold.")

# ===== Aufgabe 20: Angriffswurf gegen Rüstungsklasse =====
gegner_rk = random.randint(8, 18)
angriffswurf = random.randint(1, 20)
trefferwert = angriffswurf + staerke // 2
print(f"\nDu greifst einen Goblin an (Rüstungsklasse {gegner_rk}). Wurf: {angriffswurf} + Bonus = {trefferwert}")
if angriffswurf == 20:
    print(r"""
   \ | /
  -- * --   KRITISCHER TREFFER!
   / | \
""")
    print(f"Doppelter Schaden: {schaden * 2}!")
elif angriffswurf == 1:
    print("PATZER! Du stolperst über deinen eigenen Umhang. Der Goblin klatscht.")
elif trefferwert >= gegner_rk:
    print(f"Treffer! Der Goblin verliert {schaden} Lebenspunkte.")
else:
    print("Daneben! Der Goblin streckt dir die Zunge raus.")

# ===== Bonus: Boss-Duell =====
input("\nENTER für das große Duell gegen den Drachen ...")
dein_wurf = random.randint(1, 20) + staerke // 2
drachen_wurf = random.randint(1, 20) + 5
print(f"Du: {dein_wurf}  |  Drache: {drachen_wurf}")
if dein_wurf > drachen_wurf:
    print("SIEG! Der Drache schenkt dir gerührt einen Keks.")
elif dein_wurf < drachen_wurf:
    print("Niederlage! Der Drache benutzt deinen Helm als Zahnstocher.")
else:
    print("Unentschieden! Ihr teilt euch den Keks und werdet Freunde.")

# ===== Aufgabe 21: Gesundheitszustand für den Abschluss =====
if lebenspunkte > 50:
    zustand = "strotzt vor Kraft"
elif lebenspunkte > 25:
    zustand = "ein paar Kratzer, nichts Schlimmes"
else:
    zustand = "sieht aus, als hätte ein Ork ihn als Kissen benutzt"

# ===== Aufgabe 14 + 21: Abschluss – der vollständige Charakterbogen =====
# (ersetzt die einfache Ausgabe aus dem Ausgangscode)
gold_pro_kopf = gold / len(gruppe)
print("\n" + "=" * 32)
print("        CHARAKTERBOGEN")
print("=" * 32)
print(f"Name: {name} | Klasse: {klasse} | Stufe: {stufe} ({titel})")
print(f"Stärke: {staerke} | Geschick: {geschick} | Intelligenz: {intelligenz}")
print(f"Lebenspunkte: {lebenspunkte} | Rüstungsklasse: {ruestungsklasse}")
print(f"Zustand: {name} {zustand}")
print(f"Schaden: {schaden} | Mana: {mana}")
print(f"\nGruppe ({len(gruppe)}): {', '.join(gruppe)}")     # ', '.join(liste) klebt die Namen zusammen
print(f"Inventar ({len(inventar)} Dinge): {inventar}")
print(f"Fähigkeiten: {faehigkeiten}")
print(f"\nWürfelstatistik {wuerfe}: Summe {sum(wuerfe)}, Max {max(wuerfe)}, Min {min(wuerfe)}, Ø {durchschnitt:.2f}")
print(f"Stärkster Treffer: {angriffe[-1]} | Schwächster Treffer: {angriffe[0]}")
print(f"\nGold: {gold:.2f} (pro Kopf: {gold_pro_kopf:.2f})")
print("=" * 32)
print(f"Typ von stufe: {type(stufe)}, von gold: {type(gold)}, von inventar: {type(inventar)}")
