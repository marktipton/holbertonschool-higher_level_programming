#!/usr/bin/node
const arg1 = process.argv[2];
if (parseInt(arg1)) {
  console.log('My number:', Math.floor(arg1));
} else {
  console.log('Not a number');
}
