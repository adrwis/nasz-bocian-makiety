# Makiety Nasz Bocian: śledzenie zmian

Co zrobiłyśmy, co jest w toku i co dalej. Najnowsze na górze. Statusy: **zrobione**, **w toku**, **do zrobienia**, **do decyzji**.

## Zasady makiety (od 2026-10-20)

- Makieta pokazuje tylko nasze zmiany. Oryginalnej treści strony jeszcze w niej nie ma.
- Klikalne: kafelki i pozycje menu (strony „w przygotowaniu”), logo, „Wyszukaj” (rozwija pole), numery kryzysowe, cała stopka (linki do nasz-bocian.pl, zbiórek i mediów społecznościowych). Reszta (menu, wyszukiwarka, stopka) jest widoczna, ale wyłączona.
- Strona główna makiety to strona z 3 kafelkami („Jak możemy Ci pomóc?”).
- Najechanie na klikalne słowa: tekst robi się pomarańczowy `#F36717`, bez podkreślenia. Tak na wszystkich stronach, także nowych (szczegóły w `branding/BRANDING.md`, sekcja „Interakcje”).

## 2026-10-21, najechanie myszką

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 35 | Wybór zdjęć: ID i WA. Dla „eksperta” zdjęcie bez widocznych twarzy, dla „Szukam informacji” jeszcze opcje z osobą tyłem przy komputerze. | ID i WA na stronie głównej, zapisane w makiecie (`assets/zdjecia/`), źródła w `dokumenty/zdjecia.md`. Zdjęcia CC0 kadrowane na środku. Druga runda propozycji na `/propozycje-zdjec/`: IE do IH (tyłem przy komputerze, dłonie na laptopie) i EE do EH (rozmowa przy stole, widać tylko dłonie). | do wyboru Ady |
| 33 | Znaleźć zdjęcia stockowe, które nie wymagają licencji ani podpisu autora. | Unsplash, Pexels i Pixabay blokują automatyczne wyszukiwanie, więc szukane przez Openverse (wyszukiwarka z filtrem licencji), tylko CC0 ze StockSnap i rawpixel. Bez zdjęć z dziećmi i ciążą. Po 4 propozycje na każdy kafelek na stronie `/propozycje-zdjec/`, pokazane w prawdziwych kafelkach. | zrobione, wybór w uwadze 35 |
| 32 | Adresy stron (np. www.nasz-bocian.pl w Nocie prawnej) zawsze w jednej linii. | Adresy stron i e-maile w dokumentach i tytułach nie łamią się ani nie dzielą (skrypt oznacza je automatycznie, 32 miejsca). Dopisek na dole skrócony do „Tekst przeniesiony bez zmian ze strony nasz-bocian.pl”, bo pełna ścieżka nie mieściła się w jednej linii. Zasada w `branding/BRANDING.md`. | zrobione |
| 31 | Wyjustować teksty na stronach ze stopki (teraz poszarpany prawy brzeg). | Akapity i punkty list w dokumentach wyjustowane, z automatycznym dzieleniem wyrazów, żeby nie robiły się duże odstępy między słowami. Nagłówki i spis treści bez zmian. Na telefonie podpunkty list wyrównane do lewej (w wąskiej kolumnie justowanie robiło duże dziury). | zrobione |
| 30 | Numery kryzysowe cofnąć: po najechaniu podkreślenie, jak wcześniej. | Przywrócone. Zapisane w brandingu jako wyjątek od zasady pomarańczowego tekstu. | zrobione |
| 29 | Pomarańczowe podświetlenie się podoba: wprowadzić na każdej stronie makiety i stosować na kolejnych. | Na wszystkich stronach: menu (także bieżąca strona, zamiast paska), „Wyszukaj”, stopka, media społecznościowe, linki i spis treści w dokumentach. Zasada zapisana w `branding/BRANDING.md` (sekcja „Interakcje”) i w zasadach makiety na górze tego pliku. | zrobione |
| 28 | Czarny tekst jest za mocny, zamienić na szary jak w „Wybierz, czego teraz potrzebujesz”. | Podstawowy kolor tekstu w brandingu zmieniony z `#292728` na `#5A5A5A` (cała makieta: nagłówki, akapity, menu, stopka). Na pomarańczowym pasie „Wesprzyj” tekst zostaje ciemny, bo szary byłby tam nieczytelny. | zrobione |
| 27 | Na stronie głównej nadal widać podkreślenie zamiast zmiany koloru. | Zmiana była już na serwerze, ale GitHub Pages pozwala przeglądarce trzymać stare style przez 10 minut. Do adresów stylów i skryptu doszedł numer wersji, więc każda zmiana jest widoczna od razu. | zrobione |
| 26 | Zamiast pomarańczowego podkreślenia po najechaniu na klikalne słowa: zmiana koloru tekstu na pomarańczowy. Na razie w menu i stopce strony głównej; jeśli się spodoba, na pozostałych stronach. | Tylko strona główna (klasa `strona-glowna`): pozycje menu, „Wyszukaj”, linki w kolumnach stopki i przyciski mediów społecznościowych po najechaniu robią się pomarańczowe (`#F36717`), bez podkreślenia i bez paska pod menu. Telefony i e-mail w Kontakcie zachowują stałe podkreślenie (to oznaczenie linku, nie efekt najechania). Pozycja menu bieżącej strony na innych stronach nadal ma pasek. | zaakceptowane, rozszerzone (uwaga 29) |

