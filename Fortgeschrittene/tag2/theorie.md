
# Python Tag 2: Datenstrukturen

Heute geht es darum, Daten in Python sinnvoll zu strukturieren.

Wir arbeiten mit:

- Listen
- Tupeln
- Dictionaries
- Sets
- `sorted()`
- verschachtelten Datenstrukturen

Die einzelnen Datenstrukturen haben unterschiedliche Aufgaben. Entscheidend ist deshalb nicht nur, wie sie funktionieren, sondern auch, wann welche Struktur sinnvoll ist.

---

# 1. Listen



## Listen durchlaufen

Mit einer `for`-Schleife können wir jeden Wert einzeln verarbeiten:

```python
for temperatur in temperaturen:
    print(temperatur)
```

## Eine neue Liste aufbauen

Wir können während einer Schleife eine neue Liste erstellen:

```python
hohe_werte = []

for temperatur in temperaturen:
    if temperatur >= 20:
        hohe_werte.append(temperatur)
```

Danach enthält `hohe_werte` nur die Temperaturen ab 20 Grad.

Das ist besonders praktisch, wenn wir Daten filtern möchten.

---

# 2. Tupel

Ein Tupel speichert ebenfalls mehrere Werte in einer festen Reihenfolge.

```python
messbereich = (18.4, 23.1)
```

Die Werte können über ihren Index gelesen werden:

```python
print(messbereich[0])
print(messbereich[1])
```

Ein Tupel kann nicht auf dieselbe Weise verändert werden wie eine Liste.

```python
messbereich = (18.4, 23.1)
```

Die beiden Werte können zum Beispiel gemeinsam zurückgegeben werden:

```python
def min_max(messwerte):
    kleinster = min(messwerte)
    groesster = max(messwerte)

    return kleinster, groesster
```

Die Funktion liefert damit ein Tupel zurück:

```python
ergebnis = min_max([18.4, 21.7, 16.2, 23.1])

print(ergebnis)
```

Ausgabe:

```text
(16.2, 23.1)
```

Ein Tupel ist deshalb praktisch, wenn mehrere zusammengehörige Werte gemeinsam behandelt werden sollen.

---

# 3. Dictionaries

Ein Dictionary speichert Daten als Schlüssel-Wert-Paare.

Die wichtigsten Begriffe:

- `key` = Schlüssel
- `value` = Wert
- `item` = ein Schlüssel-Wert-Paar

Beispiel:

```python
person = {
    "name": "Sophie",
    "alter": 32,
    "stadt": "Hannover"
}
```

Das Dictionary enthält:

| key | value |
|---|---|
| `"name"` | `"Sophie"` |
| `"alter"` | `32` |
| `"stadt"` | `"Hannover"` |

Der `key` beschreibt, welche Information gespeichert ist.

Der `value` enthält die eigentliche Information.

Ein `item` ist das komplette Paar aus `key` und `value`.

---

## 3.1 Auf einen Value zugreifen

```python
person = {
    "name": "Sophie",
    "alter": 32,
    "stadt": "Hannover"
}

print(person["name"])
print(person["alter"])
print(person["stadt"])
```

---

## 3.2 Einen Value ändern

```python
person["alter"] = 33

print(person)
```

---

## 3.3 Einen neuen Key hinzufügen

```python
person["beruf"] = "Informatikerin"

print(person)
```

---

## 3.4 Prüfen, ob ein Key existiert

```python
if "name" in person:
    print("Name vorhanden")

if "telefon" not in person:
    print("Keine Telefonnummer gespeichert")
```

---

## 3.5 Alle Keys ausgeben

`.keys()` liefert alle Schlüssel des Dictionaries.

```python
for key in person.keys():
    print(key)
```

---

## 3.6 Alle Values ausgeben

`.values()` liefert alle Werte des Dictionaries.

```python
for value in person.values():
    print(value)
```

---

## 3.7 Keys und Values zusammen

`.items()` liefert die Schlüssel-Wert-Paare.

Bei:

```python
{
    "name": "Sophie",
    "alter": 33
}
```

sind die einzelnen Items:

```text
("name", "Sophie")
("alter", 33)
```

Deshalb können wir schreiben:

```python
for key, value in person.items():
    print(key, ":", value)
```

Dabei gilt:

- `key` = Schlüssel
- `value` = zugehöriger Wert

---

## 3.8 Ein Dictionary durchlaufen

```python
server = {
    "name": "web01",
    "status": "online",
    "port": 443
}

for key, value in server.items():
    print(key, ":", value)
```

---

## 3.9 Warum sind Keys wichtig?

Der `key` sagt uns, welche Bedeutung ein `value` hat.

Ohne Keys:

