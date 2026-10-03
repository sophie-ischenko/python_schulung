# Projekt: Kreaturen-Archiv

## Worum geht es?

Du baust eine Desktop-App, die eine **größere Datenmenge** aus einer JSON-Datei einliest und interaktiv darstellt. Die Daten stehen in `kreaturen.json`: ein Titel, ein Untertitel und 30 erfundene Kreaturen mit Typ, drei Werten und einer kurzen Beschreibung.

**Die Oberfläche baust du selbst.** In `projekt.py` ist nur das Fundament vorbereitet: das Laden der Daten, zwei kleine Hilfsfunktionen und das Hauptprogramm. Alles, was man im Fenster sieht, und alles, was bei einem Klick passiert, schreibst du anhand der nummerierten Aufgaben.

Am Ende kann die App:

- **Suchen:** Du tippst einen Namen ein und klickst auf "Suchen".
- **Filtern:** Mit den Typ-Buttons (Alle, Feuer, Wasser, Wald, Schatten, Eis).
- **Karten erzeugen:** Für jede passende Kreatur entsteht ein Button. Der Zähler zeigt, wie viele es sind.
- **Details anzeigen:** Ein Klick auf eine Karte zeigt Beschreibung und Werte. Die Balken wachsen animiert, und die Gesamtzahl zählt hoch wie bei einem Timer.
- **Zufällig auswählen**, die **stärkste Kreatur** der aktuellen Auswahl zeigen und ein **Duell** gegen einen zufälligen Gegner austragen.

## Dateien

| Datei | Inhalt |
|---|---|
| `kreaturen.json` | Die Daten |
| `projekt.py` | Dein Startpunkt: Fundament plus nummerierte Aufgaben |
| `projekt_loesung.py` | Die fertige Lösung |

Alle Dateien liegen im selben Ordner. Das Programm startest du mit `python3 projekt.py`.

## So arbeitest du

1. Starte `projekt.py`, bevor du etwas änderst. Es öffnet ein leeres Fenster. Das ist richtig so.
2. Lies im Text unter "AUFGABEN" (in der Mitte der Datei) die erste Aufgabe und suche im Code die Stelle `AUFGABE 1`.
3. Schreibe deinen Code an diese Stelle und starte das Programm neu. Du siehst sofort, was sich verändert hat.
4. Arbeite die Nummern der Reihe nach ab. Mit jeder Aufgabe wird das Fenster voller.
5. Die Bonus-Aufgaben (12) sind freiwillig.

Welche Aufgabe baut was?

| Aufgabe | Was danach im Fenster zu sehen ist | Theorie-Abschnitt |
|---|---|---|
| 1 | Titel und Untertitel aus der JSON-Datei | 6, 29, 30 |
| 2 | (noch unsichtbar) Linke und rechte Seite | 11, 13, 35 |
| 3 | Suchfeld mit zwei Buttons | 8, 9, 14 |
| 4 | Typ-Buttons | 32 |
| 5 | (noch unsichtbar) Zähler und Platz für die Karten | 6, 35 |
| 6 | 30 Karten erscheinen und der Zähler zeigt "30 von 30" | 31, 32, 34 |
| 7 | Suche und Typ-Buttons funktionieren | 9, 14 |
| 8 | Die leere Detailkarte | 15, 16, 35 |
| 9 | Klick auf eine Karte zeigt die Details, die Balken wachsen | 10, 17, 20, 21, 25 |
| 10 | Buttons "Zufällige Kreatur" und "Stärkste zeigen" | 9, 32 |
| 11 | Duell-Fenster | 27, 28 |

## Wie läuft das Programm ab?

1. `daten_laden` liest die JSON-Datei und berechnet für jede Kreatur den Gesamtwert.
2. `main` erstellt das Fenster. `oberflaeche_bauen` setzt alle Widgets hinein.
3. `ergebnisse_aktualisieren` filtert die Kreaturen, löscht die alten Karten und erzeugt neue.
4. Klickst du auf eine Karte, ruft der Button `detail_zeigen` auf. Die Funktion setzt die Texte und startet die Animation.
5. Die Animation läuft wie der Countdown aus der Theorie: `animation_schritt` zeichnet neu und plant sich mit `window.after(20, ...)` selbst wieder ein, bis `fortschritt` 100 erreicht.

## Die wichtigsten Ideen

**Daten im Speicher.** Alle Kreaturen stehen in `daten["kreaturen"]`. Die Liste `sichtbare` enthält nur das, was gerade zu Suche und Filter passt. Bei jeder Änderung wird sie neu aufgebaut.

