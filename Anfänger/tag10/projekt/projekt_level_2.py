"""
Python-Schulung – Tag 7: Mini-Projekt "Mein Bücherregal"
=========================================================
Du baust eine kleine Bücherverwaltung für die Konsole. Das Menü ist schon
fertig – die Funktionen dahinter baust du selbst.

Genutzte Werkzeuge: input, Listen, Strings, if/else, while, for

Anforderungen
-------------
1 - Buch hinzufügen
    - Titel und Autor dürfen nicht leer sein (Leerzeichen am Rand entfernen)
    - Ein Buch darf nicht doppelt im Regal stehen (Groß-/Kleinschreibung egal)
    - Neue Bücher sind zuerst "ungelesen" und noch nicht bewertet
2 - Regal anzeigen
    - Erst alle ungelesenen, dann alle gelesenen Bücher
    - Ungelesen:  #2 Momo – Michael Ende
    - Gelesen:    #1 Der Vorleser – Bernhard Schlink  ★★★★☆
3 - Bücher suchen
    - Stichwort im Titel oder beim Autor (Groß-/Kleinschreibung egal)
    - Keine Treffer -> passende Meldung
4 - Buch als gelesen markieren
    - Mit Bewertung von 1 bis 5 (so lange fragen, bis die Eingabe gültig ist)
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
        # TODO: Eingaben prüfen (leer? doppelt?), dann in alle vier Listen eintragen
        # Tipp: Für die Duplikat-Prüfung brauchst du eine Schleife und solltest bei der Prüfung die Groß-/Kleinschreibung ignorieren
        pass

    elif wahl == "2":
        # TODO: Zwei Durchgänge: erst ungelesene, dann gelesene Bücher ausgeben
        # Tipp: Strings lassen sich mit einer Zahl multiplizieren
        pass

    elif wahl == "3":
        # TODO: Alle Bücher durchgehen und Treffer zählen
        # Tipp: Prüfe, ob ein Text in einem anderen steckt
        pass

    elif wahl == "4":
        # TODO: Nummer prüfen (Zahl? vorhanden? schon gelesen?), dann bewerten
        # Tipp: Buch Nr. 1 liegt an Index 0; prüfe auch, ob ein Text eine Zahl ist
        pass

    elif wahl == "5":
        # TODO: Zählen, Summe bilden und das beste Buch merken
        # Tipp: Denk an den Fall, dass noch nichts gelesen wurde
        pass

    elif wahl == "0":
        # TODO: Nachfrage, falls noch ungelesene Bücher da sind
        print("Bis bald und viel Spaß beim Lesen!")
        break

    else:
        print("Ungültige Auswahl – bitte 0 bis 5 eingeben.")