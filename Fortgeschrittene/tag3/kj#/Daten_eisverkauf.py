"""
MITMACH-THEORIE: DATEN ANALYSIEREN MIT PYTHON
=============================================

Du arbeitest mit einem Dummy-Datensatz: dem Eisverkauf einer
kleinen Eisdiele an 60 Tagen.

Spalten der Datei eisverkauf.csv:

    tag             Tag 1 bis 60
    wochentag       Mo, Di, Mi, Do, Fr, Sa, So
    temperatur      Temperatur in Grad Celsius
    sonnenstunden   Stunden Sonnenschein
    regen           1 = es hat geregnet, 0 = nicht
    aktion          1 = Rabattaktion, 0 = keine
    verkauf         verkaufte Eiskugeln

Die Daten sind erfunden, aber mit typischen Problemen:
Es fehlen ein paar Werte, und ein Wert ist ein Tippfehler.
Genau wie in echten Daten.


SO ARBEITEST DU MIT DIESER DATEI
--------------------------------

1. Lege eisverkauf.csv in denselben Ordner wie diese Datei.
2. Lies die Schritte von oben nach unten.
3. Der BEISPIEL-Code läuft schon. Starte die Datei und schau
   dir die Ausgabe an.
4. Bei MACH MIT schreibst du selbst Code an die Stelle
   "# DEIN CODE:". Die Lösungswerte stehen als KONTROLLE
   direkt darunter.
5. Die Schritte bauen aufeinander auf. Lösche nichts
   aus früheren Schritten.
"""

import csv
import json
import math


# ============================================================
# SCHRITT 1: EINE TABELLE WIRD ZU PYTHON-DATEN
# ============================================================

"""
THEORIE

Ein Datensatz ist eine Tabelle:

    Zeile   = eine Beobachtung (hier: ein Tag)
    Spalte  = ein Merkmal (hier: die Temperatur)

In Python lesen wir jede Zeile als Dictionary ein.
Alle Zeilen zusammen stehen in einer Liste:

    daten = [ {Tag 1}, {Tag 2}, {Tag 3}, ... ]

Mit daten[0] bekommst du den ersten Tag.
Mit daten[0]["temperatur"] bekommst du dessen Temperatur.
"""

# BEISPIEL
daten = []

with open("eisverkauf.csv", encoding="utf-8", newline="") as datei:
    reader = csv.DictReader(datei)
    spaltennamen = reader.fieldnames

    for zeile in reader:
        daten.append(zeile)

print("SCHRITT 1")
print("Erster Tag:", daten[0])
print()

"""
MACH MIT

1. Gib den Wochentag des dritten Tages aus.
2. Gib die Temperatur des letzten Tages aus.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 2: DEN ERSTEN BLICK AUF DIE DATEN WERFEN
# ============================================================

"""
THEORIE

Bevor du rechnest, schaust du dir die Daten an:

    - Wie viele Zeilen gibt es?
    - Welche Spalten gibt es?
    - Wie sehen die ersten Zeilen aus?

len(daten) gibt die Anzahl der Zeilen.
len(spaltennamen) gibt die Anzahl der Spalten.
"""

# BEISPIEL
# print("SCHRITT 2")
# print("Zeilen:", len(daten))
# print("Spalten:", len(spaltennamen), spaltennamen)
# print()

"""
MACH MIT

3. Gib die ersten fünf Tage aus. Verwende eine for-Schleife
   mit einem Zähler und break, oder Slicing: daten[0:5].

KONTROLLE: 60 Zeilen, 7 Spalten.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 3: TEXT ODER ZAHL?
# ============================================================

"""
THEORIE

Alles in einer CSV-Datei ist zunächst TEXT.

    daten[0]["temperatur"]   ergibt "19.5"   (Text!)

Rechnen geht erst nach der Umwandlung:

    float("19.5")   ergibt 19.5   (Zahl)
    int("1")        ergibt 1      (ganze Zahl)

Ohne Umwandlung sieht Python "19.5" + "20.3" als
Textverkettung: "19.520.3".
"""

# BEISPIEL
# print("SCHRITT 3")
# text_wert = daten[0]["temperatur"]
# print("Text:", text_wert, "->", type(text_wert))
# zahl_wert = float(text_wert)
# print("Zahl:", zahl_wert, "->", type(zahl_wert))
# print()

"""
MACH MIT

