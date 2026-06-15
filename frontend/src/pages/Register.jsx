import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { register } from '../services/auth';
export default function Register() {
  const [form, setForm] = useState({ username: '', email: '', password: '', role: 'user' });
  const navigate = useNavigate();
  const handleSubmit = async (e) => {
    e.preventDefault();
    try { await register(form); alert('Регистрация успешна'); navigate('/login'); } catch { alert('Ошибка'); }
  };
  return (
    <div className="background3">
      <div className="booking-section">
        <div className="booking-card">
          <h2 className="booking-title">Регистрация</h2>
          <form className="booking-form" onSubmit={handleSubmit}>
            <div className="form-group"><label>Логин</label><input onChange={e=>setForm({...form, username: e.target.value})} required /></div>
            <div className="form-group"><label>Email</label><input type="email" onChange={e=>setForm({...form, email: e.target.value})} required /></div>
            <div className="form-group"><label>Пароль</label><input type="password" onChange={e=>setForm({...form, password: e.target.value})} required /></div>
            <button type="submit" className="submit-btn">Зарегистрироваться</button>
          </form>
        </div>
      </div>
    </div>
  );
}
