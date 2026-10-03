# Python GUI mit Tkinter

**Tag 4**

Bisher haben wir Python-Programme hauptsächlich über das Terminal ausgeführt.

Heute bauen wir zum ersten Mal eine grafische Oberfläche.

Dafür verwenden wir **Tkinter**. Tkinter gehört zur Python-Standardbibliothek und ermöglicht es, Fenster, Texte, Buttons, Eingabefelder, Bilder und weitere grafische Elemente zu erstellen.

Am Ende des Tages kannst du:

- ein Tkinter-Fenster erstellen
- Widgets wie `Label`, `Button`, `Entry` und `Canvas` verwenden
- Widgets mit `grid()` anordnen
- Eigenschaften von Widgets verändern
- Funktionen mit Buttons verbinden
- Eingaben aus `Entry` auslesen
- Bilder mit `PhotoImage` laden
- einen Countdown mit `after()` erstellen
- einen geplanten Timer mit `after_cancel()` abbrechen
- zusätzliche Fenster mit `Toplevel` öffnen
- JSON-Daten laden und in einer GUI darstellen
- Widgets mit einer `for`-Schleife dynamisch erzeugen

---

# 1. Was ist Tkinter?

Tkinter ist eine Python-Bibliothek für grafische Benutzeroberflächen.

Eine grafische Benutzeroberfläche wird häufig mit **GUI** abgekürzt.

GUI steht für:

> Graphical User Interface

Statt nur Text im Terminal auszugeben, können wir beispielsweise so etwas bauen:

```text
┌───────────────────────────────┐
│          Meine App            │
│                               │
│          00:25:00             │
│                               │
│      [ Start ]  [ Reset ]     │
│                               │
└───────────────────────────────┘
```

Tkinter stellt dafür verschiedene Elemente bereit.

Diese Elemente nennt man **Widgets**.

Typische Widgets sind:

- `Label` für Text
- `Button` für Schaltflächen
- `Entry` für Texteingaben
- `Canvas` für Zeichnungen und Bilder
- `Toplevel` für zusätzliche Fenster

---

# 2. Tkinter importieren

Tkinter gehört zur Python-Standardbibliothek.

Wir müssen es deshalb normalerweise nicht zusätzlich installieren.

Für diesen Kurs verwenden wir:

```python
import tkinter as tk
```

Dadurch können wir beispielsweise schreiben:

```python
fenster = tk.Tk()
```

oder:

```python
button = tk.Button(...)
```

Das `tk.` macht deutlich, dass das Element aus Tkinter kommt.

---

# 3. Das Hauptfenster erstellen

Jede Tkinter-Anwendung benötigt ein Hauptfenster.

Dieses erstellen wir mit:

```python
import tkinter as tk

fenster = tk.Tk()
```

`tk.Tk()` erstellt das Hauptfenster der Anwendung.

Damit das Fenster geöffnet bleibt und auf Benutzeraktionen reagiert, brauchen wir anschließend:

```python
fenster.mainloop()
```

Ein vollständiges Minimalprogramm sieht so aus:

```python
import tkinter as tk

fenster = tk.Tk()

fenster.mainloop()
```

`mainloop()` startet die Ereignisschleife.

Das Programm wartet danach beispielsweise auf:

- Mausklicks
- Tastatureingaben
- Timer
- Fensteraktionen

Ohne `mainloop()` würde das Programm direkt wieder beendet werden.

---

# 4. Das Fenster konfigurieren

Das Fenster kann verschiedene Eigenschaften bekommen.

## Fenstertitel

Mit `title()` setzen wir den Titel:

```python
fenster.title("Meine App")
```

## Hintergrundfarbe

Mit `config()` können wir Eigenschaften verändern:

```python
fenster.config(bg="lightblue")
```

## Innenabstände

Mit `padx` und `pady` können wir Abstand innerhalb des Fensters festlegen:

```python
fenster.config(
    padx=20,
    pady=20
)
```

Mehrere Eigenschaften können gleichzeitig gesetzt werden:

```python
fenster.config(
    bg="lightblue",
    padx=20,
    pady=20
)
```

---

# 5. Widgets

Die einzelnen Elemente einer Tkinter-Oberfläche heißen Widgets.

Ein Widget wird normalerweise erstellt und anschließend im Fenster positioniert.

Beispiel:

```python
label = tk.Label(
    fenster,
    text="Hallo!"
)
```

Hier passiert zunächst nur eines:

Das Label wird erstellt.

