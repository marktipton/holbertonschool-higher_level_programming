#!/usr/bin/node
const args = process.argv;
// console.log(args.length);
if (!args[4]) {
  console.log(0);
} else {
  let greatest = null;
  let second = null;
  for (let i = 2; i < args.length; i++) {
    // parseInt(args[i]);
    // console.log(args[i]);
    if (args[i] > greatest) {
      second = parseInt(greatest);
      greatest = parseInt(args[i]);
      // console.log(second, greatest);
    }
    // } else if (args[i] > second) {
    //   second = args[i];
    // }
  }
  console.log(second);
  // console.log(greatest);
}
