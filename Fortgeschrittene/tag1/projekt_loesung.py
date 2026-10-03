
"""
Tag 1 – Projektlösung: Agentenverwaltung
"""

import random


CODE_VORNAMEN = [
    "Falke",
    "Nebel",
    "Schatten",
    "Blitz",
    "Mondlicht",
    "Kolibri",
    "Eisen",
    "Panda",
]

AUFTRAEGE = [
    "Finde heraus, wer das letzte Stück Kuchen genommen hat.",
    "Entschlüssele die Nachricht auf dem Kaffeebecher.",
    "Beschatte den Drucker.",
    "Rette das WLAN vor dem Kabelsalat.",
]

agenten = []


def codename(vorname, nachname):
    """
    Erzeugt einen Codenamen aus Vor- und Nachnamen.
    """
    rueckwaerts = nachname[::-1]
    nummer = len(vorname) * len(nachname)

    return f"{rueckwaerts.capitalize()}-{nummer}"


def agent_erstellen(vorname, nachname, alter):
    """
    Erstellt einen Agenten als Liste.
    """
    vorname = vorname.strip().title()
    nachname = nachname.strip().title()

    return [
        vorname,
        nachname,
        alter,
        codename(vorname, nachname),
    ]


def agent_anzeigen(agent):
    """
    Gibt einen Agenten kompakt aus.
    """
    vorname = agent[0]
    nachname = agent[1]
    alter = agent[2]
    codename_agent = agent[3]

    print(
        f"{vorname} {nachname} | "
        f"{codename_agent} | "
        f"{alter} Jahre"
    )


def agent_suchen(agenten, suchbegriff):
    """
    Sucht im Vor- und Nachnamen nach einem Suchbegriff.
    """
    suchbegriff = suchbegriff.strip().lower()
    treffer = []

    for agent in agenten:
        vorname = agent[0].lower()
        nachname = agent[1].lower()

        if suchbegriff in vorname or suchbegriff in nachname:
            treffer.append(agent)

    return treffer


def agenten_filtern_nach_alter(agenten, mindestalter):
    """
    Gibt nur Agenten zurück, die mindestens so alt sind
    wie das angegebene Mindestalter.
    """
    ergebnis = []

    for agent in agenten:
        if agent[2] >= mindestalter:
            ergebnis.append(agent)

    return ergebnis


def ausweis_erstellen(agent):
    """
    Erstellt einen mehrzeiligen Agentenausweis.
    """
    vorname = agent[0]
    nachname = agent[1]
    alter = agent[2]
    codename_agent = agent[3]

    deckname = random.choice(CODE_VORNAMEN)
    auftrag = random.choice(AUFTRAEGE)

    zeilen = [
        "=========================",
        "     AGENTENAUSWEIS",
        "=========================",
        f"Name:      {vorname} {nachname}",
        f"Codename:  {codename_agent}",
        f"Alter:     {alter} Jahre",
        f"Deckname:  {deckname}",
        f"Auftrag:   {auftrag}",
    ]

    return "\n".join(zeilen)


def agent_aufnehmen():
    """
    Fragt die Daten eines neuen Agenten ab und speichert ihn.
    """
    print("\n--- Neuer Agent ---")

    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    alter = int(input("Alter: "))

    agent = agent_erstellen(vorname, nachname, alter)
    agenten.append(agent)

    print("\nAgent wurde aufgenommen.")
    agent_anzeigen(agent)


def alle_agenten_anzeigen():
    """
    Gibt alle gespeicherten Agenten aus.
    """
    print("\n--- Agentenkartei ---")

    if len(agenten) == 0:
        print("Keine Agenten vorhanden.")
        return

    for agent in agenten:
        agent_anzeigen(agent)


def agent_suche_starten():
    """
    Führt eine Suche über das Menü durch.
    """
    suchbegriff = input("\nSuchbegriff: ")

    treffer = agent_suchen(agenten, suchbegriff)

    print("\n--- Suchergebnisse ---")

    if len(treffer) == 0:
        print("Keine Agenten gefunden.")
        return

    for agent in treffer:
        agent_anzeigen(agent)


