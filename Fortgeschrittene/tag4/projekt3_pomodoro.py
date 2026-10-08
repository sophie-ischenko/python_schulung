"""
Projekt 3: Pomodoro-Timer

Der Rahmen (Fenster, Canvas, Bild, Labels, Buttons) steht schon.
Deine Aufgabe sind die Funktionen:

STUFE 1 (Pflicht):
    reset()        -> alles zurücksetzen
    start_timer()  -> nächste Phase bestimmen und starten
    countdown()    -> herunterzählen

STUFE 2 (Bonus):
    info_fenster()   -> zusätzliches Fenster am Ende einer Phase
    naechste_phase() -> Fenster schließen und weitermachen

Der Timer soll:

- mit Start gestartet und mit Reset zurückgesetzt werden
- automatisch herunterzählen
- zwischen Arbeits- und Pausenphasen wechseln
- nach einer Arbeitsphase ein Häkchen anzeigen
- verhindern, dass mehrere Timer gleichzeitig laufen

Start:
    python3 projekt3_pomodoro.py

Wichtig: Der Ordner "bilder" mit tomato.png muss neben dieser
Datei liegen.
"""

import tkinter as tk
from pathlib import Path


# ---------------------------- KONSTANTEN ---------------------------- #

# Zum Testen sind kurze Zeiten eingestellt.
# Die echten Pomodoro-Werte wären 25 / 5 / 20.
ARBEIT_MINUTEN = 1          # echt: 25
KURZE_PAUSE_MINUTEN = 1     # echt: 5
LANGE_PAUSE_MINUTEN = 2     # echt: 20

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


# ---------------------------- STUFE 1: RESET ---------------------------- #

def reset():
    """Setzt den Timer vollständig zurück."""

    global timer
    global phasen
    global checkmark

    # TODO 1:
    # Setze phasen auf 0 und checkmark auf "" zurück.


    # TODO 2:
    # Falls ein Timer läuft, breche ihn ab.
    #


    # TODO 3:
    # Setze die Anzeige zurück:
    #


# ---------------------------- STUFE 1: TIMER STARTEN ---------------------------- #

def start_timer():
    """Startet die nächste Timer-Phase."""

    global phasen
    global checkmark

    # TODO 4:
    # Verhindere, dass mehrere Timer gleichzeitig laufen.
    #


    # TODO 5:
    # Erhöhe phasen um 1.


    # TODO 6:
    # Nach einer Arbeitsphase soll ein Häkchen erscheinen.
    # Jede gerade Phase (ab Phase 2) kommt NACH einer Arbeitsphase.
    #
    #     if phasen > 1 and phasen % 2 == 0:
    #         checkmark += "✓"
    #
    # Zeige das Häkchen dann an:
    #


    # TODO 7:
    # Bestimme die Phase. Die Reihenfolge ist wichtig:
    # der speziellste Fall (durch 8 teilbar) steht oben!
    #


    # TODO 8:
    # Deaktiviere den Start-Button, solange der Timer läuft.
    #


# ---------------------------- STUFE 1: COUNTDOWN ---------------------------- #

def countdown(verbleibende_sekunden):
    """Zählt die verbleibende Zeit herunter."""

    global timer

    # TODO 9:
    # Rechne die Sekunden in Minuten und Sekunden um
    # und zeige sie zweistellig auf dem Canvas an.
    #


    # TODO 10:
    # Wenn die Zeit abgelaufen ist (verbleibende_sekunden == 0):
    #
    # In Stufe 1 wartet der Timer jetzt, bis du erneut auf Start klickst.
    # In Stufe 2 rufst du vor dem return noch info_fenster() auf.


    # TODO 11:
    # Ziehe eine Sekunde ab und rufe countdown nach 1 Sekunde erneut auf.
    # Speichere die Rückgabe von after() in timer.
    #

# ---------------------------- STUFE 2: INFO-FENSTER ---------------------------- #

def info_fenster():
    """Öffnet ein kleines Fenster nach Ende einer Phase."""

    # TODO 12 (Bonus):
    # Erstelle ein zusätzliches Fenster:
    #
    #
    # Darin ein Label "Zeit für die nächste Phase!" (Schriftgröße 16),
    # positioniert mit grid(row=0, column=0, pady=10).


    # TODO 13 (Bonus):
    # Erstelle einen Button "Zurück zum Timer" in diesem Fenster,
    # der naechste_phase(top) aufruft.
    #
    # Achtung: naechste_phase braucht einen Wert (top).
    # Deshalb brauchst du lambda:
    #
    #     command=lambda: naechste_phase(top)
    #
    # Positioniere ihn mit grid(row=1, column=0, pady=10).


def naechste_phase(fenster):
    """Schließt das Info-Fenster und startet die nächste Phase."""

    # TODO 14 (Bonus):
    # Schließe das Fenster mit fenster.destroy()
    # und starte danach start_timer().


# ---------------------------- HAUPTFENSTER (fertig) ---------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(bg=FARBE_HINTERGRUND, padx=100, pady=50)


# ---------------------------- CANVAS (fertig) ---------------------------- #

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

canvas.grid(row=2, column=2)


# ---------------------------- ÜBERSCHRIFT (fertig) ---------------------------- #

label_top = tk.Label(
    window,
    text="Timer",
    font=(FONT_NAME, 40),
    fg=FARBE_PAUSE,
    bg=FARBE_HINTERGRUND
)
label_top.grid(row=1, column=2, pady=10)


# ---------------------------- BUTTONS (fertig) ---------------------------- #

button_start = tk.Button(
    window,
    text="Start",
    font=(FONT_NAME, 18),
    fg=FARBE_ARBEIT,
    bg=FARBE_HINTERGRUND,
    activebackground=FARBE_HINTERGRUND,
    command=start_timer
)
button_start.grid(row=3, column=1)

button_reset = tk.Button(
    window,
    text="Reset",
    font=(FONT_NAME, 18),
    fg=FARBE_ARBEIT,
    bg=FARBE_HINTERGRUND,
    activebackground=FARBE_HINTERGRUND,
    command=reset
)
button_reset.grid(row=3, column=3)


# ---------------------------- HÄKCHEN (fertig) ---------------------------- #

label_check = tk.Label(
    window,
    text="",
    font=(FONT_NAME, 30),
    fg=FARBE_PAUSE,
    bg=FARBE_HINTERGRUND
)
label_check.grid(row=4, column=2, pady=10)


# ---------------------------- START (fertig) ---------------------------- #

window.mainloop()
