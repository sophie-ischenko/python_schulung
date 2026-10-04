"""
Tag 1 – Aufgaben: Die Missionen der Code-Akademie

LÖSUNG

Themen:
- Strings
- String-Methoden
- Indizes und Slicing
- split() und join()
- f-Strings
- Listen
- Listen verändern und durchsuchen
- Schleifen über Listen
- Listen filtern
- Funktionen mit Strings und Listen
"""


# ============================================================
# HILFSFUNKTION
# ============================================================

def check(name, erhalten, erwartet):
    """Vergleicht Ergebnis und Erwartung und gibt ✓ oder ✗ aus."""
    if erhalten == erwartet:
        print(f"✓ {name}")
    else:
        print(
            f"✗ {name} → "
            f"erwartet {erwartet!r}, "
            f"erhalten {erhalten!r}"
        )


# ============================================================
# MISSION 1: STRING-ANALYSE
# ============================================================

def bereinige_text(text):
    """
    Entfernt Leerzeichen am Anfang und Ende
    und schreibt den Text klein.
    """
    return text.strip().lower()


def normalisiere_name(name):
    """
    Bereinigt einen Namen und vereinheitlicht die Schreibweise.
    """
    woerter = name.split()
    name = " ".join(woerter)

    return name.title()


def erste_und_letzte_zeichen(text):
    """
    Gibt erstes und letztes Zeichen zurück.
    """
    return f"{text[0]}{text[-1]}"


def rueckwaerts(text):
    """
    Gibt den Text rückwärts zurück.
    """
    return text[::-1]


def zaehle_zeichen(text, zeichen):
    """
    Zählt, wie oft ein Zeichen vorkommt.
    """
    anzahl = 0

    for element in text:
        if element == zeichen:
            anzahl += 1

    return anzahl


# ★ Zusatzaufgabe
def geheimnisvolle_laenge(text):
    """
    Gibt die Länge des Textes ohne Leerzeichen zurück.
    """
    ohne_leerzeichen = text.replace(" ", "")

    return len(ohne_leerzeichen)


# ============================================================
# MISSION 2: GEHEIMSCHRIFT
# ============================================================

def initialen(name):
    """
    Erzeugt die Initialen eines Namens.
    """
    woerter = name.split()
    initialen_liste = []

    for wort in woerter:
        initiale = wort[0].upper()
        initialen_liste.append(initiale)

    return ".".join(initialen_liste) + "."


def teile_nachricht(nachricht):
    """
    Zerlegt eine Nachricht in einzelne Wörter.
    """
    return nachricht.split()


def verbinde_nachricht(woerter):
    """
    Verbindet eine Liste von Wörtern zu einem Satz.
    """
    return " ".join(woerter)


def ersetze_umlaute(text):
    """
    Ersetzt deutsche Sonderzeichen.
    """
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")

    text = text.replace("Ä", "Ae")
    text = text.replace("Ö", "Oe")
    text = text.replace("Ü", "Ue")

    text = text.replace("ß", "ss")

    return text


def maskiere_email(email):
    """
    Versteckt den Namen einer E-Mail-Adresse.
    """
    teile = email.split("@")

    name = teile[0]
    domain = teile[1]

    maskierter_name = name[0] + "*" * (len(name) - 1)

    return maskierter_name + "@" + domain


def baue_funkmeldung(agent, ort, status):
    """
    Erstellt eine Funkmeldung.
    """
    return (
        f"Agentin {agent} befindet sich in {ort}. "
        f"Status: {status}."
    )


# ★ Zusatzaufgabe
def geheimschrift(text):
    """
    Schreibt den gesamten Text groß.
    """
    return text.upper()


# ============================================================
# MISSION 3: GEHEIME LISTEN
# ============================================================

def fuege_agent_hinzu(agenten, name):
    """
    Fügt einen Agenten am Ende der Liste hinzu.
    """
    agenten.append(name)


def entferne_agent(agenten, name):
    """
    Entfernt einen Agenten aus der Liste.
    """
    agenten.remove(name)

    return agenten


def enthaelt_agent(agenten, name):
    """
    Prüft unabhängig von Groß- und Kleinschreibung,
    ob ein Agent vorhanden ist.
    """
    name = name.lower()

    for agent in agenten:
        if agent.lower() == name:
            return True

    return False


def zaehle_agenten(agenten):
    """
    Gibt die Anzahl der Agenten zurück.
    """
    return len(agenten)


def filtere_agenten(agenten, suchbegriff):
    """
    Gibt alle Agenten zurück, die den Suchbegriff enthalten.
    """
    suchbegriff = suchbegriff.lower()
    treffer = []

    for agent in agenten:
        if suchbegriff in agent.lower():
            treffer.append(agent)

    return treffer


def laengstes_wort(woerter):
    """
    Gibt das längste Wort der Liste zurück.
    """
    laengstes = ""

    for wort in woerter:
        if len(wort) > len(laengstes):
            laengstes = wort

    return laengstes


def ohne_duplikate(liste):
    """
    Entfernt doppelte Werte und erhält die ursprüngliche Reihenfolge.
    """
    ergebnis = []

    for wert in liste:
        if wert not in ergebnis:
            ergebnis.append(wert)

    return ergebnis


# ★ Zusatzaufgabe
def jedes_zweite(liste):
    """
    Gibt jedes zweite Element zurück,
    beginnend beim ersten.
    """
    return liste[::2]


# ============================================================
# MISSION 4: AGENTENKARTEI
# ============================================================

def erstelle_agent(vorname, nachname, codename):
    """
    Erstellt einen Agenten als Liste.
    """
    return [vorname, nachname, codename]


def agenten_name(agent):
    """
    Baut den vollständigen Namen aus der Agentenliste.
    """
    name = [agent[0], agent[1]]

    return " ".join(name)


def agenten_ausweis(agent):
    """
    Erstellt einen mehrzeiligen Agentenausweis.
    """
    zeilen = [
        "=====================",
        "    AGENTENAUSWEIS",
        "=====================",
        f"Name: {agenten_name(agent)}",
        f"Codename: {agent[2]}",
    ]

    return "\n".join(zeilen)


def finde_agent(agenten, suchbegriff):
    """
    Sucht im Vor-, Nachnamen und Codenamen.
    """
    suchbegriff = suchbegriff.lower()
    treffer = []

    for agent in agenten:
        vorname = agent[0].lower()
        nachname = agent[1].lower()
        codename = agent[2].lower()

        if (
            suchbegriff in vorname
            or suchbegriff in nachname
            or suchbegriff in codename
        ):
            treffer.append(agent)

    return treffer


def codenamen(agenten):
    """
    Erstellt eine Liste mit allen Codenamen.
    """
    ergebnis = []

    for agent in agenten:
        ergebnis.append(agent[2])

    return ergebnis


def agenten_anzeigen(agenten):
    """
    Gibt alle Agenten übersichtlich aus.
    """
    for agent in agenten:
        print(
            f"{agenten_name(agent)} | "
            f"{agent[2]}"
        )


# ★ Zusatzaufgabe
def agenten_sortieren(agenten):
    """
    Gibt eine sortierte Kopie der Agentenliste zurück.

    Die ursprüngliche Liste wird nicht verändert.
    """
    return sorted(agenten)


# ============================================================
# TESTS
# ============================================================

