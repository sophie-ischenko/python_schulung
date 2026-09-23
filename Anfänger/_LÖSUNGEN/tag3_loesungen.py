"""
Python-Schulung – Tag 3: Lösungen
"""

# ============================================================
# BLOCK 1: Der große Recap-Slam
# ============================================================

### Aufgabe R1: Benutzer-Verifizierung
geburtsjahr = int(input("Geburtsjahr: "))
alter = 2026 - geburtsjahr
print(alter)

### Aufgabe R2: Support-Dauer (Ganzzahl & Rest)
minuten_r2 = int(input("Minuten: "))
stunden_r2 = minuten_r2 // 60
rest_minuten = minuten_r2 % 60
print(f"{stunden_r2} Stunden und {rest_minuten} Minuten")

### Aufgabe R3: Rabatt-Kalkulator
originalpreis = float(input("Originalpreis: "))
rabatt_prozent = float(input("Rabatt in %: "))
endpreis = originalpreis - (originalpreis * rabatt_prozent / 100)
print(endpreis)

### Aufgabe R4: Speicher-Umrechner (TB in GB)
tb = float(input("Kapazität in TB: "))
gb = tb * 1024
print(gb)


# ============================================================
# BLOCK 4: Der große Übungs-Slam
# ============================================================

# ---------- Teil A: String-Slicing ----------

### Aufgabe 1: Ländercode extrahieren
servername_1 = "DE-MUN-SRV01"
print(servername_1[0:2])

### Aufgabe 2: Dateiendung bestimmen
dateiname_2 = "backup_datenbank.zip"
print(dateiname_2[-3:])

### Aufgabe 3: Seriennummer teilen
seriennummer = "SN-98765-XYZ"
print(seriennummer[3:8])

### Aufgabe 4: Rückwärtsgang
wort_4 = input("Wort eingeben: ")
print(wort_4[::-1])

### Aufgabe 5: Lizenzschlüssel-Präfix
lizenzschluessel = "ABCD-1234-EFGH-5678"
print(lizenzschluessel[0:4])
print(lizenzschluessel[-4:])

### Aufgabe 6: Jeder zweite Buchstabe
code_6 = "A1B2C3D4E5"
print(code_6[::2])

# ---------- Teil B: Recherche-Aufgaben ----------

### Aufgabe 7: Leerzeichen entfernen (Recherche)
benutzername_7 = " admin_user "
print(benutzername_7.strip())

### Aufgabe 8: Dateityp prüfen (Recherche)
dateiname_8 = input("Dateiname: ")
print(dateiname_8.endswith(".exe"))

### Aufgabe 9: Zeichen ersetzen (Recherche)
pfad_9 = "C:/Benutzer/Desktop/Dokument"
print(pfad_9.replace("/", "\\"))

### Aufgabe 10: Fehler-Zähler im Log (Recherche)
log_10 = "[INFO] Start... [ERROR] DB weg... [ERROR] Abbruch..."
print(log_10.count("[ERROR]"))

### Aufgabe 11: Nur Zahlen prüfen (Recherche)
code_11 = "12345"
print(code_11.isdigit())

### Aufgabe 12: CSV-Zeile zerlegen (Recherche)
csv_zeile_12 = "Max;Mustermann;IT-Support"
print(csv_zeile_12.split(";"))
