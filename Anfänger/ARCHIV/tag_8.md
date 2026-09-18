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

# Tag 8
## Entscheidungen treffen & Funktionen

Python-Grundlagen-Schulung

---

## Was du heute lernst



1. Wann benutze ich **if** und wann **while**?
2. Was ist eine **Funktion** – und warum brauche ich sie?
3. Was ist der Unterschied zwischen **print** und **return**?
4. Viel Übung: bekannte Aufgaben neu als Funktion schreiben

---

<!-- _class: lead -->

# Teil 1

## if oder while?

---

## Erinnerst du dich an if?

```python
if belegter_speicher > 90:
    print("Achtung, Speicher fast voll!")
```

`if` heißt: **"Wenn etwas zutrifft, dann tu das."**

Der Computer schaut sich die Bedingung **ein einziges Mal** an.

---

## Erinnerst du dich an while?

```python
while belegter_speicher > 90:
    print("Räume auf...")
```

`while` heißt: **"Solange etwas zutrifft, wiederhole das."**

Der Computer schaut sich die Bedingung **immer wieder** an – so lange, bis sie nicht mehr stimmt.

---

## Der Unterschied als Bild

<div class="center">

| 🚦 if | 🚧 while |
|:---:|:---:|
| Einmal hinschauen | Immer wieder hinschauen |
| Reagieren | Warten und immer wieder prüfen |
| Weiterfahren | Bis sich etwas ändert |

</div>

---

## Bild 1: die Ampel (if)

<div class="box center">

Du kommst zur Ampel
⬇
Du schaust **einmal** hin
⬇
Grün? → Du fährst weiter
Rot? → Du hältst an
⬇
**Fertig. Du schaust nicht nochmal hin.**

</div>

---

## Bild 2: die Bahnschranke (while)

<div class="box center">

Die Schranke ist unten
⬇
Du fragst: "Ist sie noch zu?" → Ja
⬇
Du wartest kurz
⬇
Du fragst nochmal: "Ist sie noch zu?" → Ja
⬇
... das geht so weiter, bis die Antwort **"Nein"** ist

</div>

---

## Die einfache Frage, die du dir stellst



<div class="box center">

### Passiert das nur EINMAL?
### → benutze `if`



### Muss ich das WIEDERHOLEN, bis sich etwas ändert?
### → benutze `while`

</div>

---

## Beispiel 1: Server-Speicher (einmalige Warnung)

Ich will **einmal** Bescheid geben, wenn der Speicher zu voll ist.

→ Das passiert nur einmal. **if** ist richtig.

```python
belegter_speicher = 95

if belegter_speicher > 90:
    print("WARNUNG: Speicher fast voll!")
```

---

## Beispiel 2: Server-Speicher (aufräumen)

Ich will **immer wieder** aufräumen, bis genug Platz frei ist.

→ Das wiederholt sich. **while** ist richtig.

```python
belegter_speicher = 95

while belegter_speicher > 90:
    print(f"Speicher bei {belegter_speicher}%. Räume auf...")
    belegter_speicher = belegter_speicher - 3

print("Fertig aufgeräumt!")
```

---

## Was passiert hier Schritt für Schritt?

<div class="box">

1. `belegter_speicher` ist 95 → größer als 90 → Schleife startet
2. Ausgabe: "Speicher bei 95%..." → jetzt: 95 − 3 = **92**
3. 92 ist immer noch größer als 90 → Schleife läuft nochmal
4. Ausgabe: "Speicher bei 92%..." → jetzt: 92 − 3 = **89**
5. 89 ist **nicht mehr** größer als 90 → Schleife stoppt
6. Ausgabe: "Fertig aufgeräumt!"

</div>

---

## Kurz zusammengefasst

<div class="box center">

**if** = einmal prüfen
**while** = wieder und wieder prüfen, bis Schluss ist

</div>



Jetzt übst du das an 4 kleinen Aufgaben im Colab-Notebook. 📓

---

<!-- _class: lead -->

# Teil 2

## Was ist eine Funktion?

---

## Das Problem ohne Funktionen

Stell dir vor, du willst dreimal jemanden begrüßen:

```python
print("Hallo Alex, willkommen!")
print("Hallo Sabine, willkommen!")
print("Hallo Max, willkommen!")
```

Du schreibst **fast denselben Satz** immer wieder. 😩

Was, wenn du den Satz später ändern willst? Dann musst du ihn an **jeder** Stelle ändern!

---

## Die Lösung: eine Funktion

<div class="box center">

Stell dir eine Funktion wie eine **Maschine** vor:

📥 Du wirfst etwas rein (z. B. einen Namen)
⚙️ Die Maschine macht etwas damit
📤 Es kommt etwas raus (oder wird angezeigt)

**Du baust die Maschine nur einmal.**
**Danach benutzt du sie so oft du willst.**

</div>

---

## Eine Funktion bauen

```python
def begruesse_user(username):
    print(f"Hallo {username}, willkommen!")
```

<div class="box">

- **`def`** → "ich baue jetzt eine Funktion" (def = definieren)
- **`begruesse_user`** → der Name, den ich mir ausdenke
- **`(username)`** → das, was ich reinwerfen kann
- **Einrückung** → alles, was zur Funktion gehört

</div>

⚠️ Wichtig: Nur weil ich das schreibe, passiert **noch gar nichts**!

---

## Die Funktion benutzen

