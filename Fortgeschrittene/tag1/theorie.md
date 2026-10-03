# Tag 1 – Strings & Listen

**Story:** Du bist Agent:in in Ausbildung. Die Python-Grundlagen sitzen. Heute geht es darum, Daten gezielt zu verarbeiten: Texte untersuchen und verändern, Listen verwalten und beide Strukturen miteinander kombinieren.

**Lernziele:** Du kannst Strings gezielt bearbeiten, Zeichen und Teilbereiche auswählen, Texte zerlegen und wieder zusammensetzen. Du kannst Listen erstellen, verändern, durchsuchen und mit Schleifen verarbeiten. Außerdem kannst du Strings und Listen in Funktionen miteinander kombinieren.

**Voraussetzung:** Die Inhalte aus `einfuehrung_python` werden vorausgesetzt. Dazu gehören unter anderem Variablen, Datentypen, `input()`, Bedingungen, Funktionen, Parameter, `return` und grundlegende Schleifen.

---

## 1. Strings gezielt bearbeiten

Ein String ist eine Folge von Zeichen. Strings sind in Python **unveränderbar**. Methoden verändern den bestehenden String also nicht, sondern liefern einen neuen String zurück.

```python
name = "  ada lovelace  "

bereinigt = name.strip()
gross = bereinigt.upper()

print(name)
print(bereinigt)
print(gross)
```

Das ursprüngliche `name` bleibt unverändert.

### Wichtige String-Methoden

| Aufgabe | Code |
|---|---|
| Leerzeichen am Rand entfernen | `text.strip()` |
| Alles klein schreiben | `text.lower()` |
| Alles groß schreiben | `text.upper()` |
| Wörter formatieren | `text.title()` |
| Ersetzen | `text.replace("alt", "neu")` |
| Beginnt mit ...? | `text.startswith("server-")` |
| Endet mit ...? | `text.endswith(".de")` |
| Enthält ...? | `"admin" in text` |
| Länge bestimmen | `len(text)` |

Beispiel:

```python
meldung = "  SERVER-01: OFFLINE  "

meldung = meldung.strip()
meldung = meldung.lower()
meldung = meldung.replace("offline", "wartung")

print(meldung)
```

Ergebnis:

```text
server-01: wartung
```

**Merksatz:** String-Methoden verändern den ursprünglichen String nicht. Wenn du das Ergebnis behalten möchtest, musst du es zuweisen.

---

## 2. Strings über Positionen auslesen

Zeichen in einem String haben Positionen. Die Zählung beginnt bei `0`.

```python
code = "AGENT"

print(code[0])      # A
print(code[1])      # G
print(code[-1])     # T
```

Negative Indizes zählen vom Ende.

```python
print(code[-2])     # N
```

### Slicing

Mit Slicing kannst du einen Teil eines Strings auswählen:

```python
code = "AGENT"

print(code[0:3])    # AGE
print(code[2:])     # ENT
print(code[:3])     # AGE
print(code[::2])    # AET
print(code[::-1])   # TNEGA
```

Die allgemeine Form lautet:

```text
[start:ende:schritt]
```

Das Ende gehört nicht mehr zum Ausschnitt.

Bei:

```python
code[1:4]
```

werden die Positionen `1`, `2` und `3` ausgewählt.

### Strings umdrehen

```python
nachname = "Lovelace"

print(nachname[::-1])
```

Ergebnis:

```text
ecalevoL
```

---

## 3. Strings zerlegen mit `split()`

Mit `split()` wird ein String in mehrere Teile zerlegt. Das Ergebnis ist eine Liste.

```python
name = "Ada Lovelace"

teile = name.split()

print(teile)
```

Ergebnis:

```python
["Ada", "Lovelace"]
```

Die einzelnen Bestandteile können anschließend über den Listenindex angesprochen werden:

```python
vorname = teile[0]
nachname = teile[1]

print(vorname)
print(nachname)
```

Du kannst auch ein bestimmtes Trennzeichen angeben:

```python
daten = "Ada;Lovelace;42"

teile = daten.split(";")

print(teile)
```

Ergebnis:

```python
["Ada", "Lovelace", "42"]
```

Damit entsteht ein wichtiges Muster:

```text
String → split() → Liste
```

---

## 4. Listen wieder zu Strings verbinden mit `join()`

