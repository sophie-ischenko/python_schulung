
"""
Tag 1 – Aufgaben: Die Missionen der Code-Akademie

Du bist Agent:in in Ausbildung.

Heute geht es ausschließlich um:
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

Vier Missionen:

    Mission 1  String-Analyse
    Mission 2  Geheimschrift
    Mission 3  Geheime Listen
    Mission 4  Agentenkartei

Aufgaben mit ★ sind Zusatzaufgaben für Schnelle.

Starte die Datei:
Am Ende siehst du, welche Missionen schon geschafft sind (✓ / ✗).
"""


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
# MISSION 1: String-Analyse
# ============================================================

def bereinige_text(text):
    """
    Entfernt Leerzeichen am Anfang und Ende und
    schreibt den Text komplett klein.

    Beispiel:
        "  SERVER-01  " → "server-01"
    """
    # TODO:
    # 1. Leerzeichen mit .strip() entfernen
    # 2. Mit .lower() klein schreiben
    pass


def normalisiere_name(name):
    """
    Bereinigt einen Namen.

    Mehrere Leerzeichen sollen auf ein Leerzeichen
    reduziert werden und jedes Wort soll mit einem
    Großbuchstaben beginnen.

    Beispiel:
        "  aDA   loVELACE "
        → "Ada Lovelace"
    """
    # TODO:
    # 1. Mit .split() in Wörter zerlegen
    # 2. Mit " ".join(...) wieder zusammensetzen
    # 3. .title() verwenden
    pass


def erste_und_letzte_zeichen(text):
    """
    Gibt erstes und letztes Zeichen als String zurück.

    Beispiel:
        "AGENT" → "AT"
    """
    # TODO:
    # Erstes Zeichen: [0]
    # Letztes Zeichen: [-1]
    # Beide mit einem f-String verbinden
    pass


def rueckwaerts(text):
    """
    Gibt einen Text rückwärts zurück.

    Beispiel:
        "AGENT" → "TNEGA"
    """
    # TODO:
    # Slicing mit [::-1]
    pass


def zaehle_zeichen(text, zeichen):
    """
    Gibt zurück, wie oft ein bestimmtes Zeichen
    im Text vorkommt.

    Beispiel:
        zaehle_zeichen("Banane", "a") → 3
    """
    # TODO:
    # Verwende eine Schleife und zähle passende Zeichen.
    pass


# ★ Zusatzaufgabe
def geheimnisvolle_laenge(text):
    """
    Gibt die Länge des Textes ohne Leerzeichen zurück.

    Beispiel:
        "Code Akademie" → 12
    """
    # TODO:
    # Leerzeichen entfernen oder beim Durchlaufen ignorieren.
    pass


# ============================================================
# MISSION 2: Geheimschrift
# ============================================================

def initialen(name):
    """
    Erzeugt die Initialen eines Namens.

    Beispiel:
        "Ada Lovelace" → "A.L."
    """
    # TODO:
    # 1. Name mit .split() zerlegen
    # 2. Von jedem Wort den ersten Buchstaben nehmen
    # 3. Groß schreiben
    # 4. Mit "." verbinden
    # 5. Am Ende einen Punkt ergänzen
    pass


def teile_nachricht(nachricht):
    """
    Zerlegt eine Nachricht in einzelne Wörter.

    Beispiel:
        "Treffe mich um acht"
        → ["Treffe", "mich", "um", "acht"]
    """
    # TODO:
    # split() verwenden
    pass


def verbinde_nachricht(woerter):
    """
    Verbindet eine Liste von Wörtern wieder zu einem Satz.

    Beispiel:
        ["Treffe", "mich", "um", "acht"]
        → "Treffe mich um acht"
    """
    # TODO:
    # join() verwenden
    pass


def ersetze_umlaute(text):
    """
    Ersetzt deutsche Sonderzeichen:

        ä → ae
        ö → oe
        ü → ue
        ß → ss

    Auch Großbuchstaben sollen ersetzt werden.

    Beispiel:
        "Größe: Übung"
        → "Groesse: Uebung"
    """
    # TODO:
    # Mehrfach .replace() verwenden.
    pass


def maskiere_email(email):
    """
    Versteckt den Namen einer E-Mail-Adresse.

    Beispiel:
        "ada@beispiel.de"
        → "a**@beispiel.de"

    Der erste Buchstabe bleibt sichtbar.
    """
    # TODO:
    # 1. Mit split("@") Name und Domain trennen
    # 2. Ersten Buchstaben behalten
    # 3. Für die restlichen Zeichen "*" verwenden
    # 4. Wieder zusammensetzen
    pass


