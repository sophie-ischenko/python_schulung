"""
Tag 1 – Theorie: Strings & Listen

Du bist Agent:in in Ausbildung.

Die Python-Grundlagen sitzen. Heute geht es darum, Daten gezielt
zu verarbeiten: Texte untersuchen und verändern, Listen verwalten
und beide Strukturen miteinander kombinieren.

Die Datei enthält die Theorie direkt als Kommentare.
Viele Beispiele sind auskommentiert und können zum Ausprobieren
aktiviert werden.

Entferne dafür einfach die # vor einem Beispiel und führe die
Datei erneut aus.


LERNZIELE
---------

Du kannst:

- Strings gezielt bearbeiten
- Zeichen und Teilbereiche auswählen
- Texte zerlegen und wieder zusammensetzen
- Listen erstellen und verändern
- Listen durchsuchen
- Listen mit Schleifen verarbeiten
- Strings und Listen miteinander kombinieren
- Funktionen mit Strings und Listen verwenden


VORAUSSETZUNG
-------------

Die Inhalte aus "einfuehrung_python" werden vorausgesetzt.

Dazu gehören unter anderem:

- Variablen
- Datentypen
- input()
- Bedingungen
- Funktionen
- Parameter
- return
- grundlegende Schleifen


============================================================
1. STRINGS GEZIELT BEARBEITEN
============================================================

Ein String ist eine Folge von Zeichen.

Zum Beispiel:

"""

# name = "Ada Lovelace"

# print(name)


"""
Strings sind in Python unveränderbar.

Das bedeutet:

Eine String-Methode verändert nicht den ursprünglichen String.
Sie liefert einen neuen String zurück.

Zum Beispiel:

"""

# name = "  ada lovelace  "

# bereinigt = name.strip()
# gross = bereinigt.upper()

# print(name)
# print(bereinigt)
# print(gross)


"""
Ausgabe:

    ada lovelace

    ada lovelace

    ADA LOVELACE

Das ursprüngliche name bleibt unverändert.


------------------------------------------------------------
WICHTIGE STRING-METHODEN
------------------------------------------------------------

Leerzeichen am Rand entfernen:

    text.strip()


Alles klein schreiben:

    text.lower()


Alles groß schreiben:

    text.upper()


Wörter formatieren:

    text.title()


Text ersetzen:

    text.replace("alt", "neu")


Prüfen, ob Text mit etwas beginnt:

    text.startswith("server-")


Prüfen, ob Text mit etwas endet:

    text.endswith(".de")


Prüfen, ob etwas enthalten ist:

    "admin" in text


Länge bestimmen:

    len(text)


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

"""

# meldung = "  SERVER-01: OFFLINE  "

# meldung = meldung.strip()
# meldung = meldung.lower()
# meldung = meldung.replace("offline", "wartung")

# print(meldung)


"""
Ergebnis:

    server-01: wartung


MERKSATZ:

String-Methoden verändern den ursprünglichen String nicht.

Wenn du das Ergebnis behalten möchtest, musst du es zuweisen.

Also:

    text = text.lower()

und nicht nur:

    text.lower()


============================================================
2. STRINGS ÜBER POSITIONEN AUSLESEN
============================================================

Zeichen in einem String haben Positionen.

Die Zählung beginnt bei 0.

"""

# code = "AGENT"

# print(code[0])
# print(code[1])
# print(code[-1])


"""
Ausgabe:

    A
    G
    T

Negative Indizes zählen vom Ende.

"""

# print(code[-2])


"""
Ergebnis:

    N


------------------------------------------------------------
SLICING
------------------------------------------------------------

Mit Slicing können wir einen Teil eines Strings auswählen.

"""

# code = "AGENT"

# print(code[0:3])
# print(code[2:])
# print(code[:3])
# print(code[::2])
# print(code[::-1])


"""
Ergebnisse:

    AGE
    ENT
    AGE
    AET
    TNEGA


Die allgemeine Form lautet:

    text[start:ende:schritt]


Wichtig:

Das Ende gehört nicht mehr zum Ausschnitt.

Bei:

    code[1:4]

werden die Positionen:

    1
    2
    3

ausgewählt.

Position 4 ist nicht mehr enthalten.


------------------------------------------------------------
STRINGS UMDREHEN
------------------------------------------------------------

Ein String kann mit Slicing umgedreht werden.

"""

