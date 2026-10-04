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

============================================================
SO FUNKTIONIEREN DIE AUFGABEN
============================================================

In dieser Datei sind viele Funktionen bereits vorbereitet.

Deine Aufgabe ist es, die Funktionen Schritt für Schritt
fertigzustellen.

Dafür findest du in den Funktionen:

    TODO

Das bedeutet:

    Hier musst du selbst Code schreiben.

Die Kommentare darunter geben dir Hinweise,
welche Python-Befehle du dafür verwenden kannst.

Beispiel:

    def verdopple(zahl):
        # TODO:
        # Die Zahl soll verdoppelt zurückgegeben werden.
        pass

Das Schlüsselwort "pass" bedeutet:

    Hier passiert momentan nichts.

Es sorgt dafür, dass Python die Funktion akzeptiert,
obwohl noch kein richtiger Code darin steht.

Wenn du die Aufgabe löst, ersetzt du "pass"
durch deinen eigenen Code.

Beispiel:

    def verdopple(zahl):
        return zahl * 2

============================================================
DIE TESTS
============================================================

Am Ende dieser Datei stehen automatische Tests.

Sie prüfen, ob deine Funktionen das erwartete Ergebnis liefern.

Zum Beispiel:

    check(
        "bereinige_text",
        bereinige_text("  SERVER-01  "),
        "server-01"
    )

Python führt dabei deine Funktion aus:

    bereinige_text("  SERVER-01  ")

und vergleicht das Ergebnis mit:

    "server-01"

Wenn beide Werte gleich sind, erscheint:

    ✓ bereinige_text

Wenn sie unterschiedlich sind, erscheint zum Beispiel:

    ✗ bereinige_text → erwartet "server-01", erhalten "SERVER-01"

Du bekommst dadurch direkt eine Rückmeldung,
ob deine Lösung funktioniert.

============================================================
WICHTIG: FUNKTIONEN UND RETURN
============================================================

Viele Aufgaben bestehen aus Funktionen.

Eine Funktion bekommt möglicherweise Daten:

    def begruesse(name):

und soll daraus ein Ergebnis erzeugen.

Mit "return" gibst du dieses Ergebnis zurück:

    def begruesse(name):
        return f"Hallo {name}"

Der Wert kann anschließend weiterverwendet werden:

    ergebnis = begruesse("Ada")

    print(ergebnis)

Wenn eine Funktion dagegen nur etwas mit "print()"
ausgibt, kann der Wert nicht auf dieselbe Weise
weiterverarbeitet werden.

Achte deshalb genau darauf, ob in der Aufgabe steht:

    Gibt zurück

oder:

    Gibt aus

"return" und "print()" sind nicht dasselbe.

============================================================
"""


# ============================================================
# HILFSFUNKTION FÜR DIE TESTS
# ============================================================

def check(name, erhalten, erwartet):
    """
    Vergleicht ein erhaltenes Ergebnis mit einem erwarteten Ergebnis.

    Wenn beide Werte gleich sind, wird ein Haken ausgegeben.

    Wenn sie unterschiedlich sind, werden beide Werte angezeigt.

    Beispiel:

        check("Test", 5, 5)

    ergibt:

        ✓ Test

    Bei:

        check("Test", 5, 10)

    erscheint:

        ✗ Test → erwartet 10, erhalten 5

    Diese Funktion musst du nicht verändern.
    Sie wird nur verwendet, um deine Lösungen zu testen.
    """
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

"""
============================================================
1. Strings bereinigen
============================================================

Strings sind Texte.

Python bietet viele fertige Methoden an,
mit denen Strings verändert oder untersucht werden können.

Zum Beispiel:

    text.strip()

entfernt Leerzeichen am Anfang und Ende.

    text.lower()

wandelt alle Buchstaben in Kleinbuchstaben um.

Wichtig:

String-Methoden verändern den ursprünglichen String
nicht direkt.

Deshalb schreibt man häufig:

    text = text.strip()

oder gibt das Ergebnis direkt zurück:

    return text.strip()

In dieser Aufgabe brauchst du beide Methoden:

    .strip()
    .lower()
