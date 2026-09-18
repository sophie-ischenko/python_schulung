"""
Python-Schulung – Tag 4: Aufgaben
==================================
Trage deine Lösungen direkt unter der jeweiligen Aufgabe ein.
Führe die Datei aus und teste deine Eingaben.
"""

# ============================================================
# BLOCK 1: Die Warm-up-Coding-Arena
# ============================================================

# --- Aufgabe 1: Bandbreiten-Kalkulator ---
# Konzept: input(), float(), mathematische Operationen.
# Frage den Benutzer nach der Bandbreite einer einzelnen Leitung in Mbit/s
# (z. B. 45.5). Frage nach der Anzahl der Leitungen (Ganzzahl).
# Berechne die Gesamtbandbreite und gib sie aus.



# --- Aufgabe 2: Server-Laufzeitbericht ---
# Konzept: Variablenzuweisung und f-String.
# Erstelle Variablen für server_name = "SRV-FILE", uptime_days = 124 und
# status = "optimal". Gib diese Variablen in einem formatierten Satz aus.



# --- Aufgabe 3: Code-Sanierung (Syntax-Bug) ---
# Konzept: Fehlersuche (SyntaxError).
# Finde und behebe die syntaktischen Fehler im folgenden Code:
#
#   user = "Administrator
#   print(f"Eingeloggt als: {user}"
#
# Schreibe unten die korrigierte Version:



# --- Aufgabe 4: Eingabe-Absicherung (ValueError-Bug) ---
# Konzept: Fehlersuche (ValueError).
# Der folgende Code stürzt ab, wenn der Benutzer "1.5" eingibt. Warum?
# Behebe den Fehler.
#
#   datenmenge_gb = int(input("Wie viel GB wurden übertragen? "))
#   mb_gesamt = datenmenge_gb * 1024
#   print(f"Das sind {mb_gesamt} MB.")
#
# Schreibe unten die korrigierte Version:



# --- Aufgabe 5: Token-Slicing ---
# Konzept: String-Slicing mit festen Indizes.
# Gegeben ist das Support-Token "DE-HR-89102". Extrahiere das Länderkürzel
# ("DE") und das Abteilungskürzel ("HR") jeweils in eine eigene Variable
# und gib beide aus.



# --- Aufgabe 6: Rückwärts-Slicing ---
# Konzept: String rückwärts ausgeben.
# Ein defektes Übertragungsprotokoll liefert den fehlerhaften String
# "retfaS_vrs". Gib diesen String mithilfe von Slicing rückwärts aus,
# um den korrekten Servernamen zu lesen.



# --- Aufgabe 7: E-Mail-Bereinigung ---
# Konzept: String-Methoden .strip() und .lower().
# Ein Benutzer gibt beim Login seine E-Mail-Adresse mit zusätzlichen
# Leerzeichen und in Großbuchstaben ein: "  MAX.MUSTERMANN@FIRMA.DE  ".
# Bereinige den String, sodass er keine Leerzeichen mehr enthält und
# komplett in Kleinbuchstaben ausgegeben wird.



# --- Aufgabe 8: Protokoll-Prüfung ---
# Konzept: String-Methode .startswith().
# Frage den Benutzer nach einer URL. Prüfe mit einer String-Methode,
# ob die Eingabe mit "https://" beginnt. Gib das Ergebnis (True/False) aus.



# --- Aufgabe 9: IP-Format-Korrektur ---
# Konzept: String-Methode .replace().
# Ein veraltetes System liefert IP-Adressen mit Bindestrichen statt Punkten:
# "192-168-1-100". Ersetze alle Bindestriche durch Punkte.



# --- Aufgabe 10: Log-Parser (Split) ---
# Konzept: String-Methode .split().
# Eine Log-Zeile enthält durch Kommas getrennte Werte:
# "2026-03-04,ERROR,Datenbank-Timeout,Port-3306"
# Zerlege den String am Komma in eine Liste von Einzelwerten und gib sie aus.




# ============================================================
# BLOCK 4: Der große Listen-Praxis-Slam
# ============================================================

# ---------- Teil A: IT-Inventar & Daten sammeln ----------

# --- Aufgabe 1: Der Server-Fuhrpark ---
# Erstelle eine Liste namens datenbanken mit den Werten "MySQL",
# "PostgreSQL" und "Oracle".
# Füge am Ende "MongoDB" hinzu.
# Gib das erste Element der Liste sowie die gesamte Liste aus.



# --- Aufgabe 2: Dynamische IP-Erfassung ---
# Starte mit einer leeren Liste namens ip_sammlung = [].
# Frage den Benutzer nacheinander nach 3 IP-Adressen (input()) und füge
# jede der Liste hinzu. Gib die finale Liste aus.



# --- Aufgabe 3: Active Directory Gruppen-Bereinigung ---
# Gegeben ist: admins = ["claudia", "stefan", "andreas", "markus"]
# Füge "julia" der Liste hinzu.
# Entferne "stefan" aus der Liste. Gib die bereinigte Liste aus.



# --- Aufgabe 4: Backup-Größen korrigieren ---
# Gegeben ist: backups = [12.5, 45.0, 1.2, 98.4]
# Überschreibe den dritten Wert (1.2 GB) mit dem korrekten Wert 12.0 GB.
# Berechne die Summe aller Backups mit sum(backups) und gib sie aus.




# ---------- Teil B: ToDo-Listen & Warteschlangen ----------

# --- Aufgabe 5: Die tägliche ToDo-Liste ---
# Erstelle eine Liste todos mit den Aufgaben: "Server patchen",
# "Backup prüfen", "Tickets sichten".
# Schiebe eine dringende Aufgabe "Firewall-Regel anpassen" ganz vorne
# (Index 0) ein.
# Entferne die Aufgabe "Backup prüfen" aus der Liste und gib die
# verbleibende Liste aus.



# --- Aufgabe 6: Ticket-Warteschlange (First-In, First-Out) ---
# Gegeben ist eine Ticket-Schlange: queue = ["Ticket_A", "Ticket_B", "Ticket_C"]
# Lösche das älteste Ticket (Index 0) mit .pop() aus der Liste und
# speichere es in der Variablen bearbeitet.
# Gib aus, welches Ticket bearbeitet wurde und welche Tickets noch warten.



# --- Aufgabe 7: Die sortierte Hardware-Lieferung (Recherche) ---
# Gegeben ist: lieferung = ["Monitor", "Maus", "Laptop", "Tastatur", "Headset"]
# Recherchiere nach einer Listen-Methode, um diese Liste alphabetisch zu
# sortieren, wende sie an und gib die sortierte Liste aus.
# Tipp zur Recherche: python list sort alphabetically



# --- Aufgabe 8: Software-Deinstallations-Assistent ---
# Gegeben ist: apps = ["Chrome", "Adobe Reader", "Teams", "VLC Player"]
# Frage den Benutzer per input(), welche dieser Apps deinstalliert
# (entfernt) werden soll.
# Entferne die eingegebene App aus der Liste und gib die verbleibenden
# Apps aus.