# nachname = "Lovelace"

# print(nachname[::-1])


"""
Ergebnis:

    ecalevoL


Das Muster:

    [::-1]

bedeutet:

    vom Anfang bis zum Ende
    mit einer Schrittweite von -1


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

"""

# geheimcode = "PYTHON"

# print(geheimcode[0])
# print(geheimcode[-1])
# print(geheimcode[1:4])
# print(geheimcode[::-1])


"""
Versuche anschließend selbst:

    - die ersten drei Zeichen auszugeben
    - die letzten zwei Zeichen auszugeben
    - jedes zweite Zeichen auszugeben
    - den String umzudrehen


============================================================
3. STRINGS ZERLEGEN MIT split()
============================================================

Mit split() wird ein String in mehrere Teile zerlegt.

Das Ergebnis ist eine Liste.

"""

# name = "Ada Lovelace"

# teile = name.split()

# print(teile)


"""
Ergebnis:

    ["Ada", "Lovelace"]


Die einzelnen Bestandteile können anschließend über den
Listenindex angesprochen werden.

"""

# vorname = teile[0]
# nachname = teile[1]

# print(vorname)
# print(nachname)


"""
Du kannst auch ein bestimmtes Trennzeichen angeben.

"""

# daten = "Ada;Lovelace;42"

# teile = daten.split(";")

# print(teile)


"""
Ergebnis:

    ["Ada", "Lovelace", "42"]


Damit entsteht ein wichtiges Muster:

    String
        ↓
    split()
        ↓
    Liste


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

"""

# daten = "server01,server02,server03"

# server = daten.split(",")

# print(server)

# print(server[0])
# print(server[-1])


"""
============================================================
4. LISTEN WIEDER ZU STRINGS VERBINDEN
============================================================

join() funktioniert in die andere Richtung.

"""

# teile = ["Ada", "Lovelace"]

# name = " ".join(teile)

# print(name)


"""
Ergebnis:

    Ada Lovelace


Das Trennzeichen steht vor .join():

"""

# code = "-".join(["AL", "42", "X"])

# print(code)


"""
Ergebnis:

    AL-42-X


Weitere Beispiele:

"""

# woerter = ["Zugriff", "wurde", "gewährt"]

# satz = " ".join(woerter)

# print(satz)


"""
Ergebnis:

    Zugriff wurde gewährt


Das Gegenstück zu split() ist damit:

    String → split() → Liste

    Liste  → join()  → String


============================================================
5. F-STRINGS
============================================================

F-Strings werden verwendet, um Werte in Texte einzusetzen.

"""

# name = "Ada"
# code = "AL-42"

# meldung = f"Agentin {name} hat den Code {code}."

# print(meldung)


"""
Auch Ausdrücke können innerhalb eines f-Strings verwendet werden.

"""

# punkte = 8

# print(f"Punktestand: {punkte}/10")
# print(f"Verbleibend: {10 - punkte}")


"""
F-Strings sind besonders praktisch, wenn verarbeitete Daten
anschließend als lesbarer Text ausgegeben werden.


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

"""

# server = "web01"
# status = "online"

# print(f"Server {server} ist {status}.")


"""
============================================================
6. LISTEN
============================================================

Eine Liste speichert mehrere Werte in einer bestimmten Reihenfolge.

"""

# agenten = ["Ada", "Ben", "Cem"]

# print(agenten)


"""
Auf einzelne Elemente greifst du über ihren Index zu.

"""

# print(agenten[0])
# print(agenten[-1])


"""
Listen sind veränderbar.

Elemente können hinzugefügt, entfernt oder ersetzt werden.


------------------------------------------------------------
ELEMENTE HINZUFÜGEN
------------------------------------------------------------

append() fügt ein Element am Ende der Liste hinzu.

"""

# agenten = ["Ada", "Ben", "Cem"]

# agenten.append("Dora")

# print(agenten)


"""
------------------------------------------------------------
ELEMENT AN BESTIMMTER POSITION EINFÜGEN
------------------------------------------------------------

insert() fügt ein Element an einer bestimmten Position ein.

"""

# agenten = ["Ada", "Ben", "Cem"]

# agenten.insert(1, "Clara")

# print(agenten)


"""
------------------------------------------------------------
ELEMENT ENTFERNEN
------------------------------------------------------------

remove() entfernt ein Element anhand seines Wertes.

"""

