import { useEffect, useState } from 'react';
import api from '../services/api';
export default function Profile() {
  const [apps, setApps] = useState([]);
  useEffect(() => { api.get('/appointments/my').then(res => setApps(res.data)).catch(() => {}); }, []);
  return (
    <div className="background3">
      <div className="booking-card"><h2>Мои записи</h2>
        {apps.map(a => <div key={a.id}>{a.appointment_date} - {a.service_id}</div>)}
      </div>
    </div>
  );
}