**Widgets aus Daten erzeugen.** Für jede Kreatur in `sichtbare` entsteht per Schleife ein Button. Das ist die dynamische Oberfläche aus Abschnitt 32.

**Alte Widgets löschen.** Bevor neue Karten entstehen, müssen die alten weg. Deshalb speichert die Liste `karten` jeden erzeugten Button. Das ist dasselbe Prinzip wie die Bilderliste aus Abschnitt 34. Danach reicht eine Schleife mit `.destroy()`.

**Animation.** Die Zahl `fortschritt` läuft von 0 bis 100. In jedem Schritt wird jeder Wert mit `fortschritt / 100` multipliziert. Bei `fortschritt = 50` ist also jeder Balken halb so lang. Der Balken selbst ist ein Text: `"█" * 16`. Die Gesamtzahl im Canvas ändert sich mit `itemconfig`, genau wie die Anzeige im Pomodoro-Timer.

## Typische Fehler

- **Nach dem Start siehst du nur ein leeres Fenster:** Das ist am Anfang richtig. Mit Aufgabe 1 erscheint der Titel.
- **Du siehst ein Widget nicht:** Es fehlt das `grid()`. Erstellen allein reicht nicht.
- **Zwei Widgets liegen übereinander:** Sie haben dieselbe `row` und `column` im selben Frame. Jeder Bereich (Suchzeile, Typ-Buttons, Karten) gehört in einen eigenen Frame.
- **Der Button reagiert sofort beim Start:** Bei `command=` stehen Klammern. Es muss `command=suchen` heißen, nicht `command=suchen()`.
- **`NameError` bei einer Widget-Variable:** Die Variable ist in `oberflaeche_bauen` bei `global` aufgeführt, wurde aber noch nicht erzeugt, oder du hast einen anderen Namen verwendet als in der Aufgabe.
- **`TypeError: can only concatenate str (not "int")`:** Zahlen müssen mit `str(...)` in Text umgewandelt werden.
- **Alle Karten verschwinden, sobald du etwas suchst:** Prüfe, ob `karten = []` nach dem Löschen steht und ob in 6c das `karten.append(button)` nicht fehlt.
- **Labels sind unsichtbar (Mac im Dark Mode):** Setze bei jedem Label `bg` und `fg`.

## Hinweise für dich als Kursleiterin

**Was über die Theorie hinausgeht.** Ich habe darauf geachtet, nur Bausteine aus der Tag-4-Theorie zu verwenden. Diese Punkte sind neu oder nur kurz angesprochen:

- **`lambda` bei Buttons in Schleifen.** Das ist die einzige echte Lücke. Ein Button in einer Schleife braucht `command=lambda t=typ: typ_waehlen(t)`, sonst würde jeder Button denselben Wert benutzen. Ich habe es als Merksatz in die Aufgaben geschrieben. Du könntest dafür einen kurzen Abschnitt in der Theorie ergänzen.
- **`sticky`, `wraplength`, `justify` und `insertbackground`.** Kleine Fenster-Optionen, die in den Aufgaben konkret genannt werden. Die Fenstergröße ergibt sich von selbst aus dem Inhalt, `geometry` wird nicht gebraucht.
- **`"█" * 16` und `f"{bezeichnung:<7}"`.** Textmultiplikation und eine Variante des `:02d`-Formats aus Abschnitt 23. Beides steckt in der fertigen Hilfsfunktion `balken_text`.
- **`random`.** Wird in den Aufgaben 10 und 11 benutzt. Falls es in den Tagen davor noch nicht dran war, genügt ein Satz.
- **Bonus d (`bind`).** Ist freiwillig und wird nur dort verwendet.

**Was die Teilnehmenden nicht selbst schreiben.** Das Laden der JSON-Datei (Abschnitt 29 haben sie gelesen, hier ist es vorgegeben), die Filter-Funktion `kreaturen_filtern` und die Hilfsfunktion `balken_text`.

**Bilder.** Abschnitt 18 bis 19 (`PhotoImage`) kommen in diesem Projekt nicht vor, weil keine Bilddateien mitgeliefert werden. Wenn du möchtest, kannst du bei jeder Kreatur ein Feld `"bild"` ergänzen und die Detailkarte um ein Canvas-Bild erweitern.

**Lösungen zu den Aufgaben.** Sie stehen vollständig in `projekt_loesung.py`, mit denselben Aufgaben-Kommentaren wie im Starter. Dort läuft alles: Ich habe Suche, Filter, Karten, Animation, Zufall, Stärkste und Duell in einer Testumgebung durchgespielt.