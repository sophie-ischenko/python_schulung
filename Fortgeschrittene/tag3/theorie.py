"""
Python Tag 3 – Dateien, Fehler und Module

Bisher lagen unsere Daten direkt im Python-Programm.

Das ist für Übungen praktisch, aber ein echtes Programm soll Daten
auch speichern und wieder laden können.

Außerdem müssen Programme mit Problemen umgehen können,
ohne sofort abzubrechen.

Heute lernst du:

- Dateien lesen und schreiben
- Fehler mit try und except behandeln
- eigene Fehler mit raise auslösen
- CSV-Dateien lesen
- JSON-Dateien lesen und schreiben
- Module der Standardbibliothek verwenden
- Dateipfade mit pathlib verwalten


LERNZIELE
=========

Nach diesem Tag kannst du:

- Textdateien lesen
- Textdateien schreiben
- Text an Dateien anhängen
- Fehler erkennen und gezielt behandeln
- eigene Fehler mit raise auslösen
- CSV-Dateien mit csv lesen
- JSON-Dateien mit json lesen und schreiben
- Module importieren
- Dateipfade mit pathlib verwalten
- mehrere dieser Bausteine miteinander kombinieren


WICHTIG FÜR DIESES DOKUMENT
===========================

Die Codebeispiele sind absichtlich auskommentiert.

Wenn du ein Beispiel ausprobieren möchtest,
entferne einfach das # vor den entsprechenden Codezeilen.

Beispiel:

# print("Hallo")

wird zu:

print("Hallo")

Danach kannst du die Datei ausführen und direkt sehen,
was Python macht.
"""


"""
1. DATEIEN LESEN
================

Mit open() können wir eine Datei öffnen.

Zum Lesen reicht grundsätzlich:
"""

# datei = open("notizen.txt", encoding="utf-8")


"""
Für die praktische Arbeit ist die Verwendung von with besser.

Beispiel:
"""

# with open("notizen.txt", encoding="utf-8") as datei:
#     inhalt = datei.read()


"""
with sorgt dafür, dass die Datei nach der Verwendung
automatisch geschlossen wird.

Das ist die übliche Schreibweise für die Arbeit mit Dateien.


EINE DATEI KOMPLETT LESEN
-------------------------

Mit read() lesen wir den gesamten Inhalt einer Datei.
"""

# with open("notizen.txt", encoding="utf-8") as datei:
#     inhalt = datei.read()

# print(inhalt)


"""
AUSPROBIEREN
------------

Lege im gleichen Ordner wie diese Datei eine Datei
namens notizen.txt an.

Schreibe beispielsweise:

Erste Notiz
Zweite Notiz
Python macht Spaß

Danach kannst du dieses Beispiel ausführen.
"""

# with open("notizen.txt", encoding="utf-8") as datei:
#     inhalt = datei.read()

# print(inhalt)


"""
DATEI ZEILENWEISE LESEN
-----------------------

Eine Datei kann auch mit einer for-Schleife durchlaufen werden.
"""

# with open("notizen.txt", encoding="utf-8") as datei:
#     for zeile in datei:
#         print(zeile)


"""
Dabei enthält zeile normalerweise noch den Zeilenumbruch
am Ende der Zeile.

Wir können diesen entfernen.

Dafür verwenden wir rstrip().
"""

# with open("notizen.txt", encoding="utf-8") as datei:
#     for zeile in datei:
#         zeile = zeile.rstrip("\n")
#         print(zeile)


"""
ZEILEN IN EINER LISTE SPEICHERN
-------------------------------

Wir können die einzelnen Zeilen auch in einer Liste speichern.
"""

# zeilen = []

# with open("notizen.txt", encoding="utf-8") as datei:
#     for zeile in datei:
#         zeilen.append(zeile.rstrip("\n"))

# print(zeilen)


"""
Danach enthält zeilen beispielsweise:

[
    "Erste Notiz",
    "Zweite Notiz",
    "Python macht Spaß"
]


Hier verbinden wir bereits zwei Themen:

Dateien
    ↓
for-Schleife
    ↓
Liste


AUSPROBIEREN
------------
"""

# zeilen = []

# with open("notizen.txt", encoding="utf-8") as datei:
#     for zeile in datei:
#         zeilen.append(zeile.rstrip("\n"))

# for zeile in zeilen:
#     print(zeile)


