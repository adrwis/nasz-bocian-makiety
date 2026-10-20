// Menu na telefonie, rozwijana wyszukiwarka (na razie nie wyszukuje).
document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.querySelector('.naglowek__hamburger');
  const menu = document.getElementById('menu-glowne');
  hamburger.addEventListener('click', () => {
    const otwarte = menu.classList.toggle('otwarte');
    hamburger.setAttribute('aria-expanded', String(otwarte));
  });

  const szukaj = document.querySelector('.naglowek__szukaj');
  const panel = document.getElementById('szukaj-panel');
  const pole = document.getElementById('szukaj-pole');
  const ustaw = (otwarte) => {
    panel.hidden = !otwarte;
    szukaj.setAttribute('aria-expanded', String(otwarte));
    if (otwarte) pole.focus();
  };
  szukaj.addEventListener('click', () => ustaw(panel.hidden));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !panel.hidden) { ustaw(false); szukaj.focus(); }
  });
  panel.querySelector('form').addEventListener('submit', (e) => e.preventDefault());
});

// Ustawienia cookies: w makiecie wybór nie jest nigdzie zapisywany, pokazujemy tylko potwierdzenie.
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('cookies');
  if (!form) return;
  const pola = form.querySelectorAll('input[type="checkbox"]');
  const komunikat = form.querySelector('.cookies__komunikat');
  const teksty = {
    odrzuc: 'Odrzucono pliki cookie poza niezbędnymi.',
    zapisz: 'Zapisano Twój wybór.',
    wszystkie: 'Zezwolono na wszystkie pliki cookie.',
  };
  const zakoncz = (akcja) => {
    komunikat.textContent = teksty[akcja] + ' (W makiecie wybór nie jest zapisywany.)';
  };
  form.addEventListener('submit', (e) => { e.preventDefault(); zakoncz('zapisz'); });
  form.querySelector('[data-akcja="odrzuc"]').addEventListener('click', () => {
    pola.forEach((p) => { p.checked = false; });
    zakoncz('odrzuc');
  });
  form.querySelector('[data-akcja="wszystkie"]').addEventListener('click', () => {
    pola.forEach((p) => { p.checked = true; });
    zakoncz('wszystkie');
  });
});

// Program in vitro: wyszukiwanie w pytaniach (bez polskich znaków i wielkości liter).
document.addEventListener('DOMContentLoaded', () => {
  const pole = document.getElementById('faq-pole');
  if (!pole) return;
  const norm = (t) => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ł/g, 'l');
  const pytania = [...document.querySelectorAll('.faq')].map((el) => ({ el, tekst: norm(el.textContent) }));
  const tematy = [...document.querySelectorAll('.temat')];
  const licznik = document.getElementById('faq-licznik');
  const brak = document.getElementById('faq-brak');
  const poczatkowy = licznik.textContent;
  const odmiana = (n) => (n === 1 ? 'pytanie' : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 'pytania' : 'pytań');
  pole.addEventListener('input', () => {
    const slowa = norm(pole.value).split(/\s+/).filter(Boolean);
    let ile = 0;
    pytania.forEach((p) => {
      const pasuje = slowa.every((s) => p.tekst.includes(s));
      p.el.hidden = !pasuje;
      if (pasuje) ile += 1;
    });
    tematy.forEach((t) => { t.hidden = !t.querySelector('.faq:not([hidden])'); });
    document.querySelectorAll('.tematy a').forEach((a) => {
      a.hidden = document.querySelector(a.getAttribute('href')).hidden;
    });
    licznik.textContent = slowa.length ? `Znaleziono ${ile} ${odmiana(ile)}` : poczatkowy;
    brak.hidden = ile > 0;
  });
});
