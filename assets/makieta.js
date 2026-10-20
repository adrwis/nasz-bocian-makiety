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
