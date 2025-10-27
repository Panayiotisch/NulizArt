const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
const yearEl = document.getElementById('year');

yearEl.textContent = new Date().getFullYear();

if (navToggle && navLinks) {
  const toggleNav = () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  };

  navToggle.addEventListener('click', toggleNav);
  navLinks.addEventListener('click', event => {
    if (event.target.tagName === 'A' && navLinks.classList.contains('open')) {
      toggleNav();
    }
  });
}

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

if (prefersReducedMotion.matches) {
  document.documentElement.style.setProperty('--transition-speed', '0s');
  document.querySelectorAll('.orb').forEach(orb => {
    orb.style.animation = 'none';
  });
}
