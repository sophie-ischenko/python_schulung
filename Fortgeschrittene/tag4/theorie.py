"""
Tag 4 – Theorie: Tkinter & GUI-Programmierung

Heute verlassen wir die reine Konsolenausgabe und bauen eine
grafische Benutzeroberfläche.

Wir verwenden dafür Tkinter.

Die Theorie ist direkt als Python-Datei aufgebaut.
Du kannst sie ausführen und die Beispiele an den markierten
Stellen selbst ausprobieren.

Die meisten Beispiele sind deshalb auskommentiert.
Entferne die # vor einem Beispiel und führe die Datei aus,
um es direkt auszuprobieren.


LERNZIELE
---------

Du kannst:

- ein Tkinter-Fenster erstellen
- Widgets wie Label, Button und Canvas verwenden
- Widgets mit grid() positionieren
- Eigenschaften von Widgets verändern
- Bilder in einer GUI anzeigen
- auf Button-Klicks reagieren
- Funktionen mit Buttons verbinden
- mit after() zeitgesteuerte Aktionen ausführen
- mehrere GUI-Elemente miteinander verbinden
- ein kleines GUI-Programm strukturieren


VORAUSSETZUNGEN
---------------

Du solltest bereits kennen:

- Variablen
- Datentypen
- Bedingungen
- Funktionen
- Parameter
- return
- Schleifen
- Strings
- Listen
- grundlegende Imports


============================================================
1. WAS IST EINE GUI?
============================================================

GUI steht für:

    Graphical User Interface

Also eine grafische Benutzeroberfläche.

Bisher haben wir Programme hauptsächlich über das Terminal
bedient:

    name = input("Wie heißt du? ")
    print(f"Hallo {name}!")

Eine GUI arbeitet anders.

Statt nur Text im Terminal zu verwenden, können wir zum Beispiel
folgende Elemente anzeigen:

    - Fenster
    - Texte
    - Buttons
    - Bilder
    - Eingabefelder

Der Benutzer kann anschließend mit diesen Elementen interagieren.


============================================================
2. TKINTER IMPORTIEREN
============================================================

Tkinter ist eine Python-Bibliothek für grafische
Benutzeroberflächen.

Wir importieren sie meistens so:

"""

import tkinter as tk


"""
Durch "as tk" können wir später kurz "tk" verwenden.

Zum Beispiel:

    tk.Tk()

statt:

    tkinter.Tk()


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

Entferne die Kommentare und führe das Beispiel aus.

"""

# import tkinter as tk

# window = tk.Tk()

# window.mainloop()


"""
Das Fenster sollte sich öffnen.

Das Programm bleibt geöffnet, weil mainloop() auf Ereignisse
wartet.


============================================================
3. DAS HAUPTFENSTER
============================================================

Das Hauptfenster ist der Ausgangspunkt unserer Anwendung.

"""

# window = tk.Tk()

# window.mainloop()


"""
tk.Tk()
--------

Erstellt das Hauptfenster.

mainloop()
----------

Startet die Ereignisschleife.

Das Programm wartet anschließend beispielsweise auf:

    - Mausklicks
    - Tastatureingaben
    - Buttons
    - Timer
    - Fensteraktionen

Eine Tkinter-Anwendung braucht normalerweise genau ein
Hauptfenster.


============================================================
4. FENSTERTITEL
============================================================

Mit title() können wir den Titel des Fensters setzen.

"""

# window = tk.Tk()
# window.title("Mein erstes GUI")
# window.mainloop()


"""
Du kannst den Text beliebig verändern.

Zum Beispiel:

"""

# window.title("Pomodoro")


"""
Natürlich funktioniert das nur, wenn window bereits existiert.


============================================================
5. HINTERGRUNDFARBE UND ABSTÄNDE
============================================================

Mit config() können wir Eigenschaften eines Fensters verändern.

"""

# window.config(
#     bg="#f7f5dd"
# )


"""
bg steht für background.

Wir können zusätzlich Innenabstände festlegen:

"""

# window.config(
#     bg="#f7f5dd",
#     padx=100,
#     pady=50
# )


