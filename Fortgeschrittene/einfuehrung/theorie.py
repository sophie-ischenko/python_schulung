"""
Einführung in Python – Tag 0

Willkommen zum Python-Kurs.

Bevor wir mit den eigentlichen Kursinhalten starten, wiederholen wir
die wichtigsten Grundlagen der Python-Syntax.

Dieser Einstieg ist bewusst kurz gehalten und dient als gemeinsamer
Ausgangspunkt für den weiteren Kurs.

Wir arbeiten mit:

- Ausgaben
- Zahlen
- Variablen
- einfachen Berechnungen
- Funktionen
- Bedingungen
- Benutzereingaben

Zum Abschluss setzen wir mehrere dieser Bausteine in einem kleinen
Programm zusammen.


LERNZIELE
=========

Nach diesem Einstieg kannst du:

- mit print() Werte auf der Konsole ausgeben
- Zahlen und Text unterscheiden
- einfache mathematische Berechnungen durchführen
- Werte in Variablen speichern
- Variablen in Berechnungen verwenden
- einfache Funktionen mit Parametern und return schreiben
- einfache Bedingungen formulieren
- Benutzereingaben mit input() verarbeiten


WICHTIG FÜR DIESES DOKUMENT
===========================

Die Beispiele in dieser Datei sind absichtlich auskommentiert.

Du kannst sie ausprobieren, indem du das # vor den entsprechenden
Zeilen entfernst.

Beispiel:

# print("Hallo Welt!")

wird zu:

print("Hallo Welt!")

Dann kannst du die Datei ausführen und direkt sehen, was Python macht.
"""


"""
1. AUSGABEN MIT print()
=======================

Mit print() gibt Python einen Wert auf der Konsole aus.

Ein Text wird dabei in Anführungszeichen geschrieben.
"""

# print("Hallo Welt!")


"""
Auch Zahlen können ausgegeben werden.
"""

# print(42)
# print(3.14)


"""
Mehrere Werte können durch Kommata getrennt ausgegeben werden.

Python setzt dabei automatisch ein Leerzeichen zwischen die Werte.
"""

# name = "Ada"
# alter = 25

# print("Name:", name)
# print("Alter:", alter)


"""
WICHTIG
-------

Text wird in Anführungszeichen geschrieben:

"Hallo"

Eine Zahl wird ohne Anführungszeichen geschrieben:

42

Der Unterschied ist wichtig.
"""

# print(42)
# print("42")


"""
Beide Werte sehen in der Ausgabe gleich aus:

42
42

Für Python sind sie aber unterschiedliche Datentypen.

42 ist eine Zahl.

"42" ist Text.


AUSPROBIEREN
------------

Was passiert bei den folgenden Ausgaben?
"""

# print(10)
# print("10")
# print(10 + 5)
# print("10" + "5")


"""
2. ZAHLEN UND RECHENOPERATIONEN
===============================

Python kann auch als Taschenrechner verwendet werden.

Die wichtigsten Rechenoperatoren sind:

+    Addition
-    Subtraktion
*    Multiplikation
/    Division
"""

# print(5 + 3)
# print(10 - 4)
# print(5 * 3)
# print(10 / 2)


"""
Das Ergebnis wäre:

8
6
15
5.0

Beachte:

Bei der normalen Division mit / liefert Python einen float.

10 / 2 ergibt deshalb:

5.0

und nicht:

5


AUSPROBIEREN
------------
"""

# print(20 + 7)
# print(20 - 7)
# print(20 * 7)
# print(20 / 7)


"""
3. DEZIMALZAHLEN
================

Dezimalzahlen werden in Python mit einem Punkt geschrieben.

Richtig:

preis = 12.50

Nicht:

preis = 12,50

Das Komma hat in Python eine andere Bedeutung.
"""

# preis = 12.50
# print(preis)


"""
AUSPROBIEREN

Verändere den Preis und führe das Programm aus.
"""

# preis = 19.99
# print(preis)


"""
4. STRINGS UND ZAHLEN
=====================

Ein häufiger Fehler besteht darin, Text und Zahlen zu verwechseln.

Hier ist zahl eine Zahl:

zahl = 10

Hier ist text ein String:

text = "10"
"""

# zahl = 10
# text = "10"

# print(zahl)
# print(text)


"""
Das kann man auch beim Rechnen sehen.

Bei Zahlen bedeutet + eine mathematische Addition:
"""

# print(10 + 5)


"""
Ergebnis:

15


Bei Strings bedeutet + das Aneinanderhängen von Text.
"""

# print("10" + "5")


