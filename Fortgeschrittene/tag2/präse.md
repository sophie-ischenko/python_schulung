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

# Tag 2

## Datenstrukturen

Listen, Tupel, Dictionaries, Sets & verschachtelte Daten

---

## Was du heute lernst

<br>

1. Wie **Listen** mehrere Werte speichern
2. Was ein **Tupel** ist
3. Wie **Dictionaries** mit Schlüssel und Wert funktionieren
4. Wofür **Sets** verwendet werden
5. Wie `sorted()` Daten sortiert
6. Wie man **verschachtelte Datenstrukturen** liest und verarbeitet

---

<!-- _class: lead -->

# Block 1

## Listen

---





## Listen durchlaufen

Mit einer `for`-Schleife können wir jeden Wert

**einzeln verarbeiten.**

```python
for temperatur in temperaturen:
    print(temperatur)
```

<div class="box center">

Python nimmt nacheinander

jeden Wert aus der Liste.

</div>

---

## Eine neue Liste aufbauen

Wir können während einer Schleife

eine neue Liste erstellen.

```python
hohe_werte = []

for temperatur in temperaturen:
    if temperatur >= 20:
        hohe_werte.append(temperatur)
```

<div class="box center">

`hohe_werte` enthält danach

nur Temperaturen ab 20 Grad.

</div>



---

<!-- _class: lead -->

# Block 2

## Tupel

---

## Was ist ein Tupel?

Ein Tupel speichert ebenfalls mehrere Werte

**in einer festen Reihenfolge.**

```python
messbereich = (18.4, 23.1)
```

<div class="box center">

Tupel sehen ähnlich aus wie Listen.

Der Unterschied:

**Ein Tupel wird nicht auf dieselbe Weise verändert wie eine Liste.**

</div>

---

## Auf Tupel zugreifen

Auch Tupel besitzen Indizes.

```python
messbereich = (18.4, 23.1)

print(messbereich[0])
print(messbereich[1])
```

Ausgabe:

```text
18.4
23.1
```

---

## Wofür sind Tupel praktisch?

Tupel eignen sich für

**zusammengehörige Werte**, die gemeinsam behandelt werden.

Zum Beispiel:

```python
messbereich = (18.4, 23.1)
```

<div class="box center">

Minimum und Maximum

gehören zusammen.

</div>

---

## Mehrere Werte gemeinsam zurückgeben

Eine Funktion kann mehrere Werte zurückgeben.

```python
def min_max(messwerte):
    kleinster = min(messwerte)
    groesster = max(messwerte)

    return kleinster, groesster
```

---

## Das Ergebnis ist ein Tupel

```python
ergebnis = min_max(
    [18.4, 21.7, 16.2, 23.1]
)

print(ergebnis)
```

Ausgabe:

```text
(16.2, 23.1)
```

<div class="box center">

Mehrere zusammengehörige Werte

können gemeinsam zurückgegeben werden.

</div>

---

## Liste oder Tupel?

<div class="box">

**Liste**

```python
temperaturen = [18.4, 21.7, 19.2]
```

→ mehrere Werte in einer Reihenfolge

<br>

**Tupel**

```python
messbereich = (18.4, 23.1)
```

→ zusammengehörige Werte

</div>

---


<!-- _class: lead -->

# Block 3

## Dictionaries

---

## Was ist ein Dictionary?

Ein Dictionary speichert Daten als

**Schlüssel → Wert**

auf Englisch:

**key → value**

```python
person = {
    "name": "Sophie",
    "alter": 32,
    "stadt": "Hannover"
}
```

<div class="box center">

Ein Dictionary besteht aus

**Schlüsseln (`keys`) und Werten (`values`).**

</div>

---

## Key und Value

Bei:

```python
person = {
    "name": "Sophie",
    "alter": 32,
    "stadt": "Hannover"
}
```


```text
key       value
---------------------
"name"    "Sophie"
"alter"   32
"stadt"   "Hannover"
```

<div class="box center">

**Key** = Schlüssel

**Value** = Wert

</div>

---

## Ein Key zeigt auf einen Value

Der Key beschreibt,

**welche Information** gespeichert ist.

Der Value enthält

**die eigentliche Information**.

```python
person = {
    "name": "Sophie",
    "alter": 32
}
```

