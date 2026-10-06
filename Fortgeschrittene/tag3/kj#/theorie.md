---
marp: true
theme: default
paginate: true
size: 16:9

style: |
  section {
    font-size: 28px;
    background: #E8E1D8;
    color: #293335;
  }

  h1 {
    color: #733843;
    font-size: 52px;
  }

  h2 {
    color: #733843;
  }

  code {
    background-color: #D8CEC3;
    color: #293335;
  }

  .box {
    border: 3px solid #B48469;
    border-radius: 12px;
    padding: 20px;
    background-color: #DDD4CA;
  }

  .center {
    text-align: center;
  }
---

<!-- _class: lead -->

# Tag 3

## Dateien & Fehlerbehandlung

Dateien lesen, speichern und Fehler kontrolliert behandeln

---

## Was du heute lernst

<br>

1. Wie **Dateien geöffnet und gelesen** werden
2. Wie Dateien **geschrieben und erweitert** werden
3. Warum `with` beim Arbeiten mit Dateien wichtig ist
4. Wie **`try` / `except`** Fehler abfangen
5. Wie **`raise`** eigene Fehler auslöst
6. Wie **CSV und JSON** gespeichert und geladen werden
7. Wie `pathlib` Dateipfade verwaltet

---

<!-- _class: lead -->

# Block 1

## Dateien


---

## Eine Datei öffnen

Zum Öffnen verwenden wir `open()`.

```python
datei = open(
    "notizen.txt",
    encoding="utf-8"
)
```

Damit haben wir Zugriff auf die Datei.

---

## Dateien mit `with` öffnen

Besser ist die Verwendung von `with`.

```python
with open(
    "notizen.txt",
    encoding="utf-8"
) as datei:
    inhalt = datei.read()

print(inhalt)
```

<div class="box center">

`with` sorgt dafür,

dass die Datei anschließend

**automatisch geschlossen wird.**

</div>

---

## Dateien lesen

Mit `.read()` lesen wir

den kompletten Inhalt.

```python
with open(
    "notizen.txt",
    encoding="utf-8"
) as datei:
    inhalt = datei.read()

print(inhalt)
```

Die Variable `inhalt`

enthält danach den Text der Datei.

---

## Zeilenweise lesen

Eine Datei kann auch

Zeile für Zeile durchlaufen werden.

```python
with open(
    "notizen.txt",
    encoding="utf-8"
) as datei:

    for zeile in datei:
        print(zeile)
```

Das ist praktisch,

wenn eine Datei viele Zeilen enthält.

---

## Der Dateimodus

Beim Öffnen kann angegeben werden,

was mit der Datei passieren soll.

```text
"r" → lesen
"w" → schreiben
"a" → anhängen
```

Der Modus wird an `open()` übergeben.

```python
open("notizen.txt", "r")
```

---

## Schreiben mit `"w"`

Mit `"w"` schreiben wir

neuen Inhalt in eine Datei.

```python
with open(
    "notizen.txt",
    "w",
    encoding="utf-8"
) as datei:

    datei.write("Erster Eintrag")
```

<div class="box center">

Achtung:

`"w"` überschreibt vorhandenen Inhalt.

</div>

---

## Anhängen mit `"a"`

Mit `"a"` wird neuer Inhalt

am Ende hinzugefügt.

```python
with open(
    "notizen.txt",
    "a",
    encoding="utf-8"
) as datei:

    datei.write("\nZweiter Eintrag")
```

Vorhandener Inhalt bleibt erhalten.

---

## Die drei wichtigsten Modi

<div class="box">

**`"r"`**

→ Datei lesen

<br>

**`"w"`**

→ Datei schreiben  
→ vorhandener Inhalt wird überschrieben

<br>

**`"a"`**

→ Inhalt anhängen

</div>

---

<!-- _class: lead -->

# Block 2

## Fehlerbehandlung

---

## Was passiert bei einem Fehler?

Was passiert hier?

```python
with open(
    "geheim.txt",
    encoding="utf-8"
) as datei:

    inhalt = datei.read()
```

Existiert die Datei nicht,

entsteht ein Fehler:

```text
FileNotFoundError
```

---

## `try` und `except`

Mit `try` können wir Code ausführen,

bei dem ein Fehler auftreten kann.

```python
try:
    with open(
        "geheim.txt",
        encoding="utf-8"
    ) as datei:
        inhalt = datei.read()

except FileNotFoundError:
    print("Datei nicht gefunden.")
```

<div class="box center">

`try` → Versuch

`except` → Fehler behandeln

</div>

---

## Eingaben können ebenfalls fehlschlagen

Zum Beispiel:

```python
zahl = int(
    input("Zahl: ")
)
```

Bei:

```text
hallo
```

entsteht:

```text
ValueError
```

---

## `ValueError` behandeln

```python
try:
    zahl = int(
        input("Zahl: ")
    )

except ValueError:
    print("Keine gültige Zahl.")
```

Das Programm kann den Fehler

kontrolliert behandeln.

---

## Nicht jeden Fehler verschlucken

