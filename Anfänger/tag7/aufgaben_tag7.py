"""
Python-Schulung – Tag 7: Aufgaben
==================================
Trage deine Lösungen direkt unter der jeweiligen Aufgabe ein.
Führe die Datei aus und teste deine Eingaben.
"""


# ---------- Kategorie A: Einfache Schleifen ----------

# --- Aufgabe 1: Der Pizza-Timer ---
# Schreibe ein Programm, das einen Countdown von 5 bis 1 ausgibt.
# Nach der 1 soll "Die Pizza ist fertig!" ausgegeben werden.



# --- Aufgabe 2: Die Spardose ---
# Simuliere eine Spardose. Starte bei 0 Euro.
# Erhöhe den Betrag in jedem Schleifendurchlauf um 20 Euro und gib aus:
# "Spardose: X Euro". Die Schleife endet bei 100 Euro.



# --- Aufgabe 3: Das Workout ---
# Ein Trainingsplan hat genau 4 Runden. Schreibe eine Schleife,
# die zählt und für jede Runde ausgibt: "Runde X: 10 Liegestütze geschafft!"




# ---------- Kategorie B: Schleifen mit break und continue ----------

# --- Aufgabe 4: Die Schatztruhe (3 Versuche) ---
# Der Spieler hat maximal 3 Versuche, das Zauberwort "sesam" einzugeben.
# Wenn er es richtig eingibt, bricht die Schleife mit break ab
# ("Die Truhe öffnet sich!"). Wenn er nach 3 Versuchen scheitert, gib
# "Die Truhe versiegelt sich für immer!" aus.



# --- Aufgabe 5: Der Postbote ---
# Ein Postbote liefert in der Straße die Hausnummern von 80 bis 86 aus.
# Er beliefert aber nur gerade Hausnummern. Verwende eine while-Schleife
# und continue, um nur die geraden Hausnummern auszugeben
# (Tipp: nutze % 2 == 0 zur Prüfung).



# --- Aufgabe 6: Der unendliche Papagei ---
# Schreibe eine Schleife, die den Benutzer immer wieder nach einer
# Eingabe fragt und diese wie ein Papagei wiederholt.
# Wenn der Benutzer "exit", "beenden" oder "tschüss" eingibt, soll sich
# das Programm mit einer Abschiedsmeldung beenden.




# ---------- Kategorie C: Komplexere Schleifen ----------

# --- Aufgabe 7: Das Badewasser ---
# Das Badewasser startet bei 20 Grad.
#   - In jedem Schleifendurchlauf fragt das Programm den Benutzer:
#     "Um wie viel Grad steigt die Temperatur? " (Dezimalzahl).
#   - Addiere diesen Wert zur Gesamttemperatur.
#   - Sobald die Temperatur 42 Grad überschreitet, brich die Schleife ab
#     und gib eine Warnmeldung aus: "ZU HEISS! Der Hahn wird zugedreht!"



# --- Aufgabe 8: Der Einkaufszettel ---
# Schreibe ein interaktives Programm mit einer leeren Liste
# einkaufszettel = [].
#   - Die Schleife fragt den Benutzer fortlaufend nach einer Aktion:
#     "w" (Artikel hinzufügen), "l" (Zettel anzeigen), "q" (beenden).
#   - Bei "w" wird der eingegebene Artikel der Liste hinzugefügt.
#   - Bei "l" wird die aktuelle Liste ausgegeben.
#   - Bei "q" bricht das Programm ab.