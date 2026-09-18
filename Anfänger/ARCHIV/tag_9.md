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

# Tag 9
## Funktionen rufen Funktionen & das main()-Muster

Python-Grundlagen-Schulung

---

## Was du heute lernst

<br>

1. Wie genau **wandert ein Wert** in eine Funktion hinein und wieder heraus?
2. Wie kann eine Funktion **eine andere Funktion** benutzen?
3. Was ist `main()` – und warum schreibt man das fast immer?
4. Viel Übung: eigene kleine Programme bauen

---

<!-- _class: lead -->

# Teil 1

## Wie ein Wert durch die Funktion reist

---

## Erinnerung an Tag 8

<div class="box center">

Eine Funktion ist eine **Maschine**:

📥 etwas rein → ⚙️ Verarbeitung → 📤 etwas raus

</div>

<br>

Heute schauen wir uns **ganz genau** an, was dabei im Inneren passiert.

---

## Ein Beispiel

```python
def berechne_wert(zahl):
    return zahl * 2

ergebnis = berechne_wert(10)
```

<div class="box">

Was passiert hier eigentlich Schritt für Schritt?
Schauen wir es uns wie einen Comic an →

</div>

---

## Schritt 1: Der Aufruf

<div class="box center">

```
ergebnis = berechne_wert(10)
```

Python sagt: "Ich soll `berechne_wert` mit der Zahl **10** aufrufen."

⬇️ Python springt jetzt zur Funktion

</div>

---

## Schritt 2: In der Funktion ankommen

<div class="box center">

```
def berechne_wert(zahl):
```

Die **10** wird jetzt der Variable `zahl` gegeben.

`zahl` ist wie eine **Schublade**, in die kurz die 10 reingelegt wird.

</div>

---

## Schritt 3: Rechnen

<div class="box center">

```
return zahl * 2
```

Python rechnet: `10 * 2` = **20**

Und schickt die **20 zurück** dorthin, wo die Funktion aufgerufen wurde.

</div>

---

## Schritt 4: Zurück im Hauptprogramm

<div class="box center">

```
ergebnis = berechne_wert(10)
```

Jetzt wird aus dieser Zeile:

```
ergebnis = 20
```

**`ergebnis` speichert jetzt die 20.**

</div>

---

## Der ganze Weg auf einen Blick

<div class="box center">

**10** wird übergeben<br>
⬇️<br>
kommt in der Funktion als `zahl` an<br>
⬇️<br>
wird zu **20** verarbeitet<br>
⬇️<br>
kommt als **20** zurück<br>
⬇️<br>
landet in `ergebnis`

</div>

---

## Ein wichtiger Trick

```python
mein_wert = 10
ergebnis = berechne_wert(mein_wert)
```

<div class="box">

Der Name `mein_wert` draußen und der Name `zahl` drinnen
**müssen nicht gleich heißen!**

Python interessiert sich nur für den **Wert** (die 10),
nicht für den Namen der Variable.

</div>

---

## Warum ist das nützlich?

<div class="box center">

Du kannst dieselbe Funktion mit **ganz unterschiedlichen**
Variablen oder Zahlen füttern.

Die Funktion selbst muss sich dafür **nie ändern**.

</div>

<br>

Jetzt übst du das an 3 kleinen Aufgaben im Colab-Notebook. 📓

---

<!-- _class: lead -->

# Teil 2

## Funktionen rufen Funktionen

---

## Das Problem: eine riesige Funktion

<div class="box">

Stell dir vor, eine Funktion soll **alles auf einmal** können:

Steuer berechnen, Rabatt berechnen, alles zusammenzählen...

Das wird schnell **unübersichtlich** und **schwer zu finden**,
wenn mal ein Fehler drin ist.

</div>

---

## Die Lösung: aufteilen!

<div class="box center">

Statt **einer riesigen** Maschine baust du
**mehrere kleine, spezialisierte** Maschinen.

Eine große Maschine kann dann die kleinen Maschinen benutzen!

</div>

---

## Bild: der Vorarbeiter

<div class="box center">

Ein **Vorarbeiter** macht nicht alles selbst.

Er sagt: "Du machst die Steuer, du machst den Rabatt" –
und setzt am Ende alles zusammen.

**Das nennt man Modularisierung.**

</div>

---

## Zwei kleine, einfache Funktionen

```python
def ermittle_steuer(netto_betrag):
    return netto_betrag * 0.19

def ermittle_rabatt(netto_betrag):
    if netto_betrag > 1000:
        return netto_betrag * 0.10
    return 0.0
```

<div class="box center">

Jede Funktion kann **genau eine** Sache. Nicht mehr.

</div>

---

## Eine Funktion, die die anderen benutzt

```python
def kalkuliere_gesamtpreis(netto_betrag):
    steuer = ermittle_steuer(netto_betrag)
    rabatt = ermittle_rabatt(netto_betrag)

    return netto_betrag + steuer - rabatt
```

<div class="box center">

