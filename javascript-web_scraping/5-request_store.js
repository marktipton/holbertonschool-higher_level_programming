#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileStore = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  } else {
    fs.writeFile(fileStore, body, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});
