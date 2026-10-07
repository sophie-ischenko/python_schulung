# Python GUI mit Tkinter – Mitmach-Skript

**Tag 4**

Herzlich willkommen zu Tag 4! 🎉

Bisher haben wir Python-Programme im Terminal ausgeführt. Heute bauen wir zum ersten Mal etwas, das man **sehen und anklicken** kann: richtige Fenster mit Text, Eingabefeldern und Buttons.

Dieses Skript ist ein **Mitmach-Skript**. Du liest nicht nur, du tippst mit. An jeder Stelle, an der du etwas tun sollst, steht **🛠 Mitmachen**. Alles andere ist Erklärung.

---

# So arbeiten wir heute

Wir bauen **drei Projekte**. Jedes baut auf dem vorherigen auf, und mit jedem bekommst du weniger Hilfe:

| Projekt | Was entsteht | Wie arbeiten wir | Hilfe |
|---|---|---|---|
| **1** | Fenster 1 begrüßt dich, Fenster 2 zählt deine Klicks | Wir bauen es **gemeinsam**, Schritt für Schritt | Du tippst den Code mit |
| **2** | Fenster 1 begrüßt dich, Fenster 2 zählt **herunter** statt Klicks | **Du** baust Fenster 2 | Gerüst mit Hinweisen |
| **3** | Pomodoro-Timer | **Du** baust die Logik | Gerüst mit weniger Hinweisen |

Der rote Faden: Aus dem **Klick-Zähler** wird ein **Countdown**, und aus dem Countdown wird ein **Pomodoro-Timer**. Jedes Mal kommt nur wenig Neues dazu.

---

# Vorbereitung

**1. Lege einen Ordner `tag4` an** und kopiere die Startdatei `projekt1_begruessung_zaehler.py` hinein. Das ist deine Arbeitsdatei: Sie enthält schon das leere Fenster (Schritt 1) und markiert mit `>>> SCHRITT 2 <<<` usw., wo du den Code der nächsten Schritte einfügst. Wenn du lieber bei null anfängst, lege stattdessen eine leere Datei `projekt1.py` an.


---

# Projekt 1: Begrüßung und Klick-Zähler

**Unser Ziel:** Ein Fenster fragt nach deinem Namen. Du klickst auf "Begrüßen", es erscheint "Hallo, Sophie!", und gleichzeitig öffnet sich ein zweites Fenster mit einem Klick-Zähler, in dem dein Name steht.

Wir bauen das in sieben kleinen Schritten. Nach jedem Schritt kannst du das Programm starten und siehst, was neu ist.

---

## Schritt 1: Das erste Fenster

### Was ist Tkinter?

Tkinter ist eine Python-Bibliothek für grafische Oberflächen. Die Abkürzung dafür ist **GUI** (*Graphical User Interface*). Tkinter gehört zu Python und muss nicht installiert werden.

Die Bausteine einer GUI heißen **Widgets**: Texte (`Label`), Schaltflächen (`Button`), Eingabefelder (`Entry`), Zeichenflächen (`Canvas`) und weitere Fenster (`Toplevel`).

### Das Hauptfenster

Jede Tkinter-Anwendung braucht ein Hauptfenster. Das erstellen wir mit `tk.Tk()`. Damit es offen bleibt und auf Klicks reagiert, brauchen wir ganz am Ende `mainloop()`. Das ist die Ereignisschleife: Das Programm wartet dort auf Klicks, Tastatur und Timer. Ohne `mainloop()` ist das Programm sofort wieder zu Ende.

Mit `title()` setzt du den Titel, mit `config()` Farbe und Abstände. `padx` und `pady` sind Abstände nach innen, horizontal und vertikal.

### 🛠 Mitmachen

Wenn du die Startdatei benutzt, ist dieser Code schon drin: lies ihn durch und starte ihn. Wenn du bei null anfängst, öffne `projekt1.py` und tippe:

```python
import tkinter as tk


# ---------------------------- KONSTANTEN ---------------------------- #

FARBE_HINTERGRUND = "#f7f5dd"
FARBE_TEXT = "#e7305b"
FONT_NAME = "Courier"


# ---------------------------- FENSTER 1: BEGRÜSSUNG ---------------------------- #

window = tk.Tk()
window.title("Begrüßung")
window.config(bg=FARBE_HINTERGRUND, padx=50, pady=30)


# ---------------------------- START ---------------------------- #


window.mainloop()
```

Starte das Programm mit `python3 projekt1.py`. Es sollte ein **leeres beiges Fenster** erscheinen.

Warum stehen Farben und Schrift oben als **Konstanten**? Weil du sie so an einer einzigen Stelle ändern kannst und nicht überall im Code suchen musst. Großbuchstaben zeigen: Diese Werte ändern sich im Programm nicht.

