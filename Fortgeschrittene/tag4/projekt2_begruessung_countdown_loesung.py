"""
Projekt 2: Begrüßung + Countdown (Musterlösung, inklusive Bonus B)

Start:
    python3 projekt2_begruessung_countdown_loesung.py
"""

import tkinter as tk


# ---------------------------- KONSTANTEN ---------------------------- #

START_SEKUNDEN = 10

FARBE_HINTERGRUND = "#f7f5dd"
FARBE_TEXT = "#e7305b"
FARBE_WARNUNG = "red"
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

    minuten = sekunden // 60
    rest = sekunden % 60
    return f"{minuten:02d}:{rest:02d}"


# ---------------------------- FENSTER 2: COUNTDOWN ---------------------------- #

def countdown_fenster(name):
    """Öffnet das zweite Fenster mit dem Countdown."""

    global countdown_window, canvas, zahl_text, button_start

    countdown_window = tk.Toplevel(window)
    countdown_window.title("Countdown")
    countdown_window.config(bg=FARBE_HINTERGRUND, padx=40, pady=30)
    countdown_window.protocol("WM_DELETE_WINDOW", schliessen)

    label_titel = tk.Label(
        countdown_window,
        text=f"Los geht's, {name}!",
        font=(FONT_NAME, 20),
        fg=FARBE_TEXT,
        bg=FARBE_HINTERGRUND
    )
    label_titel.grid(row=0, column=0, columnspan=2, pady=10)

    canvas = tk.Canvas(
        countdown_window,
        width=240,
        height=150,
        bg=FARBE_HINTERGRUND,
        highlightthickness=0
    )
    zahl_text = canvas.create_text(
        120,
        75,
        text=formatieren(START_SEKUNDEN),
        font=(FONT_NAME, 35, "bold"),
        fill=FARBE_TEXT
    )
    canvas.grid(row=1, column=0, columnspan=2)

    button_start = tk.Button(
        countdown_window,
        text="Start",
        font=(FONT_NAME, 18),
        fg=FARBE_TEXT,
        bg=FARBE_HINTERGRUND,
        activebackground=FARBE_HINTERGRUND,
        command=start
    )
    button_start.grid(row=2, column=0, pady=10)

    button_reset = tk.Button(
        countdown_window,
        text="Reset",
        font=(FONT_NAME, 18),
        fg=FARBE_TEXT,
        bg=FARBE_HINTERGRUND,
        activebackground=FARBE_HINTERGRUND,
        command=reset
    )
    button_reset.grid(row=2, column=1, pady=10)


# ---------------------------- COUNTDOWN-LOGIK ---------------------------- #

def start():
    """Startet den Countdown."""

    # Verhindert, dass mehrere Countdowns gleichzeitig laufen.
    if timer is not None:
        return

    button_start.config(state="disabled")

    countdown(START_SEKUNDEN)


def countdown(sekunden):
    """Zeigt die Zeit an und ruft sich nach 1 Sekunde selbst wieder auf."""

    global timer

    if sekunden == 0:
        canvas.itemconfig(zahl_text, text="Fertig!")
        timer = None
        button_start.config(state="normal")
        return

    canvas.itemconfig(zahl_text, text=formatieren(sekunden))

    # Bonus B: Warnfarbe bei den letzten 3 Sekunden
    if sekunden <= 3:
        canvas.itemconfig(zahl_text, fill=FARBE_WARNUNG)

    timer = window.after(1000, countdown, sekunden - 1)


def reset():
    """Bricht den Countdown ab und setzt die Anzeige zurück."""

    global timer

    if timer is not None:
        window.after_cancel(timer)
        timer = None

    canvas.itemconfig(
        zahl_text,
        text=formatieren(START_SEKUNDEN),
        fill=FARBE_TEXT
    )
    button_start.config(state="normal")


# ---------------------------- SCHLIESSEN ---------------------------- #

def schliessen():
    """Bricht einen laufenden Countdown ab und schließt Fenster 2."""

    global timer

    if timer is not None:
        window.after_cancel(timer)
        timer = None

    countdown_window.destroy()
    button_gruss.config(state="normal")


# ---------------------------- FENSTER 1: BEGRÜSSUNG ---------------------------- #

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


# ---------------------------- START ---------------------------- #

window.mainloop()
