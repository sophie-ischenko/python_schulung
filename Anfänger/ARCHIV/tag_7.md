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

# Tag 7
## Fehler finden & die while-Schleife

Python-Grundlagen-Schulung

---

## Was du heute lernst

<br>

1. Fehler **lesen**, **verstehen** und **reparieren** (Debugging)
2. Was ist eine **while-Schleife**?
3. Wie stoppe ich eine Schleife gezielt mit **break** und **continue**?
4. Viel Übung mit eigenen kleinen Programmen

---

<!-- _class: lead -->

# Teil 1

## Der Logik-Sanitäter

---

## Keine Angst vor Fehlermeldungen!

<div class="box center">

Eine Fehlermeldung ist **kein Weltuntergang**.

Sie ist wie ein **Wegweiser**:
Python sagt dir genau, *wo* und *warum* etwas nicht passt.

Heute übst du, diese Wegweiser lesen zu lernen.

</div>

---

## Zwei Arten von Fehlern

<div class="box">

**1. Der Absturz** 💥
Python bricht sofort ab und zeigt eine rote Fehlermeldung.
→ Leicht zu finden, weil Python selbst dich darauf hinweist.

**2. Der stille Fehler** 🤫
Das Programm läuft ganz normal durch –
liefert aber ein **falsches** Ergebnis.
→ Viel tückischer, weil nichts "rot aufblinkt"!

</div>

---

## Fehler 1: Die verschobene Einrückung

```python
if speicher_voll:
print("Warnung: Speicher voll!")
```

<div class="box center">

❌ Python meckert: **IndentationError**

Der Text nach `if:` muss **eingerückt** sein –
sonst weiß Python nicht, was zum `if` gehört.

</div>

---

## So wird es repariert

```python
speicher_voll = True

if speicher_voll:
    print("Warnung: Speicher voll!")
    print("Bitte Backup starten.")
```

<div class="box center">

✅ Beide Zeilen sind **gleich weit** eingerückt –
beide gehören zum `if`-Block.

</div>

---

## Fehler 2: Der fehlende Doppelpunkt

```python
status = "offline"

if status == "offline"
    print("Server ist offline.")
```

<div class="box center">

❌ **SyntaxError**

Nach `if ...` (und auch nach `else`) muss
immer ein **Doppelpunkt `:`** stehen.

</div>

---

## So wird es repariert

```python
status = "offline"

if status == "offline":
    print("Server ist offline.")
else:
    print("Server läuft.")
```

<div class="box center">

✅ Jetzt stehen die Doppelpunkte an der richtigen Stelle.

</div>

---

## Fehler 3: Ein Gleichheitszeichen zu wenig

```python
port = 80

if port = 80:
    print("Webserver aktiv.")
```

<div class="box center">

❌ **SyntaxError**

`=` heißt **"weise zu"** (eine Schublade befüllen)
`==` heißt **"vergleiche"** (sind zwei Dinge gleich?)

</div>

---

## So wird es repariert

```python
port = 80

if port == 80:
    print("Webserver aktiv.")
```

<div class="box center">

✅ Zum **Vergleichen** brauchst du immer **zwei** Gleichheitszeichen.

</div>

---

## Fehler 4: Der stille Logik-Fehler

**Ziel:** Zugriff erlauben, wenn der Name `"Admin"` **oder** `"Superuser"` ist.

```python
username = "Superuser"

if username == "Admin" and username == "Superuser":
    print("Zugriff erlaubt.")
else:
    print("Zugriff verweigert.")
```

<div class="box center">

⚠️ Kein Absturz – aber das Ergebnis ist **falsch**!

</div>

---

## Warum ist das falsch?

<div class="box">

`and` bedeutet: **beides gleichzeitig** muss stimmen.

Eine Variable kann aber niemals **gleichzeitig**
`"Admin"` **und** `"Superuser"` sein!

Die Bedingung ist deshalb **immer** `False`.

**Richtig wäre:** `or` – "das eine **oder** das andere"

</div>

---

## So wird es repariert

```python
username = "Superuser"

if username == "Admin" or username == "Superuser":
    print("Zugriff erlaubt.")
else:
    print("Zugriff verweigert.")
```

<div class="box center">

✅ Mit `or` reicht es, wenn **eine** der beiden Bedingungen stimmt.

</div>

---

## Fehler 5: Text und Zahl vergleichen