"""
2. DATEIEN SCHREIBEN
====================

Zum Schreiben wird open() mit dem Modus "w" verwendet.

Beispiel:
"""

# with open("notizen.txt", "w", encoding="utf-8") as datei:
#     datei.write("Erste Notiz\n")
#     datei.write("Zweite Notiz\n")


"""
Der Modus "w" bedeutet:

Datei zum Schreiben öffnen.

Wichtig:

Wenn die Datei bereits existiert, wird ihr bisheriger Inhalt
überschrieben.


AUSPROBIEREN
------------
"""

# with open("test.txt", "w", encoding="utf-8") as datei:
#     datei.write("Hallo Python!\n")
#     datei.write("Das ist meine erste Datei.\n")


"""
TEXT ANHÄNGEN
=============

Mit "a" wird neuer Inhalt an eine vorhandene Datei angehängt.

Der bisherige Inhalt bleibt erhalten.
"""

# with open("notizen.txt", "a", encoding="utf-8") as datei:
#     datei.write("Neue Notiz\n")


"""
Wenn wir das Beispiel mehrfach ausführen,
wird jedes Mal eine weitere Zeile angehängt.


AUSPROBIEREN
------------
"""

# with open("notizen.txt", "a", encoding="utf-8") as datei:
#     datei.write("Noch eine Notiz\n")


"""
DIE WICHTIGSTEN DATEIMODI
==========================

"r"
    lesen

"w"
    schreiben
    vorhandenen Inhalt ersetzen

"a"
    neuen Inhalt anhängen


Wenn kein Modus angegeben wird, wird standardmäßig gelesen.

Diese beiden Varianten sind deshalb gleich:

with open("notizen.txt", encoding="utf-8") as datei:
    ...

und:

with open("notizen.txt", "r", encoding="utf-8") as datei:
    ...


MERKSATZ

Dateien möglichst mit with öffnen.

Bei Textdateien sollte die Codierung utf-8 angegeben werden.
"""


"""
3. FEHLER VERSTEHEN
===================

Nicht jeder Programmablauf funktioniert erfolgreich.

Zum Beispiel:
"""

# zahl = int("Hallo")


"""
Python kann "Hallo" nicht in eine ganze Zahl umwandeln.

Es entsteht ein:

ValueError


Ein anderer Fehler entsteht beim Öffnen einer Datei,
die nicht existiert.

Beispiel:
"""

# with open("nicht_da.txt", encoding="utf-8") as datei:
#     inhalt = datei.read()


"""
Hier entsteht normalerweise:

FileNotFoundError


Fehler gehören zum Programmieren dazu.

Wichtig ist deshalb nicht, dass niemals ein Fehler auftritt.

Wichtig ist, dass wir verstehen, was der Fehler bedeutet
und wie wir sinnvoll damit umgehen können.
"""


"""
4. FEHLER MIT try UND except BEHANDELN
======================================

Mit try sagen wir:

"Versuche diesen Code auszuführen."

Mit except sagen wir:

"Wenn ein bestimmter Fehler auftritt,
reagiere darauf."


Beispiel:
"""

# try:
#     alter = int(input("Alter: "))
# except ValueError:
#     print("Bitte eine ganze Zahl eingeben.")


"""
Wenn die Eingabe beispielsweise:

25

lautet, funktioniert die Umwandlung.

Bei:

Hallo

wird der except-Block ausgeführt.


AUSPROBIEREN
------------
"""

# try:
#     zahl = int(input("Gib eine Zahl ein: "))
#     print("Deine Zahl ist:", zahl)
# except ValueError:
#     print("Das war keine gültige Zahl.")


"""
Das Programm bricht bei einer ungültigen Eingabe
nicht einfach mit einer Fehlermeldung ab.

Stattdessen können wir selbst eine passende Nachricht ausgeben.


FEHLERGENAUER UNTERSUCHEN
=========================

Mit as können wir den Fehler in einer Variablen speichern.
"""

# try:
#     zahl = int("Hallo")
# except ValueError as fehler:
#     print(fehler)


"""
Damit erhalten wir die konkrete Fehlermeldung von Python.


AUSPROBIEREN
------------
"""

# try:
#     zahl = int("abc")
# except ValueError as fehler:
#     print("Es ist ein Fehler aufgetreten:")
#     print(fehler)


