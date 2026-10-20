"""Składa strony makiety z szablonu (nagłówek, stopka) i plików w strony/.

strony/index.html trafia do index.html w katalogu głównym,
strony/<nazwa>.html do <nazwa>/index.html.
Tytuł strony bierze się z pierwszej linii pliku: <!-- tytul: ... -->

Użycie: python3 narzedzia/zbuduj.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STRONA = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{tytul} | Nasz Bocian (makieta)</title>
<link rel="icon" href="https://nasz-bocian.pl/sites/default/files/favi.png">
<link rel="stylesheet" href="{root}assets/makieta.css">
<script src="{root}assets/makieta.js" defer></script>
</head>
<body>
{naglowek}
{tresc}
{stopka}
</body>
</html>
"""


def czytaj(sciezka):
    return (ROOT / sciezka).read_text(encoding="utf-8")


def zbuduj():
    naglowek = czytaj("szablon/naglowek.html")
    stopka = czytaj("szablon/stopka.html").replace("{{social}}", czytaj("szablon/_social.html"))

    for plik in sorted((ROOT / "strony").glob("*.html")):
        tresc = plik.read_text(encoding="utf-8")
        tytul = re.match(r"<!-- tytul: (.*?) -->", tresc).group(1)
        tresc = tresc.split("\n", 1)[1]

        if plik.stem == "index":
            cel, root = ROOT / "index.html", "./"
        else:
            cel, root = ROOT / plik.stem / "index.html", "../"
            cel.parent.mkdir(exist_ok=True)

        html = STRONA.format(tytul=tytul, root=root, naglowek=naglowek, tresc=tresc, stopka=stopka)
        cel.write_text(html.replace("{{root}}", root), encoding="utf-8")
        print(f"Zapisano {cel.relative_to(ROOT)}")


if __name__ == "__main__":
    zbuduj()
