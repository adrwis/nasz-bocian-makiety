"""Buduje makietę strony z żywego HTML produkcji nasz-bocian.pl.

Bierze prawdziwy nagłówek, menu i stopkę, podmienia tylko treść w <main>
na wersję z pliku tresc.html w folderze makiety. Style i obrazy ładują się
z produkcji, więc makieta wygląda jak prawdziwa strona.

Użycie: python3 narzedzia/zbuduj.py jak-mozemy-ci-pomoc
"""
import re
import subprocess
import sys
from pathlib import Path

PROD = "https://nasz-bocian.pl"
ROOT = Path(__file__).resolve().parent.parent

PASEK = """
<div class="makieta-pasek" role="note">
  <strong>Makieta robocza:</strong> propozycja zmian do akceptacji przez Stowarzyszenie Nasz Bocian. Strona nieoficjalna.
  <a href="{prod}/{slug}">Obecna wersja</a> · <a href="../">Wszystkie makiety</a> · <a href="https://github.com/adrwis/nasz-bocian-makiety/blob/main/{slug}/dla-redaktora.md">Instrukcja dla redaktora</a> · <a href="https://github.com/adrwis/nasz-bocian-makiety/blob/main/{slug}/poprawki.css">CSS dla programisty</a>
</div>
"""


def pobierz(url):
    # curl zamiast urllib: Python z python.org bywa bez certyfikatów SSL.
    wynik = subprocess.run(["curl", "-sf", "-A", "Mozilla/5.0", url], capture_output=True, check=True)
    return wynik.stdout.decode("utf-8")


def zbuduj(slug):
    folder = ROOT / slug
    html = pobierz(f"{PROD}/{slug}")
    (ROOT / "zrodlo").mkdir(exist_ok=True)
    (ROOT / "zrodlo" / f"{slug}.html").write_text(html, encoding="utf-8")

    # Bez analityki, Cloudflare i banera cookies: makieta niczego nie śledzi.
    html = re.sub(r'<script[^>]*google_tag[^>]*></script>', "", html)
    html = re.sub(r'<script[^>]*email-decode[^>]*></script>', "", html)
    html = re.sub(r'<link rel="preconnect" href="https://challenges\.cloudflare\.com"[^>]*>', "", html)
    html = html.replace('"popup_enabled":true', '"popup_enabled":false')
    # Adres e-mail jest zakodowany przez Cloudflare, wstawiamy go jawnie.
    html = re.sub(
        r'<a href="/cdn-cgi/l/email-protection[^"]*"><span class="__cf_email__"[^>]*>.*?</span></a>',
        '<a href="mailto:stowarzyszenie@nasz-bocian.pl">stowarzyszenie@nasz-bocian.pl</a>',
        html,
    )

    # Ścieżki względne prowadzą do produkcji.
    html = re.sub(r'(href|src|srcset)="/(?!/)', rf'\1="{PROD}/', html)

    html = html.replace(
        "</head>",
        '<meta name="robots" content="noindex, nofollow">\n'
        '<link rel="stylesheet" href="poprawki.css">\n'
        '<link rel="stylesheet" href="../makieta.css">\n</head>',
    )
    html = re.sub(r"(<body[^>]*>)", r"\1" + PASEK.format(prod=PROD, slug=slug), html, count=1)

    tresc = (folder / "tresc.html").read_text(encoding="utf-8")
    html = re.sub(r"<main role=\"main\">.*?</main>", lambda _: tresc.strip(), html, flags=re.S)

    (folder / "index.html").write_text(html, encoding="utf-8")
    print(f"Zapisano {folder / 'index.html'}")


if __name__ == "__main__":
    zbuduj(sys.argv[1])
