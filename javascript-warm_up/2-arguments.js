#!/usr/bin/node
const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument');
} else {
  console.log('Arguments');
}
