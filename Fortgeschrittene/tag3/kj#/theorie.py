"""
Python Tag 3 – Dateien, Fehler und Module

1. DATEIEN LESEN
================

Mit open() können wir eine Datei öffnen.

Zum Lesen reicht grundsätzlich:
"""

print("\n--- 1. DATEIEN LESEN ---")
datei = open("notizen.txt", encoding="utf-8")
datei.close()


"""
Für die praktische Arbeit ist die Verwendung von with besser.

Beispiel:
"""

with open("notizen.txt", encoding="utf-8") as datei:
    inhalt = datei.read()
print("Datei über with gelesen:", inhalt)

"""
with sorgt dafür, dass die Datei nach der Verwendung
automatisch geschlossen wird.

Das ist die übliche Schreibweise für die Arbeit mit Dateien.


EINE DATEI KOMPLETT LESEN
-------------------------

Mit read() lesen wir den gesamten Inhalt einer Datei.
"""

with open("notizen.txt", encoding="utf-8") as datei:
    inhalt = datei.read()

print("Die ganze Datei in einer Variable:")
print(inhalt)


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



input("\n>> Drücke ENTER zum 'AUSPROBIEREN (Zeile 139)'... ")
print("\nErgebnis deines Ausprobierens:")
with open("notizen.txt", encoding="utf-8") as datei:
    inhalt = datei.read()

print(inhalt)


"""
DATEI ZEILENWEISE LESEN
-----------------------

Eine Datei kann auch mit einer for-Schleife durchlaufen werden.
"""

print("--- DATEI ZEILENWEISE LESEN ---")
with open("notizen.txt", encoding="utf-8") as datei:
    for zeile in datei:
        print("FOR-Loop direkt:", zeile)


"""
Dabei enthält zeile normalerweise noch den Zeilenumbruch
am Ende der Zeile.

Wir können diesen entfernen.

Dafür verwenden wir rstrip().
"""

print("--- DATEI ZEILENWEISE MIT RSTRIP() ---")
with open("notizen.txt", encoding="utf-8") as datei:
    for zeile in datei:
        zeile = zeile.rstrip("\n")
        print("RSTRIP Ergebnis:", zeile)


"""
ZEILEN IN EINER LISTE SPEICHERN
-------------------------------

Wir können die einzelnen Zeilen auch in einer Liste speichern.
"""

zeilen = []

with open("notizen.txt", encoding="utf-8") as datei:
    for zeile in datei:
        zeilen.append(zeile.rstrip("\n"))

print("\n--- Als Liste: ---")
print(zeilen)



"""
2. DATEIEN SCHREIBEN
====================

Zum Schreiben wird open() mit dem Modus "w" verwendet.

Beispiel:
"""

with open("notizen.txt", "w", encoding="utf-8") as datei:
    datei.write("Erste Notiz\n")
    datei.write("Zweite Notiz\n")


"""
Der Modus "w" bedeutet:

Datei zum Schreiben öffnen.

Wichtig:

Wenn die Datei bereits existiert, wird ihr bisheriger Inhalt
überschrieben.


AUSPROBIEREN
------------
"""

print("\n--- Schreibe neue test.txt (w Modus) ---")
with open("test.txt", "w", encoding="utf-8") as datei:
    datei.write("Hallo Python!\n")
    datei.write("Das ist meine erste Datei.\n")


"""
TEXT ANHÄNGEN
=============

Mit "a" wird neuer Inhalt an eine vorhandene Datei angehängt.

Der bisherige Inhalt bleibt erhalten.
"""

with open("notizen.txt", "a", encoding="utf-8") as datei:
    datei.write("Neue Notiz\n")


"""
Wenn wir das Beispiel mehrfach ausführen,
wird jedes Mal eine weitere Zeile angehängt.


