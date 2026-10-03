"""
TAG 2 - AUFGABEN LOESUNG
Vollstaendig geloeste Version von aufgaben.py.
"""

import json


# =============================================================
# UEBUNG 1: Der smarte Kaffeevollautomat
# =============================================================

def braue_kaffee(kaffee_art, zucker_wuerfel):
    """
    Simuliert das Bruehen eines Kaffees.

    Parameter:
        kaffee_art (str): z.B. "Espresso", "Cappuccino"
        zucker_wuerfel (int): Anzahl Zuckerwuerfel

    Rueckgabewert:
        None
    """
    print(f"Mahle Bohnen fuer {kaffee_art}...")
    print(f"Fuege {zucker_wuerfel} Stueck Zucker hinzu...")
    if zucker_wuerfel > 3:
        print("Achtung: Sehr suess!")


braue_kaffee("Espresso", 0)
braue_kaffee("Cappuccino", 4)
braue_kaffee("Latte Macchiato", 2)


# =============================================================
# UEBUNG 2: Der Passwort-Pruefer
# =============================================================

def check_password(password):
    """
    Bewertet die Staerke eines Passworts.

    Parameter:
        password (str): das zu pruefende Passwort

    Rueckgabewert:
        str: "schwach", "sehr schwach" oder "stark"
    """
    if len(password) < 8:
        return "schwach"
    if "123" in password:
        return "sehr schwach"
    return "stark"


while True:
    pw = input("Passwort: ")
    ergebnis = check_password(pw)
    print(ergebnis)
    if ergebnis == "stark":
        break


# =============================================================
# UEBUNG 3: Das Rollenspiel-Inventar
# =============================================================

# Schritt 1 (einmalig ausfuehren, danach auskommentieren):
# inventar = {"gold": 100, "traenke": 3}
# with open("savegame.json", "w", encoding="utf-8") as datei:
#     json.dump(inventar, datei)

# Schritt 3: laden, kaufen lassen, speichern
with open("savegame.json", "r", encoding="utf-8") as datei:
    inventar = json.load(datei)

print(f"Aktuelles Gold: {inventar['gold']}")
kaufen = input("Ein Schwert kostet 50 Gold. Kaufen? (ja/nein): ")

if kaufen == "ja" and inventar["gold"] >= 50:
    inventar["gold"] -= 50
    inventar["schwert"] = 1
    print("Schwert gekauft!")
elif kaufen == "ja":
    print("Nicht genug Gold!")

with open("savegame.json", "w", encoding="utf-8") as datei:
    json.dump(inventar, datei)

print(f"Neues Gold: {inventar['gold']}")
