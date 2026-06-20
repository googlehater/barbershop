import { useEffect, useRef, useState } from 'react';

export default function Home() {
  const [isDark, setIsDark] = useState(() => {
    return localStorage.getItem('theme') === 'dark';
  });
  const toggleBtnRef = useRef(null);

  useEffect(() => {
    const body = document.body;
    if (isDark) {
      body.classList.add('dark-theme');
      if (toggleBtnRef.current) toggleBtnRef.current.textContent = '☀️ Светлая тема';
    } else {
      body.classList.remove('dark-theme');
      if (toggleBtnRef.current) toggleBtnRef.current.textContent = '🌙 Тёмная тема';
    }
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  }, [isDark]);

  const toggleTheme = () => {
    setIsDark(!isDark);
  };

  return (
    <button className="theme-toggle" ref={toggleBtnRef} onClick={toggleTheme}>
      🌙 Тёмная тема
    </button>
  );
}
