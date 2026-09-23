"""
Tag 10 - Option 3: Der Cyber-Attacken-Simulator ("CyberGuard") - Loesung
===========================================================================
Enthaelt die Basisversion sowie Beispielumsetzungen der optionalen
Erweiterungen:
- Vierte Aktion "Backup einspielen" (einmalig pro Spiel, starke Integritaet)
- Schwierigkeitsgrad, der die Bedrohungssteigerung pro Runde beeinflusst
- Angriffs-Log, das alle gewaehlten Aktionen protokolliert
"""

import random

# --- Schritt 1: ASCII-Art-Vorlagen ---

SHIELD = """
     /\\
    /  \\
   /====\\
  /      \\
 [FIREWALL: AKTIV & SICHER]
"""

ATTACK = """
  [ALARM: ANGRIFF ERKANNT]
      !!!!!!!!!
      !! 404 !!
      !!!!!!!!!
"""

CRASH = """
  _____________________
 [   SYSTEM CRASHED    ]
 [      GAME OVER      ]
  ~~~~~~~~~~~~~~~~~~~~~
"""

# --- Schritt 2: Werte initialisieren ---

integrity = 100
threat_level = 10
patched_ports = []
backup_verfuegbar = True
angriffs_log = []


def main():
    global integrity, threat_level, patched_ports, backup_verfuegbar, angriffs_log

    print(SHIELD)
    print("CyberGuard Terminal gestartet. Schuetze die Server!")

    schwierigkeit = input("Schwierigkeitsgrad waehlen - [1] Leicht, [2] Normal, [3] Schwer: ")
    if schwierigkeit == "1":
        bedrohungs_spanne = (5, 15)
    elif schwierigkeit == "3":
        bedrohungs_spanne = (20, 35)
    else:
        bedrohungs_spanne = (10, 25)

    while integrity > 0 and threat_level < 100:
        print(f"\nFirewall-Integritaet: {integrity}% | Bedrohungslevel: {threat_level}%")
        print(f"Gepatchte Ports: {patched_ports}")
        print("[1] Port patchen")
        print("[2] IP-Sperre einrichten")
        print("[3] Log-Analyse (Bedrohung senken)")
        if backup_verfuegbar:
            print("[4] Backup einspielen (einmalig, +40 Integritaet)")

        wahl = input("Kommando: ")
        angriffs_log.append(wahl)

        if wahl == "1":
            port = input("Welchen Port patchen? (z.B. 80): ")
            patched_ports.append(port)
            integrity = integrity + 15
            print(f"Port {port} erfolgreich geschlossen.")

        elif wahl == "2":
            integrity = integrity + 20
            threat_level = threat_level - 10
            print("Boesartige IPs blockiert. Bedrohung sinkt.")

        elif wahl == "3":
            bedrohungs_senkung = random.randint(15, 30)
            threat_level = threat_level - bedrohungs_senkung
            print(f"Logs analysiert. Bedrohung um {bedrohungs_senkung}% gesenkt.")

        elif wahl == "4" and backup_verfuegbar:
            integrity = integrity + 40
            backup_verfuegbar = False
            print("Backup eingespielt! Integritaet stark erhoeht.")

        # Jede Runde erhoeht sich die Bedrohung und beschaedigt die Firewall
        threat_increase = random.randint(*bedrohungs_spanne)
        threat_level = threat_level + threat_increase
        integrity = integrity - random.randint(10, 20)

        print(ATTACK)
        print(f"Neuer Angriff verzeichnet! Bedrohung steigt um {threat_increase}%.")

        # Werte begrenzen
        threat_level = max(0, min(threat_level, 100))
        integrity = max(0, min(integrity, 100))

        if integrity <= 0:
            print(CRASH)
            print("Die Hacker haben die Server uebernommen!")
        elif threat_level >= 100:
            print("Sicherheitsnetz ueberlastet!")
        else:
            print("Bedrohung abgewehrt!")

    print(f"\nAngriffs-Log: {angriffs_log}")


if __name__ == "__main__":
    main()
