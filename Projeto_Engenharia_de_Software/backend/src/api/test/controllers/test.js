module.exports = {
  async send(ctx) {
    try {
      await strapi.plugin("email").service("email").send({
        to: "kauanpablo01984@gmail.com",
        from: process.env.SMTP_USER,
        subject: "Teste de envio de email Strapi",
        text: "Se você está lendo isso, funcionou! 🎉",
        html: "<h1>Funcionou! 🎉</h1><p>Seu Strapi enviou este e-mail com sucesso.</p>",
      });

      ctx.body = { message: "Email enviado com sucesso!" };
    } catch (err) {
      console.error("Erro ao enviar email:", err);
      ctx.body = { error: "Falha ao enviar o email", details: err };
    }
  },

  async populate(ctx) {
    try {
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

      // Criar categorias
      const categoriasIds = [];
      for (const categoria of categorias) {
        const entry = await strapi.entityService.create('api::categoria.categoria', {
          data: categoria,
        });
        categoriasIds.push(entry.id);
      }

      // Criar instituições
      const instituicoesIds = [];
      for (const instituicao of instituicoes) {
        const entry = await strapi.entityService.create('api::instituicao.instituicao', {
          data: instituicao,
        });
        instituicoesIds.push(entry.id);
      }

      // Dados de solicitações
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

      // Criar solicitações
      for (const solicitacao of solicitacoes) {
        await strapi.entityService.create('api::solicitacao.solicitacao', {
          data: solicitacao,
        });
      }

      ctx.body = {
        message: 'População de dados concluída com sucesso!',
        summary: {
          categoriasCount: categoriasIds.length,
          instituicoesCount: instituicoesIds.length,
          solicitacoesCount: solicitacoes.length,
        },
      };
    } catch (err) {
      console.error('Erro ao popular dados:', err);
      ctx.body = { error: 'Falha ao popular dados', details: err.message };
    }
  },
};
