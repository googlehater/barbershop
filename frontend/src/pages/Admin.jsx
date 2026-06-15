import { useEffect, useState } from 'react';
import api from '../services/api';

export default function Admin() {
  const [stats, setStats] = useState({});
  const [appointments, setAppointments] = useState([]);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Статистика
    api.get('/admin/stats').then(res => setStats(res.data)).catch(() => {});
    // Все записи
    api.get('/appointments/').then(res => setAppointments(res.data)).catch(() => {});
    // Все пользователи
    // api.get('/admin/users').catch(() => {});
  }, []);

  return (
    <div className="background3">
      <div className="booking-section">
        <div className="booking-card">
          <h2 className="booking-title">Админ-панель</h2>
          
          <div style={{ marginBottom: '30px' }}>
            <h3>Статистика</h3>
            <p>👥 Пользователей: {stats.total_users || 0}</p>
            <p>📅 Записей: {stats.total_appointments || 0}</p>
          </div>

          <div>
            <h3>Все записи</h3>
            {appointments.length === 0 ? (
              <p>Нет записей</p>
            ) : (
              <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                <thead>
                  <tr>
                    <th style={{ textAlign: 'left', padding: '8px' }}>ID</th>
                    <th style={{ textAlign: 'left', padding: '8px' }}>Пользователь</th>
                    <th style={{ textAlign: 'left', padding: '8px' }}>Услуга</th>
                    <th style={{ textAlign: 'left', padding: '8px' }}>Мастер</th>
                    <th style={{ textAlign: 'left', padding: '8px' }}>Дата</th>
                    <th style={{ textAlign: 'left', padding: '8px' }}>Статус</th>
                  </tr>
                </thead>
                <tbody>
                  {appointments.map(apt => (
                    <tr key={apt.id}>
                      <td style={{ padding: '8px' }}>{apt.id}</td>
                      <td style={{ padding: '8px' }}>{apt.user_id}</td>
                      <td style={{ padding: '8px' }}>{apt.service_id}</td>
                      <td style={{ padding: '8px' }}>{apt.master_id}</td>
                      <td style={{ padding: '8px' }}>{new Date(apt.appointment_date).toLocaleString()}</td>
                      <td style={{ padding: '8px' }}>{apt.status}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}