`join()` funktioniert in die andere Richtung.

```python
teile = ["Ada", "Lovelace"]

name = " ".join(teile)

print(name)
```

Ergebnis:

```text
Ada Lovelace
```

Das Trennzeichen steht dabei vor `.join()`:

```python
"-".join(["AL", "42", "X"])
```

Ergebnis:

```text
AL-42-X
```

Weitere Beispiele:

```python
woerter = ["Zugriff", "wurde", "gewährt"]

satz = " ".join(woerter)

print(satz)
```

Ergebnis:

```text
Zugriff wurde gewährt
```

Das Gegenstück zu `split()` ist damit:

```text
String → split() → Liste
Liste  → join()  → String
```

---

## 5. F-Strings

F-Strings werden verwendet, um Werte in Texte einzusetzen.

```python
name = "Ada"
code = "AL-42"

meldung = f"Agentin {name} hat den Code {code}."

print(meldung)
```

Auch Ausdrücke können innerhalb eines f-Strings verwendet werden:

```python
punkte = 8

print(f"Punktestand: {punkte}/10")
print(f"Verbleibend: {10 - punkte}")
```

F-Strings sind besonders nützlich, wenn verarbeitete Daten anschließend als lesbarer Text ausgegeben werden.

---

## 6. Listen

Eine Liste speichert mehrere Werte in einer bestimmten Reihenfolge.

```python
agenten = ["Ada", "Ben", "Cem"]
```

Auf einzelne Elemente greifst du über ihren Index zu:

```python
print(agenten[0])
print(agenten[-1])
```

Listen sind **veränderbar**. Elemente können hinzugefügt, entfernt oder ersetzt werden.

### Elemente hinzufügen

```python
agenten.append("Dora")
```

### An einer bestimmten Position einfügen

```python
agenten.insert(1, "Clara")
```

### Element entfernen

```python
agenten.remove("Ben")
```

Oder über die Position:

```python
agent = agenten.pop(0)

print(agent)
```

`pop()` entfernt das Element und gibt es gleichzeitig zurück.

---

## 7. Listen untersuchen

Einige wichtige Operationen:

| Aufgabe | Code |
|---|---|
| Anzahl der Elemente | `len(liste)` |
| Enthalten? | `"Ada" in liste` |
| Nicht enthalten? | `"Ada" not in liste` |
| Erstes Element | `liste[0]` |
| Letztes Element | `liste[-1]` |
| Ausschnitt | `liste[1:3]` |
| Sortierte Kopie | `sorted(liste)` |
| Liste sortieren | `liste.sort()` |
| Reihenfolge umkehren | `liste.reverse()` |

Beispiel:

```python
server = ["web01", "db01", "mail01"]

print(len(server))
print("db01" in server)

server.sort()

print(server)
```

### `sorted()` und `.sort()`

Diese beiden Varianten unterscheiden sich:

```python
server = ["web03", "web01", "web02"]

sortiert = sorted(server)

print(server)
print(sortiert)
```

`sorted()` erzeugt eine neue sortierte Liste.

```python
server.sort()
```

`.sort()` verändert die vorhandene Liste.

---

## 8. Listen mit Schleifen verarbeiten

Eine Liste wird häufig mit einer `for`-Schleife verarbeitet.

```python
server = ["web01", "db01", "mail01"]

for name in server:
    print(name)
```

Mit einer Bedingung kannst du bestimmte Elemente auswählen:

```python
server = ["web01", "db01", "mail01", "web02"]

for name in server:
    if name.startswith("web"):
        print(name)
```

Hier wird eine String-Methode direkt auf die Elemente einer Liste angewendet.

---

## 9. Listen filtern

Ein häufiges Muster besteht darin, aus einer vorhandenen Liste eine neue Liste zu erzeugen.

```python
server = ["web01", "db01", "mail01", "web02"]

webserver = []

for name in server:
    if name.startswith("web"):
        webserver.append(name)

print(webserver)
```

Ergebnis:

```python
["web01", "web02"]
```

Das Grundmuster lautet:

```text
Liste
↓
durchlaufen
↓
prüfen
↓
passende Werte übernehmen
↓
neue Liste
```

Dieses Muster wird dir im weiteren Python-Kurs immer wieder begegnen.

---

## 10. Strings und Listen kombinieren

