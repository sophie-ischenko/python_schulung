"""
Tag 9: Musterloesungen
========================
Schau hier erst rein, nachdem du es in 'tag9_aufgaben.py' selbst versucht hast!

ACHTUNG: Die drei Programm-Systeme aus Block 4 nutzen input(). Fuehre diese
Datei am besten direkt als Skript aus: python tag9_loesungen.py
Im if __name__ == "__main__"-Block unten kannst du auswaehlen, welches
Programm-System du testen willst.
"""

# =====================================================================
# BLOCK 1: Funktionsaufrufe festigen
# =====================================================================


def berechne_restspeicher(gesamt, belegt):
    return float(gesamt - belegt)


def ist_lokal(ip):
    return ip.startswith("192.168.")


def bereinige_dateiname(name):
    return name.strip().lower()


# =====================================================================
# BLOCK 4: Der modulare Programmier-Slam
# =====================================================================
# Hinweis: In einem eigenstaendigen Skript wuerde jede der drei
# main()-Funktionen unten schlicht main() heissen.


# --- Programm-System 1: Der Server-Raum-Monitor ---

def bewerte_temperatur(temp):
    if temp > 30:
        return "kritisch"
    return "normal"


def erzeuge_alarm_text(status, servername):
    if status == "kritisch":
        return f"[WARNUNG] Server {servername} ist ueberhitzt!"
    return f"[INFO] Server {servername} laeuft stabil."


def main_programmsystem_1():
    name = input("Servername: ")
    temp = float(input("Temperatur in °C: "))

    status = bewerte_temperatur(temp)
    meldung = erzeuge_alarm_text(status, name)
    print(meldung)


# --- Programm-System 2: Der Onboarding-Assistent fuer neue Mitarbeiter ---

def generiere_email(vorname, nachname):
    v = vorname.strip().lower()
    n = nachname.strip().lower()
    return f"{v}.{n}@firma.de"


def generiere_username(vorname, nachname):
    v_init = vorname.strip().lower()[0]
    n = nachname.strip().lower()
    return f"{v_init}{n}"


def main_programmsystem_2():
    print("--- Mitarbeiter Onboarding-Assistent ---")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")

    email = generiere_email(vorname, nachname)
    username = generiere_username(vorname, nachname)

    print("\nGenerierte AD-Kontodaten:")
    print(f"Windows-Login: {username}")
    print(f"E-Mail-Adresse: {email}")


# --- Programm-System 3: Der Ping-Latenz-Tester (mit Schleife) ---

def bewerte_latenz(ping):
    if ping <= 30:
        return "Hervorragend"
    elif ping <= 100:
        return "Akzeptabel"
    else:
        return "Kritisch"


def main_programmsystem_3():
    print("--- Latenz-Ueberwachungstool (Eingabe -1 zum Beenden) ---")
    while True:
        eingabe = int(input("Gemessene Latenz in ms: "))
        if eingabe == -1:
            print("Tool beendet.")
            break

        status = bewerte_latenz(eingabe)
        print(f"Latenz-Bewertung: {status}")


def _teste_block1():
    """Nicht-interaktiver Selbsttest fuer Block 1 (ohne input())."""
    frei = berechne_restspeicher(1000, 450.5)
    print(f"Freier Speicher: {frei} GB")
    print(ist_lokal("192.168.1.50"))
    print(bereinige_dateiname("  UPDATE_LOG.txt  "))


def _teste_block2():
    """Nicht-interaktiver Selbsttest fuer die Hilfsfunktionen aus Block 4."""
    print(bewerte_temperatur(35), erzeuge_alarm_text(bewerte_temperatur(35), "srv-01"))
    print(bewerte_temperatur(20), erzeuge_alarm_text(bewerte_temperatur(20), "srv-01"))
    print(generiere_email("  Max ", "MUSTERMANN"))
    print(generiere_username("  Max ", "MUSTERMANN"))
    print(bewerte_latenz(20), bewerte_latenz(80), bewerte_latenz(200))


if __name__ == "__main__":
    # Nicht-interaktive Selbsttests (Block 1 und die Hilfsfunktionen aus Block 4):
    _teste_block1()
    print()
    _teste_block2()

    # Zum interaktiven Testen eines kompletten Programm-Systems (mit input()),
    # kommentiere die gewuenschte Zeile ein:
    # main_programmsystem_1()
    # main_programmsystem_2()
    # main_programmsystem_3()
