"""
Tag 8: Entscheidungs-Recap & Einfuehrung in Funktionen - Loesungen
"""

# =====================================================================
# BLOCK 1: if/else oder while?
# =====================================================================


def aufgabe_e1_port_ueberwacher():
    """Aufgabe E1: Der Port-Ueberwacher (einmalige Pruefung -> if)."""
    port = 8080
    blacklist = [80, 8080, 22]
    if port in blacklist:
        print("Port blockiert!")


def aufgabe_e2_installations_assistent():
    """Aufgabe E2: Der Installations-Assistent (Wiederholung bis 100% -> while)."""
    status = 0
    while status < 100:
        print(f"Installation: {status}%")
        status += 25
    print("Installation abgeschlossen.")


def aufgabe_e3_ip_verifizierer():
    """Aufgabe E3: IP-Adress-Verifizierer (einmalige Pruefung -> if/else)."""
    ip = "192.168.1.50"
    if ip.startswith("192.168."):
        print("Lokale IP-Adresse.")
    else:
        print("Externe IP-Adresse.")


def aufgabe_e4_eingabe_puffer():
    """Aufgabe E4: Der unendliche Eingabe-Puffer (Endlosschleife mit break)."""
    while True:
        log_nachricht = input("Log-Nachricht ('stop' zum Beenden): ")
        if log_nachricht == "stop":
            break
        print(f"Protokolliert: {log_nachricht}")


# =====================================================================
# BLOCK 4: Der grosse Funktions-Recycling-Slam
# =====================================================================


def erzeuge_email(vorname, nachname, domain):
    """Aufgabe F1: Der E-Mail-Generator"""
    return f"{vorname.lower()}.{nachname.lower()}@{domain}"


def berechne_brutto(netto, mwst=19):
    """Aufgabe F2: Der Netto-Brutto-Rechner"""
    return netto * (1 + mwst / 100)


def fahrenheit_to_celsius(f):
    """Aufgabe F3: Der Fahrenheit-Celsius-Konverter"""
    return (f - 32) * 5 / 9


def check_temp(temp):
    """Aufgabe F4: Serverraum-Waechter"""
    if temp > 25:
        return "Zu heiss"
    elif temp < 18:
        return "Zu kalt"
    else:
        return "Optimal"


def pruefe_passwort(eingabe, korrekt):
    """Aufgabe F5: Der Passwort-Pruefer"""
    return eingabe == korrekt


def bewerte_ping(ping_ms):
    """Aufgabe F6: Der Ping-Latenz-Bewerter"""
    if ping_ms <= 30:
        return "Sehr gut"
    elif ping_ms <= 100:
        return "Normal"
    else:
        return "Schlecht"


def bestimme_prioritaet(stunden, ist_vip):
    """Aufgabe F7: Ticket-Priorisierer"""
    if ist_vip:
        return "Kritisch"
    elif stunden > 24:
        return "Hoch"
    else:
        return "Standard"


def berechne_bandbreite(leitungen, mbit):
    """Aufgabe F8: Bandbreiten-Kalkulator"""
    return leitungen * mbit


def ist_blockiert(ip, blacklist):
    """Aufgabe F9: IP-Blacklist-Checker"""
    return ip in blacklist


def empfehle_ram(cores):
    """Aufgabe F10: RAM-Empfehlung"""
    if cores > 8:
        return "32 GB"
    else:
        return "16 GB"


def kalkuliere_preis(ram_gb, stueckzahl):
    """Aufgabe F11: Hardware-Preiskalkulator"""
    return ram_gb * 4.50 * stueckzahl


def gb_to_mb(gb):
    """Aufgabe F12: Speicher-Konverter"""
    return gb * 1024


if __name__ == "__main__":
    aufgabe_e1_port_ueberwacher()
    aufgabe_e2_installations_assistent()
    aufgabe_e3_ip_verifizierer()
    # aufgabe_e4_eingabe_puffer()  # benoetigt Konsoleneingabe, separat testen

    print(erzeuge_email("Max", "Mustermann", "firma.de"))
    print(berechne_brutto(1000))
    print(fahrenheit_to_celsius(98.6))
    print(check_temp(30))
    print(pruefe_passwort("geheim", "geheim"))
    print(bewerte_ping(45))
    print(bestimme_prioritaet(10, True))
    print(berechne_bandbreite(4, 100))
    print(ist_blockiert("10.0.0.5", ["10.0.0.5", "10.0.0.6"]))
    print(empfehle_ram(16))
    print(kalkuliere_preis(16, 2))
    print(gb_to_mb(2))
