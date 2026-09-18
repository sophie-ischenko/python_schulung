# Python-Schulung – Tag 3: Lösungen

geburtsjahr = int(input("Geburtsjahr: "))
print(2026 - geburtsjahr)

minuten = int(input("Minuten: "))
print(minuten // 60)
print(minuten % 60)

originalpreis = float(input("Originalpreis: "))
rabatt = float(input("Rabatt in Prozent: "))
print(originalpreis - (originalpreis * rabatt / 100))

tb = float(input("Terabyte: "))
print(tb * 1024)

server_name = "DE-MUN-SRV01"
print(server_name[:2])

dateiname = "backup_datenbank.zip"
print(dateiname[-3:])

seriennummer = "SN-98765-XYZ"
print(seriennummer[3:8])

wort = input("Wort: ")
print(wort[::-1])

lizenzschluessel = "ABCD-1234-EFGH-5678"
print(lizenzschluessel[:4])
print(lizenzschluessel[-4:])

text = "A1B2C3D4E5"
print(text[::2])

name = "  admin_user  "
print(name.strip())

dateiname = "programm.exe"
print(dateiname.endswith(".exe"))

pfad = "C:/Benutzer/Desktop/Dokument"
print(pfad.replace("/", "\\"))

log = "[INFO] Start... [ERROR] DB weg... [ERROR] Abbruch..."
print(log.count("[ERROR]"))

text = "12345"
print(text.isdigit())

zeile = "Max;Mustermann;IT-Support"
print(zeile.split(";"))
