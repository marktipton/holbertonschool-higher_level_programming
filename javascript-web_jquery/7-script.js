#!/usr/bin/node

apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.ajax({
  url: apiUrl,
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    $('#character').text(`${data.name}`);
  },
  error: function(xhr, status, error) {
    console.error('problem fetching character data', error);
  }
});
