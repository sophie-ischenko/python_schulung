"""
Python Tag 2 – Datenstrukturen

Heute geht es darum, Daten in Python sinnvoll zu strukturieren.

Wir arbeiten mit:

- Listen
- Tupeln
- Dictionaries
- Sets
- sorted()
- verschachtelten Datenstrukturen

Die einzelnen Datenstrukturen haben unterschiedliche Aufgaben.

Entscheidend ist deshalb nicht nur, wie eine Datenstruktur
funktioniert, sondern auch, wann sie sinnvoll eingesetzt wird.


LERNZIELE
=========

Nach diesem Tag kannst du:

- Listen erstellen und verändern
- Listen mit Schleifen verarbeiten
- neue Listen aus vorhandenen Daten erstellen
- Tupel verwenden
- Dictionaries mit Schlüssel-Wert-Paaren verwenden
- Dictionaries verändern und durchsuchen
- Dictionaries zum Zählen verwenden
- Sets für eindeutige Werte verwenden
- Mengen miteinander vergleichen
- Daten mit sorted() sortieren
- verschachtelte Datenstrukturen lesen und verarbeiten
- zwischen verschiedenen Datenstrukturen unterscheiden


WICHTIG FÜR DIESES DOKUMENT
===========================

Die Beispiele sind absichtlich auskommentiert.

Wenn du ein Beispiel ausprobieren möchtest,
entferne einfach das # vor den entsprechenden Codezeilen.

Beispiel:

# temperaturen = [18.4, 21.7, 19.2]

wird zu:

temperaturen = [18.4, 21.7, 19.2]

Danach kannst du die Datei ausführen und beobachten,
was Python macht.
"""


"""
1. LISTEN
=========

Eine Liste speichert mehrere Werte in einer bestimmten Reihenfolge.

Beispiel:
"""

# temperaturen = [18.4, 21.7, 19.2, 23.1]

# print(temperaturen)


"""
Die einzelnen Werte können über ihren Index angesprochen werden.

Der erste Index ist immer 0.
"""

# temperaturen = [18.4, 21.7, 19.2, 23.1]

# print(temperaturen[0])
# print(temperaturen[2])


"""
Die Ausgabe ist:

18.4
19.2


MERKE

Der erste Wert befindet sich an Position 0.

Bei dieser Liste:

[18.4, 21.7, 19.2, 23.1]

sind die Indizes:

0 → 18.4
1 → 21.7
2 → 19.2
3 → 23.1


AUSPROBIEREN
------------
"""

# temperaturen = [18.4, 21.7, 19.2, 23.1]

# print(temperaturen[0])
# print(temperaturen[1])
# print(temperaturen[3])


"""
WERTE HINZUFÜGEN

Mit append() wird ein neuer Wert am Ende der Liste eingefügt.
"""

# temperaturen = [18.4, 21.7, 19.2, 23.1]

# temperaturen.append(24.0)

# print(temperaturen)


"""
Die Liste enthält danach:

[18.4, 21.7, 19.2, 23.1, 24.0]


AUSPROBIEREN
------------
"""

# temperaturen = [18.4, 21.7]

# temperaturen.append(22.5)
# temperaturen.append(24.1)

# print(temperaturen)


"""
LISTEN DURCHLAUFEN

Mit einer for-Schleife können wir jeden Wert einer Liste
einzeln verarbeiten.
"""

# temperaturen = [18.4, 21.7, 19.2, 23.1]

# for temperatur in temperaturen:
#     print(temperatur)


"""
Hier passiert Folgendes:

Python nimmt nacheinander jeden Wert aus der Liste.

Zuerst:

temperatur = 18.4

Dann:

temperatur = 21.7

Dann:

temperatur = 19.2

und so weiter.


AUSPROBIEREN
------------
"""

# server = ["web01", "web02", "db01"]

# for servername in server:
#     print(servername)


"""
EINE NEUE LISTE AUFBAUEN

Wir können während einer Schleife eine neue Liste erstellen.

Das ist besonders praktisch, wenn wir Daten filtern möchten.

Beispiel:
"""

# temperaturen = [18.4, 21.7, 19.2, 23.1]

# hohe_werte = []

# for temperatur in temperaturen:
#     if temperatur >= 20:
#         hohe_werte.append(temperatur)

# print(hohe_werte)


"""
Danach enthält hohe_werte nur die Temperaturen ab 20 Grad.

Das Grundmuster lautet:

Liste
    ↓
Schleife
    ↓
Bedingung
    ↓
append()
    ↓
neue Liste


AUSPROBIEREN
------------
"""

