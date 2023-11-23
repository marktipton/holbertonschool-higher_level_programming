#!/usr/bin/node
const squareSize = process.argv[2];
if (!parseInt(squareSize)) console.log('Missing size');

for (let i = 0; i < squareSize; i++) {
  console.log('X'.repeat(squareSize));
}