Damit es tatsächlich sichtbar wird, müssen wir es noch im Fenster platzieren.

Dafür verwenden wir beispielsweise `grid()`.

```python
label.grid(
    row=0,
    column=0
)
```

---

# 6. Label

Ein `Label` zeigt Informationen an.

Zum Beispiel:

```python
label = tk.Label(
    fenster,
    text="Hallo!"
)

label.grid(
    row=0,
    column=0
)
```

Das Label kann gestaltet werden.

```python
label = tk.Label(
    fenster,
    text="Hallo!",
    font=("Arial", 30),
    fg="red",
    bg="white"
)
```

Wichtige Eigenschaften:

- `text` bestimmt den Text
- `font` bestimmt die Schrift
- `fg` bestimmt die Textfarbe
- `bg` bestimmt die Hintergrundfarbe

---

# 7. Schriftarten

Eine Schrift kann als Tupel angegeben werden:

```python
font=("Arial", 30)
```

Die Bestandteile sind:

```text
("Schriftart", Größe)
```

Eine fette Schrift kann so angegeben werden:

```python
font=("Arial", 30, "bold")
```

Zum Beispiel:

```python
label = tk.Label(
    fenster,
    text="Pomodoro",
    font=("Courier", 40, "bold")
)
```

---

# 8. Button

Ein `Button` ist eine Schaltfläche.

```python
button = tk.Button(
    fenster,
    text="Start"
)

button.grid(
    row=1,
    column=0
)
```

Auch Buttons können gestaltet werden:

```python
button = tk.Button(
    fenster,
    text="Start",
    font=("Arial", 18),
    fg="red",
    bg="white"
)
```

---

# 9. Funktionen mit Buttons verbinden

Ein Button soll normalerweise eine Aktion auslösen.

Dafür schreiben wir zunächst eine Funktion:

```python
def hallo():
    print("Hallo!")
```

Diese Funktion können wir mit `command` an den Button binden:

```python
button = tk.Button(
    fenster,
    text="Klick mich",
    command=hallo
)
```

Wichtig:

Hier steht:

```python
command=hallo
```

und nicht:

```python
command=hallo()
```

Bei:

```python
command=hallo
```

geben wir die Funktion an Tkinter weiter.

Tkinter ruft die Funktion später auf, wenn der Button geklickt wird.

---

# 10. Widgets verändern

Widgets können nach ihrer Erstellung verändert werden.

Dafür verwenden wir meistens `.config()`.

Zum Beispiel:

```python
label.config(
    text="Neuer Text"
)
```

Auch Farben können geändert werden:

```python
label.config(
    text="Fertig!",
    fg="green"
)
```

Das ist für dynamische Anwendungen wichtig.

Ein Timer kann beispielsweise jede Sekunde seinen Text verändern.

---

# 11. Widgets mit `grid()` anordnen

Tkinter besitzt verschiedene Möglichkeiten, Widgets anzuordnen.

In diesem Kurs verwenden wir hauptsächlich:

```python
grid()
```

`grid()` arbeitet mit Zeilen und Spalten.

```python
label.grid(
    row=0,
    column=0
)
```

Zeilen und Spalten beginnen bei `0`.

Mehrere Widgets können beispielsweise so angeordnet werden:

```python
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
```

Das ergibt ungefähr:

```text
┌─────────┬─────────┬─────────┐
│ Button1 │ Button2 │ Button3 │
└─────────┴─────────┴─────────┘
```

---

# 12. Abstände mit `padx` und `pady`

Mit `padx` und `pady` können wir Abstand um ein Widget herum erzeugen.

```python
button.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)
```

`padx` bedeutet horizontaler Abstand.

`pady` bedeutet vertikaler Abstand.

---

# 13. Mehrere Spalten verwenden

Widgets können über mehrere Spalten reichen.

Dafür gibt es `columnspan`.

```python
titel.grid(
    row=0,
    column=0,
    columnspan=3
)
```

Das bedeutet:

Das Widget beginnt bei Spalte `0` und reicht über drei Spalten.

Das ist beispielsweise für einen Titel über mehreren Buttons praktisch.

---

# 14. Entry

Mit `Entry` kann der Benutzer Text eingeben.

```python
eingabe = tk.Entry(
    fenster
)

eingabe.grid(
    row=0,
    column=0
)
```

Den eingegebenen Text können wir mit `.get()` auslesen:

```python
text = eingabe.get()
```

Beispiel:

```python
def anzeigen():
    text = eingabe.get()
    label.config(text=text)
```