Hier bedeutet:

```text
"name"  →  "Sophie"
"alter" →  32
```

---

## Auf einen Value zugreifen

Wir verwenden den **Key**:

```python
person = {
    "name": "Sophie",
    "alter": 32
}

print(person["name"])
print(person["alter"])
```

Ausgabe:

```text
Sophie
32
```
---
<div class="box center">

Nicht:

```python
person[0]
```

Sondern:

```python
person["name"]
```

</div>

---

## Keys müssen eindeutig sein

Innerhalb eines Dictionaries kann ein Key

nicht sinnvoll mehrfach vorkommen.

```python
person = {
    "name": "Sophie",
    "alter": 32
}
```

Die Keys sind:

```text
"name"
"alter"
```

Jeder Key beschreibt eine bestimmte Information.

---

## Werte können unterschiedlich sein

Ein Dictionary kann verschiedene Datentypen enthalten.

```python
server = {
    "name": "web01",
    "status": "online",
    "ram": 32,
    "backup": True
}
```

```text
"web01"
"online"
32
True
```

<div class="box center">

Der Key beschreibt die Information.

Der Value enthält die Information.

</div>

---

## Werte verändern

Ein vorhandener Value kann

über seinen Key verändert werden.

```python
server = {
    "name": "web01",
    "status": "offline"
}

server["status"] = "online"
```

Danach:

```python
{
    "name": "web01",
    "status": "online"
}
```

---

## Neue Keys hinzufügen

Ein neuer Key kann einfach

mit einem Value angelegt werden.

```python
server = {
    "name": "web01",
    "status": "online"
}

server["ram"] = 32
```

Danach:

```python
{
    "name": "web01",
    "status": "online",
    "ram": 32
}
```

<div class="box center">

Key noch nicht vorhanden?

→ neuer Eintrag

Key vorhanden?

→ vorhandenen Value ändern

</div>

---

## Prüfen, ob ein Key vorhanden ist

Mit `in` können wir prüfen,

ob ein bestimmter Key existiert.

```python
server = {
    "name": "web01",
    "status": "online"
}

if "status" in server:
    print("Status vorhanden")
```

<div class="box center">

`in` prüft bei einem Dictionary

standardmäßig die **Keys**.

</div>

---

## Alle Keys

Mit `.keys()` erhalten wir

alle Schlüssel.

```python
server = {
    "name": "web01",
    "status": "online",
    "ram": 32
}

print(server.keys())
```

Das Ergebnis enthält:

```text
name
status
ram
```

---

## Alle Values

Mit `.values()` erhalten wir

alle Werte.

```python
server = {
    "name": "web01",
    "status": "online",
    "ram": 32
}

print(server.values())
```

Das Ergebnis enthält:

```text
web01
online
32
```

---

## Keys durchlaufen

Mit einer `for`-Schleife können wir

alle Keys durchlaufen.

```python
server = {
    "name": "web01",
    "status": "online",
    "ram": 32
}

for key in server:
    print(key)
```

Ausgabe:

```text
name
status
ram
```

<div class="box center">

`key` enthält bei jedem Durchlauf

den aktuellen Schlüssel.

</div>

---

## Key und Value gemeinsam

Oft brauchen wir

**Key und Value gleichzeitig**.

Dafür gibt es `.items()`.

```python
server = {
    "name": "web01",
    "status": "online",
    "ram": 32
}

for key, value in server.items():
    print(key, value)
```

---

## Was passiert bei `items()`?

Python gibt bei jedem Durchlauf

ein Paar aus:

```text
key       value
----------------
"name"    "web01"
"status"  "online"
"ram"     32
```

Deshalb können wir schreiben:

```python
for key, value in server.items():
```

<div class="box center">

`key` → Schlüssel

`value` → zugehöriger Wert

</div>

---

## Ein Dictionary ausgeben

Mit `.items()` können wir

alle Informationen übersichtlich ausgeben.

```python
person = {
    "name": "Sophie",
    "alter": 32,
    "stadt": "Hannover"
}

for key, value in person.items():
    print(key, ":", value)
```

Ausgabe:

```text
name : Sophie
alter : 32
stadt : Hannover
```

---

## Du bist dran

<div class="box">

Gegeben:

```python
buch = {
    "titel": "Python lernen",
    "seiten": 320,
    "verfuegbar": True
}
```

1. Gib den Titel aus.
2. Ändere die Seitenzahl auf `350`.
3. Füge `"sprache": "Deutsch"` hinzu.
4. Gib alle Keys aus.
5. Gib alle Values aus.
6. Gib mit `.items()` Key und Value gemeinsam aus.

</div>

---

## Dictionaries zum Zählen

Ein Dictionary kann auch

Häufigkeiten speichern.

```python
farben = [
    "rot",
    "blau",
    "rot",
    "gruen",
    "blau",
    "rot"
]
```

Wir möchten wissen:

```text
Wie oft kommt jede Farbe vor?
```

---

## Einen Zähler aufbauen

```python
zaehler = {}

for farbe in farben:
    if farbe in zaehler:
        zaehler[farbe] = zaehler[farbe] + 1
    else:
        zaehler[farbe] = 1
```


```python
{
    "rot": 3,
    "blau": 2,
    "gruen": 1
}
```

<div class="box center">

Key → Farbe

Value → Anzahl

</div>

---

## Das Grundprinzip

Beim Zählen:

```text
Ist der Key schon vorhanden?
        │
        ├── Ja
        │    ↓
        │  Value erhöhen
        │
        └── Nein
             ↓
           Value = 1
```

Dieses Muster ist sehr häufig,

wenn Daten ausgewertet werden.

---

## Du bist dran

<div class="box">

Gegeben:

```python
status = [
    "online",
    "offline",
    "online",
    "wartung",
    "offline",
    "online"
]
```

Erstelle ein Dictionary,

das zählt, wie oft jeder Status vorkommt.

---

Erwartetes Ergebnis:

```python
{
    "online": 3,
    "offline": 2,
    "wartung": 1
}
```

</div>

---


# Block 4

## Sets

---

## Was ist ein Set?

Ein Set speichert

**eindeutige Werte.**

Doppelte Werte werden nur einmal gespeichert.

```python
stationen = {
    "Nord",
    "Sued",
    "Nord",
    "West"
}
```

---

## Das Ergebnis

Das Set enthält nur:

```python
{
    "Nord",
    "Sued",
    "West"
}
```

<div class="box center">

`"Nord"` war zweimal vorhanden.

Im Set steht der Wert trotzdem

**nur einmal**.

</div>

---

## Wofür sind Sets praktisch?

Sets eignen sich besonders,

wenn **Duplikate entfernt** werden sollen.

```python
stationen = [
    "Nord",
    "Sued",
    "Nord",
    "West",
    "Sued"
]

eindeutig = set(stationen)
```
---

Danach:

```python
{
    "Nord",
    "Sued",
    "West"
}
```

---

## Gemeinsame Werte finden

Sets können miteinander verglichen werden.

Mit `&` erhalten wir die

**Schnittmenge**.

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
```

---

## Die Schnittmenge

```python
gemeinsam = sensoren_a & sensoren_b
```

Ergebnis:

```python
{
    "temperatur",
    "feuchtigkeit"
}
```

<div class="box center">

Das sind die Werte,

die in **beiden Sets** vorkommen.

</div>

---

## Liste oder Set?

<div class="box">

**Liste**

```python
werte = [20, 20, 21]
```

→ Reihenfolge wichtig  
→ Duplikate möglich

<br>

**Set**

```python
werte = {20, 21}
```

→ eindeutige Werte  
→ Mengen vergleichen

</div>

---


<!-- _class: lead -->

# Block 5

## Verschachtelte Datenstrukturen

---

## Datenstrukturen kombinieren

Datenstrukturen können

**miteinander kombiniert** werden.

Zum Beispiel:

Ein Dictionary enthält eine Liste.

```python
station = {
    "name": "Nord",
    "temperaturen": [18.4, 19.1, 20.3]
}
```

---

## Auf die Liste zugreifen

```python
station["temperaturen"]
```

Ergebnis:

```python
[18.4, 19.1, 20.3]
```

---

## Auf einen einzelnen Wert zugreifen

Jetzt kombinieren wir

**Dictionary + Liste + Index**.

```python
station["temperaturen"][0]
```

Ergebnis:

```text
18.4
```

<div class="box center">

Erst über den Schlüssel zur Liste.

Dann über den Index zum Wert.

</div>

---

## Liste mit Dictionaries

Mehrere Stationen können

in einer Liste gespeichert werden.

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

## Wie ist die Struktur aufgebaut?

<div class="box center">

```text
Liste
 └── Dictionary
      └── Liste
