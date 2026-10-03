"""
Tag 4 – Aufgabe: Pomodoro-Timer

Baue einen einfachen Pomodoro-Timer mit Tkinter.

Der Timer soll:

- ein Fenster anzeigen
- ein Bild anzeigen
- die aktuelle Phase anzeigen
- eine Zeit anzeigen
- mit Start gestartet werden
- mit Reset zurückgesetzt werden
- automatisch herunterzählen
- zwischen Arbeits- und Pausenphasen wechseln
- nach einer Arbeitsphase ein Häkchen anzeigen
- verhindern, dass mehrere Timer gleichzeitig laufen
- beim Ende einer Phase ein zusätzliches Fenster öffnen

Start:
    python aufgaben.py
"""

import tkinter as tk
from pathlib import Path


# ---------------------------- KONSTANTEN ---------------------------- #

ARBEIT_MINUTEN = 25
KURZE_PAUSE_MINUTEN = 5
LANGE_PAUSE_MINUTEN = 20

FARBE_HINTERGRUND = "#f7f5dd"
FARBE_ARBEIT = "#e7305b"
FARBE_PAUSE = "#9bdeac"
FARBE_LANGE_PAUSE = "#e2979c"

FONT_NAME = "Courier"

# TODO:
# Bestimme den Ordner, in dem sich diese Python-Datei befindet.
#
# Hinweis:
#
#     Path(__file__).parent
#
# Damit kann das Bild später unabhängig vom aktuellen
# Terminal-Ordner gefunden werden.


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

    # TODO:
    # Setze phasen auf 0 zurück.
    #
    # Setze checkmark auf einen leeren String zurück.
    #
    # Falls ein Timer läuft, soll er mit
    #
    #     window.after_cancel(timer)
    #
    # abgebrochen werden.
    #
    # Hinweis:
    # timer kann am Anfang None sein.
    #
    # Prüfe deshalb zuerst:
    #
    #     if timer is not None:
    #
    # Setze timer danach wieder auf None.
    #
    # Setze die Timer-Anzeige wieder auf "00:00".
    #
    # Verwende dafür:
    #
    #     canvas.itemconfig(...)
    #
    # Setze die Überschrift wieder auf "Timer".
    #
    # Setze die Farbe wieder auf FARBE_PAUSE.
    #
    # Entferne die Häkchen.
    #
    # Aktiviere den Start-Button wieder.


# ---------------------------- TIMER STARTEN ---------------------------- #

def start_timer():
    """Startet die nächste Timer-Phase."""

    global phasen
    global checkmark

    # TODO:
    # Verhindere, dass mehrere Timer gleichzeitig gestartet werden.
    #
    # Wenn timer nicht None ist, soll die Funktion
    # sofort mit return beendet werden.
    #
    # Hinweis:
    #
    #     if timer is not None:
    #         return


    # TODO:
    # Erhöhe phasen um 1.


    # TODO:
    # Nach einer Arbeitsphase soll ein Häkchen angezeigt werden.
    #
    # Ab Phase 2 ist jede gerade Phase eine Pause.
    #
    # Wenn phasen größer als 1 UND durch 2 teilbar ist,
    # hänge "✓" an checkmark an.
    #
    # Hinweis:
    #
    #     phasen % 2 == 0


    # TODO:
    # Zeige checkmark im label_check an.
    #
    # Verwende:
    #
    #     label_check.config(...)


    # TODO:
    # Prüfe zuerst, ob phasen durch 8 teilbar ist.
    #
    # Wenn ja:
    #
    #     -> lange Pause
    #     -> Überschrift "Pause"
    #     -> Farbe FARBE_LANGE_PAUSE
    #     -> countdown(LANGE_PAUSE_MINUTEN * 60)
    #
    # Hinweis:
    # 60 Sekunden = 1 Minute.


    # TODO:
    # Wenn es keine lange Pause ist, prüfe,
    # ob phasen durch 2 teilbar ist.
    #
    # Wenn ja:
    #
    #     -> kurze Pause
    #     -> Überschrift "Pause"
    #     -> Farbe FARBE_PAUSE
    #     -> countdown(KURZE_PAUSE_MINUTEN * 60)


    # TODO:
    # Wenn keine der beiden Bedingungen zutrifft,
    # handelt es sich um eine Arbeitsphase.
    #
    #     -> Überschrift "Arbeit"
    #     -> Farbe FARBE_ARBEIT
    #     -> countdown(ARBEIT_MINUTEN * 60)


    # TODO:
    # Deaktiviere den Start-Button,
    # solange der Timer läuft.
    #
    # Verwende:
    #
    #     state="disabled"


# ---------------------------- COUNTDOWN ---------------------------- #

