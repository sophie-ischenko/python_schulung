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

# Tag 1
## Erste Schritte in Python

Variablen, Datentypen, Rechnen & Text

---

## Was du heute lernst

<br>

1. Was ist Programmierung überhaupt?
2. Was ist eine **Variable**?
3. Die vier **Basis-Datentypen**
4. Wie man mit Variablen **rechnet**
5. Wie man Text und Zahlen zu einem **Satz** verbindet

---

<!-- _class: lead -->

# Block 1

## Was ist Programmierung?

---

## Bild: Der Computer als Koch

<div class="box center">

Ein Computer führt Anweisungen **stur nacheinander** aus –
genau wie ein Koch, der ein Rezept abarbeitet.

Steht im Rezept (Code) ein Fehler,
schmeckt das Essen nicht (**Programmabsturz**).

</div>

---

## Was ist Python?

<div class="box center">

Eine Programmiersprache, die sehr **nah an der
englischen Schriftsprache** ist.

Dadurch ist sie besonders **leicht zu lesen**
und ein guter Einstieg in die Programmierung.

</div>

---

## Dein erster Befehl: print()

```python
print("Hallo Welt")
```

<div class="box center">

Die Ausgabe erscheint **direkt unter der Zelle**:

```
Hallo Welt
```

`print(...)` zeigt dir das, was in den Klammern steht.

</div>

---

## Auch Zahlen und Namen funktionieren

```python
print(25)
print("Sabine")
```

<div class="box center">

`print()` kann **Zahlen** genauso ausgeben
wie **Text** (in Anführungszeichen).

</div>

---

<!-- _class: lead -->

# Variablen

## Die Umzugskartons deines Codes

---

## Bild: Der beschriftete Umzugskarton

<div class="box center">

Eine Variable ist wie ein **beschrifteter
Umzugskarton**.

Du legst einen **Wert hinein**
und schreibst einen **Namen darauf**.

```python
alter = 25
name = "Sabine"
```

</div>

---

## Eine Variable ausgeben

```python
alter = 25
name = "Sabine"

print(alter)
print(name)
```

<div class="box center">

Du sprichst die Variable einfach mit ihrem
**Namen** an – ohne Anführungszeichen!

</div>

---

<!-- _class: lead -->

# Sieben typische Anfängerfehler

## bei Variablennamen

---

## Fehler 1: Anführungszeichen um den Namen

```python
"abteilung" = "IT-Support"   # ❌
```

<div class="box center">

✅ Richtig:

```python
abteilung = "IT-Support"
```

Der **Name links** vom `=` bekommt **keine** Anführungszeichen –
nur der **Text rechts** davon!

</div>

---

## Fehler 2: Fehlende Anführungszeichen beim Text

```python
abteilung = IT-Support   # ❌
```

<div class="box center">

Python sucht jetzt nach einer Variable `IT`
und interpretiert `-` als **Minus**!

✅ Richtig:

```python
abteilung = "IT-Support"
```

</div>

---

## Fehler 3: Groß-/Kleinschreibung

```python
abteilung = "IT-Support"

print(abteilung)   # ✅ funktioniert
print(Abteilung)   # ❌ NameError
```

<div class="box center">

`abteilung` und `Abteilung` sind für Python
**zwei komplett verschiedene** Variablen!

</div>

---

## Fehler 4: Leerzeichen im Namen

```python
meine abteilung = "IT-Support"   # ❌
```

<div class="box center">

✅ Richtig – nutze einen **Unterstrich**:

```python
meine_abteilung = "IT-Support"
```

</div>

---

## Fehler 5: Bindestrich im Namen

```python
it-support = "IT-Support"   # ❌
```

<div class="box center">

Der Bindestrich wird wieder als **Minus** gelesen!

✅ Richtig:

```python
it_support = "IT-Support"
```

</div>

---

## Fehler 6: Variable zu früh benutzen

```python
print(abteilung)          # ❌ gibt es noch nicht!
abteilung = "IT-Support"
```

<div class="box center">

✅ Richtig – **erst anlegen, dann benutzen**:

```python
abteilung = "IT-Support"
print(abteilung)
```

</div>

---

## Fehler 7: Reservierte Wörter

```python
class = "IT-Support"   # ❌
```

<div class="box center">

`class` ist ein **reserviertes Wort** –
Python nutzt es selbst für eine eigene Funktion.

✅ Richtig: einen eigenen, unbenutzten Namen wählen:

```python
abteilung = "IT-Support"
```

</div>

---

<!-- _class: lead -->

# Einfache oder doppelte Anführungszeichen?

---

## Beide sind gleichwertig!

```python
abteilung = "IT-Support"
```
ist dasselbe wie
```python
abteilung = 'IT-Support'
```

<div class="box center">

Python behandelt `' '` und `" "` **völlig gleich**.

</div>

---

## Wann nimmt man die andere Sorte?

<div class="box center">

Wenn der Text selbst schon Anführungszeichen enthält!

```python
text = "Sophies Abteilung heißt 'IT-Support'."
```
```python
text = 'Er sagte: "Hallo!"'
```

</div>

---

## Merksatz

<br>

<div class="box center">

# Wichtig ist nur:
# Anfang und Ende müssen
# mit demselben Zeichen geschrieben werden.

</div>

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Block 2

## Die vier Basis-Datentypen

---

## Text (String)

```python
abteilung = "IT-Support"
```

<div class="box center">

Muss **immer** in Anführungszeichen stehen.

</div>

---

## Ganzzahl (Integer)

```python
tickets_geloest = 8
```

<div class="box center">

Für **zählbare** Dinge – ohne Nachkommastellen.

</div>

---

## Nachkommazahl (Float)

```python
preis = 49.99
```

<div class="box center">

⚠️ Wichtig: Python nutzt einen **Punkt**,
kein Komma!

</div>

---

## Wahrheitswert (Boolean)

```python
server_aktiv = True
```

<div class="box center">

Nur **zwei** mögliche Zustände: `True` oder `False`

⚠️ Wichtig: **groß geschrieben**!

</div>

---

## Die vier Datentypen im Überblick

<div class="box center">

| Typ | Beispiel |
|:---|:---|
| Text (String) | `"IT-Support"` |
| Ganzzahl (Integer) | `8` |
| Nachkommazahl (Float) | `49.99` |
| Wahrheitswert (Boolean) | `True` / `False` |

</div>

---

## Datentyp herausfinden mit type()

```python
a = 10
b = "Hallo"
c = 3.14

print(type(a))   # <class 'int'>
print(type(b))   # <class 'str'>
print(type(c))   # <class 'float'>
```

<div class="box center">

`type(...)` verrät dir, **welcher Datentyp**
sich hinter einer Variable verbirgt.

</div>

---

## Achtung: Zahl oder Text?

```python
zahl1 = 5
zahl2 = "5"

print(type(zahl1))   # <class 'int'>
print(type(zahl2))   # <class 'str'>
```

<div class="box center">

Beide **sehen** gleich aus – `5` –

aber `zahl2` steht in Anführungszeichen und
ist deshalb **Text**, keine Zahl!

</div>

---

<!-- _class: lead -->

# Block 3

## Rechnen mit Variablen

---

## Eine Variable kann ein Ergebnis speichern

```python
grundpreis = 100
neuer_preis = grundpreis + 20

print(neuer_preis)
```

<div class="box center">

```
grundpreis + 20  ──►  120  ──►  neuer_preis
   (Rechnung)      (Ergebnis)     (Box)
```

**Merke:** Die rechte Seite wird **zuerst** berechnet.
Das Ergebnis wandert danach in die Variable.

</div>

---

## Die vier Grundrechenarten

<div class="box center">

