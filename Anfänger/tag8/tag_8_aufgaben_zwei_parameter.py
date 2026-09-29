"""
Tag 8 – Teil 2: Funktionen mit mehreren Parametern
====================================================
Teil A: Funktionen mit zwei oder drei Parametern (auch mit Standardwert).
Teil B: Funktionen, die andere Funktionen aus Teil A aufrufen.
Teil C: Kleine Programme, die deine Funktionen aufrufen – ganz ohne main().

Arbeitsweise:
- Schreibe deine Lösung jeweils unter die Aufgabenstellung (ersetze 'pass').
- Nutze 'return', sofern nicht ausdrücklich 'print' gefordert ist.
- Teste jede Funktion sofort im Testbereich ganz unten, bevor du weitergehst.
- Diese Datei hat bewusst KEIN main(): Der Code läuft einfach von oben
  nach unten, und du rufst deine Funktionen direkt auf.
- Teil B und C brauchen Funktionen aus Teil A. Fehlt dir eine, schreib sie zuerst.
"""

# =====================================================================
# TEIL A: Mehrere Parameter
# =====================================================================


def rechteck_flaeche(laenge, breite):
    """
    A1: Gib die Fläche eines Rechtecks zurück.
    Beispiel: rechteck_flaeche(3, 4) -> 12
    """
    # Deine Lösung hier
    pass


def berechne_rechnung(betrag, trinkgeld_prozent=10):
    """
    A2: Der Trinkgeld-Rechner. Gib den Gesamtbetrag zurück, den du zahlst
    (Rechnungsbetrag plus Trinkgeld). Standard-Trinkgeld: 10 Prozent.
    Beispiel: berechne_rechnung(50) -> 55.0
    Beispiel: berechne_rechnung(50, 20) -> 60.0
    """
    # Deine Lösung hier
    pass


def bestimme_ticketpreis(alter, ist_mitglied):
    """
    A3: Der Kino-Preisrechner. Mitglieder zahlen immer 5.00 Euro.
    Alle anderen zahlen: unter 6 Jahren 0.00, unter 18 Jahren 6.50,
    sonst 9.50 Euro. Gib den Preis zurück.
    Beispiel: bestimme_ticketpreis(10, False) -> 6.5
    Beispiel: bestimme_ticketpreis(30, True) -> 5.0
    """
    # Deine Lösung hier
    pass


def berechne_radtour(tage, km_pro_tag, ruhetage=0):
    """
    A4: Deine Radtour dauert 'tage' Tage, davon sind 'ruhetage' Tage ohne
    Fahrt. Gib die Gesamtstrecke zurück.
    Beispiel: berechne_radtour(7, 60, 1) -> 360
    """
    # Deine Lösung hier
    pass


def kalkuliere_bestellung(anzahl_pizzen, belaege_pro_pizza):
    """
    A5: Eine Pizza kostet 8.50 Euro, jeder Belag kostet 1.20 Euro extra
    (pro Pizza). Gib den Gesamtpreis der Bestellung zurück.
    Beispiel: kalkuliere_bestellung(2, 3) -> 24.2
    """
    # Deine Lösung hier
    pass


def rechne_rezept_um(menge, personen_alt, personen_neu):
    """
    A6: Ein Rezept ist für 'personen_alt' Personen gedacht und braucht
    'menge' einer Zutat. Gib zurück, wie viel du für 'personen_neu'
    Personen brauchst.
    Beispiel: rechne_rezept_um(200, 4, 6) -> 300.0
    """
    # Deine Lösung hier
    pass


def berechne_alter(geburtsjahr, aktuelles_jahr=2026):
    """
    A7: Gib das Alter zurück, das jemand im aktuellen Jahr (mindestens)
    erreicht.
    Beispiel: berechne_alter(1990) -> 36
    Beispiel: berechne_alter(1990, 2030) -> 40
    """
    # Deine Lösung hier
    pass


def ist_im_bereich(zahl, minimum, maximum):
    """
    A8: Gib True zurück, wenn die Zahl zwischen minimum und maximum liegt
    (Grenzen zählen mit), sonst False.
    Beispiel: ist_im_bereich(5, 1, 10) -> True
    """
    # Deine Lösung hier
    pass


def zaehle_buchstabe(text, buchstabe):
    """
    A9: Gib zurück, wie oft der Buchstabe im Text vorkommt.
    Groß-/Kleinschreibung soll egal sein.
    Beispiel: zaehle_buchstabe("Banane", "a") -> 2
    """
    # Deine Lösung hier
    pass


def wiederhole_wort(wort, anzahl, trenner=" "):
    """
    A10: Gib das Wort 'anzahl'-mal zurück, getrennt durch den Trenner.
    Am Ende darf KEIN Trenner stehen.
    Beispiel: wiederhole_wort("ja", 3, "-") -> "ja-ja-ja"
    Beispiel: wiederhole_wort("ja", 3) -> "ja ja ja"
    """
    # Deine Lösung hier
    pass


