"""
Erweiterung 2: Listen, Methoden und noch mehr Dramatik (Datei3)

So ist die Datei aufgebaut:
  - Füge den fertigen Ausgangscode aus Datei2 hier ein.
  - Jede AUFGABE steht als Kommentar an der Stelle im Ausgangscode, an der sie gelöst wird.
  - Direkt darunter kommt dein Lösungscode.
  - Bei HIER entfernst du die Zeile und fügst deinen Lösungscode ein.
"""

"""
====================================================================
HIER KOMMT DER GESAMTE FERTIGE CODE AUS DATEI2 HIN
(Variablen, Berechnungen, Strings, Pausen, Schaden & Mana)
====================================================================
"""


# ===== Aufgabe: Listen erstellen =====
# Erstelle die Liste inventar mit den Werten "Schwert", "Fackel", "Heiltrank"
# HIER

# Erstelle die Liste faehigkeiten mit (klasse + "-Angriff") und "Ausweichen"
# HIER


# ---------------------------------------------------------------
# AUFGABE: Die Truhe, dramatisch
# Bevor der Held nach dem Fund gefragt wird, soll die Truhe in vier Zeilen
# aufgehen: Der Held schleicht hin, das Holz knarzt, etwas kratzt von innen,
# er reißt den Deckel auf. Zwischen den Zeilen läuft jeweils die Pause (time.sleep(pause)).
# Erst danach kommt die input()-Frage.
# ---------------------------------------------------------------

print(r"""
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|                               
""")

# HIER (Du schleichst zur Truhe...)
# HIER
# HIER (Das Holz knarzt.)
# HIER
# HIER (Etwas kratzt von innen am Deckel.)
# HIER
# HIER (Du reißt sie auf!)
# HIER

# Inventar erweitern:
# Frage den Spieler per input("Was findest du in der Truhe? ") und hänge es mit .append() an das Inventar an.
# HIER

# Füge danach "Rucksack" an Position 0 in das Inventar ein (mit .insert()).
# HIER


# ---------------------------------------------------------------
# AUFGABE: Der Händler prüft
# Nach der Frage, was verkauft wird, soll der Händler den Gegenstand in
# drei Zeilen begutachten (mit Pausen dazwischen). Danach nennt er den Preis
# von 12.75 Gold. Der Gegenstand steht dabei in der Ausgabe (f-String).
# ---------------------------------------------------------------
verkauft = input("\nWas verkaufst du? ")

# HIER (Der Händler nimmt '{verkauft}' unter die Lupe...)
# HIER
# HIER (Er hält es gegen das Licht und beißt vorsichtig hinein.)
# HIER
# HIER (Es ist kein Käse. Er wirkt enttäuscht.)
# HIER
# HIER (Er murmelt: '12.75 Gold, und keinen Cent mehr!')
# HIER

# Entferne den verkauften Gegenstand aus dem Inventar (.remove())
# HIER

# Erhöhe das Gold um 12.75
# HIER


# ===== Aufgabe 4: Gold teilen =====
gruppengroesse = int(input("\nWie viele Abenteurer teilen sich die Beute? "))
print(r"""
    _____
   (_____)
    /   \
   | $$$ |
    \___/
""")

# Gib das Gold ehrlich geteilt aus (/). Nutze einen f-String und runde auf 2 Nachkommastellen (:.2f)
# HIER

# Gib das Gold nach Zwergen-Teilung aus (//). 
# HIER

# Gib den Rest aus (%), der in der Tavernenkasse landet.
# HIER


# ===== Aufgabe 5: Gruppe =====
gefaehrte1 = input("\nWie heißt dein erster Gefährte? ")
gefaehrte2 = input("Und der zweite? ")

# Erstelle eine Liste namens 'gruppe' mit name, gefaehrte1 und gefaehrte2
# HIER

print(r"""
   o     o     o
  /|\   /|\   /|\
  / \   / \   / \
""")

# Gib mit einem f-String und len() aus, wie viele Mitglieder die Gruppe hat.
# HIER

# Gib mit einem f-String und dem Index [-1] aus, wer der Letzte in der Reihe ist.
# HIER


# ===== Aufgabe 6: Trank getrunken (pop) =====

# Entferne das letzte Element aus dem Inventar (.pop()) UND speichere es in der Variable 'letztes'.
# HIER