> **Merksatz:** Ein Fenster braucht `tk.Tk()` am Anfang und `mainloop()` am Ende.

---

## Schritt 2: Ein Label

### Was ist ein Label?

Ein `Label` zeigt Text an. Ein Widget wird in **zwei Schritten** gebaut:

1. **Erstellen:** Das Widget kennt sein Fenster und seine Einstellungen.
2. **Positionieren:** Erst jetzt erscheint es im Fenster.

```python
label = tk.Label(window, text="Hallo")      # 1. erstellen
label.grid(row=0, column=0)                 # 2. positionieren
```

> **Wichtig:** Ohne `grid()` ist das Widget **unsichtbar**. Das ist der häufigste Anfängerfehler.

Beim Erstellen bekommt jedes Widget als erstes das Fenster, in dem es liegt. Danach folgen die Einstellungen:

- `text` ist der Text
- `font` ist die Schrift als Tupel: `("Courier", 20)`
- `fg` ist die Textfarbe
- `bg` ist die Hintergrundfarbe

### `grid()`

`grid()` ordnet Widgets in einem Raster aus Zeilen und Spalten an. Gezählt wird ab **0**.

```text
┌──────────────┬──────────────┐
│ row=0,col=0  │ row=0,col=1  │
├──────────────┼──────────────┤
│ row=1,col=0  │ row=1,col=1  │
└──────────────┴──────────────┘
```

Mit `padx` und `pady` gibst du Abstand um das Widget herum, mit `columnspan` lässt du es über mehrere Spalten laufen.

### 🛠 Mitmachen

Füge **unter** `window.config(...)` und **über** dem Start-Block ein:

```python
label_titel = tk.Label(
    window,
    text="Wie heißt du?",
    font=(FONT_NAME, 20),
    fg=FARBE_TEXT,
    bg=FARBE_HINTERGRUND
)
label_titel.grid(row=0, column=0)
```

Starte das Programm. Die Frage steht jetzt im Fenster.

---

## Schritt 3: Ein Eingabefeld

### `Entry`

Mit `Entry` kann der Benutzer Text eingeben. Den Inhalt liest du später mit `.get()` aus. Ein Eingabefeld **erstellst und positionierst** du genau wie ein Label.

### 🛠 Mitmachen

Direkt unter das Label:

```python
eingabe = tk.Entry(
    window,
    font=(FONT_NAME, 16),
    width=20
)
eingabe.grid(row=1, column=0, pady=10)
```

Starte das Programm und tippe etwas in das Feld.

> **Achtung, Fallstrick:** Schreibe **nie** `eingabe = tk.Entry(...).grid(...)` in einer Zeile. `grid()` gibt nichts zurück, und deine Variable `eingabe` wäre danach `None`. Dann schlägt später `.get()` fehl. Immer zwei Schritte!

---

## Schritt 4: Der Button und die Begrüßung

### Funktionen mit Buttons verbinden

Ein Button soll etwas auslösen. Dazu schreiben wir zuerst eine **Funktion** und verbinden sie mit `command`:

```python
def hallo():
    print("Hallo!")

button = tk.Button(window, text="Klick mich", command=hallo)
```

Ganz wichtig: **ohne Klammern**!

```python
command=hallo      # richtig: Tkinter ruft hallo() später beim Klick auf
command=hallo()    # falsch: hallo() läuft sofort beim Programmstart
```

Bei `command=hallo` gibst du Tkinter die Funktion. Tkinter ruft sie auf, wenn jemand klickt.

### Widgets nachträglich ändern: `config()`

Ein Widget kannst du nach dem Erstellen verändern:

```python
label.config(text="Neuer Text")
```

### Text zusammenbauen: f-Strings

Mit einem f-String setzt du Variablen in einen Text ein:

```python
name = "Sophie"
text = f"Hallo, {name}!"
```

### 🛠 Mitmachen

**Zuerst die Funktion.** Funktionen stehen im Programm **oberhalb** des Hauptfensters. Füge diesen Block direkt nach den Konstanten ein:

```python
# ---------------------------- FENSTER 1: BEGRÜSSUNG ---------------------------- #

def begruessen():
    """Liest den Namen und zeigt die Begrüßung an."""

    name = eingabe.get().strip()

    if name == "":
        label_ausgabe.config(text="Bitte gib einen Namen ein.")
        return

    label_ausgabe.config(text=f"Hallo, {name}!")
```

Was passiert hier?

- `eingabe.get()` liest den Text aus dem Feld.
- `.strip()` entfernt Leerzeichen am Anfang und Ende.
- Ist das Feld leer, zeigen wir einen Hinweis an und beenden die Funktion mit `return`.
- Sonst zeigen wir die Begrüßung im Label `label_ausgabe` an. Das legen wir gleich an.

**Dann die Widgets.** Unter das Eingabefeld (also nach `eingabe.grid(...)`):

