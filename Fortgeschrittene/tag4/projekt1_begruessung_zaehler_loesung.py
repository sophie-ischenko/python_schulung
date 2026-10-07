"""
Projekt 1: Begrüßung + Klick-Zähler (fertiger Code zum Vergleich)

Fenster 1 begrüßt dich mit deinem Namen.
Fenster 2 (öffnet sich nach der Begrüßung) zählt deine Klicks.

Start:
    python3 projekt1_begruessung_zaehler_loesung.py
"""

import tkinter as tk


# ---------------------------- KONSTANTEN ---------------------------- #

FARBE_HINTERGRUND = "#f7f5dd"
FARBE_TEXT = "#e7305b"
FONT_NAME = "Courier"


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


# ---------------------------- FENSTER 1: BEGRÜSSUNG ---------------------------- #

def begruessen():
    """Liest den Namen, begrüßt und öffnet das Zähler-Fenster."""

    name = eingabe.get().strip()

    if name == "":
        label_ausgabe.config(text="Bitte gib einen Namen ein.")
        return

    label_ausgabe.config(text=f"Hallo, {name}!")
    button_gruss.config(state="disabled")

    zaehler_fenster(name)


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
