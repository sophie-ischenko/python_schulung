# Eingaben (str, int)
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

# Listen
inventar = ["Schwert", "Fackel", "Heiltrank"]
faehigkeiten = [klasse + "-Angriff", "Ausweichen"]

# Inventar erweitern
inventar.append(input("\nWas findest du in der Truhe? "))
inventar.insert(0, "Rucksack")

# Etwas verkaufen
verkauft = input("Was verkaufst du? ")
inventar.remove(verkauft)
gold = gold + 12.75

# Ausgabe
print("\n===== CHARAKTERBOGEN =====")
print(f"Name: {name} | Klasse: {klasse} | Stufe: {stufe}")
print(f"Stärke: {staerke} | Geschick: {geschick} | Intelligenz: {intelligenz}")
print(f"Lebenspunkte: {lebenspunkte} | Rüstungsklasse: {ruestungsklasse}")
print(f"Gold: {gold:.2f}")
print(f"Inventar ({len(inventar)} Dinge): {inventar}")
print(f"Fähigkeiten: {faehigkeiten}")
print(f"Typ von stufe: {type(stufe)}, von gold: {type(gold)}, von inventar: {type(inventar)}")

"""
Stufe 1: Variablen, Datentypen, Eingaben

1. Schaden berechnen. Frage die Waffenschaden-Zahl ab und 
berechne schaden = waffe + staerke
 
Interaktiv: Lass den Helden zuschlagen ( *WUMMS*) und den Goblin dahinter schreien, 
und zwar so, dass das Geschrei mit dem Schaden wächst: "AU" + "A" * schaden + "!". 
Dazu gehört ein ASCII-Schwert.

3. Manapunkte. Berechne mana = intelligenz * 3 und gib sie aus.
Interaktiv: Zeichne einen Manabalken aus "~" * ... und rechne aus, 
für wie viele Feuerbälle das reicht ( //).
Ein ASCII-Zauberhut macht sich gut.

3. Baue aus name + stufe die Ankündigung eines Herolds 
(„Hört, hört! Es naht Name, Stufe X!“)
Trompete ASCII

4. Gold teilen. Frage nach der Gruppengröße ( int) und berechne, 
wie viel Gold jeder bekommt. Vergleiche ehrliches teilen (/) und Zwergenteilung (//).
Bonus: Mit % bekommst du den Rest, der in der Tavernenkasse landet. 
Zeichne einen Goldsack.
"""

# Listen
inventar = ["Schwert", "Fackel", "Heiltrank"]
faehigkeiten = [klasse + "-Angriff", "Ausweichen"]


# ---------------------------------------------------------------
# AUFGABE Z2: Die Truhe, dramatisch
# Bevor der Held nach dem Fund gefragt wird, soll die Truhe in vier Zeilen
# aufgehen: Der Held schleicht hin, das Holz knarzt, etwas kratzt von innen,
# er reißt den Deckel auf. Zwischen den Zeilen läuft jeweils die Pause.
# Erst danach kommt die input()-Frage.
# ---------------------------------------------------------------
# LÖSUNG Z2:
print("\nDu schleichst zur Truhe...")
time.sleep(pause)
print("Das Holz knarzt.")
time.sleep(pause)
print("Etwas kratzt von innen am Deckel.")
time.sleep(pause)
print("Du reißt sie auf!")
time.sleep(pause)

# Inventar erweitern
inventar.append(input("Was findest du in der Truhe? "))
inventar.insert(0, "Rucksack")


# ---------------------------------------------------------------
# AUFGABE Z3: Der Händler prüft
# Nach der Frage, was verkauft wird, soll der Händler den Gegenstand in
# drei Zeilen begutachten (mit Pausen dazwischen). Danach nennt er den Preis
# von 12.75 Gold. Der Gegenstand steht dabei in der Ausgabe (f-String).
# ---------------------------------------------------------------
# Etwas verkaufen
verkauft = input("Was verkaufst du? ")

# LÖSUNG Z3:
print(f"\nDer Händler nimmt '{verkauft}' unter die Lupe...")
time.sleep(pause)
print("Er hält es gegen das Licht und beißt vorsichtig hinein.")
time.sleep(pause)
print("Es ist kein Käse. Er wirkt enttäuscht.")
time.sleep(pause)
print("Er murmelt: '12.75 Gold, und keinen Cent mehr!'")
time.sleep(pause)

inventar.remove(verkauft)
gold = gold + 12.75


# ---------------------------------------------------------------
# AUFGABE Z4: Countdown vor dem Charakterbogen
# Bevor der Bogen erscheint, soll ein Countdown laufen:
# "Das Schicksal wird enthüllt in...", dann 3..., 2..., 1... als einzelne
# Zeilen mit Pause dazwischen.
# ---------------------------------------------------------------
# LÖSUNG Z4:
print("\nDas Schicksal wird enthüllt in...")
time.sleep(pause)
print("3...")
time.sleep(pause)
print("2...")
time.sleep(pause)
print("1...")
time.sleep(pause)


# ---------------------------------------------------------------
# AUFGABE Z5: Der Charakterbogen, Zeile für Zeile
# Lass den Bogen nicht auf einmal erscheinen. Nach jeder Zeile der Ausgabe
# läuft die Pause. Experiment: Starte das Programm mit der Pause 0 und
# dann mit 2. Was ändert sich?
# ---------------------------------------------------------------
# LÖSUNG Z5:
# Ausgabe