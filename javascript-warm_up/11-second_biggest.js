#!/usr/bin/node
const args = process.argv;
// console.log(args.length);
let greatest = null;
let second = null;
if (!args[3]) {
  console.log(0);
} else {
  if (args[2] > args[3]) {
    greatest = parseInt(args[2]);
    second = parseInt(args[3]);
  } else {
    greatest = parseInt(args[3]);
    second = parseInt(args[2]);
  }
  for (let i = 4; i < args.length; i++) {
    // parseInt(args[i]);
    // console.log(args[i]);
    if (args[i] > greatest) {
      second = parseInt(greatest);
      greatest = parseInt(args[i]);
      // console.log(second, greatest);
    } else if (args[i] > second) {
      second = parseInt(args[i]);
    }
    // } else if (args[i] > second) {
    //   second = args[i];
    // }
  }
  console.log(second);
  // console.log(greatest);
}
