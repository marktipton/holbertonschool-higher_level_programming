#!/usr/bin/node

const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.ajax({
  url: apiUrl,
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    const filmData = data.results;
    const movieList = $('#list_movies');
    $.each(filmData, function(index, film) {
      movieList.append('<li>' + film.title + '</li>');
    });
  }
});