def pruefe_zauberwort(eingabe, korrekt):
    """
    A11: Gib True zurück, wenn beide Wörter übereinstimmen, sonst False.
    Groß-/Kleinschreibung und Leerzeichen am Rand spielen keine Rolle.
    Beispiel: pruefe_zauberwort("  SESAM ", "sesam") -> True
    """
    # Deine Lösung hier
    pass


def ist_verfuegbar(titel, regal):
    """
    A12: Gib True zurück, wenn der Titel im Regal (Liste) steht, sonst False.
    Groß-/Kleinschreibung soll egal sein.
    Beispiel: ist_verfuegbar("momo", ["Momo", "Heidi"]) -> True
    """
    # Deine Lösung hier
    pass


def ersetze_vokale(text, ersatz):
    """
    A13: Ersetze jeden Vokal (a, e, i, o, u, groß oder klein) im Text
    durch das Zeichen 'ersatz' und gib das Ergebnis zurück.
    Beispiel: ersetze_vokale("Hallo", "*") -> "H*ll*"
    """
    # Deine Lösung hier
    pass


def berechne_spritmenge(distanz_km, liter_pro_100km):
    """
    A14: Gib zurück, wie viele Liter Sprit für die Strecke gebraucht werden.
    Beispiel: berechne_spritmenge(400, 6.5) -> 26.0
    """
    # Deine Lösung hier
    pass


def gebe_note(punkte, max_punkte):
    """
    A15: Berechne den Prozentwert und gib die Note als Text zurück:
    ab 90% "Sehr gut", ab 75% "Gut", ab 60% "Befriedigend",
    ab 50% "Ausreichend", darunter "Nicht bestanden".
    Beispiel: gebe_note(87, 100) -> "Gut"
    Beispiel: gebe_note(21, 30) -> "Befriedigend"  (70 Prozent)
    """
    # Deine Lösung hier
    pass


def waehrung_umrechnen(betrag, kurs, gebuehr_prozent=0):
    """
    A16: Rechne einen Betrag mit dem Kurs um und ziehe vom Ergebnis die
    Wechselgebühr (in Prozent) ab. Gib den ausgezahlten Betrag zurück.
    Beispiel: waehrung_umrechnen(200, 1.25, 2) -> 245.0
    Beispiel: waehrung_umrechnen(200, 1.25) -> 250.0
    """
    # Deine Lösung hier
    pass


def filtere_zahlen(zahlen, minimum, maximum):
    """
    A17: Gib eine NEUE Liste zurück, die nur die Zahlen zwischen minimum
    und maximum enthält (Grenzen zählen mit).
    Beispiel: filtere_zahlen([1, 5, 9, 12], 4, 10) -> [5, 9]
    """
    # Deine Lösung hier
    pass


def enthaelt_alle(text, zeichen):
    """
    A18 (knifflig): Gib True zurück, wenn ALLE Zeichen aus der Liste
    'zeichen' im Text vorkommen, sonst False. Groß-/Kleinschreibung egal.
    Beispiel: enthaelt_alle("Hallo Welt", ["h", "w"]) -> True
    Beispiel: enthaelt_alle("Hallo Welt", ["h", "z"]) -> False
    """
    # Deine Lösung hier
    pass


# =====================================================================
# TEIL B: Funktionen, die andere Funktionen aufrufen
# =====================================================================
# Schreibe hier KEINE Berechnung doppelt: Nutze die Funktionen aus Teil A!


def berechne_preis_pro_person(anzahl_pizzen, belaege_pro_pizza, personen):
    """
    B1: Die Pizza-Runde wird durch alle Personen geteilt. Gib zurück, was
    jede Person zahlt.
    Nutzt: kalkuliere_bestellung()
    Beispiel: berechne_preis_pro_person(2, 3, 4) -> 6.05
    """
    # Deine Lösung hier
    pass


def reisekosten(distanz_km, liter_pro_100km, spritpreis):
    """
    B2: Gib die Spritkosten der Autofahrt zurück.
    Nutzt: berechne_spritmenge()
    Beispiel: reisekosten(400, 6.5, 2.0) -> 52.0
    """
    # Deine Lösung hier
    pass


def gruppen_kinopreis(alter_liste, ist_mitglied):
    """
    B3: Eine Gruppe geht ins Kino. Gib den Gesamtpreis für alle Personen
    der Altersliste zurück (ist_mitglied gilt für alle).
    Nutzt: bestimme_ticketpreis()
    Beispiel: gruppen_kinopreis([4, 10, 35], False) -> 16.0
    """
    # Deine Lösung hier
    pass


def trinkgeld_pro_person(betrag, personen, trinkgeld_prozent=10):
    """
    B4: Gib zurück, was jede Person zahlt, wenn die Rechnung inklusive
    Trinkgeld durch alle Personen geteilt wird.
    Nutzt: berechne_rechnung()
    Beispiel: trinkgeld_pro_person(80, 4) -> 22.0
    """
    # Deine Lösung hier
    pass


