import time

# ============================================================
# MODULE
# ============================================================
#
# Ein Modul ist eine Sammlung von bereits fertigem Python-Code.
#
# Python bringt viele Module direkt mit. Dadurch müssen wir
# bestimmte Dinge nicht selbst programmieren.
#
# Mit "import" laden wir ein Modul:
#
#     import time
#
# Danach können wir Funktionen aus diesem Modul verwenden.
#
# Eine Funktion aus einem Modul wird normalerweise so
# aufgerufen:
#
#     modulname.funktion()
#
# In unserem Beispiel:
#
#     time.sleep()
#
# "time" ist das Modul.
# "sleep" ist eine Funktion aus diesem Modul.
#
# ------------------------------------------------------------
# time.sleep()
# ------------------------------------------------------------
#
# time.sleep() pausiert das Programm für eine bestimmte
# Anzahl von Sekunden.
#
# Beispiel:
#
#     time.sleep(2)
#
# Das Programm wartet 2 Sekunden.
#
# Wir können auch eine Variable verwenden:
#
#     pause = 0.5
#     time.sleep(pause)
#
# Dann wird die Dauer aus der Variable gelesen.
#
# ------------------------------------------------------------
# Weitere bekannte Module
# ------------------------------------------------------------
#
# Python besitzt sehr viele fertige Module.
#
# Beispiele:
#
#     import random
#     import math
#     import os
#     import datetime
#
# random
#     -> Zufallszahlen und Zufallsauswahl
#
# math
#     -> mathematische Funktionen
#
# os
#     -> Funktionen für das Betriebssystem
#
# datetime
#     -> Datum und Uhrzeit
#
# Wichtig:
#
# Ein Modul muss normalerweise zuerst importiert werden,
# bevor wir seine Funktionen verwenden können.
#
#
# ============================================================
# EINGEBAUTE FUNKTIONEN
# ============================================================
#
# Neben Funktionen aus Modulen besitzt Python auch viele
# Funktionen, die direkt eingebaut sind.
#
# Diese müssen wir nicht importieren.
#
# Beispiele:
#
#     print()
#     input()
#     len()
#     str()
#     int()
#     float()
#     list()
#     type()
#
# Wir können sie direkt verwenden.
#
# ------------------------------------------------------------
# print()
# ------------------------------------------------------------
#
# print() gibt etwas auf dem Bildschirm aus.
#
# Beispiel:
#
#     print("Hallo")
#
# Wir können auch Variablen ausgeben:
#
#     name = "Held"
#     print(name)
#
#
# ------------------------------------------------------------
# input()
# ------------------------------------------------------------
#
# input() wartet auf eine Eingabe des Benutzers.
#
# Beispiel:
#
#     name = input("Wie heißt du? ")
#
# Die Eingabe wird als String gespeichert.
#
# Selbst wenn jemand eine Zahl eingibt, liefert input()
# zunächst einen String zurück.
#
# Beispiel:
#
#     alter = input("Wie alt bist du? ")
#
# Wenn der Benutzer 25 eingibt, enthält "alter" den Text:
#
#     "25"
#
# und nicht automatisch die Zahl 25.
#
#
# ------------------------------------------------------------
# str()
# ------------------------------------------------------------
#
# str() wandelt einen Wert in einen String um.
#
# Beispiel:
#
#     zahl = 42
#     text = str(zahl)
#
# Danach enthält "text":
#
#     "42"
#
# Das ist beispielsweise praktisch, wenn Zahlen mit Text
# verbunden werden sollen.
#
#
# ------------------------------------------------------------
# int()
# ------------------------------------------------------------
#
# int() wandelt einen Wert in eine ganze Zahl um.
#
# Beispiel:
#
#     zahl = int("42")
#
# Ergebnis:
#
#     42
#
#
# ------------------------------------------------------------
# float()
# ------------------------------------------------------------
#
# float() wandelt einen Wert in eine Kommazahl um.
#
# Beispiel:
#
#     pause = float("0.5")
#
# Ergebnis:
#
#     0.5
#
# Genau das verwenden wir weiter unten bei unserer Eingabe.
#
#
# ============================================================
# STRING-FUNKTIONEN
# ============================================================
#
# Strings besitzen eigene Funktionen bzw. Methoden.
#
# Damit können wir Texte untersuchen und verändern.
#
# Beispiel:
#
#     text = "Dungeon"
#
# ------------------------------------------------------------
# .upper()
# ------------------------------------------------------------
#
# Wandelt alle Buchstaben in Großbuchstaben um.
#
#     text.upper()
#
# Ergebnis:
#
#     "DUNGEON"
#
#
# ------------------------------------------------------------
# .lower()
# ------------------------------------------------------------
#
# Wandelt alle Buchstaben in Kleinbuchstaben um.
#
#     text.lower()
#
# Ergebnis:
#
#     "dungeon"
#
#
# ------------------------------------------------------------
# .strip()
# ------------------------------------------------------------
#
# Entfernt Leerzeichen am Anfang und Ende eines Strings.
#
# Beispiel:
#
#     text = "   Dungeon   "
#     text.strip()
#
# Ergebnis:
#
#     "Dungeon"
#
#
# ------------------------------------------------------------
# .replace()
# ------------------------------------------------------------
#
# Ersetzt einen Teil eines Strings durch einen anderen Text.
#
# Beispiel:
#
#     text = "Der Dungeon ist leer."
#
#     text.replace("leer", "voll")
#
# Ergebnis:
#
#     "Der Dungeon ist voll."
#
#
# ------------------------------------------------------------
# .split()
# ------------------------------------------------------------
#
# Teilt einen String in mehrere Teile auf.
#
# Dabei entsteht eine Liste.
#
# Beispiel:
#
#     text = "Feuer Wasser Erde"
#     text.split()
#
# Ergebnis:
#
#     ["Feuer", "Wasser", "Erde"]
#
# Das ist eine wichtige Verbindung zwischen Strings und Listen:
#
# Aus einem String kann mit split() eine Liste entstehen.
#
#
# ============================================================
# LISTEN-FUNKTIONEN
# ============================================================
#
# Listen speichern mehrere Werte.
#
# Beispiel:
#
#     monster = ["Goblin", "Ork", "Drache"]
#
# Die einzelnen Werte können über ihren Index angesprochen
# werden.
#
# Wichtig:
#
# Der erste Eintrag hat immer den Index 0.
#
#     monster[0] -> "Goblin"
#     monster[1] -> "Ork"
#     monster[2] -> "Drache"
#
#
# ------------------------------------------------------------
# len()
# ------------------------------------------------------------
#
# len() gibt die Anzahl der Elemente zurück.
#
# Beispiel:
#
#     monster = ["Goblin", "Ork", "Drache"]
#
#     len(monster)
#
# Ergebnis:
#
#     3
#
# len() funktioniert auch mit Strings.
#
#     len("Dungeon")
#
# Ergebnis:
#
#     7
#
#
# ------------------------------------------------------------
# .append()
# ------------------------------------------------------------
#
# Fügt ein neues Element am Ende einer Liste hinzu.
#
# Beispiel:
#
#     monster = ["Goblin", "Ork"]
#
#     monster.append("Drache")
#
# Danach:
#
#     ["Goblin", "Ork", "Drache"]
#
#
# ------------------------------------------------------------
# .remove()
# ------------------------------------------------------------
#
# Entfernt ein bestimmtes Element aus einer Liste.
#
# Beispiel:
#
#     monster = ["Goblin", "Ork", "Drache"]
#
#     monster.remove("Ork")
#
# Danach:
#
#     ["Goblin", "Drache"]
#
#
# ------------------------------------------------------------
# .sort()
# ------------------------------------------------------------
#
# Sortiert die Elemente einer Liste.
#
# Beispiel:
#
#     monster = ["Drache", "Goblin", "Ork"]
#
#     monster.sort()
#
# Danach:
#
#     ["Drache", "Goblin", "Ork"]
#
# Die Sortierung erfolgt hier alphabetisch.
#
#
# ============================================================
# UNSER PROGRAMM
# ============================================================

