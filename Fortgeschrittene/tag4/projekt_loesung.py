import json
import random
import tkinter as tk
from pathlib import Path


# ============================================================
# DATEI, LISTEN UND FARBEN
# ============================================================

DATEI = Path(__file__).parent / "kreaturen.json"

HINTERGRUND = "#F6F0E7"
TEXT = "#222222"
KARTE = "white"
AKZENT = "#DEE047"

TYP_FARBEN = {
    "Alle": "#DEE047",
    "Feuer": "#F4A261",
    "Wasser": "#8ECAE6",
    "Wald": "#A7D68F",
    "Schatten": "#C3B1E1",
    "Eis": "#CDEFF7"
}

TYPEN = ["Alle", "Feuer", "Wasser", "Wald", "Schatten", "Eis"]

STAT_FARBEN = {
    "staerke": "#E4572E",
    "tempo": "#29A3A3",
    "magie": "#7B5EA7"
}

SPALTEN = 4


# ============================================================
# GLOBALE VARIABLEN
# ============================================================

window = None
daten = None

sichtbare = []
karten = []
aktuelle = None
aktueller_typ = "Alle"

suche_eingabe = None
zaehler_label = None
ergebnis_rahmen = None

kopf_rahmen = None
name_label = None
typ_label = None
text_label = None
staerke_label = None
tempo_label = None
magie_label = None
gesamt_canvas = None
gesamt_text = None

fortschritt = 0
animation_timer = None


# ============================================================
# JSON LADEN
# ============================================================

def daten_laden(pfad):
    with open(pfad, encoding="utf-8") as datei:
        daten = json.load(datei)

    for kreatur in daten["kreaturen"]:
        kreatur["gesamt"] = (
            kreatur["staerke"] + kreatur["tempo"] + kreatur["magie"]
        )

    return daten


# ============================================================
# HILFSFUNKTIONEN (fertig)
# ============================================================

def kreaturen_filtern(suchtext, typ):
    treffer = []

    for kreatur in daten["kreaturen"]:
        passt_name = suchtext.lower() in kreatur["name"].lower()
        passt_typ = typ == "Alle" or kreatur["typ"] == typ

        if passt_name and passt_typ:
            treffer.append(kreatur)

    return treffer