"""

def bereinige_text(text):
    """
    Entfernt Leerzeichen am Anfang und Ende und
    schreibt den Text komplett klein.

    Beispiel:

        "  SERVER-01  "

    wird zu:

        "server-01"
    """

    # TODO:
    # 1. Leerzeichen mit .strip() entfernen
    # 2. Mit .lower() klein schreiben

    pass


"""
============================================================
2. split() und join()
============================================================

Mit split() kannst du einen String in mehrere Teile zerlegen.

Beispiel:

    name = "Ada Lovelace"

    name.split()

ergibt:

    ["Ada", "Lovelace"]

Das Ergebnis ist also eine Liste.

join() macht den umgekehrten Weg.

Beispiel:

    woerter = ["Ada", "Lovelace"]

    " ".join(woerter)

ergibt:

    "Ada Lovelace"

Das ist ein wichtiges Muster:

    String
        ↓
    split()
        ↓
    Liste
        ↓
    bearbeiten
        ↓
    join()
        ↓
    String

In dieser Aufgabe sollen mehrere Leerzeichen
zwischen Wörtern verschwinden.

Dafür ist split() besonders praktisch,
weil split() ohne Argument alle beliebigen
Leerzeichen als Trennzeichen behandelt.
"""

def normalisiere_name(name):
    """
    Bereinigt einen Namen.

    Mehrere Leerzeichen sollen auf ein Leerzeichen
    reduziert werden und jedes Wort soll mit einem
    Großbuchstaben beginnen.

    Beispiel:

        "  aDA   loVELACE "

    wird zu:

        "Ada Lovelace"
    """

    # TODO:
    # 1. Mit .split() in Wörter zerlegen
    # 2. Mit " ".join(...) wieder zusammensetzen
    # 3. .title() verwenden

    pass


"""
============================================================
3. Indizes
============================================================

Jedes Zeichen in einem String besitzt eine Position.

Diese Position nennt man Index.

Wichtig:

Python beginnt bei 0.

Bei:

    "AGENT"

sind die Positionen:

     A   G   E   N   T
     0   1   2   3   4

Das erste Zeichen bekommt man mit:

    text[0]

Das letzte Zeichen kann man mit einem negativen
Index erreichen:

    text[-1]

Negative Indizes zählen von hinten:

    -1 = letztes Zeichen
    -2 = vorletztes Zeichen
"""

def erste_und_letzte_zeichen(text):
    """
    Gibt erstes und letztes Zeichen als String zurück.

    Beispiel:

        "AGENT"

    ergibt:

        "AT"
    """

    # TODO:
    # Erstes Zeichen: [0]
    # Letztes Zeichen: [-1]
    # Beide mit einem f-String verbinden

    pass


"""
============================================================
4. Slicing
============================================================

Mit Slicing kannst du mehrere Zeichen eines Strings
auswählen.

Beispiel:

    text = "AGENT"

    text[1:4]

ergibt:

    "GEN"

Die Schreibweise lautet:

    text[start:ende]

Das Ende gehört nicht mehr zum Ergebnis.

Mit:

    text[::-1]

kannst du einen String rückwärts lesen.

Die -1 bedeutet hier:
Gehe durch den String rückwärts.
"""

def rueckwaerts(text):
    """
    Gibt einen Text rückwärts zurück.

    Beispiel:

        "AGENT"

    wird zu:

        "TNEGA"
    """

    # TODO:
    # Slicing mit [::-1]

    pass


"""
============================================================
5. Zeichen zählen
============================================================

Eine for-Schleife kann jedes Zeichen eines Strings
nacheinander untersuchen.

Beispiel:

    text = "Banane"

    for zeichen in text:
        print(zeichen)

Die Variable "zeichen" enthält dabei jeweils
das aktuelle Zeichen.

Um etwas zu zählen, kannst du eine Zählvariable verwenden:

    anzahl = 0

und bei einem Treffer erhöhen:

    anzahl = anzahl + 1

oder kürzer:

    anzahl += 1
