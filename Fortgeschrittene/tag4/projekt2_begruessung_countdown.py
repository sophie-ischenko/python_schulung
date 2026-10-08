"""
Projekt 2: Begrüßung + Countdown

Fenster 1 (Begrüßung) kennst du aus Projekt 1, es ist schon fertig.
Fenster 2 zählt jetzt nicht mehr Klicks, sondern läuft von 10 auf 0
herunter. Das baust du.

Fenster 2 soll:

- "Los geht's, <Name>!" als Überschrift zeigen
- auf einem Canvas die Zeit als MM:SS anzeigen (am Anfang 00:10)
- mit "Start" herunterzählen
- mit "Reset" abbrechen und wieder 00:10 anzeigen
- verhindern, dass mehrere Countdowns gleichzeitig laufen
- bei 0 "Fertig!" anzeigen

Start:
    python3 projekt2_begruessung_countdown.py
"""

import tkinter as tk


# ---------------------------- KONSTANTEN ---------------------------- #

START_SEKUNDEN = 10

FARBE_HINTERGRUND = "#f7f5dd"
FARBE_TEXT = "#e7305b"
FONT_NAME = "Courier"


# ---------------------------- VARIABLEN ---------------------------- #

timer = None

# Diese vier werden erst in countdown_fenster() erstellt:
countdown_window = None
canvas = None
zahl_text = None
button_start = None


# ---------------------------- ZEIT FORMATIEREN ---------------------------- #

def formatieren(sekunden):
    """Wandelt Sekunden in einen Text im Format MM:SS um."""

    # TODO 1:
    # Rechne die Sekunden in Minuten und Rest-Sekunden um:
    #
    #     minuten = sekunden // 60
    #     rest = sekunden % 60
    #
    # Gib dann den zweistelligen Text zurück:
    #
    # Test: formatieren(10) soll "00:10" ergeben,
    #       formatieren(125) soll "02:05" ergeben.
    pass


# ---------------------------- FENSTER 2: COUNTDOWN ---------------------------- #

def countdown_fenster(name):
    """Öffnet das zweite Fenster mit dem Countdown."""

    # TODO 2:
    # Diese vier Variablen werden hier erstellt, aber überall gebraucht.
    # Deshalb brauchst du global:
    #
    #     Beispiel: countdown_window, canvas, zahl_text, button_start
    #
    # Erstelle dann das zusätzliche Fenster:
    #
    #
    # Diese Zeile ist schon fertig, sie sorgt dafür, dass beim Schließen
    # des Fensters der Timer sauber abgebrochen wird. Kopiere sie dazu:
    #
    #     countdown_window.protocol("WM_DELETE_WINDOW", schliessen)


    # TODO 3:
    # Erstelle ein Label "label_titel" in countdown_window
    # mit dem Text "Los geht's, Name xyz!"
    # (FONT_NAME, 20, fg=FARBE_TEXT, bg=FARBE_HINTERGRUND).
    #
    # Positioniere es: row=0, column=0, columnspan=2, pady=10


    # TODO 4:
    # Erstelle ein Canvas (Zeichenfläche) und zeige die Zeit darauf an.
    #
    #
    # Mit create_text() setzt du Text auf das Canvas.
    # Die zurückgegebene ID speicherst du in zahl_text,
    # damit du den Text später ändern kannst:
    #
    #
    # Positioniere das Canvas: row=1, column=0, columnspan=2


    # TODO 5:
    # Erstelle zwei Buttons in countdown_window:
    #
    #     button_start  -> Text "Start", command=start
    #     button_reset  -> Text "Reset", command=reset
    #
    # Gestalte sie wie in Projekt 1 und positioniere sie nebeneinander:
    #     button_start:  row=2, column=0, pady=10
    #     button_reset:  row=2, column=1, pady=10
    pass


# ---------------------------- COUNTDOWN-LOGIK ---------------------------- #

def start():
    """Startet den Countdown."""

    # TODO 6:
    # Verhindere, dass mehrere Countdowns gleichzeitig laufen:
    #
    # Deaktiviere dann den Start-Button:
    #
    #     button_start.config(state="disabled")
    #
    # Starte den Countdown:
    #
    pass


def countdown(sekunden):
    """Zeigt die Zeit an und ruft sich nach 1 Sekunde selbst wieder auf."""

    global timer

    # TODO 7:
    # a) Ist der Countdown bei 0 angekommen?
    #
    # b) Sonst: Zeit anzeigen
    #
    #
    # c) Und in einer Sekunde mit einer Sekunde weniger weitermachen.
    #    after() bekommt: Millisekunden, Funktion, Argument.
    pass


def reset():
    """Bricht den Countdown ab und setzt die Anzeige zurück."""

    global timer

    # TODO 8:
    # Falls ein Countdown läuft, brich ihn ab:
    #
    # Zeige wieder die Startzeit an und aktiviere den Start-Button:

    pass


# ---------------------------- SCHLIESSEN (fertig) ---------------------------- #

def schliessen():
    """Bricht einen laufenden Countdown ab und schließt Fenster 2."""

    global timer

    if timer is not None:
        window.after_cancel(timer)
        timer = None

    countdown_window.destroy()
    button_gruss.config(state="normal")


# ---------------------------- FENSTER 1: BEGRÜSSUNG (fertig) ---------------------------- #

def begruessen():
    """Liest den Namen, begrüßt und öffnet das Countdown-Fenster."""

    name = eingabe.get().strip()

    if name == "":
        label_ausgabe.config(text="Bitte gib einen Namen ein.")
        return

    label_ausgabe.config(text=f"Hallo, {name}!")
    button_gruss.config(state="disabled")

    countdown_fenster(name)


window = tk.Tk()
window.title("Begrüßung")
window.config(bg=FARBE_HINTERGRUND, padx=50, pady=30)

label_titel = tk.Label(
    window,
    text="Wie heißt du?",
    font=(FONT_NAME, 20),
    fg=FARBE_TEXT,
    bg=FARBE_HINTERGRUND
)
label_titel.grid(row=0, column=0)

eingabe = tk.Entry(
    window,
    font=(FONT_NAME, 16),
    width=20
)
eingabe.grid(row=1, column=0, pady=10)

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


# ---------------------------- START (fertig) ---------------------------- #

# Mac-Fix: Fenster in den Vordergrund holen
window.lift()
window.attributes("-topmost", True)
window.after(300, lambda: window.attributes("-topmost", False))

window.mainloop()


# ---------------------------- BONUS ---------------------------- #

# Bonus A: Lass die Startzeit im ersten Fenster eingeben
#          (zweites Entry-Feld für die Sekunden, mit int(...) umwandeln).
#
# Bonus B: Ändere die Farbe der Zeit auf rot, sobald nur noch
#          3 Sekunden übrig sind.
#          Hinweis: canvas.itemconfig(zahl_text, fill="red")
