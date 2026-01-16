// Funções compartilhadas de autenticação

function getToken() {
  return localStorage.getItem('jwt');
}

function setToken(token) {
  localStorage.setItem('jwt', token);
}

function removeToken() {
  localStorage.removeItem('jwt');
}

async function validateToken(token) {
  try {
    const res = await fetch('http://localhost:1337/api/users/me', {
      headers: { Authorization: `Bearer ${token}` },
    });
    
    if (!res.ok) {
      removeToken();
      return null;
    }
    
    return await res.json();
  } catch (err) {
    console.error('Erro ao validar token:', err);
    removeToken();
    return null;
  }
}

async function setupMenu() {
  const mainMenu = document.getElementById('main-menu');
  const token = getToken();

  if (!token || !mainMenu) return;

  try {
    const user = await validateToken(token);
    
    if (!user) {
      // Token inválido, permita continuar como não-autenticado
      return;
    }

    const isInstituicao = !!user.instituicao;
    
    // Remove o link "Doar" se for instituição
    const doarLi = Array.from(mainMenu.children).find((li) =>
      li.textContent.trim().includes('Doar')
    );
    if (isInstituicao && doarLi) doarLi.remove();

    // Adiciona link "Seu Perfil"
    const perfilLi = document.createElement('li');
    perfilLi.innerHTML = `<a href="${isInstituicao ? 'perfil-instituicao.html' : 'perfil.html'}">Seu Perfil</a>`;
    mainMenu.appendChild(perfilLi);

    // Adiciona link "Sair"
    const sairLi = document.createElement('li');
    sairLi.innerHTML = `<a href="#" onclick="logout(); return false;">Sair</a>`;
    mainMenu.appendChild(sairLi);
  } catch (err) {
    console.error('Erro ao setup menu:', err);
  }
}

function logout() {
  removeToken();
  window.location.href = 'home.html';
}

// Chamar ao carregar a página
document.addEventListener('DOMContentLoaded', setupMenu);