"""
Ergebnis:

105

Python rechnet hier also nicht mit den beiden Zahlen 10 und 5.

Es hängt den Text "10" und den Text "5" zusammen.


AUSPROBIEREN
------------
"""

# print("Hallo " + "Python")
# print("Python " + "Kurs")
# print(5 + 5)
# print("5" + "5")


"""
5. VARIABLEN
============

Variablen speichern Werte unter einem Namen.

Beispiel:

alter = 25

Danach kann der Wert über den Namen alter verwendet werden.
"""

# alter = 25
# print(alter)


"""
Eine Variable kann auch für Berechnungen verwendet werden.
"""

# alter = 25
# naechstes_jahr = alter + 1

# print(naechstes_jahr)


"""
Das Ergebnis ist:

26


ZUWEISUNG MIT =

Das Gleichheitszeichen bedeutet bei einer Zuweisung:

"Speichere den Wert auf der rechten Seite unter dem Namen
auf der linken Seite."

Beispiel:
"""

# preis = 20


"""
Danach enthält die Variable preis den Wert 20.
"""

# print(preis)


"""
AUSPROBIEREN
------------
"""

# name = "Ada"
# alter = 25
# beruf = "Informatikerin"

# print(name)
# print(alter)
# print(beruf)


"""
6. VARIABLEN VERÄNDERN
======================

Eine Variable kann später einen neuen Wert bekommen.

Die zweite Zuweisung überschreibt den vorherigen Wert.
"""

# punkte = 10

# print(punkte)

# punkte = 20

# print(punkte)


"""
Die Ausgabe ist:

10
20


AUSPROBIEREN

Verändere die Punkte.
"""

# punkte = 50
# print(punkte)

# punkte = 75
# print(punkte)


"""
7. MIT VARIABLEN RECHNEN
========================

Variablen können miteinander kombiniert werden.

Das macht Programme flexibler als fest eingetragene Werte.
"""

# preis = 15
# anzahl = 3

# gesamtpreis = preis * anzahl

# print(gesamtpreis)


"""
Das Ergebnis ist:

45


Wenn sich anzahl verändert, wird automatisch ein anderes Ergebnis
berechnet.
"""

# preis = 15
# anzahl = 5

# gesamtpreis = preis * anzahl

# print(gesamtpreis)


"""
Das Ergebnis ist:

75


AUSPROBIEREN
------------
"""

# preis = 9.99
# anzahl = 4

# gesamtpreis = preis * anzahl

# print(gesamtpreis)


"""
8. VARIABLENNAMEN
=================

Variablennamen sollten verständlich gewählt werden.

Gut verständlich sind zum Beispiel:
"""

# name = "Ada"
# alter = 25
# preis = 19.99
# anzahl = 3


"""
Weniger aussagekräftig wären:
"""

# x = "Ada"
# a = 25
# p = 19.99
# n = 3


"""
Bei mehreren Wörtern wird in Python häufig snake_case verwendet.

Beispiele:
"""

# geburtsjahr = 2000
# aktuelles_jahr = 2026
# gesamtpreis = 59.97


"""
Ein guter Variablenname hilft dabei, Code später zu verstehen.

Statt:

x = 15
y = 3

ist zum Beispiel:

preis = 15
anzahl = 3

deutlich verständlicher.


AUSPROBIEREN
------------
"""

# artikel_preis = 12.50
# artikel_anzahl = 4
# gesamtpreis = artikel_preis * artikel_anzahl

# print(gesamtpreis)


"""
9. FUNKTIONEN
=============

Funktionen kapseln Code, der eine bestimmte Aufgabe erledigt.

Eine einfache Funktion sieht so aus:
"""

# def hallo():
#     print("Hallo!")


"""
Die Funktion wird zunächst definiert.

Ausgeführt wird sie durch einen Aufruf:
"""

# hallo()


"""
Die Ausgabe lautet:

Hallo!


Wichtig:

Das Definieren einer Funktion führt den Code noch nicht aus.

Erst der Aufruf:

hallo()

führt die Funktion aus.


AUSPROBIEREN
------------
"""

# def starte_programm():
#     print("Programm gestartet")

# starte_programm()


"""
10. PARAMETER
=============

Eine Funktion kann Werte als Parameter entgegennehmen.

Beispiel:
"""

# def begruessen(name):
#     print("Hallo", name)


"""
Beim Aufruf wird ein konkreter Wert übergeben:
"""

# begruessen("Ada")


"""
Die Ausgabe lautet:

Hallo Ada


Der Wert "Ada" wird beim Aufruf an den Parameter name übergeben.


AUSPROBIEREN
------------
"""