"""
Dabei gilt:

    padx → horizontaler Innenabstand
    pady → vertikaler Innenabstand


============================================================
6. WIDGETS
============================================================

Die einzelnen Bestandteile einer GUI nennt man Widgets.

Tkinter bietet viele verschiedene Widgets.

Für unseren Timer brauchen wir hauptsächlich:

    Label
    Button
    Canvas
    Toplevel

Einige weitere Widgets sind:

    Entry
        Eingabefeld

    Frame
        Bereich zum Gruppieren anderer Widgets

    Checkbutton
        Kontrollkästchen

    Listbox
        Liste mit auswählbaren Elementen


============================================================
7. LABEL
============================================================

Ein Label zeigt Text an.

"""

# window = tk.Tk()

# label = tk.Label(
#     window,
#     text="Hallo!"
# )

# label.pack()

# window.mainloop()


"""
Hier passiert etwas Neues.

Wir erstellen zuerst das Label:

    label = tk.Label(...)

Danach müssen wir festlegen, wo es angezeigt werden soll.

Dafür gibt es verschiedene Layout-Manager.

Wir verwenden im Kurs hauptsächlich:

    grid()


============================================================
8. GRID
============================================================

grid() ordnet Widgets in Zeilen und Spalten an.

"""

# window = tk.Tk()

# label = tk.Label(
#     window,
#     text="Hallo!"
# )

# label.grid(
#     row=0,
#     column=0
# )

# window.mainloop()


"""
Die Zählung beginnt bei 0.

Zum Beispiel:

    row=0, column=0

ist die erste Zeile und die erste Spalte.

Eine einfache Anordnung:

    column 0    column 1    column 2

    row 0         A           B           C
    row 1         D           E           F
    row 2         G           H           I


Wir können mehrere Widgets auf diese Weise anordnen:

"""

# label_a = tk.Label(window, text="A")
# label_a.grid(row=0, column=0)

# label_b = tk.Label(window, text="B")
# label_b.grid(row=0, column=1)

# label_c = tk.Label(window, text="C")
# label_c.grid(row=1, column=0)


"""
------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

Erstelle selbst drei Labels.

Positioniere sie beispielsweise so:

    A → row 0, column 0
    B → row 0, column 1
    C → row 1, column 0

------------------------------------------------------------
"""

"""
============================================================
9. ABSTÄNDE MIT GRID()
============================================================

Mit padx und pady können wir Abstände erzeugen.

"""

# label.grid(
#     row=0,
#     column=0,
#     padx=20,
#     pady=10
# )


"""
padx erzeugt horizontalen Abstand.

pady erzeugt vertikalen Abstand.


============================================================
10. LABEL GESTALTEN
============================================================

Labels können verschiedene Eigenschaften besitzen.

"""

# label = tk.Label(
#     window,
#     text="Pomodoro",
#     font=("Courier", 40),
#     fg="#e7305b",
#     bg="#f7f5dd"
# )


"""
Wichtige Eigenschaften:

    text
        Angezeigter Text

    font
        Schriftart und Schriftgröße

    fg
        Vordergrundfarbe, zum Beispiel Textfarbe

    bg
        Hintergrundfarbe


Zum Beispiel:

"""

# label = tk.Label(
#     window,
#     text="Arbeit",
#     font=("Courier", 40),
#     fg="#e7305b",
#     bg="#f7f5dd"
# )


"""
------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

Erstelle ein Label mit:

    Text: "Pomodoro"
    Schriftgröße: 30
    Schriftart: Courier

Experimentiere anschließend mit der Farbe.
------------------------------------------------------------
"""


============================================================
11. WIDGETS NACH DEM ERSTELLEN VERÄNDERN
============================================================

Mit config() können wir ein Widget später verändern.

"""

# label.config(
#     text="Pause"
# )


"""
Auch die Farbe kann geändert werden:

"""

# label.config(
#     fg="#9bdeac"
# )


"""
Oder mehrere Eigenschaften gleichzeitig:

"""

# label.config(
#     text="Pause",
#     fg="#9bdeac"
# )


"""
Das wird für unseren Timer wichtig.

Die Überschrift kann später beispielsweise zwischen:

    Timer
    Arbeit
    Pause

wechseln.


============================================================
12. BUTTONS
============================================================

Ein Button wird mit tk.Button() erstellt.

"""

# button = tk.Button(
#     window,
#     text="Start"
# )

# button.grid(
#     row=0,
#     column=0
# )


"""
Ein Button allein macht noch nichts.