4. Wandle die Temperatur der ersten beiden Tage in Zahlen um
   und gib ihre Summe aus.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 4: FEHLENDE WERTE
# ============================================================

"""
THEORIE

In echten Daten fehlen oft Werte. Hier gibt es zwei Arten:

    leere Zelle:   ""
    kaputter Text: "n/a"

Beide lassen sich nicht in eine Zahl umwandeln:
Das gibt einen ValueError.

Wir schreiben eine Funktion, die das sauber meldet
und fangen den Fehler mit try/except ab.
"""

# BEISPIEL
# def lies_zahl(text):
#     if text == "":
#         raise ValueError("Leerer Wert")
#     return float(text)


# leere_temperaturen = 0
# for tag in daten:
#     try:
#         lies_zahl(tag["temperatur"])
#     except ValueError:
#         leere_temperaturen = leere_temperaturen + 1

# print("SCHRITT 4")
# print("Tage ohne gültige Temperatur:", leere_temperaturen)
# print()

"""
MACH MIT

5. Zähle, wie viele Tage keine gültigen Sonnenstunden haben.
6. Zähle, wie viele Tage keinen gültigen Verkauf haben.

KONTROLLE: Sonnenstunden: 1, Verkauf: 0.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 5: DATEN SÄUBERN
# ============================================================

"""
THEORIE

Wir bauen eine neue Liste "sauber", in der nur Tage stehen,
bei denen alle Zahlen gültig sind.
Dabei wandeln wir die Werte gleich in Zahlen um.

Mit continue springt Python zum nächsten Durchlauf der Schleife
und überspringt den Rest.
"""

# BEISPIEL
# sauber = []
# aussortiert = 0

# for tag in daten:
#     try:
#         neuer_tag = {
#             "tag": int(tag["tag"]),
#             "wochentag": tag["wochentag"],
#             "temperatur": lies_zahl(tag["temperatur"]),
#             "sonnenstunden": lies_zahl(tag["sonnenstunden"]),
#             "regen": int(tag["regen"]),
#             "aktion": int(tag["aktion"]),
#             "verkauf": lies_zahl(tag["verkauf"]),
#         }
#     except ValueError:
#         aussortiert = aussortiert + 1
#         continue

#     sauber.append(neuer_tag)

# print("SCHRITT 5")
# print("Saubere Tage:", len(sauber), "Aussortiert:", aussortiert)
# print()

"""
MACH MIT

7. Gib den ersten Tag aus der Liste sauber aus.
   Sind die Werte jetzt Zahlen? Woran erkennst du das?

KONTROLLE: 57 saubere Tage, 3 aussortiert.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 6: MITTELWERT, MINIMUM, MAXIMUM
# ============================================================

"""
THEORIE

Drei Kennzahlen gibt es fast immer:

    Mittelwert   Summe aller Werte geteilt durch die Anzahl
    Minimum      kleinster Wert
    Maximum      größter Wert

Wir packen die Verkäufe erst in eine eigene Liste
und schreiben eine Funktion für den Mittelwert.
"""

# BEISPIEL
# def mittelwert(liste):
#     summe = 0
#     for wert in liste:
#         summe = summe + wert
#     return summe / len(liste)


# verkaeufe = []
# for tag in sauber:
#     verkaeufe.append(tag["verkauf"])

# print("SCHRITT 6")
# print("Mittelwert Verkauf:", round(mittelwert(verkaeufe), 2))
# print("Minimum:", min(verkaeufe), "Maximum:", max(verkaeufe))
# print()

"""
MACH MIT

8. Berechne den Mittelwert der Temperatur in sauber.
   Lege dafür eine Liste temperaturen an (wie verkaeufe).
9. Finde die kälteste und die wärmste Temperatur.

KONTROLLE für Aufgabe 6 (Verkauf): Mittelwert 102.49,
Minimum 5, Maximum 450.
Hm, 450 Kugeln an einem Tag? Das schauen wir uns an.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 7: MEDIAN UND AUSREISSER
# ============================================================

"""
THEORIE

