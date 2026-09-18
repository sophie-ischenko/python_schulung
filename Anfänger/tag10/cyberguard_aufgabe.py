"""
Tag 10 - Option 3: Der Cyber-Attacken-Simulator ("CyberGuard")
=================================================================
Dieses Geruest ist vollstaendig lauffaehig. Beachte die Spiellogik genau:
Jede Runde steigt die Bedrohung automatisch und die Firewall-Integritaet
sinkt automatisch (durch zwei random.randint()-Aufrufe ganz am Ende der
Schleife) - unabhaengig davon, welche Aktion du gewaehlt hast. Du kaempfst
also gegen die Zeit.

Deine Aufgabe fuer heute: Erweitere das Spiel nach eigenem Geschmack.
Ein paar Ideen (siehe auch 'cyberguard_loesung.py' fuer eine
Beispielumsetzung):
- TODO: Eine vierte Aktion "Backup einspielen", die die Integritaet stark
  erhoeht, aber nur einmal pro Spiel genutzt werden darf
- TODO: Ein Schwierigkeitsgrad, den du zu Beginn abfragst und der
  beeinflusst, wie stark die Bedrohung pro Runde steigt
- TODO: Eine Liste "angriffs_log", in der du jede Runde protokollierst,
  welche Aktion du gewaehlt hast, und die du am Ende des Spiels komplett
  ausgibst

ACHTUNG: Dieses Programm nutzt input(). Fuehre es am besten direkt als
Skript aus: python cyberguard_aufgabe.py
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

# --- Schritt 2: Das Code-Geruest (Starter-Kit) ---

integrity = 100
threat_level = 10
patched_ports = []


def main():
    global integrity, threat_level, patched_ports
    print(SHIELD)
    print("CyberGuard Terminal gestartet. Schuetze die Server!")

    while integrity > 0 and threat_level < 100:
        print(f"\nFirewall-Integritaet: {integrity}% | Bedrohungslevel: {threat_level}%")
        print(f"Gepatchte Ports: {patched_ports}")
        print("[1] Port patchen")
        print("[2] IP-Sperre einrichten")
        print("[3] Log-Analyse (Bedrohung senken)")

        wahl = input("Kommando: ")

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

        # Jede Runde erhoeht sich die Bedrohung und beschaedigt die Firewall
        threat_increase = random.randint(10, 25)
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


if __name__ == "__main__":
    main()
