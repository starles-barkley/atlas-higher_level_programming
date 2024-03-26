#!/usr/bin/node

function add(a, b) {
  return parseInt(a) + parseInt(b);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (isNaN(parseInt(arg1)) || isNaN(parseInt(arg2))) {
  console.log('Invalid input. Please provide two integers.');
} else {
  console.log(add(arg1, arg2));
}