| Zeichen | Bedeutung | Beispiel | Ergebnis |
|:---:|:---|:---:|:---:|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraktion | `5 - 3` | `2` |
| `*` | Multiplikation | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1.666...` |

Python nutzt `*` statt `×` und `/` statt `÷`.

</div>

---

## Formeln in zwei Schritten übersetzen

<div class="box">

**Schritt 1:** Formel in Worten aufschreiben

```
Fläche = Breite × Länge
```

**Schritt 2:** Wörter durch Variablennamen ersetzen

```python
flaeche = breite * laenge
```

</div>

---

## Beispiel: Fläche berechnen

```python
breite = 5
laenge = 10

flaeche = breite * laenge
print(flaeche)
```

<div class="box center">

Genau nach dem Muster von der letzten Folie:
erst die Formel, dann der Code.

</div>

---

## Umrechnungen: kleine in große Einheit

<div class="box center">

**Faustregel:** Wie viele kleine Einheiten
passen in eine große? → das ist der Multiplikator.

```
1 Stunde = 60 Minuten   →   minuten = stunden * 60
```

```python
stunden = 2
minuten = stunden * 60
print(minuten)   # 120
```

</div>

---

## Prozentrechnung: Prozent als Dezimalzahl

<div class="box center">

| Prozent | Als Dezimalzahl |
|:---:|:---:|
| 10 % | `0.10` |
| 15 % | `0.15` |
| 19 % | `0.19` |

</div>

---

## Zwei Schritte zum Endpreis

```python
preis = 200

# Schritt 1: Rabattbetrag berechnen
rabattbetrag = preis * 0.15

# Schritt 2: Rabatt vom Preis abziehen
endpreis = preis - rabattbetrag
```

<div class="box center">

```
  preis         rabattbetrag        endpreis
 ┌─────┐  ×0.15  ┌─────┐   200−     ┌─────┐
 │ 200 │ ──────► │  30 │ ─────────► │ 170 │
 └─────┘         └─────┘            └─────┘
```

</div>

---

## Warum Zwischenschritte sinnvoll sind

<div class="box center">

Jeder Rechenschritt bekommt einen **eigenen Namen**.

So bleibt dein Code **leicht lesbar**,
und du kannst jeden Schritt einzeln
mit `print()` **kontrollieren**.

</div>

---

<!-- _class: lead -->

# Vom Aufgabentext zum Code

## Die vier Übersetzungsschritte

---

## Der Ablauf, der immer funktioniert

<div class="box center">

① Text lesen
⬇️
② Formel finden
⬇️
③ Variablen benennen
⬇️
④ Code schreiben

</div>

---

## Schritt ①: Zahlen im Text markieren

<div class="box">

*"Ein Raum hat eine Breite von 5 Metern
und eine Länge von 8 Metern.
Berechnen Sie die Fläche."*

- Breite = **5**
- Länge = **8**
- Gesucht: **Fläche**

</div>

---

## Schritt ②: Die passende Formel finden

<div class="box center">

| Schlüsselwort im Text | Rechenart |
|:---|:---:|
| "Summe", "zusammen" | `+` |
| "Differenz", "Rabatt" | `-` |
| "Fläche", "Volumen" | `*` |
| "aufteilen", "pro Person" | `/` |

</div>

---

## Schritt ③: Variablennamen vergeben

<div class="box center">

| Text | Variablenname | Wert |
|:---|:---|:---:|
| Breite | `breite` | 5 |
| Länge | `laenge` | 8 |
| Fläche (Ergebnis) | `flaeche` | wird berechnet |

💡 Tipp: Nimm das deutsche Wort aus der Aufgabe –
so findest du dich im Code sofort zurecht.

</div>

---

## Schritt ④: Tabelle in Code übertragen

```python
breite = 5
laenge = 8
flaeche = breite * laenge
print(flaeche)
```

<div class="box center">

Die Tabelle von eben – **1:1** in Python übersetzt.

</div>

---

## Checkliste vor dem Ausführen

<div class="box">

☐ Habe ich für **jede Zahl** aus dem Text eine Variable?

☐ Passt mein Operator (`+ - * /`) zur Aufgabe?

☐ Ist die **Reihenfolge** richtig? (z. B. erst Rabatt berechnen,
dann abziehen)

☐ Steht am Ende ein `print()`?

</div>

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Block 4

## Text und Variablen verbinden

---

## Drei Wege zum Ziel

<div class="box center">

**Komma `,`** → einfachste Methode,
automatisches Leerzeichen

**Plus `+`** → "Zusammenkleben",
Leerzeichen selbst setzen

**f-String `f""`** → modernste Methode,
Variablen direkt in `{}`

</div>

---

## Methode 1: das Komma

```python
name = "Michael"
print("Guten Tag,", name)
```

<div class="box center">

```
"Guten Tag,"  ,  name
        ⬇️
