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


"""
PROJEKT: KREATUREN-ARCHIV

In der Datei kreaturen.json stehen ein Titel, ein Untertitel und
eine Liste mit 30 Kreaturen. Jede Kreatur ist ein Dictionary:

    {"name": "Glutfuchs", "typ": "Feuer", "staerke": 65,
     "tempo": 90, "magie": 40, "beschreibung": "Flitzt durch ..."}

Du baust eine App, in der man die Kreaturen suchen, filtern und
anschauen kann. Die Oberfläche erstellst du selbst.
So soll das Fenster am Ende aussehen:

    ┌───────────────────────────────────────────────────────┐
    │                    Kreaturen-Archiv                   │
    │              (Untertitel aus der JSON-Datei)          │
    │                                                       │
    │  [Suchfeld] [Suchen] [Zurücksetzen]  ┌──────────────┐ │
    │  [Alle][Feuer][Wasser][Wald]...      │ Glutfuchs    │ │
    │  6 von 30 Kreaturen                  │ Feuer        │ │
    │                                      │ Beschreibung │ │
    │  [Karte] [Karte] [Karte] [Karte]     │ Stärke ████  │ │
    │  [Karte] [Karte] [Karte] [Karte]     │ Tempo  █████ │ │
    │  [Karte] [Karte] [Karte] [Karte]     │ Magie  ███   │ │
    │  ...                                 │ Gesamt  195  │ │
    │                                      └──────────────┘ │
    │                                      [Zufall][Stärkste]│
    │                                      [Duell]          │
    └───────────────────────────────────────────────────────┘

Starte das Programm zuerst, bevor du etwas änderst. Es öffnet ein
leeres Fenster. Suche im Code nach "AUFGABE" und arbeite die Nummern
der Reihe nach ab. Starte das Programm nach jeder Aufgabe neu.

MERKSATZ (für Aufgabe 4 und 6)
Ein Button in einer Schleife braucht eine kleine Besonderheit,
damit jeder Button "seinen" Wert kennt. Schreibe bei command:

    command=lambda t=typ: typ_waehlen(t)

Übernimm die Zeile und tausche nur die Namen aus. Was lambda genau
macht, erklären wir später.

AUFGABEN

1. Titel und Untertitel (Funktion oberflaeche_bauen)
   Erstelle zwei Labels im Fenster. Der Text kommt aus den Daten:
   daten["titel"] und daten["untertitel"]. Platziere sie mit grid()
   in Zeile 0 und 1, jeweils mit column=0 und columnspan=2.
   Der Titel wird ein gelbes Banner: bg=AKZENT, padx=25, pady=8.

2. Linke und rechte Seite (Funktion oberflaeche_bauen)
   Erstelle zwei Frames mit bg=HINTERGRUND und nenne sie links
   und rechts. Platziere sie in Zeile 2: links in column=0,
   rechts in column=1. Mit sticky="n" kleben sie oben.

3. Suchzeile (Funktion oberflaeche_bauen)
   Erstelle in links einen Frame such_rahmen (Zeile 0). Darin:
   - ein Entry mit dem Namen suche_eingabe (column 0)
   - ein Button "Suchen" mit command=suchen (column 1)
   - ein Button "Zurücksetzen" mit command=zuruecksetzen (column 2)
   Das Entry bekommt bg="white", fg=TEXT und insertbackground=TEXT.

4. Typ-Buttons (Funktion oberflaeche_bauen)
   Erstelle in links einen Frame typ_rahmen (Zeile 1).
   Gehe mit einer for-Schleife durch die Liste TYPEN und erzeuge
   für jeden Typ einen Button. Der Text ist der Typ. Die Buttons
   stehen nebeneinander (column wird bei jedem Button um 1 größer).
   Benutze für command den Merksatz von oben.
   Jeder Button liegt in einem eigenen Farbrahmen: einem Frame mit
   bg=TYP_FARBEN[typ], padx=4 und pady=4. Den Frame platzierst du
   mit grid() in typ_rahmen, den Button mit grid() im Farbrahmen.

5. Zähler und Ergebnis-Rahmen (Funktion oberflaeche_bauen)
   Erstelle in links:
   - ein Label zaehler_label mit leerem Text (Zeile 2)
   - einen Frame ergebnis_rahmen (Zeile 3)
   Beide bekommen bg=HINTERGRUND.

6. Karten erzeugen (Funktion ergebnisse_aktualisieren)
   a) Hole die Treffer mit
          sichtbare = kreaturen_filtern(suche_eingabe.get(), aktueller_typ)
      und setze mit zaehler_label.config(...) den Text
      "6 von 30 Kreaturen". Die Zahlen kommen aus len(sichtbare)
      und len(daten["kreaturen"]). Wandle sie mit str() um.
   b) Gehe mit einer Schleife durch die Liste karten und rufe bei
      jedem Button .destroy() auf. Setze danach karten = [].
   c) Gehe durch sichtbare. Erzeuge für jede Kreatur einen Farbrahmen
      (Frame in ergebnis_rahmen mit bg=TYP_FARBEN[kreatur["typ"]],
      padx=4, pady=4) und darin einen Button:
          text:    Name, dann "\n", dann Typ
          width=13 und height=2
          command: nach dem Merksatz, aber mit detail_zeigen(k)
      Platziere den Farbrahmen mit grid(row=zeile, column=spalte,
      padx=4, pady=4) und den Button mit grid(row=0, column=0).
      Nach jeder Kreatur wird spalte um 1 größer. Wenn spalte gleich
      SPALTEN ist, setze spalte auf 0 und erhöhe zeile um 1.
      Hänge den Farbrahmen mit karten.append(farb_rahmen) an die
      Liste an. Wird der Rahmen gelöscht, verschwindet der Button mit.

7. Suchen, Zurücksetzen, Typ wählen
   - suchen(): ruft ergebnisse_aktualisieren() auf.
   - typ_waehlen(typ): speichert den Typ in aktueller_typ und
     ruft ergebnisse_aktualisieren() auf.
   - zuruecksetzen(): setzt aktueller_typ auf "Alle", leert das
     Suchfeld mit suche_eingabe.delete(0, tk.END) und ruft
     ergebnisse_aktualisieren() auf.

8. Detailkarte bauen (Funktion oberflaeche_bauen)
   Erstelle in rechts einen Frame detail_rahmen (Zeile 0) mit
   bg=KARTE, padx=25 und pady=20. Darin, untereinander:
   - kopf_rahmen: ein Frame (Zeile 0, bg=AKZENT, padx=15, pady=10,
     sticky="ew"). Er ist das bunte Band oben und enthält:
       name_label (Arial 24 bold, Text "Wähle eine Kreatur", bg=AKZENT)
       typ_label (Arial 11 bold, bg="white")
   - text_label (Zeile 1, mit wraplength=380 und justify="left")
   - staerke_label, tempo_label, magie_label (Zeile 2-4)
     Schrift ("Courier", 14, "bold"), damit die Balken gleich breit
     sind. Jedes Label hat seine eigene Farbe, zum Beispiel
     fg=STAT_FARBEN["staerke"].
   - gesamt_canvas (Zeile 5): ein Canvas (width=220, height=55) mit
     zwei Texten per create_text: "Gesamt" und eine Zahl (Farbe
     fill="#E4572E"). Speichere die ID der Zahl in gesamt_text.
   Die Labels außerhalb des Bands brauchen bg=KARTE.

9. Details anzeigen (Funktionen detail_zeigen, animation_schritt)
   a) detail_zeigen: hole die Farbe des Typs mit
          farbe = TYP_FARBEN[kreatur["typ"]]
      Setze dann mit .config(...) die Farbe von kopf_rahmen (bg),
      den Namen (mit bg=farbe), den Typ und die Beschreibung.
   b) Läuft schon eine Animation (animation_timer ist nicht None),
      brich sie mit window.after_cancel(animation_timer) ab.
      Setze danach fortschritt auf 0 und rufe animation_schritt() auf.
   c) animation_schritt: erhöhe fortschritt um 4 (höchstens 100).
      Berechne für Stärke, Tempo, Magie und Gesamt den aktuellen
      Wert, zum Beispiel:
          staerke = int(aktuelle["staerke"] * fortschritt / 100)
      Zeige die Balken mit staerke_label.config(text=balken_text(
      "Stärke", staerke)). Die Zahl im Canvas änderst du mit
      gesamt_canvas.itemconfig(gesamt_text, text=...).
      Ist fortschritt kleiner als 100, plane den nächsten Schritt:
          animation_timer = window.after(20, animation_schritt)
      Sonst setze animation_timer auf None.

10. Aktions-Buttons (Funktionen oberflaeche_bauen, zufaellige_kreatur,
    staerkste_zeigen)
    a) Erstelle in rechts einen Frame aktions_rahmen (Zeile 1) mit
       drei Buttons nebeneinander: "Zufällige Kreatur"
       (command=zufaellige_kreatur), "Stärkste zeigen"
       (command=staerkste_zeigen) und "Duell starten"
       (command=duell_starten).
    b) zufaellige_kreatur: wähle mit
       random.randint(0, len(sichtbare) - 1) eine Position und rufe
       detail_zeigen(sichtbare[position]) auf.
    c) staerkste_zeigen: merke dir zuerst die erste Kreatur in
       beste. Gehe durch sichtbare. Ist kreatur["gesamt"] größer als
       beste["gesamt"], wird kreatur die neue beste. Zeige am Ende
       beste an.

11. Duell (Funktion duell_starten)
    Der Gegner wird schon ausgewählt. Berechne punkte_a und
    punkte_b: der Gesamtwert der Kreatur plus random.randint(0, 60).
    Setze ergebnis mit if / elif / else:
    "<Name> gewinnt!" oder bei Gleichstand "Unentschieden!".
    Öffne ein Toplevel-Fenster mit drei Labels (Namen, Punkte,
    Ergebnis) und einem Button "Schließen" mit top.destroy.

12. Bonus
    a) Füge bei drei Kreaturen in kreaturen.json ein neues Feld
       "lieblingsessen" hinzu und zeige es in der Detailkarte an.
    b) Erfinde einen sechsten Typ (zum Beispiel "Blitz") mit Farbe in
       TYP_FARBEN und Eintrag in TYPEN und füge zwei Kreaturen hinzu.
    c) Zeige im Duell auch die Punkte unter jedem Namen an.
    d) Mache die Suche live: Mit
           suche_eingabe.bind("<KeyRelease>", live_suche)
       wird die Funktion live_suche bei jedem Tastendruck aufgerufen.
       Sie muss einen Parameter event haben.
"""


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
# JSON LADEN (fertig)
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
# OBERFLÄCHE (Aufgaben 1 bis 5, 8 und 10a)
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


    # --------------------------------------------------------
    # AUFGABE 2: Linke und rechte Seite
    # --------------------------------------------------------


    # --------------------------------------------------------
    # AUFGABE 3: Suchzeile
    # --------------------------------------------------------


    # --------------------------------------------------------
    # AUFGABE 4: Typ-Buttons mit einer Schleife
    # --------------------------------------------------------


    # --------------------------------------------------------
    # AUFGABE 5: Zähler und Ergebnis-Rahmen
    # --------------------------------------------------------


    # --------------------------------------------------------
    # AUFGABE 8: Detailkarte
    # --------------------------------------------------------


    # --------------------------------------------------------
    # AUFGABE 10a: Aktions-Buttons
    # --------------------------------------------------------


