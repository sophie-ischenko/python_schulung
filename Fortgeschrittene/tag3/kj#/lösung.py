from pathlib import Path

import csv
import json
import math


# ============================================================
# SCHRITT 1: CSV EINLESEN
# ============================================================

daten = []

with open("eisverkauf.csv", encoding="utf-8", newline="") as datei:
    reader = csv.DictReader(datei)
    spaltennamen = reader.fieldnames

    for zeile in reader:
        daten.append(zeile)

print("SCHRITT 1")
print("Erster Tag:", daten[0])

print("Wochentag des dritten Tages:", daten[2]["wochentag"])
print("Temperatur des letzten Tages:", daten[-1]["temperatur"])
print()


# ============================================================
# SCHRITT 2: ERSTER BLICK
# ============================================================

print("SCHRITT 2")
print("Zeilen:", len(daten))
print("Spalten:", len(spaltennamen), spaltennamen)

for i in range(5):
    print(daten[i])

print()


# ============================================================
# SCHRITT 3: TEXT ODER ZAHL?
# ============================================================

print("SCHRITT 3")

text_wert = daten[0]["temperatur"]
print("Text:", text_wert, "->", type(text_wert))

zahl_wert = float(text_wert)
print("Zahl:", zahl_wert, "->", type(zahl_wert))

temperatur_1 = float(daten[0]["temperatur"])
temperatur_2 = float(daten[1]["temperatur"])

print("Summe der ersten beiden Temperaturen:",
      temperatur_1 + temperatur_2)
print()


# ============================================================
# SCHRITT 4: FEHLENDE WERTE
# ============================================================

def lies_zahl(text):
    if text == "":
        raise ValueError("Leerer Wert")
    return float(text)


leere_temperaturen = 0

for tag in daten:
    try:
        lies_zahl(tag["temperatur"])
    except ValueError:
        leere_temperaturen = leere_temperaturen + 1

print("SCHRITT 4")
print("Tage ohne gültige Temperatur:", leere_temperaturen)

sonnenstunden_ungueltig = 0
verkauf_ungueltig = 0

for tag in daten:
    try:
        lies_zahl(tag["sonnenstunden"])
    except ValueError:
        sonnenstunden_ungueltig = sonnenstunden_ungueltig + 1

    try:
        lies_zahl(tag["verkauf"])
    except ValueError:
        verkauf_ungueltig = verkauf_ungueltig + 1

print("Ungültige Sonnenstunden:", sonnenstunden_ungueltig)
print("Ungültige Verkäufe:", verkauf_ungueltig)
print()


# ============================================================
# SCHRITT 5: DATEN SÄUBERN
# ============================================================

sauber = []
aussortiert = 0

for tag in daten:
    try:
        neuer_tag = {
            "tag": int(tag["tag"]),
            "wochentag": tag["wochentag"],
            "temperatur": lies_zahl(tag["temperatur"]),
            "sonnenstunden": lies_zahl(tag["sonnenstunden"]),
            "regen": int(tag["regen"]),
            "aktion": int(tag["aktion"]),
            "verkauf": lies_zahl(tag["verkauf"]),
        }
    except ValueError:
        aussortiert = aussortiert + 1
        continue

    sauber.append(neuer_tag)

print("SCHRITT 5")
print("Saubere Tage:", len(sauber))
print("Aussortiert:", aussortiert)

print("Erster sauberer Tag:", sauber[0])
print("Temperatur-Typ:", type(sauber[0]["temperatur"]))
print("Verkauf-Typ:", type(sauber[0]["verkauf"]))
print()


# ============================================================
# SCHRITT 6: MITTELWERT, MINIMUM, MAXIMUM
# ============================================================

def mittelwert(liste):
    summe = 0

    for wert in liste:
        summe = summe + wert

    return summe / len(liste)


verkaeufe = []

for tag in sauber:
    verkaeufe.append(tag["verkauf"])


print("SCHRITT 6")
print("Mittelwert Verkauf:", round(mittelwert(verkaeufe), 2))
print("Minimum:", min(verkaeufe))
print("Maximum:", max(verkaeufe))

temperaturen = []

for tag in sauber:
    temperaturen.append(tag["temperatur"])

print("Mittelwert Temperatur:", round(mittelwert(temperaturen), 2))
print("Kälteste Temperatur:", min(temperaturen))
print("Wärmste Temperatur:", max(temperaturen))
print()


# ============================================================
# SCHRITT 7: MEDIAN UND AUSREISSER
# ============================================================

def median(liste):
    sortiert = sorted(liste)
    n = len(sortiert)
    mitte = n // 2

    if n % 2 == 1:
        return sortiert[mitte]

    return (sortiert[mitte - 1] + sortiert[mitte]) / 2


print("SCHRITT 7")
print("Median Verkauf:", median(verkaeufe))
print("Größter Wert:", max(verkaeufe))

