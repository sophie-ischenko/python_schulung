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

# Tag 5
## Der große Praxis-Marathon

Eine ganze Woche Python in Bewegung

---

## Heute ist anders als sonst

<div class="box center">

Heute gibt es **keinen neuen Stoff**.

Heute geht es nur um **eine Sache**:
**Üben, üben, üben.**

</div>

---

## Warum ein ganzer Übungstag?

<div class="box">

Du hast diese Woche sehr viel gelernt:

Variablen • Texte (Strings) • Listen • erste Fehlersuche

Wissen setzt sich erst dann wirklich fest,
wenn du es **selbst oft genug angewendet** hast.

Heute ist dafür der ganze Tag reserviert.

</div>

---

## Wie der Tag abläuft

<br>

| Zeit | Was passiert |
|---|---|
| 09:00 – 09:15 | Kurzes Briefing: So läuft der Tag |
| 09:15 – 11:00 | Übungsblock 1 |
| 11:00 – 11:15 | ☕ Pause |
| 11:15 – 12:45 | Übungsblock 2 |
| 12:45 – 13:00 | Rückblick & Ausblick |

---

## Die "Practice Arena"

<div class="box center">

Du bekommst **80 Aufgaben** –
verteilt auf **4 Themenbereiche** mit je **20 Aufgaben**.

Du arbeitest **alleine oder zu zweit**,
in deinem **eigenen Tempo**.

Der Trainer ist die ganze Zeit da, um zu helfen.

</div>

---

## Zwei Wege durch die Aufgaben

<div class="box center">

**Weg 1:** Der Reihe nach, Aufgabe 1 bis 80

**Weg 2:** Nach Themen springen –
z. B. erst alle Listen-Aufgaben, dann Strings

**Beide Wege sind richtig.**
Wähle das, was sich für dich gut anfühlt.

</div>

---

## Die vier Themenbereiche

<div class="box">

1️⃣ **Grundlagen, Variablen & Mathematik** (40 Aufgaben)

2️⃣ **Texte bearbeiten (Strings)** (40 Aufgaben)

3️⃣ **Listen & Listen-Methoden** (40 Aufgaben)

4️⃣ **Fehlersuche (Debugging)** (40 Aufgaben)

</div>

---

<!-- _class: lead -->

# Kurze Erinnerung
## Was du diese Woche gelernt hast

---

## Thema 1: Variablen & Mathematik

<div class="box center">

Eine Variable ist eine **beschriftete Schublade**
für einen Wert.

```python
abteilung = "Support"
anzahl_monitore = 14
```

Und du kannst mit Zahlen rechnen:
`+` `-` `*` `/` – und auch `**` (Potenz), `%` (Rest)

</div>

---

## Ein Beispiel aus diesem Themenbereich

```python
netto = float(input("Netto: "))
print(netto * 0.19)
```

<div class="box center">

`input()` fragt den Benutzer –
`float(...)` wandelt die Eingabe in eine Dezimalzahl um.

Genau dieses Muster begegnet dir in vielen Aufgaben wieder.

</div>

---

## Thema 2: Texte bearbeiten (Strings)

<div class="box center">

Texte kannst du **zerschneiden**, **durchsuchen**
und **verändern**.

```python
print("Server"[0])          # S
print("update".upper())     # UPDATE
print("192.168.0.1".replace(".", "-"))
```

</div>

---

## Ein Beispiel aus diesem Themenbereich

```python
satz = "Das System läuft wieder"
print(len(satz.split()))
```

<div class="box center">

`.split()` zerlegt einen Satz in einzelne Wörter,
`len(...)` zählt dann, wie viele es sind.

Kleine Bausteine, die sich beliebig kombinieren lassen!

</div>

---

## Thema 3: Listen & Listen-Methoden

<div class="box center">

Eine Liste speichert **mehrere Werte** auf einmal.

```python
server = ["S1", "S2", "S3"]
server.append("S4")
server.sort()
```

