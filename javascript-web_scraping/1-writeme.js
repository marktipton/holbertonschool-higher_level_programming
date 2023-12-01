#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const fileName = args[2];
const writeString = args[3];

fs.writeFile(fileName, writeString, 'utf-8', (err) => {
  if (err) throw err;
});