for tag in sauber:
    if tag["verkauf"] > 300:
        print(
            "Verdächtig: Tag",
            tag["tag"],
            "mit",
            tag["verkauf"],
            "Kugeln"
        )

print("Median Temperatur:", median(temperaturen))

for tag in sauber:
    if tag["verkauf"] > 200:
        print(
            "Mehr als 200 Kugeln:",
            "Tag", tag["tag"],
            "mit", tag["verkauf"]
        )

print()


# ============================================================
# SCHRITT 8: AUSREISSER ENTFERNEN
# ============================================================

ohne = []

for tag in sauber:
    if tag["verkauf"] <= 300:
        ohne.append(tag)

verkaeufe_ohne = []

for tag in ohne:
    verkaeufe_ohne.append(tag["verkauf"])


print("SCHRITT 8")
print("Tage ohne Ausreißer:", len(ohne))
print("Mittelwert:", round(mittelwert(verkaeufe_ohne), 2))
print("Median:", median(verkaeufe_ohne))
print("Maximum:", max(verkaeufe_ohne))

print()
print("Vergleich vorher / nachher:")
print("Vorher Mittelwert:", round(mittelwert(verkaeufe), 2))
print("Nachher Mittelwert:", round(mittelwert(verkaeufe_ohne), 2))
print("Vorher Median:", median(verkaeufe))
print("Nachher Median:", median(verkaeufe_ohne))
print()


# ============================================================
# SCHRITT 9: GRUPPEN VERGLEICHEN
# ============================================================

wochenende = []
werktag = []

for tag in ohne:
    if tag["wochentag"] == "Sa" or tag["wochentag"] == "So":
        wochenende.append(tag["verkauf"])
    else:
        werktag.append(tag["verkauf"])

print("SCHRITT 9")
print(
    "Wochenende:",
    len(wochenende),
    "Tage, Ø",
    round(mittelwert(wochenende), 2)
)

print(
    "Werktag:",
    len(werktag),
    "Tage, Ø",
    round(mittelwert(werktag), 2)
)


regen = []
trocken = []

for tag in ohne:
    if tag["regen"] == 1:
        regen.append(tag["verkauf"])
    else:
        trocken.append(tag["verkauf"])

print(
    "Regen:",
    len(regen),
    "Tage, Ø",
    round(mittelwert(regen), 2)
)

print(
    "Trocken:",
    len(trocken),
    "Tage, Ø",
    round(mittelwert(trocken), 2)
)


aktion = []
keine_aktion = []

for tag in ohne:
    if tag["aktion"] == 1:
        aktion.append(tag["verkauf"])
    else:
        keine_aktion.append(tag["verkauf"])

print(
    "Aktion:",
    len(aktion),
    "Tage, Ø",
    round(mittelwert(aktion), 2)
)

print(
    "Keine Aktion:",
    len(keine_aktion),
    "Tage, Ø",
    round(mittelwert(keine_aktion), 2)
)

print()


# ============================================================
# SCHRITT 10: KORRELATION
# ============================================================

def korrelation(liste_x, liste_y):
    anzahl = len(liste_x)
    mittel_x = mittelwert(liste_x)
    mittel_y = mittelwert(liste_y)

    summe_xy = 0
    summe_xx = 0
    summe_yy = 0

    for i in range(anzahl):
        dx = liste_x[i] - mittel_x
        dy = liste_y[i] - mittel_y

        summe_xy = summe_xy + dx * dy
        summe_xx = summe_xx + dx * dx
        summe_yy = summe_yy + dy * dy

    return summe_xy / math.sqrt(summe_xx * summe_yy)


temperaturen_ohne = []
sonnenstunden_ohne = []
regen_ohne = []
aktion_ohne = []

for tag in ohne:
    temperaturen_ohne.append(tag["temperatur"])
    sonnenstunden_ohne.append(tag["sonnenstunden"])
    regen_ohne.append(tag["regen"])
    aktion_ohne.append(tag["aktion"])


print("SCHRITT 10")

r_temp = korrelation(
    temperaturen_ohne,
    verkaeufe_ohne
)

r_sonne = korrelation(
    sonnenstunden_ohne,
    verkaeufe_ohne
)

r_regen = korrelation(
    regen_ohne,
    verkaeufe_ohne
)

r_aktion = korrelation(
    aktion_ohne,
    verkaeufe_ohne
)

print("Temperatur und Verkauf:", round(r_temp, 3))
print("Sonnenstunden und Verkauf:", round(r_sonne, 3))
print("Regen und Verkauf:", round(r_regen, 3))
print("Aktion und Verkauf:", round(r_aktion, 3))

print()


# ============================================================
# SCHRITT 11: AUSREISSER UND KORRELATION
# ============================================================

temperaturen_mit = []

