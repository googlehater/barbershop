import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import { login } from '../services/auth';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await login(username, password);
      const token = res.data.access_token;
      localStorage.setItem('access_token', token);
      
      // Получаем роль пользователя
      const me = await api.get('/auth/me', {
        headers: { Authorization: `Bearer ${token}` }
      });
      localStorage.setItem('role', me.data.role);
      
      navigate('/profile');
    } catch (err) {
      alert('Ошибка входа: ' + (err.response?.data?.detail || 'Неверный логин или пароль'));
    }
  };

  return (
    <div className="background3">
      <div className="booking-section">
        <div className="booking-card">
          <h2 className="booking-title">Вход</h2>
          <form className="booking-form" onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Логин</label>
              <input value={username} onChange={e => setUsername(e.target.value)} required />
            </div>
            <div className="form-group">
              <label>Пароль</label>
              <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
            </div>
            <button type="submit" className="submit-btn">ВОЙТИ</button>
          </form>
        </div>
      </div>
    </div>
  );
}