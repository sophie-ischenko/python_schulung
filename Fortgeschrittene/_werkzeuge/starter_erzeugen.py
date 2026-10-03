"""Erzeugt aus den *_loesung.py-Dateien die Starter-Dateien für die Teilnehmenden.

Marker in den Lösungsdateien:
    # >>> Hinweistext      -> Beginn eines Lösungsblocks (wird durch TODO + pass ersetzt)
    # >>>T Hinweistext     -> wie oben, aber für Tests (wird durch raise AssertionError(...) ersetzt)
    # <<<                  -> Ende des Lösungsblocks

Aufruf (aus dem Kursordner):  python _werkzeuge/starter_erzeugen.py
"""
from pathlib import Path

PAARE = {
    "aufgaben_loesung.py": "aufgaben.py",
    "gui_aufgaben_loesung.py": "gui_aufgaben.py",
    "projekt_loesung.py": "projekt.py",
    "test_funktionen_loesung.py": "test_funktionen.py",
    "kommandozeile_loesung.py": "kommandozeile.py",
    "organizer_loesung.py": "organizer.py",
}


def starter_text(text: str) -> str:
    ausgabe, im_block = [], False
    for zeile in text.splitlines():
        s = zeile.strip()
        einzug = zeile[: len(zeile) - len(zeile.lstrip())]
        if s.startswith("# >>>T"):
            ausgabe += [f"{einzug}# TODO: {s[6:].strip()}", f'{einzug}raise AssertionError("noch nicht geschrieben")']
            im_block = True
        elif s.startswith("# >>>"):
            ausgabe += [f"{einzug}# TODO: {s[5:].strip()}", f"{einzug}pass"]
            im_block = True
        elif s.startswith("# <<<"):
            im_block = False
        elif not im_block:
            ausgabe.append(zeile)
    return "\n".join(ausgabe).replace("(LÖSUNG)", "(STARTER)").replace("_loesung", "") + "\n"


if __name__ == "__main__":
    for tag in sorted(Path(".").glob("tag*")):
        for quelle, ziel in PAARE.items():
            datei = tag / quelle
            if datei.exists():
                (tag / ziel).write_text(starter_text(datei.read_text(encoding="utf-8")), encoding="utf-8")
                print("erzeugt:", tag / ziel)
