"""
Python-Schulung – Tag 2: Lösungen
"""

# ============================================================
# BLOCK 1: Wiederholung von Tag 1
# ============================================================

### Aufgabe W1: System-Statusbericht
hostname = "srv-file01"
cpu_cores = 8
speicherauslastung = 72.5
datenbank_laeuft = True
print(hostname)
print(cpu_cores)
print(speicherauslastung)
print(datenbank_laeuft)

### Aufgabe W2: Die manuelle Preisberechnung
netto_preis = 120
steuersatz = 0.19
steuerbetrag = netto_preis * steuersatz
brutto_preis = netto_preis + steuerbetrag
print(steuerbetrag)
print(brutto_preis)

### Aufgabe W3: Steckbrief-Formatierung
mitarbeiter_name = "Anna Schmidt"
personalnummer = 4711
rolle = "Systemadministratorin"
print(f"{mitarbeiter_name} (Personalnummer {personalnummer}) arbeitet als {rolle}.")


# ============================================================
# BLOCK 4: Der große Übungs-Pool
# ============================================================

# ---------- Kategorie A: Reine Text-Interaktion ----------

### Aufgabe 1: Der Begrüßungs-Generator
vorname = input("Wie ist dein Vorname? ")
stadt = input("In welcher Stadt wohnst du? ")
print(f"Hallo {vorname}, wie ist das Wetter in {stadt}?")

### Aufgabe 2: AD-Gruppen-Zuweisung
benutzername = input("Benutzername: ")
print(f"Benutzer {benutzername} wurde erfolgreich zur Gruppe 'Domain-Admins' hinzugefügt.")

### Aufgabe 3: E-Mail-Generator
vorname_3 = input("Vorname: ")
nachname_3 = input("Nachname: ")
domain_3 = input("Firmen-Domain (z. B. firma.de): ")
email = f"{vorname_3.lower()}.{nachname_3.lower()}@{domain_3}"
print(email)

# ---------- Kategorie B: Ganzzahl-Berechnungen ----------

### Aufgabe 4: Der Verdoppler
zahl_4 = int(input("Ganzzahl eingeben: "))
print(zahl_4 * 2)

### Aufgabe 5: Server-Rack-Planer
rack_gesamt = 42
belegte_he = int(input("Belegte Höheneinheiten: "))
print(rack_gesamt - belegte_he)

### Aufgabe 6: Jahresgehalt-Rechner
monatsgehalt = int(input("Monatliches Bruttogehalt: "))
print(monatsgehalt * 12)

### Aufgabe 7: Tage in Stunden umrechnen
tage_7 = int(input("Anzahl Tage: "))
print(tage_7 * 24)

# ---------- Kategorie C: Nachkommastellen-Berechnungen ----------

### Aufgabe 8: Mehrwertsteuer-Addierer
netto_8 = float(input("Nettopreis: "))
print(netto_8 * 1.19)

### Aufgabe 9: RAM-Preiskalkulator
preis_pro_gb = 4.50
gb_bestellt = float(input("Wie viel GB RAM? "))
print(gb_bestellt * preis_pro_gb)

### Aufgabe 10: Temperatur-Konverter
fahrenheit = float(input("Temperatur in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)

# ---------- Kategorie D: IT-Support-Szenarien ----------

### Aufgabe 11: IP-Subnetz Host-Rechner
freie_bits = int(input("Anzahl freier Bits: "))
nutzbare_hosts = 2 ** freie_bits - 2
print(nutzbare_hosts)

### Aufgabe 12: IT-Budget-Aufteilung
gesamtbudget = int(input("Gesamtbudget: "))
anzahl_projekte = int(input("Anzahl Projekte: "))
betrag_pro_projekt = gesamtbudget // anzahl_projekte
restbetrag = gesamtbudget % anzahl_projekte
print(betrag_pro_projekt)
print(restbetrag)