"""

def zaehle_zeichen(text, zeichen):
    """
    Gibt zurück, wie oft ein bestimmtes Zeichen
    im Text vorkommt.

    Beispiel:

        zaehle_zeichen("Banane", "a")

    ergibt:

        3
    """

    # TODO:
    # Verwende eine Schleife und zähle passende Zeichen.

    pass


"""
============================================================
6. Zusatzaufgabe: Länge ohne Leerzeichen
============================================================

len() gibt die Anzahl der Zeichen eines Strings zurück.

Beispiel:

    len("Hallo")

ergibt:

    5

Wenn Leerzeichen nicht mitgezählt werden sollen,
musst du sie vorher entfernen oder beim Durchlaufen
des Textes ignorieren.

Du kannst dafür zum Beispiel eine Schleife verwenden.

Beispielidee:

    anzahl = 0

    for zeichen in text:
        if zeichen != " ":
            anzahl += 1
"""

def geheimnisvolle_laenge(text):
    """
    Gibt die Länge des Textes ohne Leerzeichen zurück.

    Beispiel:

        "Code Akademie"

    ergibt:

        12
    """

    # TODO:
    # Leerzeichen entfernen oder beim Durchlaufen ignorieren.

    pass


# ============================================================
# MISSION 2: Geheimschrift
# ============================================================

"""
============================================================
7. Initialen
============================================================

Ein Name kann mit split() in einzelne Wörter zerlegt werden.

Beispiel:

    "Ada Lovelace".split()

ergibt:

    ["Ada", "Lovelace"]

Von jedem Wort kannst du mit [0]
den ersten Buchstaben nehmen.

Bei:

    "Ada"

ist:

    "Ada"[0]

gleich:

    "A"

Wenn du mehrere Buchstaben hast,
kannst du sie mit join() verbinden.

Zum Beispiel:

    ".".join(["A", "L"])

ergibt:

    "A.L"

Anschließend fehlt nur noch der letzte Punkt.
"""

def initialen(name):
    """
    Erzeugt die Initialen eines Namens.

    Beispiel:

        "Ada Lovelace"

    wird zu:

        "A.L."
    """

    # TODO:
    # 1. Name mit .split() zerlegen
    # 2. Von jedem Wort den ersten Buchstaben nehmen
    # 3. Groß schreiben
    # 4. Mit "." verbinden
    # 5. Am Ende einen Punkt ergänzen

    pass


"""
============================================================
8. Nachrichten zerlegen
============================================================

split() ist besonders praktisch,
wenn ein Text aus einzelnen Wörtern besteht.

Beispiel:

    "Treffe mich um acht".split()

ergibt:

    ["Treffe", "mich", "um", "acht"]

Die einzelnen Wörter können danach
mit einer Schleife verarbeitet werden.
"""

def teile_nachricht(nachricht):
    """
    Zerlegt eine Nachricht in einzelne Wörter.

    Beispiel:

        "Treffe mich um acht"

    wird zu:

        ["Treffe", "mich", "um", "acht"]
    """

    # TODO:
    # split() verwenden

    pass


"""
============================================================
9. Nachrichten wieder zusammensetzen
============================================================

join() verbindet Elemente einer Liste zu einem String.

Beispiel:

    woerter = ["Treffe", "mich", "um", "acht"]

    " ".join(woerter)

ergibt:

    "Treffe mich um acht"

Wichtig:

Das Trennzeichen steht vor join():

    " ".join(...)
    ",".join(...)
    "-".join(...)

"""

def verbinde_nachricht(woerter):
    """
    Verbindet eine Liste von Wörtern wieder zu einem Satz.

    Beispiel:

        ["Treffe", "mich", "um", "acht"]

    wird zu:

        "Treffe mich um acht"
    """

    # TODO:
    # join() verwenden

    pass


"""
============================================================
10. replace()
============================================================

Mit replace() kannst du Text ersetzen.

Beispiel:

    text = "Hallo Welt"

    text.replace("Welt", "Ada")

ergibt:

    "Hallo Ada"

Mehrere replace()-Aufrufe können hintereinander
verwendet werden.

Beispiel:

    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")

"""

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

    wird zu:

        "Groesse: Uebung"
    """

    # TODO:
    # Mehrfach .replace() verwenden.

    pass