for tag in sauber:
    temperaturen_mit.append(tag["temperatur"])


print("SCHRITT 11")
print(
    "r mit Ausreißer:",
    round(korrelation(temperaturen_mit, verkaeufe), 3)
)

print(
    "r ohne Ausreißer:",
    round(r_temp, 3)
)

print()


# ============================================================
# SCHRITT 12: EINFACHE VORHERSAGE
# ============================================================

def gerade(liste_x, liste_y):
    anzahl = len(liste_x)
    mittel_x = mittelwert(liste_x)
    mittel_y = mittelwert(liste_y)

    summe_xy = 0
    summe_xx = 0

    for i in range(anzahl):
        dx = liste_x[i] - mittel_x
        dy = liste_y[i] - mittel_y

        summe_xy = summe_xy + dx * dy
        summe_xx = summe_xx + dx * dx

    steigung = summe_xy / summe_xx
    achsenabschnitt = mittel_y - steigung * mittel_x

    return steigung, achsenabschnitt


steigung, achsenabschnitt = gerade(
    temperaturen_ohne,
    verkaeufe_ohne
)

print("SCHRITT 12")
print("Steigung:", round(steigung, 2), "Kugeln pro Grad")
print("Achsenabschnitt:", round(achsenabschnitt, 2))

for grad in [20, 28]:
    vorhersage = achsenabschnitt + steigung * grad

    print(
        "Bei",
        grad,
        "Grad erwarte ich",
        round(vorhersage, 1),
        "Kugeln"
    )


grad = 25
vorhersage = achsenabschnitt + steigung * grad

print(
    "Bei 25 Grad erwarte ich",
    round(vorhersage, 1),
    "Kugeln"
)


temperatur_150 = (150 - achsenabschnitt) / steigung

print(
    "Ab ungefähr",
    round(temperatur_150, 2),
    "Grad sagt die Gerade mehr als 150 Kugeln voraus."
)


def sage_verkauf_vorher(grad):
    if grad < 5 or grad > 40:
        raise ValueError(
            "Temperatur muss zwischen 5 und 40 Grad liegen."
        )

    return achsenabschnitt + steigung * grad


print(
    "Vorhersage bei 25 Grad:",
    round(sage_verkauf_vorher(25), 1)
)

try:
    print(sage_verkauf_vorher(50))
except ValueError as fehler:
    print("Fehler:", fehler)

print()


# ============================================================
# SCHRITT 13: ERGEBNISSE SPEICHERN
# ============================================================

ergebnisse = {
    "tage_gesamt": len(daten),
    "tage_sauber": len(ohne),
    "aussortiert_luecken": aussortiert,
    "aussortiert_ausreisser": len(sauber) - len(ohne),
    "mittelwert_verkauf": round(mittelwert(verkaeufe_ohne), 2),
    "median_verkauf": median(verkaeufe_ohne),
    "korrelation_temperatur_verkauf": round(r_temp, 3),
    "korrelation_sonnenstunden_verkauf": round(r_sonne, 3),
    "korrelation_regen_verkauf": round(r_regen, 3),
    "korrelation_aktion_verkauf": round(r_aktion, 3),
    "steigung_pro_grad": round(steigung, 2),
}

with open(
    "eisverkauf_ergebnisse.json",
    "w",
    encoding="utf-8"
) as datei:
    json.dump(
        ergebnisse,
        datei,
        ensure_ascii=False,
        indent=2
    )

print("SCHRITT 13")
print("Ergebnisse gespeichert in eisverkauf_ergebnisse.json")


with open(
    "eisverkauf_ergebnisse.json",
    "r",
    encoding="utf-8"
) as datei:
    geladene_ergebnisse = json.load(datei)

print("Geladene Ergebnisse:")
print(geladene_ergebnisse)
print()


# ============================================================
# ABSCHLUSS
# ============================================================

print("ANALYSE ABGESCHLOSSEN")
print()
print("Gesamte Tage:", len(daten))
print("Saubere Tage:", len(ohne))
print("Aussortierte fehlerhafte Tage:", aussortiert)
print("Entfernter Ausreißer:", len(sauber) - len(ohne))
print("Verkaufs-Mittelwert ohne Ausreißer:",
      round(mittelwert(verkaeufe_ohne), 2))
print("Verkaufs-Median ohne Ausreißer:",
      median(verkaeufe_ohne))
print("Korrelation Temperatur/Verkauf:",
      round(r_temp, 3))
print("Korrelation Sonnenstunden/Verkauf:",
      round(r_sonne, 3))
print("Korrelation Regen/Verkauf:",
      round(r_regen, 3))
print("Korrelation Aktion/Verkauf:",
      round(r_aktion, 3))
'''

path = Path("/mnt/data/loesung_eisverkauf.py")
path.write_text(solution, encoding="utf-8")
print(f"Erstellt: {path}")
