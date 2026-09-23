# Dungeon Duel – Tag 1: Der interaktive Charakterbogen

**Ausgangscode:** `charakterbogen.py` (unverändert).
**Lösungen:** `loesungen/charakterbogen_stufe1.py` bis `..._stufe4.py`.

## So arbeitet ihr

- Jede Stufe baut auf der **Lösung der vorherigen Stufe** auf: Ausgangscode → Stufe 1 → Stufe 2 → Stufe 3 → Stufe 4. Ihr erweitert also immer *dasselbe* Programm.
- Jede Aufgabe folgt dem gleichen Muster: **Eingabe abfragen → verarbeiten → witzige Ausgabe** (gern mit ASCII-Art).
- ASCII-Art gehört in `r"""..."""` (ein *raw string*). Ohne das `r` würde Python Backslashes wie `\n` oder `\_` als Sonderzeichen deuten und die Zeichnung zerlegen.
- Kleiner Trick, der überall funktioniert: `"A" * 5` ergibt `"AAAAA"`. Text mal Zahl wiederholt den Text – perfekt für Balken und Schreie.

---

## Stufe 1: Variablen, Datentypen, Eingaben

**1. Schaden berechnen.** Frage die Waffenschaden-Zahl ab (`int`) und berechne `schaden = waffe + staerke // 2`.
*Interaktiv:* Lass den Helden zuschlagen (`*WUMMS*`) und den Goblin dahinter schreien, und zwar so, dass das Geschrei mit dem Schaden wächst: `"AU" + "A" * schaden + "!"`. Dazu gehört ein ASCII-Schwert.

**2. Manapunkte.** Berechne `mana = intelligenz * 3` und gib sie aus.
*Interaktiv:* Zeichne einen Manabalken aus `"~" * ...` und rechne aus, für wie viele Feuerbälle das reicht (`//`). Ein ASCII-Zauberhut macht sich gut.

**3. Typ-Experiment.** Probiere `name + stufe` aus und lies die Fehlermeldung. Wie behebst du sie mit `str()`?
*Interaktiv:* Baue daraus die Ankündigung eines Herolds („Hört, hört! Es naht *Name, Stufe X*!“) mit einer ASCII-Trompete.

**4. Gold teilen.** Frage nach der Gruppengröße (`int`) und berechne, wie viel Gold jeder bekommt. Vergleiche `/` und `//`.
*Interaktiv:* Zeige beide Varianten nebeneinander („ehrlich geteilt“ vs. „Zwergen-Teilung“). Bonus: Mit `%` bekommst du den Rest, der in der Tavernenkasse landet. Zeichne einen Goldsack. Probiere danach einmal `0` als Gruppengröße. Was passiert? (Das lösen wir in Stufe 4.)

---

## Stufe 2: Listen

**5. Gruppe.** Frage zwei Gefährten ab und lege die Liste `gruppe = [name, gefaehrte1, gefaehrte2]` an. Gib die Anzahl (`len`) und den letzten Namen (`[-1]`) aus.
*Interaktiv:* Der Letzte in der Reihe hat „natürlich die Fackel vergessen“. Dazu drei ASCII-Strichmännchen.

**6. Trank getrunken.** Entferne mit `pop()` das letzte Inventarstück und gib aus, was es war. `pop()` löscht *und* liefert das Element zurück, speichere es also in einer Variablen.
*Interaktiv:* Der Held verschlingt genau das, was er vorhin in der Truhe gefunden hat („Geschmack: Drache mit einem Hauch von Socke“).

**7. Sortiertes Inventar.** Sortiere mit `sort()` alphabetisch und drehe dann mit `reverse()` um.
*Interaktiv:* Der Ordnungs-Zwerg sortiert, der Chaos-Kobold dreht alles wieder um. Beobachte: Was passiert mit Wörtern, die klein geschrieben sind?

**8. Besitze ich das?** Gib `"Fackel" in inventar` aus. Welcher Datentyp kommt heraus?
*Interaktiv:* Frage per `input()`, wonach der Held im Rucksack wühlt, und zeige `True` oder `False` samt `type(...)`.