AUSPROBIEREN
------------
"""

with open("notizen.txt", "a", encoding="utf-8") as datei:
    datei.write("Noch eine Notiz\n")

print("(Die Dateien notizen.txt und test.txt wurden aktualisiert. Schaue in deinen Ordner!)")
input("\n>> Drücke ENTER für die THEORIE ZU DATEIMODI... ")


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

print("\n--- 3. FEHLER VERSTEHEN ---")
# zahl = int("Hallo") # <- Ich lasse das sicher auskommentiert oder in try, sonst stürzt dir dieses schöne Script hier ab!

try:
    zahl = int("Hallo")
except ValueError as e:
    print(f"Beweis-Fehler abgefangen: {e}")

"""
Python kann "Hallo" nicht in eine ganze Zahl umwandeln.

Es entsteht ein:

ValueError


Ein anderer Fehler entsteht beim Öffnen einer Datei,
die nicht existiert.

Beispiel:
"""

try:
    with open("nicht_da.txt", encoding="utf-8") as datei:
        inhalt = datei.read()
except FileNotFoundError as e:
    print(f"Zweiter Beweis-Fehler abgefangen: {e}")


"""
Hier entsteht normalerweise:

FileNotFoundError


Fehler gehören zum Programmieren dazu.

Wichtig ist deshalb nicht, dass niemals ein Fehler auftritt.

Wichtig ist, dass wir verstehen, was der Fehler bedeutet
und wie wir sinnvoll damit umgehen können.
"""
input("\n>> Drücke ENTER für TRY UND EXCEPT... ")


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

print("\n--- Probiere es mal mit Buchstaben! ---")
try:
    zahl = int(input("Gib eine Zahl ein: "))
    print("Deine Zahl ist:", zahl)
except ValueError:
    print("Das war keine gültige Zahl. Siehst du? Nicht abgestürzt!")


"""
Das Programm bricht bei einer ungültigen Eingabe
nicht einfach mit einer Fehlermeldung ab.

Stattdessen können wir selbst eine passende Nachricht ausgeben.


FEHLER GENAUER UNTERSUCHEN
=========================

Mit as können wir den Fehler in einer Variablen speichern.
"""

print("\n--- FEHLER VARIABLE ---")
try:
    zahl = int("Hallo")
except ValueError as fehler:
    print(fehler)


"""
Damit erhalten wir die konkrete Fehlermeldung von Python.


AUSPROBIEREN
------------
"""

print("\n--- Genauere Ausgabe bei 'abc' Umwandlung ---")
try:
    zahl = int("abc")
except ValueError as fehler:
    print("Es ist ein Fehler aufgetreten:")
    print(fehler)


"""
MEHRERE FEHLER BEHANDELN
========================

Unterschiedliche Fehler können unterschiedliche Ursachen haben.

Beispiel:
"""

try:
    with open("daten.txt", encoding="utf-8") as datei:
        zahl = int(datei.read())

except FileNotFoundError:
    print("Beispiel 1: Die Datei wurde nicht gefunden (und stürzt trotzdem nicht ab).")

except ValueError:
    print("Beispiel 1: Die Datei enthält keine gültige Zahl.")


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
print("\n--- MEHRFACH TRY/EXCEPT MIT INPUT ---")

try:
    zahl = int(input("Gib eine Zahl ein: "))
    print("Zahl:", zahl)

except ValueError:
    print("Die Eingabe war keine Zahl.")

except TypeError:
    print("Der Datentyp konnte nicht verarbeitet werden.")


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

print("\n--- ELSE BEISPIEL ---")
try:
    zahl = int(input("Zahl eingeben für Else-Test: "))

except ValueError:
    print("Ungültige Eingabe.")

else:
    print("Klasse! Else block getriggert: Die Zahl ist:", zahl)


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

print("\n--- FINALLY BEISPIEL ---")
try:
    zahl = int(input("Zahl eingeben für Finally-Test: "))

except ValueError:
    print("Ungültige Eingabe.")

finally:
    print("Dieser Teil wird IMMER ausgeführt (finally-Block).")


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
input("\n>> Drücke ENTER für 7. EIGENE FEHLER AUSLÖSEN... ")


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

def pruefe_betrag(betrag):
    if betrag == 0:
        raise ValueError("Der Betrag darf nicht 0 sein.")
    
    return betrag


"""
Wenn wir schreiben:

pruefe_betrag(0)

