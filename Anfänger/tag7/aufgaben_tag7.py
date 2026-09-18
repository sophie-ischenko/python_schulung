"""
Python-Schulung – Tag 7: Aufgaben
==================================
Trage deine Lösungen direkt unter der jeweiligen Aufgabe ein.
Führe die Datei aus und teste deine Eingaben.
"""

# ============================================================
# BLOCK 4: Der große while-Praxis-Slam
# ============================================================

# ---------- Kategorie A: Einfache Schleifen ----------

# --- Aufgabe 1: Der Patch-Countdown ---
# Schreibe ein Programm, das einen Countdown von 5 bis 1 ausgibt.
# Nach der 1 soll "Patchvorgang startet..." ausgegeben werden.



# --- Aufgabe 2: Der Backup-Fortschritt ---
# Simuliere einen Backup-Fortschrittsbalken. Starte bei 0 Prozent.
# Erhöhe den Wert in jedem Schleifendurchlauf um 20 Prozent und gib aus:
# "Backup-Status: X%". Die Schleife endet bei 100 Prozent.



# --- Aufgabe 3: Der Spam-Schutz (Port-Pinger) ---
# Ein Ping-Werkzeug soll maximal 4 Pings senden. Schreibe eine Schleife,
# die zählt und viermal "Ping an 192.168.1.1 gesendet..." ausgibt.




# ---------- Kategorie B: Schleifen mit break und continue ----------

# --- Aufgabe 4: Drei Login-Versuche (Sperr-Logik) ---
# Der Benutzer hat maximal 3 Versuche, das Passwort "geheim" einzugeben.
# Wenn er es richtig eingibt, bricht die Schleife mit break ab
# ("Login erfolgreich"). Wenn er nach 3 Versuchen scheitert, gib
# "Konto gesperrt!" aus.



# --- Aufgabe 5: Ungerade Ports überspringen ---
# Ein Skript scannt die Ports von 80 bis 86. Verwende eine while-Schleife
# und continue, um nur die geraden Ports auszugeben
# (Tipp: nutze % 2 == 0 zur Prüfung).



# --- Aufgabe 6: Der unendliche Chatbot ---
# Schreibe eine Schleife, die den Benutzer immer wieder nach einer
# Eingabe fragt. Wenn der Benutzer "exit", "beenden" oder "tschüss"
# eingibt, soll sich das Programm mit einer Abschiedsmeldung beenden.




# ---------- Kategorie C: Komplexe IT-Support-Schleifen ----------

# --- Aufgabe 7: Server-Überhitzung (Temperatursimulator) ---
# Die Temperatur im Serverraum startet bei 20 Grad.
#   - In jedem Schleifendurchlauf fragt das Programm den Benutzer:
#     "Um wie viel Grad steigt die Temperatur? " (Dezimalzahl).
#   - Addiere diesen Wert zur Gesamttemperatur.
#   - Sobald die Temperatur 50 Grad überschreitet, brich die Schleife ab
#     und gib eine Warnmeldung aus: "NOT-AUSSCHALTUNG AKTIVIERT!"



# --- Aufgabe 8: Interaktiver Task-Manager (ToDo-Listen-Schleife) ---
# Schreibe ein interaktives Programm mit einer leeren Liste
# offene_tickets = [].
#   - Die Schleife fragt den Benutzer fortlaufend nach einer Aktion:
#     "w" (Ticket hinzufügen), "l" (Tickets anzeigen), "q" (beenden).
#   - Bei "w" wird das eingegebene Ticket der Liste hinzugefügt.
#   - Bei "l" wird die aktuelle Liste ausgegeben.
#   - Bei "q" bricht das Programm ab.
