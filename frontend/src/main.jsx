import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/global.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(  // точка входа React в DOM - оставляем
  <StrictMode>
    <App />
  </StrictMode>,
)
