
"""
Tag 4 – Lösung: Pomodoro-Timer

Start:
    python aufgaben_loesung.py
"""

import tkinter as tk
from pathlib import Path


# ---------------------------- KONSTANTEN ---------------------------- #

ARBEIT_MINUTEN = 1
KURZE_PAUSE_MINUTEN = 1
LANGE_PAUSE_MINUTEN = 2

FARBE_HINTERGRUND = "#f7f5dd"
FARBE_ARBEIT = "#e7305b"
FARBE_PAUSE = "#9bdeac"
FARBE_LANGE_PAUSE = "#e2979c"

FONT_NAME = "Courier"
ORDNER = Path(__file__).parent


# ---------------------------- VARIABLEN ---------------------------- #

timer = None
phasen = 0
checkmark = ""


# ---------------------------- TIMER ZURÜCKSETZEN ---------------------------- #

def reset():
    """Setzt den Timer vollständig zurück."""

    global timer
    global phasen
    global checkmark

    phasen = 0
    checkmark = ""

    if timer is not None:
        window.after_cancel(timer)
        timer = None

    canvas.itemconfig(
        timer_text,
        text="00:00"
    )

    label_top.config(
        text="Timer",
        fg=FARBE_PAUSE
    )

    label_check.config(
        text=""
    )

    button_start.config(
        state="normal"
    )


# ---------------------------- TIMER STARTEN ---------------------------- #

def start_timer():
    """Startet die nächste Timer-Phase."""

    global phasen
    global checkmark

    # Verhindert, dass mehrere Timer gleichzeitig laufen.
    if timer is not None:
        return

    phasen += 1

    # Nach einer Arbeitsphase ein Häkchen anzeigen.
    if phasen > 1 and phasen % 2 == 0:
        checkmark += "✓"

    label_check.config(
        text=checkmark
    )

    # Jede 8. Phase ist eine lange Pause.
    if phasen % 8 == 0:

        label_top.config(
            text="Pause",
            fg=FARBE_LANGE_PAUSE
        )

        countdown(
            LANGE_PAUSE_MINUTEN * 60
        )

    # Gerade Phasen sind kurze Pausen.
    elif phasen % 2 == 0:

        label_top.config(
            text="Pause",
            fg=FARBE_PAUSE
        )

        countdown(
            KURZE_PAUSE_MINUTEN * 60
        )

    # Ungerade Phasen sind Arbeitsphasen.
    else:

        label_top.config(
            text="Arbeit",
            fg=FARBE_ARBEIT
        )

        countdown(
            ARBEIT_MINUTEN * 60
        )

    # Start-Button deaktivieren.
    button_start.config(
        state="disabled"
    )


# ---------------------------- COUNTDOWN ---------------------------- #

def countdown(verbleibende_sekunden):
    """Zählt die verbleibende Zeit herunter."""

    global timer

    # Minuten und Sekunden berechnen.
    minuten = verbleibende_sekunden // 60
    sekunden = verbleibende_sekunden % 60

    # Zeit anzeigen.
    anzeige = f"{minuten:02d}:{sekunden:02d}"

    canvas.itemconfig(
        timer_text,
        text=anzeige
    )

    # Timer ist fertig.
    if verbleibende_sekunden == 0:

        timer = None

        button_start.config(
            state="normal"
        )

        info_fenster()

        return

    # Eine Sekunde abziehen.
    verbleibende_sekunden -= 1

    # Nach einer Sekunde erneut aufrufen.
    timer = window.after(
        1000,
        countdown,
        verbleibende_sekunden
    )


# ---------------------------- INFO-FENSTER ---------------------------- #

def info_fenster():
    """Öffnet ein kleines Fenster nach Ende einer Phase."""

    top = tk.Toplevel(window)

    top.title("Pomodoro")

    top.config(
        bg=FARBE_HINTERGRUND,
        padx=30,
        pady=30
    )

    label = tk.Label(
        top,
        text="Zeit für die nächste Phase!",
        font=(FONT_NAME, 16),
        fg="#241914",
        bg=FARBE_HINTERGRUND
    )

    label.grid(
        row=0,
        column=0,
        pady=10
    )

    button = tk.Label(
        top,
        text="Zurück zum Timer",
        font=(FONT_NAME, 12),
        fg="#241914",
        bg=FARBE_HINTERGRUND,
        padx=15,
        pady=10,
        cursor="hand2"
    )

    button.grid(
        row=1,
        column=0,
        pady=10
    )

    button.bind(
        "<Button-1>",
        lambda event: naechste_phase(top)
    )

# ---------------------------- NÄCHSTE PHASE ---------------------------- #

def naechste_phase(fenster):
    """Schließt das Info-Fenster und startet die nächste Phase."""

    fenster.destroy()

    start_timer()


# ---------------------------- HAUPTFENSTER ---------------------------- #

window = tk.Tk()

window.title("Pomodoro")

window.config(
    bg=FARBE_HINTERGRUND,
    padx=100,
    pady=50
)


# ---------------------------- CANVAS ---------------------------- #

canvas = tk.Canvas(
    window,
    width=200,
    height=224,
    bg=FARBE_HINTERGRUND,
    highlightthickness=0
)

tomato_img = tk.PhotoImage(
    file=ORDNER / "bilder" / "tomato.png"
)

canvas.create_image(
    100,
    112,
    image=tomato_img
)

timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)

canvas.grid(
    row=2,
    column=2
)


# ---------------------------- ÜBERSCHRIFT ---------------------------- #

label_top = tk.Label(
    window,
    text="Timer",
    font=(FONT_NAME, 40),
    fg=FARBE_PAUSE,
    bg=FARBE_HINTERGRUND
)

label_top.grid(
    row=1,
    column=2,
    pady=10
)


# ---------------------------- START-BUTTON ---------------------------- #

button_start = tk.Button(
    window,
    text="Start",
    font=(FONT_NAME, 18),
    fg=FARBE_ARBEIT,
    bg=FARBE_HINTERGRUND,
    activebackground=FARBE_HINTERGRUND,
    command=start_timer
)

button_start.grid(
    row=3,
    column=1
)


# ---------------------------- RESET-BUTTON ---------------------------- #

button_reset = tk.Button(
    window,
    text="Reset",
    font=(FONT_NAME, 18),
    fg=FARBE_ARBEIT,
    bg=FARBE_HINTERGRUND,
    activebackground=FARBE_HINTERGRUND,
    command=reset
)

button_reset.grid(
    row=3,
    column=3
)


# ---------------------------- HÄKCHEN ---------------------------- #

label_check = tk.Label(
    window,
    text="",
    font=(FONT_NAME, 30),
    fg=FARBE_PAUSE,
    bg=FARBE_HINTERGRUND
)

label_check.grid(
    row=4,
    column=2,
    pady=10
)


# ---------------------------- START ---------------------------- #

window.mainloop()