"""
MEHRERE FEHLER BEHANDELN
========================

Unterschiedliche Fehler können unterschiedliche Ursachen haben.

Beispiel:
"""

# try:
#     with open("daten.txt", encoding="utf-8") as datei:
#         zahl = int(datei.read())
#
# except FileNotFoundError:
#     print("Die Datei wurde nicht gefunden.")
#
# except ValueError:
#     print("Die Datei enthält keine gültige Zahl.")


"""
Hier behandeln wir zwei verschiedene Situationen:

FileNotFoundError
    Die Datei existiert nicht.

ValueError
    Der Inhalt kann nicht in eine Zahl umgewandelt werden.

Das ist besser, als für beide Probleme dieselbe Fehlermeldung
auszugeben.


AUSPROBIEREN
------------
"""

# try:
#     zahl = int(input("Gib eine Zahl ein: "))
#     print("Zahl:", zahl)
#
# except ValueError:
#     print("Die Eingabe war keine Zahl.")
#
# except TypeError:
#     print("Der Datentyp konnte nicht verarbeitet werden.")


"""
5. else UND finally
===================

Neben try und except gibt es:

else
finally


ELSE
----

Der else-Block wird ausgeführt,
wenn im try-Block kein Fehler aufgetreten ist.

Beispiel:
"""

# try:
#     zahl = int(input("Zahl: "))
#
# except ValueError:
#     print("Ungültige Eingabe.")
#
# else:
#     print("Die Zahl ist:", zahl)


"""
Der Ablauf ist:

try
    ↓
Fehler?
    ↓
Ja → except
Nein → else


FINALLY
=======

Der finally-Block wird unabhängig davon ausgeführt,
ob ein Fehler aufgetreten ist.
"""

# try:
#     zahl = int(input("Zahl: "))
#
# except ValueError:
#     print("Ungültige Eingabe.")
#
# finally:
#     print("Dieser Teil wird immer ausgeführt.")


"""
Der Ablauf ist:

try
    ↓
Fehler?
    ↓
except oder weiter
    ↓
finally


Für den Alltag werden vor allem try und except benötigt.

else und finally sind zusätzliche Werkzeuge,
wenn ein Programm genauer strukturiert werden soll.
"""


"""
6. NUR KONKRETE FEHLER ABFANGEN
================================

Vermeide möglichst:

except:

Denn damit werden praktisch alle Fehler abgefangen.

Das kann echte Programmierfehler verstecken.

Ungünstig:
"""

# try:
#     zahl = int(eingabe)
# except:
#     print("Fehler")


"""
Besser:

"""

# try:
#     zahl = int(eingabe)
# except ValueError:
#     print("Bitte eine Zahl eingeben.")


"""
Hier ist klar, welcher Fehler erwartet wird.

MERKSATZ

Fange den Fehler ab, mit dem du sinnvoll umgehen kannst.
"""


"""
7. EIGENE FEHLER MIT raise AUSLÖSEN
===================================

Bisher haben wir Fehler behandelt,
die Python selbst ausgelöst hat.

Eine Funktion kann aber auch selbst feststellen:

"Diese Eingabe ist nicht erlaubt."

Dann können wir mit raise einen Fehler auslösen.


Beispiel:
"""

# def pruefe_betrag(betrag):
#     if betrag == 0:
#         raise ValueError("Der Betrag darf nicht 0 sein.")
#
#     return betrag


"""
Wenn wir schreiben:

pruefe_betrag(0)

wird ein ValueError ausgelöst.
"""

# pruefe_betrag(0)


"""
Warum sollte eine Funktion selbst einen Fehler auslösen?

Eine Funktion sollte nicht einfach falsche Daten akzeptieren.

Beispiel:

Ein Haushaltsbuch darf möglicherweise keine Buchung
mit einem Betrag von 0 akzeptieren.
"""

# def buchung_hinzufuegen(betrag):
#     if betrag == 0:
#         raise ValueError("Der Betrag darf nicht 0 sein.")
#
#     print("Buchung hinzugefügt.")


"""
Der Code, der die Funktion aufruft,
kann entscheiden, was danach passieren soll.

Zum Beispiel:
"""

# try:
#     buchung_hinzufuegen(0)
#
# except ValueError as fehler:
#     print("Fehler:", fehler)