"""
============================================================
11. Strings mit split() untersuchen
============================================================

Eine E-Mail-Adresse besteht beispielsweise aus:

    ada@beispiel.de

Mit:

    email.split("@")

kannst du sie am @-Zeichen trennen.

Das Ergebnis ist:

    ["ada", "beispiel.de"]

Du kannst die beiden Teile in Variablen speichern:

    name, domain = email.split("@")

Danach kannst du den Namen bearbeiten.

Mit Slicing kannst du beispielsweise
den ersten Buchstaben behalten:

    name[0]

Für jedes weitere Zeichen sollen Sternchen
angezeigt werden.

Die Länge eines Strings bekommst du mit:

    len(name)

"""

def maskiere_email(email):
    """
    Versteckt den Namen einer E-Mail-Adresse.

    Beispiel:

        "ada@beispiel.de"

    wird zu:

        "a**@beispiel.de"

    Der erste Buchstabe bleibt sichtbar.
    """

    # TODO:
    # 1. Mit split("@") Name und Domain trennen
    # 2. Ersten Buchstaben behalten
    # 3. Für die restlichen Zeichen "*" verwenden
    # 4. Wieder zusammensetzen

    pass


"""
============================================================
12. f-Strings
============================================================

Mit f-Strings kannst du Variablen direkt
in einen Text einsetzen.

Beispiel:

    name = "Ada"
    ort = "Berlin"

    f"Agentin {name} befindet sich in {ort}."

ergibt:

    "Agentin Ada befindet sich in Berlin."

Vor dem String steht ein:

    f

Variablen werden innerhalb von
geschweiften Klammern geschrieben:

    {name}

"""

def baue_funkmeldung(agent, ort, status):
    """
    Erstellt eine Funkmeldung mit einem f-String.

    Beispiel:

        baue_funkmeldung(
            "Ada",
            "Berlin",
            "einsatzbereit"
        )

    ergibt:

        "Agentin Ada befindet sich in Berlin. "
        "Status: einsatzbereit."
    """

    # TODO:
    # Einen passenden f-String erstellen.

    pass


"""
============================================================
13. Zusatzaufgabe: upper()
============================================================

Mit:

    text.upper()

werden alle Buchstaben eines Strings
in Großbuchstaben umgewandelt.

Beispiel:

    "geheimer funk".upper()

ergibt:

    "GEHEIMER FUNK"

"""

def geheimschrift(text):
    """
    Schreibt jeden einzelnen Buchstaben eines Textes groß.

    Leerzeichen und andere Zeichen bleiben erhalten.

    Beispiel:

        "geheimer funk"

    wird zu:

        "GEHEIMER FUNK"
    """

    # TODO:
    # upper() verwenden

    pass


# ============================================================
# MISSION 3: Geheime Listen
# ============================================================

"""
============================================================
14. Listen erweitern
============================================================

Listen können mehrere Werte speichern.

Beispiel:

    agenten = ["Ada", "Alan"]

Mit append() kannst du einen neuen Wert
am Ende der Liste hinzufügen:

    agenten.append("Grace")

Danach enthält die Liste:

    ["Ada", "Alan", "Grace"]

append() verändert die vorhandene Liste.

Deshalb musst du den Rückgabewert von append()
normalerweise nicht speichern.

"""

def fuege_agent_hinzu(agenten, name):
    """
    Fügt einen Agenten am Ende der Liste hinzu.

    Beispiel:

        ["Ada", "Alan"]

    + "Grace"

    ergibt:

        ["Ada", "Alan", "Grace"]
    """

    # TODO:
    # append() verwenden

    pass


"""
============================================================
15. Werte aus Listen entfernen
============================================================

Mit remove() kannst du einen bestimmten Wert
aus einer Liste entfernen.

Beispiel:

    agenten = ["Ada", "Alan", "Grace"]

    agenten.remove("Alan")

Danach:

    ["Ada", "Grace"]

Achtung:

remove() funktioniert nur,
wenn der Wert tatsächlich in der Liste vorhanden ist.

"""