```python
ping = input("Ping in ms eingeben: ")

if ping < 50:
    print("Verbindung ist schnell.")
```

<div class="box center">

❌ **TypeError**

`input()` liefert **immer Text** zurück –
auch wenn der Benutzer "45" eintippt!

Text und Zahl kann Python nicht der Größe nach vergleichen.

</div>

---

## So wird es repariert

```python
ping = int(input("Ping in ms eingeben: "))

if ping < 50:
    print("Verbindung ist schnell.")
```

<div class="box center">

✅ `int(...)` wandelt den eingegebenen Text
in eine echte Zahl um.

</div>

---

## Fehler 6: Doppelt verneint

**Ziel:** Patchen, wenn der Server **nicht** gesperrt ist.

```python
gesperrt = False

if not gesperrt == False:
    print("Patch-Vorgang startet.")
```

<div class="box center">

⚠️ Auch kein Absturz – aber verwirrend und falsch!

</div>

---

## Warum ist das falsch?

<div class="box">

`gesperrt` ist `False` → `gesperrt == False` ist bereits **True**

Das zusätzliche `not` davor dreht dieses True
wieder zu **False** um.

Das ist das **Gegenteil** von dem, was gewollt war!

</div>

---

## So wird es repariert

```python
gesperrt = False

if not gesperrt:
    print("Patch-Vorgang startet.")
else:
    print("Server ist gesperrt!")
```

<div class="box center">

✅ `not gesperrt` reicht völlig aus –
keine doppelte Verneinung nötig.

</div>

---

## Deine Aufgabe jetzt

<div class="box center">

Alle 6 Fehler warten im Colab-Notebook auf dich –
teilweise auskommentiert, damit sie den Code nicht blockieren.

Lies die Fehlermeldung, überlege dir die Ursache,
und repariere den Code selbst.

</div>

---

<!-- _class: lead -->

# Teil 2

## Die while-Schleife

---

## Warum brauchen wir Schleifen?

<div class="box">

Willst du 4-mal "Ping gesendet" ausgeben,
kannst du die Zeile 4-mal abtippen.

Aber was, wenn es **400** oder **40.000** Mal sein sollen?

Oder du weißt vorher **gar nicht**, wie oft –
z. B.: "Frag so lange nach dem Passwort, bis es stimmt."

**Genau dafür gibt es Schleifen.**

</div>

---

## Bild: Der Wachmann an der Schranke

<div class="box center">

Ein Wachmann hat eine einzige Regel:

**"Solange noch Autos warten, lasse das nächste durch."**

Er prüft das **nicht nur einmal**,
sondern vor **jedem einzelnen Auto neu**.

Erst wenn keine Autos mehr da sind, hört er auf.

</div>

---

## Genau das macht while

```python
zaehler = 1

while zaehler <= 3:
    print(f"Durchlauf Nummer: {zaehler}")
    zaehler = zaehler + 1
```

<div class="box center">

Vor **jedem** Durchlauf wird neu geprüft:
"Ist die Bedingung noch wahr?"

Schauen wir uns das Schritt für Schritt an →

</div>

---

## Durchlauf 1

<div class="box center">

Ist `zaehler <= 3`? `zaehler` ist **1** → `1 <= 3` → **Ja!**

⬇️

Ausgabe: "Durchlauf Nummer: 1"

⬇️

`zaehler` wird um 1 erhöht → jetzt **2**

</div>

---

## Durchlauf 2

<div class="box center">

Ist `zaehler <= 3`? `zaehler` ist **2** → `2 <= 3` → **Ja!**

⬇️

Ausgabe: "Durchlauf Nummer: 2"

⬇️

`zaehler` wird um 1 erhöht → jetzt **3**

</div>

---

## Durchlauf 3

<div class="box center">

Ist `zaehler <= 3`? `zaehler` ist **3** → `3 <= 3` → **Ja!**

⬇️

Ausgabe: "Durchlauf Nummer: 3"

⬇️

`zaehler` wird um 1 erhöht → jetzt **4**

</div>

---

## Die Prüfung, die alles beendet

<div class="box center">

Ist `zaehler <= 3`? `zaehler` ist **4** → `4 <= 3` → **Nein!**

⬇️

**Die Schleife stoppt.**

Das Programm läuft direkt nach der Schleife weiter.

</div>

---

## Der wichtigste Satz zur while-Schleife

<br>