```python
button_gruss = tk.Button(
    window,
    text="Begrüßen",
    font=(FONT_NAME, 18),
    fg=FARBE_TEXT,
    bg=FARBE_HINTERGRUND,
    activebackground=FARBE_HINTERGRUND,
    command=begruessen
)
button_gruss.grid(row=2, column=0)

label_ausgabe = tk.Label(
    window,
    text="",
    font=(FONT_NAME, 20),
    fg=FARBE_TEXT,
    bg=FARBE_HINTERGRUND
)
label_ausgabe.grid(row=3, column=0, pady=10)
```

Starte das Programm: Name eingeben, auf "Begrüßen" klicken. Funktioniert es? Dann probiere es auch mit leerem Feld.

> **Merksatz:** `command=funktion` ohne Klammern. Mit `config()` änderst du ein Widget später.

---

## Schritt 5: Fenster 2 mit dem Zähler

### Zusätzliche Fenster: `Toplevel`

Neben dem Hauptfenster kann eine Anwendung weitere Fenster öffnen. Dafür gibt es `tk.Toplevel(window)`. Widgets, die in dieses Fenster sollen, bekommen es als erstes Argument statt `window`.

```python
top = tk.Toplevel(window)
top.title("Zweites Fenster")
```

### Variablen in Funktionen verändern: `global`

Unser Zähler ist eine Zahl, die mehrere Funktionen brauchen: `erhoehen()` zählt hoch, `reset()` setzt sie zurück. Wenn eine Funktion eine Variable **von außen** verändern soll, braucht sie `global`:

```python
zaehler = 0

def erhoehen():
    global zaehler
    zaehler += 1
```

Ohne `global zaehler` bricht Python mit einem `UnboundLocalError` ab. `zaehler += 1` ist die Kurzform für `zaehler = zaehler + 1`.

Bei kleinen Programmen ist das praktisch. Bei großen würde man später mit Klassen arbeiten, aber das ist heute kein Thema.

### Zahl in Text umwandeln: `str()`

Ein Label zeigt Text. Eine Zahl wandelst du mit `str(...)` in Text um:

```python
label_zahl.config(text=str(zaehler))
```

### 🛠 Mitmachen

Füge **direkt nach den Konstanten** (vor `begruessen()`) die Variablen und das ganze Zähler-Fenster ein:

```python
# ---------------------------- VARIABLEN ---------------------------- #

zaehler = 0
label_zahl = None   # wird erst in zaehler_fenster() erstellt


# ---------------------------- FENSTER 2: ZÄHLER ---------------------------- #

def erhoehen():
    """Erhöht den Zähler um 1 und zeigt ihn an."""

    global zaehler

    zaehler += 1
    label_zahl.config(text=str(zaehler))


def reset():
    """Setzt den Zähler auf 0 zurück."""

    global zaehler

    zaehler = 0
    label_zahl.config(text=str(zaehler))


def zaehler_fenster(name):
    """Öffnet das zweite Fenster mit dem Klick-Zähler."""

    global label_zahl

    top = tk.Toplevel(window)
    top.title("Klick-Zähler")
    top.config(bg=FARBE_HINTERGRUND, padx=40, pady=30)

    label_titel = tk.Label(
        top,
        text=f"Klicks von {name}",
        font=(FONT_NAME, 20),
        fg=FARBE_TEXT,
        bg=FARBE_HINTERGRUND
    )
    label_titel.grid(row=0, column=0, columnspan=2, pady=10)

    label_zahl = tk.Label(
        top,
        text="0",
        font=(FONT_NAME, 40),
        fg=FARBE_TEXT,
        bg=FARBE_HINTERGRUND
    )
    label_zahl.grid(row=1, column=0, columnspan=2)

    button_plus = tk.Button(
        top,
        text="+1",
        font=(FONT_NAME, 18),
        fg=FARBE_TEXT,
        bg=FARBE_HINTERGRUND,
        activebackground=FARBE_HINTERGRUND,
        command=erhoehen
    )
    button_plus.grid(row=2, column=0, pady=10)

    button_reset = tk.Button(
        top,
        text="Reset",
        font=(FONT_NAME, 18),
        fg=FARBE_TEXT,
        bg=FARBE_HINTERGRUND,
        activebackground=FARBE_HINTERGRUND,
        command=reset
    )
    button_reset.grid(row=2, column=1, pady=10)
```

Das ist viel auf einmal, aber nichts davon ist neu: Es sind die Bausteine aus Schritt 1 bis 4, nur in einem `Toplevel`-Fenster. Drei Stellen sind besonders:

- `zaehler_fenster(name)` bekommt den Namen als **Argument** und setzt ihn in die Überschrift ein.
- `label_zahl` wird in dieser Funktion erstellt, aber in `erhoehen()` und `reset()` gebraucht. Deshalb steht oben `label_zahl = None` und in der Funktion `global label_zahl`.
- Die Buttons gehören zu `top`, nicht zu `window`. Sonst würden sie im falschen Fenster erscheinen.

