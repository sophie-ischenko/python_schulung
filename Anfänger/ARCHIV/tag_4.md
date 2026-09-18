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

# Tag 4
## Die Coding-Arena & Einstieg in Listen

Python-Grundlagen-Schulung

---

## Was du heute lernst

<br>

1. Eine Stunde intensives **Üben** von allem bisher Gelernten
2. Was ist eine **Liste** – und warum brauche ich sie?
3. Wie **greife ich auf einzelne Werte** in einer Liste zu?
4. Wie **verändere** ich eine Liste – hinzufügen, entfernen, sortieren

---

<!-- _class: lead -->

# Teil 1

## Die Warm-up-Coding-Arena

---

## Eine intensive Übungsstunde

<div class="box center">

Bevor es neuen Stoff gibt, festigst du erst einmal
**alles, was du in den letzten drei Tagen** gelernt hast:

Variablen • `input()` • Rechnen • Texte (Strings) • Fehlersuche

</div>

---

## Ein Beispiel aus dem Warm-up

```python
leitung_mbit = float(input("Bandbreite pro Leitung (Mbit/s): "))
anzahl = int(input("Anzahl der Leitungen: "))
gesamt = leitung_mbit * anzahl
print(f"Gesamtbandbreite: {gesamt} Mbit/s")
```

<div class="box center">

Nichts Neues hier – nur **input, Umwandlung und Rechnen**,
alles schon bekannt aus den letzten Tagen.

</div>

---

## Auch dabei: kleine Fehlersuchen

```python
# Fehlerhaft (User gibt 1.5 ein → Absturz):
# datenmenge_gb = int(input("Wie viel GB? "))

# Richtig:
datenmenge_gb = float(input("Wie viel GB? "))
```

<div class="box center">

`int()` kann keine Dezimalzahl wie `1.5` verarbeiten.
`float()` schon!

</div>

---

## 10 Aufgaben warten auf dich

<div class="box">

Von Bandbreiten-Rechnern über String-Slicing
bis zu kleinen Fehlersuchen –

**alles im Colab-Notebook.**

</div>

<br>

Danach geht es mit einem großen neuen Thema weiter: **Listen**!

---

<!-- _class: lead -->

# Teil 2

## Was ist eine Liste?

---

## Das Problem: viele einzelne Variablen

```python
hostname1 = "SRV-01"
hostname2 = "SRV-02"
hostname3 = "SRV-03"
```

<div class="box center">

Das geht bei 3 Servern noch.

Aber was, wenn du **50, 500 oder 5000** Server
verwalten musst? 😩

</div>

---

## Die Lösung: eine Liste

```python
server_liste = ["SRV-01", "SRV-02", "SRV-03"]
```

<div class="box center">

**Ein Name** – aber beliebig viele Werte darin!

Eckige Klammern `[ ]` markieren Anfang und Ende,
Kommas trennen die einzelnen Werte.

</div>

---

## Bild: Der Aktenschrank

<div class="box center">

Stell dir einen **Aktenschrank mit nummerierten
Schubladen** vor.

Statt für jedes Dokument einen eigenen Tisch (= eine
eigene Variable) zu haben, packst du alles in **einen
Schrank**.

Jede Schublade hat eine Nummer –
du kannst gezielt eine öffnen, ohne die anderen anzufassen.

</div>

---

## Warum ist das in der IT so wichtig?

<div class="box">

Eine Liste aller aktiven Benutzer.
Eine Liste aller offenen Tickets.
Eine Liste aller IP-Adressen im Netzwerk.

Fast **jedes echte Programm** muss irgendwann
mehrere Dinge gleichzeitig verwalten.

</div>

---

<!-- _class: lead -->

# Auf eine Schublade zugreifen

## Der Index

---

## Jedes Element hat eine Nummer

<div class="box center">

```
Liste:    "192.168.1.1"   "192.168.1.2"   "192.168.1.3"
Index:          0               1               2
```

⚠️ Ganz wichtig: Python zählt **bei 0**, nicht bei 1!

Das **erste** Element hat den Index **0**.

</div>

---

## Zugriff auf ein Element

```python
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

print(ips[0])   # Erstes Element
print(ips[-1])  # Letztes Element
print(len(ips)) # Wie viele Elemente sind drin?
```

<div class="box center">

`-1` heißt "von hinten gezählt, das erste" –
egal wie lang die Liste ist!

`len(...)` zählt dir die Elemente.

</div>

---

<!-- _class: lead -->

# Eine Liste verändern

## Der große Unterschied zu Strings

---

## Erinnerung: Strings kann man nicht ändern

<div class="box center">

