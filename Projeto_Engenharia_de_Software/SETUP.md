# 🚀 Guia de Setup - DoaAí Projeto

Bem-vindo ao **DoaAí**! Este guia ajudará você a rodar o projeto em sua máquina.

---

## ⚙️ Pré-requisitos

### Node.js v20 LTS
**⚠️ IMPORTANTE: Use a versão 20.x do Node.js**

1. Acesse: https://nodejs.org/
2. Clique em **"20.x.x LTS"** (recomendado - não use a versão 24+)
3. Baixe e instale normalmente
4. Após instalar, **reinicie o PowerShell/Terminal completamente**
5. Verifique a instalação:
   ```powershell
   node --version
   npm --version
   ```
   Deve retornar algo como `v20.x.x`

---

## 📦 Instalação das Dependências

### Backend

1. Abra um **PowerShell/Terminal** na pasta raiz do projeto

2. Navegue até a pasta backend:
   ```powershell
   cd backend
   ```

3. Instale as dependências:
   ```powershell
   npm install
   ```
   ⏳ Isso pode levar 5-10 minutos na primeira vez.

---

## ▶️ Iniciando o Projeto

### 1️⃣ Backend (Strapi)

Em um **PowerShell/Terminal**:

```powershell
cd backend
npm run develop
```

Aguarde até ver a mensagem de sucesso. O painel do Strapi abrirá automaticamente:
- **URL**: `http://localhost:1337/admin`

### 2️⃣ Frontend

Abra um **NOVO PowerShell/Terminal** (deixe o backend rodando):

```powershell
cd frontend
npm install -g http-server
http-server -p 8080
```

A aplicação estará disponível em:
- **URL**: `http://localhost:8080`

### 3️⃣ Acessar a Página Inicial

Abra no navegador:
```
http://localhost:8080/home.html
```

---

## 📝 Populando os Dados (Categorias, Instituições, Solicitações)

Se você precisa adicionar dados ao projeto, siga os passos abaixo.

### Opção 1: Via Painel Strapi (Interface Visual)

1. Acesse: `http://localhost:1337/admin`
2. Faça login com suas credenciais
3. No menu esquerdo, clique em **"Conteúdo"**
4. Escolha a seção desejada:
   - **Categoria**: Criar tipos de doação
   - **Instituição**: Criar ONGs/Igrejas
   - **Solicitação**: Criar agendamentos de doações

### Opção 2: Via Script (Automático)

Se preferir popular dados automaticamente via script:

1. Abra um **TERCEIRO PowerShell/Terminal**

2. Navegue até o backend:
   ```powershell
   cd backend
   ```

3. Execute o script de população:
   ```powershell
   node populate-data.js
   ```

**Nota**: O script espera que o **Backend esteja rodando** e usa suas credenciais de login.

---

## 📊 Dados de Exemplo (Manual)

Se preferir adicionar dados manualmente, aqui estão alguns exemplos:

### Categorias
- Roupas
- Alimentos
- Eletrônicos
- Livros
- Móveis

### Instituições
```
Endereço: Rua das Flores, 123 - Quixadá, CE
Descrição: ONG dedicada a ajudar crianças em situação de rua com alimentação e educação.
CNPJ: 12.345.678/0001-90
```

```
Endereço: Avenida Principal, 456 - Quixadá, CE
Descrição: Instituição religiosa que auxilia idosos e necessitados com refeições diárias.
CNPJ: 98.765.432/0001-10
```

```
Endereço: Praça da República, 789 - Quixadá, CE
Descrição: Centro comunitário que oferece cursos profissionalizantes para jovens carentes.
CNPJ: 11.222.333/0001-44
```

### Solicitações (Doações)
```
Título: Roupas para crianças
Descrição: Procuramos roupas infantis em bom estado para crianças carentes.
Data Disponível: 2025-02-15
Status: pendente
Categoria: Roupas
```

---

## 🛑 Parando o Projeto

Para parar os servidores, pressione **Ctrl + C** em cada terminal (backend e frontend).

---

## ❓ Dúvidas Frequentes

**P: Qual versão do Node.js devo usar?**
R: **v20.x LTS** - não use v24 ou superiores.

**P: Posso rodar sem popular dados?**
R: Sim! O projeto funciona sem dados, mas as páginas estarão vazias.

**P: Posso acessar de outro computador?**
R: Não por padrão. O projeto é local. Para deploy online, consulte a documentação do Strapi.

**P: Como criar novas páginas no frontend?**
R: Adicione um novo arquivo `.html` na pasta `frontend/` e atualize os links de navegação.

---

## 📚 Estrutura do Projeto

```
finalProjectWeb/
├── backend/                    # Servidor Strapi
│   ├── src/api/                # APIs (categoria, instituição, solicitação)
│   ├── config/                 # Configurações
│   ├── package.json
│   ├── populate-data.js        # Script para popular dados
│   └── .env                    # Variáveis de ambiente
│
├── frontend/                   # Interface web (HTML/CSS/JS)
│   ├── home.html
│   ├── login.html
│   ├── cadastro.html
│   ├── style.css
│   └── img/
│
└── README.md
```

---

## ✅ Checklist de Setup

- [ ] Instalei Node.js v20
- [ ] Instalei dependências do backend (`npm install`)
- [ ] Backend está rodando (`npm run develop`)
- [ ] Frontend está rodando (`http-server -p 8080`)
- [ ] Acessei `http://localhost:8080/home.html`
- [ ] Populei dados (manual ou script)

---

**Desenvolvido como projeto da disciplina de Desenvolvimento Web de Software - UFC Quixadá** 🎓

