"""
Tag 10 - Option 3: Der Cyber-Attacken-Simulator ("CyberGuard")
=================================================================
Musterloesung / Beispielumsetzung der "Ideen zum Weiterbauen":
- Vierte Aktion "Backup einspielen" (+40 Integritaet, nur einmal pro Spiel)
- Schwierigkeitsgrad zu Spielbeginn, der die Bedrohungssteigerung pro
  Runde beeinflusst
- Liste "angriffs_log", die jede Runde protokolliert und am Spielende
  komplett ausgegeben wird

ACHTUNG: Dieses Programm nutzt input(). Fuehre es am besten direkt als
Skript aus: python cyberguard_loesung.py
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

# --- Schritt 2: Das Code-Geruest, erweitert ---

integrity = 100
threat_level = 10
patched_ports = []
angriffs_log = []
backup_verfuegbar = True


def waehle_schwierigkeit():
    print("\nSchwierigkeitsgrad waehlen:")
    print("[1] Leicht (Bedrohung steigt langsamer)")
    print("[2] Normal")
    print("[3] Schwer (Bedrohung steigt schneller)")
    wahl = input("Grad: ")
    if wahl == "1":
        return (5, 15)
    elif wahl == "3":
        return (15, 35)
    return (10, 25)


def main():
    global integrity, threat_level, patched_ports, angriffs_log, backup_verfuegbar
    print(SHIELD)
    print("CyberGuard Terminal gestartet. Schuetze die Server!")

    threat_range = waehle_schwierigkeit()

    while integrity > 0 and threat_level < 100:
        print(f"\nFirewall-Integritaet: {integrity}% | Bedrohungslevel: {threat_level}%")
        print(f"Gepatchte Ports: {patched_ports}")
        print("[1] Port patchen")
        print("[2] IP-Sperre einrichten")
        print("[3] Log-Analyse (Bedrohung senken)")
        if backup_verfuegbar:
            print("[4] Backup einspielen (+40 Integritaet, einmalig)")

        wahl = input("Kommando: ")

        if wahl == "1":
            port = input("Welchen Port patchen? (z.B. 80): ")
            patched_ports.append(port)
            integrity = integrity + 15
            print(f"Port {port} erfolgreich geschlossen.")
            angriffs_log.append(f"Port {port} gepatcht")

        elif wahl == "2":
            integrity = integrity + 20
            threat_level = threat_level - 10
            print("Boesartige IPs blockiert. Bedrohung sinkt.")
            angriffs_log.append("IP-Sperre eingerichtet")

        elif wahl == "3":
            bedrohungs_senkung = random.randint(15, 30)
            threat_level = threat_level - bedrohungs_senkung
            print(f"Logs analysiert. Bedrohung um {bedrohungs_senkung}% gesenkt.")
            angriffs_log.append("Log-Analyse durchgefuehrt")

        elif wahl == "4" and backup_verfuegbar:
            integrity = integrity + 40
            backup_verfuegbar = False
            print("Backup erfolgreich eingespielt. +40 Integritaet.")
            angriffs_log.append("Backup eingespielt")

        else:
            angriffs_log.append("Keine gueltige Aktion gewaehlt")

        # Jede Runde erhoeht sich die Bedrohung und beschaedigt die Firewall
        threat_increase = random.randint(*threat_range)
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

    print("\n--- Angriffs-Log ---")
    for eintrag in angriffs_log:
        print(f"- {eintrag}")


if __name__ == "__main__":
    main()
