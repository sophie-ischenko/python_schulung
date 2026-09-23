"""
TAG 5 - DUNGEON DUEL - gui.py
Grafische Oberflaeche fuer Dungeon Duel mit tkinter.

Importiert db.py und game.py aus Tag 4 UNVERAENDERT - nur die
Konsolen-Ein-/Ausgabe aus main.py wird hier durch Fenster, Labels
und Buttons ersetzt.

Voraussetzung: db.py und game.py (aus Tag 4) liegen im selben Ordner.
"""

import tkinter as tk
from db import setup_db, speichere_held_db, get_top_5_helden
from game import kampfrunde, monster_greift_an, pruefe_aktion, UngueltigeAktionError

setup_db()

held_name = ""
held_hp = 100
monster_hp = 50
level = 1
besiegte_monster = 0


def kampf_starten():
    """Startet einen neuen Kampf: liest Namen ein, setzt HP zurueck, aktiviert Buttons."""
    global held_name, held_hp, monster_hp
    held_name = name_eingabe.get()
    if not held_name:
        status_label.config(text="Bitte gib zuerst einen Heldennamen ein!")
        return
    held_hp, monster_hp = 100, 50
    status_label.config(text=f"Ein Monster erscheint vor {held_name}!")
    aktualisiere_hp_anzeige()
    angriff_button.config(state="normal")
    verteidigen_button.config(state="normal")


def aktualisiere_hp_anzeige():
    """Schreibt die aktuellen HP-Werte in die beiden Anzeige-Labels."""
    held_hp_label.config(text=f"Deine HP: {max(held_hp, 0)}")
    monster_hp_label.config(text=f"Monster HP: {max(monster_hp, 0)}")


def runde_ausfuehren(aktion):
    """
    Fuehrt eine komplette Kampfrunde aus (Spieleraktion + Monster-Gegenangriff).

    Parameter:
        aktion (int): 1 = Angriff, 2 = Verteidigen (kommt aus dem Button via lambda)

    Rueckgabewert:
        None - aktualisiert Labels direkt.
    """
    global held_hp, monster_hp, besiegte_monster
    try:
        pruefe_aktion(aktion)
    except UngueltigeAktionError as e:
        status_label.config(text=str(e))
        return

    monster_hp, schaden = kampfrunde(monster_hp, aktion)
    aktualisiere_hp_anzeige()

    if monster_hp <= 0:
        besiegte_monster += 1
        status_label.config(text=f"Monster besiegt! ({besiegte_monster} insgesamt)")
        speichere_held_db(held_name, level, besiegte_monster)
        zeige_bestenliste()
        angriff_button.config(state="disabled")
        verteidigen_button.config(state="disabled")
        return

    monster_schaden = monster_greift_an(aktion)
    held_hp -= monster_schaden
    aktualisiere_hp_anzeige()
    status_label.config(text=f"Das Monster fuegt dir {monster_schaden} Schaden zu!")

    if held_hp <= 0:
        status_label.config(text="Du wurdest besiegt...")
        angriff_button.config(state="disabled")
        verteidigen_button.config(state="disabled")


def zeige_bestenliste():
    """Oeffnet ein Zusatzfenster mit der aktuellen Heldenbestenliste."""
    fenster_top5 = tk.Toplevel(fenster)
    fenster_top5.title("Heldenbestenliste")
    for platz, (name, lvl) in enumerate(get_top_5_helden(), start=1):
        tk.Label(fenster_top5, text=f"{platz}. {name} - Level {lvl}").pack(anchor="w", padx=10, pady=2)


# --- Fensteraufbau ---
fenster = tk.Tk()
fenster.title("Dungeon Duel")
fenster.geometry("350x300")

tk.Label(fenster, text="Heldenname:").pack(pady=(15, 0))
name_eingabe = tk.Entry(fenster)
name_eingabe.pack()

tk.Button(fenster, text="Kampf starten", command=kampf_starten).pack(pady=10)

held_hp_label = tk.Label(fenster, text="Deine HP: 100")
held_hp_label.pack()
monster_hp_label = tk.Label(fenster, text="Monster HP: 50")
monster_hp_label.pack()

angriff_button = tk.Button(fenster, text="Angriff", command=lambda: runde_ausfuehren(1), state="disabled")
angriff_button.pack(pady=5)

verteidigen_button = tk.Button(fenster, text="Verteidigen", command=lambda: runde_ausfuehren(2), state="disabled")
verteidigen_button.pack(pady=5)

status_label = tk.Label(fenster, text="Gib deinen Heldennamen ein und starte den Kampf.", wraplength=300)
status_label.pack(pady=10)

fenster.mainloop()


# =============================================================
# GRUPPENARBEIT: GUI fertigstellen & erweitern (2h)
# =============================================================
# 1. Diese Datei nachbauen und testen - mehrere Runden spielen,
#    Bestenliste pruefen
# 2. Kritische Treffer (aus Tag 1) einbauen, im status_label anzeigen
# 3. "Neuer Kampf"-Button nach Sieg/Niederlage einbauen
# 4. BONUS: Rundenzahl live als eigenes Label
# 5. BONUS: held_hp_label rot faerben, wenn HP < 30 (fg="red")
