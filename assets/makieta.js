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
