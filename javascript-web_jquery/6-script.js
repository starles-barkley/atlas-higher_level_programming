#!/usr/bin/node

$(document).ready(() => {
  $('div#update_header').on('click', () => {
    $('header').text('New Header!!!');
  });
});