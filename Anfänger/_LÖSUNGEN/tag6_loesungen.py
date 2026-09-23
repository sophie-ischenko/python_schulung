"""
Python-Schulung – Tag 6: Lösungen
"""

# ============================================================
# BLOCK 1: Der große Listen-Recap
# ============================================================

### Aufgabe R1: Die Port-Erweiterung
offene_ports = [80, 443, 22]
offene_ports.append(8080)
print(len(offene_ports))

### Aufgabe R2: Hot-Spare-Server einsetzen
active_servers = ["SRV-01", "SRV-02", "SRV-03"]
active_servers[1] = "SRV-02-NEW"
print(active_servers)

### Aufgabe R3: Temperatur-Auswertung
temps = [21.5, 24.0, 19.8, 25.4, 22.1]
print(min(temps))
print(max(temps))

### Aufgabe R4: Session-Verwaltung (Löschen mit Rückgabe)
sessions = ["Session_A", "Session_B", "Session_C"]
geschlossene_session = sessions.pop()
print(f"Geschlossen: {geschlossene_session}")
print(f"Noch aktiv: {sessions}")

### Aufgabe R5: Inventar-Sortierung
inventar = ["Switch", "Router", "Firewall", "AccessPoint"]
inventar.sort(reverse=True)
print(inventar)

### Aufgabe R6: Sicherheits-Check (Mitgliedschaft)
blockierte_ips = ["192.168.1.50", "10.0.0.12"]
print("192.168.1.50" in blockierte_ips)


# ============================================================
# BLOCK 4: Der große Logik-Praxis-Slam
# ============================================================

# ---------- Kategorie A: Einfache Bedingungen ----------

### Aufgabe 1: Der Festplatten-Wächter
freier_speicher = int(input("Freier Speicher in %: "))
if freier_speicher < 15:
    print("Kritischer Speicherstand!")
else:
    print("Speicherplatz ausreichend.")

### Aufgabe 2: Passwort-Prüfer
korrektes_passwort = "admin123"
eingabe_pw = input("Passwort: ")
if eingabe_pw == korrektes_passwort:
    print("Zugriff gewährt")
else:
    print("Zugriff verweigert")

### Aufgabe 3: Port-Checker
port_3 = int(input("Portnummer: "))
if port_3 == 80 or port_3 == 443:
    print("Web-Traffic erlaubt")
else:
    print("Anderer Netzwerk-Port")

# ---------- Kategorie B: Mehrere Bedingungen (elif) ----------

### Aufgabe 4: Serverraum-Temperaturalarm
temperatur_4 = float(input("Serverraum-Temperatur: "))
if temperatur_4 > 25:
    print("Kritisch: Zu heiß!")
elif temperatur_4 < 18:
    print("Warnung: Zu kalt!")
else:
    print("Temperatur optimal.")

### Aufgabe 5: Ping-Latenz-Bewerter
latenz = int(input("Ping-Latenz in ms: "))
if latenz <= 30:
    print("Hervorragende Verbindung")
elif latenz <= 100:
    print("Normale Verbindung")
else:
    print("Starke Verzögerung")

### Aufgabe 6: Ticket-Priorisierung
ticket_alter = int(input("Alter des Tickets in Stunden: "))
if ticket_alter > 48:
    print("Priorität: Kritisch")
elif ticket_alter > 24:
    print("Priorität: Hoch")
else:
    print("Priorität: Standard")

# ---------- Kategorie C: Komplexe Logik mit Listen & logischen Operatoren ----------

### Aufgabe 7: Die IP-Firewall (Blacklist-Check)
blacklist = ["192.168.1.100", "10.0.0.5"]
eigene_ip = input("Deine IP-Adresse: ")
if eigene_ip in blacklist:
    print("Verbindung blockiert!")
else:
    print("Verbindung hergestellt.")

### Aufgabe 8: Login-System mit Notfall-Modus
wartungsmodus = True
benutzername_8 = input("Benutzername: ")
if wartungsmodus and benutzername_8 != "Admin":
    print("Systemwartung. Login nur für Admins.")
else:
    print("Login erfolgreich.")

### Aufgabe 9: VIP-Support-Entscheider
eilig = input("Ist das Ticket eilig? (ja/nein): ")
vip = input("Ist der Kunde ein VIP? (ja/nein): ")
if eilig == "ja" or vip == "ja":
    print("Sofortige Bearbeitung starten.")
else:
    print("Standard-Warteschlange.")

### Aufgabe 10: Multi-Faktor-Zugang (Herausforderung)
gesperrt = False
ip_10 = input("IP-Adresse: ")
passwort_10 = input("Passwort: ")
if passwort_10 == "geheim123" and ip_10.startswith("10.0.0.") and not gesperrt:
    print("Zugang gewährt.")
else:
    print("Zugang verweigert.")
