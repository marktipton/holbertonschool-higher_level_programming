#!/usr/bin/node
$('#add_item').on('click', function () {
  // specify type of element and text inside element
  const newElement = $('<li>').text('Item');
  $('ul.my_list').append(newElement);
});