# temperaturen = [15, 21, 18, 25, 30, 17]

# hohe_werte = []

# for temperatur in temperaturen:
#     if temperatur >= 20:
#         hohe_werte.append(temperatur)

# print(hohe_werte)


"""
2. TUPEL
========

Ein Tupel speichert ebenfalls mehrere Werte in einer festen Reihenfolge.

Ein Tupel wird normalerweise mit runden Klammern geschrieben.

Beispiel:
"""

# messbereich = (18.4, 23.1)

# print(messbereich)


"""
Die Werte können über ihren Index gelesen werden.
"""

# messbereich = (18.4, 23.1)

# print(messbereich[0])
# print(messbereich[1])


"""
Ein Tupel kann nach seiner Erstellung nicht verändert werden.

Das bedeutet:

- keine neuen Werte mit append()
- keine Werte über einen Index ersetzen
- keine Werte entfernen

Eine Liste ist dagegen veränderbar.


AUSPROBIEREN

Entferne die # und beobachte, was passiert.
"""

# messbereich = (18.4, 23.1)

# messbereich.append(25.0)


"""
Auch eine direkte Änderung über einen Index funktioniert
bei einem Tupel nicht.
"""

# messbereich = (18.4, 23.1)

# messbereich[0] = 20.0


"""
TUPLE UND FUNKTIONEN

Tupel sind praktisch, wenn mehrere zusammengehörige Werte
gemeinsam zurückgegeben werden sollen.

Beispiel:
"""

# def min_max(messwerte):
#     kleinster = min(messwerte)
#     groesster = max(messwerte)
#
#     return kleinster, groesster


"""
Die Funktion liefert damit zwei Werte zurück.

Python verpackt diese Werte als Tupel.
"""

# ergebnis = min_max([18.4, 21.7, 16.2, 23.1])

# print(ergebnis)


"""
Die Ausgabe lautet:

(16.2, 23.1)


Wir können die Werte auch direkt in zwei Variablen übernehmen.
"""

# kleinster, groesster = min_max([18.4, 21.7, 16.2, 23.1])

# print(kleinster)
# print(groesster)


"""
AUSPROBIEREN
------------
"""

# def min_max(messwerte):
#     kleinster = min(messwerte)
#     groesster = max(messwerte)
#
#     return kleinster, groesster
#
#
# werte = [12, 25, 8, 19]
#
# kleinster, groesster = min_max(werte)
#
# print("Kleinster Wert:", kleinster)
# print("Größter Wert:", groesster)


"""
TUPLE IN EINER SCHLEIFE
=======================

Ein Tupel kann auch direkt beim Durchlaufen einer Liste
in mehrere Variablen aufgeteilt werden.

Beispiel:
"""

# messdaten = [
#     ("Nord", 18.4),
#     ("Sued", 22.1),
#     ("Nord", 19.1)
# ]

# for station, messwert in messdaten:
#     print(station)
#     print(messwert)


"""
Bei jedem Durchlauf passiert automatisch:

("Nord", 18.4)

wird zu:

station = "Nord"
messwert = 18.4

Beim nächsten Durchlauf:

("Sued", 22.1)

wird zu:

station = "Sued"
messwert = 22.1

Das funktioniert, weil jedes Tupel genau zwei Werte enthält.


AUSPROBIEREN
------------
"""

# messdaten = [
#     ("Nord", 18.4),
#     ("Sued", 22.1),
#     ("Nord", 19.1)
# ]

# for station, messwert in messdaten:
#     print("Station:", station)
#     print("Messwert:", messwert)


"""
3. DICTIONARIES
===============

Ein Dictionary speichert Werte über Schlüssel.

Während eine Liste Werte über ihre Position anspricht,
verwendet ein Dictionary Schlüssel.

Beispiel:
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4,
#     "sensor": "temperatur"
# }


"""
Die Schlüssel sind hier:

"name"
"temperatur"
"sensor"

Die zugehörigen Werte sind:

"Nord"
18.4
"temperatur"


WERTE LESEN

Auf einen Wert greifen wir über seinen Schlüssel zu.
"""

# print(station["name"])
# print(station["temperatur"])


"""
Die Ausgabe lautet:

Nord
18.4


AUSPROBIEREN
------------
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4,
#     "sensor": "temperatur"
# }

# print(station["name"])
# print(station["sensor"])


