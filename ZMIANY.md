# Makiety Nasz Bocian: śledzenie zmian

Co zrobiłyśmy, co jest w toku i co dalej. Najnowsze na górze. Statusy: **zrobione**, **w toku**, **do zrobienia**, **do decyzji**.

## Zasady makiety (od 2026-10-20)

- Makieta pokazuje tylko nasze zmiany. Oryginalnej treści strony jeszcze w niej nie ma.
- Klikalne są tylko 3 kafelki, logo i numery kryzysowe. Reszta (menu, wyszukiwarka, stopka) jest widoczna, ale wyłączona.
- Strona główna makiety to strona z 3 kafelkami („Jak możemy Ci pomóc?”).

## 2026-10-20, uwagi Ady do pierwszej wersji

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 1 | Kliknięcie w bociana w lewym górnym rogu zawsze wraca na stronę główną z 3 kafelkami. | Logo prowadzi do strony głównej makiety z każdej podstrony. | zrobione |
| 2 | Menu na górze zostaje i podkreśla się na pomarańczowo, ale bez rozwijanej listy po najechaniu. | Bez podmenu. Po najechaniu pomarańczowy pasek pod pozycją (6 px, jak na obecnej stronie). Pozycje nieklikalne. Na telefonie menu pod hamburgerem, pasek z lewej. | zrobione |
| 3 | „Wyszukaj” wygląda źle. Ma być polem pod menu, po prawej, pod „Szkolenia” i „O nas”. | Zaokrąglone pole „Czego szukasz?” z lupą pod menu, po prawej. Na telefonie na całą szerokość pod logo. Na razie nie wyszukuje. | zrobione |
| 4 | Kafelki są nieczytelne i za pstrokate. Inne obrazy, czytelny tekst, bez linku (podpisu autora zdjęcia) w prawym dolnym rogu. | Zamiast zdjęć ze stocku spokojne ilustracje liniowe na jasnym tle (zieleń, przy wsparciu pomarańcz). Tekst pod ilustracją na białym tle. Bez podpisów autorów, bo ilustracje są nasze. | zrobione, do oceny Ady |
| 5 | Stopka: żółtawy pomarańcz zamienić na pomarańcz z logo, ładniej poukładać, żeby nie wyglądała jak chaos. | Pas „Wesprzyj” w kolorze logo `#f36716`, ciemny tekst (biały drobny tekst byłby nieczytelny), białe przyciski. Pod spodem 4 wyrównane kolumny: Kontakt, Informacje, Zasady i polityki, Obserwuj nas. Na dole prawa autorskie i KRS, REGON, NIP. | zrobione |
| 6 | Wszystkie uwagi zapisywać w pliku do śledzenia zmian. | Ten plik. | zrobione |
| 7 | Makieta bez oryginalnych treści, klikalne tylko 3 kafelki, reszta wyłączona. | Własny nagłówek i stopka zamiast kopii z produkcji. Klikalne: 3 kafelki, logo i numery kryzysowe. Kafelki prowadzą do stron „w przygotowaniu”. | zrobione |

## 2026-10-20, pierwsza wersja

| Zmiana | Status |
|---|---|
| Strona „Jak możemy Ci pomóc?”: działające linki w kafelkach, krótsze opisy, przyciski z czasownikiem | zrobione |
| Kafle jako karty: tekst pod zdjęciem, na telefonie bez nachodzenia | zrobione |
| Blok „Potrzebujesz pomocy od razu?” z numerami 116 123, 800 70 2222, 112 | zrobione |
| Schowany pusty szary pasek okruszków | zrobione |
| Ciemniejsze przyciski zgodne z normą kontrastu | zrobione |
| Instrukcja dla redaktora (`dla-redaktora.md`) i CSS dla programisty (`poprawki.css`) | zrobione |

## Do zrobienia dalej

| Co | Status |
|---|---|
| Strona główna nasz-bocian.pl (pierwszy ekran z drogą do pomocy, baner refundacji niżej) | do zrobienia |
| Strony docelowe kafelków w makiecie (Szukam informacji, Linia pomocy, Kontakt) | do zrobienia |
| Doprecyzować `dokumenty/jak-mozemy-ci-pomoc/dla-redaktora.md` po screenach formularza edycji z dev | do zrobienia |
| Po akceptacji wyglądu przygotować CSS dla programisty pod nowy nagłówek, kafle i stopkę (obecny `poprawki.css` dotyczy pierwszej wersji) | do zrobienia |

## Do decyzji

| Pytanie | Kto |
|---|---|
| Jak zmiany z dev trafiają na produkcję, czy baza dev bywa nadpisywana | admin |
| Czy na Linii rozmawiają osoby z własnym doświadczeniem leczenia | zarząd |
| Czy Stowarzyszenie podpowiada, gdzie szukać specjalisty | zarząd |
| Data kolejnej edycji grup wsparcia | zarząd |