Wir müssen festlegen, welche Funktion beim Klick ausgeführt
werden soll.


============================================================
13. FUNKTIONEN MIT BUTTONS VERBINDEN
============================================================

Wir kennen bereits Funktionen.

"""

# def hallo():
#     print("Hallo!")


"""
Diese Funktion können wir mit einem Button verbinden:

"""

# button = tk.Button(
#     window,
#     text="Klick mich",
#     command=hallo
# )



Wenn der Benutzer klickt, wird hallo() ausgeführt.

Wichtig:

Richtig:

    command=hallo

Nicht:

    command=hallo()

Warum?

Mit:

    command=hallo

übergeben wir die Funktion.

Tkinter entscheidet dann, wann sie ausgeführt wird.

Mit:

    command=hallo()

würden wir die Funktion bereits beim Erstellen des Buttons
ausführen.


------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

"""

# def begruessen():
#     print("Hallo aus dem Button!")

# button = tk.Button(
#     window,
#     text="Klick mich",
#     command=begruessen
# )

# button.grid(
#     row=0,
#     column=0
# )


"""
============================================================
14. EIN LABEL DURCH EINEN BUTTON VERÄNDERN
============================================================

Jetzt verbinden wir zwei Widgets miteinander.

"""

# def aendern():
#     label.config(
#         text="Gestartet!"
#     )


# label = tk.Label(
#     window,
#     text="Noch nicht gestartet"
# )

# label.grid(
#     row=0,
#     column=0
# )


# button = tk.Button(
#     window,
#     text="Start",
#     command=aendern
# )

# button.grid(
#     row=1,
#     column=0
# )


"""
Hier passiert Folgendes:

    1. Das Label wird erstellt.
    2. Der Button wird erstellt.
    3. Der Button ruft aendern() auf.
    4. aendern() verändert das Label.

Das ist ein wichtiges Grundprinzip für unsere GUI.


============================================================
15. BUTTONS DEAKTIVIEREN
============================================================

Ein Button kann deaktiviert werden.

"""

# button.config(
#     state="disabled"
# )


"""
Dadurch kann der Benutzer ihn nicht mehr anklicken.

Wieder aktivieren:

"""

# button.config(
#     state="normal"
# )


"""
Bei unserem Timer ist das sinnvoll.

Während der Timer läuft, soll Start nicht erneut gedrückt werden
können.

Sonst könnten mehrere Timer gleichzeitig laufen.


============================================================
16. CANVAS
============================================================

Ein Canvas ist eine Zeichenfläche.

Wir können darauf unter anderem anzeigen:

    - Text
    - Bilder
    - Linien
    - Formen

Für unseren Pomodoro-Timer verwenden wir ein Canvas
für die Tomate und die Zeitanzeige.

"""

# canvas = tk.Canvas(
#     window,
#     width=200,
#     height=224,
#     bg="#f7f5dd",
#     highlightthickness=0
# )

# canvas.grid(
#     row=2,
#     column=2
# )


"""
width und height bestimmen die Größe des Canvas.


============================================================
17. TEXT AUF EINEM CANVAS
============================================================

Mit create_text() können wir Text auf dem Canvas anzeigen.

"""

# timer_text = canvas.create_text(
#     100,
#     130,
#     text="00:00",
#     fill="white",
#     font=("Courier", 35, "bold")
# )


"""
Die ersten beiden Werte sind die Position:

    100 → x
    130 → y

Die Rückgabe von create_text() speichern wir in:

    timer_text

Warum?

Weil wir diesen Text später verändern möchten.


============================================================
18. CANVAS-TEXT VERÄNDERN
============================================================

Mit itemconfig() können wir ein Canvas-Element verändern.

"""

# canvas.itemconfig(
#     timer_text,
#     text="24:59"
# )


"""
Damit können wir später jede Sekunde die Anzeige aktualisieren.


============================================================
19. BILDER ANZEIGEN
============================================================

Tkinter kann auch Bilder anzeigen.

Dafür verwenden wir PhotoImage.

"""

# tomato_img = tk.PhotoImage(
#     file="bilder/tomato.png"
# )


"""
Danach können wir das Bild auf dem Canvas anzeigen:

"""

# canvas.create_image(
#     100,
#     112,
#     image=tomato_img
# )


