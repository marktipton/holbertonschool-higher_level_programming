#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
