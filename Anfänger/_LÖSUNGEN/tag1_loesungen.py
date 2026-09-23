"""
Python-Schulung – Tag 1: Lösungen
"""

# ============================================================
# BLOCK 1: Was ist Programmierung
# ============================================================

### Aufgabe 1
zahl = 12
print(zahl)

### Aufgabe 2
stadt = "Hamburg"
print(stadt)

### Aufgabe 3
punkte = 100
print(punkte)

### Aufgabe 4
tier = "Katze"
print(tier)

### Aufgabe 5
zahl1 = 5
farbe = "blau"
print(zahl1)
print(farbe)


# ============================================================
# BLOCK 2: Die vier Basis-Datentypen
# ============================================================

### Aufgabe 1: Eigene Variablen anlegen
alter = 30
name = "Sophie"
hobby = "Lesen"
print(alter)
print(name)
print(hobby)

### Aufgabe 2: Variablennamen korrigieren
# Fehlerhaft:      Alter = 25 / mein hobby = "Lesen" / 2katzen = 2
# Korrektur:
alter_2 = 25
mein_hobby = "Lesen"
zwei_katzen = 2
print(alter_2, mein_hobby, zwei_katzen)

### Aufgabe 3: Datentyp erraten
x = 42
y = "42"
z = 4.2
w = True
# Vermutung:
# x = Ganzzahl (int)
# y = Text (str)
# z = Nachkommazahl (float)
# w = Wahrheitswert (bool)

### Aufgabe 4: Datentypen erkennen
a = 10
b = "Hallo"
c = 3.14
print(type(a))
print(type(b))
print(type(c))

### Aufgabe 5: Datentypen herausfinden
print(type(x))
print(type(y))
print(type(z))
print(type(w))

### Aufgabe 4b: Zahl oder Text?
zahl1_b = 5
zahl2_b = "5"
print(type(zahl1_b))
print(type(zahl2_b))
# Erklärung: zahl1_b ist eine Ganzzahl (int) und kann direkt für Berechnungen
# genutzt werden. zahl2_b ist ein Text (str) mit demselben Zeichen "5" und
# müsste erst mit int() umgewandelt werden, um damit zu rechnen.

### Aufgabe 5b: Datentypen korrigieren
# Fehlerhaft:  alter = "zwanzig" / preis = 5 / name = 123
# Korrektur:
alter_5b = 20        # Ganzzahl statt Text
preis_5b = 5.00      # Nachkommazahl statt Ganzzahl
name_5b = "Sophie"   # Text statt Zahl
print(alter_5b, preis_5b, name_5b)


# ============================================================
# BLOCK 3: Rechnen mit Variablen in Python
# ============================================================

### Aufgabe 1: Alter in 5 Jahren
aktuelles_alter = 30
alter_in_zukunft = aktuelles_alter + 5
print(alter_in_zukunft)

### Aufgabe 2: Zwei Zahlen addieren
zahl1_3 = 7
zahl2_3 = 15
summe = zahl1_3 + zahl2_3
print(summe)

### Aufgabe 3: Rechteck-Fläche berechnen
breite = 5
laenge = 8
flaeche = breite * laenge
print(flaeche)

### Aufgabe 5: Umrechnung von Minuten in Sekunden
minuten = 45
sekunden = minuten * 60
print(sekunden)

### Aufgabe 6: Rabatt berechnen
originalpreis = 150.00
rabatt = 20.00
endpreis = originalpreis - rabatt
print(endpreis)

### Aufgabe 7: Mehrwertsteuer ermitteln
netto_7 = 1000
steuersatz_7 = 0.19
steuerbetrag_7 = netto_7 * steuersatz_7
print(steuerbetrag_7)


# ============================================================
# BLOCK 4: String-Verknüpfung & f-Strings
# ============================================================

### Aufgabe 1: Der Ticket-Status-Bericht (f-String)
ticket_nr = 4092
status = "in Bearbeitung"
zustaendig = "Klaus"
print(f"Das Ticket {ticket_nr} ist {status} und wird von {zustaendig} bearbeitet.")

### Aufgabe 2: Server-Meldung zusammenbauen
server_name = "SRV-Web"
fehlercode = 500
print("Fehler auf", server_name, "Code:", fehlercode)
print(f"Fehler auf {server_name} Code: {fehlercode}")
# print("Fehler auf " + server_name + " Code: " + fehlercode)
# Diese Zeile schlägt fehl (TypeError), weil fehlercode eine Ganzzahl (int)
# ist und der +-Operator bei Strings nur andere Strings anhängen kann.
# Lösung: str(fehlercode) verwenden oder direkt einen f-String nutzen.

### Aufgabe 3: Begrüßung mit Komma
kunde = "Frau Weber"
print("Willkommen,", kunde)

### Aufgabe 4: Vollständiger Name mit Plus
vorname_4 = "Sophie"
nachname_4 = "Müller"
voller_name = vorname_4 + " " + nachname_4
print(voller_name)

### Aufgabe 5: Bestellbestätigung (f-String)
artikel = "Laptop"
menge = 2
preis = 899.99
print(f"Bestellung: {menge}x {artikel} zum Preis von {preis} Euro.")