```text
"Sophie"
33
"Hannover"
```

Wir wissen nicht sicher, was die Werte bedeuten.

Mit Keys:

```text
"name"  -> "Sophie"
"alter" -> 33
"stadt" -> "Hannover"
```

Das Dictionary beschreibt also die Daten.

---

## 3.10 Unterschied zwischen Key, Value und Item

```python
daten = {
    "temperatur": 21,
    "ort": "Hannover",
    "status": "OK"
}
```

### Keys

```text
"temperatur"
"ort"
"status"
```

### Values

```text
21
"Hannover"
"OK"
```

### Items

```text
("temperatur", 21)
("ort", "Hannover")
("status", "OK")
```

Alle Items erhalten wir mit:

```python
daten.items()
```

Zum Beispiel:

```python
for key, value in daten.items():
    print("Key:", key)
    print("Value:", value)
    print()
```

---

## 3.11 Dictionary zum Zählen

Ein Dictionary kann verwendet werden, um Häufigkeiten zu zählen.

```python
farben = [
    "rot",
    "blau",
    "rot",
    "grün",
    "blau",
    "rot"
]

anzahl = {}

for farbe in farben:
    if farbe in anzahl:
        anzahl[farbe] += 1
    else:
        anzahl[farbe] = 1

print(anzahl)
```

Ergebnis:

```python
{
    "rot": 3,
    "blau": 2,
    "grün": 1
}
```

Hier sind:

- `key` = Farbe
- `value` = Anzahl

---

## Merksatz

```text
Dictionary:

key   -> beschreibt die Information
value -> enthält die Information
item  -> key + value zusammen
```

Wichtige Methoden:

```text
.keys()   -> alle Keys
.values() -> alle Values
.items()  -> alle Key-Value-Paare
```

Besonders wichtig:

```python
for key, value in daten.items():
    print(key, value)
```

---

# 4. Sets

Ein Set speichert eindeutige Werte.

Doppelte Werte werden nur einmal gespeichert:

```python
stationen = {
    "Nord",
    "Sued",
    "Nord",
    "West"
}
```

Das Set enthält anschließend nur:

```python
{
    "Nord",
    "Sued",
    "West"
}
```

Sets eignen sich deshalb besonders gut, wenn Duplikate entfernt werden sollen.

Aus einer Liste kann ein Set erstellt werden:

```python
stationen = ["Nord", "Sued", "Nord", "West", "Sued"]

eindeutig = set(stationen)
```

## Gemeinsame Werte finden

Sets können miteinander verglichen werden.

Mit `&` erhalten wir die Schnittmenge:

```python
sensoren_a = {
    "temperatur",
    "druck",
    "feuchtigkeit"
}

sensoren_b = {
    "temperatur",
    "licht",
    "feuchtigkeit"
}

gemeinsam = sensoren_a & sensoren_b
```

Ergebnis:

```python
{
    "temperatur",
    "feuchtigkeit"
}
```

Das ist praktisch, wenn wir herausfinden möchten, welche Werte in zwei Mengen vorkommen.

---

# 5. `sorted()`

Mit `sorted()` können Werte sortiert werden.

```python
messwerte = [21.4, 18.7, 23.1, 19.5]

sortiert = sorted(messwerte)
```

Ergebnis:

```python
[18.7, 19.5, 21.4, 23.1]
```

Wichtig: `sorted()` erstellt eine neue sortierte Liste.

Die ursprüngliche Liste bleibt erhalten:

```python
messwerte = [21.4, 18.7, 23.1, 19.5]

sortiert = sorted(messwerte)

print(messwerte)
print(sortiert)
```

Ausgabe:

```text
[21.4, 18.7, 23.1, 19.5]
[18.7, 19.5, 21.4, 23.1]
```

## Absteigend sortieren

Mit `reverse=True` wird die Reihenfolge umgekehrt:

```python
sortiert = sorted(
    messwerte,
    reverse=True
)
```

Ergebnis:

```python
[23.1, 21.4, 19.5, 18.7]
```

`sorted()` funktioniert nicht nur mit Zahlen:

```python
stationen = ["West", "Nord", "Sued"]

sortiert = sorted(stationen)
```

Ergebnis:

```python
["Nord", "Sued", "West"]
```

---

# 6. Verschachtelte Datenstrukturen

Datenstrukturen können miteinander kombiniert werden.

Zum Beispiel kann ein Dictionary Listen enthalten:

```python
station = {
    "name": "Nord",
    "temperaturen": [18.4, 19.1, 20.3]
}
```

Auf die Liste greifen wir so zu:

```python
station["temperaturen"]
```

Auf einen einzelnen Messwert:

