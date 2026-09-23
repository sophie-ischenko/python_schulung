"""
Python-Schulung – Tag 4: Lösungen
"""

# ============================================================
# BLOCK 1: Die Warm-up-Coding-Arena
# ============================================================

### Aufgabe 1: Bandbreiten-Kalkulator
bandbreite = float(input("Bandbreite einer Leitung (Mbit/s): "))
anzahl_leitungen = int(input("Anzahl Leitungen: "))
print(bandbreite * anzahl_leitungen)

### Aufgabe 2: Server-Laufzeitbericht
server_name = "SRV-FILE"
uptime_days = 124
status = "optimal"
print(f"Server {server_name} läuft seit {uptime_days} Tagen und hat den Status: {status}.")

### Aufgabe 3: Code-Sanierung (Syntax-Bug)
# Fehlerhaft:
# user = "Administrator
# print(f"Eingeloggt als: {user}"

# Korrektur:
user = "Administrator"
print(f"Eingeloggt als: {user}")

### Aufgabe 4: Eingabe-Absicherung (ValueError-Bug)
# Der Code stürzt bei "1.5" ab, weil int() keine Kommazahlen umwandeln kann.
# Korrektur: float() statt int() verwenden.
datenmenge_gb = float(input("Wie viel GB wurden übertragen? "))
mb_gesamt = datenmenge_gb * 1024
print(f"Das sind {mb_gesamt} MB.")

### Aufgabe 5: Token-Slicing
support_token = "DE-HR-89102"
laendercode = support_token[0:2]
abteilungscode = support_token[3:5]
print(laendercode)
print(abteilungscode)

### Aufgabe 6: Rückwärts-Slicing
protokoll = "retfaS_vrs"
print(protokoll[::-1])

### Aufgabe 7: E-Mail-Bereinigung
email_7 = " MAX.MUSTERMANN@FIRMA.DE "
print(email_7.strip().lower())

### Aufgabe 8: Protokoll-Prüfung
url_8 = input("URL eingeben: ")
print(url_8.startswith("https://"))

### Aufgabe 9: IP-Format-Korrektur
ip_9 = "192-168-1-100"
print(ip_9.replace("-", "."))

### Aufgabe 10: Log-Parser (Split)
log_zeile = "2026-03-04,ERROR,Datenbank-Timeout,Port-3306"
print(log_zeile.split(","))


# ============================================================
# BLOCK 4: Der große Listen-Praxis-Slam
# ============================================================

# ---------- Teil A: IT-Inventar & Daten sammeln ----------

### Aufgabe 1: Der Server-Fuhrpark
datenbanken = ["MySQL", "PostgreSQL", "Oracle"]
datenbanken.append("MongoDB")
print(datenbanken[0])
print(datenbanken)

### Aufgabe 2: Dynamische IP-Erfassung
ip_sammlung = []
ip_1 = input("1. IP-Adresse: ")
ip_sammlung.append(ip_1)
ip_2 = input("2. IP-Adresse: ")
ip_sammlung.append(ip_2)
ip_3 = input("3. IP-Adresse: ")
ip_sammlung.append(ip_3)
print(ip_sammlung)

### Aufgabe 3: Active Directory Gruppen-Bereinigung
admins = ["claudia", "stefan", "andreas", "markus"]
admins.append("julia")
admins.remove("stefan")
print(admins)

### Aufgabe 4: Backup-Größen korrigieren
backups = [12.5, 45.0, 1.2, 98.4]
backups[2] = 12.0
print(sum(backups))

# ---------- Teil B: ToDo-Listen & Warteschlangen ----------

### Aufgabe 5: Die tägliche ToDo-Liste
todos = ["Server patchen", "Backup prüfen", "Tickets sichten"]
todos.insert(0, "Firewall-Regel anpassen")
todos.remove("Backup prüfen")
print(todos)

### Aufgabe 6: Ticket-Warteschlange (First-In, First-Out)
queue = ["Ticket_A", "Ticket_B", "Ticket_C"]
bearbeitet = queue.pop(0)
print(f"Bearbeitet: {bearbeitet}")
print(f"Noch wartend: {queue}")

### Aufgabe 7: Die sortierte Hardware-Lieferung (Recherche)
lieferung = ["Monitor", "Maus", "Laptop", "Tastatur", "Headset"]
lieferung.sort()
print(lieferung)

### Aufgabe 8: Software-Deinstallations-Assistent
apps = ["Chrome", "Adobe Reader", "Teams", "VLC Player"]
zu_entfernen = input("Welche App soll deinstalliert werden? ")
if zu_entfernen in apps:
    apps.remove(zu_entfernen)
print(apps)