Guten Tag, Michael
```

Python setzt **automatisch ein Leerzeichen**
zwischen den durch Komma getrennten Teilen.

</div>

---

## Methode 2: der Plus-Operator

```python
vorname = "Lisa"
nachname = "Schmid"

print(vorname + nachname)         # LisaSchmid ❌
print(vorname + " " + nachname)   # Lisa Schmid ✅
```

<div class="box center">

⚠️ Beim `+` fügt Python **kein** Leerzeichen
automatisch ein – du musst es selbst setzen!

</div>

---

## Die große Falle: Text + Zahl

```python
alter = 30
print("Ich bin " + alter)   # ❌ TypeError!
```

<div class="box center">

`+` kann nur **gleiche Datentypen** verbinden.

Text und Zahl lassen sich mit `+` **nicht**
einfach zusammenkleben!

</div>

---

## Funktioniert das oder nicht?

<div class="box center">

| Ausdruck | Funktioniert? |
|:---|:---:|
| `"Text" + "Text"` | ✅ |
| `5 + 3` | ✅ |
| `"Text" + 5` | ❌ |

</div>

---

## Methode 3: der f-String (die moderne Lösung)

```python
benutzer = "Felix"
anzahl_tickets = 4

print(f"Hallo {benutzer}, du hast heute {anzahl_tickets} Tickets gelöst.")
```

<div class="box center">

Ein `f` **vor** den Anführungszeichen –
und Variablen kommen einfach in `{geschweifte Klammern}`.

</div>

---

## So baust du einen f-String

<div class="box center">

**Schritt 1:** `f` vor die Anführungszeichen setzen → `f"..."`

**Schritt 2:** Variablen in geschweifte Klammern packen → `{variable}`

**Schritt 3:** Alles andere bleibt normaler Text

</div>

---

## Der große Vorteil von f-Strings

<div class="box center">

f-Strings verbinden Text und Zahlen
**ohne Fehler** –

der `TypeError` von Methode 2
tritt hier **niemals** auf!

</div>

---

## Alle drei Methoden im Vergleich

<div class="box center">

| Methode | Leerzeichen? | Text + Zahl mischen? |
|:---|:---:|:---:|
| Komma `,` | automatisch ✅ | problemlos ✅ |
| Plus `+` | selbst setzen ⚠️ | nur mit Umweg ❌ |
| f-String `f""` | wie normaler Text | problemlos ✅ |

🏆 **Empfehlung:** Für das Mischen von Text und Zahlen
ist der **f-String** fast immer die beste Wahl.

</div>

---

<!-- _class: lead -->

# Jetzt du: viel Übung!

---

## Was dich erwartet

<div class="box">

Zu jedem Block gibt es passende **"Du bist dran"**-Aufgaben:

- Eigene Variablen anlegen und ausgeben
- Datentypen erkennen und korrigieren
- Formeln aus Textaufgaben in Code übersetzen
- Text und Zahlen mit allen drei Methoden verbinden

</div>

<br>

Alle Aufgaben findest du im **Colab-Notebook**.

---

<!-- _class: lead -->

# Was du heute gelernt hast

<div class="box">

✅ Eine **Variable** ist ein beschrifteter Umzugskarton für einen Wert

✅ Die vier Basis-Datentypen: **String, Integer, Float, Boolean**

✅ Formeln lassen sich in **vier Schritten** in Code übersetzen

✅ Text und Zahlen verbindest du am besten mit einem **f-String**

</div>

<br>

## Morgen geht's weiter: Benutzereingaben mit input() 🎉