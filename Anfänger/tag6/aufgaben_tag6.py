"""
Python-Schulung – Tag 6: Aufgaben
==================================
Trage deine Lösungen direkt unter der jeweiligen Aufgabe ein.
Führe die Datei aus und teste deine Eingaben.
"""

# ============================================================
# BLOCK 1: Der große Listen-Recap
# ============================================================

# --- Aufgabe R1: Die Einkaufsliste ---
# Erstelle eine Liste einkauf = ["Brot", "Milch", "Eier"].
# Füge per Code "Äpfel" hinzu und gib die Gesamtanzahl der
# Artikel auf der Liste aus (nutze eine Funktion dafür).



# --- Aufgabe R2: Highscore-Update ---
# Gegeben ist: highscores = ["Anna", "Berta", "Chris"]
# Ersetze die Spielerin "Berta" (Index 1) direkt durch den neuen Namen
# "Ben". Gib die aktualisierte Liste aus.



# --- Aufgabe R3: Temperatur-Auswertung ---
# Gegeben ist: temps = [21.5, 24.0, 19.8, 25.4, 22.1]
# Bestimme mithilfe von Python-Funktionen die minimale und die maximale
# Temperatur aus dieser Liste und gib beide Werte aus.



# --- Aufgabe R4: Aufgaben-Verwaltung (Löschen mit Rückgabe) ---
# Gegeben ist: todos = ["Wäsche waschen", "Kochen", "Müll rausbringen"]
# Entferne die letzte Aufgabe aus der Liste und speichere sie
# in einer Variablen erledigt.
# Gib aus, welche Aufgabe erledigt wurde und welche noch in der Liste stehen.



# --- Aufgabe R5: Namens-Sortierung ---
# Sortiere die Liste teilnehmer = ["Zorro", "Aaron", "Xenia", "Berta"]
# alphabetisch absteigend (von Z nach A) und gib sie aus.



# --- Aufgabe R6: Gästeliste (Mitgliedschaft prüfen) ---
# Erstelle eine Liste hausverbot = ["Max", "Moritz"].
# Prüfe per Code, ob der Name "Max" in der Liste steht.
# Das Programm soll als Ergebnis direkt True oder False ausgeben.




# ============================================================
# BLOCK 4: Der große Logik-Praxis-Slam
# ============================================================

# ---------- Kategorie A: Einfache Bedingungen (Vergleichsoperatoren) ----------

# --- Aufgabe 1: Die Volljährigkeits-Prüfung ---
# Frage den Benutzer nach seinem Alter (Ganzzahl).
# Wenn das Alter unter 18 liegt, gib aus:
# "Du bist noch nicht volljährig!" Andernfalls gib aus:
# "Du bist volljährig!"



# --- Aufgabe 2: Das geheime Passwort ---
# Definiere ein festes Passwort im Code: korrektes_passwort = "kittycat".
# Frage den Benutzer nach dem Passwort. Wenn die Eingabe übereinstimmt,
# gib "Willkommen" aus, andernfalls "Zutritt verweigert".



# --- Aufgabe 3: Gerade oder ungerade? ---
# Frage den Benutzer nach einer Zahl (Ganzzahl). Prüfe mithilfe des
# Modulo-Operators (%), ob die Zahl gerade ist (Rest bei Teilung durch 2 ist 0).
# Gib entsprechend "Die Zahl ist gerade" oder "Die Zahl ist ungerade" aus.




# ---------- Kategorie B: Mehrere Bedingungen (elif) ----------

# --- Aufgabe 4: Fußball-Ergebnis ---
# Frage den Benutzer nacheinander nach den Toren der Heimmannschaft und
# den Toren der Auswärtsmannschaft.
#   - Mehr Heim-Tore: "Die Heimmannschaft hat gewonnen!"
#   - Mehr Auswärts-Tore: "Die Auswärtsmannschaft hat gewonnen!"
#   - Sonst: "Es ist ein Unentschieden!"



# --- Aufgabe 5: Noten-Bewerter ---
# Frage nach den erreichten Punkten (0 bis 100, Ganzzahl).
#   Punkte unter 50: "Durchgefallen"
#   Punkte zwischen 50 und 89: "Bestanden"
#   Punkte ab 90: "Sehr gut!"



# --- Aufgabe 6: Feiertags-Kalender ---
# Frage den Benutzer nach dem heutigen Datum als Text (z.B. "24.12.").
#   Ist die Eingabe "24.12.": "Es ist Heiligabend!"
#   Ist die Eingabe "31.12.": "Es ist Silvester!"
#   Ist die Eingabe "01.01.": "Frohes Neues Jahr!"
#   Bei allen anderen Eingaben: "Ein ganz normaler Tag."




# ---------- Kategorie C: Komplexe Logik mit Listen & logischen Operatoren ----------

# --- Aufgabe 7: Die Neffen (Listen-Check) ---
# Erstelle eine Liste: duck_neffen = ["Tick", "Trick", "Track"]
#   - Frage den Benutzer nach seinem Vornamen.
#   - Prüfe, ob der eingegebene Name in der Liste steht.
#   - Wenn ja: "Du bist ein Neffe von Donald Duck!"
#   - Wenn nein: "Diesen Namen kenne ich nicht aus Entenhausen."



# --- Aufgabe 8: VIP-Party mit Sperrstunde ---
# Definiere geschlossene_gesellschaft = True (Boolean). Frage den Benutzer
# nach seinem Namen.
#   - Wenn geschlossene_gesellschaft aktiv ist (True) UND der Name
#     ungleich "VIP" ist, gib aus: "Heute nur für geladene Gäste."
#   - Andernfalls gib aus: "Willkommen auf der Party!"



# --- Aufgabe 9: Kino-Altersfreigabe (ab 12) ---
# Frage ab:
#   1. Wie alt ist die Person? (Ganzzahl)
#   2. Ist eine erwachsene Begleitperson dabei? (ja / nein)
#
#   - Wenn das Alter mindestens 12 ist ODER die Begleitperson "ja" ist, gib aus:
#     "Viel Spaß beim Film!"
#   - Andernfalls gib aus: "Zutritt verweigert."



# --- Aufgabe 10: Multi-Faktor-Zugang (Herausforderung) ---
# Ein sicherer Tresor benötigt drei Bedingungen für die Öffnung:
#   - Der Benutzer muss das Passwort "tresor123" eingeben.
#   - Er muss eine PIN eingeben, die mit "99" beginnt
#     (simuliere dies, indem du die PIN als Text abfragst und z.B. per 
#      String-Methode oder Index prüfst).
#   - Das System darf nicht im Sperrmodus (gesperrt = True) sein.
#
# Schreibe ein Programm, das PIN und Passwort abfragt und den Tresor
# nur öffnet, wenn alle drei Bedingungen erfüllt sind.



# --- Aufgabe 11: Bußgeldkatalog ---
# https://www.bussgeldkatalog.org/geschwindigkeitsueberschreitung/
# Du findest die Tabelle im Ordner als Bild.
# Schreibe ein Programm, das den Benutzer nach der gefahrenen Geschwindigkeit fragt.
# Dann soll das Programm die Höhe des Bußgeldes ausgeben.