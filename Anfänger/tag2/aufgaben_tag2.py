"""
Python-Schulung – Tag 2: Aufgaben
==================================
Trage deine Lösungen direkt unter der jeweiligen Aufgabe ein.
Führe die Datei aus und teste deine Eingaben.
"""

# ============================================================
# BLOCK 1: Wiederholung von Tag 1
# ============================================================

# --- Aufgabe W1: System-Statusbericht (Datentypen zuweisen) ---
# Ziel: Variablen korrekt anlegen und ausgeben.
# Erstelle folgende Variablen mit passenden Datentypen für ein IT-System:
#   hostname:            Name des Servers (Text)
#   cpu_cores:           Anzahl der CPU-Kerne (Ganzzahl)
#   speicherauslastung:  Aktuelle RAM-Belegung in Prozent (Nachkommazahl)
#   datenbank_laeuft:    Status der Datenbank (Wahrheitswert)
# Gib die Werte zeilenweise mit print() aus.



# --- Aufgabe W2: Die manuelle Preisberechnung ---
# Ziel: Mathematische Grundoperationen mit festen Variablen.
# Eine Software-Lizenz kostet netto 120 Euro.
#   - Erstelle eine Variable netto_preis mit dem Wert 120.
#   - Erstelle eine Variable steuersatz mit dem Wert 0.19.
#   - Berechne den Steuerbetrag und den Bruttopreis in separaten Variablen.
#   - Gib beide Ergebnisse aus.



# --- Aufgabe W3: Steckbrief-Formatierung (f-String) ---
# Ziel: Variablen in Text einbetten.
# Erstelle die Variablen mitarbeiter_name, personalnummer und rolle.
# Gib diese in einem einzigen, lesbaren Satz mithilfe eines f-Strings aus.




# ============================================================
# BLOCK 4: Der große Übungs-Pool
# ============================================================

# ---------- Kategorie A: Reine Text-Interaktion (kein Casting nötig) ----------

# --- Aufgabe 1: Der Begrüßungs-Generator ---
# Frage den Benutzer nach seinem Vornamen und seiner Stadt.
# Gib einen Satz aus wie: "Hallo [Vorname], wie ist das Wetter in [Stadt]?"



# --- Aufgabe 2: AD-Gruppen-Zuweisung ---
# Frage einen Benutzernamen ab. Das Skript soll den Benutzer fiktiv der
# Gruppe "Domain-Admins" hinzufügen und das Ergebnis ausgeben.
# Erwartete Ausgabe bei Eingabe "t.mueller":
# "Benutzer t.mueller wurde erfolgreich zur Gruppe 'Domain-Admins' hinzugefügt."



# --- Aufgabe 3: E-Mail-Generator ---
# Frage den Vornamen, den Nachnamen und die Firmen-Domain (z. B. "firma.de") ab.
# Erzeuge daraus eine E-Mail-Adresse im Format vorname.nachname@domain.




# ---------- Kategorie B: Ganzzahl-Berechnungen (int-Casting erforderlich) ----------

# --- Aufgabe 4: Der Verdoppler ---
# Frage den Benutzer nach einer Ganzzahl.
# Multipliziere diese Zahl mit 2 und gib das Ergebnis aus.



# --- Aufgabe 5: Server-Rack-Planer ---
# Ein Standard-Server-Rack hat 42 Höheneinheiten (HE).
# Frage den Benutzer, wie viele Höheneinheiten bereits durch Server belegt sind.
# Berechne, wie viele Höheneinheiten noch frei sind.



# --- Aufgabe 6: Jahresgehalt-Rechner ---
# Frage nach dem monatlichen Bruttogehalt.
# Berechne das Jahresgehalt (Monatsgehalt mal 12) und gib es aus.



# --- Aufgabe 7: Tage in Stunden umrechnen ---
# Frage den Benutzer nach einer Anzahl von Tagen (z. B. für eine Server-Uptime).
# Berechne, wie vielen Stunden das entspricht.




# ---------- Kategorie C: Nachkommastellen-Berechnungen (float-Casting erforderlich) ----------

# --- Aufgabe 8: Mehrwertsteuer-Addierer ---
# Frage den Benutzer nach einem Netto-Preis (z. B. 45.90).
# Berechne den Brutto-Preis inklusive 19% Mehrwertsteuer (Netto-Preis mal 1.19)
# und gib ihn aus.



# --- Aufgabe 9: RAM-Preiskalkulator ---
# Ein Gigabyte RAM kostet aktuell 4.50 Euro.
# Frage den Benutzer, wie viel GB RAM er bestellen möchte (z. B. 16 oder 32).
# Berechne den Gesamtpreis.



# --- Aufgabe 10: Temperatur-Konverter (Fahrenheit in Celsius) ---
# Ein US-amerikanischer Serverraum meldet die Temperatur in Fahrenheit.
# Frage den Benutzer nach der Temperatur in Fahrenheit.
# Rechne diese in Celsius um.
# Formel: Celsius = (Fahrenheit − 32) × 5/9




# ---------- Kategorie D: IT-Support-Szenarien (Herausforderung) ----------

# --- Aufgabe 11: IP-Subnetz Host-Rechner ---
# In einem Subnetz bestimmt die CIDR-Schnittmaske die Anzahl der IPs.
# Formel für nutzbare Hosts: 2^(freie Bits) − 2
#   - Frage den Benutzer nach den freien Bits (z. B. 8 bei einer /24 Maske).
#   - Berechne die nutzbaren Hosts.
#   - Hinweis: Potenzieren in Python funktioniert mit ** (z. B. 2 ** 8).



# --- Aufgabe 12: IT-Budget-Aufteilung ---
# Eine IT-Abteilung erhält ein Budget (z. B. 50000 Euro), das zu gleichen
# Teilen auf eine bestimmte Anzahl von Projekten aufgeteilt werden soll.
#   - Frage nach dem Gesamtbudget (Ganzzahl).
#   - Frage nach der Anzahl der Projekte (Ganzzahl).
#   - Berechne den Betrag pro Projekt (Ganzzahldivision //).
#   - Berechne den verbleibenden Restbetrag, der nicht gleichmäßig
#     aufgeteilt werden kann (Modulo %).
