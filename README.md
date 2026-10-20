# Makiety nasz-bocian.pl

Robocze propozycje zmian na stronie Stowarzyszenia Nasz Bocian, do akceptacji przez Stowarzyszenie. Podgląd: https://adrwis.github.io/nasz-bocian-makiety/

Każda makieta to folder nazwany jak adres strony (np. `jak-mozemy-ci-pomoc/`):

- `tresc.html`: nowa zawartość `<main>`, w strukturze HTML Drupala z produkcji,
- `index.html`: gotowa makieta, zbudowana skryptem (nie edytować ręcznie),
- `poprawki.css`: zmiany CSS do przeniesienia do motywu,
- `dla-redaktora.md`: co wpisać w panelu Drupala.

Budowanie: `python3 narzedzia/zbuduj.py <folder>`. Skrypt pobiera stronę z produkcji, usuwa analitykę i baner cookies, podmienia `<main>` na `tresc.html` i dokleja pasek „Makieta robocza”. Style, czcionki i obrazy ładują się z nasz-bocian.pl.