"""
Die Position:

    x = 100
    y = 112

liegt ungefähr in der Mitte unseres 200 x 224 großen Canvas.


WICHTIG:

Die Bildvariable sollte erhalten bleiben:

    tomato_img = tk.PhotoImage(...)

und nicht nur innerhalb einer Funktion erstellt werden.

Sonst kann das Bild von Python wieder aus dem Speicher entfernt
werden.


============================================================
20. ZEIT DARSTELLEN
============================================================

Für unseren Timer brauchen wir Minuten und Sekunden.

Eine Möglichkeit wäre:

    minuten = 5
    sekunden = 7

Wir möchten daraus:

    05:07

machen.

Dafür können wir einen f-String verwenden.

"""

# minuten = 5
# sekunden = 7

# anzeige = f"{minuten:02d}:{sekunden:02d}"

# print(anzeige)


"""
Ergebnis:

    05:07

02d bedeutet:

    mindestens zwei Stellen
    fehlende Stellen werden mit 0 aufgefüllt.


============================================================
21. SEKUNDEN IN MINUTEN UND SEKUNDEN UMWANDELN
============================================================

Für den Timer ist es einfacher, die verbleibende Zeit
als eine einzige Zahl zu speichern.

Zum Beispiel:

    125 Sekunden

Daraus müssen wir:

    2 Minuten
    5 Sekunden

berechnen.

Dafür verwenden wir ganzzahlige Division:

"""

# verbleibende_sekunden = 125

# minuten = verbleibende_sekunden // 60

# print(minuten)


"""
Ergebnis:

    2


Für die verbleibenden Sekunden verwenden wir den Restoperator:

"""

# sekunden = verbleibende_sekunden % 60

# print(sekunden)


"""
Ergebnis:

    5

Damit:

"""

# verbleibende_sekunden = 125

# minuten = verbleibende_sekunden // 60
# sekunden = verbleibende_sekunden % 60

# print(f"{minuten:02d}:{sekunden:02d}")


"""
Ergebnis:

    02:05

Das ist für unseren Countdown deutlich einfacher als zwei
separate Variablen.


============================================================
22. after()
============================================================

Tkinter bietet mit after() eine Möglichkeit,
eine Funktion später erneut aufzurufen.

Zum Beispiel:

"""

# window.after(
#     1000,
#     hallo
# )


"""
Das bedeutet:

    Warte 1000 Millisekunden
    und rufe dann hallo() auf.

1000 Millisekunden entsprechen:

    1 Sekunde


Wichtig:

after() hält das Programm nicht mit time.sleep() an.

Bei einer GUI wollen wir normalerweise nicht:

    time.sleep(1)

verwenden.

Das würde die GUI blockieren.

Stattdessen verwenden wir:

    window.after(...)


============================================================
23. AFTER() MIT PARAMETERN
============================================================

Wir können einer Funktion auch Argumente übergeben.

Zum Beispiel:

"""

# def anzeigen(text):
#     print(text)


# window.after(
#     1000,
#     anzeigen,
#     "Hallo!"
# )


"""
Nach einer Sekunde wird also ungefähr Folgendes ausgeführt:

    anzeigen("Hallo!")


Genau dieses Prinzip brauchen wir für unseren Countdown.


============================================================
24. EIN EINFACHER COUNTDOWN
============================================================

Wir können einen Countdown mit einer einzigen
Sekunden-Variable bauen.

"""

# def countdown(verbleibende_sekunden):
#
#     print(verbleibende_sekunden)
#
#     if verbleibende_sekunden == 0:
#         return
#
#     verbleibende_sekunden -= 1
#
#     window.after(
#         1000,
#         countdown,
#         verbleibende_sekunden
#     )


"""
Wenn wir ihn mit:

    countdown(5)

starten, passiert:

    5
    4
    3
    2
    1
    0

Die Funktion ruft sich also nach einer Sekunde selbst erneut auf.

Das ist ein Beispiel für Rekursion.


============================================================
25. DEN COUNTDOWN IN EINER GUI ANZEIGEN
============================================================

Jetzt verbinden wir den Countdown mit unserem Canvas.

"""

