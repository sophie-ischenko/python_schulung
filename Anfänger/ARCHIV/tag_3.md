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
## Fehler finden, Texte zerschneiden & selbst recherchieren

Python-Grundlagen-Schulung

---

## Was du heute lernst

<br>

1. Kurzes Aufwärmen mit dem bisher Gelernten
2. Fehlermeldungen **lesen** und **reparieren** (Debugging)
3. Einzelne Zeichen aus einem Text herausschneiden (**Slicing**)
4. Wie du selbst nach Python-Lösungen **recherchierst**

---

<!-- _class: lead -->

# Teil 1

## Aufwärmen

---

## Vier kurze Wiederholungsaufgaben

<div class="box">

Bevor es weitergeht, frischt du kurz auf,
was du bisher gelernt hast:

- Alter berechnen
- Minuten in Stunden umrechnen (`//` und `%`)
- Rabatt berechnen
- Terabyte in Gigabyte umrechnen

</div>

<br>

Alle vier Aufgaben findest du im **Colab-Notebook**.

---

<!-- _class: lead -->

# Teil 2

## Der Code-Sanitäter

## Fehler lesen und reparieren

---

## Die wichtigste Debugging-Regel

<br>

<div class="box center">

# Lies die Fehlermeldung
# von UNTEN nach OBEN.

</div>

<br>

Die **letzte Zeile** verrät dir meistens,
was wirklich schiefgelaufen ist.

---

## Fehler 1: Text minus Zahl (TypeError)

```python
offene_tickets = input("Wie viele offene Tickets? ")
geloeste_tickets = 5

verbleibend = offene_tickets - geloeste_tickets
print("Es verbleiben: " + verbleibend)
```

<div class="box center">

❌ **TypeError**: `input()` liefert immer **Text** –
Text minus Zahl geht nicht!

</div>

---

## So wird Fehler 1 repariert

```python
offene_tickets = int(input("Wie viele offene Tickets? "))
geloeste_tickets = 5

verbleibend = offene_tickets - geloeste_tickets
print(f"Es verbleiben: {verbleibend}")
```

<div class="box center">

✅ `int(...)` wandelt die Eingabe in eine Zahl um.

✅ Ein f-String kann Text und Zahl problemlos mischen.

</div>

---

## Fehler 2: Klammer und Tippfehler

```python
srv_name = "SRV-Backup"
status_aktiv = True

print(f"Server {srv_Name} hat den Status: {status_aktiv}"
```

<div class="box center">

❌ Erst: fehlende schließende Klammer `)`

❌ Dann: `srv_Name` mit großem N – aber die Variable
heißt `srv_name` mit **kleinem** n!

</div>

---

## Wichtig zu wissen

<div class="box center">

Python unterscheidet **streng** zwischen
Groß- und Kleinschreibung.

`srv_name` und `srv_Name` sind für Python
**zwei völlig unterschiedliche** Variablen!

</div>

---

## So wird Fehler 2 repariert

```python
srv_name = "SRV-Backup"
status_aktiv = True

print(f"Server {srv_name} hat den Status: {status_aktiv}")
```

<div class="box center">

✅ Klammer geschlossen, Schreibweise korrigiert.

</div>

---

## Fehler 3: Dezimalzahl mit int() (ValueError)

```python
freier_speicher = int(input("Wie viel GB freier Speicher? "))
bedarf = 1.2
rest = freier_speicher - bedarf
print(f"Restlicher Speicher: {rest} GB")
```

<div class="box center">

Eingabe: `2.5` → ❌ **ValueError**

`int()` kann keine Zahl mit Komma/Punkt verarbeiten!

</div>

---

## So wird Fehler 3 repariert

```python
freier_speicher = float(input("Wie viel GB freier Speicher? "))
bedarf = 1.2
rest = freier_speicher - bedarf
print(f"Restlicher Speicher: {rest} GB")
```

<div class="box center">

✅ `float(...)` statt `int(...)` –
erlaubt Dezimalzahlen.

</div>

---

## Fehler 4: Division durch Null

```python
gesamtspeicher_gb = 500
aktive_server = 0

last_pro_server = gesamtspeicher_gb / aktive_server
```

<div class="box center">

❌ **ZeroDivisionError**

Eine Division durch Null ist mathematisch
**nicht definiert** – Python bricht deshalb ab.

</div>

---

## So wird Fehler 4 repariert

```python
gesamtspeicher_gb = 500
aktive_server = 2  # darf nicht 0 sein!

last_pro_server = gesamtspeicher_gb / aktive_server
print(f"Jeder Server erhält {last_pro_server} GB.")
```

<div class="box center">

✅ Der Nenner darf **niemals 0** sein.

Im echten IT-Alltag: genau das passiert,
wenn z. B. gerade kein Server aktiv ist!

</div>

---

<!-- _class: lead -->

# Teil 3

## Texte gezielt zerschneiden