"""
ZUSAMMENSPIEL VON raise UND except

raise
    ↓
löst einen Fehler aus

except
    ↓
fängt einen Fehler ab


Das Grundprinzip:

Funktion
    ↓
raise ValueError
    ↓
Fehler entsteht
    ↓
Aufrufer
    ↓
except ValueError
    ↓
Fehler behandeln


MERKSATZ

raise löst einen Fehler aus.

except fängt einen Fehler ab.


AUSPROBIEREN
------------
"""

# def pruefe_alter(alter):
#     if alter < 0:
#         raise ValueError("Das Alter darf nicht negativ sein.")
#
#     return alter


# try:
#     pruefe_alter(-5)
#
# except ValueError as fehler:
#     print("Fehler:", fehler)


"""
8. CSV-DATEIEN
==============

CSV steht für:

Comma-Separated Values

Eine CSV-Datei speichert tabellarische Daten.

Beispiel:

datum,kategorie,betrag
01.10.2026,Essen,-25.50
02.10.2026,Gehalt,3000.00
03.10.2026,Tanken,-60.00


CSV eignet sich besonders für Tabellen und Daten,
die beispielsweise aus Tabellenprogrammen exportiert wurden.

Python stellt dafür das Modul csv bereit.
"""

# import csv


"""
CSV MIT DictReader LESEN
========================

Mit csv.DictReader werden die Spaltennamen zu
Dictionary-Schlüsseln.

Beispiel:
"""

# import csv
#
# with open(
#     "ausgaben.csv",
#     encoding="utf-8",
#     newline=""
# ) as datei:
#
#     reader = csv.DictReader(datei)
#
#     for zeile in reader:
#         print(zeile)


"""
Eine Zeile sieht dann ungefähr so aus:

{
    "datum": "01.10.2026",
    "kategorie": "Essen",
    "betrag": "-25.50"
}


Die Daten passen damit direkt zu unseren Kenntnissen
über Dictionaries.


WICHTIG

Die Werte aus einer CSV-Datei sind zunächst Text.

Zum Beispiel:
"""

# betrag = zeile["betrag"]


"""
liefert:

"-25.50"

Das ist ein String.

Wenn wir damit rechnen möchten,
müssen wir ihn umwandeln:

"""

# betrag = float(zeile["betrag"])


"""
AUSPROBIEREN
------------

Erstelle eine Datei namens ausgaben.csv.

Beispielinhalt:

datum,kategorie,betrag
01.10.2026,Essen,-25.50
02.10.2026,Gehalt,3000.00
03.10.2026,Tanken,-60.00
"""

# import csv
#
# with open(
#     "ausgaben.csv",
#     encoding="utf-8",
#     newline=""
# ) as datei:
#
#     reader = csv.DictReader(datei)
#
#     for zeile in reader:
#         kategorie = zeile["kategorie"]
#         betrag = float(zeile["betrag"])
#
#         print(kategorie, betrag)


"""
Hier verbinden wir:

Datei
    ↓
CSV
    ↓
Dictionary
    ↓
String
    ↓
float


CSV UND DICTIONARIES

Wir können die Daten weiterverarbeiten.

Beispiel:
"""

# import csv
#
# with open(
#     "ausgaben.csv",
#     encoding="utf-8",
#     newline=""
# ) as datei:
#
#     reader = csv.DictReader(datei)
#
#     for zeile in reader:
#         kategorie = zeile["kategorie"]
#         betrag = float(zeile["betrag"])
#
#         print("Kategorie:", kategorie)
#         print("Betrag:", betrag)


"""
9. JSON-DATEIEN
===============

JSON steht für:

JavaScript Object Notation

JSON kann strukturierte Daten speichern.

Beispiel:

{
    "name": "Nord",
    "temperaturen": [18.4, 19.1, 20.3]
}


JSON passt sehr gut zu Python-Dictionaries und Listen.

Python stellt dafür das Modul json bereit.
"""

# import json


"""
10. JSON SCHREIBEN
==================

Mit json.dump() können Python-Daten in eine Datei
geschrieben werden.

Beispiel:
"""

# import json
#
# daten = {
#     "name": "Nord",
#     "temperaturen": [18.4, 19.1, 20.3]
# }
#
# with open(
#     "daten.json",
#     "w",
#     encoding="utf-8"
# ) as datei:
#
#     json.dump(
#         daten,
#         datei,
#         ensure_ascii=False,
#         indent=2
#     )