Hinzufügen, entfernen, sortieren, durchsuchen –
alles schon bekannt aus den letzten Tagen.

</div>

---

## Ein Beispiel aus diesem Themenbereich

```python
daten = [1, 2, 3]
daten[0], daten[-1] = daten[-1], daten[0]
print(daten)
```

<div class="box center">

Hier tauschen wir das erste und letzte Element
in einer einzigen Zeile – ein kleiner "Aha-Trick"
mit Listen, den du in der Praxis öfter siehst.

</div>

---

## Thema 4: Fehlersuche (Debugging)

<div class="box center">

Der letzte Themenbereich ist besonders wichtig:

Bei jeder Aufgabe siehst du **fehlerhaften Code**
als Kommentar – und darunter die **Korrektur**.

Lies dir den fehlerhaften Code genau durch,
bevor du auf die Lösung schaust!

</div>

---

## Ein Beispiel aus diesem Themenbereich

```python
# Fehlerhaft:
# anzahl = input("Menge: ")   # Eingabe: 5
# print(anzahl * 2)           # Ausgabe ist 55, nicht 10!

# Korrektur:
anzahl = int(input("Menge: "))
print(anzahl * 2)
```

<div class="box center">

`input()` liefert **immer Text** zurück –
"5" mal 2 ergibt "55" (Text wird wiederholt, nicht gerechnet)!

</div>

---

## Warum ist dieser Fehlertyp so lehrreich?

<div class="box center">

Dieser Code **stürzt nicht ab**.

Er läuft einfach durch – mit einem **falschen** Ergebnis.

Das macht ihn so wertvoll zu üben:
Du lernst, auch bei "stillen" Fehlern genau hinzuschauen.

</div>

---

<!-- _class: lead -->

# Tipps für den heutigen Tag

---

## Tipp 1: Erst denken, dann tippen

<div class="box center">

Lies dir eine Aufgabe **ganz durch**,
bevor du anfängst zu schreiben.

Überlege kurz: Welche Variable brauche ich?
Welcher Datentyp passt (Text, Zahl, Liste)?

</div>

---

## Tipp 2: Fehler sind Teil des Übens

<div class="box center">

Wenn dein Code beim ersten Versuch
nicht funktioniert – **das ist völlig normal**,
gerade bei den Debugging-Aufgaben.

Lies die Fehlermeldung genau,
das ist selbst schon eine gute Übung.

</div>

---

## Tipp 3: Nutze den Trainer

<div class="box center">

Steckst du bei einer Aufgabe fest –
frag ruhig nach!

Ein Praxistag lebt davon, dass du
**dranbleibst**, nicht davon, dass du
**alles alleine** schaffst.

</div>

---

## Tipp 4: Qualität vor Menge

<div class="box center">

Es ist **kein Wettrennen**.

Lieber 40 Aufgaben wirklich verstanden
als 80 Aufgaben nur schnell abgetippt.

</div>

---

<!-- _class: lead -->

# ☕ Pause
### 11:00 – 11:15 Uhr

---

<!-- _class: lead -->

# Rückblick & Ausblick
### 12:45 – 13:00 Uhr

---

## Sichere dein Notebook!

<div class="box center">

Speichere dein Colab-Notebook am Ende des Tages –
du hast heute eine Menge eigenen Code geschrieben,
der sich gut zum Nachschlagen eignet.

</div>

---

## Was du diese Woche geschafft hast

<div class="box center">

Variablen und Datentypen<br>
⬇️<br>
Texte bearbeiten (Strings)<br>
⬇️<br>
Listen verwalten<br>
⬇️<br>
Erste Fehler selbst erkennen und beheben

</div>

---

<!-- _class: lead -->

# Ausblick auf Woche 2

## Logik, Schleifen & Funktionen

Nächste Woche bringst du deinem Code bei,
**Entscheidungen zu treffen** und
**Dinge zu wiederholen** –

der nächste große Schritt auf deinem Weg! 🎉