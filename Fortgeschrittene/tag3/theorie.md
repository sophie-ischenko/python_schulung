
# Python Tag 3: Dateien, Fehler und Module

Bisher lagen unsere Daten direkt im Python-Programm.

Das ist für Übungen praktisch, aber ein echtes Programm soll Daten auch speichern und wieder laden können. Außerdem müssen Programme mit Problemen umgehen können, ohne sofort abzubrechen.

Heute lernst du deshalb:

- Dateien lesen und schreiben
- Fehler mit `try` und `except` behandeln
- eigene Fehler mit `raise` auslösen
- CSV-Dateien lesen
- JSON-Dateien lesen und schreiben
- Module der Standardbibliothek verwenden
- Dateipfade mit `pathlib` verwalten

---

# 1. Dateien lesen

Mit `open()` können wir eine Datei öffnen.

Zum Lesen reicht:

```python
datei = open("notizen.txt", encoding="utf-8")
```

Besser ist die Verwendung von `with`:

```python
with open("notizen.txt", encoding="utf-8") as datei:
    inhalt = datei.read()
```

`with` sorgt dafür, dass die Datei nach der Verwendung automatisch geschlossen wird.

Das ist die übliche und sichere Schreibweise.

## Eine Datei komplett lesen

Mit `.read()` lesen wir den gesamten Inhalt:

```python
with open("notizen.txt", encoding="utf-8") as datei:
    inhalt = datei.read()

print(inhalt)
```

## Eine Datei zeilenweise lesen

Eine Datei kann auch mit einer `for`-Schleife durchlaufen werden:

```python
with open("notizen.txt", encoding="utf-8") as datei:
    for zeile in datei:
        print(zeile)
```

Dabei enthält `zeile` normalerweise noch den Zeilenumbruch `\n`.

Wir können ihn entfernen:

```python
with open("notizen.txt", encoding="utf-8") as datei:
    for zeile in datei:
        zeile = zeile.rstrip("\n")
        print(zeile)
```

## Zeilen in einer Liste speichern

```python
zeilen = []

with open("notizen.txt", encoding="utf-8") as datei:
    for zeile in datei:
        zeilen.append(zeile.rstrip("\n"))
```

Danach enthält `zeilen` eine Liste mit den einzelnen Zeilen.

---

# 2. Dateien schreiben

Zum Schreiben wird `open()` mit dem Modus `"w"` verwendet:

```python
with open("notizen.txt", "w", encoding="utf-8") as datei:
    datei.write("Erste Notiz\n")
    datei.write("Zweite Notiz\n")
```

Der Modus `"w"` bedeutet:

> Datei zum Schreiben öffnen.

Wenn die Datei bereits existiert, wird ihr bisheriger Inhalt überschrieben.

## Text anhängen

Mit `"a"` wird neuer Inhalt angehängt:

```python
with open("notizen.txt", "a", encoding="utf-8") as datei:
    datei.write("Neue Notiz\n")
```

Der bisherige Inhalt bleibt erhalten.

## Die wichtigsten Modi

| Modus | Bedeutung |
|---|---|
| `"r"` | lesen |
| `"w"` | schreiben, vorhandenen Inhalt ersetzen |
| `"a"` | neuen Inhalt anhängen |

Wenn kein Modus angegeben wird, wird standardmäßig gelesen.

```python
with open("notizen.txt", encoding="utf-8") as datei:
    ...
```

Das entspricht:

```python
with open("notizen.txt", "r", encoding="utf-8") as datei:
    ...
```

## Merksatz

> Dateien immer mit `with` öffnen und bei Textdateien die Codierung `utf-8` angeben.

---

# 3. Fehler verstehen

Nicht jeder Programmablauf funktioniert erfolgreich.

Zum Beispiel:

```python
zahl = int("Hallo")
```

Python kann `"Hallo"` nicht in eine ganze Zahl umwandeln.

Es entsteht ein:

```text
ValueError
```

Auch beim Öffnen einer nicht vorhandenen Datei kann ein Fehler entstehen:

```python
with open("nicht_da.txt", encoding="utf-8") as datei:
    ...
```

Hier entsteht normalerweise ein:

```text
FileNotFoundError
```

Solche Fehler können wir gezielt behandeln.

---

# 4. Fehler mit `try` und `except` behandeln

Mit `try` sagen wir:

> Versuche diesen Code auszuführen.

Mit `except` sagen wir:

> Wenn ein bestimmter Fehler auftritt, reagiere darauf.

Beispiel:

```python
try:
    alter = int(input("Alter: "))
except ValueError:
    print("Bitte eine ganze Zahl eingeben.")
```

Wenn die Eingabe beispielsweise

```text
25
```

lautet, funktioniert die Umwandlung.

Bei

```text
Hallo
```

