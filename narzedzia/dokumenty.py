"""Pobiera strony ze stopki nasz-bocian.pl i zapisuje ich treść jako strony makiety.

Tekst przenosimy bez zmian. Z kodu Drupala zostają tylko nagłówki, akapity,
listy, linki, pogrubienia i obrazki. Linki do stron, które mamy już w makiecie,
prowadzą do makiety, pozostałe do nasz-bocian.pl.

Użycie: python3 narzedzia/dokumenty.py, potem python3 narzedzia/zbuduj.py
"""
import html
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROD = "https://nasz-bocian.pl"

# slug w makiecie: ścieżka na nasz-bocian.pl
DOKUMENTY = {
    "ogloszenia-nieodplatne": "/nasze-dzialania/zasady-zarzadzania-nieodplatnymi-ogloszeniami-na-portalu-nasz-bocianpl-i-w-mediach",
    "reklamy": "/nasze-dzialania/polityka-publikacji-tresci-o-charakterze-reklamowym-na-portalu-nasz-bocianpl-oraz-w",
    "nota-prawna": "/nota-prawna",
    "zasady-korzystania-z-serwisu": "/zasady-korzystania-z-serwisu",
    "regulamin-platnosci": "/regulamin-wplat-fanipay",
    "wspolpraca-z-biznesem": "/nasze-dzialania/polityka-wspolpracy-stowarzyszenia-nasz-bocian-z-biznesem",
    "wspolpraca-z-partiami-politycznymi": "/nasze-dzialania/polityka-wspolpracy-stowarzyszenia-nasz-bocian-z-partiami-politycznymi",
}
W_MAKIECIE = {sciezka: slug for slug, sciezka in DOKUMENTY.items()}

# Poprawki błędów w oryginałach: (stary tekst, nowy tekst, opis). Te same zmiany trzeba wprowadzić
# na nasz-bocian.pl, lista dla redaktora: dokumenty/poprawki-tekstow.md (tworzy ją ten skrypt).
ODPIS = ("odpisów 1% podatku", "odpisów 1,5% podatku", "Od 2023 roku odpis wynosi 1,5% podatku, nie 1%.")
POPRAWKI = {
    "ogloszenia-nieodplatne": [ODPIS],
    "wspolpraca-z-biznesem": [ODPIS],
    "wspolpraca-z-partiami-politycznymi": [ODPIS],
    "regulamin-platnosci": [(
        "W przypadku wystąpienia konieczność zwrotu środków za transakcję dokonaną przez wpłacającego kartą płatniczą przyjmujący wpłatę dokonana zwrotu",
        "W przypadku wystąpienia konieczności zwrotu środków za transakcję dokonaną przez Wpłacającego kartą płatniczą przyjmujący wpłatę dokona zwrotu",
        "Błędy gramatyczne: „konieczność” zamiast „konieczności”, „dokonana” zamiast „dokona”; „Wpłacającego” wielką literą jak dalej w zdaniu.",
    )],
    "reklamy": [
        ("artkuł sponsorowany", "artykuł sponsorowany", "Literówka."),
        ("POLITYKA PUBLIKACJI TREŚCI O CHARAKTERZE REKLAMOWYM NA PORTALU NASZ-BOCIAN.PL ORAZ W MEDIACH SPOŁECZNOŚCIOWYCH STOWARZYSZENIA NASZ BOCIAN",
         "Polityka publikacji treści o charakterze reklamowym na portalu nasz-bocian.pl oraz w mediach społecznościowych Stowarzyszenia NASZ BOCIAN",
         "Tytuł strony zapisany w całości wersalikami, inaczej niż pozostałe tytuły."),
    ],
}

DOZWOLONE = {"p", "br", "h2", "h3", "h4", "ul", "ol", "li", "a", "strong", "b", "em", "i", "img"}
PUSTE = {"br", "img"}


def pobierz(url):
    wynik = subprocess.run(["curl", "-sf", "-A", "Mozilla/5.0", url], capture_output=True, check=True)
    return wynik.stdout.decode("utf-8")