# ============================================================
# ERGEBNISSE ANZEIGEN (Aufgabe 6)
# ============================================================

def ergebnisse_aktualisieren():
    global sichtbare
    global karten

    # --------------------------------------------------------
    # AUFGABE 6a: Treffer holen und zählen
    # --------------------------------------------------------


    # --------------------------------------------------------
    # AUFGABE 6b: Alte Buttons löschen
    # --------------------------------------------------------


    # --------------------------------------------------------
    # AUFGABE 6c: Neue Buttons erzeugen
    # --------------------------------------------------------

    pass


# ============================================================
# AUFGABE 7: Suchen, Zurücksetzen, Typ wählen
# ============================================================

def suchen():
    pass


def zuruecksetzen():
    global aktueller_typ

    pass


def typ_waehlen(typ):
    global aktueller_typ

    pass


# ============================================================
# AUFGABE 9: Details anzeigen und animieren
# ============================================================

def detail_zeigen(kreatur):
    global aktuelle
    global fortschritt
    global animation_timer

    aktuelle = kreatur

    # AUFGABE 9a: Name, Typ und Beschreibung setzen

    # AUFGABE 9b: Alte Animation abbrechen, neu starten


def animation_schritt():
    global fortschritt
    global animation_timer

    # AUFGABE 9c: Ein Animationsschritt

    pass


# ============================================================
# AUFGABE 10b und 10c: Zufall und Stärkste
# ============================================================

def zufaellige_kreatur():
    if len(sichtbare) == 0:
        return

    # AUFGABE 10b


def staerkste_zeigen():
    if len(sichtbare) == 0:
        return

    # AUFGABE 10c


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

    # AUFGABE 11: Punkte, Ergebnis und Toplevel-Fenster


# ============================================================
# MAIN (fertig)
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