wird der `except`-Block ausgeführt.

Das Programm kann danach weiterlaufen.

## Einen Fehler genauer untersuchen

Mit `as` können wir die Fehlermeldung speichern:

```python
try:
    zahl = int("Hallo")
except ValueError as fehler:
    print(fehler)
```

Damit erhalten wir die konkrete Fehlermeldung.

## Mehrere Fehler behandeln

Unterschiedliche Fehler können unterschiedliche Ursachen haben:

```python
try:
    with open("daten.txt", encoding="utf-8") as datei:
        zahl = int(datei.read())
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")
except ValueError:
    print("Die Datei enthält keine gültige Zahl.")
```

Die Fehler werden getrennt behandelt.

Das ist besser, als einfach jeden Fehler mit derselben Meldung zu behandeln.

---

# 5. `else` und `finally`

Neben `try` und `except` gibt es `else` und `finally`.

## `else`

Der `else`-Block wird ausgeführt, wenn kein Fehler aufgetreten ist:

```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Ungültige Eingabe.")
else:
    print("Die Zahl ist:", zahl)
```

## `finally`

Der `finally`-Block wird unabhängig davon ausgeführt, ob ein Fehler aufgetreten ist:

```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Ungültige Eingabe.")
finally:
    print("Dieser Teil wird immer ausgeführt.")
```

Für den Alltag werden vor allem `try` und `except` benötigt.

---

# 6. Nur konkrete Fehler abfangen

Vermeide:

```python
try:
    ...
except:
    ...
```

Damit werden praktisch alle Fehler abgefangen.

Das kann echte Programmierfehler verstecken.

Besser:

```python
try:
    zahl = int(eingabe)
except ValueError:
    print("Bitte eine Zahl eingeben.")
```

Hier ist klar, welcher Fehler erwartet wird.

## Merksatz

> Fange den Fehler ab, mit dem du sinnvoll umgehen kannst.

---

# 7. Eigene Fehler mit `raise` auslösen

Bisher haben wir Fehler behandelt, die Python selbst ausgelöst hat.

Eine Funktion kann aber auch selbst feststellen:

> Diese Eingabe ist nicht erlaubt.

Dann können wir mit `raise` einen Fehler auslösen.

```python
def pruefe_betrag(betrag):
    if betrag == 0:
        raise ValueError("Der Betrag darf nicht 0 sein.")

    return betrag
```

Wenn wir schreiben:

```python
pruefe_betrag(0)
```

wird ein `ValueError` ausgelöst.

## Warum selbst Fehler auslösen?

Eine Funktion sollte nicht einfach falsche Daten akzeptieren.

Zum Beispiel bei einem Haushaltsbuch:

```python
def buchung_hinzufuegen(betrag):
    if betrag == 0:
        raise ValueError("Der Betrag darf nicht 0 sein.")
```

Die Funktion meldet damit:

> Mit dieser Eingabe kann ich nicht arbeiten.

Der Code, der die Funktion aufruft, kann entscheiden, was danach passieren soll.

Zum Beispiel:

```python
try:
    buchung_hinzufuegen(0)
except ValueError as fehler:
    print("Fehler:", fehler)
```

## Zusammenspiel von `raise` und `except`

```text
Funktion
   │
   │ raise ValueError
   ↓
Fehler entsteht
   │
   ↓
Aufrufer
   │
   │ except ValueError
   ↓
Fehler behandeln
```

## Merksatz

> `raise` löst einen Fehler aus.  
> `except` fängt einen Fehler ab.

---

# 8. CSV-Dateien

CSV steht für:

**Comma-Separated Values**

Eine CSV-Datei speichert tabellarische Daten.

Beispiel:

```text
datum,kategorie,betrag
01.10.2026,Essen,-25.50
02.10.2026,Gehalt,3000.00
03.10.2026,Tanken,-60.00
```

CSV eignet sich besonders für Tabellen und Daten, die aus Tabellenprogrammen exportiert wurden.

Python stellt dafür das Modul `csv` bereit.

```python
import csv
```

## CSV mit `DictReader` lesen

Mit `csv.DictReader` werden die Spaltennamen zu Dictionary-Schlüsseln.

```python
with open(
    "ausgaben.csv",
    encoding="utf-8",
    newline=""
) as datei:

    reader = csv.DictReader(datei)

    for zeile in reader:
        print(zeile)
```

Eine Zeile sieht dann ungefähr so aus:

```python
{
    "datum": "01.10.2026",
    "kategorie": "Essen",
    "betrag": "-25.50"
}
```

Wichtig:

Die Werte aus einer CSV-Datei sind zunächst Text.

Das bedeutet:

```python
betrag = zeile["betrag"]
```

liefert zum Beispiel:

```text
"-25.50"
```