def entferne_agent(agenten, name):
    """
    Entfernt einen Agenten aus der Liste.

    Gibt die veränderte Liste zurück.
    """

    # TODO:
    # remove() verwenden

    pass


"""
============================================================
16. Prüfen, ob ein Wert enthalten ist
============================================================

Mit "in" kannst du prüfen,
ob ein Wert in einer Liste vorkommt.

Beispiel:

    "Ada" in ["Ada", "Alan"]

ergibt:

    True

Die Aufgabe soll aber unabhängig von Groß-
und Kleinschreibung funktionieren.

Deshalb kannst du beide Seiten mit lower()
in Kleinbuchstaben umwandeln.

Beispiel:

    "ADA".lower()

ergibt:

    "ada"
"""

def enthaelt_agent(agenten, name):
    """
    Prüft, ob ein Agent in der Liste vorhanden ist.

    Die Suche soll unabhängig von Groß- und Kleinschreibung
    funktionieren.

    Beispiel:

        ["Ada", "Alan"]

        enthaelt_agent(agenten, "ada")

    ergibt:

        True
    """

    # TODO:
    # Über die Liste laufen und mit .lower() vergleichen.

    pass


"""
============================================================
17. Anzahl der Elemente
============================================================

len() gibt die Anzahl der Elemente einer Liste zurück.

Beispiel:

    agenten = ["Ada", "Alan", "Grace"]

    len(agenten)

ergibt:

    3
"""

def zaehle_agenten(agenten):
    """
    Gibt die Anzahl der Agenten zurück.
    """

    # TODO:
    # len() verwenden

    pass


"""
============================================================
18. Listen filtern
============================================================

Beim Filtern entsteht eine neue Liste,
die nur bestimmte Elemente enthält.

Dafür brauchst du:

1. Eine leere Ergebnisliste
2. Eine for-Schleife
3. Eine Bedingung
4. append()

Grundmuster:

    ergebnis = []

    for element in liste:
        if bedingung:
            ergebnis.append(element)

Am Ende:

    return ergebnis

In dieser Aufgabe soll geprüft werden,
ob ein Suchbegriff in einem Namen enthalten ist.

Mit:

    suchbegriff in name

kannst du prüfen, ob ein Text in einem anderen
Text vorkommt.

"""

def filtere_agenten(agenten, suchbegriff):
    """
    Erstellt eine neue Liste mit allen Agenten,
    die den Suchbegriff enthalten.

    Die Suche soll unabhängig von Groß- und Kleinschreibung
    funktionieren.

    Beispiel:

        [
            "Ada Lovelace",
            "Alan Turing",
            "Grace Hopper"
        ]

    Suchbegriff:

        "a"

    ergibt:

        [
            "Ada Lovelace",
            "Alan Turing",
            "Grace Hopper"
        ]
    """

    # TODO:
    # 1. Leere Ergebnisliste erstellen
    # 2. Mit einer for-Schleife durch die Agenten laufen
    # 3. Prüfen, ob der Suchbegriff enthalten ist
    # 4. Treffer mit append() hinzufügen

    pass


"""
============================================================
19. Das längste Wort finden
============================================================

Du kannst innerhalb einer Schleife
einen bisherigen Wert speichern.

Beispielidee:

    laengstes = ""

Dann gehst du durch alle Wörter.

Wenn ein neues Wort länger ist:

    if len(wort) > len(laengstes):

kannst du es als neues längstes Wort speichern.

Am Ende wird das bisher längste Wort zurückgegeben.

Bei gleicher Länge soll das erste Wort bleiben.

Deshalb muss die Bedingung wirklich "größer" sein:

    >

und nicht:

    >=

"""

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


"""
============================================================
20. Duplikate entfernen
============================================================

Ein Duplikat ist ein Wert,
der mehr als einmal vorkommt.

Beispiel:

    [3, 1, 3, 2, 1]

soll werden:

    [3, 1, 2]

Dabei soll die Reihenfolge erhalten bleiben.

Du brauchst deshalb eine neue Liste.

Grundidee:

    ergebnis = []

    for wert in liste:
        if wert nicht in ergebnis:
            ergebnis.append(wert)

Am Ende enthält ergebnis
nur noch die ersten Vorkommen.
"""