def link(href):
    """Zwraca (href, czy_zewnetrzny) dla linku z treści."""
    sciezka = re.sub(r"^https?://(www\.)?nasz-bocian\.pl", "", href)
    if sciezka.rstrip("/") in W_MAKIECIE:
        return "{{root}}" + W_MAKIECIE[sciezka.rstrip("/")] + "/", False
    if sciezka.startswith("/"):
        return PROD + sciezka, True
    return href, not href.startswith(("mailto:", "tel:", "#"))


class Czysciciel(HTMLParser):
    """Zostawia dozwolone znaczniki bez klas i stylów, numeruje nagłówki h2."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.wynik = []
        self.naglowki = []
        self.w_naglowku = None

    def handle_starttag(self, tag, attrs):
        if tag not in DOZWOLONE:
            return
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            href, zewn = link(a["href"])
            extra = ' target="_blank" rel="noopener"' if zewn else ""
            self.wynik.append(f'<a href="{html.escape(href)}"{extra}>')
        elif tag == "img":
            self.wynik.append(f'<img src="{html.escape(a.get("src", ""))}" alt="{html.escape(a.get("alt", ""))}" loading="lazy">')
        elif tag == "h2":
            nr = len(self.naglowki) + 1
            self.w_naglowku = []
            self.naglowki.append((f"czesc-{nr}", self.w_naglowku))
            self.wynik.append(f'<h2 id="czesc-{nr}">')
        else:
            self.wynik.append(f"<{'strong' if tag == 'b' else 'em' if tag == 'i' else tag}>")

    def handle_endtag(self, tag):
        if tag not in DOZWOLONE or tag in PUSTE:
            return
        if tag == "h2":
            self.w_naglowku = None
        self.wynik.append(f"</{'strong' if tag == 'b' else 'em' if tag == 'i' else tag}>")

    def handle_data(self, data):
        if self.w_naglowku is not None:
            self.w_naglowku.append(data)
        self.wynik.append(html.escape(data, quote=False))


def odkoduj_email(hex_):
    """Cloudflare zapisuje adresy e-mail jako hex z kluczem XOR w pierwszym bajcie."""
    b = bytes.fromhex(hex_)
    return bytes(x ^ b[0] for x in b[1:]).decode("utf-8")


def odkoduj_emaile(tekst):
    tekst = re.sub(r'<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="([0-9a-f]+)">.*?</a>',
                   lambda m: f'<a href="mailto:{odkoduj_email(m.group(1))}">{odkoduj_email(m.group(1))}</a>',
                   tekst, flags=re.S)
    tekst = re.sub(r'<span class="__cf_email__" data-cfemail="([0-9a-f]+)">.*?</span>',
                   lambda m: odkoduj_email(m.group(1)), tekst, flags=re.S)
    return re.sub(r'href="/cdn-cgi/l/email-protection#([0-9a-f]+)"',
                  lambda m: f'href="mailto:{odkoduj_email(m.group(1))}"', tekst)


def tresc_artykulu(strona):
    strona = odkoduj_emaile(strona)
    artykul = re.search(r'<article class="article">(.*?)</article>', strona, re.S).group(1)
    tytul = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", artykul, re.S).group(1))).strip()
    bloki = re.findall(r'<div class="paragraph paragraph--type--content[^"]*">(.*?)\n\s*</div>', artykul, re.S)
    c = Czysciciel()
    c.feed("\n".join(bloki))
    tekst = "".join(c.wynik)
    # Puste elementy z edytora (sama spacja albo <br>) i <br> na brzegach bloków. Tekst się nie zmienia.
    tekst = re.sub(r"<(p|h2|h3|h4|li)( [^>]*)?>(\s|\xa0|<br>)*</\1>", "", tekst)
    tekst = re.sub(r"(<(?:p|h2|h3|h4|li)(?: [^>]*)?>)(\s|<br>)+", r"\1", tekst)
    tekst = re.sub(r"(\s|<br>)+(</(?:p|h2|h3|h4|li)>)", r"\2", tekst)
    tekst = re.sub(r"\n\s*\n+", "\n", tekst).strip()
    return tytul, tekst, [(i, re.sub(r"\s+", " ", "".join(t)).strip()) for i, t in c.naglowki]


def popraw(slug, tytul, tekst):
    for stary, nowy, _ in POPRAWKI.get(slug, []):
        if stary not in tytul and stary not in tekst:
            raise SystemExit(f"{slug}: nie znaleziono tekstu do poprawy: {stary[:60]}")
        tytul, tekst = tytul.replace(stary, nowy), tekst.replace(stary, nowy)
    return tytul, tekst


ADRES = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+|(?:https?://)?(?:www\.)?[\w-]+(?:\.[\w-]+)*\.(?:pl|com|org|eu|net)(?:/[^\s<]*)?")


def bez_lamania(tekst):
    """Adresy stron i e-maile zawsze w jednej linii (Ada 2026-10-21). Zmienia tylko tekst poza znacznikami."""
    czesci = re.split(r"(<[^>]+>)", tekst)
    return "".join(c if c.startswith("<") else ADRES.sub(lambda m: f'<span class="adres">{m.group(0)}</span>', c)
                   for c in czesci)


def zapisz(slug, sciezka):
    tytul, tekst, naglowki = tresc_artykulu(pobierz(PROD + sciezka))
    tytul, tekst = popraw(slug, tytul, tekst)
    tekst = bez_lamania(tekst)
    oryginal = f'<a href="{PROD}{sciezka}" target="_blank" rel="noopener"><span class="adres">nasz-bocian.pl</span></a>'
    if slug in POPRAWKI:
        zrodlo = (f"Tekst przeniesiony ze strony {oryginal}, z poprawionymi błędami "
                  '(<a href="https://github.com/adrwis/nasz-bocian-makiety/blob/main/dokumenty/poprawki-tekstow.md">lista poprawek</a>).')
    else:
        zrodlo = f"Tekst przeniesiony bez zmian ze strony {oryginal}."
    spis = ""
    if len(naglowki) >= 3:
        pozycje = "\n".join(f'          <li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in naglowki)
        spis = f"""      <nav class="spis" aria-label="Na tej stronie">
        <p class="spis__tytul">Na tej stronie</p>
        <ol>
{pozycje}
        </ol>
      </nav>
