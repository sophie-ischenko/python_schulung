"""
Tag 8: Entscheidungs-Recap & Einfuehrung in Funktionen
========================================================
Aufgaben zu Block 1 (if/else vs. while) und Block 4 (Funktions-Recycling-Slam).

Arbeitsweise:
- Lies dir die Theorie im Notebook 'tag8_theorie.ipynb' durch, bevor du hier startest.
- Schreibe deine Loesung jeweils direkt unter die Aufgabenstellung (ersetze 'pass'
  bzw. den Kommentar "# Deine Loesung hier").
- Teste jede Funktion/jedes Skript mit einem eigenen Aufruf, bevor du weitergehst.
- Vergleiche erst danach mit 'tag8_loesungen.py'.
"""

# =====================================================================
# BLOCK 1: if/else oder while? (09:00 - 09:45 Uhr)
# =====================================================================
# Ueberlege bei jeder Aufgabe zuerst: Passiert das nur EINMAL oder WIEDERHOLT
# sich etwas, bis sich ein Zustand aendert?


def aufgabe_e1_port_ueberwacher():
    """
    Aufgabe E1: Der Port-Ueberwacher

    Szenario: Ein Server-Port 8080 soll blockiert werden, wenn er auf der
    Blacklist steht. Die Blacklist lautet [80, 8080, 22]. Es soll eine
    einmalige Meldung ausgegeben werden ("Port blockiert!").
    """
    port = 8080
    blacklist = [80, 8080, 22]
    # Deine Loesung hier
    pass


def aufgabe_e2_installations_assistent():
    """
    Aufgabe E2: Der Installations-Assistent

    Szenario: Ein Download laeuft. Der Status startet bei 0% und steigt in
    jedem Schritt um 25%. Das Programm soll den Status so lange ausgeben,
    bis 100% erreicht sind.
    """
    status = 0
    # Deine Loesung hier
    pass


def aufgabe_e3_ip_verifizierer():
    """
    Aufgabe E3: IP-Adress-Verifizierer

    Szenario: Eine eingegebene IP-Adresse soll darauf geprueft werden, ob
    sie mit "192.168." beginnt. Gib "Lokale IP-Adresse." bzw.
    "Externe IP-Adresse." aus.
    """
    ip = "192.168.1.50"
    # Deine Loesung hier
    pass


def aufgabe_e4_eingabe_puffer():
    """
    Aufgabe E4: Der unendliche Eingabe-Puffer

    Szenario: Das Programm soll dich ununterbrochen nach einer Log-Nachricht
    fragen. Erst wenn du "stop" eingibst, soll das Programm enden.

    Tipp: Hier brauchst du eine Endlosschleife (while True:), die du mit
    break gezielt verlaesst.
    """
    # Deine Loesung hier
    pass


# =====================================================================
# BLOCK 4: Der grosse Funktions-Recycling-Slam (11:30 - 12:45 Uhr)
# =====================================================================
# Schreibe bekannte Aufgaben der letzten Tage als wiederverwendbare
# Funktionen um. Nutze 'return', sofern nicht ausdruecklich 'print'
# gefordert ist. Teste jede Funktion mit einem Aufruf.


def erzeuge_email(vorname, nachname, domain):
    """
    Aufgabe F1: Der E-Mail-Generator

    Verbinde Vorname, Nachname und Domain zu einer E-Mail-Adresse und
    gib sie per return zurueck (z. B. "max.mustermann@firma.de").
    """
    # Deine Loesung hier
    pass


def berechne_brutto(netto, mwst=19):
    """
    Aufgabe F2: Der Netto-Brutto-Rechner

    Berechne aus einem Nettobetrag und einem MwSt-Satz (Standard: 19)
    den Bruttobetrag und gib ihn zurueck.
    """
    # Deine Loesung hier
    pass


def fahrenheit_to_celsius(f):
    """
    Aufgabe F3: Der Fahrenheit-Celsius-Konverter

    Rechne eine Fahrenheit-Dezimalzahl in Celsius um und gib das
    Ergebnis zurueck.
    """
    # Deine Loesung hier
    pass


def check_temp(temp):
    """
    Aufgabe F4: Serverraum-Waechter

    Gib je nach Temperatur "Zu heiss" (> 25), "Zu kalt" (< 18) oder
    "Optimal" zurueck.
    """
    # Deine Loesung hier
    pass


def pruefe_passwort(eingabe, korrekt):
    """
    Aufgabe F5: Der Passwort-Pruefer

    Gib True zurueck, wenn beide Werte uebereinstimmen, sonst False.
    Tipp: Ein Vergleich mit == liefert bereits True/False.
    """
    # Deine Loesung hier
    pass


def bewerte_ping(ping_ms):
    """
    Aufgabe F6: Der Ping-Latenz-Bewerter

    Gib je nach Latenz "Sehr gut" (<= 30), "Normal" (<= 100) oder
    "Schlecht" zurueck.
    """
    # Deine Loesung hier
    pass


def bestimme_prioritaet(stunden, ist_vip):
    """
    Aufgabe F7: Ticket-Priorisierer

    Ist ist_vip True, ist die Prioritaet immer "Kritisch". Andernfalls:
    ueber 24 Stunden "Hoch", darunter "Standard".
    """
    # Deine Loesung hier
    pass


def berechne_bandbreite(leitungen, mbit):
    """
    Aufgabe F8: Bandbreiten-Kalkulator

    Berechne die Gesamtbandbreite (leitungen * mbit) und gib sie zurueck.
    """
    # Deine Loesung hier
    pass


def ist_blockiert(ip, blacklist):
    """
    Aufgabe F9: IP-Blacklist-Checker

    Gib True zurueck, wenn die IP in der uebergebenen Blacklist steht,
    sonst False.
    """
    # Deine Loesung hier
    pass


def empfehle_ram(cores):
    """
    Aufgabe F10: RAM-Empfehlung

    Liegen die CPU-Kerne ueber 8, gib "32 GB" zurueck, sonst "16 GB".
    """
    # Deine Loesung hier
    pass


def kalkuliere_preis(ram_gb, stueckzahl):
    """
    Aufgabe F11: Hardware-Preiskalkulator

    Ein GB RAM kostet pauschal 4.50 Euro. Berechne den Gesamtpreis fuer
    den Speicher (ram_gb * 4.50 * stueckzahl) und gib ihn zurueck.
    """
    # Deine Loesung hier
    pass


def gb_to_mb(gb):
    """
    Aufgabe F12: Speicher-Konverter

    Wandle den GB-Wert in Megabyte um (1 GB = 1024 MB) und gib das
    Ergebnis zurueck.
    """
    # Deine Loesung hier
    pass


if __name__ == "__main__":
    # Nutze diesen Bereich, um deine Funktionen waehrend der Bearbeitung
    # auszuprobieren, z. B.:
    # print(erzeuge_email("Max", "Mustermann", "firma.de"))
    aufgabe_e1_port_ueberwacher()
    aufgabe_e3_ip_verifizierer()
