#!/usr/bin/node
const request = require('request');
const wedgeUrl = 'https://swapi-api.hbtn.io/api/people/18/';
const apiUrl = process.argv[2];

request(apiUrl, (error, request, body) => {
  if (error) {
    console.error('Error', error.message);
    process.exit(1);
  } else {
    const filmData = JSON.parse(body);
    let count = 0;
    console.log(filmData);
    // for (const url of filmData.results.characters) {
    //   if (url === wedgeUrl) {
    //     count++;
    //   }
    // }
    // console.log(count);
  }
});
