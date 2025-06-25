// dashboard.js

const sidebar = document.getElementById('sidebar');
const desktopBreakpoint = 768; // px

function toggleSidebar() {
  if (window.innerWidth >= desktopBreakpoint) {
    // Desktop: collapse/expand
    document.body.classList.toggle('collapsed');
  } else {
    // Mobile: slide in/out
    sidebar.classList.toggle('visible');
  }
}

// Dark‐mode toggle, persistent
function toggleDarkMode() {
  document.documentElement.classList.toggle('dark');
  localStorage.setItem(
    'theme',
    document.documentElement.classList.contains('dark') ? 'dark' : 'light'
  );
}

// On load, re-apply dark mode
window.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('theme') === 'dark') {
    document.documentElement.classList.add('dark');
  }
});
