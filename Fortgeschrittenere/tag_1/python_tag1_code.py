"""
TAG 1 - DUNGEON DUEL
Code-Begleitdatei zum Notebook "Tag 1 - Der monolithische Kampf"

Enthaelt: Theorie-Beispiele, Uebungs-Starter (mit TODOs) und das fertige
Kampf-Grundgeruest. Diese Datei ist bewusst NICHT in Funktionen aufgeteilt -
das ist an Tag 1 so gewollt (siehe Notebook).
"""




# =============================================================
# 1.1 BEISPIEL: Variablen & Datentypen
# =============================================================

held_name = "Aria"          # str    - Text
held_hp = 100                # int    - Ganzzahl
kritische_chance = 0.15      # float  - Kommazahl
ist_betaeubt = False         # bool   - Wahrheitswert

print(type(held_name), type(held_hp), type(kritische_chance), type(ist_betaeubt))

# input() liefert IMMER einen String, auch bei Ziffern:
# eingabe = input("Waehle 1 oder 2: ")   # eingabe ist "1", nicht 1
# aktion = int(eingabe)                   # erst jetzt eine echte Zahl


# =============================================================
# UEBUNG 1: Der fehlerhafte Warenkorb (30 Min)
# Lernziel: Notwendigkeit der Typumwandlung selbst erfahren
# =============================================================

# produkt = input("Produktname: ")
# preis_pro_stueck = input("Preis pro Stueck: ")
# anzahl = input("Anzahl: ")
#
# TODO: preis_pro_stueck und anzahl in die richtigen Datentypen umwandeln
# TODO: Gesamtsumme berechnen (preis * anzahl) und in einem Satz ausgeben


# =============================================================
# 1.2 BEISPIEL: Vergleiche & if/elif/else
# =============================================================

def werte_angriff(wurf, ruestung):
    """
    Bewertet einen Angriffswurf gegen die Ruestung des Ziels.

    Parameter:
        wurf (int): simulierter Wuerfelwurf, 1-20
        ruestung (int): Ruestungswert des Ziels

    Rueckgabewert:
        str: "treffer", "patzer" oder "verfehlt"
    """
    if wurf == 1:
        return "patzer"
    elif wurf >= ruestung:
        return "treffer"
    else:
        return "verfehlt"


print(werte_angriff(14, 12))   # treffer
print(werte_angriff(1, 12))    # patzer
print(werte_angriff(5, 12))    # verfehlt


# =============================================================
# UEBUNG 2: Der strenge Tuersteher (40 Min)
# Lernziel: Logische Bedingungen und Verzweigungen kombinieren
# =============================================================

# alter = int(input("Dein Alter: "))
#
# TODO: unter 18       -> "Du kommst hier nicht rein!"
# TODO: 18, 19 oder 20 -> nach "Muttizettel" fragen (ja/nein), entsprechend reagieren
# TODO: ab 21          -> "Willkommen im Club, VIP!"


# =============================================================
# 1.3 BEISPIEL: while-Schleife
# =============================================================

monster_hp_beispiel = 50
runde_beispiel = 0

while monster_hp_beispiel > 0:
    runde_beispiel += 1
    monster_hp_beispiel -= 10   # Kurzschreibweise fuer monster_hp = monster_hp - 10

print(f"Besiegt nach {runde_beispiel} Runden")


# =============================================================
# UEBUNG 3: Der nervige Papagei (30 Min)
# Lernziel: Schleifen-Abbruchbedingungen verstehen
# =============================================================

# while True:
#     satz = input("Sag etwas zum Papagei: ")
#     TODO: Abbruch (break) bei exakt "Halt die Klappe"
#     TODO: sonst immer die gleiche Antwort ausgeben


# =============================================================
# 1.4 BEISPIEL: try/except
# =============================================================

while True:
    eingabe_demo = input("Aktion (1=Angriff, 2=Verteidigen): ")
    try:
        aktion_demo = int(eingabe_demo)
    except ValueError:
        print("Bitte nur 1 oder 2 eingeben!")
        continue   # springt zurueck an den Schleifenanfang
    break

print(f"Du waehlst Aktion {aktion_demo}")


# =============================================================
# UEBUNG 4: Der unzerstoerbare Taschenrechner (40 Min)
# Lernziel: Fehler abfangen, ohne den Programmfluss zu killen
# =============================================================

# while True:
#     a = input("Erste Zahl: ")
#     b = input("Zweite Zahl: ")
#     try:
#         ergebnis = int(a) / int(b)
#     except ValueError:
#         print("Bitte nur Zahlen eingeben!")
#         continue
#     TODO: eigenen except-Block fuer Division durch Null ergaenzen (ZeroDivisionError)
#     print(ergebnis)
#     break


