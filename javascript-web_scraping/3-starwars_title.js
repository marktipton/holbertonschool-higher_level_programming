#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  } else {
    const filmData = JSON.parse(body);
    console.log(`${filmData.title}`);
  }
});
