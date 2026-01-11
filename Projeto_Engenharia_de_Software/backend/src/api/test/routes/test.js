module.exports = {
  routes: [
    {
      method: 'GET',
      path: '/test-email',
      handler: 'test.send',
      config: {
        auth: false, 
      },
    },
  ],
};