Ein Eingabefeld kann mit `.delete()` geleert werden:

```python
eingabe.delete(
    0,
    tk.END
)
```

`0` bedeutet dabei den Anfang des Textes.

`tk.END` bedeutet das Ende des Textes.

---

# 15. Canvas

Ein `Canvas` ist eine Zeichenfläche.

Auf einem Canvas können wir unter anderem:

- Text
- Bilder
- Linien
- Formen

anzeigen.

Ein Canvas wird beispielsweise so erstellt:

```python
canvas = tk.Canvas(
    fenster,
    width=300,
    height=200
)

canvas.grid(
    row=0,
    column=0
)
```

Die Größe wird in Pixeln angegeben.

---

# 16. Text auf einem Canvas anzeigen

Mit `create_text()` können wir Text auf einem Canvas anzeigen.

```python
timer_text = canvas.create_text(
    150,
    100,
    text="00:00",
    font=("Arial", 30),
    fill="white"
)
```

Die ersten beiden Werte bestimmen die Position:

```python
150, 100
```

Das sind die X- und Y-Koordinaten.

Ein Canvas beginnt ungefähr hier:

```text
(0, 0)
   ┌─────────────────────────→ x
   │
   │
   │
   ↓
   y
```

---

# 17. Canvas-Elemente später verändern

`create_text()` liefert eine ID zurück.

Diese können wir speichern:

```python
timer_text = canvas.create_text(
    150,
    100,
    text="00:00"
)
```

Später können wir genau dieses Element verändern:

```python
canvas.itemconfig(
    timer_text,
    text="24:59"
)
```

Dadurch wird die Anzeige aktualisiert.

Das ist für einen Countdown besonders praktisch.

---

# 18. Bilder mit `PhotoImage`

Tkinter kann Bilder mit `PhotoImage` laden.

```python
bild = tk.PhotoImage(
    file="bilder/tomato.png"
)
```

Das Bild können wir anschließend beispielsweise auf einem Canvas anzeigen:

```python
canvas.create_image(
    100,
    100,
    image=bild
)
```

Ein vollständiges Beispiel:

```python
canvas = tk.Canvas(
    fenster,
    width=200,
    height=200
)

canvas.grid(
    row=0,
    column=0
)

bild = tk.PhotoImage(
    file="bilder/tomato.png"
)

canvas.create_image(
    100,
    100,
    image=bild
)
```

---

# 19. Wichtig bei Bildern

Das Bild sollte in einer Variable gespeichert werden:

```python
bild = tk.PhotoImage(
    file="bilder/tomato.png"
)
```

Nicht nur:

```python
tk.PhotoImage(
    file="bilder/tomato.png"
)
```

Die Variable sorgt dafür, dass das Bild während der Laufzeit erhalten bleibt.

Eine mögliche Projektstruktur ist:

```text
tag4/
├── projekt.py
└── bilder/
    └── tomato.png
```

Der Dateiname kann natürlich geändert werden.

---

# 20. Zeitverzögerungen mit `after()`

Tkinter besitzt die Methode:

```python
after()
```

Damit können wir eine Funktion nach einer bestimmten Zeit ausführen.

Beispiel:

```python
def hallo():
    label.config(
        text="Hallo!"
    )

fenster.after(
    2000,
    hallo
)
```

Die Zeit wird in Millisekunden angegeben.

```text
1000 Millisekunden = 1 Sekunde
2000 Millisekunden = 2 Sekunden
```

Nach zwei Sekunden wird `hallo()` aufgerufen.

---

# 21. `after()` für einen Timer verwenden

Wir können eine Funktion nach einer Sekunde erneut aufrufen.

```python
def zaehlen():
    print("Tick")

    fenster.after(
        1000,
        zaehlen
    )
```

Wenn wir einmal starten:

```python
zaehlen()
```

passiert ungefähr:

```text
zaehlen()
    ↓
1 Sekunde warten
    ↓
zaehlen()
    ↓
1 Sekunde warten
    ↓
zaehlen()
    ↓
...
```

Damit können wir einen Countdown bauen.

---

# 22. Einen Countdown berechnen

Ein Countdown benötigt zwei Werte:

```python
minuten = 25
sekunden = 0
```

Nach einer Sekunde soll eine Sekunde abgezogen werden:

```python
sekunden -= 1
```

Bei:

```text
25:00
```

soll danach:

```text
24:59
```

angezeigt werden.

Danach:

```text
24:58
24:57
24:56
...
```

