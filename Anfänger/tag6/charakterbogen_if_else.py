"""

## Entscheidungen mit `if` / `elif` / `else`

Bisher lief dein Programm stur von oben nach unten. Ab jetzt kann es **Entscheidungen** treffen.


if bedingung:
    # Mach das, wenn die Bedingung wahr ist
elif andere_bedingung:
    # Mach das stattdessen, wenn die zweite Bedingung wahr ist
else:
    # Mach das, wenn NICHTS davon gestimmt hat
"""

# ====================================================================
# SETUP: DUMMY-WERTE
# Da wir den alten Code weglassen, definieren wir hier Startwerte.
# Ändere sie gerne ab (z.B. die Klasse oder Stufe), um zu testen,
# wie deine if-Abfragen reagieren!
# manche vorbereiteten print() Ausgaben sind 
# in den if-else Abfragen schon enthalten und teilweise eingerückt
# ====================================================================
name = "Gandalf"
klasse = "Magier"      # Teste später auch mal "Krieger" oder "Schurke"
stufe = 4              # Teste mal Stufe 2, 7 oder 12 für Aufgabe 17
mana = 20
lebenspunkte = 30
gold = 100
staerke = 14
schaden = 12


# ===== Sicherheitsnetz (Sicheres Teilen) =====
# Ohne ein if stürzt ein Programm ab, wenn man durch 0 teilt. Sichere es ab!
print("\n*** Teile die Beute ***")
anzahl = int(input("An wie viele Leute wird das Gold (100) verteilt? (Gib mal 0 ein!) "))

# Wenn die anzahl größer als 0 ist:
# HIER
    # Gib aus: Jeder bekommt {gold / anzahl} Gold.
    # HIER
# Sonst:
# HIER
    print("Durch 0 teilen? Netter Versuch. Du behältst das Gold einfach selbst.")


# ===== Klassen-Begrüßung (if / elif / else) =====
print("\n*** Die Gilde begrüßt dich ***")

# Prüfe, ob die Klasse (in Kleinbuchstaben!) "magier" ist 
# Achtung: Du musst die Eingabe in Kleinbuchstaben umwandeln, damit die Abfrage auch bei "Magier" oder "MAGIER" funktioniert!

# HIER
    print(r"""
      /\
     /* \
    /____\
    (o  o)
""")
    print(f"{name} murmelt: 'Abrakadabra... wo war nochmal mein Zauberstab?'")

# Sonst, prüfe ob die Klasse "krieger" ist
# HIER
    print(r"""
  ._________.
  |    |    |
  |----+----|
  |    |    |
   \   |   /
    \__|__/
""")
    print(f"{name} brüllt: 'ICH HAUE ZUERST, FRAGEN STELLE ICH NIE!'")

# Sonst, prüfe ob die Klasse "schurke" ist
# HIER
    print(r"""
    ______
   /  __  \
  |  (oo)  |   psst...
   \__||__/
""")
    print(f"{name} flüstert: 'Ich habe dein Gold nicht. Wirklich. Schau nicht in meine Taschen.'")

# In allen anderen Fällen (else):
# HIER
    print(f"'{klasse}'? So etwas kennt die Gilde noch nicht... aber das Freibier gilt trotzdem!")


# ===== Titel nach Stufe (elif-Kette) =====

# Wenn die Stufe kleiner als 3 ist, setze die Variable 'titel' auf "Novize"
# HIER
# HIER

# Sonst, wenn die Stufe kleiner als 6 ist, setze 'titel' auf "Abenteurer"
# HIER
# HIER

# Sonst, wenn die Stufe kleiner als 10 ist, setze 'titel' auf "Veteran"
# HIER
# HIER

# Sonst (10 oder höher), setze 'titel' auf "Legende"
# HIER
# HIER

print(f"\nDer Torwächter ruft: 'Willkommen, {titel} {name}!'")


# ===== Zauber wirken (and / or / in) =====
antwort = input(f"\nDu hast {mana} Mana. Feuerball wirken (kostet 15)? (ja/nein) ")

# Wenn die Antwort (in Kleinbuchstaben) "ja" oder "j" ist UND mana >= 15 ist:
# HIER
    # Ziehe 15 vom Mana ab
    # HIER
    print(r"""
     ) (
    ( ) )
     ) ( (
   (_____)   FUMP!
""")
    print(f"FEUERBALL! Du hast noch {mana} Mana.")

# Sonst, wenn die Antwort nur "ja" oder "j" ist (aber das Mana scheinbar nicht reichte):
# HIER
    print("Nur ein trauriges Fünkchen... zu wenig Mana. Der Goblin klatscht höflich.")

# Sonst (in allen anderen Fällen):
# HIER
    print("Du steckst den Zauberstab wieder ein. Feigling? Nein: strategisch.")


# ===== Truhe mit Falle (if / elif / else) =====
print("\nDu öffnest eine Truhe...")

# Wähle eine Zahl zwischen 1 und 4 und speichere sie in 'truhenwurf'
# HIER

# Wenn truhenwurf == 1 ist:
# HIER
    # Wähle Fallenschaden (1 bis 6)
    # HIER
    # Ziehe den Fallenschaden von den Lebenspunkten ab
    # HIER
    print(f"KLICK! Eine Pfeilfalle! Du verlierst {fallenschaden} Lebenspunkte.")

# Sonst, wenn truhenwurf == 2 ist:
# HIER
    # Ziehe 5 vom Gold ab
    # HIER
    print("Die Truhe hat Zähne! Ein Mimic! Du rennst weg und verlierst 5 Gold.")

# Sonst:
# HIER
    # Wähle einen Fund zwischen 5 und 25
    # HIER
    # Zähle den Fund zum Gold dazu
    # HIER
    print(f"Glitzer, glitzer! Du findest {fund} Gold.")


# ===== Angriffswurf gegen Rüstungsklasse =====

# Wähle die Gegner-Rüstungsklasse (8 bis 18)
# HIER (gegner_rk = ...)
# Wähle deinen Angriff (1 bis 20)
# HIER (angriffswurf = ...)
# Berechne den Trefferwert (angriffswurf + staerke // 2)
# HIER (trefferwert = ...)

print(f"\nDu greifst einen Goblin an (Rüstungsklasse {gegner_rk}). Wurf: {angriffswurf} + Bonus = {trefferwert}")

# Wenn angriffswurf eine natürliche 20 ist:
# HIER
    print(r"""
   \ | /
  -- * --   KRITISCHER TREFFER!
   / | \
""")
    # Gib aus, wie viel Schaden du machst (schaden * 2)
    # HIER

# Sonst, wenn angriffswurf eine 1 ist:
# HIER
    print("PATZER! Du stolperst über deinen eigenen Umhang. Der Goblin klatscht.")

# Sonst, wenn dein trefferwert >= gegner_rk ist:
# HIER
    print(f"Treffer! Der Goblin verliert {schaden} Lebenspunkte.")

# Sonst:
# HIER
    print("Daneben! Der Goblin streckt dir die Zunge raus.")

# ===== Gesundheitszustand am Ende =====
print("\n*** Fazit nach dem Abenteuer ***")
print(f"Verbleibende Lebenspunkte: {lebenspunkte}")

# Wenn lebenspunkte > 50: zustand = "strotzt vor Kraft"
# HIER
# HIER

# Sonst, wenn lebenspunkte > 25: zustand = "ein paar Kratzer, nichts Schlimmes"
# HIER
# HIER

# Sonst: zustand = "sieht aus, als hätte ein Ork ihn als Kissen benutzt"
# HIER
# HIER

print(f"Gesundheitszustand: {name} {zustand}.")


