// Script para popular dados no Strapi
const axios = require('axios');

const API_URL = 'http://localhost:1337/api';

// Credenciais (use o email/senha que você colocou no painel do Strapi)
const ADMIN_EMAIL = 'lafuentepaulino@alu.ufc.br';
const ADMIN_PASSWORD = 'Jabuticaba12';

let JWT_TOKEN = ''; // Será preenchido após login

// Dados de exemplo para categorias
const categorias = [
  { nome: 'Roupas' },
  { nome: 'Alimentos' },
  { nome: 'Eletrônicos' },
  { nome: 'Livros' },
  { nome: 'Móveis' },
];

// Dados de exemplo para instituições
const instituicoes = [
  {
    endereco: 'Rua das Flores, 123 - Quixadá, CE',
    descricao: 'ONG dedicada a ajudar crianças em situação de rua com alimentação e educação.',
    CNPJ: '12.345.678/0001-90',
  },
  {
    endereco: 'Avenida Principal, 456 - Quixadá, CE',
    descricao: 'Instituição religiosa que auxilia idosos e necessitados com refeições diárias.',
    CNPJ: '98.765.432/0001-10',
  },
  {
    endereco: 'Praça da República, 789 - Quixadá, CE',
    descricao: 'Centro comunitário que oferece cursos profissionalizantes para jovens carentes.',
    CNPJ: '11.222.333/0001-44',
  },
];

// Função para aguardar
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// Função para fazer login e obter JWT
async function login() {
  try {
    console.log('🔐 Fazendo login...');
    const response = await axios.post(`${API_URL}/auth/local`, {
      identifier: ADMIN_EMAIL,
      password: ADMIN_PASSWORD,
    });
    JWT_TOKEN = response.data.jwt;
    console.log('✅ Login realizado com sucesso!\n');
    return true;
  } catch (error) {
    console.error('❌ Erro ao fazer login:');
    console.error('   Email:', ADMIN_EMAIL);
    console.error('   Verifique se o email e senha estão corretos');
    console.error('   (Aqueles que você colocou ao se registrar no painel Strapi)\n');
    return false;
  }
}

// Função para aguardar

// Função para criar dados
async function populateData() {
  try {
    // Fazer login primeiro
    const loggedIn = await login();
    if (!loggedIn) {
      console.error('❌ Não foi possível fazer login. Abortando...');
      process.exit(1);
    }

    console.log('🚀 Iniciando população de dados...\n');

    // Headers com autenticação
    const headers = {
      Authorization: `Bearer ${JWT_TOKEN}`,
    };

    // Criar categorias
    console.log('📁 Criando categorias...');
    const categoriasIds = [];
    for (const categoria of categorias) {
      try {
        const response = await axios.post(`${API_URL}/categorias`, {
          data: categoria,
        }, { headers });
        categoriasIds.push(response.data.data.id);
        console.log(`✅ Categoria criada: ${categoria.nome}`);
      } catch (error) {
        console.error(`❌ Erro ao criar categoria ${categoria.nome}:`, error.response?.data || error.message);
      }
      await sleep(500);
    }

    // Criar instituições
    console.log('\n🏛️ Criando instituições...');
    const instituicoesIds = [];
    for (const instituicao of instituicoes) {
      try {
        const response = await axios.post(`${API_URL}/instituicaos`, {
          data: instituicao,
        }, { headers });
        instituicoesIds.push(response.data.data.id);
        console.log(`✅ Instituição criada: ${instituicao.endereco}`);
      } catch (error) {
        console.error(`❌ Erro ao criar instituição:`, error.response?.data || error.message);
      }
      await sleep(500);
    }

    // Criar solicitações (doações)
    console.log('\n📦 Criando solicitações de doação...');
    const solicitacoes = [
      {
        titulo: 'Roupas para crianças',
        descricao: 'Procuramos roupas infantis em bom estado para crianças carentes.',
        data_disponivel: '2025-02-15',
        status: 'pendente',
        instituicao: instituicoesIds[0],
        categoria: categoriasIds[0],
      },
      {
        titulo: 'Alimentos não perecíveis',
        descricao: 'Arrecadando alimentos como arroz, feijão e macarrão para famílias necessitadas.',
        data_disponivel: '2025-02-20',
        status: 'pendente',
        instituicao: instituicoesIds[1],
        categoria: categoriasIds[1],
      },
      {
        titulo: 'Livros para biblioteca comunitária',
        descricao: 'Estamos montando uma biblioteca comunitária e precisamos de livros de todos os gêneros.',
        data_disponivel: '2025-03-01',
        status: 'aceito',
        instituicao: instituicoesIds[2],
        categoria: categoriasIds[3],
      },
      {
        titulo: 'Equipamentos eletrônicos usados',
        descricao: 'Notebooks, tablets ou computadores para curso profissionalizante.',
        data_disponivel: '2025-03-10',
        status: 'pendente',
        instituicao: instituicoesIds[2],
        categoria: categoriasIds[2],
      },
      {
        titulo: 'Móveis para abrigo',
        descricao: 'Camas, mesas e cadeiras para melhorar acomodação de pessoas em situação de rua.',
        data_disponivel: '2025-03-15',
        status: 'recusado',
        instituicao: instituicoesIds[0],
        categoria: categoriasIds[4],
      },
    ];

    for (const solicitacao of solicitacoes) {
      try {
        const response = await axios.post(`${API_URL}/solicitacaos`, {
          data: solicitacao,
        }, { headers });
        console.log(`✅ Solicitação criada: ${solicitacao.titulo}`);
      } catch (error) {
        console.error(`❌ Erro ao criar solicitação ${solicitacao.titulo}:`, error.response?.data || error.message);
      }
      await sleep(500);
    }

    console.log('\n✨ População de dados concluída com sucesso!');
    console.log('\n📊 Resumo:');
    console.log(`   - ${categoriasIds.length} categorias criadas`);
    console.log(`   - ${instituicoesIds.length} instituições criadas`);
    console.log(`   - ${solicitacoes.length} solicitações criadas`);
    console.log('\n💡 Você pode acessar os dados em http://localhost:8080/');

  } catch (error) {
    console.error('❌ Erro geral:', error.message);
  }
}

// Executar script
populateData();