Wenn die Sekunden bei `0` angekommen sind, müssen wir zur nächsten Minute wechseln.

Zum Beispiel:

```text
10:00
09:59
09:58
```

---

# 23. Timer-Anzeige formatieren

Für einen Timer wollen wir immer zwei Stellen anzeigen.

Also:

```text
05:07
```

und nicht:

```text
5:7
```

Dafür können wir einen f-String mit `:02d` verwenden:

```python
anzeige = f"{minuten:02d}:{sekunden:02d}"
```

Beispiel:

```python
minuten = 5
sekunden = 7

anzeige = f"{minuten:02d}:{sekunden:02d}"

print(anzeige)
```

Ergebnis:

```text
05:07
```

`02d` bedeutet:

- mindestens zwei Stellen
- bei Bedarf mit `0` auffüllen
- Zahl als ganze Zahl formatieren

---

# 24. Einen laufenden Timer speichern

Wenn wir `after()` verwenden, können wir die Rückgabe speichern:

```python
timer = fenster.after(
    1000,
    zaehlen
)
```

Die Variable `timer` enthält dann die ID des geplanten Aufrufs.

Diese ID benötigen wir, wenn wir den Timer abbrechen möchten.

---

# 25. `after_cancel()`

Ein geplanten `after()`-Aufruf können wir mit `after_cancel()` abbrechen.

```python
fenster.after_cancel(
    timer
)
```

Das ist beispielsweise für einen Reset wichtig.

Ein Timer kann also:

```text
Start
  ↓
after()
  ↓
läuft
  ↓
Reset
  ↓
after_cancel()
  ↓
Timer gestoppt
```

Wichtig ist, dass `timer` tatsächlich eine gültige `after()`-ID enthält.

Deshalb wird die Variable häufig zunächst mit `None` angelegt:

```python
timer = None
```

---

# 26. Globale Variablen

Bei einem kleinen Programm kann eine Variable von mehreren Funktionen benötigt werden.

Beispielsweise:

```python
timer = None
```

Wenn eine Funktion diese Variable verändern soll, benötigen wir `global`:

```python
def reset():
    global timer

    timer = None
```

Das ist in kleinen Tkinter-Übungen praktisch.

Bei größeren Anwendungen würde man später häufig mit Klassen arbeiten.

Das behandeln wir heute noch nicht.

---

# 27. Zusätzliche Fenster mit `Toplevel`

Neben dem Hauptfenster kann eine Anwendung weitere Fenster öffnen.

Dafür verwenden wir:

```python
neues_fenster = tk.Toplevel(
    fenster
)
```

Das neue Fenster kann anschließend konfiguriert werden:

```python
neues_fenster.title(
    "Information"
)

neues_fenster.config(
    bg="white"
)
```

Auch dort können Widgets verwendet werden:

```python
label = tk.Label(
    neues_fenster,
    text="Timer beendet!"
)

label.grid(
    row=0,
    column=0
)
```

---

# 28. Ein zusätzliches Fenster schließen

Ein `Toplevel`-Fenster kann mit `.destroy()` geschlossen werden.

```python
neues_fenster.destroy()
```

Deshalb können wir beispielsweise einen Button erstellen:

```python
button = tk.Button(
    neues_fenster,
    text="Schließen",
    command=neues_fenster.destroy
)
```

Beim Klick wird das Fenster geschlossen.

---

# 29. JSON-Daten laden

Aus Tag 3 kennen wir JSON.

Eine JSON-Datei könnte beispielsweise so aussehen:

```json
{
  "titel": "Mein Dashboard",
  "beschreibung": "Meine Informationen"
}
```

Wir können die Datei mit `json.load()` laden:

```python
import json

with open(
    "daten.json",
    encoding="utf-8"
) as datei:
    daten = json.load(datei)
```

Danach enthält `daten` ein Dictionary.

Wir können auf die Werte zugreifen:

```python
print(daten["titel"])
```

---

# 30. JSON-Daten in einer GUI verwenden

Die geladenen Daten können direkt für Widgets verwendet werden.

```python
label = tk.Label(
    fenster,
    text=daten["titel"]
)

label.grid(
    row=0,
    column=0
)
```

Damit kommt der Text nicht direkt aus dem Python-Code.

Er kommt aus der JSON-Datei.

Das Prinzip lautet:

```text
daten.json
    ↓
json.load()
    ↓
Python-Daten
    ↓
Tkinter
    ↓
GUI
```

---

# 31. Verschachtelte JSON-Daten

JSON kann auch Listen mit Dictionaries enthalten.