---

## Schritt 6: Die Fenster verbinden

Jetzt fehlt nur noch, dass das Begrüßen das zweite Fenster öffnet. Ergänze `begruessen()` um zwei Zeilen am Ende:

### 🛠 Mitmachen

```python
def begruessen():
    """Liest den Namen, begrüßt und öffnet das Zähler-Fenster."""

    name = eingabe.get().strip()

    if name == "":
        label_ausgabe.config(text="Bitte gib einen Namen ein.")
        return

    label_ausgabe.config(text=f"Hallo, {name}!")
    button_gruss.config(state="disabled")

    zaehler_fenster(name)
```

Neu ist:

- `button_gruss.config(state="disabled")` deaktiviert den Button, damit man nicht mehrere Zähler-Fenster öffnet. Mit `state="normal"` ist er wieder aktiv.
- `zaehler_fenster(name)` öffnet das zweite Fenster.

> **Gut zu wissen:** Python muss `zaehler_fenster` kennen, wenn du auf den Button klickst. Das ist der Fall, weil alle Funktionen oben im Programm stehen und das Fenster samt `mainloop()` erst danach kommt. Wir halten uns an die Regel: Funktionen oben, Fenster unten.

---

## Schritt 7: Ausprobieren

Starte dein Programm und prüfe:

1. Leeres Feld, Klick auf "Begrüßen": Es erscheint der Hinweis.
2. Name eingeben, Klick auf "Begrüßen": Es erscheint "Hallo, <Name>!", und ein zweites Fenster öffnet sich.
3. Im zweiten Fenster auf "+1" klicken: Die Zahl wächst.
4. "Reset" klicken: Die Zahl springt auf 0.

**Geschafft! 🎉** Du hast eine Anwendung mit zwei Fenstern gebaut. Der fertige Code zum Vergleich steht in `projekt1_begruessung_zaehler_loesung.py`.

---

## Typische Fehler bei Projekt 1

| Fehler | Symptom | Lösung |
|---|---|---|
| `grid()` vergessen | Widget ist unsichtbar | `.grid(row=..., column=...)` ergänzen |
| `command=funktion()` | Funktion läuft sofort, Button tut nichts | Klammern weglassen |
| `eingabe = tk.Entry(...).grid(...)` | `AttributeError: 'NoneType'...` | Erstellen und Positionieren in zwei Zeilen |
| `global` vergessen | `UnboundLocalError` im Terminal | `global zaehler` an den Funktionsanfang |
| Widget im falschen Fenster | Button erscheint im Hauptfenster | Beim Erstellen `top` statt `window` verwenden |
| `mainloop()` vergessen | Fenster geht sofort wieder zu | Als letzte Zeile einfügen |
| Fenster nicht sichtbar (Mac) | Läuft, aber kein Fenster | `Cmd + Tab`, Mac-Fix am Ende prüfen |

---

# Projekt 2: Begrüßung und Countdown

**Unser Ziel:** Fenster 1 bleibt, wie du es kennst. In Fenster 2 zählen wir aber nicht mehr Klicks, sondern **der Countdown läuft von 10 auf 0 herunter**. Bei 0 steht "Fertig!".

```text
Projekt 1:  Klick  ->  Zahl wird größer
Projekt 2:  Zeit   ->  Zahl wird kleiner (von allein!)
```

Das Spannende: Die Zahl ändert sich jetzt **ohne Klick**. Dafür brauchen wir ein neues Werkzeug, das Tkinter für uns mitbringt.

Du arbeitest in `projekt2_begruessung_countdown.py`. Fenster 1 ist dort schon fertig. Du füllst Fenster 2 und die Countdown-Logik aus, und zwar mit den **TODO-Hinweisen** im Gerüst. Hier kommt zuerst die Theorie dazu.

---

## Theorie 1: Etwas später ausführen: `after()`

Mit `after()` sagst du Tkinter: *"Führe diese Funktion später aus."*

```python
def hallo():
    print("Hallo!")

window.after(2000, hallo)
```

Die Zeit wird in **Millisekunden** angegeben:

```text
1000 Millisekunden = 1 Sekunde
2000 Millisekunden = 2 Sekunden
```

Nach zwei Sekunden wird `hallo()` aufgerufen. Das Programm bleibt in der Zwischenzeit bedienbar, es friert nicht ein.

> **Typischer Fehler:** `window.after(1, ...)` meint *eine Millisekunde*, nicht eine Sekunde.

---

## Theorie 2: Sich selbst wieder aufrufen

Ein Countdown braucht ein Ticken im Sekundentakt. Dafür ruft sich eine Funktion mit `after()` **immer wieder selbst** auf:

```python
def ticken():
    print("Tick")
    window.after(1000, ticken)
```

Einmal gestartet mit `ticken()`, läuft es von allein weiter:

```text
ticken()  ->  1 Sekunde warten  ->  ticken()  ->  1 Sekunde warten  ->  ...
```

---

## Theorie 3: Werte mitgeben

Beim Countdown muss die Funktion wissen, **wie viele Sekunden noch übrig sind**. `after()` kann Werte an die Funktion weitergeben:

```python
window.after(1000, countdown, sekunden - 1)
```

Die Reihenfolge ist immer:

```text
window.after( Millisekunden, Funktion, Argument )
```

Ein vollständiges Beispiel (ein Raketenstart, nur zum Verstehen):

```python
def rakete(sekunden):
    print(sekunden)

    if sekunden == 0:
        print("Start!")
        return

    window.after(1000, rakete, sekunden - 1)

rakete(5)
```

Das gibt im Sekundentakt `5 4 3 2 1 0 Start!` aus. Die Funktion hat ein **Ende**: Bei 0 hört sie mit `return` auf und ruft sich nicht mehr auf. Ohne dieses Ende würde sie endlos weiterzählen.

**Achtung, die Klammern:**

```python
window.after(1000, rakete, sekunden - 1)    # richtig
window.after(1000, rakete(sekunden - 1))    # falsch: läuft sofort!
```

Das ist derselbe Fehler wie bei `command=hallo()`.

---

## Theorie 4: Den Timer merken und abbrechen

`after()` gibt eine **ID** zurück, die den geplanten Aufruf beschreibt. Die speichern wir:

```python
timer = window.after(1000, rakete, sekunden - 1)
```

Mit dieser ID können wir den Aufruf wieder **abbrechen**:

```python
window.after_cancel(timer)
```

Das brauchen wir für den Reset-Button. Außerdem können wir damit verhindern, dass der Countdown **doppelt** gestartet wird: Solange `timer` etwas enthält, läuft der Countdown noch.

Deshalb legen wir die Variable am Anfang mit `None` an (*"gerade läuft nichts"*):

```python
timer = None
```

Und prüfen so:

```python
if timer is not None:
    return        # es läuft schon einer, also nichts tun
```

Das Muster, das du dir merken solltest:

```text
Start        ->  timer = window.after(...)       (läuft)
Ende/Reset   ->  timer = None                    (läuft nicht mehr)
Reset        ->  vorher window.after_cancel(timer)
```

Weil mehrere Funktionen `timer` ändern, braucht jede ein `global timer`.

---

## Theorie 5: Minuten und Sekunden berechnen: `//` und `%`

Ein Countdown rechnet am einfachsten mit **einer** Zahl: den Gesamtsekunden. Für die Anzeige brauchen wir daraus Minuten und Sekunden. Dafür gibt es zwei Operatoren:

| Operator | Name | Bedeutung |
|---|---|---|
| `//` | Ganzzahl-Division | wie oft passt die Zahl rein, ohne Rest |
| `%` | Modulo | was bleibt als Rest übrig |

Beispiel mit 125 Sekunden:

```python
gesamt = 125

minuten = gesamt // 60    # 2, denn 60 passt 2-mal in 125
rest = gesamt % 60        # 5, denn 125 - 2*60 = 5
```

125 Sekunden sind also 2 Minuten und 5 Sekunden.

> **Merksatz:** `//` gibt dir die Minuten, `%` gibt dir den Rest.

---

## Theorie 6: Zweistellig anzeigen: `:02d`

Ein Timer zeigt immer zwei Stellen: `05:07`, nicht `5:7`. Dafür gibt es im f-String die Formatierung `:02d`:

```python
minuten = 5
rest = 7
anzeige = f"{minuten:02d}:{rest:02d}"    # "05:07"
```

`02d` bedeutet: mindestens zwei Stellen, bei Bedarf mit `0` auffüllen, als ganze Zahl.

---

## Theorie 7: Der Canvas

Ein `Canvas` ist eine Zeichenfläche. Darauf kannst du Text, Bilder und Formen platzieren. Die Größe ist in Pixeln:

```python
canvas = tk.Canvas(window, width=240, height=150)
canvas.grid(row=0, column=0)
```

Auf einem Canvas liegt der Nullpunkt **links oben**, x geht nach rechts, y nach unten:

```text
(0, 0)
   ┌────────────→ x
   │
   ↓
   y
```

### Text auf dem Canvas

Mit `create_text()` setzt du Text an eine Position (x, y). Die Funktion gibt eine **ID** zurück, die du speicherst:

```python
zahl_text = canvas.create_text(
    120, 75,
    text="00:10",
    font=("Courier", 50, "bold"),
    fill="red"
)
```

Beachte: Auf dem Canvas heißt die Textfarbe **`fill`**, nicht `fg`.

