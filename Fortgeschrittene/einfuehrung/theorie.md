# Einführung in Python – Tag 0

Willkommen zum Python-Kurs.

Bevor wir mit den eigentlichen Kursinhalten starten, wiederholen wir die wichtigsten Grundlagen der Python-Syntax. Dieser Einstieg ist bewusst kurz gehalten und dient als gemeinsamer Ausgangspunkt für den weiteren Kurs.

Wir arbeiten dabei mit Ausgaben, Zahlen, Variablen, einfachen Berechnungen und Funktionen. Zum Abschluss setzen wir mehrere dieser Bausteine in einem kleinen Programm zusammen.

## Lernziele

Nach diesem Einstieg kannst du:

- mit `print()` Werte auf der Konsole ausgeben
- Zahlen und Text unterscheiden
- einfache mathematische Berechnungen durchführen
- Werte in Variablen speichern
- Variablen in Berechnungen verwenden
- einfache Funktionen mit Parametern und `return` schreiben
- einfache Bedingungen formulieren
- Benutzereingaben mit `input()` verarbeiten

---

# 1. Ausgaben mit `print()`

Mit `print()` gibt Python einen Wert auf der Konsole aus.

```python
print("Hallo Welt!")
```

Ausgabe:

```text
Hallo Welt!
```

Auch Zahlen können ausgegeben werden:

```python
print(42)
print(3.14)
```

Mehrere Werte können durch Kommata getrennt ausgegeben werden:

```python
name = "Ada"
alter = 25

print("Name:", name)
print("Alter:", alter)
```

Ausgabe:

```text
Name: Ada
Alter: 25
```

## Wichtig

Text wird in Anführungszeichen geschrieben:

```python
print("Hallo")
```

Eine Zahl wird ohne Anführungszeichen geschrieben:

```python
print(42)
```

Der Unterschied ist wichtig:

```python
print(42)
print("42")
```

Beide sehen in der Ausgabe gleich aus:

```text
42
42
```

Für Python sind sie aber unterschiedliche Datentypen.

---

# 2. Zahlen und Rechenoperationen

Python kann als Taschenrechner verwendet werden.

Die wichtigsten Rechenoperatoren sind:

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `+` | Addition | `5 + 3` |
| `-` | Subtraktion | `5 - 3` |
| `*` | Multiplikation | `5 * 3` |
| `/` | Division | `10 / 2` |

Beispiel:

```python
print(5 + 3)
print(10 - 4)
print(5 * 3)
print(10 / 2)
```

Ergebnis:

```text
8
6
15
5.0
```

Bei der Division liefert Python standardmäßig einen `float`:

```python
10 / 2
```

ergibt:

```text
5.0
```

---

# 3. Dezimalzahlen

Dezimalzahlen werden in Python mit einem Punkt geschrieben.

```python
preis = 12.50
```

Nicht mit einem Komma:

```python
preis = 12,50
```

Das Komma hat in Python eine andere Bedeutung.

---

# 4. Strings und Zahlen

Ein häufiger Fehler besteht darin, Text und Zahlen miteinander zu verwechseln.

```python
zahl = 10
text = "10"
```

Hier ist `zahl` eine Zahl und `text` ein String.

Das kann man auch beim Rechnen sehen:

```python
print(10 + 5)
```

ergibt:

```text
15
```

Aber:

```python
print("10" + "5")
```

ergibt:

```text
105
```

Bei Strings bedeutet `+` das Aneinanderhängen von Text.

---

# 5. Variablen

Variablen speichern Werte unter einem Namen.

```python
alter = 25
```

Danach kann der Wert über `alter` verwendet werden:

```python
print(alter)
```

Ausgabe:

```text
25
```

Eine Variable kann auch für Berechnungen verwendet werden:

```python
alter = 25
naechstes_jahr = alter + 1

print(naechstes_jahr)
```

Ausgabe:

```text
26
```

## Zuweisung mit `=`

Das Gleichheitszeichen bedeutet bei einer Zuweisung:

> Speichere den Wert auf der rechten Seite unter dem Namen auf der linken Seite.

Beispiel:

```python
preis = 20
```

Danach enthält `preis` den Wert `20`.

---

# 6. Variablen verändern

Eine Variable kann später einen neuen Wert bekommen.

```python
punkte = 10

print(punkte)

punkte = 20

print(punkte)
```

Ausgabe:

```text
10
20
```

Die zweite Zuweisung überschreibt den vorherigen Wert.

---

# 7. Mit Variablen rechnen

Variablen können miteinander kombiniert werden.

```python
preis = 15
anzahl = 3

gesamtpreis = preis * anzahl

print(gesamtpreis)
```

Ausgabe:

```text
45
```

Das macht Programme flexibler als fest eingetragene Werte:

```python
preis = 15
anzahl = 3
```

Wenn sich `anzahl` ändert, wird automatisch ein anderes Ergebnis berechnet:

```python
preis = 15
anzahl = 5

gesamtpreis = preis * anzahl

print(gesamtpreis)
```

Ergebnis:

```text
75
```

---

# 8. Variablennamen

Variablennamen sollten verständlich gewählt werden.

Gut:

```python
name = "Ada"
alter = 25
preis = 19.99
anzahl = 3
```

Weniger aussagekräftig:

```python
x = "Ada"
a = 25
p = 19.99
n = 3
```

Bei mehreren Wörtern wird in Python häufig `snake_case` verwendet:

```python
geburtsjahr = 2000
aktuelles_jahr = 2026
gesamtpreis = 59.97
```