```python
station["temperaturen"][0]
```

Das ergibt:

```text
18.4
```

## Liste mit Dictionaries

Mehrere Stationen können wiederum in einer Liste gespeichert werden:

```python
stationen = [
    {
        "name": "Nord",
        "temperaturen": [18.0, 20.0]
    },
    {
        "name": "Sued",
        "temperaturen": [22.0, 24.0]
    }
]
```

Jetzt haben wir:

```text
Liste
 └── Dictionary
      └── Liste
```

Wir können diese Struktur mit einer Schleife verarbeiten:

```python
for station in stationen:
    name = station["name"]
    temperaturen = station["temperaturen"]

    print(name)
    print(temperaturen)
```

## Verschachtelte Daten lesen

Bei solchen Daten ist es wichtig, Schritt für Schritt vorzugehen.

```python
station = stationen[0]
```

Jetzt haben wir das erste Dictionary.

```python
name = station["name"]
```

Jetzt haben wir den Namen.

```python
temperaturen = station["temperaturen"]
```

Jetzt haben wir die Liste mit den Temperaturen.

```python
erste_temperatur = temperaturen[0]
```

Jetzt haben wir den ersten Messwert.

So lassen sich auch komplexere Datenstrukturen nachvollziehbar bearbeiten.

---

# 7. Welche Datenstruktur passt?

Die verschiedenen Strukturen haben unterschiedliche Aufgaben.

## Liste

Verwende eine Liste, wenn mehrere Werte in einer Reihenfolge gespeichert werden sollen.

```python
temperaturen = [18.4, 19.1, 20.3]
```

## Tupel

Verwende ein Tupel, wenn mehrere zusammengehörige Werte gemeinsam behandelt werden sollen.

```python
messbereich = (18.4, 20.3)
```

## Dictionary

Verwende ein Dictionary, wenn Werte über Namen oder Schlüssel angesprochen werden sollen.

```python
station = {
    "name": "Nord",
    "temperatur": 18.4
}
```

## Set

Verwende ein Set, wenn nur eindeutige Werte wichtig sind oder Mengen miteinander verglichen werden sollen.

```python
sensoren = {
    "temperatur",
    "druck",
    "feuchtigkeit"
}
```

## Verschachtelte Datenstrukturen

Verwende Kombinationen, wenn die Daten selbst eine Struktur besitzen.

```python
stationen = [
    {
        "name": "Nord",
        "temperaturen": [18.0, 20.0]
    },
    {
        "name": "Sued",
        "temperaturen": [22.0, 24.0]
    }
]
```

---

# 8. Häufige Fehler

## Liste und Set verwechseln

Eine Liste:

```python
werte = [20, 20, 21]
```

kann doppelte Werte enthalten.

Ein Set:

```python
werte = {20, 21}
```

enthält jeden Wert nur einmal.

---

## Falschen Schlüssel verwenden

Bei einem Dictionary muss der Schlüssel existieren:

```python
station = {
    "name": "Nord"
}

print(station["temperatur"])
```

Hier gibt es keinen Schlüssel `"temperatur"`.

---

## Index außerhalb einer Liste

```python
werte = [10, 20, 30]

print(werte[3])
```

Die gültigen Indizes sind:

```text
0
1
2
```

---

## `sorted()` vergessen

Ein Set hat keine feste Reihenfolge, auf die man sich verlassen sollte.

Wenn eine sortierte Liste benötigt wird:

```python
sensoren = {"druck", "licht", "temperatur"}

sortiert = sorted(sensoren)
```

---

# 9. Zusammenfassung

Heute hast du sechs wichtige Bausteine kennengelernt:

```text
Liste
   ↓
mehrere Werte in einer Reihenfolge

Tupel
   ↓
zusammengehörige Werte

Dictionary
   ↓
Schlüssel → Wert

Set
   ↓
eindeutige Werte und Mengen

sorted()
   ↓
sortierte neue Liste

verschachtelte Datenstrukturen
   ↓
Datenstrukturen miteinander kombinieren
```

Besonders wichtig ist die Frage:

> Welche Struktur passt zu meinen Daten?

Nicht jede Information muss in einer Liste gespeichert werden. Die richtige Datenstruktur macht den späteren Code deutlich einfacher.

---

# Ausblick auf Tag 3

Am nächsten Tag verlassen wir die Daten, die direkt im Python-Programm stehen.

Wir schauen uns Dateien an und lernen, wie Python Daten dauerhaft speichern und wieder einlesen kann.

Dabei geht es unter anderem um:

- Textdateien
- CSV-Dateien
- JSON-Dateien
- Dateien lesen
- Dateien schreiben
- strukturierte Daten aus Dateien verarbeiten
```