wird ein ValueError ausgelöst.
"""

print("\n--- TEST: RAISE AUSLÖSEN ---")
# Ich ummantel dies mit einem try/except für unser interaktives Programm:
try:
    pruefe_betrag(0)
except ValueError as e:
    print("Funktion warf einen Fehler:", e)

"""
Warum sollte eine Funktion selbst einen Fehler auslösen?

Eine Funktion sollte nicht einfach falsche Daten akzeptieren.

Beispiel:

Ein Haushaltsbuch darf möglicherweise keine Buchung
mit einem Betrag von 0 akzeptieren.
"""

def buchung_hinzufuegen(betrag):
    if betrag == 0:
        raise ValueError("Der Betrag darf nicht 0 sein.")

    print("Buchung hinzugefügt.")


"""
Der Code, der die Funktion aufruft,
kann entscheiden, was danach passieren soll.

Zum Beispiel:
"""
print("\n--- Funktion mit abfangen aufrufen: ---")

try:
    buchung_hinzufuegen(0)

except ValueError as fehler:
    print("Selbstgeworfener Fehler:", fehler)


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
print("\n--- Ausprobieren: Prüfe Alter (try me! Es kommt -5 an) ---")

def pruefe_alter(alter):
    if alter < 0:
        raise ValueError("Das Alter darf nicht negativ sein.")

    return alter

try:
    pruefe_alter(-5)

except ValueError as fehler:
    print("Fehler beim Prüfen:", fehler)


"""
8. CSV-DATEIEN
==============


CSV eignet sich besonders für Tabellen und Daten,
die beispielsweise aus Tabellenprogrammen exportiert wurden.

Python stellt dafür das Modul csv bereit.
"""
# Wieder: Skript baut Dummy-Datei vorher damit der Reader hier was hat!
with open("ausgaben.csv", "w", encoding="utf-8") as f:
    f.write("datum,kategorie,betrag\n01.10.2026,Essen,-25.50\n02.10.2026,Gehalt,3000.00\n03.10.2026,Tanken,-60.00\n")

import csv
input("\n>> Drücke ENTER für den CSV Teil... ")

"""
CSV MIT DictReader LESEN
========================

Mit csv.DictReader werden die Spaltennamen zu
Dictionary-Schlüsseln.

Beispiel:
"""

print("\n--- DICT READER EINSATZ ---")

import csv

with open(
    "ausgaben.csv",
    encoding="utf-8",
    newline=""
) as datei:

    reader = csv.DictReader(datei)

    for zeile in reader:
        print(zeile)


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


print("\n--- ZWEI BESTIMMTE SPALTEN HOLEN: ---")


with open(
    "ausgaben.csv",
    encoding="utf-8",
    newline=""
) as datei:

    reader = csv.DictReader(datei)

    for zeile in reader:
        kategorie = zeile["kategorie"]
        betrag = float(zeile["betrag"])

        print(kategorie, betrag)


"""
CSV UND DICTIONARIES

Wir können die Daten weiterverarbeiten.

Beispiel:
"""
print("\n--- DICTIONARIES WEITERVERARBEITEN ---")


with open(
    "ausgaben.csv",
    encoding="utf-8",
    newline=""
) as datei:

    reader = csv.DictReader(datei)

    for zeile in reader:
        kategorie = zeile["kategorie"]
        betrag = float(zeile["betrag"])

        print("Kategorie:", kategorie)
        print("Betrag:", betrag)


"""
9. JSON-DATEIEN
===============


Beispiel:

{
    "name": "Nord",
    "temperaturen": [18.4, 19.1, 20.3]
}


JSON passt sehr gut zu Python-Dictionaries und Listen.

Python stellt dafür das Modul json bereit.
"""
input("\n>> Drücke ENTER für den JSON Teil... ")

import json


"""
10. JSON SCHREIBEN
==================

Mit json.dump() können Python-Daten in eine Datei
geschrieben werden.

Beispiel:
"""

import json

daten = {
    "name": "Nord",
    "temperaturen": [18.4, 19.1, 20.3]
}

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

print("\nJSON gespeichert als 'daten.json'.")


"""
indent=2

sorgt für eine besser lesbare Formatierung.


