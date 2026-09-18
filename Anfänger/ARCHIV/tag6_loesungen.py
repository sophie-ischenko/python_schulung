# Python-Schulung – Tag 6: Lösungen

offene_ports = [80, 443, 22]
offene_ports.append(8080)
print(len(offene_ports))

active_servers = ["SRV-01", "SRV-02", "SRV-03"]
active_servers[1] = "SRV-02-NEW"
print(active_servers)

temps = [21.5, 24.0, 19.8, 25.4, 22.1]
print(min(temps))
print(max(temps))

sessions = ["Session_A", "Session_B", "Session_C"]
geschlossene_session = sessions.pop()
print(geschlossene_session)
print(sessions)

inventar = ["Switch", "Router", "Firewall", "AccessPoint"]
inventar.sort(reverse=True)
print(inventar)

blockierte_ips = ["192.168.1.50", "10.0.0.12"]
print("192.168.1.50" in blockierte_ips)

freier_speicher = int(input("Freier Speicher in Prozent: "))
if freier_speicher < 15:
    print("Kritischer Speicherstand!")
else:
    print("Speicherplatz ausreichend.")

korrektes_passwort = "admin123"
passwort = input("Passwort: ")
if passwort == korrektes_passwort:
    print("Zugriff gewährt")
else:
    print("Zugriff verweigert")

port = int(input("Portnummer: "))
if port == 80 or port == 443:
    print("Web-Traffic erlaubt")
else:
    print("Anderer Netzwerk-Port")

temperatur = float(input("Serverraum-Temperatur: "))
if temperatur > 25:
    print("Kritisch: Zu heiß!")
elif temperatur < 18:
    print("Warnung: Zu kalt!")
else:
    print("Temperatur optimal.")

latenz = int(input("Ping-Latenz in ms: "))
if latenz <= 30:
    print("Hervorragende Verbindung")
elif latenz <= 100:
    print("Normale Verbindung")
else:
    print("Starke Verzögerung")

ticket_alter = int(input("Ticketalter in Stunden: "))
if ticket_alter > 48:
    print("Priorität: Kritisch")
elif ticket_alter > 24:
    print("Priorität: Hoch")
else:
    print("Priorität: Standard")

blacklist = ["192.168.1.100", "10.0.0.5"]
ip = input("IP-Adresse: ")
if ip in blacklist:
    print("Verbindung blockiert!")
else:
    print("Verbindung hergestellt.")

wartungsmodus = True
benutzername = input("Benutzername: ")
if wartungsmodus and benutzername != "Admin":
    print("Systemwartung. Login nur für Admins.")
else:
    print("Login erfolgreich.")

eilig = input("Ist das Ticket Eilig? (ja/nein): ")
vip = input("Ist der Kunde VIP? (ja/nein): ")
if eilig == "ja" or vip == "ja":
    print("Sofortige Bearbeitung starten.")
else:
    print("Standard-Warteschlange.")

gesperrt = True
ip = input("IP-Adresse: ")
passwort = input("Passwort: ")
if passwort == "geheim123" and ip.startswith("10.0.0.") and not gesperrt:
    print("Zugang erlaubt.")
else:
    print("Zugang verweigert.")