## 2026-10-21, poprawki tekstów

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 25 | Poprawić wypisane błędy w tekstach. | Poprawki wpisane do skryptu `narzedzia/dokumenty.py` (lista POPRAWKI), więc nie znikną przy ponownym pobraniu tekstów. Skrypt tworzy `dokumenty/poprawki-tekstow.md` z tabelą „jest / ma być” dla redaktora. Na dole poprawionych stron dopisek z linkiem do listy poprawek. Polityki prywatności nie da się poprawić drobną zmianą, patrz „Błędy w oryginalnych tekstach”. | zrobione |

## 2026-10-21, strony ze stopki

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 23 | Kliknięcie np. „Ustawienia cookies” ma otwierać stronę w nowej makiecie (wygląd nowej strony głównej), a w środku tekst z oryginalnych cookies. Estetycznie, z frontend-design. | Nowa strona `/ustawienia-cookies/`. Tekst 1:1 z banera cookies na nasz-bocian.pl (wstęp, 5 kategorii z opisami, przyciski, zdanie o 365 dniach). Kategorie w płaskim panelu z przełącznikami, „Niezbędne” oznaczone „Zawsze włączone”. Trzy przyciski decyzji o równej wadze (na obecnej stronie „Odrzuć” to szary tekst, co lipcowy audyt wskazał jako ryzyko prawne). W makiecie wybór nie jest zapisywany, strona tylko to potwierdza. „Polityka prywatności” prowadzi na nasz-bocian.pl. | zrobione |
| 24 | Pozostałe klikalne strony ze stopki zrobić tak samo. | 7 nowych stron: `/ogloszenia-nieodplatne/`, `/reklamy/`, `/nota-prawna/`, `/zasady-korzystania-z-serwisu/`, `/regulamin-platnosci/`, `/wspolpraca-z-biznesem/`, `/wspolpraca-z-partiami-politycznymi/`. Tekst słowo w słowo z nasz-bocian.pl (sprawdzone automatycznie), wygląd nowej makiety: kolumna do czytania, nagłówki sekcji z linią, numery list w kolorze marki. Długie dokumenty mają spis treści „Na tej stronie”. Usunięte tylko puste elementy z edytora. Adresy e-mail, które Cloudflare szyfruje, są zapisane jawnie i klikalne. Na dole każdej strony link do oryginału. Linki między tymi stronami (np. „Polityka prywatności” z cookies) prowadzą w obrębie makiety. Skrypt: `narzedzia/dokumenty.py`. Newsletter nadal otwiera formularz MailerLite. | zrobione |