"""
WERTE VERÄNDERN

Ein vorhandener Wert kann über seinen Schlüssel geändert werden.
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4
# }

# station["temperatur"] = 19.2

# print(station)


"""
NEUE WERTE HINZUFÜGEN

Auch neue Schlüssel können angelegt werden.
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4
# }

# station["status"] = "aktiv"

# print(station)


"""
Danach enthält das Dictionary zusätzlich:

"status": "aktiv"


AUSPROBIEREN
------------
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4
# }

# station["status"] = "aktiv"
# station["batterie"] = 87

# print(station)


"""
PRÜFEN, OB EIN SCHLÜSSEL VORHANDEN IST

Mit in können wir prüfen, ob ein Schlüssel existiert.
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4
# }

# if "temperatur" in station:
#     print("Temperatur vorhanden")


"""
AUSPROBIEREN
------------
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4,
#     "status": "aktiv"
# }

# if "status" in station:
#     print("Status vorhanden")

# if "batterie" in station:
#     print("Batterie vorhanden")


"""
DICTIONARIES ZUM ZÄHLEN

Ein Dictionary eignet sich auch zum Zählen.

Beispiel:
"""

# messwerte = [20, 21, 20, 19, 21, 20]

# zaehler = {}

# for messwert in messwerte:
#     if messwert in zaehler:
#         zaehler[messwert] = zaehler[messwert] + 1
#     else:
#         zaehler[messwert] = 1

# print(zaehler)


"""
Danach enthält zaehler:

{
    20: 3,
    21: 2,
    19: 1
}

Der Messwert ist hier der Schlüssel.

Die Anzahl ist der Wert.

Das Grundmuster lautet:

Wert vorhanden?
    ↓
Ja → Zähler erhöhen
Nein → Zähler mit 1 anlegen


AUSPROBIEREN
------------
"""

# statusmeldungen = [
#     "online",
#     "offline",
#     "online",
#     "wartung",
#     "offline",
#     "online"
# ]

# zaehler = {}

# for status in statusmeldungen:
#     if status in zaehler:
#         zaehler[status] = zaehler[status] + 1
#     else:
#         zaehler[status] = 1

# print(zaehler)


"""
4. SETS
=======

Ein Set speichert eindeutige Werte.

Doppelte Werte werden nur einmal gespeichert.

Beispiel:
"""

# stationen = {
#     "Nord",
#     "Sued",
#     "Nord",
#     "West"
# }

# print(stationen)


"""
Das Set enthält anschließend nur die eindeutigen Werte:

Nord
Sued
West

Die Reihenfolge eines Sets sollte dabei nicht als feste Reihenfolge
verstanden werden.


SETS AUS LISTEN ERSTELLEN

Aus einer Liste kann ein Set erstellt werden.

Das ist besonders praktisch, wenn Duplikate entfernt werden sollen.
"""

# stationen = [
#     "Nord",
#     "Sued",
#     "Nord",
#     "West",
#     "Sued"
# ]

# eindeutig = set(stationen)

# print(eindeutig)


"""
AUSPROBIEREN
------------
"""

# namen = [
#     "Ada",
#     "Ben",
#     "Ada",
#     "Clara",
#     "Ben"
# ]

# eindeutige_namen = set(namen)

# print(eindeutige_namen)


"""
GEMEINSAME WERTE FINDEN

Sets können miteinander verglichen werden.

Mit & erhalten wir die Schnittmenge.

Das bedeutet:

Welche Werte kommen in beiden Sets vor?
"""

# sensoren_a = {
#     "temperatur",
#     "druck",
#     "feuchtigkeit"
# }

# sensoren_b = {
#     "temperatur",
#     "licht",
#     "feuchtigkeit"
# }

# gemeinsam = sensoren_a & sensoren_b

# print(gemeinsam)


"""
Das Ergebnis enthält:

temperatur
feuchtigkeit

Diese beiden Werte kommen in beiden Sets vor.


AUSPROBIEREN
------------
"""

# gruppe_a = {"Python", "Git", "Linux"}
# gruppe_b = {"Python", "Docker", "Linux"}

# gemeinsam = gruppe_a & gruppe_b

# print(gemeinsam)


"""
Weitere Set-Operationen gibt es ebenfalls.

Zum Beispiel:

|   Vereinigungsmenge
&   Schnittmenge
-   Differenz


AUSPROBIEREN
------------
"""

# a = {"Python", "Git", "Linux"}
# b = {"Python", "Docker", "Linux"}

# print(a | b)
# print(a & b)
# print(a - b)


"""
5. sorted()
===========

