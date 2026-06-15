import api from './api';
export const login = (username, password) => api.post('/auth/login', new URLSearchParams({ username, password }));
export const register = (data) => api.post('/auth/register', data);
export const getMe = () => api.get('/auth/me');