Zum Beispiel:

```json
{
  "aufgaben": [
    {
      "titel": "Backup prüfen",
      "status": "offen"
    },
    {
      "titel": "Server aktualisieren",
      "status": "erledigt"
    }
  ]
}
```

Nach dem Laden können wir mit einer normalen `for`-Schleife durch die Aufgaben gehen:

```python
for aufgabe in daten["aufgaben"]:
    print(aufgabe["titel"])
```

Dabei ist:

```python
aufgabe
```

jeweils ein Dictionary.

Wir können daraus direkt Widgets erzeugen.

---

# 32. Widgets mit einer Schleife erzeugen

Angenommen, wir haben mehrere Aufgaben:

```python
zeile = 0

for aufgabe in daten["aufgaben"]:

    label = tk.Label(
        fenster,
        text=aufgabe["titel"]
    )

    label.grid(
        row=zeile,
        column=0
    )

    zeile += 1
```

Für jeden Eintrag wird ein eigenes Label erzeugt.

Bei drei Aufgaben entstehen also drei Labels.

Die Oberfläche wird dadurch aus den Daten aufgebaut.

Das nennt man eine **dynamische Oberfläche**.

---

# 33. Bildpfade aus JSON verwenden

Auch Bilddateien können in einer JSON-Datei angegeben werden.

Zum Beispiel:

```json
{
  "titel": "Projekt 1",
  "bild": "bilder/bild1.png"
}
```

Nach dem Laden:

```python
pfad = daten["bild"]
```

Für einen vollständigen Pfad kann `Path` verwendet werden.

```python
from pathlib import Path

bild_pfad = Path(
    __file__
).parent / daten["bild"]
```

Anschließend kann der Pfad an `PhotoImage` übergeben werden:

```python
bild = tk.PhotoImage(
    file=bild_pfad
)
```

Damit kann eine JSON-Datei bestimmen, welches Bild zu einem Datensatz gehört.

---

# 34. Bilder in einer Liste speichern

Bei mehreren Bildern ist es sinnvoll, die Bildobjekte in einer Liste zu speichern.

Zum Beispiel:

```python
bilder = []
```

Wenn ein Bild geladen wird:

```python
bild = tk.PhotoImage(
    file="bilder/bild1.png"
)

bilder.append(
    bild
)
```

Warum?

Tkinter muss das Bildobjekt während der Laufzeit behalten.

Die Liste sorgt dafür, dass die geladenen Bilder weiterhin referenziert werden.

Bei mehreren Bildern:

```python
bilder = []

for datei in bilddateien:
    bild = tk.PhotoImage(
        file=datei
    )

    bilder.append(
        bild
    )
```

---

# 35. Eine kleine dynamische Karte

Aus diesen Bausteinen können wir beispielsweise eine Karte erstellen:

```python
karte = tk.Frame(
    fenster,
    bg="white"
)
```

Darin können mehrere Widgets liegen:

```python
titel = tk.Label(
    karte,
    text="Projekt 1",
    bg="white"
)

titel.grid(
    row=0,
    column=0
)
```

Weitere Informationen können darunter angezeigt werden:

```python
status = tk.Label(
    karte,
    text="Aktiv",
    bg="white"
)

status.grid(
    row=1,
    column=0
)
```

Eine solche Karte kann für jeden Eintrag einer JSON-Datei erzeugt werden.

---

# 36. Eine Tkinter-Anwendung strukturieren

Eine kleine Anwendung kann beispielsweise so aufgebaut werden:

```text
Imports
   ↓
Konstanten
   ↓
Funktionen
   ↓
Fenster erstellen
   ↓
Widgets erstellen
   ↓
Widgets positionieren
   ↓
mainloop()
```

Bei einer Anwendung mit JSON-Daten bietet sich folgende Struktur an:

```text
JSON laden
    ↓
Daten verarbeiten
    ↓
Fenster erstellen
    ↓
Widgets erstellen
    ↓
Daten in Widgets einsetzen
    ↓
mainloop()
```

---

# 37. Typischer Aufbau einer Funktion für einen Button

Eine Funktion, die durch einen Button aufgerufen wird, kann beispielsweise die Oberfläche verändern:

```python
def starten():
    label.config(
        text="Gestartet!"
    )
```

Der Button:

```python
button = tk.Button(
    fenster,
    text="Start",
    command=starten
)
```

Damit entsteht die Verbindung:

```text
Klick
  ↓
Button
  ↓
command
  ↓
Funktion
  ↓
GUI verändert sich
```

