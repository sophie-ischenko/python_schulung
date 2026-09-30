"""
Python-Schulung – Tag 7: Mini-Projekt "Mein Bücherregal"
=========================================================
Du baust eine kleine Bücherverwaltung für die Konsole. Das Menü ist schon
fertig – die Funktionen dahinter baust du selbst.

Genutzte Werkzeuge: input, Listen, Strings, if/else, while, for

Anforderungen
-------------
1 - Buch hinzufügen
    - Titel und Autor dürfen nicht leer sein
    - Ein Buch darf nicht doppelt im Regal stehen (Groß-/Kleinschreibung egal)
    - Neue Bücher sind zuerst "ungelesen" und noch nicht bewertet
2 - Regal anzeigen
    - Erst alle ungelesenen, dann alle gelesenen Bücher
    - Ungelesen:  #2 Momo – Michael Ende
    - Gelesen:    #1 Der Vorleser – Bernhard Schlink  ★★★★☆
3 - Bücher suchen
    - Stichwort im Titel oder beim Autor (Groß-/Kleinschreibung egal)
4 - Buch als gelesen markieren
    - Mit Bewertung von 1 bis 5
    - Ungültige Eingaben und unpassende Bücher werden abgefangen
5 - Statistik
    - Anzahl gelesen / ungelesen
    - Durchschnittsbewertung der gelesenen Bücher
    - Bestbewertetes Buch
0 - Beenden
    - Wenn noch ungelesene Bücher im Regal stehen, vorher nachfragen

Bonus
-----
- Titel und Autor mit großen Anfangsbuchstaben speichern
- Ein Buch wieder auf "ungelesen" setzen können
- Anzeige "Du hast X von Y Büchern gelesen (Z %)"
- Alle Bücher eines Autors zählen
"""

# Diese Listen gehören zusammen: Der Index verbindet die Daten.
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
        # TODO
        pass

    elif wahl == "2":
        # TODO
        pass

    elif wahl == "3":
        # TODO
        pass

    elif wahl == "4":
        # TODO
        pass

    elif wahl == "5":
        # TODO
        pass

    elif wahl == "0":
        # TODO: Nachfrage, falls noch ungelesene Bücher da sind
        print("Bis bald und viel Spaß beim Lesen!")
        break

    else:
        print("Ungültige Auswahl – bitte 0 bis 5 eingeben.")