`kalkuliere_gesamtpreis` **ruft** die beiden anderen Funktionen auf –
so, wie du im Hauptprogramm auch eine Funktion aufrufst!

</div>

---

## Schritt für Schritt: kalkuliere_gesamtpreis(1200)

<div class="box">

1. `ermittle_steuer(1200)` wird aufgerufen → liefert **228.0** zurück
2. Das landet in der Variable `steuer`
3. `ermittle_rabatt(1200)` wird aufgerufen → liefert **120.0** zurück (weil 1200 > 1000)
4. Das landet in der Variable `rabatt`
5. Am Ende: `1200 + 228.0 - 120.0` = **1308.0**

</div>

---

## Warum ist das so gut?

<div class="box">

✅ Jede kleine Funktion kannst du **einzeln testen**

✅ Der Name verrät sofort, **was** die Funktion tut

✅ Eine kleine Funktion kannst du **später woanders wiederverwenden**

</div>

---

## Merksatz

<br>

<div class="box center">

# Eine Funktion darf ruhig
# eine andere Funktion benutzen!

</div>

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Teil 3

## Die main()-Funktion

---

## Ein neues Problem

<div class="box">

Bisher haben wir Variablen einfach frei
im Notebook stehen lassen.

Bei kleinen Übungen kein Problem.
Aber bei **größeren Programmen** wird das schnell unübersichtlich –
man weiß nicht mehr, was wo herkommt.

</div>

---

## Die Lösung: eine Haupt-Schublade

<div class="box center">

Wir packen **den gesamten Ablauf** unseres Programms
in **eine einzige Funktion**.

Diese Funktion nennen wir immer **`main`**
(englisch für "Haupt-").

</div>

---

## So sieht das aus

```python
def main():
    print("Das Hauptprogramm läuft...")

if __name__ == "__main__":
    main()
```

<div class="box center">

Das ist der **Standard**, den du in fast jedem
"richtigen" Python-Programm findest.

</div>

---

## Die main-Funktion

```python
def main():
    print("Das Hauptprogramm läuft...")
```

<div class="box center">

Hier steht **alles**, was dein Programm eigentlich tun soll:
Fragen stellen, andere Funktionen aufrufen, Ergebnisse zeigen.

</div>

---

## Die geheimnisvolle letzte Zeile

```python
if __name__ == "__main__":
    main()
```

<div class="box">

Vereinfacht gesagt bedeutet das:

**"Wenn diese Datei direkt gestartet wird, dann starte main()."**

Für dich als Anfänger reicht es, diese zwei Zeilen
**immer genau so** ans Ende zu schreiben.

</div>

---

## Merksatz

<br>

<div class="box center">

`main()` bündelt den Ablauf.

`if __name__ == "__main__":` startet ihn.

Schreib diese zwei Zeilen **immer** am Ende deines Programms.

</div>

---

<!-- _class: lead -->

# Teil 4

## Jetzt du: modulare Programme bauen

---

## Was du jetzt machst

<div class="box">

Du baust drei kleine Programm-Systeme.
Jedes besteht aus:

1. Ein oder zwei **kleinen Hilfsfunktionen**
2. Einer **`main()`**-Funktion, die die Hilfsfunktionen benutzt
3. Der Abschluss-Zeile `if __name__ == "__main__": main()`

</div>

---

## Die drei Programme

<div class="box">

🌡️ **Server-Raum-Monitor**
Temperatur bewerten und Alarm-Text erzeugen

📧 **Onboarding-Assistent**
E-Mail und Benutzername für neue Mitarbeiter erzeugen

📶 **Ping-Latenz-Tester**
Mit einer `while`-Schleife immer wieder Latenz abfragen

</div>

<br>

Alle Aufgaben und Lösungen findest du im **Colab-Notebook**.

---

## Ein Beispiel zum Warmwerden

```python
def bewerte_temperatur(temp):
    if temp > 30:
        return "kritisch"
    return "normal"

def main():
    temp = float(input("Temperatur in °C: "))
    status = bewerte_temperatur(temp)
    print(status)

if __name__ == "__main__":
    main()
```

---

<!-- _class: lead -->

# Zum Schluss

## Warum das Ganze?

---

## Ein Vergleich

<div class="box">

**Ohne Struktur:** Ein Fehler? Du musst das ganze Programm
von oben bis unten durchsuchen. 😩

**Mit kleinen Funktionen + main():**
Ein Fehler in der E-Mail-Erzeugung?
Du schaust **nur** in `generiere_email` nach. 🎯

</div>

---

<!-- _class: lead -->

# Was du heute gelernt hast

<div class="box">

✅ Ein Wert reist von der Aufrufstelle in die Funktion – und mit `return` wieder zurück

✅ Eine Funktion darf **andere Funktionen** benutzen (Modularisierung)

✅ `main()` bündelt den Ablauf deines Programms an einer Stelle

</div>

<br>

## Morgen: der große Projekttag – dein eigenes Spiel! 🎉