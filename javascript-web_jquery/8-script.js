#!/usr/bin/node
$('document').ready(() => {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    context: document.body
  }).done((data) => {
    for (film of data.results) {
      $('ul#list_movies').append(`<li>${film.title}</li>`);
    }
  });
});