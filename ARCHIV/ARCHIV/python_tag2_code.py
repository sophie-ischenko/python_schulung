"""
TAG 2 - DUNGEON DUEL
Code-Begleitdatei zum Notebook "Tag 2 - Refactoring & Speicherung (JSON)"

Enthaelt: Theorie-Beispiele, Uebungs-Starter (mit TODOs) und das refactorte
Kampf-Grundgeruest mit Charakterspeicherung.
"""

import random
import json


# =============================================================
# 2.1 BEISPIEL: Funktionen & Parameter
# =============================================================

def begruesse(name, klasse):
    """
    Gibt eine Begruessung fuer einen neuen Helden aus.

    Parameter:
        name (str): Name des Helden
        klasse (str): Heldenklasse, z.B. "Kriegerin"

    Rueckgabewert:
        None - gibt direkt auf der Konsole aus.
    """
    print(f"Willkommen, {name} der/die {klasse}!")


begruesse("Aria", "Kriegerin")
begruesse("Finn", "Magier")


# =============================================================
# UEBUNG 1: Der smarte Kaffeevollautomat (40 Min)
# Lernziel: Funktionen definieren und Werte von aussen hineinreichen
# =============================================================

# def braue_kaffee(kaffee_art, zucker_wuerfel):
#     TODO: Docstring (Was/Parameter/Rueckgabewert)
#     TODO: zwei print()-Ausgaben, die den Bruehvorgang simulieren
#     TODO: wenn zucker_wuerfel > 3: zusaetzlich "Achtung: Sehr suess!" ausgeben
#
# braue_kaffee("Espresso", 0)
# braue_kaffee("Cappuccino", 4)


# =============================================================
# 2.2 BEISPIEL: Rueckgabewerte (return)
# =============================================================

def wuerfle_schaden(minimum, maximum):
    """
    Simuliert einen Schadenswurf in einem Bereich.

    Parameter:
        minimum (int): kleinster moeglicher Schaden
        maximum (int): groesster moeglicher Schaden

    Rueckgabewert:
        int: der gewuerfelte Schaden
    """
    return random.randint(minimum, maximum)


schaden = wuerfle_schaden(5, 20)
print(f"Du fuegst {schaden} Schaden zu.")


# =============================================================
# UEBUNG 2: Der Passwort-Pruefer (45 Min)
# Lernziel: Strikte Trennung von Logik (return) und Ausgabe (print)
# =============================================================

# def check_password(password):
#     TODO: Docstring
#     KEIN print() in dieser Funktion!
#     TODO: kuerzer als 8 Zeichen -> "schwach"
#     TODO: enthaelt "123" -> "sehr schwach"
#     TODO: sonst -> "stark"
#
# while True:
#     pw = input("Passwort: ")
#     ergebnis = check_password(pw)
#     print(ergebnis)
#     if ergebnis == "stark":
#         break


# =============================================================
# 2.3 BEISPIEL: Dateien & with
# =============================================================

def schreibe_notiz(text, pfad="notiz.txt"):
    """
    Schreibt einen Text in eine Datei (ueberschreibt vorhandenen Inhalt).

    Parameter:
        text (str): zu speichernder Inhalt
        pfad (str): Zieldatei, Standard "notiz.txt"

    Rueckgabewert:
        None
    """
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(text)


# schreibe_notiz("Testinhalt")   # zum Ausprobieren einkommentieren


# =============================================================
# 2.4 BEISPIEL: JSON
# =============================================================

def speichere_charakter(held, pfad="charakter.json"):
    """
    Speichert den Charakter-Zustand dauerhaft als JSON.

    Parameter:
        held (dict): z.B. {"name": ..., "hp": ..., "level": ...}
        pfad (str): Zieldatei

    Rueckgabewert:
        None
    """
    with open(pfad, "w", encoding="utf-8") as datei:
        json.dump(held, datei)


# beispiel_held = {"name": "Aria", "hp": 100, "level": 1}
# speichere_charakter(beispiel_held)


# =============================================================
# UEBUNG 3: Das Rollenspiel-Inventar (45 Min)
# Lernziel: Daten laden, veraendern und wieder speichern (Persistenz)
# =============================================================