Wenn wir damit rechnen möchten, müssen wir den Wert umwandeln:

```python
betrag = float(zeile["betrag"])
```

## CSV und Dictionaries

`DictReader` passt besonders gut zu unseren bisherigen Kenntnissen über Dictionaries.

Wir können beispielsweise:

```python
for zeile in reader:
    kategorie = zeile["kategorie"]
    betrag = float(zeile["betrag"])

    print(kategorie, betrag)
```

Damit verbinden wir Daten aus einer Datei mit den Datenstrukturen aus Tag 2.

---

# 9. JSON-Dateien

JSON steht für:

**JavaScript Object Notation**

JSON kann strukturierte Daten speichern.

Zum Beispiel:

```json
{
  "name": "Nord",
  "temperaturen": [18.4, 19.1, 20.3]
}
```

JSON passt deshalb sehr gut zu Python-Dictionaries und Listen.

Python stellt dafür das Modul `json` bereit:

```python
import json
```

---

# 10. JSON schreiben

Mit `json.dump()` können Python-Daten in eine Datei geschrieben werden:

```python
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
```

`indent=2` sorgt für eine gut lesbare Formatierung.

`ensure_ascii=False` sorgt dafür, dass beispielsweise deutsche Umlaute erhalten bleiben.

---

# 11. JSON lesen

Mit `json.load()` wird eine JSON-Datei wieder eingelesen:

```python
with open(
    "daten.json",
    encoding="utf-8"
) as datei:

    daten = json.load(datei)
```

Danach können wir die Daten wie normale Python-Daten verwenden:

```python
print(daten["name"])
print(daten["temperaturen"])
```

## JSON und Python

Typische Zuordnungen sind:

| JSON | Python |
|---|---|
| Objekt | Dictionary |
| Array | Liste |
| String | String |
| Zahl | `int` / `float` |
| `true` | `True` |
| `false` | `False` |
| `null` | `None` |

Damit können wir Daten aus Tag 2 dauerhaft speichern.

---

# 12. JSON und Fehlerbehandlung kombinieren

Beim Laden einer Datei können verschiedene Probleme auftreten.

Die Datei könnte fehlen:

```python
FileNotFoundError
```

Oder der Inhalt könnte kein gültiges JSON sein:

```python
json.JSONDecodeError
```

Beide Fälle können getrennt behandelt werden:

```python
import json

try:
    with open("daten.json", encoding="utf-8") as datei:
        daten = json.load(datei)

except FileNotFoundError:
    daten = {}

except json.JSONDecodeError:
    daten = {}
```

Das Programm kann in beiden Fällen mit einem leeren Dictionary starten.

Das ist ein wichtiges Muster für Programme, die gespeicherte Daten verwenden.

---

# 13. Module

Ein Modul ist eine Python-Datei mit fertigem Code.

Python bringt bereits viele Module mit.

Diese Sammlung nennt man:

**Standardbibliothek**

Wir müssen viele nützliche Funktionen deshalb nicht selbst programmieren.

Ein Modul wird mit `import` eingebunden:

```python
import json
```

Danach können wir Funktionen aus dem Modul verwenden:

```python
json.load(datei)
json.dump(daten, datei)
```

Ein weiteres Beispiel:

```python
import csv
```

Danach:

```python
csv.DictReader(datei)
```

## Warum Module verwenden?

Ohne Module müssten wir viele Funktionen selbst schreiben.

Mit der Standardbibliothek können wir vorhandene Werkzeuge nutzen.

---

# 14. `pathlib`

Das Modul `pathlib` hilft bei der Arbeit mit Dateipfaden.

```python
from pathlib import Path
```

Ein Pfad kann so erstellt werden:

```python
ordner = Path("daten")
```

Eine Datei innerhalb dieses Ordners:

```python
datei = ordner / "messwerte.json"
```

Das ist besser, als Pfade als einfache Strings zusammenzubauen.

## Prüfen, ob eine Datei existiert

```python
pfad = Path("daten.json")

if pfad.exists():
    print("Datei vorhanden")
else:
    print("Datei fehlt")
```

## Dateiendung auslesen

Mit `.suffix` erhalten wir die Dateiendung:

```python
pfad = Path("messwerte.csv")

print(pfad.suffix)
```

Ausgabe:

```text
.csv
```

## Dateien in einem Ordner anzeigen

Mit `.iterdir()` können wir den Inhalt eines Ordners durchlaufen:

```python
ordner = Path("daten")

for datei in ordner.iterdir():
    print(datei.name)
```

Wir können prüfen, ob ein Eintrag tatsächlich eine Datei ist:

```python
for datei in ordner.iterdir():
    if datei.is_file():
        print(datei.name)
```

## Warum `pathlib`?

