// Menu na telefonie i nieaktywna wyszukiwarka makiety.
document.addEventListener('DOMContentLoaded', () => {
  const przycisk = document.querySelector('.naglowek__hamburger');
  const menu = document.getElementById('menu-glowne');
  przycisk.addEventListener('click', () => {
    const otwarte = menu.classList.toggle('otwarte');
    przycisk.setAttribute('aria-expanded', String(otwarte));
  });

  document.querySelector('.szukaj').addEventListener('submit', (e) => e.preventDefault());
});