---

# 38. Typischer Aufbau eines Timers

Ein einfacher Countdown besteht aus mehreren Schritten:

```text
Start
  ↓
Countdown-Funktion
  ↓
Anzeige aktualisieren
  ↓
Zeit verändern
  ↓
after()
  ↓
Countdown-Funktion
  ↓
...
```

Wenn die Zeit abgelaufen ist:

```text
00:00
  ↓
nächste Phase starten
  ↓
Information anzeigen
```

Damit lässt sich beispielsweise ein Pomodoro-Timer bauen.

---

# 39. Häufige Fehler

## `mainloop()` vergessen

Falsch:

```python
fenster = tk.Tk()
```

Richtig:

```python
fenster = tk.Tk()
fenster.mainloop()
```

---

## `command` falsch verwenden

Falsch:

```python
command=hallo()
```

Richtig:

```python
command=hallo
```

---

## Widget nicht positionieren

Das Widget wurde erstellt:

```python
label = tk.Label(
    fenster,
    text="Hallo"
)
```

aber noch nicht angezeigt.

Es braucht beispielsweise:

```python
label.grid(
    row=0,
    column=0
)
```

---

## Falsche `after()`-Zeit

`after()` verwendet Millisekunden.

```python
1000
```

bedeutet:

```text
1 Sekunde
```

Nicht:

```text
1000 Sekunden
```

---

## Bild nicht speichern

Problematisch:

```python
canvas.create_image(
    100,
    100,
    image=tk.PhotoImage(file="bild.png")
)
```

Besser:

```python
bild = tk.PhotoImage(
    file="bild.png"
)

canvas.create_image(
    100,
    100,
    image=bild
)
```

---

## `after_cancel()` ohne Timer-ID

Damit ein geplanter Aufruf abgebrochen werden kann, muss seine ID gespeichert werden:

```python
timer = fenster.after(
    1000,
    funktion
)
```

Danach:

```python
fenster.after_cancel(
    timer
)
```

---

# 40. Zusammenfassung

Heute hast du gelernt:

```text
Tkinter
  ↓
Tk()
  ↓
Fenster
  ↓
Widgets
  ↓
grid()
  ↓
Benutzerinteraktion
  ↓
Funktionen
```

Die wichtigsten Widgets dieses Tages sind:

| Widget | Verwendung |
|---|---|
| `Tk` | Hauptfenster |
| `Label` | Text anzeigen |
| `Button` | Aktion auslösen |
| `Entry` | Text eingeben |
| `Canvas` | Bilder und Zeichenfläche |
| `Toplevel` | zusätzliches Fenster |
| `Frame` | Widgets gruppieren |

Wichtige Methoden:

| Methode | Verwendung |
|---|---|
| `title()` | Fenstertitel setzen |
| `config()` | Eigenschaften verändern |
| `grid()` | Widget positionieren |
| `get()` | Eingabe aus `Entry` lesen |
| `delete()` | Eingabe löschen |
| `create_text()` | Text auf Canvas anzeigen |
| `create_image()` | Bild auf Canvas anzeigen |
| `itemconfig()` | Canvas-Element verändern |
| `after()` | Funktion später ausführen |
| `after_cancel()` | geplanten Aufruf abbrechen |
| `destroy()` | Fenster schließen |

Außerdem können JSON-Daten als Datenquelle für eine GUI verwendet werden:

```text
JSON
 ↓
json.load()
 ↓
Python-Daten
 ↓
for-Schleife
 ↓
Tkinter-Widgets
 ↓
grafische Oberfläche
```

Damit können wir Oberflächen erstellen, deren Inhalt nicht fest im Python-Code steht, sondern aus externen Daten geladen wird.

---

# 41. Ausblick: Mini-Projekt

Im Mini-Projekt baust du eine kleine Desktop-App, die eine JSON-Datei einliest.

Die JSON-Datei enthält beispielsweise:

- einen Titel
- einen Untertitel
- mehrere Einträge
- Texte
- Statusinformationen
- Bildpfade

Deine Anwendung soll daraus automatisch eine grafische Oberfläche erzeugen.

Das bedeutet:

```text
daten.json
     ↓
 JSON laden
     ↓
 Daten durchlaufen
     ↓
 Widgets erzeugen
     ↓
 Bilder laden
     ↓
 Oberfläche anzeigen
```

Die Bilddateien werden dabei separat im Projektordner abgelegt.

Die konkrete Gestaltung der App kannst du selbst bestimmen.
