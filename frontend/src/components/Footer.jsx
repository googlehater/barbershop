export default function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-col">
            <div className="footer-logo">Fade</div>
            <p className="footer-description">Создает образ уютного, но по-мужски жесткого места.</p>
          </div>
          <div className="footer-col">
            <h3 className="footer-title">Навигация</h3>
            <ul className="footer-links">
              <li><a href="/">Главная</a></li>
              <li><a href="/about">Информация</a></li>
              <li><a href="/appointment">Запись</a></li>
            </ul>
          </div>
          <div className="footer-col">
            <h3 className="footer-title">Контакты</h3>
            <ul className="footer-contacts">
              <li>hair@gmail.ru</li>
              <li>+7 (999) 999-99-99</li>
              <li>ул. Стриженная, д. 14</li>
            </ul>
          </div>
          <div className="footer-col">
            <h3 className="footer-title">Мы в соцсетях</h3>
            <div className="social-links">
              <a href="#" className="social-link">Telegram</a>
              <a href="#" className="social-link">VK</a>
              <a href="#" className="social-link">YouTube</a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2026 Fade. Все права защищены.</p>
        </div>
      </div>
    </footer>
  );
}
