"""
TAG 2 - AUFGABEN (ohne Loesung)
Bearbeite die drei Uebungen der Reihe nach. Jede Uebung nennt ihr Lernziel.
Die zugehoerige Theorie steht im Jupyter-Notebook "tag2_theorie.ipynb".
"""

import random
import json


# =============================================================
# UEBUNG 1: Der smarte Kaffeevollautomat (40 Min)
# Lernziel: Funktionen definieren und Werte von aussen hineinreichen
# =============================================================
#
# 1. Schreibe eine Funktion braue_kaffee(kaffee_art, zucker_wuerfel)
#    - mit Docstring (Was / Parameter / Rueckgabewert)
#    - zwei print()-Ausgaben, die den Bruehvorgang simulieren
#    - wenn zucker_wuerfel > 3: zusaetzlich "Achtung: Sehr suess!" ausgeben
# 2. Rufe die Funktion dreimal mit unterschiedlichen Werten auf


def braue_kaffee(kaffee_art, zucker_wuerfel):
    # TODO: Docstring ergaenzen
    # TODO: Bruehvorgang simulieren
    # TODO: Suess-Warnung bei zucker_wuerfel > 3
    pass


# TODO: braue_kaffee() dreimal aufrufen


# =============================================================
# UEBUNG 2: Der Passwort-Pruefer (45 Min)
# Lernziel: Strikte Trennung von Logik (return) und Ausgabe (print)
# =============================================================
#
# 1. Schreibe eine Funktion check_password(password) - KEIN print() darin!
#    - kuerzer als 8 Zeichen -> "schwach"
#    - enthaelt "123"        -> "sehr schwach"
#    - sonst                 -> "stark"
# 2. while-Schleife: fragt, speichert Ergebnis, gibt es aus, bei "stark" -> break


def check_password(password):
    # TODO: Docstring
    # TODO: Bedingungen wie oben beschrieben
    pass


# TODO: while-Schleife mit check_password() bauen


# =============================================================
# UEBUNG 3: Das Rollenspiel-Inventar (45 Min)
# Lernziel: Daten laden, veraendern und wieder speichern (Persistenz)
# =============================================================
#
# 1. Dictionary inventar = {"gold": 100, "traenke": 3} als savegame.json speichern
# 2. Diesen Speicher-Code danach auskommentieren (Datei existiert jetzt)
# 3. Neu schreiben:
#    - Inventar aus savegame.json laden (json.load)
#    - Fragen: "Ein Schwert kostet 50 Gold. Kaufen? (ja/nein)"
#    - Bei "ja": 50 Gold abziehen, "schwert": 1 hinzufuegen
#    - Aktualisiertes Inventar wieder speichern
# 4. Skript zweimal ausfuehren und pruefen: sinkt das Gold korrekt?


# TODO: Schritt 1 (einmalig, dann auskommentieren)

# TODO: Schritt 3 (laden, kaufen lassen, speichern)