def ohne_duplikate(liste):
    """
    Entfernt doppelte Werte.

    Die Reihenfolge des ersten Auftretens bleibt erhalten.

    Beispiel:

        [3, 1, 3, 2, 1]

    wird zu:

        [3, 1, 2]
    """

    # TODO:
    # Neue Liste erstellen.
    # Nur hinzufügen, wenn der Wert noch nicht enthalten ist.

    pass


"""
============================================================
21. Zusatzaufgabe: Slicing mit Schrittweite
============================================================

Slicing kann nicht nur Start und Ende enthalten.

Die vollständige Form lautet:

    liste[start:ende:schrittweite]

Beispiel:

    [1, 2, 3, 4, 5][::2]

ergibt:

    [1, 3, 5]

Die 2 bedeutet:
Nimm jedes zweite Element.

"""

def jedes_zweite(liste):
    """
    Gibt jedes zweite Element zurück,
    beginnend beim ersten.

    Beispiel:

        [1, 2, 3, 4, 5]

    wird zu:

        [1, 3, 5]
    """

    # TODO:
    # Slicing mit einer Schrittweite verwenden.

    pass


# ============================================================
# MISSION 4: Agentenkartei
# ============================================================

"""
============================================================
22. Mehrere Werte als Liste speichern
============================================================

Eine Funktion kann mehrere Informationen
zu einem gemeinsamen Datensatz zusammenfassen.

Hier besteht ein Agent aus drei Werten:

    Vorname
    Nachname
    Codename

Beispiel:

    ["Ada", "Lovelace", "Falke"]

Die Funktion soll genau diese Liste erstellen
und zurückgeben.

"""

def erstelle_agent(vorname, nachname, codename):
    """
    Erstellt einen Agenten als Liste.

    Beispiel:

        erstelle_agent(
            "Ada",
            "Lovelace",
            "Falke"
        )

    ergibt:

        ["Ada", "Lovelace", "Falke"]
    """

    # TODO:
    # Eine Liste mit Vorname, Nachname und Codename
    # erstellen und zurückgeben.

    pass


"""
============================================================
23. Werte aus einer Liste holen
============================================================

Listen besitzen Indizes.

Bei:

    ["Ada", "Lovelace", "Falke"]

ist:

    agent[0]

der Vorname.

    agent[1]

ist der Nachname.

    agent[2]

ist der Codename.

Für den vollständigen Namen brauchst du
nur die ersten beiden Werte.

Mit join() kannst du sie verbinden.

"""

def agenten_name(agent):
    """
    Baut aus einer Agentenliste den vollständigen Namen.

    Beispiel:

        ["Ada", "Lovelace", "Falke"]

    ergibt:

        "Ada Lovelace"
    """

    # TODO:
    # Vor- und Nachnamen mit join() verbinden.

    pass


"""
============================================================
24. Mehrzeilige Texte mit join()
============================================================

Ein Agentenausweis soll aus mehreren Zeilen bestehen.

Du kannst die Zeilen zuerst als Liste speichern:

    zeilen = [
        "=====================",
        "AGENTENAUSWEIS",
        "=====================",
        "Name: Ada Lovelace",
        "Codename: Falke"
    ]

Anschließend kannst du sie mit:

    "\n".join(zeilen)

zu einem mehrzeiligen String verbinden.

"\n" bedeutet:
Neue Zeile.

Das ist ein sehr nützliches Muster,
wenn du längere Ausgaben erzeugen möchtest.
"""

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


