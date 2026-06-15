import { useEffect } from 'react';
export default function Home() {
  useEffect(() => {
    const toggleBtn = document.getElementById('themeToggle');
    const body = document.body;
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      body.classList.add('dark-theme');
      if (toggleBtn) toggleBtn.textContent = '☀️ Светлая тема';
    }
    const handler = () => {
      const isDark = body.classList.toggle('dark-theme');
      if (toggleBtn) toggleBtn.textContent = isDark ? '☀️ Светлая тема' : '🌙 Тёмная тема';
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    };
    if (toggleBtn) toggleBtn.addEventListener('click', handler);
    return () => { if (toggleBtn) toggleBtn.removeEventListener('click', handler); };
  }, []);
  return (
    <div className="background1">
      <button className="theme-toggle" id="themeToggle">🌙 Тёмная тема</button>
      <div className="hero-title">
        <h1 className="high-text">Барбершоп - Fade</h1>
        <h2 className="smal-text">Здесь варят кофе и рубят углы.</h2>
      </div>
      <section className="gallery-section">
        <div className="gallery-container">
          <div className="gallery-grid">
            <div className="gallery-item"><img src="/img/haircut_1.jpg" alt="Стрижка 1" className="gallery-img" /></div>
            <div className="gallery-item"><img src="/img/haircut_2.jpg" alt="Стрижка 2" className="gallery-img" /></div>
            <div className="gallery-item"><img src="/img/haircut_3.jpg" alt="Стрижка 3" className="gallery-img" /></div>
          </div>
        </div>
      </section>
    </div>
  );
}
