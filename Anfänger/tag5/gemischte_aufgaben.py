# --- Aufgabe 7: Leerzeichen entfernen (Recherche) ---
# Ein Benutzer hat fälschlicherweise Leerzeichen vor und nach seinem Namen
# eingegeben: "  admin_user  ". Bereinige den String.
# Tipp zur Recherche: python string remove spaces



# --- Aufgabe 8: Dateityp prüfen (Recherche) ---
# Finde eine String-Methode, mit der du prüfen kannst, ob ein Dateiname
# auf ".exe" endet.
# Tipp zur Recherche: python string check ends with



# --- Aufgabe 9: Zeichen ersetzen (Recherche) ---
# Ersetze in dem Pfad "C:/Benutzer/Desktop/Dokument" alle Slashes (/) durch
# Backslashes (\\).
# Tipp zur Recherche: python string replace character



# --- Aufgabe 10: Fehler-Zähler im Log (Recherche) ---
# Zähle, wie oft das Wort "[ERROR]" in diesem Log-String vorkommt:
# "[INFO] Start... [ERROR] DB weg... [ERROR] Abbruch..."
# Tipp zur Recherche: python string count occurrences



# --- Aufgabe 11: Nur Zahlen prüfen (Recherche) ---
# Prüfe, ob der String "12345" nur aus Ziffern besteht.
# Tipp zur Recherche: python string check if only digits



# --- Aufgabe 12: CSV-Zeile zerlegen (Recherche) ---
# Trenne den String "Max;Mustermann;IT-Support" am Semikolon auf, sodass
# eine Liste der einzelnen Werte entsteht.
# Tipp zur Recherche: python string split by character


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
