# Python-Schulung – Tag 2: Lösungen

hostname = "SRV-01"
cpu_cores = 8
speicherauslastung = 72.5
datenbank_laeuft = True

print(hostname)
print(cpu_cores)
print(speicherauslastung)
print(datenbank_laeuft)

netto_preis = 120
steuersatz = 0.19
steuerbetrag = netto_preis * steuersatz
bruttopreis = netto_preis + steuerbetrag
print(steuerbetrag)
print(bruttopreis)

mitarbeiter_name = "Max Mustermann"
personalnummer = 12345
rolle = "IT-Support"
print(f"{mitarbeiter_name} mit der Personalnummer {personalnummer} arbeitet als {rolle}.")

vorname = input("Vorname: ")
stadt = input("Stadt: ")
print(f"Hallo {vorname}, wie ist das Wetter in {stadt}?")

benutzername = input("Benutzername: ")
print(f"Benutzer {benutzername} wurde erfolgreich zur Gruppe 'Domain-Admins' hinzugefügt.")

vorname = input("Vorname: ")
nachname = input("Nachname: ")
domain = input("Firmen-Domain: ")
email = f"{vorname}.{nachname}@{domain}"
print(email)

zahl = int(input("Ganzzahl: "))
print(zahl * 2)

belegt = int(input("Belegte Höheneinheiten: "))
print(42 - belegt)

monatsgehalt = int(input("Monatliches Bruttogehalt: "))
print(monatsgehalt * 12)

tage = int(input("Anzahl der Tage: "))
print(tage * 24)

netto = float(input("Netto-Preis: "))
print(netto * 1.19)

gb = float(input("RAM in GB: "))
print(gb * 4.50)

fahrenheit = float(input("Temperatur in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)

freie_bits = int(input("Freie Bits: "))
print(2 ** freie_bits - 2)

budget = int(input("Gesamtbudget: "))
projekte = int(input("Anzahl der Projekte: "))
print(budget // projekte)
print(budget % projekte)