print(r"""
   _____
  `.___,'
   (___)
   <   >
    ) (
   /`-.\
  /     \
 / _    _\
:,' `-.' `:
|         |
:         ;
 \       /
  `.___.' 

""")

# Gib mit einem f-String aus: Du kramst im Rucksack, packst '{letztes}' und verschlingst es. *GLUCK GLUCK*
# HIER
# Gib aus, wie das restliche Inventar jetzt aussieht.
# HIER


# ===== Aufgabe 7: Sortiertes Inventar (sort, reverse) =====

# Sortiere das Inventar (A-Z) mit .sort()
# HIER
print("\nDer Ordnungs-Zwerg sortiert (A-Z):    ", inventar)

# Drehe die Reihenfolge des Inventars um (Z-A) mit .reverse()
# HIER
print("Der Chaos-Kobold dreht alles um (Z-A):", inventar)


print(r"""
    _/\_
   ( oo )   hihihi!
   /|__|\
""")

# ===== Aufgabe 8: Besitze ich das? (in) =====
suche = input("\nWonach wühlst du im Rucksack? ")

# Prüfe, ob 'suche' im 'inventar' ist (in). Speichere das Ergebnis (True/False) in der Variable 'gefunden'.
# HIER

print(f"Es raschelt und klimpert... Ist '{suche}' im Rucksack? -> {gefunden}")
print(f"(Datentyp des Ergebnisses: {type(gefunden)})")


# ===== Aufgabe 9: Beute-Ausschnitt (Slicing) =====
anzahl = int(input("\nWie viele Dinge passen an deinen Gürtel? "))

# Schneide die ersten 'anzahl' Elemente aus dem Inventar aus und speichere sie in 'guertel' ([0:anzahl])
# HIER

# Schneide die letzten zwei Elemente aus und speichere sie in 'boden' ([-2:])
# HIER

print("Griffbereit am Gürtel:      ", guertel)
print("Ganz unten im Rucksack:     ", boden)


# ===== Aufgabe 10: Ausrüstung tauschen (Hilfsvariable) =====

# Tausche das erste (Index 0) und das letzte Element (Index -1) im Inventar.
# Nutze dafür eine Hilfsvariable namens 'hilf'.
# HIER (hilf = ...)
# HIER (inventar[0] = ...)
# HIER (inventar[-1] = ...)

print(r"""
    _/\_
   ( oo )   hihihi!
   /|__|\
""")
print(f"Ein Taschendieb-Kobold hat '{inventar[0]}' und '{inventar[-1]}' vertauscht!")
print(f"Dein Inventar sieht jetzt so aus: {inventar}")


# ===== Aufgabe 11: Zwei Listen verbinden (+) =====
beute = [input("\nDer Drache lässt etwas fallen – was? "), input("Und noch etwas? ")]

# Verbinde das bisherige 'inventar' mit der Liste 'beute' durch ein +
# HIER

print(r"""
                __        _
              _/  \    _(\(o
             /     \  /  _  ^^^o
            /   !   \/  ! '!!!v'
           !  !  \ _' ( \____
           ! . \ _!\   \===^\)
            \ \_!  / __!
             \!   /    \
       (\_      _/   _\ )
        \ ^^--^^ __-^ /(__
         ^^----^^    "^--v
'""")
print(f"Du sammelst {beute} ein. Dein Rucksack quillt über: {len(inventar)} Dinge!")


# ---------------------------------------------------------------
# AUFGABE: Countdown vor dem Charakterbogen
# Bevor der Bogen erscheint, soll ein Countdown laufen:
# "Das Schicksal wird enthüllt in...", dann 3..., 2..., 1... als einzelne
# Zeilen mit Pause (time.sleep(pause)) dazwischen.
# ---------------------------------------------------------------

# HIER (Das Schicksal wird enthüllt in...)
# HIER
# HIER (3...)
# HIER
# HIER (2...)
# HIER
# HIER (1...)
# HIER


# ===== Finale Ausgabe =====
print(r"""
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
""")

# wie bisher

# Ergänze die Ausgabe des Charakterbogens um die neuen Listen und Variablen:

# 5. Ausgabe: Gruppe 
# 6. Ausgabe: Inventar
# 7. Ausgabe: Beute