---

# 9. Funktionen

Funktionen kapseln Code, der eine bestimmte Aufgabe erledigt.

Eine einfache Funktion sieht so aus:

```python
def hallo():
    print("Hallo!")
```

Die Funktion wird zunächst definiert. Ausgeführt wird sie durch einen Aufruf:

```python
hallo()
```

Ausgabe:

```text
Hallo!
```

---

# 10. Parameter

Eine Funktion kann Werte als Parameter entgegennehmen.

```python
def begruessen(name):
    print("Hallo", name)
```

Aufruf:

```python
begruessen("Ada")
```

Ausgabe:

```text
Hallo Ada
```

Der Wert `"Ada"` wird beim Aufruf an den Parameter `name` übergeben.

---

# 11. `return`

Eine Funktion kann ein Ergebnis zurückgeben.

Dafür verwenden wir `return`.

```python
def addiere(zahl1, zahl2):
    return zahl1 + zahl2
```

Die Funktion selbst gibt das Ergebnis zurück:

```python
ergebnis = addiere(5, 3)

print(ergebnis)
```

Ausgabe:

```text
8
```

Das ist ein wichtiger Unterschied:

```python
def addiere(zahl1, zahl2):
    print(zahl1 + zahl2)
```

gibt etwas aus.

Während:

```python
def addiere(zahl1, zahl2):
    return zahl1 + zahl2
```

ein Ergebnis zurückgibt, das anschließend weiterverwendet werden kann.

Zum Beispiel:

```python
ergebnis = addiere(5, 3)
doppelt = ergebnis * 2

print(doppelt)
```

Ausgabe:

```text
16
```

---

# 12. Bedingungen

Mit Bedingungen kann ein Programm unterschiedliche Wege einschlagen.

```python
alter = 20

if alter >= 18:
    print("Volljährig")
```

Ist die Bedingung wahr, wird der eingerückte Code ausgeführt.

Mit `else` kann ein zweiter Fall definiert werden:

```python
alter = 16

if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

Ausgabe:

```text
Minderjährig
```

Die Einrückung ist in Python Teil der Syntax.

---

# 13. Benutzereingaben

Mit `input()` kann ein Programm Daten vom Benutzer abfragen.

```python
name = input("Wie heißt du? ")

print("Hallo", name)
```

Wenn der Benutzer `Ada` eingibt:

```text
Wie heißt du? Ada
Hallo Ada
```

## Wichtig: `input()` liefert Text

Auch wenn eine Zahl eingegeben wird, liefert `input()` zunächst einen String.

```python
alter = input("Wie alt bist du? ")
```

Wenn der Benutzer `25` eingibt, enthält `alter` den Text `"25"`.

Wenn wir tatsächlich mit der Zahl rechnen möchten, müssen wir den Wert umwandeln:

```python
alter = int(input("Wie alt bist du? "))
```

Jetzt enthält `alter` eine ganze Zahl.

---

# 14. Mini-Wiederholung

Die wichtigsten Bausteine dieses Einstiegs:

```python
# Ausgabe
print("Hallo")

# Variable
name = "Ada"

# Berechnung
alter = 25
naechstes_jahr = alter + 1

# Funktion
def addiere(a, b):
    return a + b

# Bedingung
if alter >= 18:
    print("Volljährig")

# Eingabe
name = input("Name: ")
```

Diese Bausteine bilden die Grundlage für die folgenden Kurstage.

---

# 15. Übungen

Öffne:

```text
aufgaben.py
```

Bearbeite die drei markierten Aufgaben.

| Nr. | Funktion | Aufgabe |
|---|---|---|
| 1 | `hallo_welt()` | Einen festen Text zurückgeben |
| 2 | `addiere()` | Zwei Zahlen addieren |
| 3 | `berechne_alter()` | Das Alter aus zwei Jahreszahlen berechnen |

Starte anschließend den automatischen Test:

```bash
python aufgaben.py
```

Ein `✓` bedeutet, dass der Test erfolgreich war.

Ein `✗` zeigt dir das erwartete und das tatsächlich erhaltene Ergebnis.

---

# 16. Mini-Projekt: Der Begrüßungs-Bot

Zum Abschluss kombinieren wir mehrere Grundlagen in einem kleinen Programm.

Der Benutzer gibt seinen Namen und sein Alter ein.

Das Programm:

1. erstellt eine persönliche Begrüßung
2. prüft, ob die Person volljährig ist
3. gibt das Ergebnis auf der Konsole aus

Beispiel:

```text
=== START DES BOTS ===
Wie heißt du? Ada
Wie alt bist du? 25
Hallo Ada! Willkommen an Bord.
Du bist volljährig. Du darfst alle Funktionen nutzen.
=== ENDE ===
```

Die Funktionen `erstelle_begruessung()` und `ist_volljaehrig()` enthalten jeweils eine `TODO`-Stelle.

Bearbeite nur diese Stellen.

## Programm starten

```bash
python projekt.py
```

## Automatischen Selbsttest starten

```bash
python projekt.py test
```

Der Selbsttest überprüft verschiedene Eingaben automatisch.

---

# Abschluss

Damit sind die grundlegenden Python-Bausteine wiederholt.

Im weiteren Kurs geht es nicht mehr darum, `print()` oder Variablen einzeln kennenzulernen. Stattdessen werden die Bausteine kombiniert und auf komplexere Aufgaben angewendet.

Ab Tag 1 geht es mit den eigentlichen Kursinhalten weiter.