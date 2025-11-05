import { createContext, useState, useContext } from 'react';

// 1. Cria o Contexto
const AuthContext = createContext(null);

// 2. Cria o "Provedor" (o componente que vai guardar os dados)
export function AuthProvider({ children }) {
  const [token, setToken] = useState(null); // Aqui fica o token, em memória!
  const [scopes, setScopes] = useState(null); // Aqui ficam as permissões

  // Função para "logar" o usuário no nosso app
  const login = (accessToken, grantedScopes) => {
    setToken(accessToken);
    setScopes(grantedScopes);
  };

  // Função para "deslogar"
  const logout = () => {
    setToken(null);
    setScopes(null);
  };

  // Valor que será compartilhado com todos os componentes "filhos"
  const value = {
    token,
    scopes,
    login,
    logout,
    isAuthenticated: !!token, // Um booleano simples para saber se estamos logados
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

// 3. Cria um "Hook" (atalho) para facilitar o uso em outros componentes
export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth deve ser usado dentro de um AuthProvider');
  }
  return context;
}