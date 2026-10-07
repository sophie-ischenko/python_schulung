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

# Tkinter: die Grundkonzepte

## Tag 4

**Vom Terminal zum klickbaren Programm**

---

# Was ist Tkinter?

Tkinter ist in Python **eingebaut**. Du brauchst nichts zu installieren.

Damit baust du Programme mit **Fenstern, Buttons und Eingabefeldern**.

```python
import tkinter as tk
```

Ein Terminal-Programm läuft **von oben nach unten** und ist dann fertig.
Ein GUI-Programm **wartet** auf das, was der Mensch tut.

---

# Das Hauptfenster

```python
import tkinter as tk

window = tk.Tk()
window.title("Meine GUI")

window.mainloop()
```

- `tk.Tk()` erstellt das Fenster
- `title()` setzt die Titelzeile
- `mainloop()` hält das Fenster offen

---

# Die Ereignisschleife (`mainloop`)

`mainloop()` ist eine Schleife, die **ständig prüft**:

- Wurde geklickt?
- Wurde eine Taste gedrückt?
- Ist ein Timer abgelaufen?

Wenn ja, ruft sie die passende Funktion auf.

Ohne `mainloop()` ist das Programm **sofort wieder zu**.

Alles, was nach `mainloop()` im Code steht, läuft erst, **wenn das Fenster geschlossen ist**.

---

# Widgets: die Bausteine

Alles Sichtbare in einem Fenster ist ein **Widget**.

| Widget | Wofür |
|---|---|
| `Label` | Text anzeigen |
| `Button` | Klicken, löst eine Funktion aus |
| `Entry` | Text eingeben |
| `Canvas` | Zeichenfläche für Text, Bilder, Formen |
| `Toplevel` | zusätzliches Fenster |

---

# Widgets: erstellen und positionieren

Jedes Widget braucht **zwei Schritte**:

```python
label = tk.Label(window, text="Hallo")   # 1. erstellen
label.grid(row=0, column=0)              # 2. positionieren
```

Das **erste Argument** ist immer das Fenster, in dem das Widget liegt.

Ohne `grid()` ist das Widget **unsichtbar**.

---

# Layout mit `grid()`

Das Fenster wird in **Zeilen und Spalten** aufgeteilt.

```text
        column 0   column 1
row 0 │    A     │    B     │
row 1 │    C     │    D     │
```

```python
a.grid(row=0, column=0)
b.grid(row=0, column=1)
```

Die Zählung beginnt bei **0**.

---

# `grid()`: Abstand und Breite

```python
label.grid(row=0, column=0, columnspan=2, pady=10)
```

| Option | Bedeutung |
|---|---|
| `columnspan=2` | Widget geht über 2 Spalten |
| `padx` / `pady` | Abstand links/rechts bzw. oben/unten |

Zwei Widgets in derselben Zelle liegen **übereinander**.

---

# Button und `command`

Ein Button ruft beim Klick eine **Funktion** auf.

```python
def hallo():
    print("Hallo!")

button = tk.Button(window, text="Klick", command=hallo)
```

`command=hallo` ✅ die Funktion wird **übergeben**, Tkinter ruft sie beim Klick auf.

`command=hallo()` ❌ die Funktion wird **sofort ausgeführt**, beim Start.

---

# Widgets nachträglich ändern: `config()`

```python
label.config(text="Neuer Text")
label.config(fg="red")
button.config(state="disabled")    # sperren
button.config(state="normal")      # wieder freigeben
```

Eine Variable zu ändern ändert **nicht** automatisch die Anzeige.
Du musst das Widget **selbst aktualisieren**.

---

# Eingaben lesen: `Entry`

```python
eingabe = tk.Entry(window, width=20)
eingabe.grid(row=0, column=0)

name = eingabe.get()           # Inhalt lesen
name = eingabe.get().strip()   # Leerzeichen am Rand entfernen
eingabe.delete(0, tk.END)      # Feld leeren
```

`get()` liefert immer einen **String**.

---

# Zustand speichern: `global`

Ein Klick ruft eine Funktion auf, danach ist sie **wieder vorbei**.
Was sich merken soll, steht in einer Variable **außerhalb**.

```python
zaehler = 0

def erhoehen():
    global zaehler
    zaehler += 1
    label.config(text=str(zaehler))
```

Ohne `global` legt Python in der Funktion eine **neue, lokale** Variable an.

---

# Das Grundmuster einer GUI

```text
Klick → Funktion → Zustand ändern → Anzeige aktualisieren
```

```python
def erhoehen():
    global zaehler
    zaehler += 1                           # Zustand ändern
    label.config(text=str(zaehler))        # Anzeige aktualisieren
```

Fast jede GUI-Funktion heute folgt diesem Ablauf.

---

# Ein zweites Fenster: `Toplevel`