Die eigentliche Stärke entsteht, wenn beide Datenstrukturen miteinander kombiniert werden.

```python
name = "  ada lovelace  "

teile = name.strip().title().split()

vorname = teile[0]
nachname = teile[-1]

codename = nachname[::-1].upper()

print(f"Agentin: {vorname} {nachname}")
print(f"Codename: {codename}")
```

Hier werden mehrere Operationen kombiniert:

- `strip()` bereinigt den Text.
- `title()` formatiert den Namen.
- `split()` erzeugt eine Liste.
- `teile[0]` und `teile[-1]` greifen auf Listenelemente zu.
- `[::-1]` dreht den Nachnamen um.
- `upper()` wandelt ihn in Großbuchstaben um.
- Der f-String erzeugt die Ausgabe.

---

## 11. Listen mit Textdaten verarbeiten

Listen enthalten häufig Strings, die zunächst normalisiert werden müssen.

```python
meldungen = [
    "  SERVER-01 online ",
    "SERVER-02 OFFLINE",
    "  SERVER-03 online"
]

bereinigt = []

for meldung in meldungen:
    meldung = meldung.strip().lower()
    bereinigt.append(meldung)

print(bereinigt)
```

Ergebnis:

```python
[
    "server-01 online",
    "server-02 offline",
    "server-03 online"
]
```

Die verarbeiteten Daten können anschließend weiter untersucht werden:

```python
for meldung in bereinigt:
    if "offline" in meldung:
        print("Warnung:", meldung)
```

Damit werden mehrere bisher bekannte Konzepte miteinander verbunden:

```text
Liste
→ Schleife
→ String bearbeiten
→ Bedingung prüfen
→ Ergebnis in Liste übernehmen
```

---

## 12. Häufige Fehler

### String-Methode ohne Zuweisung

Das hier verändert `name` nicht:

```python
name = "  ada  "
name.strip()

print(name)
```

Richtig:

```python
name = name.strip()
```

### Index außerhalb der Liste

```python
namen = ["Ada", "Ben"]

print(namen[2])
```

Die Liste besitzt nur die Indizes `0` und `1`.

### `split()` und `join()` verwechseln

```text
split() → String wird zur Liste

join()  → Liste wird zum String
```

### Falsches Slicing

```python
text = "Python"

print(text[0:2])
```

Ergebnis:

```text
Py
```

Nicht `Pyt`, denn das Ende des Slices wird nicht eingeschlossen.

### Liste während des Durchlaufens verändern

Vermeide es zunächst, eine Liste direkt zu verändern, während du über genau diese Liste iterierst:

```python
for server in server:
    ...
```

Wenn eine neue Auswahl entstehen soll, ist eine zweite Liste oft die klarere Lösung:

```python
aktive_server = []

for server in server:
    if ...:
        aktive_server.append(server)
```

---

## 13. Zusammenfassung

### Strings

```python
text.strip()
text.lower()
text.upper()
text.title()
text.replace("alt", "neu")
text.startswith("...")
text.endswith("...")
"..." in text
text[0]
text[-1]
text[1:4]
text[::-1]
text.split()
```

### Listen

```python
liste.append(wert)
liste.insert(position, wert)
liste.remove(wert)
liste.pop()
liste[0]
liste[-1]
liste[1:3]
len(liste)
wert in liste
sorted(liste)
liste.sort()
liste.reverse()
```

### Verbindung beider Strukturen

```python
teile = text.split()
text = " ".join(teile)
```

und:

```python
for element in liste:
    ...
```

Das wichtigste Grundmuster dieses Tages lautet:

```text
Text analysieren
      ↓
String bearbeiten
      ↓
split()
      ↓
Liste verarbeiten
      ↓
join()
      ↓
Text erzeugen
```

---

## Ausblick

Die nächsten Tage erweitern die Datenstrukturen und den Umgang mit echten Daten:

| Tag | Thema |
|---|---|
| **Tag 0** | Python-Einführung und Syntax-Refresh |
| **Tag 1** | Strings & Listen |
| **Tag 2** | Dictionaries, Sets & Tuples |
| **Tag 3** | Dateien lesen und schreiben, CSV & JSON |
| **Tag 4** | GUI-Programmierung |

Damit geht es Schritt für Schritt von einzelnen Werten über strukturierte Daten bis hin zu gespeicherten Daten und einer interaktiven Anwendung.