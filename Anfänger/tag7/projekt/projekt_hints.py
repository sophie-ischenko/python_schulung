"""
Python-Schulung – Tag 7: Mini-Projekt "Mein Bücherregal"
=========================================================
Du baust eine kleine Bücherverwaltung für die Konsole. Das Menü ist schon
fertig – die Funktionen dahinter baust du selbst.

Genutzte Werkzeuge: input, Listen, Strings, if/else, while, for

Mindestanforderungen
--------------------
1 - Buch hinzufügen
    - Titel und Autor dürfen nicht leer sein (Leerzeichen am Rand entfernen)
    - Dasselbe Buch (gleicher Titel, Groß/Klein egal) darf nicht doppelt
      im Regal stehen
    - Neue Bücher sind zuerst "ungelesen" und haben noch keine Bewertung
2 - Regal anzeigen
    - Erst alle ungelesenen, dann alle gelesenen Bücher
    - Format ungelesen:  #2 Momo – Michael Ende
    - Format gelesen:    #1 Der Vorleser – Bernhard Schlink  ★★★★☆
3 - Bücher suchen
    - Der Nutzer gibt ein Stichwort ein, alle Bücher mit diesem Stichwort
      im Titel ODER beim Autor werden angezeigt (Groß/Klein egal)
    - Keine Treffer -> passende Meldung
4 - Buch als gelesen markieren
    - Nutzer gibt die Buchnummer ein
    - Eingabe prüfen: Ist es eine Zahl? Gibt es das Buch? Ist es schon
      gelesen? -> jeweils eigene Meldung
    - Danach Bewertung von 1 bis 5 abfragen (so lange, bis sie gültig ist)
5 - Statistik
    - Wie viele Bücher sind gelesen, wie viele ungelesen?
    - Durchschnittsbewertung aller gelesenen Bücher (ohne sum())
    - Welches Buch hat die beste Bewertung?
0 - Beenden
    - Wenn noch ungelesene Bücher im Regal stehen, vorher nachfragen:
      "Wirklich beenden? (j/n)"

Bonus
-----
- Titel und Autor automatisch mit großen Anfangsbuchstaben speichern
- Ein Buch wieder auf "ungelesen" setzen können
- Anzeige "Du hast X von Y Büchern gelesen (Z %)"
- Alle Bücher eines bestimmten Autors zählen
"""

# Vier Listen gehören zusammen: Der Index verbindet die Daten.
# Buch Nr. 1 liegt an Index 0 -> titel_liste[0], autor_liste[0], ...
titel_liste = []
autor_liste = []
status_liste = []          # "ungelesen" oder "gelesen"
bewertung_liste = []       # 0 = noch keine Bewertung, sonst 1 bis 5


while True:
    print("\n=== MEIN BÜCHERREGAL ===")
    print("1 - Buch hinzufügen")
    print("2 - Regal anzeigen")
    print("3 - Bücher suchen")
    print("4 - Buch als gelesen markieren")
    print("5 - Statistik")
    print("0 - Beenden")
    wahl = input("Auswahl: ").strip()

    if wahl == "1":
        # TODO: Titel und Autor einlesen und prüfen (nicht leer, kein Duplikat)
        # TODO: In alle vier Listen eintragen (Status "ungelesen", Bewertung 0)
        # Tipp: Duplikat-Prüfung -> for-Schleife über titel_liste, .lower() nutzen
        pass

    elif wahl == "2":
        # TODO: Wenn das Regal leer ist -> Meldung
        # TODO: Erst alle ungelesenen, dann alle gelesenen Bücher ausgeben
        # Tipp: zwei for-Schleifen über range(len(titel_liste)),
        #       Sterne mit "★" * bewertung + "☆" * (5 - bewertung)
        pass

    elif wahl == "3":
        # TODO: Stichwort einlesen, Titel UND Autor durchsuchen (in-Operator)
        # TODO: Treffer zählen, damit du "Keine Treffer" ausgeben kannst
        pass

    elif wahl == "4":
        # TODO: Nummer als Text einlesen -> mit .isdigit() prüfen -> int()
        # TODO: Bereich prüfen (1 bis len(titel_liste))
        # TODO: Status prüfen; wenn ungelesen: Bewertung 1-5 per while abfragen
        # Achtung: Buch Nr. 1 liegt an Index 0!
        pass

    elif wahl == "5":
        # TODO: Gelesene und ungelesene Bücher zählen
        # TODO: Durchschnittsbewertung berechnen (Achtung: Division durch 0!)
        # TODO: Bestbewertetes Buch finden (Index merken)
        pass

    elif wahl == "0":
        # TODO: Ungelesene Bücher zählen; wenn > 0, nachfragen
        # Bei "n" -> zurück ins Menü (continue), sonst break
        print("Bis bald und viel Spaß beim Lesen!")
        break

    else:
        print("Ungültige Auswahl – bitte 0 bis 5 eingeben.")