def balken_text(bezeichnung, wert):
    balken = "█" * (wert // 4)

    return f"{bezeichnung:<7}{balken} {wert}"


# ============================================================
# OBERFLÄCHE
# ============================================================

def oberflaeche_bauen(fenster):
    global suche_eingabe
    global zaehler_label
    global ergebnis_rahmen
    global kopf_rahmen
    global name_label
    global typ_label
    global text_label
    global staerke_label
    global tempo_label
    global magie_label
    global gesamt_canvas
    global gesamt_text

    fenster.config(
        bg=HINTERGRUND,
        padx=30,
        pady=20
    )

    # --------------------------------------------------------
    # AUFGABE 1: Titel und Untertitel
    # --------------------------------------------------------

    titel = tk.Label(
        fenster,
        text=daten["titel"],
        font=("Arial", 28, "bold"),
        bg=AKZENT,
        fg=TEXT,
        padx=25,
        pady=8
    )

    titel.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=(0, 5)
    )

    untertitel = tk.Label(
        fenster,
        text=daten["untertitel"],
        font=("Arial", 13),
        bg=HINTERGRUND,
        fg=TEXT
    )

    untertitel.grid(
        row=1,
        column=0,
        columnspan=2,
        pady=(0, 20)
    )

    # --------------------------------------------------------
    # AUFGABE 2: Linke und rechte Seite
    # --------------------------------------------------------

    links = tk.Frame(fenster, bg=HINTERGRUND)

    links.grid(
        row=2,
        column=0,
        sticky="n",
        padx=(0, 30)
    )

    rechts = tk.Frame(fenster, bg=HINTERGRUND)

    rechts.grid(
        row=2,
        column=1,
        sticky="n"
    )

    # --------------------------------------------------------
    # AUFGABE 3: Suchzeile
    # --------------------------------------------------------

    such_rahmen = tk.Frame(links, bg=HINTERGRUND)

    such_rahmen.grid(
        row=0,
        column=0,
        sticky="w",
        pady=(0, 10)
    )

    suche_eingabe = tk.Entry(
        such_rahmen,
        font=("Arial", 13),
        bg="white",
        fg=TEXT,
        insertbackground=TEXT,
        width=16
    )

    suche_eingabe.grid(
        row=0,
        column=0,
        padx=(0, 8)
    )

    button_suchen = tk.Button(
        such_rahmen,
        text="Suchen",
        command=suchen
    )

    button_suchen.grid(
        row=0,
        column=1,
        padx=(0, 8)
    )

    button_reset = tk.Button(
        such_rahmen,
        text="Zurücksetzen",
        command=zuruecksetzen
    )

    button_reset.grid(
        row=0,
        column=2
    )

    # --------------------------------------------------------
    # AUFGABE 4: Typ-Buttons mit einer Schleife
    # --------------------------------------------------------

    typ_rahmen = tk.Frame(links, bg=HINTERGRUND)

    typ_rahmen.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(0, 10)
    )

    spalte = 0

    for typ in TYPEN:
        farb_rahmen = tk.Frame(
            typ_rahmen,
            bg=TYP_FARBEN[typ],
            padx=4,
            pady=4
        )

        farb_rahmen.grid(
            row=0,
            column=spalte,
            padx=(0, 6)
        )

        button = tk.Button(
            farb_rahmen,
            text=typ,
            command=lambda t=typ: typ_waehlen(t)
        )

        button.grid(
            row=0,
            column=0
        )

        spalte += 1

    # --------------------------------------------------------
    # AUFGABE 5: Zähler und Ergebnis-Rahmen
    # --------------------------------------------------------

    zaehler_label = tk.Label(
        links,
        text="",
        font=("Arial", 11),
        bg=HINTERGRUND,
        fg=TEXT
    )

    zaehler_label.grid(
        row=2,
        column=0,
        sticky="w",
        pady=(0, 5)
    )

    ergebnis_rahmen = tk.Frame(links, bg=HINTERGRUND)

    ergebnis_rahmen.grid(
        row=3,
        column=0,
        sticky="w"
    )

    # --------------------------------------------------------
    # AUFGABE 8: Detailkarte
    # --------------------------------------------------------

    detail_rahmen = tk.Frame(
        rechts,
        bg=KARTE,
        padx=25,
        pady=20
    )

    detail_rahmen.grid(
        row=0,
        column=0,
        sticky="w"
    )

    kopf_rahmen = tk.Frame(
        detail_rahmen,
        bg=AKZENT,
        padx=15,
        pady=10
    )

    kopf_rahmen.grid(
        row=0,
        column=0,
        sticky="ew",
        pady=(0, 12)
    )

    name_label = tk.Label(
        kopf_rahmen,
        text="Wähle eine Kreatur",
        font=("Arial", 24, "bold"),
        bg=AKZENT,
        fg=TEXT
    )

    name_label.grid(
        row=0,
        column=0,
        sticky="w"
    )

    typ_label = tk.Label(
        kopf_rahmen,
        text="",
        font=("Arial", 11, "bold"),
        bg="white",
        fg=TEXT
    )

    typ_label.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(4, 0)
    )

    text_label = tk.Label(
        detail_rahmen,
        text="",
        font=("Arial", 12),
        bg=KARTE,
        fg=TEXT,
        wraplength=380,
        justify="left"
    )

    text_label.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(0, 10)
    )

    staerke_label = tk.Label(
        detail_rahmen,
        text="",
        font=("Courier", 14, "bold"),
        bg=KARTE,
        fg=STAT_FARBEN["staerke"]
    )

    staerke_label.grid(
        row=2,
        column=0,
        sticky="w"
    )

    tempo_label = tk.Label(
        detail_rahmen,
        text="",
        font=("Courier", 14, "bold"),
        bg=KARTE,
        fg=STAT_FARBEN["tempo"]
    )

    tempo_label.grid(
        row=3,
        column=0,
        sticky="w"
    )

    magie_label = tk.Label(
        detail_rahmen,
        text="",
        font=("Courier", 14, "bold"),
        bg=KARTE,
        fg=STAT_FARBEN["magie"]
    )

    magie_label.grid(
        row=4,
        column=0,
        sticky="w"
    )

    gesamt_canvas = tk.Canvas(
        detail_rahmen,
        width=220,
        height=55,
        bg=KARTE,
        highlightthickness=0
    )

    gesamt_canvas.grid(
        row=5,
        column=0,
        sticky="w",
        pady=(10, 0)
    )

    gesamt_canvas.create_text(
        5,
        28,
        text="Gesamt",
        anchor="w",
        font=("Arial", 12, "bold"),
        fill=TEXT
    )

    gesamt_text = gesamt_canvas.create_text(
        85,
        28,
        text="0",
        anchor="w",
        font=("Arial", 30, "bold"),
        fill="#E4572E"
    )

    # --------------------------------------------------------
    # AUFGABE 10: Aktions-Buttons
    # --------------------------------------------------------

    aktions_rahmen = tk.Frame(rechts, bg=HINTERGRUND)

    aktions_rahmen.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(15, 0)
    )

    button_zufall = tk.Button(
        aktions_rahmen,
        text="Zufällige Kreatur",
        command=zufaellige_kreatur
    )

    button_zufall.grid(
        row=0,
        column=0,
        padx=(0, 8)
    )

    button_staerkste = tk.Button(
        aktions_rahmen,
        text="Stärkste zeigen",
        command=staerkste_zeigen
    )

    button_staerkste.grid(
        row=0,
        column=1,
        padx=(0, 8)
    )

    button_duell = tk.Button(
        aktions_rahmen,
        text="Duell starten",
        command=duell_starten
    )

    button_duell.grid(
        row=0,
        column=2
    )


