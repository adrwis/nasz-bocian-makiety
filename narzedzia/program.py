"""Strona „Rządowy program refundacji in vitro” w stylu makiety.

Pobiera https://nasz-bocian.pl/rzadowy-program-refundacji-vitro i przenosi treść bez zmian:
najważniejsze fakty, ścieżki „Od czego zaczynasz?”, wszystkie pytania i odpowiedzi,
dokumenty, artykuły i nagrania. Zmienia się tylko wygląd: bez emoji, artykuły w jednej liście
(w oryginale te same artykuły są jako kafelki i jeszcze raz na liście).

Użycie: python3 narzedzia/program.py, potem python3 narzedzia/zbuduj.py
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dokumenty import PROD, Czysciciel, bez_lamania, odkoduj_emaile, pobierz  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SCIEZKA = "/rzadowy-program-refundacji-vitro"


def tekst(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


def czysc(fragment):
    c = Czysciciel()
    c.feed(fragment)
    wynik = "".join(c.wynik)
    wynik = re.sub(r"<(p|li)>(\s|\xa0|<br>)*</\1>", "", wynik)
    return bez_lamania(wynik.strip())


def wytnij(b, od, do):
    i = b.index(od)
    return b[i:b.index(do, i)]


def zbuduj():
    s = odkoduj_emaile(pobierz(PROD + SCIEZKA))
    b = re.search(r"<main.*?</main>", s, re.S).group(0)

    tytul = tekst(re.search(r"<h1>(.*?)</h1>", b, re.S).group(1))
    nadtytul = tekst(re.search(r'<p class="nb-hero-eyebrow">(.*?)</p>', b, re.S).group(1))
    lead = tekst(re.search(r'<p class="hero-lead">(.*?)</p>', b, re.S).group(1))
    meta = tekst(re.search(r'<p class="nb-hero-meta">(.*?)</p>', b, re.S).group(1))
    lista_klinik = re.search(r'<a class="cta-button secondary" href="([^"]+)">(.*?)</a>', b, re.S)

    fakty = re.findall(r'<p class="nb-fact"><strong>(.*?)</strong>(.*?)</p>', b, re.S)

    sciezki_html = wytnij(b, 'id="sciezki"' if 'id="sciezki"' in b else "Od czego zaczynasz?", "Pytania i odpowiedzi</h2>")
    sciezki_wstep = tekst(re.search(r"</h2>\s*<p[^>]*>(.*?)</p>", sciezki_html, re.S).group(1))
    sciezki = re.findall(
        r'<a class="nb-path-tile" href="([^"]+)"><span class="nb-path-emoji">.*?</span>'
        r'<span class="nb-path-num">(.*?)</span><span class="nb-path-title">(.*?)</span>'
        r'<span class="nb-path-ask">(.*?)</span><span class="nb-path-meta">(.*?)</span></a>', sciezki_html, re.S)

    faq_html = wytnij(b, "Pytania i odpowiedzi</h2>", "Dokumenty do pobrania")
    faq_wstep = czysc(re.search(r"<p[^>]*>(Pytania zadawali.*?)</p>", faq_html, re.S).group(1))
    tematy = []
    for kawalek in faq_html.split('<div class="faq-section')[1:]:
        tid = re.search(r'id="([^"]+)"', kawalek).group(1)
        nazwa = tekst(re.search(r"<h3>(.*?)</h3>", kawalek, re.S).group(1))
        pytania = []
        for pid, pyt, odp in re.findall(
                r'<details class="faq-item" id="([^"]+)"><summary class="faq-question">(.*?)</summary>'
                r'<div class="faq-answer">(.*?)</div></details>', kawalek, re.S):
            podobne = []
            m = re.search(r'<p class="nb-faq-alias-label">(.*?)</p><ul class="nb-faq-alias">(.*?)</ul>', odp, re.S)
            if m:
                podobne = [tekst(x) for x in re.findall(r"<li[^>]*>(.*?)</li>", m.group(2), re.S)]
                etykieta = tekst(m.group(1))
                odp = odp[:m.start()]
            pytania.append((pid, tekst(pyt), czysc(odp), podobne, etykieta if podobne else ""))
        tematy.append((tid, nazwa, pytania))

    dok_html = wytnij(b, "Dokumenty do pobrania", "Przeczytaj więcej")
    dokumenty = []
    for href, nazwa in re.findall(r'<p>\s*<a href="([^"]+)">\s*(.*?)\s*</a>\s*</p>', dok_html, re.S):
        dokumenty.append((PROD + href if href.startswith("/") else href, tekst(nazwa)))

    art_html = wytnij(b, "Przeczytaj więcej", "Webinary i podcasty")
    artykuly = []
    for href, nazwa, data in re.findall(r'<li[^>]*><a href="([^"]+)">(.*?)</a> <span class="nb-rp-date">(.*?)</span></li>', art_html, re.S):
        artykuly.append((PROD + href if href.startswith("/") else href, tekst(nazwa), tekst(data)))

    vid_html = b[b.index("Webinary i podcasty"):]
    nagrania = re.findall(r'<li[^>]*><a href="([^"]+)" target="_blank" rel="noopener">(.*?)</a> <span class="nb-rp-date">(.*?)</span></li>', vid_html, re.S)

    liczba = sum(len(p) for _, _, p in tematy)
    e = html.escape
    out = [f"<!-- tytul: {tytul} -->", '<main class="tresc tresc--program" id="tresc">', '  <div class="wnetrze">']
    out.append(f'''    <header class="program__naglowek">
      <p class="program__nadtytul">{e(nadtytul)}</p>
      <h1>{e(tytul)}</h1>
      <p class="wstep">{e(lead)}</p>
      <div class="program__cta">
        <a class="przycisk" href="#pytania">Znajdź odpowiedź</a>
        <a class="przycisk przycisk--obrys" href="{e(PROD + lista_klinik.group(1))}" target="_blank" rel="noopener">{e(tekst(lista_klinik.group(2)))}</a>
      </div>
      <p class="program__meta">{e(meta)}</p>
    </header>''')

    out.append('    <section class="program__sekcja" id="o-programie">\n      <h2>Najważniejsze o programie</h2>\n      <div class="fakty">')
    for naglowek, opis in fakty:
        out.append(f'        <div class="fakt"><h3>{e(tekst(naglowek))}</h3><p>{e(tekst(opis))}</p></div>')
    out.append("      </div>\n    </section>")

    out.append(f'    <section class="program__sekcja" id="od-czego-zaczac">\n      <h2>Od czego zaczynasz?</h2>\n      <p class="program__opis">{e(sciezki_wstep)}</p>\n      <div class="sciezki">')
    for href, etap, nazwa, opis, ile in sciezki:
        out.append(f'        <a class="sciezka" href="{e(href)}"><span class="sciezka__etap">{e(tekst(etap))}</span>'
                   f'<span class="sciezka__tytul">{e(tekst(nazwa))}</span><span class="sciezka__opis">{e(tekst(opis))}</span>'
                   f'<span class="sciezka__liczba">{e(tekst(ile))}</span></a>')
    out.append("      </div>\n    </section>")

    out.append(f'''    <section class="program__sekcja" id="pytania">
      <h2>Pytania i odpowiedzi</h2>
      <p class="program__opis">{faq_wstep}</p>
      <div class="faq-szukaj" role="search">
        <label class="szukaj__etykieta" for="faq-pole">Szukaj w pytaniach</label>
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg>
        <input id="faq-pole" type="search" placeholder="Wpisz, czego szukasz, np. wiek, leki, transfer" autocomplete="off">
      </div>
      <p class="faq-licznik" id="faq-licznik" aria-live="polite">{liczba} pytań w {len(tematy)} tematach</p>
      <nav class="tematy" aria-label="Tematy pytań">''')
    for tid, nazwa, pytania in tematy:
        out.append(f'        <a href="#{tid}">{e(nazwa)} <span>{len(pytania)}</span></a>')
    out.append("      </nav>")
    for tid, nazwa, pytania in tematy:
        out.append(f'      <div class="temat" id="{tid}">\n        <h3>{e(nazwa)}</h3>')
        for pid, pyt, odp, podobne, etykieta in pytania:
            alias = ""
            if podobne:
                alias = (f'<p class="faq-podobne__tytul">{e(etykieta)}</p><ul class="faq-podobne">'
                         + "".join(f"<li>{e(x)}</li>" for x in podobne) + "</ul>")
            out.append(f'        <details class="faq" id="{pid}"><summary>{e(pyt)}</summary><div class="faq__odpowiedz">{odp}{alias}</div></details>')
        out.append("      </div>")
    out.append('      <p class="faq-brak" id="faq-brak" hidden>Nie znaleźliśmy takiego pytania. Spróbuj innego słowa albo <a href="{{root}}linia-pomocy/">napisz do nas</a>.</p>')
    out.append("    </section>")

    out.append('    <section class="program__sekcja" id="dokumenty">\n      <h2>Dokumenty do pobrania</h2>\n      <ul class="pliki">')
    for href, nazwa in dokumenty:
        out.append(f'        <li><a href="{e(href)}" target="_blank" rel="noopener"><span class="pliki__typ">PDF</span>{e(nazwa)}</a></li>')
    out.append("      </ul>\n    </section>")

    out.append('    <section class="program__sekcja" id="artykuly">\n      <h2>Przeczytaj więcej</h2>\n      <ul class="lista-dat">')
    for href, nazwa, data in artykuly:
        out.append(f'        <li><a href="{e(href)}" target="_blank" rel="noopener">{e(nazwa)}</a><span>{e(data)}</span></li>')
    out.append("      </ul>\n    </section>")

    out.append('    <section class="program__sekcja" id="nagrania">\n      <h2>Webinary i podcasty</h2>\n      <ul class="lista-dat">')
    for href, nazwa, data in nagrania:
        out.append(f'        <li><a href="{e(href)}" target="_blank" rel="noopener">{e(tekst(nazwa))}</a><span>{e(tekst(data))}</span></li>')
    out.append("      </ul>\n    </section>")

    out.append(f'    <p class="dokument__zrodlo">Treść przeniesiona bez zmian ze strony <a href="{PROD}{SCIEZKA}" target="_blank" rel="noopener"><span class="adres">nasz-bocian.pl</span></a>.</p>')
    out.append("  </div>\n</main>\n")
    (ROOT / "strony" / "program-in-vitro.html").write_text("\n".join(out), encoding="utf-8")
    print(f"{tytul}: {len(fakty)} faktów, {len(sciezki)} ścieżek, {liczba} pytań w {len(tematy)} tematach, "
          f"{len(dokumenty)} dokumentów, {len(artykuly)} artykułów, {len(nagrania)} nagrań")


if __name__ == "__main__":
    zbuduj()