"""
indent=2

sorgt für eine besser lesbare Formatierung.


ensure_ascii=False

sorgt dafür, dass beispielsweise deutsche Umlaute
nicht unnötig in Unicode-Schreibweise umgewandelt werden.


AUSPROBIEREN
------------
"""

# import json
#
# daten = {
#     "name": "Nord",
#     "status": "aktiv",
#     "temperaturen": [18.4, 19.1, 20.3]
# }
#
# with open(
#     "daten.json",
#     "w",
#     encoding="utf-8"
# ) as datei:
#
#     json.dump(
#         daten,
#         datei,
#         ensure_ascii=False,
#         indent=2
#     )


"""
Öffne danach die Datei daten.json.

Du kannst sehen, wie aus einem Python-Dictionary
eine JSON-Datei geworden ist.
"""


"""
11. JSON LESEN
==============

Mit json.load() wird eine JSON-Datei wieder eingelesen.
"""

# import json
#
# with open(
#     "daten.json",
#     encoding="utf-8"
# ) as datei:
#
#     daten = json.load(datei)


"""
Danach können wir die Daten wie normale Python-Daten verwenden.
"""

# print(daten["name"])
# print(daten["temperaturen"])


"""
AUSPROBIEREN
------------
"""

# import json
#
# with open("daten.json", encoding="utf-8") as datei:
#     daten = json.load(datei)
#
# print("Name:", daten["name"])
# print("Temperaturen:", daten["temperaturen"])


"""
JSON UND PYTHON

Typische Zuordnungen:

JSON              Python

Objekt            Dictionary
Array             Liste
String            String
Zahl              int / float
true              True
false             False
null              None


Damit können wir Daten aus Tag 2 dauerhaft speichern.
"""


"""
12. JSON UND FEHLERBEHANDLUNG KOMBINIEREN
=========================================

Beim Laden einer Datei können verschiedene Probleme auftreten.

Die Datei könnte fehlen:

FileNotFoundError

Oder der Inhalt könnte kein gültiges JSON sein:

json.JSONDecodeError


Beide Fälle können getrennt behandelt werden.
"""

# import json
#
# try:
#     with open("daten.json", encoding="utf-8") as datei:
#         daten = json.load(datei)
#
# except FileNotFoundError:
#     daten = {}
#
# except json.JSONDecodeError:
#     daten = {}


"""
Das Programm kann in beiden Fällen mit einem leeren
Dictionary starten.


AUSPROBIEREN
------------
"""

# import json
#
# try:
#     with open("daten.json", encoding="utf-8") as datei:
#         daten = json.load(datei)
#
# except FileNotFoundError:
#     print("Die Datei existiert noch nicht.")
#     daten = {}
#
# except json.JSONDecodeError:
#     print("Die JSON-Datei ist ungültig.")
#     daten = {}
#
# print(daten)


"""
Dieses Muster ist besonders nützlich für Programme,
die beim Start gespeicherte Daten laden.


13. MODULE
==========

Ein Modul ist eine Python-Datei mit wiederverwendbarem Code.

Python bringt bereits viele Module mit.

Diese Sammlung nennt man:

Standardbibliothek


Wir müssen viele nützliche Funktionen deshalb nicht selbst
programmieren.

Ein Modul wird mit import eingebunden.

Beispiel:
"""

# import json


"""
Danach können wir Funktionen aus dem Modul verwenden.
"""

# json.load(datei)
# json.dump(daten, datei)


"""
Ein weiteres Beispiel:
"""

# import csv


"""
Danach können wir beispielsweise verwenden:

"""

# csv.DictReader(datei)


"""
Warum Module verwenden?

Ohne Module müssten wir viele Werkzeuge selbst programmieren.

Mit der Standardbibliothek können wir vorhandene Werkzeuge nutzen.

Weitere Module, die Python mitbringt, lernen wir später
bei Bedarf kennen.


AUSPROBIEREN
------------
"""

# import math

# print(math.sqrt(25))


"""
Hier verwenden wir das Modul math.

sqrt() berechnet die Quadratwurzel.


Ein weiteres Modul:
"""

# import random

# zahl = random.randint(1, 10)

# print(zahl)


