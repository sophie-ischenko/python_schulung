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

# Tag 6
## Listen-Wiederholung & Entscheidungen treffen

Python-Grundlagen-Schulung

---

## Was du heute lernst

<br>

1. Kurze Auffrischung: Was konnten Listen nochmal?
2. Wie trifft mein Programm **Entscheidungen**? (`if` / `elif` / `else`)
3. Wie **vergleiche** ich Werte miteinander?
4. Wie **kombiniere** ich mehrere Bedingungen? (`and` / `or` / `not`)

---

<!-- _class: lead -->

# Teil 1

## Kurze Listen-Auffrischung

---

## Was du schon über Listen weißt

<div class="box">

Eine Liste ist wie eine **Kiste mit mehreren Fächern**,
in der du mehrere Werte hintereinander speicherst.

```python
offene_ports = [80, 443, 22]
```

Du kannst Werte **hinzufügen**, **ändern**,
**entfernen** und **sortieren**.

</div>

---

## Ein Beispiel zum Aufwärmen

```python
offene_ports = [80, 443, 22]
offene_ports.append(8080)
print(f"Überwachte Ports: {len(offene_ports)}")
```

<div class="box center">

`.append(...)` fügt einen Wert **hinten** an

`len(...)` verrät dir, **wie viele** Werte in der Liste sind

</div>

---

## Heute im Übungsblock

<div class="box">

6 Aufgaben zum Warmwerden, unter anderem:

- Werte hinzufügen und ersetzen
- Minimum und Maximum finden
- Einen Wert entfernen und speichern
- Sortieren
- Prüfen: Ist ein Wert in der Liste enthalten?

</div>

<br>

Alle Aufgaben und Lösungen findest du im **Colab-Notebook**.

---

<!-- _class: lead -->

# Teil 2

## Entscheidungen treffen

---

## Bisher: Dein Code lief stur ab

<div class="box center">

Zeile 1 → Zeile 2 → Zeile 3 → ...

Immer **in der gleichen Reihenfolge**,
egal was passiert.

Das nennt man **sequenziellen Ablauf**.

</div>

---

## Ab heute: Dein Code kann reagieren!

<div class="box center">

"Ist der Speicher voll? → Sende eine Warnung."

"Ist er es nicht? → Mache normal weiter."

Genau das ermöglichen **Bedingungen**.

</div>

---

## Bild: Die Weggabelung

<div class="box center">

Ein Wanderer kommt an eine Weggabelung.

**"Ist der linke Weg frei? Wenn ja, gehe links.
Sonst gehe rechts."**

Eine `if`-Bedingung ist genau so eine Weggabelung
in deinem Code.

</div>

---

## Warum ist das so wichtig?

<div class="box center">

Ohne Bedingungen ist ein Programm nur eine
**Liste stur abzuarbeitender Befehle**.

**Mit** Bedingungen wird es zu einem
System, das auf seine Umgebung **reagiert**.

</div>

---

## Ein einfaches Beispiel

```python
speicher = 8  # GB freier Speicher

if speicher < 10:
    print("Achtung: Wenig Speicherplatz!")
else:
    print("Speicherplatz ist ausreichend.")
```

<div class="box center">

`speicher` ist **8** → `8 < 10` ist **wahr**

→ die erste Zeile wird ausgeführt

</div>

---

## Die einzelnen Bausteine

<div class="box">

**`if`** → "wenn" – leitet die Bedingung ein

**Bedingung** (z. B. `speicher < 10`) → ergibt `True` oder `False`

**`:`** → Doppelpunkt, **immer** nötig nach `if`/`else`

**Einrückung** → zeigt, was zum `if`-Block gehört

**`else`** → "andernfalls" – optional, fängt den Rest ab

</div>

---

## Ganz wichtig: die Einrückung

<div class="box center">

Anders als in vielen anderen Programmiersprachen
benutzt Python **keine geschweiften Klammern** `{}`.

Stattdessen zeigt die **Einrückung selbst**,
was zusammengehört.

Alle Zeilen im selben Block müssen
**gleich weit** eingerückt sein!

</div>

---

## Ein wichtiger Merksatz

<br>

<div class="box center">

# Python prüft die Bedingung
# genau EINMAL,
# an genau dieser Stelle im Code.

</div>

---

<!-- _class: lead -->

# Vergleichsoperatoren

## Das Vokabular der Bedingungen

---

## Die sechs Vergleichsoperatoren

<div class="box center">

| Zeichen | Bedeutung |
|:---:|---|
| `==` | ist gleich |
| `!=` | ist ungleich |
| `<` | kleiner als |
| `>` | größer als |
| `<=` | kleiner oder gleich |
| `>=` | größer oder gleich |

</div>

---

## Die wichtigste Stolperfalle

<div class="box center">

**`=`** → Zuweisung
"Speichere den Wert in der Variable"

**`==`** → Vergleich
"Sind diese beiden Werte gleich?"

</div>

<br>

Ein einzelnes statt doppeltes `=` in einer Bedingung
ist einer der häufigsten Anfängerfehler!

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Teil 3

