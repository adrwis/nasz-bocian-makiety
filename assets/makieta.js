// Menu na telefonie i nieaktywna wyszukiwarka makiety.
document.addEventListener('DOMContentLoaded', () => {
  const przycisk = document.querySelector('.naglowek__hamburger');
  const menu = document.getElementById('menu-glowne');
  przycisk.addEventListener('click', () => {
    const otwarte = menu.classList.toggle('otwarte');
    przycisk.setAttribute('aria-expanded', String(otwarte));
  });

  const szukaj = document.getElementById('szukaj');
  if (!szukaj) return;
  szukaj.addEventListener('submit', (e) => e.preventDefault());

  // „Wyszukaj” w nagłówku na stronie głównej przewija do pola i ustawia w nim kursor.
  document.querySelector('.naglowek__szukaj').addEventListener('click', (e) => {
    e.preventDefault();
    szukaj.scrollIntoView({ behavior: 'smooth' });
    document.getElementById('szukaj-pole').focus({ preventScroll: true });
  });
  if (location.hash === '#szukaj') document.getElementById('szukaj-pole').focus();
});