# def begruessen(name):
#     print("Willkommen", name)

# begruessen("Sophie")
# begruessen("Alex")
# begruessen("Sam")


"""
Eine Funktion kann auch mehrere Parameter besitzen.
"""

# def addiere(zahl1, zahl2):
#     print(zahl1 + zahl2)

# addiere(5, 3)


"""
Die Ausgabe lautet:

8


11. return
==========

Eine Funktion kann ein Ergebnis zurückgeben.

Dafür verwenden wir return.

Beispiel:
"""

# def addiere(zahl1, zahl2):
#     return zahl1 + zahl2


"""
Das Ergebnis kann anschließend in einer Variable gespeichert werden.
"""

# ergebnis = addiere(5, 3)

# print(ergebnis)


"""
Die Ausgabe lautet:

8


Der Unterschied zwischen print() und return ist wichtig.

Diese Funktion gibt etwas aus:
"""

# def addiere(zahl1, zahl2):
#     print(zahl1 + zahl2)


"""
Diese Funktion gibt ein Ergebnis zurück:
"""

# def addiere(zahl1, zahl2):
#     return zahl1 + zahl2


"""
Bei return kann das Ergebnis anschließend weiterverwendet werden.

Beispiel:
"""

# ergebnis = addiere(5, 3)
# doppelt = ergebnis * 2

# print(doppelt)


"""
Die Ausgabe lautet:

16


Das Ergebnis der Funktion wurde also weiterverarbeitet.


AUSPROBIEREN
------------
"""

# def multipliziere(zahl1, zahl2):
#     return zahl1 * zahl2

# ergebnis = multipliziere(4, 5)

# print(ergebnis)


"""
12. BEDINGUNGEN
===============

Mit Bedingungen kann ein Programm unterschiedliche Wege einschlagen.

Dafür verwenden wir unter anderem if und else.

Beispiel:
"""

# alter = 20

# if alter >= 18:
#     print("Volljährig")


"""
Ist die Bedingung wahr, wird der eingerückte Code ausgeführt.

Mit else kann ein zweiter Fall definiert werden.
"""

# alter = 16

# if alter >= 18:
#     print("Volljährig")
# else:
#     print("Minderjährig")


"""
Die Ausgabe lautet:

Minderjährig


Die Einrückung ist in Python Teil der Syntax.

Dieser Code gehört zur Bedingung:

if alter >= 18:
    print("Volljährig")

Die Einrückung darf deshalb nicht einfach weggelassen werden.


AUSPROBIEREN
------------
"""

# alter = 25

# if alter >= 18:
#     print("Du bist volljährig")
# else:
#     print("Du bist minderjährig")


"""
VERGLEICHSOPERATOREN

Für Bedingungen werden häufig Vergleichsoperatoren verwendet:

==    ist gleich
!=    ist nicht gleich
>     ist größer als
<     ist kleiner als
>=    ist größer oder gleich
<=    ist kleiner oder gleich

Beispiele:
"""

# alter = 18

# print(alter == 18)
# print(alter >= 18)
# print(alter < 18)


"""
Die Ergebnisse solcher Vergleiche sind:

True

oder:

False


AUSPROBIEREN
------------
"""

# punkte = 75

# if punkte >= 50:
#     print("Bestanden")
# else:
#     print("Nicht bestanden")


"""
13. BENUTZEREINGABEN MIT input()
================================

Mit input() kann ein Programm Daten vom Benutzer abfragen.

Beispiel:
"""

# name = input("Wie heißt du? ")

# print("Hallo", name)


"""
Wenn der Benutzer Ada eingibt, könnte die Ausgabe so aussehen:

Wie heißt du? Ada
Hallo Ada


WICHTIG: input() LIEFERT TEXT

Auch wenn eine Zahl eingegeben wird, liefert input() zunächst
einen String.

Beispiel:
"""

# alter = input("Wie alt bist du? ")


"""
Wenn der Benutzer 25 eingibt, enthält alter den Text:

"25"

und nicht die Zahl:

25


Wenn wir tatsächlich mit der Zahl rechnen möchten, müssen wir
den Wert umwandeln.

Dafür verwenden wir int().
"""

# alter = int(input("Wie alt bist du? "))

# print(alter + 1)


"""
Wenn der Benutzer 25 eingibt, ist das Ergebnis:

26


AUSPROBIEREN
------------
"""

# zahl = int(input("Gib eine Zahl ein: "))

# print("Deine Zahl ist:", zahl)
# print("Doppelt:", zahl * 2)


"""
Auch Dezimalzahlen können umgewandelt werden.

Dafür verwenden wir float().
"""

