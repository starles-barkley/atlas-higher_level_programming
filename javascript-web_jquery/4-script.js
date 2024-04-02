#!/user/bin/node

const { userInfo } = require("os");

$(document).ready(() => {
  $('div#toggle_header').on('click', () => {
    if ($('header').hasClass('green')) {
      $('header').addClass('red');
      $('header').removeClass('green');
    } else if ($('header').hasClass('red')) {
      $('header').addClass('green');
      $('header').removeClass('red');
    }
  });
});