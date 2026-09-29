"""
Python-Schulung – Tag 7: Mini-Projekt "Mein Bücherregal" – LÖSUNG
==================================================================
Musterlösung mit Schleifen, Listen, Strings, if/else und input.
Es gibt mehrere richtige Wege – das ist nur einer davon.
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

    # ---------- 1: Buch hinzufügen ----------
    if wahl == "1":
        titel = input("Titel: ").strip()
        autor = input("Autor: ").strip()

        if titel == "" or autor == "":
            print("Titel und Autor dürfen nicht leer sein.")
            continue

        # Duplikat-Prüfung: gleicher Titel UND gleicher Autor, Groß/Klein egal
        doppelt = False
        for i in range(len(titel_liste)):
            if titel_liste[i].lower() == titel.lower() and autor_liste[i].lower() == autor.lower():
                doppelt = True

        if doppelt:
            print("Dieses Buch steht schon im Regal.")
            continue

        titel_liste.append(titel)
        autor_liste.append(autor)
        status_liste.append("ungelesen")
        bewertung_liste.append(0)
        print(f"'{titel}' wurde als Nr. {len(titel_liste)} hinzugefügt.")

    # ---------- 2: Regal anzeigen ----------
    elif wahl == "2":
        if len(titel_liste) == 0:
            print("Das Regal ist leer.")
            continue

        print("\n--- Ungelesen ---")
        anzahl_ungelesen = 0
        for i in range(len(titel_liste)):
            if status_liste[i] == "ungelesen":
                print(f"#{i + 1} {titel_liste[i]} – {autor_liste[i]}")
                anzahl_ungelesen += 1
        if anzahl_ungelesen == 0:
            print("(keine)")

        print("\n--- Gelesen ---")
        anzahl_gelesen = 0
        for i in range(len(titel_liste)):
            if status_liste[i] == "gelesen":
                sterne = "★" * bewertung_liste[i] + "☆" * (5 - bewertung_liste[i])
                print(f"#{i + 1} {titel_liste[i]} – {autor_liste[i]}  {sterne}")
                anzahl_gelesen += 1
        if anzahl_gelesen == 0:
            print("(keine)")

    # ---------- 3: Bücher suchen ----------
    elif wahl == "3":
        stichwort = input("Stichwort: ").strip().lower()
        if stichwort == "":
            print("Bitte ein Stichwort eingeben.")
            continue

        treffer = 0
        for i in range(len(titel_liste)):
            if stichwort in titel_liste[i].lower() or stichwort in autor_liste[i].lower():
                print(f"#{i + 1} {titel_liste[i]} – {autor_liste[i]} ({status_liste[i]})")
                treffer += 1

        if treffer == 0:
            print("Keine Treffer.")

    # ---------- 4: Buch als gelesen markieren ----------
    elif wahl == "4":
        nummer_text = input("Nummer des Buches: ").strip()

        if not nummer_text.isdigit():
            print("Bitte eine Zahl eingeben.")
            continue

        nummer = int(nummer_text)
        if nummer < 1 or nummer > len(titel_liste):
            print("Dieses Buch gibt es nicht.")
            continue

        index = nummer - 1
        if status_liste[index] == "gelesen":
            print("Dieses Buch hast du schon als gelesen markiert.")
            continue

        # Bewertung so lange abfragen, bis sie gültig ist
        bewertung = 0
        while bewertung < 1 or bewertung > 5:
            eingabe = input("Bewertung (1-5): ").strip()
            if eingabe.isdigit():
                bewertung = int(eingabe)
            if bewertung < 1 or bewertung > 5:
                print("Bitte eine Zahl von 1 bis 5 eingeben.")

        status_liste[index] = "gelesen"
        bewertung_liste[index] = bewertung
        print(f"'{titel_liste[index]}' ist jetzt als gelesen markiert.")

    # ---------- 5: Statistik ----------
    elif wahl == "5":
        gelesen = 0
        ungelesen = 0
        summe = 0
        beste_note = 0
        bester_index = -1

        for i in range(len(titel_liste)):
            if status_liste[i] == "gelesen":
                gelesen += 1
                summe += bewertung_liste[i]
                if bewertung_liste[i] > beste_note:
                    beste_note = bewertung_liste[i]
                    bester_index = i
            else:
                ungelesen += 1

        print(f"\nGelesen: {gelesen} | Ungelesen: {ungelesen}")

        if gelesen == 0:
            print("Noch keine gelesenen Bücher – keine Bewertung möglich.")
        else:
            durchschnitt = summe / gelesen
            print(f"Durchschnittsbewertung: {durchschnitt:.1f} von 5")
            print(f"Bestbewertet: {titel_liste[bester_index]} – {autor_liste[bester_index]} ({beste_note} Sterne)")

    # ---------- 0: Beenden ----------
    elif wahl == "0":
        ungelesen = 0
        for status in status_liste:
            if status == "ungelesen":
                ungelesen += 1

        if ungelesen > 0:
            antwort = input(f"Noch ungelesene Bücher im Regal: {ungelesen}. Wirklich beenden? (j/n) ").strip().lower()
            if antwort != "j":
                continue

        print("Bis bald und viel Spaß beim Lesen!")
        break

    else:
        print("Ungültige Auswahl – bitte 0 bis 5 eingeben.")