```python
def begruesse_user(username):
    print(f"Hallo {username}, willkommen!")

begruesse_user("Alex")
begruesse_user("Sabine")
begruesse_user("Max")
```

<div class="box">

Erst wenn ich <code>begruesse_user("Alex")</code> schreibe,
wird die Maschine wirklich benutzt – mit "Alex" als Zutat.

</div>

---

## Bild: Die Funktion als Maschine

<div class="box center">

**"Alex"** ➡️ 🏭 `begruesse_user` 🏭 ➡️ **"Hallo Alex, willkommen!"**



**"Sabine"** ➡️ 🏭 `begruesse_user` 🏭 ➡️ **"Hallo Sabine, willkommen!"**



Gleiche Maschine – unterschiedliche Zutat – unterschiedliches Ergebnis!

</div>

---

## Warum ist das gut?

<div class="box">

✅ Ich schreibe den Text nur **einmal**

✅ Will ich den Text ändern, ändere ich ihn nur an **einer** Stelle

✅ Mein Code wird **kürzer und übersichtlicher**

</div>



Das nennt man das **DRY-Prinzip**:
**D**on't **R**epeat **Y**ourself – "Wiederhole dich nicht"

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Teil 3

## print vs. return

---

## Die wichtigste Frage heute

<div class="box center">

Will ich das Ergebnis nur **anschauen**?

→ `print`



Will ich mit dem Ergebnis später **weiterarbeiten**?

→ `return`

</div>

---

## print: nur anzeigen

```python
def addiere_print(a, b):
    print(a + b)

addiere_print(5, 5)
```

<div class="box center">

Ausgabe auf dem Bildschirm: **10**

Aber: Diese 10 ist **weg**. Ich kann nicht mehr damit rechnen.

</div>

---

## return: Ergebnis zurückgeben

```python
def addiere_return(a, b):
    return a + b

ergebnis = addiere_return(5, 5)
print(ergebnis)
```

<div class="box center">

`ergebnis` **speichert** jetzt die Zahl **10**.

Ich kann damit weiterarbeiten!

</div>

---

## Weiterarbeiten – ein Beispiel

```python
def addiere_return(a, b):
    return a + b

ergebnis = addiere_return(5, 5)
print(ergebnis * 2)    # 20
```

<div class="box">

Weil <code>ergebnis</code> die Zahl 10 gespeichert hat,
kann ich sie ganz normal weiterverwenden – z. B. mal 2 rechnen.

Mit <code>print</code> allein wäre das **nicht möglich** gewesen!

</div>

---

## Bild: print vs. return

<div class="box center">

**print** = Ich rufe dir das Ergebnis laut zu.
Danach ist es weg. 📣💨



**return** = Ich gebe dir das Ergebnis auf einem Zettel.
Du kannst ihn behalten und weiterverwenden. 📝✅

</div>

---

## Merksatz zum Einprägen



<div class="box center">

# print zeigt.
# return liefert.

</div>



💡 Falls deine Variable nach einem Funktionsaufruf leer bleibt (`None`),
hast du wahrscheinlich `return` vergessen!

---

<!-- _class: lead -->

# Teil 4

## Jetzt du: viel Übung!

---

## Was du jetzt machst

<div class="box">

Du schreibst Aufgaben, die du schon kennst, **neu als Funktion**.

Zum Beispiel:

- E-Mail-Adresse zusammenbauen
- Preis mit Mehrwertsteuer berechnen
- Temperatur bewerten (zu heiß / zu kalt / okay)
- Passwort vergleichen

</div>



Alle Aufgaben und Lösungen findest du im **Colab-Notebook**.

---

## Ein Beispiel zum Warmwerden

```python
def berechne_brutto(netto, mwst=19):
    faktor = 1 + (mwst / 100)
    return netto * faktor

print(berechne_brutto(100))      # 119.0
print(berechne_brutto(100, 7))   # 107.0
```

<div class="box">

<code>mwst=19</code> ist ein **Standardwert**.

Gebe ich keinen zweiten Wert an, wird automatisch 19 genutzt.
Gebe ich einen an (z. B. 7), wird der genutzt.

</div>

---

<!-- _class: lead -->

# Zum Schluss

## Typische Anfängerfehler

---

## Fehler 1: Einrückung vergessen

```python
def sag_hallo():
print("Hallo!")     # ❌ Fehler!
```

<div class="box center">

Der Code **innerhalb** der Funktion muss **eingerückt** sein.
Sonst weiß Python nicht, dass die Zeile zur Funktion gehört.

</div>

---

## Fehler 2: Variable "verschwindet"

```python
def berechne_quadrat(zahl):
    ergebnis = zahl * zahl
    return ergebnis

x = berechne_quadrat(4)
print(x)          # ✅ funktioniert, zeigt 16

print(ergebnis)   # ❌ Fehler! ergebnis kennt Python hier nicht
```

<div class="box center">

Eine Variable, die **in** einer Funktion entsteht,
existiert **nur dort** – nicht außerhalb.

</div>

---

<!-- _class: lead -->

# Was du heute gelernt hast

<div class="box">

✅ **if** = einmal prüfen, **while** = wiederholt prüfen

✅ Eine **Funktion** ist eine wiederverwendbare Code-Maschine

✅ **print** zeigt an, **return** liefert ein Ergebnis zum Weiterarbeiten

</div>



## Morgen geht's weiter mit: Dictionaries 🎉