# agenten = ["Ada", "Ben", "Cem"]

# agenten.remove("Ben")

# print(agenten)


"""
Oder wir können ein Element anhand seiner Position entfernen.

Dafür verwenden wir pop().

"""

# agenten = ["Ada", "Ben", "Cem"]

# agent = agenten.pop(0)

# print(agent)
# print(agenten)


"""
pop() entfernt das Element und gibt es gleichzeitig zurück.


============================================================
7. LISTEN UNTERSUCHEN
============================================================

Einige wichtige Operationen:

    len(liste)
        Anzahl der Elemente

    "Ada" in liste
        Prüft, ob Ada enthalten ist

    "Ada" not in liste
        Prüft, ob Ada nicht enthalten ist

    liste[0]
        Erstes Element

    liste[-1]
        Letztes Element

    liste[1:3]
        Ausschnitt

    sorted(liste)
        Sortierte Kopie

    liste.sort()
        Vorhandene Liste sortieren

    liste.reverse()
        Reihenfolge umkehren


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

"""

# server = ["web01", "db01", "mail01"]

# print(len(server))
# print("db01" in server)
# print("proxy01" not in server)

# print(server[0])
# print(server[-1])

# print(server[0:2])


"""
------------------------------------------------------------
SORTIEREN
------------------------------------------------------------

"""

# server = ["web03", "web01", "web02"]

# sortiert = sorted(server)

# print(server)
# print(sortiert)


"""
sorted() erzeugt eine neue sortierte Liste.

Die ursprüngliche Liste bleibt erhalten.


Mit .sort() wird die vorhandene Liste verändert.

"""

# server = ["web03", "web01", "web02"]

# server.sort()

# print(server)


"""
------------------------------------------------------------
REIHENFOLGE UMDREHEN
------------------------------------------------------------

"""

# server = ["web01", "web02", "web03"]

# server.reverse()

# print(server)


"""
============================================================
8. LISTEN MIT SCHLEIFEN VERARBEITEN
============================================================

Eine Liste wird häufig mit einer for-Schleife verarbeitet.

"""

# server = ["web01", "db01", "mail01"]

# for name in server:
#     print(name)


"""
Hier wird jedes Element nacheinander in name gespeichert.

Bei:

    ["web01", "db01", "mail01"]

passiert also:

    name = "web01"
    name = "db01"
    name = "mail01"


------------------------------------------------------------
BEDINGUNGEN VERWENDEN
------------------------------------------------------------

Wir können innerhalb der Schleife Bedingungen verwenden.

"""

# server = ["web01", "db01", "mail01", "web02"]

# for name in server:
#     if name.startswith("web"):
#         print(name)


"""
Ergebnis:

    web01
    web02


Hier werden mehrere Konzepte kombiniert:

    Liste
        ↓
    for-Schleife
        ↓
    String-Methode
        ↓
    Bedingung


============================================================
9. LISTEN FILTERN
============================================================

Ein häufiges Muster besteht darin, aus einer vorhandenen Liste
eine neue Liste zu erzeugen.

"""

# server = ["web01", "db01", "mail01", "web02"]

# webserver = []

# for name in server:
#     if name.startswith("web"):
#         webserver.append(name)

# print(webserver)


"""
Ergebnis:

    ["web01", "web02"]


Das Grundmuster lautet:

    Liste
      ↓
    durchlaufen
      ↓
    prüfen
      ↓
    passende Werte übernehmen
      ↓
    neue Liste


Dieses Muster wird dir im weiteren Python-Kurs immer wieder
begegnen.


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

Erstelle eine Liste mit verschiedenen Servernamen.

Filtere anschließend nur die Datenbankserver heraus.

Beispiel:

    web01
    db01
    mail01
    db02
    web02

Tipp:

    startswith("db")


============================================================
10. STRINGS UND LISTEN KOMBINIEREN
============================================================

Die eigentliche Stärke entsteht, wenn beide Datenstrukturen
miteinander kombiniert werden.

"""

# name = "  ada lovelace  "

# teile = name.strip().title().split()

# vorname = teile[0]
# nachname = teile[-1]

# codename = nachname[::-1].upper()

# print(f"Agentin: {vorname} {nachname}")
# print(f"Codename: {codename}")