"""
============================================================
25. Mehrere Agenten durchsuchen
============================================================

Jetzt werden mehrere bisher gelernte Konzepte kombiniert.

Die Agentenliste enthält mehrere Agenten.

Jeder Agent ist wiederum eine Liste:

    ["Ada", "Lovelace", "Falke"]

Du musst:

1. Durch alle Agenten laufen.
2. Vorname untersuchen.
3. Nachname untersuchen.
4. Codenamen untersuchen.
5. Treffer in eine neue Liste aufnehmen.

Auch hier hilft das Grundmuster:

    treffer = []

    for agent in agenten:
        ...
        if ...:
            treffer.append(agent)

Am Ende:

    return treffer

Die Suche soll unabhängig von Groß-
und Kleinschreibung funktionieren.

"""

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

    Suchbegriff:

        "fal"

    ergibt:

        ["Ada", "Lovelace", "Falke"]
    """

    # TODO:
    # 1. Leere Trefferliste erstellen
    # 2. Durch die Agenten laufen
    # 3. Alle drei Werte untersuchen
    # 4. Treffer hinzufügen

    pass


"""
============================================================
26. Codenamen auslesen
============================================================

Jeder Agent besitzt immer dieselbe Struktur:

    Index 0 = Vorname
    Index 1 = Nachname
    Index 2 = Codename

Wenn du nur die Codenamen möchtest,
brauchst du aus jedem Agenten nur:

    agent[2]

Auch hier kannst du eine neue Liste erstellen
und die Werte mit append() hinzufügen.
"""

def codenamen(agenten):
    """
    Erstellt eine neue Liste mit allen Codenamen.

    Beispiel:

        [
            ["Ada", "Lovelace", "Falke"],
            ["Alan", "Turing", "Nebel"]
        ]

    ergibt:

        ["Falke", "Nebel"]
    """

    # TODO:
    # Durch die Agenten laufen und jeweils
    # den Codenamen hinzufügen.

    pass


"""
============================================================
27. Agenten anzeigen
============================================================

Manchmal soll eine Funktion nicht einen Wert zurückgeben,
sondern direkt etwas ausgeben.

Hier soll jeder Agent beispielsweise so erscheinen:

    Ada Lovelace | Falke

Dafür brauchst du:

    for agent in agenten:

und kannst innerhalb der Schleife
die Werte des aktuellen Agenten verwenden.

Du kannst den Namen mit der vorherigen Funktion
agenten_name() erzeugen.

"""

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


"""
============================================================
28. Zusatzaufgabe: Agenten sortieren
============================================================

sorted() erzeugt eine neue sortierte Liste.

Beispiel:

    zahlen = [3, 1, 2]

    sorted(zahlen)

ergibt:

    [1, 2, 3]

Die ursprüngliche Liste bleibt dabei unverändert.

Bei Agenten ist die Situation etwas interessanter,
weil jeder Agent selbst eine Liste ist.

Beispiel:

    [
        ["Grace", "Hopper", "Schatten"],
        ["Alan", "Turing", "Nebel"],
        ["Ada", "Lovelace", "Falke"]
    ]

Standardmäßig wird bei solchen verschachtelten Listen
zuerst das erste Element verglichen.

Damit wird hier nach dem Vornamen sortiert.

"""

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

"""
============================================================
DIE TESTS IM HAUPTBEREICH
============================================================

In diesem Projekt stehen die Tests direkt im Hauptbereich
des Programms.

Das bedeutet:

    if __name__ == "__main__":

wird ausgeführt, wenn diese Datei direkt gestartet wird.

Darunter werden die einzelnen Funktionen
nacheinander getestet.

Das ist für dieses Projekt praktisch,
weil die Tests gleichzeitig die vier Missionen
sichtbar strukturieren.

Später kann es sinnvoll sein,
die Tests in eine eigene Funktion auszulagern.

Zum Beispiel:

    def selbsttest():
        ...

Dann könnte das Hauptprogramm entscheiden,
was gestartet werden soll.

Beispielsweise:

    python projekt.py

könnte das normale Programm starten.

Und:

    python projekt.py test

könnte die Tests starten.

In diesem Projekt bleiben die Tests jedoch
direkt im Hauptbereich.

Wichtig:

Die Tests sind nicht die eigentliche Programmlogik.

Sie überprüfen nur,
ob unsere Funktionen das erwartete Ergebnis liefern.

============================================================
"""


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
    sortierte = agenten_sortieren(
        [
            ["Grace", "Hopper", "Schatten"],
            ["Alan", "Turing", "Nebel"],
            ["Ada", "Lovelace", "Falke"],
        ]
    )

    check(
        "33 ★ agenten_sortieren",
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