Ein Dateipfad kann je nach Betriebssystem unterschiedlich aussehen.

`pathlib` übernimmt diese Unterschiede für uns.

Zum Beispiel:

```python
Path("daten") / "messwerte.json"
```

funktioniert unter Windows, macOS und Linux.

---

# 15. Dateien, Daten und Fehler zusammenbringen

Jetzt können wir die einzelnen Themen miteinander verbinden.

Stell dir ein Programm vor, das Messdaten dauerhaft speichern soll.

Die Daten liegen in Python:

```python
messdaten = {
    "Nord": {
        "temperaturen": [18.4, 19.1, 20.3]
    }
}
```

Wir speichern sie als JSON:

```python
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
```

Beim nächsten Programmstart laden wir sie wieder:

```python
try:
    with open(
        "messdaten.json",
        encoding="utf-8"
    ) as datei:

        messdaten = json.load(datei)

except FileNotFoundError:
    messdaten = {}
```

Damit entsteht ein vollständiger Ablauf:

```text
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
```

Genau dadurch werden aus vorübergehenden Programmdaten dauerhaft gespeicherte Daten.

---

# 16. Häufige Fehler

## Datei ohne `with` öffnen

Ungünstig:

```python
datei = open("daten.txt")
```

Besser:

```python
with open("daten.txt", encoding="utf-8") as datei:
    ...
```

---

## Falsche Codierung

Bei deutschen Texten kann eine fehlende oder falsche Codierung zu Problemen mit Umlauten führen.

Deshalb:

```python
encoding="utf-8"
```

---

## CSV-Werte direkt berechnen

Das hier funktioniert nicht wie erwartet:

```python
betrag = zeile["betrag"]

summe = summe + betrag
```

Denn `betrag` ist zunächst ein String.

Richtig:

```python
betrag = float(zeile["betrag"])
```

---

## Alle Fehler pauschal abfangen

Ungünstig:

```python
try:
    ...
except:
    print("Irgendwas ist schiefgegangen.")
```

Besser:

```python
try:
    ...
except ValueError:
    print("Ungültige Zahl.")
```

---

## `raise` und `print` verwechseln

Das hier meldet zwar etwas:

```python
print("Betrag ist ungültig.")
```

aber es wird kein Fehler ausgelöst.

Mit:

```python
raise ValueError("Betrag ist ungültig.")
```

wird tatsächlich ein Fehler ausgelöst.

---

## JSON mit CSV verwechseln

CSV:

```text
datum,kategorie,betrag
01.10.2026,Essen,-25.50
```

JSON:

```json
{
  "datum": "01.10.2026",
  "kategorie": "Essen",
  "betrag": -25.50
}
```

Als Faustregel:

> CSV eignet sich besonders für Tabellen.  
> JSON eignet sich besonders für strukturierte und verschachtelte Daten.

---

# 17. Zusammenfassung

Heute hast du gelernt:

```text
open()
  ↓
Dateien lesen und schreiben

try / except
  ↓
Fehler gezielt behandeln

raise
  ↓
eigene Fehler auslösen

csv
  ↓
Tabellendaten lesen

json
  ↓
strukturierte Daten speichern und laden

pathlib
  ↓
Dateipfade und Ordner verwalten

import
  ↓
fertige Module verwenden
```

Die wichtigsten Muster solltest du erkennen können:

Datei lesen:

```python
with open("datei.txt", encoding="utf-8") as datei:
    ...
```

Datei schreiben:

```python
with open(
    "datei.txt",
    "w",
    encoding="utf-8"
) as datei:
    ...
```

Fehler behandeln:

```python
try:
    ...
except ValueError:
    ...
```

Eigenen Fehler auslösen:

```python
raise ValueError("Ungültige Eingabe")
```

JSON laden:

```python
with open("daten.json", encoding="utf-8") as datei:
    daten = json.load(datei)
```

JSON speichern:

```python
with open(
    "daten.json",
    "w",
    encoding="utf-8"
) as datei:
    json.dump(daten, datei, ensure_ascii=False, indent=2)
```

Pfad verwalten:

```python
from pathlib import Path

pfad = Path("daten") / "daten.json"
```

---

# Ausblick auf Tag 4

Bisher haben wir Programme hauptsächlich über die Konsole bedient.

Am nächsten Tag geht es darum, eine grafische Oberfläche zu bauen.

Wir verwenden dafür Python und `tkinter`.

Dabei lernst du unter anderem:

- Fenster erstellen
- Texte und Eingabefelder anzeigen
- Buttons verwenden
- auf Klicks reagieren
- Eingaben aus einer Oberfläche auslesen
- mehrere Elemente sinnvoll anordnen

Damit wird aus einem Konsolenprogramm eine kleine Anwendung mit grafischer Benutzeroberfläche.
