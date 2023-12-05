#!/usr/bin/node
$('#toggle_header').on('click', function () {
  // toggleClass does removeClass and addClass with red and green
  // depending on which is currently being used by the header
  $('header').toggleClass('red green');
});