## Mehrere Bedingungen kombinieren

---

## Wenn eine Bedingung nicht reicht

<div class="box center">

Ein Server ist vielleicht nicht schon dann kritisch,
wenn **nur** die CPU hoch ist.

Vielleicht erst, wenn **gleichzeitig**
auch der Arbeitsspeicher knapp wird.

Dafür brauchen wir **logische Operatoren**.

</div>

---

## and: beide müssen zutreffen

<div class="box center">

🔐🔐 **Bild:** Eine Tür mit **zwei Schlössern**.

Beide müssen **gleichzeitig** aufgeschlossen sein,
damit die Tür aufgeht.

</div>

```python
if cpu_auslastung > 80 and ram_auslastung > 80:
    print("Kritisch: Gesamter Server ist überlastet!")
```

---

## or: einer reicht schon

<div class="box center">

🔔🔔 **Bild:** Eine Tür mit **zwei Klingelknöpfen**.

Es reicht, wenn **irgendjemand** klingelt,
damit die Glocke ertönt.

</div>

```python
if cpu_auslastung > 80 or ram_auslastung > 80:
    print("Warnung: Eine Komponente ist stark ausgelastet.")
```

---

## not: das Gegenteil

<div class="box center">

`not` dreht einen Wahrheitswert einfach um.

Aus `True` wird `False`.
Aus `False` wird `True`.

```python
if not gesperrt:
    print("Das System ist nicht gesperrt.")
```

</div>

---

## Die Merktabelle

<div class="box center">

| A | B | `A and B` | `A or B` |
|:---:|:---:|:---:|:---:|
| wahr | wahr | wahr | wahr |
| wahr | falsch | falsch | wahr |
| falsch | wahr | falsch | wahr |
| falsch | falsch | falsch | falsch |

</div>

---

## in: Ist etwas in einer Liste enthalten?

```python
vip_kunden = ["Müller", "Schmidt", "Fischer"]
kunde = "Schmidt"

if kunde in vip_kunden:
    print("Priorisierter VIP-Support aktivieren.")
else:
    print("Standard-Support-Warteschlange.")
```

<div class="box center">

`in` prüft: **Kommt dieser Wert in der Liste vor?**

Viel übersichtlicher als
`kunde == "Müller" or kunde == "Schmidt" or ...`

</div>

---

<!-- _class: lead -->

# Bonus

## Mehr als zwei Fälle: elif

---

## Wenn zwei Fälle nicht reichen

<div class="box center">

`elif` heißt kurz für **"else if"** – "sonst wenn".

Damit prüfst du **mehrere** Fälle nacheinander.

Python nimmt den **ersten** Fall, der zutrifft –
alle weiteren werden übersprungen.

</div>

---

## Beispiel: Temperaturalarm

```python
temp = float(input("Temperatur (°C): "))

if temp > 25:
    print("Kritisch: Zu heiß!")
elif temp < 18:
    print("Warnung: Zu kalt!")
else:
    print("Temperatur optimal.")
```

<div class="box center">

Python prüft **von oben nach unten**:
erst `> 25`, dann `< 18`, sonst `else`.

</div>

---

<!-- _class: lead -->

# Jetzt du: der große Übungsblock

---

## Was dich erwartet

<div class="box">

**Kategorie A – Einfache Bedingungen**
Festplatten-Wächter, Passwort-Prüfer, Port-Checker

**Kategorie B – mehrere Fälle mit elif**
Temperaturalarm, Ping-Bewertung, Ticket-Priorität

**Kategorie C – Kombinierte Logik**
IP-Firewall, Login mit Wartungsmodus, Multi-Faktor-Zugang

</div>

<br>

Alle Aufgaben und Lösungen findest du im **Colab-Notebook**.

---

## Ein Beispiel zum Warmwerden

```python
korrektes_passwort = "admin123"
eingabe = input("Passwort eingeben: ")

if eingabe == korrektes_passwort:
    print("Zugriff gewährt")
else:
    print("Zugriff verweigert")
```

<div class="box center">

Ein Vergleich mit `==`, verpackt in ein `if`/`else` –
genau das Grundmuster von heute.

</div>

---

<!-- _class: lead -->

# Zum Schluss

## Typischer Anfängerfehler

---

## Uneinheitliche Einrückung

```python
if speicher < 10:
    print("Wenig Speicher!")
      print("Bitte prüfen.")   # ❌ falsch eingerückt
```

<div class="box center">

❌ **IndentationError**

Alle Zeilen im selben Block müssen
**exakt gleich weit** eingerückt sein –
nicht mal 4, mal 6 Leerzeichen mischen!

</div>

---

<!-- _class: lead -->

# Was du heute gelernt hast

<div class="box">

✅ `if` / `elif` / `else` lassen dein Programm **entscheiden**

✅ Vergleichsoperatoren wie `==`, `<`, `>` liefern `True` oder `False`

✅ `and`, `or`, `not` verknüpfen mehrere Bedingungen

✅ `in` prüft, ob ein Wert in einer Liste enthalten ist

</div>

<br>

## Morgen: Fehler finden & die while-Schleife 🎉