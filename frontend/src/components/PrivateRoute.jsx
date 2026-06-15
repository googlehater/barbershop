import { Navigate, Outlet } from 'react-router-dom';
export default function PrivateRoute() {
  return localStorage.getItem('access_token') ? <Outlet /> : <Navigate to="/login" />;
}
