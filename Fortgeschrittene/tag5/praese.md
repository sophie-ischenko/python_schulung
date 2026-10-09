---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    background: #faf7f2;
    color: #2b2b2b;
    padding: 50px 70px;
  }
  h1 { color: #7a3e1d; }
  h2 { color: #7a3e1d; border-bottom: 3px solid #e0a96d; padding-bottom: 6px; }
  strong { color: #b5541c; }
  code { background: #f0e6d8; color: #7a3e1d; border-radius: 4px; }
  table { font-size: 0.72em; }
  th { background: #e0a96d; color: #2b2b2b; }
  section.titel { background: #2b2b2b; color: #faf7f2; text-align: center; justify-content: center; }
  section.titel h1 { color: #e0a96d; font-size: 2.4em; }
  section.titel h2 { color: #faf7f2; border: none; font-weight: 300; }
  section.fehler h2 { color: #a32020; border-color: #d98080; }
---

<!-- _class: titel -->
<!-- _paginate: false -->

# Kreaturen-Archiv

## Eine Desktop-App mit JSON-Daten, Suche, Filter und Animation

Python-Projekt · Tag 4

---

## Worum geht es?

Du baust eine **Desktop-App**, die eine größere Datenmenge aus einer JSON-Datei einliest und interaktiv darstellt.

- `kreaturen.json`: Titel, Untertitel und **30 erfundene Kreaturen**
- Jede Kreatur hat einen **Typ**, **drei Werte** und eine **Beschreibung**
- Die Oberfläche baust **du selbst**
- Vorbereitet ist nur das Fundament: Laden, zwei Hilfsfunktionen, Hauptprogramm

---

## Das kann die App am Ende

| Funktion | Was passiert |
|---|---|
| **Suchen** | Namen eintippen, auf „Suchen" klicken |
| **Filtern** | Typ-Buttons: Alle, Feuer, Wasser, Wald, Schatten, Eis |
| **Karten erzeugen** | Pro Treffer ein Button, der Zähler zeigt die Anzahl |
| **Details** | Klick auf Karte: Beschreibung, Werte, **animierte Balken** |
| **Zufall** | Zufällige Kreatur auswählen |
| **Stärkste** | Stärkste Kreatur der aktuellen Auswahl |
| **Duell** | Kampf gegen einen zufälligen Gegner |

---

## Die Dateien

| Datei | Inhalt |
|---|---|
| `kreaturen.json` | Die Daten |
| `projekt.py` | **Dein Startpunkt:** Fundament + nummerierte Aufgaben |
| `projekt_loesung.py` | Die fertige Lösung |

Alle Dateien liegen im **selben Ordner**.

---

## Wie läuft das Programm ab?

1. `daten_laden` liest die JSON und berechnet den **Gesamtwert** jeder Kreatur
2. `main` erstellt das Fenster, `oberflaeche_bauen` setzt alle Widgets hinein
3. `ergebnisse_aktualisieren` **filtert**, löscht alte Karten, erzeugt neue
4. Klick auf eine Karte → Button ruft `detail_zeigen` auf
5. `animation_schritt` zeichnet neu und plant sich mit `window.after(20, ...)` **selbst wieder ein**, bis `fortschritt` 100 erreicht

---

## Idee 1

- Alle Kreaturen: `daten["kreaturen"]`
- Die Liste `sichtbare` enthält nur, was gerade zu **Suche und Filter** passt
- Bei jeder Änderung wird `sichtbare` **neu aufgebaut**

```text
daten["kreaturen"]  ──Filter + Suche──▶  sichtbare  ──Schleife──▶  Karten
     (alle 30)                         (z. B. 7)                 (7 Buttons)
```

---

## Idee 2

Für **jede Kreatur** in `sichtbare` entsteht per Schleife ein Button (Abschnitt 32).

Vor dem Neuaufbau müssen die alten Karten **weg**:

```python
for k in karten:
    k.destroy()
karten = []          # Liste leeren!
```

---

## Merksatz: lambda bei Buttons in Schleifen

Ohne Trick würde **jeder** Button denselben Wert benutzen.

```python
command=lambda t=typ: typ_waehlen(t)
```

Das `t=typ` „friert" den Wert **im Moment des Erzeugens** ein, sodass jeder Button eigene Werte hat.

---

## Idee 3

- `fortschritt` läuft von **0 bis 100**
- In jedem Schritt: Wert × `fortschritt / 100`
- Bei `fortschritt = 50` ist jeder Balken **halb so lang**
- Der Balken ist nur **Text**: `"█" * 16`
- Die Gesamtzahl im Canvas ändert sich mit `itemconfig` wie beim Pomodoro-Timer

```python
"█" * 8    # → ████████   (halber Balken bei 16 Stellen)
```


---

<!-- _class: titel -->
<!-- _paginate: false -->

# Los geht's! 



