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
};