"""
random.randint() erzeugt eine zufällige ganze Zahl
innerhalb des angegebenen Bereichs.


Wichtig:

Module werden importiert, wenn wir Funktionen oder Werkzeuge
aus diesem Modul verwenden möchten.
"""


"""
14. pathlib
==========

Das Modul pathlib hilft bei der Arbeit mit Dateipfaden.

Wir können Path so importieren:
"""

# from pathlib import Path


"""
Ein Pfad kann anschließend erstellt werden:
"""

# ordner = Path("daten")


"""
Eine Datei innerhalb dieses Ordners:
"""

# datei = ordner / "messwerte.json"


"""
Das / zwischen zwei Path-Objekten verbindet die Pfade.

Das ist besonders praktisch, weil pathlib die Unterschiede
zwischen den Betriebssystemen berücksichtigt.


AUSPROBIEREN
------------
"""

# from pathlib import Path
#
# ordner = Path("daten")
# datei = ordner / "messwerte.json"
#
# print(ordner)
# print(datei)


"""
PRÜFEN, OB EINE DATEI EXISTIERT
===============================

Mit exists() können wir prüfen,
ob ein Pfad vorhanden ist.
"""

# from pathlib import Path
#
# pfad = Path("daten.json")
#
# if pfad.exists():
#     print("Datei vorhanden")
# else:
#     print("Datei fehlt")


"""
DATEIENDUNG AUSLESEN
====================

Mit suffix erhalten wir die Dateiendung.
"""

# from pathlib import Path
#
# pfad = Path("messwerte.csv")
#
# print(pfad.suffix)


"""
Die Ausgabe ist:

.csv


AUSPROBIEREN
------------
"""

# from pathlib import Path
#
# pfade = [
#     Path("daten.json"),
#     Path("ausgaben.csv"),
#     Path("notizen.txt")
# ]
#
# for pfad in pfade:
#     print(pfad.name, "→", pfad.suffix)


"""
DATEI MIT pathlib ÖFFNEN
========================

Ein Path-Objekt kann direkt an open() übergeben werden.

Wir können also einen Dateipfad mit pathlib erstellen
und diesen anschließend mit open() verwenden.
"""

# from pathlib import Path

# pfad = Path("daten") / "messwerte.json"

# with open(pfad, encoding="utf-8") as datei:
#     inhalt = datei.read()

# print(inhalt)


"""
Das ist besonders praktisch, weil wir den Dateipfad
nicht als langen String zusammensetzen müssen.

pathlib kümmert sich um den Pfad.

open() kümmert sich um das Öffnen der Datei.
"""


"""
DATEIEN IN EINEM ORDNER ANZEIGEN
================================

Mit iterdir() können wir den Inhalt eines Ordners
durchlaufen.
"""

# from pathlib import Path
#
# ordner = Path("daten")
#
# for datei in ordner.iterdir():
#     print(datei.name)

"""
Wir können prüfen, ob ein Eintrag tatsächlich eine Datei ist.
"""

# from pathlib import Path
#
# ordner = Path("daten")
#
# for datei in ordner.iterdir():
#     if datei.is_file():
#         print(datei.name)


"""
Warum pathlib?

Ein Dateipfad kann je nach Betriebssystem unterschiedlich aussehen.

pathlib übernimmt diese Unterschiede für uns.

Zum Beispiel:

Path("daten") / "messwerte.json"

funktioniert unter Windows, macOS und Linux.


AUSPROBIEREN
------------
"""

# from pathlib import Path
#
# pfad = Path("daten") / "messwerte.json"
#
# print(pfad)
# print(pfad.exists())
# print(pfad.suffix)


"""
15. DATEIEN, DATEN UND FEHLER ZUSAMMENBRINGEN
=============================================

Jetzt können wir die einzelnen Themen miteinander verbinden.

Stell dir ein Programm vor, das Messdaten dauerhaft speichern soll.

Die Daten liegen zunächst in Python:
"""

# messdaten = {
#     "Nord": {
#         "temperaturen": [18.4, 19.1, 20.3]
#     }
# }


"""
Wir können diese Daten als JSON speichern:
"""

# import json
#
# messdaten = {
#     "Nord": {
#         "temperaturen": [18.4, 19.1, 20.3]
#     }
# }
#
# with open(
#     "messdaten.json",
#     "w",
#     encoding="utf-8"
# ) as datei:
#
#     json.dump(
#         messdaten,
#         datei,
#         ensure_ascii=False,
#         indent=2
#     )


