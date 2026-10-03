
"""
Tag 1 – Projekt: Agentenverwaltung

Die Code-Akademie braucht eine kleine digitale Agentenkartei.

Im Laufe des Projekts baust du ein Programm, mit dem Agent:innen
aufgenommen, angezeigt und gesucht werden können.

Themen:
- Strings bearbeiten
- Listen
- Schleifen
- Funktionen
- Filtern
- split() und join()
- Slicing
- f-Strings


DEINE AUFGABEN
==============

1. Erstelle eine Liste namens `agenten`, in der alle Agent:innen
   gespeichert werden.

2. Schreibe eine Funktion `codename(vorname, nachname)`.

   Der Codename soll aus dem rückwärts geschriebenen Nachnamen
   und einer Zahl bestehen.

   Die Zahl entsteht aus:

       Länge des Vornamens * Länge des Nachnamens

   Beispiel:

       codename("Ada", "Lovelace")

   ergibt:

       "ecalevoL-56"


3. Schreibe eine Funktion `agent_erstellen(vorname, nachname, alter)`.

   Die Funktion soll einen Agenten als Liste zurückgeben.

   Die Liste soll enthalten:

       Vorname
       Nachname
       Alter
       Codename

   Vor- und Nachname sollen innerhalb der Funktion bereinigt werden:
   Leerzeichen am Anfang und Ende entfernen und die Schreibweise
   mit `.title()` vereinheitlichen.


4. Schreibe eine Funktion `agent_anzeigen(agent)`.

   Sie soll einen Agenten übersichtlich ausgeben.

   Beispiel:

       Ada Lovelace | ecal evoL-56 | 36 Jahre

   Der genaue Aufbau darf von dir sinnvoll gestaltet werden.


5. Schreibe eine Funktion `agent_suchen(agenten, suchbegriff)`.

   Die Funktion soll alle Agenten finden, deren Vorname oder
   Nachname den Suchbegriff enthält.

   Die Suche soll unabhängig von Groß- und Kleinschreibung funktionieren.

   Die Funktion gibt eine neue Liste mit den Treffern zurück.


6. Schreibe eine Funktion `agenten_filtern_nach_alter(agenten, mindestalter)`.

   Sie soll eine neue Liste zurückgeben, die nur Agenten enthält,
   deren Alter mindestens dem angegebenen Mindestalter entspricht.


7. Schreibe eine Funktion `ausweis_erstellen(agent)`.

   Der Agentenausweis soll aus mehreren Zeilen bestehen.

   Verwende dafür eine Liste mit Textzeilen und anschließend
   `"\n".join(...)`.

   Beispiel:

       =========================
       AGENTENAUSWEIS
       =========================
       Name:     Ada Lovelace
       Codename: ecal evoL-56
       Alter:    36 Jahre


8. Erstelle mindestens fünf Agenten und speichere sie in der
   Liste `agenten`.


9. Baue ein kleines Menü:

       ================================
          CODE-AKADEMIE
          AGENTENVERWALTUNG
       ================================

       1. Agent aufnehmen
       2. Alle Agenten anzeigen
       3. Agent suchen
       4. Agenten nach Alter filtern
       5. Agentenausweis anzeigen
       6. Beenden

   Das Menü soll so lange laufen, bis die Benutzerin oder der Benutzer
   "6" auswählt.


HINWEISE
========

Du darfst die folgenden Funktionen und Methoden verwenden:

    print()
    input()
    len()
    .strip()
    .lower()
    .title()
    .upper()
    .append()
    .split()
    .join()

Außerdem:

    in
    if / elif / else
    for
    return
    f-Strings
    Slicing

Versuche, jede größere Aufgabe in eine eigene Funktion aufzuteilen.


OPTIONALE ERWEITERUNG
=====================

Erweitere die Agentenverwaltung um einen zufälligen Decknamen
oder einen zufälligen Auftrag.

Dafür kannst du `random.choice()` verwenden.
"""

# ============================================================
# STARTER-CODE
# ============================================================

agenten = []


def codename(vorname, nachname):
    """
    Erzeugt einen Codenamen aus Vor- und Nachnamen.

    TODO:
    - Nachnamen rückwärts schreiben
    - ersten Buchstaben groß schreiben
    - Länge von Vor- und Nachnamen multiplizieren
    - alles als String zurückgeben
    """
    pass


def agent_erstellen(vorname, nachname, alter):
    """
    Erstellt einen Agenten als Liste.

    TODO:
    - Vor- und Nachnamen mit strip() bereinigen
    - Schreibweise mit title() vereinheitlichen
    - Codename erzeugen
    - Liste mit allen vier Werten zurückgeben
    """
    pass


def agent_anzeigen(agent):
    """
    Gibt einen Agenten übersichtlich aus.

    TODO
    """
    pass


def agent_suchen(agenten, suchbegriff):
    """
    Sucht nach Agenten.

    Der Suchbegriff soll sowohl im Vor- als auch im Nachnamen
    gefunden werden können.

    Die Suche soll unabhängig von Groß- und Kleinschreibung sein.

    TODO
    """
    pass


def agenten_filtern_nach_alter(agenten, mindestalter):
    """
    Gibt nur Agenten zurück, die mindestens so alt sind
    wie `mindestalter`.

    TODO
    """
    pass


def ausweis_erstellen(agent):
    """
    Erstellt einen mehrzeiligen Agentenausweis.

    Verwende eine Liste von Textzeilen und anschließend
    "\\n".join(...).

    TODO
    """
    pass


def check():
    """
    Kleine Selbsttests.

    Wenn deine Funktionen funktionieren, sollte am Ende
    "Alle Tests bestanden." ausgegeben werden.
    """
    agent = agent_erstellen("  ada ", " lovelace  ", 36)

    assert agent[0] == "Ada"
    assert agent[1] == "Lovelace"
    assert agent[2] == 36
    assert agent[3] == "ecalevoL-56"

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

    volljaehrig = agenten_filtern_nach_alter(test_agenten, 40)
    assert len(volljaehrig) == 2

    ausweis = ausweis_erstellen(agent)

    assert "Ada Lovelace" in ausweis
    assert "ecalevoL-56" in ausweis
    assert "36 Jahre" in ausweis

    print("Alle Tests bestanden.")


def main():
    """
    Hauptprogramm.

    TODO:
    - mindestens fünf Agenten anlegen
    - Menü bauen
    - Menü so lange anzeigen, bis 6 gewählt wird
    """
    pass


if __name__ == "__main__":
    main()