```

</div>

<br>

Die äußere Struktur ist eine Liste.

Jedes Element darin ist ein Dictionary.

---

## Verschachtelte Daten durchlaufen

Wir können die Liste

mit einer Schleife verarbeiten.

```python
for station in stationen:
    name = station["name"]
    temperaturen = station["temperaturen"]

    print(name)
    print(temperaturen)
```

---

## Schritt für Schritt lesen

Bei verschachtelten Daten

nicht alles gleichzeitig lesen.

```python
station = stationen[0]
```

Jetzt haben wir das erste Dictionary.

---

## Den Namen lesen

```python
name = station["name"]
```

Jetzt haben wir:

```text
Nord
```

---

## Die Temperaturen lesen

```python
temperaturen = station["temperaturen"]
```

Jetzt haben wir:

```python
[18.0, 20.0]
```

---

## Einen einzelnen Messwert lesen

```python
erste_temperatur = temperaturen[0]
```

Jetzt haben wir:

```text
18.0
```

<div class="box center">

Schritt für Schritt:

**Liste → Dictionary → Liste → Wert**

</div>

---

<!-- _class: lead -->

# Block 7

## Welche Datenstruktur passt?

---

## Die richtige Struktur wählen

<div class="box center">

Nicht fragen:

**„Welche Struktur kenne ich?“**

Sondern:

**„Welche Struktur passt zu meinen Daten?“**

</div>

---

## Liste

Verwende eine Liste,

wenn mehrere Werte

**in einer Reihenfolge** gespeichert werden sollen.

```python
temperaturen = [
    18.4,
    19.1,
    20.3
]
```

---

## Tupel

Verwende ein Tupel,

wenn mehrere zusammengehörige Werte

**gemeinsam behandelt** werden sollen.

```python
messbereich = (
    18.4,
    20.3
)
```

---

## Dictionary

Verwende ein Dictionary,

wenn Werte über

**Namen oder Schlüssel** angesprochen werden sollen.

```python
station = {
    "name": "Nord",
    "temperatur": 18.4
}
```

---

## Set

Verwende ein Set,

wenn nur **eindeutige Werte** wichtig sind

oder Mengen verglichen werden.

```python
sensoren = {
    "temperatur",
    "druck",
    "feuchtigkeit"
}
```

---

## Verschachtelte Daten

Verwende Kombinationen,

wenn die Daten selbst

**eine Struktur besitzen**.

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

## Der schnelle Überblick

<div class="box">

| Struktur | Typischer Einsatz |
|:---|:---|
| **Liste** | mehrere Werte in Reihenfolge |
| **Tupel** | zusammengehörige Werte |
| **Dictionary** | Schlüssel → Wert |
| **Set** | eindeutige Werte |
| **Verschachtelt** | strukturierte Daten |

</div>

---



<!-- _class: lead -->

# Was du heute gelernt hast

---

## Die wichtigsten Bausteine

<div class="box">

✅ **Liste**  
Mehrere Werte in einer Reihenfolge

<br>

✅ **Tupel**  
Zusammengehörige Werte

<br>

✅ **Dictionary**  
Schlüssel → Wert

<br>

✅ **Set**  
Eindeutige Werte

<br>

✅ **`sorted()`**  
Sortierte neue Liste

<br>

✅ **Verschachtelte Daten**  
Datenstrukturen miteinander kombinieren

</div>


---

<!-- _class: lead -->

# Ausblick auf Tag 3

## Daten dauerhaft speichern

Bisher leben unsere Daten

**direkt im Python-Programm.**

Morgen schauen wir uns Dateien an.

---

## Morgen geht es um

- Textdateien
- CSV-Dateien
- JSON-Dateien
- Dateien lesen
- Dateien schreiben
- strukturierte Daten aus Dateien verarbeiten

<div class="box center">

# Von Daten im Programm

# zu Daten auf der Festplatte

</div>
