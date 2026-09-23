"""
Python-Schulung – Tag 7: Lösungen
"""

# ============================================================
# BLOCK 4: Der große while-Praxis-Slam
# ============================================================

# ---------- Kategorie A: Einfache Schleifen ----------

### Aufgabe 1: Der Patch-Countdown
zahl_countdown = 5
while zahl_countdown >= 1:
    print(zahl_countdown)
    zahl_countdown -= 1
print("Patchvorgang startet...")

### Aufgabe 2: Der Backup-Fortschritt
fortschritt = 0
while fortschritt <= 100:
    print(f"Backup-Status: {fortschritt}%")
    fortschritt += 20

### Aufgabe 3: Der Spam-Schutz (Port-Pinger)
ping_zaehler = 0
while ping_zaehler < 4:
    print("Ping an 192.168.1.1 gesendet...")
    ping_zaehler += 1

# ---------- Kategorie B: Schleifen mit break und continue ----------

### Aufgabe 4: Drei Login-Versuche (Sperr-Logik)
versuche = 0
eingeloggt = False
while versuche < 3:
    eingabe_pw_4 = input("Passwort: ")
    if eingabe_pw_4 == "geheim":
        print("Login erfolgreich")
        eingeloggt = True
        break
    versuche += 1
if not eingeloggt:
    print("Konto gesperrt!")

### Aufgabe 5: Ungerade Ports überspringen
port_5 = 80
while port_5 <= 86:
    if port_5 % 2 != 0:
        port_5 += 1
        continue
    print(port_5)
    port_5 += 1

### Aufgabe 6: Der unendliche Chatbot
while True:
    eingabe_chat = input("Du: ")
    if eingabe_chat in ["exit", "beenden", "tschüss"]:
        print("Auf Wiedersehen!")
        break

# ---------- Kategorie C: Komplexe IT-Support-Schleifen ----------

### Aufgabe 7: Server-Überhitzung (Temperatursimulator)
temperatur_7 = 20
while temperatur_7 <= 50:
    anstieg = float(input("Um wie viel Grad steigt die Temperatur? "))
    temperatur_7 += anstieg
print("NOT-AUSSCHALTUNG AKTIVIERT!")

### Aufgabe 8: Interaktiver Task-Manager (ToDo-Listen-Schleife)
offene_tickets = []
while True:
    aktion = input("Aktion (w=hinzufügen, l=anzeigen, q=beenden): ")
    if aktion == "w":
        ticket = input("Ticket eingeben: ")
        offene_tickets.append(ticket)
    elif aktion == "l":
        print(offene_tickets)
    elif aktion == "q":
        break
