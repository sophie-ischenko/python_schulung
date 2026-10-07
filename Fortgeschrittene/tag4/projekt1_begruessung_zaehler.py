"""
Projekt 1: Begrüßung + Klick-Zähler (Startdatei zum Bearbeiten)

Fenster 1 begrüßt dich mit deinem Namen.
Fenster 2 (öffnet sich nach der Begrüßung) zählt deine Klicks.

So arbeitest du:
    Das Skript führt dich durch Schritt 1 bis 7.
    In dieser Datei sind die Stellen markiert, an denen du den Code
    aus dem jeweiligen Schritt einfügst: ">>> SCHRITT 2 <<<" usw.

    Schritt 1 (das leere Fenster) ist schon fertig.
    Starte die Datei einmal, du solltest ein leeres beiges Fenster sehen.

Start:
    python3 projekt1_begruessung_zaehler.py
"""

import tkinter as tk


# ---------------------------- KONSTANTEN ---------------------------- #

FARBE_HINTERGRUND = "#f7f5dd"
FARBE_TEXT = "#e7305b"
FONT_NAME = "Courier"


# ---------------------------- VARIABLEN ---------------------------- #

# >>> SCHRITT 5 <<<
# Hier kommen die Variablen für den Zähler hin:
#     zaehler = 0
#     label_zahl = None


# ---------------------------- FENSTER 2: ZÄHLER ---------------------------- #

# >>> SCHRITT 5 <<<
# Hier kommen die drei Funktionen für das zweite Fenster hin:
#     erhoehen()
#     reset()
#     zaehler_fenster(name)
#
# Denk an global in den Funktionen, die eine Variable von außen ändern!


# ---------------------------- FENSTER 1: BEGRÜSSUNG ---------------------------- #

# >>> SCHRITT 4 <<<
# Hier kommt die Funktion begruessen() hin.
#
# Sie soll:
#     - den Namen aus dem Eingabefeld lesen (.get(), .strip())
#     - bei leerem Namen einen Hinweis zeigen und mit return enden
#     - sonst "Hallo, <Name>!" im label_ausgabe anzeigen
#
# >>> SCHRITT 6 <<<
# Ergänze am Ende von begruessen():
#     - den Button deaktivieren
#     - das zweite Fenster öffnen: zaehler_fenster(name)


window = tk.Tk()
window.title("Begrüßung")
window.config(bg=FARBE_HINTERGRUND, padx=50, pady=30)

# >>> SCHRITT 2 <<<
# Hier kommt das Label "label_titel" hin ("Wie heißt du?")
# inklusive grid(row=0, column=0).


# >>> SCHRITT 3 <<<
# Hier kommt das Eingabefeld "eingabe" hin
# inklusive grid(row=1, column=0, pady=10).


# >>> SCHRITT 4 <<<
# Hier kommen der Button "button_gruss" (command=begruessen)
# und das Label "label_ausgabe" hin.
#     button_gruss:   grid(row=2, column=0)
#     label_ausgabe:  grid(row=3, column=0, pady=10)


# ---------------------------- START ---------------------------- #


window.mainloop()