pause = float(
    input("Wie dramatisch soll es werden? Pause in Sekunden (z.B. 0.5): ")
)

print("\nDer Dungeon erwacht...")

time.sleep(pause)

print("Etwas Großes rührt sich in der Dunkelheit...")

time.sleep(pause)

print("Wer wagt es einzutreten?\n")

time.sleep(pause)


# ============================================================
# KLEINE EXPERIMENTE
# ============================================================
#
# Die folgenden Beispiele kannst du ausprobieren.
#
# Sie verändern das eigentliche Dungeon-Programm noch nicht.
#
#
# ------------------------------------------------------------
# STRING
# ------------------------------------------------------------

wort = "Dungeon"

print(wort.upper())
print(wort.lower())
print(wort.replace("Dungeon", "Drache"))

print("Anzahl der Zeichen:", len(wort))


# ------------------------------------------------------------
# LISTE
# ------------------------------------------------------------

monster = ["Goblin", "Ork", "Drache"]

print(monster)

print("Erstes Monster:", monster[0])

print("Anzahl der Monster:", len(monster))

monster.append("Skelett")

print("Nach dem Hinzufügen:", monster)


# ------------------------------------------------------------
# STRING IN EINE LISTE UMWANDELN
# ------------------------------------------------------------

gegner = "Goblin Ork Drache"

gegner_liste = gegner.split()

print(gegner_liste)

print("Anzahl der Gegner:", len(gegner_liste))