## String-Slicing

---

## Ein String ist eine Kette aus Zeichen

<div class="box center">

```
Zeichen:   P   y   t   h   o   n
Index+:    0   1   2   3   4   5
Index-:   -6  -5  -4  -3  -2  -1
```

Jedes einzelne Zeichen hat eine **Nummer (Index)** –
gezählt ab **0**, von links **und** von rechts.

</div>

---

## Ein einzelnes Zeichen holen

```python
wort = "Python"

print(wort[0])    # P  (erstes Zeichen)
print(wort[-1])   # n  (letztes Zeichen)
```

<div class="box center">

Eckige Klammern `[...]` mit einer **Zahl**
holen dir genau **ein** Zeichen an dieser Position.

</div>

---

## Einen ganzen Bereich ausschneiden

```python
wort = "Python"
print(wort[0:3])   # Pyt
```

<div class="box center">

`[start:stop]` schneidet einen **Bereich** aus.

⚠️ Wichtig: **`stop` gehört nicht mehr dazu!**

`[0:3]` heißt: Index 0, 1, 2 – **nicht** Index 3.

</div>

---

## Bild: Slicing wie ein Lineal

<div class="box center">

```
   P   y   t   h   o   n
 0   1   2   3   4   5   6
```

Die Zahlen stehen **zwischen** den Buchstaben.

`wort[0:3]` schneidet zwischen Position 0 und 3 –
das ergibt **"Pyt"**.

</div>

---

## Schrittweite: Zeichen überspringen

```python
wort = "Python"

print(wort[::2])    # Pto   (jedes zweite Zeichen)
print(wort[::-1])   # nohtyP (rückwärts!)
```

<div class="box center">

`[start:stop:step]` – der dritte Wert ist die **Schrittweite**.

`::-1` ist ein beliebter Trick, um einen
kompletten String rückwärts auszugeben.

</div>

---

## Merksatz

<br>

<div class="box center">

# [start:stop] schneidet aus –
# stop selbst ist NICHT mehr dabei.

</div>

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Teil 4

## String-Methoden & selbst recherchieren

---

## Was ist eine Methode?

<div class="box center">

Eine Methode ist ein **fertiger Befehl**,
den du direkt an einen String anhängst.

```python
text = "Hallo Python"
print(text.upper())   # HALLO PYTHON
print(text.lower())   # hallo python
```

Der Punkt `.` verbindet den String mit der Methode.

</div>

---

## Die wichtigste Fähigkeit heute: selbst suchen!

<div class="box center">

Niemand kann sich **alle** Methoden merken –
auch erfahrene Programmierer/innen googeln ständig.

**Das ist völlig normal und keine Schwäche.**

</div>

---

## Die Such-Formel

<br>

<div class="box center">

# python string [was ich tun möchte]

</div>

<br>

**Beispiel:** "python string remove spaces"
→ führt dich direkt zur Methode `.strip()`

---

## So gehst du vor

<div class="box">

1. Überlege: **Was** will ich mit dem Text machen?
   (z. B. "Leerzeichen entfernen")
2. Formuliere das auf **Englisch**, ganz simpel
3. Google: `python string [dein Ziel]`
4. Meistens landest du direkt bei der passenden Methode

</div>

---

<!-- _class: lead -->

# Teil 5

## Jetzt du: der große Übungs-Slam

---

## Teil A: Slicing-Aufgaben

<div class="box">

Ländercode aus Servernamen extrahieren

Dateiendung mit negativem Index bestimmen

Mittleren Teil einer Seriennummer herausschneiden

Ein Wort rückwärts ausgeben

Jeden zweiten Buchstaben herausfiltern

</div>

---

## Teil B: Recherche-Aufgaben

<div class="box">

Diese Aufgaben verraten dir **nicht** direkt die Methode –
du sollst sie selbst googeln!

- Leerzeichen entfernen
- Prüfen, ob eine Datei auf `.exe` endet
- Zeichen in einem Pfad ersetzen
- Vorkommen eines Wortes zählen
- Prüfen, ob ein String nur Ziffern enthält
- Eine Zeile am Semikolon zerlegen

</div>

---

## Ein Beispiel zum Warmwerden

```python
server_name = "DE-MUN-SRV01"
laendercode = server_name[0:2]
print(laendercode)   # DE
```

<div class="box center">

Genau das Prinzip, das du gerade
Schritt für Schritt kennengelernt hast.

</div>

---

<!-- _class: lead -->

# Was du heute gelernt hast

<div class="box">

✅ Fehlermeldungen von **unten nach oben** lesen

✅ `[start:stop]` schneidet Text aus – `stop` zählt nicht mehr mit

✅ `[::-1]` dreht einen String um, `[::2]` überspringt Zeichen

✅ Bei unbekannten Methoden: einfach **googeln** – das ist normal!

</div>

<br>

## Morgen: Coding-Arena & Einstieg in Listen 🎉