ensure_ascii=False

sorgt dafür, dass beispielsweise deutsche Umlaute
nicht unnötig in Unicode-Schreibweise umgewandelt werden.


AUSPROBIEREN
------------
"""
print("\n--- ZWEITES AUSPROBIEREN JSON ---")

import json

daten = {
    "name": "Nord",
    "status": "aktiv",
    "temperaturen": [18.4, 19.1, 20.3]
}

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


"""
Öffne danach die Datei daten.json.

Du kannst sehen, wie aus einem Python-Dictionary
eine JSON-Datei geworden ist.
"""
input("Du hast daten.json aktualisiert. Guck gern rein (Texteditor/VScode) -> Drücke Enter.")

"""
11. JSON LESEN
==============

Mit json.load() wird eine JSON-Datei wieder eingelesen.
"""

import json

with open(
    "daten.json",
    encoding="utf-8"
) as datei:

    daten = json.load(datei)


"""
Danach können wir die Daten wie normale Python-Daten verwenden.
"""
print("\nAus JSON-Daten auslesen:")
print("Name:", daten["name"])
print("Temperaturen", daten["temperaturen"])


"""
AUSPROBIEREN
------------
"""
print("\n--- KOMPLETTER KREISLAUF: ---")
import json

with open("daten.json", encoding="utf-8") as datei:
    daten = json.load(datei)

print("Name:", daten["name"])
print("Temperaturen:", daten["temperaturen"])


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

import json

try:
    with open("daten.json", encoding="utf-8") as datei:
        daten = json.load(datei)

except FileNotFoundError:
    daten = {}

except json.JSONDecodeError:
    daten = {}


"""
Das Programm kann in beiden Fällen mit einem leeren
Dictionary starten.


AUSPROBIEREN
------------
"""

print("\n--- JSON LESE MIT SCHUTZ ---")

import json

try:
    with open("daten.json", encoding="utf-8") as datei:
        daten = json.load(datei)

except FileNotFoundError:
    print("Die Datei existiert noch nicht.")
    daten = {}

except json.JSONDecodeError:
    print("Die JSON-Datei ist ungültig.")
    daten = {}

print("Ausgespuckt:", daten)

input("\n>> Drücke ENTER für 13. MODULE... ")
"""
Dieses Muster ist besonders nützlich für Programme,
die beim Start gespeicherte Daten laden.



14. pathlib
==========

Das Modul pathlib hilft bei der Arbeit mit Dateipfaden.

Wir können Path so importieren:
"""
input("\n>> Drücke ENTER für PATHLIB... ")
from pathlib import Path


"""
Ein Pfad kann anschließend erstellt werden:
"""

ordner = Path("daten")


"""
Eine Datei innerhalb dieses Ordners:
"""

datei = ordner / "messwerte.json"


"""
Das / zwischen zwei Path-Objekten verbindet die Pfade.

Das ist besonders praktisch, weil pathlib die Unterschiede
zwischen den Betriebssystemen berücksichtigt.


AUSPROBIEREN
------------
"""
print("\n--- PFADE ---")

from pathlib import Path

ordner = Path("daten")
datei = ordner / "messwerte.json"

print(ordner)
print(datei)


"""
PRÜFEN, OB EINE DATEI EXISTIERT
===============================

Mit exists() können wir prüfen,
ob ein Pfad vorhanden ist.
"""

from pathlib import Path

pfad = Path("daten.json")

print("\nExisiert sie?")
if pfad.exists():
    print("Datei vorhanden")
else:
    print("Datei fehlt")


"""
DATEIENDUNG AUSLESEN
====================

Mit suffix erhalten wir die Dateiendung.
"""
print("\n--- SUFFIX (Dateiendung) ---")

from pathlib import Path

pfad = Path("messwerte.csv")

print(pfad.suffix)


"""
Die Ausgabe ist:

.csv


AUSPROBIEREN
------------
"""

from pathlib import Path

pfade = [
    Path("daten.json"),
    Path("ausgaben.csv"),
    Path("notizen.txt")
]

print("\nDatei-Extensions von Listen ermitteln:")
for pfad in pfade:
    print(pfad.name, "→", pfad.suffix)


"""
DATEI MIT pathlib ÖFFNEN
========================