<div class="box center">

# Ohne `zaehler = zaehler + 1`
# würde die Schleife NIE aufhören!

</div>

<br>

Diese Zeile ist **kein Extra** – sie ist der Grund,
warum die Schleife irgendwann endet.

---

## ⚡ Achtung: Die Endlosschleife

<div class="box center">

Wenn die Bedingung **niemals** `False` wird,
läuft die Schleife **für immer**.

```python
while True:
    print("Ich laufe für immer!")
```

</div>

---

## Keine Panik!

<div class="box">

Passiert dir das aus Versehen in Colab:

👉 Klick einfach auf den **Stop-Button**
("Interrupt execution") neben der Zelle.

Das ist **kein Schaden** am System –
nur eine Berechnung, die du stoppen musst.

</div>

---

## Ist while True: immer ein Fehler?

<div class="box center">

**Nein!** `while True:` ist ein bewusst genutztes,
sehr gebräuchliches Muster.

Man nutzt es genau dann, wenn man die Schleife
**von innen heraus** beenden möchte.

Wie das geht, lernst du jetzt: mit **break**!

</div>

---

<!-- _class: lead -->

# Teil 3

## break und continue

---

## break: der Notausschalter

<div class="box center">

`break` beendet die Schleife **sofort und komplett** –
egal was die Bedingung am Kopf sagt.

Das Programm springt direkt zum Code **nach** der Schleife.

</div>

---

## Beispiel: das unendliche Login

```python
while True:
    eingabe = input("Passwort eingeben: ")
    if eingabe == "admin123":
        print("Schleife wird beendet.")
        break
    print("Falsches Passwort!")
```

<div class="box">

`while True` heißt: "wiederhole für immer".

Aber die `if`-Bedingung **innerhalb** entscheidet,
wann `break` ausgelöst wird – und **dann** ist Schluss.

</div>

---

## continue: der sanfte Sprung

<div class="box center">

`continue` beendet **nicht** die ganze Schleife –

nur den **aktuellen Durchlauf** wird abgebrochen,
die Schleife läuft danach ganz normal weiter.

</div>

---

## Bild: Lied überspringen

<div class="box center">

`break` = die **ganze Playlist** stoppen 🛑

`continue` = nur **diesen einen Song** überspringen,
die Playlist läuft weiter ⏭️

</div>

---

## Beispiel: eine Zahl überspringen

```python
zahl = 0
while zahl < 5:
    zahl = zahl + 1
    if zahl == 3:
        continue
    print(f"Zahl: {zahl}")
```

<div class="box center">

Ausgabe: `1, 2, 4, 5`

Die **3** fehlt – bei ihr wurde `continue` ausgelöst,
und das `print` für diesen Durchlauf übersprungen.

</div>

---

## Merkregel

<br>

<div class="box center">

# break = Schleife komplett verlassen

# continue = diesen Durchlauf überspringen,
# aber weitermachen

</div>

---

<!-- _class: lead -->

# ☕ Kurze Pause

---

<!-- _class: lead -->

# Teil 4

## Jetzt du: der große Übungsblock

---

## Was dich erwartet

<div class="box">

**Kategorie A – Einfache Schleifen**
Countdown, Fortschrittsbalken, Ping-Zähler

**Kategorie B – mit break und continue**
Login-Versuche, Ports überspringen, Chatbot

**Kategorie C – Komplexere Aufgaben**
Temperatur-Simulator, kleiner Task-Manager

</div>

<br>

Alle Aufgaben und Lösungen findest du im **Colab-Notebook**.

---

## Ein Beispiel zum Warmwerden

```python
counter = 5
while counter > 0:
    print(counter)
    counter = counter - 1

print("Patchvorgang startet...")
```

<div class="box center">

Ein einfacher Countdown – genau das Prinzip,
das du gerade Schritt für Schritt kennengelernt hast.

</div>

---

<!-- _class: lead -->

# Was du heute gelernt hast

<div class="box">

✅ Fehlermeldungen sind **Hinweise**, keine Katastrophen

✅ `while` prüft die Bedingung **vor jedem** Durchlauf neu

✅ `break` verlässt die Schleife komplett, `continue` überspringt nur einen Durchlauf

✅ Eine Endlosschleife ist mit dem Stop-Button jederzeit sicher zu stoppen

</div>

<br>

## Morgen: Entscheidungen & Funktionen 🎉