'use strict';

module.exports = {
  routes: [
    {
      method: 'GET',
      path: '/test/test-email',
      handler: 'test.send',
      config: {
        auth: false,
      },
    },
    {
      method: 'GET',
      path: '/test/populate',
      handler: 'test.populate',
      config: {
        auth: false,
      },
    },
  ],
};