"""
Beim nächsten Programmstart laden wir sie wieder:
"""

# import json
#
# try:
#     with open(
#         "messdaten.json",
#         encoding="utf-8"
#     ) as datei:
#
#         messdaten = json.load(datei)
#
# except FileNotFoundError:
#     messdaten = {}


"""
Damit entsteht ein vollständiger Ablauf:

Python-Daten
    ↓
JSON-Datei
    ↓
Programm wird beendet
    ↓
Programm startet erneut
    ↓
JSON-Datei lesen
    ↓
Python-Daten


Genau dadurch werden aus vorübergehenden Programmdaten
dauerhaft gespeicherte Daten.


AUSPROBIEREN
------------

Hier kannst du den gesamten Ablauf selbst testen.
"""

# import json
#
#
# messdaten = {
#     "Nord": {
#         "temperaturen": [18.4, 19.1, 20.3]
#     }
# }
#
#
# with open(
#     "messdaten.json",
#     "w",
#     encoding="utf-8"
# ) as datei:
#
#     json.dump(
#         messdaten,
#         datei,
#         ensure_ascii=False,
#         indent=2
#     )
#
#
# with open(
#     "messdaten.json",
#     encoding="utf-8"
# ) as datei:
#
#     geladene_daten = json.load(datei)
#
#
# print(geladene_daten)


"""
16. pathlib UND JSON KOMBINIEREN
================================

pathlib und json können ebenfalls gemeinsam verwendet werden.

Beispiel:
"""

# from pathlib import Path
# import json
#
#
# pfad = Path("daten") / "messdaten.json"
#
#
# with open(
#     pfad,
#     "w",
#     encoding="utf-8"
# ) as datei:
#
#     json.dump(
#         messdaten,
#         datei,
#         ensure_ascii=False,
#         indent=2
#     )


"""
Damit können Dateipfade sauber getrennt von den eigentlichen
Daten behandelt werden.


17. HÄUFIGE FEHLER
==================


DATEI OHNE with ÖFFNEN
----------------------

Ungünstig:

"""

# datei = open("daten.txt")


"""
Besser:

"""

# with open("daten.txt", encoding="utf-8") as datei:
#     ...


"""
with sorgt dafür, dass die Datei nach der Verwendung
ordnungsgemäß geschlossen wird.


FALSCHE CODIERUNG
-----------------

Bei deutschen Texten kann eine fehlende oder falsche Codierung
zu Problemen mit Umlauten führen.

Deshalb:

"""

# with open("daten.txt", encoding="utf-8") as datei:
#     ...


"""
CSV-WERTE DIREKT BERECHNEN
--------------------------

Das hier funktioniert nicht wie erwartet:

"""

# betrag = zeile["betrag"]
# summe = summe + betrag


"""
Denn betrag ist zunächst ein String.

Richtig:

"""

# betrag = float(zeile["betrag"])


"""
ALLE FEHLER PAUSCHAL ABFANGEN
----------------------------

Ungünstig:

"""

# try:
#     ...
# except:
#     print("Irgendwas ist schiefgegangen.")


"""
Besser:

"""

# try:
#     ...
# except ValueError:
#     print("Ungültige Zahl.")


"""
raise UND print VERWECHSELN
--------------------------

Das hier zeigt zwar eine Meldung:

"""

# print("Betrag ist ungültig.")


"""
Aber es wird kein Fehler ausgelöst.

Mit raise wird tatsächlich ein Fehler ausgelöst:

"""

# raise ValueError("Betrag ist ungültig.")


"""
JSON UND CSV VERWECHSELN
------------------------

CSV eignet sich besonders für tabellarische Daten.

Beispiel:

datum,kategorie,betrag
01.10.2026,Essen,-25.50


JSON eignet sich besonders für strukturierte und
verschachtelte Daten.

Beispiel:

{
    "name": "Nord",
    "temperaturen": [18.4, 19.1, 20.3]
}


MERKSATZ

CSV → Tabellen

JSON → strukturierte Daten
"""


"""
18. KLEINE ÜBUNG: NOTIZEN SPEICHERN
===================================

Wir können jetzt mehrere Themen miteinander verbinden.

Aufgabe:

Schreibe ein kleines Programm, das eine Notiz vom Benutzer
entgegennimmt und in einer Textdatei speichert.

Der Benutzer gibt beispielsweise ein:

Was möchtest du notieren? Python lernen


Die Notiz soll anschließend in notizen.txt gespeichert werden.


ERSTER SCHRITT

Eingabe abfragen:
"""