"""
Hier werden mehrere Operationen kombiniert:

    strip()
        bereinigt den Text

    title()
        formatiert den Namen

    split()
        erzeugt eine Liste

    teile[0]
        greift auf das erste Element zu

    teile[-1]
        greift auf das letzte Element zu

    [::-1]
        dreht den Nachnamen um

    upper()
        wandelt ihn in Großbuchstaben um

    f"..."
        erzeugt die Ausgabe


============================================================
11. LISTEN MIT TEXTDATEN VERARBEITEN
============================================================

Listen enthalten häufig Strings, die zunächst normalisiert
werden müssen.

Zum Beispiel:

"""

# meldungen = [
#     "  SERVER-01 online ",
#     "SERVER-02 OFFLINE",
#     "  SERVER-03 online"
# ]

# bereinigt = []

# for meldung in meldungen:
#     meldung = meldung.strip().lower()
#     bereinigt.append(meldung)

# print(bereinigt)


"""
Ergebnis:

    [
        "server-01 online",
        "server-02 offline",
        "server-03 online"
    ]


Die verarbeiteten Daten können anschließend weiter untersucht
werden.

"""

# for meldung in bereinigt:
#     if "offline" in meldung:
#         print("Warnung:", meldung)


"""
Damit werden mehrere bekannte Konzepte miteinander verbunden:

    Liste
      ↓
    Schleife
      ↓
    String bearbeiten
      ↓
    Bedingung prüfen
      ↓
    Ergebnis in Liste übernehmen


============================================================
12. HÄUFIGE FEHLER
============================================================


------------------------------------------------------------
STRING-METHODE OHNE ZUWEISUNG
------------------------------------------------------------

Das hier verändert name nicht:

"""

# name = "  ada  "

# name.strip()

# print(name)


"""
Richtig:

"""

# name = "  ada  "

# name = name.strip()

# print(name)


"""
------------------------------------------------------------
INDEX AUSSERHALB DER LISTE
------------------------------------------------------------

"""

# namen = ["Ada", "Ben"]

# print(namen[2])


"""
Die Liste besitzt nur:

    Index 0 → Ada
    Index 1 → Ben

Index 2 existiert nicht.


------------------------------------------------------------
split() UND join() VERWECHSELN
------------------------------------------------------------

Merke:

    split()
        String → Liste

    join()
        Liste → String


------------------------------------------------------------
FALSCHES SLICING
------------------------------------------------------------

"""

# text = "Python"

# print(text[0:2])


"""
Ergebnis:

    Py

Nicht:

    Pyt

Das Ende des Slices wird nicht eingeschlossen.


------------------------------------------------------------
LISTE WÄHREND DES DURCHLAUFENS VERÄNDERN
------------------------------------------------------------

Vermeide es zunächst, eine Liste direkt zu verändern,
während du über genau diese Liste iterierst.

Ungünstig:

"""

# server = ["web01", "db01", "mail01"]

# for name in server:
#     server.remove(name)


"""
Wenn eine neue Auswahl entstehen soll, ist eine zweite Liste
oft die klarere Lösung:

"""

# server = ["web01", "db01", "mail01", "web02"]

# aktive_server = []

# for name in server:
#     if name.startswith("web"):
#         aktive_server.append(name)

# print(aktive_server)


"""
============================================================
13. STRINGS UND LISTEN IN FUNKTIONEN
============================================================

Strings und Listen können natürlich auch als Parameter
an Funktionen übergeben werden.

"""

# def begruessen(name):
#     name = name.strip().title()
#     return f"Hallo {name}!"


# print(begruessen("  ada lovelace  "))


"""
Auch Listen können übergeben werden.

"""

# def server_anzeigen(server):
#     for name in server:
#         print(name)


# server = ["web01", "db01", "mail01"]

# server_anzeigen(server)


"""
Damit können wir die Verarbeitung von Daten von der eigentlichen
Programmlogik trennen.


============================================================
14. KOMBINATIONSBEISPIEL
============================================================

Hier verbinden wir Strings, Listen, Schleifen,
Bedingungen und Funktionen.

"""

# def finde_webserver(server):
#
#     webserver = []
#
#     for name in server:
#         if name.startswith("web"):
#             webserver.append(name)
#
#     return webserver


# server = [
#     "web01",
#     "db01",
#     "mail01",
#     "web02",
#     "db02"
# ]

# ergebnis = finde_webserver(server)