### Text später ändern: `itemconfig()`

Mit der ID änderst du genau dieses Element:

```python
canvas.itemconfig(zahl_text, text="00:09")
```

Dadurch aktualisiert sich die Anzeige. Genau das passiert jede Sekunde im Countdown.

---

## Theorie 8: Variablen aus Funktionen heraus: `global` (Wiederholung)

Das Canvas wird in der Funktion `countdown_fenster()` erstellt, aber in `countdown()` und `reset()` gebraucht. Wie in Projekt 1 (`label_zahl`) legen wir die Variablen oben mit `None` an und schreiben in der Funktion `global`:

```python
canvas = None
zahl_text = None

def countdown_fenster(name):
    global canvas, zahl_text
    canvas = tk.Canvas(...)
    zahl_text = canvas.create_text(...)
```

Mehrere Variablen kannst du in einer `global`-Zeile mit Komma auflisten.

---

## Theorie 9: Das Fenster sauber schließen

Was passiert, wenn jemand das Countdown-Fenster mitten im Zählen schließt? Der Timer tickt weiter und will ein Fenster ändern, das nicht mehr existiert. Das gibt Fehlermeldungen.

Deshalb ist die Funktion `schliessen()` im Gerüst **schon fertig**. Sie bricht den Timer ab, schließt das Fenster und macht den Begrüßen-Button wieder aktiv. Verbunden wird sie mit:

```python
countdown_window.protocol("WM_DELETE_WINDOW", schliessen)
```

Das bedeutet: *"Wenn jemand auf das X des Fensters klickt, führe `schliessen` aus."* Du musst das nicht verstehen, nur an der richtigen Stelle abtippen (steht im TODO 2).

---

## 🛠 Dein Auftrag: Projekt 2

Öffne `projekt2_begruessung_countdown.py` und arbeite die **TODOs 1 bis 8** der Reihe nach ab:

| TODO | Was | Theorie dazu |
|---|---|---|
| 1 | `formatieren()` | `//`, `%`, `:02d` |
| 2 | Toplevel-Fenster erstellen | `Toplevel`, `global` |
| 3 | Titel-Label | wie in Projekt 1 |
| 4 | Canvas mit Text | Canvas, `create_text` |
| 5 | Start- und Reset-Button | wie in Projekt 1 |
| 6 | `start()` | `timer is not None`, `state` |
| 7 | `countdown()` | `after` mit Argument, `itemconfig` |
| 8 | `reset()` | `after_cancel` |

Tipps zum Testen:

- Nach jedem TODO kannst du starten, auch wenn noch nicht alles fertig ist.
- Mit TODO 1 bis 5 siehst du schon das Fenster, es zählt nur noch nicht.
- Zum Testen von `formatieren` kannst du eine Zeile `print(formatieren(125))` ans Dateiende setzen. Es sollte `02:05` erscheinen.

**Bonus:** Lass die Startzeit im ersten Fenster eingeben, oder färbe die Zahl in den letzten drei Sekunden rot.

### Typische Fehler bei Projekt 2

| Fehler | Symptom | Lösung |
|---|---|---|
| `after(1000, countdown(x))` | Alles läuft sofort durch | `after(1000, countdown, x)` ohne Klammern |
| `global timer` fehlt | Reset bricht nichts ab | `global timer` in jeder Funktion, die `timer` ändert |
| `timer = None` bei 0 vergessen | Start funktioniert danach nie wieder | Beim Ende `timer = None` setzen |
| Ende-Prüfung nach dem `after()` | Countdown zählt ins Negative | `if sekunden == 0` **vor** dem `after()` |
| `fg` statt `fill` auf dem Canvas | Fehlermeldung | Beim Canvas heißt es `fill` |
| `global` für `canvas` vergessen | `NameError` oder `None` | In `countdown_fenster` alle vier Variablen als `global` |

---

# Projekt 3: Pomodoro-Timer

**Unser Ziel:** Aus dem Countdown wird ein Pomodoro-Timer. Die Pomodoro-Technik teilt Arbeit in Phasen ein: 25 Minuten arbeiten, 5 Minuten Pause, nach vier Arbeitsphasen eine lange Pause. Jede geschaffte Arbeitsphase bekommt ein Häkchen.

```text
Phase 1  Arbeit
Phase 2  kurze Pause   ✓
Phase 3  Arbeit
Phase 4  kurze Pause   ✓✓
Phase 5  Arbeit
Phase 6  kurze Pause   ✓✓✓
Phase 7  Arbeit
Phase 8  lange Pause   ✓✓✓✓
```

Der Countdown aus Projekt 2 ist der **Motor**. Neu ist nur die Frage: *Welche Phase ist als Nächstes dran?* Der Rahmen (Fenster, Bild, Labels, Buttons) steht schon fertig im Gerüst `projekt3_pomodoro.py`. Du schreibst die Funktionen.