Mit sorted() können Werte sortiert werden.

Beispiel:
"""

# messwerte = [21.4, 18.7, 23.1, 19.5]

# sortiert = sorted(messwerte)

# print(sortiert)


"""
Das Ergebnis ist:

[18.7, 19.5, 21.4, 23.1]


Wichtig:

sorted() erstellt eine neue sortierte Liste.

Die ursprüngliche Liste bleibt erhalten.
"""

# messwerte = [21.4, 18.7, 23.1, 19.5]

# sortiert = sorted(messwerte)

# print("Original:", messwerte)
# print("Sortiert:", sortiert)


"""
Das ist ein wichtiger Unterschied.

messwerte enthält weiterhin die ursprüngliche Reihenfolge.

sortiert enthält die neue sortierte Reihenfolge.


ABSTEIGEND SORTIEREN

Mit reverse=True wird absteigend sortiert.
"""

# messwerte = [21.4, 18.7, 23.1, 19.5]

# sortiert = sorted(
#     messwerte,
#     reverse=True
# )

# print(sortiert)


"""
Das Ergebnis ist:

[23.1, 21.4, 19.5, 18.7]


sorted() funktioniert nicht nur mit Zahlen.

Auch Strings können sortiert werden.
"""

# stationen = ["West", "Nord", "Sued"]

# sortiert = sorted(stationen)

# print(sortiert)


"""
Das Ergebnis ist:

["Nord", "Sued", "West"]


AUSPROBIEREN
------------
"""

# namen = ["Clara", "Ada", "Ben", "Dora"]

# print(sorted(namen))


"""
6. VERSCHACHTELTE DATENSTRUKTUREN
=================================

Datenstrukturen können miteinander kombiniert werden.

Zum Beispiel kann ein Dictionary eine Liste enthalten.

Beispiel:
"""

# station = {
#     "name": "Nord",
#     "temperaturen": [18.4, 19.1, 20.3]
# }


"""
Auf die Liste greifen wir so zu:
"""

# print(station["temperaturen"])


"""
Auf einen einzelnen Messwert greifen wir so zu:
"""

# print(station["temperaturen"][0])


"""
Das Ergebnis ist:

18.4


Hier passieren zwei Schritte:

1. station["temperaturen"]

   → holt die Liste

2. [0]

   → holt den ersten Wert aus dieser Liste


AUSPROBIEREN
------------
"""

# station = {
#     "name": "Nord",
#     "temperaturen": [18.4, 19.1, 20.3]
# }

# print(station["name"])
# print(station["temperaturen"])
# print(station["temperaturen"][0])
# print(station["temperaturen"][2])


"""
LISTE MIT DICTIONARIES

Mehrere Stationen können wiederum in einer Liste gespeichert werden.

Beispiel:
"""

# stationen = [
#     {
#         "name": "Nord",
#         "temperaturen": [18.0, 20.0]
#     },
#     {
#         "name": "Sued",
#         "temperaturen": [22.0, 24.0]
#     }
# ]


"""
Jetzt haben wir:

Liste
    ↓
Dictionary
    ↓
Liste

Diese Kombination ist in echten Programmen sehr häufig.


WERTE AUS DER VERSCHACHTELTEN STRUKTUR LESEN

Wir können Schritt für Schritt vorgehen.

Zuerst holen wir das erste Dictionary:
"""

# station = stationen[0]


"""
Jetzt können wir den Namen auslesen:
"""

# name = station["name"]


"""
Jetzt holen wir die Temperatur-Liste:
"""

# temperaturen = station["temperaturen"]


"""
Und jetzt können wir einen einzelnen Messwert lesen:
"""

# erste_temperatur = temperaturen[0]

# print(name)
# print(erste_temperatur)


"""
Das Ergebnis wäre:

Nord
18.0


SCHRITT FÜR SCHRITT

Bei verschachtelten Daten ist es oft einfacher,
nicht alles auf einmal zu schreiben.

Statt:

stationen[0]["temperaturen"][0]

kann man zunächst:

station = stationen[0]

dann:

temperaturen = station["temperaturen"]

und anschließend:

erste_temperatur = temperaturen[0]

verwenden.

Das macht komplexe Datenstrukturen leichter verständlich.


