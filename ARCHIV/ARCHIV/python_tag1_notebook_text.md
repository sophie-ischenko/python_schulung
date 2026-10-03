# Tag 1 – Notebook: Der monolithische Kampf

**Tagesziel:** Am Ende des Tages steht ein lauffähiger Konsolen-Kampf: Ein Held mit Lebenspunkten (HP) tritt gegen ein Monster an. Bei jeder Runde wird gewürfelt, ob der Angriff trifft, Schaden wird abgezogen, und der Kampf endet, sobald eine Seite 0 HP erreicht.

**Wichtige Regel für heute:** Wir verzichten heute bewusst komplett auf eigene Funktionen (`def`). Alles wird als ein langes Skript von oben nach unten geschrieben (monolithisch) — um Kontrollstrukturen isoliert zu verstehen und morgen den "Schmerz" zu spüren, der zum Aufräumen mit Funktionen motiviert.

**Zugehörige Code-Datei:** `tag1_code.py` — enthält alle Beispiele, Übungs-Starter und das fertige Kampf-Grundgerüst als kommentierte, lauffähige Datei.

---

## 1.1 Variablen & Datentypen

**Definition:** Eine Variable ist ein benannter Speicherplatz für einen Wert. Python erkennt den Datentyp automatisch anhand des zugewiesenen Werts (dynamische Typisierung).

**Warum wichtig:** Jede Berechnung und jeder Vergleich im Spiel setzt voraus, dass wir wissen, mit welchem Datentyp wir es zu tun haben — besonders, weil `input()` immer Text liefert, selbst wenn Ziffern eingegeben werden.

**Syntax:**
```
variablenname = wert
```

**Merksatz:** *"input() lügt nie über den Typ — es ist immer str. Wer rechnen will, wandelt vorher um."*

**Beispiel:** siehe `tag1_code.py`, Abschnitt "1.1 Beispiel"

### Übung 1: Der fehlerhafte Warenkorb (30 Min)
*Lernziel: Die Notwendigkeit der Typumwandlung durch eigenen "Schmerz" erfahren.*

1. Frage den Nutzer per `input()` nach einem Produktnamen, dem Preis pro Stück und der gewünschten Anzahl
2. Berechne die Gesamtsumme (`preis * anzahl`) und gib das Ergebnis in einem Satz aus
3. **Teste dein Skript!** Wo müsst ihr `float()` und `int()` einbauen, damit korrekt gerechnet wird?

→ Starter-Code: `tag1_code.py`, Abschnitt "Übung 1"

---

## 1.2 Vergleiche & if/elif/else

**Definition:** Vergleichsoperatoren (`>`, `<`, `==`, `!=`, `>=`, `<=`) liefern immer `True` oder `False`. `if`/`elif`/`else` steuert, welcher Code abhängig davon ausgeführt wird.

**Warum wichtig:** Jede Entscheidung im Spiel — trifft ein Angriff, ist ein Charakter besiegt, war die Eingabe gültig — läuft über diese Bausteine.

**Syntax:**
```
if bedingung1:
    ...
elif bedingung2:
    ...
else:
    ...
```

**Merksatz:** *"Ein `=` speichert, zwei `==` vergleichen. Einrückung ist in Python der Code-Block — keine Klammern nötig."*

**Beispiel:** siehe `tag1_code.py`, Abschnitt "1.2 Beispiel" (Funktion `werte_angriff`)

### Übung 2: Der strenge Türsteher (40 Min)
*Lernziel: Logische Bedingungen und Verzweigungen kombinieren.*

1. Frage den Nutzer nach seinem Alter
2. Unter 18: "Du kommst hier nicht rein!"
3. 18-20: Frage nach "Muttizettel" (ja/nein), entsprechend reagieren
4. Ab 21: "Willkommen im Club, VIP!"

→ Starter-Code: `tag1_code.py`, Abschnitt "Übung 2"

---

## 1.3 while-Schleife

**Definition:** Eine `while`-Schleife wiederholt einen Codeblock, solange eine Bedingung `True` ist. `while True:` in Kombination mit `break` wird genutzt, wenn die Abbruchbedingung erst *innerhalb* der Schleife entsteht.

**Warum wichtig:** Ein Kampf dauert eine unbekannte Anzahl Runden — wir wissen vorher nicht, wie viele Runden gebraucht werden, bis eine Seite besiegt ist.

**Syntax:**
```
while bedingung:
    ...

while True:
    ...
    if abbruchbedingung:
        break
```

**Merksatz:** *"Vergisst man, die Bedingung in der Schleife zu verändern, entsteht eine Endlosschleife — ein Klassiker, den man einmal bewusst erlebt haben sollte."*

**Beispiel:** siehe `tag1_code.py`, Abschnitt "1.3 Beispiel"

### Übung 3: Der nervige Papagei (30 Min)
*Lernziel: Schleifen-Abbruchbedingungen verstehen.*

1. `while True:`-Schleife, die bei jedem Durchlauf zur Eingabe auffordert
2. Antwortet immer mit demselben Text (wie ein Papagei)
3. Beendet sich nur bei exakter Eingabe `"Halt die Klappe"` (mit `break`)

→ Starter-Code: `tag1_code.py`, Abschnitt "Übung 3"

---

## 1.4 try/except

**Definition:** `try/except` fängt einen definierten Fehlertyp ab, der beim Ausführen von Code auftreten kann, statt das Programm abstürzen zu lassen.

**Warum wichtig:** Benutzereingaben sind nie vollständig kontrollierbar. Ohne Absicherung stürzt das Programm bei jeder unerwarteten Eingabe ab.

**Syntax:**
```
try:
    riskanter_code
except FehlerTyp:
    reaktion_auf_fehler
```

**Merksatz:** *"Gezielt `except ValueError` statt pauschal `except Exception` — sonst verschluckt man auch Fehler, die man eigentlich bemerken sollte."*

**Beispiel:** siehe `tag1_code.py`, Abschnitt "1.4 Beispiel"

### Übung 4: Der unzerstörbare Taschenrechner (40 Min)
*Lernziel: Fehler abfangen, ohne den Programmfluss zu killen.*

1. `while`-Schleife fragt zwei Zahlen ab und teilt sie durcheinander
2. `ValueError` bei Buchstaben abfangen, `continue` zur erneuten Eingabe
3. **Zusatz-Challenge:** Division durch 0 gezielt mit eigenem `except`-Block abfangen

→ Starter-Code: `tag1_code.py`, Abschnitt "Übung 4"

---

## Praxis: Den Kampf zusammenbauen (Gruppenarbeit, 45 Min)

Das fertige Grundgerüst von **Dungeon Duel** steht in `tag1_code.py`, Abschnitt "Praxis: Kampf-Grundgerüst" — lauffähig und kommentiert.

**Erweiterungsaufgaben:**
1. Prüft gegenseitig, ob das Spiel wirklich absturzsicher ist
2. **Kritische Treffer:** Bei `random.randint(1, 20) == 20` verdoppelt sich der Schaden, Ausgabe "KRITISCHER TREFFER!"
3. **Logik-Denksport:** Wo genau muss `runde += 1` stehen, damit ungültige Aktionen nicht als Runde zählen?

→ Eure Erweiterung schreibt ihr direkt in eine Kopie von `tag1_code.py`.

---

**Tagesabschluss:** Der Kampf läuft fehlerfrei. Aber die Fehlerprüfung, die Kampflogik, der Rundenzähler – alles klebt aneinander in einem großen Block. **Ausblick:** Morgen lernen wir Funktionen kennen, um unseren Kampf aufzuräumen!