# ============================================================
# MERKE
# ============================================================
#
# Es gibt verschiedene Arten von Funktionen:
#
# Eingebaute Python-Funktionen:
#
#     print()
#     input()
#     len()
#     str()
#     int()
#     float()
#
# Funktionen aus Modulen:
#
#     time.sleep()
#
# String-Methoden:
#
#     .upper()
#     .lower()
#     .strip()
#     .replace()
#     .split()
#
# Listen-Methoden:
#
#     .append()
#     .remove()
#     .sort()
#
# Besonders wichtig:
#
#     len()       -> Anzahl bestimmen
#     str()       -> in String umwandeln
#     int()       -> in ganze Zahl umwandeln
#     float()     -> in Kommazahl umwandeln
#     .split()    -> String in Liste aufteilen
#     .append()   -> Element zur Liste hinzufügen
#
# Eigene Funktionen mit "def" kommen später.
# ============================================================

# ============================================================
# DAS MODUL random
# ============================================================
#
# Mit dem Modul "random" können wir Zufallswerte erzeugen.
#
# Zum Beispiel können wir:
#
# - eine zufällige Zahl erzeugen
# - einen zufälligen Listeneintrag auswählen
# - zufällig zwischen verschiedenen Möglichkeiten wählen
#
# Das Modul gehört bereits zu Python.
# Wir müssen es aber zuerst importieren:
#
#     import random
#
# Danach können wir Funktionen aus dem Modul verwenden.
#
# Genau wie bei time:
#
#     time.sleep()
#
# verwenden wir bei random zum Beispiel:
#
#     random.randint()
#
# Das "random." bedeutet:
#
# "Verwende die Funktion aus dem Modul random."
#
#
# ------------------------------------------------------------
# random.randint()
# ------------------------------------------------------------
#
# randint() erzeugt eine zufällige ganze Zahl innerhalb
# eines bestimmten Bereichs.
#
# Beispiel:
#
#     random.randint(1, 6)
#
# erzeugt eine zufällige Zahl zwischen 1 und 6.
#
# Wichtig:
#
# Beide Grenzen gehören dazu.
#
# Möglich sind also:
#
#     1
#     2
#     3
#     4
#     5
#     6
#
# Genau deshalb eignet sich randint() beispielsweise für
# einen Würfel.
#
# Beispiel:
#
#     wurf = random.randint(1, 6)
#     print(wurf)
#
# Bei jedem neuen Programmdurchlauf kann eine andere Zahl
# herauskommen.
#
#
# ------------------------------------------------------------
# Zufälliges Element aus einer Liste
# ------------------------------------------------------------
#
# Mit random.choice() können wir zufällig ein Element aus
# einer Liste auswählen.
#
# Beispiel:
#
#     monster = ["Goblin", "Ork", "Drache"]
#
#     gegner = random.choice(monster)
#
# Python wählt dann zufällig eines dieser Elemente aus.
#
# Zum Beispiel:
#
#     Goblin
#
# oder:
#
#     Ork
#
# oder:
#
#     Drache
#
# Das ist besonders praktisch, wenn wir beispielsweise
# zufällige Gegner, Gegenstände oder Ereignisse auswählen
# möchten.
#
#
# ------------------------------------------------------------
# random.shuffle()
# ------------------------------------------------------------
#
# shuffle() mischt die Elemente einer Liste zufällig.
#
# Beispiel:
#
#     karten = ["Ass", "König", "Dame", "Bube"]
#
#     random.shuffle(karten)
#
# Danach könnte die Liste zum Beispiel so aussehen:
#
#     ["Dame", "Bube", "Ass", "König"]
#
# Bei einem erneuten Mischen kann eine andere Reihenfolge
# entstehen.
#
# Wichtig:
#
# shuffle() verändert die vorhandene Liste.
#
#
# ============================================================
# BEISPIEL: DUNGEON
# ============================================================

import random

monster = ["Goblin", "Ork", "Drache", "Skelett"]

gegner = random.choice(monster)

print("Ein Gegner erscheint:", gegner)


# ============================================================
# BEISPIEL: WÜRFEL
# ============================================================

wurf = random.randint(1, 6)

print("Du würfelst eine", wurf)


# ============================================================
# MERKE
# ============================================================
#
# Module können fertige Funktionen bereitstellen.
#
#     import time
#     time.sleep(2)
#
#     import random
#     random.randint(1, 6)
#
#
# time
#     -> arbeitet unter anderem mit Zeit
#
# random
#     -> erzeugt Zufallswerte
#
#
# Wichtige Funktionen aus random:
#
#     random.randint(1, 6)
#         -> zufällige ganze Zahl
#
#     random.choice(liste)
#         -> zufälliges Element aus einer Liste
#
#     random.shuffle(liste)
#         -> Liste zufällig mischen
#
# ------------------------------------------------------------
# Wichtig:
#
# random ist ein Modul.
# randint(), choice() und shuffle() sind Funktionen
# beziehungsweise Methoden, die wir über dieses Modul
# verwenden können.
#
# Eigene Funktionen mit "def" haben wir hier noch nicht.
# ============================================================