#!/usr/bin/node

$('document').ready(() => {
  $.ajax({
    method: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    context: document.body
  }).done((data) => {
    $('div#hello').text(data.hello);
  })
});