**9. Beute-Ausschnitt.** Zeige mit Slicing die ersten Gegenstände und mit `inventar[-2:]` die letzten zwei.
*Interaktiv:* Frage, wie viele Dinge an den Gürtel passen (`int`), und nutze `inventar[0:anzahl]`. Was passiert, wenn die Zahl größer ist als das Inventar?

**10. Ausrüstung tauschen.** Vertausche das erste und letzte Inventarstück mit einer Hilfsvariable.
*Interaktiv:* Ein Taschendieb-Kobold war's. ASCII-Kobold inklusive.

**11. Zwei Listen verbinden.** Hänge eine Liste `beute` (zwei Eingaben) mit `+` an das Inventar an.
*Interaktiv:* Ein Drache lässt zwei Dinge fallen, und der Rucksack „quillt über“ (`len`).

---

## Exkurs: Wie würfelt ein Computer? (`random`)

Ein Computer kann nicht *wirklich* würfeln, denn er tut immer genau das, was berechnet wird. Deshalb nutzt Python **Pseudozufall**: Eine Formel erzeugt aus einer Startzahl, dem **Seed**, eine endlose Zahlenfolge, die zufällig *aussieht*.

Stell dir einen extrem langen, perfekt gemischten Kartenstapel vor. Der Seed bestimmt, an welcher Stelle du abhebst. Wer an derselben Stelle abhebt, bekommt dieselben Karten. Python wählt den Seed beim Start automatisch (aus Systemzeit bzw. Betriebssystem), deshalb sieht jeder Programmlauf anders aus.

```python
import random                      # Werkzeugkiste holen (Imports stehen ganz oben)

random.randint(1, 6)               # ganze Zahl von 1 bis 6, BEIDE Grenzen inklusive
random.choice(["Ork", "Elf"])      # zufälliges Element aus einer Liste
random.shuffle(liste)              # mischt die Liste selbst durch (gibt nichts zurück)
random.seed(42)                    # Startpunkt festlegen: ab jetzt immer dieselbe Folge
```

**Experiment:** Schreibe `random.seed(42)` vor deine Würfe und startet alle das Programm. Alle im Kurs würfeln exakt dieselben Zahlen. Nimm die Zeile wieder raus, und jeder würfelt wieder anders.

**Achtung, Stolperfalle:** `randint(1, 6)` *enthält* die 6. Bei Slicing (`[0:3]`) ist die Obergrenze dagegen *nicht* dabei.

---

## Stufe 3: Kombiaufgaben

**12. Würfelwürfe.** Würfle dreimal mit `random.randint(1, 6)` und speichere die Ergebnisse in der Liste `wuerfe`. Gib `sum()`, `max()`, `min()` und den Durchschnitt (`sum / len`) aus.
*Interaktiv:* Jeder Wurf startet erst nach **ENTER**. Speichere die sechs Würfelbilder als ASCII-Art in einer Liste und zeige mit `wuerfel_bilder[wurf - 1]` das passende Bild an (`-1`, weil Listen bei 0 beginnen). Hänge mit `random.choice` einen zufälligen Spruch an („Die Katze schaut zu. Sie urteilt nicht. Sie urteilt doch.“).

**13. Angriffsserie.** Berechne den Schaden von drei Angriffen mit `random.randint(1, waffe) + staerke // 2`, speichere ihn in einer Liste, sortiere sie und gib den stärksten und schwächsten Treffer aus.
*Interaktiv:* Jeder Angriff bekommt mit `random.choice` einen zufälligen Kampfruf („Für Ruhm und Käse!“).

**14. Abschluss.** Baue einen vollständigen, schön formatierten Charakterbogen mit Gruppe, Inventar, Fähigkeiten, Würfelstatistik und Gold pro Kopf (`gold / len(gruppe)`). Nutze `\n` und `:.2f`. Tipp: `', '.join(gruppe)` klebt die Namen hübsch zusammen.