def countdown(verbleibende_sekunden):
    """Zählt die verbleibende Zeit herunter."""

    global timer

    # TODO:
    # Berechne aus den verbleibenden Sekunden
    # Minuten und Sekunden.
    #
    # Verwende:
    #
    #     minuten = verbleibende_sekunden // 60
    #     sekunden = verbleibende_sekunden % 60


    # TODO:
    # Erstelle die Anzeige als f-String.
    #
    # Sie soll immer zweistellig sein.
    #
    # Beispiel:
    #
    #     05:07
    #
    # Verwende:
    #
    #     f"{minuten:02d}:{sekunden:02d}"


    # TODO:
    # Aktualisiere damit den Text auf dem Canvas.
    #
    # Verwende:
    #
    #     canvas.itemconfig(
    #         timer_text,
    #         text=anzeige
    #     )


    # TODO:
    # Prüfe, ob die Zeit abgelaufen ist.
    #
    # Wenn verbleibende_sekunden 0 ist:
    #
    #     -> timer auf None setzen
    #     -> Start-Button wieder aktivieren
    #     -> info_fenster() aufrufen
    #     -> return
    #
    # Hinweis:
    # Die nächste Phase soll NICHT automatisch starten.
    # Der Benutzer entscheidet im Info-Fenster,
    # wann es weitergeht.


    # TODO:
    # Ziehe eine Sekunde ab.
    #
    # Danach soll countdown nach einer Sekunde
    # erneut aufgerufen werden.
    #
    # Verwende:
    #
    #     window.after(...)
    #
    # 1000 Millisekunden entsprechen 1 Sekunde.
    #
    # Speichere die Rückgabe von after() in timer.
    #
    # Beispiel:
    #
    #     timer = window.after(
    #         1000,
    #         countdown,
    #         verbleibende_sekunden
    #     )


# ---------------------------- INFO-FENSTER ---------------------------- #

def info_fenster():
    """Öffnet ein kleines Fenster nach Ende einer Phase."""

    # TODO:
    # Erstelle ein zusätzliches Fenster:
    #
    #     top = tk.Toplevel(window)


    # TODO:
    # Setze den Titel auf:
    #
    #     "Pomodoro"


    # TODO:
    # Setze die Hintergrundfarbe auf
    # FARBE_HINTERGRUND.
    #
    # Du kannst zusätzlich padx und pady verwenden.


    # TODO:
    # Erstelle ein Label mit:
    #
    #     "Zeit für die nächste Phase!"
    #
    # Verwende als Schriftgröße 16.


    # TODO:
    # Positioniere das Label mit grid().
    #
    # Verwende:
    #
    #     row=0
    #     column=0


    # TODO:
    # Erstelle einen Button.
    #
    # Text:
    #
    #     "Zurück zum Timer"
    #
    # Der Button soll das Fenster schließen
    # und anschließend die nächste Phase starten.
    #
    # Hinweis:
    # Dafür kannst du eine eigene Funktion
    # naechste_phase() verwenden.


    # TODO:
    # Positioniere den Button mit grid().
    #
    # Verwende:
    #
    #     row=1
    #     column=0


# ---------------------------- NÄCHSTE PHASE ---------------------------- #

def naechste_phase(fenster):
    """Schließt das Info-Fenster und startet die nächste Phase."""

    # TODO:
    # Schließe das übergebene Fenster.
    #
    # Verwende:
    #
    #     fenster.destroy()


    # TODO:
    # Starte anschließend die nächste Phase.
    #
    # Verwende:
    #
    #     start_timer()


# ---------------------------- HAUPTFENSTER ---------------------------- #

window = tk.Tk()

# TODO:
# Setze den Fenstertitel auf:
#
#     "Pomodoro"


# TODO:
# Konfiguriere das Fenster mit:
#
#     bg=FARBE_HINTERGRUND
#     padx=100
#     pady=50


# ---------------------------- CANVAS ---------------------------- #

canvas = tk.Canvas(
    window,
    width=200,
    height=224,
    bg=FARBE_HINTERGRUND,
    highlightthickness=0
)

# TODO:
# Lade das Bild mit PhotoImage.
#
# Verwende den zuvor erstellten Ordner:
#
#     ORDNER
#
# Der Pfad soll auf:
#
#     bilder/tomato.png
#
# zeigen.
#
# Hinweis:
#
#     ORDNER / "bilder" / "tomato.png"


# TODO:
# Zeige das Bild mit create_image().
#
# Die Mitte des Canvas liegt ungefähr bei:
#
#     x = 100
#     y = 112
#
# Speichere das Bild NICHT in einer lokalen Variable
# innerhalb einer Funktion.
#
# Das Bild wird später für das gesamte Programm benötigt.


# TODO:
# Erstelle anschließend den Timer-Text
# mit create_text().
#
# Speichere die zurückgegebene ID in:
#
#     timer_text
#
# Der Starttext soll sein:
#
#     "00:00"
#
# Verwende:
#
#     fill="white"
#
# und eine große Schrift.


# TODO:
# Positioniere das Canvas mit grid().
#
# Verwende:
#
#     row=2
#     column=2


# ---------------------------- ÜBERSCHRIFT ---------------------------- #

label_top = tk.Label(
    window,
    text="Timer",
    font=(FONT_NAME, 40),
    fg=FARBE_PAUSE,
    bg=FARBE_HINTERGRUND
)

# TODO:
# Positioniere label_top.
#
# Verwende:
#
#     row=1
#     column=2
#
# Du kannst zusätzlich pady verwenden.


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

# TODO:
# Positioniere button_start.
#
# Verwende:
#
#     row=3
#     column=1


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

# TODO:
# Positioniere button_reset.
#
# Verwende:
#
#     row=3
#     column=3


# ---------------------------- HÄKCHEN ---------------------------- #

label_check = tk.Label(
    window,
    text="",
    font=(FONT_NAME, 30),
    fg=FARBE_PAUSE,
    bg=FARBE_HINTERGRUND
)

# TODO:
# Positioniere label_check.
#
# Verwende:
#
#     row=4
#     column=2
#
# Du kannst zusätzlich pady verwenden.


# ---------------------------- START ---------------------------- #

# TODO:
# Starte die Tkinter-Ereignisschleife.
#
# Verwende:
#
#     window.mainloop()