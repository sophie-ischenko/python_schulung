"""
Tag 9: Ausbruch im Dino-Park 
=======================================================
[SYSTEMWARNUNG]: Katastrophaler Systemausfall. Gehegezäune: OFFLINE.
Die Tiere haben ihre Zonen verlassen. Manuelle Neustarts erforderlich!

Arbeitsweise:
- HILFSFUNKTIONEN berechnen nur Daten und geben sie per 'return' zurück (KEIN print!).
- MAIN-FUNKTIONEN übernehmen das Einlesen (input) und Ausgeben (print).
- Ersetze 'pass' durch deinen Code und überlebe die Nacht.
"""

# =====================================================================
# BLOCK 1: Das Notfall-Labor (Warm-Up)
# =====================================================================
# Bevor wir fliehen, müssen wir die Forschung sichern und die Lage checken.

def berechne_rest_futter(fleisch_lager, rex_hunger):
    """
    Schritt 1: Der Fleisch-Bestand
    Berechne, wie viel Kilo Fleisch nach der Fütterung noch im Bunker sind.
    Rechnung: fleisch_lager minus rex_hunger. Gib den Wert zurück.
    """
    # Deine Lösung hier
    pass


def ist_dna_stabil(dna_sequenz):
    """
    Schritt 2: Der Gen-Scanner
    Ein Raptor-Embryo ist nur stabil, wenn die DNA-Sequenz exakt mit 
    "GATTACA" beginnt. Gib True zurück, falls ja, sonst False.
    Tipp: Nutze dna_sequenz.startswith(...)
    """
    # Deine Lösung hier
    pass


def repariere_fehlerlog(log_eintrag):
    """
    Schritt 3: Der Daten-Retter
    Das System hat den Log korrumpiert. Schneide führende und nachfolgende 
    Leerzeichen ab, wandle alles in GROSSBUCHSTABEN um und gib es zurück.
    (Tipp: .strip() und .upper() verketten)
    """
    # Deine Lösung hier
    pass


# =====================================================================
# BLOCK 4: Überlebens-Systeme (Modularer Programmier-Slam)
# =====================================================================
# Das Chaos bricht aus! Repariere die 3 Hauptsysteme.
# Jedes System hat 1-2 Hilfsfunktionen (nur rechnen!) und eine main()-Funktion.

# --- SYSTEM 1: Die Hochspannungszäune ---

def bewerte_zaun_spannung(volt):
    """
    Schritt 1: Hilfsfunktion
    - volt <= 1000: Rückgabe "LEBENSGEFAHR: Zaun ist gefallen!"
    - volt <= 5000: Rückgabe "Kritisch: Die Raptoren testen den Zaun."
    - Darüber: Rückgabe "Sicher: Spannung hält."
    """
    # Deine Lösung hier
    pass

def erzeuge_zaun_warnung(status, gehege_name):
    """
    Schritt 2: Hilfsfunktion
    Ist der status "LEBENSGEFAHR: Zaun ist gefallen!", gib zurück:
    "EVAKUIERUNG! Das Gehege <gehege_name> ist offen!"
    Andernfalls gib zurück:
    "Status für <gehege_name>: <status>"
    """
    # Deine Lösung hier
    pass

def main_sicherheitssystem():
    """
    Schritt 3: Kontroll-Modul (main)
    - Frage per input() nach dem "Namen des Geheges" (z.B. T-Rex Zone).
    - Frage per input() nach der "Aktuellen Spannung in Volt" (als int).
    - Rufe bewerte_zaun_spannung() auf und speichere das Ergebnis.
    - Rufe erzeuge_zaun_warnung() auf und speichere den Text.
    - Gib die finale Warnung mit print() aus.
    """
    # Deine Lösung hier
    pass


# --- SYSTEM 2: Die VIP-Helikopter-Evakuierung ---
# Die Parkbesitzer wollen fliehen. Registriere sie für den letzten Flug.

def generiere_rettungs_code(nachname, sektor):
    """
    Schritt 1: Hilfsfunktion
    Nimm die ersten 3 Buchstaben des Nachnamens, setze ein "_" und hänge 
    den Sektor in Kleinbuchstaben an. Gib das Ergebnis zurück.
    Beispiel: generiere_rettungs_code("Hammond", "Nord") -> "Ham_nord"
    Tipp: "Hallo"[0:3] gibt dir die ersten 3 Buchstaben.
    """
    # Deine Lösung hier
    pass

def berechne_flugzeit(entfernung_km, heli_kmh):
    """
    Schritt 2: Hilfsfunktion
    Berechne, wie viele Stunden der Helikopter für die Strecke braucht 
    (entfernung geteilt durch heli_kmh). Gib den Wert zurück.
    """
    # Deine Lösung hier
    pass

def main_evakuierung():
    """
    Schritt 3: Kontroll-Modul (main)
    - Frage Nachname, Sektor, Entfernung (int) und Heli-Speed (int) ab.
    - Nutze die Hilfsfunktionen, um den Code und die Zeit zu berechnen.
    - Gib per print() aus:
      "[HELI-START] Ticket <rettungs_code> bestätigt. 
       Flugzeit zur Küste: <zeit> Stunden. Guten Flug!"
    """
    # Deine Lösung hier
    pass


# --- SYSTEM 3: Die T-Rex Verfolgungsjagd im Jeep ---
# Du bist auf dem Weg zu den Docks. Plötzlich bebt der Boden. Er ist hinter dir!

def bewerte_trex_abstand(meter):
    """
    Schritt 1: Hilfsfunktion
    - meter <= 10: Rückgabe "OBJEKTE IM SPIEGEL SIND NÄHER ALS SIE ERSCHEINEN!"
    - meter <= 50: Rückgabe "Gas geben! Er holt auf!"
    - Darüber: Rückgabe "Abstand wächst. Weiter so!"
    """
    # Deine Lösung hier
    pass

def main_jeep_flucht():
    """
    Schritt 2: Kontroll-Modul (main) mit Schleife
    - Nutze eine while-Schleife (z.B. while True:).
    - Frage immer wieder nach dem "Abstand des T-Rex in Metern: " (als int).
    - Wenn der Nutzer -1 eingibt (du hast die Docks erreicht), 
      beende die Schleife mit 'break' (und gib aus "Boot erreicht! Wir sind in Sicherheit!").
    - Alle anderen Eingaben werden über bewerte_trex_abstand() geprüft und 
      sofort per print() ausgegeben.
    """
    # Deine Lösung hier
    pass


# =====================================================================
# EINSTIEGSPUNKT (Das eigentliche Main-Pattern)
# =====================================================================

if __name__ == "__main__":
    print(r"""
           __
          / _)
     _/\ / /     WILLKOMMEN
    |/ >/ /      IM DINO-PARK
      / / 
     /_/ 
    """)
    print("Der Regen peitscht gegen die Scheiben. Der Strom ist weg.\n")
    
    # Entferne das '#' vor dem Modul, das du gerade testen willst. 
    # Löse sie am besten nacheinander!

    # main_sicherheitssystem()
    # main_evakuierung()
    # main_jeep_flucht()
    
    pass