> **Hinweis:** Kampfschleifen (`for`, `while`) kommen erst später. Deshalb wiederholen wir Würfe hier noch von Hand. Das Programm wird dabei absichtlich länger und schreit förmlich nach Schleifen. Genau das ist der Punkt.

---

## Stufe 4: Entscheidungen mit `if` / `elif` / `else`

Bisher läuft das Programm stur von oben nach unten. Ab jetzt kann es **entscheiden**.

```python
if bedingung:
    ...
elif andere_bedingung:
    ...
else:
    ...
```

Vergleiche: `==` (gleich), `!=` (ungleich), `<`, `>`, `<=`, `>=`. Kombinieren: `and`, `or`, `not`. Wichtig: `=` weist zu, `==` vergleicht.

**15. Sicherheitsnetze.** Drei Stellen aus den früheren Stufen können abstürzen. Sichere sie ab:
- `inventar.remove(verkauft)` stürzt ab, wenn der Gegenstand nicht existiert. Prüfe vorher mit `if verkauft in inventar`. Der Händler darf beleidigt sein, wenn der Held etwas verkaufen will, das er gar nicht hat.
- `gold / gruppengroesse` stürzt bei `0` ab (Aufgabe 4).
- `random.randint(1, waffe)` stürzt ab, wenn `waffe < 1` ist (Aufgabe 13).

**16. Klassen-Begrüßung.** Begrüße den Helden je nach `klasse` mit eigener ASCII-Art und eigenem Spruch: Magier, Krieger, Schurke. Bei allem anderen greift `else` („Die Gilde kennt so etwas nicht, aber das Freibier gilt trotzdem!“). Tipp: `klasse.lower()` macht aus `"MAGIER"` ein `"magier"`, damit die Schreibweise egal ist.

**17. Titel nach Stufe.** Baue eine `elif`-Kette: Stufe unter 3 = „Novize“, unter 6 = „Abenteurer“, unter 10 = „Veteran“, sonst „Legende“. Der Torwächter begrüßt den Helden mit seinem Titel. Frage: Warum reicht bei `elif stufe < 6` die Bedingung, obwohl der Held mit Stufe 2 ja auch `< 6` wäre?

**18. Zauber wirken.** Frage, ob der Held einen Feuerball wirken will (`ja`/`nein`, kostet 15 Mana). Nur wenn er `ja` sagt **und** genug Mana hat, klappt der Zauber und das Mana sinkt. Bei zu wenig Mana gibt es ein trauriges Fünkchen, bei `nein` steckt er den Stab ein. Nutze `antwort.lower() in ["ja", "j"]`, damit auch „J“ und „JA“ funktionieren.

**19. Truhe mit Falle.** Würfle `random.randint(1, 4)`. Bei 1 gibt es eine Pfeilfalle (Lebenspunkte sinken um `randint(1, 6)`), bei 2 einen Mimic (−5 Gold), sonst Gold zwischen 5 und 25.

**20. Angriffswurf.** Würfle einen W20 gegen die Rüstungsklasse eines Goblins (`randint(8, 18)`). Bei **20** gibt es einen kritischen Treffer mit doppeltem Schaden und ASCII-Explosion, bei **1** einen Patzer. Sonst trifft der Held, wenn `wurf + staerke // 2 >= gegner_rk` gilt, andernfalls geht der Schlag daneben. Beachte die Reihenfolge der Bedingungen.

**21. Abschluss erweitern.** Ergänze den Charakterbogen um den Titel aus Aufgabe 17 und einen Gesundheitszustand per `elif`-Kette (Lebenspunkte über 50 = „strotzt vor Kraft“, über 25 = „ein paar Kratzer“, sonst „sieht aus, als hätte ein Ork ihn als Kissen benutzt“). Die Falle aus Aufgabe 19 wirkt sich jetzt direkt auf den Bogen aus.

**Bonus: Boss-Duell.** Held und Drache würfeln je einen W20 (der Held plus `staerke // 2`, der Drache plus 5). Wer höher liegt, gewinnt. Bei Gleichstand teilen sich beide einen Keks.
