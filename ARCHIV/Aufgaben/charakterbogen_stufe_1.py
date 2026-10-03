"""
Erweiterung 1: Erweiterung vom Ausgangscode (charakterbogen.py)

So ist die Datei aufgebaut:
  - Füge den fertigen Ausgangscode (charakterbogen.py) ein 
  - Jede AUFGABE steht als Kommentar an der Stelle im Ausgangscode, an der sie gelöst wird.
  - Direkt darunter kommt dein Lösungscode
  - bei HIER entfernst du die Zeile und fügst deinen Lösungscode ein
"""

import time

pause = float(input("Wie dramatisch soll es werden? Pause in Sekunden (z.B. 0.5): "))

print("\nDer Dungeon erwacht...")
time.sleep(pause)
print("Etwas Großes rührt sich in der Dunkelheit...")
time.sleep(pause)
print("Wer wagt es einzutreten?\n")
time.sleep(pause)


"""
hier kommt der Ausgangscode (charakterbogen.py) hin, den du schon fertig hast
"""

"""
Stufe 1: Variablen, Datentypen, Eingaben



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


# ===== Aufgabe 1: Schaden berechnen =====
# 1. Schaden berechnen. Frage die Waffenschaden-Zahl ab und 
# berechne schaden =  Summe aus Waffnschaden und halber Stärke 

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

# Aufgabe: String * int wiederholt den Text: je mehr Schaden, desto längeres AUAAAAAA
print("Der Goblin hinter dir schreit: AU" + "A" * schaden + "!")

# ===== Aufgabe 2: Manapunkte =====

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


# Aufgabe: Manapunkte. 
# Berechne mana = Dreifache der Intelligenz und gib sie aus.

# HIER

# Zeichne einen Manabalken aus "[~~~~~~]" * (mana geteilt durch 3)

# HIER

# Rechne aus, für wie viele Feuerbälle das reicht (Formel: mana // 5) 
# und wie viele Kerzen (mana // 2) man damit anzünden kann. Gib beides in einer Zeile aus.

# HIER

# ===== Aufgabe 3: Typ-Experiment =====

# Baue aus name + stufe die Ankündigung eines Herolds 
# -> Beispiel: „Hört, hört! Es naht Name, Stufe X!“

ankuendigung = 

print(r"""           /|
       =  =  =      / |
  ____| || || |____/  | -_-_-_-_-_-_
|)----| || || |____   |     
  ((  | || || |  ))\  | _-_-_-_-_-_-
   \\_|_||_||_|_//  \ |
    \___________/    \| 

""")

# Lass den Herold die Ankündigung ausrufen. Nutze dafür einen f-String. 
# Beginne mit "Der Herold verkündet: 'Hört, hört! Es ....

# HIER


print(r"""
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
""")

print("\n===== CHARAKTERBOGEN =====")

# 1. Ausgabe: Name | Klasse | Stufe
# pause

# HIER

# 2. Ausgabe: Stärke | Geschick | Intelligenz
# pause
# HIER

# 3. Ausgabe: Lebenspunkte | Rüstungsklasse 
# pause
# HIER

# 4. Ausgabe: Gold | Stufe
# pause
# HIER
