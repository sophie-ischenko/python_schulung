"""
Python-Schulung – Tag 7: For-Schleifen & Listen-Iterationen
===========================================================
Nachdem wir wissen, wie man Listen erstellt, lernen wir heute,
wie wir sie automatisch durchlaufen (iterieren).
"""

# ============================================================
# TEIL 1: DIE THEORIE (Kurz & Knapp)
# ============================================================

"""
Die 'for'-Schleife ist der Profi-Weg, um Listen zu verarbeiten.
Sie nimmt jedes Element einer Liste nacheinander aus der 'Kiste'
und speichert es in einer temporären Variable.

Syntax:
for element in liste:
    print(element)
"""

# Beispiel:
gilde = ["Magier", "Krieger", "Schurke"]
for klasse in gilde:
    print(f"Ein Mitglied der Gilde ist ein: {klasse}")


# ============================================================
# TEIL 2: DIE AUFGABEN
# ============================================================

# --- Aufgabe 1: Inventar-Inventur ---
# Gegeben: inventar = ["Schwert", "Trank", "Karte", "Gold"]
# Schreibe eine for-Schleife, die jedes Item einzeln ausgibt.
# Format: "Ich besitze: [Item]"
inventar = ["Schwert", "Trank", "Karte", "Gold"]
# HIER:



# --- Aufgabe 2: Der Gold-Rechner ---
# Gegeben: gold_muenzen = [10, 5, 20, 50]
# Schreibe eine for-Schleife, die alle Münzen zusammenzählt.
# (Tipp: Erstelle eine Variable 'summe = 0' VOR der Schleife!)
gold_muenzen = [10, 5, 20, 50]
summe = 0
# HIER:
print(f"Gesamtvermögen: {summe} Gold")



# --- Aufgabe 3: Der strenge Türsteher (Kombi if + for) ---
# Gegeben: alle_gaeste = ["Max", "Erika", "VIP", "Moritz", "VIP"]
# Gehe die Liste mit einer Schleife durch:
# - Wenn der Name "VIP" ist, gib aus: "VIP-Gast, bitte durchlassen!"
# - Bei allen anderen Namen: "Hallo [Name], bitte warten."
alle_gaeste = ["Max", "Erika", "VIP", "Moritz", "VIP"]
# HIER:



# --- Aufgabe 4: Die Rabatt-Aktion ---
# Gegeben: preise = [10, 20, 30, 40]
# Nutze eine for-Schleife, um jeden Preis um 10% zu reduzieren
# (multipliziere mit 0.9) und gib die neuen Preise aus.
preise = [10, 20, 30, 40]
# HIER:



