import { Navigate, Outlet } from 'react-router-dom';
export default function AdminRoute() {
  return localStorage.getItem('role') === 'admin' ? <Outlet /> : <Navigate to="/" />;
}
