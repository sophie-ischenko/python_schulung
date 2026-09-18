"""
Tag 8: Musterloesungen
=======================
Schau hier erst rein, nachdem du es in 'tag8_aufgaben.py' selbst versucht hast!
Jede Funktion/jedes Skript kann einzeln ausgefuehrt werden (siehe unten im
if __name__ == "__main__"-Block).
"""

# =====================================================================
# BLOCK 1: if/else oder while?
# =====================================================================


def aufgabe_e1_port_ueberwacher():
    """Entscheidung: if/else - wir pruefen den Port genau einmal."""
    port = 8080
    blacklist = [80, 8080, 22]
    if port in blacklist:
        print("Port blockiert!")


def aufgabe_e2_installations_assistent():
    """Entscheidung: while - der Status aendert sich schrittweise."""
    status = 0
    while status <= 100:
        print(f"Download: {status}%")
        status = status + 25


def aufgabe_e3_ip_verifizierer():
    """Entscheidung: if/else - die Pruefung findet einmal statt."""
    ip = "192.168.1.50"
    if ip.startswith("192.168."):
        print("Lokale IP-Adresse.")
    else:
        print("Externe IP-Adresse.")


def aufgabe_e4_eingabe_puffer():
    """Entscheidung: while (mit break) - Endlosschleife mit Ausstiegsbedingung."""
    while True:
        log = input("Log-Eintrag (oder 'stop'): ")
        if log == "stop":
            break
        print(f"Log gespeichert: {log}")


# =====================================================================
# BLOCK 4: Der grosse Funktions-Recycling-Slam
# =====================================================================


def erzeuge_email(vorname, nachname, domain):
    email = f"{vorname.lower()}.{nachname.lower()}@{domain.lower()}"
    return email


def berechne_brutto(netto, mwst=19):
    faktor = 1 + (mwst / 100)
    return netto * faktor


def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5 / 9
    return celsius


def check_temp(temp):
    if temp > 25:
        return "Zu heiss"
    elif temp < 18:
        return "Zu kalt"
    else:
        return "Optimal"


def pruefe_passwort(eingabe, korrekt):
    return eingabe == korrekt


def bewerte_ping(ping_ms):
    if ping_ms <= 30:
        return "Sehr gut"
    elif ping_ms <= 100:
        return "Normal"
    else:
        return "Schlecht"


def bestimme_prioritaet(stunden, ist_vip):
    if ist_vip:
        return "Kritisch"
    elif stunden > 24:
        return "Hoch"
    else:
        return "Standard"


def berechne_bandbreite(leitungen, mbit):
    return leitungen * mbit


def ist_blockiert(ip, blacklist):
    return ip in blacklist


def empfehle_ram(cores):
    if cores > 8:
        return "32 GB"
    else:
        return "16 GB"


def kalkuliere_preis(ram_gb, stueckzahl):
    preis_pro_gb = 4.50
    return ram_gb * preis_pro_gb * stueckzahl


def gb_to_mb(gb):
    return gb * 1024


if __name__ == "__main__":
    print("--- Block 1 ---")
    aufgabe_e1_port_ueberwacher()
    aufgabe_e3_ip_verifizierer()

    print("\n--- Block 4 ---")
    print(erzeuge_email("Max", "Mustermann", "firma.de"))
    print(berechne_brutto(100))       # 119.0
    print(berechne_brutto(100, 7))    # 107.0
    print(fahrenheit_to_celsius(100))
    print(check_temp(27))             # Zu heiss
    print(pruefe_passwort("admin", "admin123"))  # False
    print(bewerte_ping(120))          # Schlecht
    print(bestimme_prioritaet(5, True))   # Kritisch
    print(bestimme_prioritaet(5, False))  # Standard
    print(berechne_bandbreite(5, 50.0))
    print(ist_blockiert("10.0.0.1", ["10.0.0.1", "10.0.0.2"]))  # True
    print(empfehle_ram(16))           # 32 GB
    print(f"Kosten fuer 3 Server mit je 16 GB: {kalkuliere_preis(16, 3)} Euro")
    print(f"5 GB entsprechen {gb_to_mb(5)} MB")
