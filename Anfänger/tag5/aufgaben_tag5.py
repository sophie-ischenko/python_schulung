
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
essen = ["Pizza", "Sushi", "Pasta", "Falafel", "Eis"]

"""
1. Gib von `zahlen` das erste, das letzte und das fünfte Element aus.
2. Gib von `essen` die ersten drei per Slicing (`[:3]`) aus, danach die ganze Liste rückwärts.
3. Gib von `zahlen` nur jedes zweite Element aus (`[::2]`).
"""


einkauf = ["Milch", "Brot", "Eier"]
werte = [1, 2, 3, 4, 5]
unsortiert = [5, 2, 9, 1, 7]

"""
4. Füge `einkauf` mit `append()` "Käse" und "Tomaten" hinzu und mit `insert()` "Kaffee" an Position 0.
5. Entferne aus `einkauf` "Brot" per `remove()` und das letzte Element per `pop()`. Was gibt `pop()` zurück?
6. Ersetze in `werte` das mittlere Element durch `99`.
7. Sortiere `unsortiert` aufsteigend und absteigend. Was ist der Unterschied zwischen `sort()` und `sorted()`?
"""

namen = ["Anna", "Ben", "Clara", "David"]
punkte = [12, 5, 23, 8, 17, 3, 30]

"""
8. Gib zu jedem Namen in `namen` "Hallo, <Name>!" aus.
9. Berechne die Summe von `punkte`, erst mit Schleife, dann mit `sum()`.
10. Finde das größte Element von `punkte` ohne `max()`. Vergleiche danach mit `max()`.
11. Zähle, wie viele Werte in `punkte` größer als 10 sind.
12. Erstelle eine neue Liste mit nur den geraden Zahlen aus `punkte`.
"""

zahlen = [3, 8, 1, 9, 4]
mit_duplikaten = [1, 2, 2, 3, 3, 3, 4]
woerter = ["Anna", "Python", "Lagerregal", "Liste", "Otto"]

"""
13. Kehre `zahlen` um, ohne `reverse()` oder `[::-1]`.
14. Entferne die Duplikate aus `mit_duplikaten`, erst ohne `set()`, dann mit `set()`.
15. Gib aus `woerter` alle Palindrome aus (Groß- und Kleinschreibung ignorieren).
16. Erzeuge per List Comprehension aus `zahlen` eine Liste der Quadrate.
"""

aufgaben = ["Wäsche waschen", "Python üben", "Einkaufen"]
noten = [1.7, 2.3, 1.0, 3.0, 2.0]

"""
- To-do-Liste: Baue mit `aufgaben` ein Terminal-Menü zum Hinzufügen, Anzeigen und Abhaken.
- Notenrechner: Gib für `noten` Durchschnitt, beste und schlechteste Note aus.
"""


wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
temperaturen = [14, 17, 21, 19, 23, 25, 18]

"""
1. Gib die Temperatur von Mittwoch und von Sonntag aus (per Index).
2. Gib die Temperaturen von Dienstag bis Freitag per Slicing aus.
3. Gib mit `len()`, `min()` und `max()` die Anzahl der Tage sowie die niedrigste und höchste Temperatur aus.
4. Prüfe mit `in`, ob es einen Tag mit genau 21 Grad gab. Finde mit `index()` heraus, welcher Wochentag das war.
"""

inventar = ["Schwert", "Schild", "Trank", "Fackel"]
beute = ["Goldmünze", "Schlüssel", "Karte"]

"""
5. Hänge alle Elemente von `beute` mit `extend()` an `inventar` an. Was ist der Unterschied zu `append()`?
6. Entferne "Fackel" und füge "Bogen" an Position 1 ein.
7. Tausche das erste und das letzte Element von `inventar`.
8. Prüfe, ob "Trank" im Inventar ist. Wenn ja, entferne ihn und gib "Trank benutzt!" aus.
"""

buecher = ["Momo", "Die Physiker", "Faust", "Effi Briest", "Der Vorleser"]
seiten = [304, 96, 158, 320, 208]

"""
9. Gib die Bücher nummeriert aus, z. B. "1. Momo" (mit `enumerate()`).
10. Gib mit `zip()` zu jedem Buch die Seitenzahl aus: "Momo: 304 Seiten".
11. Berechne die durchschnittliche Seitenzahl.
12. Erstelle eine neue Liste mit allen Titeln, die mehr als 200 Seiten haben.
13. Finde den Titel des dicksten Buches (Tipp: `index()`).
"""

tore = [2, 0, 1, 3, 0, 2, 1, 4, 0, 1]
spieler = ["Mia", "Lena", "Jonas", "Ali", "Nora"]

"""
14. Zähle mit `count()`, in wie vielen Spielen kein Tor fiel.
15. Berechne die Gesamtzahl der Tore und in wie vielen Spielen mehr als ein Tor fiel.
16. Sortiere `spieler` nach der Länge der Namen (`sorted(..., key=len)`).
17. Erstelle per List Comprehension eine Liste, in der jede Torzahl verdoppelt ist.
18. Erstelle eine Liste mit dem Zwischenstand nach jedem Spiel: `[2, 2, 3, 6, ...]`.
"""

klasse = [["Anna", 1.3], ["Ben", 2.7], ["Clara", 2.0], ["David", 3.3]]

"""
19. Gib jede Person mit ihrer Note aus: "Anna hat 1.3".
20. Finde die Person mit der besten Note (kleinster Wert).
"""