Ein Path-Objekt kann direkt an open() übergeben werden.

Wir können also einen Dateipfad mit pathlib erstellen
und diesen anschließend mit open() verwenden.
"""

print("\n--- FILE MIT PATH ÖFFNEN ---")

from pathlib import Path
import json

pfad = Path(".") / "daten.json"  # (Pfad habe ich dynamisch angepasst!)

with open(pfad, encoding="utf-8") as datei:
    inhalt = datei.read()

print("Klappt direkt!", inhalt[:40], "... etc.")


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

print("\n--- WAS LIEGT IN DEM AKTUELLEN ORDNER? (Auszug) ---")

from pathlib import Path

ordner = Path(".")

zaehler = 0
for datei in ordner.iterdir():
    if zaehler < 3: # Limitiere auf 3
        print("Iterdir:", datei.name)
        zaehler+=1

"""
Wir können prüfen, ob ein Eintrag tatsächlich eine Datei ist.
"""

from pathlib import Path

ordner = Path(".")

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

print("\n--- ALL-IN-ONE PATH CHECK ---")

from pathlib import Path

pfad = Path("daten.json")

print(pfad)
print("Existiert?", pfad.exists())
print("Endung:", pfad.suffix)

input("\n>> Drücke ENTER um zur ZUSAMMENFASSUNG ZU KOMMEN... ")
"""
15. DATEIEN, DATEN UND FEHLER ZUSAMMENBRINGEN
=============================================

Jetzt können wir die einzelnen Themen miteinander verbinden.

Stell dir ein Programm vor, das Messdaten dauerhaft speichern soll.

Die Daten liegen zunächst in Python:
"""

messdaten = {
    "Nord": {
        "temperaturen": [18.4, 19.1, 20.3]
    }
}


"""
Wir können diese Daten als JSON speichern:
"""

import json

messdaten = {
    "Nord": {
        "temperaturen": [18.4, 19.1, 20.3]
    }
}

with open(
    "messdaten.json",
    "w",
    encoding="utf-8"
) as datei:

    json.dump(
        messdaten,
        datei,
        ensure_ascii=False,
        indent=2
    )


"""
Beim nächsten Programmstart laden wir sie wieder:
"""

import json

try:
    with open(
        "messdaten.json",
        encoding="utf-8"
    ) as datei:

        messdaten = json.load(datei)

except FileNotFoundError:
    messdaten = {}


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

import json

print("\n--- RUNDLAUF DATEN SPEICHERN ---")

messdaten = {
    "Nord": {
        "temperaturen": [18.4, 19.1, 20.3]
    }
}


with open(
    "messdaten.json",
    "w",
    encoding="utf-8"
) as datei:

    json.dump(
        messdaten,
        datei,
        ensure_ascii=False,
        indent=2
    )


with open(
    "messdaten.json",
    encoding="utf-8"
) as datei:

    geladene_daten = json.load(datei)


print("Geschrieben und Gelesen! ->", geladene_daten)


"""
16. pathlib UND JSON KOMBINIEREN
================================

pathlib und json können ebenfalls gemeinsam verwendet werden.

Beispiel:
"""

from pathlib import Path
import json


pfad = Path(".") / "messdaten.json"


with open(
    pfad,
    "w",
    encoding="utf-8"
) as datei:

    json.dump(
        messdaten,
        datei,
        ensure_ascii=False,
        indent=2
    )


"""
Damit können Dateipfade sauber getrennt von den eigentlichen
Daten behandelt werden.


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


"""
ZWEITER SCHRITT

Notiz speichern:
"""


"""
DRITTER SCHRITT

Die Datei anschließend wieder lesen:
"""


"""
Versuche anschließend selbst, die Aufgabe zu erweitern.

Zum Beispiel:

- eine Fehlermeldung anzeigen, wenn keine Notiz eingegeben wurde
- die Anzahl der gespeicherten Notizen ausgeben
- die Notizen nummerieren
- die Notizen als JSON speichern

"""