def zeugnis_zeile(name, punkte, max_punkte):
    """
    B5: Gib eine Zeugniszeile als Text zurück.
    Nutzt: gebe_note()
    Beispiel: zeugnis_zeile("Lena", 87, 100) -> "Lena: 87 von 100 Punkten - Gut"
    """
    # Deine Lösung hier
    pass


def verfuegbare_buecher(wunschliste, regal):
    """
    B6: Gib eine Liste mit allen Büchern der Wunschliste zurück, die im
    Regal stehen.
    Nutzt: ist_verfuegbar()
    Beispiel: verfuegbare_buecher(["Momo", "Emil"], ["momo", "Heidi"]) -> ["Momo"]
    """
    # Deine Lösung hier
    pass


def urlaubstage(budget_euro, kurs, tagessatz, gebuehr_prozent=0):
    """
    B7: Du tauschst dein Budget in die Landeswährung um. Wie viele GANZE
    Urlaubstage kannst du dir damit leisten, wenn du pro Tag 'tagessatz'
    (in Landeswährung) ausgibst?
    Nutzt: waehrung_umrechnen()
    Beispiel: urlaubstage(1000, 4.0, 300, 2) -> 13
    """
    # Deine Lösung hier
    pass


def zaehle_im_bereich(zahlen, minimum, maximum):
    """
    B8: Gib zurück, wie viele Zahlen der Liste im Bereich liegen.
    Nutzt: ist_im_bereich()
    Beispiel: zaehle_im_bereich([1, 5, 9, 12], 4, 10) -> 2
    """
    # Deine Lösung hier
    pass


# =====================================================================
# TEIL C: Kleine Programme ohne main()
# =====================================================================
# Hier schreibst du KEINE neuen Funktionen, sondern normalen Code, der
# deine Funktionen aus Teil A/B aufruft. Schreibe den Code direkt unter
# die jeweilige Aufgabe. Bearbeitete Aufgaben laufen beim Start der
# Datei automatisch mit; lass Aufgaben, die du noch nicht machst, leer.

# --- C1: Die Kino-Kasse ---
# Drei Gäste stehen an der Kasse. Frage für jeden das Alter ein und ob er
# Mitglied ist ("j"/"n"). Rufe bestimme_ticketpreis() auf und gib aus:
# "Gast X: Dein Ticket kostet Y Euro." Am Ende soll die Summe aller drei
# Tickets ausgegeben werden.



# --- C2: Der Rezept-Assistent ---
# Frage nach Menge einer Zutat, für wie viele Personen das Rezept gedacht
# ist und für wie viele du kochen möchtest. Rufe rechne_rezept_um() auf
# und gib das Ergebnis aus. Danach fragt das Programm "Noch ein Rezept?
# (j/n)" und wiederholt sich, solange du "j" eingibst.



# --- C3: Das Klassen-Zeugnis ---
# Gegeben ist die Liste namen = ["Lena", "Tom", "Ali"]. Frage für jeden
# Namen die erreichten Punkte ab (maximal 100) und gib mit Hilfe von
# zeugnis_zeile() eine Zeugniszeile aus. Am Ende: Wer hatte die meisten
# Punkte?



# =====================================================================
# TESTBEREICH – hier rufst du deine Funktionen aus Teil A und B auf
# =====================================================================
# Entferne das '#' vor einer Zeile, sobald du die Funktion geschrieben hast.

# print(rechteck_flaeche(3, 4))
# print(berechne_rechnung(50))
# print(bestimme_ticketpreis(10, False))
# print(berechne_radtour(7, 60, 1))
# print(kalkuliere_bestellung(2, 3))
# print(rechne_rezept_um(200, 4, 6))
# print(berechne_alter(1990))
# print(ist_im_bereich(5, 1, 10))
# print(zaehle_buchstabe("Banane", "a"))
# print(wiederhole_wort("ja", 3, "-"))
# print(pruefe_zauberwort("  SESAM ", "sesam"))
# print(ist_verfuegbar("momo", ["Momo", "Heidi"]))
# print(ersetze_vokale("Hallo", "*"))
# print(berechne_spritmenge(400, 6.5))
# print(gebe_note(87, 100))
# print(waehrung_umrechnen(200, 1.25, 2))
# print(filtere_zahlen([1, 5, 9, 12], 4, 10))
# print(enthaelt_alle("Hallo Welt", ["h", "w"]))

# print(berechne_preis_pro_person(2, 3, 4))
# print(reisekosten(400, 6.5, 2.0))
# print(gruppen_kinopreis([4, 10, 35], False))
# print(trinkgeld_pro_person(80, 4))
# print(zeugnis_zeile("Lena", 87, 100))
# print(verfuegbare_buecher(["Momo", "Emil"], ["momo", "Heidi"]))
# print(urlaubstage(1000, 4.0, 300, 2))
# print(zaehle_im_bereich([1, 5, 9, 12], 4, 10))