# print(ergebnis)


"""
Das Programm:

    1. bekommt eine Liste
    2. durchläuft die Liste
    3. prüft jedes Element
    4. übernimmt passende Elemente
    5. gibt eine neue Liste zurück


============================================================
15. WICHTIGE GRUNDLAGEN DIESES TAGES
============================================================

STRINGS

"""

# text.strip()
# text.lower()
# text.upper()
# text.title()
# text.replace("alt", "neu")
# text.startswith("...")
# text.endswith("...")
# "..." in text

# text[0]
# text[-1]
# text[1:4]
# text[::-1]

# text.split()


"""
LISTEN

"""

# liste.append(wert)
# liste.insert(position, wert)
# liste.remove(wert)
# liste.pop()

# liste[0]
# liste[-1]
# liste[1:3]

# len(liste)

# wert in liste

# sorted(liste)
# liste.sort()
# liste.reverse()


"""
VERBINDUNG BEIDER STRUKTUREN

"""

# teile = text.split()

# text = " ".join(teile)


"""
UND:

"""

# for element in liste:
#     ...


"""
============================================================
16. WICHTIGSTES MUSTER
============================================================

Ein besonders wichtiges Muster dieses Tages ist:

    Text
      ↓
    String bearbeiten
      ↓
    split()
      ↓
    Liste
      ↓
    Liste verarbeiten
      ↓
    join()
      ↓
    Text erzeugen


Zum Beispiel:

"""

# text = "  Ada Lovelace  "

# teile = text.strip().title().split()

# for teil in teile:
#     print(teil)

# neuer_text = " ".join(teile)

# print(neuer_text)


"""
============================================================
17. INTERAKTIVE CHALLENGES
============================================================

Bevor du mit der Aufgabe beginnst, probiere die folgenden
kleinen Aufgaben direkt in dieser Datei aus.


CHALLENGE 1
-----------

Gegeben:

    name = "  ada lovelace  "

Bereinige den Namen und gib ihn schön formatiert aus.

Ziel:

    Ada Lovelace


CHALLENGE 2
-----------

Gegeben:

    geheimcode = "PYTHON"

Gib aus:

    - das erste Zeichen
    - das letzte Zeichen
    - die ersten drei Zeichen
    - den umgedrehten Code


CHALLENGE 3
-----------

Gegeben:

    server = "web01,web02,db01,mail01"

Zerlege den String in eine Liste.


CHALLENGE 4
-----------

Gegeben:

    server = ["web01", "db01", "web02", "mail01"]

Erstelle eine neue Liste,
die nur die Webserver enthält.


CHALLENGE 5
-----------

Gegeben:

    agenten = ["ada", "ben", "cem"]

Füge einen weiteren Agenten hinzu.

Sortiere anschließend die Liste.


CHALLENGE 6
-----------

Erstelle eine Liste mit mehreren Statusmeldungen.

Zum Beispiel:

    " SERVER-01 ONLINE "
    " server-02 offline "
    " SERVER-03 ONLINE "

Bereinige alle Meldungen und wandle sie in Kleinbuchstaben um.

Gib anschließend nur die Meldungen aus,
die "offline" enthalten.


============================================================
18. ZUSAMMENFASSUNG
============================================================

Heute hast du gelernt:

    Strings
        ↓
    bearbeiten
        ↓
    Zeichen auswählen
        ↓
    Slicing
        ↓
    split()
        ↓
    Listen
        ↓
    Listen verändern
        ↓
    Listen durchsuchen
        ↓
    Schleifen
        ↓
    Listen filtern
        ↓
    join()
        ↓
    Strings und Listen kombinieren


Diese Grundlagen werden später ständig wieder auftauchen.

Besonders wichtig sind:

    split()
    join()
    strip()
    lower()
    upper()
    replace()
    startswith()
    endswith()

und:

    append()
    insert()
    remove()
    pop()
    sorted()
    sort()
    reverse()


============================================================
AUSBLICK
============================================================

Als Nächstes erweitern wir die Möglichkeiten,
Daten strukturiert zu speichern.

Zum Beispiel mit:

    Dictionaries
    Sets
    Tuples

Später kommen außerdem:

    Dateien
    CSV
    JSON
    APIs
    GUI-Programmierung

Damit geht es Schritt für Schritt von einfachen Daten
hin zu kleinen echten Anwendungen.
"""