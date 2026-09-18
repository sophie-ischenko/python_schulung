"""
Tag 9: Fortgeschrittene Funktionen & Das Main-Pattern
=======================================================
Aufgaben zu Block 1 (Wertfluss) und Block 4 (Modularer Programmier-Slam).

Arbeitsweise:
- Lies dir die Theorie im Notebook 'tag9_theorie.ipynb' durch, bevor du hier startest.
- Schreibe deine Loesung jeweils direkt unter die Aufgabenstellung (ersetze 'pass'
  bzw. den Kommentar "# Deine Loesung hier").
- Bei Block 4: Baue zuerst die Hilfsfunktion(en), teste sie einzeln, und baue dann
  erst die main()-Funktion darum herum.
- ACHTUNG: Die drei Programm-Systeme aus Block 4 nutzen input(). Fuehre diese Datei
  dafuer am besten direkt als Skript aus: python tag9_aufgaben.py
- Vergleiche erst danach mit 'tag9_loesungen.py'.
"""

# =====================================================================
# BLOCK 1: Funktionsaufrufe festigen (09:00 - 09:45 Uhr)
# =====================================================================


def berechne_restspeicher(gesamt, belegt):
    """
    Aufgabe W1: Der Speicher-Minderer

    Berechne die Differenz aus gesamt und belegt und gib sie als Float
    zurueck.
    """
    # Deine Loesung hier
    pass


def ist_lokal(ip):
    """
    Aufgabe W2: Der IP-Pruefer

    Gib True zurueck, wenn die IP mit "192.168." beginnt, sonst False.
    """
    # Deine Loesung hier
    pass


def bereinige_dateiname(name):
    """
    Aufgabe W3: Dateiname-Normalisierer

    Schneide fuehrende/nachfolgende Leerzeichen ab, wandle alles in
    Kleinbuchstaben um und gib das Ergebnis zurueck.

    Tipp: .strip() entfernt Leerzeichen am Anfang und Ende, .lower()
    wandelt in Kleinbuchstaben um. Du kannst beide Methoden direkt
    hintereinander anhaengen ("verketten").
    """
    # Deine Loesung hier
    pass


# =====================================================================
# BLOCK 4: Der modulare Programmier-Slam (11:30 - 12:45 Uhr)
# =====================================================================
# Alle drei Programme sind nach dem heutigen Standard strukturiert:
# mehrere spezialisierte Funktionen, orchestriert von einer main()-Funktion,
# abgeschlossen mit dem Einstiegspunkt-Pattern. Da in einer einzigen Datei
# nicht drei Funktionen gleichzeitig "main" heissen koennen, ist die
# main()-Funktion hier je Programm-System durchnummeriert
# (main_programmsystem_1/2/3) - in einem eigenstaendigen Skript wuerde sie
# schlicht main() heissen.


# --- Programm-System 1: Der Server-Raum-Monitor ---

def bewerte_temperatur(temp):
    """
    Schritt 1: Gib "kritisch" zurueck, wenn die Temperatur ueber 30 Grad
    liegt, andernfalls "normal".
    """
    # Deine Loesung hier
    pass


def erzeuge_alarm_text(status, servername):
    """
    Schritt 2: Ist status "kritisch", gib
    "[WARNUNG] Server <Name> ist ueberhitzt!" zurueck. Andernfalls:
    "[INFO] Server <Name> laeuft stabil.".
    """
    # Deine Loesung hier
    pass


def main_programmsystem_1():
    """
    Schritt 3: main()-Funktion, die den Servernamen und die Temperatur
    abfragt, die beiden obigen Funktionen aufruft, um die Meldung zu
    generieren, und die Meldung ausgibt.
    """
    # Deine Loesung hier
    pass


# --- Programm-System 2: Der Onboarding-Assistent fuer neue Mitarbeiter ---

def generiere_email(vorname, nachname):
    """
    Schritt 1: Bereinige die Eingaben (Leerzeichen weg, Kleinbuchstaben)
    und gib die E-Mail im Format vorname.nachname@firma.de zurueck.
    """
    # Deine Loesung hier
    pass


def generiere_username(vorname, nachname):
    """
    Schritt 2: Nimm den ersten Buchstaben des Vornamens und haenge den
    vollstaendigen Nachnamen an (alles in Kleinbuchstaben, z. B.
    "mmustermann").

    Tipp: Auf einen String kannst du mit eckigen Klammern zugreifen, um
    einzelne Zeichen herauszuholen - "hallo"[0] ergibt "h".
    """
    # Deine Loesung hier
    pass


def main_programmsystem_2():
    """
    Schritt 3: main()-Funktion, die Vorname und Nachname einliest, die
    E-Mail und den Benutzernamen ueber die Hilfsfunktionen berechnet und
    beide Ergebnisse in einem uebersichtlichen Bericht ausgibt.
    """
    # Deine Loesung hier
    pass


# --- Programm-System 3: Der Ping-Latenz-Tester (mit Schleife) ---

def bewerte_latenz(ping):
    """
    Schritt 1:
    - Ping <= 30 ms: Rueckgabe "Hervorragend"
    - Ping <= 100 ms: Rueckgabe "Akzeptabel"
    - Darueber: Rueckgabe "Kritisch"
    """
    # Deine Loesung hier
    pass


def main_programmsystem_3():
    """
    Schritt 2: main()-Funktion mit einer while-Schleife, die immer
    wieder nach einer Ping-Latenz (Ganzzahl) fragt.
    - Eingabe -1 bricht die Schleife (break) ab.
    - Alle anderen Eingaben werden ueber bewerte_latenz bewertet und das
      Ergebnis direkt ausgegeben.
    """
    # Deine Loesung hier
    pass


if __name__ == "__main__":
    # Waehle waehrend der Bearbeitung aus, welches Programm-System du
    # gerade testen willst, indem du die passende Zeile einkommentierst:

    # main_programmsystem_1()
    # main_programmsystem_2()
    # main_programmsystem_3()
    pass