AUSPROBIEREN
------------
"""

# stationen = [
#     {
#         "name": "Nord",
#         "temperaturen": [18.0, 20.0]
#     },
#     {
#         "name": "Sued",
#         "temperaturen": [22.0, 24.0]
#     }
# ]

# station = stationen[0]
# temperaturen = station["temperaturen"]
# erste_temperatur = temperaturen[0]

# print(station)
# print(temperaturen)
# print(erste_temperatur)


"""
VERSCHACHTELTE DATEN MIT EINER SCHLEIFE

Wir können die komplette Liste mit einer Schleife verarbeiten.
"""

# stationen = [
#     {
#         "name": "Nord",
#         "temperaturen": [18.0, 20.0]
#     },
#     {
#         "name": "Sued",
#         "temperaturen": [22.0, 24.0]
#     }
# ]

# for station in stationen:
#     name = station["name"]
#     temperaturen = station["temperaturen"]
#
#     print(name)
#     print(temperaturen)


"""
Wir können auch die einzelnen Temperaturen durchlaufen.
"""

# for station in stationen:
#     name = station["name"]
#
#     print("Station:", name)
#
#     for temperatur in station["temperaturen"]:
#         print("Temperatur:", temperatur)


"""
Hier sehen wir erstmals eine verschachtelte Schleife.

Die äußere Schleife verarbeitet die Stationen.

Die innere Schleife verarbeitet die Temperaturen
der jeweiligen Station.


7. WELCHE DATENSTRUKTUR PASST?
==============================

Die verschiedenen Strukturen haben unterschiedliche Aufgaben.


LISTE
-----

Verwende eine Liste, wenn mehrere Werte in einer Reihenfolge
gespeichert werden sollen.

Beispiel:
"""

# temperaturen = [18.4, 19.1, 20.3]


"""
TUPLE
-----

Verwende ein Tupel, wenn mehrere zusammengehörige Werte
gemeinsam behandelt werden sollen und die Struktur nicht
verändert werden soll.

Beispiel:
"""

# messbereich = (18.4, 20.3)


"""
DICTIONARY
----------

Verwende ein Dictionary, wenn Werte über Namen oder Schlüssel
angesprochen werden sollen.

Beispiel:
"""

# station = {
#     "name": "Nord",
#     "temperatur": 18.4
# }


"""
SET
---

Verwende ein Set, wenn nur eindeutige Werte wichtig sind
oder Mengen miteinander verglichen werden sollen.

Beispiel:
"""

# sensoren = {
#     "temperatur",
#     "druck",
#     "feuchtigkeit"
# }


"""
VERSCHACHTELTE DATENSTRUKTUREN
------------------------------

Verwende Kombinationen, wenn die Daten selbst eine Struktur besitzen.

Beispiel:
"""

# stationen = [
#     {
#         "name": "Nord",
#         "temperaturen": [18.0, 20.0]
#     },
#     {
#         "name": "Sued",
#         "temperaturen": [22.0, 24.0]
#     }
# ]


"""
Eine wichtige Frage bei der Arbeit mit Daten lautet deshalb:

Welche Struktur passt zu meinen Daten?

Die richtige Datenstruktur kann den späteren Code deutlich
einfacher machen.


8. HÄUFIGE FEHLER
=================


LISTE UND SET VERWECHSELN
-------------------------

Eine Liste kann doppelte Werte enthalten.
"""

# werte = [20, 20, 21]


"""
Ein Set enthält jeden Wert nur einmal.
"""

# werte = {20, 21}


"""
Wenn die Reihenfolge wichtig ist, ist eine Liste häufig die
passendere Struktur.

Wenn nur eindeutige Werte wichtig sind, kann ein Set sinnvoll sein.


FALSCHEN DICTIONARY-SCHLÜSSEL VERWENDEN
---------------------------------------

Bei einem Dictionary muss der Schlüssel vorhanden sein.
"""

# station = {
#     "name": "Nord"
# }

# print(station["temperatur"])


"""
Hier gibt es keinen Schlüssel "temperatur".

Python meldet deshalb einen Fehler.


INDEX AUSSERHALB EINER LISTE
----------------------------

Beispiel:
"""

# werte = [10, 20, 30]

# print(werte[3])


"""
Die gültigen Indizes sind:

0
1
2

Der Index 3 existiert nicht.


SORTIERUNG VERWECHSELN
----------------------

sorted() erstellt eine neue sortierte Liste.

Beispiel:
"""

# werte = [30, 10, 20]

# sortiert = sorted(werte)

# print(werte)
# print(sortiert)


"""
Die ursprüngliche Liste bleibt unverändert.