Der Mittelwert reagiert stark auf Ausreißer
(einzelne extreme Werte).

Der MEDIAN ist der Wert in der Mitte der sortierten Liste.
Er ist robuster.

    sortiert:  5, 20, 30, 40, 900
    Mittelwert: 199
    Median:     30

Wie berechnet man den Median?

    1. Liste mit sorted() sortieren
    2. Mitte finden: n // 2  (// ist die ganzzahlige Division)
    3. Bei ungerader Anzahl: der Wert in der Mitte
       Bei gerader Anzahl: Mittelwert der beiden mittleren Werte
"""

# BEISPIEL
# def median(liste):
#     sortiert = sorted(liste)
#     n = len(sortiert)
#     mitte = n // 2

#     if n % 2 == 1:
#         return sortiert[mitte]
#     return (sortiert[mitte - 1] + sortiert[mitte]) / 2


# print("SCHRITT 7")
# print("Median Verkauf:", median(verkaeufe))
# print("Größter Wert:", max(verkaeufe))

# for tag in sauber:
#     if tag["verkauf"] > 300:
#         print("Verdächtig: Tag", tag["tag"], "mit", tag["verkauf"], "Kugeln")
# print()

"""
MACH MIT

10. Berechne den Median der Temperatur.
11. Finde alle Tage, an denen mehr als 200 Kugeln
    verkauft wurden. Gib Tag und Verkauf aus.

KONTROLLE: Median Verkauf 100.0. Es gibt einen Tag über 200.
Es ist Tag 45: Das ist ein Tippfehler. Gemeint waren 45 Kugeln.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 8: AUSREISSER ENTFERNEN
# ============================================================

"""
THEORIE

Ein offensichtlicher Tippfehler darf die Auswertung
nicht verfälschen. Wir entfernen ihn mit einer Regel:

    Verkauf über 300 Kugeln gilt als Fehler.

Wichtig: Eine solche Regel dokumentierst du immer
und prüfst vorher, ob es wirklich ein Fehler ist.
Echte Spitzenwerte darfst du nicht einfach löschen.
"""

# BEISPIEL
# ohne = []
# for tag in sauber:
#     if tag["verkauf"] <= 300:
#         ohne.append(tag)

# verkaeufe_ohne = []
# for tag in ohne:
#     verkaeufe_ohne.append(tag["verkauf"])

# print("SCHRITT 8")
# print("Tage ohne Ausreißer:", len(ohne))
# print("Mittelwert:", round(mittelwert(verkaeufe_ohne), 2))
# print("Median:", median(verkaeufe_ohne))
# print("Maximum:", max(verkaeufe_ohne))
# print()

"""
MACH MIT

12. Vergleiche Mittelwert und Median vorher und nachher.
    Was hat sich stärker verändert?

KONTROLLE: 56 Tage. Mittelwert 96.29, Median 97.0, Maximum 185.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 9: GRUPPEN VERGLEICHEN
# ============================================================

"""
THEORIE

Oft interessiert: Unterscheiden sich zwei Gruppen?
Zum Beispiel Wochenende gegen Werktag.

Vorgehen:
    1. Zwei leere Listen anlegen
    2. Schleife: Jeden Tag in die passende Liste legen
    3. Von beiden Listen den Mittelwert berechnen
"""

# BEISPIEL
# wochenende = []
# werktag = []

# for tag in ohne:
#     if tag["wochentag"] == "Sa" or tag["wochentag"] == "So":
#         wochenende.append(tag["verkauf"])
#     else:
#         werktag.append(tag["verkauf"])

# print("SCHRITT 9")
# print("Wochenende:", len(wochenende), "Tage, Ø", round(mittelwert(wochenende), 2))
# print("Werktag:", len(werktag), "Tage, Ø", round(mittelwert(werktag), 2))
# print()

"""
MACH MIT

13. Vergleiche Regentage (regen == 1) mit trockenen Tagen.
14. Vergleiche Tage mit Rabattaktion (aktion == 1)
    mit Tagen ohne Aktion.
15. Welcher Faktor macht den größten Unterschied?