# inventar = {"gold": 100, "traenke": 3}
# with open("savegame.json", "w", encoding="utf-8") as datei:
#     json.dump(inventar, datei)
#
# -- Diesen Block jetzt auskommentieren, savegame.json existiert bereits --
#
# TODO: Inventar aus savegame.json laden (json.load)
# TODO: fragen: "Ein Schwert kostet 50 Gold. Kaufen? (ja/nein)"
# TODO: wenn "ja": 50 Gold abziehen, "schwert": 1 hinzufuegen
# TODO: aktualisiertes Inventar wieder speichern
#
# Zweimal ausfuehren und pruefen: sinkt das Gold korrekt?


# =============================================================
# PRAXIS: Kampf refactoren + Charakter speichern (lauffaehig)
# =============================================================

def kampfrunde(monster_hp, aktion):
    """
    Berechnet den Effekt einer Spieleraktion auf die Monster-HP.

    Parameter:
        monster_hp (int): aktuelle HP des Monsters
        aktion (int): 1 = Angriff, 2 = Verteidigen

    Rueckgabewert:
        tuple[int, int]: (neue Monster-HP, verursachter Schaden)
    """
    if aktion == 1:
        schaden = random.randint(5, 20)
        return monster_hp - schaden, schaden
    return monster_hp, 0


def lade_charakter(pfad="charakter.json"):
    """
    Laedt den gespeicherten Charakter, oder erstellt einen neuen Standard-Charakter.

    Parameter:
        pfad (str): Pfad zur Speicherdatei

    Rueckgabewert:
        dict: z.B. {"level": 1, "besiegte_monster": 0}
    """
    try:
        with open(pfad, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except FileNotFoundError:
        return {"level": 1, "besiegte_monster": 0}


def speichere_charakter_state(held, pfad="charakter.json"):
    """
    Speichert den aktuellen Charakterzustand.

    Parameter:
        held (dict): Charakterdaten
        pfad (str): Zieldatei

    Rueckgabewert:
        None
    """
    with open(pfad, "w", encoding="utf-8") as datei:
        json.dump(held, datei)


def spiel_starten():
    """Fuehrt einen kompletten Kampf mit Charakterspeicherung aus. Keine Parameter, keine Rueckgabe."""
    charakter = lade_charakter()
    print(f"Willkommen zurueck! Level {charakter['level']}, {charakter['besiegte_monster']} besiegte Monster.")

    held_name = input("Wie heisst dein Held? ")
    held_hp = 100
    monster_hp = 50
    runde = 0

    while True:
        runde += 1
        eingabe_text = input("Aktion (1=Angriff, 2=Verteidigen): ")
        try:
            aktion = int(eingabe_text)
        except ValueError:
            print("Bitte nur Zahlen eingeben!")
            continue

        monster_hp, schaden = kampfrunde(monster_hp, aktion)
        print(f"Du fuegst {schaden} Schaden zu! (Monster HP: {max(monster_hp, 0)})")

        if monster_hp <= 0:
            print(f"Monster besiegt nach {runde} Runden!")
            charakter["besiegte_monster"] += 1
            # TODO (Profi-Challenge): alle 3 besiegte Monster -> level += 1
            speichere_charakter_state(charakter)
            break

        monster_schaden = random.randint(5, 15)
        if aktion == 2:
            monster_schaden = monster_schaden // 2
        held_hp -= monster_schaden
        print(f"Das Monster fuegt dir {monster_schaden} Schaden zu! (Deine HP: {max(held_hp, 0)})")

        if held_hp <= 0:
            print("Du wurdest besiegt...")
            break


# spiel_starten()   # zum Testen einkommentieren


# =============================================================
# GRUPPENARBEIT: Charakter speichern (60 Min)
# =============================================================
# 1. lade_charakter() und speichere_charakter_state() in euer eigenes
#    Spiel (aus Tag 1) einbauen
# 2. Begruessung zeigt Level und Anzahl besiegter Monster
# 3. Bei Sieg: besiegte_monster erhoehen und speichern
# 4. BONUS (Profi-Challenge): Level-System - alle 3 besiegten Monster
#    ein Levelaufstieg, max. HP + 10