Besser:

```python
except ValueError:
    ...
```

als:

```python
except:
    ...
```

<div class="box center">

Je genauer der abgefangene Fehler,

desto besser können wir reagieren.

</div>

---

## `else`

Nach einem erfolgreichen `try`

kann `else` ausgeführt werden.

```python
try:
    zahl = int(input("Zahl: "))

except ValueError:
    print("Ungültig.")

else:
    print("Eingabe war korrekt.")
```

`else` läuft also nur,

wenn kein Fehler aufgetreten ist.

---

## `finally`

`finally` wird immer ausgeführt.

```python
try:
    zahl = int(input("Zahl: "))

except ValueError:
    print("Ungültig.")

finally:
    print("Programm beendet.")
```

<div class="box center">

`finally` eignet sich für Code,

der unabhängig vom Ergebnis ausgeführt werden soll.

</div>

---

<!-- _class: lead -->

# Block 3

## Eigene Fehler

---

## `raise`

Manchmal ist eine Eingabe zwar technisch gültig,

aber inhaltlich nicht erlaubt.

```python
alter = int(
    input("Alter: ")
)

if alter < 0:
    raise ValueError(
        "Alter darf nicht negativ sein."
    )
```

Mit `raise` lösen wir

**bewusst einen Fehler aus.**

---

## Validierung

`raise` eignet sich deshalb

für eigene Regeln.

```python
betrag = float(
    input("Betrag: ")
)

if betrag < 0:
    raise ValueError(
        "Betrag darf nicht negativ sein."
    )
```

<div class="box center">

`input()` prüft nur,

ob etwas eingegeben wurde.

Unsere Logik prüft,

ob die Eingabe **gültig** ist.

</div>

---

## Fehlerbehandlung zusammen

```python
try:
    alter = int(
        input("Alter: ")
    )

    if alter < 0:
        raise ValueError(
            "Alter darf nicht negativ sein."
        )

except ValueError as fehler:
    print("Fehler:", fehler)
```

Hier verbinden wir:

```text
try
↓
Eingabe
↓
Validierung
↓
raise
↓
except
```

---

<!-- _class: lead -->

# Block 4

## CSV

---


## CSV mit Python lesen

Python besitzt dafür

das Modul `csv`.

```python
import csv

with open(
    "personen.csv",
    encoding="utf-8"
) as datei:

    reader = csv.DictReader(datei)

    for person in reader:
        print(person["Name"])
```

---

## Was macht `DictReader`?

Aus einer Zeile wie:

```text
Anna,32,Bielefeld
```

wird sinngemäß:

```python
{
    "Name": "Anna",
    "Alter": "32",
    "Ort": "Bielefeld"
}
```

<div class="box center">

CSV → strukturierte Python-Daten

</div>

---

<!-- _class: lead -->

# Block 5

## JSON

---



Mit `json.dump()` schreiben wir

Python-Daten in eine Datei.

```python
import json

person = {
    "name": "Anna",
    "alter": 32,
    "skills": [
        "Python",
        "Linux"
    ]
}

with open(
    "person.json",
    "w",
    encoding="utf-8"
) as datei:

    json.dump(
        person,
        datei,
        indent=4
    )
```

---

## JSON laden

Mit `json.load()` lesen wir

JSON wieder ein.

```python
import json

with open(
    "person.json",
    encoding="utf-8"
) as datei:

    person = json.load(datei)

print(person["name"])
print(person["skills"])
```

Danach haben wir wieder

eine Python-Datenstruktur.

---

## CSV oder JSON?

<div class="box">

**CSV**

→ Tabellen  
→ Zeilen und Spalten  
→ einfache Datensätze

<br>

**JSON**

→ strukturierte Daten  
→ Dictionaries und Listen  
→ verschachtelte Daten

</div>

---

<!-- _class: lead -->

# Block 6

## `pathlib`

---

## Dateipfade mit `pathlib`

Für Dateipfade gibt es

das Modul `pathlib`.

```python
from pathlib import Path

datei = Path("daten") / "notizen.txt"
```

Der Pfad wird dabei

plattformunabhängig zusammengesetzt.

---

## Datei mit `pathlib` prüfen

```python
from pathlib import Path

datei = Path("notizen.txt")

if datei.exists():
    print("Datei vorhanden.")
```

Auch Verzeichnisse können

über `Path` verwaltet werden.

---

## Lesen und Schreiben

`pathlib` kann einfache Dateien

direkt lesen und schreiben.

```python
from pathlib import Path

datei = Path("notizen.txt")

datei.write_text(
    "Hallo Python!",
    encoding="utf-8"
)

inhalt = datei.read_text(
    encoding="utf-8"
)

print(inhalt)
```

---

## `open()` oder `pathlib`?

Beides ist sinnvoll.

<div class="box">

**`open()`**

→ klassische Dateiverarbeitung  
→ gut für `csv`, `json` und Schleifen

<br>

**`pathlib`**

→ moderne Verwaltung von Pfaden  
→ Dateien und Verzeichnisse

</div>