# notiz = input("Was möchtest du notieren? ")


"""
ZWEITER SCHRITT

Notiz speichern:
"""

# with open("notizen.txt", "a", encoding="utf-8") as datei:
#     datei.write(notiz + "\n")


"""
DRITTER SCHRITT

Die Datei anschließend wieder lesen:
"""

# with open("notizen.txt", encoding="utf-8") as datei:
#     for zeile in datei:
#         print(zeile.rstrip("\n"))


"""
Versuche anschließend selbst, die Aufgabe zu erweitern.

Zum Beispiel:

- eine Fehlermeldung anzeigen, wenn keine Notiz eingegeben wurde
- die Anzahl der gespeicherten Notizen ausgeben
- die Notizen nummerieren
- die Notizen als JSON speichern


19. ZUSAMMENFASSUNG
===================

Heute hast du gelernt:


open()
------

Dateien lesen und schreiben.


with
----

Dateien sicher öffnen und automatisch schließen.


try / except
------------

Fehler gezielt behandeln.


raise
-----

Eigene Fehler auslösen.


csv
---

Tabellendaten aus CSV-Dateien lesen.


json
----

Strukturierte Daten speichern und laden.


import
------

Module verwenden.


pathlib
-------

Dateipfade und Ordner verwalten.


Die wichtigsten Muster solltest du erkennen können.


DATEI LESEN

with open("datei.txt", encoding="utf-8") as datei:
    ...


DATEI SCHREIBEN

with open(
    "datei.txt",
    "w",
    encoding="utf-8"
) as datei:
    ...


DATEI ERWEITERN

with open(
    "datei.txt",
    "a",
    encoding="utf-8"
) as datei:
    ...


FEHLER BEHANDELN

try:
    ...
except ValueError:
    ...


EIGENEN FEHLER AUSLÖSEN

raise ValueError("Ungültige Eingabe")


JSON LADEN

with open("daten.json", encoding="utf-8") as datei:
    daten = json.load(datei)


JSON SPEICHERN

with open(
    "daten.json",
    "w",
    encoding="utf-8"
) as datei:

    json.dump(
        daten,
        datei,
        ensure_ascii=False,
        indent=2
    )


PFAD VERWALTEN

from pathlib import Path

pfad = Path("daten") / "daten.json"


20. AUSBAU DES GESAMTEN MUSTERS
================================

Bis hierhin haben wir mehrere wichtige Ebenen kennengelernt.

Tag 0:

Variablen
    ↓
Berechnungen
    ↓
Funktionen
    ↓
Bedingungen
    ↓
Eingaben


Tag 1:

Strings
    ↓
Listen
    ↓
Schleifen
    ↓
Daten verarbeiten


Tag 2:

Listen
    ↓
Tupel
    ↓
Dictionaries
    ↓
Sets
    ↓
verschachtelte Daten


Tag 3:

Daten
    ↓
Dateien
    ↓
CSV / JSON
    ↓
dauerhafte Speicherung

und:

Fehler
    ↓
try / except
    ↓
raise

sowie:

Module
    ↓
Standardbibliothek
    ↓
pathlib


Damit werden unsere Programme Schritt für Schritt vollständiger.

Wir können jetzt nicht mehr nur Daten verarbeiten.

Wir können Daten auch dauerhaft speichern,
wieder laden und kontrolliert mit Fehlern umgehen.


21. AUSBLICK AUF TAG 4
======================

Bisher haben wir Programme hauptsächlich über die Konsole bedient.

Am nächsten Tag bauen wir eine grafische Oberfläche.

Wir verwenden dafür Python und tkinter.

Dabei lernst du unter anderem:

- Fenster erstellen
- Texte anzeigen
- Eingabefelder verwenden
- Buttons erstellen
- auf Klicks reagieren
- Eingaben aus einer Oberfläche auslesen
- mehrere Elemente sinnvoll anordnen
- einfache Anwendungen mit einer grafischen Oberfläche erstellen


Damit wird aus einem reinen Konsolenprogramm
eine kleine grafische Anwendung.


ENDE TAG 3
==========
"""