// path: ./config/plugins.js

module.exports = ({ env }) => ({
  email: {
    config: {
      provider: "nodemailer",
      providerOptions: {
        host: "smtp.gmail.com",
        port: 587,
        auth: {
          user: env("SMTP_USER"),
          pass: env("SMTP_PASS"),
        },
      },
      settings: {
        defaultFrom: env("SMTP_USER"),
        defaultReplyTo: env("SMTP_USER"),
      },
    },
  },

  upload: {
    config: {
      imageOptimization: false,
      providerOptions: {
        sizeLimit: 25 * 1024 * 1024, // 25mb
      },
    },
  },
});