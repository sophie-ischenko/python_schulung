"""
Erweiterung 3: Kombiaufgaben und der Faktor Zufall (Datei4)

So ist die Datei aufgebaut:
  - Füge ganz oben den fertigen Ausgangscode aus Datei3 ein (denk daran: imports stehen IMMER ganz oben!).
  - Jede AUFGABE steht als Kommentar an der Stelle, an der sie gelöst wird.
  - Direkt darunter kommt dein Lösungscode.
  - Bei HIER entfernst du die Zeile und fügst deinen Lösungscode ein.
"""

import random    # Holt die "Werkzeugkiste" für den Zufall. Imports stehen immer ganz oben!
# random.seed(42)  # <- Einkommentieren: Dann würfelt jeder im Kurs exakt dieselben Zahlen!

"""
====================================================================
HIER KOMMT DER GESAMTE FERTIGE CODE AUS DATEI3 HIN
(Variablen, Listen, Slicing, Berechnungen etc.)
Achte darauf, dass du die Variable "waffe" (aus Aufgabe 1) hast!
====================================================================
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