Bei einem String konntest du **kein einzelnes
Zeichen** nachträglich austauschen.

Du musstest immer einen **komplett neuen** String bauen
(z. B. mit `.replace()`).

</div>

---

## Listen sind anders: sie sind veränderbar!

```python
hardware = ["Maus", "Tastatur", "Monitor"]
hardware[1] = "Headset"
print(hardware)
```

<div class="box center">

`['Maus', 'Headset', 'Monitor']`

Du kannst **direkt** ein Element austauschen –
wie den Inhalt einer Schublade wechseln,
ohne den ganzen Schrank neu zu bauen.

</div>

---

## Merksatz

<br>

<div class="box center">

# Strings: unveränderbar
# Listen: veränderbar

</div>

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Teil 3

## Listen wachsen & schrumpfen lassen

---

## Element hinzufügen: .append()

```python
tools = ["Ping", "Nslookup"]
tools.append("Tracert")
print(tools)  # ['Ping', 'Nslookup', 'Tracert']
```

<div class="box center">

`.append(...)` hängt einen Wert **ganz hinten** an.

Die häufigste Listen-Methode überhaupt!

</div>

---

## Element gezielt einfügen: .insert()

```python
tools.insert(1, "Nmap")
print(tools)  # ['Ping', 'Nmap', 'Nslookup', 'Tracert']
```

<div class="box center">

`.insert(position, wert)` schiebt einen Wert
an eine **bestimmte Stelle** – alles danach rutscht weiter.

</div>

---

## Bild: die Warteschlange am Schalter

<div class="box center">

`.append(...)` = ein neuer Kunde stellt sich **hinten** an

`.insert(0, ...)` = ein dringender Fall wird
**ganz vorne** reingelassen – alle anderen rücken auf

</div>

---

## Element entfernen (nach Wert): .remove()

```python
tools = ["Ping", "Nmap", "Nslookup"]
tools.remove("Ping")
print(tools)  # ['Nmap', 'Nslookup']
```

<div class="box center">

`.remove(wert)` sucht diesen **Wert** in der Liste
und löscht ihn.

⚠️ Ist der Wert nicht enthalten → Fehler (`ValueError`)!

</div>

---

## Element entfernen (nach Position): .pop()

```python
tools = ["Nmap", "Nslookup"]
entfernt = tools.pop(0)
print("Entfernt:", entfernt)
print("Verbleibend:", tools)
```

<div class="box center">

`.pop(position)` entfernt das Element an dieser Stelle
**und gibt es dir gleich zurück** – zum Weiterverwenden!

</div>

---

## Merkregel: remove vs. pop

<br>

<div class="box center">

**`.remove()`** → "Ich weiß, **was** weg soll"
(ich kenne den Wert, nicht die Position)

**`.pop()`** → "Ich weiß, **wo** es steht"
(und ich will den Wert noch weiterverwenden)

</div>

---

<!-- _class: lead -->

# Teil 4

## Jetzt du: der große Listen-Praxis-Slam

---

## Was dich erwartet

<div class="box">

**Teil A – IT-Inventar & Daten sammeln**
Server-Fuhrpark, IP-Erfassung, Gruppen-Bereinigung, Backups korrigieren

**Teil B – ToDo-Listen & Warteschlangen**
Tagesplanung, Ticket-Warteschlange, sortierte Lieferung, Deinstallation

</div>

<br>

Alle Aufgaben und Lösungen findest du im **Colab-Notebook**.

---

## Ein Beispiel zum Warmwerden

```python
admins = ["claudia", "stefan", "andreas", "markus"]
admins.append("julia")
admins.remove("stefan")
print(admins)
```

<div class="box center">

Eine ganz normale Kombination aus
`.append()` und `.remove()` – genau das übst du jetzt selbst!

</div>

---

<!-- _class: lead -->

# Zum Schluss

## Ein typischer Fehler

---

## IndexError: list index out of range

```python
liste = ["A", "B", "C"]
print(liste[10])
```

<div class="box center">

❌ Diese Liste hat nur **3** Elemente (Index 0, 1, 2) –
Index `10` gibt es gar nicht!

Bei diesem Fehler: einfach nochmal mit `len(...)` prüfen,
wie groß die Liste wirklich ist.

</div>

---

<!-- _class: lead -->

# Was du heute gelernt hast

<div class="box">

✅ Eine **Liste** speichert mehrere Werte unter einem Namen

✅ Zugriff über den **Index**, beginnend bei **0**

✅ Listen sind **veränderbar** – anders als Strings

✅ `.append()`, `.insert()`, `.remove()`, `.pop()` verändern die Liste

</div>

<br>

## Morgen: der große Praxis-Marathon 🎉