---

## Theorie 1: Bilder mit `PhotoImage`

Tkinter lädt Bilder mit `PhotoImage` und zeigt sie auf einem Canvas an:

```python
bild = tk.PhotoImage(file="bilder/tomato.png")
canvas.create_image(100, 112, image=bild)
```

**Wichtig:** Das Bild muss in einer **Variable** gespeichert bleiben. Sonst räumt Python es weg, und es erscheint nicht.

```python
bild = tk.PhotoImage(file="bild.png")            # richtig
image=tk.PhotoImage(file="bild.png")             # problematisch
```

---

## Theorie 2: Pfade richtig bauen

Der Pfad `"bilder/tomato.png"` funktioniert nur, wenn du das Programm **aus dem richtigen Ordner** startest. Besser ist, immer vom Ordner der Python-Datei aus zu rechnen:

```python
from pathlib import Path

ORDNER = Path(__file__).parent
```

- `__file__` ist der Pfad der aktuellen Python-Datei.
- `.parent` ist der Ordner, in dem sie liegt.

Mit `/` hängst du Ordner und Dateien an:

```python
bild = tk.PhotoImage(file=ORDNER / "bilder" / "tomato.png")
```

> **Merksatz:** Pfade immer ab dem Ordner der Python-Datei bauen, nicht ab dem Terminal.

Im Gerüst ist das schon fertig. Du musst nur darauf achten, dass der Ordner `bilder` neben der Datei liegt.

---

## Theorie 3: Entscheidungen mit `if`, `elif`, `else`

Der Timer muss entscheiden, welche Phase dran ist. Dafür gibt es eine Kette aus Bedingungen:

```python
if bedingung1:
    ...   # wird ausgeführt, wenn bedingung1 stimmt
elif bedingung2:
    ...   # sonst, wenn bedingung2 stimmt
else:
    ...   # sonst
```

Python prüft **von oben nach unten** und führt nur den **ersten** passenden Block aus.

### Modulo zum Prüfen von "teilbar durch"

Mit `%` prüfst du, ob eine Zahl durch eine andere teilbar ist: Dann ist der Rest 0.

```python
print(4 % 2)    # 0 -> gerade
print(5 % 2)    # 1 -> ungerade
print(8 % 8)    # 0 -> durch 8 teilbar
```

### Die Pomodoro-Logik

```python
if phase % 8 == 0:
    print("lange Pause")
elif phase % 2 == 0:
    print("kurze Pause")
else:
    print("Arbeit")
```

**Die Reihenfolge ist entscheidend.** Phase 8 ist auch durch 2 teilbar. Würdest du zuerst `% 2` prüfen, käme die lange Pause nie dran. Der speziellste Fall steht immer oben.

---

## Theorie 4: Häkchen sammeln

Nach jeder Arbeitsphase soll ein Häkchen dazukommen. Eine gerade Phase (ab Phase 2) kommt immer **nach** einer Arbeitsphase. Strings kannst du mit `+=` verlängern:

```python
checkmark = ""
checkmark += "✓"     # "✓"
checkmark += "✓"     # "✓✓"
```

Danach muss die Anzeige aktualisiert werden:

```python
label_check.config(text=checkmark)
```

> **Fallstrick:** Nur `checkmark += "✓"` ändert die Variable. Das Label sieht davon nichts. Du musst es mit `config()` selbst aktualisieren.

---

## Theorie 5 (Bonus): Buttons mit Argument: `lambda`

Bei `command` übergeben wir die Funktion **ohne Klammern**. Das geht nur, solange die Funktion **keine Werte braucht**. Was, wenn doch?

```python
def naechste_phase(fenster):
    fenster.destroy()
    start_timer()
```

`command=naechste_phase(top)` wäre wieder der Klammer-Fehler. Die Lösung ist `lambda`. Ein `lambda` ist eine **kleine namenlose Funktion**, die erst beim Klick ausgeführt wird:

```python
button = tk.Button(
    top,
    text="Zurück zum Timer",
    command=lambda: naechste_phase(top)
)
```

Man liest das so: *"Wenn geklickt wird, rufe `naechste_phase(top)` auf."*

| Schreibweise | Was passiert |
|---|---|
| `command=hallo` | beim Klick wird `hallo()` aufgerufen |
| `command=hallo()` | **falsch**, läuft sofort beim Start |
| `command=lambda: hallo("Ada")` | beim Klick wird `hallo("Ada")` aufgerufen |
| `command=hallo("Ada")` | **falsch**, läuft sofort beim Start |

> **Merksatz:** Braucht die Funktion einen Wert, setze `lambda:` davor.

Das Info-Fenster ist ein weiteres `Toplevel`, wie du es aus Projekt 1 und 2 kennst. `destroy()` schließt es.

---