def agenten_nach_alter_anzeigen():
    """
    Zeigt Agenten ab einem bestimmten Alter.
    """
    mindestalter = int(input("\nMindestalter: "))

    treffer = agenten_filtern_nach_alter(
        agenten,
        mindestalter
    )

    print(f"\n--- Agenten ab {mindestalter} Jahren ---")

    if len(treffer) == 0:
        print("Keine passenden Agenten gefunden.")
        return

    for agent in treffer:
        agent_anzeigen(agent)


def ausweis_anzeigen():
    """
    Zeigt den vollständigen Ausweis eines gesuchten Agenten.
    """
    suchbegriff = input("\nName des Agenten: ")

    treffer = agent_suchen(agenten, suchbegriff)

    if len(treffer) == 0:
        print("Kein Agent gefunden.")
        return

    agent = treffer[0]

    print()
    print(ausweis_erstellen(agent))


def check():
    """
    Selbsttests für die wichtigsten Funktionen.
    """
    agent = agent_erstellen(
        "  ada ",
        " lovelace  ",
        36
    )

    assert agent[0] == "Ada"
    assert agent[1] == "Lovelace"
    assert agent[2] == 36
    assert agent[3] == "Ecal EvoL-56" or agent[3] == "Ecal EvoL-56"

    test_agenten = [
        agent,
        agent_erstellen("Alan", "Turing", 41),
        agent_erstellen("Grace", "Hopper", 85),
    ]

    treffer = agent_suchen(test_agenten, "ADA")

    assert len(treffer) == 1
    assert treffer[0][0] == "Ada"

    treffer = agent_suchen(test_agenten, "ing")

    assert len(treffer) == 1
    assert treffer[0][1] == "Turing"

    volljaehrig = agenten_filtern_nach_alter(
        test_agenten,
        40
    )

    assert len(volljaehrig) == 2

    ausweis = ausweis_erstellen(agent)

    assert "Ada Lovelace" in ausweis
    assert "36 Jahre" in ausweis
    assert "Codename:" in ausweis
    assert "Deckname:" in ausweis
    assert "Auftrag:" in ausweis

    print("Alle Tests bestanden.")


def startdaten_laden():
    """
    Legt einige Beispielagenten für den Start an.
    """
    agenten.append(
        agent_erstellen("Ada", "Lovelace", 36)
    )

    agenten.append(
        agent_erstellen("Alan", "Turing", 41)
    )

    agenten.append(
        agent_erstellen("Grace", "Hopper", 85)
    )

    agenten.append(
        agent_erstellen("Katherine", "Johnson", 101)
    )

    agenten.append(
        agent_erstellen("Dennis", "Ritchie", 70)
    )


def main():
    """
    Hauptprogramm.
    """
    startdaten_laden()

    while True:
        print()
        print("==============================")
        print("   CODE-AKADEMIE")
        print("   AGENTENVERWALTUNG")
        print("==============================")
        print()
        print("1. Agent aufnehmen")
        print("2. Alle Agenten anzeigen")
        print("3. Agent suchen")
        print("4. Agenten nach Alter filtern")
        print("5. Agentenausweis anzeigen")
        print("6. Beenden")

        auswahl = input("\nAuswahl: ").strip()

        if auswahl == "1":
            agent_aufnehmen()

        elif auswahl == "2":
            alle_agenten_anzeigen()

        elif auswahl == "3":
            agent_suche_starten()

        elif auswahl == "4":
            agenten_nach_alter_anzeigen()

        elif auswahl == "5":
            ausweis_anzeigen()

        elif auswahl == "6":
            print("\nDie Agentenverwaltung wird beendet.")
            break

        else:
            print("\nUngültige Auswahl.")


if __name__ == "__main__":
    check()
    main()