def baue_funkmeldung(agent, ort, status):
    """
    Erstellt eine Funkmeldung mit einem f-String.

    Beispiel:

        baue_funkmeldung("Ada", "Berlin", "einsatzbereit")

    ergibt:

        "Agentin Ada befindet sich in Berlin. Status: einsatzbereit."
    """
    # TODO
    pass


# ★ Zusatzaufgabe
def geheimschrift(text):
    """
    Schreibt jeden einzelnen Buchstaben eines Textes groß.

    Leerzeichen und andere Zeichen bleiben erhalten.

    Beispiel:
        "geheimer funk" → "GEHEIMER FUNK"
    """
    # TODO
    # upper() verwenden
    pass


# ============================================================
# MISSION 3: Geheime Listen
# ============================================================

def fuege_agent_hinzu(agenten, name):
    """
    Fügt einen Agenten am Ende der Liste hinzu.

    Beispiel:
        ["Ada", "Alan"] + "Grace"
        → ["Ada", "Alan", "Grace"]
    """
    # TODO:
    # append() verwenden
    pass


def entferne_agent(agenten, name):
    """
    Entfernt einen Agenten aus der Liste.

    Gibt die veränderte Liste zurück.
    """
    # TODO:
    # remove() verwenden
    pass


def enthaelt_agent(agenten, name):
    """
    Prüft, ob ein Agent in der Liste vorhanden ist.

    Die Suche soll unabhängig von Groß- und Kleinschreibung
    funktionieren.

    Beispiel:

        ["Ada", "Alan"]

        enthaelt_agent(agenten, "ada")
        → True
    """
    # TODO:
    # Über die Liste laufen und mit .lower() vergleichen.
    pass


def zaehle_agenten(agenten):
    """
    Gibt die Anzahl der Agenten zurück.
    """
    # TODO:
    # len() verwenden
    pass


def filtere_agenten(agenten, suchbegriff):
    """
    Erstellt eine neue Liste mit allen Agenten,
    die den Suchbegriff enthalten.

    Die Suche soll unabhängig von Groß- und Kleinschreibung
    funktionieren.

    Beispiel:

        ["Ada Lovelace", "Alan Turing", "Grace Hopper"]

        filtere_agenten(agenten, "a")

        → ["Ada Lovelace", "Alan Turing", "Grace Hopper"]
    """
    # TODO:
    # 1. Leere Ergebnisliste erstellen
    # 2. Mit einer for-Schleife durch die Agenten laufen
    # 3. Prüfen, ob der Suchbegriff enthalten ist
    # 4. Treffer mit append() hinzufügen
    pass


def laengstes_wort(woerter):
    """
    Gibt das längste Wort einer Liste zurück.

    Bei gleicher Länge soll das erste Wort zurückgegeben werden.

    Bei einer leeren Liste:
        ""
    """
    # TODO:
    # Mit einer Variable für das bisher längste Wort arbeiten.
    pass


def ohne_duplikate(liste):
    """
    Entfernt doppelte Werte.

    Die Reihenfolge des ersten Auftretens bleibt erhalten.

    Beispiel:

        [3, 1, 3, 2, 1]

        → [3, 1, 2]
    """
    # TODO:
    # Neue Liste erstellen.
    # Nur hinzufügen, wenn der Wert noch nicht enthalten ist.
    pass


# ★ Zusatzaufgabe
def jedes_zweite(liste):
    """
    Gibt jedes zweite Element zurück,
    beginnend beim ersten.

    Beispiel:

        [1, 2, 3, 4, 5]
        → [1, 3, 5]
    """
    # TODO:
    # Slicing mit einer Schrittweite verwenden.
    pass


# ============================================================
# MISSION 4: Agentenkartei
# ============================================================

def erstelle_agent(vorname, nachname, codename):
    """
    Erstellt einen Agenten als Liste.

    Beispiel:

        erstelle_agent(
            "Ada",
            "Lovelace",
            "Falke"
        )

        → ["Ada", "Lovelace", "Falke"]
    """
    # TODO
    pass


def agenten_name(agent):
    """
    Baut aus einer Agentenliste den vollständigen Namen.

    Beispiel:

        ["Ada", "Lovelace", "Falke"]

        → "Ada Lovelace"
    """
    # TODO:
    # Vor- und Nachnamen mit join() verbinden.
    pass


