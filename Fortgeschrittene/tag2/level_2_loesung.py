"""
Tag 2 – Level 2
Lösungen

Dictionaries, Sets und Tupel
"""


def unter_10_euro(preise):
    ergebnis = []

    for produkt, preis in preise.items():
        if preis < 10:
            ergebnis.append(produkt)

    return sorted(ergebnis)


def teuerstes_produkt(preise):
    return max(preise, key=preise.get)


def preise_erhoehen(preise, prozent):
    ergebnis = {}

    for produkt, preis in preise.items():
        neuer_preis = preis * (1 + prozent / 100)
        ergebnis[produkt] = round(neuer_preis, 2)

    return ergebnis


def gemeinsame_filme(filme_a, filme_b):
    return filme_a & filme_b


def noch_nicht_gelesen_wunschliste(wunschliste, gelesen):
    return wunschliste - gelesen


def alle_gerichte(restaurant_a, restaurant_b):
    return restaurant_a | restaurant_b


def personen_ab_18(personen):
    ergebnis = []

    for name, alter in personen:
        if alter >= 18:
            ergebnis.append(name)

    return sorted(ergebnis)


def durchschnittsalter(personen):
    summe = 0

    for name, alter in personen:
        summe += alter

    return summe / len(personen)


def sortiere_nach_alter(personen):
    return sorted(personen, key=lambda person: person[1])


def besucherzahlen(veranstaltungen):
    ergebnis = {}

    for name, anzahl in veranstaltungen:
        ergebnis[name] = anzahl

    return ergebnis


def gemeinsame_teilnehmer(gruppe_a, gruppe_b):
    namen_a = set()
    namen_b = set()

    for name, alter in gruppe_a:
        namen_a.add(name)

    for name, alter in gruppe_b:
        namen_b.add(name)

    return namen_a & namen_b


def einkaufswert(einkauf, preise):
    gesamt = 0

    for produkt, anzahl in einkauf:
        preis = preise[produkt]
        gesamt += preis * anzahl

    return gesamt


if __name__ == "__main__":

    print("Lösungen geladen.")