SET-REIHENFOLGE
---------------

Bei einem Set sollte man sich nicht auf eine bestimmte Reihenfolge
verlassen.

Wenn eine sortierte Liste benötigt wird, kann sorted() verwendet werden.
"""

# sensoren = {
#     "druck",
#     "licht",
#     "temperatur"
# }

# sortiert = sorted(sensoren)

# print(sortiert)


"""
9. VERGLEICH DER DATENSTRUKTUREN
================================

LISTE

Beispiel:

[10, 20, 30]

Eigenschaften:

- Reihenfolge
- Indexzugriff
- veränderbar
- Duplikate möglich


TUPLE

Beispiel:

(10, 20, 30)

Eigenschaften:

- Reihenfolge
- Indexzugriff
- nach der Erstellung nicht veränderbar


DICTIONARY

Beispiel:

{
    "name": "Nord",
    "temperatur": 18.4
}

Eigenschaften:

- Schlüssel und Werte
- Zugriff über Schlüssel
- Werte können verändert werden
- gut für strukturierte Informationen


SET

Beispiel:

{10, 20, 30}

Eigenschaften:

- eindeutige Werte
- keine verlässliche Reihenfolge
- praktisch für Mengenoperationen
- Duplikate werden entfernt


SORTIEREN

sorted()

liefert eine neue sortierte Liste zurück.


VERSCHACHTELUNG

Datenstrukturen können kombiniert werden.

Zum Beispiel:

Liste
    ↓
Dictionary
    ↓
Liste

Das ist besonders praktisch für strukturierte Datensätze.
"""


"""
10. KLEINE ÜBUNG ZUM AUSPROBIEREN
=================================

Versuche, die folgenden Daten zu verarbeiten.

Wir haben mehrere Server:
"""

# server = [
#     {
#         "name": "web01",
#         "status": "online"
#     },
#     {
#         "name": "web02",
#         "status": "offline"
#     },
#     {
#         "name": "db01",
#         "status": "online"
#     }
# ]


"""
Aufgabe 1:

Gib die Namen aller Server aus.
"""

# for eintrag in server:
#     print(eintrag["name"])


"""
Aufgabe 2:

Gib nur die Server aus, die online sind.
"""

# for eintrag in server:
#     if eintrag["status"] == "online":
#         print(eintrag["name"])


"""
Aufgabe 3:

Erstelle eine neue Liste mit den Namen der Online-Server.
"""

# online_server = []

# for eintrag in server:
#     if eintrag["status"] == "online":
#         online_server.append(eintrag["name"])

# print(online_server)


"""
Aufgabe 4:

Sortiere die Namen alphabetisch.
"""

# sortiert = sorted(online_server)

# print(sortiert)


"""
11. ZUSAMMENFASSUNG
===================

Heute hast du mehrere wichtige Datenstrukturen kennengelernt.


LISTE

Mehrere Werte in einer Reihenfolge.

Beispiel:

[10, 20, 30]


TUPLE

Zusammengehörige Werte in einer festen Struktur.

Beispiel:

(10, 20, 30)


DICTIONARY

Schlüssel → Wert

Beispiel:

{
    "name": "Nord",
    "temperatur": 18.4
}


SET

Eindeutige Werte.

Beispiel:

{"Nord", "Sued", "West"}


sorted()

Erstellt eine neue sortierte Liste.


VERSCHACHTELTE DATEN

Datenstrukturen können miteinander kombiniert werden.

Beispiel:

Liste
    ↓
Dictionary
    ↓
Liste


Besonders wichtig ist nicht nur die Syntax.

Du solltest zunehmend überlegen:

Welche Daten habe ich?

Wie möchte ich darauf zugreifen?

Muss die Reihenfolge erhalten bleiben?

Dürfen Werte doppelt vorkommen?

Brauche ich Schlüssel?

Möchte ich die Daten später verändern?


Wenn diese Fragen beantwortet sind, wird die Wahl der
passenden Datenstruktur deutlich einfacher.


12. AUSBLICK AUF TAG 3
======================

Am nächsten Tag verlassen wir die Daten, die direkt im
Python-Programm stehen.

Wir schauen uns Dateien an und lernen, wie Python Daten
dauerhaft speichern und wieder einlesen kann.

Dabei geht es unter anderem um:

- Textdateien
- CSV-Dateien
- JSON-Dateien
- Dateien lesen
- Dateien schreiben
- strukturierte Daten aus Dateien verarbeiten


ENDE TAG 2
==========
"""