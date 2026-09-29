"""
Tag 8 – Teil 1: Funktionen mit einem Parameter
================================================
Teil A: Viele Funktionen mit genau EINEM Parameter.
Teil B: Funktionen, die andere Funktionen aus Teil A aufrufen.

Arbeitsweise:
- Schreibe deine Lösung jeweils unter die Aufgabenstellung (ersetze 'pass').
- Nutze 'return', sofern nicht ausdrücklich 'print' gefordert ist.
- Teste jede Funktion sofort im Testbereich ganz unten, bevor du weitergehst.
- Die Datei hat bewusst KEIN main(): Du rufst deine Funktionen einfach
  ganz unten direkt auf, von oben nach unten, wie in jedem anderen Skript.
- Teil B braucht Funktionen aus Teil A. Fehlt dir eine, schreib sie zuerst.
"""

# =====================================================================
# TEIL A: Ein Parameter
# =====================================================================


def begruesse(name):
    """
    A1: Gib "Hallo, <name>!" mit print aus (kein return).
    Beispiel: begruesse("Lena") gibt "Hallo, Lena!" aus.
    """
    # Deine Lösung hier
    pass


def quadrat(zahl):
    """
    A2: Gib das Quadrat der Zahl zurück.
    Beispiel: quadrat(7) -> 49
    """
    # Deine Lösung hier
    pass


def ist_gerade(zahl):
    """
    A3: Gib True zurück, wenn die Zahl gerade ist, sonst False.
    Beispiel: ist_gerade(8) -> True
    """
    # Deine Lösung hier
    pass


def fahrenheit_to_celsius(f):
    """
    A4: Rechne Fahrenheit in Celsius um (Formel: (f - 32) * 5 / 9).
    Beispiel: fahrenheit_to_celsius(68) -> 20.0
    """
    # Deine Lösung hier
    pass


def bewerte_note(note):
    """
    A5: Gib zur Schulnote den Text zurück:
    1 -> "Sehr gut", 2 -> "Gut", 3 -> "Befriedigend", 4 -> "Ausreichend",
    5 oder 6 -> "Nicht bestanden", alles andere -> "Ungültige Note".
    """
    # Deine Lösung hier
    pass


def zaehle_woerter(text):
    """
    A6: Gib zurück, wie viele Wörter der Text hat (Wörter sind durch
    Leerzeichen getrennt).
    Beispiel: zaehle_woerter("Das ist ein Test") -> 4
    """
    # Deine Lösung hier
    pass


def rufe(text):
    """
    A7: Gib den Text komplett in Großbuchstaben und mit einem "!" am
    Ende zurück.
    Beispiel: rufe("hallo welt") -> "HALLO WELT!"
    """
    # Deine Lösung hier
    pass


def erste_und_letzte(wort):
    """
    A8: Gib den ersten und den letzten Buchstaben des Wortes
    zusammen zurück.
    Beispiel: erste_und_letzte("Hallo") -> "Ho"
    """
    # Deine Lösung hier
    pass


def zaehle_vokale(text):
    """
    A9: Gib zurück, wie viele Vokale (a, e, i, o, u) der Text enthält.
    Groß-/Kleinschreibung soll egal sein.
    Beispiel: zaehle_vokale("Ananas") -> 3
    """
    # Deine Lösung hier
    pass


def ist_palindrom(wort):
    """
    A10: Gib True zurück, wenn das Wort vorwärts und rückwärts gleich
    gelesen wird, sonst False. Groß-/Kleinschreibung soll egal sein.
    Beispiel: ist_palindrom("Reittier") -> True
    """
    # Deine Lösung hier
    pass


def summe_liste(zahlen):
    """
    A11: Gib die Summe aller Zahlen der Liste zurück.
    Ohne die eingebaute Funktion sum()!
    Beispiel: summe_liste([4, 8, 15]) -> 27
    """
    # Deine Lösung hier
    pass


def groesste_zahl(zahlen):
    """
    A12: Gib die größte Zahl der (nicht leeren) Liste zurück.
    Ohne die eingebaute Funktion max()!
    Beispiel: groesste_zahl([3, 17, 9]) -> 17
    """
    # Deine Lösung hier
    pass


def gerade_zahlen(zahlen):
    """
    A13: Gib eine NEUE Liste zurück, die nur die geraden Zahlen der
    übergebenen Liste enthält.
    Beispiel: gerade_zahlen([1, 2, 3, 4, 6]) -> [2, 4, 6]
    """
    # Deine Lösung hier
    pass


def fakultaet(n):
    """
    A14: Gib n! zurück (n * (n-1) * ... * 1). Es gilt: 0! = 1.
    Beispiel: fakultaet(5) -> 120
    """
    # Deine Lösung hier
    pass


def ist_schaltjahr(jahr):
    """
    A15: Gib True zurück, wenn das Jahr ein Schaltjahr ist.
    Regel: durch 4 teilbar, ABER nicht durch 100, es sei denn, es ist
    auch durch 400 teilbar.
    Beispiele: 2024 -> True, 1900 -> False, 2000 -> True
    """
    # Deine Lösung hier
    pass


def quersumme(zahl):
    """
    A16: Gib die Quersumme der (positiven) Zahl zurück.
    Beispiel: quersumme(1234) -> 10
    """
    # Deine Lösung hier
    pass


