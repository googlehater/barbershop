// import { Link, useNavigate } from 'react-router-dom';
// import { useState, useEffect } from 'react';

// export default function Navbar() {
//   const [isLoggedIn, setIsLoggedIn] = useState(false);
//   const [isAdmin, setIsAdmin] = useState(false);
//   const navigate = useNavigate();

//   // Проверяем токен и роль при каждом рендере и при изменениях в localStorage
//   useEffect(() => {
//     const token = localStorage.getItem('access_token');
//     const role = localStorage.getItem('role');
//     setIsLoggedIn(!!token);
//     setIsAdmin(role === 'admin');
//   }, [localStorage.getItem('access_token')]); // сработает не идеально, но для демки пойдёт

//   const handleLogout = () => {
//     localStorage.removeItem('access_token');
//     localStorage.removeItem('role');
//     setIsLoggedIn(false);
//     setIsAdmin(false);
//     navigate('/');
//   };

//   return (
//     <header className="header">
//       <div className="nav">
//         <div className="container-wide">
//           <div className="row space-beetween">
//             <div className="logo">Fade</div>
//             <div className="nav-menu">
//               <ul>
//                 <li><Link to="/">Главная</Link></li>
//                 <li><Link to="/about">Информация</Link></li>
//                 {!isLoggedIn && (
//                   <>
//                     <li><Link to="/login">Вход</Link></li>
//                     <li><Link to="/register">Регистрация</Link></li>
//                   </>
//                 )}
//                 {isLoggedIn && (
//                   <>
//                     <li><Link to="/appointment">Запись</Link></li>
//                     <li><Link to="/profile">Мои записи</Link></li>
//                     {isAdmin && <li><Link to="/admin">Админ-панель</Link></li>}
//                     <li><button onClick={handleLogout} style={{ background: 'none', border: 'none', color: 'inherit', cursor: 'pointer' }}>Выйти</button></li>
//                   </>
//                 )}
//               </ul>
//             </div>
//           </div>
//         </div>
//       </div>
//     </header>
//   );
// }


import { Link, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';

export default function Navbar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isAdmin, setIsAdmin] = useState(false);
  const navigate = useNavigate();

  const checkAuth = () => {
    const token = localStorage.getItem('access_token');
    const role = localStorage.getItem('role');
    setIsLoggedIn(!!token);
    setIsAdmin(role === 'admin');
  };

  useEffect(() => {
    checkAuth();
    // Подписываемся на событие storage (если токен изменится в другой вкладке)
    window.addEventListener('storage', checkAuth);
    return () => window.removeEventListener('storage', checkAuth);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('role');
    setIsLoggedIn(false);
    setIsAdmin(false);
    navigate('/');
  };

  return (
    <header className="header">
      <div className="nav">
        <div className="container-wide">
          <div className="row space-beetween">
            <div className="logo">Fade</div>
            <div className="nav-menu">
              <ul>
                <li><Link to="/">Главная</Link></li>
                <li><Link to="/about">Информация</Link></li>
                {!isLoggedIn && (
                  <>
                    <li><Link to="/login">Вход</Link></li>
                    <li><Link to="/register">Регистрация</Link></li>
                  </>
                )}
                {isLoggedIn && (
                  <>
                    <li><Link to="/appointment">Запись</Link></li>
                    <li><Link to="/profile">Мои записи</Link></li>
                    {isAdmin && <li><Link to="/admin">Админ-панель</Link></li>}
                    <li><button onClick={handleLogout} className="logout-btn">Выйти</button></li>
                  </>
                )}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