# def countdown(verbleibende_sekunden):
#
#     minuten = verbleibende_sekunden // 60
#     sekunden = verbleibende_sekunden % 60
#
#     anzeige = f"{minuten:02d}:{sekunden:02d}"
#
#     canvas.itemconfig(
#         timer_text,
#         text=anzeige
#     )
#
#     if verbleibende_sekunden == 0:
#         return
#
#     verbleibende_sekunden -= 1
#
#     window.after(
#         1000,
#         countdown,
#         verbleibende_sekunden
#     )


"""
Jetzt wird statt print() die GUI aktualisiert.

------------------------------------------------------------
AUSPROBIEREN
------------------------------------------------------------

Starte den Countdown beispielsweise mit:

    countdown(10)

und beobachte die Anzeige.

------------------------------------------------------------


============================================================
26. WARUM BRAUCHEN WIR timer?
============================================================

after() gibt eine Kennung zurück.

Zum Beispiel:

"""

# timer = window.after(
#     1000,
#     countdown,
#     10
# )


"""
Diese Kennung können wir speichern.

Das ist wichtig, weil wir einen laufenden Timer
später abbrechen möchten.

Dafür gibt es:

"""

# window.after_cancel(timer)


"""
Wir können deshalb eine Variable verwenden:

"""

# timer = None


"""
Wenn kein Timer läuft:

    timer = None

Wenn ein Timer läuft:

    timer = <Kennung von after()>


Dadurch können wir überprüfen:

"""

# if timer is not None:
#     window.after_cancel(timer)
#     timer = None


"""
Dieses Prinzip verwenden wir später für den Reset-Button.


============================================================
27. GLOBALE VARIABLEN IN EINER GUI
============================================================

Unsere Funktionen greifen auf GUI-Elemente zu,
die außerhalb der Funktionen erstellt wurden.

Zum Beispiel:

    canvas
    timer_text
    button_start

Bei bestimmten Variablen müssen wir außerdem innerhalb einer
Funktion den Wert verändern.

Zum Beispiel:

    timer
    phasen
    checkmark

Dafür verwenden wir:

    global


Beispiel:

"""

# timer = None
#
#
# def start():
#     global timer
#
#     timer = "läuft"


"""
Ohne global würde Python innerhalb der Funktion eine neue lokale
Variable annehmen.


============================================================
28. PHASEN DES POMODORO-TIMERS
============================================================

Unser Timer besteht aus verschiedenen Phasen.

Wir zählen sie mit einer Variable:

"""

# phasen = 0


"""
Beim Start einer neuen Phase erhöhen wir den Wert:

"""

# phasen += 1


"""
Dann können wir anhand der Phasennummer entscheiden,
welche Phase gerade läuft.

Zum Beispiel:

    Phase 1 → Arbeit
    Phase 2 → kurze Pause
    Phase 3 → Arbeit
    Phase 4 → kurze Pause
    ...
    Phase 8 → lange Pause


============================================================
29. MODULO %
============================================================

Den Rest einer Division können wir mit % bestimmen.

Beispiele:

"""

# print(8 % 2)
# print(7 % 2)
# print(10 % 5)


"""
Ergebnis:

    0
    1
    0

Damit können wir prüfen, ob eine Zahl gerade ist:

"""

# if phasen % 2 == 0:
#     print("gerade")


"""
Oder ob eine Phase durch 8 teilbar ist:

"""

# if phasen % 8 == 0:
#     print("lange Pause")


"""
Damit können wir die verschiedenen Pomodoro-Phasen
unterscheiden.


============================================================
30. BEDINGUNGEN FÜR UNSEREN TIMER
============================================================

Die Reihenfolge der Bedingungen ist wichtig.

Wir prüfen zuerst:

    Ist es Phase 8?

Dann:

    Ist es eine gerade Phase?

Dann:

    Sonst ist es eine Arbeitsphase.

Also:

"""

# if phasen % 8 == 0:
#     print("lange Pause")
#
# elif phasen % 2 == 0:
#     print("kurze Pause")
#
# else:
#     print("Arbeit")


"""
Warum zuerst % 8?

Weil 8 ebenfalls durch 2 teilbar ist.

Wenn wir zuerst nur auf % 2 prüfen würden,
würde Phase 8 als normale kurze Pause erkannt werden.


============================================================
31. EIN ZUSÄTZLICHES FENSTER
============================================================

Tkinter kann zusätzliche Fenster öffnen.

Dafür verwenden wir:

    tk.Toplevel(window)

Beispiel:

"""