"""
    strona = f"""<!-- tytul: {tytul} -->
<main class="tresc tresc--dokument" id="tresc">
  <div class="wnetrze">
    <h1{' class="h1--dlugi"' if len(tytul) > 60 else ''}>{bez_lamania(html.escape(tytul))}</h1>
    <article class="dokument dokument--tekst">
{spis}      <div class="dokument__tresc">
{tekst}
      </div>
      <p class="dokument__zrodlo">{zrodlo}</p>
    </article>
  </div>
</main>
"""
    (ROOT / "strony" / f"{slug}.html").write_text(strona, encoding="utf-8")
    print(f"{slug}: {tytul} ({len(re.sub(r'<[^>]+>', '', tekst))} znaków, spis: {len(naglowki) >= 3})")


def lista_dla_redaktora():
    wiersze = []
    for slug, poprawki in POPRAWKI.items():
        for stary, nowy, opis in poprawki:
            wiersze.append(f"| [{slug}]({PROD}{DOKUMENTY[slug]}) | {stary} | {nowy} | {opis} |")
    tresc = f"""# Poprawki tekstów na nasz-bocian.pl

Błędy znalezione w tekstach stron ze stopki. W makiecie są już poprawione. Na produkcji trzeba je
zmienić w panelu: otworzyć stronę, „Edytuj”, znaleźć stary tekst (Ctrl+F), wpisać nowy, zapisać.

| Strona | Jest | Ma być | Dlaczego |
|---|---|---|---|
""" + "\n".join(wiersze) + """

Polityka prywatności („Zasady korzystania z serwisu”) wymaga napisania od nowa, nie poprawki. Opis w ZMIANY.md.
"""
    (ROOT / "dokumenty" / "poprawki-tekstow.md").write_text(tresc, encoding="utf-8")


if __name__ == "__main__":
    for slug, sciezka in DOKUMENTY.items():
        zapisz(slug, sciezka)
    lista_dla_redaktora()