```python
top = tk.Toplevel(window)
top.title("Zweites Fenster")

label = tk.Label(top, text="Hallo")
label.grid(row=0, column=0)
```

Widgets im zweiten Fenster bekommen `top` als erstes Argument, **nicht** `window`.

`top.destroy()` schließt das Fenster wieder.

---

# Zeitgesteuert: `after()`

```python
window.after(2000, hallo)
```

Ruft `hallo` **nach 2000 Millisekunden** auf (= 2 Sekunden).

Die GUI **bleibt dabei bedienbar**. `time.sleep()` würde das Fenster einfrieren.

Reihenfolge: **Millisekunden, Funktion, Argument**

```python
window.after(1000, countdown, sekunden - 1)
```

---

# Ein Countdown aus `after()`

Die Funktion **ruft sich nach einer Sekunde selbst wieder auf**.

```python
def countdown(sekunden):
    if sekunden == 0:
        return                                 # Ende

    label.config(text=str(sekunden))
    window.after(1000, countdown, sekunden - 1)
```

Die **Ende-Bedingung** muss vor dem nächsten `after()` stehen, sonst zählt er ins Negative.

---

# Timer merken und abbrechen

`after()` gibt eine **ID** zurück. Mit ihr kann man den Timer abbrechen.

```python
timer = None                                   # es läuft keiner

timer = window.after(1000, countdown, 9)       # ID merken
window.after_cancel(timer)                     # abbrechen
```

```python
if timer is not None:      # es läuft schon einer
    return
```

In Funktionen, die `timer` ändern, braucht es `global timer`.

---

# Minuten und Sekunden

```python
minuten = 125 // 60     # 2   Ganzzahl-Division
rest    = 125 % 60      # 5   Rest

f"{minuten:02d}:{rest:02d}"     # "02:05"
```

`:02d` bedeutet: **zweistellig**, mit führender Null.

---

# `Canvas`: die Zeichenfläche

```python
canvas = tk.Canvas(window, width=240, height=150)
canvas.grid(row=0, column=0)

zahl_text = canvas.create_text(120, 75, text="00:10", fill="red")
```

- Position mit **x, y** in Pixeln (von links oben)
- `create_text()` gibt eine **ID** zurück, die du dir merkst
- Die Farbe heißt hier **`fill`**, nicht `fg`


---

# Bilder auf dem Canvas

```python
from pathlib import Path
ORDNER = Path(__file__).parent

tomato_img = tk.PhotoImage(file=ORDNER / "bilder" / "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
```

- `Path(__file__).parent` ist der Ordner **neben der Datei**
- Das Bild muss in einer **Variable** bleiben, sonst verschwindet es


---

# Daten sammeln: Strings aufbauen

```python
checkmark = ""

checkmark += "✓"
checkmark += "✓"          # jetzt "✓✓"

label_check.config(text=checkmark)
```

Die Variable allein ändert das Label **nicht**. Erst `config()` zeigt es an.

---

# `lambda`: Werte an `command` übergeben

```python
command=naechste_phase(top)             # ❌ läuft sofort
command=lambda: naechste_phase(top)     # ✅ läuft beim Klick
```

`lambda:` packt den Aufruf in eine kleine Funktion, die **erst beim Klick** ausgeführt wird.

Nötig, wenn die Funktion **einen Wert** bekommen soll.

---

# Typische Fehler

| Symptom | Ursache |
|---|---|
| Button tut nichts | `command=funktion()` mit Klammern |
| Widget unsichtbar | `grid()` vergessen |
| `Entry` liefert `None` | `Entry(...).grid(...)` in einer Zeile |
| Reset bricht nichts ab | `global timer` fehlt |
| Zählt ins Negative | Ende-Prüfung nach dem `after()` |
| Bild fehlt | Bild nicht in einer Variable gespeichert |
| Kein Fenster (Mac) | `Cmd + Tab`, `python3` verwenden |

---

# Zusammenfassung

| Konzept | Merksatz |
|---|---|
| `mainloop()` | wartet auf Ereignisse |
| Widget | erst erstellen, dann `grid()` |
| `command` | Funktion **ohne** Klammern |
| `config()` | ändert ein Widget nachträglich |
| `global` | Variable außerhalb ändern |
| `after()` | später ausführen, ohne einzufrieren |
| `after_cancel()` | geplanten Aufruf abbrechen |
| `Canvas` | Elemente über ihre ID ändern |

---

# Wo brauchst du was?

| Projekt | Konzepte |
|---|---|
| **1** Begrüßung + Klick-Zähler | Fenster, Widgets, `grid`, `command`, `config`, `Entry`, `global`, `Toplevel` |
| **2** Begrüßung + Countdown | `after`, `after_cancel`, MM:SS, `Canvas` |
| **3** Pomodoro-Timer | Phasen, Häkchen, Bild, `lambda` |