# ============================================================
# ERGEBNISSE ANZEIGEN
# ============================================================

def ergebnisse_aktualisieren():
    global sichtbare
    global karten

    # --------------------------------------------------------
    # AUFGABE 6a: Treffer holen und zählen
    # --------------------------------------------------------

    sichtbare = kreaturen_filtern(
        suche_eingabe.get(),
        aktueller_typ
    )

    zaehler_label.config(
        text=str(len(sichtbare)) + " von "
        + str(len(daten["kreaturen"])) + " Kreaturen"
    )

    # --------------------------------------------------------
    # AUFGABE 6b: Alte Buttons löschen
    # --------------------------------------------------------

    for karte in karten:
        karte.destroy()

    karten = []

    # --------------------------------------------------------
    # AUFGABE 6c: Neue Buttons erzeugen
    # --------------------------------------------------------

    zeile = 0
    spalte = 0

    for kreatur in sichtbare:
        farb_rahmen = tk.Frame(
            ergebnis_rahmen,
            bg=TYP_FARBEN[kreatur["typ"]],
            padx=4,
            pady=4
        )

        farb_rahmen.grid(
            row=zeile,
            column=spalte,
            padx=4,
            pady=4
        )

        button = tk.Button(
            farb_rahmen,
            text=kreatur["name"] + "\n" + kreatur["typ"],
            width=13,
            height=2,
            command=lambda k=kreatur: detail_zeigen(k)
        )

        button.grid(
            row=0,
            column=0
        )

        karten.append(farb_rahmen)

        spalte += 1

        if spalte == SPALTEN:
            spalte = 0
            zeile += 1


# ============================================================
# AUFGABE 7: Suchen, Zurücksetzen, Typ wählen
# ============================================================

def suchen():
    ergebnisse_aktualisieren()


def zuruecksetzen():
    global aktueller_typ

    aktueller_typ = "Alle"

    suche_eingabe.delete(0, tk.END)

    ergebnisse_aktualisieren()


def typ_waehlen(typ):
    global aktueller_typ

    aktueller_typ = typ

    ergebnisse_aktualisieren()


# ============================================================
# AUFGABE 9: Details anzeigen und animieren
# ============================================================

