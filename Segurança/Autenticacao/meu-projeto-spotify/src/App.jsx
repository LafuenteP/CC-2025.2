import { Routes, Route } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'

// 1. Importe as páginas que VAMOS criar
// (Vai dar erro por enquanto, é normal)
import HomePage from './pages/HomePage'
import CallbackPage from './pages/CallbackPage'
import DashboardPage from './pages/DashboardPage'

function App() {
  return (
    // 2. O AuthProvider "abraça" todas as nossas páginas
    <AuthProvider>
      <Routes>
        {/* Rota 1: A página pública de login */}
        <Route path="/" element={<HomePage />} />
        
        {/* Rota 2: A página de callback (para onde o Spotify devolve) */}
        <Route path="/callback" element={<CallbackPage />} />
        
        {/* Rota 3: A dashboard privada (onde a mágica acontece) */}
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </AuthProvider>
  )
}

export default App