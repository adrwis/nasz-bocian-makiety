"""Składa strony makiety z szablonu (nagłówek, stopka) i plików w strony/.

Kolory i czcionki kopiuje z branding/tokeny.css, logo z logo/bocian_stopka.png.

strony/index.html trafia do index.html w katalogu głównym,
strony/<nazwa>.html do <nazwa>/index.html.
Tytuł strony bierze się z pierwszej linii pliku: <!-- tytul: ... -->

Użycie: python3 narzedzia/zbuduj.py
"""
import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Branding i logo trzymamy w repo Nasz Bocian (psycho/nasz-bocian), tu tylko kopie.
NASZ_BOCIAN = ROOT.parent.parent

# Strony, których jeszcze nie projektowałyśmy: pokazują „Tę stronę właśnie przygotowujemy”.
W_PRZYGOTOWANIU = {
    "nieplodnosc": "Niepłodność",
    "adopcja": "Adopcja",
    "rodzina-zastepcza": "Rodzina zastępcza",
    "zaakceptowana-bezdzietnosc": "Zaakceptowana bezdzietność",
    "zachowaj-plodnosc": "Zachowaj płodność",
    "szkolenia": "Szkolenia",
    "o-nas": "O nas",
    "szukam-informacji": "Szukam informacji",
    "linia-pomocy": "Linia pomocy „Pacjent dla pacjenta”",
    "kontakt": "Kontakt",
}

STRONA = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{tytul} | Nasz Bocian (makieta)</title>
<link rel="icon" href="https://nasz-bocian.pl/sites/default/files/favi.png">
<link rel="stylesheet" href="{root}assets/branding.css?v={wersja}">
<link rel="stylesheet" href="{root}assets/makieta.css?v={wersja}">
<script src="{root}assets/makieta.js?v={wersja}" defer></script>
</head>
<body class="{klasa}">
{naglowek}
{tresc}
{stopka}
</body>
</html>
"""


# Spójniki i jednoliterowe słowa nie zostają na końcu wiersza (Ada 2026-10-21):
# po nich zwykłą spację zamieniamy na twardą. Zmienia się tylko łamanie wierszy, nie tekst.
SIEROTY = re.compile(r"(?<![\w\u00C0-\u017F])(i|a|o|u|w|z|oraz|albo|lub|czy|ani|ale|bo|że|czyli|I|A|O|U|W|Z|Oraz|Albo|Lub|Czy|Ani|Ale|Bo|Że|Czyli) (?=\S)")


def bez_sierot(html_):
    czesci = re.split(r"(<[^>]+>)", html_)
    wynik, w_skrypcie = [], False
    for c in czesci:
        if c.startswith("<"):
            w_skrypcie = c.lower().startswith(("<script", "<style")) or (w_skrypcie and not c.lower().startswith(("</script", "</style")))
            wynik.append(c)
        else:
            wynik.append(c if w_skrypcie else SIEROTY.sub(lambda m: m.group(1) + "\u00a0", c))
    return "".join(wynik)


def czytaj(sciezka):
    return (ROOT / sciezka).read_text(encoding="utf-8")


def zbuduj():
    shutil.copyfile(NASZ_BOCIAN / "branding" / "tokeny.css", ROOT / "assets" / "branding.css")
    shutil.copyfile(NASZ_BOCIAN / "logo" / "bocian_stopka.png", ROOT / "assets" / "logo.png")

    # Numer wersji w adresach plików: GitHub Pages pozwala przeglądarce trzymać je 10 minut,
    # więc bez niego zmiany w stylach nie byłyby od razu widoczne.
    wersja = hashlib.sha1(b"".join((ROOT / "assets" / f).read_bytes()
                                   for f in ("branding.css", "makieta.css", "makieta.js"))).hexdigest()[:8]

    naglowek = czytaj("szablon/naglowek.html")
    stopka = czytaj("szablon/stopka.html").replace("{{social}}", czytaj("szablon/_social.html"))

    strony = {}
    for plik in sorted((ROOT / "strony").glob("*.html")):
        tresc = plik.read_text(encoding="utf-8")
        tytul = re.match(r"<!-- tytul: (.*?) -->", tresc).group(1)
        strony[plik.stem] = (tytul, tresc.split("\n", 1)[1])
    szablon = czytaj("szablon/w-przygotowaniu.html")
    for slug, tytul in W_PRZYGOTOWANIU.items():
        strony.setdefault(slug, (tytul, szablon.replace("{{tytul}}", tytul)))

    for slug, (tytul, tresc) in strony.items():
        if slug == "index":
            cel, root = ROOT / "index.html", "./"
        else:
            cel, root = ROOT / slug / "index.html", "../"
            cel.parent.mkdir(exist_ok=True)

        # Bieżąca pozycja menu dostaje aria-current, żeby była podkreślona.
        nag = naglowek.replace(f'href="{{{{root}}}}{slug}/"', f'href="{{{{root}}}}{slug}/" aria-current="page"')
        html = STRONA.format(tytul=tytul, root=root, naglowek=nag, tresc=tresc, stopka=stopka,
                             klasa="strona-glowna" if slug == "index" else "", wersja=wersja)
        cel.write_text(bez_sierot(html.replace("{{root}}", root)), encoding="utf-8")
        print(f"Zapisano {cel.relative_to(ROOT)}")

if __name__ == "__main__":
    zbuduj()
