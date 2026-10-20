# Makiety nasz-bocian.pl

Robocze propozycje zmian na stronie Stowarzyszenia Nasz Bocian, do akceptacji przez Stowarzyszenie. Podgląd: https://adrwis.github.io/nasz-bocian-makiety/

Makieta pokazuje tylko proponowane zmiany. Klikalne są kafelki, logo i numery kryzysowe, reszta jest wyłączona. Historia uwag i stan prac: [ZMIANY.md](ZMIANY.md).

- `strony/`: treść każdej strony (`index.html` to strona główna makiety),
- `szablon/`: wspólny nagłówek i stopka,
- `assets/`: style i skrypt makiety,
- `dokumenty/`: instrukcje dla redaktora i CSS dla programisty,
- `narzedzia/dokumenty.py`: strony ze stopki z tekstem z nasz-bocian.pl (i listą poprawek),
- `narzedzia/program.py`: strona „Rządowy program refundacji in vitro” z treścią z nasz-bocian.pl,
- `narzedzia/zbuduj.py`: składa strony (`python3 narzedzia/zbuduj.py`). Gotowych plików `index.html` nie edytujemy ręcznie.