def sterne_anzeige(bewertung):
    """
    A17: Gib eine Bewertung von 0 bis 5 als Sterne-Text zurück:
    ausgefüllte Sterne "★" plus leere Sterne "☆", insgesamt immer 5.
    Beispiel: sterne_anzeige(4) -> "★★★★☆"
    """
    # Deine Lösung hier
    pass


def jahreszeit(monat):
    """
    A18: Gib zum Monat (1 bis 12) die Jahreszeit zurück:
    12, 1, 2 -> "Winter", 3-5 -> "Frühling", 6-8 -> "Sommer",
    9-11 -> "Herbst". Alles andere -> "Ungültiger Monat".
    """
    # Deine Lösung hier
    pass


# =====================================================================
# TEIL B: Funktionen, die andere Funktionen aufrufen
# =====================================================================
# Schreibe hier KEINE Berechnung doppelt: Nutze die Funktionen aus Teil A!


def begruesse_laut(name):
    """
    B1: Gib per return "HALLO <NAME>!" zurück.
    Nutzt: rufe()
    Beispiel: begruesse_laut("max") -> "HALLO MAX!"
    """
    # Deine Lösung hier
    pass


def ist_quersumme_gerade(zahl):
    """
    B2: Gib True zurück, wenn die Quersumme der Zahl gerade ist.
    Nutzt: quersumme(), ist_gerade()
    Beispiel: ist_quersumme_gerade(1234) -> True (Quersumme 10)
    """
    # Deine Lösung hier
    pass


def wetterbericht(fahrenheit):
    """
    B3: Gib einen Wetterbericht als Text zurück. Rechne zuerst in Celsius
    um: unter 10 Grad "kalt", bis einschließlich 25 Grad "angenehm",
    darüber "heiß".
    Nutzt: fahrenheit_to_celsius()
    Beispiel: wetterbericht(68) -> "Es hat 20.0 Grad - angenehm"
    """
    # Deine Lösung hier
    pass


def durchschnitt(zahlen):
    """
    B4: Gib den Durchschnitt der (nicht leeren) Liste zurück.
    Nutzt: summe_liste()
    Beispiel: durchschnitt([2, 4, 9]) -> 5.0
    """
    # Deine Lösung hier
    pass


def textstatistik(text):
    """
    B5: Gib zurück, wie viele Wörter und Vokale der Text hat.
    Nutzt: zaehle_woerter(), zaehle_vokale()
    Beispiel: textstatistik("Das ist ein Test") -> "4 Wörter, 5 Vokale"
    """
    # Deine Lösung hier
    pass


def ist_satz_palindrom(satz):
    """
    B6: Gib True zurück, wenn der ganze Satz ein Palindrom ist. Leerzeichen
    werden dabei ignoriert.
    Nutzt: ist_palindrom()
    Beispiel: ist_satz_palindrom("Roma tibi subito motibus ibit amor") -> True
    """
    # Deine Lösung hier
    pass


def pruefe_zahl(zahl):
    """
    B7: Gib einen Steckbrief der Zahl als Text zurück.
    Nutzt: ist_gerade(), quersumme(), quadrat()
    Beispiel: pruefe_zahl(12) -> "12 ist gerade, Quersumme 3, Quadrat 144"
    Beispiel: pruefe_zahl(7)  -> "7 ist ungerade, Quersumme 7, Quadrat 49"
    """
    # Deine Lösung hier
    pass


def kritik(bewertung):
    """
    B8: Gib die Sterne und einen Kurztext zurück:
    5 -> "Meisterwerk", 4 -> "Sehr gut", 3 -> "Ganz okay",
    2 -> "Schwach", 1 -> "Enttäuschend", 0 -> "Ungenießbar".
    Nutzt: sterne_anzeige()
    Beispiel: kritik(4) -> "★★★★☆ - Sehr gut"
    """
    # Deine Lösung hier
    pass


def naechstes_schaltjahr(jahr):
    """
    B9 (knifflig): Gib das nächste Schaltjahr NACH dem übergebenen Jahr
    zurück.
    Nutzt: ist_schaltjahr()
    Beispiel: naechstes_schaltjahr(2024) -> 2028
    """
    # Deine Lösung hier
    pass


# =====================================================================
# TESTBEREICH – hier rufst du deine Funktionen auf
# =====================================================================
# Entferne das '#' vor einer Zeile, sobald du die Funktion geschrieben hast.

# begruesse("Lena")
# print(quadrat(7))
# print(ist_gerade(8))
# print(fahrenheit_to_celsius(68))
# print(bewerte_note(2))
# print(zaehle_woerter("Das ist ein Test"))
# print(rufe("hallo welt"))
# print(erste_und_letzte("Hallo"))
# print(zaehle_vokale("Ananas"))
# print(ist_palindrom("Reittier"))
# print(summe_liste([4, 8, 15]))
# print(groesste_zahl([3, 17, 9]))
# print(gerade_zahlen([1, 2, 3, 4, 6]))
# print(fakultaet(5))
# print(ist_schaltjahr(2024))
# print(quersumme(1234))
# print(sterne_anzeige(4))
# print(jahreszeit(7))

# print(begruesse_laut("max"))
# print(ist_quersumme_gerade(1234))
# print(wetterbericht(68))
# print(durchschnitt([2, 4, 9]))
# print(textstatistik("Das ist ein Test"))
# print(ist_satz_palindrom("Roma tibi subito motibus ibit amor"))
# print(pruefe_zahl(12))
# print(kritik(4))
# print(naechstes_schaltjahr(2024))