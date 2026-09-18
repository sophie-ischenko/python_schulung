# Python-Schulung – Tag 4: Lösungen

bandbreite = float(input("Bandbreite pro Leitung in Mbit/s: "))
leitungen = int(input("Anzahl der Leitungen: "))
print(bandbreite * leitungen)

server_name = "SRV-FILE"
uptime_days = 124
status = "optimal"
print(f"Server {server_name} läuft seit {uptime_days} Tagen. Status: {status}.")

user = "Administrator"
print(f"Eingeloggt als: {user}")

datenmenge_gb = float(input("Wie viel GB wurden übertragen? "))
print(f"Das sind {datenmenge_gb * 1024} MB.")

token = "DE-HR-89102"
print(token[:2])
print(token[3:5])

server = "retfaS_vrs"
print(server[::-1])

email = input("E-Mail-Adresse: ")
email = email.strip().lower()
print(email)

url = input("URL: ")
print(url.startswith("https://"))

ip = "192-168-1-100"
print(ip.replace("-", "."))

log = "2026-03-04,ERROR,Datenbank-Timeout,Port-3306"
print(log.split(","))

datenbanken = ["MySQL", "PostgreSQL", "Oracle"]
datenbanken.append("MongoDB")
print(datenbanken[0])
print(datenbanken)

ip_sammlung = []
ip_sammlung.append(input("IP-Adresse 1: "))
ip_sammlung.append(input("IP-Adresse 2: "))
ip_sammlung.append(input("IP-Adresse 3: "))
print(ip_sammlung)

admins = ["claudia", "stefan", "andreas", "markus"]
admins.append("julia")
admins.remove("stefan")
print(admins)

backups = [12.5, 45.0, 1.2, 98.4]
backups[2] = 12.0
print(sum(backups))

todos = ["Server patchen", "Backup prüfen", "Tickets sichten"]
todos.insert(0, "Firewall-Regel anpassen")
todos.remove("Backup prüfen")
print(todos)

queue = ["Ticket_A", "Ticket_B", "Ticket_C"]
bearbeitet = queue.pop(0)
print(f"Bearbeitet: {bearbeitet}")
print(f"Wartende Tickets: {queue}")

lieferung = ["Monitor", "Maus", "Laptop", "Tastatur", "Headset"]
lieferung.sort()
print(lieferung)

apps = ["Chrome", "Adobe Reader", "Teams", "VLC Player"]
app = input("Welche App soll deinstalliert werden? ")
apps.remove(app)
print(apps)
