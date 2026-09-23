"""
TAG 5 - DUNGEON DUEL
Code-Begleitdatei zum Notebook "Tag 5 - Die grafische Oberflaeche (GUI) mit tkinter"

Enthaelt: Theorie-Beispiele (5.1-5.3) und Uebungs-Starter mit TODOs.
Die finale Praxis-Anwendung steht separat in "gui.py".
"""

import tkinter as tk


# =============================================================
# 5.1 BEISPIEL: tkinter Grundlagen
# =============================================================

def angreifen_demo():
    """Reagiert auf einen Klick auf den Demo-Button. Kein Parameter, keine Rueckgabe."""
    print("Du greifst an!")


# Zum Ausprobieren einkommentieren:
# fenster_demo = tk.Tk()
# fenster_demo.title("Dungeon Duel - Demo")
# tk.Button(fenster_demo, text="Angriff!", command=angreifen_demo).pack(pady=20)
# fenster_demo.mainloop()


# =============================================================
# UEBUNG 1: Der digitale Klickzaehler (35 Min)
# Lernziel: Fenster, Label und Button verknuepfen
# =============================================================

# klicks = 0
#
# def erhoehe_klicks():
#     TODO: global klicks
#     TODO: klicks um 1 erhoehen
#     TODO: label.config(text=f"Klicks: {klicks}")
#
# fenster1 = tk.Tk()
# label = tk.Label(fenster1, text="Klicks: 0")
# label.pack()
# button = tk.Button(fenster1, text="Klick mich", command=erhoehe_klicks)
# button.pack()
# fenster1.mainloop()


# =============================================================
# 5.2 BEISPIEL: Entry & Event-Handling
# =============================================================

# def verarbeite_eingabe():
#     """
#     Liest den Heldennamen aus dem Eingabefeld und zeigt ihn im Label an.
#     Kein Parameter (Callback), keine Rueckgabe.
#     """
#     text = eingabefeld.get()
#     ausgabe_label.config(text=f"Heldenname: {text}")
#
# fenster2 = tk.Tk()
# eingabefeld = tk.Entry(fenster2)
# eingabefeld.pack(pady=10)
# tk.Button(fenster2, text="Bestaetigen", command=verarbeite_eingabe).pack()
# ausgabe_label = tk.Label(fenster2, text="")
# ausgabe_label.pack(pady=10)
# fenster2.mainloop()


# =============================================================
# UEBUNG 2: Der GUI-Taschenrechner (40 Min)
# Lernziel: Eingabefelder auslesen und mit try/except verarbeiten
# =============================================================

# def addieren():
#     TODO: Werte aus entry_a und entry_b mit int() umwandeln (try/except!)
#     TODO: Summe berechnen, in ergebnis_label anzeigen
#
# def zuruecksetzen():
#     TODO: entry_a.delete(0, tk.END)
#     TODO: entry_b.delete(0, tk.END)
#     TODO: ergebnis_label.config(text="")
#
# fenster3 = tk.Tk()
# entry_a = tk.Entry(fenster3)
# entry_a.pack()
# entry_b = tk.Entry(fenster3)
# entry_b.pack()
# tk.Button(fenster3, text="Addieren", command=addieren).pack()
# tk.Button(fenster3, text="Zuruecksetzen", command=zuruecksetzen).pack()
# ergebnis_label = tk.Label(fenster3, text="")
# ergebnis_label.pack()
# fenster3.mainloop()


# =============================================================
# 5.3 BEISPIEL: Zustand in der GUI
# =============================================================

def zeige_bestenliste(eintraege):
    """
    Oeffnet ein Zusatzfenster mit der Heldenbestenliste.

    Parameter:
        eintraege (list[tuple]): z.B. [("Aria", 5), ("Finn", 4)]

    Rueckgabewert:
        None
    """
    fenster_top5 = tk.Toplevel()
    fenster_top5.title("Heldenbestenliste")
    for platz, (name, level) in enumerate(eintraege, start=1):
        tk.Label(fenster_top5, text=f"{platz}. {name} - Level {level}").pack()


# zeige_bestenliste([("Aria", 5), ("Finn", 4), ("Tom", 2)])   # Testaufruf (braucht laufendes tk-Fenster)


# =============================================================
# UEBUNG 3: Die Ampel-Simulation (30 Min)
# Lernziel: Globalen Zustand ueber mehrere Klicks verwalten
# =============================================================

# ampel_zustaende = ["Rot", "Gelb", "Gruen"]
# ampel_index = 0
#
# def naechste_farbe():
#     TODO: global ampel_index
#     TODO: ampel_index um 1 erhoehen, bei Erreichen des Listenendes wieder auf 0 (Modulo!)
#     TODO: ampel_label.config(text=ampel_zustaende[ampel_index])
#
# fenster4 = tk.Tk()
# ampel_label = tk.Label(fenster4, text="Rot", font=("Arial", 40))
# ampel_label.pack()
# tk.Button(fenster4, text="Weiter", command=naechste_farbe).pack()
# fenster4.mainloop()


# =============================================================
# HINWEIS ZUR PRAXIS
# =============================================================
# Die fertige GUI-Anwendung fuer Dungeon Duel steht in der separaten
# Datei "gui.py" - sie importiert db.py und game.py aus Tag 4
# unveraendert. Nutzt sie als Ausgangspunkt fuer die Gruppenarbeit.
