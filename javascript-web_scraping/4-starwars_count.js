#!/usr/bin/node
const request = require('request');
const wedgeId = '18';
const apiUrl = process.argv[2];

request(apiUrl, (error, request, body) => {
  if (error) {
    console.error('Error', error.message);
    process.exit(1);
  } else {
    const filmData = JSON.parse(body);
    let count = 0;
    for (const film in filmData.results) {
      const characterList = filmData.results[film].characters;
      for (const character in characterList) {
        if (characterList[character].includes(wedgeId)) count++;
      }
    }
    console.log(count);
  }
});