## 🛠 Dein Auftrag: Projekt 3

Öffne `projekt3_pomodoro.py`. Der Rahmen ist fertig. Die TODOs sind in **zwei Stufen** gegliedert:

**Stufe 1 (Pflicht):** `reset()`, `start_timer()`, `countdown()`. Wenn das läuft, hast du einen funktionierenden Pomodoro-Timer. Nach jeder Phase klickst du selbst wieder auf Start.

**Stufe 2 (Bonus):** `info_fenster()` und `naechste_phase()`. Dann öffnet sich am Ende jeder Phase ein Fenster, und der Button darin startet die nächste Phase.

Die Test-Zeiten (1, 1, 2 Minuten) sind absichtlich kurz, damit du nicht 25 Minuten warten musst. Die echten Werte stehen als Kommentar daneben.

Tipps:

- Der Countdown aus Projekt 2 ist dein Vorbild. `countdown()` ist fast dasselbe.
- Teste `start_timer()` zuerst nur mit der Arbeitsphase und ergänze dann Pausen und Häkchen.
- Um Pausen schneller zu sehen, kannst du die Konstanten oben zum Testen auf `1` lassen und bei Bedarf kurz verkleinern. Sie sind absichtlich kurz gewählt.

### Typische Fehler bei Projekt 3

| Fehler | Symptom | Lösung |
|---|---|---|
| Häkchen-Label nicht aktualisiert | Häkchen erscheinen nie | `label_check.config(text=checkmark)` |
| `global checkmark` fehlt | Fehler im Terminal, nichts läuft | `global` am Funktionsanfang |
| `% 2` vor `% 8` geprüft | Lange Pause kommt nie | Speziellsten Fall nach oben |
| `command=naechste_phase(top)` | Fenster schließt sofort | `lambda: naechste_phase(top)` |
| Bild nicht gefunden | `TclError: couldn't open` | Ordner `bilder` neben die Datei legen |
| Häkchen kaum sichtbar | Label da, aber unsichtbar | Zum Testen `fg="black"` setzen |

---

# Zusammenfassung

Heute hast du gelernt:

```text
Tk()  ->  Fenster  ->  Widgets  ->  grid()  ->  Funktionen  ->  Timer
```

| Widget | Verwendung |
|---|---|
| `Tk` | Hauptfenster |
| `Toplevel` | zusätzliches Fenster |
| `Label` | Text anzeigen |
| `Button` | Aktion auslösen |
| `Entry` | Text eingeben |
| `Canvas` | Text und Bilder auf einer Fläche |

| Methode / Operator | Verwendung |
|---|---|
| `title()`, `config()` | Fenster einstellen |
| `grid()` | Widget positionieren |
| `command=funktion` | Funktion an Button binden (ohne Klammern) |
| `lambda:` | Funktion mit Wert an Button binden |
| `get()` | Eingabe lesen |
| `create_text()`, `create_image()`, `itemconfig()` | Canvas-Elemente |
| `after(ms, funktion, arg)` | Funktion später ausführen |
| `after_cancel(id)` | geplanten Aufruf abbrechen |
| `destroy()` | Fenster schließen |
| `//`, `%` | Minuten und Sekunden, "teilbar durch" |
| `Path(__file__).parent` | Ordner der Python-Datei |

## Dein Fahrplan

```text
Projekt 1:  Klick  ->  Zahl hoch                (gemeinsam gebaut)
Projekt 2:  Zeit   ->  Zahl runter, von allein  (du mit Hinweisen)
Projekt 3:  Phasen ->  Arbeit/Pause wechseln    (du mit weniger Hinweisen)
```

Du hast heute gesehen, wie aus einem kleinen Klick-Zähler Schritt für Schritt ein richtiges Programm wird. Genau so entstehen auch große Anwendungen: ein Baustein nach dem anderen. Gut gemacht! 🍅

---

# Ausblick: Mini-Projekt (Selbststudium)

Wenn du mehr üben möchtest, baue ein kleines **Dashboard**, das seinen Inhalt aus einer JSON-Datei liest:

```text
daten.json  ->  json.load()  ->  for-Schleife  ->  Labels  ->  Fenster
```

Beispiel für `daten.json`:

```json
{
  "titel": "Mein Dashboard",
  "aufgaben": [
    {"titel": "Backup prüfen", "status": "offen"},
    {"titel": "Server aktualisieren", "status": "erledigt"}
  ]
}
```

Laden und Widgets per Schleife erzeugen:

```python
import json

with open("daten.json", encoding="utf-8") as datei:
    daten = json.load(datei)

zeile = 1
for aufgabe in daten["aufgaben"]:
    label = tk.Label(window, text=aufgabe["titel"])
    label.grid(row=zeile, column=0)
    zeile += 1
```

Die Gestaltung ist dir überlassen. Viel Spaß beim Ausprobieren!