## 2026-10-21, uwagi Ady do czwartej wersji

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 20 | Przyciski na kafelkach są w złych kolorach. | Kolory marki: zieleń `#1BA574` (praktycznie `#1EAA78` ze strony) i pomarańcz z logo `#F36717`, biały napis 19 px pogrubiony. Przy tej wielkości napis spełnia normę kontrastu dla dużego tekstu. Wcześniejsze ciemniejsze odcienie (`#12805A`, `#C2490A`) zostają tylko do małych elementów. Zapisane w `branding/BRANDING.md`. | zrobione |
| 21 | „Potrzebujesz pomocy od razu?” jest za okrągła, nie wygląda poważnie, za duża (zmniejszyć o połowę). | Płaski panel z małym zaokrągleniem (4 px), bez gradientu i ikony. Tekst po lewej, 3 numery w rzędzie po prawej, oddzielone liniami. Wysokość z ok. 480 px do ok. 140 px. Na telefonie numery jeden pod drugim, numer z opisem w jednej linii. | zrobione |
| 22 | W stopce Informacje oraz Zasady i polityki: tekst bez zmian, estetyka jak na obecnej stronie. | Typografia i odstępy ze stopki nasz-bocian.pl: małe nagłówki wersalikami, zwarte listy, telefony i e-mail podkreślone na pomarańczowo, linki podkreślają się po najechaniu. Kolory z brandingu zamiast śliwkowego. Tekst 14 px (na produkcji 12,5 px, za mały do wygodnego czytania). | zrobione |

## 2026-10-20, uwagi Ady do trzeciej wersji

| # | Uwaga Ady | Co robimy | Status |
|---|---|---|---|
| 14 | Wyśrodkować „Obserwuj nas” razem z serwisami społecznościowymi. | Napis i przyciski na środku stopki. | zrobione |
| 15 | Usunąć pole wyszukiwania pod „Jak możemy Ci pomóc?”. „Wyszukaj” zostaje w prawym górnym rogu i ma się rozwijać. | Pole pod tytułem usunięte. Kliknięcie „Wyszukaj” rozwija pod nagłówkiem pasek z polem „Napisz, czego szukasz” i przykładami. Ikona zmienia się w krzyżyk, Esc zamyka. Na razie nie wyszukuje. | zrobione |
| 16 | Ładniej zrobić „Potrzebujesz pomocy od razu?” (z użyciem skilla frontend-design). | Ciepłe tło z gradientem, ikona serca, duże karty z numerami. | zastąpione (uwaga 21) |
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

## Błędy w oryginalnych tekstach

W makiecie poprawione 2026-10-21 (uwaga 25). Na nasz-bocian.pl trzeba je poprawić w panelu: gotowa lista „jest / ma być” w `dokumenty/poprawki-tekstow.md`.

| Strona | Problem | Status |
|---|---|---|
| Zasady korzystania z serwisu | To jedyna „Polityka prywatności” na stronie (link z banera cookies), a opisuje głównie forum, którego już nie ma (przekierowuje na stronę główną). „Ostatnia aktualizacja: 25.05.2018.” Nie opisuje Google Analytics, Meta Pixel, MailerLite ani FaniMani, o których mówi baner cookies. | do decyzji: nowa polityka prywatności, z prawnikiem |
| Ogłoszenia nieodpłatne, Współpraca z biznesem, Współpraca z partiami | „odpisów 1% podatku”: od 2023 roku jest 1,5%. | poprawione w makiecie |
| Regulamin wpłat FaniPay | „W przypadku wystąpienia konieczność zwrotu… przyjmujący wpłatę dokonana zwrotu”: zmienione na „konieczności”, „dokona”. | poprawione w makiecie |
| Reklamy | Literówka „artkuł sponsorowany”. Tytuł w całości wersalikami, zmieniony na zwykłą pisownię jak w pozostałych dokumentach. | poprawione w makiecie |

## Do decyzji

| Pytanie | Kto |
|---|---|
| Jak zmiany z dev trafiają na produkcję, czy baza dev bywa nadpisywana | admin |
| Czy na Linii rozmawiają osoby z własnym doświadczeniem leczenia | zarząd |
| Czy Stowarzyszenie podpowiada, gdzie szukać specjalisty | zarząd |
| Data kolejnej edycji grup wsparcia | zarząd |
| Potwierdzić, że połączenia z 116 123 i 800 70 2222 są bezpłatne (tekst w bloku „Potrzebujesz pomocy od razu?”), przed wdrożeniem na produkcję | Ada |
| Zdjęcia w kafelkach są z Freepika (podpis na zdjęciu: „zdjęcie utworzone przez … freepik.com”). Darmowa licencja Freepika wymaga podania autora. Skoro chowamy podpis na zdjęciu, na produkcji trzeba dać podpis gdzie indziej (np. „Zdjęcia: Freepik” w stopce), wykupić licencję albo wymienić zdjęcia. | Ada, zarząd |
