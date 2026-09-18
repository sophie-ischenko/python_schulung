# Python-Schulung – Tag 7: Lösungen

# Aufgabe 1
zahl = 5
while zahl >= 1:
    print(zahl)
    zahl -= 1
print("Patchvorgang startet...")


# Aufgabe 2
fortschritt = 0
while fortschritt < 100:
    fortschritt += 20
    print(f"Backup-Status: {fortschritt}%")


# Aufgabe 3
zaehler = 0
while zaehler < 4:
    print("Ping an 192.168.1.1 gesendet...")
    zaehler += 1


# Aufgabe 4
versuche = 0
while versuche < 3:
    passwort = input("Passwort: ")
    versuche += 1

    if passwort == "geheim":
        print("Login erfolgreich")
        break
else:
    print("Konto gesperrt!")


# Aufgabe 5
port = 80
while port <= 86:
    if port % 2 != 0:
        port += 1
        continue

    print(port)
    port += 1


# Aufgabe 6
while True:
    eingabe = input("Eingabe: ")

    if eingabe in ["exit", "beenden", "tschüss"]:
        print("Auf Wiedersehen!")
        break

    print(f"Eingabe: {eingabe}")


# Aufgabe 7
temperatur = 20.0

while temperatur <= 50:
    anstieg = float(input("Um wie viel Grad steigt die Temperatur? "))
    temperatur += anstieg

print("NOT-AUSSCHALTUNG AKTIVIERT!")


# Aufgabe 8
offene_tickets = []

while True:
    aktion = input("Aktion (w/l/q): ")

    if aktion == "w":
        ticket = input("Ticket: ")
        offene_tickets.append(ticket)

    elif aktion == "l":
        print(offene_tickets)

    elif aktion == "q":
        break