def detail_zeigen(kreatur):
    global aktuelle
    global fortschritt
    global animation_timer

    aktuelle = kreatur

    farbe = TYP_FARBEN[kreatur["typ"]]

    kopf_rahmen.config(bg=farbe)

    name_label.config(
        text=kreatur["name"],
        bg=farbe
    )

    typ_label.config(text="  " + kreatur["typ"] + "  ")

    text_label.config(text=kreatur["beschreibung"])

    # Läuft noch eine Animation? Dann abbrechen.
    if animation_timer is not None:
        window.after_cancel(animation_timer)

    fortschritt = 0

    animation_schritt()


def animation_schritt():
    global fortschritt
    global animation_timer

    fortschritt += 4

    if fortschritt > 100:
        fortschritt = 100

    staerke = int(aktuelle["staerke"] * fortschritt / 100)
    tempo = int(aktuelle["tempo"] * fortschritt / 100)
    magie = int(aktuelle["magie"] * fortschritt / 100)
    gesamt = int(aktuelle["gesamt"] * fortschritt / 100)

    staerke_label.config(text=balken_text("Stärke", staerke))
    tempo_label.config(text=balken_text("Tempo", tempo))
    magie_label.config(text=balken_text("Magie", magie))

    gesamt_canvas.itemconfig(gesamt_text, text=str(gesamt))

    if fortschritt < 100:
        animation_timer = window.after(20, animation_schritt)
    else:
        animation_timer = None


# ============================================================
# AUFGABE 10: Zufall und Stärkste
# ============================================================

def zufaellige_kreatur():
    if len(sichtbare) == 0:
        return

    index = random.randint(0, len(sichtbare) - 1)

    detail_zeigen(sichtbare[index])


def staerkste_zeigen():
    if len(sichtbare) == 0:
        return

    beste = sichtbare[0]

    for kreatur in sichtbare:
        if kreatur["gesamt"] > beste["gesamt"]:
            beste = kreatur

    detail_zeigen(beste)


# ============================================================
# AUFGABE 11: Duell
# ============================================================

def duell_starten():
    if aktuelle is None:
        return

    # Gegner: eine zufällige andere Kreatur
    gegner = aktuelle

    while gegner == aktuelle:
        gegner = random.choice(daten["kreaturen"])

    punkte_a = aktuelle["gesamt"] + random.randint(0, 60)
    punkte_b = gegner["gesamt"] + random.randint(0, 60)

    if punkte_a > punkte_b:
        ergebnis = aktuelle["name"] + " gewinnt!"
    elif punkte_b > punkte_a:
        ergebnis = gegner["name"] + " gewinnt!"
    else:
        ergebnis = "Unentschieden!"

    top = tk.Toplevel(window)

    top.title("Duell")

    top.config(
        bg=HINTERGRUND,
        padx=40,
        pady=30
    )

    namen = tk.Label(
        top,
        text=aktuelle["name"] + "  gegen  " + gegner["name"],
        font=("Arial", 20, "bold"),
        bg=HINTERGRUND,
        fg=TEXT
    )

    namen.grid(
        row=0,
        column=0,
        pady=(0, 15)
    )

    punkte = tk.Label(
        top,
        text=str(punkte_a) + "  :  " + str(punkte_b),
        font=("Arial", 28, "bold"),
        bg=HINTERGRUND,
        fg=TEXT
    )

    punkte.grid(
        row=1,
        column=0,
        pady=10
    )

    sieger = tk.Label(
        top,
        text=ergebnis,
        font=("Arial", 16),
        bg=AKZENT,
        fg=TEXT,
        padx=15,
        pady=8
    )

    sieger.grid(
        row=2,
        column=0,
        pady=10
    )

    button_schliessen = tk.Button(
        top,
        text="Schließen",
        command=top.destroy
    )

    button_schliessen.grid(
        row=3,
        column=0,
        pady=(15, 0)
    )


# ============================================================
# MAIN
# ============================================================

def main():
    global window
    global daten

    daten = daten_laden(DATEI)

    window = tk.Tk()

    window.title(daten["titel"])

    oberflaeche_bauen(window)

    ergebnisse_aktualisieren()

    # Erste Kreatur direkt anzeigen
    if len(sichtbare) > 0:
        detail_zeigen(sichtbare[0])

    window.mainloop()


# ============================================================
# PROGRAMM STARTEN
# ============================================================

if __name__ == "__main__":
    main()