KONTROLLE:
    Wochenende 14 Tage Ø 106.14, Werktag 42 Tage Ø 93.0
    Regen 15 Tage Ø 31.07, trocken 41 Tage Ø 120.15
    Aktion 13 Tage Ø 110.46, ohne 43 Tage Ø 92.0
"""

# DEIN CODE:


# ============================================================
# SCHRITT 10: KORRELATION
# ============================================================

"""
THEORIE

Die Korrelation r zeigt, wie stark zwei Zahlenreihen
zusammenhängen. Sie liegt immer zwischen -1 und +1.

    nahe +1   je mehr x, desto mehr y
    nahe  0   kein erkennbarer Zusammenhang
    nahe -1   je mehr x, desto weniger y

Rechenweg in fünf Schritten:

    1. Mittelwert von x und y
    2. Abstände vom Mittelwert: dx = x - mittel_x, dy = y - mittel_y
    3. summe_xy = Summe aller dx * dy
    4. summe_xx = Summe aller dx * dx, summe_yy = Summe aller dy * dy
    5. r = summe_xy / Wurzel(summe_xx * summe_yy)

In der Funktion unten verwenden wir range(anzahl).
Das liefert die Zahlen 0, 1, 2, ... bis anzahl - 1.
Mit liste_x[i] und liste_y[i] greifen wir immer auf
das Wertepaar derselben Position zu.
"""

# BEISPIEL
# def korrelation(liste_x, liste_y):
#     anzahl = len(liste_x)
#     mittel_x = mittelwert(liste_x)
#     mittel_y = mittelwert(liste_y)

#     summe_xy = 0
#     summe_xx = 0
#     summe_yy = 0

#     for i in range(anzahl):
#         dx = liste_x[i] - mittel_x
#         dy = liste_y[i] - mittel_y
#         summe_xy = summe_xy + dx * dy
#         summe_xx = summe_xx + dx * dx
#         summe_yy = summe_yy + dy * dy

#     return summe_xy / math.sqrt(summe_xx * summe_yy)


# temperaturen_ohne = []
# for tag in ohne:
#     temperaturen_ohne.append(tag["temperatur"])

# print("SCHRITT 10")
# r_temp = korrelation(temperaturen_ohne, verkaeufe_ohne)
# print("Temperatur und Verkauf: r =", round(r_temp, 3))
# print()

"""
MACH MIT

16. Berechne r für Sonnenstunden und Verkauf.
17. Berechne r für Regen (0/1) und Verkauf.
    Warum ist r hier negativ?
18. Berechne r für Aktion (0/1) und Verkauf.
    Warum ist r hier so klein, obwohl die Aktion den Mittelwert
    um ca. 18 Kugeln erhöht?

KONTROLLE:
    Temperatur       0.905
    Sonnenstunden    0.858
    Regen           -0.74
    Aktion           0.146
"""

# DEIN CODE:


# ============================================================
# SCHRITT 11: WIE GEFÄHRLICH SIND AUSREISSER?
# ============================================================

"""
THEORIE

Ein einziger Tippfehler kann die Korrelation stark
verändern. Das siehst du, wenn du r mit und ohne den
Fehlerwert berechnest.
"""

# BEISPIEL
# temperaturen_mit = []
# for tag in sauber:
#     temperaturen_mit.append(tag["temperatur"])

# print("SCHRITT 11")
# print("r mit Ausreißer:", round(korrelation(temperaturen_mit, verkaeufe), 3))
# print("r ohne Ausreißer:", round(r_temp, 3))
# print()



# ============================================================
# SCHRITT 12: EINE EINFACHE VORHERSAGE
# ============================================================

"""
THEORIE

Wenn ein Zusammenhang deutlich ist, können wir eine
Gerade durch die Punkte legen:

    verkauf = achsenabschnitt + steigung * temperatur

Die Steigung sagt: Um wie viel steigt y, wenn x um 1 steigt?

Berechnung (dieselben Summen wie bei der Korrelation):

    steigung = summe_xy / summe_xx
    achsenabschnitt = mittel_y - steigung * mittel_x

