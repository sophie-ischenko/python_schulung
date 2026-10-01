"""
Tag 9: Dungeon Duel - Mission im Drachenhort
=======================================================
[QUEST-LOG]: Du stehst vor deiner ersten echten Mission. Repariere 
deine Ausrüstung und schleiche dich in den Hort des Drachen.

Arbeitsweise:
- HILFSFUNKTIONEN berechnen nur Daten und geben sie per 'return' zurück (KEIN print!).
- MAIN-FUNKTIONEN übernehmen das Einlesen (input) und Ausgeben (print).
- Ersetze 'pass' durch deinen Code und hole dir den Schatz!
"""

# =====================================================================
# BLOCK 1: Das Rüstlager (Warm-Up)
# =====================================================================
# Überprüfe deine Werte, bevor du in die Dunkelheit hinabsteigst.

def berechne_ruestungsklasse(basis_rk, geschick):
    """
    Schritt 1: Der Rüstungsschmied
    In D&D ist deine Rüstungsklasse (RK) der Basiswert PLUS die Hälfte 
    deines Geschicks (ganzzahlige Division).
    Rechnung: basis_rk + (geschick // 2). Gib den Wert zurück.
    """
    # Deine Lösung hier
    pass


def ist_elfen_waffe(waffen_name):
    """
    Schritt 2: Der Antiquitäten-Händler
    Elfenwaffen sind besonders leicht. Sie sind am Namen erkennbar.
    Gib True zurück, wenn der waffen_name exakt mit "der Elfen" ENDET, 
    sonst False. (Tipp: Nutze waffen_name.endswith(...))
    """
    # Deine Lösung hier
    pass


def formatiere_kampfschrei(schrei):
    """
    Schritt 3: Der Herold
    Damit dich jeder hört: Schneide führende und nachfolgende Leerzeichen ab, 
    wandle alles in GROSSBUCHSTABEN um und hänge am Ende ein "!!!" an. 
    Gib den fertigen Schrei zurück. (Tipp: .strip() und .upper() verketten)
    """
    # Deine Lösung hier
    pass


# =====================================================================
# BLOCK 4: Der Dungeon-Abstieg (Modularer Programmier-Slam)
# =====================================================================
# Drei Stationen trennen dich vom Sieg. Jedes System hat 
# 1-2 Hilfsfunktionen (nur rechnen!) und eine main()-Funktion (Ein-/Ausgabe).

# --- SYSTEM 1: Der Angriffs-Simulator ---
# Du trainierst an einer Strohpuppe. Trifft dein Schlag?

def bewerte_angriff(wuerfel_wurf, gegner_rk):
    """
    Schritt 1: Hilfsfunktion
    - wuerfel_wurf == 20: Rückgabe "KRITISCHER TREFFER"
    - wuerfel_wurf < gegner_rk: Rückgabe "Fehlschlag"
    - Andernfalls (wenn Wurf >= RK): Rückgabe "Normaler Treffer"
    """
    # Deine Lösung hier
    pass

def erzeuge_kampf_meldung(status, waffe):
    """
    Schritt 2: Hilfsfunktion
    Ist der status "KRITISCHER TREFFER", gib zurück:
    "BÄÄM! Mit deiner Waffe <waffe> triffst du perfekt den Schwachpunkt!"
    Andernfalls gib zurück:
    "Angriff mit <waffe> -> Ergebnis: <status>."
    """
    # Deine Lösung hier
    pass

def main_kampf_simulator():
    """
    Schritt 3: Kontroll-Modul (main)
    - Frage per input() nach deiner "Waffe".
    - Frage per input() nach dem "Würfelwurf" (als int).
    - Frage per input() nach der "Gegner-Rüstungsklasse" (als int).
    - Rufe bewerte_angriff() auf und speichere das Ergebnis.
    - Rufe erzeuge_kampf_meldung() auf und speichere den Text.
    - Gib die finale Kampf-Meldung mit print() aus.
    """
    # Deine Lösung hier
    pass


# --- SYSTEM 2: Die Magieschmiede ---
# Du findest eine Schmiede im Dungeon und verstärkst deine Ausrüstung.

def generiere_schmiede_code(waffen_art, element):
    """
    Schritt 1: Hilfsfunktion
    Nimm die ersten 3 Buchstaben des Elements, setze ein "-" und hänge 
    die ersten 3 Buchstaben der Waffen-Art an. Alles in GROSSBUCHSTABEN!
    Gib das Ergebnis zurück.
    Beispiel: generiere_schmiede_code("Schwert", "Feuer") -> "FEU-SCH"
    Tipp: string[0:3] gibt dir die ersten 3 Buchstaben.
    """
    # Deine Lösung hier
    pass

def berechne_magieschaden(grundschaden, elementar_bonus):
    """
    Schritt 2: Hilfsfunktion
    Berechne den finalen Schaden: grundschaden + (elementar_bonus * 3).
    Gib den Wert zurück.
    """
    # Deine Lösung hier
    pass

def main_magieschmiede():
    """
    Schritt 3: Kontroll-Modul (main)
    - Frage Waffen-Art, Element, Grundschaden (int) und Bonus (int) ab.
    - Nutze die Hilfsfunktionen, um den Code und den finalen Schaden zu berechnen.
    - Gib per print() aus:
      "[SCHMIEDE-CODE: <code>] Verzauberung erfolgreich. 
       Deine Waffe macht nun <schaden> Schadenspunkte!"
    """
    # Deine Lösung hier
    pass


# --- SYSTEM 3: Der Drachenhort (Schleichen) ---
# Du stehst in der Schatzkammer. Vor dir schläft ein riesiger Drache.
# Mache bloß keinen Lärm!

def bewerte_schleichen(laerm_pegel):
    """
    Schritt 1: Hilfsfunktion
    - laerm_pegel <= 15: Rückgabe "Lautlos wie ein Schatten."
    - laerm_pegel <= 40: Rückgabe "Ein Stein kullert weg... Der Drache blinzelt."
    - Darüber: Rückgabe "SCHEPPER! ROOOAAR! Der Drache spuckt Feuer!"
    """
    # Deine Lösung hier
    pass

def main_drachen_hort():
    """
    Schritt 2: Kontroll-Modul (main) mit Schleife
    - Nutze eine while-Schleife (z.B. while True:).
    - Frage immer wieder nach deinem verursachten "Lärmpegel (0 bis 100): " (als int).
    - Wenn der Nutzer -1 eingibt (du hast dir das Amulett geschnappt und bist draußen), 
      beende die Schleife mit 'break' (und gib aus: "Schatz gesichert! Erfolgreich entkommen!").
    - Alle anderen Eingaben werden über bewerte_schleichen() geprüft und 
      sofort als Warnung des Spielleiters per print() ausgegeben.
    """
    # Deine Lösung hier
    pass


# =====================================================================
# EINSTIEGSPUNKT (Das eigentliche Main-Pattern)
# =====================================================================

if __name__ == "__main__":
    print(r"""
          (  )   (   )  )
           ) (   )  (  (
           ( )  (    ) )
           _____________
          <_____________>
          |             |
          |   HORT DES  |
          |   DRACHEN   |
          |_____________|
    """)
    print("Zieh dein Schwert und entzünde die Fackel...\n")
    
    # Entferne das '#' vor der Mission, die du gerade testen willst. 
    # Löse sie am besten nacheinander!

    # main_kampf_simulator()
    # main_magieschmiede()
    # main_drachen_hort()
    
    pass