#!/usr/bin/node

$(document).ready(function() => {
  $('div#red_header').on('click', () => {
    $('header').addClass('red');
  });
});