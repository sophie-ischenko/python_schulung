# ============================================================
# BLOCK 5: Fehlersuche (Bug-Hunting)
# ============================================================
# In den folgenden 4 Code-Schnipseln haben sich typische Fehler
# eingeschlichen. Finde sie, repariere den Code und teste ihn!


# --- Fehler 1: Die defekte Kaffeemaschine ---

kaffee_leer = True

if kaffee_leer:
print("Warnung: Kaffeebohnen nachfüllen!")
  print("Brühvorgang abgebrochen.")


# --- Fehler 2: Der vergessliche Wetter-Frosch ---

wetter = "regen"

if wetter == "regen"
    print("Vergiss deinen Regenschirm nicht.")
else
    print("Genieße die Sonne.")


# --- Fehler 3 ---

rabatt_gruppe = "Student"

# Überlege genau, was hier das Problem ist:
if rabatt_gruppe == "Student" and rabatt_gruppe == "Rentner":
    print("Glückwunsch! Du bekommst das Ticket zum halben Preis!")
else:
    print("Du zahlst den vollen Preis.")


# --- Fehler 4 ---

laden_geschlossen = False

# Ziel: Wenn der Laden NICHT geschlossen ist, soll man eintreten dürfen.
# Der folgende Code funktioniert zwar theoretisch, ist aber unsauber 
# und führt zur falschen Ausgabe. Mach es besser!
if not laden_geschlossen == False:
    print("Willkommen! Tritt ein, wir haben geöffnet.")
else:
    print("Wir haben leider schon zu.")