def agenten_ausweis(agent):
    """
    Erstellt einen formatierten Agentenausweis.

    Beispiel:

        =====================
        AGENTENAUSWEIS
        =====================
        Name: Ada Lovelace
        Codename: Falke

    Verwende dafür eine Liste mit Textzeilen
    und anschließend "\\n".join(...).
    """
    # TODO
    pass


def finde_agent(agenten, suchbegriff):
    """
    Sucht nach einem Agenten.

    Gesucht werden darf im Vor- und Nachnamen
    sowie im Codenamen.

    Beispiel:

        [
            ["Ada", "Lovelace", "Falke"],
            ["Alan", "Turing", "Nebel"]
        ]

        Suchbegriff: "fal"

        → ["Ada", "Lovelace", "Falke"]
    """
    # TODO:
    # 1. Leere Trefferliste erstellen
    # 2. Durch die Agenten laufen
    # 3. Alle drei Werte untersuchen
    # 4. Treffer hinzufügen
    pass


def codenamen(agenten):
    """
    Erstellt eine neue Liste mit allen Codenamen.

    Beispiel:

        [
            ["Ada", "Lovelace", "Falke"],
            ["Alan", "Turing", "Nebel"]
        ]

        → ["Falke", "Nebel"]
    """
    # TODO:
    # Durch die Agenten laufen und jeweils
    # den Codenamen hinzufügen.
    pass


def agenten_anzeigen(agenten):
    """
    Gibt alle Agenten übersichtlich aus.

    Beispiel:

        Ada Lovelace | Falke
        Alan Turing | Nebel
    """
    # TODO:
    # Mit einer for-Schleife durch die Liste laufen.
    pass


# ★ Zusatzaufgabe
def agenten_sortieren(agenten):
    """
    Gibt eine sortierte Kopie der Agentenliste zurück.

    """
    # TODO:
    # Eine neue Liste erstellen oder sorted() verwenden.
    pass


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

    check(
        "14 fuege_agent_hinzu",
        fuege_agent_hinzu(agenten, "Grace"),
        None
    )

    check(
        "15 Liste nach append",
        agenten,
        ["Ada", "Alan", "Grace"]
    )

    check(
        "16 entferne_agent",
        entferne_agent(agenten, "Alan"),
        ["Ada", "Grace"]
    )

    check(
        "17 enthaelt_agent",
        enthaelt_agent(agenten, "ada"),
        True
    )

    check(
        "18 enthaelt_agent nicht vorhanden",
        enthaelt_agent(agenten, "Turing"),
        False
    )

    check(
        "19 zaehle_agenten",
        zaehle_agenten(agenten),
        2
    )

    check(
        "20 filtere_agenten",
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
        "21 laengstes_wort",
        laengstes_wort(
            ["Agent", "Geheimcode", "Funk", "Passwort"]
        ),
        "Geheimcode"
    )

    check(
        "22 laengstes_wort leer",
        laengstes_wort([]),
        ""
    )

    check(
        "23 ohne_duplikate",
        ohne_duplikate(
            [3, 1, 3, 2, 1]
        ),
        [3, 1, 2]
    )

    check(
        "24 ★ jedes_zweite",
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
        "25 erstelle_agent",
        ada,
        ["Ada", "Lovelace", "Falke"]
    )

    check(
        "26 agenten_name",
        agenten_name(ada),
        "Ada Lovelace"
    )

    ausweis = agenten_ausweis(ada)

    check(
        "27 agenten_ausweis enthält Name",
        "Ada Lovelace" in ausweis,
        True
    )

    check(
        "28 agenten_ausweis enthält Codename",
        "Falke" in ausweis,
        True
    )

    check(
        "29 finde_agent",
        finde_agent(test_agenten, "fal"),
        [ada]
    )

    check(
        "30 finde_agent Nachname",
        finde_agent(test_agenten, "turing"),
        [alan]
    )

    check(
        "31 codenamen",
        codenamen(test_agenten),
        ["Falke", "Nebel", "Schatten"]
    )

    # agenten_anzeigen() gibt direkt Text aus.
    # Deshalb wird hier nur geprüft, dass die Funktion
    # ohne Fehler ausgeführt werden kann.
    print()
    print("32 agenten_anzeigen:")
    agenten_anzeigen(test_agenten)

    # ★ Zusatzaufgabe
    sortierte = agenten_nach_namen_sortieren(
        [
            ["Grace", "Hopper", "Schatten"],
            ["Alan", "Turing", "Nebel"],
            ["Ada", "Lovelace", "Falke"],
        ]
    )

    check(
        "33 ★ agenten_nach_namen_sortieren",
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
