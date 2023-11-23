#!/usr/bin/node
const arg = process.argv[2];

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
if (parseInt(arg)) {
  console.log(factorial(arg));
} else console.log(1);
