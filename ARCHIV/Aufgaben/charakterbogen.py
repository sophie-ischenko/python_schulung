"""
Basis: Ausgangscode (charakterbogen.py)

So ist die Datei aufgebaut:
  - Jede AUFGABE steht als Kommentar an der Stelle im Ausgangscode, an der sie gelöst wird.
  - Direkt darunter kommt dein Lösungscode
"""

print(r"""
   ____________________________
  |                            |
  |   D U N G E O N   D U E L  |
  |____________________________|
       ||                ||
       ||                ||
""")

# ===== Eingaben  =====
name = input("Name deines Helden oder deiner Heldin: ")
klasse = input("Klasse (z.B. Magier/in, Krieger/in): ")

# Frage nach der Stufe als int, damit wir später damit rechnen können
stufe = 

# ===== Attribute  =====

# Frage nach den drei Attributen als int, damit wir später damit rechnen können
staerke = 
geschick = 
intelligenz = 

# ===== Berechnungen =====

# Berechne die Lebenspunkte, Rüstungsklasse und Gold

# Lebenspunkte = Stufe + ein Bonus durch Stärke
lebenspunkte = 

# Rüstungsklasse = 10 + Bonus durch halbes Geschick (ganzzahlige Division)
ruestungsklasse = 

# Gold = stufe * 10 + ein Bonus durch Intelligenz
gold =                            

# Ausgabe der Werte, die wir bisher haben

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

# 2. Ausgabe: Stärke | Geschick | Intelligenz

# 3. Ausgabe: Lebenspunkte | Rüstungsklasse 

# 4. Ausgabe: Gold | Stufe
