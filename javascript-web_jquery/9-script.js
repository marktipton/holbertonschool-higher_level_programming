#!/usr/bin/node

const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.ajax({
  url: apiUrl,
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    $('#hello').text(data.hello);
  },
});
