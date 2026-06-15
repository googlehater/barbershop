import { useState, useEffect } from 'react';
import api from '../services/api';
export default function Appointment() {
  const [services, setServices] = useState([]);
  const [form, setForm] = useState({ service_id: '', master_id: '', appointment_date: '', client_wish: '' });
  useEffect(() => { api.get('/services/').then(res => setServices(res.data)).catch(() => {}); }, []);
  const handleSubmit = async (e) => {
    e.preventDefault();
    try { await api.post('/appointments/', form); alert('Запись создана!'); } catch (err) { alert('Ошибка'); }
  };
  return (
    <div className="background3">
      <div className="booking-section">
        <div className="booking-card">
          <h2 className="booking-title">ЗАПИСЬ</h2>
          <p className="booking-subtitle">Заполните форму — мы подтвердим запись</p>
          <form className="booking-form" onSubmit={handleSubmit}>
            <div className="form-row">
              <div className="form-group">
                <label>Услуга *</label>
                <select onChange={e => setForm({...form, service_id: e.target.value})} required>
                  <option value="">Выберите</option>
                  {services.map(s => <option key={s.id} value={s.id}>{s.services_name} -- {s.price}</option>)}
                </select>
              </div>
              <div className="form-group">
                <label>Дата *</label>
                <input type="date" onChange={e => setForm({...form, appointment_date: e.target.value})} required />
              </div>
            </div>
            <div className="form-group-full">
              <label>Пожелания</label>
              <textarea onChange={e => setForm({...form, client_wish: e.target.value})}></textarea>
            </div>
            <button type="submit" className="submit-btn">ЗАПИСАТЬСЯ</button>
          </form>
        </div>
      </div>
    </div>
  );
}