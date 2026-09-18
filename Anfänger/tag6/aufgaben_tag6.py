"""
Python-Schulung – Tag 6: Aufgaben
==================================
Trage deine Lösungen direkt unter der jeweiligen Aufgabe ein.
Führe die Datei aus und teste deine Eingaben.
"""

# ============================================================
# BLOCK 1: Der große Listen-Recap
# ============================================================

# --- Aufgabe R1: Die Port-Erweiterung ---
# Erstelle eine Liste offene_ports mit den Werten 80, 443 und 22.
# Füge per Code den Port 8080 hinzu und gib die Anzahl der
# überwachten Ports aus.



# --- Aufgabe R2: Hot-Spare-Server einsetzen ---
# Gegeben ist: active_servers = ["SRV-01", "SRV-02", "SRV-03"]
# Ersetze den Server "SRV-02" (Index 1) direkt durch das neue Modell
# "SRV-02-NEW". Gib die aktualisierte Liste aus.



# --- Aufgabe R3: Temperatur-Auswertung ---
# Gegeben ist: temps = [21.5, 24.0, 19.8, 25.4, 22.1]
# Bestimme mithilfe von Python-Funktionen die minimale und die maximale
# Temperatur aus dieser Liste und gib beide Werte aus.



# --- Aufgabe R4: Session-Verwaltung (Löschen mit Rückgabe) ---
# Gegeben ist: sessions = ["Session_A", "Session_B", "Session_C"]
# Entferne die letzte Sitzung mit .pop() aus der Liste und speichere sie
# in einer Variablen geschlossene_session.
# Gib aus, welche Session geschlossen wurde und welche noch aktiv sind.



# --- Aufgabe R5: Inventar-Sortierung ---
# Sortiere die Liste inventar = ["Switch", "Router", "Firewall", "AccessPoint"]
# alphabetisch absteigend und gib sie aus.



# --- Aufgabe R6: Sicherheits-Check (Mitgliedschaft) ---
# Erstelle eine Liste blockierte_ips = ["192.168.1.50", "10.0.0.12"].
# Prüfe mit dem in-Operator, ob die IP "192.168.1.50" blockiert ist.
# Das Programm soll direkt True oder False ausgeben.




# ============================================================
# BLOCK 4: Der große Logik-Praxis-Slam
# ============================================================

# ---------- Kategorie A: Einfache Bedingungen (Vergleichsoperatoren) ----------

# --- Aufgabe 1: Der Festplatten-Wächter ---
# Frage den Benutzer nach dem freien Festplattenspeicher in Prozent
# (Ganzzahl). Wenn der Wert unter 15 liegt, gib aus:
# "Kritischer Speicherstand!". Andernfalls gib aus:
# "Speicherplatz ausreichend."



# --- Aufgabe 2: Passwort-Prüfer ---
# Definiere ein festes Passwort im Code: korrektes_passwort = "admin123".
# Frage den Benutzer nach dem Passwort. Wenn die Eingabe übereinstimmt,
# gib "Zugriff gewährt" aus, andernfalls "Zugriff verweigert".



# --- Aufgabe 3: Port-Checker ---
# Frage den Benutzer nach einer Portnummer (Ganzzahl). Wenn der Port
# 80 oder 443 ist, gib aus: "Web-Traffic erlaubt". Andernfalls gib aus:
# "Anderer Netzwerk-Port".




# ---------- Kategorie B: Mehrere Bedingungen (elif) ----------

# --- Aufgabe 4: Serverraum-Temperaturalarm ---
# Frage die Serverraum-Temperatur ab (Dezimalzahl).
#   Temperatur über 25 Grad: "Kritisch: Zu heiß!"
#   Temperatur unter 18 Grad: "Warnung: Zu kalt!"
#   Dazwischen (18 bis 25 Grad): "Temperatur optimal."



# --- Aufgabe 5: Ping-Latenz-Bewerter ---
# Frage die Ping-Latenz in Millisekunden ab (Ganzzahl).
#   Latenz kleiner gleich 30 ms: "Hervorragende Verbindung"
#   Latenz zwischen 31 und 100 ms: "Normale Verbindung"
#   Latenz über 100 ms: "Starke Verzögerung"



# --- Aufgabe 6: Ticket-Priorisierung ---
# Frage den Benutzer nach dem Alter eines Support-Tickets in Stunden.
#   Über 48 Stunden: "Priorität: Kritisch"
#   Über 24 Stunden: "Priorität: Hoch"
#   Alles darunter: "Priorität: Standard"




# ---------- Kategorie C: Komplexe Logik mit Listen & logischen Operatoren ----------

# --- Aufgabe 7: Die IP-Firewall (Blacklist-Check) ---
# Erstelle eine Liste blockierter IPs: blacklist = ["192.168.1.100", "10.0.0.5"]
#   - Frage den Benutzer nach seiner IP-Adresse.
#   - Prüfe, ob die eingegebene IP in der Blacklist steht.
#   - Wenn ja: "Verbindung blockiert!"
#   - Wenn nein: "Verbindung hergestellt."



# --- Aufgabe 8: Login-System mit Notfall-Modus ---
# Definiere wartungsmodus = True (Boolean). Frage den Benutzer nach
# seinem Benutzernamen.
#   - Wenn der Wartungsmodus aktiv ist (True) UND der Benutzername
#     ungleich "Admin" ist, gib aus: "Systemwartung. Login nur für Admins."
#   - Andernfalls gib aus: "Login erfolgreich."



# --- Aufgabe 9: VIP-Support-Entscheider ---
# Frage ab:
#   1. Ist das Ticket als "Eilig" eingestuft? (ja / nein)
#   2. Handelt es sich um einen VIP-Kunden? (ja / nein)
#
#   - Wenn das Ticket "Eilig" ist ODER der Kunde ein "VIP" ist, gib aus:
#     "Sofortige Bearbeitung starten."
#   - Andernfalls gib aus: "Standard-Warteschlange."



# --- Aufgabe 10: Multi-Faktor-Zugang (Herausforderung) ---
# Ein hochsicherer Server benötigt drei Bedingungen für den Zugang:
#   - Der Benutzer muss das Passwort "geheim123" kennen.
#   - Er muss eine IP aus dem erlaubten Subnetz "10.0.0.X" haben
#     (simuliere dies, indem du prüfst, ob die IP mit "10.0.0." beginnt).
#   - Das System darf nicht im Sperrmodus (gesperrt = True) sein.
#
# Schreibe ein Programm, das die IP und das Passwort abfragt und den
# Zugang nur erlaubt, wenn alle Bedingungen erfüllt sind.