# top = tk.Toplevel(window)

# top.title("Pomodoro")

# top.config(
#     bg="#f7f5dd",
#     padx=30,
#     pady=30
# )


"""
Dieses Fenster können wir anschließend mit Widgets füllen.

Zum Beispiel:

"""

# label = tk.Label(
#     top,
#     text="Zeit für die nächste Phase!",
#     font=("Courier", 16),
#     fg="#241914",
#     bg="#f7f5dd"
# )

# label.grid(
#     row=0,
#     column=0
# )


"""
Das zusätzliche Fenster wird für unseren Timer angezeigt,
wenn eine Phase beendet ist.


============================================================
32. EIN FENSTER SCHLIESSEN
============================================================

Ein Toplevel-Fenster kann mit destroy() geschlossen werden.

"""

# top.destroy()


"""
Wenn wir das Fenster innerhalb einer Funktion schließen möchten,
können wir das Fenster als Parameter übergeben.

"""

# def schliessen(fenster):
#     fenster.destroy()


"""
Dann kann die Funktion mit dem entsprechenden Fenster
aufgerufen werden.


============================================================
33. BUTTONS MIT PARAMETERN
============================================================

Hier entsteht ein kleines Problem.

Bei:

    command=schliessen

können wir nicht einfach ein Argument übergeben.

Wir möchten beispielsweise:

    schliessen(top)

ausführen.

Dafür können wir in Tkinter unter anderem lambda verwenden.

"""

# button = tk.Button(
#     top,
#     text="Schließen",
#     command=lambda: schliessen(top)
# )


"""
lambda erstellt hier eine kleine Funktion,
die beim Klick schliessen(top) aufruft.


============================================================
34. KLICK-EVENTS MIT bind()
============================================================

Neben command können Widgets auch direkt auf Ereignisse reagieren.

Mit bind() können wir beispielsweise einen Mausklick erkennen.

"""

# button.bind(
#     "<Button-1>",
#     lambda event: schliessen(top)
# )


"""
<Button-1> bedeutet:

    linke Maustaste

Die Funktion bekommt dabei ein Event-Objekt.

Deshalb steht hier:

    lambda event: ...

Das Event-Objekt brauchen wir in diesem Fall nicht,
aber Tkinter übergibt es trotzdem.


============================================================
35. LABEL ALS KLICKBARES ELEMENT
============================================================

Ein Label kann ebenfalls auf Mausklicks reagieren.

Zum Beispiel:

"""

# button = tk.Label(
#     top,
#     text="Zurück zum Timer",
#     font=("Courier", 12),
#     fg="#241914",
#     bg="#f7f5dd",
#     cursor="hand2"
# )

# button.grid(
#     row=1,
#     column=0
# )

# button.bind(
#     "<Button-1>",
#     lambda event: naechste_phase(top)
# )


"""
Ein Label kann damit optisch wie ein Button verwendet werden.

Das kann besonders hilfreich sein, wenn das native
Tkinter-Button-Design auf dem verwendeten Betriebssystem
nicht so aussieht wie gewünscht.


============================================================
36. RESET
============================================================

Unser Reset-Button soll den kompletten Timer zurücksetzen.

Dafür müssen mehrere Dinge passieren:

    - laufenden after()-Timer abbrechen
    - timer auf None setzen
    - phasen auf 0 setzen
    - checkmark leeren
    - Anzeige auf 00:00 setzen
    - Überschrift auf Timer setzen
    - Start wieder aktivieren

Das Grundprinzip:

"""

# def reset():
#
#     global timer
#     global phasen
#     global checkmark
#
#     phasen = 0
#     checkmark = ""
#
#     if timer is not None:
#         window.after_cancel(timer)
#         timer = None


