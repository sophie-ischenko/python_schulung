"""
Tag 9: Fortgeschrittene Funktionen & Das Main-Pattern - Loesungen
"""

# =====================================================================
# BLOCK 1: Funktionsaufrufe festigen
# =====================================================================


def berechne_restspeicher(gesamt, belegt):
    """Aufgabe W1: Der Speicher-Minderer"""
    return float(gesamt - belegt)


def ist_lokal(ip):
    """Aufgabe W2: Der IP-Pruefer"""
    return ip.startswith("192.168.")


def bereinige_dateiname(name):
    """Aufgabe W3: Dateiname-Normalisierer"""
    return name.strip().lower()


# =====================================================================
# BLOCK 4: Der modulare Programmier-Slam
# =====================================================================

# --- Programm-System 1: Der Server-Raum-Monitor ---


def bewerte_temperatur(temp):
    if temp > 30:
        return "kritisch"
    else:
        return "normal"


def erzeuge_alarm_text(status, servername):
    if status == "kritisch":
        return f"[WARNUNG] Server {servername} ist ueberhitzt!"
    else:
        return f"[INFO] Server {servername} laeuft stabil."


def main_programmsystem_1():
    servername = input("Servername: ")
    temperatur = float(input("Temperatur: "))
    status = bewerte_temperatur(temperatur)
    meldung = erzeuge_alarm_text(status, servername)
    print(meldung)


# --- Programm-System 2: Der Onboarding-Assistent fuer neue Mitarbeiter ---


def generiere_email(vorname, nachname):
    vorname_clean = vorname.strip().lower()
    nachname_clean = nachname.strip().lower()
    return f"{vorname_clean}.{nachname_clean}@firma.de"


def generiere_username(vorname, nachname):
    vorname_clean = vorname.strip().lower()
    nachname_clean = nachname.strip().lower()
    return f"{vorname_clean[0]}{nachname_clean}"


def main_programmsystem_2():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    email = generiere_email(vorname, nachname)
    username = generiere_username(vorname, nachname)
    print("--- Onboarding-Bericht ---")
    print(f"E-Mail: {email}")
    print(f"Benutzername: {username}")


# --- Programm-System 3: Der Ping-Latenz-Tester (mit Schleife) ---


def bewerte_latenz(ping):
    if ping <= 30:
        return "Hervorragend"
    elif ping <= 100:
        return "Akzeptabel"
    else:
        return "Kritisch"


def main_programmsystem_3():
    while True:
        eingabe = int(input("Ping-Latenz in ms (-1 zum Beenden): "))
        if eingabe == -1:
            break
        print(bewerte_latenz(eingabe))


if __name__ == "__main__":
    # Waehle waehrend der Bearbeitung aus, welches Programm-System du
    # gerade testen willst, indem du die passende Zeile einkommentierst:

    main_programmsystem_1()
    # main_programmsystem_2()
    # main_programmsystem_3()