Eine Funktion kann mehrere Werte auf einmal zurückgeben.
Dazu schreibst du sie durch Komma getrennt hinter return.
"""

# BEISPIEL
# def gerade(liste_x, liste_y):
#     anzahl = len(liste_x)
#     mittel_x = mittelwert(liste_x)
#     mittel_y = mittelwert(liste_y)

#     summe_xy = 0
#     summe_xx = 0

#     for i in range(anzahl):
#         dx = liste_x[i] - mittel_x
#         dy = liste_y[i] - mittel_y
#         summe_xy = summe_xy + dx * dy
#         summe_xx = summe_xx + dx * dx

#     steigung = summe_xy / summe_xx
#     achsenabschnitt = mittel_y - steigung * mittel_x
#     return steigung, achsenabschnitt


# steigung, achsenabschnitt = gerade(temperaturen_ohne, verkaeufe_ohne)

# print("SCHRITT 12")
# print("Steigung:", round(steigung, 2), "Kugeln pro Grad")
# print("Achsenabschnitt:", round(achsenabschnitt, 2))

# for grad in [20, 28]:
#     vorhersage = achsenabschnitt + steigung * grad
#     print("Bei", grad, "Grad erwarte ich", round(vorhersage, 1), "Kugeln")
# print()

"""
MACH MIT

20. Wie viele Kugeln erwartest du bei 25 Grad?
21. Ab welcher Temperatur sagt die Gerade mehr als 150 Kugeln
    voraus? Probiere verschiedene Werte aus, oder stelle die
    Formel um.
22. Schreibe eine Funktion sage_verkauf_vorher(grad), die
    die Vorhersage zurückgibt. Löse mit raise einen ValueError
    aus, wenn grad kleiner als 5 oder größer als 40 ist, denn
    unsere Daten reichen nur von etwa 13 bis 32 Grad.
    Die Gerade ist außerhalb dieses Bereichs nicht verlässlich.
"""

# DEIN CODE:


# ============================================================
# SCHRITT 13: ERGEBNISSE SPEICHERN
# ============================================================

"""
THEORIE

Gute Analysen speichert man ab: Was wurde gefunden?
Mit welchen Daten?

Wir legen ein Dictionary an und schreiben es als JSON.
"""

# BEISPIEL
# ergebnisse = {
#     "tage_gesamt": len(daten),
#     "tage_sauber": len(ohne),
#     "aussortiert_luecken": aussortiert,
#     "aussortiert_ausreisser": len(sauber) - len(ohne),
#     "mittelwert_verkauf": round(mittelwert(verkaeufe_ohne), 2),
#     "median_verkauf": median(verkaeufe_ohne),
#     "korrelation_temperatur_verkauf": round(r_temp, 3),
#     "steigung_pro_grad": round(steigung, 2),
# }

# with open("eisverkauf_ergebnisse.json", "w", encoding="utf-8") as datei:
#     json.dump(ergebnisse, datei, ensure_ascii=False, indent=2)

# print("SCHRITT 13")
# print("Ergebnisse gespeichert in eisverkauf_ergebnisse.json")
# print()

"""
MACH MIT

23. Füge die Korrelationen für Sonnenstunden und Regen
    zum Dictionary ergebnisse hinzu, bevor du speicherst.
24. Lade die JSON-Datei danach mit json.load() wieder
    und gib sie aus.
"""

# DEIN CODE:


# ============================================================
# ABSCHLUSS: DEIN ERSTER KLEINER DATENBERICHT
# ============================================================

"""
FAZIT: DER ABLAUF EINER DATENANALYSE

    1. Einlesen        CSV -> Liste von Dictionaries
    2. Ansehen         Zeilen, Spalten, erste Einträge
    3. Umwandeln       Text -> Zahlen
    4. Säubern         Lücken und Ausreißer behandeln
    5. Beschreiben     Mittelwert, Median, Minimum, Maximum
    6. Vergleichen     Gruppen gegeneinander
    7. Zusammenhänge   Korrelation
    8. Vorhersagen     einfache Gerade
    9. Speichern       Ergebnisse festhalten

KLEINE ABSCHLUSSAUFGABE


BONUS

26. Erzeuge einen eigenen Dummy-Datensatz und führe dieselbe
    Analyse durch.
"""
