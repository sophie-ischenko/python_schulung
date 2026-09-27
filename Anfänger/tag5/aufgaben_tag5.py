# ---------- Tiere: Zugreifen ----------
tiere = ["Hund", "Katze", "Hase", "Fisch", "Vogel"]

"""
1. Gib das erste Element von `tiere` aus.
2. Gib das dritte Element aus.
3. Gib das letzte Element mit dem Index `-1` aus.
4. Gib mit `len()` aus, wie viele Tiere in der Liste sind.
"""


# ---------- Schulfächer: Slicing ----------
faecher = ["Mathe", "Deutsch", "Kunst", "Sport", "Musik", "Bio"]

"""
1. Gib die ersten zwei Fächer aus (`[:2]`).
2. Gib alle Fächer ab dem dritten aus (`[2:]`).
3. Gib nur "Kunst", "Sport" und "Musik" aus (`[2:5]`).
4. Gib die ganze Liste rückwärts aus (`[::-1]`).
"""


# ---------- Obstkorb: Hinzufügen und Ändern ----------
obst = ["Apfel", "Banane", "Kirsche"]

"""
1. Füge mit `append()` "Mango" hinzu.
2. Füge mit `insert()` "Erdbeere" an Position 0 ein.
3. Ersetze "Banane" durch "Birne" (per Index).
4. Gib die Liste nach jedem Schritt mit `print()` aus.
"""


# ---------- Snacks: Entfernen ----------
snacks = ["Chips", "Kekse", "Nüsse", "Gummibärchen", "Popcorn"]

"""
1. Entferne "Kekse" mit `remove()`.
2. Entferne das letzte Element mit `pop()` und speichere es in einer Variable. Gib die Variable aus.
3. Entferne das erste Element mit `pop(0)`.
4. Gib die Liste aus. Was ist übrig?
"""


# ---------- Würfeln: Auswerten ----------
wuerfe = [4, 6, 2, 6, 1, 3, 6]

"""
1. Gib aus, wie oft gewürfelt wurde (`len()`).
2. Gib den kleinsten und den größten Wurf aus (`min()`, `max()`).
3. Gib die Summe aller Würfe aus (`sum()`).
4. Gib mit `count()` aus, wie oft eine 6 gewürfelt wurde.
5. Prüfe mit `in`, ob eine 5 dabei war.
"""


# ---------- Preise und Namen: Sortieren ----------
preise = [3.5, 1.2, 4.8, 2.0, 0.9]
namen = ["Zoe", "Ben", "Amir", "Clara"]

"""
1. Gib `sorted(preise)` aus. Gib danach `preise` selbst aus. Was fällt dir auf?
2. Gib die Preise absteigend sortiert aus (`sorted(preise, reverse=True)`).
3. Sortiere `namen` mit `namen.sort()` und gib die Liste danach aus.
4. Gib `namen` einmal mit `reverse()` umgedreht aus.
"""


# ---------- Freunde und Zahlen: Erste Schleifen ----------
freunde = ["Mia", "Jonas", "Lea"]
zahlen = [2, 4, 6, 8]

"""
1. Gib mit einer `for`-Schleife jeden Namen aus `freunde` aus.
2. Gib zu jedem Namen "Hallo, <Name>!" aus.
3. Gib mit einer `for`-Schleife jede Zahl aus `zahlen` verdoppelt aus.
4. Berechne die Summe von `zahlen` mit einer Schleife (Tipp: Starte mit `summe = 0`).
"""


# ---------- Bücherregal: Gemischte Aufgaben ----------
buecher = ["Momo", "Faust", "Emil und die Detektive"]

"""
1. Gib das zweite Buch aus.
2. Füge ein weiteres Buch am Ende hinzu.
3. Prüfe mit `in`, ob "Momo" im Regal steht, und gib "Ja" oder "Nein" aus.
4. Entferne "Faust" und gib die Liste danach aus.
5. Gib mit `len()` aus, wie viele Bücher jetzt im Regal stehen.
"""


# ---------- Mini-Projekt: Wunschliste ----------
wuensche = ["Fahrrad", "Buch"]

"""
1. Frage die Nutzerin mit `input()` nach einem weiteren Wunsch und füge ihn mit `append()` hinzu.
2. Wiederhole das dreimal (kopiere den Code einfach untereinander).
3. Gib am Ende alle Wünsche mit einer `for`-Schleife aus.
4. Gib zusätzlich aus, wie viele Wünsche es sind.
"""