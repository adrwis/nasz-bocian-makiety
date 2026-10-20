# Makiety Nasz Bocian: śledzenie zmian

Co zrobiłyśmy, co jest w toku i co dalej. Najnowsze na górze. Statusy: **zrobione**, **w toku**, **do zrobienia**, **do decyzji**.

## Zasady makiety (od 2026-10-20)

- Makieta pokazuje tylko nasze zmiany. Oryginalnej treści strony jeszcze w niej nie ma.
- Klikalne: kafelki i pozycje menu (strony „w przygotowaniu”), logo, „Wyszukaj” (rozwija pole), numery kryzysowe, cała stopka (linki do nasz-bocian.pl, zbiórek i mediów społecznościowych). Reszta (menu, wyszukiwarka, stopka) jest widoczna, ale wyłączona.
- Strona główna makiety to strona z 3 kafelkami („Jak możemy Ci pomóc?”).

## 2026-10-20, uwagi Ady do trzeciej wersji

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 14 | Wyśrodkować „Obserwuj nas” razem z serwisami społecznościowymi. | Napis i przyciski na środku stopki. | zrobione |
| 15 | Usunąć pole wyszukiwania pod „Jak możemy Ci pomóc?”. „Wyszukaj” zostaje w prawym górnym rogu i ma się rozwijać. | Pole pod tytułem usunięte. Kliknięcie „Wyszukaj” rozwija pod nagłówkiem pasek z polem „Napisz, czego szukasz” i przykładami. Ikona zmienia się w krzyżyk, Esc zamyka. Na razie nie wyszukuje. | zrobione |
| 16 | Ładniej zrobić „Potrzebujesz pomocy od razu?” (z użyciem skilla frontend-design). | Ciepłe tło z delikatnym przejściem pomarańczu i zieleni, ikona serca, nagłówek na środku. Numery jako 3 duże karty z przyciskiem „Zadzwoń”, 112 wyróżnione pomarańczem. Na telefonie karty jedna pod drugą. Dopisane „połączenia są bezpłatne”. | zrobione |
| 17 | Wyśrodkować napis „Jak możemy Ci pomóc?”. | Tytuł i zdanie „Wybierz, czego teraz potrzebujesz.” na środku. | zrobione |
| 18 | Kliknięcie w pozycję menu (między logo a „Wyszukaj”) pokazuje stronę „w przygotowaniu”, jak po kliknięciu kafelka. | Każda pozycja menu prowadzi do strony „Tę stronę właśnie przygotowujemy” z przyciskiem powrotu, tak jak kafelki. Pozycja menu bieżącej strony ma pomarańczowe podkreślenie. | zrobione |
| 19 | W stopce Kontakt, Informacje, Zasady i polityki klikalne, prowadzą do stron z oryginalnej strony. | Linki prowadzą do stron na nasz-bocian.pl (w nowej karcie), telefony i e-mail klikalne. „Ustawienia cookies” prowadzi do zasad korzystania z serwisu, bo w makiecie nie ma banera cookies. | zrobione |

## 2026-10-20, uwagi Ady do drugiej wersji

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 8 | Cofnąć ilustracje. Kafelki mają wyglądać jak w pierwszej wersji. | Wróciły zdjęcia z obecnej strony, nad tekstem na białym tle, tytuły i przyciski wersalikami. Zdjęcia przycięte od dołu, żeby nie było widać podpisu autora. | zrobione |
| 9 | „Wyszukaj” w nagłówku jak wcześniej. | Szary blok z lupą i napisem „Wyszukaj” po prawej stronie menu, jak na obecnej stronie. Na stronie głównej przewija do pola wyszukiwania. | zrobione |
| 10 | Pole wyszukiwania pod pytaniem „Jak możemy Ci pomóc?”, z tekstem w stylu „Napisz, czego szukasz”. | Duże pole „Napisz, czego szukasz” z przyciskiem „Szukaj” zaraz pod tytułem, pod nim przykłady (in vitro, adopcja, AMH, grupa wsparcia), dalej „Albo wybierz, czego teraz potrzebujesz:” i kafelki. Na razie nie wyszukuje. | zrobione |
| 11 | Patronite, Siepomaga i FaniMani klikalne. | Prowadzą na prawdziwe strony zbiórek, otwierają się w nowej karcie. | zrobione |
| 12 | „Obserwuj nas” na dole poziomo: ikony i nazwy w jednym rzędzie, klikalne. | Osobny rząd pod kolumnami stopki, 6 przycisków z ikoną i nazwą, prowadzą na profile Stowarzyszenia. | zrobione |
| 13 | Osobny folder z brandingiem: kolory, logo, czcionki. | `psycho/nasz-bocian/branding/`: `BRANDING.md` (opis i zasady) i `tokeny.css` (wartości). Makieta kopiuje kolory z `tokeny.css` i logo z `logo/bocian_stopka.png` przy każdym budowaniu. Pomarańcz ujednolicony do `#F36717` (dokładny kolor z pliku logo). | zrobione |

## 2026-10-20, uwagi Ady do pierwszej wersji

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 1 | Kliknięcie w bociana w lewym górnym rogu zawsze wraca na stronę główną z 3 kafelkami. | Logo prowadzi do strony głównej makiety z każdej podstrony. | zrobione |
| 2 | Menu na górze zostaje i podkreśla się na pomarańczowo, ale bez rozwijanej listy po najechaniu. | Bez podmenu. Po najechaniu pomarańczowy pasek pod pozycją (6 px, jak na obecnej stronie). Pozycje nieklikalne. Na telefonie menu pod hamburgerem, pasek z lewej. | zrobione |
| 3 | „Wyszukaj” wygląda źle. Ma być polem pod menu, po prawej, pod „Szkolenia” i „O nas”. | Zaokrąglone pole „Czego szukasz?” z lupą pod menu, po prawej. | zastąpione (uwagi 9 i 10) |
| 4 | Kafelki są nieczytelne i za pstrokate. Inne obrazy, czytelny tekst, bez linku (podpisu autora zdjęcia) w prawym dolnym rogu. | Zamiast zdjęć ze stocku spokojne ilustracje liniowe na jasnym tle (zieleń, przy wsparciu pomarańcz). Tekst pod ilustracją na białym tle. Bez podpisów autorów, bo ilustracje są nasze. | cofnięte (uwaga 8) |
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
| Potwierdzić, że połączenia z 116 123 i 800 70 2222 są bezpłatne (tekst w bloku „Potrzebujesz pomocy od razu?”), przed wdrożeniem na produkcję | Ada |
| Zdjęcia w kafelkach są z Freepika (podpis na zdjęciu: „zdjęcie utworzone przez … freepik.com”). Darmowa licencja Freepika wymaga podania autora. Skoro chowamy podpis na zdjęciu, na produkcji trzeba dać podpis gdzie indziej (np. „Zdjęcia: Freepik” w stopce), wykupić licencję albo wymienić zdjęcia. | Ada, zarząd |
