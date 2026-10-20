# „Jak możemy Ci pomóc?”: co zmienić w panelu

Strona: `/jak-mozemy-ci-pomoc` (w Drupalu `node/11935`).
Podgląd docelowego wyglądu: [makieta](https://adrwis.github.io/nasz-bocian-makiety/).

Instrukcja jest wstępna. Dokładne nazwy pól uzupełnimy po obejrzeniu formularza edycji na wersji testowej.

## Najpierw: wersja testowa

1. Zaloguj się na https://dev.nasz-bocian.pl i otwórz `/jak-mozemy-ci-pomoc`.
2. Kliknij „Edytuj”.
3. Zanim cokolwiek zmienisz, zrób zrzut całego formularza (na wypadek, gdyby trzeba było wrócić do starej wersji).

## Kafle (3 elementy na stronie)

Każdy kafel ma: zdjęcie, tytuł, opis, link i przycisk. Zdjęcia i tytuły zostają bez zmian.

| Kafel | Opis (wklej w całości) | Link | Tekst przycisku |
|---|---|---|---|
| Szukam informacji | Artykuły o niepłodności, adopcji, rodzinie zastępczej i zachowaniu płodności. | `/szukam-informacji` (bez zmian) | Przeglądaj tematy |
| Potrzebuję wsparcia | Porozmawiaj z wolontariuszem Linii pomocy „Pacjent dla pacjenta”. Poniedziałek, środa i piątek, 20:00 do 22:00. | `/nasze-projekty/linia-pomocy-pacjent-dla-pacjenta` (było `/node/12032`, strona nie istnieje) | Zadzwoń lub napisz |
| Chcę porozmawiać z ekspertem | Napisz albo zadzwoń do Stowarzyszenia. Podpowiemy, gdzie szukać pomocy specjalisty. | `/o-nas/kontakt` (było forum, które już nie działa) | Skontaktuj się |

Jeśli w formularzu nie ma pola na tekst przycisku, zostaw „Dowiedz się więcej”. Zmianę napisu dopisze programista w szablonie.

## Zdanie pod tytułem

Jeśli strona ma pole na tekst (np. „Treść” albo „Wstęp”), wpisz:

> Wybierz, czego teraz potrzebujesz.

## Blok „Potrzebujesz pomocy od razu?”

Pod kaflami, jako osobny element tekstowy (np. akapit typu „Tekst”). Jeśli edytor ma przycisk „Źródło”, wklej kod poniżej. Wtedy blok dostanie wygląd z makiety.

```html
<div class="pomoc-teraz">
  <h2>Potrzebujesz pomocy od razu?</h2>
  <p>Jeśli jest Ci bardzo ciężko albo myślisz o zrobieniu sobie krzywdy, nie czekaj na godziny naszej Linii. Zadzwoń:</p>
  <ul>
    <li><a href="tel:116123">116 123</a> Kryzysowy Telefon Zaufania</li>
    <li><a href="tel:800702222">800 70 2222</a> Centrum Wsparcia dla osób w kryzysie psychicznym</li>
    <li><a href="tel:112">112</a> w sytuacji zagrożenia życia</li>
  </ul>
</div>
```

Bez przycisku „Źródło”: wpisz nagłówek, zdanie i trzy punkty listy zwykłym edytorem, a każdy numer zaznacz i dodaj link `tel:116123`, `tel:800702222`, `tel:112`. Będzie działać, tylko bez szarego tła.

## Zapisz i sprawdź

1. Zapisz stronę.
2. Sprawdź na telefonie: każdy kafel prowadzi tam, gdzie powinien, a numery w bloku dzwonią po dotknięciu.
3. Daj znać adminowi, że strona czeka na akceptację, i podeślij link do [poprawek CSS](poprawki.css).

## Czego nie zrobisz w panelu (zadanie dla programisty)

Plik [`poprawki.css`](poprawki.css):
- ukrywa pusty szary pasek okruszków nad tytułem,
- zmienia kafle w karty (zdjęcie na górze, tekst pod spodem), dzięki czemu tekst nie przecina twarzy, a na telefonie karty nie nachodzą na siebie,
- przyciemnia przyciski do normy kontrastu WCAG,
- nadaje wygląd zdaniu pod tytułem i blokowi z numerami.

## Do potwierdzenia z zarządem

- Czy na Linii rozmawiają osoby z własnym doświadczeniem leczenia? Jeśli tak, dopiszemy to w opisie kafla.
- Czy Stowarzyszenie podpowiada, gdzie szukać specjalisty? Jeśli nie, zmienimy opis trzeciego kafla.