# preis = float(input("Wie viel kostet das Produkt? "))

# print("Preis:", preis)


"""
MERKE

input()
    liefert Text

int()
    wandelt in eine ganze Zahl um

float()
    wandelt in eine Dezimalzahl um


14. MEHRERE BAUSTEINE KOMBINIEREN
=================================

Jetzt können wir mehrere Grundlagen miteinander verbinden.

Beispiel:

Eine Person gibt ihren Namen und ihr Alter ein.

Das Programm gibt anschließend eine passende Nachricht aus.
"""

# name = input("Wie heißt du? ")
# alter = int(input("Wie alt bist du? "))

# print("Hallo", name)

# if alter >= 18:
#     print("Du bist volljährig.")
# else:
#     print("Du bist minderjährig.")


"""
Hier werden bereits mehrere Python-Grundlagen kombiniert:

- input()
- Variablen
- int()
- print()
- if
- else
- Vergleichsoperatoren

Genau dieses Zusammenspiel wird im weiteren Kurs immer wichtiger.


15. MINI-WIEDERHOLUNG
=====================

Die wichtigsten Bausteine dieses Einstiegs:
"""

# Ausgabe
# print("Hallo")


# Variable
# name = "Ada"


# Berechnung
# alter = 25
# naechstes_jahr = alter + 1


# Funktion
# def addiere(a, b):
#     return a + b


# Bedingung
# if alter >= 18:
#     print("Volljährig")


# Eingabe
# name = input("Name: ")


"""
Diese Bausteine bilden die Grundlage für die folgenden Kurstage.


16. ÜBUNGEN
===========

Öffne die Datei:

aufgaben.py

Bearbeite dort die drei markierten Aufgaben.

1. hallo_welt()

   Die Funktion soll einen festen Text zurückgeben.

2. addiere()

   Die Funktion soll zwei Zahlen addieren.

3. berechne_alter()

   Die Funktion soll das Alter aus zwei Jahreszahlen berechnen.


STARTE DIE AUFGABEN

Im Terminal:

python aufgaben.py


Ein Häkchen bedeutet:

Der Test war erfolgreich.

Ein Kreuz zeigt:

Das Ergebnis entspricht noch nicht der erwarteten Lösung.


Wichtig:

Versuche zuerst selbst herauszufinden, was die Funktion tun soll.

Nutze die Beispiele aus diesem Theorie-Dokument als Hilfe.
"""


"""
17. MINI-PROJEKT: DER BEGRÜSSUNGS-BOT
=====================================

Zum Abschluss kombinieren wir mehrere Grundlagen in einem kleinen
Programm.

Der Benutzer gibt seinen Namen und sein Alter ein.

Das Programm soll:

1. eine persönliche Begrüßung erstellen
2. prüfen, ob die Person volljährig ist
3. das Ergebnis auf der Konsole ausgeben


BEISPIEL

Das Programm könnte beispielsweise so aussehen:

=== START DES BOTS ===
Wie heißt du? Ada
Wie alt bist du? 25
Hallo Ada! Willkommen an Bord.
Du bist volljährig. Du darfst alle Funktionen nutzen.
=== ENDE ===


In projekt.py gibt es dafür zwei Funktionen:

erstelle_begruessung()
ist_volljaehrig()

In beiden Funktionen befindet sich eine TODO-Stelle.

Bearbeite nur diese Stellen.

Versuche, die Lösung mit den Grundlagen aus diesem Dokument
selbst zu entwickeln.


PROGRAMM STARTEN

Im Terminal:

python projekt.py


AUTOMATISCHEN SELBSTTEST STARTEN

Im Terminal:

python projekt.py test


Der Selbsttest überprüft verschiedene Eingaben automatisch.
"""


"""
18. ABSCHLUSS
=============

Damit sind die grundlegenden Python-Bausteine wiederholt.

Du kannst jetzt:

- Werte mit print() ausgeben
- Text und Zahlen unterscheiden
- mit Zahlen rechnen
- Variablen verwenden
- Variablen verändern
- Funktionen definieren
- Parameter verwenden
- Ergebnisse mit return zurückgeben
- Bedingungen mit if und else formulieren
- Benutzereingaben mit input() verarbeiten
- mehrere dieser Bausteine miteinander kombinieren


IM WEITEREN KURS

Ab jetzt geht es nicht mehr darum, einzelne Befehle isoliert
kennenzulernen.

Stattdessen kombinieren wir die Bausteine und wenden sie auf
größere Aufgaben an.

Ab Tag 1 geht es mit den eigentlichen Kursinhalten weiter.


ENDE TAG 0
==========
"""