"""
Anschließend aktualisieren wir die Widgets.


============================================================
37. WIDGETS UND FUNKTIONEN ZUSAMMENFÜHREN
============================================================

Jetzt haben wir alle wichtigen Bausteine.

Unser Programm besteht ungefähr aus:

    Konstanten
        ↓
    Variablen
        ↓
    Funktionen
        ↓
    Hauptfenster
        ↓
    Widgets
        ↓
    mainloop()


Für den Pomodoro-Timer kommen zusätzlich dazu:

    Start
        ↓
    nächste Phase
        ↓
    Countdown
        ↓
    Phase beendet
        ↓
    Info-Fenster
        ↓
    nächste Phase


============================================================
38. WICHTIGES MUSTER FÜR GUI-PROGRAMME
============================================================

Bei einer GUI schreiben wir nicht einfach:

    mache A
    warte
    mache B
    warte
    mache C

Stattdessen reagiert das Programm auf Ereignisse.

Zum Beispiel:

    Benutzer klickt Start
            ↓
    start_timer()
            ↓
    countdown()
            ↓
    after()
            ↓
    countdown()
            ↓
    Zeit = 0
            ↓
    info_fenster()


Die GUI läuft dabei die ganze Zeit weiter.


============================================================
39. HÄUFIGE FEHLER
============================================================

FEHLER 1: mainloop() vergessen

Ohne:

    window.mainloop()

wird die GUI nicht dauerhaft ausgeführt.


FEHLER 2: command falsch verwenden

Falsch:

    command=start_timer()

Richtig:

    command=start_timer


FEHLER 3: time.sleep() für den GUI-Countdown verwenden

Vermeide:

    time.sleep(1)

für unseren Tkinter-Timer.

Verwende:

    window.after(1000, ...)


FEHLER 4: Mehrere Timer gleichzeitig starten

Wenn Start mehrfach geklickt werden kann,
können mehrere after()-Aufrufe parallel laufen.

Deshalb prüfen wir:

    if timer is not None:
        return

und deaktivieren zusätzlich den Button.


FEHLER 5: after()-Timer beim Reset nicht abbrechen

Wenn Reset gedrückt wird, während ein Countdown läuft,
muss der alte after()-Aufruf beendet werden:

    window.after_cancel(timer)


FEHLER 6: Canvas-Text nicht speichern

Wenn wir später Text verändern möchten,
brauchen wir die ID:

    timer_text = canvas.create_text(...)

Danach:

    canvas.itemconfig(
        timer_text,
        text="00:00"
    )


============================================================
40. ZUSAMMENFASSUNG
============================================================

Die wichtigsten Befehle für heute:

Fenster erstellen:

    window = tk.Tk()


Fenster offen halten:

    window.mainloop()


Fenstertitel:

    window.title("Pomodoro")


Eigenschaften verändern:

    window.config(...)


Label:

    tk.Label(...)


Button:

    tk.Button(...)


Button mit Funktion:

    command=start_timer


Positionieren:

    widget.grid(
        row=0,
        column=0
    )


Canvas:

    tk.Canvas(...)


Text auf Canvas:

    canvas.create_text(...)


Bild auf Canvas:

    canvas.create_image(...)


Canvas-Element verändern:

    canvas.itemconfig(...)


Zusätzliches Fenster:

    tk.Toplevel(window)


Fenster schließen:

    fenster.destroy()


Zeitverzögerung:

    window.after(
        1000,
        funktion
    )


Timer abbrechen:

    window.after_cancel(timer)


Mausklick:

    widget.bind(
        "<Button-1>",
        ...
    )


============================================================
41. DAS WICHTIGSTE FÜR DIE AUFGABE
============================================================

Für unseren Pomodoro-Timer brauchst du vor allem diese Bausteine:

    tkinter
        ↓
    Hauptfenster
        ↓
    Label
        ↓
    Canvas
        ↓
    Button
        ↓
    Funktionen
        ↓
    after()
        ↓
    Countdown
        ↓
    Phasen
        ↓
    Toplevel


Die Aufgabe besteht anschließend darin,
diese Bausteine zu einer funktionierenden Anwendung
zusammenzusetzen.


============================================================
AUSPROBIER-CHALLENGE
============================================================

Bevor du mit der Aufgabe beginnst:

1. Erstelle ein Fenster.
2. Gib ihm einen eigenen Titel.
3. Erstelle ein Label.
4. Erstelle einen Button.
5. Verbinde den Button mit einer Funktion.
6. Lass die Funktion den Text des Labels verändern.
7. Erstelle ein Canvas.
8. Zeige Text auf dem Canvas an.
9. Starte einen kurzen Countdown.
10. Experimentiere mit Farben, Schriftgrößen und Positionen.

Danach kannst du mit dem Pomodoro-Timer starten.
"""