if __name__ == "__main__":

    print()
    print("==========================================")
    print("   MISSION 1: STRING-ANALYSE")
    print("==========================================")

    check(
        "1 bereinige_text",
        bereinige_text("  SERVER-01  "),
        "server-01"
    )

    check(
        "2 normalisiere_name",
        normalisiere_name("  aDA   loVELACE "),
        "Ada Lovelace"
    )

    check(
        "3 erste_und_letzte_zeichen",
        erste_und_letzte_zeichen("AGENT"),
        "AT"
    )

    check(
        "4 rueckwaerts",
        rueckwaerts("AGENT"),
        "TNEGA"
    )

    check(
        "5 zaehle_zeichen",
        zaehle_zeichen("Banane", "a"),
        3
    )

    check(
        "6 ★ geheimnisvolle_laenge",
        geheimnisvolle_laenge("Code Akademie"),
        12
    )

    print()
    print("==========================================")
    print("   MISSION 2: GEHEIMSCHRIFT")
    print("==========================================")

    check(
        "7 initialen",
        initialen("Ada Lovelace"),
        "A.L."
    )

    check(
        "8 teile_nachricht",
        teile_nachricht("Treffe mich um acht"),
        ["Treffe", "mich", "um", "acht"]
    )

    check(
        "9 verbinde_nachricht",
        verbinde_nachricht(
            ["Treffe", "mich", "um", "acht"]
        ),
        "Treffe mich um acht"
    )

    check(
        "10 ersetze_umlaute",
        ersetze_umlaute("Größe: Übung für Äpfel"),
        "Groesse: Uebung fuer Aepfel"
    )

    check(
        "11 maskiere_email",
        maskiere_email("ada@beispiel.de"),
        "a**@beispiel.de"
    )

    check(
        "12 baue_funkmeldung",
        baue_funkmeldung(
            "Ada",
            "Berlin",
            "einsatzbereit"
        ),
        "Agentin Ada befindet sich in Berlin. Status: einsatzbereit."
    )

    check(
        "13 ★ geheimschrift",
        geheimschrift("geheimer funk"),
        "GEHEIMER FUNK"
    )

    print()
    print("==========================================")
    print("   MISSION 3: GEHEIME LISTEN")
    print("==========================================")

    agenten = ["Ada", "Alan"]

    fuege_agent_hinzu(agenten, "Grace")

    check(
        "14 fuege_agent_hinzu",
        agenten,
        ["Ada", "Alan", "Grace"]
    )

    check(
        "15 entferne_agent",
        entferne_agent(agenten, "Alan"),
        ["Ada", "Grace"]
    )

    check(
        "16 enthaelt_agent",
        enthaelt_agent(agenten, "ada"),
        True
    )

    check(
        "17 enthaelt_agent nicht vorhanden",
        enthaelt_agent(agenten, "Turing"),
        False
    )

    check(
        "18 zaehle_agenten",
        zaehle_agenten(agenten),
        2
    )

    check(
        "19 filtere_agenten",
        filtere_agenten(
            [
                "Ada Lovelace",
                "Alan Turing",
                "Grace Hopper"
            ],
            "a"
        ),
        [
            "Ada Lovelace",
            "Alan Turing",
            "Grace Hopper"
        ]
    )

    check(
        "20 laengstes_wort",
        laengstes_wort(
            ["Agent", "Geheimcode", "Funk", "Passwort"]
        ),
        "Geheimcode"
    )

    check(
        "21 laengstes_wort leer",
        laengstes_wort([]),
        ""
    )

    check(
        "22 ohne_duplikate",
        ohne_duplikate(
            [3, 1, 3, 2, 1]
        ),
        [3, 1, 2]
    )

    check(
        "23 ★ jedes_zweite",
        jedes_zweite([1, 2, 3, 4, 5]),
        [1, 3, 5]
    )

    print()
    print("==========================================")
    print("   MISSION 4: AGENTENKARTEI")
    print("==========================================")

    ada = erstelle_agent(
        "Ada",
        "Lovelace",
        "Falke"
    )

    alan = erstelle_agent(
        "Alan",
        "Turing",
        "Nebel"
    )

    grace = erstelle_agent(
        "Grace",
        "Hopper",
        "Schatten"
    )

    test_agenten = [ada, alan, grace]

    check(
        "24 erstelle_agent",
        ada,
        ["Ada", "Lovelace", "Falke"]
    )

    check(
        "25 agenten_name",
        agenten_name(ada),
        "Ada Lovelace"
    )

    ausweis = agenten_ausweis(ada)

    check(
        "26 agenten_ausweis enthält Name",
        "Ada Lovelace" in ausweis,
        True
    )

    check(
        "27 agenten_ausweis enthält Codename",
        "Falke" in ausweis,
        True
    )

    check(
        "28 finde_agent",
        finde_agent(test_agenten, "fal"),
        [ada]
    )

    check(
        "29 finde_agent Nachname",
        finde_agent(test_agenten, "turing"),
        [alan]
    )

    check(
        "30 codenamen",
        codenamen(test_agenten),
        ["Falke", "Nebel", "Schatten"]
    )

    print()
    print("31 agenten_anzeigen:")
    agenten_anzeigen(test_agenten)

    sortierte = agenten_sortieren(
        [
            ["Grace", "Hopper", "Schatten"],
            ["Alan", "Turing", "Nebel"],
            ["Ada", "Lovelace", "Falke"],
        ]
    )

    check(
        "32 ★ agenten_sortieren",
        sortierte,
        [
            ["Ada", "Lovelace", "Falke"],
            ["Grace", "Hopper", "Schatten"],
            ["Alan", "Turing", "Nebel"],
        ]
    )

    print()
    print("==========================================")
    print("   ALLE MISSIONEN ABGESCHLOSSEN")
    print("==========================================")